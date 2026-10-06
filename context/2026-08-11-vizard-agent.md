---
product: "Vizard Agent"
slug: "vizard-agent"
date: "2026-08-11"
rank: 5
votes: 0
comments: 1

category: "AI agent / 消费级应用"
subcategory: "视频 AI agent"
tags: ["video AGI", "AI 剪辑", "视频生成", "本地化翻译", "唇形同步", "对话式 agent", "Freemium", "Vizard"]

tech_stack: []  # 未披露
platform: ["Web"]
open_source: false
license: ""

business_model: "Freemium（Vizard 主站 credits 制，Agent 单独定价未披露）"
pricing_start: "免费层可用（具体 Agent 起步价未披露）"
funding_stage: "未披露"
funding_amount: ""

related_products: ["Vizard (vizard.ai)", "OpusClip", "Jupitrr AI", "VEED", "Augie Studio", "Visla", "Runway", "Pika", "Descript"]
maker_previous: ["Vizard (vizard.ai 长视频→短视频再利用工具)"]
archived_at: "2026-08-11"
sources_count: 5
---

# Vizard Agent · 扩展阅读上下文

> PT 2026-08-11 第 5 名 · 👍 0（早期快照） · 💬 1
> 归档日期 2026-08-11 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Vizard Agent |
| 英文 tagline | One AI agent for every kind of video |
| 中文 tagline | 一个 AI agent，搞定所有类型的视频 |
| 官网 | https://agent.vizard.ai |
| PH 页 | https://www.producthunt.com/products/vizard-agent-the-first-video-agi |
| 品类标签 | Productivity · Artificial Intelligence · Video（PH 标记为 "AI Video Editor"） |
| 票数 / 评论 | 0 / 1（早期快照） |
| 公司主体 | Vizard, Corp.（注册于美国特拉华州，与 vizard.ai 同一主体） |
| 企业版/关联站点 | vizard.ai（主站，长视频再利用工具）；agent.vizard.ai（Agent 子站）；vizard.ai/ai-studio（含 seedance-video-generator） |

## 是做什么的（如实复述，不评价）

Vizard Agent 是 Vizard, Corp. 推出的新产品线，官方自称"the first video AGI"（首个视频 AGI）。形态是一个**对话式 AI 视频代理**：用户用自然语言下指令，Agent 完成从输入到成品视频的全流程工作。

官方称其能力覆盖整个视频创作工作流——"from editing and generation to repurposing, localization, and revisions"（编辑、生成、再利用、本地化、修订）。接受的输入包括：原始素材、已有视频、URL、脚本、图片，或仅一个想法。创始人 Gary Zhang 在 PH 评论里把它类比成"Claude Code 之于程序员，Vizard Agent 之于视频"，并称团队用 6 个月构建"a full video editor that works like a human editor"（一个像人类剪辑师一样工作的完整视频编辑器）。

入口为 agent.vizard.ai，使用 Vizard 账号登录（PH 标注 "Free Options"）。落地页为 JS 渲染 SPA，WebFetch 仅能拿到标题与 tagline，正文能力清单无法静态抓取，下述能力以 PH 创始人评论与主站信息为准。

## 解决什么问题（事实层面，不判断值不值得解）

- 视频创作链路工具碎片化：剪辑、生成、再利用、翻译、字幕、唇形同步通常分属不同专业工具，学习成本与切换成本高。
- 传统剪辑软件门槛高：需操作时间线、理解剪辑语言；目标用户（内容营销人员、独立创作者）需更轻量的对话式入口。
- 长视频再利用到社媒短片的流程繁琐（Vizard 主站既已解决该细分场景，Agent 是对该能力的泛化扩展）。
- 本地化（翻译 + 唇形匹配）跨语言视频发布需求增长。

## 怎么做的（技术原理/机制，事实层面）

- **运行方式**：对话式 agent，用户给指令（含素材/URL/想法），Agent 自主规划并执行剪辑/生成/翻译/修订等步骤，产出成品视频。无需手动操作时间线。
- **能力清单**（据 PH 创始人评论）：
  - 剪辑（editing）
  - 生成（generation）
  - 再利用/长转短（repurposing）
  - 本地化（localization）
  - 唇形同步翻译（lip-sync translation）—— 例："Translate this into Spanish — and make my lips match"
  - 修订/局部修复（revisions）—— 例："The logo on my shirt is wrong in this shot. Fix it"
  - 从 URL/脚本/想法生成广告片 —— 例："Make a 30-second ad for my product — here's my website"
- **差异化声明**：官方称用一个 agent 替代多个专用工具（对位 OpusClip/VEED/Visla 等单点产品）。
- **技术栈**：未披露。落地页与主站均未列出底层模型或框架；主站提到主产品使用"语音与图像识别等先进技术"，但未点名具体模型/API。
- **误报/失败处理**：未披露。
- **"first video AGI" 声明依据**：官方自称，未见第三方背书或技术基准。PH 产品页 slug 含 "the-first-video-agi"，但页面无对该声明的论证性说明。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Gary Zhang（Vizard 创始人） | PH 产品页 maker comment |
| 团队成员 | Gary Zhang、Wenqi、Charlie X（PH 团队字段共 3 人） | PH 产品页 |
| 公司主体 | Vizard, Corp.，注册于美国特拉华州 | vizard.ai/about |
| 融资 | 未披露 | 主站/PH/公开搜索均未查到 |
| 投资方 | 未查到 | — |
| 加速器 | 未查到 | — |
| 合规认证 | 未查到 | — |

## 定价 / 商业模式

- **Vizard Agent 本身**：PH 标注 "Free Options"。Agent 子站定价单独页未抓到（SPA 渲染），是否沿用主站 credits 制待补。
- **Vizard 主站定价**（vizard.ai/pricing，同主体，可作参照）：
  - **Free**：$0，60 credits/月，720p 导出，3 天存储，上传 60min/1GB/1080p，1 个社媒账号。
  - **Creator**（最受欢迎）：动态滑块定价（年付 50% off，具体美元金额静态页未显示）；600–6,200 credits/月起；4K 导出、无水印、100GB 存储、6 个社媒账号、调度发布、AI 字幕/翻译/AI clipping/auto reframe/AI B-rolls。
  - **Business**：共享工作区，20 个社媒账号，无限存储，团队席位 $0/seat，品牌 kit/模板/自定义字体。
  - 1 credit = 1 分钟视频。自动续费。
- **模式**：Freemium + credits 用量计费 + 年/月订阅。

## 关联信息 / 生态

- **与旧 Vizard 的关系**：同一公司主体（Vizard, Corp.）。旧 Vizard（vizard.ai 主站）定位为长视频→社媒短片的再利用工具，2018 年起面向内容营销人员；Vizard Agent（2026 上线，主站导航标 "NEW"）是更高层的 agent 产品线，覆盖剪辑/生成/翻译/修订全流程，主站是其在再利用细分场景的能力子集。
- **PH 列出的相似产品**：Jupitrr AI、OpusClip、VEED、Augie Studio、Visla。
- **同类空间（扩展）**：Runway、Pika（生成）；Descript（对话式剪辑）；十一 lab / HeyGen（数字人/翻译唇形）。
- **主站曾获 PH 早期榜单徽章**（post ID 427451，tagline "Repurpose any long video into 10 viral shorts instantly"）。
- **生态**：主站提供 API（free 1/min·10/hour；Creator 3/min·20/hour；Business 10/min·60/hour）。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| （主站早期，日期未披露） | Vizard 长视频再利用工具上线，曾登 PH 榜单 |
| 2026（PH 标 "Launching today"，maker comment 标 "7d ago"） | Vizard Agent 上线，6 个月构建期 |

> 主站/about 未列里程碑时间线，以上为可从 PH 与主站推断的全部节点。

## 评论区反馈（事实摘录，不评价）

- 仅有创始人 Gary Zhang 一条 maker comment（社区评论数为 0，"Login to comment"）：
  - 强调 6 个月构建、对话式入口、类 Claude Code 的定位类比。
  - 列出三条示例指令（30 秒广告片 / 西班牙语唇形同步翻译 / 局部 logo 修复）。
  - 邀请反馈："I read every message myself, and the next version will be built on what you say."

## 信息来源

- PH 产品页：https://www.producthunt.com/products/vizard-agent-the-first-video-agi（拿到了描述、maker comment、能力示例指令、团队 3 人、Free Options 标注、相似产品列表）
- 官网 agent.vizard.ai：https://agent.vizard.ai（301 重定向自 PH 跳转链接；落地页为 SPA，仅拿到标题 "Vizard Agent — The First Video AGI" 与 tagline "One AI, Every Video Job"，正文能力/定价未静态渲染）
- vizard.ai/about：https://vizard.ai/about（拿到公司主体 Vizard, Corp.、特拉华注册、主产品定位、Vizard Agent 在导航中标 NEW）
- vizard.ai/pricing：https://vizard.ai/pricing（拿到主站 Free/Creator/Business 三档定价与 credits/API 限速；Agent 单独定价未单独披露）
- GitHub：无公开官方仓库（搜 "vizard agent"/"vizard video" 仅第三方无关项目，如 enisaras/vizard 数据可视化、kirat11X 的 Vizard 副本实现，均非官方）
- 公开报道/融资：WebSearch 未返回有效结果（工具返回异常会话，未拿到 crunchbase/新闻条目）

## 未查到 / 待补

- **融资**：阶段、金额、投资方、加速器均未查到。主站/about 不披露，公开搜索无结果。
- **技术栈**：底层模型（自研/调 GPT-4o/Runway/自训?）、框架、是否开源均未披露。
- **Agent 单独定价**：agent.vizard.ai 落地页为 SPA，WebFetch 拿不到正文；是否沿用主站 credits 制、是否有独立付费墙，待补。
- **"first video AGI" 第三方背书**：未见任何基准测试或独立评测，仅为官方自称。
- **创始人 Gary Zhang 背景**：过往履历、学历、其他项目未查到。
- **准确率/性能基准**：未披露任何量化指标（剪辑准确率、唇形同步质量分、生成时长等）。
- **里程碑时间线**：主站未提供 dated timeline，仅有 PH "Launching today" 标记与 maker comment "6 months building" 的相对时间。
- **GitHub**：无官方公开仓库。
