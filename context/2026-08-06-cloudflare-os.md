# Cloudflare OS · 扩展阅读上下文

> PT 2026-08-06 Product Hunt 榜单第 1 名 · 👍 0（PH API 2026-08-06 返回 votes=0，页面显示"Launching today"，票数未呈现） · 💬 1
> 归档日期 2026-08-06 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Cloudflare OS（Cloudflare 公司第 52 个 PH 上线产品；产品页挂在 products/cloudflare 下，launch=cloudflare-os） |
| 英文 tagline | Build the AI operating system for your company |
| 中文 tagline | 为你的公司构建 AI 操作系统 |
| 官网 | https://os.cloudflare.app（产品入口）；https://www.cloudflare.com（公司） |
| PH 页 | https://www.producthunt.com/products/cloudflare?launch=cloudflare-os |
| 品类标签 | Open Source · Artificial Intelligence · GitHub |
| 票数 / 评论 | votes=0 / comments=1（PH API 实时值；PH 产品页显示"Launching today"） |
| 公司主体 | Cloudflare, Inc.（NYSE: NET，纳斯达克上市公司，全球边缘网络/CDN/安全公司） |
| logo | https://ph-files.imgix.net/edcb3719-f3b7-49e8-9676-27631af01cb9.png |
| 关联站点 | 博客 https://blog.cloudflare.com/cloudflare-os/ ；CIO 内部使用篇 https://blog.cloudflare.com/how-we-use-ai-with-cloudflare-os/ ；GitHub 双仓（见下） |

## 是做什么的（如实复述，不评价）

Cloudflare OS 是一个**开源的"公司级 AI 操作系统"**：公司里每个人（不只开发者）都获得一个 **agent 和可修改的工作空间**，围绕公司自己的上下文（术语、流程、系统、标准、工作方式）来构建应用、自动化工作、安全访问内部系统。它强调"操作系统"的双关：一是公司安全地用 AI 提效的底座，二是管理 AI 工作负载的系统（类比传统 OS 管计算资源）。

三个核心组件：
1. **Agent 工作空间**：grounded 在公司上下文和技能里，有隔离运行时，agent 可以写代码、跑代码。
2. **安全与治理框架**：控制 agent 对内部数据和服务的访问（见"怎么做的"）。
3. **个人可修改的应用平台**：公司里的人能构建、分享、持续改动的全栈小应用（gadgets）。

产品描述（PH/API 原文）："Give every person an agent and workspace built around how your company works, what it knows, and the systems it relies on. Cloudflare OS is the open source AI operating system companies can shape around their own context, tools, and rules."

## 解决什么问题（事实层面，不判断值不值得解）

- **内部 AI 应用碎片化 / 各自为政**：每个人各用各的 AI 工具，上下文不共享、不落地为公司资产。
- **非工程师被 AI 工具排除**：CIO Sam Rhea 称早期 AI 行动工具都是开发界面（CLI、编辑器、终端、Git），把非工程师留在外面。原则："Everyone deserves superpowers"（每个人都该有超能力）。
- **AI 访问内部系统的权限失控**：云安全团队一名销售员工曾向 CIO 要一堆 API key + 生产系统管理员权限去搭"SuperApp"。Cloudflare 原则："你用 AI 时，在系统里拥有的权限永远不该超过你本来有的。"（"You should never have more permission with systems of record when using AI"）
- **组织上下文比模型重要**：通用模型不了解公司的术语/流程/系统，必须有一层"精选的公司上下文"。
- **重复性人工苦活**（内部案例）：
  - CIO 的 IT 工单日报告：V1 每天烧"数千 tokens"重建几乎相同的报告 + 分类 + 起草，V2 用 gatekeeper 后原话 "I burn exactly zero tokens each time I load the initial report"（每次加载初版报告烧零 token）。
  - 销售团队过去一个月在 territory planning、proposal creation 等人工任务上省下 10,000+ 小时。

## 怎么做的（技术原理/机制，事实层面）

来源：官方博客（cloudflare-os / how-we-use-ai）双篇 + GitHub README

- **运行架构**：服务器代码跑在 **Dynamic Worker**（全局出站网络被禁用）；客户端代码跑在浏览器内沙箱 frame。
- **应用隔离**：每个 app 按需加载为 Dynamic Worker，实例化为一个 **Durable Object Facet**，每个 app 有自己的 **SQLite 数据库**——"slide deck 应用不可能有泄露你 slides 的安全 bug"。
- **RPC**：浏览器到服务器调用用 **Cap'n Web**（Cloudflare 开源的对象能力 RPC 系统），客户端代码可当普通 JS 函数调用，agent 也能调。
- **MCP 兼容**：支持现有 MCP 服务器（MCP Server Portals）；Cloudflare 内部多为自己按系统写 MCP server（即使系统有原生的），以加角色/区域级限流等控制，跑在 Workers 上，"维护负担几乎为零"。
- **模型路由**：所有推理调用走 **Cloudflare AI Gateway**，任意模型可用；请求按人/团队/工作空间归属；管理员可设预算、限流；AI Gateway 按角色门控模型，把用例导到更便宜模型——"不是人人都要 max-thinking，也不该每小时的邮箱摘要花 $20"。
- **权限模型（零访问起点）**：agent 和 app **默认零权限**，可申请资源、被授予或拒绝。生成的代码通过**类型化绑定**拿到资源（如 `env.PROJECT`），凭证与 agent/生成代码完全隔离。
- **Gatekeepers（安全网关）**：服务特定的 Workers，介于 Cloudflare OS 和外部服务之间。它们理解服务的 API/资源/操作、处理 OAuth、持有凭证、执行策略、记录读取、调解有副作用的操作。示例限制：只允许单个 repo、只读 issue 不读源码、字段脱敏、限流、合并 PR 前要求审批。GitHub README 称其为"超级版 MCP server"，支持异步人审（本地模拟结果，agent 不用干等审批）。
- **观察追踪（Observation tracking）**：系统记录 agent 观察过的每个资源；当任何人打开工作空间或其输出，Gatekeepers 会**重新验证**该人对被观察资源的当前访问权。观察日志还能门控外部请求：读敏感数据会阻止写外部源、邀请协作者、把工作交给另一个 agent、或发出站请求。
- **入口与审计**：Cloudflare Access（Zero Trust）控制谁能进；Secure Web Gateway 的 DLP 规则可阻止数据集到达模型提供商。
- **分享模式**：Share app（别人实时协作同一份状态）vs Share **blueprint**（别人拿一份代码副本自己实例化，副本不含 SQLite 数据/对话历史/凭证/已连资源）。
- **确定性工作流**：mostly code，模型只在"判断能加分"处介入；可按需、按计划、按事件触发。
- **技术栈**：Cloudflare Workers + Durable Objects + Dynamic Workers + Facets；credits 提及 Pi (pi-agent-core)、Monaco、Yjs、Vite；可跑在 `workerd`（开源 Workers runtime）自托管（标注 COMING SOON）。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 公司主体 | Cloudflare, Inc.，纳斯达克上市公司（NYSE: NET），以全球边缘网络/CDN/Web 安全/Workers 平台知名 | 公司官网；PH 公司页（5.0 分 / 201 reviews / 5.5K followers / 2014 年首次上 PH） |
| 发布团队 | Phillip Jones、Dan Carter（官方博客作者）；PH 页面 launch team 另列 Chris Messina（PH 身份 "Hunter at Osaurus"，在评论中以 Hunter 身份发言，非博客作者，与 Cloudflare 的具体关系待核实） | 官方博客；PH launch post |
| CIO | Sam Rhea，撰写内部使用 companion 博客，引用内部使用数据与原则 | blog.cloudflare.com/how-we-use-ai-with-cloudflare-os |
| 融资 | 上市公司，无传统融资轮；Cloudflare 2026 年密集在 PH 上线新品（Wallets 8-05、Drop 7-11、Temporary Accounts 6-22、Email Service 4-17） | PH 公司页 launch 历史 |
| 加速器 | 不适用（上市公司产品） | — |
| 合规/认证 | 官方博客强调安全为平台内建（Access 入口、观察日志、DLP 路由）；具体 SOC2/ISO 认证未在抓取内容中提及 | — |

## 定价 / 商业模式

- PH 页标 **Free**；软件 **开源 Apache-2.0**，可部署进自己的 Cloudflare 账户（自己的 Access 策略、AI Gateway 配置、数据和集成）。
- **托管版**（Cloudflare dashboard 内 managed product）在官方博客中列为 future work，未公布价格。
- **商业逻辑**（事实归纳）：把平台开源免费，拉动对 Cloudflare 基础设施的消费——部署要求 Cloudflare 账户的 Workers、KV、R2、Browser Rendering、Dynamic Worker Loaders，AI 产品可选但推理默认走 AI Gateway。战略合作伙伴 **Presidio** 和 **Happy Cog** 负责给企业定制/落地（curating 技能与上下文、定制界面、接内部系统、配置安全/模型/成本控制），即"软件开源 + 生态服务收钱"的形态。
- 内部采用数据（CIO 博客，作为需求与效果的佐证）：数千人每周使用；日活每个工作日都在涨；近 30 天用户创建 4,000+ 个 apps/tools；销售团队月省 10,000+ 小时；过去四个月 Engineering Codex 标记约 250,000 个潜在问题、拦下 16,000 个 merge、在写代码前抓住约 600 个设计中的架构问题。

## 关联信息 / 生态

- **Cloudflare 2026 年 PH 上线序列**：Wallets（"the programmable wallet for the agentic Internet"，8-05 日榜 #5）、Drop（"Drop your folder in browser & deploy instantly"，7-11 日榜 #2）、Temporary Accounts（"Let agents deploy before signup"，6-22）、Email Service（"Turn any email inbox into a native interface for AI agents"，4-17）——同一波"agentic Internet / 企业 AI 基建"主题。
- **GitHub**：`cloudflare/cloudflare-os`（3.7k stars、252 forks、626 commits、Apache-2.0，README 自述 early access、v2 为完整重写、aug 2026 release "very capable, but still has many rough edges"）；`cloudflare/cloudflare-os-starter`（86 stars、18 forks、Apache-2.0，部署指南：pin 上游版本 + deployment.jsonc 控制 branding/identity/routing/data/integrations/AI/operations）。当前不接受外部贡献（"not seeking outside contribution"，≤~12 行小修复可能收）。
- **内部落地经验**（CIO 博客）：曾尝试"给非工程师友好的 dev 工具"，结果是"一屋子 vibe coded app 找问题"；后改为"魔法 email 别名"（小团队用 AI 工具处理大家不愿做的杂活）来发掘高频重复任务，再固化成 skills/context/data connections/自动响应。初期未雇专属 AI 团队，而是把各地区的早期采用者设成 champions（伦敦销售负责人、德州解决方案工程师、葡萄牙 IR 负责人、日本 BD、美国 Sales Ops）。
- **内部五个原则**：用 AI 是为了多陪客户/多做技术（先定义 jobs-to-be-done）；人人有超能力；人拥有产出（agent 创建者对输出负责）；组织上下文比模型重要；用 AI 时权限不得超过原有权限。
- **Roadmap**（官方博客）：Cloudflare dashboard 托管版；面向开发工作流的容器；Slack 及其他聊天工具里的工作空间。

## 技术时间线（官网/博客里程碑）

| 日期 | 事件 |
|---|---|
| 2014 | Cloudflare 首次上 Product Hunt（公司页，累计 52 次 launch） |
| 2025 | Cloudflare 内部对 AI 持"相当保守"态度——信息类聊天 app 和 boilerplate 代码 |
| 2026 跨年周 | 数百名成员（含非技术）在新年安静的几周试验 agent 行动能力 |
| 2026-05 | Cloudflare OS 在 Cloudflare 内部上线（V1），数千人每天使用 |
| 2026-07-11 | Cloudflare Drop 上线 PH（日榜 #2） |
| 2026-08-05 | 官方博客发布《Cloudflare OS》，开源（V2 为完整重写）；CIO Sam Rhea 发内部使用 companion 篇 |
| 2026-08-05 | Cloudflare Wallets 上线 PH（日榜 #5） |
| 2026-08-06 | Cloudflare OS 上线 PH（日榜 #1，"Launching today"，第 52 次 launch） |

## 评论区反馈（事实摘录，不评价）

- **Chris Messina（PH Hunter，评论 ID "Hunter at Osaurus"）**："Bold stuff from Cloudflare, and not just a random app. They're rethinking work in the agentic era from soup to nuts." ——"Cloudflare OS gives every person — not just developers — an agent and workspace that actually knows how your company works: its context, its tools, its rules." ——"Agents start with access to nothing and only ever see what you explicitly grant them, so collaboration never leaks what someone shouldn't see." ——开源（指向 Cloudflare OS Starter），并拿它与近期 "Buzz" launch 对比。
- 当日评论区其他线程（截至抓取，💬 1，仅上述 hunter 开场评论可见；其余反馈未查到）。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/cloudflare?launch=cloudflare-os（产品描述、launch team、hunter 开场评论、logo/gallery URL、Free 标价、tags、公司评分 5.0/201 reviews/5.5K followers、52 次 launch 历史）
- PH API v2：ph_daily 抓取（2026-08-06 榜单，votes=0/comments=1，thumbnail URL）
- 官方博客：https://blog.cloudflare.com/cloudflare-os/（产品形态、三组件、架构、权限/Gatekeeper/观察日志、开源说明、Presidio/Happy Cog 合作伙伴、Roadmap、发布时间 2026-08-05）
- CIO 内部使用篇：https://blog.cloudflare.com/how-we-use-ai-with-cloudflare-os/（五个原则、内部案例、10,000+ 小时、4,000+ apps、zero-token 报告、Codex 数据、champions 制度）
- GitHub：https://github.com/cloudflare/cloudflare-os（3.7k stars、Apache-2.0、README 概念与架构、gatekeeper 清单、自托管 workerd COMING SOON）；https://github.com/cloudflare/cloudflare-os-starter（86 stars、deployment.jsonc 控制面、README 部署步骤）

## 未查到 / 待补

- **当日票数**：PH API 返回 votes=0（页面显示 "Launching today"），PH 页未渲染出具体数字；context 无法确认真实票数。
- **托管版定价**：官方博客明确"managed product 为 future work"，无价格。
- **Chris Messina 与 Cloudflare 的关系**：PH 身份 "Hunter at Osaurus"（Osaurus 为 PH 站外 hunter 组织名），非官方博客作者；是否 Cloudflare 员工/顾问未查到。
- **V1 vs V2 详细差异**：博客仅称 V2 为完整重写；具体功能 diff 未查到。
- **外部企业采用案例**：除 Presidio/Happy Cog 两合作方外，尚无公开客户名。
- **真实票数/评论增长**：归档生成于北京时间 16:30（= PT 凌晨），当日榜单数据随票数积累会变动。
