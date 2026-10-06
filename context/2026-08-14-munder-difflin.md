---
# 结构化元数据（用于索引和聚合）
product: "Munder Difflin"
slug: "munder-difflin"
date: "2026-08-14"
rank: 5
votes: 113
comments: 7

# 分类标签
category: "AI agent"
subcategory: "多智能体编排 / 编码助手外壳"
tags: [开源, 本地优先, Claude Code, 多智能体, 语音交互]

# 技术信息
tech_stack: [TypeScript, "OpenAI Realtime API", WebRTC]
platform: [本地/CLI, Web UI]
open_source: true
license: "MIT"

# 商业信息
business_model: "开源免费"
pricing_start: "免费（需自备各 CLI 的 API Key 或本地模型）"
funding_stage: "未查到/待补"
funding_amount: ""

# 关联信息
related_products: ["DeepSeek Harness", "Hoplite"]
maker_previous: []

# 速览信号
key_signals:
  - "本地多智能体harness，包一层调用Claude Code、Codex、Antigravity(Gemini)、Grok、Kimi Code、Qwen、OpenCode、Crush、GitHub Copilot CLI等9+种编码CLI"
  - "MIT开源免费，本地运行不上传数据；上线即2000+用户、677 GitHub star"
  - "GOD编排者\"Michael\"支持语音交互（OpenAI Realtime API + WebRTC），说话即可派发/终止任务"
  - "官方演示配置：$100/月Claude套餐跑1个Opus编排者+9个Sonnet工作agent，可连续跑数周不触顶"

# 元信息
archived_at: "2026-08-14"
sources_count: 4
---

# Munder Difflin · 扩展阅读上下文

> PT 2026-08-14 Product Hunt 榜单第 5 名 · 👍 113 · 💬 7
> 归档日期 2026-08-14 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Munder Difflin |
| 英文 tagline | Make clones with Claude Code and Codex to do your work |
| 中文 tagline | 用 Claude Code 和 Codex 造出你的克隆体来干活 |
| 官网 | https://munderdiffl.in/ |
| PH 页 | https://www.producthunt.com/products/munder-difflin |
| 品类标签 | Productivity / Developer Tools / AI |
| 票数 / 评论 | 113 / 7 |
| 公司主体 | 未查到/待补（GitHub 作者 chaitanyagiri） |
| 企业版/关联站点 | 未查到/待补 |

## 是做什么的（如实复述，不评价）

Munder Difflin 是一个本地运行的多智能体编排 harness，它不自己造编码 agent，而是把用户已有的终端编码 CLI（Claude Code、OpenAI Codex、Antigravity/Gemini、xAI Grok、Kimi Code、Qwen、OpenCode、Crush、pi.dev、GitHub Copilot CLI）包装成一个"虚拟办公室"里的多个持久化 agent。用户通过一个叫 Michael 的 GOD 编排者下达目标（Goal），Michael 负责拆解、派发、监控这些克隆 agent，可以让它们长时间（数小时到数天）自主推进复杂任务，用户像老板一样"看楼层"巡视进度，也可以让某个克隆代替自己当老板。

## 解决什么问题（事实层面，不判断值不值得解）

- 单个编码 CLI 一次只能推进一个任务，长周期/多线程的工程任务需要人工反复切换、盯着终端
- 用户已经在用 Claude Code / Codex 等多种 CLI，缺一个统一的多 agent 协作和任务派发层
- 希望在自己不在电脑前时，任务仍能继续被自主推进

## 怎么做的（技术原理/机制，事实层面）

- 本地多智能体 harness：agent 之间可以互相消息、路由任务、共享记忆
- GOD 编排者 "Michael" 提供低延迟语音通道（基于 OpenAI Realtime API，WebRTC 传输），用户说话即可创建/分配任务、派发、生成或终止工作 agent，带语音回声确认
- 支持 bring-your-own-keys（自备各家 CLI 的 API Key）以及本地 LLM，本地运行、数据不出本机
- v0.3.3 版本新增内置 Monaco IDE，并支持 GitHub Copilot CLI

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | 未查到确切姓名/待补（GitHub 账号 chaitanyagiri） | GitHub |
| 融资 | 未查到/待补 | - |
| 投资方 | 未查到/待补 | - |
| 加速器 | 未查到/待补 | - |
| 合规认证 | 未查到/待补 | - |

## 定价 / 商业模式

MIT 协议开源，工具本身免费且承诺"free forever"，本地运行；使用成本取决于用户自己接入的各家编码 CLI 的 API 用量（官方举例：$100/月 Claude 套餐可跑 1 个 Opus 编排者 + 9 个 Sonnet 工作 agent）。

## 关联信息 / 生态

- 上线即获 2000+ 用户、GitHub 677 星（数据来自搜索时点，可能已变化）
- 定位为"本地多智能体 harness"，与 DeepSeek Harness（同样标榜 agent harness / 插件化）、Hoplite（云端部署编码 agent）构成同赛道不同切入点：Munder Difflin 强调本地、多 CLI 兼容、语音编排；DeepSeek Harness 强调插件化架构本身；Hoplite 强调云端规模化部署

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 未查到具体日期 | 发布 v0.3.3，新增内置 Monaco IDE 与 GitHub Copilot CLI 支持 |

## 评论区反馈（事实摘录，不评价）

- 未查到 PH 评论区具体内容/待补（WebFetch 访问 PH 页面受限）

## 信息来源

- PH 产品页：https://www.producthunt.com/products/munder-difflin（标题、tagline，正文因访问受限未抓取）
- 官网：https://munderdiffl.in/（因访问受限，信息来自搜索摘要）
- GitHub：https://github.com/chaitanyagiri/munder-difflin（MIT 协议、677 星、项目描述，来自搜索摘要）
- 公开报道：Munder Difflin 官方博客（munderdiffl.in/blog）关于 v0.3.3 发布说明，来自搜索摘要

## 未查到 / 待补

- 创始人真实姓名、团队规模、地理位置
- 是否有融资
- PH 评论区具体问答内容
- 精确的 GitHub star 数量变化和发布时间线
