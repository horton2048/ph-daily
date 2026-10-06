# VIDEO AI ME · 扩展阅读上下文

> PT 2026-08-04 Product Hunt 榜单第 9 名 · 👍 125 · 💬 5
> 归档日期 2026-08-05 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | VIDEO AI ME（官网书写为 VIDEOAI.ME，PH 本次发布名 VIDEO AI ME Social Scheduler） |
| 英文 tagline | Make videos and post them everywhere with just one tool（PH 页另有 "Create videos with AI actors that sound and look real"） |
| 中文 tagline | 用一个工具做视频并发布到所有平台 |
| 官网 | https://videoai.me |
| PH 页 | https://www.producthunt.com/products/video-ai-me |
| 品类标签 | Social Media · Marketing · Artificial Intelligence |
| 票数 / 评论 | 125 / 5 |
| 公司主体 | 未查到注册主体（官网自述 founder-led and independent） |
| logo | https://ph-files.imgix.net/59d086af-edf3-4faf-ad74-2a936f34a41d.png |

## 是做什么的（如实复述，不评价）

VIDEO AI ME 是一个面向电商品牌、效果广告主和营销代理的 **AI 视频生成 + 社交发布一体工具**，定位"AI 视频生成器，专门产出能投广告、能原生爆火的视频"。

- **视频生成端**：把产品照片和脚本变成成片广告素材——UGC 风格广告、产品演示、口播（talking-head）、解说视频。AI 演员 300+ 个、可自定义克隆；支持 70+ 语言配音与对口型。
- **发布调度端（本次 Social Scheduler 发布的核心）**：通过官方 API 连接 15 个平台（TikTok、Instagram、YouTube、X、LinkedIn + 另外 10 个），AI 按平台自动写 caption，可批量定时发布 25-30+ 条视频，并有表现数据页（Performance tab）告诉你哪个平台哪条视频赢了，可一键转发赢家或让 AI 重新生成新版本。

官网一句话：把"脚本 + 产品照片"变成"可直接投放的广告创意"，不需要摄像机、不需要复杂软件。

## 解决什么问题（事实层面，不判断值不值得解）

来源：PH maker 开场评论 + 官网

- **内容生产之后的分发断层**（maker 亲述痛点）：用户用 AI 能生成"真的很不错的视频"，但"勤奋地日更一周就停了"。maker 观察："视频从来不是问题，分发才是（Distribution was）。" 用户缺的是持续的、多平台的分发能力，于是他把调度直接做进工具里。
- **制作成本与周期**（官网成本对比）：外包一个 UGC 视频 $150-200+、耗时 1-2 周；官网示例 8 条视频/月外包 $1,600，对比 Pro 档 $99/月，宣传"你省下 $1,501 + 22 小时"。
- **多语言多平台适配耗时**：同一脚本要适配不同平台调性和语言，官网宣传"获奖脚本可在 70+ 语言、原生对口型地重投"，一条视频从创意到可发布约 15 分钟。
- **目标场景**：电商/铺货（dropshipping）广告素材、SaaS/App 演示、机构为客户批量出素材、各平台多账号分发。

## 怎么做的（技术原理/机制，事实层面）

来源：官网首页 / about / pricing / llms.txt + PH maker 评论

- **AI 演员与克隆**：300+ 现成 AI 演员；用一张照片即可克隆自定义演员（custom actor），每位演员可配最多 200 套服装/场景造型；Premium 档含 10 个自定义演员。
- **声音**：300+ 拟真声音；用一小段音频样本即可克隆声音（voice cloning）；70+ 语言 TTS + 帧级对口型（frame-accurate lip-sync）。
- **Photo-to-Ad 机制**：上传产品照片 + 简短描述，"VIDEO AI ME 推断目标、受众和 CTA，然后自行撰写并产出广告"。
- **AI 剪辑**：自动生成与配音同步的字幕（auto captions）、静音自动裁剪（smart trim）、AI 自动插入 B-roll。
- **视频模型**：单一订阅内含 Sora 2、Kling 2.6、Grok Imagine 1.5 及"独家"的 Seedance 2.0；每个生成任务可选模型（"You pick the model per generation"），宣传可"Day 0 拿到新模型"。
- **输出规格**：竖屏 9:16、横屏 16:9、方形 1:1；Starter/Pro 最长 3 分钟，Premium 最长 12 分钟；无水印、每支视频含完整商业授权（含为客户工作）。
- **调度端机制（Social Scheduler）**：通过官方 API 连 15 个平台；AI 按平台自动写 caption（如 TikTok 加 hashtag、LinkedIn 用专业语气）；按地点/主题/行业算最优发布时间批量排期；Performance tab 展示各平台表现数据。
- **账号要求边界**（maker 评论区）：需 business/pro 账号的平台——Instagram、Facebook（发布到 Page 而非个人主页）、Pinterest、Google Business、Snapchat、WhatsApp；普通账号即可——X、Reddit、Bluesky、Threads、YouTube、TikTok；Telegram/Discord 只需添加 bot；LinkedIn 个人主页与公司页均可。
- **token 过期处理**（maker 评论区）：帖子在队列页显示 Failed 或 Partial + 失败原因，对应账号被标 "Reconnect needed"，可一键重连；重试仅重发失败的平台，不重复已成功的。
- **路线图**（maker 评论）：下一步是自动化广告投放平台（Meta、TikTok、Google）。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Paul G（PH 昵称 @grsl_fr，本次发布 maker） | PH 产品页 |
| 公司结构 | "founder-led and independent"；"同一个小组负责产品、每周上线改进、直接回复支持邮件" | 官网 About |
| 融资 | 未查到 | — |
| 投资方 | 未查到 | — |
| 加速器 | 未查到 | — |
| 联系 | support@videoai.me | 官网 About |

## 定价 / 商业模式

来源：videoai.me/pricing（2026-08-05 抓取）+ llms.txt

- **无免费版**。模式：月订阅 + 视频 credit 制；年付赠 4 个月（宣传"from $19/month billed annually"）；Stripe 收款、一键取消；credits 不结转，用完后暂停到下一计费周期。
- **Starter**：$29/月，年付 $232/年（折 $19/月）——1,400 credits/月，1 个自定义演员 + 10 造型，1 条克隆声音 / 10 声音分钟，视频最长 3 分钟。（1,400 credits ≈ "约 127 秒 premium 模型输出，或约 3 分钟口播视频"）
- **Pro**（标"最受欢迎"）：$99/月，年付 $792/年（折 $66/月）——5,600 credits/月，3 个自定义演员 + 100 造型，3 条克隆声音 / 100 声音分钟，视频最长 3 分钟；宣传约 30+ 广告变体/月。
- **Premium**：$199/月，年付 $1,592/年（折 $132/月）——12,000 credits/月，10 个自定义演员 + 200 造型，10 条克隆声音 / 600 声音分钟，视频最长 12 分钟。
- **每档均含**：完整商业授权（含代理客户工作）、300+ 现成 AI 演员、70+ 语言配音/克隆、AI 剪辑、三规格输出、无水印、项目/片段数量不限。
- **自定义量级**：超过 Premium 的量可通过 support@videoai.me 定制。
- **限时促销**：Product Hunt 发布优惠码 **SOCIAL50** = 首月 5 折（"today only"）。
- **对比锚点**：官网用"一个外包 UGC 视频 $150-200+"来锚定价格感知。

## 关联信息 / 生态

- **API**：提供 AI Video API、Lip Sync API（llms.txt 列出）。
- **对比站**：官网有 comparison hub，对比 **34 款** AI 视频工具（Grok Imagine、Runway、HeyGen、Kling AI、Sora 2、Veo 3、Synthesia、D-ID、Tavus、Descript、VEED.io、InVideo AI、Pika、Luma、Captions、Fliki 等）。
- **免费工具**：Hook Generator、AI Actor Prompt Generator。
- **客户 logo 墙**：Uber、Adeagle、MentorCruise、Postdrips、Simple Analytics、SiteGPT、UserMaven、Sparkbase；引用了 Promptmonitor.io、Adeagle、Arcads、Simple Analytics、Youform & OneUp、SiteGPT 创始人的话。
- **垂直行业页**：SaaS & Tech、E-commerce、Coaches & Creators、Marketing Agencies、Real Estate、Finance & Insurance、Food & Restaurant 等 13 类。
- **PH 相似产品列表**：VEED、Synthesia、HeyGen、DeepBrain AI、RunwayML。
- **PH 关注数**：365 followers。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-04-27 | VIDEO AI ME 首次 PH 发布，当日榜单第 5 名，216 points、19 条评论 |
| 2026-08-04 | 第二次 PH 发布（主题 Social Scheduler），当日第 9 名、125 points、5 条评论 |

## 评论区反馈（事实摘录，不评价）

- **Anastasiia（@alieksia）**：祝贺发布；自己最关心分发，"用官方 API 是诚实的做法，也正因如此存在限制"。提问：(1) 15 个平台里哪些需要 business account 或 partner approval？(2) 用户如何得知 token 过期？
- **Paul G（maker）回复**：需要 partner 审批的（TikTok posting、Instagram publishing、YouTube upload）由公司处理；需要 business/pro 账号的——Instagram、Facebook（发到 Page 而非 profile）、Pinterest、Google Business、Snapchat、WhatsApp；普通账号即可——X、Reddit、Bluesky、Threads、YouTube、TikTok；Telegram/Discord 只需加 bot；LinkedIn 个人或公司页均可。token 过期时：帖子在队列页显示 Failed/Partial + 原因，账号被标 "Reconnect needed"，一键重试且只重发失败平台。
- **Natalia Iankovych（@natalia_iankovych）**：提问 "Can I clone my appearance and my voice?"（能否克隆我的外貌和声音？）——未见到 maker 回复（PH 页无可见回复）。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/video-ai-me（产品名/描述、maker Paul G 开场评论、Anastasiia & Natalia 评论及 maker 回复、logo URL、follower 数、此前发布信息、相似产品列表）
- 官网首页：https://videoai.me（tagline、功能清单、AI 演员/声音/语言、模型列表、成本对比、客户 logo、SOCIAL50 促销）
- 官网 About：https://videoai.me/about（公司结构 founder-led and independent、目标用户、联系邮箱、功能概述）
- 官网 Pricing：https://videoai.me/pricing（三档定价、credits/演员/声音配额、FAQ、促销）
- 机器可读上下文：https://videoai.me/llms.txt（产品定位、API 列表、34 款工具对比、行业垂直、免费工具）
- 公开报道：WebSearch（"VIDEO AI ME video creation tool"、"videoai.me AI video generator"、创始人背景、中文介绍）多次未返回有效结果，未找到独立报道
- GitHub：org `videoaime` 返回 404；maker PH 昵称对应的 GitHub（grsl-fr）404——无公开仓库

## 未查到 / 待补

- **公司注册主体 / 注册地 / 成立日期**：官网未披露，未查到
- **创始人全名及背景**：PH 仅显示 "Paul G"（@grsl_fr），未查到其 LinkedIn/其他社交身份
- **融资金额 / 轮次 / 投资方 / 加速器**：未查到
- **团队规模**：仅"founder-led + small team"，人数未披露
- **运营数据**：用户数、月视频生成量等未披露
- **credit 的精确换算规则**：官网只给了 1,400 credits ≈ 127 秒 premium 输出 / 3 分钟口播的大致换算
- **Natalia 提问"能否克隆我的外貌和声音"**：PH 页无 maker 回复（产品能力上官网确认支持 custom actor + voice cloning，但该提问无直接回复）
- **独立公开报道 / 媒体测评**：公开搜索未找到，未查到
- **GitHub**：无公开仓库（org 与创始人 GitHub 均 404）
