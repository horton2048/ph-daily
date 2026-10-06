---
# 结构化元数据（用于索引和聚合）
product: "Gemini 3.7 Flash"
slug: "gemini-3-7-flash"
date: "2026-08-14"
rank: 4
votes: 139
comments: 1

# 分类标签
category: "AI"
subcategory: "大语言模型 / 编码与 Agent 模型"
tags: [Google, 大模型, 编码, Agent, 长上下文]

# 技术信息
tech_stack: [Gemini API, Google AI Studio, Vertex AI]
platform: [API, Web]
open_source: false
license: ""

# 商业信息
business_model: "API 按 token 计费"
pricing_start: "$0.75/百万输入 token，$3.75/百万输出 token（截至2026-12-31的介绍价，2027-01-01起涨至$1.50/$7.50）"
funding_stage: "不适用（Google DeepMind 内部产品）"
funding_amount: "不适用"

# 关联信息
related_products: [Gemini 3.6 Flash, Claude, GPT系列, Codex]
maker_previous: [Gemini 3.6 Flash（三周前发布的上一代模型）]

# 速览信号
key_signals:
  - "距上一代 Gemini 3.6 Flash 发布仅三周，是迭代速度的新纪录"
  - "介绍价 $0.75/百万输入token，是上一代同档价格的一半，且有效期到2026年底"
  - "FrontierCode 1.1 Main 编码基准从34.4%提升到43.6%，DeepSWE v1.1 长程软件工程基准从49.0%升到65.3%"
  - "支持100万token上下文窗口，最高6.4万token输出，128k长文本needle测试得分97.0%"

# 元信息
archived_at: "2026-08-14"
sources_count: 6
---

# Gemini 3.7 Flash · 扩展阅读上下文

> PT 2026-08-14 Product Hunt 榜单第 4 名 · 👍 139 · 💬 1
> 归档日期 2026-08-14 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Gemini 3.7 Flash |
| 英文 tagline | Google's smartest workhorse yet for coding & agents |
| 中文 tagline | 谷歌迄今最能干的编码与 Agent 主力模型 |
| 官网 | https://deepmind.google/models/model-cards/gemini-3-7-flash/ |
| PH 页 | https://www.producthunt.com/products/gemini-3-7-flash |
| 品类标签 | AI / Development |
| 票数 / 评论 | 139 / 1 |
| 公司主体 | Google DeepMind |
| 企业版/关联站点 | Google AI Studio、Vertex AI |

## 是做什么的（如实复述，不评价）

Gemini 3.7 Flash 是 Google DeepMind 发布的 Flash 系列大语言模型新版本，定位为面向编码、AI Agent、知识型工作和网页开发的"主力模型"（workhorse）。支持文本、图像、音频、视频多模态输入，上下文窗口达 100 万 token，最高可输出 6.4 万 token。于 2026-08-13 发布，距上一代 Gemini 3.6 Flash 发布仅三周。

## 解决什么问题（事实层面，不判断值不值得解）

- 面向需要高频调用、成本敏感的编码/Agent 场景，提供比旗舰模型更低成本但性能够用的选项
- 上一代模型在多步骤 Agent 任务中的规划、工具调用及遇阻后的适应能力有限，导致开发者需要更多重试和人工介入
- 知识密集型文档处理（如财报类 PDF）和企业工作流自动化场景下模型准确率不足

## 怎么做的（技术原理/机制，事实层面）

- 在完成多步骤任务（规划、工具调用）方面比上一代更"守纪律"，遇到障碍时适应能力更强，旨在减少 Agent 工作流中的重试和人工监督
- 编码能力提升：FrontierCode 1.1 Main（衡量生产级代码质量）得分从 34.4%（3.6 Flash）提升到 43.6%；DeepSWE v1.1（长程软件工程测试）从 49.0% 提升到 65.3%
- 文档处理能力提升：GDP.pdf 基准从 22.0% 提升到 34.0%；AutomationBench（企业工作流完成度）从 17.0% 提升到 30.4%
- 长上下文：128k needle-in-haystack 长文本检索测试得分 97.0%
- Artificial Analysis Intelligence Index 综合评分 53（medium 档），高于同类模型中位数 34

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | 不适用（Google DeepMind 内部团队） | - |
| 融资 | 不适用 | - |
| 投资方 | 不适用 | - |
| 加速器 | 不适用 | - |
| 合规认证 | 未查到 | - |

## 定价 / 商业模式

API 按 token 计费。介绍价（有效期至 2026-12-31）：输入 $0.75/百万 token，输出 $3.75/百万 token，即上一代 Gemini 3.6 Flash 原价的一半。2027-01-01 起价格上调至输入 $1.50/百万 token、输出 $7.50/百万 token。

## 关联信息 / 生态

- 与三周前发布的 Gemini 3.6 Flash 相比，本次迭代速度被多家媒体称为"低成本模型领域的新速度纪录"
- 通过 Google AI Studio 和 Vertex AI 提供访问
- 面向编码、Agent、文档处理、Web 开发四大场景定位，与 Claude、GPT 系列、Codex 等模型在编码/Agent 赛道形成竞争

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 约2026-07-23（三周前） | Gemini 3.6 Flash 发布 |
| 2026-08-13 | Gemini 3.7 Flash 正式发布 |
| 2026-08-14 | 登上 Product Hunt 当日榜单第 4 名 |
| 2026-12-31 | 介绍价定价窗口截止 |
| 2027-01-01 | 价格上调至 $1.50/$7.50 每百万 token |

## 评论区反馈（事实摘录，不评价）

PH 页面仅 1 条评论，具体内容未抓取，待补。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/gemini-3-7-flash（基本信息、票数评论数）
- 官方 Model Card：https://deepmind.google/models/model-cards/gemini-3-7-flash/（多模态、上下文窗口等规格）
- 公开报道：VentureBeat「Google's Gemini 3.7 Flash targets coding and agents with a 50% introductory price cut」、MarkTechPost、the-decoder.com、techtimes.com（发布时间、定价、基准分数）
- GitHub：不适用（闭源模型，无公开仓库）

## 未查到 / 待补

- 是否有免费额度（free tier）具体限额
- 具体训练数据/模型架构细节（Google 未披露）
- PH 页面唯一评论的具体内容
- 与 Gemini 3 Pro / Ultra 等同代旗舰模型的定位区分细节
