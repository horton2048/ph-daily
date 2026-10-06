# /// script
# requires-python = ">=3.11"
# dependencies = ["tzdata"]
# ///
"""冒烟测试: 不碰 PH API,用假数据验证 Slack/MD 渲染（脚本不再调 LLM）。"""
import json
from datetime import datetime
import ph_daily as m

day = datetime(2026, 6, 2, tzinfo=m.PT)
posts = [
    {"name": "Cursor 2.0", "tagline": "The AI code editor that ships features for you",
     "description": "Agentic IDE that plans, edits, and verifies across your whole repo.",
     "votes": 1284, "comments": 96, "url": "https://www.producthunt.com/posts/cursor",
     "website": "https://cursor.com", "thumbnail": "", "topics": ["Developer Tools", "AI"],
     "zh_tagline": "", "comment": ""},
    {"name": "Granola", "tagline": "AI notepad for back-to-back meetings",
     "description": "Transcribes and summarizes your meetings without a bot joining the call.",
     "votes": 902, "comments": 51, "url": "https://www.producthunt.com/posts/granola",
     "website": "https://granola.ai", "thumbnail": "", "topics": ["Productivity", "AI"],
     "zh_tagline": "", "comment": ""},
]

print(">>> 测 Markdown 渲染（无中文点评，回退英文 tagline）...")
md = m.build_markdown(posts, day)
print(md[:600])
assert "Cursor 2.0" in md and "Granola" in md

print("\n>>> 测 Slack blocks 渲染 ...")
blocks = m.build_slack_blocks(posts, day)
print(f"  blocks 数: {len(blocks['blocks'])}")
print(json.dumps(blocks["blocks"][3], ensure_ascii=False, indent=2))
print("\n[ok] 渲染链路通过。")
