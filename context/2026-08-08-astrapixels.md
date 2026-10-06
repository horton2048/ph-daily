---
product: "AstraPixels"
slug: "astrapixels"
date: "2026-08-08"
rank: 3
votes: 0
comments: 2
category: "消费级应用"
subcategory: "像素风太阳系 Web 应用（广告/认领变现）"
tags: ["Web App", "Art", "Advertising", "像素风", "天文", "Million Dollar Homepage", "程序生成"]
tech_stack: ["astronomy-engine (轨道力学库)", "客户端渲染", "Stripe"]
platform: ["Web"]
open_source: false
license: ""
business_model: "一次性认领 + 广告位租赁（CPM 计价）+ 稀缺位租赁"
pricing_start: "$5（认领一颗小行星，一次性）"
funding_stage: "未查到（个人项目）"
funding_amount: ""
related_products: ["NASA Picture of the Day", "Solis Watch Face For Wear OS", "T-Minus", "Enigma", "Solar System Explorer", "Million Dollar Homepage"]
maker_previous: ["@nicklaunches：Nick Launches（产品发布目录站点，DR 68 回链）"]
archived_at: "2026-08-08"
sources_count: 3
---

# AstraPixels · 扩展阅读上下文

> PT 2026-08-08 Product Hunt 榜单第 3 · 👍 未查到（archive 显示 0） · 💬 2  
> 归档日期 2026-08-08 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | AstraPixels |
| 英文 tagline | A pixel-art solar system at its real current positions. |
| 中文 tagline | 像素画太阳系，天体处于真实当前位置 |
| 官网 | https://astrapixels.com/ |
| PH 页 | https://www.producthunt.com/products/astrapixels |
| 品类标签 | Web App · Art · Advertising（PH 页面分类：Maps and GPS） |
| 票数 / 评论 | PH 页面访问时未显示 upvote 数；archive 👍 0 / 💬 2；62 followers；1 条可见评论 |
| 公司主体 | 未查到（个人项目；官网版权行 "astrapixels.com · 2026"） |
| 企业版/关联站点 | /browse、/browse/belt、/events、/advertise、/terms |

## 是做什么的（如实复述，不评价）

一个逐像素（pixel-art）的太阳系动画地图，每个天体都处于真实当前位置——位置按公开发表的轨道根数用 `astronomy-engine` 计算，而非抄静态列表。可缩放浏览从太阳到柯伊伯带，浏览 171 个已编目天体（每个物体页的事实都带来源标注），并可查看未来六个月天象（合、冲、流星雨、食）。商业化部分：每个"岩石"可购买——$5 认领一颗小行星永久持有并命名（名字仅显示在 AstraPixels 站内，不是 IAU 命名）。

官网标题："AstraPixels: The Solar System, Live and in Pixels."

## 解决什么问题（事实层面，不判断值不值得解）

- PH 描述：把太阳系变成可浏览、可"拥有"（认领命名）的互动地图。
- 创始人自述：构建商业侧是为了规避 "Million Dollar Homepage clone" 的三种常规死法——库存售罄、无回头客、链接腐烂（原文："the three ways a Million Dollar Homepage clone normally dies: inventory sell-out, no repeat visitors, and link rot"）。
- 针对三种死法的设计：库存（主带 3,000 颗程序生成岩石，$5 地板价永不可售罄；真正稀缺的太阳/行星皮肤/彗星改租赁）；留存（天象页计算未来六个月合/冲/流星雨/月食）；链接腐烂（链接每月检查，三次失败把岩石变成可见的破败幽灵 sprite 再回收回库存；官方引述"原始 Million Dollar Homepage 的链接 22% 在十年内失效"）。

## 怎么做的（技术原理/机制，事实层面）

- 位置计算：用 `astronomy-engine` 库 + 公开发表的轨道根数实时计算（创始人："computed from published orbital elements with astronomy-engine, not copied from a list"）。
- 时间可向前推进一周；"true scale" 视图展示地图对现实比例的失真程度。
- 客户端渲染（有 loading 状态）。
- 账户系统："There is no sign-up. Stripe asks for your email and that is the whole account system."（无注册，Stripe 收邮件即全部账户系统。）
- 广告位计数规则（/advertise 页面）：tooltip 需 400ms 连续可见计 1 次曝光；隐藏 tab 不计注意力（计时器在 tab 不可见时停止）；每 placement 每 session 每天可计费曝光上限 20 次；桌面与触屏分开统计；"client 提议、server 决定"（浏览器上报原始、服务器应用规则）；原始事件不存储、只聚合日报；不提供 forecast，只报已发生历史。
- 免责声明（认领页重复出现）："Official minor planet names are assigned by the IAU and cannot be bought."（官方小行星命名由 IAU 授予，不可购买。）/ "A custom name on a body is shown on astrapixels.com only and is not an IAU designation."

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | @nicklaunches（"Nick Launches"，唯一列出的 launch team 成员；nicklaunches.com 是一个产品发布目录站点——"Don't just build → Get discovered"，主打 DR 68 站点回链；无个人简历/实名） | PH 页 / nicklaunches.com |
| 融资 | 未查到（个人项目） | — |

## 定价 / 商业模式

永久认领（claims，买断一次）：
- 小行星：$5 一次性、永久持有、可自由命名。
- 月亮/卫星：$49。
- 一次性广告卫星：$29（90 个，logo 绕行星轨道公转，槽位数按行星真实半径缩放——"Jupiter carries eighteen and Mars carries seven"）。

稀缺位租赁（leased，不售罄）：
- 太阳、8 颗行星皮肤、彗星——只租不卖。

广告位租赁（rented surfaces，按月按印象 CPM 计费）：
- Tooltip 赞助行：$9/月（基准价），测量注意力 $1.20/1,000 desktop hovers，发布价 $4.50/月；桌面 hover 才显示、不可点击、24 字符上限。
- Modal header strip：$19/月（$1.20/1,000 modal opens；发布价 $9.50/月）；可外链，仅当 modal 停留同一 body 时计曝光。
- Network native card：$6/月（$1.20/1,000 modal opens；发布价 $3/月）；每 14 秒轮换、按 share of voice 加权、权重发布在 map payload。
- 行星赞助商：$249/年（每行星 1 个、共 8 个），把行星 sprite 染成赞助商品牌色。
- 系统缩放时无广告图标，改为 count badge（如 "+12 over Jupiter"）。
- Founding advertiser 五折（"because this surface has no measured history yet"，有数据那天即失效）；当前测量注意力 $0（30 天 trailing 为 0）。
- 租赁位外链一律 `nofollow`；买家创意发布前需审核；示例创意为虚构（fixture id 带 `sample:` 前缀，不计数）。

## 关联信息 / 生态

- PH Similar Products：Solis Watch Face For Wear OS、NASA Picture of the Day、T-Minus、Enigma、Solar System Explorer。
- 天象页与认领/广告位构成主要留存与变现机制。
- 主带 3,000 程序生成岩石 + 171 个已编目带来源事实的天体。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026 | 官网版权 2026 |
| 2026-08-08 | PH 当日榜第 3（"Launching today"，leaderboard URL 2026/8/8） |

## 评论区反馈（事实摘录，不评价）

- Leopold（1 小时前）："The pixel art style makes space feel approachable rather than overwhelming." 并提问：认领的小行星自定义名字对别的访客可见，还是仅当前会话内可见？——未看到创始人回复。
- 创始人发布评论要点：位置按轨道根数实时计算而非抄列表；$5 认领小行星、$49 月亮、太阳租赁；无注册仅 Stripe 邮箱；收尾请求 "I would rather have your criticism than your upvote"（更想要批评而非 upvote），自称最不确定的是"地图前五秒读起来像玩具还是像仪器"。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/astrapixels（拿到 tagline、描述、maker 评论全文、pricing 模型、评论、similar products、followers）
- 官网：https://astrapixels.com/（拿到标题、计算方式、浏览/天象路由、免责声明）
- 官网广告页：https://astrapixels.com/advertise（拿到所有广告位定价、计数规则、治理条款）
- nicklaunches.com（拿到发布目录站点定位、DR 68、周榜数据）

## 未查到 / 待补

- 确切票数（PH 页面未显示 upvote 计数）
- maker 真实姓名与完整背景（仅 "Nick Launches" 笔名）
- 认领/广告营收实际数字
- 认领总量、活跃访客数
- 轨道根数的具体来源数据集（仅知 astronomy-engine 库）
