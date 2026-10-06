# FreqWave EQ · 扩展阅读上下文

> PT 2026-08-02 Product Hunt 榜单第 10 名 · 👍 93 · 💬 8
> 归档日期 2026-08-03 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | FreqWave EQ |
| 英文 tagline | Customize your web audio with a real-time EQ |
| 中文 tagline | 用实时均衡器定制网页音频 |
| 官网 | https://bob3x.github.io/freqwave-eq |
| PH 页 | https://www.producthunt.com/products/freqwave-eq-browser-audio-equalizer |
| GitHub | https://github.com/Bob3x/freqwave-eq |
| 品类标签 | Chrome Extensions · Music · GitHub |
| 票数 / 评论 | 93 / 8 |
| 公司主体 | 个人开发者项目（无公司主体） |
| 创始人 / Maker | Borislav Ginov（@borislavginov，GitHub: Bob3x） |
| logo | https://ph-files.imgix.net/cabf6ec0-90c5-49db-930e-5f399b90a3e8.gif |

## 是做什么的（如实复述，不评价）

FreqWave EQ 是一款 **8 段参数均衡器（8-band parametric EQ）Chrome 浏览器扩展**，通过 Web Audio API 实时处理网页中的 HTML5 音频/视频流，让用户在任何标准网页媒体（YouTube、Twitch、SoundCloud、播客等）上调节频响、增强人声、应用压缩。形态是浏览器扩展（Manifest V3，使用 offscreen document 做音频处理），核心能力是实时 EQ + 语音增强 DSP + 频谱可视化。

## 解决什么问题（事实层面，不判断值不值得解）

- **播客/直播音质差**： muddy（浑浊）、harsh（刺耳）、对话太轻——创始人称"播客那种罐头音效就是我做这个扩展的主要原因之一"。
- **网页端没有可用 EQ**：系统级 EQ 不针对单个网页，浏览器原生不提供音频频响控制；现有扩展多为简单音量/低频增强，缺参数化能力。
- **DRM 流媒体不可处理**：Netflix、Spotify Web 等 EME 保护流在浏览器层禁止音频节点访问——这是 Web 平台限制，FreqWave 也不支持（创始人明确说明）。
- **目标场景**：YouTube、Twitch、SoundCloud、播客站点、视频会议网页端等标准 HTML5 媒体。

## 怎么做的（技术原理/机制，事实层面）

来源：GitHub README + PH 创始人评论

- **8 段参数化 EQ**：覆盖 sub-bass / midrange / treble，参数化（每段可调频率/增益/Q，而非仅推子）。
- **Voice Enhancer DSP**：三种预设模式——DIALOGUE / LEVELER / CLARITY，针对人声和对话场景。
- **DSP 压缩**：内置动态压缩，提亮低音量对话。
- **实时频谱可视化**：弹窗内显示实时频谱。
- **MV3 + offscreen document**：Manifest V3 下用 isolated offscreen document 跑 Web Audio API（chrome.tabCapture），规避 service worker 不可直接处理音频的限制。
- **状态持久化**：`chrome.storage.sync` 全局保留 EQ 设置，跨浏览器重启生效。
- **Per-domain 自动切换**：**未上线**，创始人称计划在下个版本加入。
- **DRM 限制**：对 Netflix / Spotify Web 等 EME 保护流不工作（Web 平台限制，非产品缺陷）。
- **技术栈**：VS Code + Vite + React + Chrome Extension MV3。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Borislav Ginov（@borislavginov / Bob3x） | PH 产品页 / GitHub |
| 团队规模 | 个人开发者（未披露其他成员） | GitHub 仓库无 contributor 列表 |
| 融资 | 未查到（个人项目，无融资公告） | — |
| 加速器 | 未查到 | — |
| 开源协议 | MIT | GitHub |

## 定价 / 商业模式

来源：PH 产品页 + GitHub README

- **完全免费 + 开源（MIT）**：扩展本身免费，源代码公开。
- **捐赠通道**：Buy Me A Coffee（buymeacoffee.com/borislavginov）——非订阅非付费，自愿捐赠。
- **无 freemium / 无付费层**：所有功能（8 段 EQ、Voice Enhancer、压缩、可视化、持久化）全部免费。
- 模式：开源 + 捐赠。无 SaaS、无订阅、无企业版。

## 关联信息 / 生态

- **PH "Similar Products"**：Browser FX、Ritmo、SuperDev Pro、Jiffy Reader、Dark Reader
- **技术生态**：Chrome 扩展 MV3 生态，依赖 chrome.tabCapture + Web Audio API + chrome.storage.sync
- **DRM 边界**：明确不支持 Netflix / Spotify Web（EME 保护流）
- **GitHub 指标**：2 stars / 1 fork / 27 commits / MIT license

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-08-02 | PH 上线首日，排第 10 名，93 票 |
| 下个版本（计划） | Per-domain 自动切换（创始人评论区说明） |

## 评论区反馈（事实摘录，不评价）

- **Yuki_Code1**（提问）：DRM 流媒体支持吗？ / **创始人回复**：标准 HTML5 媒体支持，Netflix/Spotify Web 等 EME 保护流不支持，碰到了 Web 平台的墙。
- **Gal Dayan**（提问）：EQ 设置会持久化吗？ / **创始人回复**：全局保留最后配置，跨浏览器重启生效；per-domain 自动切换下个版本上。
- **Emirhan**（讨论）：播客那种罐头音效。 / **创始人回复**：这正是做这个扩展的主要原因之一。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/freqwave-eq-browser-audio-equalizer（tagline、95 票/8 评论、maker Borislav Ginov、创始人评论区回复、logo URL、相似产品列表）
- GitHub 仓库：https://github.com/Bob3x/freqwave-eq（MIT、2 stars/1 fork、README 技术细节：MV3 offscreen document、chrome.storage.sync、Voice Enhancer 三模式、DRM 限制说明、技术栈、捐赠链接）
- 官网：https://bob3x.github.io/freqwave-eq（ECONNRESET，未抓到内容，待补）
- 公开报道：搜索 freqwave.app / audiotechweekly.com 均未命中真实页面（搜索结果为重复 PH 描述，无独立评测）

## 未查到 / 待补

- **创始人背景**：Borislav Ginov 的过往经历、所在地、其他项目，未查到
- **团队规模**：疑似个人项目，GitHub 无 contributor 列表
- **融资 / 加速器**：未查到（个人开源项目，可能无）
- **官网内容**：bob3x.github.io/freqwave-eq 抓取时 ECONNRESET，未拿到截图/文案
- **用户量 / 安装量**：PH 页只显示 112 followers，未披露 Chrome Web Store 安装数
- **公开评测**：搜索到的 "Audio Tech Weekly" 链接无法解析（ENOTFOUND），未拿到独立第三方评测
- **Chrome Web Store 详情**：直接访问 chromewebstore.google.com 主页未命中 FreqWave EQ 条目，具体评分/评论数待补
- **commit 最新日期**：GitHub 显示 27 commits，未显示具体最后 commit 日期
