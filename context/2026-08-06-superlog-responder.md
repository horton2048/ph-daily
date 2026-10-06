# Superlog Responder · 扩展阅读上下文

> PT 2026-08-06 Product Hunt 榜单第 8 · 👍 票数（归档未含具体数字） · 💬 9 评论
> 归档日期 2026-08-06 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Superlog Responder（PH 产品页主体名：superlog） |
| 英文 tagline | FREE AI bug-fixing agent |
| 中文 tagline | 免费 AI 修 bug 智能体 |
| 官网 | https://responder.superlog.sh/ （主站 https://superlog.sh/） |
| PH 页 | https://www.producthunt.com/products/superlog |
| 品类标签 | Developer Tools · Artificial Intelligence · GitHub |
| 票数 / 评论 | 票数：归档未含；PH 页抓取未显示 upvote 数字。评论：9（归档 2026-08-06） |
| 公司主体 | Pulsent Labs Inc.（主站版权行：© 2026 Pulsent Labs Inc.） |
| 企业版/关联站点 | superlog 主产品（可观测性平台）+ Responder（Slack 内修 bug 智能体）；GitHub org: superloglabs |

## 是做什么的（如实复述，不评价）

Superlog Responder 是 Superlog 推出的一个 AI 修 bug 智能体，接在团队已有的 Sentry 或 Datadog Slack 频道里运行，不需要装新的埋点/遥测（PH 页原话："one-click synch, no new telemetry to install"）。每次告警进来，它用完整上下文调查、过滤噪音，确认是真问题后直接在 Slack 线程里回帖，给出根因、证据和一个"可直接合并的 PR"。Prompt、记忆、仓库访问权限、升级规则都可由用户定制。产品开源（Apache-2.0）。它是 Superlog 的第二次发布（第一次是 2026-06-03 发布主产品，当日榜单第 3）。

Responder 与 Superlog 主产品是同一公司、同一开源代码库下的不同入口：主产品是 OTel-first 的"自愈式"可观测性平台（采集 trace/log/metric，把相似报错聚成 incident，派 AI agent 调查并开修复 PR）；Responder 是把它做成一个"活在告警 Slack 频道里"的产品形态，服务那些"遥测已就绪、只想要 bug 被修掉"的团队。

## 解决什么问题（事实层面，不判断值不值得解）

- 团队已有 Sentry/Datadog 遥测和 Slack 告警流，但告警之后仍要人工翻日志、查 trace、看代码定位根因。PH 开篇评论引述用户反馈："我遥测已经配好了，告警已经进 Slack 了……我只想要 bug 被修掉。"
- 噪音告警多：主站称 Superlog 把相似错误"合并成清晰的 incident"（fingerprinting 指纹归组），减少重复告警淹没。
- 修完的 PR 需要人审：产品带 PR autopilot（跟踪 PR、跑 review、回评论），并给出置信度门（Confidence Gate）——置信度不足时改为把发现发群里并拉工程师参与。
- 目标场景：on-call / 工程团队，误报过滤 + 根因定位 + 自动开 PR，覆盖 Datadog/Sentry 数据源和 AWS、GCP、Cloudflare、Vercel、Render、Railway 的日志/指标。

## 怎么做的（技术原理/机制，事实层面）

- 数据接入：从 Datadog / Sentry 导入错误；日志/指标从 AWS、GCP、Cloudflare、Vercel、Render、Railway 导入；任意应用可通过 OpenTelemetry 协议发送（docs 页：instrument with OTel → 把 OTLP exporter 指向 Superlog ingest 端点）。
- 处理流水线（docs 四步）：采集 → 存高基数可查询存储 → 后台 worker 对错误做 fingerprint 归组为 incident → AI agent 看 trace、diff 代码仓库、开修复 PR。
- Agent 上下文来源：Notion、Linear、GitHub、AGENTS.md、CLAUDE.md、自定义 prompt、自定义 MCP。
- 记忆系统：主站称"对 Superlog PR 的每一条评论和 review 都会提升准确度和质量"。
- 严重度与影响：SEV1–3 分级 + 影响评估（示例："SEV-1 … revenue impact: checkout down"）。
- 置信度门：不满足置信度时，改为发群 + 拉工程师补充上下文，而不是直接开 PR。
- MCP：有 Superlog MCP server，"把 incident 上下文直接带进你的 coding agent"（docs 功能卡）。
- 技术栈（GitHub README）：TypeScript pnpm monorepo（Turborepo、Biome、Drizzle ORM、Postgres、ClickHouse、React/Vite），apps/web、apps/api、apps/proxy（OTLP 摄取）、apps/worker（agent 编排）；本地 Quick Start 用 Docker Compose。
- 误报/失败处理：Confidence Gate + 人工升级路径；PR 要过 review。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Nicolò Magnante（CEO，此前在 BCG，帮初创公司做到数百万美元 ARR）；Arseniy Shishaev（CTO，此前在 Datadog 做数据管道/工具，联合创办过 Bluco） | superlog.sh/team |
| 融资 | 未查到具体金额 | — |
| 投资方 | Y Combinator（S26 / YC Spring 2026，GitHub 标注 "Y Combinator P26"） | superlog.sh、GitHub |
| 加速器 | Y Combinator（公司 2026 年创立，总部旧金山） | superlog.sh/team |
| 合规认证 | 未查到 | — |

## 定价 / 商业模式

- Responder：PH 页标注免费层级含 "100 free credits"，有 cloud 选项；详细 Responder 专属价目在抓取页面未展开。
- Superlog Cloud 免费计划（$0 "forever"）：1M spans、5M logs、10M metric points、30 天留存、50 次 incident 调查/月。
- Pay As You Go：无基础费，一次性送 100 次推广调查 + 每月含 50 次；超量每次调查 $1.50；spans/logs 每百万 $0.50；metric points 每百万 $0.15。
- 开源：主仓库 Apache-2.0，Community Edition 可自托管（web/API/OTLP proxy/worker/Postgres schema 全开源）；Cloud 版托管。
- 商业模式：open-core——开源社区版 + 托管云按用量计费。

## 关联信息 / 生态

- 准确率声明：主站称"90% acceptance rate——领先团队 10 个 PR 合并 9 个"；PH 评论区 Victor Gross 提到 "+90% PR-merge rate"。
- 生态仓库（superloglabs org，10 个公开仓库）：superlog（1.2k stars）、skills（一条 prompt 装 instrumentation）、cli、otel-helpers、superlog-expo（Expo/RN SDK）、agent（macOS AppleScript OTel 代理）、helm-charts、homebrew-tap、docs、mintlify-docs。
- 社区渠道：Discord、X @superlogYC。
- 相似产品（PH 页）：Middleware、Better Stack、Datadog、SigNoz、OpenObserve。
- 首次发布：superlog 主产品 2026-06-03 发布，当日榜第 3，80 upvotes，当时 518 followers（PH 页）。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-05-06 | otel-helpers 仓库创建 |
| 2026-05-07 | cli 仓库创建 |
| 2026-06-03 | superlog 主产品首次在 PH 发布（榜第 3）；superlog-expo 仓库创建 |
| 2026-06-04 | skills 仓库创建 |
| 2026-07-21 | helm-charts 仓库更新 |
| 2026-08-05 | superlog 主仓库最近一次更新 |
| 2026-08-06 | Responder 在 PH 第二次发布（当日榜第 8） |

（时间线依据 GitHub 仓库创建/更新日期与 PH 发布信息，非完整官方里程碑）

## 评论区反馈（事实摘录，不评价）

- 用户 Bengeekly 提问："How do I make sure it doesn't create more bugs?"（如何保证它不制造更多 bug）——抓取页面未见 maker 回复。
- 用户 Luigi Pederzani 提问：关于 MCP 支持和 on-prem/BYOC 部署（引用了 docs.superlog.sh）——抓取页面未见 maker 回复。
- 用户 Camille Epitalon：称自己在 beta 期使用 Responder（maker 回复致谢）。
- 用户 Victor Gross：提及 "+90% PR-merge rate"。
- 用户 Romàn Czerny：评论称其是 "One of the best product I know."（个人评价，非事实陈述，仅作摘录）。
- 用户评价（1 条 review）：Francois de Fitte——"Really powerful product, huge time saver"（个人评价摘录）。
- maker（Nicolò Magnante）开篇：说明 Responder 活在告警已存在的 ops 频道，用"你的 Datadog、你的 Sentry、你的 Notion、你的 repo、你的只读 DB"调查后开修复 PR；可定制且开源，"你不是在租我们的 agent，你在搭自己的调试队友"；当周手工 onboarding 早期团队。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/superlog（拿到：描述、maker 开篇评论、评论区提问、followers 838、rating 5.0(1 条)、相似产品、logo URL、官网/GitHub 链接、首次发布记录）
- 官网：https://superlog.sh/（拿到：主产品定位、工作方式、PR autopilot、Confidence Gate、90% 接受率、YC、Pulsent Labs Inc.）；https://superlog.sh/pricing（拿到：免费计划与 PAYG 数字）；https://superlog.sh/team（拿到：两位创始人背景）
- 文档：https://docs.superlog.sh/（拿到：OTLP 流水线四步、MCP server、Apache-2.0、Cloud/Community 版）
- GitHub：https://github.com/superloglabs/superlog（拿到：1.2k stars、Apache-2.0、TypeScript monorepo 结构、YC P26）；https://github.com/orgs/superloglabs/repositories（拿到：10 个公开仓库列表）
- 公开报道：WebSearch 多次未返回可用的报道条目，未检索到独立媒体报道
- Responder 专属子站 https://responder.superlog.sh/ 抓取两次均只返回页面标题，未获得独立页面内容

## 未查到 / 待补

- Responder 专属价目（PH 仅"100 free credits"，pricing 页未展开 Responder 独立定价）
- 具体融资额、投资方名单（除 YC 外）
- 榜单票数具体数字（归档与 PH 页抓取均未给出 upvote 数）
- 两位创始人更多个人背景（教育、此前后续）与公开媒体访谈
- 独立媒体报道（TechCrunch 等）未检索到
- Responder 与主产品在代码层面的边界（是否同一仓库、同一 agent runtime）未从文档确认
