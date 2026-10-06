---
# 结构化元数据（用于索引和聚合）
product: "Claude Watermark Remover"
slug: "claude-watermark-remover"
date: "2026-08-19"
rank: 4
votes: 163
comments: 7

# 分类标签
category: "开发者工具"
subcategory: "AI 文本溯源/清洗"
tags: ["AI 检测", "零宽字符", "MIT 开源", "浏览器端", "隐私", "文本清洗", "Claude 水印"]

# 技术信息
tech_stack: ["JavaScript", "浏览器原生"]
platform: ["Web"]
open_source: true
license: "MIT"

# 商业信息
business_model: "开源免费"
pricing_start: "免费"
funding_stage: "未融资（个人项目）"
funding_amount: ""

# 关联信息
related_products: ["GPTZero", "Originality.ai", "guillaumemeyer/watermarks-remover"]
maker_previous: []

# 速览信号（给 caption.md / INDEX.md 等下游用，避免整篇重读正文才能省 token）
key_signals:
  - "不碰 Anthropic 统计水印——明确声明'Anthropic 外无人能检测'，只清聊天界面留下的字节级痕迹"
  - "检测对象：HTML 类名、零宽字符、异形空格、排版字符——按字节事实而非概率打分，逐条给计数和位置"
  - "引擎 MIT 开源，纯浏览器端运行不上传，免费无限次"
  - "用十部前计算机时代小说证伪'破折号是 AI 标志'：Moby Dick 每千字 26 个，Austen/Stoker 为 0"

# 元信息
archived_at: "2026-08-20"
sources_count: 3
---

# Claude Watermark Remover · 扩展阅读上下文

> PT 2026-08-19 Product Hunt 榜单第 4 · 👍 163 · 💬 7
> 归档日期 2026-08-20 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Claude Watermark Remover |
| 英文 tagline | Find and remove every trace AI leaves in your text |
| 中文 tagline | 找出并清除 AI 在你文本里留下的每一处痕迹 |
| 官网 | PH redirect 链接（403 无法直连，见信息来源） |
| PH 页 | https://www.producthunt.com/products/claude-watermark |
| 品类标签 | Writing · Privacy · Artificial Intelligence |
| 票数 / 评论 | 163 / 7 |
| 公司主体 | 个人项目（maker: Ofir Smolinsky） |
| 企业版/关联站点 | 未查到 |

## 是做什么的（如实复述，不评价）

一个浏览器端工具。粘贴任意文本，它会逐条列出"聊天界面在复制时带进去的痕迹"——隐藏的 HTML class 名、零宽字符、异形空格、排版特殊字符——每条都给出现次数和位置坐标。一键清除。

核心定位声明（创始人原话）："这些是关于字节的事实，不是概率分数。" 也就是说，它不做 AI 生成概率判断，只如实报告文本里客观存在的、可逐字节指认的隐藏字符。

## 解决什么问题（事实层面）

- **复制粘贴带毒**：从 Claude/ChatGPT 等 AI 聊天界面复制文本，会夹带聊天框的 HTML 标记、零宽字符、非标准空格，发布/投稿时留下"AI 痕迹"被工具误判
- **概率型检测器的误判风险**：市面主流 AI 检测器（GPTZero 等）基于 perplexity/burstiness 打分，对非母语写作者误判率偏高——本工具走"字节事实"路线避开这一类争议
- **2026-08 Claude 水印新闻后**：大量工具声称能"去除 Claude 水印"，但创始人指出统计水印 Anthropic 外无人能检测——本工具只做"真实存在的那部分"

## 怎么做的（技术原理/机制，事实层面）

**检测/清除对象（字节级，确定性）**：
- 隐藏的 HTML class 名（聊天界面 DOM 残留）
- 零宽字符（U+200B 零宽空格、U+200C 零宽非连接符、U+200D 零宽连接符、U+FEFF BOM 等）
- 异形空格（U+00A0 不间断空格、U+2009 细空格、U+2003 全角空格等）
- 排版特殊字符（特殊引号、连字符变体等）

**机制特点**：
- 按字节扫描，逐字符匹配 Unicode 类别，命中即报计数+位置——非概率模型，不会"猜"
- 一键清除：把上述字符替换/剥离为标准等价物
- 纯前端运行，不上传文本

**明确不做的事（创始人声明，信息增量最大）**：
1. 不检测 Anthropic 的统计水印——"Anthropic 外无人能检测，因为验证需要一把未公开的密钥。任何声称能做到的工具都是在猜"
2. 不把破折号当 AI 标志——创始人跑了十部前计算机时代小说做证伪：Melville 的《白鲸》每千字 26 个破折号，而 Austen 和 Stoker 一个都没有。"一个在人类作者间从 0 摆动到 26 的信号，没法指控任何人"

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Ofir Smolinsky（个人开发者） | PH API makers 字段 |
| 融资 | 未披露（个人项目形态） | 无融资信号 |
| 投资方 | 无 | — |
| 加速器 | 未查到 | — |
| 合规认证 | 无（定位为隐私工具：浏览器端、不上传） | PH description |

## 定价 / 商业模式

免费、无限次、无需账号、浏览器端运行不上传。开源（MIT）。无付费层、无企业版。典型的工具型个人项目，无直接变现路径（至少当前如此）。

## 关联信息 / 生态

- **同类竞品**：GPTZero、Originality.ai（但二者走概率打分路线，与本工具"字节事实"路线正交）
- **相关开源项目**：guillaumemeyer/watermarks-remover（GitHub 15k+ stars，MIT，同为多厂商 AI 溯源痕迹剥离——但那是另一个独立项目，非本产品的引擎；本产品具体仓库链接未在搜索中查到）
- **背景事件**：2026-08 Anthropic Claude 水印相关新闻，催生一批"去水印"工具，本产品以"只做真实存在的那部分"做差异化

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-08-19 | Product Hunt 上线，#4，163 票 |

## 评论区反馈（事实摘录，不评价）

- **创始人（Ofir Smolinsky）发布评论**：解释动机——Claude 水印新闻后网上充斥"去除一个没人能检测的水印"的工具，他做"真实存在的那部分"。两点主动声明：①不检测 Anthropic 统计水印（密钥未公开，声称能做到的都是猜）；②破折号不是 AI 标志（十部前计算机时代小说证伪：Moby Dick 26/千字，Austen/Stoker 为 0）。检测引擎 MIT 开源可自查。免费无限、浏览器端不上传。
- **用户 A**：肯定"领先声明自己做不到什么"的诚实姿态，复述了破折号实验数据。
- **用户 B**：认可"无 Anthropic 密钥无法检测水印"的前提，但在"移除"上不完全同意——指出有研究表明统计水印多在改写/来回翻译后不存活，"不需要检测也能移除"。这是对本产品"只清字节痕迹、不碰统计水印"路线的学术性质疑。
- **用户 C**：对云水印无异议，认可细分定位。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/claude-watermark（拿到 description 全文 + 创始人发布评论 + 4 条用户评论 + maker Ofir Smolinsky）
- PH API（GraphQL，本项目 token）：拿到 description、votes、comments、makers 字段
- 公开报道：2026-08 Claude 水印新闻（背景，非本产品专属报道，未查到针对本产品的独立报道）
- GitHub：创始人称引擎 MIT 开源，但未在搜索中定位到具体仓库链接——未查到，待补

## 未查到 / 待补

- 具体开源仓库 URL（创始人称 MIT 开源，但搜索未命中本产品专属 repo；guillaumemeyer/watermarks-remover 是同名方向的另一个独立项目，非本引擎）
- 官网真实域名（PH redirect 链接对脚本 403，无法解析到最终落地页）
- 创始人过往产品 / 背景（maker_previous 空）
- 独立融资或媒体报道（无）
