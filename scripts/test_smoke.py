# /// script
# requires-python = ">=3.11"
# dependencies = ["tzdata"]
# ///
"""冒烟测试: 不碰 PH API,用假数据验证 LLM 中文点评 + Slack/MD 渲染。"""
import json
from datetime import datetime
import ph_daily as m

cfg = json.loads(m.CONFIG_PATH.read_text(encoding="utf-8"))  # 跳过 ph_token 校验
day = datetime(2026, 6, 2, tzinfo=m.PT)
posts = [
    {"name": "Cursor 2.0", "tagline": "The AI code editor that ships features for you",
     "description": "Agentic IDE that plans, edits, and verifies across your whole repo.",
     "votes": 1284, "comments": 96, "url": "https://www.producthunt.com/posts/cursor",
     "website": "https://cursor.com", "thumbnail": "", "topics": ["Developer Tools", "AI"]},
    {"name": "Granola", "tagline": "AI notepad for back-to-back meetings",
     "description": "Transcribes and summarizes your meetings without a bot joining the call.",
     "votes": 902, "comments": 51, "url": "https://www.producthunt.com/posts/granola",
     "website": "https://granola.ai", "thumbnail": "", "topics": ["Productivity", "AI"]},
]

print(">>> 测 LLM 中文点评 ...")
m.annotate_zh(cfg, posts)
for p in posts:
    print(f"  {p['name']}: zh={p.get('zh_tagline')!r} comment={p.get('comment')!r}")

print("\n>>> 测 Markdown 渲染 ...")
print(m.build_markdown(posts, day)[:600])

print("\n>>> 测 Slack blocks 渲染 ...")
blocks = m.build_slack_blocks(posts, day)
print(f"  blocks 数: {len(blocks['blocks'])}")
print(json.dumps(blocks["blocks"][3], ensure_ascii=False, indent=2))
print("\n[ok] 渲染链路通过。")
