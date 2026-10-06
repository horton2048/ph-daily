# Customer.io Summer Release · 扩展阅读上下文

> PT 2026-07-31 Product Hunt 榜单第 8 · 👍 140 · 💬 3
> 归档日期 2026-08-01 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Customer.io Summer Release |
| 英文 tagline | New ways to reach customers in the moments that matter |
| 中文 tagline | 在关键时刻触达客户的新方式 |
| 官网 | https://customer.io/ |
| PH 页 | https://www.producthunt.com/products/customer-io |
| 品类标签 | Marketing automation platforms · Email · Email Marketing |
| 票数 / 评论 | 140 👍 / 3 💬（PH 页显示 152 points） |
| 公司主体 | Peaberry Software, Inc.（dba Customer.io） |
| 企业版/关联站点 | customer.io（主站）；trust center、academy、docs 等子站 |

## 是做什么的（如实复述，不评价）

Customer.io 是一个客户互动 / 营销自动化平台（Customer Engagement Platform），把客户数据、跨渠道消息（email / SMS / push / in-app / WhatsApp / LINE / webhook）和 AI 整合到同一平台，让企业基于第一方数据在"对的时刻"触达用户。本次 "Summer Release" 是 Customer.io 自 2017 年以来首次回 PH 发布的版本更新，一次性推出 10+ 个新功能，核心是扩展触达客户的"触发器、渠道、终端"三类能力，让品牌能在用户进店、锁屏实时更新、消息回看等"关键时刻"出现。

PH 页将其描述为"Customer.io's most expansive launch yet"。这是版本发布（product launch），不是新公司。

## 解决什么问题（事实层面，不判断值不值得解）

- 客户互动的难点不是"建好旅程"，而是"在对的时刻出现"——这是创始人 Jeff Zats 在 PH 评论区转述的客户反馈（"It's not enough to build great customer journeys. You need to show up at exactly the right moment."）
- 跨渠道分散：移动、Web、SMS、in-app、WhatsApp、email 多端各自为政，团队需要一个统一平台来编排
- 移动端实时触达能力欠缺：传统营销自动化平台缺乏原生 geofencing、Live Activities 等移动原生能力
- WhatsApp 模板管理零散；SMS 供应商锁定（不能自带供应商）
- 历史消息不可回看（用户错过通知后无法找回）

## 怎么做的（技术原理/机制，事实层面）

本次 Summer Release 新增 / 强化的能力（来自 PH 创始人评论及官网"10+ new features"宣传）：

- 📍 **Native Geofencing**（原生地理围栏）：基于用户地理位置触发消息，例如用户进店时即时推送
- 📱 **Live Notifications**：对应 iOS 的 Live Activities 和 Android 的 Live Updates，在锁屏实时更新（如订单状态、活动进度）
- 💬 **Bring your own SMS provider**（灵活 SMS 供应商）：客户可自带 SMS 服务商，不再锁定官方供应商
- 📥 **Notification inbox**（通知收件箱）：给用户提供一个集中回看历史消息的地方
- 🟢 **Native WhatsApp template management**（原生 WhatsApp 模板管理）
- 🤖 **Enhanced AI actions**：AI 直接内嵌在 campaign builder 里做分段、audience 选择、workflow 创建（创始人回复评论区强调"AI 是构建活动的一部分，不是单独切换的工具"）
- 🌙 **Dark mode**
- 多 workspace 多 app（multiple apps per workspace）
- 全渠道订阅控制（omnichannel subscription controls）
- 消息频率上限（message frequency caps）
- Tooltips

技术栈 / 基础设施（来自官网）：US/EU 数据中心、SOC Tier II、HIPAA、GDPR 合规；MCP server 支持（可与外部 AI 工具配合）；Mobile SDKs；提供 API、CLI、webhook 多种接入方式。日均 12B+ API 调用、2025 年累计发送 100B+ 消息、100B+ webhooks（官网 About 页）。

误报 / 失败处理：未查到。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Colin Nederkoorn（CEO）+ John Allison（联合创始人） | 官网 About 页 + CEO 公告 + Tracxn |
| CEO | Colin Nederkoorn | 官网 / PH / LATKA |
| CFO | Zhi Li | 官网 About 领导团队 |
| CTO | Matthew Newhook | 官网 About 领导团队 |
| CRO | John Schoenstein | 官网 About 领导团队 |
| CMO | Jason Lyman | 官网 About 领导团队 |
| CPO | Jennifer Fong | 官网 About 领导团队 |
| Chief of Staff | Meenakshi Sharma | 官网 About 领导团队 |
| 员工数 | 352 人 | LATKA（2025） |
| 总部 | Portland, Oregon, USA（公司分布式运营） | LATKA / LinkedIn |
| 融资总额 | 约 $38.8M（6 轮，15 个投资方） | Tracxn / The Company Check |
| 最新一轮 | $29.9M，2022-03-08 | Tracxn |
| 投资方 | Spectrum Equity、FJ Labs、Oregon Venture Fund、Seven Peaks Ventures 等 | Tracxn |
| 2021 众筹轮 | 约 $20M ARR 时众筹，约 2,500 人投资（含客户） | 官网 CEO 公告 |
| 估值 | 官方称 $690M（LATKA 估算，非官方披露） | LATKA |
| 加速器 | 未查到 | — |
| 合规认证 | GDPR / AICPA SOC / HIPAA | 官网 |

## 定价 / 商业模式

三档套餐（官网 /pricing/，2026-08 抓取）：

- **Essentials**：$100/月（按月付），含 5,000 profiles（people + objects）、100 万 email/月、AI Agent 标准配额、LLM 100K credit sample、社区+邮件支持
- **Premium**：$1,000/月起（按年付），自定义 profile/email 量、10 种 object types、Elevated Agent 限额、HIPAA、90 天 onboarding、Premium chat+email 支持
- **Enterprise**：议价（Talk to sales），专属硬件、CSM、迁移支持、审计日志、数据治理、共享 Slack 频道

按量超额：
- 额外 profile：$0.009 / profile（Essentials）
- 额外 1,000 封 email：$0.12（全档统一）
- 额外 AI credit：$10 / 100K

商业模式核心：
1. **订阅制 + profile 量阶梯定价**：按管理的"人 + object"数据量计价，量越大单价越议价
2. **AI Agent credit 计费**（beta）：LLM 操作按 100K credit 一档售卖
3. **Startup Program**：融资 <$10M 的早期公司可申请 12 个月免费（含 Essentials 等效能力）
4. **14 天免费试用，免信用卡**

营收规模：官方称 2025 年 9 月突破 $100M ARR（PH 创始人评论 + CEO 公告）；2021 年约 $20M ARR；8,000+ 公司客户（CEO 公告）/ 9,000+ 品牌（PH + 首页宣传）

## 关联信息 / 生态

- 客户基数：官方称 9,000+ 品牌（PH tagline）/ 8,000+ 公司（CEO 公告，2025-09），含 Notion、Lovable、Wispr Flow、Cursor
- 历史收购：2022 年收购 Gist 和 Parcel（用于移动 SDK、in-app 通知、编辑器体验）
- 竞品定位（PH Similar Products）：Loops、Mailmodo、Moda、Intuit Mailchimp、Braze
- 平台能力矩阵：Journeys / Audiences / Data & integrations / Design Studio / Analytics / AI Agent（beta）
- 生态：MCP server（可与外部 AI 工具协作）、CLI、API、webhook；integration 生态分 Basic / Premium 两档
- 历史 PH 发布：本次是第 6 次 PH 发布，前 5 次分别为 2014（首发）、2016（Actions、Slack Action）、2017（From Churn to Earn）

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2012 | Colin Nederkoorn + John Allison 创立 Customer.io，前 5 个客户加入 |
| 2014 | 规模化扩张，团队转为全分布式 |
| 2016 | 跨过 1,000 客户；扩展至 push / SMS / Slack / webhook（首次走出 email） |
| 2018 | 推出 Premium Plan + HIPAA 合规 |
| 2020 | 推出 Visual Workflow Builder（可视化客户旅程画布） |
| 2021 | 约 $20M ARR 时进行众筹轮，约 2,500 人投资（含客户） |
| 2022 | 收购 Gist + Parcel；推出新 Mobile SDKs、in-app 通知、编辑器更新；最新一轮融资 $29.9M（Tracxn） |
| 2023 | CDP 能力扩展，数据进出端口数量翻倍 |
| 2024 | 稳定性 / 性能 / 大规模体验优化 |
| 2025-09 | 官方称突破 $100M ARR；累计发送 64B 消息（12 个月） |
| 2025~2026 | AI 能力覆盖 Customer.io 各模块；Summer Release 推出 |
| 2026-07-31 | Summer Release 上 PH 榜单第 8，10+ 新功能发布 |

## 评论区反馈（事实摘录，不评价）

- **Jeff Zats（Customer.io Maker）开场评论**：宣布这是 Customer.io 自 2017 年以来首次回 PH 发布；列出 10+ 新功能（geofencing、Live Notifications、自带 SMS 供应商、notification inbox、原生 WhatsApp 模板管理、增强 AI actions、暗黑模式、多 app/workspace、全渠道订阅控制、消息频率上限、tooltips）；强调这些功能在同一 automations / segments / data 体系内协同工作
- **Çınar Koçanaoğlu（用户）**：称赞 AI 直接内嵌在 campaign builder 里，不是事后附加；感觉平台在 segmentation 上承担了重活，让人能专注创意
- **Jeff Zats 回复**：确认这就是目标——AI 应该是构建活动的一部分，不是另一个要切换/学习的工具；帮助处理重复工作（segmentation、audience selection、workflow creation）

PH 评价摘要（Summarized with AI）：评论者画像偏窄、混合——有直接用户反馈偏负面（小团队使用痛苦、UI 混乱、journey 不灵活、email 编辑器草稿/投递细节隐藏）；创始人反馈偏正面（IFTTT makers 称赞 behavioral triggers / segmentation / 多渠道 / event-based 自动化）

## 信息来源

- **PH 产品页**：https://www.producthunt.com/products/customer-io
  - 拿到：tagline、票数（140/152）、排名（#8）、创始人 Jeff Zats 完整开场评论（10+ 新功能列表）、用户评论、Similar Products、历史发布记录、logo URL
  - logo: https://ph-files.imgix.net/b1288607-8b86-4ce8-b593-1814b7c8bab1.png?auto=compress,format&codec=mozjpeg&cs=strip&fit=crop&frame=1&h=64&w=64
- **官网首页**：https://customer.io/
  - 拿到：定位、9,000+ 品牌背书、能力矩阵（Journeys/Audiences/Data & integrations/Design Studio/Analytics/AI Agent）、合规徽章、案例数字（28% CTR↑、22% 邮件转化↑、3.36% 流失↓、4.4% app 互动↑）
- **官网 About 页**：https://customer.io/about/
  - 拿到：成立年份 2012、累计消息量 100B+（2025）、12B+ 日 API 调用、78k 活跃用户、9,000+ 品牌、领导团队（CEO Colin Nederkoorn 等 7 人）、公司主体 Peaberry Software, Inc.、媒体覆盖列表
- **官网 Pricing 页**：https://customer.io/pricing/
  - 拿到：三档定价（Essentials $100/mo、Premium $1,000/mo、Enterprise 议价）、超额单价、AI credit 计费、Startup Program 12 个月免费
- **CEO 100M ARR 公告**：https://customer.io/learn/announcements/customerio-crossed-100m-note-from-ceo
  - 拿到：$100M ARR 时间（2025-09）、12 个月发送 64B 消息、8,000+ 公司客户、完整时间线（2012→2025）、联合创始人 John Allison、2021 众筹轮 2,500 人投资、2022 Gist + Parcel 收购
- **Tracxn / The Company Check**（搜索引擎结果）：
  - 拿到：融资总额 $38.8M、6 轮、15 投资方、最新轮 $29.9M（2022-03-08）、投资方 Spectrum Equity / FJ Labs / Oregon Venture Fund / Seven Peaks Ventures、联合创始人 John Allison
- **LATKA**（搜索引擎结果）：
  - 拿到：估值估算 $690M、员工 352 人、总部 Portland
- **GitHub**：未查（非本次重点；Customer.io 有 SDK 开源仓库如 customerio-android / customerio-ios，未逐一核实）

## 未查到 / 待补

- Summer Release 各新功能的具体技术实现细节（geofencing 精度、Live Notifications 后端架构、AI actions 模型来源）——未在官网 / PH 公开披露
- 各新功能是否需要额外付费 / 仅 Premium / Enterprise 可用——Pricing 页未单独标注本次新功能的可用层级（部分标 "New" 但未标 tier）
- 估值 $690M 为 LATKA 第三方估算，非官方披露，谨慎使用
- 加速器背景：未查到（公司 2012 年成立时是否经过加速器未公开）
- 本次 Summer Release 的具体上线日期（除 PH 发布日 2026-07-31 外）未查到
- 官网首页 banner 提到"Aug. 6th webinar: See 10+ new features"，说明 webinar 在 2026-08-06，本次 PH 发布为预热
