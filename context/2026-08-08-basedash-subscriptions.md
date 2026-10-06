---
product: "Basedash"
slug: "basedash-subscriptions"
date: "2026-08-08"
rank: 2
votes: 0
comments: 1
category: "SaaS"
subcategory: "AI-native BI 平台"
tags: ["Business Intelligence", "AI", "No-code", "自然语言", "Semantic Layer", "MCP", "YC", "Self-hosted"]
tech_stack: ["TypeScript", "Python", "Snowflake", "BigQuery", "PostgreSQL", "MySQL", "GPT-5.6 (AI Kit 发布提及)"]
platform: ["Web", "Slack app", "MCP server", "Desktop app", "Embedding"]
open_source: false
license: ""
business_model: "订阅制（Startup 计划 + Enterprise 自定义）"
pricing_start: "$1,000/月 + AI usage（Startup 计划）"
funding_stage: "未查到具体轮次/金额（YC Summer 2020）"
funding_amount: ""
related_products: ["Tableau", "Looker", "Omni", "Hex", "Metabase", "Metabase"]
maker_previous: ["Max Musing：Basedash 创始人兼 CEO（YC S20 公司，2019/2020 年创办）"]
archived_at: "2026-08-08"
sources_count: 4
---

# Basedash Subscriptions · 扩展阅读上下文

> PT 2026-08-08 Product Hunt 榜单第 2 · 👍 未查到（archive 显示 0） · 💬 1  
> 归档日期 2026-08-08 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Basedash（本次发布的是子功能 "Basedash Subscriptions"） |
| 英文 tagline | Subscribe to any dashboard. Delivered on schedule.（PH 页当前文案） |
| 中文 tagline | 订阅任意 dashboard，按计划投递 |
| 官网 | https://www.basedash.com/ |
| PH 页 | https://www.producthunt.com/products/basedash |
| 品类标签 | Artificial Intelligence · Data & Analytics · Business Intelligence |
| 票数 / 评论 | PH 页面访问时未显示 upvote 数；archive 👍 0 / 💬 1；2.8K followers；5.0 星（9 条评论） |
| 公司主体 | Y Combinator Summer 2020 公司；多伦多（Toronto, Canada）；团队 6 人 |
| 企业版/关联站点 | GitHub org github.com/Basedash；基于 `baseda.sh/download` 的桌面 app；X @Basedash |

## 是做什么的（如实复述，不评价）

Basedash 是 AI-native BI 平台：自然语言连接数据、描述想要的可视化，AI 生成，无需 SQL。覆盖全数据栈——数据同步、语义层（可复用 SQL 指标）、BI 与报表。本次 Subscriptions 发布：把任意 dashboard 或 chart 订阅成定时快照，按计划投递到邮箱或 Slack 频道。创始人 Max Musing 评论："Nobody has manually posted a dashboard screenshot since."

官网功能面：AI 数据分析师、Dashboards、Warehouse（750+ 数据源）、Embedding、Insights（AI 每日数据简报）、Automations（AI 数据工作流）、MCP server（连任意 AI client 到数据）、Semantic layer。

## 解决什么问题（事实层面，不判断值不值得解）

- 传统 BI 依赖 SQL-heavy 工作流与手动建 dashboard。
- 业务用户想自助分析，但数据团队担心指标口径失控——官方价值主张："Every answer is computed from your governed metric definitions and shows the SQL behind it — so business users can self-serve without your data team losing sleep."
- 用户评论（PH 9 条 review 亮点）："speeding up analytics work, making data access conversational"、"我们的 #1 BI tool，建 dashboard 能力 5x"；批评点：定价偏高、缺 Firestore 支持、想要主动 insight 建议。
- Subscriptions 解决的问题：手动截图/发 dashboard 快照的重复劳动。

## 怎么做的（技术原理/机制，事实层面）

- 用户用自然语言提问，系统转成结构化查询并直接对已连接数据库/仓库执行校验（非自由生成答案）。
- 内置 semantic layer：指标定义为一次可复用的 SQL 定义，chat、charts、dashboards、insights、automations 共用。
- demo 工作流：agent 读指标定义 → 扫描数据目录 → 跑 Snowflake 查询 → 对账 Stripe → 建 dashboard，全程展示 SQL。
- 官方声明：客户数据不用于训练模型。
- 支持 750+ 数据源集成（PostgreSQL、MySQL、Snowflake、BigQuery、Salesforce、HubSpot、Stripe、Google Analytics 等）。
- 2026-07-23 AI Kit 发布标称 "powered by GPT-5.6"。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Max Musing（Founder & CEO） | YC 页面 |
| 团队 | 6 人；YC primary partner Gustaf Alstromer | YC 页面 |
| Launch team | Max Musing、Kristofer Lachance、Derek Reynolds | PH 页 |
| 成立 | YC 页面写 Founded 2020；PH 页写 launched 2019（两口径并存） | YC / PH |
| 融资 | 未查到具体轮次与金额（公开未见融资新闻） | — |
| 合规认证 | 官网口径：SOC 2 Type II、HIPAA、ISO 27001、GDPR（FAQ）；SOC 2 Type II 年度审计+持续监控 | 官网 |

## 定价 / 商业模式

官网 /pricing：
- Startup 计划：$1,000/月 + AI usage。含最多 25 用户（无单独 per-seat 费用）、750+ 数据源、$1,000/月 AI credits、Slack support、Basedash Warehouse、MCP server、Slack app、Automations、Insights。14 天免费试用、免信用卡。
- Enterprise 计划：自定义。含 self-hosting、Embedding、SSO、dedicated support、SCIM、audit logs、自定义 AI models、自定义用户数、VPC-oriented workflows。
- 每月 AI usage 有免费额度，超量在下一期账单计费；非营利折扣与企业采购可用。
- PH 页标 "Free Options"（Free Options 标签，非完全免费——按官网 CTA "Start free" 理解为试用）。

## 关联信息 / 生态

- 官网信任声明：BI Bench #1 most accurate AI analyst；"SOC 2, GDPR, HIPAA Compliance-ready"；200+ 公司客户。
- 客户 logo 墙：Exa、Tiger Data、Purpose、Gumloop、Composio、Fullscript、Shiftrx、Drata；客户引语来自 FullEnrich、Taxfyle。
- 对比页 vs Tableau / Looker / Omni / Hex / Metabase；FAQ 与 ChatGPT/Claude Code 类通用 AI 工具区分（"purpose-built for production analytics"）。
- GitHub 组织（56 followers）：非 fork 仓库 ClawReview（"Human review system for OpenClaw"）、utilities.dev、full-embed-demo、macindash、dockhunt（295★，最热）、self-hosted（41★）、dockhunt-cli（63★）；fork 了 radix-ui/primitives、airbyte、react-grid-layout。
- PH 历史发布（2026）：Audit Logs（8/1）、AI Kit（7/23）、Suggestions（7/17）、SCIM（7/11）。奖项：#2 of the day（2025-01-28、2022-07-26）、#3 of the week（2025-01-28）。本次为第 28 次 PH 发布。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2019/2020 | PH 页写 2019 年发布；YC 页写 Founded 2020（口径并存） |
| 2020 | Y Combinator Summer 2020 |
| 2022-07-26 | PH #2 of the day / #4 of the week |
| 2025-01-28 | PH #2 of the day / #3 of the week |
| 2026-07-11 | PH 发布 Basedash SCIM |
| 2026-07-17 | PH 发布 Basedash Suggestions |
| 2026-07-23 | PH 发布 Basedash AI Kit（"powered by GPT-5.6"） |
| 2026-08-01 | PH 发布 Basedash Audit Logs |
| 2026-08-08 | PH 发布 Basedash Subscriptions（第 28 次发布，当日榜第 2） |

## 评论区反馈（事实摘录，不评价）

- 创始人 Max Musing："Nobody has manually posted a dashboard screenshot since."（发布评论）
- 历史 reviews 亮点：加速分析工作、对话式数据访问、响应及时；批评：定价偏高、缺 Firestore、想要主动 insight 建议。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/basedash（拿到本次 tagline、描述、maker 评论、28 次发布史、awards、reviews、followers、2.8K followers）
- 官网：https://www.basedash.com/（拿到定位、功能面、安全合规、客户、对比页、信任声明）
- 官网定价：https://www.basedash.com/pricing（拿到 Startup/Enterprise 计划、$1,000/月、AI usage、试用）
- YC：https://www.ycombinator.com/companies/basedash（拿到 Founded 2020、Max Musing、多伦多、6 人、S20）
- GitHub：https://github.com/Basedash（拿到组织描述、仓库清单、活跃时间）

## 未查到 / 待补

- 确切票数（PH 页面未显示 upvote 计数）
- 融资轮次与金额（YC S20 之后无公开融资新闻）
- Revenue / 客户数实际数字（官网"200+ 公司"为官网口径）
- Subscriptions 功能是否单独计价
- 创始团队除 Max Musing 外的完整名单与背景
