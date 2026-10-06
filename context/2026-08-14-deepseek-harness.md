---
# 结构化元数据（用于索引和聚合）
product: "DeepSeek Harness"
slug: "deepseek-harness"
date: "2026-08-14"
rank: 7
votes: 102
comments: 1

# 分类标签
category: "AI agent"
subcategory: "开源agent运行时框架"
tags: [开源, 插件化, DeepSeek, Claude Code竞品, 命令行]

# 技术信息
tech_stack: [TypeScript, "Cordis 插件框架"]
platform: [CLI, Web]
open_source: true
license: "MIT"

# 商业信息
business_model: "开源免费"
pricing_start: "免费（配合 DeepSeek API 或其他模型使用，API 另计费）"
funding_stage: "不适用（DeepSeek 官方项目）"
funding_amount: ""

# 关联信息
related_products: ["Claude Code", "Munder Difflin", "Hoplite"]
maker_previous: []

# 速览信号
key_signals:
  - "DeepSeek官方开源项目，MIT协议，定位为Claude Code的免费开源替代品，dsh命令行工具"
  - "核心设计理念\"一切皆插件\"：模型、工具、技能、会话、沙箱、文件系统、循环、编排、UI全部可替换可扩展，底层基于Cordis插件框架"
  - "2026年8月13日发布v0.1开发者预览版，上线数小时内GitHub star突破2.7万"
  - "内置4种运行模式：标准编码agent模式、PTC模式（模型可编写TypeScript程序调用工具）、Minimal模式（仅持久化Bash+文件编辑）、Creative模式（实时检视运行时、试验插件）"

# 元信息
archived_at: "2026-08-14"
sources_count: 3
---

# DeepSeek Harness · 扩展阅读上下文

> PT 2026-08-14 Product Hunt 榜单第 7 名 · 👍 102 · 💬 1
> 归档日期 2026-08-14 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | DeepSeek Harness |
| 英文 tagline | Composable agent harness where everything is a plugin |
| 中文 tagline | 一切皆插件的可组合 agent 运行时 |
| 官网 | https://deepseek.com/harness/en/ |
| PH 页 | https://www.producthunt.com/products/deepseek |
| 品类标签 | Open Source / AI / Development |
| 票数 / 评论 | 102 / 1 |
| 公司主体 | DeepSeek（深度求索） |
| 企业版/关联站点 | GitHub: deepseek-ai/deepseek-harness |

## 是做什么的（如实复述，不评价）

DeepSeek Harness（命令行简称 dsh）是 DeepSeek 官方发布的开源 agent 运行时框架，即把一个语言模型变成能读文件、跑命令、执行多步任务的"agent"所需要的运行时外壳。它于 2026 年 8 月 13 日以 v0.1 开发者预览版形式开源，基于 TypeScript 编写，底层使用名为 Cordis 的插件化框架，官方将其定位为"Claude Code 的免费开源替代品"，可通过 `npx @deepseek-ai/dsh web` 直接启动。

## 解决什么问题（事实层面，不判断值不值得解）

- 现有主流编码 agent（如 Claude Code）的模型、工具、编排逻辑通常是固定绑定的一整套，开发者难以替换单个组件
- 开发者想要自定义/试验 agent 运行时的某一层（比如换沙箱、换文件系统实现、换编排策略）时缺少统一可插拔的框架
- 想要一个开源、免费、可自托管的编码 agent 运行时，而非依赖闭源商业产品

## 怎么做的（技术原理/机制，事实层面）

- 核心设计原则"Everything is a plugin"：模型、工具、技能（skills）、会话（sessions）、沙箱（sandboxes）、文件系统、循环（loops）、编排（orchestration）、用户界面全部作为可替换插件，而非写死在一个agent里
- 底层基于 Cordis 插件框架
- 内置四种运行模式：Standard Mode（全功能编码 agent）、PTC Mode / Programmatic Tool Calling（让模型编写 TypeScript 程序来调用工具）、Minimal Mode（仅提供持久化 Bash shell 和文件编辑工具）、Creative Mode（可实时检视运行时状态、试验 Cordis 插件，用于快速原型开发）
- MIT 协议开源，代码托管于 github.com/deepseek-ai/deepseek-harness

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | 不适用，DeepSeek（深度求索）官方项目 | - |
| 融资 | 不适用/待补（DeepSeek 公司层面融资未在本次搜索中核实） | - |
| 投资方 | 未查到/待补 | - |
| 加速器 | 不适用 | - |
| 合规认证 | 未查到/待补 | - |

## 定价 / 商业模式

Harness 本身开源免费（MIT）。同期 DeepSeek 发布了 V4-Pro 模型的 API，报道提及该 API 定价高于此前版本，但具体数字未在本次搜索中核实，属"未查到/待补"。使用 Harness 搭配的模型若走 DeepSeek API 则按 API 用量另计费。

## 关联信息 / 生态

- 上线数小时内 GitHub star 突破 27,000（数据来自搜索时点的媒体报道，可能已变化）
- 媒体报道明确将其定位为"Claude Code 的开源免费替代品"（VentureBeat、The New Stack 等多家科技媒体报道）
- 生态已有社区项目 awesome-deepseek-harness 收录周边插件、工具、基础设施
- 与同榜的 Munder Difflin（本地多智能体 harness，包装多家闭源 CLI）、Hoplite（云端部署编码 agent）同属"编码 agent 基础设施"赛道，DeepSeek Harness 的差异化在于开源、插件化架构本身，而非多 agent 编排或云端部署

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-08-13 | DeepSeek Harness v0.1 开发者预览版开源发布，同期发布 V4-Pro API |
| 2026-08-13（发布数小时内） | GitHub star 突破 27,000 |

## 评论区反馈（事实摘录，不评价）

- 未查到 PH 评论区具体内容/待补（WebFetch 访问 PH 页面受限，且该产品仅 1 条评论）

## 信息来源

- PH 产品页：https://www.producthunt.com/products/deepseek（标题、tagline，正文因访问受限未抓取）
- 官网：https://deepseek.com/harness/en/（因访问受限，信息来自搜索摘要）
- GitHub：https://github.com/deepseek-ai/deepseek-harness（MIT 协议、README 概况，来自搜索摘要）
- 公开报道：VentureBeat「DeepSeek Harness launches as open source rival to Claude Code」、The New Stack「DeepSeek open sources an agent harness where everything is a plugin」，均来自搜索摘要

## 未查到 / 待补

- DeepSeek V4-Pro API 具体定价数字
- Harness 项目的核心贡献团队/负责人姓名
- PH 评论区具体问答内容
- Harness 与 DeepSeek 主站模型账号体系的具体绑定关系
