# Halo by Scam AI · 扩展阅读上下文

> PT 2026-07-31 Product Hunt 榜单第 6 名 · 👍 162 · 💬 29
> 归档日期 2026-08-01 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Halo by Scam AI |
| 英文 tagline | Know who's real on every video call |
| 中文 tagline | 让每次视频通话都能识别人脸真伪 |
| 官网 | https://scam.ai/halo |
| PH 页 | https://www.producthunt.com/products/scam-ai |
| 品类标签 | Meetings · Artificial Intelligence · Security |
| 票数 / 评论 | 162 / 29 |
| 公司主体 | Reality Inc.（官网页脚 © 2026 Reality Inc.） |
| 企业版站点 | checkreality.ai |

## 是做什么的（如实复述）

Halo 是一个**端侧（on-device）实时深度伪造检测应用**，在视频通话进行中检测合成人脸和换脸。它驻留在 Windows 系统托盘，与 Zoom / Teams / Google Meet / WebEx / Slack 等会议应用并行运行——无需插件、无需浏览器扩展。通话过程中逐帧分析视频画面中的每一张脸（约每秒 4 次），若检测到合成人脸则实时弹出警报。

定位：在**通话进行时**捕获深度伪造，而非事后上传录制录像分析。

## 解决什么问题（事实层面，不判断值不值得）

- **实时视频通话中的合成高管欺诈**：官网引用的核心案例——2024 年工程公司 Arup 一名财务员工加入视频通话，画面中看似其 CFO 和同事，但每一张脸都是深度伪造，该员工授权了 15 笔总计约 $25M 的转账。
- 官网主张：现有深度伪造检测工具多为**事后**分析（上传录制→等待→出报告），决策已做出；没有为"通话进行中"这一时刻设计的工具。
- 目标场景（官网列出）：财务与资金管理（转账审批前核实）、人力资源与招聘（确认面试对象）。

## 怎么做的（技术原理/机制，事实层面）

- **端侧运行**：检测在用户设备本地完成，无云端往返，不录制、不存储、不传输视频帧。帧数据在内存中分析后即丢弃。
- **逐帧扫描**：通话中约每秒 4 次分析视频画面中的每一张脸。
- **安装形态**：下载到 Windows 电脑，驻留系统托盘，紧邻会议应用，不依赖插件或浏览器扩展。官网下载页明确标注"Halo is a Windows-only desktop app"，提供 Windows x64（Intel/AMD）与 Windows ARM64（Snapdragon/Windows-on-ARM）两个安装包；macOS / Linux 暂无对应构建。
- **误报处理**（来自 PH 创始人评论回复）：检测画面质量——光照差、视频抖动、压缩严重、人脸离镜头太远时，不立即判定，而是等待更好数据再决策，避免单帧误报破坏真实关系。
- **检测模型**：API 产品线用 Eva-v1-Fast / Eva-v1-Pro 模型；Halo 端侧应用的具体模型官网未明示。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 联合创始人 | Neo Tiangratanakul（PH 评论区自述 co-founder） | PH 产品页 maker 评论 |
| 种子轮融资 | $2.6M 股权融资 | 官网 About 里程碑（2025-12-15） |
| 领投 | Llama Venture | 官网 About |
| 跟投 | SCVxSBI、Welight Capital、SkyDeck Fund、Beta Fund | 官网 About |
| 加速器 | UC Berkeley SkyDeck（录取率不到 1%，种子前融资） | 官网 About（2025-05-15） |
| 合规 | GDPR 合规 + SOC 2 Type I 认证 | 官网 About（2025-08-25） |

## 定价 / 商业模式

两条产品线，定价不同：

**1. API 检测服务（Eva 模型，按张计费）**
- 自助服务：每月免费 200 张图片（Eva-v1-Fast 模型），超出后 $0.05/张
- 增值功能：自适应防御 +$0.01/张、活体检测 +$0.01/张、极速通道（3s 内响应）+$0.01/张
- 取证功能（企业级）：$500/张，含篡改时间线、证据链文档、法律证据包、专家证人支持
- 企业版：定制价格，含 Eva-v1-Pro、Thinking 高级推理、批量折扣、SLA、专属客户经理

**2. Halo 端侧应用**
- 官网定价页未单独标价，标注"下载 Halo"，支持 Windows
- 本文档生成时未查到 Halo 应用的具体售价

## 关联信息 / 生态

- **检测能力矩阵**：官网列 GenAI 检测、音频深度伪造检测（语音克隆准确率 92%，支持 MP3/WAV/AAC，2025-11-05 发布）、4K 视频分析（2026-01-15）
- **准确率声明**：98.2% 检测准确率，处理时间 4 秒以内（官网 2026-01-15 里程碑）
- **竞品定位**：官网对比表将 Halo 与"云端检测 API"和"平台原生"能力对照，强调实时通话运行、媒体数据留设备、无按分钟云端 GPU 成本
- **关联产品**：企业版独立站点 checkreality.ai
- **GitHub 组织**：github.com/scamai（官网页脚 GitHub 链接指向此处，非 `scam-ai`）。组织公开仓库 7 个、成员 2 人、followers 32。仓库均为辅助资源（org profile `.github`、Halo 安装包更新通道 `halo-releases`——其内部代号 **DeepfakeGuard**，基于 Velopack 更新分发；早期项目 `DeepFakeDefenders` 已归档标注"[DISCONTINUED — reorg 2026]"、`ftc-scam-database` 已归档迁移；`PII_ZERO` 等）。**核心检测模型源代码未开源**，符合闭源商业产品预期。
- **准确率口径差异**：官网里程碑（2026-01-15）声明 98.2% 准确率、4 秒内处理；GitHub org README 则写 "95.3% detection accuracy, processing times under 200ms"。两套数字口径不同（疑似 API 端侧 vs 综合指标），本文采用官网数字并标注"官方称"。

## 技术时间线（官网里程碑）

| 日期 | 事件 |
|---|---|
| 2025-01-05 | 深度伪造检测模型 v0.1 发布（图像+视频） |
| 2025-01-31 | 获 Product Hunt 每日最佳产品 |
| 2025-05-15 | 入选 Berkeley SkyDeck 加速器（种子前） |
| 2025-08-25 | GDPR + SOC 2 Type I 合规 |
| 2025-11-05 | 音频检测发布 |
| 2025-12-10 | GenAI 检测发布（文本/图像/视频） |
| 2025-12-15 | 种子轮 $2.6M |
| 2026-01-15 | 准确率 98.2%、4K 支持 |
| 2026-02-02 | 无代码平台与自助式上线 |

## 评论区反馈（事实摘录，不评价）

- **Raffay Sajjad**（提问）：失败模式——光照差/压缩严重的真实人脸被误判为合成时会怎样？打断通话还是可忽略警告？因为误判会损失真实关系。
- **Neo（创始人）回复**：Halo 先检查画面质量，条件差时收集更多数据或等待光照/画面改善后再决策，不因单帧误报触发警报。
- 评论者 Marcin Michalak、Raffay Sajjad 均表正向反馈。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/scam-ai（创始人评论、产品描述、评论反馈）
- 官网 Halo 页：https://scam.ai/zh-CN/halo（技术原理、对比表、Arup 案例）
- 官网定价页：https://scam.ai/zh-CN/pricing（API 定价、增值功能、企业版）
- 官网 About 页：https://scam.ai/zh-CN/about（融资、加速器、合规、技术时间线）
- GitHub：https://github.com/scamai（组织存在，7 个公开仓库但均为辅助资源：`.github` profile、`halo-releases` 更新通道、`DeepFakeDefenders`/`ftc-scam-database` 已归档、`PII_ZERO` 等；核心检测模型源代码未开源）

## 未查到 / 待补

- Halo 端侧应用本身的具体售价（官网定价页仅列 API/Eva 模型按张计费，未单独标 Halo 应用的售价或订阅档；下载页直接给安装包无价格门槛，是否免费/内测未明示）
- Halo 端侧应用使用的具体检测模型名称（API 线用 Eva-v1-Fast / Eva-v1-Pro，Halo 端侧应用官网未明示模型名；GitHub 仓库未公开模型源码）
- 团队规模、其他联合创始人信息（官网 About 页无 team 章节，仅 PH 评论区查到 Neo Tiangratanakul 一位 co-founder；GitHub 组织成员显示 2 人但未公开身份）
- macOS / Linux 支持计划（官网下载页明确写 "Halo is a Windows-only desktop app"，仅提供 Windows x64 与 ARM64 构建，未见 Mac/Linux 路线图）
