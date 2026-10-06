---
# 结构化元数据（用于索引和聚合）
product: "Cronloop"           # 产品名（PH 上为 "Cronloop AI"，官网及 footer 自称 Cronloop）
slug: "cronloop-ai"           # PH slug（文件名用）
date: "2026-08-19"            # 上榜日期
rank: 10                      # 榜单排名
votes: 106                    # 票数
comments: 1                   # 评论数

# 分类标签
category: "AI agent"          # 主品类
subcategory: "agent 编排/定时调度"  # 子品类
tags: ["MCP", "Codex", "Claude Code", "BYOK", "定时调度", "agent 编排"]

# 技术信息
tech_stack: ["MCP server", "OAuth custom connector", "沙箱运行环境", "Tailwind CSS v4"]  # 具体后端语言未披露
platform: ["Web", "MCP"]      # 平台：Web SaaS + 暴露标准 MCP server
open_source: false            # 闭源，未见公开仓库
license: ""                   # 闭源，无开源协议

# 商业信息
business_model: "Freemium（订阅制 + BYOK）"  # 调度层收订阅费，模型 token 走用户自有订阅/API key
pricing_start: "$0/月（Free）"  # 起步价
funding_stage: "未披露"       # 融资阶段未披露
funding_amount: ""            # 无披露

# 关联信息
related_products: ["Vapi", "AgentQL", "Lindy", "AutoGPT", "Cron"]  # 定时/循环 agent 调度与自动化编排类
maker_previous: []            # 创始人过往产品未查到

# 速览信号
key_signals:
  - "用 Markdown 写任务、选 Codex 或 Claude Code 当运行时，agent 每 5 分钟到每周循环跑一次，运行间保留持久记忆"
  - "BYOK：模型 token 走用户自己的 ChatGPT/Claude 订阅或 OpenAI/Anthropic API key；Cronloop 只收调度费——Free $0（每小时一次/200分钟/月），Pro $25/月（每 5 分钟一次/无月分钟上限）"
  - "暴露标准 MCP server（app.cronloop.ai/v1/mcp），可从 ChatGPT/Claude 里 OAuth 直连管理 agent，无需复制 API key"
  - "母公司 Cactal, Inc.；闭源 SaaS，无公开 GitHub 仓库"

# 元信息
archived_at: "2026-08-20"     # 归档时间戳
sources_count: 2              # 官网首页 + 官网定价区块（PH 页被 Cloudflare 拦截未取到）
---

# Cronloop AI · 扩展阅读上下文

> PT 2026-08-19 Product Hunt 榜单第 10 · 👍 106 · 💬 1  
> 归档日期 2026-08-20 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Cronloop（PH 榜单名 "Cronloop AI"） |
| 英文 tagline | AI agents that run in a loop |
| 中文 tagline | 循环运行的 AI agent |
| 官网 | https://cronloop.ai （应用 https://app.cronloop.ai） |
| PH 页 | https://www.producthunt.com/products/cronloop-ai |
| 品类标签 | SaaS · Software Engineering · Artificial Intelligence |
| 票数 / 评论 | 106 / 1 |
| 公司主体 | Cactal, Inc.（官网 footer "© 2026 Cactal, Inc."） |
| 企业版/关联站点 | MCP 端点 https://app.cronloop.ai/v1/mcp |

## 是做什么的（如实复述，不评价）

Cronloop 是一个让 AI agent 按固定时间间隔循环运行（"run in a loop"）的调度平台。用户用纯 Markdown 描述任务，选择 Codex 或 Claude Code 作为 agent 运行时，设定从每 5 分钟到每周一次的执行节奏；每次运行实时可见，且 agent 在运行之间保留持久记忆（durable memory）。

每次运行在一个全新沙箱中启动，agent 可在其中安装任务所需的任何依赖。用户可接入团队已有的软件（Gmail、HubSpot、Zendesk、Notion、Linear、GitHub、Stripe 等数十种），或从目录中添加 skill。官网强调"只要它有 API、MCP 或 CLI，你的 agent 就能用"。

此外 Cronloop 暴露一个标准 MCP server，用户可在 ChatGPT 或 Claude 里把 Cronloop 添加为 custom connector，用自然语言直接创建/暂停 agent、查看运行、回顾失败，无需打开 Cronloop 控制台。

## 解决什么问题（事实层面，不判断值不值得解）

- agent 能一次性完成任务，但很多真实工作需要**反复持续运行**（每 5 分钟查工单、每 30 分钟外呼、每天早上看数据、每小时处理 issue 转 PR）
- 自建定时 agent 需要搞定调度器、沙箱、记忆持久化、OAuth、监控——Cronloop 把这一整套托管掉
- 模型调用成本随循环跑而累积；Cronloop 让模型 token 走用户已有的 ChatGPT/Claude 订阅或自带 API key，只在调度层收费

## 怎么做的（技术原理/机制，事实层面）

- **运行时选择**：每个 agent 指定 Codex 或 Claude Code 作为执行引擎；模型用量走用户自有 provider 订阅或 API key，不经 Cronloop 转售
- **调度**：Free 版最快每小时一次，Pro 版最快每 5 分钟一次；每次单次运行 Free 上限 10 分钟、Pro 上限 60 分钟
- **持久记忆**：每个 agent 在运行之间携带 memory，可经 MCP memory_read/memory_write/memory_clear 读写
- **沙箱**：每次运行在全新沙箱启动，agent 可自行安装依赖
- **MCP server**：标准 OAuth 登录接入（无 key 复制）；暴露 agents_* / runs_* / secrets_* / memory_* / configuration_* 等工具，可被任何支持 remote MCP server 的客户端（Claude、ChatGPT）调用
- **集成目录**：覆盖 CRM/客服/协作/代码/支付/分析/社媒等大类（Gmail、Apollo、HubSpot、Zendesk、Intercom、Notion、Linear、Jira、GitHub、GitLab、Vercel、Stripe、QuickBooks、Semrush、Search Console、Buffer、X、TikTok 等）

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | 未查到 | 官网未披露；PH 页被 Cloudflare 拦截未取到评论区 |
| 融资 | 未披露 | 官网无融资信息 |
| 投资方 | 未披露 | — |
| 加速器 | 未查到 | — |
| 合规认证 | 未提及 | — |

> 备注：官网演示 UI 中出现 "Maya Chen / [email protected]"，为产品 demo 示例用户而非团队信息，不作团队事实采用。

## 定价 / 商业模式

Freemium + BYOK（Bring Your Own Key）。模型 token 费用由用户的 ChatGPT/Claude 订阅或 OpenAI/Anthropic API key 承担，Cronloop 只在调度层收费：

| 档位 | 月费 | agent 数 | 频率上限 | 月运行分钟 | 单次时长 | 并发 |
|---|---|---|---|---|---|---|
| Free | $0 | 3 | 每小时一次 | 200 分钟/月 | ≤10 分钟 | 1 路 |
| Pro | $25/月（年付 $20/月） | 无固定上限 | 每 5 分钟一次 | 无月上限 | ≤60 分钟 | 3 路 |

Pro 含优先支持。登录方式：GitHub / Google / 工作邮箱。

## 关联信息 / 生态

- 官网给出的用例及对应节奏/示例结果（均为官网声称）：
  - 外呼 prospect → 每 30 分钟 → "本周 booked 12 个 demo"
  - 客服工单 → 每 5 分钟 → "83% 工单自动解决"
  - 有机流量 → 每天早上 → "90 天 +38% organic clicks"
  - issue 转 PR → 每小时 → "本周开 9 个 PR"
  - 社媒内容 → 每天 3 次 → "本月 +4800 followers"
  - 竞品监控 → 每天 2 次 → "售前抓到 3 次定价变动"
- 母公司 Cactal, Inc.；资源经 cdn.cactal.app 分发，Cronloop 为其旗下产品（具体关系官网未详述）

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-08-19 | 登录 Product Hunt 榜单第 10（官方称"New: Manage your agents from ChatGPT and Claude"为新近上线的 MCP 接入能力） |
| 2026 | 官网 footer 标注 "© 2026 Cactal, Inc." |

> 官网未提供更详细的产品发布时间线。

## 评论区反馈（事实摘录，不评价）

- PH 页评论数仅 1 条，且因 Cloudflare 拦截未能抓取原文，待补。

## 信息来源

- 官网首页：https://cronloop.ai （拿到 tagline、机制、用例、集成目录、MCP server 说明、定价）
- 官网定价区块：cronloop.ai 首页内嵌（拿到 Free/Pro 两档价格与额度）
- GitHub：搜索 "cronloop" 仅返回无关个人仓库（znerol74/cronloops 等）；cactal-app 组织 404——**未见开源信号，判定闭源 SaaS**

## 未查到 / 待补

- 创始人 / 团队背景：官网未披露，PH 评论区被 Cloudflare 拦截未取到
- 融资阶段与金额：未披露
- 具体后端技术栈（编程语言）：官网未披露
- PH 评论区（仅 1 条）原文：待补
