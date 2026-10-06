# ph-daily — PH 产品每日观察 专家 Agent

每天拉取 Product Hunt 当日 Top 10 热门产品 → 落本地 Markdown 归档；再由 Agent 按
`product-sense` skill 逐个深挖，沉淀成 `context/` 知识库，出小红书图文。完整架构见
项目根的 `CLAUDE.md`。

目录地图见 [`PROJECT_STRUCTURE.md`](PROJECT_STRUCTURE.md)。

## 架构(及为什么这么选)

- **数据源:Product Hunt 官方 V2 GraphQL API**。V1 REST 已于 2023 关停;爬虫违反 ToS 且易碎。
  Developer Token 免费、只读、不过期。注意默认仅限非商用。
- **时区:按太平洋时间(PT)日界取榜**。PH 的"今日榜"按 PT 0 点结算;脚本用显式
  `postedAfter/postedBefore`,不依赖 API 隐式 today。产品太少时自动回退前一 PT 日。
- **文案:由 Agent 按 `.claude/skills/product-sense` 撰写**。脚本只负责抓数据与渲染，
  不再内置调用任何 LLM 网关；中文点评 / 小红书文案在 Muse 等环境里由 Agent 写。
- **调度:手动挡**。之前用 macOS launchd 每天定时跑,已于 2026-08-11 关闭;现在想跑就手动
  `bash run_daily_full.sh`（只跑抓数+归档）或对 Agent 说"做今天的 product-sense"。
- **归档只留 Markdown**。之前同时落 `.md`/`.html` 两份,HTML 那份没人看,2026-08-12 起
  只产出 `.md`(给 AI 读 / 检索用,token 开销也小)。

## 一次性配置

### 1. Product Hunt Developer Token(~2 分钟)
1. 登录 → https://www.producthunt.com/v2/oauth/applications
2. "Add an application",名字随意,Redirect URI 随便填(如 `https://example.com`)
3. 创建后在应用页面底部找到 **Developer Token**,复制
4. 粘进 `config.json` 的 `ph_token`

### 2. Slack Incoming Webhook（可选）
1. https://api.slack.com/apps → Create New App → From scratch,选你的 workspace
2. 左侧 "Incoming Webhooks" → 打开 → "Add New Webhook to Workspace" → 选目标频道
3. 复制形如 `https://hooks.slack.com/services/T.../B.../xxx` 的 URL
4. 粘进 `config.json` 的 `slack_webhook_url`（不填则只落 MD、不推 Slack）

### 3. 生成 config.json

```bash
cp config.example.json config.json   # 填入 ph_token（必需）; top_n 默认 10
```

`config.json` 只需 **`ph_token`**（和可选的 `top_n` / `slack_webhook_url`）。文案由 Agent
遵循 `.claude/skills/product-sense` 完成，不需要任何 `llm_*` 密钥。

## 手动测试 / 运行

```bash
uv run scripts/ph_daily.py --dry-run          # 抓取 + 落 MD,不推 Slack(预览)
uv run scripts/ph_daily.py                    # 完整跑一次(含 Slack，若已配置)
uv run scripts/ph_daily.py --date 2026-06-01  # 取指定 PT 日

bash run_daily_full.sh                # 阶段1: 抓数据+归档；阶段2交给 Agent（product-sense）
```

## 文件
- `scripts/ph_daily.py` — 主脚本(零三方依赖,仅 tzdata；只抓 PH + 渲染)
- `scripts/render_xhs.py` — 小红书图片渲染脚本
- `scripts/_retired/` — 已停用的历史脚本，仅供追溯
- `config.json` — 凭据(**含密钥,勿提交/分享**)
- `run_daily_full.sh` — 手动跑阶段1（抓数+归档）；文案由 Agent 写
- `archive/YYYY-MM-DD.md` — 每日归档(Markdown,给 AI / 检索)
- `logs/YYYY-MM-DD.log` — 每日运行日志
- `.claude/skills/product-sense/` — 本项目唯一 Skill：深挖产品 + 出小红书图
- `data/raw/product-hunt/` — PH API 原始响应和调试快照，不是业务入口

## 排错
- **PH 403/401**:token 没填或失效 → 重新生成。
- **PH 返回空**:可能 PT 当日刚开始,加 `--date` 指定昨天试试。
- **Slack 没收到**:webhook URL 错或频道被移除 → 重建 webhook。日志看 `logs/`。
- **限流**:PH 6250 复杂度/15 分钟,每天一次远没问题。
- **需要中文文案 / 信息图**:对 Agent 说"做今天的 product-sense"，按 skill 执行；脚本侧不再调模型。
