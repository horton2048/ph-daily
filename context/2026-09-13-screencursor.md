---
# 结构化元数据（用于索引和聚合）
product: "ScreenCursor"
slug: "screencursor"
date: "2026-09-13"
rank: 4
votes: 123
comments: 3

# 分类标签
category: "消费级应用"
subcategory: "屏幕录制"
tags: ["Chrome 扩展", "本地优先", "一次性买断", "自动缩放", "离线可用"]

# 技术信息
tech_stack: ["Chrome Extension", "WebCodecs / 浏览器视频编码", "本地处理"]
platform: ["Chrome", "macOS", "Windows", "Linux"]
open_source: false
license: ""

# 商业信息
business_model: "一次性买断（lifetime license）"
pricing_start: "$24.50（PH 首发 7 天半价）/ 标准 $49（早鸟价，正价 $79）"
funding_stage: "未披露（个人/独立开发者）"
funding_amount: ""

# 关联信息
related_products: ["Screen Studio", "Loom", "Tella", "Arcade", "Guidde", "Descript", "Camtasia"]
maker_previous: []

# 速览信号
key_signals:
  - "Chrome 扩展形态，全本地处理，录制视频永不离开电脑（无需账号、无需上传）"
  - "把每次点击/拖拽/按键自动转成预先到达的镜头缩放，免后期剪辑"
  - "明确对标 macOS 独占的 Screen Studio，跨平台卖一次性 $49（Screen Studio 订阅约 $108/年）"
  - "独立开发者 Phoenix 自述为 Windows / Linux 用户做的，因为这两平台缺测试者"

# 元信息
archived_at: "2026-09-13"
sources_count: 4
---

# ScreenCursor · 扩展阅读上下文

> PT 2026-09-13 Product Hunt 榜单第 4 · 👍 123 · 💬 3  
> 归档日期 2026-09-13 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | ScreenCursor |
| 英文 tagline | Screen recorder with auto zoom effects |
| 中文 tagline | 带自动缩放效果的屏幕录制工具 |
| 官网 | https://screencursor.com |
| PH 页 | https://www.producthunt.com/products/screencursor |
| 品类标签 | Chrome Extensions · Productivity · Video（Screenshots and screen recording apps） |
| 票数 / 评论 | 123 / 3 |
| 公司主体 | 未披露（独立开发者 Phoenix，@phoenixiam） |
| 企业版/关联站点 | 无；通过 Polar 作为 merchant of record 收款 |

## 是做什么的（如实复述，不评价）

一款 Chrome 扩展形态的屏幕录制工具。用户在 Chrome 里选好要录的屏幕区域后按录制，扩展会自动把录制期间的每一次鼠标点击、拖拽、按键变成一段"自动缩放镜头"——缩放会先于动作到达、跟随光标移动，全程不需要用户后期剪辑。录完后可以修剪、调整缩放深度/时序/缓动、加背景与浏览器外框，最后导出 720p 或 1080p MP4 到本地 Downloads。Chromium 的屏幕分享条会在录制时显示且无法关闭（官网 FAQ 明确说明）。录制对象是整个屏幕，包括 Chrome 之外的 App。

## 解决什么问题（事实层面，不判断值不值得解）

- 做产品演示 / 教程视频时，手动给点击位置加缩放镜头很耗时；ScreenCursor 把这件事自动化
- Screen Studio 等同类工具是 macOS 独占，Windows 与 Linux 用户长期没对标替代
- 不想为屏幕录制付年费（Screen Studio 约 $108/年 vs ScreenCursor $49 一次性）
- 关心隐私 / 合规的用户：视频全部在浏览器本地处理，不上传任何服务器

## 怎么做的（技术原理/机制，事实层面）

- 形态：Chrome 扩展，不需安装器、不需管理员权限
- 处理位置：所有视频处理在浏览器本地完成；不需要账号、不需要后端服务
- 录制流程（3 步，按官网描述）：1) 按录制 → 3 秒延迟后开始（用于藏掉 Chrome 自带的屏幕分享条）；2) 自动缩放——点击/拖拽/按键被检测为事件，生成"提前到达、跟随光标"的镜头运动；3) 导出——修剪、剪辑、调整缩放参数后导出 MP4
- 可手动二次编辑：缩放时序、深度、缓动风格（snappy / gentle）都可调整，可手动删/加缩放；预览实时重渲染
- 硬件要求：需要硬件视频编码（近十年出的机器都满足）
- 输出：720p 或 1080p MP4
- 帧率 / 编码器 / 事件检测算法等具体技术细节官网未披露

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Phoenix（PH 用户名 @phoenixiam） | PH 页面 |
| 融资 | 未披露 | — |
| 投资方 | 未披露 | — |
| 加速器 | 未披露 | — |
| 合规认证 | 未披露 | — |

## 定价 / 商业模式

- **商业模式**：一次性买断（lifetime），无订阅、无席位、无水印、无录制时长上限
- **首发期（PH 上线 7 天）**：使用优惠码 `PRODUCTHUNT` 立减 50%，实付 $24.50
- **早鸟价**：$49（终身含更新；可在最多 3 台个人电脑上使用）
- **正价**：$79（官网"early pricing"为 $49，对比暗示正价为 $79）
- **多设备**：最多 3 台，机器名额可释放再分配到新机器
- **退款**：通过 Polar 处理，按 Polar 退款政策
- **已售渠道**：Polar（merchant of record）

## 关联信息 / 生态

- **直接对标**：Screen Studio（macOS 独占，4.9★，184 评价，订阅制）——Phoenix 在 PH 评论里自述"受 Screen Studio 启发，但 Screen Studio 只支持 Mac，所以做了 Chrome 扩展版本给 Windows / Mac / Linux"
- **PH 页"类似产品"列出的竞品**：Screen Studio（4.9★）、Loom（4.8★）、Tella（4.8★）、Arcade（4.9★）、Guidde（4.8★）
- **广义的屏幕录制 / 演示生态**：Loom（异步视频消息）、Descript（音视频转录 + 编辑）、Camtasia（重型专业录制/编辑套件）
- **官网对比说明**（FAQ）：Screen Studio 提供 webcam 叠加、运动模糊、iPhone USB 录制等 ScreenCursor 没有的能力；ScreenCursor 在价格和跨平台上占优

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-09-13 | 在 Product Hunt 上线，当日 #4 |

## 评论区反馈（事实摘录，不评价）

- **Tehreem Fatima（7h 前）**："终于有给 Windows 和 Linux 用的 Screen Studio 替代品了！自动缩放、不上传服务器、一次性终身买断不用年年付费，这是大胜利。"（↑1）
- **Phoenix 回复（6h 前）**："非常感谢！希望能真正帮到大家！"（↑1）
- **Phoenix 上线帖**：自述为 Windows 和 Linux 用户做这个产品（"我最少有测试者的两个平台"），邀请这两平台的用户试用并反馈

## 信息来源

- PH 产品页：https://www.producthunt.com/products/screencursor（拿到：tagline、完整描述、定价、maker、2 条公开评论、类似产品列表、99 followers）
- 官网：https://screencursor.com（拿到：3 步操作流程、可编辑缩放细节、帧率/导出参数、FAQ 中的隐私与多设备说明、与 Screen Studio 对比）
- 公开报道：搜索 "ScreenCursor auto zoom screen recorder Chrome extension" 与 "ScreenCursor screencursor.com" 均为一般性介绍，无 2026 上线相关独立报道（搜索结果混淆为 Cursor IDE，未发现可信新闻源）
- GitHub：未见开源信号，未查 GitHub

## 未查到 / 待补

- 创始人 Phoenix 的真实姓名、过往产品、所在地区——PH 与官网均未披露更多
- 融资 / 投资方 / 加速器——未披露
- 底层使用的视频编码器（推测是 Chrome WebCodecs API，但官网未明示）
- 自动缩放的"事件检测算法"具体实现——未披露
- 99 个 followers 之外的早期用户规模 / 销量数字——未披露
- 是否计划推出 macOS 原生 App 或 Windows 桌面端——官网仅强调"Chrome 跑得了就行"
