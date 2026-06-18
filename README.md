# ph-daily — Product Hunt 每日热门日报

每天 09:30(本机计划任务)拉取 Product Hunt 当日 Top 10 热门产品 →
LLM(Agnes AI)生成中文 tagline + 一句话点评 → 推 Slack 富卡片 + 落本地 Markdown 归档。

## 架构(及为什么这么选)

- **数据源:Product Hunt 官方 V2 GraphQL API**。V1 REST 已于 2023 关停;爬虫违反 ToS 且易碎。
  Developer Token 免费、只读、不过期。注意默认仅限非商用。
- **时区:按太平洋时间(PT)日界取榜**。PH 的"今日榜"按 PT 0 点结算;脚本用显式
  `postedAfter/postedBefore`,不依赖 API 隐式 today。北京 09:30 跑时 PT 约前一日傍晚,
  当日榜已有大半天数据。产品太少时自动回退前一 PT 日。
- **点评:Agnes AI 网关 `agnes-2.0-flash`**(OpenAI 兼容、免费、非推理无 `<think>`、~1s)。
  不用 `response_format`(实测不可靠),裸 JSON + 防御性解析(剥 `<think>`/围栏)+ 失败重试 3 次;
  强约束简体中文。点评失败自动降级为纯英文,日报照发。provider 由 config 的 `llm_*` 字段决定。
- **调度:本机 Windows 计划任务**。云端托管 routine 碰不到本地盘、headless 也拿不到
  Slack OAuth,故选本机。Slack 用 Incoming Webhook(比复用 MCP token 稳)。
- **归档双格式,MD 给 AI、HTML 给人**。同一份数据同时落 `.md` 和 `.html`:Markdown
  标记即语义、token 开销小,适合喂模型 / 检索分析;HTML 带样式、可点链接,适合人看与分享。
  要让 AI 读历史日报时,优先喂 `.md` 而非 `.html`。

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

```powershell
copy config.example.json config.json   # 然后填入上面三处凭据
```

### 5. 注册计划任务
```powershell
cd C:\Users\huang\projects\ph-daily
powershell -ExecutionPolicy Bypass -File .\setup_task.ps1
```

## 手动测试 / 运行

```powershell
uv run ph_daily.py --dry-run        # 抓取 + 点评 + 落 MD,不推 Slack(预览)
uv run ph_daily.py                  # 完整跑一次(含 Slack)
uv run ph_daily.py --date 2026-06-01  # 取指定 PT 日
uv run ph_daily.py --no-zh          # 跳过中文点评(省一次 LLM 调用)

Start-ScheduledTask -TaskName "PH-Daily-Digest"   # 触发计划任务
Get-ScheduledTaskInfo -TaskName "PH-Daily-Digest" # 看下次运行/上次结果
```

## 文件
- `ph_daily.py` — 主脚本(零三方依赖,仅 tzdata)
- `config.json` — 凭据(**含密钥,勿提交/分享**)
- `run.ps1` — UTF-8 包装 + 日志,计划任务调用此脚本
- `setup_task.ps1` — 注册/更新计划任务
- `archive/YYYY-MM-DD.md` — 每日归档(Markdown,给 AI / 检索)
- `archive/YYYY-MM-DD.html` — 每日归档(HTML,给人看 / 分享)
- `logs/YYYY-MM-DD.log` — 每日运行日志

## 排错
- **PH 403/401**:token 没填或失效 → 重新生成。
- **PH 返回空**:可能 PT 当日刚开始,加 `--date` 指定昨天试试。
- **Slack 没收到**:webhook URL 错或频道被移除 → 重建 webhook。日志看 `logs\`。
- **点评是英文/葡语**:日志看 LLM 是否报错降级(`[warn] LLM 点评…失败`);模型/网关由 `config.json` 的 `llm_*` 字段决定,默认 Agnes `agnes-2.0-flash`。
- **限流**:PH 6250 复杂度/15 分钟,每天一次远没问题。
