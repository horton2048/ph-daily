# ph-daily — PH 产品每日观察 专家 Agent

每天拉取 Product Hunt 当日 Top 10 热门产品 → LLM 生成中文 tagline + 一句话点评 →
落本地 Markdown 归档；再由 Claude Code 的 `product-sense` skill 逐个深挖，沉淀成
`context/` 知识库，出小红书图文。完整架构见项目根的 `CLAUDE.md`。

目录地图见 [`PROJECT_STRUCTURE.md`](PROJECT_STRUCTURE.md)。

## 架构(及为什么这么选)

- **数据源:Product Hunt 官方 V2 GraphQL API**。V1 REST 已于 2023 关停;爬虫违反 ToS 且易碎。
  Developer Token 免费、只读、不过期。注意默认仅限非商用。
- **时区:按太平洋时间(PT)日界取榜**。PH 的"今日榜"按 PT 0 点结算;脚本用显式
  `postedAfter/postedBefore`,不依赖 API 隐式 today。产品太少时自动回退前一 PT 日。
- **点评:Agnes AI 网关 `agnes-2.0-flash`**(OpenAI 兼容、免费、非推理无 `<think>`、~1s)。
  不用 `response_format`(实测不可靠),裸 JSON + 防御性解析(剥 `<think>`/围栏)+ 失败重试 3 次;
  强约束简体中文。点评失败自动降级为纯英文,日报照发。provider 由 config 的 `llm_*` 字段决定。
- **调度:手动挡**。之前用 macOS launchd 每天定时跑,已于 2026-08-11 关闭;现在想跑就手动
  `bash run_daily_full.sh` 或对 Codex 说"做今天的 product-sense"。
- **归档只留 Markdown**。之前同时落 `.md`/`.html` 两份,HTML 那份没人看,2026-08-12 起
  只产出 `.md`(给 AI 读 / 检索用,token 开销也小)。

## 一次性配置

### 1. Product Hunt Developer Token(~2 分钟)
1. 登录 → https://www.producthunt.com/v2/oauth/applications
2. "Add an application",名字随意,Redirect URI 随便填(如 `https://example.com`)
3. 创建后在应用页面底部找到 **Developer Token**,复制
4. 粘进 `config.json` 的 `ph_token`

### 2. Slack Incoming Webhook(~2 分钟)
1. https://api.slack.com/apps → Create New App → From scratch,选你的 workspace
2. 左侧 "Incoming Webhooks" → 打开 → "Add New Webhook to Workspace" → 选目标频道
3. 复制形如 `https://hooks.slack.com/services/T.../B.../xxx` 的 URL
4. 粘进 `config.json` 的 `slack_webhook_url`

### 3. LLM 网关 key

`config.example.json` 已预填 Agnes AI 免费网关的 `llm_base_url` / `llm_model`,只需把你自己的 `llm_api_key` 填进 `config.json`(点评失败会自动降级为纯英文,不填也能跑,只是没中文点评)。

### 4. 生成 config.json

```bash
cp config.example.json config.json   # 然后填入上面三处凭据
```

## 手动测试 / 运行

```bash
uv run scripts/ph_daily.py --dry-run          # 抓取 + 点评 + 落 MD,不推 Slack(预览)
uv run scripts/ph_daily.py                    # 完整跑一次(含 Slack)
uv run scripts/ph_daily.py --date 2026-06-01  # 取指定 PT 日
uv run scripts/ph_daily.py --no-zh            # 跳过中文点评(省一次 LLM 调用)

bash run_daily_full.sh                # 完整流程:抓数据 + Top 10 调研 + 10 张图 + 发布文案
bash run_daily_full.sh --check        # 只检查 Codex CLI 是否存在且已登录
```

## 文件
- `scripts/ph_daily.py` — 主脚本(零三方依赖,仅 tzdata)
- `scripts/render_xhs.py` — 小红书图片渲染脚本
- `scripts/_retired/` — 已停用的历史脚本，仅供追溯
- `config.json` — 凭据(**含密钥,勿提交/分享**)
- `run_daily_full.sh` — 手动跑完整流程用(以前由 launchd 定时触发,现已关闭)
- `archive/YYYY-MM-DD.md` — 每日归档(Markdown,给 AI / 检索)
- `logs/YYYY-MM-DD.log` — 每日运行日志
- `.claude/skills/product-sense/` — 本项目唯一 Skill：深挖产品 + 出小红书图
- `data/raw/product-hunt/` — PH API 原始响应和调试快照，不是业务入口

## 排错
- **PH 403/401**:token 没填或失效 → 重新生成。
- **PH 返回空**:可能 PT 当日刚开始,加 `--date` 指定昨天试试。
- **Slack 没收到**:webhook URL 错或频道被移除 → 重建 webhook。日志看 `logs/`。
- **点评是英文/葡语**:日志看 LLM 是否报错降级(`[warn] LLM 点评…失败`);模型/网关由 `config.json` 的 `llm_*` 字段决定,默认 Agnes `agnes-2.0-flash`。
- **限流**:PH 6250 复杂度/15 分钟,每天一次远没问题。
- **研究阶段启动失败**:先跑 `bash run_daily_full.sh --check`;脚本优先使用桌面 App 内置 Codex CLI 和 ChatGPT 登录态，不再依赖 Claude 网关余额。
