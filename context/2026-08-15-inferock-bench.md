---
# 结构化元数据（用于索引和聚合）
product: "Inferock Bench"
slug: "inferock-bench"
date: "2026-08-15"
rank: 1
votes: 190
comments: 31

# 分类标签
category: "开发者工具"
subcategory: "LLM 成本审计/可观测性"
tags: ["开源", "LLM计费", "本地代理", "FSL协议", "自托管"]

# 技术信息
tech_stack: ["Node.js"]
platform: ["CLI", "本地代理"]
open_source: true
license: "FSL-1.1-ALv2（2年后转 Apache-2.0）；子包 @inferock/measure 为 Apache-2.0"

# 商业信息
business_model: "开源免费（自托管）；托管推理版定价细节未披露"
pricing_start: "免费（npx inferock-bench 一分钟起用）"
funding_stage: "未披露"
funding_amount: "未披露"

# 关联信息
related_products: []
maker_previous: []

# 速览信号
key_signals:
  - "开源本地代理，FSL-1.1-ALv2 协议（2年后转 Apache-2.0），npx 一条命令一分钟起用，免费"
  - "GitHub 122 star，支持 OpenAI/Anthropic/Gemini/OpenRouter(pinned 端点) 四类供应商"
  - "创始人称核心动机：'AI 回答说到一半断了还照常计费，没人说得清钱去哪了'——供应商只给总账单不给单次凭证"
  - "检测5类计费异常：未完成回复仍计费、空回复计费、token数与可见输出不符、静默重试重复扣费、漏记缓存折扣"

# 元信息
archived_at: "2026-08-15"
sources_count: 4
---

# Inferock Bench · 扩展阅读上下文

> PT 2026-08-15 Product Hunt 榜单第 1 名 · 👍 190 · 💬 31
> 归档日期 2026-08-15 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Inferock Bench |
| 英文 tagline | An independent receipt for every LLM API call |
| 中文 tagline | 给每一次 LLM API 调用一张独立收据 |
| 官网 | https://inferock.ai |
| PH 页 | https://www.producthunt.com/products/inferock-bench |
| 品类标签 | Open Source · Developer Tools · Artificial Intelligence |
| 票数 / 评论 | 190 / 31 |
| 公司主体 | OpiusAI |
| 企业版/关联站点 | inferock.ai（含 how-it-works / methodology / faq 子页） |

## 是做什么的（如实复述，不评价）

Inferock Bench 是一个本地代理（proxy）工具，拦截应用发往 OpenAI、Anthropic、Gemini、
OpenRouter 的 LLM API 调用，在本地生成一份独立于供应商账单的"收据"，记录每次调用的
token 用量、失败原因、重试情况和计费异常。用户只需修改 SDK 里的 `apiKey` 和 `baseURL`
两个设置，供应商密钥仍留在本地，不经过第三方。同时提供开源仓库 `inferock-bench`（本地
代理）和独立包 `@inferock/measure`（把捕获的调用转成实时的美元损失收据）。

## 解决什么问题（事实层面，不判断值不值得解）

- LLM 供应商账单只给总额，不给逐次调用的凭证，用户无法核实计费是否准确
- 回答中途断掉（mid-stream cut off）仍可能被完整计费
- 空回复、token 数与可见输出不符、静默重试重复扣费等异常难以自行发现
- 目标场景：调用量较大、想审计 AI 成本支出的开发者/团队

## 怎么做的（技术原理/机制，事实层面）

- 本地代理拦截模式：应用把正常开发流量发到 localhost，`inferock-bench` 转发给供应商
  （带供应商 key），`@inferock/measure` 把捕获的调用转成实时的美元损失收据
- 证据收集分两类：被动检查捕捉结构性故障（如空回复、mid-stream cutoff）；主动探测
  处理模型漂移和基线偏差
- 生成"月度损失报告"：失败调用数、成本估算、补救状态
- 检测的计费异常类型：未完成回复仍计费、空回复计费、token 计数与可见输出不符、
  静默重试重复扣费、漏记缓存折扣
- 误报/失败处理：未查到具体的误报率或校准方法说明

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | 三位 maker：Bharath Koneti、fmerian、Hamza Afzal Butt | PH 页面 |
| 融资 | 未披露 | — |
| 投资方 | 未披露 | — |
| 加速器 | 未查到 | — |
| 合规认证 | 未查到 | — |

## 定价 / 商业模式

自托管本地代理完全免费开源（`npx inferock-bench` 即可运行）。官网提到还有"BYOK可见性"
或"托管推理"两种定价路径，托管模式提供有限额度的信用补偿机制，但具体价格未在公开页面
披露。

## 关联信息 / 生态

- GitHub 仓库 122 star，支持 OpenAI、Anthropic（Claude）、Gemini Developer API，以及
  OpenRouter 的多个 pinned 端点（meta-llama、deepseek、mistral、moonshot/kimi、
  z-ai/glm、qwen）
- 创始人 Koneti 在评论区提问社区"是否有人成功用逐次调用证据跟供应商argue账单并拿到过
  退款/credit"，说明产品定位是给用户提供跟供应商谈判的凭证，而非仅做可视化

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-08-05 | GitHub 仓库最近一次公开 run card 记录 |
| 2026-08-15 | Product Hunt 上榜，登顶当日榜单第 1 |

## 评论区反馈（事实摘录，不评价）

- 创始人 Bharath Koneti 自述动机："We kept paying for AI answers that died mid
  sentence, and nobody could tell us where the money went."（我们一直在为说到一半
  断掉的 AI 回答付费，却没人说得清钱去哪了）
- 创始人在评论区发起提问：是否有人曾用详细的逐次调用记录成功跟 AI 供应商argue账单
  并拿到 credit，用于验证"凭证是否真能影响供应商侧的处理结果"

## 信息来源

- PH 产品页：https://www.producthunt.com/products/inferock-bench（拿到创始人自述、团队名单、定价、核心功能）
- 官网：https://inferock.ai/how-it-works/（拿到机制说明、商业模式框架）
- GitHub：https://github.com/inferock/inferock-bench（拿到 star 数、license、支持的供应商列表、核心机制 README 摘录）
- 公开报道：未额外搜索融资/团队背景新闻

## 未查到 / 待补

- 具体融资情况（是否融资、金额、投资方）
- 托管推理版本的具体定价
- 误报率/校准方法的技术细节
- 团队背景（是否连续创业者、过往项目）
