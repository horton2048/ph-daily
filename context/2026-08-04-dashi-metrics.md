# Dashi Metrics · 扩展阅读上下文

> PT 2026-08-04 Product Hunt 榜单第 5 名 · 👍 206 · 💬 11
> 归档日期 2026-08-05 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Dashi（Dashi Metrics） |
| 英文 tagline | Visualize your revenue on a 3D globe |
| 中文 tagline | 在 3D 地球仪上可视化你的收入 |
| 官网 | https://www.dashimetrics.com/ |
| PH 页 | https://www.producthunt.com/products/dashi-metrics |
| 品类标签 | Analytics · SaaS · Data Visualization（PH 品类：Data visualization tools / Website analytics） |
| 票数 / 评论 | 206 / 11（任务快照口径；PH 页实时抓取显示 211 票、评论区 7 条主评论，任务口径与实时值略有差异） |
| 公司主体 | 未查到（官网无页脚公司注册信息） |
| logo | https://ph-files.imgix.net/0de98738-612d-476a-9213-aa01c533f1aa.png |

## 是做什么的（如实复述，不评价）

Dashi 是一个把网站访客和收入实时映射到 3D 地球仪上的"环境式 / lofi（ambient）"数据可视化产品。运行形态：全屏 3D 地球，访客到访时在地球对应地理位置弹出标记（pin），支付发生时出现动画并播放"收银机"音效（官网素材含 `/audio/revenue-cha-ching.m4a`）。产品自我定位是"Lofi analytics on the globe"——"live stats, music, and vibes. Not a spreadsheet dashboard"（代码内文案）。官网 meta 描述："A full-screen ambient analytics globe with live numbers, chill music, and vibes. Leave it open all day — not another SaaS dashboard." PH 页面描述："Watch your business come alive—every visitor and payment mapped in real time on a dynamic 3D globe. Dashi transforms static dashboards into live, geographic visualizations… Perfect for SaaS teams and founders who want actionable, visual insights instead of boring charts." 用法上，用户在官网"claim your globe"（认领自己的地球）、安装追踪脚本、连接 Stripe 后，收入即开始落到地图上。PH 页面标注产品于 2026 年发布。

## 解决什么问题（事实层面，不判断值不值得解）

- **仪表盘"死气沉沉"**：创始人 Ammar Rayess 开场评论："frustrated by how lifeless most dashboards feel—just rows of numbers and static charts"（大多数仪表盘只有成排数字和静态图表）。
- **静态图表不直观 / 缺乏"正在发生"的感觉**：把数据变成地理维度的实时可视化；评论区用户 xinyuanwei 转述官网语境："Sometimes a dashboard's real job isn't analysis"——让团队感到有事情在发生（官网文案 "Somewhere out there, they're shipping" / "They're probably checking analytics rn"）。
- **GA4 归因报表难翻**：创始人评论区回应 Gal Dayan："full attribution in an easy and simple one click rather than digging into the complex reporting system of GA4"（一键看完整归因，不必钻进 GA4 的复杂报表体系）。
- **目标场景**：SaaS 团队与创始人的大屏 / 办公室显示器，作为"常驻屏幕"的沉浸式数据展示（创始人："i open it when i start my work day and just leave it open"）。

## 怎么做的（技术原理/机制，事实层面）

来源：官网 JS 资源反编译 + https://dashimetrics.com/js/script.js 追踪脚本原文（2026-08-05 抓取）

- **接入方式**：认领 globe → 安装追踪脚本 →（可选）连接 Stripe，收入即出现在地图上（官网引导文案："Claim your globe, install the script, connect Stripe — your revenue starts landing."）。
- **追踪脚本机制**（客户脚本为自建 Plausible 式第一方脚本，URL 形如 `https://dashimetrics.com/js/script.js`，用 `data-domain` / `data-website-id` / `data-api` / `data-track-localhost` 属性配置）：
  - **事件端点**：默认取脚本路径推导为 `<origin>/api/event`，可用 `data-api` 覆盖（支持反广告拦截器代理前缀 proxyPrefix）。
  - **事件类型**：pageview、goal、revenue、outbound、friction（卡住评分），另有设备端 bot 过滤。
  - **收入事件 API**：`dashi("purchase", { revenue: 29.99, currency: "usd", product: "Pro" })`，脚本内 `payload.rc = Math.round(revenue*100)` 将金额转成分发送。
  - **第一方访客 ID**：localStorage 为准 + 镜像到 `dashi_visitor_id` cookie，供服务端（如结账路由）读取，实现收入归因到访客。
  - **bot 检测**：检查 `navigator.webdriver`、`_phantom` / `__nightmare`、UA 正则（headlesschrome|phantomjs|selenium|puppeteer|playwright|webdriver）。
  - **"访客卡住"（friction）评分**：纯设备端计算，超过阈值发 friction 事件（每 pageview 上限 3 条）。
  - **投递**：优先 `navigator.sendBeacon`，否则 fetch；处理 SPA 导航与页面停留深度 flush。
- **收入归因维度**：每个支付追溯至 keyword（关键词）、page（落地页）、channel（渠道）、country（国家/地域）。官网文案："Every payment traced back to the keyword, page, channel, and country it came from. Traffic tells you who came — this tells you who paid."
- **实时呈现**：访客 pin 实时落在对应经纬度并显示数量峰值动画；支付触发庆祝动画 + 音效；左面板展示流量 / 渠道 / 页面（owner 选择可共享的），右面板实时流展示访客 / 目标 / 退出，底部可用 emoji 互动。
- **目标条**：周 / 月目标，团队与分享链接访客看到同一进度（代码内 feature guide："The goal bar tracks a weekly or monthly target — team and share-link guests see the same progress."）。
- **权限 / 分享**：globe 默认私有，分享链接 + 团队邀请控制进入；owner 可在设置中选择自己的 pin 是否出现在只读世界地图，或隐藏走 invite-only（"What you see as a guest is what the owner chose to share… Nothing is leaked by accident."）。
- **个性化**：Globe skins（地球皮肤）、pin 动画、访客头像风格、背景音乐（默认 ambient 或自定义 YouTube 链接 + 可选随节拍光晕 glow pulse）、环境天气效果（`/api/weather?globeId=…` 返回昼夜/氛围 mood）。
- **技术栈线索**（JS chunk 反编译）：Next.js + React、Better Auth + Neon Postgres（neon auth / OAuth popup）、Stripe（订阅 / `/api/stripe/checkout`，含 `stripeProductIds`、billingLocked 状态）、Supabase 引用、Radix UI、Tailwind CSS、自建第一方统计脚本 + GTM（GTM-PZW6PN7C）埋点；PH 页标注 "Built with Cursor"。
- **演示模式**：`/demo` 提供带样本数据的可交互 demo globe（含 dev 演示事件：pageview、goal "Sign up"、revenue "Pro plan" $49、outbound "GitHub"、friction "Checkout form"）。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Ammar Rayess（@therayess，PH maker）与 Dev Tanna（@dev_tanna，PH maker） | PH 产品页 |
| 团队 | 两位公开 maker，规模未披露 | PH 产品页 |
| 融资 | 未查到（无任何融资报道；创始人称仍在验证阶段） | WebSearch |
| 投资方 | 未查到 | — |
| 加速器 | 未查到 | — |
| 公司注册主体 | 未查到（官网无页脚公司信息） | — |
| 发布时间 | 2026 年 | PH 产品页 |
| PH 关注数 | 266 followers | PH 产品页 |

## 定价 / 商业模式

- **现状：免费，仍在验证阶段**。PH 上线标价 Free，提供免费档给 PH 用户试用并认领自己的 globe（创始人开场评论）。创始人回复 Germán Merlo 的货币化提问："can't think of monetizing yet, still in validation phase… probably it'll be a subscription based on how many events you're collecting"（还没想清楚怎么变现，还在验证阶段；大概率会做成按收集事件量计费的订阅）。
- **代码线索**：存在 Stripe 结账路由（`/api/stripe/checkout`）与"subscription inactive — renew →"提示、"billingLocked"（订阅未激活时部分功能锁定）等状态；demo 演示数据里有一个 "Pro plan" 事件，revenueCents:4900（即 $49），但这属于演示/开发样本数据，非正式对外定价。
- 模式方向：按事件量计费的订阅制（创始人自述，未落地）。

## 关联信息 / 生态

- **产品形态定位**：与 "ambient analytics" / "lofi analytics" 绑定，强调"不是又一个 SaaS 仪表盘"（官网 meta："not another SaaS dashboard"）。
- **竞品对照（评论区）**：被问到与 Apple Store Analytics（自带购买地点图）的区别，创始人答：Dashi 覆盖普通网站流量/访问而不只是商店购买，"不同工种、不同心情"；被问到 vs 按国家排序表格，创始人答"同样的数据，更 zen 的体验"，且一键完整归因优于深挖 GA4。
- **隐私口径**（创始人评论区回应 Brent Vardy）：只收集做站点分析和收入归因所需的数据，保持 first-party，globe 默认私有，"we're not an ad tracker"。
- **安全/交互能力**：分享链接 + 团队邀请、只读世界地图、访客 emoji 互动、目标条。
- **内部埋点**：dashimetrics.com 自身站点用 GTM + 自建统计脚本统计（页面活动事件含 domain_connected、checkout_started 等）。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-08-04 | 登上 Product Hunt 日榜第 5 名（PH 页标注产品于 2026 年发布；官网无更早时间线/新闻页） |

## 评论区反馈（事实摘录，不评价）

- **Ammar Rayess（Maker 开场评论）**：为何做 Dashi——"We built Dashi because we were frustrated by how lifeless most dashboards feel"；给 PH 用户提供免费档试用并认领自己的 globe；向用户征集"你希望仪表盘能展示哪些全球趋势/实时信号"。
- **Henrick（提问）**：很惊艳，但和 Apple Store Analytics（本身已显示购买发生地点）有什么区别？/ 创始人：它是报表，Dashi 更像"在你桌面上开着的窗"——地球上的实时流量、一点音乐、氛围；且 Dashi 覆盖普通网站流量/访问，不只是商店购买，"different job, different mood"。
- **Brent Vardy（提问）**：有没有文档说明如何把数据分享到仪表盘？有隐私政策吗？/ 创始人：安装有两种方式——复制一段 AI 提示词直接丢给你的 coding agent（AI-prompt-based setup），或手动流程；隐私：只收集站点分析与收入归因所需、保持 first-party、globe 默认私有、"我们不是广告追踪器"。/ Brent 回复："Thanks for the clarification."
- **Germán Merlo（提问）**：太酷了，你打算怎么变现？/ 创始人：还没想好，仍在验证阶段；"probably it'll be a subscription based on how many events you're collecting"。
- **xinyuanwei（评论）**：自定义项多到"几乎太多"，但放大办公室大屏后所有人都停下来看下一个支付落在哪。/ 创始人：它是个体验——我每天开工就打开一直放着，"command center-like" 的感觉就是不一样。
- **Gal Dayan（质疑）**：一旦客户超过几个，旋转的地球就不可读了……地球视图到底能告诉你什么按国家排序的表格给不了的？/ 创始人：给的是同样的数据，但更 zen 的体验；且一键完整归因，不必钻进 GA4 复杂报表。
- **MD Amirul Islam（评论）**：大多数分析工具聚焦图表，Dashi 让数据"活起来"，地球可视化立刻抓住注意力。/ 创始人："makes the data feel alive" 正是我想达到的效果。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/dashi-metrics（产品描述、tagline、品类标签、logo URL（ph-files.imgix.net 0de98738-612d-476a-9213-aa01c533f1aa.png）、创始人 Ammar Rayess/Dev Tanna 标注、maker 开场评论、评论区 6 条用户互动与创始人回复、266 followers、Built with Cursor）
- 官网首页：https://www.dashimetrics.com/（meta 标题/描述、"Lofi analytics on the globe" 定位、"claim your globe →"、/demo 演示入口）
- 官网 JS 资源反编译（`/_next/static/chunks/*.js`，2026-08-05 抓取）：feature guide 文案（How Dashi works / Set up your globe / What guests see / Happening now / Target goals / Personalize）、收入归因文案、权限与分享文案、技术栈线索（Better Auth + Neon、Stripe checkout、supabase、radix、GTM）、/api/weather 与环境氛围
- 官网追踪脚本：https://www.dashimetrics.com/js/script.js（事件端点 /api/event、事件类型、bot 检测、friction 评分、dashi_visitor_id cookie、收入事件 API）
- 官网 API 探测：/api/weather（需真实 globeId）、/api/stripe/checkout（返回 307，重定向至 Stripe）
- GitHub：无公开仓库（api.github.com/users/dashimetrics 不存在；仓库搜索 "dashi metrics" 无相关结果）
- 公开报道/融资：WebSearch 多组关键词（"Dashi Metrics revenue 3D globe startup" / "Dashi lofi analytics globe" / "Ammar Rayess Dashi" / "Dev Tanna developer"）均无相关结果

## 未查到 / 待补

- **公司注册主体 / 注册地**：官网无公司信息，未查到
- **融资金额/轮次/投资方/加速器**：未查到（无任何融资报道）
- **团队规模**：仅两位公开 maker（Ammar Rayess + Dev Tanna），具体人数未披露
- **创始人过往经历/背景**：WebSearch 未检索到 Ammar Rayess 与 Dev Tanna 的公开履历
- **正式定价**：未对外公布。代码 demo 数据中的 "Pro plan $49/月"（revenueCents:4900）仅属演示样本，不能视为正式价格
- **收入/事件量上限、各档权益明细**：官网无 Pricing 静态文案，定价页由 Stripe 产品数据客户端渲染，未抓取到
- **精确评论数**：任务快照 11 条 vs 页面抓取口径（211 票；评论区 7 条主评论），存在口径差异，未统一
- **媒体测评/第三方报道**：未查到
- **GitHub**：无公开仓库（闭源）
