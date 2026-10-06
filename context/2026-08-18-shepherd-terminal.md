---
product: "Shepherd Terminal"
slug: "shepherd-terminal"
date: "2026-08-18"
rank: 6
votes: 113
comments: 14

category: "AI agent / 开发者工具"
subcategory: "AI 编码 agent 终端"
tags: ["Codex", "Claude Code", "持久化终端", "macOS", "Apple Silicon", "SSH", "Agent Monitor", "本地优先", "免费", "Beta"]

tech_stack: ["macOS native", "Swift/SwiftUI（推断）", "SSH", "本地 STT 模型", "Claude Code", "OpenAI Codex CLI"]
platform: ["macOS", "iOS（计划中）"]
open_source: false
license: ""

business_model: "免费（首版公测，未披露付费计划）"
pricing_start: "免费"
funding_stage: "未披露"
funding_amount: ""

related_products: ["Warp", "Claude Code", "opencode", "Pi Coding Agent", "Maestri", "Cursor", "Cline"]
maker_previous: ["无公开过往独立产品（开发者为本人在职 ML 工程师）"]

key_signals:
  - "首个公测版本（2026-08-18 上 PH），免费下载，macOS 14+ Apple Silicon 专属"
  - "核心差异点：终端进程在 app 关闭后继续运行、重连后恢复同 tabs/panes/sessions——专为多 agent 并行而生的持久化工作区"
  - "Shepherd Plugin 让 agent 程序化控制终端（create_pane/create_tab/send_input/read_output），agent 可自排布局、委派子 agent、自验结果"
  - "支持 SSH 远程开发 + Routes 端口转发（远程 localhost:3000 → 本地 localhost:43120）；iOS 伴侣 app 开发中"

archived_at: "2026-08-18"
sources_count: 4
---

# Shepherd Terminal · 扩展阅读上下文

> PT 2026-08-18 Product Hunt 榜单第 6 名 · 👍 113 · 💬 14
> 归档日期 2026-08-18 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Shepherd Terminal（官网称 "Shepherd"） |
| 英文 tagline | A persistent terminal for Codex and Claude side by side |
| 中文 tagline | 让 Codex 与 Claude 并排跑的持久化终端 |
| 官网 | https://sheperd.kojunseo.link/ |
| 下载页 | https://update-shepered.kojunseo.link/ （signed & notarized .dmg，注意官网 URL 拼写为 "shepered"/"sheperd" 不一致） |
| PH 页 | https://www.producthunt.com/products/shepherd-terminal-designed-for-agent |
| 品类标签 | Developer Tools · Artificial Intelligence · Change Management · Terminals |
| 票数 / 评论 | 113 票 / 14 评论（PH 4.0 评分，1 review） |
| 公司主体 | © 2026 Shepherd（开发者 Junseo (Chato) Ko，首尔；隐私页 /privacy/） |
| 企业版/关联站点 | 开发者个人主页 kojunseo.link；博客 velog.io/@korkite/posts；YouTube @kojunseo；Google Scholar 主页 |

## 是做什么的（如实复述，不评价）

Shepherd 是一款 macOS（Apple Silicon、macOS 14+）原生工作区应用，专为同时跑多个 AI 编码 agent（目前支持 OpenAI Codex 和 Claude Code）而设计。它不是传统终端的 AI 增强，而是反过来：以 agent 为中心组织终端 tabs、panes、远程会话与文件查看。

三个核心能力：
1. **持久化 agent 终端**：终端进程在 app 关闭后继续运行，重连后恢复同样的 tabs、panes 和 sessions。官方原话："Shepherd keeps every process running when the app closes, then restores the same tabs, panes, and sessions when you reconnect."
2. **实时 Agent Monitor**：常驻视图，每个 agent 任务的当前状态分为"working / waiting for you / done since last check"三档，并显示分配的 agent（Codex 或 Claude Code）和任务名（如 auth-refactor、dashboard、integration-tests）。
3. **Session Resume + Change Inspection**：返回某个 agent session 时还原它的 tab/pane，并在工作区内直接查看文件改动和 git diff（行级 +/−）。

附加能力：文件浏览器与 Git Diff Viewer、Shepherd Plugin（agent 程序化控制终端）、SSH 远程开发 + Routes 端口转发、Worktree 集成、CPU/RAM/Context 使用量监控、本地 STT 语音"vibe coding"。iOS 伴侣 app 列为"coming soon"（监控、告警、反馈、终端控制、远程重连）。

## 解决什么问题（事实层面，不判断值不值得解）

- **多 agent 状态散落难追踪**：maker 主帖原话——"running multiple coding agents quickly became harder to manage than the code itself"，"Codex and Claude were spread across terminal windows, and I kept losing track of which agent was working, waiting, or finished."
- **关 app / 关 tab 即丢长任务**：评论区 Gal Dayan 表示"has lost track of long-running agents by closing the wrong terminal tab"。
- **远程开发中 SSH 中断文件写到一半**：Gal Dayan 提出，若 SSH 连接在文件编辑过程中断开，Shepherd 是继续监听同一进程，还是会让 agent 行为中断留下半写文件（maker 暂未回复）。
- **agent 与代码改动脱节**：Kyle P. Coleman 评论"Git history beside the agent context makes a lot of sense"；maker 回应目标是把"agent 的工作与产生的代码改动保持在同一上下文"。

## 怎么做的（技术原理/机制，事实层面）

- **运行方式**：macOS 原生 app，签名并 notarized 的 .dmg 分发。下载后本地运行，agent（Codex / Claude Code）通过本地 CLI 接入；Shepherd 自己不跑模型，复用用户已安装的 agent CLI。
- **持久化机制**：终端进程在 app 关闭后继续运行（不是 freeze/resume，是 detach + 重连）。官网截图显示 Codex v0.147.0、model "gpt-5.6-sol low"；每个会话显示 CPU/RAM 与 "Context 8% used"、"Weekly 92% left" 等用量指标。
- **Shepherd Plugin**：给 agent 的程序化控制接口，提供 `create_pane` / `create_tab` / `send_input` / `read_output` 等命令。maker 在 PH 评论说明控制范围"currently scoped to the Shepherd workspace, not just the agent's own tab"，agent 可以在显式指令下检查 sibling pane；访问是"tool-mediated rather than ambient"——agent 不会自动读取或控制 sibling 会话；正在探索更细粒度权限（current pane / selected panes / entire workspace）。
- **远程开发**：SSH 连接到远程机器；"Routes" 把远程 localhost 上的服务端口转发回本地 Mac（示例：远程 localhost:3000 → 本地 localhost:43120）；远程文件可像本地一样浏览。
- **语音**：内置本地 STT 模型用于 voice-based "vibe coding"。
- **技术栈**：macOS 原生（Swift/SwiftUI 为合理推断，官网未明示语言）；构建标明使用 Claude Code 和 OpenAI Codex CLI（PH "Built with" 标签）；本地 STT；SSH。
- **安全讨论（评论区）**：Clement Morel 指出 agent-to-agent pane 可见性的 prompt injection 风险——"If agent A can inspect agent B's pane, B's output becomes untrusted input to A"，询问 sibling pane 内容是标记为 data 还是 prompt。maker 尚未在该 follow-up 上回复。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 主创始人 / Maker | Junseo (Chato) Ko（@kojunseo），首尔 | PH maker post + GitHub profile |
| 学历 | 成均馆大学 Applied AI 本科与硕士 | GitHub profile |
| 当前主业 | ML Engineer @ heydealer/PRND（2025.04–至今） | GitHub profile |
| 过往工作 | ML Engineer @ HealingPaper（2024.09–2025.04）；AI Engineer @ RAONDATA（2021.09–2024.09）；AI Researcher @ DSAIL | GitHub profile |
| 学术 | Google Scholar 主页存在（scholar.google.com/citations?user=qt7vHIMAAAAJ） | GitHub profile |
| 过往独立产品 | 未查到公开独立产品；GitHub 70 个仓库以学术 / 工具脚本为主（SumRAG、pretty-confusion-matrix、mojo-wav 等），无 Shepherd 公开仓库 | GitHub profile |
| 融资 | 未披露 | 官网无信息 |
| 投资方 | 未查到 | — |
| 加速器 | 未查到 | — |
| 合规认证 | 未查到 | — |
| Hunter | 未在 PH 页明示（maker 自发布） | PH 页 |

## 定价 / 商业模式

- 当前为**免费**：PH 页标 "Pricing: Free"，官网下载页直接提供 .dmg，无付费墙。
- maker 帖说明这是 "first public beta"，未披露未来付费计划或商业模式。
- 未查到订阅、企业版、Pro 档位信息。

## 关联信息 / 生态

- **直接对标**：Warp（AI 终端，PH 4.8 / 77 reviews）、Claude Code、opencode、Pi Coding Agent、Maestri（PH 列出的相似产品）。
- **生态依赖**：用户需自行安装 OpenAI Codex CLI 与 Claude Code；Shepherd 是它们的容器/编排层，不替代它们。
- **iOS 伴侣 app**（开发中）：监控、告警、反馈、终端控制、远程重连——maker 在主帖列出。
- **隐私**：官网 /privacy/ 页存在但未在本档中详细抓取。
- **GitHub**：kojunseo 个人账号下未见 Shepherd 公开仓库，闭源。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026 | 官网 Copyright 标注 2026 |
| 2026-08-18 | 在 Product Hunt 上线，第 6 名，113 票 / 14 评论；标注为 "first public beta" |

更早的里程碑（产品首发、版本号、内测开始时间）官网未公开时间线，待补。

## 评论区反馈（事实摘录，不评价）

- **Clement Morel**（非 maker）：① 询问 agent 控制范围是否限于自身 tab。maker 回复：当前控制范围是整个 Shepherd workspace，agent 可在显式指令下检查 sibling pane，"tool-mediated rather than ambient"，正在探索更细粒度权限。② follow-up 指出 prompt injection 风险——"If agent A can inspect agent B's pane, B's output becomes untrusted input to A"，询问 sibling pane 内容是否标记为 data 而非 prompt（maker 未回复）。
- **Gal Dayan**：重视 session 持久化（自己曾因关错 tab 丢失长任务）；询问 SSH 中断时远程文件编辑如何处理（maker 未回复）。
- **Sebastian Patterson**："I can already see this saving me from terminal window chaos."maker 回复："Terminal window chaos was exactly what pushed me to build Shepherd."
- **Brielle Marie**："This feels built around how people actually use coding agents now."maker 回复：目标是围绕"人们实际如何与多个编码 agent 协作"来设计，而非把每个 agent 当作孤立 chat。
- **Kyle P. Coleman**："Git history beside the agent context makes a lot of sense."maker 回复：目标是把 agent 工作与代码改动保持在同一上下文；反问用户通常同时跑几个 agent session 以指导 monitor 设计。
- **Alice Hayes**：询问"what did testing 200+ prompts teach you about product research?"maker 回复："I didn't run a formal 200+ prompt test, so I may be missing the context."并反问指的是 Shepherd 哪部分。
- 评论区第 2 页存在但本次未抓取（PH 显示有分页）。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/shepherd-terminal-designed-for-agent — 拿到 tagline、品类标签、票数/评论数、相似产品列表、maker 主帖全文、6 条 maker 回复与 5 条社区评论、Built with（Claude Code、Codex CLI）、关注数 142、4.0 评分。
- 官网：https://sheperd.kojunseo.link/ — 拿到核心机制（持久化进程、Agent Monitor 三态、Session Resume、Shepherd Plugin 命令、SSH Routes 端口转发示例、Worktree、CPU/RAM/Context 监控）、平台要求（macOS Apple Silicon 14+）、下载链接（signed & notarized .dmg）、iOS app coming soon、版权 © 2026 Shepherd。
- GitHub：https://github.com/kojunseo — 确认开发者身份（Junseo (Chato) Ko，首尔，ML Engineer @ heydealer/PRND，成均馆大学 Applied AI）、70 个仓库均与 Shepherd 无关、Shepherd 闭源无公开仓库。
- WebSearch：未返回有效公开报道结果（多查询均无第三方媒体覆盖）。

## 未查到 / 待补

- 融资阶段与金额：未披露。
- 公司注册主体（法律实体名称、注册地）：未查到，仅 © 2026 Shepherd 标注。
- 商业模式/未来付费计划：未披露，当前免费。
- 技术实现细节：持久化具体机制（detach 还是其他）、app 实现语言（Swift 推断）、Shepherd Plugin 协议规范文档未抓到独立页面。
- Hunter 信息：PH 页未明示（疑似 maker 自发布）。
- 评论区第 2 页内容：未抓取。
- Alice Hayes 提到的 "200+ prompts" 上下文：maker 表示不知情，未澄清。
- Clement Morel 第二个 follow-up（prompt injection / data vs prompt 标记）：maker 未回复。
- Gal Dayan 关于 SSH 中断文件写入的提问：maker 未回复。
- 早期内测时间、首发日期、版本号历史：官网无公开时间线。
- 开源信号：未见，未查到独立开源仓库，标注闭源。
