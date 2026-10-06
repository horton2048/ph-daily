---
# 结构化元数据（用于索引和聚合）
product: "Cognition's SWE-2"
slug: "cognition-s-swe-2"
date: "2026-09-13"
rank: 3
votes: 128
comments: 2

# 分类标签
category: "AI agent"
subcategory: "编码助手"
tags: ["编码模型", "RL训练", "成本优化", "Devin", "Kimi后训练", "开发者工具", "多档effort"]

# 技术信息
tech_stack: ["Kimi K3 (2.8T 参数基座, MoE)", "强化学习 (RL) + cost-aware reward", "DSpark 推测解码 + SpecForge draft model", "NVFP4/FP8 量化 + QAT", "MLA K/Q/V 用 FP8、NoPE FP8、RoPE BF16", "prefill delayer"]
platform: ["Devin Desktop (Mac)", "Devin CLI", "Devin Web (app.devin.ai, 滚动)", "Devin Fusion (滚动)"]
open_source: false
license: "未独立开源 SWE-2 权重（底层 Kimi K3 为 Moonshot AI 发布的修改版 MIT）"

# 商业信息
business_model: "闭源编码模型 + Devin Agent 订阅"
pricing_start: "SWE-2 单独定价未披露；按官方'比 Fable 5.1 Medium $3.28/task 便宜 64%'反推 ≈ $1.18/task（官方未给）"
funding_stage: "Series D+（母公司 Cognition 层面）"
funding_amount: "2026-05 Series D $1B+ 估值 ~$26B；2026-09-09 报道新一轮目标 ~$47B（待官方确认）"

# 关联信息
related_products: ["Devin", "Cursor", "GitHub Copilot", "Claude Code", "Kimi K3", "Fable 5.1", "GPT-6 Astra", "Codex 3.0", "Grok 4.6"]
maker_previous: ["Cognition AI 此前产品：Devin（自主 AI 软件工程师，2024-03 首发）、SWE-1.6 / SWE-1.7；2025 中收购 Windsurf（AI 编码 IDE）"]

# 速览信号（给 caption.md / INDEX.md 等下游用，避免整篇重读正文才能省 token）
key_signals:
  - "Kimi K3 (2.8T 参数 MoE) RL 后训练，把美元成本塞进训练奖励 R = S − λ_e C"
  - "FrontierCode 1.1 Main 50.0%，Terminal-Bench 2.1 92.8%；比 Fable 5.1 便宜 64%，约为 GPT-6 Astra 成本的 1/4"
  - "对比 SWE-1.7：少 58% turns / 省 81% 成本 / 首次代码编辑从 48 步降到 18 步（medium 档）"
  - "2026-09-10 上线，Devin Desktop + CLI 当天可用，Web/Fusion 滚动开放；三档 effort (medium/high/max) 一次 RL 跑完"

# 元信息
archived_at: "2026-09-13"
sources_count: 5
---

# Cognition's SWE-2 · 扩展阅读上下文

> PT 2026-09-13 Product Hunt 榜单第 3 · 👍 128 · 💬 2  
> 归档日期 2026-09-13 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Cognition's SWE-2 |
| 英文 tagline | Cognition's coding model, 64% cheaper than Fable 5.1 |
| 中文 tagline | Cognition 编程模型，比 Fable 5.1 便宜 64% |
| 官网 | https://cognition.com/blog/swe-2 |
| PH 页 | https://www.producthunt.com/products/cognition-s-swe-2 |
| 品类标签 | AI Coding Agents · Foundation Models |
| 票数 / 评论 | 128 / 2 |
| 公司主体 | Cognition AI（Devin 的母公司） |
| 企业版/关联站点 | Devin Desktop / Devin CLI / Devin Web (app.devin.ai) / Devin Fusion |

## 是做什么的（如实复述，不评价）

Cognition 推出的新一代编程大模型，从月之暗面 Kimi K3（2.8T 参数 MoE）做 RL 后训练而来，定位是 Devin 产品线背后的"推理引擎升级"。SWE-2 在 Devin Desktop 与 CLI 当天上架，Devin Web 和 Devin Fusion 滚动开放。

模型在四个基准上拿到第一梯队成绩：FrontierCode 1.1 Main 50.0%、DeepSWE 1.1 73.0%、Terminal-Bench 2.1 92.8%；Terminal-Bench 4 上 27.3%（仍显著低于 Fable 5.1 的 55.8% 与 GPT-6 Astra 的 57.9%，说明"中短链路 + 成本档"是主战场，长链任务仍是前沿模型的强项）。相对 SWE-1.7 平均少 58% 的执行步数、少 81% 的成本；首次代码编辑从中位数 48 步降到 18 步。

PH 上对应 tagline："Cognition's coding model, 64% cheaper than Fable 5.1"。

## 解决什么问题（事实层面，不判断值不值得解）

- SWE-1.7 用户反馈："over-explored simple tasks"——简单任务过度探索、浪费 token
- Fable 5.1 等头部编码模型单任务成本偏高（官方列价 Fable 5.1 Medium $3.28/task、Fable 5.1 Max $12.83/task）
- 多数 RL 训练把"准确率"和"成本"当两件事调优，SWE-2 想在一个训练 run 里同时管住两边
- 目标场景：Devin 自主软件工程师、CI 自动修 bug、大规模代码迁移

## 怎么做的（技术原理/机制，事实层面）

- **基座**：月之暗面 Kimi K3（2.8T 参数 MoE，2026-02-15 开源，修改版 MIT），官方称基座本身已是强编码模型
- **RL 奖励函数**：把美元成本塞进奖励 `R = S − λ_e C`，λ_e 调到基座 Pareto frontier 在 effort level e 处的斜率；同一个训练 run 同时出 medium / high / max 三档推理强度（不用事后拼接）
- **长度加权奖励基线**：`b̂ = ΣR_iL_i / ΣL_i`，自 SWE-1.6 起在用，稳定训练、压低 inference-training KL
- **推理栈优化**：
  - prefill delayer：TPM/TPS 提升 10-20%
  - DSpark 推测解码 + SpecForge 训练的 draft model：accept length 长 15%
  - 量化：NVFP4 / FP8 + quantization-aware training；MLA 的 K/Q/V 用 FP8、NoPE 用 FP8、RoPE 用 BF16
- **数据**：
  - RL 环境数 ×3
  - 加 instruction-following overlays
  - 把前代 SWE-2 checkpoint 喂进 RL flywheel 反向硬化 verifier
- **行为改进**：端到端测试覆盖更严；资源受限时主动找替代路径（如 MCP 不可用时从 Slack 历史重建数据）；被挑战时重新推导结论而非顺从
- **Trustworthiness 评估**：整体 98.0% 通过；英语 99.8%、简体中文 95.2%、繁体中文 99.1%

**对比表（Cognition 官方 09.10.26 公告）**：

| Benchmark | SWE-2 | Kimi K3 | Grok 4.6 | Fable 5.1 | GPT-5.6 Sol | GPT-6 Astra | SWE-1.7 |
|---|---|---|---|---|---|---|---|
| FrontierCode 1.1 Main | **50.0%** | 44.2% | 48.0% | 50.9% | 47.5% | 53.3% | 42.0% |
| DeepSWE 1.1 | **73.0%** | 68.5% | 67.5% | 67.4% | 72.7% | 74.1% | 37.7% |
| Terminal-Bench 2.1 | **92.8%** | 88.3% | 88.4% | 91.4% | 88.8% | 89.9% | 81.5% |
| Terminal-Bench 4 | 27.3% | 21.5% | 20.3% | 55.8% | 37.3% | 57.9% | 7.6% |

官方表述："within ~3.3 pts of GPT-6 Astra at ~1/4 the cost；within 1 pt of Fable 5.1 while 64% cheaper"。

**FrontierCode 1.1 Main Mean Steps**：SWE-1.7 = 127；SWE-2 medium = 53，high = 80，max = 98。**首次有效编辑中位数**：SWE-2 medium = 18 步，vs SWE-1.7 = 48 步。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 公司 | Cognition AI（Devin 的母公司），2023 成立 | 公开报道 |
| 创始人 | Scott Wu（CEO）、Steven Hao、Walden Yan | 公开报道 |
| 团队背景 | 三位均为 IOI 金牌；核心团队截至 2024-03 共持 10 枚 IOI 金牌 | 公开报道 |
| 早期融资 | 2024-04 Series A $175M（Founders Fund 领投，估值 $2B） | 公开报道 |
| 中期融资 | 2025-03 8VC 领投估值 $4B；2025-09 Founders Fund 领投 $400M，估值 $10.2B | 公开报道 |
| 近期融资 | 2026-05 Series D $1B+（Lux Capital / General Catalyst / 8VC），估值 ~$26B；2026-09-09 报道新一轮进行中，目标估值 ~$47B（待官方确认） | finsmes.com / agihunt.info |
| 重大并购 | 2025 年中从 Google 手中收购 Windsurf（AI 编码 IDE） | 公开报道 |
| 合规 / 安全评估 | Cognition 公开了对 SWE-2 的 propaganda/censorship 评测（98.0% 通过） | cognition.com/blog/swe-2 |
| SWE-2 产品页披露 | 公司层面信息（融资 / 投资方 / 加速器）官方 blog 未单独披露 | — |

## 定价 / 商业模式

PH 页标注"Free Options"（含免费档）。SWE-2 单独定价未在官方 blog 列出——官方文档以"对比 Fable 5.1 Medium $3.28/task 便宜 64%"的方式呈现成本优势（按此反推 SWE-2 Medium ≈ $1.18/task，但官方未给正式价目）。

模式比数字重要：**闭源编码模型 + Devin Agent 订阅 + 企业版 contact sales**——SWE-2 不是独立售卖产品，而是 Devin 升级后默认启用的底座模型。

## 关联信息 / 生态

- **同公司前代**：SWE-1.6 / SWE-1.7（Devin 早期模型迭代，本次 SWE-2 直接对标 SWE-1.7）
- **PH 列出的同类对比**：Claude by Anthropic、Claude Code、Cursor、Codex 3.0 by OpenAI、Kilo Code——都是 AI 编码助手 / 模型，SWE-2 走的不是 IDE 替代路线，而是 Devin Agent 底层模型的升级
- **直接竞品（产品层）**：Cursor / GitHub Copilot / Claude Code
- **直接竞品（模型层）**：Fable 5.1 / GPT-6 Astra / Grok 4.6 / GPT-5.6 Sol
- **底座**：Kimi K3（月之暗面 Moonshot AI，2026-02-15 开源）
- **官方称**："Pushing the Pareto Frontier"；在 Terminal-Bench 4 上 27.3% 实际弱于 Fable 5.1（55.8%）和 GPT-6 Astra（57.9%）
- **生态位**：Cognition 同时跑 Devin（产品）+ SWE 系列（底座模型）+ Windsurf（被收购的 IDE），覆盖编码 Agent 全栈
- **大客户**（公司层面）：Mercedes-Benz、Goldman Sachs、Infosys、Itau、Nubank

## 技术时间线

| 日期 | 事件 |
|---|---|
| 2023 底 | Cognition 成立（Scott Wu / Steven Hao / Walden Yan） |
| 2024-03 | Devin 首次亮相（SWE-Bench 13.86% 无人协助解题） |
| 2024-04 | Series A $175M，估值 $2B |
| 2025-03 | 8VC 领投轮，估值 $4B |
| 2025 中 | 从 Google 收购 Windsurf |
| 2025-09 | $400M 轮，估值 $10.2B |
| 2026-02-15 | Moonshot AI 发布 Kimi K3（SWE-2 底座） |
| 2026-05 | Series D $1B+，估值 ~$26B |
| 2026-09-09 | 报道新一轮进行中，目标估值 ~$47B（待官方确认） |
| 2026-09-10 | Cognition 发布 SWE-2（Devin Desktop + CLI 当日上线） |
| 2026-09-10 起 | Devin Web (app.devin.ai) 和 Devin Fusion 滚动开放 |
| 2026-09-13 | 上榜 PH 每日榜 #3 |

## 评论区反馈（事实摘录，不评价）

- **Rohan Chaubey**（PH 猎人，1d ago）：把 SWE-2 总结为"贴 frontier 但不带 frontier 价"；特别提到 RL 奖励里嵌入实际美元成本、三档 effort 一次跑完的设计
- **Tehreem Fatima**（7h ago，PH 标记 "Likely AI"）："把运行成本写进 RL 奖励是优化 agent 效率的聪明做法，希望保持联系同步 AI 进展"
- 产品页未见 SWE-2 团队成员的官方回复

## 信息来源

- PH 产品页：https://www.producthunt.com/products/cognition-s-swe-2（tagline、128 票/2 评论、品类、相关产品对比、猎人 Rohan Chaubey）
- 官方 blog：https://cognition.com/blog/swe-2（09.10.26 发布日期、完整 benchmark 表、训练方法、推理栈细节、成本曲线、Trustworthiness 评测）
- Kimi K3 底座：Hugging Face / moonshotai 官方仓库（2026-02-15, 2.8T MoE, 修改版 MIT）
- 公司融资：finsmes.com（2026-05 Series D $1B+）、agihunt.info（2026-09 报道新一轮 $47B 目标估值）、Wikipedia / aiwiki.ai 团队背景
- 公开报道：panewslab、analyticsindiamag（IOI 金牌、团队背景）
- GitHub / HuggingFace：未见 SWE-2 自身的开源仓库；HF 上 `cognition-ai/SWE-2` 模型卡片当前返回 401（页面需要登录或仓库未公开），暂无法直接确认权重是否放出；底层 Kimi K3 在 HF / GitHub（moonshotai/Kimi-K3-Thinking）公开

## 未查到 / 待补

- SWE-2 官方 API 单价（按 token 还是按 task 计费均未披露）
- SWE-2 权重是否实际在 Hugging Face `cognition-ai/SWE-2` 公开（页面 401，第三方报道未明确"开源 / 仅模型卡"）
- "Fable 5.1" 在公开模型目录（HuggingFace、OpenRouter、Artificial Analysis）中查不到独立条目，疑为 Cognition 内部代号或定制对比基准；待补独立第三方评测
- Kimi K3 与 SWE-2 之间 post-training 用了多少 token / 多少 GPU-hour，Cognition 未披露
- 2026-09 报道中 ~$47B 估值的新一轮尚未官方确认
- "Free Options" 具体指 Devin 哪一档定价（Free / Pro / Max / Enterprise）尚未在本次核验