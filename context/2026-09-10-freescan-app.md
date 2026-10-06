---
product: "FreeScan.app"
slug: "freescan-app"
date: "2026-09-10"
rank: 9
votes: 97
comments: 18

category: "开发者工具 / SEO / UX 审计"
subcategory: "AI 时代网站健康度一键扫描"
tags: ["Freemium", "订阅制", "SEO", "AEO", "GEO", "无障碍审计", "安全头检查", "页面体检", "AI 可发现性", "MCP", "LLM 检索优化", "Closed Source", "Bootstrapped（推测）"]

tech_stack: ["Next.js（从 _next/ 静态资源推断）", "确定性规则引擎（自家声明非 AI 评分）", "MCP（Model Context Protocol，Pro 版）", "真实浏览器渲染做无障碍检查", "公开 llms.txt 接口：https://www.freescan.app/llms.txt"]
platform: ["Web（任意浏览器）", "MCP 客户端（Pro 版）"]
open_source: false
license: "闭源（FreeScan.app GitHub 用户为无关旧账号，创始人 JacobCounsell 在 GitHub 无个人主页）"

business_model: "Freemium + 订阅"
pricing_start: "免费（单页 40 项检查） / Pro $19/月"
funding_stage: "未披露（独立创始人项目，从首页未发现融资或公司主体信息）"
funding_amount: "未披露"

related_products: ["Lighthouse（Google）", "WAVE（WebAIM，无障碍）", "SecurityHeaders.com", "Ahrefs / Semrush（综合 SEO 套件）", "Screaming Frog（爬虫）", "Sitebulb", "Chrome DevTools", "Axe DevTools"]
maker_previous: []

key_signals:
  - "免费档 0 摩擦——无需注册/邮箱/所有权验证/crawler 配置，贴 URL 即可拿报告；用免费扫描做获客漏斗顶端的 Hook"
  - "Pro $19/月锁的不是单一功能，而是把单点扫描升级成持续监测（最多 5 个站点 · 25 个核心页周扫 · 5 次手动扫描/周 · 30 天一次全量基线 · 周报邮件 + 站点 uptime）"
  - "明确把 AEO/GEO 写进产品——审计项覆盖 llms.txt、answer-ready content、entity clarity、citation eligibility，抓的是 AI 搜索新范式的早期需求"
  - "Pro 版提供 MCP（Model Context Protocol）接入，让 Claude/Cursor 等 agent 直接读取私有审计结果——产品形态从「报表」变成「agent 工作流的输入端」"

archived_at: "2026-09-10"
sources_count: 4
---

# FreeScan.app · 扩展阅读上下文

> PT 2026-09-10 Product Hunt 榜单第 9 · 👍 97 · 💬 18
> 归档日期 2026-09-10 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | FreeScan.app |
| 英文 tagline | Fix what's hurting your visibility, trust, and conversions |
| 首页主标语 | Run a free website audit with 40 checks for SEO / AEO / GEO, website security, accessibility, and design standards. Get prioritized fixes to improve search rankings, AI visibility, user trust, and conversions. |
| 中文 tagline | 一键发现拖垮你曝光、可信度、转化的问题 |
| 官网 | https://www.freescan.app / https://freescan.app |
| PH 页 | https://www.producthunt.com/products/freescan-app |
| 品类标签 | User Experience · SEO · Developer Tools |
| 票数 / 评论 | 97 / 18 |
| 公司主体 | 未单独披露（schema.org Organization 仅署 "FreeScan.app"，无独立公司名/Crunchbase 实体） |
| 创始人 | Jacob Counsell（X：@JacobCounsell，schema.org founder 字段） |
| 累计审计数（首页公示） | 2,180 audits |
| 关联文件 | https://www.freescan.app/llms.txt（AEO/GEO 直接对接 LLM 的信号文件） |

## 是做什么的（如实复述，不评价）

打开官网贴一个公开 URL，**无需注册**即可拿到一份 40 项检查的审计报告，覆盖 SEO、AEO、GEO、网站安全、可访问性、设计/转化五个维度；每条未通过的检查都附带证据、严重度和具体修复建议（含可直接贴给 agent 修问题的 prompt）。

付费 Pro 版（$19/月）把"单次单页扫描"扩展为**多站点持续监测**：最多 5 个监控站点，每个站点初筛最高 60 个核心公开页，每周最多 5 次手动扫描、25 个核心页自动周扫、每 30 天一次全量基线，自动周报邮件，并附 SEO Workspace、AI Visibility Workspace 和可选 uptime 监测（公开 status page、实时 widget、官网徽章）。

首页用 Claude / ChatGPT / Perplexity 三个 AI 引擎 logo 暗示产品对 AI 检索可见性的关注；schema.org 中 SoftwareApplication 列出的 featureList 长达 14 条，其中"agent workspaces & MCP"模块允许 Pro 用户把 SEO/AI Visibility/Fixes 工作区导出为 Markdown，或通过 MCP 让 agent 读取私有审计结果并触发重新扫描。

## 解决什么问题（事实层面，不判断值不值得解）

- **多工具拼装成本**：FAQ 自述"Lighthouse、WAVE、SecurityHeaders、SEO 工具各有分工但要拼起来看"，FreeScan 把五类检查合到一张 scorecard
- **扫描摩擦**：免费档明确写"无需账号、无需邮箱、无需所有权验证、无需 project 设置、无需 crawler 配置"——降低"想看一眼"的成本
- **AI 搜索新范式**：传统 SEO 工具对 llms.txt、answer-ready content、entity clarity、citation eligibility 覆盖少；FreeScan 把 AEO（Answer Engine Optimization）和 GEO（Generative Engine Optimization）独立成审计项
- **问题看不懂也修不动**：首页描述每条失败项"自带证据 + 严重度 + 修复方法"，并提供可直接贴给 Claude Code 等 agent 的 prompt
- **修复效果难以追踪**：Pro 版保留详细 scan history 和 scan-to-scan 对比，把修复效果可视化
- **可访问性门槛高**：典型 WCAG 审计需要付费买专业工具/认证服务，免费档先跑 alt text、labels、heading order、landmarks、semantic controls、lang、contrast 等基础自动项

## 怎么做的（技术原理/机制，事实层面）

- **评分机制：明确非 AI 评分**。FAQ 直说："Scores come from deterministic rules, crawl logic, scoring criteria, and a remediation library. The goal is to avoid fake scoring, random scoring, and AI-generated guesses."——避免"AI 生成的虚假分数"
- **五大检查类**（schema.org featureList 原文）：
  - **SEO / AEO / GEO**：title、meta description、heading 结构、canonical、internal links、robots.txt、sitemap.xml、structured data、Open Graph、**llms.txt**、answer-ready content
  - **Security**：HTTPS、mixed content indicators、common public security headers、insecure forms、sensitive public file exposure、cookie flags
  - **Accessibility**：alt text、form labels、heading order、landmarks、semantic controls、language、contrast、**真实浏览器渲染下的可访问性问题**
  - **Design / Conversion**：CTA clarity、hero clarity、text density、credibility signals、viewport setup、readability、spacing、visual hierarchy、performance、runtime health、layout stability
  - **Monitoring（Pro）**：自动周扫、邮件报告、scan-to-scan 对比、uptime、公开 status page、live widget、website score badge
- **明确不做的事**（FAQ 边界声明）：
  - 不是完整安全审计——不做漏洞扫描、渗透测试、exploit 检查、端口扫描、认证态安全测试
  - 不是 WCAG 认证——只做自动化基础检查，不替代专业无障碍审计
- **Pro MCP**：允许外部 agent（Claude/Cursor 等）通过 Model Context Protocol 读取私有 findings 并触发 rescan——把工具从"网页报表"变成"agent 工作流的输入端"
- **可分享报告**：免费档的扫描结果是一个公开 URL（如 `/scan/businessnetworking-club-81-launch-readiness-report-e5dcd1aa`），可直接发链接分享
- **首页公示**：累计 2,180 次审计（数字直接显示在首页）
- **公开首页排行榜**：列出 Top 3 Pro 站点的 SEO/AEO、Security、Accessibility、Design 四项分数，可见 Verifieddr 100、Carmptrton 98、Wysera 95 等分数档
- **生态对接**：自带 `https://www.freescan.app/llms.txt` 文件，让外部 LLM 抓取产品自身信息

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Jacob Counsell（@JacobCounsell） | freescan.app schema.org Organization.founder |
| 公司主体 | 未单独披露 | 无独立 about / 公司页 / Crunchbase |
| 团队规模 | 未披露 | 仅有 founder 字段，无 employee 数 |
| 融资 | 未披露 | 无 Crunchbase / PitchBook 公开记录 |
| 投资方 | 无 | — |
| 加速器 | 无 | — |
| 合规认证 | 无（B2B 自助工具） | — |

## 定价 / 商业模式

| 档位 | 价格 | 核心差异 |
|---|---|---|
| Free | **$0** | 单公开 URL · 40 项检查 · 可分享报告 · 无账号/邮箱/所有权/crawler 摩擦 |
| FreeScan Pro | **$19/月 USD** | 多站点持续监测：最多 5 站点 · 初筛 60 个公开页基线 · 每周 25 个核心页自动扫 · 每周 5 次手动扫描 · 30 天一次全量 rebaseline · 自动周报邮件 · SEO Workspace + AI Visibility Workspace · scan history + scan-to-scan diff · 可选 uptime（公开 status page + live widget + 官网 score badge）· MCP 接入 · Markdown 导出 |

- 模式要点：**免费档 0 摩擦做获客漏斗**（FAQ 原话：paste a public URL and get the report first），**$19/月锁的不是单一功能而是"持续监测 + 多站管理 + agent 工作流"**——5 站点封顶，明显是个人/小团队/agency 价位，不是企业级定价
- 付费阶梯：**单次单页 → 多站点持续监测**，跨越的不是功能数量而是工作场景（一次性诊断 vs. 持续运维）

## 关联信息 / 生态

- **对标/竞品定位**（FAQ 自述对比）：
  - **Lighthouse**（Google，performance/SEO 为主）
  - **WAVE**（WebAIM，无障碍）
  - **SecurityHeaders.com**（安全头专项）
  - **通用 SEO 套件**（Ahrefs / Semrush，覆盖 backlink + rank tracking）
  - 差异化卖点："bundles SEO, security, accessibility, and design checks into one scorecard"
- **明确不替代的领域**：完整安全审计（漏洞/渗透）、WCAG 认证、专业无障碍审计、backlink 分析、rank tracking、流量分析——主动划清边界
- **AI 检索新范式**：与 llms.txt 生态直接对接（产品自身也提供了 `/llms.txt`），把 AEO/GEO 当作与 SEO 并列的一类审计
- **Agent 工作流**：Pro 版 MCP 让 Claude/Cursor 等 agent 把 FreeScan 作为"读取私有 findings + 触发 rescan"的工具——契合 2026 年 agentic coding 浪潮
- **首页公示分数**（Pro 站 leaderboard 快照）：Verifieddr 100 / Camprtron 98 / Wysera 95 / Godaddy 48 / Give 96 / Pixelnode 82 / Holiranggilal 86 / Heybrady 38 / Waresport 90 / Businessnetworking 81 等
- **媒体/榜单**：本次仅 PH 上榜（#9 · 97 票 · 18 评论），其他公开榜单/媒体报道未查到

## 技术时间线（官网/Schema 提及）

| 日期 | 事件 |
|---|---|
| 2026-08-04 之前 | 已上线（首页 testimonial 最早一条 @HixonStudio 推文日期） |
| 2026-08-19 ~ 09-03 | 多位 indie hacker 在 X 发推公开使用结果（@Inglehoff / @JustinHammon / @JessePeplinski / @MarkZofMarkZ / @GirishKotte / @AfterimageDev / @techie_piyush / @SoloBossApp） |
| 2026-09-10 | PH 上榜 #9（97 票 / 18 评论） |
| 2026-09-10 | 首页公示累计 2,180 次审计 |

> 官网未提供 changelog 或 release notes 页，本次未抓到具体版本/迭代节奏。

## 评论区反馈（事实摘录，不评价）

本次 PH 页（https://www.producthunt.com/products/freescan-app）受 Cloudflare 拦截未能抓到评论原文，以下 10 条用户证言来自 freescan.app 首页 JSON-LD 中署名引用的 X 推文（全部为公开可链接的帖子，时间 2026-08-04 ~ 2026-09-03）：

- **Jay（@SoloBossApp，2026-09-03）**：扫描 EverList 修复后 "SEO/AEO: 100 / Security: 100 / Real-browser accessibility: clean"
- **Piyush Sachdeva（@techie_piyush，2026-09-02）**：之前用 Lighthouse，FreeScan 审计了更多东西，正在用生成的 prompt 提升分数
- **Afterimage（@AfterimageDev，2026-09-02）**：扫描 ScreenshotPop 后做了改进，"excellent explanations and tailored prompts to paste right into your agent to fix"
- **Girish Kotte（@gkotte1，2026-08-30）**：第一次扫描 wysera 拿到 80 分，"every failed check came with the evidence, the severity, and the actual fix"；修复后 100/100，四类全 100，"37 of 37 checks passing"
- **Mark Z（@MarkZofMarkZ，2026-08-25）**："the freakin' bomb ... most complete FREE tool with even prompts you can give to AI to help fix things"
- **Jesse Peplinski（@JessePeplinski，2026-08-20）**：扫描 FreeScan 自身（自我审计），承认有改进空间
- **Justin Hammon（@justinhammon_，2026-08-20）**：为 RoleNavigator 不知如何改 SEO/无障碍，"It even has prompts you give Claude Code to target the fix"
- **Inglehoff（@Inglehoff，2026-08-19）**：工作流 "scan → give my agent the results url → PR review → ship"，workwomp.com 无障碍分从 72 提到 100
- **Hixon（@HixonStudio，2026-08-04）**：hackyard.tech 40 → 86，"free, no signup wall, genuinely useful"
- **YoloBytes（@yolobytes，2026-08-05）**：请求增加"导出分数为 jpg"按钮，方便发 X vanity 截图

## 信息来源

- **PH 产品页**：https://www.producthunt.com/products/freescan-app（拿到 tagline · 品类标签 · 票数评论数 · logo URL · 排名 #9；本次抓取被 Cloudflare challenge 拦截，未抓到评论原文）
- **官网首页**：https://www.freescan.app（拿到完整 JSON-LD · featureList 14 条 · Pro 定价 $19/月 · 创始人字段 · FAQ 10 条 · 累计 2,180 审计数 · leaderboard 样例分数 · 10 条用户证言推文链接 · llms.txt 路径）
- **GitHub**：github.com/freescan 为无关旧用户（3 个仓库，user_id 2087801，与 FreeScan.app 项目无关）；github.com/JacobCounsell 返回 404——项目**闭源**，未公开仓库
- **创始人 X**：https://x.com/JacobCounsell（schema.org founder 字段指向，10 条 testimonial 推文均 @ 创始人，本次未深挖创始人过往产品履历）
- **公开报道**：本次未抓到第三方媒体报道（搜索未发现 TechCrunch / The Verge / Hacker News 等独立报道）

## 未查到 / 待补

- **PH 评论原文**：被 Cloudflare 拦截，仅抓到首页 JSON-LD 引用的 10 条 X 证言，PH 页面 18 条评论的创始人回复/提问者具体诉求未抓到
- **公司主体 / 融资**：未单独披露，无 Crunchbase / LinkedIn 实体记录
- **创始人 Jacob Counsell 履历**：本次未查到过往产品 / 工作经历（LinkedIn / X 历史未深挖）
- **MCP 服务器实现细节**：Pro 版说"MCP 接入可读取私有 findings 并请求 rescan"，具体 SDK、鉴权方式、限速未公开
- **Pro 档是否限速/限页**："5 站点 / 25 核心页周扫 / 5 手动扫描/周"是基线，但超量后的硬限/软限未在 FAQ/首页说明
- **年付折扣**：首页只看到月付 $19/月，年付价/团队版/agency 多席位套餐未在抓取范围内出现
- **审计准确率声明**：FAQ 说"deterministic rules"，但未公布 40 项检查的覆盖率、误报率、对抗测试结果
- **数据保留 / 隐私**：免费档扫描结果生成公开 URL，分享/私有化选项未在 FAQ 明确
- **国际支付**：是否支持非美元结算、是否提供发票（针对独立开发者/小团队常见需求）未在抓取范围内
- **第三方权威背书**：无媒体报道、无奖项、无审计合作伙伴（如 WebAIM/OWASP 联合推荐）
- **独立技术评审**：Wappalyzer / BuiltWith 类工具未在本次范围内交叉验证 Next.js/规则引擎等栈
