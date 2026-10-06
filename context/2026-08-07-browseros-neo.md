---
product: "BrowserOS neo"
slug: "browseros-neo"
date: "2026-08-07"
rank: 6
votes: 0
comments: 2
category: "开发者工具"
subcategory: "local browser for AI agents"
tags: ["Open Source", "Claude Code", "Codex", "MCP", "local-first", "browser automation", "YC"]
tech_stack: ["Chromium fork", "Rust", "TypeScript", "Go", "Bun", "React", "WXT", "MCP"]
platform: ["Mac", "Windows", "Linux", "Browser", "MCP"]
open_source: true
license: "AGPL-3.0"
business_model: "开源免费 / BYOK（未查到订阅制）"
pricing_start: "免费"
funding_stage: "YC Summer 2024 / 具体融资金额未披露"
funding_amount: "未披露"
related_products: ["Browserbase", "Playwright MCP", "browser-use", "Claude Code", "Codex", "Cursor"]
maker_previous: ["Nithin Sonti、Nikhil Sonti：Google/YouTube/NVIDIA、Meta 等背景（公开资料）"]
archived_at: "2026-08-07"
sources_count: 4
---

# BrowserOS neo · 扩展阅读上下文

> PT 2026-08-07 Product Hunt 榜单第 6 · 👍 未从归档取得 · 💬 2  
> 归档日期 2026-08-07 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | BrowserOS neo |
| 英文 tagline | The Missing Browser for Claude, Cowork & Codex |
| 中文 tagline | 给 Claude、Cowork、Codex 用的本地浏览器 |
| 官网 | BrowserOS / neo 官方站点（PH 跳转） |
| PH 页 | https://www.producthunt.com/products/browseros_ai |
| 品类标签 | Open Source · Privacy · Artificial Intelligence |
| 票数 / 评论 | 归档未记录票数；归档评论 2 |
| 公司主体 | Felafax Inc. / BrowserOS 团队（公开资料） |
| 企业版/关联站点 | GitHub / 官网 / MCP 连接文档 |

## 是做什么的（如实复述，不评价）

BrowserOS neo 是一个给 AI agents 使用的本地浏览器。它让 Claude Code、Cowork、Codex 等 agent 在用户真实登录态下执行网页任务，同时保留本地可视、可回放和可审计的浏览器环境。

产品强调不是给人日常浏览网页，而是给 agent 用：agent 可以拥有独立标签页，用户通过 cockpit 看多个 agent 的浏览状态、视频回放和 action log。

## 解决什么问题（事实层面，不判断值不值得解）

- 云端浏览器常遇到数据中心 IP、风控、登录态和 headless 可见性问题；本地浏览器可复用用户真实登录状态。
- 多个 agent 同时跑网页任务时，用户需要知道它们在哪个页面、做了什么、是否卡住。
- 公开资料称它简化页面 snapshot 以减少 token 使用，并把浏览状态放在本地目录。
- 隐私边界：公开资料称本地存储在 `~/.browserclaw/`；可选 anonymous telemetry；不会上传 URLs、content、prompts、results、screenshots。

## 怎么做的（技术原理/机制，事实层面）

- 架构：GitHub 显示其基于 Chromium fork，包含 Rust/TypeScript/Go 等组件；`claw-server-rust` 提供 MCP + JSON API，`claw-app` 使用 WXT + React，server 使用 Bun，CLI 使用 Go。
- Agent 连接：通过 MCP 连接 Claude Code、Codex、Cursor 等工具，官网列 53 browser tools 和 40+ MCP app integrations。
- 登录导入：公开资料提到 one-click Chrome login import，解决 agent 在真实网站登录的问题。
- 可观测性：提供 cockpit、session video replay、action log，用于观察多个 agents 的浏览任务。
- 隐私：本地优先，BYOK；是否有企业云同步或托管版未查到明确公开说明。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Nithin Sonti、Nikhil Sonti | 公开资料 / YC |
| 公司 | Felafax Inc. / BrowserOS | 公开资料 |
| 背景 | 公开资料提到 Google/YouTube/NVIDIA、Meta 等经历 | 公开资料 |
| 融资 | 未查到具体融资金额 | 公开搜索 |
| 投资方 | YC Summer 2024 信号；其他投资方未查到 | YC / PH |
| 加速器 | Y Combinator Summer 2024 | 公开资料 |
| 合规认证 | 未查到 SOC 2、ISO 27001 等认证信息 | 官网公开页面未列出 |

## 定价 / 商业模式

公开资料显示 BrowserOS neo 免费、开源，用户自带模型 API key；云模型费用由 provider 收取，本地 Ollama/LM Studio 可免费使用。未查到独立订阅制或企业版价格。

## 关联信息 / 生态

- 与 Browserbase 等 cloud browser 不同，它更强调本地登录态、隐私和 agent 可视化。
- 与 Playwright MCP/browser-use 类工具相比，它提供一个 agent-first browser shell 与 cockpit，而不仅是自动化库。
- 相关生态包括 Claude Code、Codex、Cursor、MCP、Chrome/Chromium、browser automation。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2024 | 团队进入 YC Summer 2024（公开资料） |
| 2026-08-07 | BrowserOS neo 出现在 Product Hunt 当日榜第 6 |
| 未查到 | 未查到完整版本历史和 release cadence |

## 评论区反馈（事实摘录，不评价）

- PH 归档显示当日评论 2；本文未完整保存逐条评论。
- 公开叙述重点围绕：给 Claude/Cowork/Codex 的本地浏览器、真实登录态、session replay、action log、MCP 连接。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/browseros_ai（拿到 tagline、分类、评论数、logo）
- 官网：BrowserOS neo 官方站（拿到本地浏览器、cockpit、隐私和指标叙述）
- GitHub：BrowserOS 相关公开仓库（拿到 AGPL-3.0、架构和语言栈线索）
- 公开资料：YC / 团队背景公开信息

## 未查到 / 待补

- 具体融资金额和投资方名单
- 企业版、商业化路线和支持 SLA
- 安全审计、代码签名、权限模型和数据保留政策全文
- 真实生产用户案例和任务成功率 benchmark
