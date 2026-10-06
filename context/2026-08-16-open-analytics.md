---
product: "Open Analytics"
slug: "open-analytics"
date: "2026-08-16"
rank: 9
votes: 12
comments: 4

category: "开发者工具"
subcategory: "网站分析 / 隐私优先分析"
tags: ["开源", "AGPL", "无 Cookie", "MCP", "隐私优先", "GA 替代"]

tech_stack: ["Neon", "Next.js", "Stripe"]
platform: ["Web", "自托管"]
open_source: true
license: "AGPL"

business_model: "开源免费 + 托管订阅"
pricing_start: "自托管免费 / 托管 $9/月起"
funding_stage: "未披露"
funding_amount: ""

related_products: ["Google Analytics", "Plausible", "PostHog", "Umami"]
maker_previous: ["Sleek Analytics"]

key_signals:
  - "AGPL 开源、无 Cookie 的 GA 替代，一条 script 即用；自托管免费、托管 $9/月起"
  - "隐私设计：salted hash 午夜轮换、不存原始 IP、不跨站画像；GPC 在采集层服务端强制"
  - "AI 原生：MCP server 让 AI 工具自然语言查流量数据 + 内置 AI Chat；自定义事件无需 JS（data-oa-event）"
  - "Stripe 集成把收入归因到具体访问；'每档含全部功能，按量付费而非按功能付费'"

archived_at: "2026-08-16"
sources_count: 1
---

# Open Analytics · 扩展阅读上下文

> PT 2026-08-16 Product Hunt 榜单第 9 名 · 👍 12 · 💬 4
> 归档日期 2026-08-16 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Open Analytics |
| 英文 tagline | AI-native Google Analytics alternative for the modern web |
| 中文 tagline | 面向现代 Web 的 AI 原生 Google Analytics 替代品 |
| 官网 | https://www.producthunt.com/r/4JTFIOB7KPSQ25 |
| PH 页 | https://www.producthunt.com/products/open-analytics-2 |
| 品类标签 | Open Source · Analytics · GitHub |
| 票数 / 评论 | 12 / 4 |
| 公司主体 | 关联 Sleek Analytics |
| 企业版/关联站点 | 托管版 |

## 是做什么的（如实复述，不评价）

一个开源、隐私优先的 Google Analytics 替代，为人与 AI agent 双方设计。用一条轻量无 Cookie
脚本追踪实时访客、漏斗、收入。自托管免费（AGPL），托管版 $9/月起。

## 解决什么问题（事实层面，不判断值不值得解）

- 现有工具逼人在"有用分析"与"隐私"间二选一：GA 数据全但复杂且要同意横幅；隐私替代"只停在页面浏览数"
- 自定义事件需写 JS，接入门槛高
- 收入与流量数据难关联归因

## 怎么做的（技术原理/机制，事实层面）

- **无 Cookie 设计**：访客身份用 salted hash、午夜轮换；不存原始 IP、不跨站画像
- **GPC 强制**：Global Privacy Control 在采集层服务端强制——"即使 snippet 配置忽略，请求也会被丢弃"
- **自定义事件无需 JS**：给元素加 `data-oa-event="signup"` 即自动追踪
- **Stripe 集成**：把收入归因到产生付款的具体访问
- **MCP server**：把分析数据接入 AI 工具，自然语言查流量；内置 AI Chat 用大白话问数据
- 技术栈：Neon（Postgres）、Next.js、Stripe
- 部署：一条 script tag 贴上即刷新看实时流量

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Abbas Aga（@uaghazade，关联 Sleek Analytics）、Rahul Bridge（@rahul_bridge） | PH 页 |
| 融资 | 未披露 | — |
| 投资方 | 无 | — |
| 加速器 | 未查到 | — |
| 合规认证 | 隐私优先架构（无 Cookie / GPC 强制） | PH 页 |

## 定价 / 商业模式

- 自托管：免费（AGPL 开源）
- 托管版：$9/月起，首发"终身 5 折"
- "每档含全部功能，按量付费而非按功能付费"

## 关联信息 / 生态

- 同类：Google Analytics、Plausible、PostHog、Umami
- 差异化：隐私 + 收入归因 + AI 可查询（MCP）三者合一，而非只做页面浏览
- 关联产品：Sleek Analytics（maker 关联）

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 未查到 | — |

## 评论区反馈（事实摘录，不评价）

- Abbas Aga：现有工具逼人二选一，GA 复杂带同意横幅，隐私替代停在页面浏览数
- 四大特性：强制隐私、收入归因、AI 可查询、无代码自定义事件
- Rahul Bridge："一条 script tag：贴上即刷新"

## 信息来源

- PH 产品页：https://www.producthunt.com/products/open-analytics-2（WebFetch 拿到创始人、
  license AGPL、技术栈、隐私机制、MCP、定价、评论）
- 官网：未单独抓取
- 公开报道：未单独检索
- GitHub：开源信号确认（AGPL），未单独查仓库

## 未查到 / 待补

- GitHub stars / 仓库地址
- 融资情况
- 托管版各档具体用量计费
