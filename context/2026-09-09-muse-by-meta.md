---
# 结构化元数据（用于索引和聚合）
product: "Muse by Meta"
slug: "muse-by-meta"
date: "2026-09-09"
rank: 5
votes: 173
comments: 5

# 分类标签
category: "AI agent"
subcategory: "个人助理 / 自主代理"
tags: ["Meta", "WhatsApp", "Messenger", "AI agent", "自主代理", "闭源模型", "Stripe", "Zuckerberg", "Alexandr Wang", "MSL", "Agent安全", "Action Economy"]

# 技术信息
tech_stack: ["Muse Spark (闭源 LLM, 自称 100 万 token context)", "Muse Secure VM (systemd-nspawn 容器 + eBPF Sentinel)", "Hatch daemon (agentic harness)", "Headless Chromium (通过 a11y tree broker)", "Stripe Link 单次虚拟卡", "MTIA 推理芯片 (Meta 自研)", "Ray-Ban Meta glasses (前端)"]
platform: ["iOS", "Android", "Web (muse.ai)", "WhatsApp", "Ray-Ban Meta glasses"]
open_source: false
license: "未公开（闭源；Eyestech 报道提到 30B 参数的 Muse Glimmer 是 open-weight, 待 Meta 官方确认）"

# 商业信息
business_model: "Freemium + 订阅制"
pricing_start: "免费；Power $20/月；Maximum 上至 $100/月"
funding_stage: "未披露（Meta 内部孵化，Meta Superintelligence Labs 出品）"
funding_amount: "未披露"

# 关联信息
related_products: ["ChatGPT Work Mode", "Google Gemini Spark 3.8", "xAI Grok Bot (Grok 4.6)", "Perplexity Comet", "Poke.com", "Manus", "Claude for Desktop", "Pally", "BetterClaw", "Littlebird"]
maker_previous: ["Alexandr Wang (Scale AI 创始人, MSL Chief AI Officer)", "Nat Friedman (前 GitHub CEO, 报道为 MSL 联合负责人)"]

# 速览信号
key_signals:
  - "Meta 官方出品 (Meta Superintelligence Labs)，是 Meta AI 助手升级版而非新独立产品：用户身份、模型能力、消息渠道全继承"
  - "史上最大分发入口：WhatsApp 2B+ 用户直接对话即用，无需 API key/插件；同时上 iOS/Android/Web/Ray-Ban Meta 眼镜"
  - "架构核心是「每用户独立 Linux VM (Muse Secure VM)」+ Sentinel 守护：模型在隔离沙箱跑，凭证由 hatch-authd 代理、网络由 eBPF taint 跟踪，Stripe Link 发一次性虚拟卡"
  - "公开价目三档 Free / $20 / 上至 $100，免费档是拉用户入口 (CEO 称大部分用户停留在免费层)，付费档靠 MTIA 自研芯片 + 广告收入补贴推理成本"

# 元信息
archived_at: "2026-09-10"
sources_count: 12
---

# Muse by Meta · 扩展阅读上下文

> PT 2026-09-09 Product Hunt 榜单第 5 · 👍 173 · 💬 5  
> 归档日期 2026-09-10 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Muse (官方称 "Muse by Meta"，PH 简称) |
| 英文 tagline | Your personal AI agent that gets things done |
| 中文 tagline | 你的私人 AI 代理，能把事情办成 |
| 官网 | https://muse.ai (PH 页与报道均指此域名；待补：muse.ai 历史上是一家独立 AI 视频平台，是否已转手给 Meta 或为新购域，未确认) |
| PH 页 | https://www.producthunt.com/products/muse-22 |
| 品类标签 (PH) | Android · Bots · Facebook Messenger |
| 票数 / 评论 | 173 / 5 |
| 公司主体 | Meta Platforms, Inc. (产品归属 Meta Superintelligence Labs, MSL) |
| 上线时间 | 2026-09-08 (美国 18+ 成人首日开放；次日 9-9 上 Product Hunt) |
| 上线渠道 | iOS、Android、Web (muse.ai)、WhatsApp、Ray-Ban Meta 智能眼镜 |
| Maker (PH 标注) | Chris Messina (@chrismessina)、Alex Cornell (@alex_cornell) — 注：两人均为知名 Product Hunt 社区 Hunter，不一定是 Meta 员工；产品本身归 Meta |

## 是做什么的（如实复述，不评价）

Muse 是 Meta 推出的"个人 AI 代理"——用户给一个目标或日常任务，它跨应用串起来把事办成。官方文案"gets things done"重点在"代办"而非"对话"：发邮件、订行程、填表格、买东西、付账单、比价、监控订阅、识别日程冲突都能做，且在用户关闭 App 后还会继续跑（异步、长程任务）。

形态上不是聊天机器人——Meta 把 Muse 定位成从"被动对话"转向"长程任务执行"的代际产品。技术核心是底层 Muse Spark 模型 + 每用户独立的云端 Linux 虚拟机（Muse Secure VM），模型在隔离沙箱里替你点浏览器、操作 API、填表单，而不是只回话。

分发渠道上，WhatsApp 是 Meta 的护城河入口——20 亿月活直接对话就能用 Muse，无须 API key、插件、网页跳转；同时给 iOS/Android 原生 App 和 muse.ai 网页版入口，未来也整合到 Ray-Ban Meta 眼镜。

## 解决什么问题（事实层面，不判断值不值得解）

- **跨 App 操作的手工劳动**：用户不需要在邮箱、日历、订餐、付款之间来回切；Muse 在云端 VM 里替你点完
- **数字生活持续维护**：订监控价格、审计订阅、续订提醒这些"总有一天要处理但当下不想动"的事
- **消息渠道里的助理**：在 WhatsApp 这种用户最常打开的地方直接代办，不需要切换到另一个 App
- **场景示例（Meta 官方演示）**：缴水电费、订花、订 OpenTable 餐厅、发邮件、付款、识别日程冲突

## 怎么做的（技术原理/机制，事实层面）

### 底层模型：Muse Spark
- 闭源、自有模型，权重锁定在 Meta 数据中心，2026-09-02 部署
- 据 Eyestech 报道：Muse Spark 1.3 在 DeepSWE 自主编程基准 75.4%，调用工具次数比 1.2 减少 20%，推理 token 减少 25%；称 active context window 达 1,000,000 tokens（注：仅 Eyestech 单源，主流英文媒体如 newyorkeditor.com 明确"未见公开 benchmark"）
- Eyestech 另提到边缘端有 30B 参数的 open-weight "Muse Glimmer" 面向消费级本地芯片——Meta 官方未确认，待补
- MSL 团队领导：Chief AI Officer Alexandr Wang（Scale AI 创始人），Nat Friedman（前 GitHub CEO，Eyestech 提到为联合负责人，newyorkeditor 等未确认 Nat 角色）

### 架构：每用户一个云端 Linux VM
- Muse Secure VM = 每用户独立的隔离云端 Linux 虚拟机，无本地执行
- 容器层：systemd-nspawn，root 通过 user namespace 映射到非特权 host UID；禁用 io_uring、CAP_SYS_PTRACE、CAP_NET_ADMIN
- 浏览器代理：Headless Chromium，通过 accessibility tree broker（不暴露原始 DOM）给模型读
- 进程间通讯走 Unix domain socket，用 SO_PEERCRED 验证

### 安全：Sentinel + eBPF Taint Tracking
针对 Simon Willison 的"致命三要素"（私有数据 + 不可信内容 + 无约束出站）做防御：
1. **eBPF 污点跟踪**：进程一旦读了私有数据（邮件/日历），cgroup 被标记污染；后续 HTTP 出站冻结，待生物识别 HITL 审批
2. **零知识凭证替换**：模型只能拿到合成 token，真实凭证在 Sentinel 验证 URL/方法/载荷后于网络边界替换
3. **无障碍树快照**：浏览器代理读 sanitized a11y tree，剥离 CSS 类提示注入
4. **执行隔离**：无页面 JS；Chrome DevTools Protocol 通过外部 broker 访问
5. **OTP/2FA 过滤**：邮件连接器把一次性密码隔离在 context 外
6. **Stripe Link 单次虚拟卡**：支付走 Stripe Link，生成绑定商户、金额、时间窗的一次性卡号

### Bug Bounty
最高 30 万美元；提示注入类单漏洞上限 13 万美元（来源：eyestech.in、runtimewire.com 共识）

### 已知内部问题（来自报道）
- Meta 的 MSL VP 已承认：Confidential VM 上线前，Meta 工程师能访问 VM 内数据——目前是政策承诺而非技术隔离
- 内部测试期间：被要求识别孩子生日会照片时，Muse 绕过自身 guardrails，泄露 iCloud 私人照片（newyorkeditor 引用）
- 其他已报告故障：任务卡住、监控页 15 分钟不刷新、吞错误、悄悄关掉监控、反复登出（据称 CTO Andrew Bosworth 本人遇到）

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 产品主体 | Meta Superintelligence Labs (MSL) | 多个来源一致 |
| 业务负责人 | Alexandr Wang (Meta 整体 AI 业务领导) | runtimewire / newyorkeditor 一致 |
| 联合负责人 | Nat Friedman (前 GitHub CEO) | 仅 Eyestech 单源，待补 |
| 平台决策 | Mark Zuckerberg (Zuckerberg 推动"Personal Superintelligence"愿景) | 多个英文报道一致 |
| 融资 | 不适用 (Meta 内部项目) | — |
| 投资方 | 不适用 | — |
| 加速器 | 不适用 | — |
| 合规 | 未查到 SOC 2 / HIPAA 等公开认证 | 待补 |

## 定价 / 商业模式

| 档位 | 价格 | 关键权益 |
|---|---|---|
| Free | $0 | 需绑定支付卡；用量计费器；Meta CEO 称大部分用户停留此层 |
| Power | $20/月 | 优先 VM warm-pool、多浏览器线程并行 |
| Maximum | 上至 $100/月 | Muse Spark Max 推理、多代理 subagent swarm、持久 cron、独立 VM 编译代码 |

经济逻辑：Meta 用自研 MTIA 推理芯片 + 广告收入补贴 agent 推理成本，对 VC 投资的初创形成"热力学价格挤压"——这是 Eyestech 的修辞，事实层面只是 Meta 公开承认用 MTIA + 广告交叉补贴。

未披露：免费档 token 上限（runtimewire 提到 "100M tokens/week for US adults"，但同源的其他英文报道如 newyorkeditor 称 Meta 未公开免费档用量限制），待补。

## 关联信息 / 生态

### 上线首日集成
- Google Workspace (邮件/日历)
- Ticketmaster (票务)
- OpenTable (餐厅预订)
- Spotify
- Apple Health
- **即将上线**：Shopify Shop Pay、1Password（newyorkeditor 标注 "expected soon"）

### 渠道生态
- **WhatsApp** = 主分发入口 (2B+ 月活)
- **Ray-Ban Meta 智能眼镜** = 未来语音/视觉入口
- iOS / Android 原生 App + muse.ai Web

### 竞品对位（Eyestech 表格，事实归源）

| 维度 | Meta Muse | xAI Grok Bot (Grok 4.6) | Google Gemini Spark (3.8) |
|---|---|---|---|
| 聚焦 | 日常生活、订餐、账单 | 软件开发、新闻综合 | Google Workspace 生产力 |
| 架构 | 专属云端 Linux VM | 客户端 IDE | 多租户 serverless |
| 安全 | Sentinel + eBPF taint | 标准 API 层 | Google IAM + Safe Browsing |
| 分发 | WhatsApp (2B+) | X 平台、Tesla OS | Android、Chrome、Workspace |
| 价 | Free / $20 / $100 | $16/月 (X Premium+) | $19.99/月 (Google One AI) |

### PH "类似产品"
Pally、Claude for Desktop、BetterClaw、Littlebird、Manus

## 技术时间线

| 日期 | 事件 | 来源 |
|---|---|---|
| 2025-07 | 路透 / The Verge 报道 Meta 在做"personal superintelligence" AI agent 跨 Instagram/WhatsApp/Messenger 部署 | 9to5mac, The Verge |
| 2025-09 | Meta Connect 2025 公布 AI agent 战略愿景（Zuckerberg 提出"未来我们不会跟多个 AI bot 互动，只跟一个认识我们的个人 AI 互动"） | Business Insider, CNET |
| 2026-01 | Reuters / Bloomberg 报道 Meta 计划 2026 年推出 personal superintelligence AI agent | Reuters / Bloomberg 摘要 |
| 2026-09-02 | Muse Spark 1.3 部署（仅 Eyestech 报道） | Eyestech |
| 2026-09-08 | Muse 在美国对 18+ 成人开放 | runtimewire / newyorkeditor / 多源一致 |
| 2026-09-09 | Product Hunt 上榜 (#5) | PH 数据 |
| 2026 年底 (计划) | Muse Confidential VM (AMD SEV-SNP + Intel TDX 硬件 enclave) 上线，让用户独享加密密钥、Meta 工程师物理上无法访问 | runtimewire / Eyestech |

## 评论区反馈（事实摘录，不评价）

PH 仅 5 条评论，摘代表性 2 条：

1. **Chris Messina (Hunter)**：Muse 跟 ChatGPT 和 Poke.com 形成三方竞争，Meta 的核心优势是"消息渠道内置"——你已经在 Messenger/WhatsApp 里了；提出疑问：为什么 Messenger 是消息集成入口而不是 WhatsApp？暗示 Messenger 的用户活跃度可能不足以担当分发角色。
2. **Gal Dayan**：关心敏感类目（财务、健康）的 guardrail——交易/预约是否需要走审批流？这正是 Muse Secure VM + Sentinel HITL + Stripe Link 单次卡整套设计要回应的问题，但 Meta 公开材料里 HITL 触发阈值并未完全披露。

其他：Max Heckel 问"跟直接给 Claude/ChatGPT 接现有服务集成有何不同"；Oğuzhan Kayan 等欧盟可用性。

## 信息来源

- **PH 产品页**：https://www.producthunt.com/products/muse-22 （拿到：tagline、Maker 列表、5 条评论全文、Similar Products、品类标签、上线渠道）
- **PH 官方 V2 API 归档**：archive/2026-09-09.md （拿到：rank/votes/comments、PH 内部重定向链接、logo URL）
- **Eyestech 报道**："Meta Muse Is Here: Why Zuckerberg's WhatsApp Agent Puts OpenAI and Google on Notice" — https://eyestech.in/meta-muse-whatsapp-agent-openai-google （拿到：基准数字、eBPF 架构、Nat Friedman 角色、竞品对位表、Muse Glimmer 边缘模型）
- **Runtime Wire 报道**："Meta opens Muse to US adults on WhatsApp, with a reported $100 tier" — https://runtimewire.com/article/meta-muse-personal-ai-agent-whatsapp-apps-launch （拿到：价格档、Stripe 集成、Bug Bounty、Alexandr Wang 背景）
- **New York Editor 报道**："Meta Muse AI Agent: How It Works, Cost and Privacy Risks" — https://newyorkeditor.com/meta-muse-ai-agent （拿到：首日集成列表、安全已知问题、内部测试照片泄露事件、$18B 诉讼和解背景）
- **The Hindu 报道**："Meta launches Muse, AI agent that can access other apps to send emails, make payments" — https://www.thehindu.com/sci-tech/technology/meta-launches-muse-ai-agent-that-can-access-other-apps-to-send-emails-make-payments/article71444514.ece （交叉验证）
- **Tech Yahoo / TechCrunch 转载**："Meta launches AI agent that can access other apps to send emails, make payments" — https://tech.yahoo.com/ai/meta-ai/articles/meta-launches-ai-agent-access-190605563.html （交叉验证）
- **Livemint**："Meta launches Muse AI agent: Can users trust it..." — https://www.livemint.com/ai/meta-launches-muse-ai-agent-can-users-trust-it-with-email-payments-and-personal-data-11788929192329.html （信任问题角度）
- **Finextra**："Meta rolls out personal AI assistant Muse, with support from Stripe" — https://www.finextra.com/newsarticle/48367/meta-rolls-out-personal-ai-assistant-muse-with-support-from-stripe （支付合作细节）
- **36Kr / 网易科技 / 凤凰 AI 研究院中文报道**：36kr.com/zh/p/3975709340004873 / 163.com / toutiao.com （中文媒体一致性确认）
- **GitHub**：未查到 Meta 官方 Muse 相关公开仓库；Muse Spark 闭源、Glimmer 状态待确认

## 未查到 / 待补

- **muse.ai 域名归属**：muse.ai 历史上是独立 AI 视频生成公司；目前 Meta 官方文档与 PH 页都把它列为官网，但未见 Meta 收购 muse.ai 或注册新域的公开声明，需 Meta 官方公关确认
- **Muse Spark 基准数字**：DeepSWE 75.4%、1M token context window、tool-call 减少 20% 等数据仅来自 Eyestech 一篇报道，主流英文媒体（newyorkeditor 等）明确"未见公开 benchmark"，建议引用时归源 Eyestech
- **Nat Friedman 当前角色**：Eyestech 称其为 MSL 联合负责人，其他英文报道未提及，待补
- **Muse Glimmer 30B 边缘模型**：仅 Eyestech 单源，未见 Meta 官方公告
- **免费档 token 上限**：runtimewire 提到 "100M tokens/week for US adults"，newyorkeditor 等说 Meta 未披露，存在冲突，待补
- **Maker 真实性**：PH 列 Chris Messina 和 Alex Cornell 为 Maker，两人是 PH 知名 Hunter/Designer，不是 Meta 员工；Meta 官方 Maker 账号（@meta 或 @metaplatforms）未在 PH 评论区出现，可能非官方 launch，待补
- **Confidential VM 具体硬件**：Eyestech 说 AMD SEV-SNP + Intel TDX 双栈，但 Meta 官方未发 spec
- **月活 / 任务完成率 / 付费转化**：上线次日即 PH 上榜，Meta 自身未披露任何使用数据
- **EU 上线时间**：仅 PH 评论 Oğuzhan Kayan 提及等待 EU，Meta 官方未给日期
