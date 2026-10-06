# YourSitee · 扩展阅读上下文

> PT 2026-08-02 Product Hunt 榜单第 3 名 · 👍 约 213 · 💬 未查到精确数
> 归档日期 2026-08-03 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | YourSitee |
| 英文 tagline | Make your bio link worth clicking |
| 中文 tagline | 让你的 bio 链接值得被点 |
| 官网 | https://yoursit.ee/ （yoursitee.com 301 跳转至此） |
| PH 页 | https://www.producthunt.com/products/yoursitee |
| 品类标签 | Website Builders · Social Media Management · No-Code Website Builder |
| 票数 / 评论 | 约 213 票 / PH 页显示 307 followers，评论数未精确抓取 |
| 公司主体 | 未查到注册主体；团队标注 "Built in Hungary 🇭🇺" |
| logo | https://ph-files.imgix.net/701f9f04-01cb-4405-a25f-c212a02610e9.png |
| GitHub Sponsors | https://github.com/sponsors/YourSitee（开源仓库未查到） |

## 是做什么的（如实复述，不评价）

YourSitee 是一个**可视化 link-in-bio 平台**：把链接、社交账号、内容、在线身份整合到一个可自定义的页面，链接以**卡片（detailed cards）**形式呈现而不是按钮清单。提供 20+ widget（YouTube、Instagram、Spotify、GitHub、TikTok、Twitch、Last.fm、Patreon、Ko-fi、Buy Me a Coffee、Cal.com 等），支持 AI 从 Linktree URL 导入旧页面。内置分析（访问、点击、访客国家、Top 链接）。形态是网页 builder + 托管 bio 页。

## 解决什么问题（事实层面，不判断值不值得解）

- **bio 工具页面同质化**：创始人 Andras 表述"bio 页要么是一列链接、要么是过度堆砌的 creator stack，我们想做中间的东西"。
- **迁移摩擦高**：用户从 Linktree 等迁走要手动重建，"迁移不应成为留在不再喜欢的工具里的理由"（创始人原话）。
- **免费层被卡**：评论区 Sarvesh "Linktree 在 free plan 上感觉过时"。YourSitee 把核心体验放在 Free。
- **目标场景**：创作者、学生、专业人士、小商家、社区把零散在线身份整合到一页。

## 怎么做的（技术原理/机制，事实层面）

来源：YourSitee 官网 + PH 创始人评论

- **卡片式渲染**：链接以"详细卡片"展示，而非按钮列表；可自由排版 widget。
- **AI 导入**：粘贴 Linktree URL，AI 生成起始版本（官网提醒"需复核结果"）。
- **自定义维度**：profile / colors / fonts / background / layout / widgets。
- **分析**：访问量、点击、访客国家、Top 链接（不同套餐历史保留 30 天 / 90 天）。
- **集成**：官网首页列出 31 个平台 icon（Reddit、GitHub、Steam、SoundCloud、Discord、Twitch、YouTube、X、Bluesky、Threads、Patreon、PayPal、Ko-fi 等）。
- **闭源**：未查到公开代码仓库，仅有 GitHub Sponsors 页面。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 CEO | András Czeizel（2022 起意，注册 yoursit.ee 域名 2022-12-27） | 官网 /about |
| 联合创始人 CTO | Ábel Herfort（2023-09 加入；同时任 BlackRock 平台/后端工程师） | 官网 /about |
| 联合创始人 Lead Engineer | Dávid Szalovszky（2023-09 加入） | 官网 /about |
| 团队 | 三位创始人 + harey、xou、David、vvdesign、fish、Pearoo、satoko、Adam；远程、兼职（含大学与全职工作） | 官网 /about |
| 起源 | 2022 年 András 找分享项目的方式受挫 → 受一个匈牙利社区自建平台启发（该平台后消失，但 idea 留下）→ 2023 重建 → 2023-12-24 closed alpha → beta → 2026 公开上线 | 官网 /about |
| 融资 | **Bootstrapped**，无外部投资；50+ 早期付费支持者在平台还免费未完成时赞助 | 官网 /about |
| 加速器 | 未查到 | — |
| 早期 traction | 官方称 1300+ 用户创建 Sitee；50+ 早期财务支持者 | 官网 /about |

## 定价 / 商业模式

来源：yoursit.ee/pricing（2026-08-03 抓取）

- **Free $0（永久）**：可视化 profile + rich widget、颜色/布局/profile media、标准字体；动态 widget ≤15、图片 widget ≤2、外链自定义图 ≤3、社交链接 ≤9、联系按钮 1；分析历史 30 天；用户名 14 天改一次。不含：渐变背景、Pro badge/Discord 角色、widget 隐藏/spotlight/赞助标、自定义联系按钮样式、外链描述。
- **Pro $10/月 或 $100/年**（年付省 $20；PH 页另说 "$5/月" 与 FAQ "$10/月" 自相矛盾，以 FAQ 为准）：Free 全部 + Pro badge & Discord 角色；动态 widget ≤30、图片 widget ≤10、外链自定义图 ≤10、社交链接 ≤12、联系按钮 2；标准 + Pro 字体；渐变背景；自定义联系按钮颜色/图标；外链描述；隐藏 widget；spotlight 推荐位；赞助内容标签；分析历史 90 天；用户名 24h 改一次。
- **PH 推广**：launch 当日 "30 days free, on us!"（应为 Pro 试用 30 天，未明确）
- 模式：核心体验永久免费 + Pro 订阅（月/年）卖高级 widget 配额、样式、分析历史。无企业版/定制。

## 关联信息 / 生态

- **社区入口**：Discord、X、Instagram、Telegram
- **基础设施**：status.yoursit.ee、help.yoursit.ee、blog.yoursit.ee
- **合规页面**：Privacy、Terms、Community Standards、Law Enforcement、Impressum、Acknowledgements
- **llms.txt**：官网根有 /llms.txt（面向 LLM 的站点描述文件）
- **竞品定位**（PH 页类似产品）：Taplink（5.0/316 评）、Linktree（4.6/24）、Hopp by Wix（4.9/11）、Beacons（5.0/11）、Tiles（5.0/3）

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2022-12-27 | yoursit.ee 域名注册 |
| 2023-09 | Ábel Herfort、Dávid Szalovszky 加入为联合创始人 |
| 2023-12-24 | Closed Alpha 上线（圣诞夜） |
| 2024 | Beta 阶段 |
| 2026-08-02 | PH 公开上线，当日榜 #3 |

## 评论区反馈（事实摘录，不评价）

- **Vikram** 问：能否给 widget 加密码/邮箱门控用于数字下载 → 创始人答：暂未，但在 roadmap。
- **Dogan Akbulut** 问集成 → 创始人列 20+ 当前集成。
- **Sarvesh Chidambaram**：Linktree 在 free plan 上感觉过时，想换。
- **Sercan Karagül**：夸 AI importer，widget "feel curated instead of bloated"。
- **Andras（创始人）**："bio 页要么是一列链接、要么是过度堆砌的 creator stack，我们想做中间的东西"；"迁移不应成为留在不再喜欢的工具里的理由"。
- **Dávid（创始人）**：保持编辑器简单，同时给用户"足够自由做出不像别人的页面"。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/yoursitee（tagline、213 票、#3、三位创始人、logo URL、PH post ID 757840）
- 官网首页：https://yoursit.ee/（卡片式 link-in-bio 定位、31 平台 icon、子页面索引）
- 官网 /pricing：https://yoursit.ee/pricing（Free / Pro 套餐明细，$5 vs $10 矛盾）
- 官网 /about：https://yoursit.ee/about（创始团队、起源故事 2022、bootstrapped、50+ 早期支持者、1300+ 用户、里程碑时间线）
- GitHub Sponsors：https://github.com/sponsors/YourSitee（仅赞助页，无公开代码仓库）

## 未查到 / 待补

- **公司注册主体/注册地**：官网 Impressum 未深入抓取，仅知 "Built in Hungary"
- **精确评论数**：PH 页未抓到评论数字，仅有 followers=307、votes≈213
- **Pro 精确价格**：pricing 卡片显示 $5/月，FAQ 显示 $10/月或 $100/年，二者矛盾，未澄清
- **PH "30 days free" 含义**：未明确是 Pro 试用 30 天还是其他
- **融资金额/投资方**：bootstrapped，无外部投资；官网表态"对契合愿景的投资人保持对话"但未启动融资
- **加速器背景**：未查到
- **GitHub 公开仓库**：未查到，仅有 Sponsors 页
- **精确活跃用户/留存数据**：官方称 1300+ 用户创建 Sitee，无 MAU/留存
