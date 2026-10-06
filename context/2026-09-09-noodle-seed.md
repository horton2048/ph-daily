---
product: "Noodle Seed"
slug: "noodle-seed"
date: "2026-09-09"
rank: 4
votes: 189
comments: 30

category: "开发者工具"
subcategory: "AI Agent 运行时 / MCP 基础设施"
tags: ["MCP", "TypeScript", "Apache-2.0", "ChatGPT Apps", "Claude", "Agent", "运行时", "SDK", "无代码"]

tech_stack: ["TypeScript", "Zod", "Node.js 24+", "MCP", "OAuth 2.1", "JWT", "Stripe"]
platform: ["macOS", "Windows via WSL2/Ubuntu", "云托管"]
open_source: true
license: "Apache-2.0"

business_model: "Freemium + 订阅 + 实施服务"
pricing_start: "$0 免费档，Pro $30/月"
funding_stage: "已融资（Crunchbase 显示有融资轮次但具体投资方被 Pro 墙遮蔽）"
funding_amount: "未披露"

related_products: ["Claude by Anthropic", "Pickaxe", "Agentplace", "Taskade", "CometChat Agent Platform", "Shopify for ChatGPT Apps"]
maker_previous: ["Asad Iqbal 2018 年在巴基斯坦拉合尔创办 Noodleseed 家教平台（5000+ 节课程）"]

key_signals:
  - "双向口号拆解：'AI in your product' = 在自家 SaaS 内嵌沙箱化品牌助手；'Your product in AI' = 把自家能力作为 MCP server/app 投喂到 ChatGPT/Claude/Codex"
  - "Apache-2.0 开源平台，'薄语言厚运行时'：开发者只写 server.ts 一个文件 + Zod schema，身份/OAuth/凭据代理/限流/审计全部由多租户托管运行时承担"
  - "npm 包 @noodleseed/one + Node 24+；声称 #1 ChatGPT app directory 开发者、用 Noodle Seed 做出的 ChatGPT apps 比任何公司都多"
  - "定价 4 档：Free / Pro $30 / Scale $300 / Enterprise 定制；超出 $5/百万次调用；另有实施服务 $1.5k-$25k+"
  - "公司主体 The NoodleSeed Corporation（Santa Clara）；创始人 Asad Iqbal + Fahd Rafi；客户页列出 Meta/Arm 领导者背书（Rawan, Epik, Kitchen OS, Jettly, Layla, Heymate, Slotted, Commerce OPS Studio 9 家）"

archived_at: "2026-09-10"
sources_count: 4
---

# Noodle Seed · 扩展阅读上下文

> PT 2026-09-09 Product Hunt 榜单第 4 · 👍 189 · 💬 30
> 归档日期 2026-09-10 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Noodle Seed |
| 英文 tagline | Your product in AI and AI in your product |
| PH 副标 | Connect your business to AI conversations in minutes |
| 中文 tagline | 让你的产品进 AI，也让 AI 进你的产品 |
| 官网 | https://noodleseed.com |
| 文档 | https://docs.noodleseed.dev/docs |
| Console | https://console.noodleseed.dev/ |
| PH 页 | https://www.producthunt.com/products/noodle-seed |
| 品类标签 | SaaS · Developer Tools · Artificial Intelligence（PH 标签）；No-Code AI Agent Builder（PH 自填分类） |
| 票数 / 评论 | 189 / 30 |
| 公司主体 | The Noodle Seed Corporation（Santa Clara, CA，注册代理 Asad Iqbal） |
| X / LinkedIn | @noodle_seed / linkedin.com/company/noodle-seed |
| 第二次上榜 | 2026-01-19 首发拿下当日 #1 / 当周 #5 |

## 是做什么的（如实复述，不评价）

让现有 SaaS 产品"为 AI 代理做好准备"——同一条 TypeScript 工作流既能在自家产品里跑出一个沙箱化的、带品牌色的客户助手（"AI in your product"，对应 Halo 嵌入式 widget），也能以 MCP server / MCP Apps 的形式被外面的 ChatGPT、Claude、Codex、Cursor、Copilot 等代理客户端调用（"Your product in AI"）。两条路径走同一个后端，所以数据、身份和商业规则不会因为多了"代理"这层就被绕过。

不是无代码聊天机器人外壳。开发者写一个 `server.ts`，声明 tools / resources / prompts / widgets，运行时把协议、认证、HTTP、重试、验证全部兜起来。

## 解决什么问题（事实层面，不判断值不值得解）

- 软件团队被要求"加 AI 助手/AI 接入"但一条 workflow 很快变成基础设施项目（创始人 Asad 原话）。
- 代理从外面调用 SaaS 时，OAuth、凭据、限流、审计、租户隔离每家都要重做一遍——Fahd 把它拆成"所有代理化 SaaS 都需要同一套积木"。
- 访客在 AI 助手那里能拿到有用结果后必须再注册一次 SaaS——Noodle Seed 用"signup continuity"在登录前后串起同一段对话。
- 知识库更新、FAQ、testimonial 等内容要喂给助手时常见靠手工刷——Hassan 的评论提到内置 knowledge base 文档作为护栏。

## 怎么做的（技术原理/机制，事实层面）

- **薄语言、厚运行时**：开发者写 `server.ts`，用 `@noodleseed/one` SDK + Zod schema 声明 tool / resource / prompt / widget。运行时负责身份、OAuth、凭据代理（brokered credentials：入站 token 不直传后端，校验后换成下游 scope 凭据）、secrets、限流、audit、observability。
- **Server is data**：TypeScript 编译成可移植的运行时描述，不是打包后的服务器进程。
- **多租户默认开启**：同一份 runtime 给多个 server 提供服务，带隔离。
- **四步模型 Connect → Authorize → Operate → Prove**：连接现有 API/MCP server/后端；签约/校验身份；上线运维；审计/合规可证。
- **跨表面同一后端**：一份代码同时在 ChatGPT app、Claude、Codex、Cursor、Copilot、Gemini、MCP Inspector 上跑。
- **沙箱 React UI**：返回给客户端的 UI 是 html/js，被支持 MCP Apps 的客户端在 sandboxed iframe 里渲染（Fahd 评论原话）。
- **审计范围**：记录部署、回滚、策略拒绝、运维操作；不记请求体或 token 内容。
- **运行环境**：macOS 原生；Windows 通过 WSL2 + Ubuntu。
- **依赖**：Node.js ≥ 24。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 / CEO | Asad Iqbal（注册代理） | Crunchbase · LinkedIn · 加州公司注册 |
| 联合创始人 | Fahd Rafi（CTO/工程，@fahd-noodleseed，GitHub 维护者） | PH maker · GitHub |
| PH 页面 maker 列表（8 人） | Asad Iqbal (@asadatnoodle)、Fahd Rafi (@fahd_rafi)、Syed Muzamil Hasan Zaidi、Ebere Ukoh、Naveed Rafi、Hassan Iftikhar、Shayma El Omri、Ben Lang (@benln) | PH 页 |
| Ben Lang 在 maker 列表里的角色 | 资料显示其为 Product Hunt 联合创始人兼 CEO，本身有 2012–2014 同名"Noodle Seed"应用发现平台的渊源；本次以 maker 身份出现但非 Noodle Seed 当前运营方 | LinkedIn · The Next Web 2014 |
| 团队过往 | Asad Iqbal 2018 年在巴基斯坦拉合尔创办同名家教 marketplace Noodleseed（LUMS 校友，5000+ 节课程），后转型 AI 方向 | LinkedIn · Crunchbase |
| 总部 | Santa Clara, California | 加州公司注册 |
| 团队规模 | 1–10 人 / LinkedIn 2–10 人 | Crunchbase / LinkedIn |
| 融资 | Crunchbase 显示有融资轮次但金额与投资方被 Pro 墙遮蔽；官网展示"Backed by leaders at Meta and Arm" | Crunchbase · 官网 |
| 加速器 | 未查到 | — |
| 合规认证 | 提到 SSO、SCIM、审计导出在 Enterprise 档；具体认证（SOC2 等）未查到 | 定价页 |

## 定价 / 商业模式

| 档位 | 价格 | 关键限额 |
|---|---|---|
| Free | $0 永久 | 1M MCP 调用/月、1 个生产 app、本地开发免账号、托管部署 |
| Pro | $30/月（年付 2 个月免费） | 10M 调用/月、5 个生产 app、团队访问、托管 secrets、部署历史 + 回滚、邮件支持 |
| Scale | $300/月（年付 2 个月免费，官方"推荐"档） | 100M 调用/月、25 个生产 app、自定义域名、策略 + audit log、release history + 回滚、优先支持 |
| Enterprise | 定制 | 自定义限额、SSO/SCIM/审计导出、私有连接、专属部署、合同 SLA + 实施支持 |
| 实施服务 | Discovery $1,500 / Launch bundle 至多 $15,000 / Enterprise enablement 起 $25,000 | — |
| 超量 | $5 / 每 100 万次调用（Pro/Scale，月度开票） | — |
| 支付 | Stripe | — |
| 推广 | Product Hunt 上榜当周，年付 Pro 或 Scale 赠送上手工程支持 | — |

## 关联信息 / 生态

- **自有客户清单**（官网 logo 墙）：Rawan、Epik、Kitchen OS、Jettly、Layla、Heymate、Slotted、Commerce OPS Studio。
- **数据声明**：官网 "Trusted by 2,000+ teams building with Noodle Seed"；产品页 "1K followers"。
- **位置**："#1 developer in the ChatGPT app directory"、"Used to build more ChatGPT apps than any other company"（官网自述，未给具体数据来源）。
- **可比产品**（PH 列出）：Claude by Anthropic、Pickaxe、Agentplace、Taskade、CometChat Agent Platform。
- **历史同名词**：2012–2014 年 Ben Lang 联合创办的应用发现平台"App.net / Noodle Seed"已关闭（同名巧合，非延续关系）；2018 年 Asad Iqbal 在拉合尔创办的家教 marketplace"Noodleseed"（beta 阶段、5000+ 课次），后转型为本次 AI 产品。
- **相关 GitHub 项目**：`fahd-noodleseed/perplexity-mcp-server`（TypeScript，Apache-2.0，1 star），Perplexity API 的 MCP server 封装，提供 perplexity_ask / perplexity_reason / perplexity_research 三个工具；fork 自 `cyanheads/mcp-ts-template`。

## 技术时间线（官网 + PH 里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-01-19 | Noodle Seed 首次登陆 PH，当日 #1 / 当周 #5 |
| Halo 上线（≈ 2025 年底/2026 年初） | 嵌入式 AI chat widget，"一行 script、5 分钟部署"（社区帖） |
| 2026-07 | "Introducing Discovery"：回应客户最高频问题的新版本（社区帖） |
| 2026-09-09 | 第二次 PH 上榜，本档案对应这次 |

## 评论区反馈（事实摘录，不评价）

- **Fahd Rafi（M）**：分享个人决策——"I never purchase any software that doesn't already have an MCP connector for my Claude or Codex"；点明行业新基线。
- **Fahd Rafi（M）**：定义"代理化 SaaS"的共同积木——MCP skills、credential brokering、OAuth、rate limiting。
- **Fahd Rafi（M）**：明确整条栈的目标是"用你自己的 Claude Code / Codex / AI 编码工具就能搭"。
- **Fahd Rafi（M）**：UI 设计的取舍——"最可控的确定性来自小而 minified 的 UI 元素，能直接随请求送到用户面前"。
- **Fahd Rafi（M）**：判断——"对话不只是演化成新的搜索界面，而是演化成双向的、可交易的界面"。
- **Asad Iqbal（M）**：解释做这个产品的原因——"一个有用的 workflow 很快变成基础设施项目"。
- **Asad Iqbal（M）**：技术细节——react UI 以 html/js 打包，被支持 MCP Apps 的客户端在沙箱 iframe 里渲染。
- **Hassan Iftikhar（M）**：内置 knowledge base 文档作为助手护栏。
- **Ebere Ukoh（M）**：客户想要的不是 workflow，而是结果——"let me check inventory and place an order from ChatGPT"。
- **Shayma El Omri（M）**：最强的对话 workflow 是目标导向、可用自然语言描述的那种。
- **MD Amirul Islam（用户）**：能不能支撑更复杂的购买/下单流程？
- **Tanjum（用户）**：业务方对助手回复有多少控制？能不能为品牌表达设护栏？
- **Harini Mukesh（用户）**：让现有产品被 AI 使用、又不用围绕 agent 重写整套，思路有意思。
- **Monir（用户）**：如果对话演化成新"搜索界面"，这就是个顺理成章的方向。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/noodle-seed（基本盘、tagline、maker 列表、30 条评论与创始人回复全文、Similar Products、第二次上榜历史）
- 官网首页：https://noodleseed.com（产品描述、Connect→Authorize→Operate→Prove 四步、信任信号、客户 logo 墙、Meta/Arm 背书）
- 定价页：https://noodleseed.com/pricing（4 档定价、超量费、PH 推广、Stripe）
- 文档站：https://docs.noodleseed.dev/docs（`@noodleseed/one` SDK、Zod schema、server.ts 示例、本地开发命令、Apache-2.0、Node 24+、平台支持矩阵）
- Blog：https://noodleseed.com/blog/halo-ai-chat-widget-every-website（Halo widget 介绍）
- Apps 目录：https://noodleseed.com/apps（Agent connectivity infrastructure 入口）
- npm：https://www.npmjs.com/package/@noodleseed/one（包元数据）
- GitHub：https://github.com/fahd-noodleseed/perplexity-mcp-server（TypeScript、Apache-2.0、1 star，Perplexity MCP server 封装，fork 自 cyanheads）
- Crunchbase：https://www.crunchbase.com/organization/noodle-seed（AI 实体：Santa Clara、Asad Iqbal + Fahd Rafi、有融资轮次但细节被 Pro 墙遮蔽）
- LinkedIn（公司页）：https://www.linkedin.com/company/noodle-seed（2–10 人）
- LinkedIn（Asad Iqbal）：https://pk.linkedin.com/in/asad-iqbal-noodleseed（巴基斯坦 LUMS 校友，2018 创办同名家教 marketplace）

## 未查到 / 待补

- 融资轮次金额、领投方、其他跟投方（Crunchbase 显示有轮次但被 Pro 付费墙遮蔽）。
- 是否已通过 SOC2、ISO 27001 等合规认证（Enterprise 档提到 SSO/SCIM，但无具体审计报告链接）。
- 2000+ teams / #1 ChatGPT app directory 数据的统计口径（时间窗口、是否含自注册）。
- Ben Lang 在本次 PH launch maker 列表里的具体角色（顾问 / 投资人 / 出镜帮忙——官网与 PH 页未注明）。
- 公司公开的 GitHub 组织页（`github.com/noodleseed` 或 `github.com/fahd-noodleseed` 其他仓库目前只查到 perplexity-mcp-server 一个仓库）。
- 与 Mastra Factory（PH 当日 #1，同为 MCP / Agent 基础设施）的功能差异未在公开资料里直接对比。
