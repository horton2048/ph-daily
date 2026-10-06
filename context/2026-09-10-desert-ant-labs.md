---
product: "Desert Ant Labs"
slug: "desert-ant-labs"
date: "2026-09-10"
rank: 7
votes: 99
comments: 3

category: "AI 基础设施 / 模型 API"
subcategory: "端侧(on-device)小型专用模型 SDK"
tags: ["on-device", "端侧推理", "SDK", "Swift", "Kotlin", "WebAssembly", "小型模型", "开源底层+专有封装", "欧洲合规", "数据主权"]

tech_stack: ["Core ML (Apple)", "LiteRT / TFLite (Android)", "WebAssembly (Web)", "Apple Neural Engine", "Parakeet 0.6B v3 (Voz 底层)", "DeepFilterNet 3 (Clear 底层)", "DistilHuBERT (Uhm 底层)", "MobileNetV4-Conv-Medium (Moderator 底层)"]
platform: ["iOS", "macOS", "visionOS", "tvOS", "Android", "Web (WASM)"]
open_source: false
license: "Desert Ant Labs Source-Available License v1.0（非 MIT/Apache；底层模型各自保留开源协议，如 DistilHuBERT/MobileNetV4 = Apache 2.0）"

business_model: "免费层（每 SDK 平台每月 100K MAU 以下）+ 商业授权（超 100K MAU 需 licensing@desertant.com）"
pricing_start: "免费（≤100K MAU/平台）"
funding_stage: "未披露独立融资（母体 Detail 累计 ~$12.62M）"
funding_amount: "未披露独立融资"

related_products: ["Whisper (OpenAI)", "Apple SpeechAnalyzer", "Picovoice Leopard/Cheetah", "Vosk", "DeepFilterNet", "Nvidia Parakeet", "Picovoice Cobra (VAD)", "LiteRT/ExecuTorch"]

maker_previous:
  - "Detail (iPad App of the Year 2025，AI 视频创作 app；2020 创办，HQ Amsterdam)"
  - "Paul Veugen:Usabilla → SurveyMonkey 收购 (~$80M)"
  - "Paul Veugen:Human → Mapbox 收购"

key_signals:
  - "2026-09-08 一次发布 18 个端侧模型（12 stable + 6 beta），覆盖语音/视觉/文本全栈——不是单点工具而是 SDK 矩阵"
  - "Voz 自称 iPhone 上比 Whisper 快 4.7 倍（10 分钟音频 ~2 秒），底层是 NVIDIA Parakeet 0.6B v3 + ANE 优化"
  - "许可证不是 MIT，是 'Desert Ant Labs Source-Available License v1.0'：≤100K MAU 免费，超阈值需商业授权 + 禁训竞品条款"
  - "欧洲团队出身（Detail 同班底，iPad App of the Year 2025），主打 'cerebellum-first' 架构 + 数据不出设备，迎合欧盟合规叙事"

archived_at: "2026-09-10"
sources_count: 6
---

# Desert Ant Labs · 扩展阅读上下文

> PT 2026-09-10 Product Hunt 榜单第 7 · 👍 99 · 💬 3  
> 归档日期 2026-09-10 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Desert Ant Labs |
| 英文 tagline | Small specialized AI models for speech, text, vision |
| 中文 tagline | 面向语音/文本/视觉的端侧小型专用 AI 模型 |
| 官网 | https://desertant.com（同时指向 desertant.ai） |
| PH 页 | https://www.producthunt.com/products/desert-ant-labs |
| Hugging Face 组织 | https://huggingface.co/desert-ant-labs |
| GitHub 组织 | https://github.com/Desert-Ant-Labs |
| 许可证 | Desert Ant Labs Source-Available License v1.0（详见 https://license.desertant.com/1.0 ） |
| 品类标签 | Artificial Intelligence · SDK |
| 票数 / 评论 | 99 / 3 |
| 关注者 | （未查到） |
| 公司主体 | 与 Detail 同班底；未单独披露公司实体 |
| 母体产品 | Detail（iPad App of the Year 2025）— https://detail.co |

## 是做什么的（如实复述，不评价）

为 iOS/macOS/visionOS/tvOS/Android/Web 平台提供一组**端侧(on-device)运行的小型专用 AI 模型**，每个模型只做一个任务（语音转写、降噪、关键短语提取、人脸识别、NSFW 检测等），模型权重和推理全部在用户设备本地完成，**不依赖任何云端 API**。通过 Swift / Kotlin / JavaScript 三套 SDK 暴露，开发者按"每月活跃用户数 × 平台"付费门槛接入。

## 解决什么问题（事实层面，不判断值不值得解）

- **成本/隐私/延迟三角**：很多产品场景并不需要"全宇宙最强的通用模型"，但被云端 API 的每 token 计费、跨境数据传输合规、200ms+ 往返延迟卡住
- **大模型不是够大就够了**：NVIDIA 研究显示 40-70% 的生产 AI 调用其实不需要 frontier 模型（来源：Desert Ant Labs 自述，未独立核实）
- **欧盟合规 / 数据主权**：欧洲团队自述"sovereign default"，数据从不离开设备

## 怎么做的（技术原理/机制，事实层面）

- **"Cerebellum-first" 架构**：小模型始终在线；只有当小模型置信度不足时才回退到更大的本地模型或云端（具体回退策略未披露）
- **平台专属推理后端**：Apple 设备走 Core ML + Apple Neural Engine (ANE)；Android 走 LiteRT；Web 走 WebAssembly
- **底层模型打包 + ANE/WASM 重度优化**：自研包装层 + Apple Neural Engine 优化是把 NVIDIA Parakeet 等开源 checkpoint 压到 ~300× realtime 的关键
- **覆盖任务一览**（12 stable + 6 beta，合计 18 个）：

| 模型 | 任务 | 大小/亮点 |
|---|---|---|
| Voz | 语音转文字（25 语言） | iPhone 上 10 分钟音频 ~2 秒；自称比 Whisper 快 4.7×（底层 NVIDIA Parakeet 0.6B v3） |
| Clear | 音频增强（降噪/去混响/归一化） | 9 MB；5 分钟录音 ~1 秒出棚音质（底层 DeepFilterNet 3） |
| Redact | PII 隐私擦除 | 12 MB；27 语言；实时 |
| Tongue | 语言识别 | 2 MB；3 个词即可判别 84 语言；0.933 准确率 |
| Clips | 高光片段选择 | 284 MB；自述替代 Claude Sonnet、声称 10× 快 / 470× 少能耗 |
| Uhm | 语气词检测（"uh/um"） | 帧级精度，多语（底层 DistilHuBERT, Apache 2.0） |
| Ear | 口语语言检测 | 99 语言 |
| Align | 词时间戳对齐 | 增强 Apple SpeechAnalyzer |
| Emo | Emoji 建议 | （未查到大小） |
| Gist | 主题标签 | （未查到大小） |
| Shapes | 形状识别 | （未查到大小） |
| Title | 标题生成 | （未查到大小） |
| Schemer | JSON 抽取 | （未查到大小） |
| Toxic | 仇恨言论检测 | （未查到大小） |
| Moderator | NSFW 检测 | （底层 MobileNetV4-Conv-Medium, Apache 2.0） |
| Eye | 画面评分 | （未查到大小） |
| Face | 人脸匹配 | （未查到大小） |
| Who | 说话人分离 | （未查到大小） |

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 团队 | Detail 同班底 | 多源 |
| 主要创始人/CEO | Paul Veugen | LinkedIn / 公开报道 |
| 关键成员 | Fredrik Wallin、Lauren Waller、Finn Voorhees | LinkedIn / 公开报道 |
| 团队所在地 | Amsterdam / Montreal / Cape Town / 欧洲多地 | Detail 官方 |
| 母体产品 Detail 融资 | ~$12.62M | Dealroom |
| Detail 投资方 | Connect Ventures（pre-seed 领投 2021-03）、Point Nine Capital（种子轮 €4.3M 2021-07 领投）、Taavet Hinrikus、TQ Ventures、Kleiner Perkins、Air Street、Hustle Fund、Sten Tamkivi、Janis Krūms、Mart Kelder、Alexander Ljung、Hiten Shah、Othman Laraki、Omri Amir | 公开报道 |
| Desert Ant Labs 独立融资 | 未披露 | — |
| 加速器 | 未披露独立加速器（Detail 未参加 YC 等公开加速器） | — |
| 合规认证 | 自述"sovereign default / 数据不出设备"（无第三方 GDPR 合规审计披露） | 官方 |
| Paul Veugen 经历 | Usabilla（创办，被 SurveyMonkey 以 ~$80M 收购）；Human（创办，被 Mapbox 收购）；2020 创办 Detail | LinkedIn |

## 定价 / 商业模式

- **免费层**：≤100,000 Monthly Active Devices / SDK 平台 / 模型 —— 没有 token 计费、没有强制登录
- **商业层**：超过 100K MAU 需向 licensing@desertant.com 申请商业授权
- **底层开源 vs 上层专有**：包装好的 SDK、ANE 优化、模型权重走 Source-Available 协议；底层 checkpoint（Parakeet / DeepFilterNet / DistilHuBERT / MobileNetV4）仍是各自的开源协议（多 Apache 2.0）
- **禁用条款**：不得用输出训练竞品模型（no-compete clause）；需署名
- **企业定制**：未单独披露价格

## 关联信息 / 生态

- 与 OpenAI Whisper、Apple SpeechAnalyzer、Picovoice Leopard/Cheetah、Vosk、Nvidia Parakeet 同台（语音转写赛道）
- 与 DeepFilterNet 同链（降噪）
- 与 LiteRT / Core ML / ExecuTorch 同链（端侧推理基础设施）
- Hugging Face 上 `desert-ant-labs` 组织已公开大量模型权重 + Spaces
- npm 上 `@desert-ant-labs/*` 系列 SDK 包已发布（redact、clear、shapes 等）
- GitHub 上 `Desert-Ant-Labs` 组织有多个仓库：`desert-ant-core`、`clear-kotlin`、`clear-js`、`shapes-swift`、`shapes-kotlin`、`db_exporter`（后者 MIT）

## 技术时间线（已查到的里程碑）

| 日期 | 事件 |
|---|---|
| 2020 | Paul Veugen 创办 Detail |
| 2021-03 | Detail pre-seed $2M（Connect Ventures 领投） |
| 2021-07 | Detail seed €4.3M（Point Nine 领投） |
| 2025 末 | Detail 获 Apple iPad App of the Year |
| 2026-09-08 | Desert Ant Labs 正式发布 18 个端侧模型 + SDK |
| 2026-09-10 | 上榜 Product Hunt 当日榜 #7 |

## 评论区反馈（事实摘录，不评价）

PH 评论仅 3 条，未公开具体内容；Hacker News（dev.to 报道转述）有评论指出 Voz 底层是 NVIDIA Parakeet 0.6B v3、Clear 底层是 DeepFilterNet 3、Uhm 底层是 DistilHuBERT、Moderator 底层是 MobileNetV4——即发布内容更接近"包装 + ANE 优化"而非"自训前沿模型"。Desert Ant Labs 回应：ANE 优化是 ~300× realtime 速度的核心。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/desert-ant-labs（票数/排名/品类标签/logo）
- 官网：https://desertant.com/blog/introducing-desert-ant-labs/（抓到摘要）
- 公开报道 1：https://news.linxi.com.au/news/desert-ant-labs-launches-18-specialised-ai-models-for-on-device-use（团队 + 模型清单 + SDK 矩阵）
- 公开报道 2：https://byteiota.com/desert-ant-labs-ships-18-on-device-ai-models-free（Whisper 4.7× 比较 + 100K MAU 免费门槛）
- 公开报道 3：https://dev.to/breachprotocol/a-new-lab-ships-18-small-models-that-run-entirely-on-your-device-kjp（HN 评论指出底层 checkpoint 来源）
- GitHub：https://github.com/Desert-Ant-Labs（查到 desert-ant-core、clear-kotlin、shapes-swift 等仓库）
- Hugging Face：https://huggingface.co/desert-ant-labs（模型权重托管 + Spaces）

## 未查到 / 待补

- 公司独立法律实体名称 / 注册地（官网未单列）
- Desert Ant Labs 独立融资轮次 / 估值
- 当前生产客户名单（PH 仅 3 条评论，自述没有大规模客户披露）
- License v1.0 全文（license.desertant.com/1.0 WebFetch 被屏蔽，未拉到原文）
- 18 个模型的完整 benchmark 表（官网仅披露 Voz vs Whisper 4.7× 一个数字）
- 各模型的具体内存/电量消耗基线
- 与 Picovoice 等老牌端侧语音玩家的功能/性能横向对比
- "Cerebellum-first" 回退机制的具体触发条件