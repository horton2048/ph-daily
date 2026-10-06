# Website to Markdown API · 扩展阅读上下文

> PT 2026-08-06 Product Hunt 榜单第 7 名 · 👍 票数 PH 页未显示 · 💬 2
> 归档日期 2026-08-06 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Website to Markdown API |
| 英文 tagline | Turn any website into LLM-ready Markdown |
| 中文 tagline | 把任意网站转成 LLM 可直接用的 Markdown |
| 官网 | https://exabase.io/tools/website-to-markdown |
| PH 页 | https://www.producthunt.com/products/website-to-markdown-api |
| 品类标签 | API · Developer Tools · Data |
| 票数 / 评论 | 票数未显示 / 评论 2（归档 2026-08-06） |
| 公司主体 | Exabase（exabase.io，"Context infrastructure for your agents"）；也是 Fabric AI 工作区的基础设施层 |
| 企业版/关联站点 | Exabase 平台（memory/bases/resources/deep-search/extract/workers）；npm SDK `@exabase/sdk`；X/Twitter @exabaseio |

## 是做什么的（如实复述，不评价）

这是 Exabase 平台下的一个 API 工具：给一个 URL，返回该网页内容的 Markdown 文档。页面会在提取前先做 JS 渲染，所以 React、Next.js、Vue、Angular 等动态站也能像静态 HTML 一样被提取；导航、页脚、cookie 横幅、广告会被去掉，只留正文。官方称输出可直接喂进 LLM 上下文窗口、知识库或 RAG 流水线，无需再清洗。同一个端点也处理 PDF、DOCX、PPTX、EPUB、图片、音频、视频。作为 Exabase 的一部分，同一个 API key 还可用平台的其他能力（deep search、memory、automation）。

## 解决什么问题（事实层面，不判断值不值得解）

- Maker（Johnny）开场评论："把网站变成干净、可用的文本，仍然比它应有的难度大得多"；"前 10 个站好使，第 11 个就崩了，所以我们把它做成了一个 API 调用"。
- 痛点：网站抓取通常要处理 JS 渲染、反爬、导航/页脚噪声、以及不同文件格式（PDF/PPTX/音视频）。
- 目标场景：LLM 上下文窗口、知识库、RAG 流水线、研究型 agent 的直接输入源。

## 怎么做的（技术原理/机制，事实层面）

- 提交方式：`POST /v2/extract` 异步提交任务，轮询 `GET /v2/extract/{jobId}` 直到 state 为 "completed"；或配置 webhook（`webhookFormat: "markdown"`）让服务器把结果 POST 到你的服务，免轮询。
- 输出：`GET /v2/extract/{jobId}?format=markdown` 返回 `Content-Type: text/markdown` 的单文本文档；头部为页面标题、站点名、MIME、大小等元数据，正文在 `## Content` 段落下。
- 默认仍是 JSON；Markdown 与 JSON 是"同一次提取的两种视图"；`?format=json` 可拿结构化文本分块。
- 技术细节：页面在提取前先渲染（服务器端处理 JS），无需自己维护 headless browser；反爬处理内置（代理轮换、浏览器指纹、重试）；robots.txt 阻止第三方访问的站点会返回错误。
- 多格式：同一端点处理网页、PDF、图片、音频、视频；图片输出尺寸 + OCR 文本，音视频输出时长 + 完整转写。
- 认证与存储：所有请求带 `X-Api-Key` 头；存储文件自任务创建起保留 1 天，之后永久删除。
- 局限：只能提取公开页面；登录后才可见的内容无法提取。
- 平台底座：Exabase 自称"为 AI agent 做基础设施"，提供 memory（自我维护的知识图谱，两条 API 调用完成存取）、bases（每租户隔离实例 + 版本回滚）、resources、deep search（子文档级多模态混合检索）、workers（定时自然语言任务）等。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| Maker | Johnny（PH 用户名 @johnny_makes），自称"team behind the Website to Markdown API"的创始人；真名 Jonathan Bree，同时是 Exabase 与 Fabric 的创始人/CEO | PH 页 / LinkedIn / Arrfounder |
| 公司 | Exabase（Jonathan Bree 任 Founder & CEO）；LinkedIn 自我描述"Building infrastructure for the world's private data. Products: Fabric - self-organizing personal cloud & AI workspace; Exabase - data layer for agents" | LinkedIn（Jonathan Bree） |
| 关联产品 | Fabric（fabric.so）：AI 个人数据平台/工作区，Exabase 是其后端基础设施层，官方称"数十万用户" | exabase.io / fabric.so |
| 融资 | 未查到（本次未抓到融资报道；Crunchbase 有 Exabase 词条但内容未抓取） | 待补 |
| 团队规模 | 未查到（官网无团队页） | 待补 |
| 合规/安全声明 | "CASA certified"、99.9% uptime、传输 SSL 加密、静态 AES-256 加密（官网营销声明，未独立验证） | exabase.io |

## 定价 / 商业模式

- Exabase 定价页（2026-08 抓取）：
  - Free：$0/月，每小时 1k 请求，含 1GB 存储（超出 $0.06/GB/月），每月 200 credits（超出 $0.02/credit），最多 100 个 bases，新用户 $30 免费额度。
  - Scale：$149/月（按年 $1490/年，相当于免 2 个月），每小时 5k 请求，含 2TB 存储（超出 $0.05/GB/月），每月 5k credits（超出 $0.01/credit），最多 10k bases，零数据留存策略，基础支持。
  - Enterprise：定制（联系销售），无限请求、可谈存储、无限 bases、优先支持。
  - Credit 换算：1 credit ≈ 约 18 次 PDF 提取 / 约 18 次网站提取 / 约 30 次音频提取 / 约 0.8 次视频提取 / 约 65 条 memory（或带 inference 约 10 条）。
- Website to Markdown 工具页口径："Free plan available, no credit card required"；未列出该工具专属的付费档金额（同页面）。
- 官网营销声明：token 花费可降"最多 81%"，示例为 $14.9K/月 → $2.8K/月（未独立验证）。

## 关联信息 / 生态

- 平台对比（Exabase 官方页面给出）：vs Jina Reader——Jina 聚焦纯净文本提取，Exabase 把 Markdown 作为更大提取 API 的其中一种输出；vs Firecrawl——Firecrawl 聚焦大规模爬取，Exabase 聚焦单个 URL 提取 + 存储/搜索/记忆/自动化平台；vs Trafilatura——开源 Python 库自己跑，Exabase 是托管 API。
- 同平台工具页：PDF/DOCX/PPT/EPUB/发票/合同/简历→JSON/Markdown、Link preview API、PDF thumbnail 生成器、token 成本计算器等。
- 生态位置：为 Fabric 提供基础设施；Fabric 支持多模型（Gemini、OpenAI、Claude、Deepseek、xAI、Z.ai、Kimi、MiniMax、Qwen），文件支持 PDF/video/EPUB/docx/pptx/CSV/HTML/JSON/Markdown 等。
- PH 页相似产品区列出：Mintlify、Firecrawl、Context.dev、ChatDox AI、Hashnode。
- 营销数据：官方称处理超过 100,000,000 个页面（exabase.io 首页，未独立验证）。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 | 来源 |
|---|---|---|
| 2026 | Website to Markdown API 上线并在 PH 发布（"Launched in 2026"，PH 页；maker 开场评论约在发布前 5 天，发布日前后） | PH 页 |
| 2026-08-06 | PH 榜第 7 名发布日 | 归档 2026-08-06 |
| （未查到） | Exabase M-1 memory 系统 BEAM 基准"最高分"声明（HN 帖子存在） | HN / exabase.io blog（未深抓） |

## 评论区反馈（事实摘录，不评价）

- Soumyadip Banerjee（@seomaxtech，用户）："试了几次，输出好得离谱。干得漂亮！"（发布于 maker 开场评论之后约 1h；maker 开场评论获 2 个赞）
- 其余未抓到更多评论；归档 2026-08-06 记录评论数为 2。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/website-to-markdown-api（描述、maker 开场评论、评论区、相似产品、logo URL）
- 官网工具页：https://exabase.io/tools/website-to-markdown（端点、webhook、反爬、多格式、局限、对比、免费计划）
- 官网首页/定价：https://exabase.io/ 、https://exabase.io/pricing（平台能力、Free/Scale/Enterprise 金额、credit 换算、安全声明、与 Fabric 的关系）
- 公开报道/检索：DuckDuckGo 搜索 "Exabase Fabric founder Johnny AI"（Arrfounder、HN 帖子、Biotech Now 稿）；LinkedIn（Jonathan Bree）
- GitHub：https://github.com/exabase（Exabase Services 组织存在，6 个仓库，但无产品开源仓库；@exabase/sdk 为 npm 客户端 SDK）

## 未查到 / 待补

- Exabase / Fabric 的融资与团队规模：本次未抓到（Crunchbase 词条存在但未抓取成功），待补。
- Website to Markdown 专属的付费档定价（区别于 Exabase 平台档位）：未查到。
- "CASA certified"的具体认证机构/范围与 81% token 节省的具体方法学：营销声明，未独立验证，待补。
- 具体票数：PH 页未显示（归档亦未含票数）。
- Fabric 与 Exabase 的公司法律主体关系（同一实体或子公司）：官网未明说，待核。
