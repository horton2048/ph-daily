---
product: "Airuncode"
slug: "airuncode"
date: "2026-09-07"
rank: 6
votes: 120
comments: 1
category: "开发者工具"
subcategory: "本地多 Agent 运行时"
tags: ["本地优先", "BYOK", "多 Agent", "自动测试", "Vulkan"]
tech_stack: ["Vulkan", "Vitest", "Jest", "pytest", "Cargo", "GGUF"]
platform: ["Mac", "Windows", "Linux"]
open_source: false
license: ""
business_model: "Freemium + 订阅制"
pricing_start: "免费；Pro $15/月"
funding_stage: "未披露"
funding_amount: "未披露"
related_products: ["Claude Code", "Codex", "Cursor", "OpenCode"]
maker_previous: []
key_signals: ["代码、提示词与执行都留在本机，用户自带模型密钥并直接付供应商价格", "一次提示可触发扫描、Agent 辩论、原子编辑、安全审计和测试自愈", "Pro 每月 15 美元开放多 Agent swarm，token 不加价", "内置 Vulkan 3D 运行时 V-CORE，覆盖 AI 辅助游戏开发"]
archived_at: "2026-09-08"
sources_count: 3
---

# Airuncode · 扩展阅读上下文

> PT 2026-09-07 Product Hunt 榜单第 6 名 · 👍 120 · 💬 1  
> 归档日期 2026-09-08 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Airuncode / AIRUNCODE |
| 英文 tagline | Run multiple local coding agents on your machine |
| 中文 tagline | 在本机运行多个编码 Agent |
| 官网 | https://airuncode.com/ |
| PH 页 | https://www.producthunt.com/products/airuncode |
| 品类标签 | Software Engineering · Developer Tools · Artificial Intelligence |
| 票数 / 评论 | 120 / 1 |
| Maker | Gustavo Arretureta |
| 当前版本 | v1.4.7 |

## 是做什么的（如实复述，不评价）

Airuncode 是跨平台、本地优先的编码 Agent 运行时。它让用户在自己的机器上并行运行多个 Agent，连接自带的云模型密钥或本地 GGUF 模型，直接编辑文件、运行测试并根据失败日志尝试修复；还内置 V-CORE Vulkan 3D 运行时。

## 解决什么问题（事实层面，不判断值不值得解）

- 编码工作流如果绑定单一模型、订阅或云平台，切换供应商和控制成本较困难。
- 多 Agent 方案常需要另建云端编排层，代码和提示可能离开本机。
- Agent 生成代码后，测试、读日志、修复和重跑仍可能需要人工接手。

## 怎么做的（技术原理/机制，事实层面）

- 一个提示触发 `RESEARCH → BUILD → SHIP` 流程：深度扫描代码库、多 Agent 相互质疑方案、原子文件编辑和安全审计。
- 支持 OpenRouter、NVIDIA、DeepSeek、MiniMax、本地 GGUF，以及多家主流模型供应商。
- 自动识别 Vitest、Jest、pytest、Cargo 等测试框架；测试失败后读取日志和 stack trace，以 diff 形式应用修复并重跑。
- 代码和提示保存在本地磁盘；模型费用由用户直接付供应商，Airuncode 不对 token 加价。
- V-CORE 为原生 Vulkan PBR 渲染器，提供地形、着色和实时 3D 能力。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| Maker | Gustavo Arretureta | PH 产品页 |
| 开发动机 | 不希望工作流依赖单一 AI 公司、订阅或模型 | Maker 评论 |
| 融资 | 未查到 | 公开页面 |
| 公司主体 | 未查到 | 公开页面 |

## 定价 / 商业模式

- Free：$0，含每周 2 个 48 小时 key、无限本地模型、成本跟踪和 V-CORE basic。
- Pro：$15/月，含无限 BYOK、多 Agent swarm、上下文快照和 V-CORE full。
- Studio：$49/月，最多 5 个席位，含多工作区、审计记录导出和私有端点。
- 模型 token 按供应商原价另付，产品不加价。

## 关联信息 / 生态

- 与 Claude Code、Codex、Cursor、OpenCode 等编码 Agent 工具相邻，但定位为可替换模型的本地运行时层。
- 支持 Mac、Windows、Linux。
- 官网未见开源声明或代码仓库入口，因此未查 GitHub。

## 技术时间线

| 日期 | 事件 |
|---|---|
| 2026-09 | v1.4.7 面向 Windows、macOS、Linux 提供下载 |
| 2026-09-07 | 登上 Product Hunt 日榜 |

## 评论区反馈（事实摘录，不评价）

- Maker 主动询问试用者：哪些地方损坏或令人困惑，以及什么条件能让它成为日常编码 Agent。
- Maker 表示仍在重建 PWA，并计划加入集中讨论更新、bug 和功能的社区/论坛。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/airuncode（定位、Maker、平台和评论）
- 官网：https://airuncode.com/（运行机制、支持模型、测试流程、版本与定价）
- 公开评测：https://www.stork.ai/en/airuncode（定价与产品信息交叉核对）

## 未查到 / 待补

- 是否存在公开代码仓库、许可证与安全审计报告
- 本地 Agent 的进程隔离、权限沙箱和密钥存储方式
- 公司主体、团队规模和融资情况
