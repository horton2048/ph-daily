# Screencap · 扩展阅读上下文

> PT 2026-07-31 Product Hunt 榜单第 9 名 · 👍 135 · 💬 19
> 归档日期 2026-08-01 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Screencap |
| 英文 tagline | Turn your team's real workflows into AI training data |
| 中文 tagline | 将团队真实工作流程转化为 AI 训练数据 |
| 官网 | https://screencap.sh |
| PH 页 | https://www.producthunt.com/products/screencap |
| 品类标签 | Productivity · SaaS · Artificial Intelligence |
| 票数 / 评论 | 135 / 19 |
| 公司主体 | Ivy Research LLC（GitHub CLA.md / CONTRIBUTING.md 版权持有方，footer © 2026 Screencap） |
| GitHub 组织 | github.com/proteus-computer-use/screencap（PolyForm Noncommercial 1.0.0，source-available） |
| 关联站点 | screencap.sh/dataset（开放数据集浏览） |

## 是做什么的（如实复述，不评价）

Screencap 是一款 **macOS 上的本地优先（local-first）屏幕记忆工具**，把团队真实工作流程录下来并转为可搜索、可结构化导出的数据。形态：

- **录制维度**：屏幕画面、键盘输入、点击、音频、窗口上下文（active app/window），按 15 分钟分块写盘，崩溃只丢几分钟而非整段。
- **本地存储**：默认全部存到 `~/.screencap`，永不上传除非用户显式选择云同步。`recording.db` 永不离开本机。
- **端侧智能切片**：内置 on-device 模型把录像切成带标签的「任务」（如"Payroll run — Gusto"、"Invoice reconciliation"），并对每个口头/屏幕时刻建索引，使数月后可按文本搜索。
- **MCP 上下文注入**：录制过程中查询用户连接的 MCP 服务器（Gusto / Attio / Linear / Notion / 任意 MCP server），把屏幕上对应记录（如 "Payroll run #214 — May"）的快照存进录像。
- **两种分发**：原生 macOS App（含时间线、Journal、搜索、Chat、设置），以及 CLI + 后台 daemon（`screencap start/status/list/view`，支持脚本化和 headless）。
- **导出形态**：JSONL 交互轨迹（每次点击/键盘/窗口事件，SQLite 结构化），用于训练 computer-use agents 或构建自动化；亦供剪辑回放。
- **开放数据集**：用户可主动捐献审查过的录像到 screencap.sh/dataset，给开源 computer-use 模型提供「真实工作流」训练数据（默认关闭，逐条审查，不自动）。

定位：团队工作流的「持久记忆」+ AI/自动化训练数据的「真实样本源」，强调隐私在录制时强制执行而非事后补救。

## 解决什么问题（事实层面，不判断值不值得解）

- **团队知识随人离开而流失**：创始人 Rute 在 PH 评论区自述——"knowledge inside teams keeps getting lost. Sometimes it lives in someone's head, and when that person leaves, it leaves with them." 重复工作流时丢几小时重建上次的步骤。
- **合成/抓取数据训练 computer-use 模型的局限**：官网 Open Dataset 段落——开源 computer-use 模型当前主要靠"synthetic interactions and scraped screen captures"训练，缺乏真实、有意贡献的工作流样本。
- **新员工 onboarding 缺真实素材**：可把多个录像按序组装成 onboarding collection 共享给新成员。
- **现有"本地+隐私"屏幕录像器的事后补救模式**：README 主张——竞品通常"redact things afterwards"，Screencap 在录制时即阻断敏感内容。

## 怎么做的（技术原理/机制，事实层面）

来自 GitHub README 的 SECURITY/privacy 模型与官网 #privacy 段：

- **Capture-time blocking, fail-closed**：实时过滤器监听 foreground window，对敏感 app 在写入前阻断捕获——被排除的截图永不触盘、键盘事件置空、视频帧丢弃。过滤器以 blocked 状态启动，出错时保持 blocked，即"失败=少录，不是多录"。
- **上下文分类矩阵**：把 app 归类到 contexts（Password managers / Banking / Login-SSO / Checkout / Email-chat-calendar-video / Browser unverified / Cloud storage / Code editors-terminals / Admin consoles / Other），按 public/internal 两种隐私模式执行 Exclude / Mask window / Text redact / Allow。
  - Exclude：截图不写、键盘置空、视频帧丢弃。
  - Mask window：捕获但键盘置空、视频帧丢弃、截图在 scrub 时用不透明纯色填充（非模糊，不可恢复）。
  - Text redact：保留捕获，scrub 时清 PII/secrets。
- **强制默认**：Password managers 在所有模式下都 Exclude；Banking/Login/Checkout 在 public 模式 Exclude、internal 模式 Mask window。用户可覆盖但排除类需显式确认；`SCREENCAP_PRIVACY_MODE` 环境变量只能收紧不能放松。
- **macOS Secure Input 集成**：用户在密码字段时自动阻断键盘捕获；通过 accessibility attributes 检测的密码字段进一步阻断屏幕/视频/键盘，带 hold timer。切换离开 blocked app 后短暂继续阻断以覆盖 app-switch 动画。
- **Scrub 阶段（二次防御）**：`screencap scrub` 在录制后跑 PII/secrets 检测——Presidio + GLiNER NER backend，外加 detect-secrets 和 regex 模式，开箱即用，无需额外安装。云上传前必跑且 app 加 review step（你审批的 copy = 实际上传的 copy）。
- **搜索是 consent-gated + 加密**：on-device search 必须用户先确认披露，搜索语料（screenshots + 文本索引）at-rest 加密，永不上传。`screencap search enable` 是 deliberate consent step。索引位于 `~/.screencap/content_index.db`，仅由隐私策略允许的帧构建。
- **三个搜索入口**（都本地）：App 内 Chat（如"周二那个报错是什么"）、daemon API（content.search / transcript.search / timeline.query / frame.nearest，本地 UNIX socket）、MCP server（`screencap mcp` 跑 stdio MCP，供 Claude Desktop / Codex 等查询，带 citation）。
- **结构化数据格式**：每条录像 = SQLite + 可导出为 JSONL 交互轨迹（click/keystroke/scroll/window event），可喂给 computer-use agent 训练或自动化。
- **录制模式**：Action-gated capture——按实际活动写视频/截图而非 24/7 firehose，footprint 小到能全天运行；默认 15 分钟分块。
- **技术栈**：Python（pyproject.toml、pip 安装、`pip install -e ".[dev]"`，要求 macOS + Python 3.10+）、PyInstaller 打包（独立 binary，无 Python 依赖）、PyObjC（macOS Accessibility 集成）、CLI 安装 `curl -sSfL https://get.screencap.sh | sh` 装到 `~/.screencap/bin`。
- **误报/失败处理**：fail-closed 设计——分类器出错时少录而非多录；用户显式 allow 在敏感 browser 页（login/checkout）不生效。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 公司主体 | Ivy Research LLC | GitHub CLA.md / CONTRIBUTING.md（"name Ivy Research LLC as copyright holder"） |
| 团队成员 | Rute Figueiredo（Software Engineer，PH maker、GitHub commit rutefig）、yogesh shahi（"Building @ivy-research"，PH maker）、@aayushtheg（PH 评论区被点名负责 labeling 层） | PH makers 页 / GitHub |
| 团队规模 | 已公开 3 人，PH makers 页显示 2 名正式 maker + 评论区提到 1 名同事 | PH makers 页 |
| 融资 | 未查到 | 官网/PH/GitHub 均未披露融资 |
| 投资方 | 未查到 | — |
| 加速器 | 未查到 | — |
| 合规认证 | 无明示 SOC 2/GDPR 等认证，但提供公开威胁模型 SECURITY.md 与"source-available"可验证设计 | GitHub SECURITY.md |
| GitHub Star | 7 stars, 1 fork, 2,464 commits, 23 branches, 84 tags（截至归档日） | GitHub repo |
| 当前版本 | v0.20.0（官网 dataset 页 footer）/ README 示例 pin 到 0.24.6 | 官网 / README |

## 定价 / 商业模式

官网 #pricing 段三档（清晰分个人/团队）：

- **This Mac only**：$9/月 · 单 Mac。无限录制与搜索、全部留本地、通过导出加密文件分享。
- **Personal cloud**：$20/月 · 单人。跨 Mac 加密备份、按链接分享单条录像、可随时升级到团队。
- **Team cloud**：定价"联系销售"。共享团队库（端到端加密）、有序 onboarding collections、密钥留在团队。
- **个人使用源码自建免费**：Plans 段明确——"The source is public, and building it yourself for personal use is always free." Plans 覆盖的是签名+公证的构建、更新、支持、云。
- **商业 license**：嵌入到产品中或需要超出上述 plans 的条款时可购买商业 license。
- **试用**：7 天 business trial（GitHub CLA.md commit "add 7-day trial"）。

模式：开源 + 双轨订阅（个人云 $20 / 团队云 contact-us）+ 商业 license。源码 PolyForm Noncommercial 1.0.0——非商用可自建，商用需付费。这与纯闭源 SaaS 或纯 MIT 开源都不同。

## 关联信息 / 生态

- **Open Dataset**：screencap.sh/dataset 浏览捐献的真实工作流录像，每条由 owner 逐帧审查 + app 同款 anonymizer 清洗，"what you see here is exactly what a training run sees"。归档当日页面显示"0 recordings"（数据集刚启动，尚无捐献内容）。
- **MCP 生态对接**：录制时查询连接的 MCP 服务器（Gusto / Attio / Linear / Notion / 任意 MCP）拿屏幕上记录的元数据，存进录像做 ground truth 标注。
- **CLI 工具集**：`screencap setup` 交互式扫描已装 app 配隐私规则；`screencap settings privacy` 直接编辑 exclude/allow 列表；`screencap backfill start` 给老录像建索引；`screencap mcp` 跑 stdio MCP server。
- **平台支持**：macOS（已发布），Windows / Browser extension / Android 标注 "Coming soon"。
- **竞品定位（评论区事实摘录）**：被问及是否对标 screenpipe，创始人回复"focus more on teams and also making it more accessible to everyone, even non technical people"，差异在团队云分享与端到端加密。
- **License**：PolyForm Noncommercial 1.0.0（source-available，非 OSI 开源但源码全公开）。

## 技术时间线（GitHub commit / 官网里程碑）

| 日期 | 事件 |
|---|---|
| —（具体日期未查到） | relicense 为 PolyForm Noncommercial 1.0.0 |
| — | CLA.md 将版权人命名为 Ivy Research LLC，加入 7-day trial |
| — | docs(security): 记录 tightening-only user rules (SCR-225) |
| — | feat(macos): 让 Mask segment 和 default-action banner 上线 |
| — | refactor(brand): 把 ScreenCap 重命名为 Screencap（贯穿 docs/Python/tests/build scripts） |
| 当前 | v0.20.0（官网 footer） |

> 注：GitHub commit 只给相对时间和 commit message，未见带绝对日期的公开里程碑表。绝对时间线未查到。

## 评论区反馈（事实摘录，不评价）

- **Adityaharish2002**：Is this a competitor to screenpipe?
  - **Rute**：focus more on teams and more accessible to non-technical people；团队用例有 cloud 端到端加密分享。
- **dalemooney**：Blocking banking and password managers is the easy half. Harder half is the app that's fine 95% of the time——e.g. CRM 直到有人打开客户记录。app-level blocklist 抓不到。"I have to review every clip" 是 quietly kills daily use 的事。问是否有 content-level 而非 app-level 的工作，还是 review step 兜底？
  - **Rute**：yes it is also in terms of content——anything that looks password, emails, names 等都 masked；review mostly just another safeguard。
  - **dalemooney**：Masking at content level 才能在团队中部署。但内部 identifiers（account reference / invoice number）通常不像 masker 能识别的形状——customer-defined pattern list 能覆盖知道自家格式的团队。
- **leo404**（solo 用例）：是否必须用 team cloud sync 才能生成训练数据？想本地捕获编辑工作流，故意分享特定 clip 而非全部自动上传。导出/保存的 clip 是什么格式？能否拉进视频编辑器还是只能在 Screencap 内回放？
  - **Rute**：solo 也能用，本地或云都可；导出是 structured steps + window context。
- **doganakbulut**：会先用它记录 process 实际怎么发生 vs 我们以为怎么发生。导出 dataset 实际长什么样——structured steps with clicks/window context 还是 raw video + metadata？
  - **Rute**：structured steps yes and window context。
- **未署名（多段长评论）**：
  - "You asked what it would take to leave it on all day. Honest answer: nothing in your privacy section, because that is not where the fear lives."
  - "Consent to be recorded is not consent to be compared. The day someone can ask how long I take on a workflow versus the person next to me, this stops being team memory and becomes a performance review with a video attached." 呼吁：Traces can build automations. Traces cannot be queried per person. 问产品是否愿把这个 boundary 写明。
  - "Blocking sensitive apps is a denylist, and denylists fail open. An allowlist captures far less and makes the pilot conversation much shorter." 建议 allowlist 取舍。
- **kritishpuri**：How do you get consistent labeling out of messy real usage? Real workflows are noisy next to curated demos.
  - **Rute**：Labeling is not done at this layer；同事 @aayushtheg 可给更多 insight。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/screencap
  - 拿到：tagline、188 followers、maker intro 段、评论区全文（含 Rute 与多位用户的隐私/labeling 讨论）、makers 页团队名单。
- 官网首页：https://screencap.sh/
  - 拿到：how it works 三步、privacy 6 条精确声明、MCP context 段、open dataset 段、source-available 段、pricing 三档、download（macOS only，Windows/extension/Android coming soon）、首页脚注版本 v0.20.0、license PolyForm NC 1.0.0。
- 官网 dataset 页：https://screencap.sh/dataset
  - 拿到：开放数据集定位、每条 owner 逐帧审查 + 同款 anonymizer、归档当日 0 recordings。
- 官网 pricing 段：https://screencap.sh/#pricing
  - 拿到：$9/$20/Contact 三档 + 个人自建免费 + 商业 license + 7 天 business trial。
- GitHub 仓库：https://github.com/proteus-computer-use/screencap
  - 拿到：README 全文（capture-time fail-closed、上下文分类矩阵、Secure Input、scrub Presidio+GLiNER、MCP/daemon API、CLI 命令、JSONL 导出、SQLite 结构）、LICENSE PolyForm Noncommercial 1.0.0、CLA.md 版权人 Ivy Research LLC、commit 列表（rename ScreenCap→Screencap、relicense、7-day trial、SECURITY tightening rules）、star 7 / fork 1 / 2,464 commits。
- PH makers 页：https://www.producthunt.com/products/screencap/makers
  - 拿到：yogesh shahi（Building @ivy-research）、Rute Figueiredo（Software Engineer）。
- 公开报道：未搜索（无显式融资新闻线索，官网未披露）。

## 未查到 / 待补

- **融资 / 投资方 / 加速器**：官网、PH、GitHub 均未披露，Ivy Research LLC 是否拿过钱未查到。
- **团队规模全貌**：仅查到 Rute Figueiredo、yogesh shahi、@aayushtheg 三人；公司所在地、其他成员未查到。
- **绝对里程碑时间线**：GitHub commit 仅给 commit message 与相对顺序，未见官网 About/Company 页或带绝对日期的 changelog 表。
- **数据集实际内容与体量**：归档当日 screencap.sh/dataset 显示 0 recordings，捐献规模、首批合作训练方未查到。
- **标注（labeling）层技术细节**：创始人明确说 labeling 不在这层，由 @aayushtheg 负责，具体方案未公开。
- **Windows / Browser / Android 发布时间**：仅标注 "Coming soon"，无具体日期。
- **Team cloud 定价**：仅 "Contact us"，无公开价格。
- **license 边界**：PolyForm NC 1.0.0 是否允许企业内部用源自建（非商用内部使用算不算商用）需法务判读，本文档不判断。
