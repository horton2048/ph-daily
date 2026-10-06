---
product: "Modeinspect"
slug: "modeinspect-1-0"
date: "2026-09-10"
rank: 8
votes: 98
comments: 7

category: "设计工具 / AI 设计 / 开发工具"
subcategory: "代码库内 AI 设计画布（design-to-PR）"
tags: ["Canvas", "AI 设计", "Design-to-Code", "Figma 替代", "设计系统 1:1", "Design QA", "PR 自动化", "TypeScript", "React", "SOC 2", "Acreom inc"]

tech_stack: ["Next.js (官网前端)", "Mintlify (docs)", "TypeScript", "React", "Tailwind/CSS tokens", "AI 设计生成（具体模型未披露）"]
platform: ["Web (app.modeinspect.com)", "macOS / Windows / Linux（浏览器）"]
open_source: false
license: "闭源；docs 仓库使用 MIT"

business_model: "Freemium + 订阅 + 企业定制（Hobby 免费 → Pro $20/月 → 企业定制）"
pricing_start: "$0/月（Hobby，无需信用卡） / $20/月（Pro，无 token 计费）/ 企业 Custom"
funding_stage: "未披露机构轮次；公司页公开 4 位个人/operator 投资人"
funding_amount: "未披露"

related_products: ["Figma", "v0 (Vercel)", "Lovable", "Bolt.new", "Cursor", "Replit", "Galileo AI", "Visily", "Figma Make", "CodeSandbox", "Bricks (设计系统 1:1)"]
maker_previous: []

key_signals:
  - "定位是「AI-native Figma」，但形态是画布坐在真实 codebase 之上——组件、tokens、状态、breakpoints 全部读自产品自身的库，不是出图导出代码"
  - "商业模式明确做反 AI app builder：'no tokens, no usage meters'——$20/人/月 flat，不按生成量计费（区别于 v0/Lovable 的 credit 制）"
  - "Prelude 案例给出硬数字：idea → merged PR 从 ~31 天降到 13 天，handoff 从 5+ 降到 1，95% 输出复用现有组件/0 硬编码值——主打「设计师自己开 PR」，把 engineering review 留在 critical path"
  - "PH tagline 写「99 Days Free AI Credits」但定价页只是「$0/mo Hobby 无信用卡」——「99 天」更像 PH 上线期的免费试用 framing 而非常驻机制"
  - "公司主体是「Acreom inc」——同主体下还有一个开源 dev PKM 产品 Acreom（个人知识库 + Jira/GitHub/Linear 集成），两产品共享公司壳"

archived_at: "2026-09-10"
sources_count: 5
---

# Modeinspect · 扩展阅读上下文

> PT 2026-09-10 Product Hunt 榜单第 8 · 👍 98 · 💬 7
> 归档日期 2026-09-10 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Modeinspect（站内文案有时简称「Mode」） |
| 英文 tagline | 99 Days Free AI Credits - Design product UI in your codebase |
| 中文 tagline | 在你自己的代码库里设计产品 UI，前 99 天 AI credits 免费 |
| 官网 | https://modeinspect.com |
| App | https://app.modeinspect.com |
| 社区 | https://go.modeinspect.com/community |
| PH 页 | https://www.producthunt.com/products/modeinspect-1-0 |
| GitHub | https://github.com/modeinspect |
| 品类标签 | Design Tools · Developer Tools · Artificial Intelligence |
| 票数 / 评论 | 98 / 7 |
| 公司主体 | Acreom inc（官网 footer © 2026 Acreom inc） |
| 关联站点 | /pricing · /enterprise · /about · /customers/prelude · /v2 |

## 是做什么的（如实复述，不评价）

一个**坐在你真实代码库之上的 AI 设计画布**：把产品的 components / design tokens / 状态 / breakpoints / 真实数据当成画布的「素材」，让设计师在这张画布上做原型、做 Design QA、再以 **merge-ready PR** 的形式直接提交到 GitHub。

核心动作分三条工作流（站内有原话）：Prototyping / Design QA / Ship PRs。每一步都在**同一个 codebase 上**进行，不出静态稿，不写规格文档，不重画组件——画布里出现的就是产品本身。

画布支持把生产环境里的真实路由拖进来（"Capture to canvas"），所见即真实路由渲染；改画布上的内容，会回写成对 codebase 的 PR，diff 是 scoped 的、type-safe 的，复用现有组件和 token，不写平行设计系统。

## 解决什么问题（事实层面，不判断值不值得解）

- **设计—工程的反复翻译**：站内的数字：传统 handoff 链从设计到 ship 平均 **45+ 天**；用 Mode 是 **~10 天**；Prelude 案例具体到 **31 天 → 13 天**
- **设计稿漂移**：Figma 里的 mock 组件和真实组件总会偏离，画布直接读产品组件库就消除了这个问题（"Components 1:1"）
- **设计系统被绕开**：AI 生成代码常硬编码颜色/数字/新组件，Mode 强制走现有 tokens 和组件库（"Tokens, enforced" / "No generated UI debt"）
- **设计 QA 永远在最后**：传统流程在「build 完之后」做 design QA，Mode 把 design QA 提到「PR 合并之前」（Prelude 案例：Design QA 被移出 critical path）
- **设计师起手难**：传统要求设计师配本地 dev 环境，Mode 让设计师"Connect the codebase, open the product, and start designing from real routes, states, components, and tokens"，无需本地 dev 机器

## 怎么做的（技术原理 / 机制，事实层面）

- **画布层**：浏览器内的可视化设计画布，组件 / frame 可拖拽、设 breakpoint（sm/md/lg 并排 reflow）
- **代码库感知**：连上 GitHub repo 后，工具读产品的 file layout、components、design tokens、conventions、existing logic
- **设计 token 强制**：所有颜色 / 间距 / 文字样式都从产品 token 库取，画布里放不进去"系统外"的东西（"Nothing off-system can sneak in"）
- **真实状态建模**：hover / focus / error / empty / loading / success 等动态状态在真实组件上编辑，不是静态 placeholder
- **真实数据接入**：Prototype 跑在真实数据上（"long names, empty states, the messy edge cases"）
- **AI 探索**：用"最新的 AI 模型"探索 variants / 调整 copy / 套设计方向（站方措辞，未点名模型）
- **代码生成输出**：写出的代码 scoped、type-safe、复用现有组件/token；props/state/events/data shape 对照产品代码检查（不是从 mockup 猜）
- **PR 闭环**：design → code → PR → engineering review & merge，工程 review 仍把守合并门槛
- **部署形态**：Web 应用（app.modeinspect.com），官方未披露 VS Code / JetBrains 插件；GitHub 仓库里看到的是 docs（Mintlify）+ 几个公开 starter 代码模板（open-react-template、kiwi-blank-codebase、mui-blank-codebase、sample）

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 公司主体 | Acreom inc | 官网 footer "© 2026 Acreom inc" |
| 关联产品 | Acreom（开源 dev PKM 工具：Jira/GitHub/Linear/Google Calendar 集成的 markdown 知识库） | acreom.com |
| 创始人 | **未披露**（/about 页只列 investors/operators，未列 maker 名单） | — |
| 团队规模 | 未披露 | — |
| 工作方式 | "Office-first"（/about 页明示） | /about |
| 投资人/operator | Jude Gomila、Fredrik Björk、Michal Vasko、Jozef Képesi（"quietly on the cap table, loudly in the group chat"） | /about |
| 机构轮次 | 未披露 | — |
| 合规 / 认证 | SOC 2 Type II（独立审计）· 审计日志可导出 · 数据驻留可选 · SSO/SAML · SCIM · RBAC | /enterprise |

## 定价 / 商业模式

> PH tagline 写「99 Days Free AI Credits」，但 `/pricing` 页没有写 99 天的限制——Hobby 直接是 `$0/mo`，无信用卡可用。99 天看起来是 PH 上线期间的免费试用 framing。

| 计划 | 价格 | 关键能力 |
|---|---|---|
| **Hobby** | **$0 / 月** | 完整画布、无限连接 repo、个人项目的月度 agent 上限、无需信用卡 |
| **Pro** | **$20 / 人 / 月** | 扩展 agent 上限、按人 flat（**no tokens, no usage meters**）、merge-ready PR、design QA live product、优先支持 |
| **Teams & Enterprises** | **Custom** | 全员 Pro、定价随 seat 和 usage 走、SSO/SAML + SCIM + SOC 2 Type II、centralized billing、dedicated contact |

**模式上值得记的几点**：
- 明确做反 AI app builder：**不按 token / 不按 usage 计费**，按人头 flat
- 把"Design QA"作为独立价值层放进 Pro plan（不只是出图）
- Enterprise 把 SOC 2 / SSO / SCIM / 数据驻留 / RBAC 写成 day-one 默认能力（"on day one, not on a roadmap"）

## 关联信息 / 生态

- **vs Figma**：站内原话——"Figma can still be useful for blank-page exploration and early concepts"，Mode 定位为「live product 上做高保真」的接力者，不替代 Figma 的早期探索
- **vs v0 / Lovable / Bolt.new**（AI app builder）：定位明确区隔——这些工具是「从 0 生成新应用」，Mode 是「在已有 codebase 上做 UI 改动并开 PR」。首页 FAQ "Is this just another AI app builder?" 间接承认常被这样问
- **vs Cursor / Replit**（AI 编码工具）：方向不同——Cursor/Replit 面向工程师在 IDE 里写代码；Mode 面向设计师在画布上做改动、产出 PR
- **客户引用**：Prelude（Series A $27M，20VC/Singular/Seedcamp 投资，客户 BeReal/Suno/Voodoo）· Kiwi.com · Moss · NCCER
- **PH 关键词**（meta tag）：design tool, AI design, design engineering, design engineer, design system, design QA, prototyping, design to code, Figma alternative, production design
- **同类产品候选（待 PH 页解封后核对）**：未拿到 PH 「similar products」位，从功能定位推测包括 Figma、Figma Make、v0、Lovable、Bolt.new、Galileo AI、Visily、Bricks、Cursor、Replit

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-09-10 | PH 上榜（slug `modeinspect-1-0`，按命名推断为 v1.0 上线） |
| 2026-09-10 | 归档日，`/pricing` 当前版本已是 $0 / $20 / Custom |

> 官网 changelog / 完整里程碑本次未取回。

## 评论区反馈（事实摘录，不评价）

> PH 页本次抓取被 Cloudflare 拦截（curl + WebFetch 均返回 challenge），7 条评论的具体内容**未拿到**，下列只列**站外 / 公开材料**中创始人侧和客户的直接陈述（标注来源，不评价）。

- **Quentin Le Bras（Prelude 首席产品与设计官，官网首页引用）**："My designers explore on our actual codebase, with real data, and open the PR themselves. We go from idea to a merged PR without a handoff in between — that's a superpower, not a workflow."
- **Guillaume Fiette（Prelude 工程，Prelude 案例页引用）**："I was skeptical going in, everyone's seen AI slop end up in a codebase. Modeinspect lets our design team build what they have in mind while respecting our conventions and design tokens. It gives us a solid starting point to take over from, and it cut a lot of the back-and-forth between design and engineering."
- **Martin MJ Jancik（Kiwi.com 产品设计经理，官网首页引用）**："Modeinspect integrates seamlessly with our codebase and design system, which is exactly what we have been looking for in AI design tools. It enables iteration on top of an already complex product."
- **Tereza Reznickova（Moss Principal PM，官网首页引用）**："Modeinspect is the first AI tool that respects our design system 1:1. It allows us to create production-like prototypes, which makes our whole team faster."
- **Christian Bistany（NCCER UX Designer，官网首页引用）**："The biggest value add was being able to make changes in real time, using our design system, and immediately pushing the changes to code for senior devs to review and merge."

## FAQ（首页公开 Q&A 摘录，事实层面）

> 站内 FAQ 标题是 "Design Engineers ask before they switch"，答案从 Next.js 注入的 JSON 里提取，原文。

- **Do I need a dev environment to use Mode?**  
  No. Mode lets designers work on the product without setting up a local dev machine. Connect the codebase, open the product, and start designing from real routes, states, components, and tokens.
- **Where does Mode fit with Figma?**  
  Figma can still be useful for blank-page exploration and early concepts.
- **What do I get out of Mode: prototype or code?**  
  Both — 在真实 codebase 上跑的真实 prototype，并能作为 merge-ready PR 提交
- **Does Mode work with our existing components and design system?**  
  Yes. Mode is built around the system your product already uses: components, tokens, states, breakpoints, data, and code.
- **What if the screen I need is behind auth, mid-flow, or in a weird state?**  
  （答案文本未在抓取片段中完整取回）
- **Is this just another AI app builder?**  
  （答案文本未在抓取片段中完整取回）
- **How does engineering stay involved?**  
  Yes（工程师仍是 review / merge 的把关者）。"Instead of translating static frames into product decisions, the team works from something much closer to the thing that will actually ship."
- **Can I use Mode just for design QA and polish?**  
  Yes. Mode is for the moment when design needs to touch the real product: existing screens, components, states, data, breakpoints, and flows.

## 信息来源

- **官网首页**：https://modeinspect.com （拿到 hero · 8 张 feature cards · 4 张 code-output cards · 3 workflows · 4.5× 数据 · 8 条 FAQ · 客户引用 · footer 公司主体 "Acreom inc" · OG / Twitter meta · 关键词标签）
- **官网 /pricing**：https://modeinspect.com/pricing （拿到 Hobby $0 / Pro $20 / Enterprise Custom 三档、no tokens/no usage meters、6 条 FAQ）
- **官网 /enterprise**：https://modeinspect.com/enterprise （拿到 7× faster QA / 80% less eng time / >50% less handover / 90% production code / SOC 2 Type II / SSO/SAML / SCIM / RBAC / data residency）
- **官网 /about**：https://modeinspect.com/about （拿到 mission · 三原则 · investor/operator 名单：Jude Gomila / Fredrik Björk / Michal Vasko / Jozef Képesi · Careers）
- **官网 /customers/prelude**：https://modeinspect.com/customers/prelude （拿到完整 Prelude 案例：13 天数字、31 天对比、5+ handoff → 1 handoff、95% 复用组件 / 0 硬编码值、Prelude 公司信息 Series A $27M / 客户 BeReal/Suno/Voodoo / 投资方 20VC/Singular/Seedcamp、Quentin + Guillaume 双引用）
- **GitHub org**：https://github.com/modeinspect （拿到 3 followers、5 个公开仓库：docs、open-react-template、sample、kiwi-blank-codebase、mui-blank-codebase；推断 starter 模板矩阵覆盖 React、MUI、Kiwi.com 代码库集成）
- **PH 产品页**：https://www.producthunt.com/products/modeinspect-1-0 （**未取回**——curl 与 WebFetch 均被 Cloudflare challenge 拦截，7 条评论内容缺失；PH 提供的仅有 tagline / 票数 / 评论数 / 品类标签 / logo URL）

## 未查到 / 待补

- **PH 评论区 7 条**（Cloudflare 拦截）：用户提问、创始人回复全部缺失
- **创始人/CEO 姓名**：PH makers 列表未抓到，/about 页只列投资人/operator 不列 maker
- **机构融资轮次**：仅披露 4 位个人/operator 在 cap table，是否有 VC 轮未提
- **支持的 framework 范围**：仅从 UI 代码示例确认 React（cn()、Next.js 风格 import）、MUI；从 `mui-blank-codebase` 仓库名确认支持 Material UI；**Vue / Svelte / Angular / Tailwind 纯项目 / SwiftUI 等支持情况未披露**
- **VS Code / JetBrains 插件**：未在官网 / pricing / docs 看到任何 IDE 插件入口；当前定位是 Web app
- **"99 Days Free AI Credits" 的精确机制**：定价页 Hobby 直接 $0/mo、无天数限制，"99 天"可能是 PH 上线期的一次性 promo，文案本身含糊
- **AI 模型的选用**：站方只写 "latest AI models"，未点名 Claude / GPT / Gemini / 自研
- **企业版定价区间**：Custom，无公开 seat 价格或最小合约
- **代码托管的具体集成范围**：仅见 GitHub，从 demo 推断；GitLab / Bitbucket 集成未提
- **设计系统的具体识别方式**（Storybook / Style Dictionary / Figma Tokens / 自定义格式）未在公开材料说明
- **官网 `/v2` 路径存在但内容未抓到**（与 PH slug `-1-0` 命名是否相关未确认）
- **完整 changelog**：未抓取到具体版本里程碑
- **付费转化数据 / ARR / 客户数**：未披露
