---
product: "myAIcademy"
slug: "myaicademy"
date: "2026-09-04"
rank: 2
votes: 281
comments: 36

category: "SaaS"
subcategory: "企业 AI 素养培训平台"
tags: ["EdTech", "个性化学习路径", "AI 工具模拟器", "Freemium", "iOS / Android / Web"]

tech_stack: ["Lovable SPA（官网）", "Google Cloud Platform", "Claude Code（开发工具）", "Wispr Flow（开发工具）"]
platform: ["Web", "iOS", "Android"]
open_source: false
license: ""

business_model: "Freemium（免费试用 + Pro 订阅 + 企业定制）"
pricing_start: "免费试用；Pro $12.99/月"
funding_stage: "未披露"
funding_amount: ""

related_products: ["Coursera", "Udemy", "LinkedIn Learning", "DataCamp"]
maker_previous: []

key_signals:
  - "官方称重大 AI 工具变更后 72 小时内刷新受影响课程——把课程当软件维护，对策'内容债'（content debt）"
  - "练习在内置安全模拟器进行：自建有状态（stateful）仿真、逐步 rubric 打分，不调真实第三方 API，学员不拿公司真实账号试错"
  - "按角色定制：官方称覆盖 24 类职业 persona（律师、医生、前向部署工程师、营销、创意、教师等）"
  - "创始人 Malika Malik 为 Ex-Google 生成式 AI Blackbelt；定价 Pro $12.99/月；开发用 Claude Code、官网用 Lovable 搭建"

archived_at: "2026-09-05T12:00+08:00"
sources_count: 7
---

# myAIcademy · 扩展阅读上下文

> PT 2026-09-04 Product Hunt 榜单第 2 · 👍 281 · 💬 36  
> 归档日期 2026-09-05 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | myAIcademy |
| 英文 tagline | Learn AI skills for your specific role and team |
| 中文 tagline | 为你的具体角色和团队学习 AI 技能 |
| 官网 | https://www.myaicademy.com/（PH 重定向指向此域名；根域 myaicademy.com 与 www 子域内容不一致，见"未查到"） |
| PH 页 | https://www.producthunt.com/products/myaicademy |
| 品类标签 | Android · Productivity · Education（带 Free Options 徽章） |
| 票数 / 评论 | 281 / 36（PH API 快照） |
| 公司主体 | myAIcademy（伦敦 + 迪拜，2025 年创立；被孵化器/风投 F4 Fund 收录为 EdTech 初创，团队 1-10 人） |
| 企业版/关联站点 | 有 Enterprise 档（定价页）；另有 myaicademy.com/schools（K-12 方向，部分功能标 Coming soon）；App Store / Google Play 有原生应用（包名 com.myaicademy.ui，名 "myAIcademy: AI Fluency for All"，主打"每天 15 分钟"） |

## 是做什么的（如实复述，不评价）

myAIcademy 是一个**按角色定制的 AI 技能学习平台**（官网自称 "The enterprise AI fluency platform"）：

- 用户在 onboarding 里填**角色、经验水平、目标和所用 AI 工具**，系统生成个性化学习路径（beginner → advanced 有序排列）
- 课程形态：约 15 分钟的跟做式（follow-along）课程，围绕一个真实工作流展开而非理论视频；学完不直接算通过，要在**检查点（checkpoint）模拟器**里独立复现该工作流，系统按逐步评分标准给反馈
- 内容维护：官方称系统持续监控模型/功能/界面的变更，定位受影响课程并在 **72 小时内**复核刷新（创始人称"AI 学习内容要像软件一样维护"，对应的问题是"content debt"——课程快速过时）
- 配套：每月大师课（masterclass，周末直播）、Signals（AI 更新速报）、可分享的 Skill Passport、iOS/Android/Web 账号同步
- 路线图：**Aimy**——"AI 学习智能体"，在获批准的 AI 工具内引导用户完成真实任务，把任务翻译成 prompt/步骤/操作，并套用组织的安全/隐私/合规策略（PH 发布时标注 coming soon）

## 解决什么问题（事实层面，不判断值不值得解）

- 创始人描述的链条：公司买了 AI 席位、要求员工"用起来"，然后只提供通用课程/prompt 库，员工退回试错——"差距不在获取（access），在落地（adoption）"
- 通用 AI 课程过时快：Khaleej Times 报道援引的行业数据称 60% 以上 AI 内容 6 个月内过时（公司援引，非独立核实）
- 通用课程与岗位脱节：课程按"生成式 AI 入门"组织，而非"律师/医生/工程师如何在自己的工作流里用"
- 学习完成率低：同一报道援引行业数据称学习者辍学率约 80%（公司援引）

## 怎么做的（技术原理/机制，事实层面）

- 个性化：onboarding 采集角色/水平/目标/工具 → 生成结构化有序路径；目前一次只设一个主角色，多角色档案在路线图上（可"叠两个角色"，也可在设置里切换角色后重做 onboarding，已完成课程保留）
- 内容保鲜（工程负责人 Ruchit Sharma 评论区说明）：课程是"结构化、版本化的工作流"；监控管线追踪模型发布、功能变化、弃用与 UI 更新，映射到受影响课程，触发重生成 + 人工复核，形成 72 小时更新循环
- 模拟器：自建的**有状态（stateful）专用仿真**，不调用真实第三方 API；每个学员操作被捕获并与"预期工作流 + 逐步评分标准（rubric）"比对——官方称这样结果一致、安全、不暴露组织数据，也不要求学员有付费工具账号
- 角色覆盖：PH 评论区（团队 Ashfaq Imran 回复）称目前覆盖 **24 类职业 persona**，持续新增
- 工具链（PH 页公开信息）：官网为基于 Lovable 构建的 SPA（页面元数据 og:image 指向 *.lovable.app）；PH "Built With" 栏列出 Google Cloud Platform、Claude Code、Wispr Flow

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Malika Malik（CEO & Founder）：Ex-Google 生成式 AI Blackbelt（为大型企业做 AI 落地），此前在微软云业务，Georgetown University 兼职教员，"Most Influential Women in Tech UK 2021"；称已与 10,000+ 专业人士和领导团队合作过；现还在 Dubai AI Academy（Dubai AI Campus 旗下）开 AI 大师课系列 | PH 创始人评论 / LinkedIn / WebSearch |
| 团队 | PH 评论区亮相：Ashfaq Imran（设计）、Rahul Naik（founding engineer）、Ruchit Sharma（工程），加创始人共 4 人；Khaleej Times 称创始团队含来自 IIT 和 Google 的工程师 | PH 评论区 / Khaleej Times |
| 发布团队 | PH Launch Team 名单含 Ben Lang（知名 PH 发布协作者）、Ruchit Sharma、Malika Malik | PH 页 |
| 顾问 | Lucy Chow（World Business Angels Investment Forum 的 GP）、Roberto Ordonez（Georgetown 教授、FIKRA Ventures 董事会成员） | Khaleej Times |
| 融资 | 未披露轮次与金额；被 F4 Fund 收录在其初创列表（EdTech，UAE，1-10 人），是否获其投资未确认 | F4 Fund / WebSearch |
| 总部 | 伦敦 + 迪拜 | LinkedIn / WebSearch |

## 定价 / 商业模式

- 官网定价页：**Free（起步）/ Pro $12.99/月 / Enterprise（团队定制）** 三档
- PH 上线带 "Free Options" 徽章；创始人评论称"免费试用，无需信用卡"
- 商业模式三层（创始人评论）：个人专业人士（订阅）；团队/企业（把 AI 投资转化为采用率，官网元数据提到 admin dashboard 度量）；未来第三层——AI 厂商/软件公司把 myAIcademy 当作其产品的培训与采用层
- 2025-12 报道时曾提供"lifetime access"优惠（当时形态），现主推订阅

## 关联信息 / 生态

- 同类（企业 AI 培训/课程平台）：Coursera、Udemy、LinkedIn Learning、DataCamp（通用课程模式）；myAIcademy 的差异主张是"按角色 + 模拟器实操 + 持续刷新"
- 公司另有 K-12 方向页面 myaicademy.com/schools（"Bring AI literacy to your school"）
- 官方使命口径：Khaleej Times 标题为"让数百万人在 2030 年前具备 AI 素养（make millions AI-literate by 2030）"；其 LinkedIn 帖子写作"100 million people AI-fluent by 2030"——两处均为官方自述，口径不一

## 技术时间线

| 日期 | 事件 |
|---|---|
| 2025 | 公司创立（伦敦/迪拜） |
| 2025-12-14 | Khaleej Times 报道平台发布（当时 Aimy 定位为"语音 AI 导师"；含 XP/徽章/连胜/排行榜等游戏化机制；提供终身访问优惠） |
| 2026-09-04 | PH 上线，当日 rank #2（👍 281 / 💬 36，PH API 快照） |

## 评论区反馈（事实摘录，不评价）

共 36 条评论（PH API 快照）；本次摘录第 1、3 页共 12 条问答要点（第 2 页未完整读取）：

- Kshitij Mishra："72 小时刷新，规模上很难做到" / 创始人：系统持续监控模型、功能、界面变更 → 定位受影响课程 → 72 小时内刷新
- Priya K：喜欢"完成真实任务而非一小时理论视频" / 创始人：每课短、实操、围绕真实职业任务，prompt 可复制/改编/应用；检查点带反馈；周末直播大师课
- Adana Marukhyan：覆盖所有行业吗？ / Ashfaq Imran（团队）：目前 24 类职业 persona（律师、医生、前向部署工程师、营销、创意、教师），持续新增
- Maria Telegina：混合职业（如教师+创始人）怎么处理？ / 创始人：onboarding 目前设一个主角色，多角色档案在路线图，可叠两个角色，设置里可切换
- Daniel Carter：上完课之后呢？ / 创始人：结课不算证明学会——要在模拟器检查点独立复现工作流并拿反馈，再应用到真实工作
- Andy Da Costa：路径是结构化还是碎片？ / 创始人：基于角色与水平的结构化路径，beginner → advanced 顺序
- Dylan Friddle：中途换角色？ / 创始人：重做 onboarding 生成新路径，已完成课程保留；Discover 区可浏览全部课程
- James Wilson：团队可否按不同角色（营销/销售/产品）建不同路径？（未见官方回复摘录）
- Manuel Lorenzo Bouzada：与直接问 ChatGPT 学有何区别？ / 创始人：ChatGPT 基于训练时知识，给的步骤可能已不存在（UI 已变）；本产品课程用当前真实截图、对产品逐条核验，并告诉你该职业该用哪些工具、持续更新
- Tehreem Fatima：模拟器接真实 API 还是 mock？刷新如何规模化？ / Ruchit Sharma（工程）：自建有状态仿真、非真实第三方 API，逐步 rubric 评估；监控管线自动映射变更 → 重生成 + 复核，支撑 72 小时循环
- Filxa Adam：对模拟器感兴趣 / 创始人：检查点是练习"角色专属真实任务"的安全场所
- Gal Dayan（Likely AI 创始人）：Aimy 从"模拟器里引导"到"真实工具里执行"是另一类风险，是每个 agent 产品都要回答的权限问题；问是按 persona 限定权限还是开放设计问题（未见官方回复）

## 信息来源

- PH 产品页：https://www.producthunt.com/products/myaicademy（tagline、描述、创始人发布评论、评论第 1/3 页、Built With、Launch Team、Followers 767、1 条 5.0 评价）
- 官网（PH 重定向）：https://www.myaicademy.com/（元数据：enterprise AI fluency platform、"refreshed every 72 hours"、admin dashboard）
- 官网定价页：https://www.myaicademy.com/pricing（Free / Pro $12.99/月 / Enterprise）
- Khaleej Times 报道（2025-12-14）：平台发布、顾问名单、Aimy 当时定位、游戏化机制、行业数据
- F4 Fund：https://f4.fund/startups/myaicademy（EdTech、UAE、1-10 人）
- WebSearch 摘要：创始人 LinkedIn 背景、Google Play 应用信息、myaicademy.com/schools、LinkedIn 使命口径
- GitHub：无开源信号，未查 GitHub（PH "Built With" 列的是第三方工具，非自家仓库）

## 未查到 / 待补

- 融资：是否已完成股权融资、金额与投资方（与 F4 Fund 的关系未确认）
- 用户数 / 收入 / 企业客户名单
- Pro 与 Enterprise 的具体功能分界（官网定价页为 SPA，正文细节未抓全，仅拿到档位与 Pro 价格）
- 24 类 persona 的完整清单、课程总量
- Aimy 上线时间表
- 根域 myaicademy.com（不带 www）在 2026-09-05 抓取时返回 "myAIcademy | AI Learning for Kids"（儿童 AI 夏令营内容），与 www 子域的企业平台不一致；与 /schools 页面的关系未查到
- PH 评论第 2 页未完整读取（约 1/3 评论未摘录）
