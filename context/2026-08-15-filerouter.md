---
product: "FileRouter"
slug: "filerouter"
date: "2026-08-15"
rank: 8
votes: 92
comments: 1

category: "生产力工具"
subcategory: "文件管理 / 默认程序路由"
tags: ["Mac", "菜单栏应用", "一次性买断", "独立开发者"]

tech_stack: []
platform: ["Mac"]
open_source: false
license: ""

business_model: "一次性买断"
pricing_start: "$15.99（原价 $19.99，介绍价 8 折，7 天免费试用）"
funding_stage: "未融资（独立开发者产品）"
funding_amount: ""

related_products: ["FileMinutes", "FolderX", "FileBar"]
maker_previous: ["Marked 2/3", "nvUltra", "nvALT", "Bunch"]

key_signals:
  - "解决的是 macOS 默认打开程序的痛点：按文件夹/文件类型自定义规则路由到不同编辑器（如博客文件夹里的 Markdown 用 nvUltra 打开，文档文件夹里的用 VS Code 打开）"
  - "创始人 Brett Terpstra 是资深 Mac 独立开发者，代表作 Marked 2/3、nvUltra、nvALT、Bunch，深耕效率工具十余年"
  - "一次性买断制：$15.99（原价 $19.99），7 天免费试用，不是订阅"
  - "首日排名第 8，92 票，评论区仅 1 条——热度不算高但精准命中 Mac 效率工具的细分需求"

archived_at: "2026-08-15"
sources_count: 3
---

# FileRouter · 扩展阅读上下文

> PT 2026-08-15 Product Hunt 榜单第 8 名 · 👍 92 · 💬 1
> 归档日期 2026-08-15 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | FileRouter |
| 英文 tagline | Take control of files and editors |
| 中文 tagline | 掌控文件该用哪个编辑器打开 |
| 官网 | https://filerouter.app |
| PH 页 | https://www.producthunt.com/products/filerouter |
| 品类标签 | Mac · Productivity · Menu Bar Apps |
| 票数 / 评论 | 92 / 1 |
| 公司主体 | 未查到（独立开发者项目） |
| 企业版/关联站点 | 未查到 |

## 是做什么的（如实复述，不评价）

一个 macOS 菜单栏应用，让用户自定义"哪种文件类型/哪个文件夹的文件"该用哪个编辑器打开，
替代系统默认的"一种文件类型只能绑定一个默认程序"逻辑。提供径向选择器（radial picker）
和自定义规则引擎，双击图片等文件时可以弹出多应用选项菜单。

## 解决什么问题（事实层面，不判断值不值得解）

- macOS 系统默认每种文件类型只能绑定一个默认打开程序，无法按场景区分
- 创始人举例：想让博客草稿文件夹里的 Markdown 用 nvUltra 打开，文档文件夹里的 Markdown
  用 VS Code 打开——系统默认设置做不到
- 图片等文件双击后想要"选哪个 app 打开"的选择权，而不是固定跳到一个程序

## 怎么做的（技术原理/机制，事实层面）

- 作为默认处理程序（default handler）接管指定文件类型的打开事件
- 支持按文件夹、文件类型等条件设置路由规则
- 提供径向菜单（radial menu）做快速选择交互
- 支持复制 POSIX 路径等辅助功能，可设置编辑器优先级顺序
- 未查到底层实现语言/技术栈

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Brett Terpstra，独立 Mac 开发者，代表作 Marked 2/3、nvUltra（与 Fletcher Penney 合作）、nvALT、Bunch，博客写作超 20 年，Overtired 播客主持人之一 | WebSearch |
| 融资 | 未融资，独立开发者项目 | — |
| 投资方 | 无 | — |
| 加速器 | 无 | — |
| 合规认证 | 未查到 | — |

## 定价 / 商业模式

一次性买断制：介绍价 $15.99（原价 $19.99，8 折），7 天免费试用，非订阅制。

## 关联信息 / 生态

- 同类 Mac 文件管理/默认程序工具：FileMinutes、FolderX（菜单栏文件浏览器）、FileBar
- 创始人过往产品线均围绕 Mac 效率/写作工具展开（Markdown 预览 Marked、笔记应用
  nvUltra/nvALT、自动化工具 Bunch），FileRouter 延续同一细分方向

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 未查到 | — |

## 评论区反馈（事实摘录，不评价）

- 创始人 Brett Terpstra 在 PH 产品描述中留言："我一直想更好地控制文件打开的位置"，并给出
  博客/文档文件夹分用不同编辑器、图片文件多选项菜单的具体使用场景

## 信息来源

- PH 产品页：https://www.producthunt.com/products/filerouter（WebFetch 拿到创始人评论、票数、关注者数）
- 官网：https://filerouter.app（WebFetch 拿到定价、功能列表）
- 公开报道：WebSearch "Brett Terpstra developer nvUltra Marked apps indie maker"
- GitHub：无公开开源信号，未查

## 未查到 / 待补

- 具体系统要求（macOS 版本兼容性）
- 底层技术栈
- 用户评论区原文（仅 1 条评论，未取得内容）
- 公司主体/是否个体户
