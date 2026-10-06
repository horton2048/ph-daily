# Wispr Flow Notetaker · 扩展阅读上下文

> PT 2026-08-05 Product Hunt 榜单第 2 名 · 👍 539 · 💬 72
> 归档日期 2026-08-06 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Wispr Flow Notetaker（简称 Wispr Notetaker；公司 Wispr Inc.，主产品 Wispr Flow 口述听写） |
| 英文 tagline | Meeting notes that get the details right. |
| 中文 tagline | 把细节做对的会议纪要：名字、说话人、术语都对，笔记能直接行动 |
| 官网 | https://wisprflow.ai（Notetaker 页 https://wisprflow.ai/notetaker） |
| PH 页 | https://www.producthunt.com/products/wisprflow（本次 launch post slug `wispr-flow-notetaker`） |
| 品类标签 | Notes · Meetings · AI（PH 产品页另标 AI Dictation Apps） |
| 票数 / 评论 | 539 / 72（PH V2 API 2026-08-06 抓取；日榜截稿 537） |
| 公司主体 | Wispr Inc.（官网 © Wispr Flow 2026；产品线 Flow + Notetaker） |
| logo | https://ph-files.imgix.net/aa083f4b-ca21-4b5c-97a2-602ac3c0b253.png（Wispr Flow 产品 logo）；Notetaker 封面图 https://ph-files.imgix.net/4754f10b-0e91-4d5f-9d45-877ef6a06ca2.gif |
| PH 关注 / 评分 | 8.5K followers；4.7（73 reviews）；"The People's Champ Award for AI Dictation Apps（Winter 2025）"；本次是 Wispr Flow 第 5 次 PH launch |
| Launch 团队 | 60+ 人（含 CEO/创始人 Tanay Kothari @tanaykothari、Growth 负责人 Matt Swulinski @mswulinski 等） |

## 是做什么的（如实复述，不评价）

Wispr Flow Notetaker 是把 Wispr Flow 的语音引擎（口述听写，"把词说对"）从"对自己电脑说话"扩展到"对别人说话"（会议场景）的 Mac 会议纪要应用。核心卖点不是"生成摘要"，而是**先把转写/说话人做对**，再在其上构建摘要、跟进、MCP 对接。

官方描述原文："Your follow-ups are only as good as your meeting notes. Wispr Notetaker gets your words and your speakers right, so your recaps, follow-ups, and answers are too. Before the meeting starts, it checks the invite so names are spelled correctly, and it brings the terminology you've already taught Wispr Flow into every conversation. Your transcripts use real names instead of 'Speaker 1' and 'Speaker 2,' and every meeting is ready to pull into Claude or ChatGPT via MCP. Available on Mac. Free to try."

运行形态：Mac 应用，一个按钮加入并录制会议；自动接上日历上的背靠背会议和不在日历上的临时通话。输出物包括：带真人名的转写、会前 Brief、会中一键补课（What did I miss?）、标注决策与下一步的摘要。所有会议可通过 MCP 拉到 Claude / ChatGPT / Cursor 等工具里。目前 Mac only、英文 only，免费可试。

## 解决什么问题（事实层面，不判断值不值得解）

- **转写错一个名字/缩写就全局传染**：官方判断"几乎没人读原始转写，但一切都构建在它之上——单个名字或缩写错了会到处传播；说话人标错，下游一切不可信"，所以从"capture（采集）"这个最基础环节做起（Tanay 开场评论）。
- **摘要质量上限 = 采集质量**：用户评论指出"如果采集错了，所有基于它的 AI 洞察也是错的"；"summary 决定丢掉什么"才是 notetaker 最难的部分。
- **参会三难（听 + 记 + 追踪谁说啥）**：内部员工评论称在密集多干系人会议里"active listening、track who said what、记详细笔记"三者不可兼得，Notetaker 的说话人分离让人能 100% 在场。
- **follow-up / 行动项归属**：官方描述与 Growth 负责人评论都指向"recaps、follow-ups、answers"质量取决于纪要；说话人/任务归属漂移会让 to-do 错乱（"别人拿到了我的待办，我拿到了别人的"）。
- **会议数据要进 AI 工具**：不想复制粘贴，希望直接把会议变成 Claude/ChatGPT 可推理的上下文（MCP 定位）。
- **竞品迁移成本**：官方 FAQ 明确支持从 Granola / Otter / Fathom 一键迁移全部历史。

## 怎么做的（技术原理/机制，事实层面）

来源：PH 描述 + Tanay 开场评论 + 官网 Notetaker/FAQ 页

- **会前上下文注入**：开会前读日历邀请，人名拼写预先放对；Flow 里用户已教的词汇/词典（名字、公司术语、缩写）自动带进会议。
- **双音轨分离采集**：麦克风音轨与"电脑播放的所有声音"分开采集，"你的话永远不会跟别人的混在一起"。
- **真人名说话人分离**：最终转写用真人名而非 Speaker 1/2；识别错了可一键修正并**全篇生效**（同一修正应用到整份转写）。
- **二次校对**：官方 FAQ——"每个转写都会再过一遍更强大的模型来抓错"，且因为带有用户词典上下文，人名（如 Aditya）拼写正确、产品名保持完整。
- **摘要与 Brief**：会前 Brief（带相关背景）、会中 one-click catch-up（错过的东西）、会后摘要（明确标出 decisions 和 next steps）、未在日历的通话一键录制。
- **MCP 支持**：官方称"every meeting is ready to pull into Claude or ChatGPT via MCP"；官网 Notetaker 页进一步写"plugs into Claude, ChatGPT, Cursor and any tool that speaks MCP"。
- **底层是 Flow 的自有模型/基础设施**：Wispr 官方自述"building our own models and infrastructure rather than relying solely on general-purpose LLMs"（2025-11 融资博客），保证即时响应与跨 app 一致性。
- **隐私**：Privacy Mode（零存储），SOC 2 Type II / HIPAA / ISO 27001 认证；HIPAA 在所有计划可用（需签 BAA），SOC 2 仅 Enterprise，ISO 27001 认证进行中（官网 Business 页）。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Tanay Kothari（CEO，PH @tanaykothari；官方称为"Wispr 创始人"）；约 60+ 人 launch team | PH makers；wisprflow.ai/about |
| 公司定位 | "The Voice Interface Company"，打造 voice-native computing system；自述从硬件（神经接口穿戴设备）转型而来 | 官网 about；StartupHub 公司简介 |
| 融资 | 累计 **$81M**：$30M Series A（2025-06，Menlo Ventures 领投）+ $25M Series A 延期（2025-11-20，Notable Capital 领投）；TechCrunch 报道 post-money 估值 **$700M** | TechCrunch 2025-11-20；PR Newswire；wisprflow.ai/new-funding |
| 投资方 | Menlo Ventures、Notable Capital、NEA、8VC、Flight Fund（Steven Bartlett）及多位天使（Evan Sharp、Henry Ward、Flo Crivelli、Kenneth Schlenker 等） | TechCrunch；techcapsules；StartupHub |
| 关键背书人 | Hans Tung（Notable Capital，加入董事会/观察员）；Reid Hoffman、Arash Ferdowsi、Dave Gilboa、Kevin Weil、Will Ahmed、Jeff Seibert、Fred Ehrsam、Rahul Vohra（官网"Backed by the best"） | wisprflow.ai/about；wisprflow.ai/new-funding |
| 增长数据（官方/媒体口径） | 2025-11 时：40% MoM 增长、270 家 Fortune 500、每周新增 125 家企业客户、用户年增 100x、12 个月留存 70% | TechCrunch 2025-11-20 |
| 合规认证 | SOC 2 Type II、HIPAA（BAA）、ISO 27001（进行中） | wisprflow.ai/business |
| 加速器 | 未查到 | — |

## 定价 / 商业模式

- **Free（$0/月）**：100+ 语言听写；**Notetaker 在免费档即可用**（Mac only）——含说话人识别、跨会议提问、"用 Claude/ChatGPT 等 AI 工具处理笔记（MCP）"、日历/Slack 连接、数据隐私、可随时退出模型训练。
- **Pro（$12/user/月，年付 20% 折扣）**：无限听写、更多会议且保留更久、先进 AI thinking 模型、新模型/功能提前体验、优先工单、集中计费与用户管理。
- **Enterprise（联系销售）**：企业级安全与管理员控制、SOC 2 Type II / ISO 27001 / HIPAA-ready BAA、IT 管理员免费席位、审计日志 / MDM / 域名管理、SAML SSO / SCIM、专属支持、批量折扣、全员可退出模型训练。官网标注"Notetaker coming soon to Enterprise"。
- **Business 页（团队档能力）**：共享自定义词典、共享 snippets、团队级 admin 使用仪表盘、跨会议/Slack/邮件"ask anything"（带来源引用）；案例数字（官方口径）：Clay 案例"Flow 加速 20% GTM 执行"，客户回复快 52%，年省估算 $3.08M。
- **模式要点**：Freemium + 团队订阅；Notetaker 作为 Flow 生态新增能力随订阅档提供，而非单独计价；官网 ROI 计算器示例（$12/月换约 22 小时/月，年省估算 $13,056）。

## 关联信息 / 生态

- **Wispr Flow 产品线**：Dictation（Mac/Windows/iOS/Android）+ Notetaker（Mac only，更多平台"coming soon"）；官方 Notetaker 页说"Fits into your workflow. Doesn't change it."。
- **生态对接**：MCP（Claude、ChatGPT、Cursor 及任何说 MCP 的工具）；日历与 Slack 连接；Gmail/Slack 上下文（FAQ 提到"information from connected tools like Gmail and Slack"）。
- **迁移钩子**：官网直接宣传"Coming from Granola? 历史一键搬"；FAQ 也覆盖 Otter、Fathom。
- **竞品位置**：同类会议 notetaker 包括 Granola、Otter、Fathom（官方 FAQ 直接点名）；差异化宣称是"capture（采集）正确性 + Flow 既有词典迁移 + MCP"。
- **认证与信任**：Privacy Mode 零服务器存储；SOC 2 Type II / HIPAA / ISO 27001。
- **已知版本边界**：Mac only、English only 首发；多语言/多平台"roll out later"（Tanay 开场评论）。

## 技术时间线（官网/公开里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2025-06 | Wispr 完成 $30M Series A（Menlo Ventures 领投），主产品 Flow 快速成长 |
| 2025-11-20 | $25M Series A 延期（Notable Capital 领投 + Flight Fund），累计 $81M、估值 $700M；官方宣布"build the voice OS" |
| 2026-02-28 | 官方/媒体：Flow Android 版本上线（"Wispr Flow is the dictation upgrade Android users deserve"） |
| 2026-04 前后 | 进入 Notable Capital"Prosumer AI 40"、AI 50 Brink List 等榜单 |
| 2026-07-24 | 媒体报道：Wispr 宣布推出 Lab 做"J.A.R.V.I.S."（官网新闻条目） |
| 2026-08-01 前后 | Notetaker 内部测试约一个月（团队评论："Having tested Notetaker internally for the last month"） |
| 2026-08-05 | Notetaker 上线 Product Hunt（post created 2026-08-05T07:01:00Z），日榜 #2（539 👍 / 72 💬） |

## 评论区反馈（事实摘录，不评价）

- **Tanay（CEO，开场）**：Notetaker 解决"Flow 管你对电脑说的话，Notetaker 管你对别人说的话"；bet 是"几乎没人读原始转写，但一切都构建在它之上"，所以先从改进 capture 入手（名字拼对、Flow 术语带入、双音轨分离、真人名 + 一键全篇修正）；另有 Brief、一键补课、摘要（决策+下一步）、临时通话一键录制、MCP；Mac + 英文首发，希望用户用一天后反馈。
- **Lenny Rachitsky（Lenny's Podcast）**：评价"Genius move"。
- **Fabian Dittrich（用户）**：圆桌线下会议、WhatsApp 电话、Zoom/Teams 都能用，因为 Notetaker 绑定的是电脑进出的音频而非特定软件。
- **Matt Swulinski（Growth 负责人，maker）**：过去依赖会议纪要派 action items，说话人/任务归属漂移导致 to-do 错乱（"别人拿到我的待办，我拿到别人的"）；Notetaker 让转写和名字归属可信，配合 MCP 全系统同步。
- **Granola 用户提问**：长期 Granola 用户问对比与迁移的 killer features。
- **API/集成提问**：用户问能否把会议导进其他服务（如 Zentrik）有无 API → maker 回复 **"MCP is built in!"**。
- **技术观察（用户评论）**：notetaker 的价值不在转写质量而在"它决定丢弃什么"——"把一切保住的摘要就是多此一举的转写"；standup 和首次客户 call 想要的默认值相反，问取舍是否可按会议类型调（API 未抓到 maker 对该条的回复）。
- **员工/团队成员评论**：内部测试一个月后"自豪发布"；社交负责人（入职一周）称 Notetaker"没漏掉任何东西"。
- **普通用户**：用于语音备忘、回顾 takeaway 与下一步；"accuracy and speaker diarization 是最爱功能"（密集多方会议中能保持 100% 在场）。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/wisprflow（Wispr Flow 聚合页：第 5 次 launch、8.5K followers、4.7/73 reviews、People's Champ Award、logo、Built with）
- PH launch post：https://www.producthunt.com/posts/wispr-flow-notetaker（产品描述、launch 信息；跳转到产品页 ?launch= 视图）
- PH V2 API：post slug `wispr-flow-notetaker`（id 1214897，votesCount/commentsCount/createdAt/description/makers 60+ 人精确值；comments + replies 抓取）
- 官网首页/Notetaker 页/定价页：https://wisprflow.ai 、/notetaker 、/pricing 、/business 、/about 、/new-funding（功能、FAQ、三档定价、企业能力、融资公告、背书人名单）
- 公开报道：TechCrunch（2025-11-20，"Wispr secures $25M from Notable Capital"，$700M 估值、增长数据、$30M Menlo Series A）；PR Newswire（2025-11-20）；techcapsules / StartupHub（Series A $30M 领投方与天使名单）
- GitHub：未查到 Wispr 官方公开仓库（github 搜索命中均为第三方替代/移植项目，如 whishpy、VoiceInk 等；官方闭源）
- 说明：评论区用户名为 API 打码 [REDACTED]，maker 身份通过 makers 列表 username 对照（Tanay Kothari、Matt Swulinski、Jacob Shwirtz、Wil Morton 等均在 makers 列表中）

## 未查到 / 待补

- **Notetaker 的多语言/多平台时间表**：官方只说"英文 + Mac 首发，后续再铺"，无公开路线图日期。
- **免费档 Notetaker 的会议数量/保留期具体数字**：定价页只写"Standard/Extended retention"、"Weekly limit 更高/更高"，无具体数字。
- **转写/说话人分离的准确率**：官方仅定性宣称（"gets it right, every word exactly as it was said"），无第三方评测或精确数字。
- **创始人 Tanay Kothari 的详细履历**：官网 about 只有创始人寄语；学历/前东家未查到。
- **Wispr 硬件转型历史细节**：StartupHub 提到最初想做神经接口穿戴设备，具体经过未查到。
- **SOC 2 / HIPAA / ISO 27001 认证状态**：官网自述，未核验证书原文。
- **"40% MoM / 270 家 Fortune 500 / 每周 125 家企业客户"**：TechCrunch 口径，为官方提供数据，无独立验证。
