---
product: "WeatherNext 3"
slug: "weathernext-3"
date: "2026-09-04"
rank: 7
votes: 123
comments: 1

category: "SaaS"
subcategory: "气象 AI 模型与数据服务"
tags: ["AI 气象", "预报模型", "实时卫星数据", "清洁能源变量", "Google DeepMind"]

tech_stack: ["FGN mesh transformer（Functional Generative Network）", "地球静止卫星实时马赛克输入", "稀疏气象站观测直接训练", "IMERG / 卫星雷达降水再分析", "BigQuery / Earth Engine / Cloud Storage 分发"]
platform: ["Google Search", "Gemini app", "Google Maps", "Google Maps Platform Weather API", "Earth Engine", "BigQuery", "Google Cloud Storage"]
open_source: false
license: ""

business_model: "数据/模型服务（经 Google Cloud 三通道分发，消费端集成进 Google 自有产品）"
pricing_start: "研究/教育/非营利免费（Earth Engine，需注册申请）；商业使用按 Google Cloud 计费"
funding_stage: "Alphabet 体内项目（Google DeepMind + Google Research）"
funding_amount: ""

related_products: ["WeatherNext 2（上一代）", "Weather Lab", "GraphCast（前身研究模型）", "Brightband 独立评测榜", "ECMWF（数据源/对标）"]
maker_previous: ["WeatherNext By Google（同系列上一代曾单独在 PH 发布）"]

key_signals:
  - "训练数据换了：不再吃 NWP 物理模型输出（有 6 小时滞后），直接学实时静止卫星马赛克 + 稀疏站点观测，每小时出一次报"
  - "官方称关键地面变量分辨率到 5 公里，整体锐度约为 WeatherNext 2（25 公里格点、6 小时步长）的 5 倍"
  - "官方称中期降水预报 CRPS 对 IMERG 基线最高提升 60%；新增 100m 风速（风机高度）、云量、辐照等清洁能源变量"
  - "分发即商业化：BigQuery / Earth Engine / GCS 三条数据通道，同日接入 Search、Gemini、Maps；历史数据 CC BY 4.0，实时数据走 GDM 专有条款"

archived_at: "2026-09-05T12:00+08:00"
sources_count: 4
---

# WeatherNext 3 · 扩展阅读上下文

> PT 2026-09-04 Product Hunt 榜单第 7 · 👍 123 · 💬 1  
> 归档日期 2026-09-05 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | WeatherNext 3 |
| 英文 tagline | Our most advanced and accurate global weather AI model |
| 中文 tagline | 我们最先进、最准确的全球天气 AI 模型（tagline 直译，官方自述；"最准确"依据为 Brightband 独立实时评测） |
| 官网 | 官方博客 https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-weathernext-3/（PH 官网重定向指向该博客，无独立产品站） |
| PH 页 | https://www.producthunt.com/products/weathernext-3 |
| 品类标签 | Weather · Artificial Intelligence（PH 页面另列 Weather Apps · Predictive AI，带 Free Options 徽章） |
| 票数 / 评论 | 123 / 1 |
| 公司主体 | Google / Alphabet（Google DeepMind 与 Google Research 联合发布） |
| 企业版/关联站点 | Earth Engine 数据目录（weathernext_3_0_0_0p1deg）、BigQuery、Google Cloud Storage、Weather Lab |

## 是做什么的（如实复述，不评价）

WeatherNext 3 是 Google DeepMind + Google Research 的旗舰全球天气 AI 预报模型，2026-09-03 发布。核心变化：

- **实时观测驱动**：直接从实时观测数据学习（前身主要学习数值天气预报 NWP 模型的输出），用原始卫星数据**每小时产出一次高分辨率全球预报**
- **分辨率**：关键地面变量（温度、湿度）5 公里，其他地面变量 10 公里，大气变量（风速等）25 公里；官方称整体比上一代 WeatherNext 2（25 公里格点、6 小时步长）锐度约 5 倍
- **新增预报变量**：面向清洁能源——100 米高度风速（约风机高度）、高分辨率云量、太阳辐照（帮助风电/光伏估算出力）
- **两种消费形态**：① 研究者/开发者/企业经 BigQuery、Earth Engine 查询或从 GCS 批量下载预报数据（无需自己搭模型）；② 普通用户从 2026-09-03 起在 Google Search、Gemini app、Google Maps、Google Maps Platform Weather API、Earth Engine 中被动用到

## 解决什么问题（事实层面，不判断值不值得解）

- **数据滞后**：多数 AI 气象模型（含 WeatherNext 2）训练自 NWP 模型数据，而 NWP 是超算驱动的物理仿真，带 6 小时数据滞后，对降雨、地表温度等快变变量产生偏差
- **分辨率不够**：传统模型空间分辨率低，无法刻画海岸线、山谷、山脉几公里尺度内的温湿度剧变；区域高分辨率数值模型算力成本高，拉美、非洲、亚太部分地区历史上服务不足
- **降水预报差**：全球模式对降水的预报以模糊估计或漏掉强风暴边界著称
- **清洁能源规划**：电网和新能源开发商需要风机高度风速、地面辐照等变量来预测发电出力

## 怎么做的（技术原理/机制，事实层面）

- **架构**：单个 Flexible Functional Generative Network（FGN）mesh transformer；输入 = 实时 1 小时级地球静止卫星马赛克 + 传统历史分析场；输出 = 密集格点场、离散气旋路径，并原生预测站点级稀疏坐标（官方博客 Fig.1）
- **训练数据（与上一代的关键差异）**：
  - 直接学习实时卫星马赛克 → 每小时一次新预报，均基于最近可得卫星观测
  - 直接学习**稀疏气象站观测数据** → 全球 5 公里格点预报能考虑地形等区域细节
  - 降水用两个高质量源训练：NASA IMERG（多卫星反演）+ Google 自建的基于卫星雷达的全球降水再分析
- **精度声明（官方称，评测基线）**：中期全球预报中，CRPS 相对基线的提升最高为——对 IMERG 60%、对 MRMS 30%、对雨量计 10%（早期预报时效）
- **分发形态（Earth Engine 数据目录核实）**：Earth Engine 集合为 0.1°（约 11 公里）格点、19 个地面变量的集合统计量（mean/p10/p25/p50/p75/p90，共 114 波段）；6 小时起报（00/06/12/18 UTC）时效至 360 小时（15 天），中间 1 小时起报时效 48 小时；完整集合与大气数据走 GCS。注意：博客称模型原生最高 5 公里（0.05°），Earth Engine 上发布的集合统计量为 0.1°，两者口径不同，原文如此
- **数据许可**：历史实验数据 CC BY 4.0；实时实验数据走 GDM Real-Time Weather Forecasting Experimental Data 专有条款；目录注明模型使用了 ECMWF 及第三方数据（致谢页）

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 发布方 | Google DeepMind + Google Research | 官方博客 |
| 博客署名 | The WeatherNext team | 博客元数据 |
| PH 发布团队 | Launch Team 显示 Ankit Sharma、Sundar Pichai（作者字段标注 Sundar Pichai，另有成员被折叠未展开） | PH 页 |
| 融资 | Alphabet 体内项目，无独立融资 | — |
| 背景 | 系列前身：GraphCast（研究模型，曾开源——此为背景知识，本次未重新核验）、WeatherNext 1/2；Earth Engine 目录中 WeatherNext 2 数据集在册 | WebSearch/EE 目录 |

## 定价 / 商业模式

- **数据分发三条通道**：BigQuery（经 Analytics Hub）、Earth Engine、GCS 批量下载（Zarr）；访问需提交 WeatherNext Data Request 表单（申请制），联系方式 weathernext@google.com
- **免费口径**：Earth Engine 对研究、教育、非营利用途免费（需注册）；PH 页带 Free Options 徽章。商业用途按 Google Cloud 计费（BigQuery 按标准查询/存储计费、GCS 按存储/流出计费）——具体价目本次未抓到
- **许可双轨**：历史数据 CC BY 4.0（开放数据）；实时数据专有条款
- **消费端**：Search/Gemini/Maps 内置使用；官方称计划一天以上的行程时降水预报准确度最高提升 50%（历史预报欠佳地区改善最大）
- 博客免责声明：官方预报与灾害预警仍以当地气象机构为准

## 关联信息 / 生态

- **精度背书**：官方称"迄今最先进、最准确"的依据是 Brightband 的独立实时评测榜（博客附榜单独立入口，具体名次本次未抓取）
- **同场 PH 类似品**：WeatherNext By Google（系列上一代发布）、Google Cloud Platform、Rainbow AI（第三方天气 AI）
- **数据生态**：致谢 ECMWF 及第三方数据提供方；与 AlphaEarth Foundations、Earth AI 同属 Google 地理空间 AI 板块（博客文末导流）

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-09-03 | 官方博客发布（15:00 UTC，署名 The WeatherNext team）；同日起接入 Search、Gemini app、Google Maps、Google Maps Platform Weather API、Earth Engine |
| 2026-09-04 | PH 上榜，rank #7（123 票 / 1 评论） |
| （已就位） | Earth Engine 目录 weathernext_3_0_0_0p1deg 已建成（申请制访问；历史数据 CC BY 4.0） |

## 评论区反馈（事实摘录，不评价）

仅 1 条评论，评论者 Gal Dayan，主题围绕新增的清洁能源预报变量（风电/光伏相关变量）。原文要点未完整存档，此为按主题转述，待补。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/weathernext-3（拿到 tagline、描述、品类、Launch Team、Free Options 徽章、类似品）
- 官方博客（经 PH 官网重定向抓取全文）：https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-weathernext-3/（拿到架构、分辨率、训练数据、CRPS 数字、分发渠道）
- Earth Engine 数据目录：https://developers.google.com/earth-engine/datasets/catalog/projects_gcp-public-data-weathernext_assets_weathernext_3_0_0_0p1deg（拿到论文标题 "WeatherNext 3: Increasing resolution and performance of global weather models with raw observations"、0.1° 集合说明、15 天时效、CC BY 4.0/专有条款双轨、ECMWF 致谢）
- WebSearch 摘要：Earth Engine 对研究/教育/非营利免费的政策、BigQuery Analytics Hub/按 GCP 计费的访问方式（developers.google.com、cloud.google.com 相关结果）
- GitHub：未见模型开源信号（数据需申请访问），未查 GitHub

## 未查到 / 待补

- BigQuery/Earth Engine 商用具体价目（仅确认"按 GCP 标准计费 + 申请制"）
- Brightband 榜单上 WeatherNext 3 的具体名次/分数
- 论文全文内容（标题已核实，正文未读）
- 模型参数量、推理成本、数据同化细节
- PH 唯一评论的原文全文
- Earth Engine 目录样例代码按 2026-05-01 起查询，数据集起始可得日期未官方确认
