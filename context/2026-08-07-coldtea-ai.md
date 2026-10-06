---
# 结构化元数据（用于索引和聚合）
product: "Coldtea.ai"
slug: "coldtea-ai"
date: "2026-08-07"
rank: 1
votes: 0
comments: 14

# 分类标签
category: "AI agent"
subcategory: "agentic development environment"
tags: ["AI Coding Agents", "Visual QA", "Production Monitoring", "本地 IDE", "Claude Code", "Codex", "OpenCode"]

# 技术信息
tech_stack: ["未完整披露", "Shell integration", "E2E testing agents", "observability integrations"]
platform: ["Mac", "IDE"]
open_source: false
license: "不适用/未查到开源仓库"

# 商业信息
business_model: "Freemium / 订阅制未披露（PH 显示 Free Options）"
pricing_start: "免费选项（具体额度/付费价未披露）"
funding_stage: "未披露"
funding_amount: "未披露"

# 关联信息
related_products: ["Claude Code", "Codex", "OpenCode", "Cursor", "Playwright", "Sentry", "Linear"]
maker_previous: ["Ohans Emmanuel：曾任 HelloFresh Staff Engineer（PH 自述）"]

# 元信息
archived_at: "2026-08-07"
sources_count: 4
---

# Coldtea.ai · 扩展阅读上下文

> PT 2026-08-07 Product Hunt 榜单第 1 · 👍 未从归档取得 · 💬 14  
> 归档日期 2026-08-07 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Coldtea.ai |
| 英文 tagline | Make your software delivery self-driving |
| 中文 tagline | 让软件交付流程变成自驱动 |
| 官网 | https://www.coldtea.ai/ |
| PH 页 | https://www.producthunt.com/products/coldtea |
| 品类标签 | Software Engineering · Developer Tools · Artificial Intelligence；PH 页面另列 AI Coding Agents、Testing and QA software、AI Code Editors |
| 票数 / 评论 | 归档未记录票数；归档评论 14；PH 页面访问时显示 5.0、1 review、139 followers 与 Free Options |
| 公司主体 | Coldtea（官网未披露注册公司名） |
| 企业版/关联站点 | 官网未查到独立企业版；提供 macOS 下载入口 |

## 是做什么的（如实复述，不评价）

Coldtea.ai 把自己定位为 agentic development environment。它把终端、编码 agent、端到端测试和生产监控放进一个 IDE：编码 agent 负责编写或修改代码，视觉 QA agent 在真实应用里执行测试路径，监控 agent 在上线后观察错误日志、客户反馈、用户会话和 agent traces，并把问题转成后续任务或 PR。

产品强调它不是单独的 dashboard，而是运行在开发者机器上的 IDE，贴近本地 repo、shell、agent 设置和现有开发环境。官网称可与 Claude Code、Codex、OpenCode 等 coding agents 搭配使用。

## 解决什么问题（事实层面，不判断值不值得解）

- Maker Ohans Emmanuel 在 PH 自述，他在 HelloFresh 做 Staff Engineer 时长期关注 post-merge regression 与 production stability；Coldtea 针对的是代码合并后仍可能出现的回归、测试缺口和线上稳定性问题。
- 官网叙述的工作流问题是：编码 agent 可以更快地产生改动，但测试、发布门禁、生产监控和线上问题回收仍分散在不同工具里。
- PH 回复中提到，传统视觉回归容易误报；Coldtea 的 Visual QA 更接近意图测试，例如验证 feed item 的标题、时间戳和点击行为，而不是简单 pixel diff。
- 目标场景包括：让多个 coding agents 并行工作、用自然语言描述 Web/mobile 旅程并转成自愈测试、在 PR preview 上跑完整套件、上线后把 production signal 拉回开发任务。

## 怎么做的（技术原理/机制，事实层面）

- 终端集成：PH maker 回复称 terminal pane 运行用户已有 login shell，zshrc、aliases、PATH、env 会保留；agent 可以读取其他 panes/workspace，上下文可共享。
- 多 agent 协作：官网称可以把任务同步到工程 board，并分配给 background cloud agents；PH 回复提到不同 pane 中的 agents 可以互相发消息。
- 视觉 QA：用户用自然语言描述 Web 或 mobile journey，QA agents 转成 self-healing tests；官网称可在每个 PR preview 上运行完整套件并 gate deployments。
- 生产监控：监控 agents 连接 logging、observability tools、customer feedback、user sessions 与 agent traces；发现问题后调查并打开 PR 或把技术债加入 board。
- 代码数据边界：官网 FAQ 称产品运行在用户机器旁边，不会把代码移出机器；cloud execution 只有在用户打开时才使用。具体加密、审计、权限模型未公开。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 / maker | Ohans Emmanuel | PH maker 自述 |
| 背景 | 曾任 HelloFresh Staff Engineer，关注 post-merge regressions 与 production stability | PH maker 自述 |
| 融资 | 未查到公开融资轮次、金额或投资方 | 官网、PH 页面及公开搜索未查到 |
| 投资方 | 未查到 | 同上 |
| 加速器 | 未查到 | 同上 |
| 合规认证 | 未查到 SOC 2、ISO 27001 等认证信息 | 官网公开页面未列出 |

## 定价 / 商业模式

Product Hunt 页面显示 Free Options；官网可见 macOS 下载入口，但未查到公开 pricing page 的完整档位、付费价格、团队版或企业版条款。产品可能以 IDE 下载、云端 agent 执行或团队功能收费，但公开材料没有足够信息确认。

## 关联信息 / 生态

- Coldtea 处在 AI coding agent 的下游工作流：不是替代 Claude Code / Codex / OpenCode，而是围绕它们补交付、测试、监控和任务流。
- 与传统 IDE 的差异在于把 agentic testing 和 production monitoring 放进同一个开发环境；与传统 QA/observability 工具的差异在于强调 agent 可直接调查、开 PR、回写任务。
- 相关工具方向包括 Cursor、Claude Code、Codex、OpenCode、Playwright、Sentry/Datadog 类 observability、Linear/Jira 类工程 board。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-08-07 | Coldtea.ai 出现在 Product Hunt 当日榜第 1；tagline 为 Make your software delivery self-driving |
| 未查到 | 官网未提供明确版本号、成立日期或公开路线图 |

## 评论区反馈（事实摘录，不评价）

- Ohans Emmanuel（maker）：Coldtea 来源于自己在 HelloFresh 对 post-merge regressions 和 production stability 的经历；希望重新思考完整的 agentic development environment。
- Maker 回复：terminal pane 运行用户已有 shell，保留 zshrc、aliases、PATH 与 env；agents 可以读其他 pane/workspace，并可互相发消息。
- Maker 回复：Visual QA 不是 pixel diff；测试意图更像“feed item title/timestamp 与点击行为仍正确”，动态内容位置变化不应导致失败。
- Maker 回复：任务会保留 description、implementation plan 与 session logs，方便团队和 agent 在同一个上下文里协作。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/coldtea（拿到 tagline、分类、Free Options、maker 背景、terminal/Visual QA 回复、logo）
- 官网：https://www.coldtea.ai/（拿到 IDE 定位、Terminal / Agentic Testing / Self-driving software / Tasks 模块、FAQ、macOS 下载入口）
- 公开报道：截至 2026-08-07 未查到可核实融资报道
- GitHub：未查到 Coldtea 官方公开仓库

## 未查到 / 待补

- 完整定价、免费额度、团队/企业版价格
- 注册公司主体、成立时间、团队规模和所在地
- 融资轮次、金额、投资方、加速器
- 底层模型、数据存储、安全审计、权限模型与第三方集成清单
- Visual QA 的可复现 benchmark、误报率或客户案例
