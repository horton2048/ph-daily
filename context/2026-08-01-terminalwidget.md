# TerminalWidget · 扩展阅读上下文

> PT 2026-08-01 Product Hunt 榜单第 1 名 · 👍 0 · 💬 1
> 归档日期 2026-08-03 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | TerminalWidget |
| 英文 tagline | Put script output in your Desktop/Home screen widgets. |
| 中文 tagline | 将脚本输出显示在桌面/主屏幕小组件中 |
| 官网 | https://terminalwidget.app |
| PH 页 | https://www.producthunt.com/products/terminalwidget |
| 品类标签 | Productivity · Developer Tools · Apple（PH 分类：Automation Tools · Command Line Tools） |
| 票数 / 评论 | 0 / 1（API 快照时点，PH 页后端显示 148 upvote points / #6 day rank，数据存在时间差） |
| 公司主体 | 未查到（独立开发者产品，官网页脚未列注册主体） |
| logo | https://ph-files.imgix.net/e7fd4aac-35df-48c0-a8e9-fc12775a16b1.png |
| 平台 | macOS / iOS / iPadOS（通用 App，App Store 一次性买断） |

## 是做什么的（如实复述，不评价）

TerminalWidget 是一款原生 macOS/iOS 小组件应用，把任意脚本的输出（文本、进度、数字序列、表格、图片）渲染成桌面或主屏幕上的 WidgetKit 小组件。它本身**不执行脚本**，只接收输出并展示——用户通过 CLI、Shortcuts、AppleScript 或 URL scheme 四条路径把数据"喂"给具名小组件（如 `sales`、`backup`）。

核心定位：给开发者和重度自动化用户一个"一瞥可见"的仪表盘，不用开终端、不用自建 Electron dashboard、不用订阅 SaaS。创始人 Brett Terpstra 自述动机是想在桌面看销售、传输进度、uptime 和长脚本状态，"不是又一个浏览器标签页"。

## 解决什么问题（事实层面，不判断值不值得解）

- **监控数据看不到**：跑长脚本、传输进度、API 状态要看就得切终端或开网页 dashboard；想在桌面/手机主屏一瞥可见。
- **自建 dashboard 重**：Electron 应用或自托管监控栈要起服务、维护前端、跨设备还要做中继。
- **SaaS 订阅疲劳**：监控类工具普遍按月收费，且数据要过第三方。
- **目标场景**：长脚本进度、CI/CD 状态、销售/uptime 监控、API 数据看板、自动化任务可视化。

## 怎么做的（技术原理/机制，事实层面）

来源：terminalwidget.app + Brett Terpstra 发布博客

- **原生 WidgetKit + 小 CLI**：不是 Electron，不起常驻 web server。CLI 工具 `terminal-widget` 带 `--target/--text/--progress/--chart/--icon/--fg` 等标志。
- **四条输入路径**：① CLI `terminal-widget`；② Shortcuts.app 动作（Mac+iOS 通用）；③ AppleScript（macOS）；④ URL scheme（Mac+iOS）。四路都喂同一个 target/payload 系统。
- **具名 target**：每个小组件按名字（如 `widget1`、`sales`）独立寻址，可同时跑多个不同数据的组件。
- **更新时机**：macOS 端即时生效；iOS/iPadOS 通过 iCloud 同步，需开通知权限做后台刷新，存在短暂延迟。iOS 也可作为更新发起方，不是 Mac-only 单向。
- **支持的数据形态**：纯文本/格式化文本、进度值（0-100）、整数序列（sparkline/图表）、矩阵整数数组、表格（CSV/TSV/JSON）、图片（本地/远程/API 生成，含 edge-to-edge）。
- **组件类型**：文本、进度条、sparkline、各类图表（含 radial）、矩阵、表格、图片。
- **交互动作**：每个组件可配 tap/click 动作——打开 URL、打开 Mac App、运行 Shortcut、运行 shell 命令（macOS）、从 URL 刷新。
- **样式**：颜色、字体、图标、标题、caption 全部按更新逐次可控。
- **同步**：payload 和 action 都通过 iCloud 跨设备同步。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Brett Terpstra（@ttscoff，独立开发者，Marked 3 作者） | PH 产品页 / 官网 |
| 团队 | PH 页面 co-listed "fmerian"，具体团队规模未披露 | PH 产品页 |
| 融资 | 未查到（独立开发者产品，无融资公告） | — |
| 加速器 | 未查到 | — |
| 合规认证 | App Store 上架（Apple 审核） | 官网 |

## 定价 / 商业模式

来源：terminalwidget.app（2026-08-03 抓取）

- **$19.99 一次性买断**：通用 App，一次购买覆盖 Mac + iPhone + iPad。
- **TestFlight 公测**：开放中。
- **Setapp**：创始人博客表示"如果有兴趣可能会上 Setapp"，未承诺。
- 模式：**一次性买断**（非订阅、非 SaaS、非 credit 制）。不做托管，数据不过第三方服务器，iCloud 同步走用户自己的 Apple 账号。

## 关联信息 / 生态

- **创始人前作**：Marked 3（Markdown 预览工具，长期在 Mac 开发者圈有名）。
- **配方分享平台**：发布即上线，用户可分享/复用 widget 配方。
- **PH 类似产品**：NotchNook、Usage for Mac、Mindr、SuperWidget、Patterns Habit Tracker。
- **定位对手**（官网自比）：自建 Electron/web dashboard、自托管监控栈（Grafana 类）、SaaS 监控订阅服务。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-04-20 | Brett 早期博文《terminal feedback on the Desktop》，TerminalWidget 概念首次公开 |
| 2026-08-01 | 正式发布博文《Introducing TerminalWidget》+ Product Hunt 上线 |

## 评论区反馈（事实摘录，不评价）

- **Rabnoor Singh / Dale Mooney**（质疑）：iOS 控制小组件刷新频率，显示值可能已过时数小时但仍读作"当前"。希望有 staleness 契约——max-age 声明或对过期数据做视觉衰减。
- **Brett 回复**：输出由用户脚本控制，错误处理由脚本作者负责，TerminalWidget 不干涉。
- **Valeria**（提问）：脚本是否继承 `.zshrc` 的 PATH？Brett 澄清：TerminalWidget 不执行脚本，只接收输出。
- **Valeria**（后续）：了解后表示"这彻底改变了信任模型"。
- **Raffay Sajjad**（质疑）：output 镜像到 iPhone 时，secrets/API keys 是否会被存储？PH 页第 2 页评论，创始人未直接回答。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/terminalwidget（maker Brett Terpstra 开场评论、评论区 staleness/信任模型/凭据安全讨论、logo、148 upvote points）
- 官网：https://terminalwidget.app（功能、$19.99 定价、WidgetKit 架构、四路输入、数据形态、跨设备 iCloud 同步）
- Brett 博客：https://brettterpstra.com/2026/08/01/introducing-terminalwidget/（动机、技术架构、命名 target、macOS 即时/iOS iCloud 延迟、Setapp 可能性、4 月早期博文线索）
- GitHub：未查到公开仓库（闭源商业 App Store 产品，符合预期）

## 未查到 / 待补

- **公司注册主体/注册地**：官网页脚未列，未查到
- **融资金额/轮次/投资方**：无融资公告，疑似独立开发者自筹，未证实
- **团队规模**：Brett + co-listed fmerian，具体人数未披露
- **加速器背景**：未查到
- **下载量/用户数**：未披露
- **Raffay Sajjad 凭据安全问题的官方回答**：创始人未在 PH 页正面回应
- **GitHub**：无公开仓库（闭源商业产品）
