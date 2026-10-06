# Zen Whisper · 扩展阅读上下文

> PT 2026-08-02 Product Hunt 榜单第 5 名 · 👍 134 · 💬 17
> 归档日期 2026-08-02 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Zen Whisper |
| 英文 tagline | On-device Mac dictation that types into any app |
| 中文 tagline | 可在任意 Mac 应用中使用的本地语音输入工具 |
| 官网 | https://zenproducts.ai |
| PH 页 | https://www.producthunt.com/products/zen-whisper |
| 品类标签 | Productivity · Writing · Menu Bar Apps |
| 票数 / 评论 | 134 / 17 |
| 公司主体 | ZENPRODUCTS TECHNOLOGIES PRIVATE LIMITED（zenproducts.ai 页脚版权） |
| logo | https://ph-files.imgix.net/30730b1c-fffe-40bb-b2fc-4091bf12b05a.png |
| 联系邮箱 | hello@zenproducts.ai |
| 社交 | X/Twitter @getzenproducts |
| 产品编号 | zenproducts.ai 产品矩阵第 03 号（共 8 款） |

## 是做什么的（如实复述，不评价）

Zen Whisper 是一款 **本地优先（local-first）的 Mac 听写+转写工具**，形态为菜单栏应用。用户按住快捷键即可在任意 Mac 应用中听写，核心语音识别在设备本地运行，音频不发送到云端。除实时听写外，还支持长录音/会议语音备忘、媒体文件转写（上传音视频或粘贴 YouTube 等公开链接）、转写历史搜索、以及本地写作工具（语法修正、改写、正式化、缩短、扩写、清理选中文字）。Pro 档解锁更大模型与翻译功能。

定位：不是"又一个云听写"，而是把听写、长录音转写、媒体转写、写作后处理整合在一个本地工作流里。

## 解决什么问题（事实层面，不判断值不值得解）

- **云端听写延迟与隐私顾虑**：云端 STT 有往返延迟，评论用户 Rui Min 称长文本场景"unusable for anything longer than a quick note"；音频上传云端有隐私顾虑。Zen Whisper 本地跑，音频不离开设备。
- **技术词汇识别差**：通用模型对 API 名、包名、产品名等专有词识别弱。Zen Whisper 内置自定义词典+代码片段（dictionary & snippets）针对专有词训练。
- **多语言弱，尤其印度地区语言**：官方称支持 100+ 语言，特别强化印度多语言工作流。
- **工具碎片化**：听写、长录音转写、媒体转写、文本润色分散在多个应用。Zen Whisper 整合为一个工作流。
- **目标场景**：长篇听写、会议录音转写、YouTube 等媒体转写、技术文档口述、多语言写作。

## 怎么做的（技术原理/机制，事实层面）

来源：zenproducts.ai + PH 创始人评论区

- **本地语音识别**：核心 STT 在 Mac 本地运行，"core speech recognition on your Mac"，不发送音频到云端。
- **模型策略**：未明确命名模型架构。产品名 "Zen Whisper" 暗示基于 OpenAI Whisper 系列本地模型，但官网/PH 页未明确说明。Pro 档提供"larger models"，暗示有模型档位分层。
- **快捷键听写**：按住快捷键在任意 Mac 应用中输入。
- **自定义词典+代码片段**：针对 API 名、包名、产品名等专有词做用户级训练。
- **媒体转写**：上传文件或粘贴公开媒体链接（如 YouTube）。
- **本地写作工具**：选中文字后做语法修正/改写/正式化/缩短/扩写，本地执行。
- **隐私设计**："Your data is encrypted on your device before anything syncs"。
- **菜单栏应用**：常驻后台，"lightweight on system resources"。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 公司主体 | ZENPRODUCTS TECHNOLOGIES PRIVATE LIMITED | zenproducts.ai 页脚 |
| 产品矩阵 | 8 款产品（Zen Passwords / Zen Horology / Zen Whisper / Zen Slate / Zen Teleprompter / Zen LeanTracker / Bulk Delete / Swifty Car） | zenproducts.ai/about |
| 创始人 | 未查到（官网未署名个人） | — |
| 团队规模 | 未披露（"we" 自称） | — |
| 融资 | 未查到（官网无 About/Newsroom 融资公告） | — |
| 投资方 | 未查到 | — |
| 加速器 | 未查到 | — |
| 合规认证 | 未查到 | — |

## 定价 / 商业模式

来源：PH 产品页 + zenproducts.ai + Gumroad 链接

- **Free**：免费试用 + 免费档长期可用，"starts with a free trial, stays usable on the free tier after that"
- **Pro**：付费解锁更大模型 + 翻译功能，通过 Gumroad 售卖（PH 页显示 "Free Options" 标签，具体价格未在 PH 页和官网公开）
- 模式：freemium（免费可用 + Pro 升级），按一次性或订阅未明确（Gumroad 404 无法确认）

## 关联信息 / 生态

- **同类竞品**（PH 页列出）：Wispr Flow（4.7/73 评论）、superwhisper（4.9/21）、TalkTastic（4.9/26）、MacWhisper（4.9/7）、Snaply（5.0/6）
- **平台**：仅 Mac，无 iOS 版。创始人称 iOS 上麦克风在听写结束后仍会持续激活（橙色指示灯），在 Apple 改进该隐私控制前不上 iOS；"If Apple loosens that control in the future, we could move on an iOS launch very quickly."
- **zenproducts.ai 产品矩阵**：覆盖 iPhone/iPad/Mac/Chrome 平台，主打"privacy-first, one task done well"。

## 技术时间线（官网里程碑，若有）

官网无里程碑页。未查到。

## 评论区反馈（事实摘录，不评价）

- **Gal Dayan**（提问）：技术词汇识别如何？/ 创始人回复：内置 dictionary + snippets 针对专有词训练，附演示视频。
- **Avery Hope**（提问）：转写历史搜索如何？/ 创始人回复：强调 "no extra tab, no unnecessary cloud hop"——实时听写、转写搜索、语音备忘、长录音、媒体转写一个工作流闭环。
- **Ankur Jeswani**（提问）：iOS 版？/ 创始人回复：iOS mic 隐私控制问题暂不发布，等 Apple 放宽。
- **Rui Min**（用户反馈）：本地跑避免云端往返延迟，长文本场景可用（暗指云听写不可用）。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/zen-whisper（创始人 ZenProducts 评论区、定价标签、logo、竞品列表）
- 官网首页：https://zenproducts.ai（产品描述、privacy-first 哲学、公司主体）
- 官网 About：https://zenproducts.ai/about（8 款产品矩阵、公司主体、价值观）
- Gumroad 售卖页：404，无法确认 Pro 具体价格
- 公开报道：未查到融资/创始人背景报道

## 未查到 / 待补

- **创始人姓名/个人背景**：官网未署名，未查到
- **融资金额/轮次/投资方/加速器**：无 About/Newsroom 融资公告，未查到
- **团队规模**：仅 "we" 自称，具体人数未披露
- **Pro 档具体价格**：Gumroad 页 404，PH 页和官网均未公开数字
- **STT 模型架构**：未明确命名（疑似 Whisper 系列，但无官方确认）
- **准确率基准数据**：PH 页无量化准确率声明，创始人强调质量但未给数字
- **GitHub**：未查（疑似无公开仓库，闭源商业产品）
- **公司注册地**：未查到（公司名含 PRIVATE LIMITED，疑似印度注册，未证实）
