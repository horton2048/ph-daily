---
# 结构化元数据（用于索引和聚合）
product: "GrowthBook 5.0"
slug: "growthbook"
date: "2026-08-04"
rank: 11
votes: 114
comments: 0

# 分类标签
category: "开发者工具"
subcategory: "功能开关 / 实验 / 产品分析"
tags: [功能开关, 实验, A/B测试, 产品分析, AI, 数据仓库, 开源, Agent, 治理]
tech_stack: [React, Next.js, Node.js, TypeScript, MongoDB, PostgreSQL, JavaScript SDK, Python SDK, Go SDK]
platform: [Web]
open_source: true
license: "MIT（GrowthBook 主仓库）"

# 商业信息
business_model: "开源 + SaaS 订阅"
pricing_start: "未查到（官方提供免费/付费套餐）"
funding_stage: "未披露"
funding_amount: "未披露"

# 关联信息
related_products: [LaunchDarkly, Statsig, Split, PostHog]
maker_previous: []

# 元信息
archived_at: "2026-08-10T13:06:22Z"
sources_count: 2
---

# GrowthBook 5.0 · 扩展阅读上下文

> PT 2026-08-04 Product Hunt 榜单第 11 · 👍 114 · 💬 未查到  
> 归档日期 2026-08-10 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | GrowthBook（5.0 版本） |
| 英文 tagline | 大规模构建、发布和持续改进（Build, ship, and iterate at scale） |
| 中文 tagline | 大规模构建、发布和持续改进 |
| 官网 | https://www.growthbook.io/ |
| PH 页 | https://www.producthunt.com/products/growthbook |
| 品类标签 | 开发者工具 / 功能开关 · 实验 · 产品分析 |
| 票数 / 评论 | 114 / 未查到 |
| 公司主体 | GrowthBook（公司主体未披露） |
| 企业版/关联站点 | GitHub 开源仓库（growthbook/growthbook） |

## 是做什么的（如实复述，不评价）

GrowthBook 是一个以数据仓库为原生平台的实验与功能发布平台，整合功能开关（feature flags）、实验（A/B 测试）和产品分析三块能力。5.0 版本将这三者统一到一个以 AI 为核心、原生支持数据仓库的平台上：用户可用全新的 AI 可视化编辑器在浏览器中构建无代码实验；代理（agents）可利用 25 种开源技能创建功能标志和草拟实验；应用内 AI 助手可探索产品数据；并声称在更强大的治理保障下安全发布、查询更快、实验流程更简化。官方定位"用于你的团队和你的 agents"。

## 解决什么问题（事实层面，不判断值不值得解）

- 解决功能发布风险：通过功能开关（feature flags）支持自动回滚、灰度发布（ramp schedules + guardrails），让团队在高速发布时保持安全。
- 解决实验门槛：AI 可视化编辑器让无代码构建实验成为可能，降低实验的工程门槛。
- 解决"AI 时代发布加速但失控"的问题：官方定位"AI 编码工具让团队/agents 更快发布，auto-rollbacks 和 ramp schedules 让你仍能安心睡觉"。
- 解决数据洞察链路断裂：产品分析连接所有产品数据，配合 AI Analyst 与 agents 探索数据、发现增长机会。
- 服务规模：官方称被 3000+ 公司采用（如 Dropbox、Khan Academy、TodayTix、Lingokids、Oda 等）；Dropbox 日均 30 亿次功能评估。

## 怎么做的（技术原理/机制，事实层面）

- 5.0 核心新能力：AI 可视化编辑器（浏览器内无代码实验）、25 种开源技能（供 agents 创建功能标志/草拟实验）、应用内 AI 助手（探索产品数据）、更快的查询与更简洁的实验流程、更强的治理保障。
- 数据仓库原生：直接连接数据仓库（Snowflake、BigQuery、Redshift 等）运行实验与分析。
- 技术栈（公开资料）：前端 React + Next.js 管理界面；后端 Node.js + TypeScript RESTful API；数据存储支持 MongoDB、PostgreSQL；多语言 SDK（JavaScript、React、Python、Go、Java 等）。
- 部署模式：云托管、自托管、混合部署。
- 实验机制：用户一致分配追踪、百分比灰度、用户属性定向、时间窗口控制、互斥实验分组；支持复杂目标规则与用户分段。
- 开源：GrowthBook 主仓库为开源项目（MIT 协议，GitHub）。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | 未查到（GrowthBook 开源社区驱动） | — |
| 融资 | 未披露 | — |
| 投资方 | 未查到 | — |
| 加速器 | 未查到 | — |
| 合规认证 | 未查到 | — |

## 定价 / 商业模式

开源 + SaaS。GrowthBook 提供自托管开源版与云托管付费套餐（具体套餐价格未查到）；官方定位仓库原生平台。5.0 版本的具体定价调整未查到。

## 关联信息 / 生态

- 竞品：LaunchDarkly（功能开关）、Statsig、Split（实验/功能管理）、PostHog（产品分析）。
- 客户案例：Dropbox（AI 产品开发 + 日均 30 亿功能评估）、Khan Academy（AI 辅导正确率 +6.1%）、TodayTix（页面浏览提升 24%）、Lingokids、Oda（400+ 实验）等。
- 生态：面向团队与 AI agents 双端；开源仓库 + 25 种开源技能构成 agent 生态。

## 技术时间线（官网里程碑，若有）

未查到（无明确公开版本时间线；5.0 为本期上榜版本）。

## 评论区反馈（事实摘录，不评价）

未查到（PH 评论区不可访问）。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/growthbook（URL 确认，内容被 Cloudflare 拦截）
- CSDN 每日热榜镜像：https://laughingzhu.blog.csdn.net/article/details/163542450（tagline、5.0 中文介绍、票数 🔺114、关键词、发布时间 2026-08-04）
- 官网：https://www.growthbook.io/（产品定位、功能开关/实验/分析三合一、3000+ 公司、客户案例、仓库原生）

## 未查到 / 待补

- GrowthBook 5.0 官方发布公告 / 详细 changelog
- 创始人 / 团队 / 融资信息
- 云托管付费套餐具体价格
- 25 种开源技能的具体清单
- 评论数与评论区内容
- AI 可视化编辑器与 AI 助手背后的模型/技术细节