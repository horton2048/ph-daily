---
# 结构化元数据（用于索引和聚合）
product: "Keystroke"
slug: "keystroke"
date: "2026-08-05"
rank: 7
votes: 153
comments: 0

# 分类标签
category: "开发者工具"
subcategory: "AI 代理构建平台 / 工作流自动化"
tags: [AI代理, 工作流, 开源, YC, 集成, TypeScript, 自动化, 触发器, 无代码/低代码]
tech_stack: [TypeScript, n8n替代]
platform: [Web, CLI, 终端]
open_source: true
license: "开源（具体协议未查到）"

# 商业信息
business_model: "开源 + 云平台订阅"
pricing_start: "首次赠送 $20 信用额度"
funding_stage: "YC 孵化"
funding_amount: "未披露"

# 关联信息
related_products: [n8n, Composio, Zapier, AgentOps]
maker_previous: []

# 元信息
archived_at: "2026-08-10T13:06:22Z"
sources_count: 2
---

# Keystroke · 扩展阅读上下文

> PT 2026-08-05 Product Hunt 榜单第 7 · 👍 153 · 💬 未查到  
> 归档日期 2026-08-10 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Keystroke |
| 英文 tagline | Build powerful AI agents and workflows（构建强大的人工智能代理和工作流程） |
| 中文 tagline | 构建强大的人工智能代理和工作流程 |
| 官网 | https://www.buster.so/（Keystroke 产品页面） |
| PH 页 | https://www.producthunt.com/products/keystroke-2 |
| 品类标签 | 开发者工具 / AI 代理构建 · 工作流自动化 |
| 票数 / 评论 | 153 / 未查到 |
| 公司主体 | Keystroke HQ（keystrokehq） |
| 企业版/关联站点 | YC 孵化项目 |

## 是做什么的（如实复述，不评价）

Keystroke 是一个一体化平台，用于构建 AI 代理（agents）与工作流自动化。用户只需描述需要的助手，Keystroke 就会构建它、连接工具、进行测试并部署到共享工作区。可为助手赋予记忆、工作流程、触发器、审批权限，并接入 1000+ 应用集成。官方定位"为编码代理而生的 n8n 替代品"——即如果 n8n 是为 Claude Code、Cursor 等编码代理而构建的样子。所有构建内容都是仓库中实际的 TypeScript 代码，可推送到 Keystroke 平台，管理凭证、用量、日志、共享与访问控制。

## 解决什么问题（事实层面，不判断值不值得解）

- 解决工作流自动化对非技术/非编码用户的门槛：描述需求即可构建 AI 助手。
- 解决代理与业务工具脱节问题：接入 1000+ 应用集成，连接工具并部署到共享工作区。
- 解决编码代理生态中缺少 n8n 式自动化编排的问题：让 Claude Code、Cursor 等编码代理直接构建代理与自动化。
- 解决凭证/访问控制管理问题：集中管理 credentials、usage、logs、sharing、access controls。
- 解决内部代理/自动化部署慢的问题：官方称"几分钟内部署内部代理与自动化"，支持计划、事件（如 Stripe 支付成功、通话结束）等触发器。

## 怎么做的（技术原理/机制，事实层面）

- 无代码/描述式构建：用自然语言描述所需助手，平台生成并组装代理。
- 代码即配置：所有构建内容都是实际 TypeScript，存在于用户仓库中（如 agents/kevin.ts，使用 @keystrokehq/keystroke/agent 定义）。
- 与编码代理集成：连接 Claude Code、Cursor 等编码代理进行构建。
- 平台部署：通过 CLI（如 keystroke deploy）将构建推送到 Keystroke 平台。
- 触发器与自动化：计划触发器、Stripe 支付事件、通话结束等触发自动化工作流。
- Agent Composer 2.5：平台的代理构建/编排组件。
- 开源 + 云平台：开放源代码，同时提供云平台用于管理凭证、用量、日志、共享、访问控制。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | 未查到 | — |
| 融资 | 获得 Y Combinator 支持（YC 孵化） | CSDN 上榜介绍 |
| 投资方 | 未查到（YC 为孵化器） | — |
| 加速器 | Y Combinator | CSDN 上榜介绍 |
| 合规认证 | 未查到 | — |

## 定价 / 商业模式

开源 + 云平台订阅。首次尝试免费获得 $20 信用额度。云平台（凭证管理、部署、日志、访问控制）具体订阅定价未查到。

## 关联信息 / 生态

- 竞品定位：自称"为编码代理而生的 n8n 替代品"，对标 n8n（工作流自动化），也涉及 Zapier、Composio（1000+ toolkits）等自动化/工具集成领域。
- 生态：面向编码代理（Claude Code、Cursor 等），构建结果以 TypeScript 存入用户仓库，可推送到平台。
- 开源生态：开放源代码，允许自托管/定制。

## 技术时间线（官网里程碑，若有）

未查到（无明确公开版本时间线；提到 Agent Composer 2.5 组件）。

## 评论区反馈（事实摘录，不评价）

未查到（PH 评论区不可访问）。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/keystroke-2（URL 确认，内容被 Cloudflare 拦截）
- CSDN 每日热榜镜像：https://blog.csdn.net/Jackxiaochen/article/details/163542498（tagline、中文介绍、票数 🔺153、关键词、发布时间 2026-08-05、YC 支持、$20 信用额度）
- 官网：https://www.buster.so/（n8n 替代定位、Agent Composer 2.5、TypeScript 代码构建、CLI 部署、凭证/日志/访问控制、触发器示例）

## 未查到 / 待补

- 创始人 / 团队信息
- YC 具体批次 / 融资金额
- 开源仓库地址与具体许可证
- 云平台订阅定价
- 评论数与评论区内容
- 1000+ 集成的完整清单