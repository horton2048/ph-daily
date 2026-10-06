---
product: "Clipwing Autopilot"
slug: "clipwing-autopilot"
date: "2026-08-18"
rank: 9
votes: 105
comments: 18

category: "消费级应用 / SaaS"
subcategory: "短视频剪辑与内容生产服务"
tags: ["Video Clipping", "Short-form Video", "AI + Human Editor", "Content Repurposing", "Subscription", "Podcasting Tools", "Social Media Marketing"]

tech_stack: ["Deepgram", "Convex", "Coolify"]
platform: ["Web"]
open_source: false
license: ""

business_model: "订阅制 + 一次性买断（混合：SaaS 工具 + 产品化服务）"
pricing_start: "$24.99（一次性测试视频）/ SaaS 编辑器免费层 $0"
funding_stage: "未披露"
funding_amount: ""

related_products: ["Opus Clip", "Vizard", "Submagic", "Dumme", "10LevelUp", "FrameTomato"]
maker_previous: ["Clipwing（2024 首版，PH #1 POTD）"]

key_signals: [
  "Autopilot 三段式工作流：AI 找moment + 内容团队人工 review + 专业剪辑师出片，明确对标「AI slop」与「雇佣麻烦」两端",
  "母产品 Clipwing 2024-05-10 首发即拿 PH #1 POTD / #5 POTW；本次为同一品牌的二次升级发布",
  "技术栈：Deepgram（语音转写）+ Convex（后端）+ Coolify（自托管）",
  "Studio 服务档起价 $2,999.99/月、$3,999.99/月、Custom 三档，5 天交付、一次一个 request；另设 $24.99 一次性测试视频"
]

archived_at: "2026-08-18"
sources_count: 4
---

# Clipwing Autopilot · 扩展阅读上下文

> PT 2026-08-18 Product Hunt 榜单第 9 名 · 👍 105 · 💬 18
> 归档日期 2026-08-18 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Clipwing Autopilot |
| 英文 tagline | Get your clips without AI slop or hiring hassle |
| 中文 tagline | 拿到你的短视频切片，没有 AI 粗制滥造，也不必折腾雇人 |
| 官网 | https://clipwing.pro |
| Autopilot 落地页 | https://clipwing.pro/autopilot |
| PH 页 | https://www.producthunt.com/products/clipwing |
| X / Twitter | @clip_wing（https://x.com/clip_wing） |
| 品类标签 | Social Media · Social media marketing · Video（PH topics 另含 Video Editing / Podcasting Tools / Prompt Engineering Tools） |
| 票数 / 评论 | 105 票 / 18 评论 |
| 公司主体 | Clipwing（品牌），具体法律实体未查到 |
| 企业版/关联站点 | clipwing.pro 主站 + /autopilot 服务页 + /pricing 定价页 |
| PH 粉丝 / 评分 | 699 followers / 5.0 评分（1 条 review） |

## 是做什么的（如实复述，不评价）

Clipwing Autopilot 是 Clipwing 品牌在 2026 年推出的升级形态，把原来"长视频→短视频切片"的 SaaS 工具升级为一个端到端的"产品化剪辑服务"。用户上传一段长视频（播客、访谈、教学等长内容）、选择剪辑风格，平台交付可直接发布的成片切片。

核心工作流分三段（maker 主帖原文）：
1. **AI moment-finding**：AI 用"在真实客户视频上测试过的 prompt"自动找切片点。
2. **Human review**：内部 content team 人工 review 并改进 AI 给出的切片想法。
3. **Professional editing**：专业剪辑师把想法做成最终成片。

平台侧功能：在 board 上追踪切片、在视频上留评论、review/approve 剪辑、调度发布、把一条长视频延展成数周内容。官网 tagline 写"Smarter than an AI clipper, easier than hiring"——明确把自己定位在"纯 AI 切片器"和"自己雇剪辑师"两个极端中间。

SaaS 工具层（原 Clipwing 编辑器）仍独立存在：基于转录文本高亮选句即可生成切片、自动字幕、动画字高亮、可调字幕样式、自定义背景与品牌，导出 720p/1080p 短视频。

## 解决什么问题（事实层面，不判断值不值得解）

- 切片仍然"too much work"：maker 主帖原文"creating clips still takes too much work"，列举痛点为需雇佣剪辑师、跨 Slack / Google Drive 反馈、来回修订。
- 纯 AI 切片器输出质量差：被定义为"AI slop"，Autopilot 用"AI + 人工 content team + 专业剪辑师"三段流程规避。
- 雇佣管理剪辑师成本高：Studio 全服务档起步 $2,999.99/月，对应"dedicated pro editor"模式，目标客户为 startups / creators / tech companies。
- 目标场景：把一条长视频延展成"weeks of content"，跨 TikTok / Reels / Shorts 分发。

## 怎么做的（技术原理/机制，事实层面）

- **三段流水线**：AI moment-finding（用真实客户视频测试过的 prompt 库）→ content team 人工 review 切片想法 → professional editor 出最终成片。
- **平台协作层**：clip board 任务追踪、视频内评论、review/approve 编辑版本、调度发布。
- **底层 SaaS 工具**：基于 Deepgram 转写 → 文本高亮选段生成切片 → 自动字幕 + 动画 word highlighting（karaoke 式）→ 自定义字幕样式/品牌背景 → 导出。
- **技术栈**（PH "Built with" 字段）：Deepgram（语音转写）、Convex（后端平台）、Coolify（自托管 PaaS）。
- **未披露**：AI 找 moment 用的具体模型、prompt 库内容、人工团队规模与地理位置、内部协作工具。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 主 Maker | Lera Kuntsevich（@lera_kuntsevich1） | PH 产品页 maker 主帖 |
| 联合 Maker | Igor Krasnik（@igorkrasnik） | PH 产品页 launch team |
| Hunter | 未单独列出（maker 自发） | PH 产品页 |
| 团队规模 | 内部 content team + professional editors，具体人数未披露 | maker 主帖提及角色，无数字 |
| 过往产品 | Clipwing 首版（2024-05-10 上线 PH，当日 #1 POTD、当周 #5 POTW） | PH 产品页 badges |
| 融资 | 未披露 | 官网无融资信息 |
| 投资方 | 未查到 | — |
| 加速器 | 未查到 | — |
| 合规认证 | 未提及 | — |
| 规模声明 | ">1000 clips were created"（主站文案） | 官网 |

## 定价 / 商业模式

混合模式：SaaS 工具订阅 + 产品化服务订阅 + 一次性测试。

### SaaS 编辑器（自助用）

| 档位 | 价格 | 关键限制 |
|---|---|---|
| Free | $0 | 1 video hour/月、最多 3 次导出、720p、7 天存储、带水印 |
| Pro | $29.99/月 | 20 video hours/月、无限导出、1080p、无水印 |

### Studio 产品化服务（人工剪辑）

| 档位 | 价格 | 关键差异 |
|---|---|---|
| Studio Pro | $2,999.99/月 | 每次 request 3 条 short-form 视频、切片 moment 识别、自定义品牌、Slack 团队群 |
| Studio Advanced | $3,999.99/月 | Pro 全部 + 完整长版 episode（视频+音频）、YouTube 封面设计、文字素材（摘要/timecodes） |
| Studio Full-time | 定制 | 专属 pro video editor，需预约 call |

- **通用条款**：One request at a time、5 天交付。
- **测试包**：$24.99 一次性，可先要求一条测试视频再决定是否订阅。
- **Autopilot 专项**：PH 页标"Free Options"+ "$600 off" launch tag，但 /autopilot 落地页与 /pricing 页未单独列出 Autopilot 的具体订阅金额。"$600 off" 应为首发限时折扣，原始订阅价未在公开页查到。
- **免费层**：SaaS 编辑器可"try for free"，无信用卡。

## 关联信息 / 生态

- **对标定位**：tagline 直接对标两端——纯 AI clipper（Opus Clip / Vizard / Dumme / Submagic 一类）与"自己雇剪辑师"。Autopilot 主打中间地带。
- **PH 相似产品**：Video Editing / Podcasting Tools 同类（PH 自动列出，未逐项抓取）。
- **客户证言**：主站引用 Stephan Schott、John O'Nolan、Joao Aguiam 的推文，定位为"community of our creators"，但具体合作内容未详。
- **演化路径**：2 年前首版 Clipwing 是简单文本高亮切片工具 → 已"grown into a video studio"，服务 startups / creators / tech companies。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2024-05-10 | Clipwing 首版上线 Product Hunt，当日 #1 Product of the Day、当周 #5 Product of the Week |
| 2024–2026 | 从单一切片工具扩展为 video studio，增加 content team + professional editor 服务 |
| 2026-07-29 | 主站发布日期标注（UTC 18:52） |
| 2026-08-18 | Clipwing Autopilot 上线 Product Hunt，当日第 9 名（105 票 / 18 评论） |

更早里程碑（首版 beta、首笔融资、团队扩张）官网未公开时间线，待补。

## 评论区反馈（事实摘录，不评价）

- **Lera Kuntsevich**（maker 主帖）：回顾 2 年前首版 Clipwing → 现已"grown into a video studio"，服务 startups/creators/tech companies；介绍三段式流程；强调"upload one long video, choose your style, get ready-to-post clips"。
- **Igor Krasnik**（launch team）：祝贺 Lera，"great to see how your story evolves"。
- **João Aguiam**（reviewer）：称赞极简——"You select the sentences you want to have in your clip and that's it"（针对 SaaS 编辑器层）。
- **Karan Arora**：注意到"product → service → product"演化路径，称"going to be a beast for creators by a creator"。
- **Artyom Shimanski**：感慨两年从"small clipping tool to this"的演化。
- **Ilias Ism**：表达对"productized service + agency-ish work"在 AI 时代模式的兴奋。
- **Rotimi Best**：热情支持，"Clipwing just keeps getting better"。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/clipwing — 拿到 tagline、maker 主帖（三段式流程）、2 位 maker（Lera Kuntsevich / Igor Krasnik）、topics、Built with（Deepgram/Convex/Coolify）、699 followers / 5.0 评分、105 票 / 18 评论、社区评论摘录、"$600 off" + "Free Options" launch tag、原 2024 上线 #1 POTD/#5 POTW badges。
- 官网主站：https://clipwing.pro — 拿到 SaaS 编辑器机制（文本高亮切片、Deepgram 转写、字幕动画、自定义品牌）、">1000 clips created"、客户推文引用、主站发布日期 2026-07-29。
- 官网定价页：https://clipwing.pro/pricing — 拿到 Studio Pro $2,999.99/月、Studio Advanced $3,999.99/月、Studio Full-time Custom、$24.99 测试视频、5 天交付、One request at a time；Autopilot 专项定价未在定价页列出。
- Autopilot 落地页：https://clipwing.pro/autopilot — 仅拿到 tagline "Smarter than an AI clipper, easier than hiring"，无更多详情。
- GitHub：未见开源信号，未查 GitHub。
- WebSearch：补充 Lera Kuntsevich / Igor Krasnik 背景、Autopilot 订阅价（搜索结果提到 $600/年但未独立核实，未写入正文）。

## 未查到 / 待补

- Autopilot 专项订阅金额：PH 页仅"$600 off"折扣，独立订阅价未在 /autopilot 或 /pricing 公开，待补。
- 公司法律实体名称、注册地：未查到。
- 团队规模（content team / professional editors 人数、地理位置）：未披露。
- 融资阶段、金额、投资方：未披露。
- AI moment-finding 使用的具体模型与 prompt 库内容：未披露。
- Lera Kuntsevich 与 Igor Krasnik 的过往履历、LinkedIn 关联：未独立核实。
- WebSearch 提示 Autopilot "约 $600/年"的数字未在官网验证，本次不写入正文，待用户复核。
