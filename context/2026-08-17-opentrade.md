---
product: "OpenTrade"
slug: "opentrade"
date: "2026-08-17"
rank: 7
votes: 107
comments: 10

category: "开发者工具"
subcategory: "AI 交易工具包 / 开源 harness"
tags: ["开源", "交易", "Claude Code", "Codex", "MCP", "Robinhood", "cron"]

tech_stack: ["Claude Code", "Codex", "MCP", "Robinhood MCP"]
platform: ["CLI", "GitHub"]
open_source: true
license: "未查到具体协议"

business_model: "开源免费"
pricing_start: "免费"
funding_stage: "未披露"
funding_amount: ""

related_products: ["Claude Code", "Codex", "Robinhood", "HarnessRouter"]
maker_previous: []

key_signals:
  - "开源交易 harness：给 Claude Code/Codex agent 提供交易工具和护栏"
  - "通过 Robinhood 官方 MCP 接入交易，支持 cron 定时任务和后台持久运行"
  - "agent 可自主设置交易计划、执行交易、管理持仓"
  - "创始人 Viraat Das"

archived_at: "2026-08-17"
sources_count: 2
---

# OpenTrade · 扩展阅读上下文

> PT 2026-08-17 Product Hunt 榜单第 7 名 · 👍 107 · 💬 10
> 归档日期 2026-08-17 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | OpenTrade |
| 英文 tagline | Open-source trading harness for Claude Code / Codex. |
| 中文 tagline | 面向Claude Code/Codex的开源交易工具包 |
| 官网 | https://www.producthunt.com/r/VSZ2NL5GB7AXU6 |
| PH 页 | https://www.producthunt.com/products/opentrade |
| 品类标签 | Open Source · Investing · Artificial Intelligence · GitHub |
| 票数 / 评论 | 107 / 10 |
| 公司主体 | 未查到（独立开发者项目） |
| 企业版/关联站点 | 未查到 |

## 是做什么的（如实复述，不评价）

一个开源的交易 harness，为 Claude Code / Codex agent 提供交易工具和护栏。
通过 Robinhood 官方 MCP 接入交易。开箱即用，agent 可以设置 cron 定时任务
和后台持久运行。agent 可以自主设置交易计划、执行交易、管理持仓。

## 解决什么问题（事实层面，不判断值不值得解）

- AI agent 缺少安全交易的工具和护栏
- 交易需要持续运行（定时执行），但 agent 通常只在交互时运行
- 缺少 agent 与券商 API 的标准化接入

## 怎么做的（技术原理/机制，事实层面）

- 开源 harness 封装 Claude Code / Codex agent
- 通过 Robinhood 官方 MCP 接入交易
- 支持 cron 定时任务：agent 可定时执行交易计划
- 后台持久运行：不依赖交互式会话
- 提供"护栏"（guardrails）防止异常交易，具体机制未查到
- 技术栈：Claude Code、Codex、MCP、Robinhood MCP

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Viraat Das（其余 maker 被 PH 标记 [REDACTED]） | PH API |
| 融资 | 未披露 | — |
| 投资方 | 无 | — |
| 加速器 | 未查到 | — |
| 合规认证 | 未查到（涉及交易，可能有合规要求） | — |

## 定价 / 商业模式

开源免费。具体开源协议未查到。无付费层信息。

## 关联信息 / 生态

- 互补品：Claude Code、Codex（agent 工具）、Robinhood（券商）
- 同类：HarnessRouter（前一天 8-16 上榜的统一 harness 接口，概念相似）
- 差异化：专注交易场景的 harness，而非通用 agent 编排
- 开源信号确认（PH 标签含 Open Source + GitHub）

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 未查到 | — |

## 评论区反馈（事实摘录，不评价）

- 未取得评论区原文（10 条评论）

## 信息来源

- PH API：拿到了产品描述、创始人、票数、话题标签
- 公开报道：未单独检索
- GitHub：开源信号确认（PH 标签含 GitHub），未单独查仓库

## 未查到 / 待补

- 开源协议
- GitHub 仓库地址
- 护栏（guardrails）具体机制
- 融资情况
- 评论区原文
