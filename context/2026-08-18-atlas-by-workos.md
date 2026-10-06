---
product: "Atlas by WorkOS"
slug: "atlas-by-workos"
date: "2026-08-18"
rank: 10
votes: 103
comments: 3

category: "AI agent / SaaS"
subcategory: "Slack 内 AI coworker"
tags: ["Slack", "AI Coworker", "WorkOS", "企业级", "Agent", "MCP Auth", "SSO", "Audit Logs", "闭源"]

tech_stack: ["WorkOS 身份基础设施", "Next.js（官网）", "未披露 LLM 提供商"]
platform: ["Slack"]
open_source: false
license: ""

business_model: "未披露（Atlas）；WorkOS 主业为 usage-based + Annual Credits"
pricing_start: "未披露（Atlas）"
funding_stage: "Series B（WorkOS）"
funding_amount: "$80M Series B（2022-03，训练数据，未独立核实）"

related_products: ["WorkOS（User Management / SSO / Directory Sync / AuthKit / Radar / Vault / MCP Auth / Audit Logs / Pipes）", "Slack", "Devin", "Cleric", "Glean", "Moveworks", "Atlassian Rovo", "Notion AI Connector"]
maker_previous: ["WorkOS（2020 创立，已 7 次 PH 发布）"]

key_signals: ["WorkOS 自研内部用 AI coworker，2026-08-04 官博公开、08-18 上 PH 榜单第 10", "原生跑在 Slack 里——@mention 即用，无需独立界面；200+ 工具集成 + 任意 API", "支持自定义 'team agent'：每个 agent 有名字、job description、skills、memory、独立集成与审计", "复用 WorkOS 身份/权限基础设施：无 superuser、无数据影子副本，请求遵循组织既有权限"]

archived_at: "2026-08-18"
sources_count: 4
---

# Atlas by WorkOS · 扩展阅读上下文

> PT 2026-08-18 榜单第 10 名 · 👍 103 · 💬 3
> 归档日期 2026-08-18 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Atlas by WorkOS |
| 英文 tagline | Your AI coworker in Slack |
| 中文 tagline | 你的 Slack 内 AI 同事 |
| 官网 | https://workos.com/atlas |
| 产品入口 | https://atlas.workos.com/install |
| PH 页 | https://www.producthunt.com/products/workos |
| 品类标签 | Slack · Productivity |
| 票数 / 评论 | 103 票 / 3 评论 |
| 公司主体 | WorkOS, Inc.（Copyright 2026） |
| 企业版/关联站点 | workos.com；联系邮箱 atlas@workos.com；WorkOS 在 PH 已发布 7 次，6.8K 关注，4.9 分（18 条评论） |

## 是做什么的（如实复述，不评价）

Atlas 是 WorkOS 推出的 AI coworker，运行形态完全原生在 Slack 内——用户在 DM、channel、thread 任意位置 `@mention Atlas` 即可调用，无需独立应用界面。它会从团队的 Slack 对话中学习组织内部用语、优先级、流程和人员，"correct it once, and the correction sticks"——团队成员的纠正会持久化进 agent 记忆。

除默认的 Atlas agent 外，用户可在对话中描述一个自定义 "team agent"：给一个名字（@gtm、@oncall）、一份工作描述（角色、职责、工作流、语气）和工具访问权限，就能创建一个独立 agent。每个 agent 拥有独立的 instructions、skills、memory、integrations 和 @-name。心智模型是 "an agent is a named teammate with a job description"。

Atlas 连接 200+ 工具（GitHub、Salesforce、Notion、Linear、Jira、Sentry、Stripe、Snowflake 等）外加任意带 API 的系统，可跨多个系统回答问题。官网展示的使用场景包括项目 standup 总结、customer-success 休假归来恢复上下文、incident 根因排查、new hire onboarding 问答。

## 解决什么问题（事实层面，不判断值不值得解）

- 团队知识/上下文散落在 Slack 各 channel、文档、ticket、CRM 系统之间，新成员或休假归来的人需要快速恢复上下文。
- 通用 AI 助手缺乏组织内部语境（shorthand、优先级、谁负责什么），答案泛泛。
- 现有 Slack bot 多为单向通知或单工具集成，无法跨多系统回答复合问题、也无法在共享频道里让多人协同修正。
- 目标场景：客户拜访前准备、休假归来恢复、incident 排查、onboarding、support escalation 分流、产品增长仪表盘定位。

## 怎么做的（技术原理/机制，事实层面）

- 运行方式：Slack 原生——`@mention Atlas` 触发；agent 在共享频道"公开"工作，队友可在 thread 中追加上下文、纠正答案、续接同事未完成的工作。
- Team agent 机制：用户在对话里描述需求 → 命名 + 选工具 → 生成一个有独立 instructions / skills / memory / integrations 的 agent，可被 @mention 调用。Skills 是可复用、跨 agent 共享的指令集。
- 记忆机制：agent 跨会话保留所学，不会每条 thread 重置；纠正持久化。
- 集成模型：每个用户连接自己的账号，可组织级共享连接；Atlas 自称支持 "200+ tools out of the box, plus anything with an API"（博客原文 150+，/atlas 产品页 200+，以产品页为准）。
- 安全模型（关键差异化）：复用 WorkOS 的身份与权限基础设施——每个请求遵循组织既有权限，"no standing superuser and no shadow copy of your company data"；agent 拥有隔离记忆、scoped integrations、server-side secrets、audit logs；创建 agent 时配置 file-saving 权限、memory 写权限、允许的集成、可运行的 workflow。Agent 仅响应本组织内的 mention、仅在 Slack 中活跃。
- 保留名：agent 不可用 `workos` / `slack` / `admin` / `security` / `support` / `everyone` / `here` / `channel` 等名字。
- Agent 指令不可覆盖平台在安全、密钥处理、工具访问上的规则。
- 底层 LLM 提供商：未披露。博客与产品页均未提及 OpenAI / Anthropic / Google 等。
- 误报/失败处理：未披露。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 母公司 | WorkOS, Inc. | 官网 |
| 创始人 / CEO | Michael Grinich（Atlas 官博署名作者；此前 Dropbox 背景） | workos.com/blog/atlas；WebSearch 摘要（训练数据，未独立核实 LinkedIn） |
| 团队规模 | 100+ 人，remote-first | workos.com/about |
| PH Makers | Michael Grinich、fmerian（"Show more" 显示还有更多） | PH 产品页 |
| Hunter | fmerian（Kilo Code） | PH 产品页 |
| 融资 | Series B：$80M（2022-03，led by Lachy Groom，Sequoia 跟投）；Series A：~$24M（2021，led by Sequoia） | **训练数据，未经独立核实**——WebSearch 工具未返回真实抓取结果，待用 Crunchbase / TechCrunch 原始报道核实 |
| 估值 | ~$500M post-money（Series B，训练数据） | 同上，未独立核实 |
| 加速器 | 未查到 | — |
| 合规认证 | WorkOS 主业服务企业客户（OpenAI、Cursor、Perplexity、Webflow、PlanetScale、Drata、Netlify、Indeed、Warp 等），Atlas 复用同一基础设施 | 官网 |
| PH 历史 | WorkOS 在 PH 已发布 7 次，6.8K 关注，4.9 分（18 条评论） | PH 产品页 |

## 定价 / 商业模式

- **Atlas 定价**：未披露。/atlas 产品页与博客均无价格信息，CTA 仅为 "Add to your Slack"，无 freemium / paid tier 区分说明。
- **WorkOS 主业定价**（作为 Atlas 复用基础设施的参考）：
  - AuthKit User Management：前 1M MAU 免费，超出 $2,500/月 per 1M MAU。
  - Radar：前 1,000 checks 免费，超出 $100/月 per 50K checks。
  - SSO & Directory Sync：$125/连接（1-15），递减到 $50/连接（101-200），201+ 定制。
  - Audit Logs：streaming $125/月 per SIEM 连接；retention $99/月 per 1M events。
  - Custom Domain：$99/月。
  - 三档支持：Standard（免费）/ Scale $1,000/月 / Enterprise 定制。
  - Staging 环境免费，仅生产环境计费。
- WorkOS 主业模式：usage-based "Pay as You Go" + Annual Credits（pre-pay 折扣 + 99.99% SLA + guided migration）。

## 关联信息 / 生态

- **与 WorkOS 主业关系**：Atlas 是 WorkOS 内部自用工具对外化（"built internally at WorkOS for our own use"），复用 WorkOS 的身份/权限/审计基础设施作为差异化卖点。这是 WorkOS 从"开发者基础设施 API"扩展到"AI agent 产品"的关键一步。
- **WorkOS 产品矩阵**（截至 2026-08）：User Management、Enterprise SSO、Directory Sync、AuthKit、RBAC、MFA、Admin Portal、Audit Logs、Radar、Vault（EKM）、MCP Auth、Pipes、API Gateway（2026-06 发布）、WorkOS MCP（2026-07 发布）。
- **Agent Night 社区活动**：WorkOS 主办 AI agent demo 系列（Mastra、Evil Martians、Airlock、exe.dev、Brian Douglas self-healing Pokémon agent 等），并在 2026-07-28 举办 Applied AI Showcase NYC。
- **竞品 / 相邻产品**：Glean（企业搜索 + AI）、Moveworks（企业 AI assistant）、Atlassian Rovo、Notion AI Connector、Slack 自家的 Slack AI、Devin / Clerkic（更偏工程 agent）。Atlas 差异化点在"原生 Slack 形态 + WorkOS 身份/权限栈"。
- **客户**：WorkOS 主业客户含 OpenAI、Cursor、Perplexity、Webflow、PlanetScale、Drata、Chromatic、Incident.io、Netlify、Copy.ai、Warp、Indeed 等——这些也是 Atlas 潜在客户池。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2020 | WorkOS 在 Product Hunt 首发 |
| 2021 | Series A ~$24M（Sequoia 领投，训练数据未核实） |
| 2022-03 | Series B $80M（Lachy Groom 领投，Sequoia 跟投，估值 ~$500M，训练数据未核实） |
| 2026-06-30 | API Gateway 发布 |
| 2026-07-01 | WorkOS MCP（远程 MCP server）发布 |
| 2026-07-28 | Applied AI Showcase NYC |
| 2026-08-04 | Atlas 官博公开（Michael Grinich 署名） |
| 2026-08-17 | Agent Night demo 系列 recap 发布 |
| 2026-08-18 | Atlas 上 Product Hunt 榜单第 10 名（103 票 / 3 评论） |

## 评论区反馈（事实摘录，不评价）

- **Sam Bhagwat**（Mastra）："Exciting!"（2 upvotes，~14h 前）
- **fmerian**（Kilo Code，Hunter）："strong +1"（~11h 前）
- **Hamza Afzal Butt**："Looks cool! Congrats!!!"（~2h 前）

PH 产品页未见 maker 长帖说明，仅 short maker 标注。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/workos — 拿到 tagline、topics（Slack · Productivity）、票数 103 / 评论 3、makers（Michael Grinich、fmerian）、hunter（fmerian）、WorkOS 历史（7 次发布、6.8K 关注、4.9 分）、3 条社区评论。
- Atlas 产品页：https://workos.com/atlas — 拿到形态（Slack 原生 @mention）、200+ 集成清单（GitHub/Salesforce/Notion/Linear/Jira/Sentry/Stripe/Snowflake 等）、自定义 team agent 机制、安全模型（无 superuser、无数据影子副本、audit logs、scoped integrations）、使用场景（project-orbit / customer-success / incidents / new-hires 四个示例 channel）。
- Atlas 官博：https://workos.com/blog/atlas（2026-08-04，Michael Grinich 署名）— 拿到"内部自用对外化"定位、team agent 心智模型、skills/memory/integrations 机制、安全细节（保留名列表、指令不可覆盖平台规则）、安装入口 atlas.workos.com/install。
- WorkOS 主站 / 定价 / About：https://workos.com/、https://workos.com/pricing、https://workos.com/about — 拿到 WorkOS 产品矩阵、定价（AuthKit 1M MAU 免费、SSO $125/连接等）、团队规模（100+，remote-first）、客户名单。
- GitHub：未查到 WorkOS 开源 Atlas 的信号；WorkOS 主业 SDK 在 GitHub 上有公开 SDK 仓库（Node.js / Ruby / Python / Go / PHP / Java / .NET），但 Atlas 本身闭源，未单独建仓。
- 公开报道：WebSearch 工具未返回真实抓取结果（仅训练数据合成回答），WorkOS Series A/B 融资数据来自训练数据，标注为"未独立核实"。

## 未查到 / 待补

- **Atlas 定价**：官网、博客、PH 页均无定价信息，无 free/paid 区分，未披露。
- **Atlas 底层 LLM 提供商**：未披露，未提及 OpenAI / Anthropic / Google。
- **WorkOS 融资细节**：Series A ~$24M / Series B $80M / 估值 ~$500M 均来自训练数据，WebSearch 未返回真实抓取结果，**待用 Crunchbase / TechCrunch / The Information 原始报道独立核实**。WorkOS 官网未披露融资信息。
- **WorkOS 创始人完整背景**：Michael Grinich Dropbox 出身来自训练数据，未核实 LinkedIn；是否有其他联合创始人未查到。
- **WorkOS 总部**：仅知 remote-first、有 SF/NYC 活动，未查到注册地。
- **Atlas 发布时间线**：2026-08-04 官博公开，但何时开始内测、何时首次在 WorkOS 内部使用未披露。
- **PH 完整 maker 列表**：产品页 "Show more" 未展开，仅见 Michael Grinich 和 fmerian。
- **误报/失败处理**：未披露。
- **Atlas 是否单独计费**：未明确——可能作为 WorkOS 平台功能、可能单独计费、可能有免费层，待官方确认。
