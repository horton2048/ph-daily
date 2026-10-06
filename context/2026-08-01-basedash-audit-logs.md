# Basedash Audit Logs · 扩展阅读上下文

> PT 2026-08-01 Product Hunt 榜单第 8 名 · 👍 113 · 💬 9
> 归档日期 2026-08-03 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Basedash Audit Logs（Basedash 的审计日志功能） |
| 英文 tagline | Every action in your BI tool, on the record. |
| 中文 tagline | BI 工具里的每项操作都有迹可查 |
| 官网 | https://www.basedash.com |
| PH 页 | https://www.producthunt.com/products/basedash |
| 品类标签 | Artificial Intelligence · Data & Analytics · Business Intelligence |
| 票数 / 评论 | 113 / 9 |
| 公司主体 | Basedash（YC 背书公司） |
| logo | https://ph-files.imgix.net/71904071-f19e-4fc9-b2e1-38d6d3f7c648.png |
| 平台 | Web（SaaS），企业版 |

## 是做什么的（如实复述，不评价）

Basedash Audit Logs 是 Basedash（AI-native BI 平台）的第 27 次 PH 发版，提供一份原生的、不可篡改的操作日志，记录 Basedash 组织内发生的每一个动作——登录、查询、配置变更、AI 代跑查询。定位是企业安全审查与合规 rollout 的基础设施。

创始人 Max Musing 在 launch post 里写道："Today we're launching audit logs: a native record of everything that happens in your Basedash organization." 核心承诺是：当 Basedash AI 回答一个问题时，它跑的查询会被记录、归因、可追溯——"the query it ran is logged, attributed, and traceable."

## 解决什么问题（事实层面）

- **AI 进 BI 后审计对象变模糊**：以前审计员查人，现在 AI 也代跑 SQL，"谁看了什么、何时"难以归因到具体查询。
- **合规审查缺原生日志**：很多 BI 工具的日志是后补的，企业为了过 SOC 2 / HIPAA 得自建审计层。
- **SIEM 对接需求**：安全团队要把 BI 操作事件汇入现有 SIEM（Splunk/Sumo 等）做统一监控。
- **目标场景**：企业安全合规、SOC 2 审计、内部数据访问追溯、AI 代跑行为取证。

## 怎么做的（技术原理/机制）

来源：basedash.com + PH 产品页

- **原生日志层**：每个动作（SSO 登录、AI 查询、行级策略应用、访问拒绝、SCIM 同步、SQL trace、dashboard 分享、密钥轮换、metric 定义版本化）都进日志。
- **AI 代跑归因**：当 Basedash AI 替用户跑查询时，日志记录"由 AI 代 <用户> 跑了这条 SQL"，不只是 session 级。
- **SIEM 流式推送**：事件流可推到 SIEM 系统（页面上有 "Audit export · streamed to SIEM" 演示条目）。
- **保留期可配**：按组织政策调整留存时长。
- **API 全量访问**：日志数据可通过 API 取出。
- **配套合规栈**：与 SSO、SCIM、RBAC 同期发布；AES-256 at rest、传输加密、SOC 2 Type II、"数据从不用于训练模型"。
- **metric 定义版本化**：如 "MRR · definition v12"，定义变更可追溯。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Max Musing（Founder/CEO，最活跃评论者） | PH 产品页 |
| 联合团队 | Derek Reynolds、Kristofer Lachance（均列 launch team，Kristofer 为 maker） | PH 产品页 |
| 加速器 | Y Combinator（YC 背书） | PH / 公开报道 |
| 融资 | 网络检索约 $5M（含 YC 标准投资 + seed 轮），具体轮次/投资方未在官网披露 | 公开报道（未坐实） |
| PH 关注数 | 2.8K | PH 产品页 |
| 历史发版 | 27 次 PH 发版（Basedash AI Kit 2026-07-23、Suggestions 07-17、SCIM 07-11、Actions 07-02 等） | PH 产品页 |

## 定价 / 商业模式

来源：PH 产品页 + basedash.com

- **Audit Logs 仅在 Enterprise 计划提供**（maker 原话："Audit logs are available on the Basedash Enterprise plan today"）。
- **Free 起步**：免费版供试用（具体额度未在抓取页面明示）。
- **Enterprise**：含 SSO/SCIM/RBAC/Audit Logs，定制报价。
- 模式：**SaaS 订阅**，企业版高客单 + 卖合规护栏。审计日志是"进企业必须配齐"的功能模块，与 SSO/SCIM/RBAC 同套打包。

## 关联信息 / 生态

- **定位对手**：Retool、Appsmith、Metabase（admin panel / BI 内部工具赛道）。
- **AI Kit**（前次发版 2026-07-23）："Ship AI analytics in your product, powered by GPT-5.6"——Basedash 把自家 AI 能力也 SDK 化对外卖。
- **合规栈**：SOC 2 Type II、AES-256 at rest、传输加密、SCIM、SSO、RBAC。
- **PH 发版节奏**：近一个月每 1-2 周一次发版（SCIM、Suggestions、AI Kit、Audit Logs），高频 ship 节奏。
- **GitHub**：github.com/Basedash（存在公开组织，具体仓库内容未抓取）。

## 技术时间线

| 日期 | 事件 |
|---|---|
| 2019 | Basedash 创立（PH 页公开信息） |
| 2026-07-02 | Basedash Actions 发版 |
| 2026-07-11 | Basedash SCIM 发版 |
| 2026-07-17 | Basedash Suggestions 发版 |
| 2026-07-23 | Basedash AI Kit 发版（GPT-5.6 驱动） |
| 2026-08-01 | Basedash Audit Logs 发版（PH #8） |

## 评论区反馈（事实摘录）

- **Artem Fedorovich**（提问）：日志是查询级还是操作级？Max 回复："yup! We log every query and who ran it, including if it was queried by an AI on behalf of a user."（确认查询级 + AI 归因）
- **Raffay Sajjad**（提问）：保留期能否针对特定字段脱敏，避免 PII 在被删除请求后仍存于日志？maker 未直接回答。
- **Asad M.**（提问）：AI 自然语言摘要是否与查询一同存储？正确查询配上错误摘要是真正的风险。maker 未直接回答。
- **Hazy**（提问）：日志存的是完整原始 SQL 还是仅 metadata/hash 用于 SIEM 导出？maker 未直接回答。
- **Kristofer Lachance**（maker 评论）："We've been getting more requests for audit ability, which is a big reason why companies choose Basedash."

## 信息来源

- PH 产品页：https://www.producthunt.com/products/basedash（maker Max Musing / Kristofer Lachance 评论、AI 代跑归因确认、Enterprise 计划说明、logo、27 次发版历史）
- 官网：https://www.basedash.com（审计日志事件演示、SIEM streaming、SOC 2 Type II、AES-256、SCIM/SSO/RBAC 配套）
- 公开报道：网络检索（YC 背书、约 $5M 融资、Max Musing 创始人身份）—— 融资具体数字未在官网坐实
- GitHub：github.com/Basedash（公开组织存在，仓库内容未深入抓取）

## 未查到 / 待补

- **融资金额/轮次/具体投资方**：网络检索约 $5M，未在官网或权威来源坐实
- **YC 具体批次**：未明确是哪一期
- **Free / Pro / Enterprise 三档具体价格**：抓取页面未明示
- **Audit Logs 保留期默认值与上限**：未披露
- **SIEM 具体支持厂商**（Splunk/Sumo/Datadog？）：未明确
- **API 取日志的端点/限速**：未公开
- **Raffay/Asad/Hazy 三个未答问题的官方回复**：PH 评论区未见
- **公司注册主体/注册地**：未在抓取页面明示
