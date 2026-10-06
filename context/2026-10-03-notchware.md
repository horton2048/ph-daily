---
product: Notchware
slug: notchware
date: '2026-10-03'
rank: 8
votes: 71
comments: 1
category: 消费级应用
subcategory: Mac 刘海状态栏
tags:
- Mac
- 刘海
- AI agent 提醒
- 本地优先
tech_stack:
- SwiftUI
platform:
- Mac
open_source: false
license: ''
business_model: Freemium（免费 + Pro 一次性买断）
pricing_start: 免费；Pro 一次性 $3.99
funding_stage: 未披露
funding_amount: ''
related_products: []
maker_previous: []
key_signals:
- 把 MacBook 刘海做成实况岛：现在播放、电量、音量、亮度、专注模式、网络
- Pro：Codex/Claude Code/Cursor 需批准或完成时刘海提醒；锁屏音乐控制
- 本地运行无账号无分析；agent hook 可审阅，只写状态不读 prompt
archived_at: '2026-10-03T21:30:00+08:00'
sources_count: 3
---

# Notchware · 扩展阅读上下文

> PT 2026-10-03 Product Hunt 榜单第 8 · 👍 71 · 💬 1  
> 归档日期 2026-10-03 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Notchware |
| 英文 tagline | Music and AI agent alerts in your MacBook notch |
| 中文 tagline | 在 MacBook 刘海里看音乐和 AI 助手提醒 |
| 官网 | https://ballmac.com/notchware |
| PH 页 | https://www.producthunt.com/products/notchware |
| 品类标签 | Mac · Productivity · Artificial Intelligence |
| 票数 / 评论 | 71 / 1 |
| 公司主体 | Ballmac |

## 是做什么的（如实复述，不评价）

原生 macOS 应用，把带刘海 MacBook 顶部做成动态状态岛：显示正在播放、电量、音量/亮度、Focus、网络；Pro 版用本地 hook 接入 Codex、Claude Code、Cursor，在需要批准或任务结束时提醒，并扩展锁屏音乐控制。

## 解决什么问题（事实层面，不判断值不值得解）

- 刘海两侧空白浪费，查菜单栏成本高
- 跑 AI 编码 agent 时不想一直盯终端

## 怎么做的（技术原理/机制，事实层面）

- SwiftUI；macOS 14.6+ 与带刘海机型
- AI 提醒：可先检查再安装的本地 shell hook，只写状态事件
- 可调岛宽度与指示器；全屏时可隐藏
- 第三方摘要称尚未 Apple notarize，需右键打开

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 开发者 | Ballmac | 官网 |
| 融资 | 未查到 | |

## 定价 / 商业模式

免费核心功能。Pro 一次性约 $3.99，解锁 AI 提醒与锁屏相关能力。

## 关联信息 / 生态

未见完整应用开源（hooks 可审阅 ≠ 应用开源）。

## 技术时间线

| 日期 | 事件 |
|---|---|
| 2026-10-03 | 登 PH 日榜 |

## 评论区反馈

PH 1 条，未展开。

## 信息来源

- https://ballmac.com/notchware
- https://www.productcool.com/product/notchware
- https://www.producthunt.com/products/notchware

## 未查到 / 待补

- notarize 计划
