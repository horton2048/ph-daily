---
product: "Lettertrace"
slug: "lettertrace"
date: "2026-08-12"
rank: 2
votes: 0
comments: 18

category: "AI 营销工具"
subcategory: "AI 曝光度追踪"
tags: ["开源", "AEO", "BYOK", "免费"]

tech_stack: ["Node.js/CLI"]
platform: ["CLI"]
open_source: true
license: "MIT"

business_model: "开源免费（BYOK，用户直付模型商 API 费用）"
pricing_start: "免费"
funding_stage: "未披露"
funding_amount: "未披露"

related_products: ["Profound", "Peec AI"]
maker_previous: ["未查到"]

key_signals: ["追踪 Claude/ChatGPT/Gemini 提及公司频率，BYOK 模式免掉竞品 $250/月订阅费", "cron job 定期调用模型 API 实现测量，非独家算法", "MIT 全开源，非 open-core"]

archived_at: "2026-08-12"
sources_count: 2
---

# Lettertrace · 扩展阅读上下文

> PT 2026-08-12 Product Hunt 榜单第 2 名 · 👍 0（未返回）· 💬 18
> 归档日期 2026-08-12 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Lettertrace |
| 英文 tagline | Track your AI visibility for free (using your own API keys!) |
| 中文 tagline | 免费追踪你的 AI 曝光度（用自己的 API key） |
| 官网 | lettertrace.com |
| PH 页 | https://www.producthunt.com/products/lettertrace |
| 品类标签 | Open Source · Analytics · Marketing |
| 票数 / 评论 | 0（未返回）/ 18 |
| 公司主体 | The Letter Company |

## 是做什么的（如实复述，不评价）

Lettertrace 是一个开源工具，追踪 Claude、ChatGPT、Gemini 等大模型在回答中提及某公司的频率（即"AI 搜索可见度"/AEO 指标）。通过 `npm install lettertrace` 安装的 CLI，用定时任务编排一批模型调用完成测量。

## 解决什么问题（事实层面，不判断值不值得解）

- 同类 AEO（Answer Engine Optimization）监测工具多为订阅制，创始人称竞品收费约 $250/月；Lettertrace 免费开源，用户自己出模型调用的钱。
- 创始人 Mathew Pregasen 称"AI search is effectively measured by a crafty cron job that orchestrates a bunch of model provider calls"——机制本身并不神秘，核心是把这套编排开源出来。

## 怎么做的（技术原理/机制，事实层面）

- BYOK（bring-your-own-key）模式：用户提供自己的 Claude/OpenAI/Gemini API key，工具直接调用模型问答，统计公司被提及频率。
- 单次测量周期成本官方估算约 $3（模型调用费，直付服务商不加价）。
- MIT 协议，非 open-core（无隐藏付费版本）。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Mathew Pregasen（The Letter Company） | PH 页 |
| 团队 | Deepak、Casey Millstein、fmerian | PH 页评论区 |
| 融资 | 未查到 | 未搜索到公开信息 |

## 定价 / 商业模式

完全免费，无付费层级，无需信用卡。用户只需承担自己 API key 的模型调用费用（估算约 $3/测量周期）。

## 关联信息 / 生态

- 品类对标 Profound、Peec AI 等 AEO/AI 可见度监测工具（多为付费 SaaS）。
- GitHub：github.com/letterstory/lettertrace

## 信息来源

- PH 产品页：https://www.producthunt.com/products/lettertrace（描述、创始人评论、定价、GitHub）

## 未查到 / 待补

- 融资情况、公司成立时间
- 与 Profound/Peec AI 等竞品的功能对比细节
- 准确票数（PH API 当日未返回）
