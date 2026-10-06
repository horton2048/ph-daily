---
product: "Compliance by TwelveLabs"
slug: "twelvelabs"
date: "2026-09-04"
rank: 3
votes: 242
comments: 18

category: "SaaS"
subcategory: "视频合规审查 SaaS"
tags: ["视频理解", "合规审查", "规则包", "合成内容检测", "REST API", "企业 SaaS"]

tech_stack: ["Pegasus 1.5（视频语言模型）", "Marengo（多模态嵌入/检索）", "NVIDIA Synthetic Video Detector", "REST API", "Framer（官网）"]
platform: ["Web", "API"]
open_source: false
license: ""

business_model: "企业定制 SaaS（Compliance 应用未公开报价）+ 底层模型 API 按量计费"
pricing_start: "Compliance 应用未公开（Talk to Sales）；底层 API 有免费档（累计 600 分钟索引额度）"
funding_stage: "B 轮（2026-07）"
funding_amount: "B 轮 $100M；累计约 $160M+"

related_products: ["Sieve", "VeedoAI", "ezML", "Reka Vision"]
maker_previous: ["Jockey by TwelveLabs", "Rodeo by TwelveLabs", "Pegasus 1.5", "Marengo 3.0"]

key_signals:
  - "TwelveLabs 从模型 API 走向垂直 SaaS 应用：这是其 PH 第 6 次发布（近 10 个月第 5 次），此前有 Jockey（视频 agent）、Rodeo（剪辑初稿）"
  - "'rules you control' 机制：规则书存在客户租户而非供应商代码库，可 fork 地区包、调阈值、发版本；现有 40+ 规则包（US MPA、UK Ofcom、法 CNC、沙特 Gmedia、巴西 ClassInd、澳 ACB）"
  - "内置 NVIDIA Synthetic Video Detector 做帧级合成内容评分；官方称 53 资产验证集上与人工基线一致率 92.5%、人工复审时间降 80%、12 条规则包审 2 小时母带 12 分钟"
  - "融资：2026-07 B 轮 $100M（NEA + NAVER Ventures 联合领投，Amazon/Radical/Index/Quadrille/Red Bull 参投）；2024-06 A 轮 $50M 由 Nvidia + NEA 联投"

archived_at: "2026-09-05T12:00+08:00"
sources_count: 7
---

# Compliance by TwelveLabs · 扩展阅读上下文

> PT 2026-09-04 Product Hunt 榜单第 3 · 👍 242 · 💬 18  
> 归档日期 2026-09-05 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Compliance by TwelveLabs（公司：TwelveLabs, Inc.） |
| 英文 tagline | Video compliance review powered by rules you control |
| 中文 tagline | 用你自己掌控的规则做视频合规审查 |
| 官网 | https://www.twelvelabs.io/compliance |
| PH 页 | https://www.producthunt.com/products/twelvelabs |
| 品类标签 | SaaS · Artificial Intelligence · Video |
| 票数 / 评论 | 242 / 18（PH API 快照） |
| 公司主体 | TwelveLabs, Inc.，旧金山，2021 年创立；PH 产品档案显示 1.5K followers、累计 6 次发布、1 条 5.0 评价 |
| 企业版/关联站点 | 本身即企业 SaaS；同公司还有 Marengo/Pegasus 模型 API 与 Jockey、Rodeo 等应用 |

## 是做什么的（如实复述，不评价）

Compliance by TwelveLabs 是一个视频合规审查 SaaS 应用：把客户的视频库接入后，按**客户自己编写、管理的合规规则包**逐条审查，输出"审核员可直接处理"的发现（findings）——不只是时间戳 + 标签，而是带上下文的解释（由 Pegasus 1.5 说明某个时刻为什么可能违反某条规则）。审核员在一个排序队列里对每条发现做接受/拒绝/标注，最后可导出签名的 JSON/PDF/CSV 报告。官方表述：目标是把"数小时的人工审片"变成"跑一遍规则包 + 人工只处理有争议的标记"。

## 解决什么问题（事实层面，不判断值不值得解）

- 合规审查仍以人工为主：官方称其内部评估中人工复审时间可降 80%（自述数字）
- 只有"违规标签"不够：maker 发布评论的原话——"如果审核员还得重看整条视频来验证 AI 的标记，那我们到底给他们省了什么？"（需要带语境的解释，而不是裸标签）
- 各市场规则不同：同一条素材在不同国家、不同播出方、不同时段/受众下结论不同（同一支广告在儿童时段与深夜标准不同；同一国家两家播出方标准也可不同）
- AI 生成内容涌入：需要检测合成媒体——集成 NVIDIA Synthetic Video Detector 做帧级评分

## 怎么做的（技术原理/机制，事实层面）

- 底层模型：公司自研两条线——Marengo（把画面、音频、语音、屏幕文字映射成统一可检索表征，负责"感知"）+ Pegasus 1.5（视频语言模型，生成有依据的解释/回答/摘要，负责"推理"）；公司主张"感知-记忆-推理"闭环架构（官方称 Video Cognition System）
- 审查流程：ingest 视频 → 套用规则包 → 产出按严重度排序、带时间戳证据的队列 → 审核员 accept / reject / annotate → 导出签名报告
- "rules you control" 机制：规则书存在**客户自己的租户**里，不在供应商代码库；合规团队可 fork 地区规则包、编辑、调检测阈值、发布版本，"不用提工单、不等供应商路线图"；现有 **40+ 地区/场景规则包**（US MPA、UK Ofcom、French CNC、Saudi Gmedia、Brazilian ClassInd、Australian ACB），另支持片厂内部政策
- 语境组合：把视频内理解（画面/对白/文字/语境）与客户提供的审查信息（投放地、播出方、受众、时段）结合；信息缺失或存在多种解读时，标记并说明缺什么、留给人工，而非强给 pass/fail（maker 评论区回复）
- 合成内容检测：NVIDIA Synthetic Video Detector 提供帧级评分，与语境分析并列输出
- 目标指标：maker 称目标是"审核员拒绝率 ≤15%"（减少审核员被误报浪费的时间）
- 部署与安全（官网 FAQ）：fully managed 多租户 SaaS，明确**不支持**部署到客户自己的 AWS 账号（BYO-AWS 不可）；RBAC 细粒度权限 + super-admin 角色；静态/传输加密 + WAF；CDN 签名 URL 交付媒体；可加购网络隔离；所有 Web 能力都有对应 REST API
- 官方内测数字（自述，官网注明"内部评估，结果随内容/规则包/阈值而变"）：53 个资产的验证集上与人工基线**一致率 92.5%**；人工复审时间**降 80%**；12 条规则包审 2 小时母带**12 分钟**

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Jae Lee（CEO & Co-founder）与 Dave Chung（COO），2021 年创立于旧金山 | 官方 Series B 博文 / KED Global |
| 本次发布团队 | Maker：Simon Lecointe（Head of Field Engineering）；Hunter：fmerian（Kilo Code）；Launch Team 另有 Lior Berezinski | PH 页 |
| A 轮 | $50M（2024-06），Nvidia 与 NEA 联合领投；A 轮后累计约 $62M（意味着此前种子轮合计约 $12M） | KED Global |
| B 轮 | $100M（2026-07-01 官宣，博文署名 Jae Lee），NEA 与 NAVER Ventures 联合领投，Amazon 参投，另有 Radical Ventures、Korea Investment Partners、Index Ventures、Quadrille Capital、Red Bull Ventures；另有报道称同批宣布与 AWS 的 Trainium 芯片训练合作（SiliconANGLE/NEA 报道） | 官方博文 / Bloomberg / GlobeNewswire / WebSearch |
| 累计融资 | 约 $160M+（种子合计约 $12M + A 轮 $50M + B 轮 $100M，按公开披露推算） | KED Global + 官方博文推算 |
| 合规认证 | 官网 Compliance 页脚显示 TPN（Trusted Partner Network，MPA 旗下内容安全认证网络）徽章图；具体认证状态未核实 | 官网页脚 |

## 定价 / 商业模式

- Compliance 应用本身：**未公开定价**，官网入口为 "Talk to Sales"；FAQ 明确当前只提供 fully managed SaaS，不支持自部署
- 底层模型 API 定价（官网 pricing 页，供参照 Compliance 的底层成本结构）：
  - Free 档：累计 600 分钟索引额度、无需信用卡、5 个并发索引任务、索引数据保留 90 天
  - Developer 档（按量）：Search API 视频索引 $2.50/小时（一次性）、embedding 基础设施 $0.09/小时、检索 $4/千次查询；Analyze API 输入 $1.75/小时 + 输出文本 $7.5/百万 token；Embed（Marengo）视频 $0.260/百万 token；Pegasus 视频索引 $0.042/分钟（一次性）；25 并发任务
  - Enterprise 档：定制、不限索引小时数；支持按业务需求微调（需联系）
- 商业结构（观察事实）：模型 API 按量收费 + 上层应用按企业合同收费；Compliance 是公司"应用层"产品线之一

## 关联信息 / 生态

- PH 相似产品：Sieve（视频 AI 基础设施）、VeedoAI、ezML（计算机视觉）、Reka Vision
- 同公司 PH 历次发布：Marengo 3.0（2025-12-01，当日 #3）、Pegasus 1.5（2026-04-20，当日 #5）、Rodeo（2026-06-02，描述镜头生成初剪）、Jockey（2026-07-21，"理解你整个视频库的视频 AI agent"）——本次 Compliance 为第 6 次发布
- 官网 Solutions 栏目标行业：Media & Entertainment、Advertising、Government、Security、Sports & Broadcasting
- 客户侧证言：Tellers.AI（Bjay Kamwa）在 PH 评论区称其复杂剪辑的深度视频分析由 TwelveLabs 驱动

## 技术时间线（公开里程碑）

| 日期 | 事件 |
|---|---|
| 2021 | 公司创立（旧金山） |
| 2024-06 | A 轮 $50M（Nvidia + NEA 联投） |
| 2025-12-01 | Marengo 3.0 发布（PH 当日 #3） |
| 2026-04-20 | Pegasus 1.5 发布（PH 当日 #5） |
| 2026-07-01 | B 轮 $100M 官宣（NEA + NAVER Ventures 领投，Amazon 参投） |
| 2026-07-21 | Jockey 发布（视频 AI agent） |
| 2026-09-04 | Compliance 发布，PH 当日 #3（👍 242 / 💬 18，PH API 快照），公司第 6 次 PH 发布 |

## 评论区反馈（事实摘录，不评价）

共 18 条评论（PH API 快照），本次逐条读到第 1 页约 9 条：

- Evan Taft：规则依赖"画面之外"的语境时怎么处理？ / Simon Lecointe：很多规则取决于投放地、播出方、受众、时段——把视频理解与客户提供的审查信息结合；信息缺失或可解读时标记并说明缺什么，留给人工而非强判 pass/fail
- Hamza Afzal Butt：各国标准不同，适配多容易？ / Simon：规则评估框架支持添加国家特定要求，并对真实视频测试看什么被标记、为什么，再修正过严/漏检的规则——是配置与验证本地规则，不用改应用
- Priya K：findings 就绪 + API 访问让集成更顺
- Grant Wilkins：审核队列合理——"没人想为了验证一个标记重看 20 分钟"
- Ethan Blake：多市场视角对大型内容团队有用
- Vipul Kumar / Henry Habib：祝贺与泛支持
- Hunter fmerian 补充：这是 TwelveLabs 第 6 次 PH 发布、近 10 个月第 5 次

## 信息来源

- PH 产品页：https://www.producthunt.com/products/twelvelabs（描述、maker 评论、评论区、历次发布记录、Launch Team）
- 官网 Compliance 产品页：https://www.twelvelabs.io/compliance（规则包机制、FAQ、40+ 规则包、RBAC/安全/部署限制、92.5%/80%/12min 数据、目标行业）
- 官网定价页：https://www.twelvelabs.io/pricing（API 三档与单价）
- 官方 Series B 博文：https://www.twelvelabs.io/blog/twelvelabs-series-b-100m（金额、投资方名单、Marengo/Pegasus、Video Cognition System、Jae Lee 署名）
- KED Global（2024-06）：A 轮 $50M、Nvidia/NEA 联投、创始人 Jae Lee（CEO）/Dave Chung（COO）
- Bloomberg / GlobeNewswire（2026-07-01）：B 轮 $100M、Amazon 参投（经 WebSearch 摘要核实）
- GitHub：PH 公司信息列有 GitHub 链接（公司有公开 SDK 仓库）；Compliance 应用本身无开源信号，未进一步查 GitHub

## 未查到 / 待补

- Compliance 应用的定价/合同模式（按席位还是按分钟量）——官网只有 Talk to Sales
- 92.5% / 80% / 12min 数据的验证方法细节（官方仅标注"内部评估"）
- "审核员拒绝率 ≤15%" 目标的实际达成情况
- 现有企业客户名单与案例（官网 Case Studies 未抓取）
- TPN 认证的具体范围与状态（仅见页脚徽章图）
- 公司员工规模
- PH 评论区第 2 页（约一半评论）未逐条摘录
