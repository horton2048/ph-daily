#!/usr/bin/env python3
"""Generate the remaining 2026-08-08 Product Hunt XHS cards (#2-#10)."""

from __future__ import annotations

import html
import subprocess
from pathlib import Path


DATE = "2026-08-08"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "xhs" / DATE
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

PRODUCTS = [
    {
        "rank": 2, "slug": "basedash-subscriptions", "icon": "📊", "name": "Basedash Subscriptions",
        "sub": "订阅任意 dashboard，按计划投递到邮箱或 Slack",
        "pain": "业务用户要自助看数，数据团队又怕指标口径失控；dashboard 截图还得反复手动发送。",
        "what": "AI-native BI 平台的新功能：把任意 dashboard 或 chart 变成定时快照；自然语言分析、SQL 与语义层共用同一套受治理指标。",
        "rows": [("手动截图转发", "按计划自动投递"), ("自由生成答案", "展示 SQL 可追溯"), ("各处指标分裂", "语义层统一口径")],
        "nums": [("YC", "S20"), ("6", "人团队"), ("750+", "数据源"), ("28", "次发布")],
        "capline": "Max Musing 创办；融资金额未查到",
        "biz": "<b>$1,000/月</b> Startup + AI usage；Enterprise 自定义，支持自托管与 SSO。",
        "hook": "BI 的下一步不是再造一张图，而是让<b>可信指标主动抵达决策现场</b>。订阅把分析从“去看 dashboard”改成按节奏触发行动。",
    },
    {
        "rank": 3, "slug": "astrapixels", "icon": "🪐", "name": "AstraPixels",
        "sub": "像素画太阳系，天体处于真实当前位置",
        "pain": "互动地图常死于库存卖完、访客不再回来、旧链接腐烂；原始百万美元首页十年后约 22% 链接失效。",
        "what": "用 astronomy-engine 实时计算天体位置的像素太阳系：可浏览 171 个天体、未来六个月天象，并认领小行星或购买广告位。",
        "rows": [("静态天体列表", "轨道实时计算"), ("库存卖完即死", "3,000 岩石续供"), ("链接永久烂掉", "月检失败后回收")],
        "nums": [("171", "天体"), ("3k", "岩石"), ("$5", "认领"), ("6月", "天象")],
        "capline": "个人项目；未查到融资",
        "biz": "<b>$5</b> 小行星认领 + 广告位月租/CPM + 行星、太阳等稀缺位租赁。",
        "hook": "它不是只卖一次性的像素格，而是用<b>实时天象做留存、程序库存做供给、链接回收做治理</b>，把一次性噱头改造成可循环市场。",
    },
    {
        "rank": 4, "slug": "hexis", "icon": "⬡", "name": "Hexis",
        "sub": "把企业 agent 的技能、工具与上下文变成 Git 资产",
        "pain": "skills 和 context 放进 GitHub 后，非开发者难操作、文件级权限难管；放在供应商产品里又不真正属于公司。",
        "what": "Git 之上的企业 agent 控制面：Markdown/YAML 定义 context、skills、tools、permissions 与 identity，经 review 和访问控制后供任意 runtime 消费。",
        "rows": [("供应商内封闭配置", "公司自有文件"), ("共享服务账号", "具名 agent 身份"), ("黑盒 prompt 片段", "可 diff 的技能")],
        "nums": [("1.5k+", "CodeMode★"), ("45k+", "下载"), ("Git", "底座"), ("开源", "核心")],
        "capline": "Bevel 团队；融资金额未查到",
        "biz": "PH 标 <b>Free</b>；官网走企业咨询销售，付费数字未披露。",
        "hook": "企业 agent 的护城河未必是 runtime，而是<b>谁拥有技能、上下文、权限和审计历史</b>。Git 让这些资产可迁移、可审查、可追责。",
    },
    {
        "rank": 5, "slug": "toolport", "icon": "🔌", "name": "Toolport",
        "sub": "所有 MCP server 共用一个本地网关端口",
        "pain": "仅 3 个 MCP server、62 个工具，就可能在提问前吞掉约 24,000 tokens；不同客户端还要反复配置密钥。",
        "what": "本地优先 MCP gateway：桌面 app 管理 server、profile 与凭据，gateway 只暴露 4 个 meta-tools，按需发现并加载真实工具。",
        "rows": [("全量工具塞上下文", "lazy discovery"), ("每客户端一份 JSON", "一套共享 registry"), ("密钥明文复制", "OS Keychain 注入")],
        "nums": [("91%", "最多省"), ("33", "客户端"), ("113", "GitHub★"), ("MIT", "开源")],
        "capline": "Tyler 独立开发；872 commits",
        "biz": "个人版 <b>免费 MIT</b>；Teams 5 人内免费，之后 <b>$39/月</b>。",
        "hook": "MCP 普及后，竞争从“有没有工具”转向<b>工具发现、上下文成本和调用治理</b>。网关层会成为多 agent 工作台的控制平面。",
    },
    {
        "rank": 6, "slug": "patch-your-security-center", "icon": "🛡️", "name": "Patch — Your Security Center",
        "sub": "把个人数字安全检查集中到 Mac 与 iPhone",
        "pain": "密码泄露、诈骗判断、2FA 与信用冻结散落在不同流程里；普通用户很难持续维护自己的安全状态。",
        "what": "个人安全中心：检查邮箱与密码泄露、识别诈骗、指导 2FA/信用冻结/数据经纪商移除，并用 AI 顾问解释下一步。",
        "rows": [("把敏感数据上云", "多数检查本地跑"), ("安全建议一大堆", "按标签页给下一步"), ("黑盒 AI 判断", "确定性检查兜底")],
        "nums": [("19", "类攻击"), ("4", "月开发"), ("$1.99", "月起"), ("1年", "发布免费")],
        "capline": "Cory 单人开发；无独立安全审计",
        "biz": "免费层；Patch <b>$1.99/月</b>，Premium $3.99，Family $6.99。",
        "hook": "安全产品最难卖的不是功能，而是<b>可信边界的解释</b>。把离机数据、失败场景与未审计状态主动写清楚，本身就是产品能力。",
    },
    {
        "rank": 7, "slug": "voicedumps", "icon": "🎙️", "name": "VoiceDumps",
        "sub": "按住 globe 键，说话，文字出现在任意光标处",
        "pain": "云端听写受字数、网络和隐私限制，语音还要往返别人的 GPU；会议转写又常需要 bot 入会。",
        "what": "macOS 本地语音转文字：按住 globe 键听写到任意 app，也能导入音视频转写；Whisper 模型在 Apple Silicon 上完全离线运行。",
        "rows": [("语音上传云端", "whisper.cpp 本地跑"), ("会议 bot 入会", "本机双音轨"), ("订阅与字数上限", "MIT 免费不限量")],
        "nums": [("~0.4s", "热启动"), ("720MB", "模型"), ("42", "commits"), ("MIT", "开源")],
        "capline": "Naveen 一人项目；未披露融资",
        "biz": "<b>免费开源</b>，无订阅、无账户、无 API key、无付费层。",
        "hook": "本地 AI 的交换条件很具体：<b>用 720MB 下载换隐私、离线与低延迟</b>。把成本明确量化，比泛泛喊“端侧更安全”更有说服力。",
    },
    {
        "rank": 8, "slug": "arbyn", "icon": "🛍️", "name": "Arbyn",
        "sub": "能对 Shopify 订单采取行动的 AI 客服 agent",
        "pain": "电商客服重复问题多；现有工具常按工单涨价，或只会回答却不能退款、取消、重发与修改订单。",
        "what": "面向 Shopify 的客服与销售 agent：自动回复邮件/聊天，读取订单和政策；涉及钱的操作先准备动作，经一键批准后执行。",
        "rows": [("只回答不执行", "直接操作订单"), ("动钱全自动", "审批闸 + 额度"), ("先搭知识库", "安装时自动读取")],
        "nums": [("21", "语言"), ("50", "影子对话"), ("$59", "月起"), ("7年", "客服经验")],
        "capline": "Odera Joseph 创办；融资未披露",
        "biz": "150 对话 <b>免费</b>；500 条 $59/月；无限对话 <b>$99/月</b>。",
        "hook": "客服 agent 的价值不止是回答率，而是<b>能否安全完成订单动作</b>。先影子模式学习，再用审批、退款上限和 kill switch 扩权。",
    },
    {
        "rank": 9, "slug": "supabase-rls-leak-demo", "icon": "🧪", "name": "Supabase RLS Leak Demo",
        "sub": "复现跨租户 RLS 泄漏，并用同一套测试验证修复",
        "pain": "“已经打开 RLS”不等于租户隔离成立；策略可能通过 happy path，却仍把一个租户的行泄给另一个租户。",
        "what": "可本地运行的 Postgres 安全测试夹具：broken 分支 4 项失败，fixed 分支 5 项通过，唯一差异是一个 policies.sql。",
        "rows": [("看配置猜安全", "负向测试给证据"), ("管理员角色跑测试", "应用角色断言"), ("依赖云项目与 Docker", "PGlite 进程内跑")],
        "nums": [("4→5", "测试"), ("1", "SQL 差异"), ("9", "审计查询"), ("MIT", "开源")],
        "capline": "Cenk 独立开发；未融资",
        "biz": "夹具 <b>免费 MIT</b>；RLS Audit Kit $29，固定价审计 $99 起。",
        "hook": "安全功能不能靠“已开启”的截图验收。可复用的标准应是：<b>同租户能读、跨租户零行、并以真实应用角色执行</b>。",
    },
    {
        "rank": 10, "slug": "pesterly", "icon": "📎", "name": "Pesterly",
        "sub": "自动催客户交文件，交齐后立即停止",
        "pain": "报税、开户和律所流程常卡在客户漏交文件；门户容易被忽略，团队只能反复人工追问“还差什么”。",
        "what": "Google Workspace 文件催收：把清单变成邮件，在第 0/3/7/10 天自动跟进；只列缺失项，上传直接进入自己的 Drive。",
        "rows": [("让客户登录门户", "熟悉邮箱里完成"), ("每次重发全清单", "只追未交项"), ("人工盯进度", "交齐自动停止")],
        "nums": [("0/3/7/10", "天跟进"), ("2", "项权限"), ("$9", "月起"), ("0", "文件托管")],
        "capline": "两位创始人；融资未披露",
        "biz": "Solo <b>$9/月</b>；3 邮箱 $19；10 邮箱 $39，客户与请求不限量。",
        "hook": "低频 B2B 流程不一定需要新门户。把动作放回<b>客户本来就会回复的邮件线程</b>，再把进度与停止条件自动化，摩擦更小。",
    },
]


CSS = """
:root{--ink:#2b2b2b;--dim:#8a8a8a;--red:#ff4d4f;--orange:#ff7a45;--yellow:#ffd666;--blue:#3b82f6;--green:#52c41a;--purple:#a855f7}
*{margin:0;padding:0;box-sizing:border-box}html,body{background:transparent;font-family:-apple-system,"PingFang SC","SF Pro Display",system-ui,sans-serif;color:var(--ink);overflow:hidden}
.card{width:375px;height:500px;background:#fff;border-radius:22px;overflow:hidden;display:flex;flex-direction:column}.hero{background:linear-gradient(135deg,#ff9a56,#ff7a45);padding:16px 20px 12px;color:#fff;flex-shrink:0}.badge{display:inline-block;background:rgba(255,255,255,.28);border-radius:99px;padding:3px 10px;font-size:10px;font-weight:600;letter-spacing:.5px;margin-bottom:7px}.title-row{display:flex;align-items:center;gap:9px;margin-bottom:3px}.logo{width:28px;height:28px;border-radius:6px;background:rgba(255,255,255,.82);display:flex;align-items:center;justify-content:center;font-size:15px;flex-shrink:0;box-shadow:0 2px 6px #0002}.hero h1{font-size:21px;font-weight:800;line-height:1.15;flex:1;min-width:0}.sub{font-size:11px;opacity:.94;line-height:1.4}.pain{background:#fff5f0;padding:9px 20px;flex-shrink:0}.pain .tag{color:var(--orange);font-size:9.5px;font-weight:700;letter-spacing:1px;margin-bottom:3px}.pain .case{font-size:11px;line-height:1.45;font-weight:500}.mid{flex:1;display:flex;flex-direction:column;min-height:0;overflow:hidden}.block{padding:8px 20px;border-bottom:1px solid #f5f5f5;flex-shrink:1;min-height:0}.tagline{display:flex;align-items:center;gap:5px;font-size:9.5px;font-weight:700;letter-spacing:1px;margin-bottom:3px}.dot{width:15px;height:15px;border-radius:4px;display:flex;align-items:center;justify-content:center;font-size:8px;color:#fff}.block .tagline{color:var(--blue)}.block .dot{background:var(--blue)}.body{font-size:11px;line-height:1.45}.vs{background:#f9f9fb;padding:8px 20px;flex-shrink:1;min-height:0}.vs .lbl{font-size:9.5px;color:var(--orange);font-weight:700;letter-spacing:1px;margin-bottom:3px}.row{display:grid;grid-template-columns:1fr auto 1fr;gap:5px;align-items:center;font-size:10px;margin:2px 0}.old{color:var(--dim);text-decoration:line-through}.arrow{color:var(--orange);font-weight:800}.new{font-weight:600}.duo{display:grid;grid-template-columns:1fr 1fr;flex-shrink:1;min-height:0}.col{padding:8px 14px 12px;border-bottom:1px solid #f5f5f5}.cap{padding-left:20px;border-right:1px solid #f5f5f5}.col .tagline{margin-bottom:4px}.cap .tagline{color:var(--purple)}.cap .dot{background:var(--purple)}.biz .tagline{color:var(--green)}.biz .dot{background:var(--green)}.nums{display:grid;grid-template-columns:1fr 1fr;gap:5px;margin-bottom:5px}.n{background:#f5f0ff;border-radius:7px;padding:3px;text-align:center}.big{font-size:12px;font-weight:800;color:var(--purple);line-height:1.1}.lb{font-size:7.5px;color:var(--dim);margin-top:1px}.dim-line{font-size:8.5px;color:var(--dim);line-height:1.3}.biz-body{font-size:10px;line-height:1.45}.hook{background:linear-gradient(135deg,#2b2b2b,#1a1a1a);color:#fff;padding:11px 20px;flex-shrink:1;min-height:0}.hook .q{font-size:9.5px;color:var(--yellow);font-weight:700;letter-spacing:1.5px;margin-bottom:5px}.insight{font-size:10.5px;line-height:1.5;font-weight:500}.insight b{color:var(--yellow)}.foot{padding:6px 20px;display:flex;justify-content:space-between;background:#fafafa;flex-shrink:0}.foot span{font-size:8.5px;color:var(--dim)}
"""


def render_card(item: dict) -> None:
    rows = "".join(
        f'<div class="row"><span class="old">{html.escape(old)}</span><span class="arrow">➜</span><span class="new">{html.escape(new)}</span></div>'
        for old, new in item["rows"]
    )
    nums = "".join(
        f'<div class="n"><div class="big">{html.escape(big)}</div><div class="lb">{html.escape(label)}</div></div>'
        for big, label in item["nums"]
    )
    doc = f'''<!doctype html><html lang="zh"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><style>{CSS}</style></head><body><div class="card">
<div class="hero"><span class="badge">PH 每日榜 #{item['rank']} · 👍 0</span><div class="title-row"><div class="logo">{item['icon']}</div><h1>{html.escape(item['name'])}</h1></div><div class="sub">{html.escape(item['sub'])}</div></div>
<div class="pain"><div class="tag">⚠️ 痛点锚</div><div class="case">{html.escape(item['pain'])}</div></div><div class="mid">
<div class="block"><div class="tagline"><span class="dot">📱</span>它干嘛的</div><div class="body">{html.escape(item['what'])}</div></div>
<div class="vs"><div class="lbl">🎯 凭什么是它</div>{rows}</div>
<div class="duo"><div class="col cap"><div class="tagline"><span class="dot">💰</span>验证信号</div><div class="nums">{nums}</div><div class="dim-line">{html.escape(item['capline'])}</div></div><div class="col biz"><div class="tagline"><span class="dot">💵</span>怎么赚钱</div><div class="biz-body">{item['biz']}</div></div></div>
<div class="hook"><div class="q">▌ 🪝 PM 视角</div><div class="insight">{item['hook']}</div></div></div>
<div class="foot"><span>来源：Product Hunt 每日榜</span><span>{DATE}</span></div></div></body></html>'''
    temp = Path(f"/tmp/ph-xhs-{item['slug']}.html")
    temp.write_text(doc, encoding="utf-8")
    target = OUT / f"{item['rank']:02d}-{item['slug']}.png"
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=4", "--window-size=375,500", "--default-background-color=00000000", f"--screenshot={target}", temp.as_uri()]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=45)
        print(target)
    finally:
        temp.unlink(missing_ok=True)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for product in PRODUCTS:
        render_card(product)


if __name__ == "__main__":
    main()
