---
# 结构化元数据（用于索引和聚合）
product: "Perplexity Hybrid Compute"
slug: "perplexity-hybrid-compute"
date: "2026-09-13"
rank: 2
votes: 145
comments: 2

# 分类标签
category: "AI agent"
subcategory: "本地推理 / 隐私路由"
tags: ["Mac", "Apple Silicon", "本地优先", "AI 助手", "隐私", "开源", "Pro/Max 订阅", "企业版"]

# 技术信息
tech_stack: ["Perplexity Computer (Mac app)", "Apple Silicon", "On-device LLM inference", "Cloud LLM API", "PII detection classifier"]
platform: ["macOS (15+)"]
open_source: true
license: "MIT (PII-Tracer 模型权重)"

# 商业信息
business_model: "订阅制（Pro / Max / Enterprise 限定功能）"
pricing_start: "需 Pro/Max/Enterprise 订阅，本地生成 token 免费，云端 token 照常计费；具体订阅价格未在本次信息源中验证"
funding_stage: "Series E-6 / 后期"
funding_amount: "公司层面：2025-09 估值 200 亿美元；2026 年初 Series E-6 估值 212.1 亿美元（来自 Wikipedia，未单独交叉验证）"

# 关联信息
related_products: ["Ollama", "LM Studio", "Apple Intelligence (Private Cloud Compute)", "ChatGPT Desktop", "Claude Desktop"]
maker_previous: ["Perplexity AI Inc. 同期产品：Perplexity 主搜索、Comet 浏览器、Perplexity Computer（Mac app）、Deep Research、Perplexity Labs、Tasks、Assistant、Patents"]

# 速览信号（给 caption.md / INDEX.md 等下游用，避免整篇重读正文才能省 token）
key_signals:
  - "Hybrid Compute 把同一任务拆给云端（推理/搜索）和本地（私人文件/敏感数据）两套模型，本地侧用 Gemma E4B + 两个 Qwen 3.6 35B 变体（其中一个 Perplexity 后训练过），云端用 frontier 模型"
  - "本地侧有一个 on-device PII 分类器（PII-Tracer，~0.6B 参数，Qwen3 双向编码器，MIT 开源，Hugging Face: perplexity-ai/pplx-pii-masking），决定哪些数据可以上传到云"
  - "硬门槛：Apple Silicon + macOS 15+ + 至少 24GB（推荐 32GB）统一内存；用户可从 iPhone 远程触发任务，敏感步骤仍在 Mac 本地执行"
  - "只对 Pro / Max / Enterprise 订阅者开放；PH 评论里已有人抱怨 Perplexity Computer Max 订阅 'extremely expensive' 并希望支持 Mac Studio 跑本地以省 pplx credit"

# 元信息
archived_at: "2026-09-13"
sources_count: 5
---

# Perplexity Hybrid Compute · 扩展阅读上下文

> PT 2026-09-13 Product Hunt 榜单第 2 · 👍 145 · 💬 2  
> 归档日期 2026-09-13 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Perplexity Hybrid Compute |
| 英文 tagline | Splitting AI tasks: Cloud for research, Mac for privacy |
| 中文 tagline | 拆分 AI 任务：云端研究，Mac 端隐私 |
| 官网 | https://www.perplexity.ai/hub/products/hybrid-compute（403 未抓到正文，仅 PH 帖转链） |
| PH 页 | https://www.producthunt.com/products/perplexity-ai |
| 品类标签 | Mac · Artificial Intelligence |
| 票数 / 评论 | 145 / 2 |
| 公司主体 | Perplexity AI, Inc.（旧金山，私营） |
| 上榜日期（PT） | 2026-09-13 |
| PH Hunter | Rohan Chaubey (@rohanrecommends) |

## 是做什么的（如实复述，不评价）

Perplexity Computer（Mac 端 app）的一项新功能。开启后，同一个 AI 任务会被拆分：需要大规模推理和联网搜索的部分交给 Perplexity 云端 frontier 模型；涉及用户本地私人文件、敏感数字、客户文档的部分，留在 Mac 上由本地小模型处理，文件本身不上传。本质上是在同一个对话/任务里同时调度云端 + 本地两套模型，由 app 自动决定哪段给谁。

## 解决什么问题（事实层面，不判断值不值得解）

- **隐私顾虑**：律师、财务、并购从业者希望用 frontier 模型做研究，但合同、尽调底稿、客户 PII 不能离开本机
- **成本顾虑**：纯云端 frontier 模型消耗 token 极快，本地能处理的部分免费（本地 token 0 成本，云端 token 照常计费）
- **多端工作流**：在 iPhone 上发指令，敏感步骤仍在 Mac 本地执行（Perplexity 官方把 Mac mini / Mac Studio 定位为「ideal dedicated local inference nodes」）

公开案例场景（来自报道）：
- 金融：上市公司公开信息放云做尽调，机密交易文件留本地
- 法律：判例研究放云，当事人特权文件留本地
- 广告：市场调研放云，未公开的创意素材留本地

## 怎么做的（技术原理/机制，事实层面）

- **任务拆分**：云端 frontier 模型负责搜索、推理、规划；本地模型负责读/处理私人文件、做本机动作
- **on-device privacy gate（隐私网关）**：每次用户上传文件或发消息时，本地一个 PII 分类器自动判断内容敏感度；可执行的动作有四种：mask（遮蔽敏感字段）、block（留在本地）、refuse（拒绝执行）、ask（弹窗让用户确认是否上传云端）
- **三类本地模型**（用户可切换，号称"one-click setup"，无需 Ollama 或 API key）：
  - Gemma E4B
  - Qwen 3.6 35B-A3B
  - Qwen 3.6 35B-A3B 的 Perplexity 后训练版本
- **PII-Tracer 分类器**（已开源到 Hugging Face）：
  - ~0.6B 参数，Qwen3 backbone + 双向 attention
  - 1024 → 37 维 BIOES token 分类头 + 1024 → 1 维文档级敏感度头
  - 4,096 token 上下文
  - 训练数据 ~714K 样本、3 epochs
  - MIT 协议
  - 9 个 PII 类别：private_person / private_email / private_phone / private_address / private_url / private_date / account_number / secret / other_pii
  - 长文档用 50%-overlap 滑窗解码，单窗 recall 从 0.975（<1K 字符）降到 0.687（>10K 字符），滑窗后回到 0.965
- **远程触发**：iPhone 可远程派发任务，UI 显示实时 CPU/GPU/内存占用和 token 计数侧栏
- **企业能力**：管理员控制面板 + 审计日志（记录什么数据离开了设备）

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 公司 | Perplexity AI, Inc.（私营） | Wikipedia |
| 总部 | San Francisco, CA, US | Wikipedia |
| 创始人 | Aravind Srinivas（前 OpenAI、Google DeepMind）、Denis Yarats、Johnny Ho、Andy Konwinski | Wikipedia |
| CEO | Aravind Srinivas | Wikipedia |
| Hybrid Compute 产品负责人 | Jon Staff（Perplexity Mac product lead / PM） | AIBase 报道 |
| 公司成立 | 2022-08 | Wikipedia |
| 搜索引擎首发 | 2022-12-07 | Wikipedia |
| 2024-04 | $165M 融资，估值 $1B+ | Wikipedia |
| 2025-06 | $500M 融资，估值 $14B | Wikipedia |
| 2025-09 | 估值 $20B（未单独披露轮次细节） | Wikipedia |
| 2026 年初 | Series E-6，估值 $21.21B | Wikipedia（本次未单独交叉验证） |
| 已知投资人 | Jeff Bezos、Nvidia、Databricks、1789 Capital | Wikipedia |
| 员工数 | 52（截至 2024，Wikipedia 数据，可能已过时） | Wikipedia |

## 定价 / 商业模式

- **功能可用性**：仅 Perplexity Pro / Max / Enterprise 订阅者可用
- **token 计费**：本地生成的 token 免费；云端 frontier 模型 token 照常按订阅档位计费
- **未在本次信息源验证**：Pro / Max / Enterprise 三个档的具体价格、年度计费是否打折；公开历史口径是 Pro ≈ $20/月，Max ≈ $200/月（2025 年），但本次未能验证 2026-09-13 时点是否调整
- **PH 评论区反馈**：用户 André J 明确表示 Perplexity Computer Max 订阅 "extremely expensive"，希望 Hybrid Compute 能扩展到 Mac Studio 本地推理以避免一天用光 pplx credit

## 关联信息 / 生态

- **上游产品**：Perplexity Computer（Mac app，本次 Hybrid Compute 是它的一个功能/模式）
- **同公司历次上榜 PH 的产品**（按 PH 页 parent 显示）：Deep Research（2025-02-22 #2）、Perplexity Labs（2025-05-30 #1）、Comet（2025-08-14 #4）、Patents（2025-10-31 #3）、Assistant（2025-01-24 #5）、Tasks（2025-06-20 #2）
- **直接对标**：Ollama、LM Studio（纯本地 LLM 路线）、Apple Intelligence / Private Cloud Compute（系统级本地 AI）、ChatGPT Desktop、Claude Desktop（云端为主）
- **差异化叙事**：竞品要么纯云、要么纯本地；Hybrid Compute 卖的是「同任务内自动路由 + 用户可控的滑动条」
- **领导层公开表态**（Jon Staff）：「Pure cloud frontier models are almost always better at output quality」「I think this should be a tunable scale… ultimately, the user should decide」—— 官方默认承认云端更强，Hybrid 是给用户一个调节阀

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-09-13 | Hybrid Compute 在 PH 上线（PT 日期） |
| 2026-09-13 | PII-Tracer 模型权重在 Hugging Face 开源（MIT） |
| 未查到 | PII-TRACE 数据集本身是否随模型同步开源：报道提示"as of early September 2026" 数据集尚未公开，只有模型 checkpoint 和 benchmark 方法论公开——**待补确认** |

## 评论区反馈（事实摘录，不评价）

- **André J**：Perplexity Computer Max 订阅 "extremely expensive"，建议把 hybrid 思路扩展到 Mac Studio 本地推理，"avoid running out of allotted pplx credits in a day"
- **PH 帖内另有 maker 留言确认**：3 个本地模型 + 一键安装（无需 Ollama / API key）、on-device 隐私检查器（mask / block / ask）、iPhone 远程触发敏感步骤留在 Mac、企业 admin 控制 + 审计日志

## 信息来源

- **PH 产品页**：https://www.producthunt.com/products/perplexity-ai（拿到 launch 日期、tagline、票数 145、评论 2、Hunter 名、5 张截图、parent 产品历史榜记录）
- **官网（Hub）**：https://www.perplexity.ai/hub/products/hybrid-compute（HTTP 403，未抓到正文；链接由 PH 帖跳转链指向）
- **官方博客 PII-Tracer**：https://www.perplexity.ai/hub/blog/pii-trace-detecting-personal-data-before-it-leaves-the-device（HTTP 403，未抓到正文）
- **官方博客 Hybrid Compute**：https://www.perplexity.ai/hub/blog/introducing-hybrid-compute-on-mac（HTTP 403，未抓到正文）
- **Hugging Face 模型卡**：https://huggingface.co/perplexity-ai/pplx-pii-masking（已验证存在；MIT、0.6B、Qwen3 双向、9 类 PII、月下载 1,806）
- **第三方报道（AIBase）**：https://news.aibase.com/news/30768（拿到产品架构、本地模型清单、隐私机制、需求、Jon Staff 引用）
- **第三方报道（Gadgets360）**：https://www.gadgets360.com/ai/news/perplexity-hybrid-compute-feature-rollout-11992584（Claude Code 无法抓取，仅标题可见）
- **第三方报道（Mashdigi 繁体）**：https://mashdigi.com/balancing-privacy-and-cost-perplexity-launches-hybrid-compute-for-mac-allowing-sensitive-tasks-to-be-handled-by-native-ai/（Claude Code 无法抓取，仅标题可见）
- **Wikipedia**：https://en.wikipedia.org/wiki/Perplexity_AI（公司基本面、融资里程碑）
- **GitHub**：尝试 `https://github.com/perplexityai/pii-tracer` 返回 HTTP 404；HF 模型卡提到 backbone 来自 `perplexity-ai/pplx-embed-v1-0.6b`，但未在 GitHub 验证到对应代码仓

## 未查到 / 待补

- Pro / Max / Enterprise 三档 2026-09-13 时点的确切订阅价格
- Hybrid Compute 官方博客原文（perplexity.ai/hub 系列 403，未能直读正文，依赖第三方转述）
- PII-TRACE benchmark 数据集本身是否同步开源
- GitHub 代码仓 `perplexityai/pii-tracer` 是否真实存在（HF 模型卡提到 `trust_remote_code=True` + vendored `modeling_pii_masking.py`，但仓库 URL 404）
- 公司 2026 年初 Series E-6 估值的具体投资方和金额细节（仅 Wikipedia 提及，未交叉验证）
- Hybrid Compute 的延迟 / 准确率官方数据（云端 vs 本地的具体差异数字）
- 公司 2024 年之后员工数是否仍为 52 人
