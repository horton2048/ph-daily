---
product: "Devin Voice"
slug: "devin-voice"
date: "2026-09-11"
rank: 8
votes: 106
comments: 1

category: "AI 编码代理 / 实时语音交互"
subcategory: "语音驱动的 AI 软件工程师前端"
tags: ["闭源", "Realtime Voice AI", "AI Coding Agent", "SWE-2", "GPT-Live", "Cognition", "Devin", "语音对话", "Cloud"]

tech_stack: ["GPT-Live（对话层）", "SWE-2（Coding 模型）", "WebRTC/实时音频栈（未披露细节）", "Devin Agent Runtime（Devin 既有后端）"]
platform: ["Web（docs.devin.ai）", "Devin Desktop（Mac/Win，Windsurf 改造版）", "Devin CLI", "Devin Fusion"]
open_source: false
license: "闭源商业产品（SWE-2 模型未开源，Devin Voice 为功能模块不开源）"

business_model: "SaaS 订阅 + 按 Agent Compute Unit (ACU) 计费；语音模式作为 Devin 能力开放给所有 Devin 用户"
pricing_start: "PH 标注 Free（对应 Devin 的 Free 入门档）；语音时长按 ACU 计费（具体单价待补）"
funding_stage: "晚期（公司层面 2026 年 8 月据报道在谈 400 亿美元估值融资）"
funding_amount: "公司累计融资未单独披露；最近一轮估值 ≥ $40B（2026-08 在谈）"

related_products: ["Devin（母公司核心产品）", "Devin Desktop（前身 Windsurf）", "Cursor", "Claude Code", "Codex 3.0", "Replit Agent", "Lovable", "Bolt.new", "Wispr Flow（语音输入维度类似）", "ChatGPT Voice Mode（实时语音对话维度）"]
maker_previous:
  - "KP (@thisiskp_) — Hunter，PH 主页标注关联 Netlify；其余履历待补"
  - "Walden Yan (@walden_yan) — Cognition 联合创始人 & CPO，IOI 金牌（公司三位创始人共 10 枚 IOI 金牌）"
  - "Neal Wu (@wuneal) — Cognition 团队，IOI 金牌，Scott Wu 兄弟"

key_signals:
  - "SWE-2 发布（2026-09-10）次日即上线 Voice——把'最强编码模型'和'实时语音前端'同日打包，是 Cognition 在 Devin 商业化加速期的关键发布节奏"
  - "对话层用 GPT-Live（非自研）——Cognition 选择外购实时语音方案，把自研精力集中在 coding 模型上，是典型的'用最好的轮子造自己的车'分工"
  - "SWE-2 基准 FrontierCode 1.1 Main 50.0%，距 Fable 5.1 仅 1 个百分点但便宜 64%——把'前沿编码模型'重新拉回'每美元产出'的性价比维度"
  - "语音模式定位是'当你离开键盘时的任务接力'——打字框仍可用、call 期间可在 Devin 内导航、转录文本存入会话历史，是给 Devin 加一个'语音通道'而非另起一个产品"
  - "母公司 2025-07 收购 Windsurf、2026-06 改名 Devin Desktop——Voice 是这条'整合后统一品牌'产品线的下一块拼图，不是独立创业项目"

archived_at: "2026-09-12"
sources_count: 5
---

# Devin Voice · 扩展阅读上下文

> PT 2026-09-11 Product Hunt 榜单第 8 · 👍 106 · 💬 1
> 归档日期 2026-09-12 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Devin Voice |
| 英文 tagline | You say it, Devin ships it |
| 中文 tagline | 你说出来，Devin 把它交付 |
| 母公司 | Cognition（Cognition AI Labs） |
| 官网/文档 | https://docs.devin.ai/work-with-devin/voice-mode |
| PH 产品页 | https://www.producthunt.com/products/devin-voice |
| PH 发帖页 | https://www.producthunt.com/posts/devin-voice |
| Hunter 发帖 | https://www.producthunt.com/r/4RQP6CHF5CGKTB |
| X 公告 | https://x.com/cognition/status/2098142686486356185（抓取被 X 反爬拦截，仅拿到链接） |
| 票数 / 评论 / 关注者 | 106 / 1 / 51（PH 抓取时不同源显示 106 或 108，以 archive/2026-09-11.md 为准 106） |
| 当日名次 | #8（Day Rank） |
| 标签 | Productivity · Developer Tools · Artificial Intelligence |
| 附加分类（PH 发帖页） | AI Engineer · Realtime Voice AI |
| 定价 | PH 标注 Free（Devin 整体按 ACU 计费，Voice 调用走 ACU 通道） |

## 是做什么的（如实复述，不评价）

给 Cognition 的 AI 软件工程师 **Devin** 加一个**实时语音通道**：用户对着 Devin 说话描述需求，Devin 边听边规划、编码、出活；用户也可以在 voice call 期间照常在 Devin 里浏览/导航、添加上下文。

技术分工两层：
- **对话层**：GPT-Live（OpenAI 的实时语音方案），负责把用户语音转成 Devin 能理解的任务流
- **编码层**：Cognition 自研的 **SWE-2**（2026-09-10 刚发布），负责软件工程工作——规划、改码、验证、交付

官方 hunter 评论原话："Cognition just gave Devin a landline. You talk through the task, and Devin plans, codes, and ships it."

## 解决什么问题（事实层面，不判断值不值得解）

- **离开键盘时的任务接力**：开车、走路、家里走动时无法打字，但任务已经在脑子里——语音通道让任务不卡在"找不到键盘"
- **边想边说的工作流**：口头描述比打字快，并且能保留"边说边澄清"的自然对话节奏（官方明示鼓励用户随时打断、追问、澄清）
- **已有的 Devin 任务上下文复用**：call 期间 Devin 内部可以正常导航、转录文本会自动存进 session 历史——用户回来能从文字版继续

## 怎么做的（技术原理 / 机制，事实层面）

公开材料只讲到三层协作，更细节的传输/中断策略未披露：

- **音频入口**：web 端在首页（Agent 模式）或已有 session 的消息框旁边点 voice call 按钮，浏览器请求麦克风权限；call 开始时消息框里已输入但未发送的文字会作为上下文一起送出
- **实时对话循环**：GPT-Live 负责语音 → 意图 → 语音回放；任务执行由 SWE-2 接管
- **可打断 / push-to-talk**：
  - Mute / Unmute（用户麦克风）
  - Hold Space（mute 时按住空格键 push-to-talk）
  - Silence / Unsilence Devin（只关 Devin 的语音输出，不影响用户麦克风）
  - End voice call（挂断）
- **并行性**：call 期间允许在 Devin 内导航，转录文本实时落入 session 历史（call 结束后仍可查阅）
- **可定制偏好**：用户可以口头要求"说话快点 / 慢点 / 别啰嗦"，偏好由 LLM 层实时响应（具体持久化策略未披露）

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 母公司 | Cognition（Cognition AI Labs / cognition.com） | Wikipedia + cognition.com |
| 成立 | 2023-08 | Wikipedia |
| 总部 | 美国旧金山 | Wikipedia |
| 创始团队 | Scott Wu（CEO）· Steven Hao（CTO）· Walden Yan（CPO） | Wikipedia |
| 创始团队履历亮点 | 三人均 IOI 金牌；公司早期 10 人团队累计 10 枚 IOI 金牌（包含 Neal Wu、Gennady Korotkevich、Andrew He 等） | Wikipedia |
| 团队规模 | 200 人（2026） | Wikipedia |
| 早期融资（2024 初） | $21M，Founders Fund（Peter Thiel）领投，估值 $350M | Wikipedia |
| A 轮（2024-04） | $175M，Founders Fund 领投，估值 $2B（独角兽） | Wikipedia |
| B 轮（2025-03） | 8VC（Joe Lonsdale）领投，估值 $4B | Wikipedia |
| Windsurf 收购（2025-07） | 收购 Windsurf（此前 Google 以 $2.4B 收走其 CEO 与高管团队），估值推至 $10B | Wikipedia |
| 2026-05 估值 | $26B | Wikipedia |
| 2026-08 报道 | 早期融资讨论，估值 ≥ $40B | Wikipedia |
| 关键人物近期动态 | 2026-09 工程师 Eric Lu 用 Devin 协作的 GPU 实现分解 RSA-260 | Wikipedia |
| PH 此处 maker | KP（@thisiskp_，Hunter，PH 主页关联 Netlify）· Walden Yan（@walden_yan，CPO）· Neal Wu（@wuneal） | PH 发帖页 makers |

## 定价 / 商业模式

- **PH 标注**：Free（指向 Devin 的免费入门档，voice 用量按调用时长折算成 ACU）
- **公司实际收费方式**：Devin 整体按 Agent Compute Unit (ACU) 计费，Voice 是 Devin 能力之一不单独定价（具体单价表未在本次抓取中拿到，cognition.com/pricing 与 docs.devin.ai/get-started/pricing 均返回 404/429）
- **ACU 含义**：把"LLM tokens / 计算时长 / 工具调用"打包成一个统一计量单位（Devin 自创的计费概念）
- **Voice 模式的成本结构**：用户语音→GPT-Live 转写/理解→任务执行交给 SWE-2（每一步都消耗 ACU）——长对话会显著放大成本

## 关联信息 / 生态

- **与母公司产品线关系**：Devin Voice 是 Devin 的语音通道，不是独立产品。Devin 现有四个入口：Desktop（前 Windsurf，2026-06 改名）/ CLI / Web / Fusion；Voice 在这些入口都能启用
- **与 Windsurf 的关系**：Cognition 2025-07 收购 Windsurf（彼时核心团队被 Google $2.4B 收走），2026-06 改名 Devin Desktop——Voice 是这条整合后产品线的下一块拼图
- **与 SWE-2 的关系**：SWE-2 是 Cognition 自研 coding 模型（2026-09-10 发布，Voice 是它的首个"对外 voice 通道"配套产品）。SWE-2 base 来自 Moonshot 的 Kimi K3（2.8T 参数），后训练在 SWE-1.7 的 RL 基础设施上
- **与 GPT-Live 的关系**：Cognition 没有自研实时语音 LLM，而是直接外购 GPT-Live 作为对话层——这和 SWE-2 自研形成"对话外购 + 编码自研"的清晰分工
- **竞品矩阵（PH 推荐位）**：
  - **编码 agent 维度**：Claude by Anthropic（5.0 · 987 reviews）· Cursor（5.0 · 942）· Claude Code（5.0 · 679）· Codex 3.0（5.0 · 85）· Replit / Lovable / Bolt.new（未列入 PH 推荐位但常被并列）
  - **语音输入维度**：Wispr Flow（4.7 · 78 reviews）——但 Wispr Flow 是"语音转文字写邮件/文档"，与 Devin Voice 的"语音驱动 agent 干工程活"目标不同
- **媒体露出**：PH Hunter KP 转发 Cognition 官方 X（@cognition）公告；SWE-2 在 cognition.com/blog/swe-2 详细技术博文（标题："How we trained SWE-2"）

## SWE-2 关键技术指标（与 Devin Voice 同周发布）

| 维度 | 数据 / 描述 |
|---|---|
| 发布日期 | 2026-09-10（Voice 发布前一天） |
| Base 模型 | Kimi K3（2.8T 参数，Moonshot AI），Cognition 做后训练 |
| 训练规模亮点 | 首次把 RL 推到"多 trillion 参数"规模 |
| Effort 档位 | medium / high / max（按本地 Pareto 斜率做线性 cost penalty） |
| FrontierCode 1.1 Main | 50.0%（距 Fable 5.1 的 50.9% 仅 1pt，便宜 64%） |
| DeepSWE 1.1 | 73.0%（榜首） |
| Terminal-Bench 2.1 | 92.8%（领先） |
| Terminal-Bench 4 | 27.3%（落后 GPT-6 Astra 的 57.9%） |
| 效率（vs SWE-1.7） | medium 档 58% 更少 steps（53 vs 127 mean），81% 更便宜 |
| 行为改进 | 首次编辑步数中位数 18（vs SWE-1.7 的 48）；更好的 test 覆盖；受阻时找替代路径；验证时重新推导而非复述结论 |
| 可信度评估 | 宣传/审查类 prompt 98.0% 通过率（英文 99.8% / 简体中文 95.2% / 繁体中文 99.1%）；上下文化诱导注入未引发显著脆弱性变化 |
| 关键 RL 技术 | NVFP4/FP8 推理 · 量化感知训练 · prefill delayer（10-20% 吞吐增益）· 在线 DSpark draft 模型训练 · 3 倍 RL 环境扩容 · flywheel 强化 verifier |
| 部署 | 当日上线 Devin Desktop + Devin CLI；Devin Web 与 Fusion 滚动推送 |

## 技术时间线

| 日期 | 事件 |
|---|---|
| 2023-08 | Cognition 成立（Scott Wu / Steven Hao / Walden Yan 联合创立） |
| 2024-03 | Devin AI demo 公开，"AI 软件工程师"概念出圈 |
| 2024-初 | $21M 融资，Founders Fund 领投，估值 $350M |
| 2024-04 | $175M 融资，估值 $2B，进入独角兽 |
| 2025-03 | 估值 $4B（8VC 领投） |
| 2025-07 | 收购 Windsurf（Google 收走其 CEO 后残部） |
| 2025-09 | Windsurf 收购后估值推至 $10B |
| 2026-05 | 估值 $26B |
| 2026-06 | Windsurf 改名 Devin Desktop（产品线统一） |
| 2026-08 | 早期融资讨论，估值 ≥ $40B |
| 2026-09 | 工程师 Eric Lu 用 Devin 协作 GPU 实现分解 RSA-260 |
| 2026-09-10 | SWE-2 模型发布（cognition.com/blog/swe-2） |
| 2026-09-11 | Devin Voice 上线 PH（#8，106 票，1 评论） |

## 评论区反馈（事实摘录，不评价）

PH 页评论数极少（1 条），仅 Hunter KP 一条猎人帖：

- **KP（Hunter，~18h ago）**："Excited to hunt Devin Voice today. Cognition just gave Devin a landline. You talk through the task, and Devin plans, codes, and ships it. The announce leans on GPT-Live for the conversation layer, with their new SWE-2 model doing the software engineering. Same day they also pushed SWE-2 as Cognition's latest coding model."
  - 链接：docs.devin.ai/work-with-devin/voice-mode · x.com/cognition/status/2098142686486356185 · cognition.com/blog/swe-2
  - 标签：Cognition · @walden_yan · @wuneal · Scott Wu · Devin team

> PH 投票用户评论几乎缺位（除 Hunter 帖外），本次未抓到任何独立用户的评论或质疑——可能与上线后不到 24 小时抓取有关，也可能与产品形态（现有 Devin 用户的"加量"而非"破圈"）有关。

## 信息来源

- **PH 产品页**：https://www.producthunt.com/products/devin-voice（拿到 tagline · 完整描述 · 票数/评论/关注者 · 6 张 gallery 图（无 alt） · 5 个类似产品 · maker 列表 · 链接）
- **PH 发帖页**：https://www.producthunt.com/posts/devin-voice（拿到发帖版描述 · 附加分类"AI Engineer / Realtime Voice AI" · Hunter KP 评论全文 · 关联 X/SWE-2 链接）
- **Devin Voice 官方文档**：https://docs.devin.ai/work-with-devin/voice-mode（拿到功能描述 · 启用方法 · call 期间控件 · 偏好定制方式）
- **Cognition SWE-2 博文**：https://cognition.com/blog/swe-2（拿到 SWE-2 模型细节 · 训练方法 · benchmarks · effort 档位 · 与 SWE-1.7 对比 · 可信度评估）
- **Wikipedia**：https://en.wikipedia.org/wiki/Cognition_AI（拿到公司成立时间 · 创始团队 · 历轮融资与估值 · Windsurf 收购 · Devin Desktop 改名 · RSA-260 事件）

## 未查到 / 待补

- **公司具体累计融资金额**：Wikipedia 只给估值不给累计金额
- **ACU 单价**：cognition.com/pricing 与 docs.devin.ai/get-started/pricing 均返回 404/429，本次未取回
- **Voice 模式的语言支持**：官方文档没明确列出支持语种；SWE-2 可信度测试覆盖英/简中/繁中，但 voice 通道是否同样未说明
- **Voice 模式的延迟规格**：端到端 P50/P99 latency 未披露
- **Voice 模式是否调用 ACP（Agent Compute Pricing）的额外溢价**：定价页未取到，无法判断语音时长是否比纯文本更贵
- **KP（@thisiskp_）的完整背景**：PH 主页只显示"associated with Netlify"，其余履历未抓到
- **Steven Hao（CTO）是否参与此次 PH 帖**：makers 列表只有 KP / Walden Yan / Neal Wu，未列 Steven Hao
- **Wispr Flow 类语音输入工具的对比数据**：Wispr Flow 是 PH 推荐位里的"语音类"产品，但定位（语音转文字 vs 语音驱动 agent）不同，未做横评
- **6 张 gallery 图的具体内容**：PH 抓取只给 CDN URL，无 alt/描述，无法判断截图展示什么场景
