---
product: Smooth Recorder
slug: smooth-recorder
date: '2026-10-04'
rank: 2
votes: 137
comments: 9
category: 消费级应用
subcategory: Mac 屏幕录制
tags:
- Mac
- 屏幕录制
- 一次买断
- 本地优先
- 自动缩放
tech_stack:
- SwiftUI
- AppKit
platform:
- Mac
open_source: false
license: ''
business_model: 一次性买断
pricing_start: 早鸟 $9（正式价 $69）
funding_stage: 未披露
funding_amount: 未披露
related_products:
- Screen Studio
- CleanShot X
- Loom
maker_previous: []
key_signals:
- 录完即带自动缩放、光标平滑与 3D 视角；停录即像剪过
- 本机转写：按文字删词即剪视频；截图支持智能打码
- 一次买断：早鸟 $9，标价 $69；原生 Mac 应用（非 Electron）
archived_at: '2026-10-04T21:20:00+08:00'
sources_count: 2
---

# Smooth Recorder · 扩展阅读上下文

> PT 2026-10-04 Product Hunt 榜单第 2 · 👍 137 · 💬 9  
> 归档日期 2026-10-04 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Smooth Recorder |
| 英文 tagline | Mac screen recordings that look edited when you hit stop |
| 中文 tagline | Mac 录屏：停录时看起来像已经剪辑过 |
| 官网 | https://smoothrecorder.com/ |
| PH 页 | https://www.producthunt.com/products/smooth-recorder |
| 品类标签 | Mac · Design Tools · Video |
| 票数 / 评论 | 137 / 9 |
| 公司主体 | 未查到公司实体名；支持邮箱 hello@smoothrecorder.com |
| 企业版/关联站点 | 无 |

## 是做什么的（如实复述，不评价）

Smooth Recorder 是 macOS 原生屏幕录制与截图工具。录制时自动跟点击做缩放、平滑光标轨迹，并支持 3D 视角（1.1 新特性）；停录后即可得到偏成品感的演示视频。还支持本机转写字幕、按文字剪辑、GIF、滚动长截图、OCR 取字，以及截图编辑（壁纸/圆角/箭头/智能打码等）。对比页自称相对 Screen Studio / CleanShot X / Loom：一次买断、自动缩放、本机字幕与按文字剪辑等。

## 解决什么问题（事实层面，不判断值不值得解）

- 产品演示录完通常还要长时间剪辑缩放与光标
- 订阅制录屏工具成本高，希望一次买断
- 希望字幕识别与隐私打码留在本机

## 怎么做的（技术原理/机制，事实层面）

- SwiftUI + AppKit 原生应用；要求 macOS 15 Sequoia 及以上
- 点击驱动自动缩放；平滑光标与相机；3D 角度预设
- 字幕、文字识别、Smart Redact（邮箱/电话/卡号/API key/人脸）在本机跑
- 快捷键叠加层：截图 / 录制 / GIF / 滚动截图 / 取字
- 导出：MP4、MOV（30/60 fps）、GIF（最高约 24 fps）
- 刘海区库、菜单栏与 Dock 快捷入口（1.1）

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | 未查到公开姓名 | |
| 融资 | 未查到 | |
| 投资方 | 未查到 | |
| 加速器 | 未查到 | |

## 定价 / 商业模式

一次买断。早鸟 Early Access：$9（正式价页面写 $69）。无订阅对比叙事。

## 关联信息 / 生态

官网对比 Screen Studio、CleanShot X、Loom。未见开源信号，未查 GitHub。注意：与 SmoothCapture（smoothcapture.app）为不同产品。

## 技术时间线

| 日期 | 事件 |
|---|---|
| 未查到 | 首次公开日期未查到 |
| 1.1 | 3D 角度、菜单栏/Dock 能力（官网标注） |
| 2026-10-04 | 登 PH 日榜第 2 |

## 评论区反馈

官网引用用户评价（Opencals 创始人等）；PH 评论原文本次未抓到。

## 信息来源

- https://smoothrecorder.com/
- archive logo / PH 产品摘要

## 未查到 / 待补

- 创始人与融资
- PH 评论原文
- 正式价是否已结束早鸟
