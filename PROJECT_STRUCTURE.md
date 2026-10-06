# 项目结构

这个项目按“入口 → 数据 → 研究 → 输出”组织。根目录只放项目说明、配置和启动入口。

```text
ph-daily/
├── README.md                 使用说明与常用命令
├── PROJECT_STRUCTURE.md      本文件：目录地图
├── AGENTS.md / CLAUDE.md     Agent 工作约定
├── config.example.json       配置模板
├── config.json               本机密钥（不提交）
├── run_daily_full.sh         阶段1：抓数+归档（文案由 Agent / product-sense）
├── scripts/                  可执行代码
│   ├── ph_daily.py           抓取 PH 榜单、生成日报（不调 LLM）
│   ├── render_xhs.py         渲染小红书图片
│   ├── generate_index.py     生成知识库索引
│   ├── check_logo.py         检查产品 Logo
│   ├── test_smoke.py         冒烟测试
│   └── _retired/             已停用脚本，仅供追溯
├── .claude/skills/           本项目唯一 Skill
│   └── product-sense/        产品研究与小红书内容生产规范
├── data/raw/product-hunt/    PH API 原始响应与调试快照
├── archive/                  每日 Product Hunt 榜单归档
├── research/                 产品调研来源与编辑稿
├── context/                  长期产品知识库与分类索引
└── xhs/                      按日期保存的小红书图文成品
```

找东西时：要运行代码看 `scripts/`；要看 Skill 看 `.claude/skills/product-sense/`；要看原始抓取响应看 `data/raw/product-hunt/`；要看研究结论看 `context/`；要看发布图片看 `xhs/`。
