# /// script
# requires-python = ">=3.11"
# dependencies = ["tzdata"]
# ///
"""
ph_daily.py — Product Hunt 每日热门日报

管线: 官方 V2 GraphQL API 抓取当日 Top N(按票数)
      -> LLM(Agnes AI 网关, agnes-2.0-flash)出中文 tagline + 一句话点评
      -> 推 Slack(Block Kit 富卡片) + 落本地 Markdown 归档

设计要点:
- 时区: PH 的"今日榜"按太平洋时间(PT)0 点结算。脚本按 PT 日界显式
  取 postedAfter/postedBefore,不依赖 API 隐式的 today。北京时间 9:30 跑时,
  PT 约为前一日傍晚,"今日(PT)"榜已有大半天数据,排名足够有意义。
- LLM: 走 OpenAI 兼容网关(config 的 llm_*),不用 response_format,改裸 JSON
  + 防御性解析;强约束简体中文。点评失败时降级为只用英文 tagline,日报照发。
- 零第三方依赖(除 tzdata 供 zoneinfo 在 Windows 上识别 IANA 时区)。

用法: uv run ph_daily.py            # 取 PT 今日榜
      uv run ph_daily.py --date 2026-06-01   # 取指定 PT 日
      uv run ph_daily.py --dry-run    # 不推 Slack,只打印 + 落 MD
"""
from __future__ import annotations

import argparse
import json
import ssl
import sys
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
CONFIG_PATH = HERE / "config.json"
ARCHIVE_DIR = HERE / "archive"
PT = ZoneInfo("America/Los_Angeles")

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
        thumbnail { url }
        topics(first: 3) { edges { node { name } } }
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


def fetch_posts(token: str, day_pt: datetime, top_n: int) -> list[dict]:
    after, before = pt_day_bounds(day_pt)
    payload = json.dumps({
        "query": GQL_QUERY,
        "variables": {"after": after, "before": before, "n": top_n},
    }).encode("utf-8")
    try:
        raw = http_post(PH_ENDPOINT, payload, {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        })
        data = json.loads(raw.decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        sys.exit(f"[fatal] PH API HTTP {e.code}: {body[:500]}")
    except urllib.error.URLError as e:
        sys.exit(f"[fatal] PH API 网络错误: {e}")

    if "errors" in data:
        sys.exit(f"[fatal] PH GraphQL 错误: {json.dumps(data['errors'], ensure_ascii=False)[:500]}")

    edges = data.get("data", {}).get("posts", {}).get("edges", [])
    out = []
    for e in edges:
        n = e["node"]
        topics = [t["node"]["name"] for t in n.get("topics", {}).get("edges", [])]
        out.append({
            "name": n["name"],
            "tagline": n.get("tagline") or "",
            "description": (n.get("description") or "").strip(),
            "votes": n.get("votesCount", 0),
            "comments": n.get("commentsCount", 0),
            "url": n.get("url") or "",
            "website": n.get("website") or "",
            "thumbnail": (n.get("thumbnail") or {}).get("url") or "",
            "topics": topics,
        })
    return out


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
# LLM 中文点评(Agnes AI 网关, OpenAI 兼容)
# --------------------------------------------------------------------------- #
def annotate_zh(cfg: dict, posts: list[dict]) -> None:
    """批量给 posts 加 zh_tagline / comment 字段。失败则降级(留空)。

    走 OpenAI 兼容的 /chat/completions,provider 由 config 的 llm_* 字段决定;
    当前用 Agnes AI 免费网关的 agnes-2.0-flash(非推理、无 <think>、~1s)。
    """
    api_key = cfg.get("llm_api_key")
    if not api_key:
        return
    items = [
        {"i": i, "name": p["name"], "tagline": p["tagline"], "desc": p["description"][:300]}
        for i, p in enumerate(posts)
    ]
    sys_prompt = (
        "你是科技产品编辑。下面是 Product Hunt 今日热门产品列表。"
        "对每个产品:1) 把 tagline 翻译成自然的简体中文(zh);"
        "2) 写一句不超过 40 字的简体中文点评(comment),说清它解决什么问题/亮点。"
        "必须用简体中文,严禁葡萄牙语或其他语言。"
        '只输出 JSON 数组,每项 {"i":序号,"zh":"...","comment":"..."},不要任何解释或代码块标记。'
    )
    body = json.dumps({
        "model": cfg.get("llm_model", "agnes-2.0-flash"),
        "messages": [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": json.dumps(items, ensure_ascii=False)},
        ],
        # 低温让 JSON 输出更可控。
        "temperature": 0.2,
    }).encode("utf-8")
    url = cfg.get("llm_base_url", "https://apihub.agnes-ai.com/v1").rstrip("/") + "/chat/completions"
    # 重试:网关偶发抖动或返回非法 JSON,重抽一次通常就过;3 次都不行才降级为纯英文。
    last_err = None
    for attempt in range(1, 4):
        try:
            raw = http_post(url, body, {"Authorization": f"Bearer {api_key}"}, timeout=90)
            data = json.loads(raw.decode("utf-8"))
            content = data["choices"][0]["message"]["content"]
            parsed = _loads_lenient(content)
            by_i = {int(x["i"]): x for x in parsed}
            for i, p in enumerate(posts):
                x = by_i.get(i)
                if x:
                    p["zh_tagline"] = (x.get("zh") or "").strip()
                    p["comment"] = (x.get("comment") or "").strip()
            return
        except Exception as e:
            last_err = e
            print(f"[warn] LLM 点评第 {attempt}/3 次失败: {e}", file=sys.stderr)
    print(f"[warn] LLM 点评 3 次均失败,降级为纯英文: {last_err}", file=sys.stderr)


def _loads_lenient(text: str):
    """剥掉推理 <think> 块、可能的 ```json 围栏,截取第一个 [..] 数组再解析。"""
    text = text.strip()
    # agnes-2.0-flash 不带 <think>;但若换成推理模型会在 content 里带
    # <think>...</think>,先剥掉,否则 think 里的方括号会把数组切割逻辑带偏。
    if "</think>" in text:
        text = text.split("</think>", 1)[-1]
    if "```" in text:
        text = text.replace("```json", "").replace("```", "")
    l, r = text.find("["), text.rfind("]")
    if l != -1 and r != -1:
        text = text[l:r + 1]
    return json.loads(text)


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
        title = f"*{rank}. <{link}|{_esc(p['name'])}>*  👍 {p['votes']}"
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
        lines.append(f"## {rank}. [{p['name']}]({link}) 👍 {p['votes']} · 💬 {p['comments']}")
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
        lines.append("")
    return "\n".join(lines)


def _h(s: str) -> str:
    """HTML 转义(含引号,供属性值用)。"""
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def build_html(posts: list[dict], day_pt: datetime) -> str:
    day = day_pt.strftime("%Y-%m-%d")
    cards = []
    for rank, p in enumerate(posts, 1):
        link = p["url"] or p["website"]
        zh = p.get("zh_tagline") or ""
        thumb = (
            f'<img class="thumb" src="{_h(p["thumbnail"])}" alt="" loading="lazy">'
            if p.get("thumbnail") else '<div class="thumb thumb-ph"></div>'
        )
        topics = "".join(
            f'<span class="topic">{_h(t)}</span>' for t in p["topics"]
        )
        comment = (
            f'<p class="comment">💡 {_h(p["comment"])}</p>' if p.get("comment") else ""
        )
        # 默认中文:有译文时中文占据主标语位,英文原文降为次行参考
        if zh:
            primary_line = f'<p class="tagline">{_h(zh)}</p>'
            zh_line = f'<p class="zh">🔤 {_h(p["tagline"])}</p>'
        else:
            primary_line = f'<p class="tagline">{_h(p["tagline"])}</p>'
            zh_line = ""
        site = (
            f'<a class="site" href="{_h(p["website"])}" target="_blank" rel="noopener">官网 ↗</a>'
            if p["website"] else ""
        )
        cards.append(f"""    <article class="card">
      <div class="rank">{rank}</div>
      {thumb}
      <div class="body">
        <h2 class="name"><a href="{_h(link)}" target="_blank" rel="noopener">{_h(p['name'])}</a></h2>
        {primary_line}
        {zh_line}
        {comment}
        <div class="meta">
          <span class="stat">👍 {p['votes']}</span>
          <span class="stat">💬 {p['comments']}</span>
          {site}
        </div>
        <div class="topics">{topics}</div>
      </div>
    </article>""")

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Product Hunt 今日热门 · {day}</title>
<style>
  :root {{ --bg:#0f1115; --card:#181b22; --line:#262b35; --fg:#e6e8ec; --mut:#9aa3b2; --ph:#ff6154; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--fg);
    font:16px/1.55 -apple-system,"Segoe UI",Roboto,"Helvetica Neue","PingFang SC","Microsoft YaHei",sans-serif; }}
  .wrap {{ max-width:760px; margin:0 auto; padding:32px 20px 64px; }}
  header h1 {{ margin:0 0 6px; font-size:1.6rem; }}
  header .sub {{ color:var(--mut); font-size:.9rem; margin-bottom:28px; }}
  .card {{ display:grid; grid-template-columns:36px 64px 1fr; gap:14px; align-items:start;
    background:var(--card); border:1px solid var(--line); border-radius:14px;
    padding:16px; margin-bottom:14px; }}
  .rank {{ font-size:1.1rem; font-weight:700; color:var(--mut); text-align:center; padding-top:4px; }}
  .thumb {{ width:64px; height:64px; border-radius:12px; object-fit:cover; background:#222; }}
  .thumb-ph {{ background:linear-gradient(135deg,#2a2f3a,#1c2029); }}
  .body {{ min-width:0; }}
  .name {{ margin:0 0 2px; font-size:1.08rem; }}
  .name a {{ color:var(--fg); text-decoration:none; }}
  .name a:hover {{ color:var(--ph); }}
  .tagline {{ margin:0 0 4px; font-weight:600; }}
  .zh {{ margin:0 0 4px; color:var(--mut); }}
  .comment {{ margin:0 0 8px; color:#cdd3dd; font-size:.92rem; }}
  .meta {{ display:flex; align-items:center; gap:14px; flex-wrap:wrap; margin-bottom:8px; }}
  .stat {{ color:var(--mut); font-size:.9rem; }}
  .site {{ color:var(--ph); text-decoration:none; font-size:.9rem; }}
  .site:hover {{ text-decoration:underline; }}
  .topics {{ display:flex; gap:6px; flex-wrap:wrap; }}
  .topic {{ font-size:.75rem; color:var(--mut); border:1px solid var(--line);
    border-radius:999px; padding:1px 9px; }}
  footer {{ color:var(--mut); font-size:.8rem; text-align:center; margin-top:32px; }}
  @media (max-width:480px) {{ .card {{ grid-template-columns:28px 1fr; }} .thumb {{ display:none; }} }}
</style>
</head>
<body>
  <div class="wrap">
    <header>
      <h1>🚀 Product Hunt 今日热门 · {day} (PT)</h1>
      <div class="sub">按票数排序 · Top {len(posts)} · 数据源 Product Hunt 官方 V2 API</div>
    </header>
{chr(10).join(cards)}
    <footer>由 ph_daily 生成</footer>
  </div>
</body>
</html>
"""


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def now_pt() -> datetime:
    return datetime.now(tz=PT)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="指定 PT 日期 YYYY-MM-DD(默认 PT 今日)")
    ap.add_argument("--dry-run", action="store_true", help="不推 Slack,只打印 + 落 MD")
    ap.add_argument("--no-zh", action="store_true", help="跳过 LLM 中文点评")
    args = ap.parse_args()

    cfg = load_config()
    top_n = int(cfg.get("top_n", 10))

    if args.date:
        day = datetime.strptime(args.date, "%Y-%m-%d").replace(tzinfo=PT)
        posts, used_day = fetch_posts(cfg["ph_token"], day, top_n), day
    else:
        posts, used_day = fetch_with_fallback(cfg["ph_token"], now_pt(), top_n)

    if not posts:
        sys.exit("[fatal] 没取到任何产品。检查 token / 日期 / 网络。")

    print(f"[info] 取到 {len(posts)} 个产品 (PT {used_day.strftime('%Y-%m-%d')})")

    if not args.no_zh:
        annotate_zh(cfg, posts)

    # 归档
    ARCHIVE_DIR.mkdir(exist_ok=True)
    md = build_markdown(posts, used_day)
    md_path = ARCHIVE_DIR / f"{used_day.strftime('%Y-%m-%d')}.md"
    md_path.write_text(md, encoding="utf-8")
    print(f"[info] 已归档 {md_path}")

    html = build_html(posts, used_day)
    html_path = ARCHIVE_DIR / f"{used_day.strftime('%Y-%m-%d')}.html"
    html_path.write_text(html, encoding="utf-8")
    print(f"[info] 已归档 {html_path}")

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
