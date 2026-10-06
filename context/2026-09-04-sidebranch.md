---
product: "sidebranch"
slug: "sidebranch"
date: "2026-09-04"
rank: 10
votes: 100
comments: 6

category: "开发者工具"
subcategory: "Git worktree 可视化 UI 对比"
tags: ["Git", "worktree", "视觉 diff", "Chrome 扩展", "本地优先", "开源信号未确认"]

tech_stack: ["Chrome/Edge Extension", "Node.js CLI", "本地 sidecar daemon", "HTTP dev server", "Git worktree", "Node built-ins"]
platform: ["Chrome", "Edge", "macOS/Linux/Windows（未完全披露）", "本地 Web 应用"]
open_source: false
license: "未查到"

business_model: "免费工具（未见付费计划）"
pricing_start: "免费（官网未列价格）"
funding_stage: "未披露"
funding_amount: ""

related_products: ["Git worktree", "GitHub Codespaces", "VS Code Source Control", "Tower", "Fork"]
maker_previous: []

key_signals:
  - "Chrome/Edge 扩展配合本地 sidecar daemon，在每个分支建立隔离 Git worktree 和 dev server，不触碰当前工作目录"
  - "浏览器内的 branch pill 可切换分支；两块 live pane 支持 side-by-side、blend 和 onion diff，直接对比运行中的 UI"
  - "通过 `.sidebranch.json` 声明 dev/install/copy 命令，`npx sidebranch init/start/doctor/clean` 管理环境；daemon 默认 loopback 127.0.0.1:49400"
  - "官网 v0.2.0；工具宣称零外部依赖（Node built-ins），框架无关，只要应用能在端口上响应 HTTP 即可"

archived_at: "2026-09-05T14:59+08:00"
sources_count: 4
---

# sidebranch · 扩展阅读上下文

> PT 2026-09-04 Product Hunt 榜单第 10 · 👍 100 · 💬 6  
> 归档日期 2026-09-05 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | sidebranch |
| 英文 tagline | Easy git-based visual diffing |
| 中文 tagline | 简单的基于 Git 的视觉差异对比 |
| 官网 | https://sidebranch.dev/ |
| PH 页 | https://www.producthunt.com/products/sidebranch |
| 品类标签 | Productivity · Developer Tools · Artificial Intelligence |
| 票数 / 评论 | 100 / 6 |
| 公司主体 | 未查到；官网署名 Cris Graña |
| 企业版/关联站点 | Chrome Web Store 扩展、npm 包 `sidebranch`、本地 daemon |

## 是做什么的（如实复述，不评价）

sidebranch 用浏览器扩展和本地命令行 daemon，把 Git 分支或 worktree 启动成多个隔离的开发服务器，然后在正在运行的应用里切换分支并比较 UI。它提供并排、混合和 onion 等视觉 diff 模式，用于审查 PR 或检查不同分支的页面变化。

## 解决什么问题（事实层面，不判断值不值得解）

- 传统 `git diff` 主要显示文本，前端开发者还需要手动切分支、启动多份应用才能看视觉变化。
- 在单一工作目录切换分支会打断当前开发状态，难以同时查看多个 UI 版本。
- 目标场景是本地开发中的 UI review、PR 视觉审查和设计回归检查。

## 怎么做的（技术原理/机制，事实层面）

- 在仓库目录执行 `npx sidebranch init` 生成 `.sidebranch.json`，配置 `dev`、`install` 和要复制的环境文件。
- `npx sidebranch start` 启动仅监听 loopback 的 daemon（默认 `http://127.0.0.1:49400`），为每个 pane 创建独立 worktree 并运行 dev command。
- 浏览器扩展向应用注入 widget；用户从 branch pill 选择分支，A/B 两个 pane 分别加载不同 worktree 的 HTTP 服务。
- `doctor` 检查环境，`stop` 停止 daemon 和 pane 服务，`clean` 清理 worktree；官方称实现只使用 Node built-ins、无外部依赖。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人/作者 | Cris Graña（官网署名） | sidebranch.dev |
| 融资 | 未查到 | 公开搜索未见披露 |
| 投资方 | 未查到 | 公开搜索未见披露 |
| 加速器 | 未查到 | 公开搜索未见披露 |
| 合规认证 | 未查到 | 官网未列 |

## 定价 / 商业模式

官网提供 Add the extension、Install the package 的免费安装说明，未列订阅、授权或企业价格。Chrome Web Store 扩展和 npm 包的具体发布条款、许可证未查到。

## 关联信息 / 生态

- 支持 Next、Vite、Django、Rails 等，只要应用能在端口上提供 HTTP 响应。
- 官网展示 v0.2.0，并提供 `sidebranch.dev` 交互式示例，示例含 main、feat/dashboard、fix/nav-overlap 等分支。
- 功能与 Git worktree、VS Code/桌面 Git 客户端形成互补，定位集中在运行中 UI 的视觉比较。

## 评论区反馈（事实摘录）

- PH 评论原文未能通过 Cloudflare 验证页抓取，待补。

## 信息来源

- 官网：https://sidebranch.dev/（版本、功能、安装与命令）
- PH 产品页：https://www.producthunt.com/products/sidebranch（榜单信息；正文受 Cloudflare 挑战）
- 公开搜索：`"Sidebranch is a browser extension paired with a local sidecar daemon"`
- Google 搜索结果摘要：`sidebranch — worktree visual diffing`（官网域名确认）

## 未查到 / 待补

- GitHub/npm 源码仓库、许可证、创始团队完整信息和融资未查到。
- 扩展在 Chrome Web Store 的权限清单、支持操作系统矩阵和隐私策略细节待补。
- PH 评论原文待 Cloudflare 验证通过后补充。
