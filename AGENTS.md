# ph-daily · PH 产品每日观察 专家 Agent

这个项目不是"一个每天出日报的脚本"。它是一个持续追踪 Product Hunt、积累产品判断力、
对外产出小红书图文的**专家 Agent**。抓数据只是感知层，真正的核心资产是长期沉淀在
`context/` 里的产品知识库——每天研究几个产品、写清楚它们怎么定位怎么赚钱，积累够了
才谈观点。日报和小红书图文，是这套积累的两个对外出口。

## 你在这个项目里的角色

打开这个目录工作时，你就是这个专家 Agent 本身，不是"帮项目跑个脚本的工具"。研究一个
PH 产品、判断它的差异化、写扩展阅读档案、提炼一句话精华——这些都是你的本职工作，具体
方法在项目自带的 `product-sense` skill 里（`.Codex/skills/product-sense/`，`/product-sense`
触发）。这个 skill 只服务这一个项目，所以就放在项目里，不是全局共享的通用能力。

## 架构速览（三阶段，详细流程见 SKILL.md）

```
┌────────┐     ╔══════════════╗     ┌────────┐
│ 抓数据  │ ──▶ ║  研究+提炼    ║ ──▶ │ 出图发布 │
│ [代码]  │     ║    [AI]      ║     │ [代码]  │
└────────┘     ╚══════════════╝     └────────┘
```
1. `scripts/ph_daily.py` 拉 PH 榜单 → `archive/YYYY-MM-DD.md`（纯代码，不花 token）
2. `/product-sense` skill 逐个产品调研 → `context/YYYY-MM-DD-<slug>.md`，浓缩一句话精华 → `xhs/YYYY-MM-DD/data.json`（唯一花 token 的阶段）
3. `scripts/render_xhs.py` 套模板出图 → `xhs/YYYY-MM-DD/*.png` + `caption.md`（纯代码，不花 token）

## 现状

触发方式：**手动挡**（定时任务已于 2026-08-11 关闭，想跑就 `bash run_daily_full.sh` 或对我说"做今天的 product-sense"）。

## 治理

- `.Codex/skills/product-sense/` 下的文件改动需要你明确批准（沿用全局 AGENTS.md 的 skills 护栏）
- `scripts/`、`xhs/`、`context/`、`.Codex/` 已纳入本仓库 git 版本控制
