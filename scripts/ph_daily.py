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
        if p.get("thumbnail"):
            lines.append(f"- 🖼️ logo: {p['thumbnail']}")
        lines.append("")
    return "\n".join(lines)



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

    backfill_votes_from_producthunt_pages(posts)

    if not args.no_zh:
        annotate_zh(cfg, posts)

    # 归档
    ARCHIVE_DIR.mkdir(exist_ok=True)
    md = build_markdown(posts, used_day)
    md_path = ARCHIVE_DIR / f"{used_day.strftime('%Y-%m-%d')}.md"
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
