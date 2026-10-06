---
product: "Ass Auction"
slug: "ass-auction"
date: "2026-09-09"
rank: 6
votes: 126
comments: 18

category: "营销/广告"
subcategory: "实验性广告位 / 行为艺术式营销"
tags: ["拍卖", "Stripe", "行为艺术", "病毒营销", "Cloudflare", "indie hacker"]

tech_stack: ["Cloudflare", "Stripe", "Claude Code"]
platform: ["Web"]
open_source: false
license: ""

business_model: "实时付费排名广告位（按累计支付金额定排名）"
pricing_start: "$5 起付"
funding_stage: "未披露（独立开发者副业项目）"
funding_amount: ""

related_products: ["DesignQA", "Peeko", "Sondo", "Weirdo", "muxo"]
maker_previous: ["DesignQA (AI 工具，把 UI bug 转成 PR)", "Peeko (AI 分析平台)", "Sondo (AI 知识库)", "Weirdo (App Store emoji 猜词游戏)", "muxo (tmux 终端 UI)"]

key_signals:
  - "机制是付费排名拍卖（total spend = rank），不是众筹；最低 $5 即可上榜"
  - "前 22 名品牌的 logo / handle 会被真的印在一条物理内裤上"
  - "创始人 Mahdi Farra 是湾区资深设计 leader，主业是 Meta Staff Designer + DesignQA founder"
  - "自称对营销过度严肃化的 small protest，X 上一条相关趋势据称拿到 1M 浏览"

archived_at: "2026-09-10"
sources_count: 4
---

# Ass Auction · 扩展阅读上下文

> PT 2026-09-09 Product Hunt 榜单第 6 · 👍 126 · 💬 18  
> 归档日期 2026-09-10 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Ass Auction |
| 英文 tagline | Brands outbid each other to put their logo on my ass |
| 中文 tagline | 品牌互相竞价，把 logo 印到我屁股上 |
| 官网 | （未独立建站，直接挂 PH 产品页） |
| PH 页 | https://www.producthunt.com/products/ass-auction |
| 品类标签 | Funny · Marketing · Advertising |
| 票数 / 评论 | 126 / 18（评论板总条数 127 含论坛帖） |
| 公司主体 | 独立开发者项目，无公司主体 |
| 企业版/关联站点 | 无 |

## 是做什么的（如实复述，不评价）

Ass Auction 是一个"只有一个广告位的广告网络"：作者本人穿的一条物理内裤。前 22 名品牌的 logo 或社媒 handle 会被印在这条内裤上。任何人付 $5 以上即可上榜，品牌之间通过加价互相挤位。

作者把它定位成"最小可行的广告网络"，没有套餐、没有销售环节、没有账号体系——直接 Stripe 付款，付款完成就上排行榜。配套的还有实时点击计数、被挤下位时的邮件提醒、共享卡片，以及一个叫 "gossip bar" 的社区吐槽栏。

## 解决什么问题（事实层面，不判断值不值得解）

- 痛点：传统数字广告投放门槛高、转化路径长，对独立开发者 / 小品牌不友好
- 痛点：注意力稀缺，营销越来越严肃，缺少"能让人停下来看一眼"的形式
- 目标场景：indie hackers、SaaS 创始人、meme 账号、加密项目、想用最低成本做病毒式曝光的小品牌
- 创始人自己的说法："brands pay so much for attention and no one remembers any of it"——所以做了一个最荒诞的反讽

## 怎么做的（技术原理/机制，事实层面）

- **付费排名机制**：排名 = 累计支付金额（total spend），不是单次出价；想爬回原来的位次只需要补差价，不用重付全款
- **支付**：Stripe，无账号体系，只接收 URL 或 @handle
- **上榜阈值**：$5 起付
- **上榜容量**：前 22 名（会被真的印在物理内裤上）
- **辅助功能**：
  - 实时点击计数器
  - 被挤出位时的邮件提醒
  - 可分享的推广卡片（share card）
  - "gossip bar" 社区弹幕
  - 一个隐藏彩蛋（"pull the boxers down" 时触发）
- **技术栈**：Cloudflare + Stripe + Claude Code
- **失败/异常处理**：未查到（"排名被挤掉"会发邮件，其它未披露）

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Mahdi Farra | PH 页 + 个人站 mahdif.com |
| 融资 | 未披露 / 无 | — |
| 投资方 | 无 | — |
| 加速器 | 无 | — |
| 合规认证 | 无（Stripe 标准商户） | — |

**创始人画像**（来源：mahdif.com）：
- 17 年产品 / 设计经验，自称 "Design Leader Who Codes"
- 主业：Meta Staff Product Designer（负责 Facebook Plus & Meta AI 订阅）
- 早期：Ronday（Head of Design → 代理 CEO，协助 $7M 种子轮）、Airtime、Rakuten Ready
- 所在地：Bay Area（出生地 Amman, Jordan）

**过往副业 / 独立产品**：
- **DesignQA**：AI 工具，把 UI bug 转成 GitHub PR 的修复；2024 年创立，已有付费客户
- **Peeko**：下一代 AI 分析平台
- **Sondo**：AI 知识库 chat，可挂任意产品 / 网站
- **Weirdo**：App Store 上的每日 emoji 猜词游戏
- **muxo**：tmux 的终端 UI

听他 Indie Hackers / Starter Story 类的播客，属典型的"主业 + 副业 indie hacker"路径。

## 定价 / 商业模式

- **起步价**：$5（即可上榜）
- **计费模式**：累计支付金额 = 当前排名；加价差挤对手，不需要从头付
- **结算**：Stripe
- **承接量**：物理内裤只能印前 22 名 → 22 名之后等于"露脸不出镜"
- **退款政策**：官网明确 no refunds
- **实时榜单快照（2026-09-09 抓取）**：#1 由 Smackdab CRM 以 $25 占据（"Steal spot for $25"），在线 10 人，累计访客 1,625 人
- **商业模式本质**：不是 SaaS，不是订阅，是一个一次性的"竞猜/拍卖式广告位"。本身没有软件订阅收入，靠每笔 $5+ 的付款产生现金流，但成交越多意味着内裤越满——是个会自我饱和的产品

## 关联信息 / 生态

- **官方竞品对比定位**："more with attention-grabbing PR stunts than with traditional ad tech"——对标的是 PR stunt，不是 Meta Ads / Google Ads
- **目标受众**：indie hackers、SaaS 创始人、meme 账号、加密项目、niche 电商
- **传播机制**：网站本身（leaderboard）+ 实物（内裤被作者穿出门被拍照）+ X 趋势（创始人提到一条趋势拿到 1M 浏览）三层叠加
- **彩蛋**：网站有一个 "pull the boxers down" 的隐藏互动

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-09-09 | PH 发布，第 6 名，126 票 / 18 评论 |
| （更早） | "as a joke" 启动，作者称是想做 "small protest" |

## 评论区反馈（事实摘录，不评价）

- 提问者："reach 到底有多少？" / 创始人回：reach 就是拍卖本身——公开 leaderboard + X 1M 浏览的趋势 + 内裤被到处发图
- 创始人自述："I cut every feature that wasn't funnier"——能砍的功能都砍了
- 创始人金句：
  - "Ask me anything. Especially about the tattoo."
  - "writing Terms of Service for a pair of boxers with a straight face"
  - "outbidding a SaaS company for the left cheek at 2am"
- 整体社区氛围：觉得好笑、夸简洁、有人说是 "rainy day better"（消磨时间的最优解）

**可见的具体评论者（PH 页抓取样本，按时间倒序）**：

- **Maria Anosova**（@maria_anosova，2h 前）："That's funny. I wonder what kind of reach will this type of advertising have?"
- **Julian Ting**（@julian_ting2，6h 前）："Honestly, the simplicity is what makes this funny."
- **Maria Telegina**（@maria_telegina，5h 前）："Made a rainy day better. Thanks for reminding that marketing should be fun!"
- **Dascalita Neculai**（@dascalita_neculai，4h 前）："the roi is real here"
- **Adana Marukhyan**（@adana，7h 前）："The funniest launch I've seen yet!"
- **Joyce Spencer**（@joyce_spencer1，8h 前）："Hahaha, nice idea! Wish you all the best with ass.auction"
- **Daniel Nwankwo**（@daniel_nwankwo，9h 前）："😂😂😂😭"

> 18 条评论中其余约 11 条在抓取片段里未完整呈现。整体评论基调：轻松玩梗、无深度质疑、亦无品牌方现身说法承认付费。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/ass-auction — 拿到：tagline、票数、评论数、品类、launch 日期
- PH 论坛帖（`/p/ass-auction`）：拿到：创始人自述、机制细节、引用金句
- 公开报道：未独立报道（ProductCool 是归档站，非新闻），无主流媒体覆盖
- GitHub：无公开仓库
- 创始人个人站：mahdif.com / mahdif.github.io — 拿到：职业背景、过往项目列表

## 未查到 / 待补

- **具体哪些品牌真的付了钱**：未查到（评论区和 leaderboard 都没公开具体名单）
- **总成交额 / GMV**：未查到
- **内裤实物是否已印出来 / 被穿上**：未查到图片证据，只有创始人自述
- **X 1M 浏览的趋势原帖**：未查到具体推文链接
- **是否真有人"被印上 logo"**：未查到图证
- **公司主体 / 收款主体**：未披露
- **Stripe 收款方**：未披露
- **22 个位次满了之后怎么办**（重开新一轮？换内裤？涨价？）：未查到说明
