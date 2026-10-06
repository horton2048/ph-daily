---
# 结构化元数据（用于索引和聚合）
product: "Mastra Factory"
slug: "mastra-factory"
date: "2026-09-09"
rank: 1
votes: 320
comments: 71

# 分类标签
category: "开发者工具"
subcategory: "AI agent / 软件交付自动化"
tags: ["开源", "TypeScript", "AI agents", "GitHub Actions 替代", "Y Combinator", "Apache 2.0", "SDLC 自动化"]

# 技术信息
tech_stack: ["TypeScript", "Node.js", "React", "Postgres + pgvector", "Redis (可选)", "Mastra 框架", "pnpm workspaces", "Turborepo", "Vitest"]
platform: ["Web", "CLI", "Mac", "Linux", "Self-hosted", "Cloud"]
open_source: true
license: "Apache 2.0 (核心) + Mastra Enterprise License (ee/ 目录)"

# 商业信息
business_model: "开源核心 + 云平台托管订阅 (Freemium → 团队订阅 → 企业定制)"
pricing_start: "免费 (自部署) / $0/月 Starter / $250/月 Teams / Enterprise 定制"
funding_stage: "A 轮"
funding_amount: "$35M 累计 (种子 $13M + A 轮 $22M)"

# 关联信息
related_products: ["GitHub Copilot", "Cursor", "Devin", "LangChain", "Replit Agent", "Spotify Xirp"]
maker_previous: ["Gatsby.js (Sam Bhagwat / Abhi Aiyer / Shane Thomas 三人是 Gatsby 核心团队)"]

# 速览信号（给 caption.md / INDEX.md 等下游用，避免整篇重读正文才能省 token）
key_signals: [
  "Mastra Factory 是 Mastra 框架的第四次 PH 上线，定位从'agent 框架'演进到'软件工厂'框架",
  "开源 (Apache 2.0) + 自部署 + Mastra Platform 云托管三档，云版 $0/$250/月/Enterprise 定制",
  "六道显式闸门：Intake → Triage → Planning → Building → Review → Done，每道闸门规则可配置",
  "团队 = Gatsby 三位联合创始人 + 35 人，YC W25，累计融资 $35M (Spark Capital 领投 A 轮)"
]

# 元信息
archived_at: "2026-09-10"
sources_count: 9
---

# Mastra Factory · 扩展阅读上下文

> PT 2026-09-09 Product Hunt 榜单第 1 · 👍 320 · 💬 71  
> 归档日期 2026-09-10 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Mastra Factory |
| 英文 tagline | From issue to production, run by agents. |
| 中文 tagline | 从 issue 到生产，全部由 agent 跑通。 |
| 官网 | https://mastra.ai/factory |
| PH 页 | https://www.producthunt.com/products/mastra/launches/mastra-factory |
| 模板仓库 | https://github.com/mastra-ai/softwarefactory-template |
| 品类标签 | Open Source · Developer Tools · Artificial Intelligence |
| 票数 / 评论 | 320 / 71 |
| 公司主体 | Mastra (YC W25) |
| 企业版/关联站点 | Mastra Platform (cloud) · Mastra framework (开源框架) · Mastra Studio |
| 主理人 PH 账号 | fmerian |

## 是做什么的（如实复述，不评价）

Mastra Factory 是一个**开源、由 agent 驱动的软件交付环境**——把"接 issue → 写代码 → 出 PR"这条 SDLC 流水线接到一个可配置的 web 应用里。具体形态：

- 用户连接 GitHub organization + 仓库（可选 Linear 项目 + 一个 model provider），打开 Factory UI；
- Factory 从接入源拉取 issues/PR，进入 **Intake → Triage → Planning → Building → Review → Done** 六道显式闸门；
- 每个闸门可配置规则、按 work type 分支；人在 Triage 阶段回答 agent 提问、在 Planning 阶段 review/编辑方案、在 Review 阶段决定是否合并 PR；
- 默认面向软件开发（feature、bugfix、refactor、写测试），但因代码开源且基于 Mastra 框架，可把 agents/tools/workflows/UI 复用到内容生产、研究、数据分析等其他多步流程；
- 部署方式二选一：本地 `npm create factory` 起项目后 `mastra deploy` 到 **Mastra Platform**（托管 auth / DB / sandbox），或完全自托管。

> 原话："Mastra Factory is an open source, agent-powered software delivery environment that combines persistent coding agents, repository workspaces, issue intake, planning, implementation, and pull request review in a web application you control."

## 解决什么问题（事实层面，不判断值不值得解）

- **SDLC 自动化"放养"困境**：goal-driven 单一 supervisor agent 拆任务容易失控；Mastra Factory 用 **staged automation + 学习基础设施**两条腿搭配——"explicit gates around intake, triage, planning, building, review, and completion"。
- **Coding agent 散落在个人终端**：现有 agent（Cursor / Copilot / Claude Code 等）跑在工程师个人 terminal 里，团队没法集中看到进展；Factory 把多个 agent 聚到一个共享 dashboard。
- **开源可控 vs. 托管省心二选一**：Spotify Xirp 等闭源竞品不让企业自托管；Mastra Factory 走"开源核心 + Mastra Platform 托管"双路径，企业可自托管也可上云。
- **传统 CI 不懂 issue**：传统 GitHub Actions 只在代码 push 后做事；Factory 从 issue 入口就开始介入，由 agent 完成 triage → plan → code → review。

## 怎么做的（技术原理/机制，事实层面）

- **Mastra 框架层**：Factory 直接构建在 Mastra 框架之上，复用其 typed workflows（`.then() / .branch() / .parallel()` 图式 workflow 引擎）、memory（对话历史 + RAG + "Observational Memory"）、scheduling、tools（MCP server 集成）、observability。
- **生命周期显式闸门**：六道 stage — Intake / Triage / Planning / Building / Review / Done——每道 stage 可定义规则、按 work type 分支。人在三处显式介入（Triage 答问、Planning 审方案、Review 决定是否合 PR）。
- **持久 coding agents**：Factory 用"durable background agents + shared state"，在后台长跑任务，不止一次性 LLM 调用。
- **托管依赖**：Factory 项目用 Mastra Platform 做 auth / database / sandbox；本地开发时 Mastra server / Factory UI / Studio 都跑在本地，部署时再 `mastra deploy`。需要 Postgres + pgvector（Docker compose 起），Redis 可选（分布式部署用）。
- **技术栈**：TypeScript + Node.js + React + pnpm workspace + Turborepo；测试用 Vitest，lint 用 Oxlint/Oxfmt。
- **可选全目标模式**：Factory 默认走 staged automation，但可"implement full /goal mode via subagents, durable background agents, and shared state"——目标驱动作为另一种可行配置。
- **可观测性**：`npm create factory` 出来的项目跑在 4111 端口（UI + API 同端口），事件 / CPU hours / retention 三项是云版主要计量。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Sam Bhagwat (CEO) · Abhi Aiyer (CTO) · Shane Thomas (CPO) | mastra.ai/about |
| 联合创始人背景 | 三人均为 Gatsby.js 核心团队；公司自我描述："We've been building open-source JavaScript for over a decade. Previously, we were the team behind Gatsby." | mastra.ai/about |
| 团队规模 | 35 人，San Francisco 总部，远程分布 | mastra.ai/about |
| 加速器 | Y Combinator W25 批次 | mastra.ai/about、PH 评论 |
| 种子轮 | $13M · 2025-10-08 · 领投 Y Combinator (Paul Graham) + Gradient Ventures · 跟投 SVAngel、Orange Collective、Runa Capital、basecase；个人天使 120+，含 Amjad Masad (Replit CEO)、Guillermo Rauch (Vercel)、Arash Ferdowsi (Dropbox)、Balaji Srinivasan | mastra.ai/blog/seed-round |
| A 轮 | $22M · 2026-04-09 · 领投 Spark Capital · 累计融资 $35M | mastra.ai/blog/series-a、mastra.ai/about |
| 客户 / 使用方 | Replit (Agent 3 每天生成 thousands of Mastra agents)、SoftBank ("restoring Japan's white-collar productivity")、Sanity ("Content Agent")、Marsh (LenAI agentic search)、Brex、Salesforce、Adobe、MongoDB、Workday、Indeed、Appwrite、Revolte、Superset | mastra.ai/factory |

## 定价 / 商业模式

**双轨制**：开源核心可完全自托管免费；Mastra Platform 云托管按用量分三档。

| 档位 | 价格 | 主要配额 | 备注 |
|---|---|---|---|
| 自部署 | $0 | — | Apache 2.0 开源，本地起 `npm create factory` 即可 |
| Starter（云） | $0/月 | 100K observability events（+$10/100K）· 24 CPU hours（+$0.35/hr）· 15 天 retention · unlimited users/deployments/projects | 免费层 |
| Teams（云） | $250/月 | 1M observability events（+$8/100K）· 250 CPU hours（+$0.25/hr）· 6 月 retention · multiple teams · SSO · SOC 2 docs | 标准团队档 |
| Enterprise（云） | 定制 | 容量与 retention 定制 · RBAC · audit logs · uptime SLA · dedicated engineer | 企业档 |

商业模式重点：**核心永远开源可自部署**；云版靠用量 + 团队规模 + 企业合规分层收钱。npm 包 `create-factory` v0.1.12，约 3.3K weekly downloads；母框架 `npm create mastra@latest` 据 PH 评论周下载 300K+。

## 关联信息 / 生态

- **Mastra 框架本身**：Apache 2.0 开源 TypeScript AI agent 框架，GitHub 27.9K stars / 2.7K forks / 19,108 commits，"the third-fastest-growing JS framework ever"。模型路由接 40+ provider；workflow 图式引擎；human-in-the-loop suspend/resume；MCP server authoring；Observational Memory；built-in evals + observability。话题标签：agents / ai / chatbots / evals / javascript / llm / mcp / nextjs / nodejs / reactjs / tts / typescript / workflows。
- **Mastra 平台产品**：Mastra Studio（IDE 类）· Mastra Server（运行 runtime）· Memory Gateway（记忆/检索层）——三者构成本次 Factory 落地的托管底座。
- **同系列 PH 上线**：这是 Mastra 第 4 次 PH 上线；前 3 次分别是 Mastra 框架首发、Mastra 1.0（2026-01-21，含 19,400+ stars / 300K weekly npm 数据）、Mastra Code（2026-02-27）。
- **竞品对照**：
  - **闭源同类**：Spotify Xirp（Maker 公开点名对标，区别是 Xirp 闭源、Mastra Factory 开源可配置）、Devin（Cognition，闭源）；
  - **AI IDE 类**：Cursor、Replit Agent 3；
  - **框架层**：LangChain（Python 优先，Mastra 强调 TypeScript-first 对比）。
- **可复用方向**：Factory 因开源 + 基于 Mastra，agents/tools/workflows/UI 可复用到内容生产、研究、数据分析等多步流程。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2024 | Sam Bhagwat 创办 Mastra，公司"started in 2024" |
| 2025-10-08 | 完成 $13M 种子轮（YC + Gradient + 120+ 天使） |
| 2026-01-21 | Mastra 1.0 在 PH 上线（PH 第 2 次上线），宣布 19,400+ GitHub stars、300K+ weekly npm |
| 2026-02-27 | Mastra Code 在 PH 上线（PH 第 3 次上线） |
| 2026-04-09 | 完成 $22M A 轮（Spark Capital 领投），同日上线 Mastra Platform（Studio / Server / Memory Gateway） |
| 2026-09-09 | Mastra Factory 在 PH 上线（PH 第 4 次上线），拿下 #1 / 320 票 / 71 评论 |

## 评论区反馈（事实摘录，不评价）

**Maker 评论（fmerian）**：

> "Mastra (YC W25) is building an agent-powered software factory, and it's open source. What's a software factory? It's a system for agents to take software from issue into production. @Spotify recently launched Xirp. @Mastra's is open source and configurable."

Maker 还引了两位客户的话：

> Eldad Fux（Imagine / Appwrite）："Mastra helps us coordinate specialized agents and reliably turn high-level intent into structured execution. Their focus on developer experience and composability made it possible for us to move fast without sacrificing correctness."

> flyakiet（Superset）："Mastra is an amazing framework and an amazing product. It makes developing agents seamless."

**评论摘要**：

- 第三方引用 Rajagopalan Raghavan（Revolte）："Mastra's modern TypeScript stack gave us type safety, real workflow control, and structure we could actually build a platform on, without the sprawl and glue code that slows other frameworks down."
- Joseph Walker：评价 Mastra "turns AI agents from simple coding assistants into a full, open-source software delivery workflow"；同时提到 "The learning curve could be smoother, especially for beginners."
- Maker 致谢团队：calcsam（Abhi Aiyer）、smthomas3（Shane Thomas）、bookercodes（Alex Booker，DevRel）。

## 信息来源

- **PH 产品页**：https://www.producthunt.com/products/mastra/launches/mastra-factory （launch rank #1、votes 320、comments 71、tagline、Maker fmerian）
- **PH 论坛/历史 launch**（前三次上线）：https://www.producthunt.com/products/mastra/posts/mastra-1-0-reasoning ；https://www.producthunt.com/products/mastra/launches/observational-memory-by-mastra
- **Mastra Factory 官方介绍**：https://mastra.ai/factory （六道闸门、staged automation + 学习型基础设施定位、定价三档、客户引用）
- **Mastra 官方博客**："Announcing Mastra Factory" — https://mastra.ai/blog/announcing-mastra-factory ；"How to Build an AI Software Factory with AI Agents in TypeScript" — https://founders@mastra.ai/blog/software-factory
- **A 轮官宣**：https://mastra.ai/blog/series-a （$22M / Spark Capital / 2026-04-09）
- **种子轮官宣**：https://mastra.ai/blog/seed-round （$13M / 2025-10-08 / YC + Gradient + 120+ 天使）
- **团队页**：https://mastra.ai/about （35 人名单、$35M 累计、Gatsby 出身）
- **GitHub 主框架**：https://github.com/mastra-ai/mastra （27.9K stars、Apache 2.0 + Enterprise License 双协议、TypeScript / pnpm / Turborepo / Vitest 技术栈）
- **GitHub Factory 模板**：https://github.com/mastra-ai/softwarefactory-template （`npm create factory` 克隆此仓库）
- **npm 包**：https://socket.dev/npm/package/create-factory （v0.1.12，约 3.3K weekly downloads）
- **第三方报道**：https://openorchestrators.org/news/mastra-series-a-agent-platform 、https://faq.com.tw/zh/developer-tools/2026-04-10-mastra-22m-series-a-typescript-agents-zh

## 未查到 / 待补

- **Mastra Factory 独立 Apache 2.0 LICENSE 文件**：GitHub 主仓库是 Apache 2.0 + Enterprise 双协议；Factory 模板仓库（mastrab-ai/softwarefactory-template）的 LICENSE 未在本次抓取中确认是 Apache 2.0 还是其他（官网 FAQ 只说"yes, open source"，未明示协议）。待补：克隆模板仓库看根目录 LICENSE 文件。
- **PH 71 条评论具体内容**：本次只拿到 Maker 帖 + 2 条客户引用 + 2 条评论摘要，其余 65 条评论未拉取。待补：直接抓 PH launch 页面 comments 区。
- **Spotify Xirp 详细信息**：Maker 用作对标，但 Xirp 本身的产品形态、发布时间、定价本次未深查。
- **Mastra Factory 自我标榜的 usage 数据**（如"agents 跑通多少 issue""PR 通过率"等具体指标）：官网未披露。
- **PH 评论区具体技术提问细节**（如关于 Memory / pgvector schema / WorkOS 集成问题）：未抓到原文，待补。
- **Gatsby 三位联合创始人离开 Gatsby 的具体时间和原因**：本次未查；公司自述是 Gatsby 核心团队但没写离职节点。
