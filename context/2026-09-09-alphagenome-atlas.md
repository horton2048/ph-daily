---
product: "AlphaGenome Atlas"
slug: "alphagenome-atlas"
date: "2026-09-09"
rank: 8
votes: 120
comments: 12
category: "医疗 AI"
subcategory: "基因组学数据库 / 变体效应预测"
tags: ["Google DeepMind", "DNA 突变", "非编码基因", "AI for Science", "预计算数据集", "可视化门户", "API"]
tech_stack: ["JAX", "Python", "Transformer", "CNN", "TFRecords", "TPU v3+", "NVIDIA H100"]
platform: ["Web", "API", "Google Cloud", "Google Antigravity"]
open_source: true
license: "Apache-2.0（客户端代码）/ CC-BY 4.0（文档与示例）/ CC-BY-NC 4.0（其他材料）/ 模型权重非商用"
business_model: "学术研究免费 + 商业化将通过 Google Cloud 推出"
pricing_start: "学术研究免费（仅限非商用）；商业化定价未披露"
funding_stage: "未披露（隶属 Google DeepMind/Google 内部项目）"
funding_amount: ""
related_products: ["AlphaGenome", "AlphaMissense", "AlphaFold", "DeepVariant"]
maker_previous: []
key_signals:
  - "1 PB 数据集预计算了 9 billion（90 亿）个单核苷酸变体的调控效应，规模约为 AlphaFold Database 的 30 倍"
  - "2026-09-08 由 Google DeepMind 官方发布（早于 PH 上榜 1 天），Pushmeet Kohli（VP Science）和 Žiga Avsec（Genomics Initiative Lead）牵头"
  - "引入 AlphaGenome Variant Impact（AVI）分数：把 AlphaGenome + AlphaMissense 整合成单一排序指标，覆盖编码与非编码区"
  - "仅供非商用研究（API 和 Web 门户），明示未做临床验证；商业化路径将走 Google Cloud"
archived_at: "2026-09-10"
sources_count: 8
---

# AlphaGenome Atlas · 扩展阅读上下文

> PT 2026-09-09 Product Hunt 榜单第 8 · 👍 120 · 💬 12
> 归档日期 2026-09-10 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息
| 字段 | 值 |
|---|---|
| 产品名 | AlphaGenome Atlas |
| 英文 tagline | Google's AI map of every possible human DNA mutation |
| 中文 tagline | 谷歌绘制的「人类 DNA 每一位点突变 AI 地图」 |
| 官网 | https://alphagenome.google/atlas （301 跳转至 https://deepmind.google.com/science/alphagenome/atlas） |
| PH 页 | https://www.producthunt.com/products/alphagenome-atlas |
| 品类标签 | Health & Fitness · Artificial Intelligence（PH 展示为 Medical） |
| 票数 / 评论 | 120 / 12（PH 另显示 136 followers） |
| 公司主体 | Google DeepMind（Google 旗下 AI 研究实验室） |

## 是做什么的（如实复述，不评价）

AlphaGenome Atlas 是 Google DeepMind 在 AlphaGenome 模型基础上推出的**预计算变体效应数据库 + 可视化查询门户**：把 AlphaGenome 对"人类基因组中每一个可能的单字母 DNA 变化（共约 9 billion / 90 亿个单核苷酸变体）"的预测结果一次性算好，形成一个 1 PB 的数据集。研究者不需要写代码就能在 Web 门户里浏览、按基因/变体查询，也支持通过 AlphaGenome API 程序化访问、以及作为 skill 接入 Google Antigravity。

它是**数据库/查询界面**（Atlas），不是新的预测模型本身——模型是 AlphaGenome（2026-01-22 由 DeepMind 公布，论文见 arXiv 2506.05588，2026 年登 Nature）。

## 解决什么问题（事实层面）

- 人类基因组约 98% 是非编码区，传统方法难以系统解读；AlphaGenome 模型的目标是预测非编码 DNA 变异对基因调控的影响。
- 过去研究者想回答"我的基因区域里每个可能的点突变有什么影响"必须自跑模型、复现管线。Atlas 把这件事提前算完并以可查询形式公开。
- 通过整合 AlphaMissense 的编码区预测，生成统一的 **AlphaGenome Variant Impact（AVI）** 分数，让研究者能同时在编码区与非编码区对变体进行排序与优先级筛选。
- 公布时给出的早期用例：Broad Institute 的 Laura Covill 用 AVI 分数在 DNM1 基因上解决一例罕见病（epileptic encephalopathy）；Gareth Hawkes 在 5.4 万 UK Biobank 样本中发现 22% 更多的非编码关联位点、识别 19 个 BMI 相关新位点。

## 怎么做的（技术原理/机制）

- **底层模型 AlphaGenome**：基于 Transformer + CNN 的统一 DNA 序列模型，输入长度可达 1 million base pairs，输出单碱基分辨率下的多种功能性预测（基因表达、剪接、染色质可及性、接触图谱等）。
- **预计算规模**：90 亿个单核苷酸变体 × 全基因组覆盖，输出约 1 PB 数据；据 Google 公开描述，规模约为 AlphaFold Database 的 30 倍。
- **AVI 分数**：将 AlphaGenome（调控/非编码）与 AlphaMissense（编码区错义突变致病性）预测合成单一指标，并提供 feature attribution 拆解"哪种分子过程被破坏"（如 RNA 剪接、基因表达等）。
- **额外组件**：2500+ 反复出现的 DNA 序列 motif（基因组"单词"）及其位置索引，便于转录因子行为分析。
- **访问层**：
  - 免代码 **Web 门户**（`alphagenome.google/atlas`）；
  - Python **API 客户端**（`google-deepmind/alphagenome` 仓库，Apache-2.0）；
  - **Google Antigravity skill** 形态；
  - 后续将上线 **Google Cloud** 上的商业化访问。
- **预计算 vs 实时**：预计算的 Atlas 查询配额高于按需 API；按需 API 文档明示"不适合需要超过 1 million 次预测的分析"。

## 团队 / 背景 / 融资

- 隶属 **Google DeepMind**，由 AlphaGenome Atlas 团队发布；牵头人在公开报道中提及 **Pushmeet Kohli**（VP Science, DeepMind）与 **Žiga Avsec**（Genomics Initiative Lead, DeepMind）。
- 协作机构在报道中被点名：**Broad Institute**（Laura Covill）、**University of Exeter**、**Stowers Institute**、**Harvard** 等；UK Biobank 数据用于人口遗传学验证。
- 资金来源：Google 内部投入，非独立融资项目。
- **PH 上的 hunter / 提交人**显示为 **Justin Jincaid**（个人 PH 用户，与团队无明确所属关系；PH 该产品页也关联其个人项目 Mom Clock）。

## 定价 / 商业模式

- **学术研究**：Web 门户 + API **免费**（API 当前条款明确为 **非商用 only**，商用条款见 `deepmind.google.com/science/alphagenome/terms`）。
- **商业化**：Google 公开口径"商用将通过 Google Cloud 推出"；具体定价、SLA、上线时间未披露。
- 模型权重：可通过 Kaggle / Hugging Face 加载，须遵守 DeepMind 的非商用模型条款。
- 限制：按需 API 不适合 >1 million 预测规模；预计算 Atlas 查询享有更高配额。

## 关联信息 / 生态

- **同源项目**：
  - **AlphaGenome**（底层模型，2026-01-22 公布；Nature 论文 + arXiv 2506.05588）。
  - **AlphaMissense**（DeepMind 的错义突变致病性预测模型，是 AVI 分数的编码区来源）。
  - **AlphaFold**（蛋白结构预测；Atlas 数据规模被表述为"约 30× AlphaFold Database"）。
- **同类/相关变体效应工具**：DeepVariant（Google Brain 团队的变体识别 CNN，开源；与 AlphaGenome 关注点不同，DeepVariant 解决"从测序读段识别变体"，AlphaGenome 解决"变体有什么功能影响"）。
- **PH 页相似产品推荐**：Eden AI、FutureTools.io、Baseten、Hasura、Docus.ai（与本产品技术关联度低，属 PH 算法推荐）。

## 技术时间线

| 日期 | 事件 |
|---|---|
| 2025-06-05 | AlphaGenome 预印本首发至 arXiv（2506.05588）。 |
| 2026-01-13 | DeepMind 博客"A glimpse of the future with AlphaGenome"；同日 `deepmind.google/alphagenome` 上线，API 进入非商用研究开放。 |
| 2026-01-22 | Google 官方博客"An atlas for human genomics"等系列文章介绍 AlphaGenome 整体。 |
| 2026-09-08 | **AlphaGenome Atlas 在 Google DeepMind 官方博客发布**（PH 早一天前预热/同一周节奏）。 |
| 2026-09-09 | 上榜 Product Hunt 当日榜 #8。 |
| 未定 | 商业化访问（Google Cloud）；持续扩展预计算覆盖与模型升级。 |

## 评论区反馈（事实摘录，不评价）

> 以下为 PH 产品页前 7 条可见评论（按时间倒序），摘录 1-3 条最有信息量。

1. **Abdul Rehman**（8h，评论）："9 billion DNA variants mapped and free to explore, no coding needed. Feeling like a really big deal for genetics research. Bookmarking this."（强调 90 亿变体 + 免费免代码的访问门槛，被其他用户作为"重大发布"信号引用）
2. **Olivia Bennett**（8h）："9 billion variants in one resource is hard to wrap your head around. How fast can researchers explore the dataset?"（关注查询性能与数据集浏览速度，触及 Atlas 与按需 API 的配额差异）
3. **Victor Guichard**（8h，2 up）："The non-coding DNA part is really interesting. Feels like there's a lot to dig into."（聚焦非编码区价值，与官方定位一致）

> 多位评论者（Fletcher Oliver、Indigo Carpiniello）将 AlphaGenome Atlas 类比为"AlphaFold 时刻"；该类比属评论者主观感受，本档案不背书。

## 信息来源

- **PH 产品页**：https://www.producthunt.com/products/alphagenome-atlas
- **Google 官方博客（AlphaGenome Atlas 发布文）**：https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/
- **Google DeepMind 博客（Atlas 详细介绍）**：https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/
- **DeepMind AlphaGenome 总览页（含 API 入口）**：https://deepmind.google/alphagenome/（亦可经 https://deepmind.google.com/science/alphagenome/atlas 进入 Atlas 门户）
- **AlphaGenome 预印本（arXiv）**：https://arxiv.org/abs/2506.05588
- **AlphaGenome 论文 PDF（DeepMind 存储）**：https://storage.googleapis.com/deepmind-media/papers/AlphaGenome.pdf
- **API 客户端仓库**：https://github.com/google-deepmind/alphagenome（Apache-2.0，模型代码仓库：`google-deepmind/alphagenome_research`）
- **API 文档站**：https://www.alphagenomedocs.com/

## 未查到 / 待补

- **商业化定价 / Google Cloud 上线时间**：官方仅说"coming soon"，无具体时间表与价目。
- **Nature 论文具体卷期 / DOI**：搜索引擎未直接命中，确认出版事实但未抓到正式 DOI；待 arXiv 2506.05588 转入 Nature 后补全。
- **PH 提交人 Justin Jincaid 与 Google DeepMind 的关系**：PH 页面将其标为 hunter/maker，未见 DeepMind 官方公示其团队成员身份；推测为 PH 社区用户代为发布（产品本身确为 DeepMind 官方出品），但**未找到权威来源确认**。
- **模型具体参数量 / 训练数据规模 / 训练能耗**：技术博客与论文摘要均未在公开页面给出，参数量、token 数等细节需查 arXiv 全文 / Nature 正式版。
- **Atlas 数据集在国内的可访问性**：未查到任何关于中国/中文区访问限制或本地化的说明。
- **PH 完整评论数**：产品页显示"comments continue on page 2"，本档案仅记录前 7 条可见评论。
