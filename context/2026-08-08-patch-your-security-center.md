---
# 结构化元数据（用于索引和聚合）
product: "Patch — Your Security Center"
slug: "patch-your-security-center"
date: "2026-08-08"
rank: 6
votes: 0
comments: 1

# 分类标签
category: "SaaS"
subcategory: "个人安全（Personal Security）"
tags: ["Apple", "隐私", "本地优先", "Claude", "订阅制", "Mac", "iPhone"]

# 技术信息
tech_stack: ["Swift", "Claude API", "Anthropic", "Have I Been Pwned", "Vercel", "Upstash"]
platform: ["Mac", "iPhone", "iOS"]
open_source: false
license: ""

# 商业信息
business_model: "订阅制（免费层 + 分级订阅）"
pricing_start: "$1.99/月"
funding_stage: "未披露"
funding_amount: ""

# 关联信息
related_products: ["1Password", "Bitdefender", "Debitize", "PrivacyHawk"]
maker_previous: []

# 元信息
archived_at: "2026-08-08"
sources_count: 4
---

# Patch — Your Security Center · 扩展阅读上下文

> PT 2026-08-08 Product Hunt 榜单第 6 名 · 👍 票数未知 · 💬 1（仅 maker launch 评论）
> 归档日期 2026-08-08 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Patch — Your Security Center（官网 patch-security.com） |
| 英文 tagline | Lock down your digital life and stay on top of it. |
| 中文 tagline | 锁定你的数字生活，并始终掌握主动权 |
| 官网 | https://patch-security.com/ |
| PH 页 | https://www.producthunt.com/products/patch-your-security-center |
| PH launch post | https://www.producthunt.com/posts/patch-your-security-center |
| 品类标签 | Privacy · Apple · Security |
| 票数 / 评论 | 票数未知；评论 1（maker 仅一条，无第三方用户评论） |
| 公司主体 | 官网无公司实体名（页脚 © 2026 Patch），联系邮箱 hello@patch-security.com |
| 企业版/关联站点 | patch-security.com/privacy/ · /trust/deeper-dive/ · /faq/ |
| Maker | Cory（PH @getpatch） |
| Built with（PH 页） | Have I Been Pwned · Vercel · Claude Code |

## 是做什么的（如实复述，不评价）

Mac + iPhone 的个人安全聚合应用（iPhone 版在发布时处于"App Store 审核中"）。把个人安全任务集中到一处：邮箱/密码泄露检测、重复密码发现、信用冻结引导、退出数据经纪商名单、诈骗识别（文本/邮件/图片），并内置一个由 Claude 驱动的"安全顾问"答疑和逐步修复引导。无需账户，"服务器上不存任何东西"——官方定位为"手电筒，不是保险柜"（展示暴露面，不存凭据）。

## 解决什么问题（事实层面，不判断值不值得解）

- 反复收到 breach 提醒却不知从何下手 → 聚合到一处、按优先级排序并给修复路径
- 已泄露/重复使用的密码 → 本地比对 + 分步修复引导
- 骗子邮件/短信/图片难辨真伪 → 粘贴即查
- 信用冻结（四大信用局）、退出数据经纪商 → 分步引导
- 官方 FAQ 自述目标人群："收到过 breach 通知、诈骗短信、'这是真的吗'时刻的普通用户"；设计取向"温暖安抚而非恐吓"

## 怎么做的（技术原理/机制，事实层面）

- **隐私模型**：无账户、无用户数据库、无分析/phone-home、不报告本地扫描结果；"最安全的数据库是不存在的数据库"
- **密码/邮箱泄露检查**：仅向 Have I Been Pwned 发送邮箱"单向 SHA-1 哈希的前 5 个字符"，本地匹配，不经 Patch 服务器；密码永不离机（官方 FAQ）
- **唯一离机场景**（均需用户主动操作）：①诈骗检查内容 → 后端 → Anthropic API，不落盘；②breach 检查邮箱 → HIBP，地址不存储；③顾问问题 + 当前标签页名 → Anthropic，30 天内删除、不用于训练
- **后端**：4 个 serverless 函数、无数据库、无会话状态、无文件系统写入；托管 Vercel，限流用 Upstash（IP 计数 24h 过期）；邮件处理代码文件顶部明确写"地址永不写入/存储/记录/持久化"；错误日志只带状态码不带内容
- **Mac↔iPhone 同步**：直接走用户自有 Wi-Fi 或 iCloud，不经过 Patch 服务器；订阅通过 Apple ID/iCloud 购买记录解锁，无客户数据库，仅限 Apple 生态内
- **平台**：Mac 仅 Apple Silicon（M1+），Developer ID 签名 + Apple 公证；不入 Mac App Store（官方称沙盒会阻止读取浏览器保存密码和系统 Keychain）
- **对抗测试**（官网 trust 页自述）：19 种提示注入攻击测试（指令覆盖、伪造权威、伪造工具调用、输出模仿、同形字、零宽字符、RTL 覆盖、Base64 走私指令、越狱框架、图片内嵌指令）全部保持判为诈骗；发现 1 个失败场景——模糊发票中嵌入"厂商已验证"声明的行把结论从警惕翻成安全，已用"确定性检查：只能把结论升为警惕、绝不降低"修复；已知短板是只读文本不读图片
- **已披露的未解决问题**：无独立安全审计；限流不绑定身份（可轮换标识耗尽月度预算，失效模式是顾问当月不可用而非账单失控）；图片内嵌注入未完全覆盖；单人运营无安全团队

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Cory（PH @getpatch），自述"rookie vibe-coder"，非程序员用 AI 工具做了 4 个月，单人开发 | trust/deeper-dive + PH 评论 |
| 融资 | 未查到 | — |
| 投资方 | 未查到 | — |
| 加速器 | 未查到 | — |
| 合规认证 | 无独立安全审计（官方明确：未做过独立安全审计、无安全资质审过代码） | trust/deeper-dive |

## 定价 / 商业模式

- **免费层（$0 永久）**：每月 1 次邮箱 + 1 次密码泄露检查、2 次诈骗检查，无需信用卡
- **Patch $1.99/月 或 $19.99/年**：无限泄露/密码检查、数据经纪商移除、信用冻结引导、2FA 设置、诈骗检查、顾问 30 问/月、Mac+iPhone 同步
- **Premium $3.99/月 或 $39.99/年**：全部 Patch + 顾问 150 问/月
- **Family $6.99/月 或 $69.99/年**：完整功能 5 人份，各 150 问/月
- **Launch 促销**：到 2027-08-08 前全功能免费一年（完整 Mac 版、无需账户/付费），促销期后按上述付费解锁；免费层促销后仍保持免费
- 模式：订阅制（免费层 + 分级订阅）

## 关联信息 / 生态

- 第三方依赖：Have I Been Pwned（breach 数据）、Anthropic（诈骗检查/顾问）、Vercel（托管）、Upstash（限流）
- 定位声明："不是保险库、VPN 或杀毒软件"；核心差异点 = 不存凭据的"手电筒"
- 三阶段方法论：Find（按优先级列出暴露面）→ Fix（分步修复引导）→ Stay safe（跨设备持续监测）

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-08-08 | Product Hunt 上线；iPhone 版处于 App Store 审核中 |
| 2027-08-08 | Launch 促销"全功能免费一年"截止 |

## 评论区反馈（事实摘录，不评价）

- Maker Cory（10h 前发布）：自述因反复忽略 breach 通知后想做点实事；"安全应用就该接受审视，问我尖锐的问题"；承认"Patch 很紧，但没什么是不可攻破的"；附隐私政策与 deeper-dive 链接；确认"现在完整版免费一年、无需信用卡"
- 无其他用户评论

## 信息来源

- PH 产品页 + PH launch post：tagline、品类、Built with、maker 评论、iPhone 审核中状态
- 官网 https://patch-security.com/ ：功能清单、定价、隐私模型、定位
- 官网 /trust/deeper-dive/ ：技术架构、HIBP/Anthropic/Vercel/Upstash、注入测试、单人生成背景、未解决问题
- 官网 /faq/ ：免费层细节、SHA-1 前缀、Wi-Fi/iCloud 同步、Apple 公证、目标人群

## 未查到 / 待补

- 票数（archive 与 PH 页面抓取均未显示）
- 公司注册实体名
- 创始人全名
- 融资
- iPhone 版实际上架时间
- 独立安全审计（官方确认无）
