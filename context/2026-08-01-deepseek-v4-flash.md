# DeepSeek-V4-Flash-0731 · 扩展阅读上下文

> PT 2026-08-01 Product Hunt 榜单第 1 名 · 👍 347 · 💬 10
> 归档日期 2026-08-03 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | DeepSeek-V4-Flash-0731 |
| 英文 tagline | Frontier agent intelligence at Flash prices |
| 中文 tagline | 以 Flash 价格提供前沿智能体能力 |
| 官网 | https://www.deepseek.com |
| API 平台 | https://platform.deepseek.com |
| API 文档 | https://api-docs.deepseek.com |
| PH 页 | https://www.producthunt.com/products/deepseek-v4-flash-0731 |
| 品类标签 | API · Open Source · Artificial Intelligence |
| 票数 / 评论 | 347 / 10 |
| 公司主体 | 杭州深度求索人工智能基础技术研究有限公司（Hangzhou DeepSeek Artificial Intelligence Basic Technology Research Co., Ltd.） |
| 稳定模型 ID | `deepseek-v4-flash`（后端版本号 `DeepSeek-V4-Flash-0731`） |
| logo | https://avatars.githubusercontent.com/u/148330874?s=200&v=4 |

## 是做什么的（如实复述，不评价）

DeepSeek-V4-Flash-0731 是 DeepSeek 于 2026 年 7 月 31 日公开的智能体模型，对应 V4-Flash 系列的 0731 后端版本。它属于 V4-Flash 架构（284B 总参数 / 13B 激活的 MoE，43 层），相较 4 月的 V4-Flash 预览版**参数和权重不变，仅重做后训练**。核心卖点：在保持 Flash 价格（$0.14/$0.28 per 1M tokens）的同时，agent 能力大幅增强，**官方称在 9 项 vendor-reported agent benchmark 上反超自家旗舰 V4-Pro-Preview**（1.6T 总参数 / 49B 激活）。原生支持 OpenAI Responses API（含 function tools 和 server-side web search）和 Codex CLI 集成，1M token 上下文，384K max output，思考默认开启、可调 effort。

## 解决什么问题（事实层面，不判断值不值得解）

- **闭源旗舰跑 agent 又贵又难接**：GPT/Claude 旗舰按 $5-15/M token 计费，agent 多步调用累积成本高；DeepSeek 以 $0.14/$0.28 把单次调用成本压到约 1/50。
- **Codex CLI 适配碎片化**：业界通常要单独做 provider 适配才能接 Codex CLI；V4-Flash-0731 原生支持 Responses API，可作为 custom provider 直接接入 Codex CLI、ChatGPT 桌面 app 和 Codex VS Code 扩展。
- **闭源模型不可自部署**：对于有数据合规/主权诉求的用户（半导体厂、政府、企业），闭源 API 不可控。V4-Flash-0731 MIT 开源权重，可自部署。
- **大模型才能跑 agent 的刻板印象**：1.6T 旗舰 V4-Pro-Preview 在 agent benchmark 上被 13B 激活的 Flash 反超。

## 怎么做的（技术原理/机制，事实层面）

来源：DeepSeek 官网 + 多源公开报道（explainx.ai, kingy.ai, getllms.org, byteiota.com, felloai.com, aimodeling.com, deepseekv4guide.org）

- **架构**：284B-MoE / 13B 激活参数，43 层，1M token 上下文，384K max output。继承 V4 系列的 Manifold-constrained Hyper Connections（mHC）、Constrained Sparse Attention（CSA）、Muon optimizer。
- **后训练重做**：相比 4 月 V4-Flash 预览版，参数与权重不变，仅重做后训练（post-training），agent 能力提升主要来自这一步。
- **原生 Responses API**：支持 OpenAI Chat Completions API 兼容 + 原生 Responses API（stateless、function tools、server-side web search）。
- **Codex CLI 集成**：作为 custom provider 跨 Codex CLI、ChatGPT 桌面 app、Codex VS Code 扩展可用。
- **思考默认开启**：thinking 默认 on，可配置 effort 级别。
- **开源许可**：MIT License（自 R1 起所有新模型均 MIT）。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | 梁文锋（Liang Wenfeng），同时任 DeepSeek 与母公司 High-Flyer（幻方量化）CEO | Wikipedia |
| 母公司/出资方 | High-Flyer（幻方量化，中国对冲基金）；2016 年起建 AI 算力，2021 年 Fire-Flyer 2 集群约 5000 块 A100 | Wikipedia |
| 公司注册 | 杭州深度求索人工智能基础技术研究有限公司，2023-07-17 注册，总部杭州 | Wikipedia + 官网 |
| 融资 | 2026-04 报道寻求 $300M 轮次，估值 $10B；2026-07 Bloomberg/FT 报道筹备最早 2027 年 IPO | Wikipedia/Bloomberg/FT |
| 控股 | 梁文锋个人通过两家壳公司持股 84%（2024-05 数据） | Wikipedia |
| 团队规模 | 约 160 人（2025 年数据），从中国顶尖高校及非 CS 领域招聘 | Wikipedia |
| 加速器 | 无（自有资金起家，VC 早期犹豫） | Wikipedia |
| 合规认证 | 无提及；相反：US FY2026 NDAA 要求从国防部和情报系统移除 DeepSeek；澳大利亚政府范围禁用；2026-02 Anthropic 指控 DeepSeek 用数千欺诈账号从 Claude 抽取训练数据 | Wikipedia |

## 定价 / 商业模式

来源：morphllm.com 抓取 DeepSeek API 定价页（2026-08）

- **deepseek-v4-flash**：
  - 输入 $0.14/1M（cache miss）
  - 输入 $0.0028/1M（cache hit，命中缓存约 1/50 价格）
  - 输出 $0.28/1M
- **deepseek-v4-pro**：
  - 输入 $0.435/1M
  - 输出 $0.87/1M
- **开源权重**：MIT License，可自部署免 API 费
- **1M context window** via OpenAI-compatible endpoint
- 模式：API 按量计费（走量）+ 开源权重自部署（免费）+ 企业采用（华为、寒武纪等半导体厂商已采用 V4 系列）

## 关联信息 / 生态

- **V4 系列**（2026-04 发布）：V4-Flash（284B/13B 激活，43 层）+ V4-Pro（1.6T/49B 激活，61 层），均 1M context、MIT
- **架构创新**（V4 引入）：Manifold-constrained Hyper Connections（mHC）、Constrained Sparse Attention（CSA）、Muon optimizer
- **历史模型**：V3（671B/37B 激活，2024-12）、R1（推理模型，2025-01，引发 Nvidia 单日跌 $600B）、Coder V2、VL、V2、Math 等
- **半导体采用**：华为、寒武纪等采用 V4 系列
- **GitHub**：github.com/deepseek-ai（开源仓库 DeepEP、FlashMLA、DeepGEMM、DeepSpec、3FS、DeepSeek-OCR 等）

## Benchmark（vendor-reported，官方称）

来源：byteiota.com、felloai.com、deepseekv4guide.org、deepseekreasonix.com 引用 DeepSeek 官方 model card

| Benchmark | V4-Flash-0731 | V4-Pro (Preview) | V4-Flash (4 月预览) |
|---|---|---|---|
| Terminal-Bench 2.1 | 官方称 82.7 | 72.1 | 61.8 |
| DeepSWE | 官方称 54.4 | 12.8 | — |
| AA Intelligence Index | 50 | — | — |

- 官方称在 9 项 agent benchmark 上反超 V4-Pro-Preview
- **caveat**：benchlm.ai 提示 Terminal-Bench 跳跃是比较了两个 benchmark 版本；DeepSeek 自己的表显示在全部 9 行上仍落后于 Opus 4.8

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2023-07-17 | DeepSeek 成立（High-Flyer AGI 实验室独立） |
| 2024-12 | V3 发布（671B/37B 激活） |
| 2025-01 | R1 发布（引发 Nvidia 单日跌 $600B） |
| 2026-02 | Anthropic 指控 DeepSeek 用欺诈账号抽取 Claude 数据 |
| 2026-04 | V4 系列（Flash + Pro）发布 |
| 2026-04 | 报道寻求 $300M 轮次，$10B 估值 |
| 2026-07 | Bloomberg/FT 报道筹备 2027 IPO |
| 2026-07-31 | V4-Flash-0731 公测（agent 升级 + Responses API + Codex CLI） |

## 评论区反馈（事实摘录，不评价）

- PH 评论数仅 10（对比 Zinley 91），评论区样本小，未抓到创始人长评论或典型质疑。
- 公开报道中的关键质疑：benchlm.ai 提示 Terminal-Bench 版本不一致；DeepSeek 自己的表显示仍落后于 Opus 4.8。

## 信息来源

- PH 产品页：producthunt.com/products/deepseek-v4-flash-0731（票数 347、tagline、描述）— 抓取受限，未能直接拿到页面全文
- 官网：deepseek.com（公司主体、模型列表、API 平台入口）
- Wikipedia：DeepSeek（公司）— 创始人梁文锋、High-Flyer 背景、融资 $300M/$10B 估值、IPO 2027、团队 160 人、争议事件
- 多源公开报道（explainx.ai、kingy.ai、getllms.org、byteiota.com、felloai.com、aimodeling.com、deepseekv4guide.org、deepseekreasonix.com、codex.danielvaughan.com、morphllm.com、benchlm.ai）：定价、benchmark、架构、Responses API、Codex CLI 集成细节
- GitHub：github.com/deepseek-ai（开源仓库列表，未直接发布 V4-Flash-0731 release 公告）

## 未查到 / 待补

- **PH 产品页全文/创始人评论**：producthunt.com 抓取受限，未拿到 maker 长评论和典型用户反馈（PH 仅 10 条评论，样本小）
- **官方 model card 原始数据**：未直接抓到 DeepSeek 官方 model card 全文，benchmark 数字来自二手报道引用
- **企业版/合作伙伴具体名单**：仅 Wikipedia 提"华为、寒武纪等半导体厂商采用"，未拿到官方合作公告
- **IPO 具体进度**：仅 Bloomberg/FT 2026-07 报道筹备 2027 上市，无更新进展
- **V4-Flash-0731 的 SWE-bench Verified 数字**：报道中未见 SWE-bench，只有 DeepSWE（54.4）
- **OpenAI Chat Completions 与 Responses API 的具体差异实现**：未深入抓取
