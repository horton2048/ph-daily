# NextDoor.Company · 扩展阅读上下文

> PT 2026-08-05 Product Hunt 榜单第 3 名 · 👍 430 · 💬 61
> 归档日期 2026-08-06 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | NextDoor.Company |
| 英文 tagline | Discover startups hiring near you, on a map |
| 中文 tagline | 在地图上发现你附近正在招人的创业公司 |
| 官网 | https://www.nextdoor.company |
| PH 页 | https://www.producthunt.com/products/nextdoor-company |
| 品类标签 | Hiring · Maps · Career（PH 页另标 Job boards、Free Options、Lifetime Plan） |
| 票数 / 评论 | 430 / 61（PH V2 API 2026-08-06 抓取；日榜截稿 431） |
| 公司主体 | 独立开发者产品（Sankalp Sinha 个人，印度 Bangalore；未查到法律实体名） |
| 企业版/关联站点 | 未查到（无企业版/公司信息页） |
| logo | https://ph-files.imgix.net/a13767d4-9635-476d-8220-5c0394971562.png |
| PH 关注 | 643 followers |

## 是做什么的（如实复述，不评价）

NextDoor.Company 是一个**地图优先（map-first）的创业公司求职发现平台**：把"正在招人的 startup"放在一张可旋转的 3D 地球/地图（底层用 Mapbox）上，用户按地理位置探索机会，而不是在传统列表页里刷。

官方定位原文："Find startups hiring near you, on a map. 400+ hand curated startups globally, 16,000+ live job openings updated weekly. Filter by work mode: remote, hybrid, or on site. See funding, valuation, and revenue details, verified founder profiles, key investors, and their investment details, all in one place."

上线时规模：410 家公司、16,541 个职位（官网 2026-08-06 抓取）。除了地图发现，还带"公司情报"档案（创始人、融资额、估值、收入、关键投资人、投资人明细、福利、工作模式、融资阶段、办公地址）和求职者工具（收藏职位、标记已申请、职位追踪器、职位提醒、Add company）。早期 beta，登录墙为 LinkedIn/Google。

## 解决什么问题（事实层面，不判断值不值得解）

- **好 startup 在招人但很难被找到**：maker 开场评论——"great startups are hiring every day, yet finding them often means jumping between LinkedIn, company websites, X and funding databases"；朋友抱怨"如果 startup 在招人，它们在哪儿？"、"在 LinkedIn/Indeed 上找不到好 startup 了"。
- **公司背景信息要开 20+ 个 tab**：求职者想看创始人是谁、融了多少、runway 够不够、有没有好 VC 背书、福利怎样、远程还是到岗——官方定位把这些"dig through 20+ tabs to find"的东西收进一个档案。
- **位置相关性**：用户想先知道公司离自己多远、是否真的在本地 hiring；用户评论称"帮我过滤掉其实不在我所在地招人的公司"。
- **列表式搜索的反面**：官方主打"不是另一张列表，而是一个可以探索的世界"——"X marks the opportunity. Quite literally."

## 怎么做的（技术原理/机制，事实层面）

- **地图优先界面**：Mapbox 驱动，支持 3D 地球旋转、缩放、多公司同址聚类（clustering）、"Go to my location"；公司以"图钉"形式分布（页面标语"X marks the opportunity"）。
- **数据为手工精选 + 全网聚合**：maker 自述自 2025 年 8 月起**手工挑选全球 top-tier startup**，职位每周更新；公司情报从全网收集后"stitches them together，再做一遍准确性校验"。
- **数据更新频率**：maker 称融资/估值类数据"变化不每周发生"，app 每几个月检查一次；职位类数据每周更新。
- **分层信息展示**：紧凑 pop-up 看要点，可展开侧栏看详细档案；公司档案示例（Figma）：行业、成立年、创始人（含个人介绍）、工作模式、IPO 阶段、总融资 $332.9M、估值 $10B、办公地址、8 个开放职位。
- **诚实性标注**：官网明示"NextDoor.Company is in early βeta and some information could be inaccurate or in the ballpark. Always double-check with original sources"；公司档案底部显示"Last updated: 25th February 2026 (5 months ago)"。
- **验证/登录墙**：仅允许 LinkedIn 或 Google 登录，官方说明"To make sure the platform remains spam free & only accessed by vetted professionals"。
- **筛选体系**：Hiring status（是否活跃招聘 206）、Work mode（Remote 1569 / Hybrid 865 / On-site 4312）、国家（US 1059 / India 626 / UK 178 / Canada 145 / Australia 140）、城市（Bengaluru 141 / SF 116 / NY 106 / Seattle 96 / Mumbai 96）、部门（Engineering 1945 / Sales 1310 / Marketing 511 / Product 403…）、融资阶段（Series A 48 / B 38 / Seed 32…）、投资人（Y Combinator 38 / Accel 20 / Peak XV 18 / Sequoia 15 / Tiger Global 11…）。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Sankalp Sinha（PH @sankalpdomore；独立开发者，Bangalore，33 岁，自称 14+ 年产品设计师） | PH 开场评论 |
| 背景 | 曾为创始人/startup 做数字产品设计；2025 年辞去月薪 $15,000 的全职工作全职做自己的产品（solopreneur 约 12 个月）；上次在 PH 展示产品是 2018 年 | PH 开场评论 |
| 融资 | 未查到外部融资（个人独立项目） | — |
| 投资方 / 加速器 | 未查到 | — |
| 合规认证 | 未查到 | — |
| 规模数据（maker 自述） | 约 50,000+ 注册用户；410 公司 / 16,541 职位 | PH 开场评论；官网 |

## 定价 / 商业模式

- **免费层可用**：登录后可看地图、筛选、收藏职位、标记已申请、职位追踪器；免费层解锁的公司数量有限（maker 在评论区回应"已扩大免费解锁的公司数"）。
- **Lifetime 一次性买断计划**：PH 上线周 42% 折扣，优惠码 **PH42**（maker 开场评论）；具体价格未公开抓到（定价页在登录墙后）。
- **商业模式要点**：面向求职者免费/一次性买断 + 平台"Add company"等增值入口；未查到面向企业的 B 端收费。

## 关联信息 / 生态

- **底层技术**：Mapbox（官网直接外链 mapbox.com）。
- **数据覆盖示例**：公司 logo 墙包含大量印度与全球公司（Swiggy、Flipkart、Zomato、Stripe、Google、Microsoft、Figma、Anthropic、AWS、Razorpay 等）；筛选面板投资人列表以 YC / Accel / Peak XV / Sequoia / Tiger Global 领先。
- **竞品定位**：maker 明确"不是另一个 job board"，差异化在"地图发现 + 公司深度情报"；用户对比对象为 LinkedIn / Indeed 及发现类产品。
- **PH 标签**：Free Options、Lifetime Plan；品类 Job boards。
- **公开用户评价（官网摘录）**：多位产品设计师/工程师反馈（Amazon、GitLab、Planful、XoXoDay 等）集中在"发现了 LinkedIn 上没见过的公司、全球/远程职位、地图交互流畅、信息 pop-up 恰好"。

## 技术时间线（官网/公开里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2025-08 前后 | 作为周末 hackathon 项目起步；开始手工精选全球 top-tier startup（"Since August last year"） |
| 2025-08 ~ 2026-08 | 持续增长至约 50,000+ 注册用户、410+ 公司、16,000+ 职位（周更新） |
| 2026-08-05 | 上线 Product Hunt（post created 2026-08-05T07:01:00Z），日榜 #3（430 👍 / 61 💬）；上线周 Lifetime 计划 42% 折扣（PH42） |

## 评论区反馈（事实摘录，不评价）

- **Akhil BVS（Hunter，开场）**：引荐 Sankalp；称 startup 招聘发现"broken"，NextDoor 帮助在地图上发现高质量 startup 并提供真正重要的上下文。
- **Sankalp（maker，自述）**：33 岁、Bangalore、14+ 年产品设计；2025 年辞去月薪 $15,000 工作做 solopreneur（12 个月）；产品源于周末 hackathon，因为"看到 startup 招聘潮但朋友说在 LinkedIn/Indeed 找不到"；手工精选自 2025 年 8 月；50,000+ 注册；上线周 Lifetime 42% off（PH42）。
- **Curious Kitty（提问）**：价值主张依赖"context"（融资/估值/收入、投资人、创始人），这些字段怎么采集和验证、怎么传达置信度/新鲜度？→ **Sankalp 回复**：全网收集、拼接、再做一遍准确性校验；融资/估值数据几个月才变一次，所以 app 只每隔几个月检查一次。
- **Rabnoor Singh（评论）**：新鲜度才是这类产品的生死线且要分字段——融资/估值老化慢、谁在招人几周就失效；一个笼统的"last updated"时间戳掩盖了这种差异；per-field 时间戳"是唯一诚实的版本"（该条未见 maker 直接回复）。
- **Lambert de beru（批评）**：想法好但**付费墙太激进**，不付费看不到价值；没找到删除账号/个人数据的入口 → **Sankalp 回复**：已扩大 freemium 解锁的公司数；如需可重置数据再看；想删账号可告知。
- **Prajwal Varma（用户）**：公司信息"spot on"，发现了 LinkedIn 上没见过/没发过招聘的公司；App 体验干净。
- **Kaavya Prasad（用户）**：被 launch 视频吸引，产品里探索了很久停不下来；地图优先 + 公司情报是亮点 → **Sankalp 回复**："open world discoverability on map"正是设计目标。
- **UI 反馈**：用户建议"2.5D UI 可能更好"。
- **功能建议**：希望加入非技术岗位、fractional work（远程碎片化工作）；已点赞远程选项。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/nextdoor-company（描述、643 followers、tag、Free Options / Lifetime Plan、maker 评论）
- PH V2 API：post slug `nextdoor-company`（id 1214477，votesCount/commentsCount/createdAt/description/makers 精确值；comments + replies 抓取）
- 官网首页：https://www.nextdoor.company（410 公司 / 16,541 职位、筛选面板数值、Figma 档案示例、beta 声明、logo 墙、Mapbox 外链、LIFETIME 入口）
- 官网登录/落地页：https://www.nextdoor.company/login（功能清单、用户评价摘录、"linkedin or google login"声明）
- 公开报道：未查到独立媒体报道（仅 PH 评论与官网用户评价）
- GitHub：未查到 NextDoor.Company 公开仓库（github 搜索命中无关项目）
- 说明：评论区用户名为 API 打码 [REDACTED]；maker 为 Sankalp Sinha（@sankalpdomore，makers 列表唯一成员）；开场 hunter 为 Akhil BVS（@akhilbvs）

## 未查到 / 待补

- **Lifetime 计划具体价格**：登录墙后，未公开抓到金额；仅知 PH42 折扣码与"42% off"。
- **公司法律主体**：未查到（产品页/官网无公司注册信息）。
- **公司情报数据源**：具体供应商（是否 Crunchbase / 官方融资公告）未披露；maker 只说"collects all the information across the web"。
- **收入 / 付费用户数**：未查到。
- **团队规模**：评论区与官网显示为单人（Sankalp），无团队页可证。
- **职位数据是否与公司官方招聘源直连**：未查到。
