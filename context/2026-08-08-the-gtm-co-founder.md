---
product: "The GTM Co-Founder"
slug: "the-gtm-co-founder"
date: "2026-08-08"
rank: 1
votes: 0
comments: 1
category: "开发者工具"
subcategory: "GTM / 营销 Agent Skills"
tags: ["Open Source", "Agent Skills", "GTM", "Marketing", "dev-tool", "Claude", "Playbook", "MIT"]
tech_stack: ["Markdown", "Agent Skills", "Claude Code", "Node.js (npx skills)"]
platform: ["Claude Code", "Cursor", "Codex", "Windsurf", "Antigravity", "任何 Agent Skills 兼容 agent"]
open_source: true
license: "MIT"
business_model: "开源免费"
pricing_start: "免费"
funding_stage: "未查到（无融资信息）"
funding_amount: ""
related_products: ["copy.ai", "Marketing Strategy Generator", "MakerBox", "Elsa by M1-project"]
maker_previous: ["Shane O'Connor：The DevTool GTM Company / QC Growth 创始人，Founding AE 与 GTM advisor 背景（PH 描述自述）"]
archived_at: "2026-08-08"
sources_count: 3
---

# The GTM Co-Founder · 扩展阅读上下文

> PT 2026-08-08 Product Hunt 榜单第 1 · 👍 未查到（archive 显示 0） · 💬 1  
> 归档日期 2026-08-08 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | The GTM Co-Founder |
| 英文 tagline | Open-source GTM skills for technical founders |
| 中文 tagline | 面向技术创始人的开源 GTM skills |
| 官网 | https://gtmcofounder.com/ |
| PH 页 | https://www.producthunt.com/products/the-gtm-co-founder |
| 品类标签 | Open Source · Marketing · Developer Tools（PH 页面分类：Sales enablement） |
| 票数 / 评论 | PH 页面访问时未显示 upvote 数（按钮仅显示 Upvote）；archive 👍 0 / 💬 1；68 followers |
| 公司主体 | The DevTool GTM Company（官网版权行 2026） |
| 企业版/关联站点 | GitHub AIDevGTM/gtm-cofounder、X @thegtmcofounder、LinkedIn linkedin.com/in/devtoolgtm |

## 是做什么的（如实复述，不评价）

一套开源的 GTM（Go-to-Market）Agent Skills，面向单打独斗的技术型 dev-tool 创始人。核心流程：先问一遍问题（约 15 分钟 intake），agent 据此生成一份排好优先级的 GTM 路线图，落地为 `docs/gtm-cofounder/founder-brief.md` → `docs/gtm-cofounder/gtm-roadmap.md`，输出"一个 Now、一个 Next、一个 park 到 Later"的行动项。共 14 个 markdown playbook skill，覆盖定位、首批用户、发布、定价、创始人销售、内容等。

官网定位语："Your agent is too nice. Just like the team around you. This is the GTM co-founder that says what they won't."（你的 agent 太客气了，就像你身边的人一样。这是那个敢说他们不敢说的话的 GTM co-founder。）

## 解决什么问题（事实层面，不判断值不值得解）

- 创始人论坛帖（Shane O'Connor 5 天前发布，"You can build anything. Then nobody comes. Anyone else?"）描述的痛点：技术创始人投入时间金钱做出世界级产品，发布后却无人问津。
- 官方列举的问题：定位模糊（"for developers" 不是客户）、landing page 糟糕导致没人看懂产品在做什么。
- PH 描述原话："Most AI hands dev-tool founders the same generic sales and marketing advice. The GTM Co-Founder doesn't."（大多数 AI 给 dev-tool 创始人同样的通用销售营销建议，它不这样。）
- 目标场景：技术创始人独自 building，需要带优先级、可执行的 GTM 路线图，而非通用建议。

## 怎么做的（技术原理/机制，事实层面）

- 全部内容为 markdown playbook + SKILL.md；每个 skill 包含"真实阈值（非原则）、决策树、看起来合理但悄悄杀死你的错误、真实案例、30 分钟可跑的 checklist"。
- 14 个 skill 分组：Setup（start-here、strategy-and-roadmap）、Gate（review-the-work）、Audience（who-is-this-for、talk-to-users）、Messaging（positioning-and-story、beyond-the-wrapper、value-prop-that-converts、the-homepage）、First users（time-to-first-value、first-50-users、launch-it、market-to-devs-sell-to-buyers、pricing、founder-led-sales）、Sustaining（founder-led-content、know-if-its-working、market-scan）。
- 4 种安装路径：零配置把 skill 文本粘贴进任意聊天 bot；从 latest release 下载 zip 放进 Claude apps 或 `~/.claude/skills/`；clone 仓库后粘贴 prompt；正规安装 `git clone` + 复制到 `~/.claude/skills/`、Claude Code plugin 命令（`/plugin marketplace add AIDevGTM/gtm-cofounder`）、或 `npx skills add AIDevGTM/gtm-cofounder`。
- 兼容 Claude Code、Cursor、Codex、Windsurf、Antigravity 及任何 Agent Skills 兼容 agent。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Shane O'Connor（@gtmnerd；GitHub AIDevGTM；LinkedIn devtoolgtm），The DevTool GTM Company 与 QC Growth 创始人；PH 描述自称有 Founding AE 与 GTM advisor 经历 | PH/GitHub/官网 |
| 顾问 | Adam Frankl（The Developer-Facing Startup）、Jakub Czakon（markepear.dev）——playbook 由二人打磨 | GitHub README |
| 压测用户 | Lubos（hey/api）、Thibault & Max（OpenStatus） | GitHub README |
| 融资 | 未查到 | — |

## 定价 / 商业模式

- 免费、MIT 开源（"MIT, free to use, fork, and distribute."）。
- 无付费层、无付费数字；变现方式未查到。

## 关联信息 / 生态

- GitHub 仓库：54 stars / 6 forks / 43 commits；语言主要为 markdown；含 `.claude-plugin/`、`skills/`、模板（founder-brief.template.md、gtm-roadmap.template.md）、AGENTS.md、CONTRIBUTING.md。
- PH Built With：Granola、Tella、Claude by Anthropic。
- PH Similar Products：copy.ai、Pythia World (Retired)、Elsa by M1-project、MakerBox、Marketing Strategy Generator。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026 | 项目创建（GitHub © 2026、官网版权 2026） |
| 2026-08-08 | PH 当日榜第 1；GitHub 最新 release 存在 |

## 评论区反馈（事实摘录，不评价）

- @fmerian（hunter，"If you're in dev tools, @fmerian is a great Hunter to ask."）：3 天前评论 "appreciate for the mention, @gtmnerd! enjoy the launch, keep up the great work"。
- 创始人论坛帖 "You can build anything. Then nobody comes. Anyone else?"（5 天前，2 comments / 6 upvotes）——描述技术创始人发布后无人问津的处境。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/the-gtm-co-founder（拿到 tagline、描述、maker、hunter、Built With、similar products、followers、论坛帖）
- 官网：https://gtmcofounder.com/（拿到定位、5 问流程、MIT、安装方式、GitHub/LinkedIn）
- GitHub：https://github.com/AIDevGTM/gtm-cofounder（拿到 MIT、54★/6 forks/43 commits、14 skills 清单、安装路径、顾问/压测用户）

## 未查到 / 待补

- 确切票数（PH 页面未显示 upvote 计数）
- Shane O'Connor 完整个人履历（教育/过往公司）
- 用户数、使用量、营收等任何数字
- 是否有付费版规划
