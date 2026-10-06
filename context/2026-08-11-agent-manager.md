---
product: "agent-manager"
slug: "agent-manager"
date: "2026-08-11"
rank: 8
votes: 0
comments: 1

category: "开发者工具 / AI agent"
subcategory: "AI 编码工作流 / agent 编排"
tags: ["开源", "tmux", "TUI", "Go", "Claude Code", "Codex", "Gemini CLI", "多 agent 编排", "终端"]

tech_stack: ["Go", "tmux", "bubbletea", "TOML"]
platform: ["macOS", "Linux", "Windows (WSL2)", "CLI", "Homebrew"]
open_source: true
license: "Apache-2.0"

business_model: "开源免费"
pricing_start: "$0"
funding_stage: "未披露"
funding_amount: ""

related_products: ["Claude Code", "Codex CLI", "OpenCode", "Gemini CLI", "Grok", "Aider", "Cline", "Cursor", "tmuxinator"]
maker_previous: []

archived_at: "2026-08-11"
sources_count: 4
---

# agent-manager · 扩展阅读上下文

> PT 2026-08-11 第 8 名 · 👍 0（早期快照） · 💬 1 · Apache-2.0 开源
> 归档日期 2026-08-11 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | agent-manager |
| 英文 tagline | The fastest workflow for developing with AI |
| 中文 tagline | 与 AI 协作开发的最快工作流 |
| 官网 | https://agent-manager.dev/ |
| PH 页 | https://www.producthunt.com/products/agent-manager |
| 品类标签 | Open Source · Developer Tools · Artificial Intelligence（PH）/ AI Coding Agents · Terminals |
| 票数 / 评论 | 0（快照） / 1 条创始人评论 |
| 公司主体 | 个人项目（Yoan Wainmann，GitHub: YoanWai） |
| 企业版/关联站点 | 无 |

## 是做什么的（如实复述，不评价）

终端 UI 工具，用于在 tmux 中同时管理多个 AI 编码 agent 会话。在一个私有 tmux server（名为 `agentmgr`）里把 Claude Code、OpenCode、Codex、Grok、Gemini CLI、Pi 等若干 CLI agent 各自跑在一个持久 tmux session 里，用户从单一列表视图即可看到每个 agent 的实时状态、回复被阻塞的 agent、做整文件 diff review 并把行内评论作为 review prompt 回传给 agent、fork 会话、开 git worktree、或直接开一个普通 shell。编译产物是单个 Go 二进制，不替换 tmux，退出 manager 后所有 agent 继续在后台运行。

核心交互是一键式：space 启动 agent 或回复被阻塞的 agent；ctrl+r 进入 review 模式看 diff、行评论变成 review prompt；f fork 当前对话；T 开一个普通 shell tab；tab 在已配置的 CLI 工具间切换；x kill 会话保留行；v 在同一对话上 revive 已 kill 的会话；Alt+W 把 agent 开进一个新 git worktree。

## 解决什么问题（事实层面，不判断值不值得解）

- 多 agent 并行时要在多个 tmux pane/tab 间反复切换才能知道哪个 blocked、哪个 finished、哪个 errored。
- 给被阻塞的 agent 回答问题需要先 attach 进对应 pane，打断当前注意力。
- agent 产出的 diff 评审通常要跳出终端去 GitHub/IDE，行内评论难以直接回传给 agent 作为后续 prompt。
- 一个 agent 吃光内存时只能手动 kill；之后想继续同一条对话线程没有原生手段。
- 想让多个 agent 在同一仓库的不同 git worktree 上并行干活，需要手工配 worktree 与 session 绑定。

## 怎么做的（技术原理/机制，事实层面）

- **运行方式**：单个 Go 二进制，启动一个私有 tmux server（`agentmgr`），每个 agent 会话是该 server 上的一个独立 session。manager 自身是一个基于 bubbletea 的 TUI，读取 `config.toml`。
- **状态检测**：6 种状态（working / waiting / finished / errored / idle / dead），通过 Claude Code 的 hook 事件检测，或对其他 agent 用可配置的 pattern 匹配。
- **MCP 集成**：agent-manager 注册自己的 MCP server，agent 可通过 MCP 调用来 rename session、声明 repo/branch、设置 diff scope。
- **Review 模式**：全屏 diff viewer，支持语法高亮、split/unified 切换、行内评论（c 键写单条、C 键把所有评论打包成 review prompt 发给 agent）、可选 repo / branch / diff target、cycle diff scope。
- **Fork / Kill / Revive**：f 创建一个命名兄弟 session 继续同一对话；x kill 进程回收内存但保留行；v 在同一对话线程上重启。
- **Git worktree**：Alt+W 把 agent 开进一个全新 git worktree，便于多 agent 在同仓库不同分支并行。
- **失败处理**：errored 状态会显示；dead 表示进程退出；具体重试/恢复策略 README 未详述。
- **技术栈**：Go + bubbletea（TUI 框架）+ tmux + TOML 配置。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Yoan Wainmann（GitHub: YoanWai，X: @yoanwaidev） | PH 产品页 / 官网 |
| 融资 | 未披露（个人开源项目） | 官网无融资信息 |
| 投资方 | 无 | — |
| 加速器 | 无 | — |
| 合规认证 | 无 | — |
| 贡献者 | GitHub 显示 7 个贡献者 badge | GitHub 仓库 |
| 仓库活跃度 | 382 commits / 19 open issues / 3 open PRs | GitHub 仓库 |

## 定价 / 商业模式

完全免费开源（Apache-2.0）。安装方式：

```
brew install yoanwai/tap/agent-manager
```

或从 GitHub Releases 下载带 checksum 校验的平台二进制。无付费版、无 SaaS、无企业定制。Windows 需通过 WSL2 运行。

## 关联信息 / 生态

- **支持的 agent**：Claude Code、OpenCode、Codex、Grok、Gemini CLI、Pi+，以及可配置加入"any CLI"。
- **GitHub topics**：agentic, ai-agents, bubbletea, claude-code, cli, code-review, codex, coding-agent, developer-tools, gemini-cli, golang, grok, opencode, terminal, tmux, tui, wsl。
- **报道/收录**：HN Show HN 讨论、TLDR Dev newsletter、daily.dev、EveryDev、Trendshift daily trending、Claude Workshop field note（官网自述）。
- **竞品/互补定位**：与 tmuxinator（纯 tmux session 编排，不含 agent 语义）、Aider / Cline / Cursor（单 agent IDE 内编码）、Claude Code 自身的多 session 能力相比，agent-manager 强调"多 agent 持久化 + 一键 review 回传"的终端编排层。
- **不做的**：成本跟踪、鼠标驱动（wheel 只用于滚动，其余全键盘）——创始人自述"honest about the scope"。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-08-11 | Product Hunt 上线当日榜第 8 |
| 更早 | GitHub 仓库已积累 382 commits、7 贡献者、289 stars（具体起始日期未查到） |

## 评论区反馈（事实摘录，不评价）

- 创始人 Yoan Wainmann（PH 评论）：自述"the fastest way I have found to work with coding agents, and everything in it is one keypress"；space 启动或回复 blocked agent、ctrl+r 开 file diff 且行评论变 review prompt、f fork 对话、T pin 一个 shell；强调不替换 tmux——"quitting the manager leaves every agent running"；诚实声明范围：无成本跟踪、键盘驱动（wheel 只滚动）。PH 显示该评论为 10 天前所发（早于 8-11 上榜日，疑为提前预热评论）。
- 社区评论：PH 页面快照未见其他用户评论。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/agent-manager（拿到 tagline、描述、创始人评论、topics、官网重定向入口）
- 官网：https://agent-manager.dev/（拿到功能、快捷键、支持 agent 列表、技术栈 Go+tmux+bubbletea、license Apache-2.0、brew 安装命令、GitHub 链接）
- GitHub：https://github.com/YoanWai/agent-manager（stars 289、forks 19、open issues 19、PRs 3、commits 382、contributors 7、license Apache-2.0、primary language Go、topics 列表、Homebrew tap yoanwai/tap）
- 官网重定向入口：https://www.producthunt.com/r/TYR5KARYLBAMED → 301 → https://agent-manager.dev/?ref=producthunt

## 未查到 / 待补

- PH 实际票数（快照为 0，但上榜第 8 应有更多票，待榜单更新后补）。
- 仓库创建日期、首个 release 日期与版本号（GitHub 页面未直接展示，需进 releases 页）。
- 创始人 Yoan Wainmann 过往产品/履历（maker_previous 未查到，X 账号 @yoanwaidev 未深入抓取）。
- 融资信息（无任何披露，按个人开源项目处理）。
- 重试/失败恢复的具体策略（README 未详述 errored 后如何自动处理）。
- 各支持 agent 的状态检测 pattern 配置细节（仅 Claude Code 用 hook 事件，其余"可配置 pattern"未给示例）。
