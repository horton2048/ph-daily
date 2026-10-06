---
product: Web Search API
slug: cloudflare
date: '2026-10-05'
rank: 6
votes: 113
comments: 2
category: 开发者工具
subcategory: AI 联网搜索 API
tags:
- Web 搜索
- AI Gateway
- Zero Data Retention
- BYOK
tech_stack:
- Cloudflare AI Gateway
- Workers AI binding
- REST API
platform:
- API
- Workers
open_source: false
license: ''
business_model: 按用量（供应商标价，无加价）
pricing_start: 每千次 $0.25（Ceramic）/ $5（Linkup）/ $7（Exa）
funding_stage: 上市公司
funding_amount: 不适用
related_products:
- Exa
- Linkup
- Ceramic.ai
- Tavily
maker_previous: []
key_signals:
- 2026-10-02 beta：经 AI Gateway 让 agent 搜实时网页，不再猜 URL 或靠训练截止数据
- 首批三家搜索供应商 Ceramic.ai / Exa / Linkup，均支持零数据保留并遵守 Cloudflare 验证爬虫标准
- 按各供应商标价计入 AI Gateway 额度，Cloudflare 不加价；也可自带 key
- 每千次请求 $0.25（Ceramic，默认）/ $5（Linkup）/ $7（Exa）（ppc.land 报道）
archived_at: '2026-10-05T21:50:00+08:00'
sources_count: 4
---

# Web Search API · 扩展阅读上下文

> PT 2026-10-05 Product Hunt 榜单第 6 · 👍 113 · 💬 2  
> 归档日期 2026-10-05 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Web Search API |
| 英文 tagline | Give AI Agents Access to Live Internet Data |
| 中文 tagline | 让 AI agent 接入实时网页数据 |
| 官网 | https://blog.cloudflare.com/introducing-web-search-api/ |
| PH 页 | https://www.producthunt.com/products/cloudflare |
| 品类标签 | API · Developer Tools |
| 票数 / 评论 | 113 / 2 |
| 公司主体 | Cloudflare |
| 企业版/关联站点 | Changelog https://developers.cloudflare.com/changelog/product-group/ai/ |

## 是做什么的（如实复述，不评价）

Cloudflare Web Search API（beta）让 AI agent 和应用通过 AI Gateway 搜索互联网，用实时信息支撑回答。可用 REST 端点或 Workers 的 env.AI.websearch 调用，在请求里选择供应商（ceramic/exa/linkup），搜索请求进入网关日志、统一计费和访问控制。官方称后续会把 web search 做成 AI Gateway 内置的 Server Tool。

## 解决什么问题（事实层面，不判断值不值得解）

- agent 靠猜 URL 或训练截止前数据作答
- 搜索供应商各自计费、无统一日志与权限

## 怎么做的（技术原理/机制，事实层面）

- POST /accounts/{account_id}/ai/websearch/，参数 query、provider、limit（1-10）、gateway id
- 计费走 AI Gateway 额度，按供应商标价无加价；支持 BYOK
- 三家供应商承诺标识爬虫、遵守站点规则并标注来源

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 作者 | 博客作者 Michelle Chen、Sam Else、Gabriel Massadas | ppc.land 摘要 |
| 公司 | Cloudflare（上市公司） |  |

## 定价 / 商业模式

- Ceramic.ai（默认）：$0.25/千次
- Linkup：$5/千次
- Exa：$7/千次
- Cloudflare 不加价

## 关联信息 / 生态

历史同类：2026-08-05 Cloudflare Wallets、2026-08-06 Cloudflare OS 亦上过榜；与今日 #1 FastRouter 同属“AI 网关”生态。

## 技术时间线

| 日期 | 事件 |
|---|---|
| 2026-10-02 | Cloudflare 博客与 changelog 发布 beta |
| 2026-10-05 | 登 PH 日榜第 6 |

## 评论区反馈

评论仅 2 条：问最擅长的查询类型、用于抓取还是知识工作。

## 信息来源

- https://blog.cloudflare.com/introducing-web-search-api/
- https://developers.cloudflare.com/changelog/product-group/ai/
- https://ppc.land/cloudflare-web-search-for-ai-agents-costs-0-25-to-7-per-1-000-requests/
- PH API

## 未查到 / 待补

- beta 期限与 GA 时间
