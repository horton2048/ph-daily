---
product: "HarnessRouter Community Edition"
slug: "harnessrouter"
date: "2026-08-16"
rank: 3
votes: 135
comments: 16

category: "开发者工具"
subcategory: "AI agent 基础设施 / 工具接口"
tags: ["开源", "Apache-2.0", "Agent", "Claude Code", "Codex", "MCP", "YC"]

tech_stack: ["Docker", "OpenAPI 3.1", "JSON Schema"]
platform: ["CLI", "Docker", "API"]
open_source: true
license: "Apache-2.0"

business_model: "开源免费 + Cloud 托管"
pricing_start: "免费（Community Edition）"
funding_stage: "已融资（Epsilla，YC S23）"
funding_amount: ""

related_products: ["Codex", "Claude Code", "Hermes", "MCP"]
maker_previous: ["Epsilla", "ClawTrace", "SwarmStack"]

key_signals:
  - "Apache-2.0 开源统一 agent harness 接口，一个 API 接入 Codex/Claude Code/Hermes，换后端不改应用"
  - "Unified Harness Protocol (UHP)：OpenAPI 3.1 + JSON Schema，47 项一致性检查，类似 LSP 的能力协商"
  - "全栈（Gateway/Runner/Console）打成一个 Docker 容器；CE 与 Cloud 实现同一协议，本地→云是选择不是强制迁移"
  - "Epsilla（YC S23）出品，Richard Song / Kuanze Ma；称 agent 功能交付从数周缩到数小时"

archived_at: "2026-08-16"
sources_count: 1
---

# HarnessRouter Community Edition · 扩展阅读上下文

> PT 2026-08-16 Product Hunt 榜单第 3 名 · 👍 135 · 💬 16
> 归档日期 2026-08-16 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | HarnessRouter Community Edition |
| 英文 tagline | Open-source unified interface for agent harnesses |
| 中文 tagline | 开源的统一 Agent 工具接口 |
| 官网 | https://github.com/HarnessRouter |
| PH 页 | https://www.producthunt.com/products/epsilla |
| 品类标签 | API · Developer Tools · Artificial Intelligence |
| 票数 / 评论 | 135 / 16 |
| 公司主体 | Epsilla（YC S23） |
| 企业版/关联站点 | HarnessRouter Cloud |

## 是做什么的（如实复述，不评价）

一个开源的统一接口，让产品团队通过单一 API 把多个 agent harness 接入产品。创始人称过去
"每次需要 agent runtime 都要重建同一套后端"，改用现成 harness 后"agent 功能交付从数周
缩到数小时"。当前支持 Codex、Claude Code、Hermes，候选加入 Pi 和 dsh（DeepSeek harness）。

## 解决什么问题（事实层面，不判断值不值得解）

- 每个 agent harness（Codex / Claude Code 等）接口不同，产品层每接一个都要重写后端
- 切换 / 并行多个 harness 需要改应用代码
- agent 会话、流式、文件、artifact、取消、失败处理等横切逻辑重复实现

## 怎么做的（技术原理/机制，事实层面）

- 定义 **Unified Harness Protocol (UHP)**：用 OpenAPI 3.1 + JSON Schema 规范应用与
  harness 的通信，含 47 项一致性检查
- harness 声明自身能力，应用据此 feature-detect——类似 LSP 的能力协商机制
- 协议处理 sessions、streaming、files、artifacts、cancellation 和全部失败处理
- 全栈（Gateway / Runner / Console）打包进**一个 Docker 容器**
- 提供非编码场景 starter kit（PPT、电子表格、BI 仪表盘、视频剪辑）

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Richard Song、Kuanze Ma；launch team 含 Garry Tan | PH 页 |
| 公司 | Epsilla（YC S23），2024 年起多次发布 | PH 页 |
| 融资 | 已融资（YC S23），金额未披露 | — |
| 投资方 | Y Combinator | — |
| 加速器 | Y Combinator S23 | — |
| 合规认证 | 无 | — |

## 定价 / 商业模式

- Community Edition：免费，Apache-2.0 开源
- Cloud 版：托管基础设施 + 可观测性，与 CE 实现同一协议规范
- 强调"从本地迁 Cloud 是选择，不是强制迁移"——集成在两者间不变

## 关联信息 / 生态

- 支持的 harness：Codex、Claude Code、Hermes（候选 Pi、dsh）
- 定位在 harness "上一层"：dsh 这类 DeepSeek harness 可作为被支持的 harness 而非竞品
- 评论区用户称赞 Apache-2.0 选择，对比"近期太多'开源'实为 source-available 带附加条件"

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 本次 | Epsilla 第 5 次发布（前四次：HarnessRouter、ClawTrace、SwarmStack、Epsilla） |

## 评论区反馈（事实摘录，不评价）

- 用户赞 Apache-2.0："太多近期'开源'其实是 source-available 带附加条件"
- 问 composability vs DeepSeek dsh——Richard 答 HarnessRouter 在更上层，dsh 可作被支持的 harness
- maker 征求社区：下一个该支持哪个 harness、抽象在哪里泄漏

## 信息来源

- PH 产品页：https://www.producthunt.com/products/epsilla（WebFetch 拿到协议机制、支持的 harness、
  定价、创始人、评论）
- GitHub：https://github.com/HarnessRouter（PH 页提及开源，license Apache-2.0）
- 公开报道：未单独检索

## 未查到 / 待补

- 具体融资金额
- Cloud 版定价
- GitHub stars 数
