---
# 结构化元数据（用于索引和聚合）
product: "Clipto MCP"           # 产品名（英文原名）
slug: "clipto-mcp"             # PH slug（文件名用）
date: "2026-08-19"             # 上榜日期 YYYY-MM-DD
rank: 2                        # 榜单排名
votes: 298                     # 票数
comments: 73                   # 评论数

# 分类标签
category: "开发者工具"           # 主品类（AI agent / 开发者工具 / SaaS / 消费级应用）
subcategory: "MCP / 媒体检索"    # 子品类
tags: ["MCP", "本地优先", "视频检索", "隐私", "Claude", "Cursor"]   # 特征标签

# 技术信息
tech_stack: ["MCP", "AI 转录", "自动打标(场景/主体/镜头)"]   # 技术栈
platform: ["Mac (Apple Silicon M1+ / 16GB)", "Windows (12GB)", "Premiere Pro 插件", "DaVinci Resolve 插件"]
open_source: false             # 闭源，无公开 GitHub 仓库
license: ""                    # 闭源

# 商业信息
business_model: "订阅制 + 7天试用"
pricing_start: "$9.99/月（首月，次月 $24.99）/ 年付 $12.49/月"
funding_stage: "未披露"
funding_amount: ""

# 关联信息
related_products: ["Opus Clip", "Vizard", "MacWhisper", "本地 RAG 工具"]  # 相关产品（竞品或互补品）
maker_previous: []            # 创始人过往产品（未查到）

# 速览信号（给 caption.md / INDEX.md 等下游用）
key_signals:
  - "本地 AI memory 平台，统一视频/会议/音频/文档为单一可搜 Memory，按画面内容而非文件名搜片段"
  - "MCP server 给 Claude/ChatGPT/Cursor：搜本地媒体、按脚本配 B-roll、组装视频序列、导出带时间码的素材日志"
  - "本地处理不上云，只索引已授权文件夹；Pro $9.99首月→$24.99/月，99+语言转录，支持6小时长视频"
  - "附 Premiere Pro / DaVinci Resolve 插件；Mac 需 M1+ 16GB，公司主体 Clipto, Inc."

# 元信息
archived_at: "2026-08-20"      # 归档时间戳
sources_count: 1              # 信息源数量（仅 archive/PH API 直出字段；一手官网与 PH 页因网络受限未取到）
---

# Clipto MCP · 扩展阅读上下文

> PT 2026-08-19 Product Hunt 榜单第 2 · 👍 298 · 💬 73  
> 归档日期 2026-08-20 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Clipto MCP |
| 英文 tagline | Let agents source clips from terabytes of your local video |
| 中文 tagline | 让 agent 从 TB 级本地视频里检索片段 |
| 官网 | 见 PH 页重定向（producthunt.com/r/OTKPG4D4Y4NG66） |
| PH 页 | https://www.producthunt.com/products/clipto-ai |
| 品类标签 | Productivity · Search · Video |
| 票数 / 评论 | 298 / 73 |
| 公司主体 | 未查到 |
| 企业版/关联站点 | 未查到 |

## 是做什么的（如实复述，不评价）

Clipto 是本地 AI memory 平台，把用户电脑上的视频、会议、音频、文档、图片、想法统一成单一可搜索的 "Memory"——全部在本地处理，不上传云端（官网定位语："Local Memory — One Memory for everything you know, right on your computer"）。核心能力是按画面内容（场景、主体、镜头类型）自动打标检索，而非依赖文件名；可直接跳到精确帧、就绪剪辑。PH tagline 强调 terabytes 级本地视频。产品定位在 Productivity · Search · Video 三个品类交叉点。

MCP server 形态让它成为 Claude/ChatGPT/Cursor 的本地媒体记忆引擎，同时提供 Premiere Pro 与 DaVinci Resolve 插件。

## 解决什么问题（事实层面，不判断值不值得解）

- AI agent（如 Claude、Cursor）无法直接感知用户本地磁盘上的视频内容；要把视频里的信息喂给 agent，通常需手动上传云端或人工截取片段
- 本地视频库体积大（tagline 强调 terabytes 级），人工定位某一片段成本高
- 隐私敏感场景下不希望把视频上传第三方云端做检索（待核：是否明确主打隐私，tagline 未直接声明，但"local video"暗示本地处理）

## 怎么做的（技术原理/机制，事实层面）

- **部署形态**：MCP server，以 Clipto 桌面 app 作为本地媒体记忆引擎；在 app 左侧 MCP 标签页连接任意 MCP 兼容 agent，ChatGPT 支持一键安装
- **MCP 暴露的能力**：① 按人物/场景/物体/动作/对白搜本地媒体 ② 按脚本配 B-roll（带时间戳） ③ 把文字/脚本转成视频序列 ④ 剪播客（标出假开头、停顿、重复） ⑤ 生成素材日志（源路径/时长/入出点时间码/描述/口播话题或引文） ⑥ 每条结果带时间戳、证据和"在 Clipto 中打开"回链
- **记忆网络**：跨 People / Scenes / Objects / Actions / Dialogue 分类索引
- **本地优先**：源文件默认不上传；AI 工具只能搜已显式授权的文件夹；可随时在"已连接 AI 工具"页撤销访问
- **数据规模**：tagline 明确面向 terabytes 级本地视频；支持长达 6 小时的单条视频分析
- **转录与语言**：自动语音转录 + 自动人物打标，支持 99+ 语言
- **硬件门槛**：Mac 需 Apple Silicon M1+ / 16GB RAM；Windows 需 12GB RAM
- **具体嵌入模型/索引引擎品牌**：官网未披露（"advanced models"，未指明）

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | 未查到 | PH 页因网络受限未取到 |
| 融资 | 未披露 | — |
| 投资方 | 未披露 | — |
| 加速器 | 未查到 | — |
| 合规认证 | 未查到 | — |

## 定价 / 商业模式

- 7 天免费试用（含全部高级功能，随时取消）
- **Pro 月付**：首月 $9.99（原价 $24.99），次月起 $24.99/月
- **Pro 年付**：$12.49/月（ billed yearly，官网标 50% off）
- 两档付费功能完全一致：无限视频/音频搜索、自动语音转录、自动人物打标、99+ 语言、最长 6 小时视频分析、高级模型
- 无团队/企业定价档；另有 affiliate 与学生/校园大使计划

## 关联信息 / 生态

- MCP 生态：Model Context Protocol 是 Anthropic 主导的 agent 工具协议，Clipto 作为 MCP server 可被任意 MCP 客户端调用
- 相关/对标产品：Opus Clip、Vizard（云端 AI 视频剪辑 SaaS，但定位创作者而非 agent 本地检索）、MacWhisper（本地音频转录，互补而非检索）
- 与 8-19 当日 #3 Origin by Cursor 同属"为 coding agent 时代造基础设施"的品类信号

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-08-19 | 登录 Product Hunt，当日第 2 名 |

## 评论区反馈（事实摘录，不评价）

- 未取到 PH 页评论原文（producthunt.com 域名在本环境被网络策略拦截）
- 73 条评论为当日较高互动量，仅次于 #1 Astute（106 条）

## 信息来源

- archive/2026-08-19.md（PH 官方 V2 API 直出：tagline、票数、评论数、品类、logo、PH 页与官网重定向链接）— 已取
- 官网 clipto.com（301 重定向自 clipto.ai）— 已取：产品定位、MCP 能力、定价、硬件门槛、转录/打标机制
- 官网 clipto.com/mcp — 已取：MCP server 暴露的 6 类能力、记忆网络分类、本地优先隐私控制
- 官网 clipto.com/pricing — 已取：Pro 月付/年付定价、试用、功能清单
- PH 产品页 producthunt.com/products/clipto-ai（创始人评论、技术细节）— 未取到，域名被网络策略拦截
- 公开报道（融资、创始人背景）— WebSearch 后端不可用，未取
- GitHub — 官网无开源信号，未查；公司主体 Clipto, Inc.（官网页脚）

## 未查到 / 待补

- 创始人/团队、融资背景（官网未列，PH 页未取到）
- 具体嵌入模型/转录引擎品牌（官网仅称"advanced models"）
- PH 页创始人评论原文（73 条，常含技术细节与用户反馈，本次缺失，建议后续用继承登录态的浏览器补抓）
