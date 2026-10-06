---
# 结构化元数据（用于索引和聚合）
product: "Supabase RLS Leak Demo"
slug: "supabase-rls-leak-demo"
date: "2026-08-08"
rank: 9
votes: 0
comments: 1

# 分类标签
category: "开发者工具"
subcategory: "安全测试夹具 / RLS 审计"
tags: ["开源", "MIT", "Supabase", "Postgres", "安全", "RLS", "测试"]

# 技术信息
tech_stack: ["TypeScript", "Vitest", "PGlite", "Postgres", "SQL", "GitHub Actions"]
platform: ["Web", "CLI"]
open_source: true
license: "MIT"

# 商业信息
business_model: "开源免费 + 配套付费审计服务"
pricing_start: "免费（开源）；审计服务 $99 起"
funding_stage: "未融资"
funding_amount: ""

# 关联信息
related_products: ["Supabase", "pg_timetable", "Row Level Security"]
maker_previous: []

# 元信息
archived_at: "2026-08-08"
sources_count: 2
---

# Supabase RLS Leak Demo · 扩展阅读上下文

> PT 2026-08-08 Product Hunt 榜单第 9 名 · 👍 票数未知 · 💬 1（仅 maker launch 评论）
> 归档日期 2026-08-08 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Supabase RLS Leak Demo |
| 英文 tagline | Reproduce a cross-tenant RLS leak and verify the fix |
| 中文 tagline | 复现跨租户 RLS 泄露，并验证修复 |
| 官网 | https://github.com/cekuu35/supabase-rls-leak-demo |
| PH 页 | https://www.producthunt.com/products/supabase-rls-leak-demo |
| PH launch post | https://www.producthunt.com/posts/supabase-rls-leak-demo |
| GitHub | https://github.com/cekuu35/supabase-rls-leak-demo（MIT，28 commits，捕获时 0 stars/forks） |
| 品类标签 | Open Source · Developer Tools · GitHub |
| 票数 / 评论 | 票数未知；评论 1（maker 仅一条）；2 followers |
| 公司主体 | 无公司实体（独立开发者项目） |
| 企业版/关联站点 | Gumroad 审计服务（gumroad.com/l/supabase-rls-3-table-review） |
| Maker | Cenk KURTOĞLU（PH @cekuu35，X @kurtoglucenk1） |

## 是做什么的（如实复述，不评价）

一个可本地运行的 Supabase/Postgres 安全测试夹具：证明"一条 RLS 策略看起来正确、却仍会跨租户泄漏行"。同一套测试在 broken 分支跑红、在 fixed 分支跑绿，唯一差异是一个 SQL 文件。`npm ci && npm test` 即可跑，"无需 Docker、云项目、凭据或生产数据"。面向"想在发布多租户应用前拿到证据的创始人和开发者"。

## 解决什么问题（事实层面，不判断值不值得解）

- 团队把"开了 RLS"当成租户隔离已成立的证明（maker 原话："它并不是"）
- 策略可能通过 happy-path 检查，却因关系/归属条件漏出另一个租户的行
- 提供一个 maker 认可的最小证明标准：同租户访问成功、跨租户读返回 0 行、跨租户写改 0 行、断言在**应用角色**（而非 admin 角色）下运行

## 怎么做的（技术原理/机制，事实层面）

- **运行方式**：PGlite 进程内 Postgres 跑本地测试，无需 Supabase 项目/凭据/Docker/生产数据；TypeScript + Vitest；GitHub Actions CI、ESLint、vitest.config.ts
- **分支与单文件修复**：`broken` 与 `fixed` 共用逐字节相同的测试套件，唯一差异是 `db/policies.sql`（启用 RLS + 为 SELECT/INSERT/UPDATE/DELETE 加四条策略）；需适配真实应用的授权模型
- **测试逻辑**（`tests/isolation.test.ts`，两分支逐字节相同）：设置合成 JWT subject claim → 切到 `authenticated` 数据库角色 → 查询全部 `public.notes` → 断言不返回属主 A 的行；同时断言 B 仍能读自己的行（防止 `revoke all` 靠"全禁"糊弄过关）
- **测试结果**：broken = 4 failed / 1 passed；fixed = 5 passed；隔离失败信息示例："user B received 1 row(s) belonging to another user: ["A: card ending 4471, expiry 09/29"]"（合成种子数据，非真实卡）
- **复现的泄漏模式**：认证角色拥有表权限、而表缺少策略文件时，跨用户行被返回。README 列出三种值得检查的配置：①表从未启用 RLS；②RLS 已启用但无匹配策略（Postgres 默认 deny）；③存在策略但 RLS 根本没开（策略不生效）。强调 RLS 只是行级闸门，grant 与 API/schema 暴露是围绕它的另外两层闸门
- **附带资源**：`audit/rls-audit.sql`（9 条只读目录查询：RLS 覆盖、带角色策略、写检查缺口、grant、SECURITY DEFINER 函数、owner bypass、auth.uid() 使用、BEGIN…ROLLBACK 角色模拟测试台）、`RLS_TEST_MATRIX.md`（可复制的负向测试矩阵）、`SAMPLE_AUDIT_REPORT.md`（合成样例审计报告）
- **免责声明**：明说"不模拟 Supabase Auth、PostgREST、Data API 暴露、网络控制或生产配置"，结果只证明该夹具的数据库级行为；也不是对任何具名 AI/无代码工具的导出或证据；README 标注"AI 辅助 + 人工审阅"，commit trailer 中的模型标签"未经独立验证，不应视为模型证明"

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Cenk KURTOĞLU（独立开发者） | PH + GitHub |
| 融资 | 未融资（独立项目） | — |
| 投资方 | 未查到 | — |
| 加速器 | 未查到 | — |
| 合规认证 | 未查到 | — |
| 商业产品 | RLS Audit Kit（$29）、固定价 Supabase RLS 安全审计（$99 起）、2 页 launch 检查清单 PDF（$1） | GitHub README + PH 评论 |

## 定价 / 商业模式

- **开源免费**：MIT 协议
- **商业补充**（maker 个人服务）：launch 特惠 = 固定范围 24 小时审查 3 张敏感表，共 $15.20（$7.60 定金），经 Gumroad
- 模式：开源免费 + 配套付费审计服务

## 关联信息 / 生态

- 面向 Supabase/Postgres 多租户应用开发者的安全验证工具；与 Supabase RLS、Postgres 安全体系直接相关
- PH 论坛帖（1d 前）："什么样最小的测试能让你信任一条 RLS 策略？"（0 回复）

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-08-08 | PH 上线（maker 评论与论坛帖约 1 天前发布） |

## 评论区反馈（事实摘录，不评价）

- Maker Cenk（1d 前）："我是在看到团队把'RLS 已启用'当成租户隔离已成立的证明之后做的这个。它不是。"；邀请社区建议应覆盖的泄漏模式
- Maker 论坛帖：失败模式 = "用户 A 通过 permissive 关系或缺失归属条件，能读/改属于租户 B 的行"
- 无用户评论

## 信息来源

- PH 产品页 + PH launch post + 论坛帖：tagline、maker 评论、Gumroad 特惠、论坛讨论
- GitHub repo（README）：描述、测试逻辑与结果、分支结构、附带资源、license、免责声明

## 未查到 / 待补

- 票数（archive 与 PH 页面抓取均未显示）
- Maker 公开背景/公司（仅 PH + GitHub 身份）
- 任何独立报道/第三方验证（未检索到）
- 该夹具是否被实际项目采用（捕获时 0 stars/forks）
