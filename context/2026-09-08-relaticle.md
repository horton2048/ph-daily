---
product: "Relaticle"
slug: "relaticle"
date: "2026-09-08"
rank: 8
votes: 101
comments: 17
category: "SaaS"
subcategory: "AI 原生 CRM"
tags: ["CRM", "开源", "自托管", "MCP", "审批门", "本地数据"]
tech_stack: ["PHP 8.5", "Laravel 13", "Filament 5", "Livewire 4", "PostgreSQL 17", "Redis", "Docker"]
platform: ["Web", "Self-hosted", "MCP", "REST API"]
open_source: true
license: "AGPL-3.0"
business_model: "开源免费 + 托管服务"
pricing_start: "自托管免费"
funding_stage: "未披露"
funding_amount: ""
related_products: ["Attio", "HubSpot", "Twenty", "Salesforce"]
maker_previous: []
key_signals: ["所有 AI 新增、修改、删除操作必须人工批准后才写入 CRM", "MCP 提供 37 个工具并支持 Claude、GPT 或本地 Ollama", "AGPL 自托管版不限席位且数据留在自有服务器"]
archived_at: "2026-09-09"
sources_count: 4
---

# Relaticle · 扩展阅读上下文

> PT 2026-09-08 Product Hunt 榜单第 8 · 👍 101 · 💬 17  
> 归档日期 2026-09-09 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Relaticle |
| 英文 tagline | Open-source CRM with approval-gated AI writes |
| 中文 tagline | 所有 AI 写操作都需审批的开源 CRM |
| 官网 | https://relaticle.com/ |
| PH 页 | https://www.producthunt.com/products/relaticle |
| 品类标签 | Open Source / AI / GitHub |
| 票数 / 评论 | 101 / 17 |
| 公司主体 | Relaticle（法律主体未查到） |
| 企业版/关联站点 | Relaticle Cloud；自托管版 |

## 是做什么的（如实复述，不评价）

Relaticle 是面向人与 AI Agent 协作的开源 CRM，支持公司、联系人、机会、任务等业务数据。它提供 MCP、REST API 和内置 AI 助手；自托管与 Cloud 使用同一开源代码和数据 schema。

## 解决什么问题（事实层面，不判断值不值得解）

- 传统 CRM 的 AI 接入常受封闭接口与席位计费约束。
- Agent 写入客户数据存在误改、误删风险，需要人在落库前审阅。
- 开发者团队希望控制数据存储位置并按自身字段模型扩展。

## 怎么做的（技术原理/机制，事实层面）

- MCP server 提供 37 个 CRM 操作与分析工具，另有完整 CRUD REST API。
- AI 的 create/update/delete 先生成 proposal card，展示字段及旧值→新值；用户批准后才执行，批量删除为全有或全无。
- 提供 22 种自定义字段、字段级加密、5 层授权与 team-scoped 隔离；项目称有 2,000+ 自动测试。
- 自托管可通过 Docker Compose 部署；AI 可配置 Claude、GPT 或本地 Ollama。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | 未在官方页核实姓名 | 官网/GitHub |
| 融资 | 未查到 | 公开搜索 |
| 投资方 | 未查到 | 公开搜索 |
| 加速器 | 未查到 | 公开搜索 |
| 合规认证 | 未披露 | 官网 |

## 定价 / 商业模式

AGPL-3.0 自托管版免费、无限用户；Cloud 托管方案存在，但本次公开抓取未获得价格。自托管所需模型 API 与服务器费用由使用者承担。

## 关联信息 / 生态

- GitHub README 显示约 1.6k stars、192 forks（抓取当日快照，会变化）。
- 自托管最低建议 2 GB RAM/1 core，推荐 4 GB；要求 Docker 20.10+ 与 Compose v2。
- 所有记录类型可 CSV 导出，官方称可在自托管和 Cloud 间迁移。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-08-13 | 审批式 AI 写入帮助页更新 |
| 2026-09-08 | 登上 PH 当日榜第 8 |

## 评论区反馈（事实摘录，不评价）

- PH 可抓取页面未返回 17 条评论正文。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/relaticle（发布定位）
- GitHub：https://github.com/relaticle/relaticle（协议、技术栈、MCP、测试与功能）
- 自托管：https://relaticle.com/self-hosted（部署、数据位置、模型配置与迁移）
- 审批机制：https://relaticle.com/help/ai-assistant/approve-what-the-assistant-changes（proposal 与审批规则）

## 未查到 / 待补

- 团队、融资、Cloud 定价与 PH 评论原文未查到。
