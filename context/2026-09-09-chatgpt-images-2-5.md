---
# 结构化元数据（用于索引和聚合）
product: "ChatGPT Images 2.5"
slug: "openai"
date: "2026-09-09"
rank: 3
votes: 198
comments: 2

# 分类标签
category: "消费级应用"
subcategory: "AI 图像生成"
tags: ["OpenAI", "ChatGPT", "AI 生图", "多模态", "原生图像生成", "Sketch-to-image", "API"]

# 技术信息
tech_stack: ["GPT-Image-2.5 Flare", "GPT-Image-2.5 Sunburst", "OpenAI API", "Codex"]
platform: ["Web", "iOS", "Android", "API", "Codex"]
open_source: false
license: ""

# 商业信息
business_model: "Freemium（ChatGPT 内置）+ API 按 token 计费"
pricing_start: "免费（ChatGPT 内置，含 Free/Plus/Pro/Team/Enterprise 全部档位）；API $30/M output tokens"
funding_stage: "未披露（OpenAI 母公司）"
funding_amount: ""

# 关联信息
related_products: ["DALL·E 3", "GPT Image 1", "GPT Image 1.5", "Midjourney", "Stable Diffusion", "Adobe Firefly", "Google Imagen"]
maker_previous: []

# 速览信号（给 caption.md / INDEX.md 等下游用，避免整篇重读正文才能省 token）
key_signals:
  - "ChatGPT 内置图像生成的 2.5 升级，相对 2.0 生成延迟最高降低 50%"
  - "API 拆成两档：Flare（默认/快） + Sunburst（精确/慢），双 SKU 同时上线"
  - "新增 Sketch-to-image（@Sketch 在聊天框手绘）与图像局部圈选批注两大交互"
  - "OpenAI 官方披露 ChatGPT Images + API 周生成图像数已超 30 亿张"

# 元信息
archived_at: "2026-09-10"
sources_count: 4
---

# ChatGPT Images 2.5 · 扩展阅读上下文

> PT 2026-09-09 Product Hunt 榜单第 3 名 · 👍 198 · 💬 2
> 归档日期 2026-09-10 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | ChatGPT Images 2.5 |
| 英文 tagline | Sharper visuals, faster flow, better creative control |
| 中文 tagline | 更锐利的视觉、更快的生成、更强的创作控制 |
| 官网 | https://chatgpt.com/images（PH 上挂在 openai 公司主页） |
| PH 页 | https://www.producthunt.com/products/openai |
| 品类标签 | Design Tools · API · Artificial Intelligence（PH） |
| 票数 / 评论 | 198 / 2（PH 页；hunt 描述显示 199 points，两口径并存） |
| 公司主体 | OpenAI |
| 企业版/关联站点 | ChatGPT（Free/Plus/Pro/Team/Enterprise）、ChatGPT Work、Codex、OpenAI Images API |
| PH 上挂载页 | OpenAI 公司主页（slug=openai）——这是 OpenAI 在 PH 的第 49 次发布 |
| 上线日期 | 2026-09-09（PT） |

## 是做什么的（如实复述，不评价）

**ChatGPT Images 2.5 是 OpenAI 给 ChatGPT 内置图像生成功能做的 2.5 代升级**。它是"产品形态"（ChatGPT 里的图像生成）+ "底层模型"（GPT-Image-2.5 系列 API）的组合升级。功能形态不变——在 ChatGPT 对话框里出图、对图片做编辑——但底层模型换成了 GPT-Image-2.5，相对 2.0 在生成速度、画质、编辑稳定性上都做了提升。

OpenAI 官方描述："next-generation image model built for sharper details, faster generation, and more precise editing. It helps turn sketches, prompts, and reference photos into polished visuals with better consistency, natural lighting, richer textures, and stronger control across every edit."

产品形态（用户能在 ChatGPT 里看到的新东西）：
- **Sketch-to-image**：聊天框输入 `@Sketch` 直接画草图，模型把草图转成成片
- **Templates**：内置海报、传单、周边、电商产品图等模板
- **Image commenting**：直接在生成的图上圈选/标注，告诉模型"改这里"
- **Prompt sharing**：随图分享提示词，让别人用自己的照片复刻同款风格
- **进度条**：生成过程中显示百分比
- **新画质档**：新增 `xhigh` 与 `max` 两档，最长边最高支持 3840px（4K 横向）

## 解决什么问题（事实层面，不判断值不值得解）

- **生成速度**："Up to 50% lower generation latency vs. Images 2.0" —— 直接对标 2.0 把延迟砍掉一半
- **主体一致性**：参考图（人脸、宠物、纹理如卷发）在多次编辑后仍保留身份特征 —— 解决"改一处、整张脸崩"的老问题
- **多轮编辑稳定**：之前的编辑不会在后续修改中走形 —— "earlier edits hold up across multiple rounds of changes"
- **精细控制**：用户能圈出图中具体区域告诉模型"只改这里"，避免"我只想换背景，模型把整张图都重画了"
- **复杂材质**：皮革、玻璃、毛发等难材质的渲染质量提升
- **专业工作流**：广告、产品图、营销素材这种"出片即可用"的场景

**对 OpenAI 自身的战略意图**（不评价）：
- 紧接 2026-09-03 GPT-6 Astra 发布，是同一个 9 月连发的第二个主力模型
- 营销上把这次发布定位成"AGI 时代的第一个生图模型"，强调多模态输出而非数学/推理基准
- Sam Altman 在 X 上亲自站台推

## 怎么做的（技术原理/机制，事实层面）

### API 模型矩阵（核心升级点）

OpenAI 把底模拆成两个 SKU 同时上线：

| 模型 | 定位 | 适用场景 |
|---|---|---|
| **GPT-Image-2.5 Flare** | 默认档，平衡速度/质量/编辑 | 社交内容、快速原型、高并发批量 |
| **GPT-Image-2.5 Sunburst** | 精确档，慢但更可控 | 广告、产品摄影、需精修的专业工作流 |

两者 API 价格一致，区别在速度-质量权衡上（Sunburst 处理时间更长但更精确）。

### 关键改进机制（官方披露）

- **生成速度**：相比 Images 2.0，Flare 档延迟降低最多 50%（官方原话）
- **主体保持**：人脸/对象/纹理（如卷发）的身份特征在多轮编辑中保持
- **多轮编辑**：之前的编辑不会因后续指令丢失
- **局部编辑**：圈选区域只修改指定部分，其余保持原样
- **草图理解**：支持 chat 内直接画草图作为视觉参考（无需上传图片文件）
- **画质档**：新增 `xhigh` 与 `max`，最高 3840px（4K 横向）
- **进度可见**：ChatGPT 界面增加生成进度条

### 已知局限（第三方测评披露）

- 部分输出仍会出现"AI smudging"（局部模糊/涂抹感）
- 用户手绘草图时模型可能误判比例
- 人体四肢偶尔出现退化
- 演示中有阴影保留原轮廓的情况（给狗穿衣服后阴影没跟着换姿势）

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 产品主体 | OpenAI | PH 页 / 官方公告 |
| PH 上架发起人 | Rohan Chaubey（产品猎人） | PH 页 |
| 站台者 | Sam Altman（OpenAI CEO） | PH 页 + X 推广 |
| 母公司融资 | OpenAI 整体融资节奏，未单列此产品 | 未查到针对此 SKU 的独立融资 |
| 合规 | 跟随 OpenAI 整体合规框架 | 未查到 |

> 注：这是 OpenAI 的产品升级，不是独立创业项目——没有"创始人/独立融资"概念。PH 页将其挂在 OpenAI 公司主页（slug=openai）。

## 定价 / 商业模式

### ChatGPT 内置（消费者侧）
- 对所有 ChatGPT 用户开放：Free / Plus / Pro / Team / Enterprise
- 用户配额随档位变化（具体数字未在官方公告中单列，沿用 ChatGPT 整体配额规则）

### API（开发者侧）

两个新模型共用的 token 定价：

| 项目 | 价格 |
|---|---|
| Text input | $5 / 1M tokens |
| Cached text input | $1.25 / 1M tokens |
| Image input | $8 / 1M tokens |
| Cached image input | $2 / 1M tokens |
| Image output | **$30 / 1M tokens** |

参考每张图成本估算（output only）：
- Low 质量 1024×1024：~$0.006
- Medium 质量 1024×1024：~$0.053
- High 质量 1024×1024：~$0.211
- Max 质量 3840px 横向：未在公开材料中给出估算

**商业模式要点**：
- 对消费者侧：免费档可用 → 拉升 OpenAI 整体订阅粘性（Plus/Pro 用户得到的是更高配额和更快速度）
- 对开发者侧：API 按 token 计费，是 OpenAI 的直接营收
- 与 GPT Image 1.5 的定价对比：Image 1.5 Image output $32/M（高 7%），Image 1 已宣布 2026-10-23 deprecate

## 关联信息 / 生态

### 历史脉络

- **DALL·E 2**：2022-04 发布，ChatGPT 早期生图后端
- **DALL·E 3**：2023-10 发布
- **ChatGPT 原生图像生成（社区称 Images 2.0）**：2025-03-25 发布，后端为 **GPT Image 1**，这是 ChatGPT 把图像"原生集成进 GPT 多模态模型"的转折点
- **GPT Image 1.5**：2025-12-16 发布（同期已被 Image 2 系列取代/即将废弃）
- **GPT Image 2 系列**：社区报道（gptimg2.ai 等），属于 2.0 命名口径下的 API 模型线
- **GPT-Image-2.5（= ChatGPT Images 2.5）**：2026-09-09 发布，本次主角

### 与 PH 上其他 AI 生图产品的关系

PH 同期榜单（如 2026-08 之前的 sample）已多次出现消费级 AI 生图工具，但大多聚焦：
- **模板化/海报工作流**（如 Canva Magic Studio 之类）—— ChatGPT Images 2.5 的 Templates 直接对标
- **角色一致性**（如 photo maker 类）—— 对标其"主体保留"能力
- **设计协同**（如 Figma AI）—— 对标其"圈选批注"能力

OpenAI 用"ChatGPT 入口 + API 双 SKU + 内置草图/模板/批注"这套组合，把消费级生图的工作流入口抢回 ChatGPT。

### 关键数据（官方披露）

- **周生成图像数超 30 亿张**（OpenAI 官方在 2.5 发布材料中披露，覆盖 ChatGPT Images + GPT-Image API 全口径）

## 技术时间线（关键节点）

| 日期 | 事件 |
|---|---|
| 2022-04 | DALL·E 2 发布 |
| 2023-10 | DALL·E 3 发布 |
| 2025-03-25 | ChatGPT 原生图像生成（GPT Image 1）发布 |
| 2025-12-16 | GPT Image 1.5 API 发布 |
| 2026-09-03 | GPT-6 Astra 发布（OpenAI 同周另一个主力模型） |
| 2026-09-09 | **ChatGPT Images 2.5（GPT-Image-2.5 Flare + Sunburst）发布** |
| 2026-10-23 | GPT Image 1 API 计划废弃（社区资料；OpenAI 文档未在本次公告中再次强调） |

## 评论区反馈（事实摘录，不评价）

- **Oğuzhan Kayan**（4 小时前）："Our marketing team uses gpt-image-2 a lot! 2.5 will be great to have! Congrats!"
  - 印证：gpt-image-2 是本次 2.5 之前已被营销团队广泛使用的版本

> 注：PH 上评论仅 2 条，相对其他上榜产品（动辄 30-70 条）显著偏低——可能因为 OpenAI 在 PH 主页挂新功能后，主流讨论集中在 X/官方公告/科技媒体，PH 评论区未成主战场。

## 信息来源

- **PH 产品页**：https://www.producthunt.com/products/openai
  - 拿到：tagline、198 票 / 2 评论、上线日期、launch team（Rohan Chaubey + Sam Altman）、49 次发布计数、评论原文
- **OpenAI 官方博客**：https://openai.com/index/images-2-5/（HTTP 403 未直接抓到，但通过搜索引擎拿到摘要）
  - 拿到：完整改进列表（50% 延迟降低、Sketch/Templates/Commenting/Prompt sharing 等）
- **OpenAI API 文档**：https://platform.openai.com/docs/guides/image-generation
  - 拿到：token 计费规则、模型列表、画质档定义
- **公开报道**：
  - 36kr「AGI时代的第一个生图模型, ChatGPT Images 2.5上线」—— 拿到 AGI 营销框架背景
  - 今日头条「OpenAI最强AI生图模型：ChatGPT Images 2.5登场，延迟降低50%」—— 拿到细节
  - 163.com、sina.cn、qq.com 同步报道 —— 交叉印证核心改进点
  - 第三方分析（gptimg2.ai 中文博客）—— 拿到 gpt-image-2 vs 1.5 的 API 价格对比
- **GitHub**：未查到（OpenAI 极少开源模型权重，无信号）

## 未查到 / 待补

- 2026-09-09 当天 OpenAI 官方公告的完整 URL 与发布日期确切时间（PT vs 北京时间）
- API 文档中关于 GPT-Image-2.5 Flare 与 Sunburst 的 max quality 3840px 实际 token 成本估算
- Codex 集成 GPT-Image-2.5 的具体调用方式（"Codex users"被官方提及但未见细节）
- "Templates"功能目前的模板数量、来源（OpenAI 自建 vs 用户共享）
- ChatGPT 各档位的 Images 2.5 具体配额数字
- 相对 Images 2.0 的 benchmark 对比数据（除"50% 延迟"外，无准确率/胜出率等可量化指标公开）
- 是否影响现有 GPT Image 1.5 / GPT Image 2 用户的迁移路径与弃用时间表
