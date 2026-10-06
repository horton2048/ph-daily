---
product: "AI Observability by OpenObserve"
slug: "openobserve"
date: "2026-09-10"
rank: 1
votes: 187
comments: 64

category: "开发者工具 / AI 基础设施 / 可观测性"
subcategory: "LLM/Agent 可观测性 + 质量评估（OpenTelemetry 原生）"
tags: ["开源", "AGPL-3.0", "OpenTelemetry", "LLM Observability", "Agent 追踪", "LLM-as-a-judge", "Rust", "Parquet", "DataFusion", "S3", "AI SRE", "MCP", "自托管", "SOC2"]

tech_stack: ["Rust", "TypeScript / Vue", "Apache Parquet", "Apache DataFusion", "OpenTelemetry", "S3-native 对象存储", "单二进制部署"]
platform: ["Self-hosted（单二进制 / Kubernetes / Terraform）", "Cloud（AWS us-west、eu-central-1 法兰克福、ap-south-1 孟买；Azure us-west-2）", "Enterprise（BYOC / BYOB）"]
open_source: true
license: "AGPL-3.0（开源核心）；Cloud / Enterprise 为商业许可"

business_model: "开源核心 + 按用量计费 Cloud + Enterprise 自定义"
pricing_start: "自托管开源版免费；Cloud Professional $0.50/GB 摄入 + $0.01/GB 查询（保留期已含），14 天免费试用；Enterprise 联系销售"
funding_stage: "Series A（2026-04-28 官方公告）"
funding_amount: "A 轮 $10M（Nexus Venture Partners + Dell Technologies Capital 领投）；更早期种子轮金额未在官网核实"

related_products:
  - "Langfuse / Helicone / LangSmith / Arize Phoenix（LLM 专项可观测性，官方博客标签体系里有对标）"
  - "Datadog / New Relic / Splunk / Dynatrace / Dash0（商业 APM，官网有逐个对比页）"
  - "Elasticsearch / ELK 栈（存储成本对比基准）"
  - "Grafana LGTM 栈（查询性能对比基准）"
  - "SigNoz / HyperDX / Coroot（开源 APM 直接竞品）"

maker_previous:
  - "Prabhat Sharma（创始人 & CEO，前 AWS Solutions Architect）——公司 2022 年成立"
  - "团队与 ZincSearch（Elasticsearch 替代搜索引擎）的前身关系：多处二手资料如此描述，官网 About 页未直接印证，标注待复核"

key_signals:
  - "LLM span 与底层基础设施 span 共用同一条 trace、同一个存储：官网 LLM 页给的实例是「这条 trace 有 41% 耗时是 Postgres 锁等待，不是模型；专做 LLM 的工具不携带这条 span」"
  - "不止记录「跑了没」，还打分「跑得好不好」：线上 LLM-as-a-judge（用你自己的模型 API key）+ 上线前离线实验对比 + 人工标注沉淀数据集；分数直接落在 span 上，可按 span/trace/session 三种粒度评分"
  - "AGPL-3.0 开源核心，21.7k GitHub stars、9,000+ 活跃部署、单客户日均 5 PB 遥测；官方基准：对 Elastic 140x 存储效率与 30x 计算效率，对 Datadog 8x 成本，对 Grafana 栈 5-15x 查询速度"
  - "Cloud 定价 $0.50/GB 摄入 + $0.01/GB 查询且保留期已含；但 AI SRE、AI Assistant 等 AI 能力划在 Enterprise 档且标注 Preview——开源自托管版拿不到"

archived_at: "2026-09-10"
sources_count: 9
---

# AI Observability by OpenObserve · 扩展阅读上下文

> PT 2026-09-10 Product Hunt 榜单第 1 · 👍 187 · 💬 64  
> 归档日期 2026-09-10 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | AI Observability by OpenObserve（PH 当日主打模块名为 "AI Observability"，底层平台为 OpenObserve） |
| 英文 tagline | OpenTelemetry-native observability for agents and LLMs |
| 中文 tagline | 为 Agent 和 LLM 而生的 OpenTelemetry 原生可观测性 |
| 官网 | https://openobserve.ai |
| 模块页 | /ai-observability/ · /llm-observability/ · /ai-sre/ · /ai-assistant/ · /mcp-server/ |
| PH 页 | https://www.producthunt.com/products/openobserve |
| GitHub | https://github.com/openobserve/openobserve |
| 品类标签 | Developer Tools · Artificial Intelligence · Tech |
| 票数 / 评论 | 187 / 64 |
| 公司主体 | OpenObserve Inc.（成立于 2022 年） |
| 总部 | 3000 Sand Hill Rd, Building 1, Suite 260, Menlo Park, CA 94025（官网页脚） |
| 合规 | SOC2 Type II Certified（官网页脚标注） |
| 创始人 | Prabhat Sharma（前 AWS Solutions Architect） |

## 是做什么的（如实复述，不评价）

OpenObserve 是一个**统一的开源可观测性平台**，把日志（logs）、指标（metrics）、追踪（traces）、前端监控（RUM / Session Replay）、合成监控、管道、告警与事故管理、SLO 放在同一个后端里。

今天 PH 上线的 **"AI Observability"** 是这个平台上专门面向 LLM / Agent 工作负载的能力集。官网把它定义成三步，原文措辞是 Monitor / Evaluate / Improve：

1. **Monitor（看它做了什么）**——每一次 prompt、工具调用、agent 交接都被记成一个 OpenTelemetry span，span 上挂 token 数、按你自己的模型价目表算出的成本、延迟。多步 / 多 agent 的运行通过 W3C context propagation 拼回一整条 trace，再按 session ID 归并成一次完整对话。
2. **Evaluate（判断它做得好不好）**——对输出打分：相关性、幻觉、毒性、偏见。既能在生产流量上实时打分（LLM-as-a-judge，用你自己的 provider key，或接你自己的 HTTP 打分服务），也能在上线前拿数据集跑离线实验、两次运行并排对比。
3. **Improve（让它变好）**——人工标注复核，把复核结果蒸馏成数据集，再对比实验版本决定推哪个上线。

官网对自己的差异化表述很直白：「纯评估工具跳过了基础设施，APM 套件跳过了质量，OpenObserve 两件事在同一个存储里做。」

## 解决什么问题（事实层面，不判断值不值得解）

- **「HTTP 200 的幻觉」**：官网原话——一个 AI 应用可以返回一个又快又没报错、但完全错误的答案。传统 APM / 追踪工具捕获延迟、错误、token 数，但「幻觉返回的是 HTTP 200」，监控这一层答不出「答案对不对」「这次发版比上次好了吗」。
- **专做 LLM 的工具看不见底层**：官网 LLM 页给的具体例子——某条 support-agent trace 共 14 个 span、8.42 秒、$0.0412，其中 **41% 的耗时是 Postgres 锁等待，而不是模型**。原话是「专做 LLM 的工具不携带这条 span」。
- **遥测存储成本**：传统栈（ELK、Datadog、Splunk）要么按主机 / GB 计价昂贵，要么运维复杂。官网主张「成本本身是一个功能」，让「全量留存成为默认，而不是奢侈品」。
- **告警到根因之间的人力**：AI SRE 面向的是「告警响了之后没人能立刻查」——目标是让工程师醒来时看到的是根因，而不是原始遥测。

## 怎么做的（技术原理 / 机制，事实层面）

**存储与查询底座**

- **存储**：Apache Parquet 列式存储 + S3-native 对象存储。官网强调**不建索引**——原话「没有索引要建，所以没有东西需要付两次钱」。
- **查询引擎**：Apache DataFusion（Rust 编写的列式查询执行器），与 Parquet 同栈，无 JVM 依赖。
- **语言 / 部署**：核心 Rust 编写，单二进制部署；另有官方 Terraform provider 与 Kubernetes module。仓库语言构成为 TypeScript 32MB / Rust 25MB / Vue 15MB——前端占比大是因为自带完整 UI。
- **官方基准数字**（/ai-sre/ 页 Benchmarks 区块，均声明为「对具名厂商实测，非行业均值」）：对 **Elastic 140x 存储效率**、**30x 计算效率**；对 **Datadog 8x 成本效率**；对 **Grafana 栈 5-15x 查询速度**。

**AI / LLM 观测机制**

- **OpenTelemetry 原生，无需重新埋点**——官网反复强调 "no re-instrumentation"，直接消费既有 OTel SDK / collector 输出。
- **span 上的字段**：`gen_ai.input_messages`（模型实际收到的 prompt 原文）、`gen_ai.output_messages`、模型参数、token 数、`cost_total`、错误，以及评估分数（官网示例 `faithfulness 0.91`）。
- **成本按调用算，不按月算**：输入 / 输出 token 成本用你自己的模型价目表算到每个 span 上——官网原话「贵的那一步是一行可以排序的数据，而不是账单上的一行」。
- **执行图（Agent Graph）**：把 trace 还原成 planner → 各 agent → 工具调用 → synthesizer 的可点击节点图，失败的交接是一个节点而不是一条要翻找的日志。
- **评分粒度**：span（单次调用）/ trace（一次完整运行）/ session（整段对话）三选一；每个评分配置自带阈值，所以分数读出来是一个「判定」而非裸数字。
- **数据不出域**：自托管或跑在自己的云里，摄入时可脱敏、字段级掩码——官网原话「你的 prompt 是你客户的数据」。

**AI SRE（标注 Preview）**

- 告警触发的瞬间就开始调查，而不是等人开工单。
- 通过 **MCP** 调用 OpenObserve 自己的工具链，「和人操作 UI 的方式一样，只是它不会漏步骤」。
- **自带你自己的 AI provider**：接你自己的 LLM API key，安全、治理与开销由你控制。
- 输出结构化发现：诊断、根因、修复方案，附完整证据链（相关日志 / trace / 指标、服务拓扑图、事件时间线），可回溯它分析了哪些数据、怎么得出结论。
- 关联历史事件，每次事故进入知识库。

**生态集成**（据官方博客标签体系）：LangChain、LlamaIndex、CrewAI、OpenAI Agents SDK、Claude Agent SDK、n8n、Amazon Bedrock 等。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Prabhat Sharma（前 AWS Solutions Architect） | 官网 / 公开资料 |
| 成立时间 | 2022 年 | openobserve.ai/about/ |
| **A 轮（2026-04-28）** | **$10M**，**Nexus Venture Partners + Dell Technologies Capital 领投**，与 Observability 3.0（AI SRE / 异常检测 / LLM observability）同日发布 | openobserve.ai/whats-new/（官方） |
| 早期种子轮 | 二手资料称 $3.6M-$4M（Nexus 领投，Dell Tech Capital 等跟投）——**本次未在官网核实，待复核** | 二手 |
| 团队规模 | 官网未披露 | — |
| 合规认证 | **SOC2 Type II Certified** | 官网页脚 |
| 加速器 | 未查到（有二手资料称 YC，本次未获任何一手证据，**不采信**） | — |

## 定价 / 商业模式

官网口号：「按 GB 计费，无按主机、无按席位费用。」

| 档位 | 价格 | 关键内容 |
|---|---|---|
| **自托管开源版（AGPL-3.0）** | 免费 | 单二进制；开源核心（logs / metrics / traces / RUM / pipelines 等） |
| **Cloud Professional** | **$0.50/GB 摄入 + $0.01/GB 查询**，按月计费（价格含年付 30% 折扣） | Logs、Metrics、Traces、RUM、Session Replay、Error tracking；**保留期已包含**：指标 15 个月，非指标（日志 / trace 等）30 天；14 天免费试用，无需信用卡 |
| **Enterprise** | Custom，联系销售 | 额外保留期、**BYOB 无限保留（自带存储桶）**、Pipelines、敏感数据脱敏、**AI 驱动可观测性**、**事故管理 & AI SRE Agent**、AI Assistant、审计日志、不限用户数、SSO、RBAC、高级支持、公有云或 BYOC 部署、架构评审、量价折扣、SLA |

> **值得注意的商业设计**：AI SRE、AI Assistant、AI-Powered Observability 都列在 **Enterprise 档**，且 AI SRE 页面标注 **Preview**。开源自托管版拿不到这几项。
>
> 官网成本估算器示例：日摄入 1 GB/天 → Datadog 估算 $140/月 vs OpenObserve Cloud $15/月，标注「省 89%」。官网另提供 Datadog Bill Analyzer 与 Dynatrace Bill Analyzer 两个上传账单估算省钱的工具。

## 关联信息 / 生态

- **开源核心协议**：AGPL-3.0——可自由使用改造，但以网络服务形式提供修改版时须开源。仓库 `openobserve/openobserve`，2023-02-02 创建。
- **规模数字**（存在口径差异，如实并列）：GitHub **21,712 stars / 1,075 forks**（本次 API 实测）；官网 About 页称 **9,000+ 活跃部署**、**5 PB/天** 数据处理、21.5K stars；官网首页则写 **+10K enterprises**——两处口径不一致，未见统一说明。
- **对比矩阵**：官网设有 vs Datadog / Splunk / New Relic / Grafana / Dynatrace / Dash0 六个对比页。官方博客标签里同时存在 **Langfuse、Helicone、LangSmith、SigNoz、ClickHouse、Mimir**，说明 LLM 专项工具也在其对标视野内。
- **MCP**：既有独立的 MCP Server 模块（让外部 AI agent 通过 MCP 查询可观测数据），AI SRE 内部也通过 MCP 调用平台自身工具。
- **客户背书**：DevZero CEO Debo Ray——「OpenObserve 帮我们在一小时内完成了从 Datadog 的迁移……可观测性成本降低 4 倍。」

## 技术时间线（官方 What's New 页，2026 年）

| 日期 | 事件 |
|---|---|
| 2022 | 公司成立 |
| 2023-02-02 | GitHub 仓库 `openobserve/openobserve` 创建 |
| 2026-03-15 | Datadog Bill Analyzer 上线；Azure US West 2 区域上线（Azure Marketplace 统一计费） |
| 2026-03-16 | AWS EU-Central 1（法兰克福）区域上线（GDPR / 数据主权） |
| **2026-04-28** | **$10M A 轮（Nexus + Dell Tech Capital 领投）+ Observability 3.0 发布**（AI SRE、异常检测、LLM observability） |
| 2026-05-12 | **BYOB（自带存储桶）**——接自己的 S3 / Azure Blob，数据留在自己账户下 |
| 2026-05-14 | Terraform Provider + Kubernetes Module |
| 2026-06-02 | AWS ap-south-1（孟买）区域上线 |
| **2026-06-23** | **v0.91.0 重大版本**——UI 重设计 + **AI agent observability，含 MCP 协议支持、agent 追踪、平台内置 AI 辅助** |
| 2026-07-16 | GitHub stars 突破 **20,000**（官方公告） |
| 2026-08-06 | 合成监控（Synthetic Monitoring，beta） |
| 2026-08-19 | SLO（含错误预算、多窗口燃尽率告警）、分组告警、Terraform/GitOps 双向支持 |
| **2026-09-10** | **v1.0.0-rc5 发布**（GitHub Releases，当日 11:08 UTC）；同日 "AI Observability by OpenObserve" 登陆 Product Hunt 并居当日第 1 |

## 评论区反馈（事实摘录，不评价）

> **未获取**。PH 产品页受 Cloudflare 人机校验拦截（返回 "Just a moment..." 挑战页），本次未能抓到 64 条评论正文。archive 数据仅含评论计数。待后续换浏览器类工具抓取后补充本节。**不做推断性描述。**

## 信息来源

- **GitHub API**：`api.github.com/repos/openobserve/openobserve` + `/languages` + `/releases/latest`——实测确认 AGPL-3.0 协议、21,712 stars / 1,075 forks、语言构成、仓库描述（含 140x 存储成本主张）、最新版本 v1.0.0-rc5（2026-09-10）。
- **官网首页** `openobserve.ai/`——140x / 30x 效率主张、AI SRE 与 agentic observability 演示、四大卖点、5 PB/天。
- **官网定价页** `openobserve.ai/pricing`——Cloud Professional $0.50/GB + $0.01/GB 查询、保留期、Enterprise 功能清单、vs Datadog/Splunk/Dash0 对比表、成本估算器。
- **官网 AI Observability 页** `openobserve.ai/ai-observability/`——Monitor/Evaluate/Improve 三段式定义、在线评估、离线实验、LLM-as-a-judge、人工标注、数据集、「幻觉返回 HTTP 200」论述。
- **官网 LLM Observability 页** `openobserve.ai/llm-observability/`——span 字段结构、Postgres 锁等待 41% 案例、agent 执行图、span/trace/session 评分粒度、W3C context propagation。
- **官网 AI SRE 页** `openobserve.ai/ai-sre/`——AI SRE 工作机制、MCP 自主调用、BYO LLM provider、证据链，以及 Benchmarks 区块三组对比数字。
- **官网 About 页** `openobserve.ai/about/`——2022 年成立、9,000+ 活跃部署、5 PB/天、21.5K stars、公司理念。
- **官网 What's New 页** `openobserve.ai/whats-new/`——2026 全年官方里程碑，含 A 轮 $10M（2026-04-28）与 v0.91.0 AI agent observability。
- **官网 Blog 页** `openobserve.ai/blog/`——标签体系印证竞品对标面（Langfuse / Helicone / LangSmith）与集成生态（LangChain / CrewAI / OpenAI Agents SDK / Claude Agent SDK / n8n）。
- **PH 产品页**（`producthunt.com/products/openobserve`）：**抓取失败**，Cloudflare 挑战页拦截。tagline / 票数 / 评论数 / 品类 / logo 取自本项目 archive 数据。

> **抓取方式说明**：本次 WebSearch 工具返回异常内容（非搜索结果），WebFetch 对 github.com 与 openobserve.ai 均被域名校验拦截，因此全部一手事实改由 curl 直取官网 HTML + GitHub REST API 获得。以上数字均为直接实测，非搜索摘要转述。

## 未查到 / 待补

- **PH 评论区 64 条正文**（提问 + 创始人回复要点）——Cloudflare 拦截，待换工具抓取
- **早期种子轮的确切金额与时间**——官网 What's New 未收录，二手资料称 $3.6M-$4M，未核实
- **团队规模、ZincSearch 前身关系**——官网 About 页未提及，二手资料说法待复核
- **是否 YC 批次公司**——本次未取得任何一手证据，不采信二手「YC W22」说法
- **异常检测的具体算法**（统计 / 时序模型 / LLM）——官网未披露
- **AI SRE 何时脱离 Preview、是否会下放到非 Enterprise 档**——未披露
- **内置 LLM-as-a-judge 的默认评分模型与提示词**——官网只说「用你自己的 provider key」，未说默认实现
- **与 Langfuse / Helicone / Arize Phoenix 的逐项功能 / 价格对比**——官网对比页只到 Datadog/Splunk/New Relic/Grafana/Dynatrace/Dash0，LLM 专项工具仅在博客散见
- **140x / 30x / 8x / 5-15x 各基准的具体测试条件**（数据量、查询模式、保留期）——官网称有 case study，未展开核验
- **9,000+ 部署与 10K+ enterprises 的口径差异解释**、Fortune 100 客户具体名单
