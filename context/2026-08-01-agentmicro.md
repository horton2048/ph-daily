# AgentMicro · 扩展阅读上下文

> PT 2026-08-01 Product Hunt 榜单第 4 名 · 👍 179 · 💬 9
> 归档日期 2026-08-01 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | AgentMicro |
| 英文 tagline | Live Codex task status in your macOS menu bar |
| 中文 tagline | 在 macOS 菜单栏里实时看 Codex 任务状态 |
| 官网 | 无独立官网（GitHub 仓库为主页） |
| PH 页 | https://www.producthunt.com/products/agentmicro |
| GitHub | https://github.com/fizzy718/AgentMicro |
| 品类标签 | Developer Tools · Menu Bar Apps · Open Source |
| 票数 / 评论 | 179 / 9 |
| 公司主体 | 无公司主体（个人开源项目，MIT 协议） |
| logo | https://ph-files.imgix.net/dc4ce086-ba4f-4900-8de6-7a15b24b2496.png |
| 创始人/maker | Andy（PH @idky_wis，GitHub fizzy718） |

## 是做什么的（如实复述，不评价）

AgentMicro 是一个 **local-first 的 macOS 菜单栏应用**，用来**实时监控并行运行的 Codex Desktop 和 Codex CLI 任务**。它在菜单栏里用彩色图标显示每个任务的状态——蓝(thinking)、绿(unread 结果)、橙(需输入)、红(error)、白(idle)，并显示项目名、当前轮次耗时和 fast-mode 徽章。点击即可跳回对应的 Codex Desktop 任务。它只读取本地 Codex 进程和会话的元数据，不上传 prompt、响应、源码或任务历史，不读取 Keychain，不需要 Full Disk Access。

项目派生自 Peter Steinberger 的 CodexBar，由 fizzy718 独立维护，与 OpenAI 无关。

## 解决什么问题（事实层面，不判断值不值得解）

- **并行 Codex 任务失去线索**：开发者同时跑多个 Codex 任务时，"我开着几个、跑到哪步了、是不是卡住要输入"很难追踪。Andy 自述就是为此而建（"I kept losing the thread when I had several Codex tasks running in parallel"）。
- **Codex 桌面端缺少任务状态总览**：原生 UI 不在菜单栏呈现并行状态，需切换窗口逐一查看。
- **担心代码外泄**：开发场景对隐私敏感，云端 dashboard/任务系统会让人犹豫。AgentMicro 只读本地元数据解决"在不把代码送出去的前提下监控任务"。
- **目标场景**：在 macOS 上用 Codex Desktop/CLI 跑多任务的并行开发工作流。

## 怎么做的（技术原理/机制，事实层面）

来源：GitHub README + PH 创始人评论

- **状态机**：5 个可视状态（Idle/Unread/Thinking/Needs input/Error），外加一个内部 unknown 状态（显示为 idle）。
- **数据源**：读取本地 Codex 进程和会话目录的元数据 + rollout 事件，用 filesystem events 驱动更新，带 fallback polling。
- **只读**：明确不批准动作、不停止/继续任务、不编辑 Codex 状态、不监控 token 配额、不上传任务历史。
- **base 模式**：无需 Accessibility 权限即可工作。
- **Enhanced Status Detection（可选 opt-in）**：识别选中任务和当前 Codex 窗口里可见的 approval/error 控件；明确"never clicks, types, or approves anything for you"。默认关闭，opt-in 后才请求 Accessibility 权限。
- **菜单栏六格图标**：镜像前 6 个任务，工作中带动画。
- **技术栈**：Swift 6.2+ / SwiftUI / Swift Package Manager；macOS 14 Sonoma+；Sparkle 签名自动更新；GitHub Actions CI；SwiftLint + SwiftFormat。
- **分发**：GitHub Releases（Developer ID 签名 + Apple 公证 DMG）、Homebrew cask `fizzy718/tap/agentmicro`、源码自建。
- **本地化**：23 种界面语言，跟随系统语言。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Andy（PH @idky_wis，GitHub fizzy718） | PH 产品页 / GitHub |
| 团队规模 | 个人开发者（独立开源项目） | GitHub |
| 融资 | 无（个人开源，MIT 协议，免费） | GitHub LICENSE |
| 投资方 | 无 | — |
| 加速器 | 未查到 | — |
| 派生自 | CodexBar by Peter Steinberger | GitHub README |

## 定价 / 商业模式

- **Free / 开源 (MIT)**：全功能免费，GitHub Releases、Homebrew、源码三种分发方式均可获得全部功能。
- 无付费档、无订阅、无企业版。
- 模式：纯开源个人项目，无商业化。Sparkle 自动更新由作者签名发布。

## 关联信息 / 生态

- **派生关系**：fork 自 Peter Steinberger 的 CodexBar，保留原 LICENSE 与 notice。
- **与 OpenAI 关系**：明确声明不隶属、未被 OpenAI 背书。
- **关联产品**：Codex Desktop、Codex CLI（OpenAI 的编码 agent 产品）。
- **GitHub stats**（抓取时）：12 stars · 1 fork · 30 commits。
- **PH maker 资料**：Andy 自述"Founder and storyteller. Building apps."，PH 加入时间 2026-07-30，AgentMicro 是其首个发布的产品。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-07-30 | maker Andy 注册 Product Hunt |
| 2026-08-01 | AgentMicro 登 PH 日榜第 4 名（179 票/9 评） |
| 抓取时近 4 天前 | GitHub 最后更新（12 stars, 30 commits） |

## 评论区反馈（事实摘录，不评价）

- **Andy (maker)**：动机是"同时跑几个 Codex 任务时老丢线索"；定位是"再加一个 dashboard/托管任务系统/自动化层"的反面。
- **Dale Mooney**：建议区分"idle"与"lost"（stale 元数据）；blue "thinking" 状态应能衰减——"duration in state 比 raw elapsed 更重要"。
- **Asad M.**：担心 base 模式假阳性——长 tool call 被误判为等待输入；强调"orange is never wrong"必须成立系统才有用。
- **Rabnoor Singh**：建议给现有 5 状态加 aging 而非新增第 6 个；让阈值自学（thinking 超过用户 p90 时自己 escalate）。
- **Raffay Sajjad**：问是否支持远程 SSH 的 Codex 会话——未见回复。
- **Arshita Sharma**：问能否判断任务是否正确完成还是部分完成——未见回复。
- **Raj Nagulapalle**：赞赏"只有 orange 要你 act now"的设计，以及 base 模式不需要 Accessibility 权限。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/agentmicro（tagline、描述、maker Andy/@idky_wis、评论区 9 条、logo）
- GitHub 仓库：https://github.com/fizzy718/AgentMicro（README 全文、LICENSE=MIT、12 stars、Swift/SwiftUI 技术栈、Homebrew 分发、派生自 CodexBar 声明）
- PH maker 主页：https://www.producthunt.com/@idky_wis（bio、加入日期、Top 5 Launch 徽章）
- 公开报道：未查到相关报道
- 独立官网：未查到（agentmicro.com 无法解析）

## 未查到 / 待补

- **独立官网**：agentmicro.com DNS 解析失败，无独立官网
- **公司主体**：个人开源项目，无公司
- **融资金额/投资方/加速器**：无
- **团队规模**：仅 Andy 一人
- **OpenAI 官方关系**：仓库明确声明无关联、未背书
- **远程 SSH Codex 会话支持**：评论区提问未获回复
- **任务正确性评估能力**：评论区提问未获回复
- **公开报道**：未查到媒体覆盖
