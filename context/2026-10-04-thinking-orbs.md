---
product: Thinking Orbs
slug: thinking-orbs
date: '2026-10-04'
rank: 10
votes: 76
comments: 1
category: 开发者工具
subcategory: React 状态指示组件
tags:
- 开源
- React
- UI 组件
- AI 状态
- MIT
tech_stack:
- React
- SVG
- TypeScript
platform:
- Web
- npm
- shadcn
open_source: true
license: MIT
business_model: 开源免费
pricing_start: 免费
funding_stage: 未披露
funding_amount: 未披露
related_products: []
maker_previous: []
key_signals:
- 无依赖 React（及 vanilla）动画「思考球」组件，面向 Agent UI 状态
- 多状态：working/reasoning/searching/compacting 等；约 3.8KB gzip
- MIT；npm `@yogesharc/thinking-orbs`；也可 shadcn 拷贝进项目
archived_at: '2026-10-04T21:20:00+08:00'
sources_count: 3
---

# Thinking Orbs · 扩展阅读上下文

> PT 2026-10-04 Product Hunt 榜单第 10 · 👍 76 · 💬 1  
> 归档日期 2026-10-04 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Thinking Orbs |
| 英文 tagline | Animated AI Status Indicator Component Library for React |
| 中文 tagline | 给 React 用的动画 AI 状态指示组件库 |
| 官网 | https://www.thinkingorbs.com/ |
| PH 页 | https://www.producthunt.com/products/thinking-orbs |
| 品类标签 | Open Source · Artificial Intelligence · Design resources |
| 票数 / 评论 | 76 / 1 |
| 公司主体 | 个人开源（Yogesh / yogesharc） |
| 企业版/关联站点 | npm `@yogesharc/thinking-orbs`；GitHub yogesharc/thinking-orbs |

## 是做什么的（如实复述，不评价）

Thinking Orbs 是面向 AI / Agent 界面的状态指示动画组件：用「点状思考球」表达 working、reasoning、searching、background、retrying、compacting、waiting、base 等状态，并有多种 variant。官网宣称无依赖、约 3.8 KB gzip；默认约 20px 可读。提供 React `Orb` 与 vanilla `mountOrb`；形状与渲染器可按需 import 以控制打包体积。支持 reduced motion 静止、可暂停。

## 解决什么问题（事实层面，不判断值不值得解）

- Agent UI 需要可区分的「正在想/搜/压缩上下文」等状态，而非单一转圈
- 希望组件小、无重依赖、可拷贝进设计系统

## 怎么做的（技术原理/机制，事实层面）

- `npm i @yogesharc/thinking-orbs` 或 `npx shadcn@latest add https://thinkingorbs.com/r/orb.json`
- Props：state、variant、size、speed、shape、render、density、dotSize、tilt、paused、label、className
- 可选 shapes：cube/octahedron/tetrahedron/torus；renders：dashes/squares/halftone 等
- 绘制跟 `currentColor`，可用 Tailwind `text-*` 染色

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 作者 | Yogesh（yogesharc.com） | llms.txt |
| 融资 | 未查到；有 Patreon | llms.txt |
| License | MIT | 官网 |

## 定价 / 商业模式

开源免费（MIT）。赞助链接指向 Patreon。

## 关联信息 / 生态

GitHub 镜像/相关仓库抓取时可见不同路径摘要（yogesharc/thinking-orbs 为官网声明源）。未见商业 SaaS。

## 技术时间线

| 日期 | 事件 |
|---|---|
| 未查到 | 首发精确日未查到 |
| 2026-10-04 | 登 PH 日榜第 10 |

## 评论区反馈

PH 1 条；本次未抓取原文。

## 信息来源

- https://www.thinkingorbs.com/ 、https://www.thinkingorbs.com/llms.txt
- npm / GitHub 摘要

## 未查到 / 待补

- 精确 star 数与首发日（不同镜像摘要不一致）
- PH 评论原文
