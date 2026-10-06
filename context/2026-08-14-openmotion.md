---
# 结构化元数据（用于索引和聚合）
product: "Openmotion"           # 产品名（英文原名）
slug: "openmotion"              # PH slug（文件名用）
date: "2026-08-14"              # 上榜日期 YYYY-MM-DD
rank: 10               # 榜单排名
votes: 90              # 票数
comments: 1              # 评论数

# 分类标签
category: "设计工具"          # 主品类
subcategory: "AI 动效/宣传视频生成"          # 子品类
tags: ["Claude Code", "Codex", "本地优先", "免费", "macOS"]              # 特征标签

# 技术信息
tech_stack: ["Claude Code", "Codex"]        # 依托用户已有的 Claude Code / Codex 订阅作为 AI 引擎
platform: ["Mac"]        # 平台，官网明确 Apple Silicon + Intel 原生构建
open_source: false    # 是否开源，未查到公开仓库（注意与同名开源项目 open-design 不同，见下方说明）
license: ""            # 开源协议（若开源）

# 商业信息
business_model: "免费（未来可能推出 Pro 计划）"    # Freemium
pricing_start: "免费"     # 起步价
funding_stage: "未查到，推测未融资/独立开发"     # 融资阶段
funding_amount: "未披露"     # 融资金额（若披露）

# 关联信息
related_products: ["Motion", "Motionflare", "motionfly.co", "motionvid.ai", "open-design（nexu-io，开源，功能相似但为不同项目）"]  # 相关产品
maker_previous: []  # 未查到创始人过往产品

# 速览信号
key_signals: ["复用用户已有的 Claude Code / Codex 订阅作为 AI 引擎，无需单独 API key", "免费 macOS 原生应用（支持 Apple Silicon 与 Intel）", "输出可在真实画布/时间轴上二次编辑图层、时间、缓动、镜头、音效，而非一键黑盒生成", "支持导出 MP4、透明 WebM、可自包含的 HTML 网页版"]

# 元信息
archived_at: "2026-08-14"       # 归档时间戳
sources_count: 2       # 信息源数量
---

# Openmotion · 扩展阅读上下文

> PT 2026-08-14 Product Hunt 榜单第 10 · 👍 90 · 💬 1
> 归档日期 2026-08-14 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Openmotion |
| 英文 tagline | Turn product screenshots and prompts into motion videos |
| 中文 tagline | 把产品截图和文字描述变成动效视频 |
| 官网 | https://openmotion.design/ |
| PH 页 | https://www.producthunt.com/products/openmotion |
| 品类标签 | Design Tools / SaaS / Developer Tools |
| 票数 / 评论 | 90 / 1 |
| 公司主体 | 未查到 |
| 企业版/关联站点 | 未查到 |

注意：需与 GitHub 上 nexu-io 团队的开源项目 "open-design"（同样主打"Claude Code 驱动的设计/视频生成"）区分，两者定位相似但未查到隶属关系，本文档所述信息均针对 openmotion.design 官网内容。

## 是做什么的（如实复述，不评价）

Openmotion 是一款免费的 macOS 原生动效设计工具，面向创始人、设计师和开发者。用户用自然语言描述一个画面场景，并可附上产品截图、Logo 或品牌素材包，产品内置的 AI agent 会据此自动搭建一段可编辑的动效视频（产品发布视频、SaaS 讲解视频等）。生成后用户可以在真实的画布与时间轴上进一步调整图层、时间、缓动曲线、颜色、镜头运动和音效，最终导出 MP4。

## 解决什么问题（事实层面，不判断值不值得解）

- 传统一键式 AI 视频生成工具产出结果不可控、不可精调，用户拿到的是"黑盒"成片
- 专业动效/视频编辑软件学习门槛高，非设计背景的创始人和开发者难以独立产出宣传视频
- 目标场景：产品发布视频、SaaS 功能讲解视频、社媒/官网展示素材

## 怎么做的（技术原理/机制，事实层面）

- 复用用户本地已有的 Claude Code 或 Codex 订阅作为 AI 生成引擎，官网明确说明"不需要单独管理 API key"
- 输入形式：自然语言场景描述 + 产品截图/品牌素材
- 输出后仍是"可编辑工程文件"而非最终锁定视频：图层、时间、缓动、颜色、镜头、音效均可在时间轴上二次调整
- 导出格式支持 MP4、透明背景 WebM，以及可自包含运行的 HTML 网页版本
- 原生支持 Apple Silicon 与 Intel 架构的 Mac

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | 未查到具体姓名 | — |
| 融资 | 未查到 | — |
| 投资方 | 未查到 | — |
| 加速器 | 未查到 | — |
| 合规认证 | 未查到 | — |

## 定价 / 商业模式

- 当前为完全免费，官网说明"目前只有一个免费计划"
- 官网提及未来"可能"推出 Pro 计划，提供更高生成额度和更多功能，但未披露具体价格或时间表

## 关联信息 / 生态

- 同类"AI 生成宣传/动效视频"工具：Motion（motion.so，定位"动效设计前沿 agent"）、Motionflare（对标"面向动效视频的 Lovable"）、motionfly.co、motionvid.ai
- 差异化点：Openmotion 明确绑定 Claude Code / Codex 生态，把用户已付费的编码 agent 订阅复用为视频生成引擎，是它区别于纯 SaaS 竞品的核心机制
- 需注意与开源项目 open-design（github.com/nexu-io/open-design，同样主打"你的编码 agent 变成设计引擎"，支持 Claude Code/Codex/Cursor 等 20+ CLI）功能定位高度相似，但未查到两者是否为同一团队或有归属关系，故不作为同一产品处理

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 未查到 | 官网因网络限制未能直接抓取，暂无里程碑信息 |

## 评论区反馈（事实摘录，不评价）

- PH 页面仅 1 条评论，因反爬限制未能抓取具体内容，待补

## 信息来源

- PH 产品页：https://www.producthunt.com/products/openmotion（获取 tagline 与简介摘要，评论区因反爬无法读取原文）
- 官网：https://openmotion.design/（因网络限制未能直接抓取，信息来自搜索引擎摘要）
- 公开报道：未查到独立报道
- GitHub：未见明确开源信号（注意 nexu-io/open-design 为疑似同定位但未确认关联的独立开源项目），未进一步查证归属

## 未查到 / 待补

- 创始人/团队姓名与背景
- 是否融资、公司主体信息
- 与 GitHub 开源项目 open-design 的关系（同一团队 / 无关竞品 / fork 关系均未确认）
- Pro 计划具体价格与上线时间
- PH 评论区完整原文
