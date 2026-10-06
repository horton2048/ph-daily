---
product: "Weave Router 2.0"
slug: "weave-router-2"
date: "2026-09-16"
rank: 1
votes: 229
comments: 25
category: "开发者工具"
subcategory: "模型路由器"
tags: ["Open Source", "Developer Tools", "Artificial Intelligence"]
tech_stack: ["Go", "TypeScript", "PostgreSQL"]
platform: ["API", "CLI"]
open_source: false
license: "Elastic License 2.0（源码可见）"
business_model: "按用量收费"
pricing_start: "路由成本的5%"
funding_stage: "未核实"
funding_amount: "未查到"
related_products: ["Claude Code", "Codex"]
maker_previous: []
key_signals: ["按请求复杂度选择模型", "切换收益需超过重建缓存成本", "支持已有订阅的额度感知路由"]
archived_at: "2026-09-17T00:14:58"
sources_count: 3
---

# Weave Router 2.0 · 扩展阅读上下文

> PT 2026-09-16 第 1 · 👍 229 · 💬 25。当日快照，未结榜。

## 基本信息

| 字段 | 内容 |
|---|---|
| 英文 tagline | Subscription aware coding agent router (GPT-6 Intelligence) |
| 中文 tagline | 按复杂度、缓存成本和剩余额度路由编码模型 |
| 官网 | https://weaveos.com/blog/introducing-weave-router-2-0 |
| PH | https://www.producthunt.com/products/weave |
| 品类 | 模型路由器 |

## 是做什么的

面向编码代理的模型路由层，在不同供应商模型之间选择，并考虑用户已有订阅的剩余额度。

## 解决什么问题

每一步都用高价模型成本高，频繁切换又可能丢失缓存收益。

## 怎么做的

官方发布文介绍逐请求复杂度评分、缓存感知切换与遇难升级；当前仓库README强调per-action路由，且提交摘要出现移除struggle escalation routing。升级机制可能随版本或部署而变，本次未逐行审计，不作为已确认通用能力。供应商订阅可用性也受模型及认证方式限制。

## 团队 / 背景 / 融资

发布文章署名Andrew Churchill；PH资料标YC W25，本次未核实融资金额与完整创始团队。

## 定价 / 商业模式

官方发布文章列个人和初创团队收取路由成本的5%；模型和供应商订阅费用不能视为已包含。可托管或自行部署，具体商业条款以官方为准。

## 关联信息 / 生态与核验边界

许可证为Elastic License 2.0，属于源码可见，不直接称OSI开源。所谓与Astra同水平、半价和两倍速度来自厂商基准；文章说明每任务两次尝试，与要求至少五次的正式榜单不可直接对比。

## 技术时间线

2026-09-09：官方介绍Router 2.0。2026-09-16：本次PH上榜。

## 评论区反馈

已取得官方API评论数，但未取得本次发布的完整评论及回复，不将评论数当作满意度证据。

## 信息来源

- [PH发布信息（官方API）](https://www.producthunt.com/products/weave)
- [官方产品/文档/目录资料](https://weaveos.com/blog/introducing-weave-router-2-0)
- [官方产品/文档/目录资料](https://github.com/weave-os/router)

## 未查到 / 待补

- 独立使用测试、付费结算与本次评论区逐条核验未完成。
- 未有来源支持的融资、用户规模、性能及安全保证不作推断。
- 公开仓库已确认，但Elastic License 2.0属于源码可见；部署版本与发布文中的升级策略差异待进一步核验。
