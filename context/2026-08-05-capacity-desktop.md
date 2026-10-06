# Capacity Desktop · 扩展阅读上下文

> PT 2026-08-05 Product Hunt 榜单第 9 名 · 👍 140 · 💬 8
> 归档日期 2026-08-06 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Capacity Desktop |
| 英文 tagline | A free Lovable that lives on your Mac |
| 中文 tagline | Mac 上的免费 Lovable |
| 官网 | https://capacity.so/desktop |
| PH 页 | https://www.producthunt.com/products/capacity |
| GitHub | 未查到公开仓库（闭源产品） |
| 品类标签 | Website Builder · Artificial Intelligence · No-Code |
| 票数 / 评论 | 140 / 8 |
| 公司主体 | Capacity（2 位联合创始人） |
| logo | https://ph-files.imgix.net/4a00c723-c329-4e83-9d0a-d7bfcc7649e6.png |
| 创始人/maker | Samuel Rondot (Co-Founder), Baptiste Studer (Co-Founder) |

## 是做什么的（如实复述，不评价）

Capacity Desktop 是一个 **Mac 原生桌面应用**，用自然语言生成全栈 web/mobile/desktop 应用。用户选择设计模板、用英文描述想法，应用会在本地 Mac 上构建真实可运行的 app，一键发布到网络。

核心定位是"**A free Lovable on your Mac**"——对标 Lovable（热门 AI 全栈应用构建工具），但：
- **使用用户自己的 AI 订阅**（Claude / GPT / Open Router API key），按 AI 提供商成本价计费，无加价积分
- **代码和构建过程在本地 Mac 上**，不依赖 Capacity 的云服务器
- **代码属于用户**，可导出完整代码库、连接自己的 GitHub、使用自定义域名
- **无锁定**：构建的应用不绑定 Capacity 平台

官网描述："Build web, mobile & desktop apps with AI on your Mac. 80+ designer templates, one-click publish, one-click undo — your AI subscriptions, your GitHub, your code. No credit card required."

## 解决什么问题（事实层面，不判断值不值得解）

- **AI 应用构建工具的积分系统不透明**：Lovable 等竞品按"积分"计费，用户不知道失败的修复循环消耗了多少积分，工具从用户的重试中获利。Capacity 创始人在 PH 页评论中明确表态："Our take is that you feel the credits system is unfair, you never know what a failed fix loop just cost you, and you feel the tool profits from your retries."
- **代码锁定在平台上**：竞品生成的代码托管在平台服务器，导出受限或需付费。Capacity 让代码在用户本地 Mac 生成和存储。
- **AI 服务加价**：竞品对 AI API 调用加价再转给用户。Capacity 让用户直接使用自己的 Claude/GPT key，按成本价计费。
- **缺少规划阶段，直接猜测需求**：多数 AI 构建工具拿到一句话就开始构建，Capacity 提供"Spec Mode"——先提问、写规划文档（plain words），用户确认后再构建（"Plan first, build better"）。
- **目标用户**：非技术创始人、独立开发者、小团队，想快速构建 MVP 但不想被工具锁定、不想为 AI 调用多付钱。

## 怎么做的（技术原理/机制，事实层面）

来源：官网 capacity.so/desktop + capacity.so/pricing + capacity.so/about-us + PH 产品页

### 构建模式
- **Vibe Coding**：从一句 prompt 直接生成原型，快速验证想法
- **Spec Coding（核心差异化）**：AI 先提问（项目简介、用户体验、设计要求、技术架构），生成结构化规划文档（project-spec.md），用户审阅确认后再构建。规划文档包含：
  - Project Brief（目标和范围）
  - User Experience（用户角色和旅程）
  - Design（组件和风格）
  - Technical Architecture（技术栈、数据模型、SEO 策略）
- **AI Co-founder**：交互式助手，用户可随时问"接下来做什么""为什么这里看起来不对""怎么获得第一批用户"，AI 用自然语言回答并执行工作

### 技术栈与集成
- **前端**：React + Tailwind CSS
- **后端**：Supabase（认证、数据库、API）
- **AI 模型**：用户自带 API key，支持 Claude、GPT、Open Router
- **版本控制**：连接用户自己的 GitHub 账号
- **部署**：内置托管（免费）+ 自定义域名支持
- **模板**：80+ 设计师模板（官方称）

### 定价与积分机制
- **Desktop 应用本身**：免费，无需信用卡，无需注册（官网强调"Free, no sign-up"）
- **云端 Web 版 Capacity.so**：按积分计费（用户在平台上构建时消耗 Capacity 提供的 AI 服务）
  - Starter: $25/月（100 credits）
  - Growth: $69/月（250 credits）- 最受欢迎
  - Professional: $129/月（500 credits）
  - Business: $299/月（1000 credits）
  - 一次性充值包：10 credits $9 / 50 credits $39 / 100 credits $69
  - 积分规则："每条消息根据任务复杂度消耗可变数量积分，简单请求消耗少，复杂操作（构建功能、调试代码）消耗多。按使用量付费，积分永不过期。"
- **Desktop vs Web 定价差异**：Desktop 版让用户使用自己的 AI key，避开 Capacity 的积分系统，直接按 Claude/OpenAI 成本价计费。这是核心卖点之一。

### 其他功能特性
- **One-click undo**：一键撤销上一次构建变更
- **One-click publish**：一键发布到网络（内置托管 + SSL）
- **代码导出**：完整代码库可导出（Growth 及以上计划）
- **Living Documentation**：规划文档随代码迭代同步更新
- **Self-Fixing Code**：AI 检测和修复代码问题

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Samuel Rondot (Co-Founder), Baptiste Studer (Co-Founder) | capacity.so/about-us |
| 团队规模 | 2 位联合创始人（"team of 2 co-founders"） | capacity.so/about-us |
| 成立时间 | 2024 年末（"late 2024"） | capacity.so/about-us |
| 融资 | 未查到公开融资信息 | — |
| 投资方 | 未查到 | — |
| 加速器 | 未查到 | — |
| 团队背景 | 自述"Vibe coders since day 1"，希望让无编程技能的人也能构建优秀应用和网站 | capacity.so/about-us |

## 定价 / 商业模式

- **Desktop 应用**：免费（用户自带 AI key，成本由用户直接付给 Claude/OpenAI）
- **Web 版 SaaS**：订阅制 + 积分消耗制（$25-$299/月，覆盖 Starter 到 Business 四档）
- **一次性充值包**：无需订阅，按需购买积分（$9-$69）
- **增值服务**：
  - 代码导出（Growth $69/月起）
  - 自定义域名（Growth $69/月起）
  - WhatsApp 专属支持频道（Growth $69/月起）
  - 专属客户成功经理（Business $299/月）
  - 定制集成（Business $299/月）
- **联盟计划**：20% 终身经常性佣金，60 天归因期，$100 最低提现

商业模式：**Freemium + BYOK (Bring Your Own Key)**。Desktop 版用免费策略获客（用户零成本试用，用自己的 AI key），Web 版 SaaS 对不想自己管 API key 的用户收费。积分永不过期降低用户顾虑。

## 关联信息 / 生态

- **对标产品**：Lovable（主要竞品，Capacity 明确定位为"free Lovable"）
- **技术生态**：React、Tailwind CSS、Supabase、Claude、GPT、Open Router
- **替代品场景**（官方营销点）：
  - 从 Lovable 迁移：因积分消失快或应用达到复杂度上限
  - 从 Bubble 迁移：需要 AI 辅助全栈开发而非纯 no-code
- **目标人群**：首次创业的创始人、独立开发者、远程团队、小型机构、需要快速 MVP 的创业者

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2024 年末 | Capacity 成立（2 位联合创始人） |
| 2026-08-05 | Capacity Desktop 登 PH 日榜第 9 名（140 票/8 评） |

## 评论区反馈（事实摘录，不评价）

由于网络限制未能抓取 PH 评论区详情，待后续补充。根据搜索结果显示的 PH 页文案：
- 创始人明确表态：积分系统不公平，用户不知道失败循环花了多少钱，工具从重试中获利——这是设计 Desktop 版（用户自带 key）的核心动机
- 强调"Your code, your GitHub, your own AI at cost. No marked-up credits, no lock-in. Free, no sign-up."

## 信息来源

- 官网 Desktop 页：https://capacity.so/desktop（产品描述、技术特性、"A free Lovable on your Mac" 定位）
- 官网定价页：https://capacity.so/pricing（四档订阅计划 + 一次性充值包 + 积分规则）
- 官网 About Us 页：https://capacity.so/about-us（2 位联合创始人、成立时间 2024 年末、团队动机）
- PH 产品页：https://www.producthunt.com/products/capacity（tagline、品类标签、票数、创始人对积分系统的表态）
- PH 榜单档案：/Users/hut/Projects/ph-daily/archive/2026-08-05.md（排名第 9、140 票/8 评）
- 对比页：https://dupple.com/compare/capacity-vs-lovable（与 Lovable 的功能差异）
- 替代品页：https://capacity.so/alternatives/lovable（为何从 Lovable 迁移到 Capacity）
- AlternativeTo 页面：https://alternativeto.net/software/capacity-so/about/（订阅价格范围 $25-$320/月 + 免费版）

## 未查到 / 待补

- **PH 评论区详细反馈**：因网络限制未能抓取完整评论（8 条评论内容）
- **GitHub 仓库**：未查到公开开源仓库（闭源产品）
- **融资金额/投资方/加速器**：无公开融资信息
- **产品 logo URL**：需从 PH 页 HTML 中提取 ph-files.imgix.net 图片
- **用户数量/案例**：官网提到"thousands of people with no coding experience"但未给出确切数字
- **Desktop 应用下载量/活跃用户**：未查到
- **80+ 模板的具体分类**：官网提及但未详细列出
- **团队成员背景**：Samuel Rondot 和 Baptiste Studer 的职业履历未查到
- **与 Lovable 的具体功能对比表**：虽有对比页，但因网络限制未能提取完整对比维度
