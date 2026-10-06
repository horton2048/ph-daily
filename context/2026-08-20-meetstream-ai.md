---
product: "MeetStream AI"
slug: "meetstream-ai"
date: "2026-08-20"
rank: 5
votes: 125
comments: 12

category: "AI agent"
subcategory: "会议智能体基础设施"
tags: ["API", "基础设施", "BYO 模型", "Zoom", "Google Meet", "Teams", "语音智能体", "会议机器人"]

tech_stack: ["统一会议 API", "MIA（MeetStream Infrastructure Agents）", "BYO STT/LLM/TTS 编排"]
platform: ["API（面向开发者）"]
open_source: false
license: ""

business_model: "按 meeting minute / 订阅（基础设施类典型）"
pricing_start: "未披露（PH 上未给出定价表）"
funding_stage: "未披露"
funding_amount: ""

related_products: ["Recall.ai", "Read AI", "Otter.ai", "Tactiq", "Fathom", "VAPI", "Retell AI"]
maker_previous: []

key_signals:
  - "两位 co-founder：Sidhdharth Sivasubramanian（CEO）+ Navaneeth Jawahar（CTO）"
  - "2nd PH launch，30+ AI 产品在生产中用其作为底层基础设施"
  - "BYO models（Deepgram/AssemblyAI/OpenAI/Gemini/ElevenLabs/Sarvam），MIA 把 bot 加入会议 + 智能体发言放在一个系统里"

archived_at: "2026-08-21T10:00+08:00"
sources_count: 2
---

# MeetStream AI · 扩展阅读上下文

> PT 2026-08-20 Product Hunt 榜单第 5 · 👍 125 · 💬 12  
> 归档日期 2026-08-21 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | MeetStream AI |
| 英文 tagline | Unified API & Infra for AI Meeting Agents |
| 中文 tagline | AI会议智能体的统一API与基础设施 |
| 官网 | https://meetstream.ai |
| PH 页 | https://www.producthunt.com/products/meetstream-ai |
| 品类标签 | API · Meetings · Developer Tools |
| 票数 / 评论 | 125 / 12 |
| 公司主体 | meetstream.ai |
| 关联站点 | — |

## 是做什么的（如实复述，不评价）

MeetStream AI 给做 AI 产品的团队提供"会议智能体基础设施"——让第三方开发者能用**一个统一 API** 把 AI 智能体接入 Zoom / Google Meet / Microsoft Teams，让智能体**作为真实参会人**加入会议，能听、能说、能调用工具。

定位是 **developer-facing infrastructure**（不直接卖给终端用户），不是会议笔记产品。

## 解决什么问题（事实层面，不判断值不值得解）

- 当前大部分"语音智能体进会议"方案是 3 家供应商拼接：会议 bot API + 语音平台 + 桥接 widget/iframe——三个集成、三份账单、三套 license，延迟在每一跳叠加
- Zoom CEO 公开表示想派"数字孪生"去开会，Microsoft 把 Teams 重组为"人 + 智能体团队"——会议正从"人类专属空间"变成"人 + 智能体"空间
- Gartner 预测：到 2026 年底，企业应用里 40% 会内置任务型智能体（vs 2025 年不到 5%）——会议基础设施需求侧在爆发

## 怎么做的（技术原理/机制，事实层面）

- **统一捕获引擎**：一个 API 实时输出 50+ 数据点（per-participant 音视频、live transcript + speaker attribution、参与者事件、完整会议 lifecycle via webhook），覆盖 Zoom / Meet / Teams
- **MIA（MeetStream Infrastructure Agents）**：让 bot 加入会议和让智能体在会议中说话**共用一套系统**——不是拼接多家
- **BYO models**：STT / LLM / TTS 都可插拔。STT 接 Deepgram、AssemblyAI；LLM 接 OpenAI、Gemini；TTS 接 ElevenLabs、Sarvam
- **会议发言控制**：内置 VAD（voice activity detection）、可调"wake up word"、可调"listening window"——解决多人会议里智能体何时该说话的 turn-taking 问题

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| Co-founder #1 | Sidhdharth Sivasubramanian（CEO/Maker） | PH 评论 |
| Co-founder #2 | Navaneeth Jawahar（CTO/Maker） | PH 评论 |
| PH 历史 | 第 2 次上 Product Hunt（2nd launch） | PH 评论 |
| 当前规模 | 30+ AI 产品在生产中使用 MeetStream | PH 评论 |
| 融资 | 未在公开 PH 帖子中披露 | — |

## 定价 / 商业模式

PH 上未公布具体定价表。基础设施类典型定价模式：免费试用层 + 按 meeting minute + Enterprise 合同。本次未抓到精确数字。

## 关联信息 / 生态

- 客户场景：CRM（自动 log sales call）、ATS（自动 interview 转录评分）、医疗（ambient clinical documentation / SOAP notes）、销售辅导、HR Tech
- 对比/竞品：
  - 会议 bot 基础设施：Recall.ai
  - 会议智能产品：Read AI、Otter.ai、Tactiq、Fathom
  - 语音智能体平台：VAPI、Retell AI

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 早期 | Private beta，只对小范围团队开放 |
| 2026-08-20 | 第 2 次 PH 上线，正式开放给所有人（无 waitlist、无 sales call） |

## 评论区反馈（事实摘录，不评价）

- **Kamal Sharma（7h）**：问智能体发言时怎么处理多人同时说话和 turn-taking
  - **Sidhdharth 回复**：内置 VAD 系统可调；额外提供 Wake Up Word、Listening Window 等控制
- **Sidhdharth 补充**：上述控制可在 dashboard 配置，也支持 API 配置
- **Navaneeth（CTO）** 单独发长评论解释架构：MIA 把 bot 加入会议和智能体说话放在**同一个系统**里，不是拼接多家

## 信息来源

- PH 产品页 + 创始人长评论：https://www.producthunt.com/products/meetstream-ai（拿到创始人、定位、机制、BYO models 清单、客户数）
- 通用类目级 WebSearch 摘要（参考会议基础设施品类信息）
- GitHub：无公开仓库

## 未查到 / 待补

- 具体定价表 / meeting minute 价格
- 投资方和融资金额
- 团队规模和注册地