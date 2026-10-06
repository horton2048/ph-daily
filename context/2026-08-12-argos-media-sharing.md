---
product: "Media Sharing (Argos)"
slug: "argos-media-sharing"
date: "2026-08-12"
rank: 9
votes: 0
comments: 3

category: "开发者工具"
subcategory: "PR 媒体附件/CI 截图分享"
tags: ["CI", "GitHub", "MCP", "第三次PH发布"]

tech_stack: ["Playwright", "ImageKit", "GitBook"]
platform: ["CLI", "Node.js SDK", "REST API", "MCP"]
open_source: false
license: ""

business_model: "订阅制（按 screenshot/video 用量计费，含免费层）"
pricing_start: "免费层可用，图片1单位/视频25单位"
funding_stage: "未披露"
funding_amount: "未披露"

related_products: ["Chromatic", "Percy"]
maker_previous: ["未查到"]

key_signals: ["解决GitHub无公开API给PR评论加图片/视频附件的问题", "AI coding agent 从终端也能把截图贴到PR,不用像人一样拖拽浏览器", "Argos成立于2023,这是第三次PH发布,非新公司"]

archived_at: "2026-08-12"
sources_count: 1
---

# Media Sharing (Argos) · 扩展阅读上下文

> PT 2026-08-12 Product Hunt 榜单第 9 名 · 👍 0（未返回）· 💬 3
> 归档日期 2026-08-12 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Media Sharing（Argos 出品） |
| 英文 tagline | Let AI agents put screenshots and videos on pull requests |
| 中文 tagline | 让 AI 代理在 PR 上添加截图和视频 |
| 官网 | argos-ci.com |
| PH 页 | https://www.producthunt.com/products/argos |
| 品类标签 | Artificial Intelligence · GitHub · Tech |
| 票数 / 评论 | 0（未返回）/ 3 |
| 公司主体 | Argos（成立于 2023，这是第三次 PH 发布） |

## 是做什么的（如实复述，不评价）

Argos 的 Media Sharing 功能让 AI coding agent 和 CI 系统能把截图/录屏转换成稳定的分享链接和可粘贴的 Markdown，自动发到 PR 上。支持图片版本管理（重新上传保持同一 URL，PR 内嵌自动更新）、评论可精确定位到图片坐标。

## 解决什么问题（事实层面，不判断值不值得解）

联合创始人 Greg Bergé 指出核心问题："GitHub has no public API for comment attachments. A signed-in browser can drag a screenshot into a pull request, a coding agent working from a terminal cannot."——从终端跑的 coding agent 没法像人一样拖拽截图到 PR。

## 怎么做的（技术原理/机制，事实层面）

- 多入口访问：CLI、Node.js SDK、REST API、MCP server
- 底层用 Playwright（截图/录制）、ImageKit（图片处理/CDN）
- 计费单位：图片 1 单位、视频 25 单位，含现有付费方案中

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 联合创始人 | Greg Bergé、Jeremy Sfez | PH 页 |
| 公司成立 | 2023 年 | PH 页 |
| 融资 | 未查到 | — |

## 定价 / 商业模式

集成进 Argos 现有订阅方案（含免费层），按用量计费：截图 1 单位/张，视频 25 单位/条。

## 关联信息 / 生态

- GitHub：github.com/argos-ci
- 品类邻近 Chromatic、Percy 等视觉回归/截图工具，但这次发布聚焦"AI agent 场景下的 PR 媒体附件"这一细分需求。
- 这是 Argos 第三次在 Product Hunt 发布。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/argos（描述、创始人评论、Build tools、公司背景）

## 未查到 / 待补

- 融资情况
- 完整定价方案（各档位价格）
- 与 Chromatic/Percy 的具体功能对比
