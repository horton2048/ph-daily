# Brandfetch MCP · 扩展阅读上下文

> PT 2026-08-06 Product Hunt 榜单第 5 名 · 👍 票数 PH 页未显示 · 💬 3
> 归档日期 2026-08-06 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Brandfetch MCP（Model Context Protocol server） |
| 英文 tagline | Stop your AI from guessing brand logos |
| 中文 tagline | 别再让 AI 瞎猜品牌 logo |
| 官网 | https://brandfetch.com/ |
| PH 页 | https://www.producthunt.com/products/brandfetch |
| 品类标签 | Design Tools · Developer Tools · Artificial Intelligence |
| 票数 / 评论 | 票数未显示 / 评论 3（归档 2026-08-06） |
| 公司主体 | Brandfetch（品牌数据平台公司），本次是其在 PH 的第 10 次发布 |
| 企业版/关联站点 | 品牌数据平台 brandfetch.com；MCP 文档 docs.brandfetch.com/mcp/overview；开发者定价 brandfetch.com/developers/pricing；Claude 连接器 claude.ai/directory/connectors/brandfetch |

## 是做什么的（如实复述，不评价）

Brandfetch 本身是一个品牌数据平台：可按品牌名搜索官方 logo、配色、字体与公司信息，也对外提供 API。本次 PH 发布的是它的 MCP server（Model Context Protocol 服务器），作用是让 AI 助手（Claude、Cursor、VS Code、Codex 等）在生成内容时直接调用 Brandfetch 数据库，取回真实品牌资产，而不是靠模型自己"猜"logo 和配色。官方口径数据库覆盖 50M+ 品牌，自称客户包括 Canva、Typeform、Pitch。MCP 发布页标注"免费（Free）"。它工作方式上是远程托管的 MCP 端点（https://mcp.brandfetch.io/mcp），也支持自托管。

## 解决什么问题（事实层面，不判断值不值得解）

- 官方描述（PH 页）："AI agents redraw logos, invent hex codes, pull the wrong assets, and make up brand voice"——即 AI 代理会重绘 logo、编造色值、取错素材、虚构品牌语调。
- 目标场景：面向客户的品牌化文档、带正确客户 logo 的 pitch deck/原型、以及带公司画像与品牌上下文的富集（enrichment）流程。
- 具体案例（maker 开场评论建议）：让 Claude "用 Stripe、Adyen、Airbnb 各自的 logo、配色和定位做一张销售对比 deck"。

## 怎么做的（技术原理/机制，事实层面）

- PH 页 maker 开场评论列出 5 个 MCP 工具：
  1. `brand_search`——按名称/域名/模糊查询解析一家公司
  2. `get_brand`——logo、配色、字体、公司信息、社交链接
  3. `get_brand_context`——品牌语调、定位、受众、产品（LLM-ready 上下文）
  4. `enrich_transaction`——从原始交易描述（如信用卡/银行流水字符串）解析商户品牌
  5. `build_logo_urls`——生成生产可用的 CDN logo URL（无需 API 调用）
- GitHub 仓库 README 显示共 7 个工具，另有 `get_asset_base64`（把 CDN 资产以 base64 取回）和 `send_feedback`。
- 托管端点 `https://mcp.brandfetch.io/mcp`，无需安装；认证用 `bf1.` 开头的 bearer token（在 Brandfetch dashboard 的 "Keys and MCP" 页面生成）或 OAuth。
- 支持客户端：Claude Desktop / Claude Code（HTTP 配置 + Bearer 头）、Cursor（`~/.cursor/mcp.json` 或项目配置）；支持 OAuth 的客户端可直接指到托管地址。
- 自托管：用 FastMCP 构建，HTTP（streamable-http）服务器，可 Docker 打包；需 Python 3.11 与 uv；MIT 许可证。
- 仓库状态：5 commits、8 stars、1 fork（GitHub 抓取时点）。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Amin Kasimov、Nuri Kasimov（PH maker，kasimov 兄弟）；Hunter 为 Nicolas Grenié（Typeform） | PH 页 |
| 成立时间 | PH 页显示"2019 年在 Product Hunt 上线"；Tracxn 显示 2006 年成立于瑞士 Renens（两处不一致） | PH 页 / Tracxn |
| 共同创始人 | Tracxn 记载 Amin Kasimov、Jeremy Jaques、Nuri Kasimov | Tracxn |
| 融资 | 已融资（有 funding），金额被掩码；仅一轮；唯一机构投资人为 FIT | Tracxn |
| 员工数 | 7 人（截至 2026-05-31） | Tracxn |
| 总部 | Renens, Switzerland（Tracxn）；ZoomInfo 记 Vaud, Switzerland | Tracxn / ZoomInfo |

注：PH 页显示公司"Launched in 2019 on Product Hunt"，Tracxn 记"founded 2006"，两者对不上，本档两处都如实列出。

## 定价 / 商业模式

- MCP 本次 PH 发布标注"Free"（PH 页）。
- 官方开发者定价页（经搜索结果摘录）：Free 计划 100 次 fetch，外加 Logo CDN 与 Brand Search 各最多 500K 请求/月，无需信用卡。
- 付费档数字在不同二手来源不一致：Dynamic Business 记 Brand API $99/月 2,500 次调用；HongKoala 记 $129/月 5,000 请求；Enterprise 为"无限量 + 定制条款 + SLA"（二手来源）。官方付费档具体金额本次未直接抓取到（brandfetch.com 返回 403）。
- 官网口径：品牌方在 Brandfetch 托管自家品牌免费，商业模式靠 API 产品（搜索结果摘录）。

## 关联信息 / 生态

- 历史 PH 发布（PH 页"Previous Launches"）：Brand Context API（2026-06-03）、Brand Search API（2023-03-07）、Brand API（2022-11-17）、Brandfetch for Miro（2020-10-05）。
- 历史奖项：Personalization API 2019-05-07 当日第 1、当周第 3；Brandfetch Figma 插件 2019-09-03 当日第 3（PH 页）。
- GitHub 组织 github.com/Brandfetch 下有 5 个公开仓库：brandfetch-mcp-server（官方 MCP 代码，MIT）、Brandfetch-Sketch-Plugin（18 stars）、Logo-API、Brand-API、n8n-nodes-brandfetch。
- PH 页相似产品区列出：Kittl、Typogram、Icons8、Zoviz、Icon buddy。
- 数据库规模口径：PH 页与官网均为"50M+ 品牌"；搜索结果中出现"60M+ 品牌 logo"的第三方说法（Dynamic Business）。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 | 来源 |
|---|---|---|
| 2006（Tracxn 口径）/ 2019（PH 口径） | 公司成立 | Tracxn / PH 页 |
| 2019-05-07 | Personalization API 上线，PH 当日第 1 | PH 页 |
| 2019-09-03 | Brandfetch Figma 插件，PH 当日第 3 | PH 页 |
| 2020-10-05 | Brandfetch for Miro 发布 | PH 页 |
| 2022-11-17 | Brand API 发布 | PH 页 |
| 2023-03-07 | Brand Search API 发布 | PH 页 |
| 2026-06-03 | Brand Context API 发布 | PH 页 |
| 2026-08 | brandfetch-mcp-server 仓库更新（Aug 2026） | GitHub |

## 评论区反馈（事实摘录，不评价）

- Amin Kasimov（Maker，发布约 21h）：开场评论讲"AI 生成的东西只要涉及品牌就会出问题"，列出 5 个工具并给出使用建议。
- Nicolas Grenié（Hunter，Typeform，约 1h）："你很可能正在用代码助手给你的客户做网站、报告或提案……需要正确的、更新的 logo，Brandfetch MCP 正是干这个的。"
- Amin Kasimov（Maker 回复，约 1h）：回应 Nicolas "这正是我们设想的工作流，写作部分已经不错，缺的是给 AI 正确的品牌上下文"。
- 评论总数 3 条；评论区还出现一条推广位（Robynn AI）。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/brandfetch（描述、5 工具清单、maker 开场评论、历史 launch 与奖项、相似产品、logo URL）
- 官网：https://brandfetch.com/（403，未直接抓取；经搜索摘录"品牌托管免费、商业模式靠 API"）；开发者定价页 brandfetch.com/developers/pricing（经搜索结果摘录免费档）
- GitHub：https://github.com/Brandfetch/brandfetch-mcp-server（7 工具、托管端点、认证、自托管方式、MIT、仓库状态）；https://github.com/Brandfetch（组织页，5 仓库）
- 公开报道/数据库：Tracxn（成立/创始人/融资/员工数）；DuckDuckGo 搜索"Brandfetch funding""Brandfetch API pricing"（Dynamic Business、HongKoala 等二手定价来源）

## 未查到 / 待补

- PH 页具体票数：抓取时未显示（归档也未含票数）。
- 官方付费档定价金额与明细：brandfetch.com 被 403 拦截，未直接抓到一手页；二手来源数字不一致（$99/月 vs $129/月），待核。
- 公司成立年份矛盾（2006 vs 2019）：未能核实，建议查瑞士公司注册信息。
- 融资轮次金额、估值、投资人 FIT 的全名：Tracxn 掩码，未查到。
- 数据库"50M+/60M+"精确口径与更新时间：未查到官方说明。
