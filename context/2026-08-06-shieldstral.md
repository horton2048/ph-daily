# Shieldstral · 扩展阅读上下文

> PT 2026-08-06 Product Hunt 榜单第 6 名 · 👍 票数 PH 页未显示 · 💬 1
> 归档日期 2026-08-06 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Shieldstral（模型名 Shieldstral-1.0-3B） |
| 英文 tagline | Define safety at runtime for text and images |
| 中文 tagline | 在运行时为文本和图像定义安全策略 |
| 官网 | https://mistral.ai（发布公告：https://mistral.ai/news/shieldstral/） |
| PH 页 | https://www.producthunt.com/products/mistral-7b（注意：URL slug 是 mistral-7b，这是 Mistral AI 公司的 PH 公司页） |
| 品类标签 | Open Source · Artificial Intelligence · Security |
| 票数 / 评论 | 票数未显示 / 评论 1（归档 2026-08-06） |
| 公司主体 | Mistral AI（法国巴黎的开放权重 AI 实验室）；这是其在 PH 的第 23 次发布 |
| 企业版/关联站点 | Hugging Face 权重 mistralai/Shieldstral-1.0-3B；技术报告 arXiv:2607.25857；治理页 legal.mistral.ai/ai-governance/models/shieldstral |

## 是做什么的（如实复述，不评价）

Shieldstral 是 Mistral AI 于 2026-08-04 发布的一个约 3B 参数、开放权重、多模态安全分类器（guardrail/内容审核模型）。它把内容审核改成"二分类问答"任务：审核策略不作为固定分类写死在权重里，而是在推理时以自然语言的 yes/no 问题传入，模型对文本、图像或文本+图像返回一个单一的是/否概率分数。因为策略在 prompt 里、不在权重里，想换审核尺度时改问题文字即可，不需要重新训练。官方称可在单块 16GB GPU 上本地跑。PH 发布页标注"免费（Free）"。

## 解决什么问题（事实层面，不判断值不值得解）

- 官方口径（PH 页 maker 评论）：审核的难点在于"线画在哪里"——儿童应用、网络安全工具、心理健康平台对同一内容的安全判断标准不同。
- 官方示例问题（PH/HF/blog）："这张图对未成年人安全吗？""这条回复是否宣扬身体暴力？"同一个 checkpoint 换问题即换策略。
- 目标场景：用户 prompt 审核、模型回复审核、模型拒答（refusal）分类；本地/私有部署，策略变更不需要重训。
- 部署形态：一个 checkpoint 服务不同严格度场景（如心理健康平台 vs 网络安全研究工具），只改 query 文字。

## 怎么做的（技术原理/机制，事实层面）

- Prompt 三段式：`<Instruct>`（评估上下文/严格度）、`<Query>`（单个 yes/no 策略问题）、`<Document>`（待审核内容）。固定 system 消息："Judge whether the Document meets the requirements based on the Query and the Instruction provided... answer can only be 'yes' or 'no'."
- 推理时只读 yes/no 两个 logit，softmax 归一化成连续校准分数；可调阈值或按置信度排序，而非离散标签。
- 多模态：文本、图像、文本+图像；prompt、response、prompt-response 对均可审。
- 12 种语言：英语、法语、西班牙语、德语、意大利语、葡萄牙语、荷兰语、中文、日语、韩语、阿拉伯语、俄语。
- 上下文：训练序列最长 32k tokens；官方称理论上支持 256k 上下文窗口。
- 基础模型 `mistralai/Ministral-3-3B-Base-2512`，含原生 Pixtral 视觉编码器；BF16 下模型文件约 4B 参数。
- 训练方法（Mistral 公告 + explainx.ai 整理）：把异构的公开安全数据集统一成 instruction-query-document 格式（对不同来源设不同严格度）；构造"相似的、易混淆的策略对"，用 LLM 改写安全文本使其只违反某一个策略；用通用图像数据补充审核图像数据、用视觉语言重排器过滤；用 LoRA 微调、SLERP 合并三个 checkpoint（公开数据校准版 + 细粒度策略判别版 + 基础 instruct 模型）。全程在 Mistral 的 Forge 训练平台端到端构建。
- 训练数据规模：官方口径 5,410 万（54.1M）对比对、12 种语言（aiweekly 报道）。
- 支持框架：vLLM ≥ 0.26.0（推荐）、llama.cpp、SGLang（需特定修复）、Transformers（Mistral3ForConditionalGeneration + mistral-common ≥ 1.11.5）；可用 Axolotl 微调。
- 基准（Mistral 自报，未被独立复现）：WildGuardTest（prompt）88.1、ToxicChat 84.1、HarmBench（prompt）99.4、XSTest（refusal）94.6、Aegis v2（response）87.2、VLGuard 97.7、UnsafeBench 81.8；官方称在文本安全与多模态上匹配或超过"至多 7 倍大小"的开源 guardrail 模型（对比基线未点名）。
- 局限（HF model card / 报道）：跨语言与领域覆盖不均；对抗性/混淆输入与超长文档可靠性下降；输出只有分数没有解释，无法追溯到具体策略条款；音频/视频审核不在本版。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 发布主体 | Mistral AI，PH 第 23 次 launch；launch team 列 Zac Zuo、Sophia Yang、Margaret Jennings（+更多未显示） | PH 页 |
| 公司定位 | "巴黎的开放权重 AI 实验室"，以发布开放权重模型而非封闭 API 著称 | ai-news.ge / pondero.ai |
| 创始人 | Arthur Mensch（前 DeepMind）等；公开报道常识，本次未直接抓取到一手来源，待核实 | 待核 |
| 融资 | 未查到（本次未抓取到一手来源；Wikipedia 抓取失败） | 待补 |
| 开放联盟 | Open Secure AI Alliance：NVIDIA 牵头、50+ 公司，成员含 Mistral、Microsoft、Cisco，2026 年 7 月底成立；Shieldstral 是联盟的首批落地发布之一 | ai-news.ge / pondero.ai |
| 治理 | 有模型治理/生命周期页（legal.mistral.ai/ai-governance/models/shieldstral），记录版本、发布日期、退役状态 | 搜索摘录 |

## 定价 / 商业模式

- 模型开放权重，Apache 2.0 许可，可商用可非商用，免费下载（Hugging Face）；PH 发布页标"Free"。
- 与封闭审核 API 的差异点（报道口径）：无需按调用付费，无使用限制；但自托管企业需自行承担合规审计义务（如文档与对抗性测试要求）。
- 备注：欧盟 AI 法案合规、安全报告与审计线索方面，该模型可能相关（pondero.ai 观点，非事实判断）。

## 关联信息 / 生态

- 所属生态：Mistral AI 2026 年的小尺寸任务专用模型路线（OCR、embodied navigation 等），而非通用大模型对齐竞赛（explainx.ai 观察）。
- 生态位置：与 OpenAI 审核 API 对比——OpenAI 内置固定分类法；Shieldstral 无内嵌分类法、策略每次请求传入（explainx.ai）。
- PH 页相似产品区列出：OpenAI、Hugging Face、DeepSeek、Gemini、Cohere。
- Mistral 此前 PH 发布（背景）：Mistral Vibe（2026-06）、Voxtral TTS（2026-03）、Voxtral Transcribe 2（2026-02）、Mistral OCR 3（2025-12）；Mistral AI PH 页有 41 条评价、4K 关注者、2023 Golden Kitty 奖（AI 模型年度产品 Runner Up）。
- Hugging Face 数据：权重下载量上月 1,511 次；有 53 个微调衍生、8 个量化版本（抓取时点）。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 | 来源 |
|---|---|---|
| 2026-07 底 | NVIDIA 牵头、50+ 公司组建 Open Secure AI Alliance（Mistral、Microsoft、Cisco 等） | ai-news.ge |
| 2026-08-04 | Mistral 博客发布 Shieldstral 公告（By Mistral），同日发布技术报告（arXiv:2607.25857） | Mistral 博客 / aiweekly |
| 2026-08-06 | PH 榜第 6 名发布日 | 归档 2026-08-06 |

## 评论区反馈（事实摘录，不评价）

- Calin Rasniceru（用户）："超快且轻量，容易安装"；觉得更新频率可再高点；称其为"完全符合 GDPR 的欧盟模型"，把隐私当基本权利。（注：该评论针对轻量开放模型的通用好评，未指名具体功能。）
- Matteo Garza（用户）："轻量但强大的开源模型，我用 ollama 在本地跑"；改进建议是上下文窗口可以更宽；称其为欧洲、快速、可靠、符合 GDPR。
- Alexen SCH（用户）："对这个模型的轻量高效印象很深"，在摘要、写码、通用推理上表现好，适合本地/边缘使用；称其为"当前最好的开源模型之一"。
- 说明：这三条评论在抓取时位于 Shieldstral 发布讨论区，但内容是对"轻量开源模型"的通用评价；归档 2026-08-06 记录该发布评论数为 1，数字以归档为准。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/mistral-7b（产品名 Shieldstral、描述、maker 评论、launch team、相似产品、Mistral AI 页背景）
- 官网：https://mistral.ai/news/shieldstral/（发布公告、机制、基准、未来方向）
- Hugging Face model card：https://huggingface.co/mistralai/Shieldstral-1.0-3B（规格、许可、语言、框架、基准、局限）
- 公开报道：aiweekly.co（54.1M 对比对、Open Secure AI Alliance 语境）；ai-news.ge（NVIDIA 牵头 50+ 公司、成员名单、2026-07 底成立）；pondero.ai（Forge、SLERP、EU AI Act 语境）；explainx.ai（训练四法、prompt 格式、局限与部署模式）
- GitHub：无仓库（模型发布在 Hugging Face，非 GitHub）；记为"无公开代码仓库"

## 未查到 / 待补

- Mistral AI 公司融资轮次/金额/估值与创始人详细履历：本次未直接抓取到一手来源（Wikipedia 抓取 ECONNRESET），仅确认"巴黎的开放权重 AI 实验室"；待补。
- 官方 7× 对比的具体基线模型名单与第三方复现：公告未点名，无独立复现，待补。
- 具体票数：PH 页未显示（归档亦未含票数）。
- 评论区仅 1 条（归档口径）但抓取到 3 条通用好评：评论归属与时间需进一步核实。
