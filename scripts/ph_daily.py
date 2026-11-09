# /// script
# requires-python = ">=3.11"
# dependencies = ["tzdata"]
# ///
"""
ph_daily.py — Product Hunt 每日热门日报

管线: 官方 V2 GraphQL API 抓取当日 Top N(按票数)
      -> 推 Slack(Block Kit 富卡片) + 落本地 Markdown 归档
      （中文文案 / 点评由 Agent 按 .claude/skills/product-sense 产出，脚本不调模型）

设计要点:
- 时区: PH 的"今日榜"按太平洋时间(PT)0 点结算。脚本按 PT 日界显式
  取 postedAfter/postedBefore,不依赖 API 隐式的 today。北京时间 9:30 跑时,
  PT 约为前一日傍晚,"今日(PT)"榜已有大半天数据,排名足够有意义。
- 文案: 脚本只抓数据与渲染; zh_tagline / comment 字段留空,由 Agent 按
  product-sense skill 撰写。渲染侧已有非 LLM 回退(英文 tagline)。
- 零第三方依赖(除 tzdata 供 zoneinfo 在 Windows 上识别 IANA 时区)。

用法: uv run ph_daily.py            # 取 PT 今日榜
      uv run ph_daily.py --date 2026-06-01   # 取指定 PT 日
      uv run ph_daily.py --dry-run    # 不推 Slack,只打印 + 落 MD
      uv run ph_daily.py --refresh-votes 2026-06-01   # 次日补票:回写该 PT 日最终票数
      uv run ph_daily.py --refresh-votes 2026-06-01 --rerender  # 补票后顺带重渲图片
"""
from __future__ import annotations

import argparse
import json
import shutil
import ssl
import subprocess
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

# Windows 默认 GBK 控制台编码不了 emoji/中文,会让任何 print(榜单) 或日志 Tee
# 直接崩(UnicodeEncodeError)。在模块加载时统一把 stdout/stderr 钉成 UTF-8,
# 这样 main()、--dry-run 预览、test_smoke、PowerShell 日志都不再乱码或中断。
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass

HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parent
CONFIG_PATH = PROJECT_ROOT / "config.json"
ARCHIVE_DIR = PROJECT_ROOT / "archive"
PT = ZoneInfo("America/Los_Angeles")
CN = ZoneInfo("Asia/Shanghai")
RAW_DIR = PROJECT_ROOT / "data" / "raw" / "product-hunt"
XHS_DIR = PROJECT_ROOT / "xhs"

PH_ENDPOINT = "https://api.producthunt.com/v2/api/graphql"
# 本机网络坑(CLAUDE.local.md):对 Cloudflare 前置 endpoint,TLSv1.3 握手报
# UNEXPECTED_EOF,必须钉 TLSv1.2;且需 curl UA 绕 bot 指纹。PH/Slack 都可能走 CF。
USER_AGENT = "curl/8.4.0"


def _tls12_ctx() -> ssl.SSLContext:
    ctx = ssl.create_default_context()
    ctx.minimum_version = ssl.TLSVersion.TLSv1_2
    ctx.maximum_version = ssl.TLSVersion.TLSv1_2
    return ctx


_SSL = _tls12_ctx()


def http_post(url: str, payload: bytes, headers: dict, timeout: int = 30) -> bytes:
    h = {"User-Agent": USER_AGENT, "Content-Type": "application/json"}
    h.update(headers or {})
    req = urllib.request.Request(url, data=payload, method="POST", headers=h)
    with urllib.request.urlopen(req, timeout=timeout, context=_SSL) as resp:
        return resp.read()


# 网络类错误(连接/DNS/超时/5xx/429)的递增重试间隔(秒)。
# 覆盖 Mac 唤醒后网络就绪、PH API 瞬时抖动等场景;总等待约 7.5 分钟。
_RETRY_DELAYS = [30, 60, 90, 120, 150]


def _post_with_retry(payload: bytes, headers: dict) -> bytes:
    """POST 到 PH API。网络类错误按 _RETRY_DELAYS 递增重试,仍失败则抛出最后一次异常。"""
    last_exc: BaseException | None = None
    for i, delay in enumerate(_RETRY_DELAYS):
        try:
            return http_post(PH_ENDPOINT, payload, headers)
        except urllib.error.HTTPError as e:
            if e.code not in (429,) and e.code < 500:
                raise  # 4xx 客户端错误(401/400 等)重试无意义,直接抛给上层
            last_exc = e
        except urllib.error.URLError as e:
            last_exc = e
        if i < len(_RETRY_DELAYS) - 1:
            print(f"[warn] PH API 网络错误({last_exc}),{delay}s 后重试 {i+1}/{len(_RETRY_DELAYS)}", file=sys.stderr)
            time.sleep(delay)
    assert last_exc is not None
    raise last_exc

GQL_QUERY = """
query ($after: DateTime, $before: DateTime, $n: Int!) {
  posts(order: VOTES, postedAfter: $after, postedBefore: $before, first: $n) {
    edges {
      node {
        id
        name
        tagline
        description
        votesCount
        commentsCount
        url
        website
        thumbnail { type url videoUrl }
        topics(first: 3) { edges { node { name } } }
        slug
        dailyRank
        featuredAt
        media { type url videoUrl }
        productLinks { type url }
        makers { name username headline twitterUsername websiteUrl }
      }
    }
  }
}
"""


# --------------------------------------------------------------------------- #
# config
# --------------------------------------------------------------------------- #
def load_config() -> dict:
    if not CONFIG_PATH.exists():
        sys.exit(f"[fatal] 缺少配置文件 {CONFIG_PATH}。先复制 config.example.json 为 config.json 并填入凭据。")
    cfg = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    if not cfg.get("ph_token") or cfg["ph_token"].startswith("PASTE_"):
        sys.exit("[fatal] config.json 里 ph_token 还没填。去 https://www.producthunt.com/v2/oauth/applications 建个 app,用页面底部的 Developer Token。")
    return cfg


# --------------------------------------------------------------------------- #
# Product Hunt
# --------------------------------------------------------------------------- #
def pt_day_bounds(day: datetime) -> tuple[str, str]:
    """给定 PT 时区的某天,返回该 PT 日 [00:00, 次日00:00) 的 UTC ISO8601 边界。"""
    start_pt = day.replace(hour=0, minute=0, second=0, microsecond=0)
    end_pt = start_pt + timedelta(days=1)
    to_iso = lambda d: d.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return to_iso(start_pt), to_iso(end_pt)


def _resolve_ph_redirect(url: str, timeout: int = 8) -> str:
    """PH 的 website/productLinks 都是 producthunt.com/r/XXX 跳转链接。GET 会被 CF 挡(403),
    HEAD 能拿到 301 Location。解析失败返回空串,调用方保留原链接。"""
    if "producthunt.com/r/" not in (url or ""):
        return ""

    class _NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k):
            return None

    opener = urllib.request.build_opener(_NoRedirect, urllib.request.HTTPSHandler(context=_SSL))
    req = urllib.request.Request(url.split("?", 1)[0], method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        opener.open(req, timeout=timeout)
        return ""
    except urllib.error.HTTPError as e:
        loc = e.headers.get("Location") or ""
    except Exception:
        return ""
    for tail in ("?ref=producthunt", "&ref=producthunt"):
        loc = loc.replace(tail, "")
    return loc if loc.startswith(("http://", "https://")) else ""


def _strip_utm(url: str) -> str:
    return (url or "").split("?utm_campaign=", 1)[0]


def _post_from_node(n: dict) -> dict:
    """GraphQL node -> 下游统一结构。老字段保持不变,新字段只追加。"""
    topics = [t["node"]["name"] for t in n.get("topics", {}).get("edges", [])]
    thumb = n.get("thumbnail") or {}
    makers = [
        {k: m.get(k) for k in ("name", "username", "headline", "twitterUsername", "websiteUrl")}
        for m in (n.get("makers") or [])
        if (m.get("username") or "") != "[REDACTED]"  # PH 对未公开资料的 maker 返回 [REDACTED]
    ]
    return {
        "name": n["name"],
        "tagline": n.get("tagline") or "",
        "description": (n.get("description") or "").strip(),
        "votes": n.get("votesCount", 0),
        "comments": n.get("commentsCount", 0),
        "url": n.get("url") or "",
        "website": n.get("website") or "",
        "thumbnail": thumb.get("url") or "",
        "topics": topics,
        # ---- 2026-11-09 起新增(只加不改) ----
        "id": n.get("id") or "",
        "post_slug": n.get("slug") or "",
        "daily_rank": n.get("dailyRank"),
        "featured_at": n.get("featuredAt"),
        # PH 官方 logo = Post.thumbnail(API 没有独立 product/logo 字段;视频缩略图类型时 url 仍是静帧)
        "logo_url": thumb.get("url") or "",
        "logo_type": thumb.get("type") or "",
        "media": [
            {"type": x.get("type") or "", "url": x.get("url") or "", "videoUrl": x.get("videoUrl")}
            for x in (n.get("media") or [])
        ],
        "product_links": [
            {"type": x.get("type") or "", "url": _strip_utm(x.get("url") or "")}
            for x in (n.get("productLinks") or [])
        ],
        "makers": makers,
        "makers_redacted": sum(1 for m in (n.get("makers") or []) if (m.get("username") or "") == "[REDACTED]"),
    }


def resolve_websites(posts: list[dict]) -> None:
    """把 PH 跳转链接解析成真实官网,写进 website_resolved / product_links[].resolved。"""
    for p in posts:
        p["website_resolved"] = _resolve_ph_redirect(p.get("website", ""))
        for link in p.get("product_links") or []:
            link["resolved"] = _resolve_ph_redirect(link.get("url", ""))


def save_raw_snapshot(day_pt: datetime, data: dict, suffix: str = "") -> Path | None:
    """原始 GraphQL 响应落 data/raw/product-hunt/(gitignore,不进仓库)。失败不影响主流程。"""
    try:
        RAW_DIR.mkdir(parents=True, exist_ok=True)
        path = RAW_DIR / f"{day_pt.strftime('%Y-%m-%d')}{suffix}.json"
        snap = {"fetched_at": datetime.now(tz=CN).isoformat(timespec="seconds"), "response": data}
        path.write_text(json.dumps(snap, ensure_ascii=False, indent=1), encoding="utf-8")
        return path
    except Exception as e:
        print(f"[warn] 原始快照写入失败: {e}", file=sys.stderr)
        return None


def fetch_posts(token: str, day_pt: datetime, top_n: int, raw_suffix: str | None = "") -> list[dict]:
    after, before = pt_day_bounds(day_pt)
    payload = json.dumps({
        "query": GQL_QUERY,
        "variables": {"after": after, "before": before, "n": top_n},
    }).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    try:
        raw = _post_with_retry(payload, headers)
        data = json.loads(raw.decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        sys.exit(f"[fatal] PH API HTTP {e.code}: {body[:500]}")
    except urllib.error.URLError as e:
        sys.exit(f"[fatal] PH API 网络错误: {e}")

    if "errors" in data:
        sys.exit(f"[fatal] PH GraphQL 错误: {json.dumps(data['errors'], ensure_ascii=False)[:500]}")

    if raw_suffix is not None:
        save_raw_snapshot(day_pt, data, raw_suffix)
    edges = data.get("data", {}).get("posts", {}).get("edges", [])
    return [_post_from_node(e["node"]) for e in edges]


def fetch_with_fallback(token: str, day_pt: datetime, top_n: int, min_count: int = 5):
    """先取 PT 今日;若产品太少(PT 日刚开始),回退到前一 PT 日。"""
    posts = fetch_posts(token, day_pt, top_n)
    used_day = day_pt
    if len(posts) < min_count:
        prev = day_pt - timedelta(days=1)
        prev_posts = fetch_posts(token, prev, top_n)
        if len(prev_posts) > len(posts):
            posts, used_day = prev_posts, prev
    return posts, used_day



# --------------------------------------------------------------------------- #
# 渲染: Slack + Markdown
# --------------------------------------------------------------------------- #
def build_slack_blocks(posts: list[dict], day_pt: datetime) -> dict:
    blocks = [
        {"type": "header", "text": {"type": "plain_text",
            "text": f"🚀 Product Hunt 今日热门 · {day_pt.strftime('%Y-%m-%d')} (PT)", "emoji": True}},
        {"type": "context", "elements": [{"type": "mrkdwn",
            "text": f"按票数排序 · Top {len(posts)} · 数据源 PH 官方 API"}]},
        {"type": "divider"},
    ]
    for rank, p in enumerate(posts, 1):
        link = p["url"] or p["website"]
        badge = _badge_str(p)
        title = f"*{rank}. <{link}|{_esc(p['name'])}>*  {badge}"
        zh = p.get("zh_tagline") or p["tagline"]
        line = f"{title}\n{_esc(zh)}"
        if p.get("comment"):
            line += f"\n💡 _{_esc(p['comment'])}_"
        if p["topics"]:
            line += f"\n🏷️ {' · '.join(p['topics'])}"
        blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": line}})
    return {"blocks": blocks}


def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _badge_str(p: dict) -> str:
    """票数/评论 badge：票数>0 显示👍，否则用💬，都为0只显示排名。"""
    parts = []
    if p["votes"] > 0:
        parts.append(f"👍 {p['votes']}")
    if p["comments"] > 0:
        parts.append(f"💬 {p['comments']}")
    return " · ".join(parts) if parts else ""


def _js_string_literal(s: str) -> str:
    """把字符串安全嵌进 ego-browser heredoc 里的 JS 字面量。"""
    return json.dumps(s, ensure_ascii=False)


def backfill_votes_from_producthunt_pages(posts: list[dict], timeout: int = 180) -> int:
    """当 PH API 没给 votes 时，用 ego-browser 打开 PH 页面兜底抓当前 Upvote points。

    只抓文本里明确出现的 "Upvote • N points"，不把 followers、comments 或 rank 当票数。
    ego-browser 不可用或页面没暴露 points 时静默跳过，保留 votes=0。
    """
    missing = [(i, p) for i, p in enumerate(posts) if int(p.get("votes") or 0) <= 0 and p.get("url")]
    if not missing:
        return 0
    if not shutil.which("ego-browser"):
        print("[warn] ego-browser 不可用，跳过 PH 页面票数兜底。", file=sys.stderr)
        return 0

    items = [
        {"i": i, "name": p.get("name", ""), "url": p.get("url", "")}
        for i, p in missing
    ]
    script = f"""const task = await useOrCreateTaskSpace('ph-daily votes fallback')
const items = {_js_string_literal(json.dumps(items, ensure_ascii=False))}
const parsed = JSON.parse(items)
const out = []
for (const item of parsed) {{
  try {{
    await openOrReuseTab(item.url, {{wait:true, timeout:30}})
    await wait(1)
    const text = await js(String.raw`document.body.innerText`)
    const m = text.match(/Upvote\\s*[•·]\\s*([0-9][0-9,]*)\\s*points?/i)
    out.push({{i:item.i, name:item.name, votes:m ? Number(m[1].replace(/,/g,'')) : 0}})
  }} catch (e) {{
    out.push({{i:item.i, name:item.name, votes:0, error:String(e && e.message || e)}})
  }}
}}
cliLog(JSON.stringify(out))
"""
    try:
        proc = subprocess.run(
            ["ego-browser", "nodejs"],
            input=script,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
    except Exception as e:
        print(f"[warn] PH 页面票数兜底失败: {e}", file=sys.stderr)
        return 0

    if proc.returncode != 0:
        print(f"[warn] PH 页面票数兜底失败(rc={proc.returncode}): {proc.stderr[:300]}", file=sys.stderr)
        return 0

    lines = [ln.strip() for ln in proc.stdout.splitlines() if ln.strip()]
    if not lines:
        return 0
    try:
        results = json.loads(lines[-1])
    except json.JSONDecodeError as e:
        print(f"[warn] PH 页面票数兜底输出无法解析: {e}", file=sys.stderr)
        return 0

    filled = 0
    for r in results:
        votes = int(r.get("votes") or 0)
        idx = int(r.get("i"))
        if votes > 0 and 0 <= idx < len(posts):
            posts[idx]["votes"] = votes
            filled += 1
    if filled:
        print(f"[info] PH 页面兜底补齐 {filled} 个票数字段")
    return filled


def post_to_slack(webhook: str, payload: dict) -> None:
    http_post(webhook, json.dumps(payload).encode("utf-8"), {})


def build_markdown(posts: list[dict], day_pt: datetime) -> str:
    lines = [
        f"# Product Hunt 今日热门 · {day_pt.strftime('%Y-%m-%d')} (PT)",
        "",
        f"> 按票数排序 · Top {len(posts)} · 数据源:Product Hunt 官方 V2 API",
        "",
    ]
    for rank, p in enumerate(posts, 1):
        link = p["url"] or p["website"]
        badge = _badge_str(p)
        lines.append(f"## {rank}. [{p['name']}]({link}) {badge}")
        zh = p.get("zh_tagline")
        if zh:  # 默认中文:中文译名做主行,英文原文降为参考
            lines.append(f"- **{zh}**")
            lines.append(f"- 🔤 {p['tagline']}")
        else:
            lines.append(f"- **{p['tagline']}**")
        if p.get("comment"):
            lines.append(f"- 💡 {p['comment']}")
        if p["topics"]:
            lines.append(f"- 🏷️ {' · '.join(p['topics'])}")
        if p["website"]:
            lines.append(f"- 🔗 官网: {p['website']}")
        if p.get("website_resolved"):
            lines.append(f"- 🏠 官网直达: {p['website_resolved']}")
        if p.get("thumbnail"):
            lines.append(f"- 🖼️ logo: {p['thumbnail']}")
        if p.get("makers"):
            ms = ", ".join(f"{m['name']} (@{m['username']})" + (f" · {m['headline']}" if m.get("headline") else "")
                           for m in p["makers"])
            lines.append(f"- 👥 makers: {ms}")
        if p.get("media"):
            kinds = ", ".join(f"{k}×{sum(1 for x in p['media'] if x['type'] == k)}"
                              for k in dict.fromkeys(x["type"] for x in p["media"]))
            lines.append(f"- 🎞️ media: {kinds}")
        lines.append("")
    return "\n".join(lines)



# --------------------------------------------------------------------------- #
# 次日补票: 同一 PT 日重新拉一次,回写 archive + xhs data.json
# --------------------------------------------------------------------------- #
def _product_slug(url: str) -> str:
    """https://www.producthunt.com/products/<slug>?utm... -> <slug>(data.json 的 slug 就是它)。"""
    path = _strip_utm(url).split("?", 1)[0].rstrip("/")
    return path.rsplit("/", 1)[-1] if "/products/" in path or "/posts/" in path else ""


_FINAL_MARK = "- 🏁 最终:"


def refresh_votes(token: str, date: str, rerender: bool = False) -> dict:
    """按 PT 日界重拉该日榜单(多取一些防排名变动),按产品 slug/名称匹配回原来那批产品。

    - archive/DATE.md: 标题行的早期票数不动(图上印的就是它),每个产品追加/更新一行
      `- 🏁 最终: 👍 N · 💬 M · 最终第 K（刷新于 ... UTC+8）`,文件头追加/更新刷新说明。
    - xhs/DATE/data.json: votes 改成最终票数,首次刷新时把原值留在 votes_snapshot。
    - 默认不重渲图片;rerender=True 时调用 render_xhs.py 重出全部 PNG。
    """
    day = datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=PT)
    fresh = fetch_posts(token, day, 30, raw_suffix=".final")
    stamp = datetime.now(tz=CN).strftime("%Y-%m-%d %H:%M")
    by_slug, by_name = {}, {}
    for rank, p in enumerate(fresh, 1):
        p["final_rank"] = rank
        s = _product_slug(p["url"])
        if s:
            by_slug.setdefault(s, p)
        by_name.setdefault(p["name"].strip().lower(), p)

    def match(slug: str, name: str):
        return by_slug.get(slug) or by_name.get((name or "").strip().lower())

    result = {"date": date, "refreshed_at": stamp, "items": [], "archive": None, "data_json": None}

    md_path = ARCHIVE_DIR / f"{date}.md"
    if md_path.exists():
        import re
        lines = md_path.read_text(encoding="utf-8").splitlines()
        out, i, total = [], 0, 0
        head_re = re.compile(r"^## (\d+)\. \[(.*?)\]\((\S*?)\)\s*(.*)$")
        while i < len(lines):
            ln = lines[i]
            m = head_re.match(ln)
            if not m:
                if not ln.startswith(_FINAL_MARK):
                    out.append(ln)
                i += 1
                continue
            out.append(ln)
            total += 1
            i += 1
            block = []
            while i < len(lines) and not lines[i].startswith("## "):
                if not lines[i].startswith(_FINAL_MARK):
                    block.append(lines[i])
                i += 1
            hit = match(_product_slug(m.group(3)), m.group(2))
            if hit:
                old = re.search(r"👍 (\d+)", m.group(4))
                result["items"].append({"rank": int(m.group(1)), "name": m.group(2),
                                        "votes_before": int(old.group(1)) if old else None,
                                        "votes_final": hit["votes"], "comments_final": hit["comments"],
                                        "final_rank": hit["final_rank"]})
                final = f"{_FINAL_MARK} 👍 {hit['votes']} · 💬 {hit['comments']} · 最终第 {hit['final_rank']}（刷新于 {stamp} UTC+8）"
                # 插在空行之前,保持块尾空行
                while block and block[-1] == "":
                    block.pop()
                block += [final, ""]
            out.extend(block)
        text = "\n".join(out)
        note = f"> 🏁 最终票数已于 {stamp}（UTC+8）按 PT 日界补拉；标题行票数为出图时的早期快照。"
        text = re.sub(r"^> 🏁 最终票数已于.*$\n?", "", text, flags=re.M)
        text = re.sub(r"^(> 按票数排序.*)$", lambda mm: mm.group(1) + "\n" + note, text, count=1, flags=re.M)
        md_path.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")
        result["archive"] = str(md_path)

    dj = XHS_DIR / date / "data.json"
    if dj.exists():
        data = json.loads(dj.read_text(encoding="utf-8"))
        changed = 0
        for item in data.get("products", []):
            hit = match(item.get("slug", ""), item.get("name", ""))
            if not hit or not hit["votes"]:  # API 偶尔给 0 票(隐藏期),不拿 0 覆盖
                continue
            item.setdefault("votes_snapshot", item.get("votes"))
            item["votes"] = hit["votes"]
            item["votes_refreshed_at"] = f"{stamp} UTC+8"
            changed += 1
            if not any(x["rank"] == item.get("rank") for x in result["items"]):
                result["items"].append({"rank": item.get("rank"), "name": item.get("name"),
                                        "votes_before": item["votes_snapshot"], "votes_final": hit["votes"],
                                        "comments_final": hit["comments"], "final_rank": hit["final_rank"]})
        dj.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        result["data_json"] = str(dj)
        print(f"[info] data.json 已回写 {changed} 个产品的最终票数")
        if rerender:
            subprocess.run([sys.executable, str(HERE / "render_xhs.py"), str(dj)], check=False)

    for it in sorted(result["items"], key=lambda x: x["rank"] or 99):
        print(f"  #{it['rank']} {it['name']}: 👍 {it['votes_before']} -> {it['votes_final']} (最终第 {it['final_rank']})")
    expected = total if md_path.exists() else len(result["items"])
    missing = expected - len(result["items"])
    if missing > 0:
        print(f"[warn] 有 {missing} 个产品没匹配上(可能改名/下架),保持原票数", file=sys.stderr)
    return result


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def now_pt() -> datetime:
    return datetime.now(tz=PT)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="指定 PT 日期 YYYY-MM-DD(默认 PT 今日)")
    ap.add_argument("--dry-run", action="store_true", help="不推 Slack,只打印 + 落 MD")
    ap.add_argument("--refresh-votes", metavar="DATE", help="次日补票:重拉该 PT 日最终票数,回写 archive 与 xhs/DATE/data.json")
    ap.add_argument("--rerender", action="store_true", help="配合 --refresh-votes:回写后重渲该日 PNG(默认不重渲)")
    ap.add_argument("--out-dir", help="归档写到这个目录而不是 archive/(验证用,不覆盖正式归档)")
    args = ap.parse_args()

    cfg = load_config()
    top_n = int(cfg.get("top_n", 10))

    if args.refresh_votes:
        refresh_votes(cfg["ph_token"], args.refresh_votes, rerender=args.rerender)
        return

    if args.date:
        day = datetime.strptime(args.date, "%Y-%m-%d").replace(tzinfo=PT)
        posts, used_day = fetch_posts(cfg["ph_token"], day, top_n), day
    else:
        posts, used_day = fetch_with_fallback(cfg["ph_token"], now_pt(), top_n)

    if not posts:
        sys.exit("[fatal] 没取到任何产品。检查 token / 日期 / 网络。")

    print(f"[info] 取到 {len(posts)} 个产品 (PT {used_day.strftime('%Y-%m-%d')})")

    backfill_votes_from_producthunt_pages(posts)
    resolve_websites(posts)

    # 归档（zh_tagline/comment 留空；文案由 Agent 按 product-sense skill 写）
    out_dir = Path(args.out_dir) if args.out_dir else ARCHIVE_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    md = build_markdown(posts, used_day)
    md_path = out_dir / f"{used_day.strftime('%Y-%m-%d')}.md"
    # 下游可直接读的结构化数据(含 makers/media/官方 logo/官网直达),与 MD 同名
    md_path.with_suffix(".json").write_text(json.dumps(posts, ensure_ascii=False, indent=1), encoding="utf-8")
    md_path.write_text(md, encoding="utf-8")
    print(f"[info] 已归档 {md_path}")

    # Slack
    if args.dry_run:
        print("[info] --dry-run,跳过 Slack。预览:\n")
        print(md)
        return

    webhook = cfg.get("slack_webhook_url", "")
    if not webhook or webhook.startswith("PASTE_"):
        print("[warn] 未配置 slack_webhook_url,跳过 Slack 推送(MD 已落盘)。", file=sys.stderr)
        return
    post_to_slack(webhook, build_slack_blocks(posts, used_day))
    print("[info] 已推送 Slack。")


if __name__ == "__main__":
    main()
