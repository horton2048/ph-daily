#!/usr/bin/env python3
"""render_xhs.py — 小红书信息图统一渲染器

读取 xhs/YYYY-MM-DD/data.json（当天各产品的六锚点文案），套
product-sense skill 的 references/xhs-template.html 做占位符替换，
Chrome headless 渲染成 PNG。

设计意图：CSS/HTML 骨架只活在模板文件里，不再每天被重新生成一遍；
Claude 每天的产出收窄成 data.json（六锚点文案），渲染是纯确定性的
字符串替换 + 截图，不需要 LLM 参与。

HTML 落在 xhs/YYYY-MM-DD/temp_html/，渲染后不删——留底用于事后 diff/
排查（8-06 事故教训，见 memory: xhs-infographic-html-preservation）。

logo 下载后规范化，暂存在 xhs/YYYY-MM-DD/.tmp/logos/；下载或解析失败
（SVG、404、超时等）自动退化成纯色块+首字母，不让单个 logo 问题挡住
整批渲染。无 logo_url，或缩略图明显不是标识（过宽、照片、整幅截图/海报）时，
先按官网查品牌标识（apple-touch-icon、最大 rel=icon、页面上的 logo 图），
查不到再退回首字母。

用法:
  python3 scripts/render_xhs.py xhs/2026-08-11/data.json
  python3 scripts/render_xhs.py xhs/2026-08-11/data.json --only betterclaw,bullet   # 只重渲指定几个

 data.json 结构见 references/xhs-data.schema.json 或 xhs-template.html 头部注释。
"""
from __future__ import annotations

import argparse
import base64
import html
import json
import re
import subprocess
import sys
from html.parser import HTMLParser
from io import BytesIO
from pathlib import Path
from urllib.parse import unquote_to_bytes, urljoin, urlparse

from PIL import Image
import requests

def _resolve_chrome() -> str:
    import os
    env = os.environ.get("CHROME_PATH")
    if env:
        return env
    mac = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    for c in (mac, "/usr/bin/google-chrome", "/usr/bin/chromium-browser", "/usr/bin/chromium"):
        if Path(c).exists():
            return c
    return mac  # keep Mac default for error message clarity

CHROME = _resolve_chrome()
PROJECT_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = PROJECT_ROOT / ".claude/skills/product-sense/references"
# style key → 模板文件名 + 输出文件名后缀。默认 cream-glass 无后缀；mono/calendar 加后缀实现并存。
TEMPLATE_REGISTRY = {
    "": ("xhs-template.html", ""),
    "mono": ("xhs-template-mono.html", "-mono"),
    "calendar": ("xhs-template-calendar.html", "-cal"),
}
LOGO_CANVAS_SIZE = 256


_UA = {"User-Agent": "Mozilla/5.0 (compatible; ph-daily-render/1.0)"}
_URL_RE = re.compile(r"https?://[^\s<>\"')\]]+")
_WIDE_RATIO = 1.7
_SKIP_SITE_HOSTS = {"producthunt.com", "www.producthunt.com", "npmjs.com", "www.npmjs.com"}


def _http_get(url: str, timeout: int = 10) -> requests.Response | None:
    try:
        resp = requests.get(url, timeout=timeout, headers=_UA, allow_redirects=True)
        resp.raise_for_status()
        return resp
    except Exception:
        return None


def _clean_url(url: str) -> str:
    return url.strip().rstrip(").,;；、>")


def _host(url: str) -> str:
    return urlparse(url).netloc.lower().split(":")[0]


def _non_mark_reason(img: Image.Image) -> str | None:
    """缩略图明显不是标识时返回原因。方形纯色/透明角标图标返回 None，避免误伤真 logo。"""
    im = img.convert("RGBA")
    w, h = im.size
    if w < 8 or h < 8:
        return "too small"
    if max(w, h) / min(w, h) >= _WIDE_RATIO:
        return f"very wide {w}x{h}"
    small = im.resize((64, 64), Image.BOX)
    px = small.load()

    def sample(x: int, y: int):
        r, g, b, a = px[x, y]
        if a < 128:
            return None
        return (r, g, b)

    def dist(a, b) -> float:
        return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

    corners = [sample(1, 1), sample(62, 1), sample(1, 62), sample(62, 62)]
    # 圆角 app icon 四角透明，是标识不是截图。
    if any(c is None for c in corners):
        return None
    spread = max(dist(corners[i], corners[j]) for i in range(4) for j in range(i + 1, 4))
    bg = tuple(sum(c[i] for c in corners) / 4 for i in range(3))
    n = near = 0
    buckets: dict[tuple, int] = {}
    edge_sum = edge_n = 0
    lums: list[float] = []
    for y in range(64):
        prev = None
        for x in range(64):
            c = sample(x, y)
            if c is None:
                prev = None
                continue
            n += 1
            lums.append((c[0] + c[1] + c[2]) / 3)
            key = (c[0] // 32, c[1] // 32, c[2] // 32)
            buckets[key] = buckets.get(key, 0) + 1
            if dist(c, bg) < 28:
                near += 1
            if prev is not None:
                edge_sum += dist(c, prev)
                edge_n += 1
            prev = c
    if n < 64:
        return "empty"
    top = max(buckets.values()) / n
    near_bg = near / n
    mean_edge = edge_sum / edge_n if edge_n else 0
    mean_l = sum(lums) / len(lums)
    lum_std = (sum((v - mean_l) ** 2 for v in lums) / len(lums)) ** 0.5
    # 四角不是同一块底、底色也盖不住画面：整幅界面截图。
    if spread >= 70 and near_bg < 0.12:
        return "screenshot"
    # 柔和棚拍/产品照片：边缘少、有一块背景，但不是大色块图标。
    if mean_edge < 16 and near_bg > 0.45 and lum_std < 40 and top < 0.75:
        return "mostly a photo"
    # 大段文字海报：平地底上到处是硬边，不是单独的标。
    if mean_edge >= 45 and lum_std >= 50 and top >= 0.55:
        return "poster"
    return None


def _is_svg(data: bytes, ctype: str, url: str) -> bool:
    if "svg" in (ctype or "").lower() or url.lower().split("?", 1)[0].endswith(".svg"):
        return True
    head = data[:300].lstrip().lower()
    return head.startswith(b"<svg") or (head.startswith(b"<?xml") and b"<svg" in data[:800].lower())


def _rasterize_svg(svg: bytes, work_dir: Path) -> Image.Image | None:
    """PIL 不能读 SVG。用已经负责截图的 Chrome 把图标栅格化成 256 PNG。"""
    work_dir.mkdir(parents=True, exist_ok=True)
    html_path = work_dir / "_svg_preview.html"
    png_path = work_dir / "_svg_preview.png"
    body = svg.decode("utf-8", "replace")
    html_path.write_text(
        "<!doctype html><meta charset=utf-8><style>"
        "html,body{margin:0;background:transparent;width:256px;height:256px}"
        "svg{width:256px;height:256px;display:block}</style>" + body,
        encoding="utf-8",
    )
    cmd = [
        CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--default-background-color=00000000", "--window-size=256,256",
        f"--screenshot={png_path.resolve()}", html_path.resolve().as_uri(),
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True, timeout=30)
        img = Image.open(png_path).convert("RGBA")
        img.load()
        return img
    except Exception:
        return None
    finally:
        html_path.unlink(missing_ok=True)
        png_path.unlink(missing_ok=True)


def _bytes_to_image(data: bytes, ctype: str, url: str, work_dir: Path) -> Image.Image | None:
    try:
        if _is_svg(data, ctype, url):
            return _rasterize_svg(data, work_dir)
        img = Image.open(BytesIO(data))
        img.load()
        return img
    except Exception:
        return None


def _decode_data_uri(url: str) -> tuple[bytes, str] | None:
    header, _, payload = url.partition(",")
    if not payload:
        return None
    try:
        raw = base64.b64decode(payload) if ";base64" in header else unquote_to_bytes(payload)
    except Exception:
        return None
    ctype = header[5:].split(";", 1)[0] if header.startswith("data:") else ""
    return raw, ctype


def _download_image(url: str, work_dir: Path) -> Image.Image | None:
    if url.startswith("data:"):
        decoded = _decode_data_uri(url)
        if not decoded:
            return None
        raw, ctype = decoded
        if len(raw) > 2_000_000:
            return None
        return _bytes_to_image(raw, ctype, url, work_dir)
    resp = _http_get(url)
    if resp is None or len(resp.content) > 8_000_000:
        return None
    ctype = resp.headers.get("content-type", "")
    if "text/html" in ctype and "image" not in ctype:
        return None
    return _bytes_to_image(resp.content, ctype, resp.url or url, work_dir)


def _imgix_hires(url: str) -> str:
    sep = "&" if "?" in url else "?"
    return f"{url}{sep}w=512&h=512"


def _load_mark(url: str, work_dir: Path) -> tuple[Image.Image | None, str | None]:
    """返回 (可用标识, None) 或 (None, 原因)。过宽/照片/截图/海报不算标识。"""
    img = _download_image(url, work_dir)
    if img is None:
        return None, "download failed"
    reason = _non_mark_reason(img)
    if reason:
        return None, reason
    if "imgix.net" in url and max(img.size) < 480:
        upgraded = _download_image(_imgix_hires(url), work_dir)
        if upgraded is not None and _non_mark_reason(upgraded) is None:
            img = upgraded
    return img, None


def _write_logo(img: Image.Image, dest: Path) -> None:
    img = img.convert("RGBA")
    side = max(img.size)
    canvas = Image.new("RGBA", (side, side), (255, 255, 255, 0))
    canvas.paste(img, ((side - img.width) // 2, (side - img.height) // 2), img)
    canvas = canvas.resize((LOGO_CANVAS_SIZE, LOGO_CANVAS_SIZE), Image.LANCZOS)
    dest.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(dest)


class _IconParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.icons: list[tuple[str, str, str]] = []
        self.imgs: list[dict] = []
        self.og = ""
        self.og_w = ""
        self.og_h = ""

    def handle_starttag(self, tag: str, attrs) -> None:
        d = {k.lower(): (v or "") for k, v in attrs if k}
        if tag == "link":
            rel = d.get("rel", "").lower()
            href = d.get("href", "")
            if href and "icon" in rel:
                self.icons.append((rel, href, d.get("sizes", "")))
        elif tag == "meta":
            prop = (d.get("property") or d.get("name") or "").lower()
            content = d.get("content", "")
            if prop == "og:image" and content and not self.og:
                self.og = content
            elif prop == "og:image:width":
                self.og_w = content
            elif prop == "og:image:height":
                self.og_h = content
        elif tag == "img":
            self.imgs.append(d)


def _size_score(sizes: str) -> int:
    text = (sizes or "").strip().lower()
    if not text or text == "any":
        return 192 if not text else 256
    best = 0
    for part in text.split():
        if "x" not in part:
            continue
        a, b = part.split("x", 1)
        try:
            best = max(best, int(float(a)), int(float(b)))
        except ValueError:
            continue
    return best or 32


def _abs_url(base: str, href: str) -> str | None:
    href = (href or "").strip()
    if not href or href.startswith(("javascript:", "mailto:")):
        return None
    if href.startswith(("data:", "http://", "https://")):
        return href
    return urljoin(base, href)


def _icon_candidates(page_url: str, html_text: str) -> list[str]:
    parser = _IconParser()
    try:
        parser.feed(html_text)
    except Exception:
        return []
    ranked = []
    for rel, href, sizes in parser.icons:
        score = _size_score(sizes)
        if "apple" in rel and score < 180:
            score = 180
        ranked.append((0 if "apple" in rel else 1, -score, href))
    ranked.sort()
    out: list[str] = []
    for _, _, href in ranked:
        abs_u = _abs_url(page_url, href)
        if abs_u:
            out.append(abs_u)
    for attrs in parser.imgs:
        blob = " ".join(attrs.get(k, "") for k in ("alt", "class", "id", "src")).lower()
        if "logo" not in blob:
            continue
        if any(bad in blob for bad in ("hero", "screenshot", "banner", "poster", "og-image", "social")):
            continue
        try:
            w = float(attrs["width"]) if attrs.get("width", "").isdigit() else 0
            h = float(attrs["height"]) if attrs.get("height", "").isdigit() else 0
        except ValueError:
            w = h = 0
        if w and h and min(w, h) > 0 and max(w, h) / min(w, h) >= _WIDE_RATIO:
            continue
        abs_u = _abs_url(page_url, attrs.get("src", ""))
        if abs_u:
            out.append(abs_u)
    if not parser.icons:
        for path in ("/apple-touch-icon.png", "/favicon.ico"):
            out.append(urljoin(page_url, path))
    if parser.og:
        wide = False
        try:
            w, h = float(parser.og_w), float(parser.og_h)
            wide = min(w, h) > 0 and max(w, h) / min(w, h) >= _WIDE_RATIO
        except ValueError:
            wide = False
        if not wide:
            abs_u = _abs_url(page_url, parser.og)
            if abs_u:
                out.append(abs_u)
    deduped = []
    seen = set()
    for u in out:
        if u not in seen:
            seen.add(u)
            deduped.append(u)
    return deduped


def _github_homepage(owner: str, repo: str) -> str | None:
    resp = _http_get(
        f"https://api.github.com/repos/{owner}/{repo}",
        timeout=8,
    )
    if resp is None:
        return None
    try:
        home = (resp.json().get("homepage") or "").strip()
    except Exception:
        return None
    if home.startswith(("http://", "https://")):
        return _clean_url(home)
    return None


def _expand_site(url: str) -> list[str]:
    url = _clean_url(url)
    host = _host(url)
    if host in _SKIP_SITE_HOSTS:
        return []
    if host in {"github.com", "www.github.com"}:
        m = re.match(r"/([^/]+)/([^/#?]+)", urlparse(url).path or "")
        if not m:
            return []
        owner, repo = m.group(1), m.group(2).removesuffix(".git")
        if owner in {"topics", "features", "orgs", "settings"}:
            return []
        sites = []
        home = _github_homepage(owner, repo)
        if home and _host(home) not in {"github.com", "www.github.com"} | _SKIP_SITE_HOSTS:
            sites.append(home)
        sites.append(f"https://{owner}.github.io/{repo}/")
        return sites
    return [url]


def _urls_from_context(date: str, slug: str) -> list[str]:
    path = PROJECT_ROOT / "context" / f"{date}-{slug}.md"
    if not path.exists():
        return []
    found = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if "官网" not in line:
            continue
        found.extend(_clean_url(u) for u in _URL_RE.findall(line))
    return found


def _urls_from_archive(date: str, slug: str) -> list[str]:
    path = PROJECT_ROOT / "archive" / f"{date}.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8", errors="replace")
    idx = text.find(f"/products/{slug}")
    if idx < 0:
        return []
    m = re.search(r"官网:\s*(https?://\S+)", text[idx:idx + 900])
    if not m:
        return []
    return [_clean_url(m.group(1))]


def _candidate_sites(slug: str, date: str | None, website: str | None) -> list[str]:
    raw: list[str] = []
    if website:
        raw.extend(_clean_url(u) for u in _URL_RE.findall(website))
        if not raw and website.strip().startswith(("http://", "https://")):
            raw.append(_clean_url(website))
    if date:
        raw.extend(_urls_from_context(date, slug))
        raw.extend(_urls_from_archive(date, slug))
    out: list[str] = []
    seen = set()
    for u in raw:
        for site in _expand_site(u):
            if site not in seen:
                seen.add(site)
                out.append(site)
    return out


def _lookup_brand_logo(slug: str, date: str | None, website: str | None, work_dir: Path):
    """官网优先 apple-touch-icon，其次最大的 rel=icon，再是页面上的 logo 图。宽 og:image 跳过。"""
    for site in _candidate_sites(slug, date, website):
        resp = _http_get(site)
        if resp is None:
            continue
        ctype = resp.headers.get("content-type", "")
        if ctype.startswith("image/"):
            img, reason = _load_mark(resp.url, work_dir)
            if img is not None and reason is None:
                return img, resp.url
            continue
        if "html" not in ctype and "xml" not in ctype:
            continue
        for icon_url in _icon_candidates(resp.url, resp.text[:1_500_000]):
            img, reason = _load_mark(icon_url, work_dir)
            if img is not None and reason is None:
                return img, icon_url
    return None


def _logo_src_label(url: str) -> str:
    if url.startswith("data:"):
        kind = url.split(",", 1)[0][:48]
        return f"{kind} (inline)"
    return url.split("?", 1)[0]


def stage_logo(
    slug: str,
    logo_url: str | None,
    tmp_logos_dir: Path,
    name: str,
    website: str | None = None,
    date: str | None = None,
) -> str:
    """下载+规范化 logo。无标识或缩略图不是标识时先查品牌 logo，失败再用色块首字母。"""
    dest = tmp_logos_dir / f"{slug}.png"
    if dest.exists():
        return f'<img class="logo cover" src="{dest.as_uri()}">'
    tmp_logos_dir.mkdir(parents=True, exist_ok=True)
    img = None
    if logo_url:
        try:
            img, reason = _load_mark(logo_url, tmp_logos_dir)
        except Exception as e:
            img, reason = None, str(e)
        if img is None:
            why = "下载/处理失败" if reason == "download failed" else f"缩略图不是标识（{reason}）"
            print(f"  [warn] {slug}: {why}，转查品牌标识")
    else:
        print(f"  [warn] {slug}: 无 logo_url，转查品牌标识")
    if img is None:
        found = _lookup_brand_logo(slug, date, website, tmp_logos_dir)
        if not found:
            print(f"  [warn] {slug}: lookup failed，用色块首字母")
            return _fallback_logo_html(name)
        img, src = found
        print(f"  [logo] {slug}: 品牌标识 {_logo_src_label(src)}")
    _write_logo(img, dest)
    return f'<img class="logo cover" src="{dest.as_uri()}">'


def _fallback_logo_html(name: str) -> str:
    letter = html.escape((name or "?")[0].upper())
    return f'<div class="logo-fallback">{letter}</div>'


def _compute_name_font_size(name: str) -> int:
    """按产品名长度选字号：长名缩小避免折行挤底，单行宽度按 0.6em/字符估算。
    38px 满字号上限；330px max-width / 0.6 ≈ 14 字符能装下，超出逐级缩小。"""
    n = len(name)
    if n <= 11:
        return 38
    if n <= 14:
        return 32
    if n <= 18:
        return 26
    return 22


def fill_template(template_text: str, item: dict, date: str, logo_html: str) -> str:
    # calendar 模板额外需要日期的日号 + 月份缩写（DAY / MONTH）
    day = month = ""
    try:
        from datetime import datetime
        dt = datetime.strptime(date, "%Y-%m-%d")
        day = str(dt.day)
        month = dt.strftime("%b").upper()  # SEP / OCT / NOV ...
    except Exception:
        day, month = "", ""
    replacements = {
        "{{RANK}}": str(item["rank"]),
        "{{VOTES}}": str(item.get("votes", "")),
        "{{PRODUCT_NAME}}": html.escape(item["name"]),
        "{{NAME_FONT_SIZE}}": str(_compute_name_font_size(item["name"])),
        "{{LOGO_HTML}}": logo_html,
        "{{SUB}}": html.escape(item["sub"]),
        # one_liner 允许作者嵌 <b>/<br>（copy-guideline 规范），不转义
        "{{ONE_LINER}}": item["one_liner"],
        "{{DATE}}": date,
        "{{DAY}}": day,
        "{{MONTH}}": month,
    }
    out = template_text
    for k, v in replacements.items():
        out = out.replace(k, v)
    return out


def render_png(html_path: Path, png_path: Path) -> None:
    cmd = [
        CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=4", "--window-size=375,500",
        "--default-background-color=00000000",
        f"--screenshot={png_path}",
        html_path.as_uri(),
    ]
    subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=45)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("data_json", help="xhs/YYYY-MM-DD/data.json 路径")
    ap.add_argument("--only", help="只(重)渲染指定 slug（逗号分隔），不传则渲染全部")
    ap.add_argument("--template", default="", help="模板风格: 空=cream-glass (默认), mono=黑白版。mono 输出文件名加 -mono 后缀并存")
    ap.add_argument("--no-preview", action="store_true", help="已废弃，保留参数兼容旧调用")
    args = ap.parse_args()

    data_path = Path(args.data_json).resolve()
    if not data_path.exists():
        sys.exit(f"[fatal] 找不到 {data_path}")

    if args.template not in TEMPLATE_REGISTRY:
        sys.exit(f"[fatal] 未知 --template '{args.template}'，可选: {', '.join(k or '(默认)' for k in TEMPLATE_REGISTRY)}")
    template_file, suffix = TEMPLATE_REGISTRY[args.template]
    template_path = TEMPLATE_DIR / template_file
    if not template_path.exists():
        sys.exit(f"[fatal] 找不到模板 {template_path}")

    data = json.loads(data_path.read_text(encoding="utf-8"))
    date = data["date"]
    day_dir = data_path.parent
    temp_html_dir = day_dir / "temp_html"
    tmp_logos_dir = day_dir / ".tmp" / "logos"
    temp_html_dir.mkdir(parents=True, exist_ok=True)

    template_text = template_path.read_text(encoding="utf-8")
    only = set(args.only.split(",")) if args.only else None

    failed = []
    for item in sorted(data["products"], key=lambda p: p["rank"]):
        if only and item["slug"] not in only:
            continue
        logo_html = stage_logo(item["slug"], item.get("logo_url"), tmp_logos_dir, item["name"], website=item.get("website"), date=date)
        html_text = fill_template(template_text, item, date, logo_html)
        # mono 风格加 -mono 后缀实现与 cream-glass 并存；默认无后缀
        html_path = temp_html_dir / f"{item['rank']:02d}-{item['slug']}{suffix}.html"
        png_path = day_dir / f"{item['rank']:02d}-{item['slug']}{suffix}.png"
        html_path.write_text(html_text, encoding="utf-8")
        try:
            render_png(html_path, png_path)
            print(f"✓ {png_path}")
        except Exception as e:
            print(f"✗ {item['slug']}: 渲染失败 {e}", file=sys.stderr)
            failed.append(item["slug"])

    if failed:
        sys.exit(f"[warn] {len(failed)} 张渲染失败: {', '.join(failed)}")


if __name__ == "__main__":
    main()
