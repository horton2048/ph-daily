---
product: CoreSpeed
slug: corespeed
date: '2026-10-04'
rank: 1
votes: 181
comments: 26
category: AI agent
subcategory: Agent 访问层 / MCP 统一端点
tags:
- MCP
- Agent 基础设施
- 记忆
- OAuth
- 审批策略
tech_stack:
- MCP
- OAuth 2.0
platform:
- Web
- Claude Code
- Codex
- Cursor
open_source: false
license: ''
business_model: Freemium / 订阅制
pricing_start: 免费起；Pro $20/月
funding_stage: 未披露
funding_amount: 未披露
related_products:
- Claude Code
- Codex
- Cursor
maker_previous: []
key_signals:
- 单一 MCP 端点：OAuth 连应用 + 跨 Agent 可携带记忆 + 内置搜索/媒体/社媒工具
- 用自然语言写审批策略；预算上限与活动日志控 Agent 行为
- 免费起步；Pro $20/月（含 1 万积分/月、最多 25 成员）
archived_at: '2026-10-04T21:20:00+08:00'
sources_count: 4
---

# CoreSpeed · 扩展阅读上下文

> PT 2026-10-04 Product Hunt 榜单第 1 · 👍 181 · 💬 26  
> 归档日期 2026-10-04 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | CoreSpeed |
| 英文 tagline | One MCP for everything your agents need: apps, memory, tools |
| 中文 tagline | 给 Agent 一个 MCP：应用、记忆、工具都从此接入 |
| 官网 | https://corespeed.io/ |
| PH 页 | https://www.producthunt.com/products/corespeed |
| 品类标签 | Productivity · Marketing · Developer Tools |
| 票数 / 评论 | 181 / 26 |
| 公司主体 | CoreSpeed（corespeed.io / LinkedIn corespeedhq） |
| 企业版/关联站点 | https://app.corespeed.io/ ；定价 https://corespeed.io/pricing |

## 是做什么的（如实复述，不评价）

CoreSpeed 宣称自己是 Agent 的访问层：授权一次 OAuth 连接应用，把共享或私有记忆、内置工具（媒体生成、网页搜索/抓取、社媒研究等）接到 Claude Code、Codex、Cursor 等 MCP 客户端，通过**一个 MCP 端点**使用。凭证由 CoreSpeed 保管；预算上限、活动日志与 Smart Approval（beta，用自然语言描述审批规则）用于约束 Agent。官网写明可移植：换 Agent 时应用连接、记忆与策略一起带走。规划中能力包括 Agent Drive、Mail、Pay、沙箱等。

## 解决什么问题（事实层面，不判断值不值得解）

- 每个 Agent / 每台机器各自管连接与记忆，云端或无人值守时记忆与密钥难共享
- 为每个服务单独申请 API 与管理密钥成本高
- 需要可审计的花费上限与「先批准再执行」策略

## 怎么做的（技术原理/机制，事实层面）

- 通过 OAuth 2.0 连接服务，官方称不接收密码，只拿作用域令牌
- 单一认证 MCP 端点；可用 `set up https://corespeed.io/SKILL.md` 让 Agent 自助接入
- Smart Approvals：自然语言规则转成可读 authorization 代码；未覆盖动作可设默认运行/询问/拒绝
- Spend cap 在下一次付费调用前截断；全部动作进活动账本
- 内置工具示例：图像/音视频生成、网页搜索与抓取、Agent mail、代码沙箱（营销页列举）
- 宣称连接器规模为「1000+」量级（官网滚动数字；未独立核验）

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | LinkedIn 可见 spencerzhyp 等参与发布；完整创始人名单未查到 | LinkedIn 帖 |
| 融资 | 未查到 | |
| 投资方 | 未查到 | |
| 加速器 | 未查到 | |
| 合规认证 | 未查到 | |

## 定价 / 商业模式

- Free：$0；3,000 积分/90 天；1 成员；200 MB 记忆；30 天历史
- Pro：$20/月；10,000 积分/月；最多 25 成员；2 GB 记忆；1 年历史
- Enterprise：定制（SSO、审计保留、部署选项等）
- 标准连接器免费；优质连接器按次扣积分；记忆操作免费

## 关联信息 / 生态

兼容 Claude、Codex、OpenClaw、Hermes、Cursor 与自定义 Agent。未见开源信号，未查 GitHub。

## 技术时间线

| 日期 | 事件 |
|---|---|
| 2026-09-16 | LinkedIn 公开介绍（连接应用、跨 Agent 记忆、单一 MCP） |
| 2026 | PH 产品页标注 Launched in 2026 |
| 2026-10-04 | 登 PH 日榜第 1 |

## 评论区反馈

本次未抓取到足够可靠的 PH 评论原文（PH 页抓取被拦）。

## 信息来源

- https://corespeed.io/ 、https://corespeed.io/pricing 、https://corespeed.io/pricing.md
- https://www.producthunt.com/products/corespeed（WebSearch 摘要）
- LinkedIn corespeedhq / spencerzhyp 发布帖摘要

## 未查到 / 待补

- 融资与完整创始人名单
- PH 评论原文
- 「1000+ 连接器」独立核验
