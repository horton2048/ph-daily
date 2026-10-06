---
product: "ElevenLabs MCP in Claude"
slug: "elevenlabs-mcp"
date: "2026-08-18"
rank: 5
votes: 145
comments: 7

category: "AI agent / 开发者工具"
subcategory: "MCP 集成 / 语音 Agent 管理"
tags: ["MCP", "Claude", "ElevenLabs", "Voice Agent", "Audio", "官方集成", "MIT"]

tech_stack: ["Python", "MCP", "ElevenLabs API", "uv"]
platform: ["Claude（claude.ai）", "Claude Desktop"]
open_source: true
license: "MIT"

business_model: "Freemium（依赖 ElevenLabs 账号额度）"
pricing_start: "免费（ElevenLabs 免费层 10k credits/月）"
funding_stage: "Series C"
funding_amount: "$180M（Series C，2025 年初，估值 $3.3B）"

related_products: ["ElevenAgents", "ElevenCreative", "ElevenAPI", "Claude Desktop", "Cursor", "Windsurf", "OpenAI Agents"]
maker_previous: ["ElevenLabs（母公司，2022 年创立）"]

key_signals: ["ElevenLabs 官方 MCP server（MIT，Python，1.5k stars），PH 产品是其接入 Claude Directory 的语音 Agent 管理入口", "在 Claude 对话内创建/更新/复制/删除 ElevenLabs 语音 agent，预估 LLM 用量，查知识库大小", "ElevenLabs 2022 年创立，Series C 估值 $3.3B，a16z 领投", "底层 MCP server 通用（也支持 Cursor/Windsurf/OpenAI Agents），PH 上线的是 Claude 目录里的官方 app"]

archived_at: "2026-08-18"
sources_count: 4
---

# ElevenLabs MCP in Claude · 扩展阅读上下文

> PT 2026-08-18 榜单第 5 名 · 👍 145 · 💬 7
> 归档日期 2026-08-18 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | ElevenLabs MCP in Claude |
| 英文 tagline | Create and manage ElevenLabs voice agents in your chat |
| 中文 tagline | 在聊天里创建并管理 ElevenLabs 语音 agent |
| 官网 | https://elevenlabs.io/ |
| 集成页 | https://claude.ai/directory/elevenlabs |
| PH 页 | https://www.producthunt.com/products/elevenlabs-mcp-2 |
| 品类标签 | Artificial Intelligence · Audio · AI Voice Agents |
| 票数 / 评论 | 145 票 / 7 评论 |
| 公司主体 | ElevenLabs（ ElevenLabs Inc.） |
| 企业版/关联站点 | elevenlabs.io；GitHub org：github.com/elevenlabs |

## 是做什么的（如实复述，不评价）

ElevenLabs MCP in Claude 是 ElevenLabs 官方接入 Claude Directory 的 MCP（Model Context Protocol）集成。用户在 Claude 聊天界面里通过 OAuth 登录自己的 ElevenLabs workspace，即可直接在对话中管理 ElevenLabs 语音 agent，不必跳到 ElevenLabs 控制台。能力包括：

- 列出已有 agent 并查看摘要
- 查看单个 agent 的配置（prompt、voice、knowledge size、widgets、links）
- 更新 agent 的 prompt 与 voice
- 复制（duplicate）/ 删除 agent
- 在改动前预估 LLM 用量（estimate LLM usage before changes）

定位是减少 context-switching，把语音 agent 的生命周期管理搬进 Claude 对话。Hunter 把目标用户描述为"在代码、生产力、设计和销售/市场团队工作的人"。

需要注意的是：底层 ElevenLabs 官方 MCP server（`github.com/elevenlabs/elevenlabs-mcp`，MIT、Python、1.5k stars）能力更广——还包括 TTS 语音合成、voice cloning、speech-to-text 转写、speech-to-speech、audio isolation、soundscape、video-to-music 等。PH 上线的这款 "ElevenLabs MCP in Claude" 更聚焦于**语音 Agent 管理**这一子集，是同一官方 MCP 体系在 Claude Directory 里的呈现入口。

## 解决什么问题（事实层面，不判断值不值得解）

- 语音 agent 配置需要在 ElevenLabs 控制台和日常工作流（Claude 对话）之间反复切换，context-switching 成本高。
- 改 agent prompt/voice 前无法预估对 LLM 用量的影响，容易超额度。
- 团队成员多（代码/设计/销售/市场），不一定都熟悉 ElevenLabs 控制台，希望在自己常用的聊天工具里操作。
- 目标场景：在 Claude 里迭代语音 agent 的 prompt 和 voice、复制变体做 A/B、清理废弃 agent、上线前检查 knowledge/widgets/links。

## 怎么做的（技术原理/机制，事实层面）

- 协议：基于 Anthropic 的 Model Context Protocol（MCP），ElevenLabs 官方维护一个 MCP server（`elevenlabs-mcp`，PyPI 包名同），Claude 作为 MCP client 调用其工具。
- 集成方式：在 Claude Directory (`claude.ai/directory/elevenlabs`) 通过 OAuth 授权 ElevenLabs workspace 访问；本地 Claude Desktop 也可走 `claude_desktop_config.json` 用 `uvx elevenlabs-mcp` 启动，配 ElevenLabs API key。
- 通用性：同一 MCP server 也可接 Cursor、Windsurf、OpenAI Agents 等其他 MCP client（README 列出）。
- 可配置项：`ELEVENLABS_MCP_BASE_PATH`（文件 I/O 目录，默认 `~/Desktop`，兼做输入文件安全边界）、`ELEVENLABS_MCP_OUTPUT_MODE`（`files` / `resources` base64 / `both`）、`ELEVENLABS_API_RESIDENCE`（数据驻留区域，企业版，默认 `us`）。
- 依赖：Python，建议用 `uv` 安装（`uvx elevenlabs-mcp`），或 `pip install elevenlabs-mcp`；仓库带 Dockerfile。
- LLM 用量预估：评论区 Sabber Ahamed 追问是 token-diff 估算还是对新配置跑一次模拟调用，官方未在 PH 页明确回答（待补）。
- License：MIT。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Mateusz (Mati) Staniszewski、Piotr Dąbkowski（2022 年联合创立 ElevenLabs） | 公开报道 |
| Hunter | Rohan Chaubey (@rohanrecommends) | PH 产品页 |
| 融资 | Series C，约 $180M，估值 $3.3B（2025 年初） | 公开报道 |
| 历轮融资 | Series A $19M（2023）；Series B $80M @ $1.1B（2024 年 1 月，a16z 领投） | 公开报道 |
| 投资方 | Andreessen Horowitz（a16z）、Nat Friedman、Mustafa Suleyman 等 | 公开报道 |
| 加速器 | 未查到 | — |
| 合规认证 | 企业版支持数据驻留（`ELEVENLABS_API_RESIDENCE`），其他合规认证未在 PH/集成页披露 | GitHub README |

## 定价 / 商业模式

PH 产品页将定价标为 "Free Options"。集成本身不单独收费——它走 ElevenLabs 账号的既有额度。ElevenLabs 的通用定价（截至本次检索未在官网首页明确列数字，以下为公开报道/历史档参考，实际以 elevenlabs.io/pricing 为准）：

- Free：$0，约 10,000 credits/月，商业使用受限
- Starter：约 $5/月
- Pro：约 $22/月
- Scale：约 $99/月
- Business / Enterprise：定制

MCP server 仓库 README 明确提到免费层提供 10k credits/月。PH 集成不引入额外订阅。

## 关联信息 / 生态

- ElevenLabs 三大产品线：ElevenCreative（内容创作）、ElevenAgents（对话 agent，本集成的管理对象）、ElevenAPI（开发者 API）。
- 声称 5,000+ 声音、70+ 语言。
- MCP client 生态：Claude（Desktop + claude.ai）、Cursor、Windsurf、OpenAI Agents。
- 同类 MCP 官方集成：ElevenLabs 也在其他 MCP client 的目录/配置里出现，但 Claude Directory 是本次 PH 上线的入口。
- PH 列出 topics：Artificial Intelligence、Audio、AI Voice Agents。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2022 | ElevenLabs 成立 |
| 2023 | Series A $19M |
| 2024-01 | Series B $80M，估值 $1.1B（a16z 领投） |
| 2025 年初 | Series C 约 $180M，估值 $3.3B |
| 2026-08-18 | ElevenLabs MCP in Claude 上线 Product Hunt 榜单第 5 名 |

底层 MCP server 的首发日期、关键版本里程碑未在 GitHub README 公开时间线，待补。

## 评论区反馈（事实摘录，不评价）

- **Sabber Ahamed**：问多人同时通过各自 Claude session 修改同一 agent 时的并发编辑冲突如何处理。
- **Anuj**：问 MCP 在 projected usage 上升或 handoff 规则变化时是否展示 diff 或要求确认（生产级 agent 关心）。
- **Alexandr Mucha**：问 Claude 是否也能直接生成语音（不只是管理 agent）。
- **Christopher martin**：问通过聊天做的 prompt 编辑是否支持版本/回滚。
- **Sabber Ahamed**（追问）：LLM 用量预估是 token-diff 计算还是对新配置做一次模拟调用。
- **Lucas Pols**：肯定把生命周期管理（review/update/duplicate/delete）和 agent 创建放一起的设计。
- Hunter Rohan Chaubey 在主帖说明集成入口与能力范围。

PH 页面上的 maker 帖未在检索中逐字呈现完整回复，待补。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/elevenlabs-mcp-2 — 拿到 tagline、描述、topics（AI/Audio/AI Voice Agents）、145 票/第 5 名/7 评论、hunter Rohan Chaubey、6 条社区评论要点、定价标 "Free Options"。
- 官网：https://elevenlabs.io/ — 拿到 ElevenLabs 三大产品线（ElevenCreative/ElevenAgents/ElevenAPI）、5,000+ 声音/70+ 语言定位；首页未提及 MCP/Claude 集成，也未列具体定价数字与融资信息。
- GitHub：https://github.com/elevenlabs/elevenlabs-mcp — 官方 MCP server，MIT、Python、1.5k stars、78 commits；README 含完整工具列表（TTS/voice cloning/STT/STS/audio isolation/soundscape/video-to-music/agent）、安装（uvx/pip）、配置项（`ELEVENLABS_MCP_BASE_PATH` / `ELEVENLABS_MCP_OUTPUT_MODE` / `ELEVENLABS_API_RESIDENCE`）、Dockerfile、免费层 10k credits/月。
- 公开报道（WebSearch 摘要）：ElevenLabs 2022 年由 Mateusz Staniszewski 与 Piotr Dąbkowski 创立；Series A $19M（2023）；Series B $80M @ $1.1B（2024-01，a16z 领投，Nat Friedman、Mustafa Suleyman 参投）；Series C 约 $180M @ $3.3B（2025 年初）。具体报道链接未逐一独立核实。
- Claude Directory 集成页 https://claude.ai/directory/elevenlabs 返回 403，未直接抓到正文（登录态限制），能力描述来自 PH 页与 hunter 主帖。

## 未查到 / 待补

- 集成页 `claude.ai/directory/elevenlabs` 正文：WebFetch 返回 403，未拿到官方落地页文案，能力描述依赖 PH 页与 GitHub README 交叉印证。
- PH 页上 maker 的逐字回复（仅拿到 hunter 主帖摘要与社区提问，maker 对每条问题的具体回复未检索到）。
- LLM 用量预估的实现（token-diff 还是模拟调用）：评论区 Sabber Ahamed 提出，官方未在 PH 页公开回答。
- 并发编辑冲突处理、prompt 编辑版本/回滚：评论区提出，未见官方答复。
- 底层 MCP server 的首发日期与版本里程碑：GitHub README 无时间线。
- ElevenLabs 当前定价数字：官网首页未列，公开报道档为历史参考，标注"以 elevenlabs.io/pricing 为准"。
- Series C 的领投方与具体条款：公开报道摘要未明确，待独立核实。
- 票数 145 与评论 7 为任务给定快照，未在检索时刻重新核对。
