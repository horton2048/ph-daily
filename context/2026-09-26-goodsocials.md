---
# 结构化元数据（用于索引和聚合）
product: "GoodSocials"
slug: "goodsocials"
date: "2026-09-26"
rank: 5
votes: 110
comments: 7

# 分类标签
category: "SaaS"
subcategory: "AI 社交媒体管理 / LinkedIn 内容自动化"
tags: ["LinkedIn", "AI 内容生成", "Claude Code", "审批工作流", "数据驱动", "Freemium", "Agency"]

# 技术信息
tech_stack: ["Claude Code", "Vercel", "Neon", "Canva", "Flora AI", "Buffer"]
platform: ["Web"]
open_source: false
license: ""

# 商业信息
business_model: "订阅制（按月付费）"
pricing_start: "$100/月（Pro，7 天免费试用）"
funding_stage: "未披露（独立创始人项目，未提及融资）"
funding_amount: ""

# 关联信息
related_products: ["Buffer", "Hootsuite", "Taplio", "Supergrow", "AuthoredUp", "MagicPost", "Publer", "Typefully", "Postli"]
maker_previous: ["TimeTuna (PH #1 of the Day, 2025-12-18)", "Bookva.ai (TimeTuna 前身, 2025-07 PH #6)", "TimeTuna.com (2026-06 PH #9)", "GoodLads (2026-09 与 Yannick Veys 合作, PH #7)"]

# 速览信号（给 caption.md / INDEX.md 等下游用，避免整篇重读正文才能省 token）
key_signals:
  - "创始人 Pavel Kucherbaev 此前做 TimeTuna 拿下 PH #1 of the Day (2025-12-18)，现在专攻 LinkedIn AI 内容"
  - "三档订阅：Pro $100/月、Agency $1,000/月（10 个客户档案）、Consultancy $2,000/月（创始人亲自陪跑）"
  - "内容只来自深度研究或用户自有数据（GitHub PR、Stripe、PostHog、Plausible、Notion），过滤绝对数字和敏感数据"
  - "审批式 Kanban 工作流：写 → 配图 → 用户审 → 每周四傍晚经 Buffer 自动排程，工作日每日一篇"

# 元信息
archived_at: "2026-09-26"
sources_count: 4
---

# GoodSocials · 扩展阅读上下文

> PT 2026-09-26 Product Hunt 榜单第 5 · 👍 110 · 💬 7  
> 归档日期 2026-09-26 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | GoodSocials |
| 英文 tagline | AI social media manager for LinkedIn. Only authentic content |
| 中文 tagline | 给 LinkedIn 用的 AI 社媒经理，只发「不像 AI」的内容 |
| 官网 | https://goodsocials.co/ |
| PH 页 | https://www.producthunt.com/products/goodsocials |
| 品类标签 | Artificial Intelligence · LinkedIn · Social media marketing |
| 票数 / 评论 | 110 / 7（93 followers） |
| 公司主体 | 版权署 © 2026 GoodSocials, Amsterdam；法律实体未披露 |
| 企业版/关联站点 | 创始人 Pavel "Pasha" Kucherbaev（linkedin.com/in/pavelkucherbaev/） |

## 是做什么的（如实复述，不评价）

一个专门针对 LinkedIn 的 AI 社媒经理：每天工作日生成一篇帖子（每周 5 篇），内容只来源于两类——**深度市场研究**或**用户自己的数据**（如 GitHub PR、Stripe 营收、PostHog 用户行为、Google Calendar 会议、Notion 笔记）。生成流程包含**写稿 + 配图**，用户在一个 Kanban 看板里逐条审批，审批通过后由 Buffer 在每周四傍晚统一排程到 LinkedIn。配套有"Brand Principles"（3 条品牌准则）随用户每次打回重写而自动学习，最终沉淀为「声音规则库」，让写作语气逐渐贴近用户本人。

## 解决什么问题（事实层面，不判断值不值得解）

- 创始人自己过去每周给 TimeTuna 写一条 LinkedIn 更新，要花约 1 小时/篇；产品目标是把"维护一条活跃的 LinkedIn 个人号"的工时大幅压低。
- PH 描述直指一个具体不满：现有 AI 写的 LinkedIn 帖子常带"slop"味道（同质化、口号化、可一眼识破是 AI 写的）。
- 对标一位"$3,000/月的人类社媒经理"：把价格降到 $100/月 Pro，但保持工作日日更频率与请假不中断的连续性。
- PH 上榜 launch 优惠码 NOCRINGE33（3 个月 33% off）也呼应"No AI cringe"的定位。

## 怎么做的（技术原理/机制，事实层面）

- **数据接入层**：用户授权接入 PostHog、Stripe、GitHub、Plausible、Notion 等数据源，**只读**，不会写入；官方称"Coming soon"的是 Codex、Claude Code、Grok bot 三类集成。
- **生成模型**：官方明确写 Built With `Claude Code`（即 Claude Agent SDK 类工具），辅以 Canva + Flora AI 生成图片；排程交付 `Buffer`。
- **三类帖子模板**：Market research、Deep dive、Your numbers——前两类走外部研究，第三类只引用用户自己的指标。
- **隐私/可信度过滤**：明确**禁止**输出个人数据、客户数据、绝对数字，**只允许**趋势和百分比（"31% of August signups chose annual, up from 19% in July. Two candidate causes, neither confirmed."是官网给出的样例）。
- **品牌准则（Brand Principles）**：起步给 3 条；用户每条评论/打回一次，相关帖子会被改写并把这条修改沉淀为新的"声音规则"，规则数量随时间累加（官网给的时间线：Week 1 = 1 rule，Week 4 = 2 rules，Week 12 = 5 rules）。
- **审批流**：7 篇草稿在 90 秒内生成完毕；用户拖拽卡片在 Kanban 看板中审批或打回；节假日用户可事先"积压一批草稿"，AI 会按节奏继续发。
- **基础设施**：Vercel 部署 + Neon（Postgres）。
- **明文"反特性"**（Anti-features）：不写"Nobody talks about this"开头、不写"It's not X, it's Y"句式、不写"cringe hooks"。品牌口号："Peace. Love. No AI cringe."

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Pavel "Pasha" Kucherbaev（单人独立项目） | goodsocials.co / PH 页面 |
| 融资 | 未披露（无外部融资迹象，官方未提） | 未查到 |
| 投资方 | 未披露 | 未查到 |
| 加速器 | Antler 校友（Founder 履历） | indiehackers / hunted.space 资料 |
| 合规认证 | 官网声明"Not affiliated with LinkedIn"，以用户授权身份代发 | goodsocials.co 脚注 |

创始人履历要点（来自第三方 PH 资料库与个人简介）：
- 学术：Human Computer Interaction 博士
- 大厂：曾在阿姆斯特丹 Booking.com 与 Atlassian 任 Data Science Manager
- Product Hunt 历史：账号 @pavelk2，2015-08 加入，至今 262 followers；hunter 记录 3 个 featured、846 total upvotes、1 个 #1 placement
- 时间线上的产品发布：
  - 2025-07 Bookva.ai（TimeTuna 前身） PH #6 of the Day
  - 2025-12-18 TimeTuna PH **#1 of the Day**（384 upvotes，44 comments）
  - 2026-06 TimeTuna.com PH #9
  - 2026-09 与 Yannick Veys（Hypefury 创始人）联合发布 GoodLads（AI Google Ads 增长经理），PH #7
  - 2026-09-26 GoodSocials PH #5（本日）

## 定价 / 商业模式

| 档位 | 价格 | 内容 |
|---|---|---|
| Pro | $100/月 | 1 个 LinkedIn 档案；3 条 Brand Principles；每月最多 200 张生成图；7 天免费试用 |
| Agency | $1,000/月 | 最多 10 个客户档案；每客户一块独立看板；客户自己授权、平台不持有密码；客户访问到期前邮件提醒 |
| Consultancy | $2,000/月 | 创始人 Pasha 亲自设主题、原则、数据源；每周与 Pasha 视频同步 |

- 启动优惠：3 个月 33% off，优惠码 `NOCRINGE33`
- 7 天免费试用，三档都支持；随时取消，可从页面或设置里改方案

## 关联信息 / 生态

- **官方明确列出的对比对象**（官网有专属对比页）：Buffer、Hootsuite、Taplio、Supergrow、AuthoredUp、ChatGPT（另有 "All 20 comparisons"）
- **PH 同类项排名截图列出的竞品**：Publer（4.9, 55 评）、MagicPost（5.0, 5 评）、Typefully（4.7, 22 评）、Postli（4.8, 5 评）、Supergrow（5.0, 1 评）
- **典型样例输出（TimeTuna.com demo board）**：
  - "Failed deploys per release fell about 62% after one CI rule. Small sample, 11 releases. Encouraging so far."（源自 GitHub）
  - "31% of August signups chose annual, up from 19% in July. Two candidate causes, neither confirmed."（源自 Stripe）
  - "Most retainers end in month four. Across 38 client engagements, one meeting shows up in 29 of the exits."（源自 Notion）
- **创始人的产品矩阵**：TimeTuna（Calendly 替代品，定价 $10/月起） + GoodLads（Google Ads AI 经理） + GoodSocials（LinkedIn AI 经理）—— 形成"独立创业者个人/小公司"全栈 AI 运营工具带。

## 技术时间线（官网里程碑）

| 日期 | 事件 |
|---|---|
| 2025-07 | Bookva.ai（TimeTuna 前身） PH #6 |
| 2025-12-18 | TimeTuna PH #1 of the Day（384 upvotes） |
| 2026-06 | TimeTuna.com PH #9 |
| 2026-09 | GoodLads（与 Yannick Veys 合作） PH #7 |
| 2026-09-26 | GoodSocials PH #5（本日）；launch promo NOCRINGE33 |

## 评论区反馈（事实摘录，不评价）

- **Adana Marukhyan**：是否支持 LinkedIn 之外的平台？  
  **Pavel 回复**：Instagram 和 X 正在做，下一步上。
- **Nika**：为什么选 LinkedIn 而不是其它平台？  
  **Pavel 回复**：源于自己经营 TimeTuna 时养成的 LinkedIn 更新习惯；同时表示未来在考虑把 Reddit 也纳入营销渠道。
- 品牌哲学自陈："Peace. Love. No AI cringe."

## 信息来源

- PH 产品页：https://www.producthunt.com/products/goodsocials（tagline、品类、Built With、launch offer、相似产品、评论、maker 背景）
- 官网：https://goodsocials.co/（定价三档、数据源列表、生成流程、Anti-features、样例帖、品牌准则机制、创始人姓名）
- 公开报道：indiehackers.com / hunted.space 关于 TimeTuna 的 PH #1 历史、创始人履历（Antler 校友、Atlassian/Booking.com 数据科学背景）
- GitHub：无公开仓库（产品为闭源 SaaS，未检索到官方仓库或 repo 链接）

## 未查到 / 待补

- 公司法律实体全名、注册形式（BV/NV 等）、具体注册地址（官网仅写 Amsterdam + © 2026 GoodSocials）
- 是否有外部融资、种子轮或投资方（官网与 PH 均未提及）
- 实际生成时所用的具体 Claude 模型版本（仅披露 Built With "Claude Code"）
- 接入 PostHog / Stripe / GitHub 等数据源时是否走 OAuth 标准流程还是反向代理抓取
- "Up to 200 generated images/month" 在 Agency / Consultancy 档位的具体上限是否叠加或单独计算
- Canva + Flora AI 是仅作为底层图像生成调用，还是 GoodSocials 自带样式预设
- Instagram / X 的上线时间表（评论里仅说"coming next"，无日期）