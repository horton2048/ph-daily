---
product: "EquityBee Benchmark"
slug: "equitybee"
date: "2026-08-11"
rank: 3
votes: 0
comments: 3

category: "Fintech"
subcategory: "股权薪酬基准"
tags: ["股权", "期权", "薪酬基准", "创业公司", "免费", "数据驱动", "员工侧"]

tech_stack: ["Webflow", "Claude API", "ChatGPT API"]
platform: ["Web"]
open_source: false
license: ""

business_model: "免费工具 + 股权融资服务（非追索权融资）"
pricing_start: "免费"
funding_stage: "Series B-II"
funding_amount: "约 $83.1M 累计"

related_products: ["Levels.fyi", "Carta Benchmark", "Pave", "OptionImpact"]
maker_previous: ["未查到"]

archived_at: "2026-08-11"
sources_count: 5
---

# EquityBee Benchmark · 扩展阅读上下文

> PT 2026-08-11 第 3 名 · 👍 0（早期快照） · 💬 3
> 归档日期 2026-08-11 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | EquityBee Benchmark |
| 英文 tagline | Compare your startup equity grant for free. |
| 中文 tagline | 免费比较你的创业公司股权授予 |
| 官网 | https://equitybee.com/startup-equity-benchmark |
| PH 页 | https://www.producthunt.com/products/equitybee |
| 品类标签 | Fintech · Data & Analytics · Career |
| 票数 / 评论 | 0 / 3 |
| 公司主体 | EquityBee Inc.（证券业务通过关联方 EquityBee Securities, LLC，FINRA 成员提供） |
| 企业版/关联站点 | equitybee.com（员工股权融资主站）；Palo Alto + Tel Aviv 双办公地 |

## 是做什么的（如实复述，不评价）

EquityBee Benchmark 是 EquityBee 推出的免费股权授予基准查询工具，面向美国创业公司员工。用户选择"职能部门 / 职级 / 公司阶段"后，工具基于 EquityBee 平台自有数据集生成对比组，返回该对比组内新员工股权授予 FMV（授予时公平市场价值）的 25 分位、中位数、75 分位和均值，用以对照自己拿到的 offer。

页面明确声明："The goal is not to predict what those options may eventually be worth. It is to give employees a relevant comparison point."（目标不是预测期权最终价值，而是给员工一个相关对比点。）

## 解决什么问题（事实层面，不判断值不值得解）

- 公司方长期使用薪酬基准来设计股权 offer，员工评估 offer 时几乎没有同等市场参照——Oren Barzilai 在 PH 评论中明确把这一不对称作为动机。
- 薪酬有基准（Levels.fyi 类），股权"更难比较"——Benchmark 页面主标题即"Salaries have benchmarks. Equity is harder to compare."
- 目标场景：员工评估新 offer、谈判股权条款时获取同行可比数据。

## 怎么做的（技术原理/机制，事实层面）

- **数据来源**：来自员工通过 EquityBee 平台提交的已核验新员工股权授予（"verified new-hire equity grants submitted through Equitybee"），明确写"derived exclusively from Equitybee's platform data"。
- **数据规模**：9,000+ 条已核验授予，覆盖 2,500+ 家美国创业公司，阶段从 Seed 到 Pre-IPO。数据最后更新于 2026 年 7 月。
- **口径**：只统计"新员工授予"（new-hire grants，即入职时拿到首笔），不含 refresh 或晋升授予。
- **比较口径**：Fair Market Value at grant = Options Granted × FMV per Share at Grant；对大多数期权，授予时 FMV = 行权价（strike price）。
- **输出**：选定对比组的 25 分位、中位数、75 分位、平均授予 FMV。
- **差异化**：对比 Levels.fyi（自报总薪酬）与 Carta Benchmark（公司侧 cap table 记录），EquityBee 是员工侧数据、聚焦创业公司股权而非总薪酬。
- **免责声明**："has not been independently verified"，"may not represent the full startup market"——明确不保证代表性。
- **技术栈**：PH 页 Build tools 标注 Webflow + Claude by Anthropic + ChatGPT by OpenAI。
- **访问要求**：免费，但查看详细对比组结果需注册账户。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Oren Barzilai（CEO & 联合创始人） | equitybee.com/about、PH 评论、LinkedIn |
| 创办年 | 2017（About 页口径）；CB Insights 公司档案记 2018 | 两源不一致 |
| 公司主体 | EquityBee Inc.（特拉华？未查到注册州） | equitybee.com 页脚 |
| 证券通道 | EquityBee Securities, LLC（FINRA 成员，关联方） | 官网页脚 |
| 双办公地 | Palo Alto（955 Alma St., Suite B）+ Tel Aviv（55 Menachem Begin St.） | 官网 |
| 累计融资 | $83.1M | CB Insights |
| 最近一轮 | Series B-II，约 5 年前，$55M | CB Insights |
| 已知投资方 | Battery Ventures、Group 11（Series B 领投，据 TC 标题）、Phoenix Court、ICON Continuity Fund、AltaIR Capital | CB Insights |
| 收购状态 | **未查到被收购记录**。CB Insights 标"Series B - II | Alive"（仍独立运营）。用户提到的"2023 年被 Citadel 的 Equifax 收购"经搜索未获任何证据，且 Citadel 与 Equifax 为不同实体，此说法**未核实，疑似错误**。 | CB Insights、DuckDuckGo/Google 搜索无相关结果 |
| 加速器 | 未查到 | |
| 合规认证 | EquityBee Securities, LLC 为 FINRA 成员；页面声明 Benchmark 数据未独立核验、仅供参考 | 官网 |

## 定价 / 商业模式

- **Benchmark 工具本身**：完全免费，需账户查看详细对比组。
- **EquityBee 主业务**：非追索权融资（non-recourse financing）——出资帮员工行权或变现股权，员工不出自付现金；若公司未退出，EquityBee 承担损失（非追索）。具体费率/分成比例未在公开页面披露。
- **投资者侧**：可投单家公司员工期权，提供 ROI 计算器对比二级市场投资；有 DPI 业绩季报（Q1 2026、Q4 2025）和流动性案例（Groq、Wiz、Circle、eToro）。
- **客户成功案例**（官网引用）：Wiz 员工"收购时保留 $5.2M+"；Groq 员工"保留 $2.9M+"；Circle 员工"IPO 时保留 $430K"。

## 关联信息 / 生态

- 直接对标：Levels.fyi（自报总薪酬）、Carta Benchmark（公司侧 cap table）、Pave、OptionImpact（员工股权基准）。
- EquityBee 自身已发产品：股权融资行权、二级市场流动性、投资者单公司投资、ROI 计算器、DPI 业绩报告。Benchmark 是其面向 C 端员工的获客入口之一。
- PH 页显示这是 EquityBee 在 Product Hunt 上的第 3 次发布。
- 评论区高赞评论者：Oren Barzilai（CEO，详细讲数据来源与机制）、Gal Steinman（员工，痛点叙事）、Or Shemesh（"leveling the playing field"）。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2017/2018 | EquityBee 成立（两源口径不一） |
| 2021-11 | $55M Series B，由 Group 11 领投（据 TechCrunch 标题） |
| 2026-07 | Benchmark 数据集最近一次更新（官网注明） |
| 2026-08-11 | EquityBee Benchmark 登上 PH 第 3 名 |

## 评论区反馈（事实摘录，不评价）

- **Oren Barzilai（CEO）**：解释动机——公司方长期有基准，员工方没有市场参照；说明机制——9,000+ 已核验新员工期权覆盖 2,500+ 美国创业公司，按部门/职级/阶段生成对比组，返回 25/中位/75 分位和均值；强调"不是预测期权最终价值，而是给员工相关对比点"；明确"免费、专为创业公司员工而非 HR 团队设计"。
- **Gal Steinman（员工）**：称之为"the tool I wish existed years ago"，痛点是"我手里的授予到底怎么比？"，称 Benchmark 填补了这一空白。
- **Or Shemesh**：称之为"为创业公司员工拉平赛场的里程碑"，强调"用真实、已核验的数据帮助人们应对 offer letter 和股权谈判"。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/equitybee（拿到了 tagline、描述、Oren Barzilai / Gal Steinman / Or Shemesh 的评论全文、topics、Build tools 标签）
- 官网 Benchmark 页（PH 重定向目标）：https://equitybee.com/startup-equity-benchmark?ref=producthunt（拿到了数据规模 9,000+/2,500+、口径 FMV、免费声明、对比 Levels.fyi/Carta、办公地、EquityBee Securities FINRA 主体、其他业务线）
- CB Insights 公司档案：https://www.cbinsights.com/company/equitybee（拿到了累计融资 $83.1M、Series B-II、办公地、投资方、收购状态为"Alive 未被收购"）
- EquityBee About 页：https://www.equitybee.com/about（仅拿到页面标题，正文未渲染；Oren Barzilai 创始人身份来自搜索结果摘要）
- GitHub 组织：https://github.com/equitybee（4 个公开仓库：team-label-action、eslint-config-equitybee、branch-block-action、public-assets，均为内部开发工具，无产品代码开源）

## 未查到 / 待补

- 创始人除 Oren Barzilai 外的联合创始人名单（About 页正文未渲染，待直接抓 team 页或 LinkedIn）
- Series B 估值（未公开披露）
- 非追索权融资的具体费率/分成比例（未在公开页面披露）
- 用户提到的"2023 年被 Citadel 的 Equifax 收购"——多渠道搜索未获证据，CB Insights 仍标"Alive"，此说法**未核实，疑似错误**
- EquityBee Benchmark 是否对 EquityBee 主业务带来明显转化（未披露）
- Oren Barzilai 此前创办的其他产品（maker_previous 未查到）
- EquityBee 数据集中"已核验"的具体核验流程（未在公开页详述）
- 公司注册州与法律实体细节
