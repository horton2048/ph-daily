#!/usr/bin/env python3
"""Generate the 2026-08-09 Product Hunt XHS cards (10 张).

用法: python3 scripts/generate_0809.py
渲染: Google Chrome headless 截图 375x500 @4x。
"""
from __future__ import annotations

import html
import subprocess
from pathlib import Path

DATE = "2026-08-09"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "xhs" / DATE
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# PRODUCTS 由 research 填充。每项字段:
# rank, slug, icon, name, votes, sub, pain, what, rows[(old,new)x3],
# nums[(big,label)x4], capline, biz, hook
PRODUCTS: list[dict] = [
    {
        "rank": 1, "slug": "omniwork", "icon": "🐾", "name": "Omniwork", "votes": 275,
        "sub": "桌面创意智能体操作系统",
        "pain": "内容创作者每天在选题、写作、剪辑、发布、复盘之间反复横跳，工具碎片化让创意时间被运营琐事吞掉。",
        "what": "常驻桌面的 AI agent 工作空间，由研究、写作、视觉等专业智能体协作跑通从选题到发布的全流程。桌面宠物伴侣实时推送 working/done/error 状态，agent 会记住你的品味和历史项目。",
        "rows": [("手动查热点找选题再分发", "agent 监测趋势并协调多智能体接力"), ("开多个 SaaS 反复切标签", "一个桌面工作空间端到端"), ("每次重喂背景与风格", "记忆系统沉淀品味越用越懂")],
        "nums": [("275", "PH 票数"), ("373", "PH 关注者"), ("4", "宠物状态"), ("100", "首批 credits")],
        "capline": "Zac Zuo、Zoey Chen、Finn Ding 三人小队；融资未披露",
        "biz": "<b>credits 积分制</b>，有免费额度，订阅付费；PH 首订 8 折码，首批邀请码额外送 100 credits，具体档位未披露。",
        "hook": "把 agent 从浏览器对话框升级成 <b>常驻桌面 OS</b>，用「桌面宠物」轻状态层降低信任成本——创意工作流的护城河不是模型，而是 <b>记忆+常驻触达</b>。",
    },
    {
        "rank": 2, "slug": "solouno", "icon": "🌱", "name": "SoloUno", "votes": 203,
        "sub": "游戏化戒掉拔毛咬甲抠皮肤",
        "pain": "拔头发、抠皮肤、咬指甲这类身体聚焦重复行为(BFRB)往往持续几十年，靠意志力「一刀切」戒断几乎都会复发，且伴随强烈羞耻感。",
        "what": "基于 HRT/CBT/ACT 疗法的游戏化自助 App，用每日小胜利替代「全有或全无」戒断目标。提供习惯日志、无习惯挑战与连胜、触发器分析、冲动接纳会话，逐步降低拔毛/咬甲/抠皮肤频率。",
        "rows": [("靠意志力「明天再也不拔」", "记每日无习惯连胜小步积累"), ("复发后陷入羞耻自责", "复盘触发器无羞耻接纳冲动"), ("行为记录散落脑子里", "一键日志+报表可视化趋势")],
        "nums": [("203", "PH 票数"), ("2周", "免费试用"), ("$7.99", "月费"), ("$59.99", "年费省37%")],
        "capline": "创始人 Omer Bialer 独立开发，本人患拔毛症多年；无融资，Bubble+Xano 无代码栈",
        "biz": "订阅制，<b>$7.99/月</b>、<b>$59.99/年</b>(省约37%)，均含 <b>2 周免费试用</b>；高级版解锁连胜/挑战/报告/冲动会话。",
        "hook": "<b>反戒断式设计</b>把目标从「永远不拔」拆成「今天不拔」，把 BFRB 典型的全有全无失败循环改造成可累积小赢；创始人即重度患者，<b>真人叙事</b>让信任成本极低。",
    },
    {
        "rank": 3, "slug": "voiceos-app-store", "icon": "🎙️", "name": "VoiceOS App Store", "votes": 203,
        "sub": "藏于灵动岛的语音原生应用商店",
        "pain": "想做个小工具得开 IDE、写代码、配环境，灵感凉了一半；做完想分享给朋友，还得走 TestFlight 那套繁琐流程。",
        "what": "一句话描述需求，当场生成可运行的语音原生 app，藏在 Mac/Windows 刘海凹槽里随时呼出。app 能编成链接发给任何人，对方点一下就装好并自动更新，底层 JSON 可手动或让 Claude/Codex 改。",
        "rows": [("写代码搭小工具立项到能跑半天", "说一句话 app 当场生成即用"), ("TestFlight 邀请签名一堆步骤", "发链接对方一键装好自动更新"), ("语音助手只能调固定技能", "用户自己造语音 app 装进刘海")],
        "nums": [("203", "PH 票数"), ("20k+", "声称用户"), ("10×", "宣称生产力倍数"), ("100", "听写语种")],
        "capline": "母公司 WakoAI，YC 孵化；联合创始人 Gabe Perez、Jonah Daian",
        "biz": "新账号 <b>7 天 Pro 试用</b>；免费档每周 25 次 Agent+100 次听写；Pro <b>$11.99/月(年付)</b>，无限用量；另有企业版与学生/Builder 半价。",
        "hook": "把 <b>应用分发</b> 从应用商店拉回到链接层，用刘海当常驻入口——把 Superhuman 那套快捷键肌肉记忆换成一句话造工具。赌注是 <b>语音原生 app 能否成为新品类</b>。",
    },
    {
        "rank": 4, "slug": "proxy-tester-by-scrapeops", "icon": "🛰️", "name": "Proxy Tester by ScrapeOps", "votes": 138,
        "sub": "按目标站点实测代理性能",
        "pain": "选代理全靠厂商营销文案，买完 credits 才发现自家目标站点被墙——折腾几天、烧掉预算才知道哪家用不了。",
        "what": "输入目标 URL，自动用 20+ 家代理服务商(住宅/机房/移动/反爬 API)真实请求该站点，测成功率、延迟、稳定性、带宽和单位成本，输出针对该具体目标的排名报告，而非厂商通用 benchmark。",
        "rows": [("买各家 credits 自己跑几天才出结论", "提交 URL 几分钟拿横向对比"), ("信厂商首页 99% 成功率", "看自己目标站点实测数据"), ("选定一家绑定长期合同", "按目标差异分别选最优组合")],
        "nums": [("20+", "对比代理服务商"), ("~100", "累计实测 API"), ("138", "PH 票数"), ("1k", "母站免费额度/月")],
        "capline": "Ian Kerins 与 Joe Kearney 联合创立，bootstrapped；Hiten Shah 助阵发布",
        "biz": "Proxy Tester 本身免费(获客漏斗)；导流母站 ScrapeOps 代理聚合 API，免费层 <b>1,000 credits/月</b>，付费按用量阶梯计费。",
        "hook": "把「选代理」这件重决策做成免费工具——<b>用实测数据替代营销话术</b>，既是流量入口也是母站信任锚，典型 <b>工具即获客</b> 路径。",
    },
    {
        "rank": 5, "slug": "agentconnect", "icon": "🏷️", "name": "AgentConnect", "votes": 131,
        "sub": "AI agent 跨平台协作开源中枢",
        "pain": "团队成员各自在终端跑 Claude Code 或 Codex，agent 成了「看不见的同事」——别人接不上手、上下文没法复用，跨 Slack/GitHub 协同更是无从谈起。",
        "what": "开源可自托管的多 agent 协作平台：在 Slack/Telegram/Discord/GitHub 里 @tag 任意 agent，统一配置角色、模型、工具、记忆与权限，agent 间还能互相交接。基于 ACP/MCP 协议，兼容 Claude Code、Codex、DeepSeek 等运行时。",
        "rows": [("本地跑 agent 互相看不到上下文", "@tag agent 在共享频道协作可见"), ("为每个平台单独写机器人", "一套配置接入四平台+1000+应用"), ("agent 没有角色和权限边界", "按角色配模型/工具/记忆/权限沙箱")],
        "nums": [("131", "PH 票数"), ("19", "GitHub★"), ("719", "提交次数"), ("Apache", "开源")],
        "capline": "三人小队 fmerian、Fuyao Zhao、Space Dragon；融资未披露",
        "biz": "核心 <b>Apache-2.0 开源自托管免费</b>；另提供 <b>Cloud 托管版</b>(候补内测)与 <b>Enterprise 私有部署</b>(SSO+专属支持)。",
        "hook": "押注 <b>ACP/MCP 开放协议</b> 做模型厂商中立的「agent 即同事」中间件，方向正确；但 GitHub★仅 19、社区冷启动是最大风险，能否跑通 <b>开发者生态</b> 决定生死。",
    },
    {
        "rank": 6, "slug": "docsalot-cli", "icon": "📚", "name": "DocsAlot CLI", "votes": 118,
        "sub": "让 AI 写好的草稿变成精美文档站",
        "pain": "Claude/Codex 生成的文档初稿散落在对话里，既不好看也难统一发布；产品一更新文档就过期，AI 检索也找不到。",
        "what": "面向 AI 编码 agent 的 CLI + 托管平台，让 Claude Code 或 Codex 用自然语言新建、拉取、更新文档并发布成精美站点。提供 hosted MCP、llms.txt、skill.md 让 agent 原生可调用，底层仍保留真实 CLI 供开发者接 CI。",
        "rows": [("手写 Markdown 丢进 GitBook 排版", "告诉 agent 改稿+预览+发布"), ("帮助中心/知识库/开发者文档三套", "统一一个文档源服务人和 AI"), ("发版后人工补变更文档", "agent 读 skill.md 自动同步")],
        "nums": [("118", "PH 票数"), ("$39", "Startup 月费"), ("3", "定价档位"), ("2", "PH 发射次数")],
        "capline": "创始人 Faizan Khan，成员 Haya Jawed；融资未披露",
        "biz": "SaaS 订阅制无免费档：<b>Startup $39/月</b>、<b>Team $99/月</b>、<b>Enterprise</b> 联系销售；CLI 经 npm 安装但需绑定工作区账号。",
        "hook": "护城河不是文档排版而是 <b>agent 原生可调用</b>：MCP+skill.md+llms.txt 把文档变成 AI 检索的「第一手数据源」，是 GitBook/Mintlify 没做的卡位；风险是定价偏高且依赖 Claude/Codex 生态。",
    },
    {
        "rank": 7, "slug": "prompt-golf", "icon": "⛳", "name": "Prompt Golf", "votes": 111,
        "sub": "把提示词工程玩成高尔夫",
        "pain": "学 prompt engineering 太枯燥，背一堆模板却没反馈。想练手却找不到能立刻打分、能看到别人怎么写得更短的地方。",
        "what": "竞技式 prompt 解谜游戏。每局 5 关，每关给一个目标词(如让 AI 输出 MANGO)和限制条件(禁用某些词、只能用 emoji)，用最少字符和消息数让 AI 输出目标，分数越低越好。带实时排行榜、回放、防作弊 transcript 审查。",
        "rows": [("看教程背模板学完就忘", "限制条件下现场拆解 AI 行为立刻打分"), ("刷算法题练手感", "刷 prompt 关卡练和 AI 对话的直觉"), ("公司 prompt 培训靠 PPT", "自托管应用让大家线上对战")],
        "nums": [("111", "PH 票数"), ("5", "每局关卡"), ("MIT", "开源"), ("0", "GitHub★")],
        "capline": "独立开发者 Jugal Mistry 个人作品；未披露融资",
        "biz": "完全 <b>免费开源(MIT)</b>，无付费层。纯 PHP+SQLite 可丢进任意 public_html 自托管，作者靠 Azure OpenAI 提供模型能力。",
        "hook": "把 prompt engineering 从 <b>技能培训</b> 重定义成 <b>竞技娱乐</b>，借高尔夫计分天然产生可比较的 leaderboard——冷启动社区最便宜的钩子。极简栈说明作者赌的是 <b>玩法而非技术</b>。",
    },
    {
        "rank": 8, "slug": "macrobite", "icon": "🍱", "name": "Macrobite", "votes": 108,
        "sub": "拍照即得宏量营养素分析",
        "pain": "增肌减脂的人都知道要记蛋白质、碳水、脂肪，但每顿饭翻数据库搜食物、选份量、一条条录入，坚持两周就放弃；要么快但记不准，要么准但太慢。",
        "what": "拍一张饭菜照片，AI 瞬间给出热量/蛋白质/碳水/脂肪估算，支持语音和 Siri 记录、条码扫描、保存常用餐食，还有 iPhone 小组件和 Apple Watch 快速查看。估计不准还能手动微调，不用翻数据库。",
        "rows": [("翻数据库搜食物选份量", "拍张照秒得宏量"), ("手动录入两周放弃", "语音/Siri 一句记"), ("到饭点忘了今天吃了多少", "小组件实时看剩余")],
        "nums": [("5.0", "App Store 评分"), ("108", "PH 票数"), ("$50", "年订阅"), ("2周", "免费试用")],
        "capline": "开发者 Alex Grzechowski + 顾问 Jeremy Toeman；融资未披露",
        "biz": "单一订阅 <b>$50/年</b>，下载免费但两周试用后必付费，无永久免费档；规划接入 Instacart 下单。",
        "hook": "痛点抓得准——<b>\"快\"和\"准\"二选一</b>是健身饮食 App 最大流失点，用 AI 照片识别绕开数据库搜索摩擦，但 <b>$50/年偏贵</b>，留存能否撑住订阅得看识别准确率。",
    },
    {
        "rank": 9, "slug": "argos", "icon": "🤖", "name": "Argos", "votes": 105,
        "sub": "浏览器内替你干活的 AI 代理",
        "pain": "你让 ChatGPT 帮你订机票、填报销单、整理邮件，它只能给你一步步操作指南，最后还得你自己手动点几十下；真正的浏览器任务从未真正自动化。",
        "what": "浏览器侧边栏里用你的已登录账户直接点击、输入、填表，完成真实任务；也能通过 Telegram/WhatsApp 远程指挥。集成 Gmail/Docs/Sheets，可连 GitHub/Slack/Notion，所有数据留在本地，破坏性操作需确认。",
        "rows": [("AI 给指南你手动点", "AI 直接替你执行"), ("切第三个 Tab 手填表单", "侧边栏/Telegram 下发任务"), ("账号密码传云端", "数据全留本地")],
        "nums": [("105", "PH 票数"), ("免费", "起步价"), ("Gmail", "原生集成"), ("本地", "数据存储")],
        "capline": "团队 Arystan Tanekov 与 Gleb Babichev；前身 Lyto 改名；融资未披露",
        "biz": "PH 标 <b>免费起步</b>，具体付费档位未披露；Claude 驱动 + 本地执行架构。",
        "hook": "浏览器自动化赛道多数做 RPA 脚本或云端 Agent，Argos 选了 <b>本地执行 + 用你的登录态</b> 这条最直接的路——但安全模型必须极强，一旦出事就是账号级事故，<b>信任成本是最大壁垒</b>。",
    },
    {
        "rank": 10, "slug": "duckdisk", "icon": "🖥️", "name": "DuckDisk", "votes": 100,
        "sub": "Mac 存储分析表格派开源工具",
        "pain": "Mac 磁盘满了要清理，用 DaisyDisk 之类的彩色圆图扫一圈，看到大块色块却不知道具体是哪个文件、分配了多少、文件类型分布；扫云盘还得单独装别的工具。",
        "what": "表格优先的 macOS 存储分析器，一眼看到目录大小、分配空间、占父目录百分比、文件数和类型统计；支持本地盘、OneDrive、Google Drive 和 SSH 服务器，云盘只读元数据不下载，删除前先入待审清单。",
        "rows": [("圆图看出大块不知具体文件", "表格树直达文件级"), ("本地/云盘/SSH 各装工具", "一个 App 全扫"), ("扫完直接删误删无救", "先入待审清单可撤")],
        "nums": [("29", "GitHub★"), ("AGPL", "开源"), ("$0", "完全免费"), ("v0.6", "最新版")],
        "capline": "开发者 puppypi（qiyang77）；Tauri+Rust+React 栈",
        "biz": "<b>完全免费开源</b>（AGPL-3.0），Mac App Store 与 GitHub Releases 双渠道，靠 Apple 公证签名。",
        "hook": "表格派在 Windows 一直有忠实用户，Mac 上却被 DaisyDisk 的圆图审美统治；DuckDisk 押注 <b>信息密度 > 视觉花哨</b>，顺手塞进云盘和 SSH——<b>开源免费是降维打击，但 29★说明冷启动还得靠口碑</b>。",
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
    votes = item.get("votes", "")
    doc = f'''<!doctype html><html lang="zh"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><style>{CSS}</style></head><body><div class="card">
<div class="hero"><span class="badge">PH 每日榜 #{item['rank']} · 👍 {votes}</span><div class="title-row"><div class="logo">{item['icon']}</div><h1>{html.escape(item['name'])}</h1></div><div class="sub">{html.escape(item['sub'])}</div></div>
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
