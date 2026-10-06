---
# 结构化元数据（用于索引和聚合）
product: "Paragraph Notes"
slug: "paragraph-notes"
date: "2026-09-26"
rank: 7
votes: 105
comments: 1

# 分类标签
category: "消费级应用"
subcategory: "本地优先 Markdown 笔记"
tags: ["Mac", "本地优先", "隐私优先", "Markdown", "一次性买断", "独立开发者", "纯本地"]

# 技术信息
tech_stack: []            # 未披露
platform: ["Mac"]
open_source: false
license: ""

# 商业信息
business_model: "Freemium + 一次性买断（in-app purchase）"
pricing_start: "$19.99（Pro 一次性 IAP；免费档上限 20 条笔记）"
funding_stage: "未披露（独立开发者单人项目）"
funding_amount: ""

# 关联信息
related_products: ["Obsidian", "Bear", "iA Writer", "MinkNote", "Supernotes"]
maker_previous: []

# 速览信号
key_signals:
  - "纯本地+不联网：笔记存为单一 JSON 文件，应用从不连接互联网，App Store 隐私标签为 Data Not Collected"
  - "免费 20 条，Pro 一次性 $19.99 IAP 解锁无限笔记 + 额外字体 Cousine；无订阅"
  - "葡萄牙里斯本独立产品设计师 João Alfaiate 单人开发，公司主体 Enough Pepper Lda"
  - "同步靠自托管：把 JSON 数据库文件放进 iCloud Drive / Dropbox 等云盘文件夹，App 本身无内置同步"

# 元信息
archived_at: "2026-09-26"
sources_count: 4
---

# Paragraph Notes · 扩展阅读上下文

> PT 2026-09-26 Product Hunt 榜单第 7 · 👍 105 · 💬 1  
> 归档日期 2026-09-26 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Paragraph Notes |
| 英文 tagline | A private Markdown notes app for Mac |
| 中文 tagline | 一款主打隐私的 Mac 端 Markdown 笔记应用 |
| 官网 | https://paragraphnotes.md/ |
| 用户指南 | https://paragraphnotes.md/guide/ |
| PH 页 | https://www.producthunt.com/products/paragraph-notes |
| Mac App Store | https://apps.apple.com/us/app/paragraph-notes/id6787725025 |
| 品类标签 | Note and writing apps；Mac, Writing, Notes |
| 票数 / 评论 | 105 / 1（PH 页显示 106 点，archive 取 105） |
| 公司主体 | Enough Pepper, Lda（https://enoughpepper.com） |
| 应用体积 | 110.3 MB |
| 当前版本 | 1.0.7（2026-09-23 左右更新，更新说明为 "Minor bug fixes"） |
| 支持语言 | English |
| 年龄分级 | 4+ |
| App Store 隐私 | Data Not Collected（开发者不收集任何数据） |

## 是做什么的（如实复述，不评价）

一款 Mac 独占的 Markdown 笔记应用，主打「隐私优先 + 纯本地 + 单一可移植数据文件」。用户在一个干净的纯文本编辑器里写 Markdown（标题、粗体、斜体、引用、列表等基础语法），应用自动保存，支持搜索、查找替换、文件夹分类、置顶、按名称/修改日期排序。笔记以单条纯文本文件（.txt / .md / .markdown）形式存在，所有笔记打包成一个 JSON 数据库文件，应用从不连接互联网。数据库位置可自定义，可被 AES-256 加密的 ZIP 密码锁住，可单独导出或整体导出。

## 解决什么问题（事实层面，不判断值不值得解）

- 不想把笔记交给云端、又想要比纯文本编辑器更顺手 UI 的人（应用从不联网、App Store 隐私标签为 Data Not Collected）
- 希望数据可移植、便于备份和迁移的人（数据 = 一个 JSON 文件，可以放进 iCloud Drive / Dropbox 等任意云盘文件夹实现自托管同步）
- 只需要基础 Markdown 写作、不需要 Obsidian 那种双链图谱、Bear 那种富文本的「简单写作者」
- 个人小知识库 / 日记本 / 备忘场景（免费档上限 20 条，覆盖轻度使用）

## 怎么做的（技术原理/机制，事实层面）

- 存储格式：每条笔记存为单独的纯文本文件（.txt / .md / .markdown）；所有笔记汇总到一个 JSON 数据库文件
- 默认数据库路径：`~/Library/Containers/com.enoughpepper.paragraphnotes/Data/Library/Application Support/Paragraph Notes`，用户可改到任意位置
- 同步机制：App 内置无同步；通过把 JSON 文件放进 iCloud Drive / Dropbox / Google Drive 等云盘文件夹实现跨设备同步
- 安全模型：数据库可设为密码保护，密码以 AES-256 ZIP 形式加密保存
- 编辑器：纯文本编辑器，支持 Markdown 语法高亮/渲染（heading, bold, italic, quote, list），自动保存，提供单文件查找替换
- 文件夹：用户可建任意多个文件夹（无子文件夹），含 3 个内置不可删除文件夹：All、Inbox、Trash
- 设置：字体（IBM Plex Mono / Red Hat Mono / SF Mono / Source Code Pro，Pro 多一个 Cousine）、字号、编辑器宽度、行长、边距、外观（Light/Dark/Auto）、数据库位置、笔记上限指示器、文件夹排序、锁定数据库
- 平台：仅 Mac（通过 Mac App Store 分发），未提及 iOS / iPadOS / Web 版本
- 技术栈：未披露；包名 `com.enoughpepper.paragraphnotes` 暗示是 Mac App Sandbox 下的原生应用（Swift/AppKit 概率较高），但官方未公开说明

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 / 开发者 | João Alfaiate（@jlft）—— 葡萄牙里斯本，产品设计师 | PH 页 maker 区 |
| PH Hunter | Chris Messina（@chrismessina） | PH 页 |
| 公司主体 | Enough Pepper, Lda（葡萄牙有限责任公司） | Mac App Store 开发者字段 + 官网 about 链接 |
| 融资 | 未披露（个人独立项目） | — |
| 投资方 | 无 | — |
| 加速器 | 无 | — |
| 合规认证 | Mac App Store 上架（Apple 审核）；App Store 隐私标签 Data Not Collected | App Store |

## 定价 / 商业模式

- 免费档：上限 20 条笔记，含全部基础功能（编辑、Markdown、文件夹、搜索、查找替换、Pin、导出、导入、AES-256 密码锁、Light/Dark/Auto 外观、四种等宽字体）
- Pro 档：通过 Mac App Store 内购一次性 $19.99 买断，解锁：
  - 无限条笔记（突破 20 条上限）
  - 额外一种字体 Cousine（Cousine 是 Google Fonts 上的开源等宽字体，免费档也能从系统装，但应用内置选择里 Pro 才列）
  - 升级提示中无其它功能差异，4 种核心字体在免费档即可用
- 非订阅制，无月费/年费；提供 Restore Purchase 用于换机后恢复 Pro
- 收入全部来自 Mac App Store 内购分成（Apple 标准 70/30，小型开发者 85/15 第一年）

## 关联信息 / 生态

- 竞品 / 同类（PH 页 Related 区）：
  - **Obsidian** —— 「A versatile writing app tailored to your thinking」，本地 Markdown + 插件生态，强于知识图谱
  - **Bear** —— 「a beautiful, simple Markdown note-taking app」，仅 Apple 平台，富文本 + Markdown
  - **iA Writer** —— 「Plain text. Full ownership. Total focus.」，极简写作工具，跨平台
  - **MinkNote** —— 「Private macOS notes built on plain Markdown files」，定位最近（也是「Mac + 本地 Markdown + 隐私」）
  - **Supernotes** —— 「Free your thoughts」，卡片式协作笔记
- 差异化定位：相比 Obsidian/Bear/iA Writer，Paragraph Notes 走「更小、更窄、更本地」——只服务「想用最朴素方式写 Markdown + 数据完全在自己手里」的用户，砍掉了双链、图谱、协作、富文本
- 与 PH 推广位 Viktor.com（"An AI coworker that actually does the work"）无关联，仅为同页推广位
- PH 关注者 93

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-09-23 前后 | Mac App Store 当前版本 v1.0.7 发布（"Minor bug fixes"），首次上架时间早于此 |
| 2026-09-26 | 上 Product Hunt 榜单（距当前版本约 3 天），日榜 #7 |

（注：未披露首发日期 / 早期版本历史；官网无公开 changelog 页。）

## 评论区反馈（事实摘录，不评价）

- PH 评论数 1 条，创始人 João Alfaiate 在 maker comment 强调：「Paragraph Notes is simple, private, fully local, and gives users control over their data.」
  - 关键卖点（创始人自述）：Markdown 纯文本编辑器、零打扰界面、纯本地永不联网、单一开放可移植 JSON 数据库、密码保护数据库
- 具体评论与回复内容：未抓到完整文字（评论区仅 1 条，未提供问答摘录细节）

## 信息来源

- PH 产品页：https://www.producthunt.com/products/paragraph-notes（拿到 tagline / 描述 / maker / hunter / 相关产品 / 投票数 / 评论摘要）
- 官网：https://paragraphnotes.md/（拿到 features 摘要、隐私声明「never connects to the internet」、公司主体链接 enoughpepper.com）
- 用户指南：https://paragraphnotes.md/guide/（拿到完整功能矩阵、JSON 数据库路径、AES-256 ZIP 密码锁、字体清单、文件夹模型、导出格式、同步机制）
- Mac App Store：https://apps.apple.com/us/app/paragraph-notes/id6787725025（拿到公司主体 Enough Pepper Lda、版本 1.0.7、IAP 价格 $19.99、应用体积 110.3 MB、隐私 Data Not Collected）
- 公开报道：无（搜索 "Paragraph Notes" 未返回独立媒体文章/评测）
- GitHub：无公开仓库（搜索未命中 github.com 上的 paragraphnotes / paragraph-notes / jlft 仓库；应用未声明开源）

## 未查到 / 待补

- 创始人 João Alfaiate 的过往产品 / 作品集 / LinkedIn（Web 搜索无具体结果，仅 PH maker 简介「product designer based in Lisbon」）
- 首发日期 / 完整版本历史（官网无 changelog；Mac App Store 历史页未抓取）
- 最低支持 macOS 版本（官网与 App Store 抓取内容均未给出）
- Pro IAP 除 Cousine 字体外的功能差异（仅有「无限条笔记 + 字体」两项已确认；是否存在主题 / 多数据库 / 高级导出等差异未明确）
- 是否有 iOS / iPadOS 版本计划（官网与 App Store 当前均只见 Mac 版本）
- 真实评论数量与回复（PH 页面评论 1 条，未抓取完整问答原文）
- João Alfaiate 在 PH 简介之外的更多身份背景（Twitter/X @jlft 账号未抓取）
- 任何独立媒体评测 / 用户评论汇总（搜索未命中）