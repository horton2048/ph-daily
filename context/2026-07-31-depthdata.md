# DepthData · 扩展阅读上下文

> PT 2026-07-31 Product Hunt 榜单第 5 名 · 👍 170 · 💬 24
> 归档日期 2026-08-01 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | DepthData（官网写作 Depthdata） |
| 英文 tagline | The system of record for your company's AI spend. |
| 中文 tagline | 企业 AI 支出的统一记录系统 |
| 官网 | https://depthdata.vercel.app/ |
| PH 页 | https://www.producthunt.com/products/depthdata |
| 品类标签 | Analytics · SaaS · Artificial Intelligence（PH 另分类：Budgeting apps · Business intelligence software） |
| 票数 / 评论 | 170 / 24（PH 页快照显示 175 points；归档数据为 170） |
| 公司主体 | Depthdata（官网页脚 © 2026 Depthdata. All rights reserved.，未查到注册主体） |
| 企业版/关联站点 | 未查到独立企业版站点；LinkedIn: linkedin.com/company/depth-data/ |

## 是做什么的（如实复述）

DepthData 是一个**面向企业的 AI 支出与采用度（adoption）统一记录系统**。它通过 OAuth 只读连接企业已在用的 AI 工具管理控制台（ChatGPT Enterprise、Claude Enterprise、GitHub Copilot、Gemini Workspace、Cursor、Vercel + AI Gateway、Notion AI、Replit、Lovable、Mistral/DeepSeek/Grok/GLM 等），把分散在多个 admin console 里的 seat、session、usage、spend 数据同步到一个统一数据模型，输出四个产品面：（1）Overview 工作区健康分；（2）Coaching 教练/提示；（3）Analytics 趋势分析；（4）Leaderboard 深度使用排行。

定位：不是又一个 AI 使用看板，而是"可审计、可追溯到一个来源"的 system of record——每个数字都带一个置信度标签（MEASURED / DERIVED / MODELLED），标签随数字一起导出。

部署形态：纯 SaaS，无 agent 装在员工设备上，无浏览器扩展，只读 OAuth 接入厂商官方 admin API。

## 解决什么问题（事实层面，不判断值不值得解）

- **多 AI 工具支出不可见**：官网主张——公司一年付六位数（six figures）AI 工具费用，却答不出董事会最基本的问题："这些钱花得值吗？" ChatGPT、Claude、Copilot、Gemini 各自有 admin panel、各自定义"usage"，没有人能看到全貌。
- **财务/工程/IT 数据对不上**：PH 评论区用户 Artur Brugeman 真实反馈——"每个团队开始自己 expense API key 和 seat license 那一刻，我们就失去了对 AI 支出的追踪。财务看到一个数，工程看到另一个，没人能解释 gap。"
- **看板"看起来自信但来源不清"**：创始人 Ali Uyanik 自述——"我厌倦了那种看起来很自信、但你一问'这个数从哪来'就崩的看板。"
- **目标场景**：CFO/CIO/Board 汇报、季度审计、IT 许可证优化、AI 采用度 coaching。

## 怎么做的（技术原理/机制，事实层面）

- **只读 OAuth 接入厂商 admin API**：每日定时同步（daily sync）拉取 seats、sessions、usage events、spend。无 agent、无浏览器扩展、无 scraping。
- **5 段流水线**（methodology 文档 V3.23）：①INGEST 只读取 → ②NORMALIZE 解析到 canonical person（通过 SCIM 目录身份）→ ③BASELINE 对比你自己的前 4 周 → ④ESTIMATE 仅在无法直接测量时建模，带 ± band → ⑤SCORE 用公开公式加权。原则："流水线从不倒置，估算永远是第四步而非第一步。"
- **3 类置信度标签**（每个数字都带，随导出一起）：
  - `MEASURED`：直接从 API 拉取，原样不变（tokens、spend、seat count）。
  - `DERIVED`：从 measured 输入计算，公式可见（cost-per-outcome、weighted output）。
  - `MODELLED`：从信号和样本估算，必带 ± band（baseline-relative lift、hours saved）。
- **Connector 透明度矩阵**（官网公开）：明确列出每个厂商 API 能暴露什么、不能暴露什么。例如：
  - ChatGPT Enterprise：seats/roles=API, usage=EXPORTS+LOGS, spend=API, audit=API
  - Claude Enterprise：全部 API
  - GitHub Copilot：全部 API（audit 需 GitHub Enterprise Cloud）
  - Gemini (Workspace)：spend=CLOUD BILLING（非直接 API）
  - Notion AI：spend=NOT EXPOSED
  - Replit：spend=NOT EXPOSED（仅 SCIM + EXPORTS）
  - Lovable：usage/spend/audit 全部 NOT EXPOSED
  - 官网主张："vendor 暴露不了的部分，我们显示为 gap，不估算。"
- **Prompt 永不读取**：架构层面保证——只读 metadata scope，能含对话内容的 feed 在 ingestion 时丢弃，不含内容的 API 设计上就不到达。是"架构属性，不是设置项"。
- **Right-sizing engine**（产品功能）：识别可降 tier 的 seat、idle license、duplicate coverage（如 Cursor + Copilot 重叠），给出可回收金额估算，并标注"within tolerance"是离线估算，建议先 pilot 2 周。
- **Expense reconciliation**（评论区迭代产物）：用户 Dale Mooney 在 PH 评论区建议——"财务每月已导出 CSV 给会计，做个 dumb upload 把 vendor 名匹配到已连工具上"。创始人回复："你的评论太好，我当场 built 了。"功能：上传财务 CSV，浏览器内匹配 vendor 名，未匹配项显示为"named gap"，全程不上传服务器。
- **输出连接器**（cost-per-outcome 的分母侧）：Jira、GitHub、Linear、HubSpot、Salesforce、Zendesk 拉取 completed-work metadata，按 identity join。Product/Design/Legal 无 clean per-person output unit → 官网主张"flagged, never estimated"。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Ali Uyanik（PH 自述 Senior Product Designer；PH 评论"I'm building it mostly solo"） | PH makers 页 + 创始人评论 |
| 团队规模 | 1 人（solo，自述） | PH 创始人评论 |
| 融资 | 未查到（官网/PH 页/LinkedIn 均未披露） | — |
| 投资方 | 未查到 | — |
| 加速器 | 未查到 | — |
| 合规认证 | 未查到（官网有 Security / Privacy / Terms 页面占位，但本文档生成时未抓到具体认证内容） | — |
| 上线时间 | 2026 年（PH 页"Launched in 2026"，"Launched this week"） | PH 页 |

## 定价 / 商业模式

- **官网未公开定价**。首页 CTA 为 "GET EARLY DEMO"，跳转到联系表单（Name / Work Email / Company / 询问内容）。
- 无自助注册、无免费试用入口、无公开价目表。
- 推断为**早期企业销售制**（demo-driven onboarding），但本文档不下结论，标注为"未查到公开定价"。
- 商业模式（机制层面）：连接企业已在付费的 AI 工具 admin console，按"治理 + 审计 + 许可证优化"价值向 CFO/CIO 卖。Right-sizing engine 给出可回收金额（demo 示例：49 seats ChatGPT Enterprise → Business 降级，月省 $1.58k）——是面向财务的 ROI 切入点。

## 关联信息 / 生态

- **16 个连接器**（官网列）：ChatGPT Enterprise、Claude Enterprise、GitHub Copilot、Gemini (Workspace)、Cursor、Perplexity、Notion AI、Slack AI、Replit、Lovable、Mistral、DeepSeek、Grok、GLM、Vercel + AI Gateway（共称"16 tools. One ledger."）。
- **Built With**（PH 页标注）：Anthropic Claude。
- **Demo 数据**：官网所有数字（218/287 active seats、$48.2k/mo spend、76/100 health score、1,248 hours automated、14% shadow AI 等）均为**modelled workspace, not a customer**——methodology 页明确声明"Every figure on this page matches the DepthData product demo and carries the same confidence label the product would give it."。
- **竞品定位**：PH 页"Similar Products"列出 beams（Work Intelligence Platform）、Datatera.ai、Eden AI、Basedash: AI data analyst、Ada.im。官网未做显式竞品对比表。
- **关联社交**：X / Twitter（官网外链占位）、LinkedIn: linkedin.com/company/depth-data/。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026 | PH 页标注"Launched in 2026" |
| 2026-07-28 | PH 上线（"3d ago" 相对 2026-07-31），榜单第 5 |
| 2026-07-29 / 30 | 创始人在 PH 评论区与用户讨论并当场 ship 了 expense reconciliation 功能（"built it just now"） |
| methodology V3.23 | 当前 methodology spec 版本号（无具体日期） |

官网无独立 About / Company / Milestones 页面，技术时间线主要从 PH 评论区推断。

## 评论区反馈（事实摘录，不评价）

- **Artur Brugeman**：每个团队自己 expense API key 和 seat license 后，AI 支出就失控了。财务一个数、工程另一个、gap 没人解释。问：是从 provider billing 拉还是 usage log？能 attribute 到 team/project 吗？
  - **Ali 回复**：两者都有，看工具。Anthropic、OpenAI、Cursor 有真实 cost API，直接拉 dollar spend。其他工具拉 usage data + 合同价。每个数带 label。团队：工具知道谁有 seat 但不知道 org chart，manager 在 employee table 里手动分配。项目：能直拉的直拉（OpenAI API platform、Vercel tagging）；Claude 给 project usage 但不给 cost → 按每人 project 使用比例分摊，标 ALLOCATED 而非 measured。Session level："honest no"——reporting API 不暴露单次 run。
- **Martín Herrán**：自家产品跑在 Anthropic API 上，每个 feature 每 run 成本靠手工 spreadsheet。问能不能 trace 到 feature/session 级。
  - **Ali 回复**：Anthropic API 最深到 daily by workspace/model/token type；usage 到 minute bucket by API key/workspace/model。Trick：每个 feature 给独立 API key/workspace。Session level 不行。
- **Dale Mooney**（被创始人称"too good to leave as a comment"）：AWS 支出经验里 totals 从来不是难点，attribution 才是；改变行为的是"名字旁边的 line"。建议——shadow spend（个人 ChatGPT 订阅）vendor API 永远给不了，但财务每月已导出 CSV，做个 dumb upload 匹配即可。
  - **Ali 回复**：当场 built 了 expense reconciliation section。上传 CSV → 浏览器内匹配 vendor 名 → 未匹配项显示为 named gap。并接受 Dale 后续建议（vendor 字符串脏，需让用户确认一次 mapping 并记住；未匹配 pile 作为 first-class output 而非 error state）。
- **Gal Dayan**：跨工具重叠（两个工具 80% 重叠功能、同一拨人用）才是真浪费，不是单工具内 idle seat。
  - **Ali 回复**：可测——同一个人在两个同类工具都有 seat 且都活跃，能给出"40 人同时付 X 和 Y，第二个的成本"。但不替你选 winner，judgment 留给客户。
- **Asad M.**：verification label 才是真产品，dashboard 只是载体。usage-priced 工具上一个人能 outspend 四十人，seat view 看不出来。
  - **Ali 回复**：展示 cost per person 而非只 seats；Anthropic/OpenAI/Cursor 都暴露 per-user spend。Gap：Gemini 在 Workspace 里 bundle，无 per-user cost；Replit credits pool 无 per-member API；Vercel 需先 tagging。
- **Raffay Sajjad**：ALLOCATED vs measured 标签是对的——六个月后没人记得哪个是估算、哪个是事实。
  - **Ali 回复**：标签随数字走，exports 和 reports 每个数都带 MEASURED/ALLOCATED。"Once an estimate loses its label it becomes a fact, and that's how dashboards quietly go wrong."
- **Arash Rahimi**：never reading prompts 是过 security review 的关键细节。
  - **Ali 回复**：read-only + metadata only，连接的 endpoint 根本不带 prompt content。"Narrow scope is the architecture, not a promise."
- **Shivarchan C**：建议把"哪些 vendor 暴露不了什么"放页面上而非藏在 doc 里；建议未来 cross-check SSO/IdP（Okta、Entra）拿更真实的使用情况。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/depthdata（拿到了产品描述全文、254 followers、Launch Team #5 175 points、评论区全文）
- PH makers 页：https://www.producthunt.com/products/depthdata/makers（拿到了创始人 Ali Uyanik 头衔 Senior Product Designer）
- 官网首页：https://depthdata.vercel.app/（拿到了产品定位、四个产品面、16 个连接器、connector 透明度矩阵、Right-sizing engine、AI risk register、demo 数据声明）
- 官网 methodology 页：https://depthdata.vercel.app/methodology.html（拿到了 5 段流水线、3 类置信度标签、7 条原则、V3.23 spec 版本号）
- 公开报道：未搜到独立媒体报道（搜索关键词：DepthData AI spend / Ali Uyanik DepthData）
- GitHub：未查到公开仓库（官网/PH 页无 GitHub 链接；公司疑似闭源）
- LinkedIn：linkedin.com/company/depth-data/（存在公司页面，本文档未单独抓取）

## 未查到 / 待补

- **融资信息**：官网、PH 页、LinkedIn 均未披露融资轮次、金额、投资方、加速器。solo founder 自述"building it mostly solo"。
- **公开定价**：无定价页，无自助注册，仅"GET EARLY DEMO"联系表单。
- **企业注册主体**：官网页脚仅"© 2026 Depthdata"，未查到具体公司注册名、注册地、税号。
- **团队规模**：仅确认 Ali Uyanik 一人，是否有 co-founder 或早期员工未查到。
- **合规认证**：官网有 Security / Privacy / Terms 占位页，本文档生成时未抓到 SOC 2 / GDPR 等具体认证内容。
- **客户案例**：官网 demo 数据明确声明"modelled workspace, not a customer"，无真实客户 case study 或 logo 墙。
- **GitHub 仓库**：未查到公开仓库。
- **独立媒体报道**：未搜到 TechCrunch / SaaSHub 等第三方报道。
