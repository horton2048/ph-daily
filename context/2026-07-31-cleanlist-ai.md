# Cleanlist AI · 扩展阅读上下文

> PT 2026-07-31 Product Hunt 榜单第 2 名 · 👍 280 · 💬 27
> 归档日期 2026-08-01 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Cleanlist AI |
| 英文 tagline | Natural-language prospecting: find, enrich and sync leads. |
| 中文 tagline | 自然语言线索挖掘：查找、丰富并同步潜在客户 |
| 官网 | https://www.cleanlist.ai |
| PH 页 | https://www.producthunt.com/products/cleanlist-ai |
| 品类标签 | Sales · SaaS · Artificial Intelligence（PH）；Lead generation software · AI sales tools（官网） |
| 票数 / 评论 | 280 / 27（PH 页同时显示"308 points"，两个口径并存） |
| 公司主体 | Cleanlist（官网页脚 © 2026 Cleanlist）；GitHub 组织显示注册地 Canada |
| 企业版/关联站点 | app.cleanlist.ai（应用入口）；AppSumo / G2 / Chrome Web Store 上架 |

## 是做什么的（如实复述）

Cleanlist AI 是一个**面向 B2B GTM 团队的"线索挖掘 + 数据富化 + CRM 同步"一体化平台**。它把传统 prospecting 流程——查找、富化、验证邮箱/电话、清洗、推送到 CRM——压缩成一个工作流，核心卖点是用一句自然语言提示（"找 50-200 人的纽约 SaaS 创始人 100 个"）就能产出一条已富化、已验证、可直接推到 HubSpot/Salesforce 的列表。

支持四种输入起点：
1. CSV 上传（已有名单）
2. LinkedIn / Sales Navigator URL 粘贴
3. People Search 过滤器（按职位、地区、行业、人数、融资阶段等）
4. Chrome 扩展（在 LinkedIn 个人页一键取邮箱/电话）

以及两种"问"的方式：Copilot 自然语言对话；或通过 API + MCP server 从 Claude / Cursor 等 AI 工具里驱动。

定位：把"需要 GTM 工程师拼 5+ 工具"的活儿，做成"开箱即跑"的成品 playbook。

## 解决什么问题（事实层面，不判断值不值得）

- **流程碎片化**：创始人 Levon 在 PH 评论区描述的痛点——"导出名单→A 工具富化→B 工具验证→修 CSV→灌 CRM，结果一半邮件还是 bounce"。
- **数据时效性**：买家 Artur Brugeman 在 PH 评论区提到"买过的名单一半邮件 bounce，决策人几个月前已离职"。创始人回复称 Cleanlist **不持有自己的数据库**，每次查询实时跨 15+ 个 provider 走瀑布，避免数据陈旧。
- **GTM 工具门槛**：对标 Clay 等需要专职 GTM 工程师配置的工作流编排器，定位为"无 GTM 工程师团队也能用"。
- **目标场景**：B2B 销售、市场、founder-led 团队的 outbound 线索建设、CRM 清洗、ICP 评分。

## 怎么做的（技术原理/机制，事实层面）

- **15-provider 瀑布富化**：每条记录按"命中率×成本"排序依次查询 15+ 数据供应商（页面示例中出现 Cleanlist / Wiza / Findymail / Prospeo / Lusha 等），命中即停。官方称大多数记录在前 1-2 个 provider 解决。
- **不持有数据库**：创始人 Victor 在 PH 评论区称"我们不拥有数据库，所以数据不会在我们服务器上变陈旧；每次富化实时出去 15+ provider 瀑布到找到匹配为止"。
- **按命中计费**：每个验证邮箱 = 1 credit，无论背后走了 1 个还是 9 个 provider；查不到不收费。
- **验证状态回传**：每个邮箱都带验证状态，发信前可知是否安全发送，避免伤域名信誉。
- **Smart Agents（AI 研究列）**：自然语言问"这家公司在用什么 CRM、是否在招 SDR、网站是否提及 SOC 2、是否符合我们 ICP"，AI agent 读网站和招聘信息填到单元格里。
- **CRM 双向同步**：HubSpot/Salesforce/Pipedrive 原生双向同步；默认 fill-empty-only（不覆盖已有数据），可按字段配置 overwrite/append；HubSpot 按 email 匹配去重并更新现有联系人。
- **集成**：HubSpot、Salesforce、Pipedrive、Outreach、Salesloft、Lemlist 原生集成；另提供 REST API + Webhooks。
- **数据出处（provenance）**：每条富化字段记录来源 provider，存储于记录上（PH 评论区 Victor 回复 Dale Mooney 的 GDPR Article 14 提问）；**该能力目前未在 UI 中暴露**，需联系支持拉取，创始人称"自助导出"在路线图上但未给日期。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Levon Adamyan（Co-Founder & CEO）、Sal Anvarov（Co-Founder & CTO）、Victor Paraschiv（Co-Founder & COO） | 官网 About |
| CEO 背景 | 前 Float（加拿大企业支出管理平台）Head of GTM Operations，称其增长项目使 outbound pipeline 翻倍、次季度 outbound 收入预测提升 175%；前 Keep Growth Lead（称建到 100+ meetings/月）；HUI Consulting 从 2 人扩到 25 人，年生成 $25M+ 客户 pipeline | 官网 About |
| CTO 背景 | 前 Shopify / Amazon / Intuit / IBM 工程师；称把 Stan 旗舰产品 Stanley 两个月内做到约 $2M ARR；维护开源 NestJS boilerplate | 官网 About |
| COO 背景 | 前 EffyDesk 唯一市场 hire，管理 $100K+/月广告预算 3.5 年，称驱动 $15M+ 盈利收入；LearnToCut 从 $0 做到 $150K/月；Risedesk 工作 $1.2M 收入；多伦多大学 Rotman Commerce BBA；Mensa 会员 | 官网 About |
| 团队前公司 | Float、Keep、Hopin、Shopify、Litmus | 官网 About（"Leadership Team"行） |
| 融资 | 未查到（官网 About 无融资信息；PH 评论区无；公开搜索无相关报道） | — |
| 投资方 | 未查到 | — |
| 加速器 | 未查到（无 YC / Techstars 公开记录） | — |
| 合规认证 | GDPR Article 14 数据出处能力（PH 评论区回复）；具体合规认证未查到 | PH 评论 |
| 公司所在地 | Canada（GitHub 组织页显示） | github.com/cleanlist-ai |

## 定价 / 商业模式

credit 制（按命中计费，1 验证邮箱 = 1 credit，查不到不收费），年付比月付省 25%，所有付费档未用 credits 可 rollover。

| Plan | 价格（年付） | Credits/年 | 免费座位 | 关键能力 |
|---|---|---|---|---|
| Free | $0 | 360 | 1 | 15+ provider 富化、Chrome 扩展、CSV 导出、每列表 100 条 |
| Starter | $59/月 | 18,000 | 2 | AI Search、CSV 上传、Sales Navigator、AI Agents（基础）、每列表 2,500 条 |
| Pro（推荐） | $172/月 | 60,000 | 5 | CRM 导入与集成、API + Webhooks、原生 CRM 同步、优先支持 |
| Scale | $449/月 | 180,000 | 10 | Playbooks、AI Agents（高级）、分析仪表盘、批量 credit 费率 |
| 额外座位 | +$15/座/月（年付；功能对比表显示 +$20/座） | — | — | — |

- PH 评论区 Levon 称已有 **500+ 付费用户**（"We have over 500 paying users already!"）。
- 官网首页称 **1,500+ GTM 团队使用**（"Used by 1,500+ GTM teams"，口径不同于付费用户）。
- 官网首页称数据准确率对比图：Cleanlist 98%，并列出 Apollo ~80%、ZoomInfo 85% 等同行对比数字。
- 公开评分：G2 5.0、Chrome Web Store 5.0、AppSumo 4.86/5。
- PH 专属优惠码 `PH25` = 永久 25% off；夏日促销码 `SUMMER25` 同样永久 25% off（截止 2026-07-31）。

商业模式特点：**按命中计费的 credit 制**（不是按座位计费为主，座位是次要收入），团队共享一个 credit 池；未命中不扣费；高客单靠 Scale 档的 180K credits + 多座位 + Playbooks/高级 Agent。

## 关联信息 / 生态

- **能力矩阵**（官网导航"PLATFORM"）：Waterfall Enrichment、Email Verification、Data Enrichment、Smart Agents、ICP Scoring
- **工具**（"TOOLS"）：People Search、Playbook Builder、Sales Nav Scraper、LinkedIn Scraper
- **免费小工具**：Reverse Email Lookup、Email Verifier、Email Extractor、LinkedIn Email Finder、Phone Number Validator、Contact Finder、Email Format Finder
- **集成**：HubSpot、Salesforce、Pipedrive（双向 CRM sync）；Outreach、Salesloft（enrich & sync）；Lemlist（推送到 campaign）；REST API + Webhooks
- **案例研究**（官网）：
  - Float：替换 5+ 数据工具，平均交易规模 +30%（Ruslan Valeev，Senior Director, RevOps）
  - Warp：冷电话接通率从 8% 提到 13%（Hayk Ghon, GTM Lead）
  - Proposify：inbound 转化翻倍、整体转化率 +30%（Evan Santa, VP of Sales）
  - Gastronomous：一天内搭起完整 outbound 流程（Kristian Tazbazian, COO & Co-Founder）
- **竞品定位**：官网有专门对比页 Cleanlist vs Apollo / ZoomInfo / Clay / Lusha / FullEnrich；首页数据准确率对比图把 Cleanlist 98% 与若干同行并列
- **历史发布**（PH"Launches"栏）：本次是第 3 次在 PH 发布
  - 2025-11-30："Find, enrich, clean, and verify prospecting leads instantly."
  - 2025-12-15："Run Playbooks - Find, Enrich, Clean & Sync Leads Instantly"
  - 2026-07-31：本次（自然语言 prospecting 主题）

## 技术时间线（官网里程碑）

官网 About 未公开融资 / 加速器 / 合规认证等里程碑，仅有"前 Float/Keep 等公司工作经验"叙事。技术时间线只能从 PH launch 历史推出：

| 日期 | 事件 |
|---|---|
| 2025-11-30 | 第 2 次 PH 发布（find/enrich/clean/verify） |
| 2025-12-15 | 第 1 次 PH 发布（Run Playbooks 主题） |
| 2026-07-31 | 第 3 次 PH 发布（Natural-language prospecting 主题），日榜 #2 |

## 评论区反馈（事实摘录，不评价）

- **Artur Brugeman**（买家视角）：质疑数据时效性与置信度标记——"买过的名单一半邮件 bounce，决策人几个月前已离职"。
  - **Victor（创始人）回复**：称邮件验证率 95%+，电话匹配率 ~85%；不持有自己的数据库，每次实时跨 15+ provider 瀑布；未命中不收费。
- **Dale Mooney**（GDPR Article 14 质疑）：15-provider 瀑布对 provenance 不友好，UK/EU GDPR Article 14 要求能告知个人数据来源； lawful basis（合法利益）对冷触达个人有限。
  - **Victor 回复**：每个富化字段记录来源 provider，存于记录上；UI 尚未暴露，可联系支持拉取；承诺会在 footer 上线公开的 lawful basis + DPA 页面。
  - **Dale 续**：建议自助导出（subject access request 有 1 个月时限，邮件支持在量大时会失效）；建议公开 lawful basis 页面用稳定 URL、纯文本而非营销语气，方便 DPO/安全审查转发。
  - **Victor 续**：承认没想到" requester arrives with no context and a deadline"；会上线 lawful basis 公开页；自助导出未给日期。
- **Steven J. Morell**：质疑"是不是简化版 Clay？CSV + Claude Code 不能做吗？"
  - **Victor 回复**：Clay 需要专职 GTM 工程师，Cleanlist 更便宜且开箱即用；Claude Code 没有 underlying 数据库，Cleanlist 提供真数据库 + 瀑布富化 + Smart Agents；提供 API + MCP server，可由 Claude Code 驱动。
- **Alex**：15-provider 瀑布跑全部会贵。
  - **Victor 回复**：按命中率×成本排序，多数记录前 1-2 个 provider 解决；每个验证邮箱 1 credit，背后 provider 数量无关；未命中不收费。
- **Raffay Sajjad**（运维质疑）：批量 CSV 上传几千行时，如何应对各 provider 自己的 rate limit？
  - （截至归档时尚无官方回复）
- **Andrei-Constantin Alexandru**（实测反馈）：Google 注册正常，但 Network 中很多 GET 返回 401；Copilot 过滤 QA Manager 时生成了未执行的 function_calls 代码片段。
  - **Victor 回复**：People Search 有手动 title 过滤器可直接精确匹配；其余问题联系 live chat / support@cleanlist.ai。
- **Dogan Akbulut**：HubSpot 同步是否去重？
  - **Victor 回复**：按 email 匹配更新现有联系人，默认 fill-empty-only，可按字段配置 overwrite/append；建议先小批跑验证。
- **Suryansh Tiwari**（负面评论）：UI 老旧、导航混乱、不推荐。
  - **Victor 回复**：指出该用户并无账号，是曾主动联系承诺刷票被拒的 agency，要求其删评论。
  - **Levon 回复**：贴出该用户威胁"Going to do mass bot attack"的原话，请求 PH 官方处理。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/cleanlist-ai（拿到了 maker 长帖、12 条 maker 回复、2 页评论全部、产品描述、Launches 历史、Similar Products 列表）
- PH 评论第 2 页：https://www.producthunt.com/products/cleanlist-ai?page=2#comments
- 官网首页：https://www.cleanlist.ai/（拿到了产品定位、4 种输入、瀑布富化演示、数据准确率对比图、定价表嵌入、客户案例、集成列表、积分 G2/Chrome/AppSumo）
- 官网 About：https://www.cleanlist.ai/about（拿到了 3 位创始人完整背景、团队前公司、产品理念、内部 origin story）
- 官网 Pricing：https://www.cleanlist.ai/pricing（确认了 4 档定价、credit 制、年付 25% off）
- GitHub：https://github.com/cleanlist-ai（组织存在，"This organization has no public repositories"，注册地 Canada，2 followers，符合闭源商业产品预期）
- 公开报道：通过 WebSearch / WebFetch 搜索 "Cleanlist AI funding"、"Cleanlist AI Levon Adamyan seed YC Techstars 2025" 均无相关公开报道

## 未查到 / 待补

- **融资信息**：无任何公开的种子轮/VC/加速器记录。官网 About 无融资里程碑（不像 Halo 的 About 会列）。PH 评论区无。WebSearch / WebFetch 均未命中。
- **公司法律主体名称**：官网页脚仅 "© 2026 Cleanlist"，无 Inc./Ltd. 等法律后缀；具体注册地（多伦多？）未在官网 About 中确认，仅 GitHub 组织页显示 Canada。
- **公司规模**：员工数未披露。
- **成立日期**：未明确披露（PH 显示 "Launched in 2025"，最早一次 PH 发布 2025-12-15）。
- **数据准确率第三方审计**：98% / 95%+ / 85% 均为官方自称数字，未找到独立审计报告。
- **lawful basis / DPA 公开页**：截至归档时仍在路线图上，Victor 承诺会上线但未给日期。
- **Raffay Sajjad 关于批量 rate limit 处理的问题**：截至归档时创始人未回复。
- **企业版（超过 Scale 档）**：官网未列出 Scale 之上的 enterprise 档；PH maker 帖提到 "Get a Demo" / "Talk to a human" 入口指向 Calendly，但未公开 enterprise 定价。
