---
product: "easyspecs.ai"
slug: "easyspecs-ai"
date: "2026-09-11"
rank: 6
votes: 132
comments: 18

category: "SaaS / 开发者工具"
subcategory: "Spec 评审平台 / SDD 工具"
tags: ["Spec-Driven Development", "Trust Engineering", "Oracles & Rubrics", "MCP", "代码库文档化", "BYOK", "AI 代理协作", "知识沉淀", "AI 治理"]

tech_stack: ["Web (SaaS)", "Git 仓库直连（GitHub / GitLab / Azure DevOps / Bitbucket）", "OpenRouter（AI 网关）", "MCP Server", "VS Code / Cursor / Codex / Claude Code / Antigravity 兼容 IDE"]
platform: ["Web (SaaS)", "MCP 集成", "VS Code 兼容 IDE（Cursor / Codex / Claude Code / Antigravity）"]
open_source: false
license: ""

business_model: "Freemium + 订阅制（按 repo / 月）+ 企业私有化"
pricing_start: "€0（3 credits 试用）· €5/repo/月（Workbench，BYOK）· €150/月（Factory，含 AI credits）"
funding_stage: "未披露"
funding_amount: "未披露"

related_products: ["Codex 3.0（OpenAI）", "Swimm", "Kiro", "Traycer AI", "GitStart", "Greptile", "Sourcery", "CodeRabbit"]
maker_previous: ["Xesca Alabart：15+ 年 fintech/insurtech/media 行业 CTO 经历（PH makers 描述）", "Carlos Guirao Capistany：软件架构 + AI 系统（公司 about 页描述）"]

key_signals:
  - "Spec 是 SDD 时代的合并单元——官方明文 'Code review is the enemy'，把质量前移到 Spec 评审环节；不是替代代码评审，而是上游拦截"
  - "每个 Spec 都自带 Oracles（机器可跑的 pass/fail 检查）+ Rubrics（人/AI 评分准则）——这是与一般文档工具的关键差异：文档自带可验证的'信任凭证'"
  - "三层定位清晰：developer（停止 babysitting agent）/ Technical PM（写开发者能照着做的 spec）/ Org leader（一套 SDD 操作系统）"
  - "Workbench €5/repo/月 BYOK（无 AI markup）+ Factory €150/月自带 credits——按 repo 计费而非按席位计费，对大仓库小团队友好"
  - "PH 票数 132 排名第 6，评论 18 条里过半是产品/技术细节追问（Oracles 准确性、MCP 联通、legacy 语言覆盖），可见目标用户偏开发者向"

archived_at: "2026-09-12"
sources_count: 5
---

# easyspecs.ai · 扩展阅读上下文

> PT 2026-09-11 Product Hunt 榜单第 6 · 👍 132 · 💬 18  
> 归档日期 2026-09-12 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | easyspecs.ai（官方次称 "Your Spec Engineering Assistant"） |
| 英文 tagline | The spec review platform |
| 中文 tagline | Spec 评审平台 |
| 官网 | https://easyspecs.ai |
| PH 页 | https://www.producthunt.com/products/easyspecs-ai |
| 品类标签 | SaaS · Developer Tools · Development · Knowledge base software |
| 票数 / 评论 | 132 / 18 |
| 关注者 | 105 |
| 公司主体 | Spaii Labs SL（页脚："© 2026 EasySpecs.ai · Built by Spaii Labs SL"） |
| 办公地址 | Pier07, Via Laietana 26, 08003 Barcelona, Spain（Gothic Quarter，近 Jaume I 地铁） |
| 联系人邮箱 | xesca.alabart@easyspecs.ai |
| 关联站点 | /features/spec-review · /features/from-code-to-documentation · /features/migration-harness · /mission · /code-review-is-dead · /use-cases/* · /labs/learn-trust-engineering |

## 是做什么的（如实复述，不评价）

Spec-Driven Development（SDD）平台。把"写代码前先把规格写清楚"做成一门可被 AI 代理消费的工作产物，而不是停留在 PR 描述或 wiki 草稿。

每个 Spec 由一组配对产物组成：核心是 Spec（结构化 + HTML 双视图），旁边挂 **Trust Spec**——一组机器可跑的 Oracles（pass/fail 验证）+ 人/AI 共用的 Rubrics（评分准则）。一个完整 Spec 还会展开成 Change（改动说明）、Intent（意图）、Diagram（结构图）、Steps（步骤）。

最核心的产品动作分三步：

1. **从代码生成文档**：自动给未文档化代码库生成功能文档，官方宣称"up to 98% LOC coverage assignment"
2. **打磨意图并落地到当前代码库**：把模糊的"想做 X"细化成可评审的 Spec
3. **产出 Trust by Design Spec**：结构化 + HTML 视图，附带可执行校验

PH 描述用一句话概括："As AI agents generate code faster than humans can review, spec review becomes the new merge request review. The tool grounds agents in reality, helping teams ship code you actually verified."

## 解决什么问题（事实层面，不判断值不值得解）

- **文档腐烂（docs lag）**：legacy 系统（PH 评论里举例 Delphi 等老语言）几乎没有文档，新人接手和 AI 代理理解都无从下手
- **AI 时代代码评审过载**：代理写代码速度 >> 人类评审速度，merge request 排队堆积（官方首页原话："Merge requests have surged"）
- **需求到实现的失真**：business 想要 X，开发实现成 Y，中间缺乏可被共同引用的"事实"层
- **缺乏可验证的成功标准**：PRD 写"用户体验好"，但无机器可跑的验收条件——Oracles + Rubrics 试图补这一层
- **非开发者参与障碍**：PM / 业务方想验证 Spec 是否符合预期，但传统 spec 写得开发者才能看懂（官方原话："Built for non-developers — PMs and leads can verify specs without reading source"）

## 怎么做的（技术原理/机制，事实层面）

- **Git 直连**：通过只读 PAT 接入 GitHub / GitLab / Azure DevOps / Bitbucket
- **AI 推理网关**：走 OpenRouter，支持 OpenAI / Anthropic / Google / OpenRouter 等多家模型
- **MCP Server**：PH 评论里 Carlos 明确回复——编码代理可通过 MCP 下载生成的 Spec，并能把 Spec 标记为 implemented
- **IDE / 代理兼容**：Codex · Claude Code · Cursor · VS Code · Antigravity，以及任何 VS Code 兼容 IDE
- **项目工具联动**：Jira · Linear
- **文档同步机制**：自动跟代码变更重同步（应对 docs lag），但不支持"代码一行变文档实时更新"那种被动同步——官方在 PH 回复 Naim 时明确："we dont in the way you are thinking"，Spec 是写变更请求（feature/fix/bug）+ 自动文档两条独立路径
- **Trust Spec 结构**：每个 Spec 内置 Oracles（机器可跑校验）+ Rubrics（评分标准），目的是把"什么叫好"从 code generation 一路定义到 runtime
- **失败处理 / 准确率**：Dipanshu 在 PH 评论里追问"代码库巨大且混乱时文档准确性如何"——公开材料未给出量化错误率，但官方强调 Oracles/Rubrics 是为应对"不可信"而设

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 / CEO | Xesca Alabart（PH handle @xesca_i_am，LinkedIn: linkedin.com/in/x-alabart）| PH makers + 公司 about 页 |
| 联合创始人 / CTO | Carlos Guirao Capistany（PH handle @carlos_guirao，LinkedIn: linkedin.com/in/carlos-guirao-capistany-8b20712b）| PH makers + 公司 about 页 |
| 其他 maker | Chima Ojimma（@chima_peter）· Ayo Ajayi（@ayomi_）| PH makers 列表（PH 显示 4 人，非公司创始团队全员） |
| 融资 | 未披露 | — |
| 投资方 | 未披露 | — |
| 加速器 | 未披露 | — |
| 合规认证 | 无（B2B SaaS，无合规声明）| — |
| 公司主体 | Spaii Labs SL（西班牙巴塞罗那）| 页脚 |

> PH 上 4 位 maker 含两位 CTO/联合创始人 + 两位协作者；PH launch 致谢里 Ayo Ajayi 自称 "FINALLY"，Xesca 回复"would not have been possible without you"——合作关系紧密，但具体角色未公开说明。

## 定价 / 商业模式

| 套餐 | 价格 | 关键约束 | AI 推理 |
|---|---|---|---|
| Free Trial | €0 | 一次性 3 credits | EasySpecs 自带 key |
| Workbench | **€5/repo/月**（限免 50%，原价 €10）| BYOK，无 credit 系统 | 用户自带 key，无 markup |
| Factory | **€150/月** | 15 credits/月，可任意 repo 使用；额外 credits €150/10 个 | EasySpecs 自带 key |
| Enterprise | Custom（联系销售）| 私有工厂（VPC / 私有云 / on-prem）+ Migration Harness + 自定义 token / credit 条款 | 含 Migration Harness |

补充说明：
- 计费按 **repo**，非按席位
- 兼容仓库：GitHub / GitLab / Azure DevOps / Bitbucket
- "How credits convert"（每个动作消耗多少 credit 的明细表）页面未抓取到
- 企业版独家功能 Migration Harness 子模块：Docs as Golden Validator · Generate Porting · Adhoc Harness · Drift Analysis

**除 SaaS 外，官方还提供交付型服务**（非纯订阅）：Code Audit · Dark Factory Delivery · In-House Factory Buildout · Control Plane Implementation · Token Optimization · Company / individual training · Catalyst workshop。这意味着收入结构是 SaaS + 高端咨询混合。

## 关联信息 / 生态

- **同 PH 标签位的相关产品**：Codex 3.0（OpenAI，5.0 · 85 reviews）· Swimm（5.0 · 7 reviews）· Kiro（5.0 · 11 reviews）· Traycer AI（5.0 · 5 reviews）· GitStart（4.9 · 12 reviews）
- **与 AI 代码评审工具（Greptile / Sourcery / CodeRabbit）的关系**：用户提问里常被并列，但官方姿态不同——首页明文"Code review is the enemy"，把质量前移到 Spec 评审环节，定位是**上游拦截**而非**评审补充**。两者解决不同环节的问题：easyspecs.ai 在"写代码前"，CodeRabbit 类工具在"写代码后"
- **与 Swimm 的关系**：Swimm 也是代码文档化工具，差异在于 easyspecs.ai 强调"文档自带可验证凭证（Oracles/Rubrics）"+ SDD 工作流，Swimm 偏向开发者学习/上手文档
- **与 Kiro / Traycer AI 的关系**：后者也走 spec/plan-first 路线，但 easyspecs.ai 的差异点是 Trust Spec（Oracles + Rubrics 内嵌）+ MCP 标准协议
- **官方服务矩阵**：Code Audit（代码审计）/ Dark Factory Delivery（暗灯工厂交付）/ In-House Factory Buildout（内部工厂搭建）/ Token Optimization（token 成本优化）/ Catalyst workshop——表明不只卖 SaaS，还在卖方法论落地
- **媒体露出**：未查到第三方独立报道
- **GitHub 仓库**：未查到公开仓库（PH 页 + 官网均未提 GitHub 链接）

## 技术时间线

| 日期 | 事件 |
|---|---|
| 2026 | Spaii Labs SL 注册并推出 EasySpecs.ai（页脚标注 "© 2026"）|
| 2026-09-11 | PH 上榜（#6，132 票，18 评论）|

> 官网有 `/changelog` 风格入口，但本次抓取未拿到具体里程碑条目。

## 评论区反馈（事实摘录，不评价）

- **Priya K**："nice launch congrats for shipping 🙌"
- **Dipanshu Kushwaha**："How accurate is the documentation when the codebase is really large and messy?" — 团队未量化回答
- **Meet Patel**："Can the approved specs be directly used by coding agents through MCP?"
  - **Carlos Guirao 回复**："Yes we have a MCP server that allows coding agents to download the generated specs. Also they can mark the spec as implemented."
- **Fenil Patel**："How does EasySpecs handle specs for complex legacy systems?"
  - **Xesca 回复**："yes it does, we even tested with some clients with legacy code with languages like Delphi and other reaaaaally old frameworks that are hardly maintained for their teams."
- **Naim Azoutar**："How do you keep the specs tied to the code over time, do they update automatically when the code changes?"
  - **Xesca 回复**："we dont in the way you are thinking. that's why the tools has two main functions, 1.- Help you craft the best (change request (feature, fix, bug, whatever) and 2.- the automatic documentation based on the code. We all have been complaining since always that we dont have updated documentation of the application the tool does this automatically for you."
- **Shivam Kushwaha**："This is a really useful product for AI teams How do you see EasySpecs fitting into the dev workflow long term?"
  - **Xesca 回复**："humans need a UI to interact with the 'what we want build' -> lets call it the change request, lets call it the ask, whatever is, needs to be validated, reviewed and understood."
- **Rahul Pahuja**："Didn't know that these sort of tools existed. Excited to see this in action going forward"
  - **Xesca 回复**："sure, still a new things, only the real top people are doing spec reviews, but wait that's going to explode!"
- **Ayo Ajayi**："FINALLY!!!! 🍾🎉🎊"
  - **Xesca 回复**："would not have been possible without you."

> 18 条评论里过半是技术追问（Oracles 准确性、MCP 联通、legacy 覆盖），未见价格争议、负面反馈或 bug 报告；评论氛围以祝贺+求证为主，提问者多偏开发者向。

## 信息来源

- **PH 产品页**：https://www.producthunt.com/products/easyspecs-ai（拿到 tagline · 完整描述 · 18 条评论 · 4 位 maker · 5 个类似产品 · 关注者数 · 上榜日期）
- **官网首页**：https://easyspecs.ai（拿到产品定位 · 三步走工作流 · 目标用户分层 · IDE/项目工具集成清单 · 服务矩阵 · 哲学口号 · Spaii Labs 主体）
- **官网 pricing 页**：https://easyspecs.ai/pricing（拿到四档定价 · credits 机制 · BYOK/自带 key 区别 · Migration Harness 是企业版独占 · 兼容仓库清单）
- **官网 about 页**：https://easyspecs.ai/about（拿到 Xesca + Carlos 全名 · 巴塞罗那办公地址 · 双方 LinkedIn · 邮箱 · 母公司 Spaii Labs SL）
- **官网 mission 页**：https://easyspecs.ai/mission（拿到 "ground truth first, then direction" 哲学 · 三步走 · Xesca 签名）
- **官网 manifesto 入口**：https://easyspecs.ai/code-review-is-dead（拿到 "code review is damage" 立场 · Change → Trust engineering → Deployment 流程图 · 抗 code-review 哲学）

## 未查到 / 待补

- **GitHub 公开仓库**：官网与 PH 页均未提 GitHub 链接，无开源代码可审计
- **融资信息**：未披露（无 Crunchbase / PitchBook / 任何公开融资公告）
- **完整 founder 履历**：Carlos Guirao Capistany 的具体经历只有公司页一段简介，第三方履历未抓到
- **Credit 消耗明细**："How credits convert" 表本次未抓取，每个动作的 credit 单价不明
- **Oracles / Rubrics 的具体技术实现**：是 LLM-as-judge？静态规则？测试代码生成？公开材料未披露
- **准确率声明**：Dipanshu 追问大代码库的文档准确性，官方未给出量化数字；"98% LOC coverage assignment" 是覆盖度而非准确度
- **Migration Harness 细节**：四个子模块名字列出但功能描述未公开
- **独立第三方报道**：未查到
- **Twitter/X 账号**：官网未提供，PH handle 有但主页未深挖
- **changelog 历史**：官网有 changelog 入口但本次未抓取到具体里程碑
- **企业版客户案例**：定价页"contact sales"无任何已公开客户或案例