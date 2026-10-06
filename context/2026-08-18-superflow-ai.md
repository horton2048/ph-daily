---
product: "Superflow AI"
slug: "superflow-ai"
date: "2026-08-18"
rank: 3
votes: 210
comments: 23

category: "AI agent / SaaS"
subcategory: "网站 QA 与视觉评审"
tags: ["AI Agent", "Web QA", "Webflow", "Framer", "Shopify", "WordPress", "Claude", "Velt", "评论标注", "SOC 2", "HIPAA", "Freemium", "YC W22"]

tech_stack: ["Claude (Anthropic)", "Velt SDK", "React", "Next.js", "Webflow", "REST API", "Webhooks"]
platform: ["Web", "Webflow", "Framer", "WordPress", "Shopify", "Next.js", "Netlify", "Drupal", "HubSpot", "Bubble", "Wix", "Elementor", "Squarespace"]
open_source: false
license: ""

business_model: "Freemium + 按席位订阅 + Credit 加油包"
pricing_start: "$0（Starter 永久免费）"
funding_stage: "种子轮（母公司 Velt）"
funding_amount: "$2.5M（Velt 母公司，2022 YC Demo Day 附近披露）"

related_products: ["Velt", "Markup.io", "Pastel", "BugHerd", "ruttl", "Commented", "Screpy", "Builder.io"]
maker_previous: ["Velt (YC W22) — Rakesh Goyal 创办的 SDK 母公司"]
key_signals: ["母公司 Velt 是 YC W22，融过 $2.5M 种子轮；Superflow 是其旗下第 7 次发布", "把 QA checklist 转成 AI agents，团队称平均能抓到手工约 90% 的问题", "按 10 credit / (agent×page) 计费，Starter 永久免费 60 credit/月 + 500 一次性", "SOC 2 Type II + HIPAA with BAA，明确不跨客户训练模型"]

archived_at: "2026-08-18"
sources_count: 4
---

# Superflow AI · 扩展阅读上下文

> PT 2026-08-18 榜单第 3 名 · 👍 210 · 💬 23
> 归档日期 2026-08-18 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Superflow AI |
| 英文 tagline | AI agents that QA your website before launch |
| 中文 tagline | 上线前替你 QA 网站的 AI agents |
| 官网 | https://usesuperflow.ai |
| PH 页 | https://www.producthunt.com/products/superflow-webflow-plugin-for-revisions |
| PH 帖子 | https://www.producthunt.com/posts/superflow-ai |
| 品类标签 | Design Tools · Artificial Intelligence · Marketing automation |
| 票数 / 评论 | 210 票 / 23 评论 |
| 公司主体 | Velt, Inc.（© 2026 Superflow，产品归属母公司 Velt） |
| 企业版/关联站点 | usesuperflow.ai；母公司 velt.dev；YC 公司页 ycombinator.com/companies/velt |

## 是做什么的（如实复述，不评价）

Superflow AI 是一个面向网站交付团队的 AI QA 评审平台。用户把现有的 QA checklist（Excel / CSV / PDF）导入平台，系统把每条检查项变成一个 AI agent，每个 agent 在桌面端和移动端逐页扫描站点，把发现的问题以图钉形式钉在 live site 的对应元素上，并附截图。创始人称平均能抓到团队手工发现问题的约 90%，剩下 10% 由人类评审员判断。整体框架是 "AI 先过一遍、人再签字"——"nothing ships until a person approves it"。

默认 4 个 agent：Accessibility（无障碍）、Broken Links（死链）、Spell Check（拼写）、OG Image（Open Graph 图）。用户也可以基于自家 checklist 生成自定义 agent。

除 AI 评审外，Superflow 还保留了一套传统的视觉评审能力：在 live 站点上钉评论（评论在页面改版和重新部署后依然存活）、客户通过 shareable link 以 guest 模式参与评审无需登录、跨端（桌面/手机/平板）、可评审登录后/SSO/鉴权页面、Kanban 评审工作流、Memory 学习客户偏好。

支持格式：网站、视频、图片、PDF、Lottie。

## 解决什么问题（事实层面，不判断值不值得解）

- 创办前先做 agency 业务的 Rakesh Goyal 在主帖里描述的痛点：一个 agency 有 400 条检查的 spreadsheet、10 人 QA 团队，随着页面数量增长"process stopped fitting the number of pages"，手工 QA 不再 scalable。
- 创意被 AI 大幅加速、成本下降后，"verification" 这一面仍停留在手工阶段——Superflow 主张补的就是 verification 这一段。
- 客户评审来回拉扯：传统 agency 反馈轮数多、approval 周期长，官网案例 Wonderist 称用后"每月省回 47 小时、反馈轮数减 3 轮、3 天到 approval"。
- 目标场景：dental / 医疗内容、home services、real estate marketing、in-house 内容/品牌团队、freelancer/studio。

## 怎么做的（技术原理/机制，事实层面）

- 运行方式：导入 checklist（Excel/CSV/PDF）→ 平台把每条检查变成一个 agent → agents 在桌面端和移动端并行扫描每一页 → 钉 finding 到 live site 元素 + 截图 → 人工 judge 和 sign off。
- 默认 4 个 agent：Accessibility、Broken Links、Spell Check、OG Image；可基于自家 checklist 自定义 agent。
- 自学习机制（Raghul S 在评论中描述）：被 reviewer 拒掉的 finding 不再重复出现；reviewer 手动补的漏检项会沉淀为将来的检查项。
- "Ask AI"：在评审现场调用 AI，回答关于历史客户/站点数据的问题。
- 评审协作：pinned comments 在页面 edit / redeploy 后存活；客户用 shareable link 以 guest 模式参与（无需账号）；可评审登录后/SSO/鉴权页；Kanban + 自定义状态。
- 双向同步：与 Slack / Monday / ClickUp / Asana 双向同步——finding 进 PM 工具成 task，关闭 task 同步关闭 Superflow 中的对应项。
- 集成：Webflow / Framer / WordPress / Shopify / Next.js / Netlify / Drupal / HubSpot / Bubble / Wix / Elementor / Squarespace / HTML / GTM（一键安装或 script tag）；REST API + Webhooks。
- 技术栈：Claude (Anthropic) + Velt SDK（PH "Built with" 列出）；官网 Footer Copyright 为 Velt, Inc.。
- 安全/合规：SOC 2 Type II、HIPAA（带 BAA）、数据驻留选项、客户端 surface 满足 WCAG 2.1 AA；每条 comment/finding/approval 都有 audit trail；per-client 数据隔离，"Nothing is used to train models across customers"；Roles: Admin / Member / Guest（per-project，guest 无限席位）；Enterprise 提供 SSO + SCIM。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 主创始人 / Maker | Rakesh Goyal（@rakeshgoyal）— Velt, Inc. CEO，前 Google PM 9 年（AR in Google Maps & Search） | YC 公司页 + PH maker post |
| 联合 Maker | Mihir（@itsmiri_，Velt）；Raghul S（@itsraghul，Engineer）；Garry Tan（YC 总裁兼集团合伙人，列在 launch team 但非运营 maker） | PH 产品页 |
| Hunter | 未在抓取片段中明确（待补） | — |
| 母公司 | Velt, Inc.，San Francisco，YC W22 批次（Jared Friedman 为对接 YC partner），团队规模 15 人，成立 2020 年 | YC 公司页 |
| 融资 | 母公司 Velt 在 2022 YC Demo Day 前后披露 $2.5M 种子轮 | WebSearch 摘要（具体投资方未在 YC 页列出，待补） |
| 投资方 | 未查到具体名单 | — |
| 加速器 | Y Combinator W22（Velt） | YC 公司页 |
| 合规认证 | SOC 2 Type II、HIPAA with BAA、WCAG 2.1 AA、GDPR APIs（Enterprise） | 官网定价页 |

注：PH "Built with" 同时列出 Claude 和 Velt——Velt 既是母公司也是被引用的 SDK（Velt 提供 embeddable review/approval 组件，Superflow 本身是其上层产品）。

## 定价 / 商业模式

Freemium + 按席位订阅 + Credit 加油包。Credit 定义：1 agent review = 10 credits，即"1 个 agent 跑 1 页消耗 10 credit"。跑 3 个 agent × 1 页 = 30 credit。

| 档位 | 月价（年付） | 月价（月付） | 月 Credit | 约等于 agent review 数 | 关键差异 |
|---|---|---|---|---|---|
| Starter | $0 | — | 60 | ~6 | 1 项目 / 1 seat / 无限 guest / 1GB / 仅 Email 通知 / 99.9% SLA / 500 一次性 signup bonus credit |
| Growth | $24/seat | $29/seat | 300 | ~30 | 无限项目 / 10GB / Recordings + 自动截图 + live review / Slack+Email / dashboard 分析 |
| Scale | $28/seat | $34/seat | 600 | ~60 | 在 Growth 上加：私有评论 / anonymous guest / access control / 自定义状态与品牌 / ClickUp+Asana+Monday+Webhooks |
| Enterprise | Custom | — | Custom | — | 加 REST API / SAML SSO / SOC 2 Type 2 报告 / HIPAA+BAA / 渗透测试 / DPA / 数据自托管 / 多区域 / 99.999% SLA / 专属 CSM |

- Credit 加油包（Growth 及以上）：500 credit $18–$20；2,500 credit $80–$90；10,000 credit $300–$340。加油包 credit 可结转下月，套餐内 credit 不可结转。
- 10 天免费全功能 trial，无需信用卡；trial 结束自动落到 Starter 永久免费。
- 官网有 ROI calculator：solo studio / 300 assets/月 / 20 QA 分钟/asset / $125/小时计费 → $105,000/年 billings recovered。
- PH 列出的 "Pricing: Free" 指 Starter 永久免费 + 500 signup credit，"enough for one real site run"（主帖原文）。

## 关联信息 / 生态

- 母公司/姊妹产品：Velt（YC W22）—— embeddable review/approval SDK，给 AI-native 应用加 "agent + human governance layer"；Superflow 是 Velt 团队面向网站 QA 场景的具体产品/品牌，PH 上是第 7 次发布。
- PH 列出的相似产品：Screpy、Commented、ruttl、Lindo AI、Builder.io。
- 官网 FAQ 里明确点名的竞品：Markup.io、Pastel、BugHerd——区分点是这些"manual by design: a person marks up a screenshot by hand"，Superflow 强调 AI 先过一遍。
- 历史 PH 发布（同一产品线）：Superflow for Lottie Files（2024-03-07）、Superflow for Web Apps（2023-09-19）、Superflow Multiplayer Flock Mode（2023-04-19）、Superflow AI Copilot (GPT-4)（2023-03-20）。
- 客户/可信方 logo：Cox Automotive、GMH、Finsweet、UserVoice、Redshark、Phenyx、Zanger、Children's Defense Fund。
- 客户证言：Wonderist（月省 47 小时 / 减 3 轮反馈 / 3 天到 approval）；Manvi Agarwal, Writesonic；Riley Hennigh, Headway；Simon Smallchua, Harvey。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2020 | Velt, Inc. 成立（YC 公司页） |
| 2022 | Velt 入选 YC W22 批次；2022 Demo Day 前后披露 $2.5M 种子轮 |
| 2023-03-20 | Superflow AI Copilot (GPT-4) 上线 Product Hunt |
| 2023-04-19 | Superflow Multiplayer Flock Mode 上线 |
| 2023-09-19 | Superflow for Web Apps 上线 |
| 2024-03-07 | Superflow for Lottie Files 上线 |
| 2026-08-18 | Superflow AI "AI agents that QA your website before launch" 上线 PH，榜单第 3，210 票 / 23 评论（第 7 次发布） |

更早的产品首发时间、版本里程碑官网未给公开时间线，待补。

## 评论区反馈（事实摘录，不评价）

- **Rakesh Goyal**（maker 主帖）：自述 agency 背景、400 条检查 spreadsheet、10 人 QA 团队、"process stopped fitting the number of pages"；邀请用户"post checks you think no agent can handle, I'll run them live"。
- **Raghul S**（engineer / maker）：描述 agent 并行扫描 + 自学习（rejected finding 不再返回、漏检项变未来检查）、Ask AI、双向 PM 同步、"nothing ships until a person approves it"。
- **Mihir**（maker，Velt）："Agencies can now have QA Agent teammates who run 24/7 and never miss a beat."
- **Gor Geghamyan**：祝贺上线。
- **Jed White**（Andi）：称这是"a cool way to handle the last mile problem on web projects"。
- **Dogan Akbulut**：反馈在 install 页卡住、找不到清晰安装入口（maker 未在抓取片段中回复要点）。
- **Ankush Singh**：称"just in time"——周日要上线 landing site + webapp，刚好用来 QA。
- **Ninuna Ungiadze**：指出对 marketing 团队、尤其本地化内容错误的价值。
- **Lucas Pols**：引用 Rakesh 关于 agency QA 流程的表述。
- **DeAndre Holland**（review）：称赞 Webflow 集成减少了"back and forth phone calls and slack messages"。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/superflow-webflow-plugin-for-revisions — 拿到 tagline、topics、4 位 maker（Rakesh Goyal / Mihir / Raghul S / Garry Tan）、maker 主帖与评论、Built with（Claude + Velt）、相似产品、历史 launches、Pricing: Free、4.7/5 7 reviews、~1K followers。
- PH 帖子页：https://www.producthunt.com/posts/superflow-ai — 拿到 maker 主帖全文、社区评论、Raghul S 技术描述、Rakesh 邀请"live run checks"。
- 官网：https://usesuperflow.ai — 拿到产品机制（checklist→agents、self-learning、Ask AI、双向同步、Memory）、默认 4 agents、集成清单（12 verified）、安全合规（SOC 2 Type II / HIPAA+BAA / WCAG 2.1 AA / per-client isolation）、客户证言、ROI calculator、Copyright Velt, Inc.。
- 官网定价页：https://usesuperflow.ai/pricing — 拿到 Starter/Growth/Scale/Enterprise 四档完整定价与 Credit 结构、加油包价格、SLA、Enterprise 安全特性。
- YC 公司页：https://www.ycombinator.com/companies/velt — 拿到 Velt W22 batch、founded 2020、San Francisco、团队 15、founder Rakesh Goyal（前 Google PM 9 年，AR in Maps & Search）、YC partner Jared Friedman、Superflow 列在 Velt 的 Key Products/Launches。
- WebSearch：Velt 母公司 $2.5M 种子轮（具体投资方名单未列出，待补）。
- GitHub：未见开源信号，未查 GitHub。

## 未查到 / 待补

- 融资具体投资方名单：YC 页和搜索摘要只确认 $2.5M 种子轮，未列投资人。
- Hunter（PH launch hunter）字段：本次抓取片段未明确 hunter 用户名，待补。
- 公司法律实体注册地、税务主体：仅知 Velt, Inc. / San Francisco，更细信息未查到。
- 完整团队名单与职务：仅知 Rakesh Goyal（CEO）、Mihir、Raghul S（Engineer）三人；YC 页团队规模 15 人但未具名。
- 产品首发日期与版本里程碑：官网无公开 changelog/timeline，仅从 PH 历史 launches 反推。
- "Garry Tan 列在 launch team" 的角色定性：是个人支持/站台还是结构参与，未在 PH 页说明，待用户判断。
- WebSearch 工具在本次任务中多次返回"no access"风格占位回复，融资和投资方信息未能进一步交叉核实。
