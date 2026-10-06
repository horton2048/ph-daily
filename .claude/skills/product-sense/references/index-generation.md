# Context 知识库索引生成规范

## 目标

将分散的 context 档案转化为可检索、可聚合、可发现趋势的 wiki 知识库。

## 索引结构

```
context/
├── YYYY-MM-DD-<slug>.md          # 原始档案（带 frontmatter）
├── INDEX.md                       # 主索引：所有产品按时间倒序
├── by-category/                   # 按品类聚合
│   ├── AI-agent.md
│   ├── developer-tools.md
│   └── ...
├── by-tech/                       # 按技术栈聚合
│   ├── MCP.md
│   ├── Claude.md
│   ├── open-source.md
│   └── ...
├── by-business/                   # 按商业模式聚合
│   ├── freemium.md
│   ├── open-source-free.md
│   └── ...
└── timeline/                      # 时间轴趋势
    ├── 2026-08.md                 # 8 月所有产品 + 趋势
    └── weekly/
        └── 2026-W32.md            # 本周趋势报告
```

## 索引页格式

### INDEX.md（主索引）

```markdown
# Product Hunt Context 档案索引

> 共 <N> 个产品 · 最后更新 <日期>

## 最近更新（按日期倒序）

### 2026-08-06（10 个产品）

1. [Cloudflare OS](2026-08-06-cloudflare-os.md) · 为公司构建 AI 操作系统 · AI 基础设施
2. [Muse Code](2026-08-06-muse-code.md) · Meta 长时程编码 agent · 开发者工具
...

### 2026-08-05（10 个产品）

1. [AdAnt AI](2026-08-05-adant-ai.md) · Claude 驱动的社交广告生成 · AI 营销工具
...

## 快速导航

- [按品类浏览](by-category/) · [按技术栈浏览](by-tech/) · [按商业模式浏览](by-business/)
- [时间轴趋势](timeline/)

## 统计

- AI agent: <N> 个
- 开发者工具: <N> 个
- 采用 MCP: <N> 个
- 开源产品: <N> 个
```

### by-category/AI-agent.md（品类索引）

```markdown
# AI Agent 产品档案

> 共 <N> 个 · 最后更新 <日期>

## 编码助手（<N> 个）

- [Muse Code](../2026-08-06-muse-code.md) · Meta 长时程编码 agent · 2026-08-06
- [Kiro Crew](../2026-08-05-kiro-crew.md) · 持久化智能体工作空间 · 2026-08-05

## 会议纪要（<N> 个）

- [Wispr Flow](../2026-08-05-wispr-flow.md) · 把细节做对的会议纪要 · 2026-08-05

## 趋势观察

<本品类的共性信号、进化方向>
```

### by-tech/MCP.md（技术栈索引）

```markdown
# 采用 MCP 协议的产品

> 共 <N> 个 · 最后更新 <日期>

## 产品列表（按时间倒序）

- [Brandfetch MCP](../2026-08-06-brandfetch-mcp.md) · 品牌资产 MCP 服务器 · 2026-08-06
- [BackEngine MCP](../2026-08-05-backengine-mcp.md) · 客户知识预处理 MCP · 2026-08-05
- [AdAnt AI](../2026-08-05-adant-ai.md) · 免费 MCP 插件接入 Claude Code · 2026-08-05

## 趋势

- 2026-08-04: 3 个 MCP 同日上榜（ZapDigits/GrowthBook/Atlaso）
- 2026-08-05: 2 个 MCP（AdAnt AI/BackEngine）
- 从"数据接入"卷到"领域知识预处理"
```

### timeline/2026-08.md（月度时间轴）

```markdown
# 2026 年 8 月 Product Hunt 产品时间轴

> 共 <N> 个产品 · 更新至 <日期>

## 本月趋势

1. **基础设施中间层战役**：网关/钱包/知识图/工作空间都在做"模型调不了"的那层
2. **MCP 协议成为标配**：从"能接 AI"到"预处理领域知识"
3. **持久化成为长任务前提**：会话即状态是原罪

## 按日产品

### 2026-08-06（10 个）

1. [Cloudflare OS](../2026-08-06-cloudflare-os.md) · AI 操作系统
2. [Muse Code](../2026-08-06-muse-code.md) · Meta 编码 agent
...

### 2026-08-05（10 个）

1. [AdAnt AI](../2026-08-05-adant-ai.md) · 社交广告生成
...

## 按品类统计

- AI agent: <N> 个
- 开发者工具: <N> 个
- SaaS: <N> 个

## 按技术统计

- MCP: <N> 个
- 开源: <N> 个
- 本地优先: <N> 个
```

## 索引生成时机

1. **每次扩展阅读后**：增量更新 INDEX.md（追加新产品）
2. **手动触发**：`/product-sense index` 重建所有索引
3. **每周日**：生成本周趋势报告（`timeline/weekly/YYYY-Wxx.md`）

## 实现方式

### 方案 A：纯 Markdown + 脚本

- 读取所有档案的 frontmatter
- 按分类/技术/时间聚合
- 生成 Markdown 索引文件
- 简单、轻量、git 友好

### 方案 B：SQLite + 生成器

- frontmatter 导入 SQLite
- SQL 查询聚合统计
- 生成 Markdown 索引
- 支持复杂查询，但引入依赖

**建议先用方案 A**，积累到 100+ 产品后再考虑 B。

## 双向链接规范

在档案正文中提到其他产品时，自动转为链接：

```markdown
**差异化点**：类似 [copy.ai](2026-07-15-copy-ai.md) 但专注社交广告。
```

实现：
1. 写档案时手动加 `[[产品名]]` 占位符
2. 索引生成时替换为实际路径
3. 或者不做自动替换，直接用相对路径手写

## 搜索接口（可选）

```bash
# 简单版：grep + awk
./search.sh "MCP 协议"

# 输出
context/2026-08-05-backengine-mcp.md:23: 通过 MCP 协议暴露给 Claude
context/2026-08-06-brandfetch-mcp.md:15: 实现为 MCP 服务器
```

## 下一步

1. 先改一个档案（如 AdAnt AI）加上 frontmatter，验证格式
2. 写索引生成脚本（Python/Node/Shell 都可以）
3. 更新 SKILL.md：扩展阅读步骤增加"填写 frontmatter"
4. 手动 backfill 现有档案的 frontmatter
5. 自动化：每次扩展阅读后自动更新索引

要我先写索引生成脚本吗？
