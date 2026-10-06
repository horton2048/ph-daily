# Terminal Candy · 扩展阅读上下文

> PT 2026-08-01 Product Hunt 榜单第 7 名 · 👍 130 · 💬 11
> 归档日期 2026-08-03 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Terminal Candy |
| 英文 tagline | A native macOS terminal you can skin and theme |
| 中文 tagline | 可贴皮换肤的原生 macOS 终端 |
| 官网 | https://www.terminalcandy.com |
| PH 页 | https://www.producthunt.com/products/terminal-candy |
| 品类标签 | Mac · Productivity · Developer Tools（PH 分类：Terminals） |
| 票数 / 评论 | 130 / 11 |
| 公司主体 | 未查到（独立开发者产品，官网页脚未列注册主体） |
| logo | https://ph-files.imgix.net/2328bc32-b057-4279-8163-34374aca092d.png |
| 平台 | macOS 14 (Sonoma)+ 通用二进制（Apple Silicon + Intel），无 Windows/Linux 版 |

## 是做什么的（如实复述，不评价）

Terminal Candy 是一款原生 macOS 终端模拟器，核心差异是"可贴皮"——用户挑一张图（Game Boy、卡带、Pip-Boy 或自制），用魔棒抠掉背景，把终端窗口直接画到这幅 artwork 上。创始人 Peter Hough 自述动机："I spend basically all day in the terminal, and I got tired of it being a grey box."

另一条主线是 **AI 代理通知**：当 Claude Code 或 Codex 这类 coding agent 需要用户输入时，Terminal Candy 通过声音 + dock 弹跳提醒。Peter 原话："The skins are why I built it, the alerts are why it stays open all day."

## 解决什么问题（事实层面）

- **终端是灰框没人想多看**：开发者全天泡在终端里，但默认外观枯燥；想要个性化又不想上重型主题框架。
- **AI 代理需要 babysit**：跑 Claude Code / Codex 时用户得来回切窗口看"它是不是在等我输入"，长任务尤其烦。
- **Electron 终端占内存**：市面可换肤终端多为 Electron 套壳，原生体验和资源占用都有妥协。
- **目标场景**：开发者日常终端 + AI coding agent 并行跑的桌面工作流。

## 怎么做的（技术原理/机制）

来源：terminalcandy.com + PH 产品页

- **100% 原生 macOS**：非 Electron。基于 **SwiftTerm** 做的真 PTY，全 VT 仿真、scrollback、xterm mouse、true color、多 session。
- **Skin Builder**：三步流程——挑图 → 魔棒抠背景 → 把终端方框画上去。改动实时生效，"No restart, no compiler"。
- **CRT 特效**：GPU 合成的扫描线、磷光 glow、曲率、grain。
- **84 套内置配色**：含 Dracula、Nord、Tokyo Night、Solarized、CRT greens。
- **⌥Space 全局热键**：任何 app 之上呼出/隐藏终端，**不需要 Accessibility 权限**。
- **⌘M 切换皮肤开关**：保留 session 和 scrollback。
- **社区皮肤 marketplace**：浏览、一键安装、上传自己的；发 10 个 approved 皮肤 = 免单。
- **AI 代理提醒**：响 terminal bell 的 agent 会跳对应窗口（per-window attribution 可用）；dock 弹跳是 app 级的，macOS 只给一个 dock icon，没法在 icon 上标哪个 agent——Peter 在 to-do list 里加了 per-window "waiting on you" 徽标。
- **系统要求**：macOS 14+，Apple Silicon 与 Intel 通用二进制。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Peter Hough（PH 用户 @terminal_candy，X @terminalcandy） | PH 产品页 |
| 团队规模 | 未披露（疑似单人独立开发） | — |
| 融资 | 未查到（无融资公告） | — |
| 加速器 | 未查到 | — |
| 合规认证 | Apple Mac App Store 上架审核（如走 App Store 分发，未明确） | — |

> 备注：网络检索指向一个同名 "Candy" 终端配色主题作者 Peter Hough，但与本项目关系未坐实，仅作线索，不作为事实。

## 定价 / 商业模式

来源：terminalcandy.com（2026-08-03 抓取）

- **14 天免费试用**：最多 5 个皮肤槽。
- **$10 一次性买断**：无限皮肤 + 社区会员，"never a subscription"。
- **PH 限时码 STOPBABYSITTING**：前 100 名 $7。
- **发 10 个 approved 社区皮肤 = 免单**（$10 全免）。
- **退款政策**："如果在你 Mac 上真跑不了，退款。"

模式：**一次性买断**（非订阅、非 SaaS）。数据不过第三方服务器，皮肤走本地 + 社区 marketplace。

## 关联信息 / 生态

- **PH 类似产品**：Ghostty、iTerm2、cmux、Sindre Sorhus、Pinto。
- **AI 代理目标**：Claude Code、Codex（OpenAI）。
- **配色生态**：内置 84 套主流配色，兼容 iTerm2/VS Code 主题文化。
- **Skin Builder 定位**：Peter 自述"preset skins 只是证明 builder 能用，魔棒一张照片画个方框你就进来了"。

## 技术时间线

| 日期 | 事件 |
|---|---|
| 2026 | PH 上线（#7 day rank，130 票） |

> 早期里程碑未在官网公开时间线，待补。

## 评论区反馈（事实摘录）

- **Abdullah Javaid**（提问）：多 agent 并行时 dock 弹跳能否归因到具体哪个 agent？Peter 回复：dock 弹跳是 app 级，macOS 只给一个 dock icon；但响 bell 的 agent 会跳对应窗口；per-window "waiting on you" 徽标已在 to-do。
- **Arash Rahimi**（提问）：Skin Builder 是核心还是预设皮肤？Peter：预设皮肤只是证明 builder 能用，核心是魔棒抠图 + 画方框。
- **Asad M.**（建议）：把"$10 一次"提到落地页前段，否则"会有人以为 $10/月直接关 tab"。Peter 采纳，已改 launch page copy，把 ping 提到顶部。
- **Asad M.**（追问）：agent 提醒是不是日用主功能？Peter：皮肤是建它的理由，提醒是它整天开着的理由。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/terminal-candy（maker Peter Hough 开场评论、评论区 dock 归因/Skin Builder/agent 提醒讨论、logo、定价 $7/$10）
- 官网：https://www.terminalcandy.com（$10 买断、14 天试用、SwiftTerm/PTY/VT 仿真、⌥Space 全局热键、⌘M 皮肤开关、社区 marketplace、macOS 14+ 通用二进制）
- 公开报道：网络检索未找到融资公告或深度报道
- GitHub：未查到公开仓库（闭源商业产品）

## 未查到 / 待补

- **公司注册主体/注册地**：官网页脚未列，未查到
- **融资金额/轮次/投资方**：无融资公告，疑似独立开发者自筹，未证实
- **团队规模**：仅 Peter Hough 一人公开，是否有协作未披露
- **加速器背景**：未查到
- **下载量/用户数**：未披露
- **GitHub 仓库**：无公开仓库
- **Peter Hough 是否为"Candy"终端主题作者**：检索有线索但未坐实
