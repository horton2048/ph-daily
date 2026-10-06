---
product: "AgentScore"
slug: "agentscore"
date: "2026-09-23"
rank: 5
votes: 129
comments: 6
category: "开发者工具"
subcategory: "代理质量评分"
tags: ["Open Source", "Developer Tools"]
tech_stack: ["OpenTelemetry", "TypeScript", "Rust", "Python"]
platform: ["Web", "API", "OpenTelemetry"]
open_source: true
license: "平台主仓库MIT；评分范围待核实"
business_model: "Freemium"
pricing_start: "平台免费开始；评分费用待核实"
funding_stage: "未核实"
funding_amount: "未查到"
related_products: ["Latitude", "OpenTelemetry"]
maker_previous: []
key_signals: ["结果、可靠性、成本、速度、安全五维评分", "至少1000个合格生产会话", "证据不足不出分并展示95%置信区间"]
archived_at: "2026-09-24T01:29:41"
sources_count: 4
---

# AgentScore · 扩展阅读上下文

> PT 2026-09-23 第 5 · 👍 129 · 💬 6。当日快照，未结榜。

## 基本信息

| 字段 | 内容 |
|---|---|
| 英文 tagline | Daily score to see if your agent gets better |
| 官网 | https://latitude.so/benchmark |
| PH | https://www.producthunt.com/products/latitude-4 |
| 品类 | 代理质量评分 |

## 是做什么的

Latitude中的生产代理质量评分，将任务结果、可靠性、成本、速度与安全放在同一个评分框架内，并跟踪变化。

## 解决什么问题

只看回答质量、延迟或单次成本，可能掩盖多步任务实际未完成的问题。

## 怎么做的

接入生产会话或OpenTelemetry轨迹；官网要求至少1000个合格session，五维均通过流量、覆盖与置信门槛。使用满足要求的最短7/14/21/28天整周窗口，分数附95%置信区间，证据不足不出分。

## 团队 / 背景 / 融资

官网主体Latitude Data S.L.；相关文章署名César Migueláñez，但不据作者署名认定创始身份。融资未核实。

## 定价 / 商业模式

Latitude主仓库README列免费每月20K credits、30天保留、不限席位；本次未核实AgentScore具体套餐权益或独立附加费。MIT自托管代码不包含基础设施成本。

## 关联信息 / 核验边界

PH称每日更新，含义不是上线第一天就能出分；公开方法仍依赖输入数据覆盖和评估器。官网“端到端加密”描述实际列传输和静态加密，未据此推断服务器无法读取。

## 技术时间线

2026-09-23：本次PH上榜；上榜日期不自动等于首次上线。

## 评论区反馈

已取得官方API评论数，尚未逐条核验完整评论及回复；不将评论数当作满意度证据。

## 信息来源

- [PH发布信息（官方API）](https://www.producthunt.com/products/latitude-4)
- [官方页面 / 文档 / 仓库](https://latitude.so/benchmark)
- [官方页面 / 文档 / 仓库](https://latitude.so/)
- [官方页面 / 文档 / 仓库](https://github.com/latitude-dev/latitude-llm)

## 未查到 / 待补

- 独立使用测试、付款流程和完整用户评论未核验。
- 文中标为未核实的融资、模型实现与套餐条件不作推断。
