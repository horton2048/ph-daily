#!/usr/bin/env python3
"""
正确生成 2026-08-06 小红书信息图
严格按照 product-sense 规范：HTML 模板 + Chrome headless 渲染
"""
import os
import re
import json
import subprocess
from pathlib import Path

# 配置
CONTEXT_DIR = Path.home() / "Projects/ph-daily/context"
XHS_DIR = Path.home() / "Projects/ph-daily/xhs/2026-08-06"
DATE = "2026-08-06"
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# 10 个产品（按排名）
PRODUCTS = [
    "cloudflare-os",
    "muse-code",
    "annotate",
    "ai-spend-console-by-rippling",
    "brandfetch-mcp",
    "shieldstral",
    "website-to-markdown-api",
    "superlog-responder",
    "aveiro",
    "ododok",
]

# Product Hunt logo URLs refreshed via ego-browser on 2026-08-07.
LOGO_URLS = {
    "cloudflare-os": "https://ph-files.imgix.net/edcb3719-f3b7-49e8-9676-27631af01cb9.png",
    "muse-code": "https://ph-files.imgix.net/aaeba1be-643c-4283-8a81-abe32d32dde5.png",
    "annotate": "https://ph-files.imgix.net/e75e84d4-a8a6-4678-9315-41e3722bc803.png",
    "ai-spend-console-by-rippling": "https://ph-files.imgix.net/53c0c89f-1ce9-435a-9cce-8ffb70118915.png",
    "brandfetch-mcp": "https://ph-files.imgix.net/155640fe-c6ec-473b-b0e0-f9f035874e4f.png",
    "shieldstral": "https://ph-files.imgix.net/f429754c-62e0-45ca-b61d-92204dd75c8f.svg",
    "website-to-markdown-api": "https://ph-files.imgix.net/4e8c2ab3-baf7-485a-b79d-ecad0be8c8fd.png",
    "superlog-responder": "https://ph-files.imgix.net/f5e16691-e739-48ba-9494-535f6a7ac36c.png",
    "aveiro": "https://ph-files.imgix.net/0b9f6d6b-4980-42fc-af75-acb55e53d825.svg",
    "ododok": "https://ph-files.imgix.net/0e15f596-110a-4c86-9c64-51b8faa72ec2.png",
}

MANUAL_COPY = {
    "cloudflare-os": {
        "insight": "上市公司开源 AI OS、内部数千人日活，是软件免费、拉动基础设施消费、生态服务收钱的 open-core 范式。销售团队月省 10,000+ 小时，是量化 ROI 的教科书级表述。",
    },
    "muse-code": {
        "insight": "Meta 没把 Muse Code 只做成一个 CLI，而是把长任务拆成主 agent、后台 agent 和可追溯事件日志，核心卖点是长时程协作的工程系统。",
    },
    "annotate": {
        "insight": "它把录屏从沟通素材变成 agent 可读输入，真正的产品机会不在录制，而在关键帧、语音、标注和任务上下文的结构化交接。",
    },
    "ai-spend-console-by-rippling": {
        "product": "AI Spend Console",
        "insight": "Rippling 用自己最强的员工、权限、费用数据切入 AI 治理，比单点报表更有黏性；预算控制和业务结果归因才是企业愿意付费的部分。",
    },
    "brandfetch-mcp": {
        "insight": "Brandfetch MCP 把品牌资产从静态 API 变成 agent 工具，需求很窄但高频：只要 AI 进入对外物料生产，logo 和品牌色就不能再靠猜。",
    },
    "shieldstral": {
        "insight": "Mistral 把安全策略做成运行时可配置层，而不是只靠模型训练阶段内化规则，这更接近企业治理需要的可审计、可切换、可解释。",
    },
    "website-to-markdown-api": {
        "insight": "把网页转 Markdown 看似工具小，但它卡在 RAG 和 agent 工作流最前面；稳定处理 JS、噪声、多格式，比再做一个爬虫 demo 更接近真实需求。",
    },
    "superlog-responder": {
        "insight": "Superlog 从发现 bug 延伸到自动回复评论，把研发协作里的高频琐事接进 PR 流程；关键壁垒是置信门槛，而不是自动化本身。",
    },
    "aveiro": {
        "insight": "Aveiro 把内容管理、网站发布和 MCP 放进同一个发布面板，押注的是 agent 生成内容后还需要一个可靠的上线和审批层。",
    },
    "ododok": {
        "insight": "Ododok 的产品信号很轻，但儿童阅读这类场景更看重低摩擦和可持续习惯；后续能否变成订阅，取决于内容供给和家长反馈闭环。",
    },
}

def extract_pm_anchors(product_slug):
    """从 context 文件提取 6 个 PM 锚点"""
    context_file = CONTEXT_DIR / f"{DATE}-{product_slug}.md"

    if not context_file.exists():
        print(f"    ⚠️  context 文件不存在: {context_file}")
        return None

    content = context_file.read_text(encoding='utf-8')

    anchors = {
        'product': '',
        'tagline_en': '',
        'tagline_zh': '',
        'logo': '',
        'votes': '',
        'rank': 0,
        'pain': '',  # 痛点锚
        'what': '',  # 它干嘛的
        'why': '',   # 凭什么是它
        'capital': {'founders': '', 'funding': ''},  # 资本信号
        'biz': '',   # 怎么赚钱
        'insight': ''  # PM 视角
    }

    # 基本信息
    match = re.search(r'\| 产品名 \| ([^\n]+) \|', content)
    if match:
        # 清理产品名中的括号说明
        product_raw = match.group(1).strip()
        # 提取括号前的部分
        product_clean = re.split(r'[（(]', product_raw)[0].strip()
        anchors['product'] = product_clean

    match = re.search(r'\| 英文 tagline \| ([^\n]+) \|', content)
    if match:
        anchors['tagline_en'] = match.group(1).strip()

    match = re.search(r'\| 中文 tagline \| ([^\n]+) \|', content)
    if match:
        anchors['tagline_zh'] = match.group(1).strip()

    match = re.search(r'\| logo \| (https://[^\s|]+) \|', content)
    if match:
        anchors['logo'] = match.group(1).strip()

    match = re.search(r'\| 票数 / 评论 \| ([^\n]+) \|', content)
    if match:
        votes_raw = match.group(1).strip()
        # 提取票数
        votes_match = re.search(r'votes?[=:]\s*(\d+)', votes_raw, re.IGNORECASE)
        if votes_match:
            anchors['votes'] = votes_match.group(1)
        elif '归档未含' in votes_raw or 'votes=0' in votes_raw:
            anchors['votes'] = '—'
        else:
            anchors['votes'] = '—'

    # 6 个 PM 锚点需要手工从 context 提炼
    # 这里使用简化逻辑：从"解决什么问题"和"怎么做的"段落提取关键句

    # 痛点锚：从"解决什么问题"段落提取第一个要点
    pain_section = re.search(r'## 解决什么问题.*?\n\n(.*?)\n\n##', content, re.DOTALL)
    if pain_section:
        pain_text = pain_section.group(1)
        # 提取第一个列表项或段落
        pain_items = re.findall(r'^[-*]\s+\*\*(.+?)\*\*[：:](.*?)(?=\n[-*]|\n\n|$)', pain_text, re.MULTILINE | re.DOTALL)
        if pain_items:
            pain_title, pain_detail = pain_items[0]
            # 简化描述（去掉来源标注等）
            pain_clean = re.sub(r'（.*?）', '', pain_detail).strip()
            pain_clean = re.sub(r'\(.*?\)', '', pain_clean).strip()
            pain_clean = pain_clean.split('。')[0] + '。'
            anchors['pain'] = pain_clean[:100]  # 限制长度

    # "它干嘛的"：从"是做什么的"提取核心句
    what_section = re.search(r'## 是做什么的.*?\n\n(.*?)(?=\n\n##|\Z)', content, re.DOTALL)
    if what_section:
        what_text = what_section.group(1)
        # 提取第一段
        first_para = what_text.split('\n\n')[0]
        # 清理
        what_clean = re.sub(r'\*\*', '', first_para)
        what_clean = re.sub(r'（.*?）', '', what_clean)
        what_clean = re.sub(r'\(.*?\)', '', what_clean)
        # 取前两句
        sentences = what_clean.split('。')
        anchors['what'] = '。'.join(sentences[:2]) + '。' if sentences else ''
        anchors['what'] = anchors['what'][:150]

    # "凭什么是它"：从"怎么做的"提取关键技术特点（简化版）
    why_section = re.search(r'## 怎么做的.*?\n\n(.*?)(?=\n\n##|\Z)', content, re.DOTALL)
    if why_section:
        why_text = why_section.group(1)
        # 提取前3个技术要点
        why_items = re.findall(r'^[-*]\s+\*\*(.+?)\*\*[：:](.*?)(?=\n[-*]|\n\n|$)', why_text, re.MULTILINE | re.DOTALL)[:3]
        if why_items:
            why_points = []
            for title, detail in why_items:
                point = f"{title}"
                why_points.append(point)
            anchors['why'] = ' · '.join(why_points)[:120]

    # 资本信号：从"团队/背景/融资"提取
    team_section = re.search(r'## 团队.*?融资.*?\n\n(.*?)(?=\n\n##|\Z)', content, re.DOTALL)
    if team_section:
        team_text = team_section.group(1)
        # 提取融资信息
        funding_match = re.search(r'\| 融资 \| ([^\n|]+) \|', team_text)
        if funding_match:
            anchors['capital']['funding'] = funding_match.group(1).strip()
        # 提取创始人/团队信息
        founders_match = re.search(r'\| (?:创始人|发布团队|团队|公司主体) \| ([^\n|]+) \|', team_text)
        if founders_match:
            anchors['capital']['founders'] = founders_match.group(1).strip()[:50]

    # 怎么赚钱：从"定价/商业模式"提取
    biz_section = re.search(r'## 定价.*?商业模式.*?\n\n(.*?)(?=\n\n##|\Z)', content, re.DOTALL)
    if biz_section:
        biz_text = biz_section.group(1)
        # 提取前两个要点
        biz_items = re.findall(r'^[-*]\s+(.*?)(?=\n[-*]|\n\n|$)', biz_text, re.MULTILINE | re.DOTALL)[:2]
        if biz_items:
            biz_clean = []
            for item in biz_items:
                item_clean = re.sub(r'\*\*', '', item).strip()
                item_clean = re.sub(r'（.*?）', '', item_clean)
                item_clean = item_clean.split('。')[0]
                biz_clean.append(item_clean)
            anchors['biz'] = '；'.join(biz_clean)[:100]

    # PM 视角：优先使用人工校准版本，避免长文案溢出和占位味太重。
    anchors['insight'] = f"该产品针对特定场景的痛点提供解决方案，值得关注其落地效果和市场反馈。"

    anchors['logo'] = LOGO_URLS.get(product_slug, anchors['logo'])
    anchors.update(MANUAL_COPY.get(product_slug, {}))

    return anchors


def generate_html(rank, anchors):
    """生成信息图 HTML"""

    # 选择渐变色（根据排名）
    gradients = [
        "linear-gradient(135deg,#ff9a56 0%,#ff7a45 100%)",  # 橙色
        "linear-gradient(135deg,#6366f1 0%,#4f46e5 100%)",  # 紫蓝
        "linear-gradient(135deg,#ec4899 0%,#db2777 100%)",  # 粉红
        "linear-gradient(135deg,#10b981 0%,#059669 100%)",  # 绿色
        "linear-gradient(135deg,#f59e0b 0%,#d97706 100%)",  # 黄色
        "linear-gradient(135deg,#8b5cf6 0%,#7c3aed 100%)",  # 紫色
        "linear-gradient(135deg,#06b6d4 0%,#0891b2 100%)",  # 青色
        "linear-gradient(135deg,#f43f5e 0%,#e11d48 100%)",  # 红色
        "linear-gradient(135deg,#14b8a6 0%,#0d9488 100%)",  # 蓝绿
        "linear-gradient(135deg,#a855f7 0%,#9333ea 100%)",  # 深紫
    ]
    hero_bg = gradients[(rank - 1) % len(gradients)]

    # 处理 logo（如果是 URL）
    logo_html = ''
    if anchors['logo'] and anchors['logo'].startswith('http'):
        logo_html = f'<img class="logo" src="{anchors["logo"]}" alt="" onerror="this.style.display=\'none\'">'
    else:
        # 使用产品名首字母
        initial = anchors['product'][0] if anchors['product'] else '#'
        logo_html = f'<div class="logo">{initial}</div>'

    votes_display = f"👍 {anchors['votes']}" if anchors['votes'] and anchors['votes'] != '—' else ''

    html = f'''<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{anchors['product']} · 小红书信息图</title>
<style>
  :root{{
    --bg:#faf6f0; --card:#ffffff;
    --ink:#2b2b2b; --dim:#8a8a8a;
    --red:#ff4d4f; --orange:#ff7a45; --yellow:#ffd666;
    --blue:#3b82f6; --green:#52c41a; --purple:#a855f7;
    --hero-bg:{hero_bg};
  }}
  *{{margin:0;padding:0;box-sizing:border-box}}
  html,body{{background:transparent;font-family:-apple-system,"PingFang SC","SF Pro Display",system-ui,sans-serif;
    color:var(--ink);margin:0;padding:0;overflow:hidden}}
  .card{{width:375px;height:500px;background:var(--card);
    border-radius:22px;overflow:hidden;display:flex;flex-direction:column}}
  .hero{{background:var(--hero-bg);
    padding:13px 20px 10px;color:#fff;flex-shrink:0}}
  .hero .badge{{display:inline-block;background:rgba(255,255,255,.28);
    border-radius:999px;padding:3px 10px;font-size:10px;font-weight:600;
    letter-spacing:.5px;margin-bottom:7px}}
  .hero .title-row{{display:flex;align-items:center;gap:9px;margin-bottom:3px}}
  .hero .logo{{width:28px;height:28px;border-radius:6px;background:#fff;
    object-fit:cover;flex-shrink:0;box-shadow:0 2px 6px rgba(0,0,0,.15)}}
  .hero .logo-placeholder{{width:28px;height:28px;border-radius:6px;background:rgba(255,255,255,.3);
    display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:800;
    color:#fff;flex-shrink:0}}
  .hero h1{{font-size:20px;font-weight:800;line-height:1.12;flex:1;min-width:0;
    display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}}
  .hero .sub{{font-size:10.5px;opacity:.94;line-height:1.35;
    white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
  .pain{{background:#fff5f0;padding:8px 20px;flex-shrink:0}}
  .pain .tag{{color:var(--orange);font-size:9.5px;font-weight:700;letter-spacing:1px;margin-bottom:3px}}
  .pain .case{{font-size:10.5px;line-height:1.42;font-weight:500;
    display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}}
  .mid{{flex:1;display:flex;flex-direction:column;min-height:0;overflow:hidden}}
  .block{{padding:7px 20px;border-bottom:1px solid #f5f5f5;flex-shrink:0}}
  .block .tag{{display:flex;align-items:center;gap:5px;font-size:9.5px;font-weight:700;
    letter-spacing:1px;margin-bottom:3px}}
  .block .tag .dot{{width:15px;height:15px;border-radius:4px;display:flex;
    align-items:center;justify-content:center;font-size:8px;color:#fff}}
  .block .body{{font-size:10.5px;line-height:1.42;color:var(--ink);
    display:-webkit-box;-webkit-line-clamp:5;-webkit-box-orient:vertical;overflow:hidden}}
  .t-do .dot{{background:var(--blue)}} .t-do .tag{{color:var(--blue)}}
  .vs{{background:#f9f9fb;padding:7px 20px;flex-shrink:0}}
  .vs .lbl{{font-size:9.5px;color:var(--orange);font-weight:700;letter-spacing:1px;margin-bottom:3px}}
  .vs .body{{font-size:10px;line-height:1.42;color:var(--ink);
    display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}}
  .duo{{display:grid;grid-template-columns:1fr 1fr;gap:0;flex-shrink:0}}
  .duo .col{{padding:7px 13px 9px;border-bottom:1px solid #f5f5f5;min-width:0}}
  .duo .col.cap{{padding-left:20px}}
  .duo .col:first-child{{border-right:1px solid #f5f5f5}}
  .duo .tag{{display:flex;align-items:center;gap:5px;font-size:9.5px;font-weight:700;
    letter-spacing:1px;margin-bottom:4px}}
  .duo .tag .dot{{width:15px;height:15px;border-radius:4px;display:flex;
    align-items:center;justify-content:center;font-size:8px;color:#fff}}
  .duo .cap .dot{{background:var(--purple)}} .duo .cap .tag{{color:var(--purple)}}
  .duo .biz .dot{{background:var(--green)}} .duo .biz .tag{{color:var(--green)}}
  .duo .body{{font-size:9.5px;line-height:1.38;
    display:-webkit-box;-webkit-line-clamp:5;-webkit-box-orient:vertical;overflow:hidden}}
  .hook{{background:linear-gradient(135deg,#2b2b2b 0%,#1a1a1a 100%);color:#fff;
    padding:9px 20px;flex:1;min-height:0;overflow:hidden}}
  .hook .q{{font-size:9.5px;color:var(--yellow);font-weight:700;letter-spacing:1.5px;
    margin-bottom:5px;display:flex;align-items:center;gap:6px}}
  .hook .q::before{{content:"";display:inline-block;width:3px;height:10px;
    background:var(--yellow);border-radius:2px}}
  .hook .insight{{font-size:10px;line-height:1.42;font-weight:500;
    display:-webkit-box;-webkit-line-clamp:5;-webkit-box-orient:vertical;overflow:hidden}}
  .foot{{padding:5px 20px;display:flex;justify-content:space-between;align-items:center;
    background:#fafafa;flex-shrink:0}}
  .foot .src{{font-size:8.5px;color:var(--dim)}}
  .foot .date{{font-size:8.5px;color:var(--dim)}}
</style>
</head>
<body>
<div class="card">

  <div class="hero">
    <span class="badge">PH 每日榜 #{rank}{' · ' + votes_display if votes_display else ''}</span>
    <div class="title-row">
      {logo_html}
      <h1>{anchors['product']}</h1>
    </div>
    <div class="sub">{anchors['tagline_zh']}</div>
  </div>

  <div class="pain">
    <div class="tag">⚠️ 痛点锚</div>
    <div class="case">{anchors['pain'] if anchors['pain'] else '针对特定场景的实际痛点'}</div>
  </div>

  <div class="mid">

    <div class="block t-do">
      <div class="tag"><span class="dot">📱</span>它干嘛的</div>
      <div class="body">{anchors['what'] if anchors['what'] else anchors['tagline_zh']}</div>
    </div>

    <div class="vs">
      <div class="lbl">🎯 凭什么是它</div>
      <div class="body">{anchors['why'] if anchors['why'] else '独特的技术方案和产品定位'}</div>
    </div>

    <div class="duo">
      <div class="col cap">
        <div class="tag"><span class="dot">💰</span>资本信号</div>
        <div class="body">{anchors['capital']['founders'][:40] if anchors['capital']['founders'] else '—'}<br>{anchors['capital']['funding'][:40] if anchors['capital']['funding'] else '未披露融资'}</div>
      </div>
      <div class="col biz">
        <div class="tag"><span class="dot">💵</span>怎么赚钱</div>
        <div class="body">{anchors['biz'] if anchors['biz'] else 'SaaS 订阅或按量计费'}</div>
      </div>
    </div>

    <div class="hook">
      <div class="q">🪝 PM 视角</div>
      <div class="insight">{anchors['insight']}</div>
    </div>

  </div>

  <div class="foot">
    <span class="src">来源：Product Hunt 每日榜</span>
    <span class="date">{DATE}</span>
  </div>

</div>
</body>
</html>'''

    return html


def render_to_png(html_path, png_path):
    """使用 Chrome headless 渲染 HTML 为 PNG"""
    # Chrome 参数：
    # --headless=new: 新版 headless 模式
    # --disable-gpu: 禁用 GPU（兼容性）
    # --window-size=375,500 + --force-device-scale-factor=4: 输出 1500×2000 高清图
    # --force-device-scale-factor=4: 高清渲染
    # --screenshot: 截图
    cmd = [
        CHROME_PATH,
        '--headless=new',
        '--disable-gpu',
        '--window-size=375,500',
        '--force-device-scale-factor=4',
        '--hide-scrollbars',
        f'--screenshot={png_path}',
        f'file://{html_path}'
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            print(f"    ⚠️  Chrome 渲染失败: {result.stderr}")
            return False
        return True
    except subprocess.TimeoutExpired:
        print(f"    ⚠️  Chrome 渲染超时")
        return False
    except Exception as e:
        print(f"    ⚠️  渲染错误: {e}")
        return False


def main():
    """主函数"""
    print(f"🎨 正确生成 {DATE} 的小红书信息图")
    print(f"📐 规范: 375×500px @ 4x scale → 1500×2000px PNG")
    print(f"🌐 渲染: Chrome headless")
    print()

    # 确保输出目录存在
    XHS_DIR.mkdir(parents=True, exist_ok=True)
    temp_dir = XHS_DIR / 'temp_html'
    temp_dir.mkdir(exist_ok=True)

    success_count = 0
    failed_count = 0

    for rank, product_slug in enumerate(PRODUCTS, 1):
        print(f"[{rank}/10] {product_slug}")

        # 提取 PM 锚点
        print(f"    📋 提取 PM 锚点...")
        anchors = extract_pm_anchors(product_slug)
        if not anchors:
            print(f"    ❌ 无法提取信息")
            failed_count += 1
            continue

        anchors['rank'] = rank

        # 生成 HTML
        print(f"    📝 生成 HTML...")
        html_content = generate_html(rank, anchors)
        html_path = temp_dir / f"{rank:02d}-{product_slug}.html"
        html_path.write_text(html_content, encoding='utf-8')

        # 渲染 PNG
        print(f"    🎨 Chrome 渲染...")
        png_path = XHS_DIR / f"{rank:02d}-{product_slug}.png"
        if render_to_png(html_path, png_path):
            print(f"    ✅ 已保存: {png_path.name}")
            success_count += 1
        else:
            print(f"    ❌ 渲染失败")
            failed_count += 1

        print()

    print("=" * 60)
    print(f"✅ 完成！共处理 {len(PRODUCTS)} 个产品")
    print(f"   - 成功: {success_count} 个")
    print(f"   - 失败: {failed_count} 个")
    print(f"   - 输出目录: {XHS_DIR}")
    print(f"   - 临时 HTML: {temp_dir}")


if __name__ == "__main__":
    main()
