---
name: product-sense
description: >
  为 Product Hunt 每日上榜产品做扩展阅读，构建如实详细可信的结构化上下文档案，
  并产出完整小红书发布包（Top 10 信息图和文案）。手动调用：想深度了解某天某产品、做小红书图文、
  或积累产品 sense 时触发。触发词包括"产品 sense""扩展阅读""上下文档案""小红书信息图""/product-sense"。
  前提是 ph-daily 数据层已就绪（archive/YYYY-MM-DD.md 存在）。
metadata:
  version: "0.8"
  date: "2026-09-29"
---

# product-sense · 扩展阅读与信息图

ph-daily 数据层只给"上榜了什么"（名字/tagline/票数）。本 skill 负责**从原始榜单到一条完整小红书帖**的全流程：

1. **扩展阅读**：对每个上榜产品，从多源（官网/PH页/公开报道/GitHub）抓事实，构建**如实详细可信**的结构化上下文档案。
2. **小红书信息图**：从档案里挑一条最强信号，浓缩成"品类定位 + 一句话精华"，套 cream-glass 风格模板出一张 3:4 高清 PNG。
3. **发布打包**：全部产品出图后，按排名命名图片 + 配文案（榜一一句话洞察 + 5 个话题），汇总到 `xhs/YYYY-MM-DD/` 一键直发。

**默认交付范围**：用户说“开工”“做今天的 product-sense”或指定日期时，当次完成该日 Top 10 的 `context` 档案、`data.json`、10 张 PNG 和 `caption.md`。不要只交首图，也不要把文案留到用户追问。已有合格文件可复用；若用户明确只要求单个产品，才缩小范围。

> 设计哲学：先建上下文，再谈观点。没有积累时硬逼观点只会得到"听起来像洞察的转述"。
> 这个阶段产出的是**事实档案**，不是洞察报告。等产品 sense 积累够了，再提炼观点。

## 调用方式

```
/product-sense                      # 取最新一天的 archive，完成 Top 10 档案 + 10 张信息图 + caption.md
/product-sense 2026-07-31           # 指定某天
/product-sense 2026-07-31 halo      # 用户明确只做单个产品时使用
```

### 手动运行完整流程

定时任务已关闭。用户手动运行 `bash run_daily_full.sh` 或在对话中调用本 skill 时：
1. `ph_daily.py` 取数据并归档 Markdown；归档已存在时可复用。
2. 对当天 Top 10 逐一研究并写档案，再为全部 10 个产品写 `data.json` 条目、渲染 10 张信息图、生成 `caption.md`。
3. 缺少某个官网或具体事实时，在档案中标明“未查到/待补”，以已核实内容完成对应信息图和文案，不因此省略整张图或整份发布文案。

重跑同一日期时，复用已有合格档案和图片，补齐缺失项；发现 logo 或文案错误，只重渲相应图片。不要把“先出 #1 张，等确认再补 9 张”作为默认流程。

## 工作流

### 1. 取数据
读 `~/Projects/ph-daily/archive/YYYY-MM-DD.md` 拿上榜产品列表。缺省日期用 `ls -t` 取最新。文件不存在则告诉用户有哪些天可选，停。

### 2. 扩展阅读（每个产品）
对每个产品（或指定产品），从 4 类源抓事实。源：

- **产品官网**：About / Pricing / 产品页 → 团队、融资、定价、技术原理、里程碑
- **PH 产品页**：`producthunt.com/products/<slug>` → 创始人评论（常含技术细节和用户反馈）、产品描述
- **公开报道**：搜索引擎查融资新闻、创始人背景
- **GitHub**：`github.com/<org>` 查开源仓库、技术栈——**只在有开源信号时才查**（官网/PH 页提到
  open source、MIT/Apache 协议、GitHub 徽章或链接）。没信号就不查，直接记"未见开源信号，未查
  GitHub"；不要对大概率闭源的 SaaS 逐个跑一遍必然 404 的请求。

**先摘要、后全文，省无谓的整页抓取**：每类源先用 WebSearch 摘要判断能不能直接拿到要填的事实；
摘要不够用（定价细节、评论区原文、团队页这类需要原文的）才用 ego-browser（继承登录态，能过
PH/微信风控）开页面抓全文。不要不看摘要就四类源一律先开全文。

抓不到的事实**明确写"未查到/待补"**，绝不编造。

### 3. 结构化上下文档案（Markdown + frontmatter）

按 `references/context-template-v2.md` 的字段填写，写到 `~/Projects/ph-daily/context/YYYY-MM-DD-<slug>.md`。

**两部分内容**：
1. **frontmatter（YAML）**：结构化元数据，用于知识库索引和聚合
   - 基本信息：产品名/日期/排名/票数/评论数
   - 分类标签：category/subcategory/tags
   - 技术信息：tech_stack/platform/open_source/license
   - 商业信息：business_model/pricing_start/funding_stage
   - 关联信息：related_products/maker_previous
2. **正文（Markdown）**：详细事实档案，原则不变：如实、详细、可信、结构化

**填写 frontmatter 指南**：
- `category`：AI agent / 开发者工具 / AI 营销工具 / SaaS / 消费级应用
- `tags`：特征标签数组，如 `["MCP", "开源", "Claude", "本地优先"]`
- `tech_stack`：技术栈数组，如 `["Python", "Claude API", "Electron"]`
- `business_model`：Freemium / 订阅制 / 一次性买断 / 开源免费 / 企业定制
- `pricing_start`：起步价，如 `"$9/月"` / `"免费"` / `"未披露"`
- `related_products`：竞品或互补品数组，如 `["copy.ai", "jasper.ai"]`
- `key_signals`：2-4 条最值得记住的事实，写正文时顺手摘，供 caption.md/INDEX.md 等下游省 token 复用（不用整篇重读正文）

### 3.5. 更新知识库索引

每次完成扩展阅读后，运行索引生成器：
```bash
python3 ~/Projects/ph-daily/scripts/generate_index.py
```

这会自动更新：
- `context/INDEX.md`（主索引，按日期倒序）
- `context/by-category/*.md`（按品类聚合）
- `context/by-tech/*.md`（按技术栈/标签聚合）
- `context/by-business/*.md`（按商业模式聚合）
- `context/timeline/YYYY-MM.md`（月度时间轴）

索引让 context 从"写了就忘的档案馆"变成"可检索、可聚合、可发现趋势的知识库"。

### 4. 浓缩为一句话精华

不再拆 6 个锚点，只从档案里**挑一条信息增量最大的事实**，浓缩成两个字段（方法详见
`references/framework.md`）：
1. **定位**（`sub`）：品类 + 形态，4-10 字，回答"这是什么"
2. **一句话精华**（`one_liner`）：背景/对比半句 + `<b>` 加粗的核心亮点（4-10 字）+ `<br>` +
   补充半句（数据/机制/差异化），回答"凭什么值得记住"

优先从 frontmatter 的 `key_signals`（写档案时已经摘好的 2-4 条精炼信号）里选，不用重新通读正文。

### 5. 小红书信息图（一句话精华 → data.json → 统一渲染脚本出图）

CSS/HTML 骨架只活在 `references/xhs-template.html` 里（cream-glass 版式：品牌线 + 玻璃质感
logo + 产品名 + 定位 + 一句话精华 + 票数），**Claude 不现场生成整份 HTML**——只把定位和一句话
精华整理成 `xhs/YYYY-MM-DD/data.json`，渲染交给 `scripts/render_xhs.py`（占位符替换 + logo
下载规范化 + Chrome headless 截图，纯确定性执行，不需要 LLM）。

**data.json 结构**（`products` 数组，一个产品一条）：
```json
{
  "date": "YYYY-MM-DD",
  "products": [
    {
      "rank": 1, "slug": "<slug>", "name": "<产品名>", "votes": <票数>,
      "logo_url": "<优先取 archive/YYYY-MM-DD.md 的 `🖼️ logo:`，核对内容；无效时换已核实的产品或品牌标识，仍无可用标识才留 null>",
      "sub": "<定位：品类+形态，4-10字>",
      "one_liner": "<背景半句+<b>核心亮点</b>+<br>+补充半句>"
    }
  ]
}
```

**渲染**（一次跑完当天全部产品）：
```bash
python3 ~/Projects/ph-daily/scripts/render_xhs.py xhs/YYYY-MM-DD/data.json
```
HTML 落 `xhs/YYYY-MM-DD/temp_html/`（留底不删，8-06 事故教训，见 memory:
xhs-infographic-html-preservation）、PNG 落 `xhs/YYYY-MM-DD/`。
logo 下载失败（404/SVG/超时）自动退化成纯色圆角块+首字母，
不中断整批渲染。

- 改完某个产品的文案想单独重渲一张（不用整批重来）：`--only <slug>` 重跑同一条命令
- 产品 logo：先用 archive.md 的 `🖼️ logo:` 行；渲染前核对它确实是该产品或所属品牌的标识。若链接失效或缩略图不是 logo，去产品官网或 PH 产品主页找品牌标识；不要用发布配图、截图代替 logo。没有单独产品标识时用所属品牌标识。候选标识仍无法核实时，使用首字母占位并说明。
- 严格遵守小红书合规规范（见下）

### 6. 美观性审查（写 data.json 时必须过一遍）

写 `data.json` 时、跑渲染脚本前审查：

- `sub` ≤ 10 字，不然会跟 `.sub` 的宽字间距（letter-spacing:3px）挤在一起换行
- `one_liner` 两行合计 ≤ 28 字（不含标点），单行装不下会被 `max-width:290px` 挤成三行、显拥挤
- `<b>` 只包一个核心短语（4-10 字），不要整句加粗——加粗是为了一眼抓重点，不是强调全部
- logo 正常应优先从 archive.md 的 `🖼️ logo:` 行取得，但需确认其内容与产品一致；链接损坏或图像内容不符时按上文查找品牌标识。只有可核实的标识都不可用时才留 `null`，退化成纯色块+首字母。

**每张单图渲染完做文件级检查**（尺寸、命名、文字是否溢出）；发现问题只改那一条 data.json 记录，
`render_xhs.py ... --only <slug>` 重渲一张，不用整批重来。

## 小红书合规规范（信息图必须守）

- ❌ **禁止外链**：正文和底栏都不放 URL（`scam.ai`、`producthunt.com` 等）。底栏用"来源：Product Hunt 每日榜"代替。
- ❌ 禁止引流话术（关注/私信/加V/加群）
- ❌ 禁止联系方式（电话/微信/二维码）
- ⚠️ 绝对数值（如"98.2% 准确率"）加"官方称"前缀更稳；事实数据陈述可保留，但不要包装成营销承诺
- ❌ 禁止绝对化夸大用语（最/第一/100% 保证）
- ❌ 禁止诱导互动（点赞收藏转发）

### 7. 打包发布（全量产出后汇总）

所有产品都渲染完 PNG 后，把图片和文案汇总到一个发布文件夹，方便直接拖到小红书：

```
~/Projects/ph-daily/xhs/YYYY-MM-DD/
├── 01-<slug>.png      # 按排名序号命名
├── 02-<slug>.png
├── ...
├── 10-<slug>.png
└── caption.md         # 榜一一句话洞察 + 5 个话题
```

**图片命名**：`<排名序号>-<slug>.png`（如 `01-zinley.png`），序号补零两位。

**文案 `caption.md`** 生成规范详见 `references/copy-guideline.md`，包含两部分：
1. **一句话洞察**：关于今天的产品趋势，说一句最具产品 sense 的话，三十个字以内，语气像推特、贴吧、即刻上的帖子，一眼看上去性感、非主流。
2. **话题标签**：固定 5 个，不是 10 个。格式仍是一行 `#话题`，用空格分开。

**不要产品排名列表**：图片已展示产品细节。文案只写榜一这一句，不逐个介绍其余产品。

**文案写作流程**：
1. 读当天榜一，对照 `context/` 和 `archive/`，关于今天的产品趋势，说一句最具产品 sense 的话，三十个字以内，语气像推特、贴吧、即刻上的帖子，一眼看上去性感、非主流
2. 配 5 个话题标签
3. 输出到 `xhs/YYYY-MM-DD/caption.md`（仅这一句 + 分隔线 + 5 个话题，纯文本）

**交付前逐项核对**：当天 Top 10 的 10 份 context 档案、`data.json` 中 10 条完整记录、对应的 10 张可打开的 1500×2000 PNG、`caption.md` 的榜一一句话和 5 个话题。缺任何一项就继续补齐，并在最终回复中同时给出图片目录与文案文件。

> 用户场景：刷到帖子 → 看榜一这句话 → 滑图看 10 张信息图。

## 输出位置

- 上下文档案：`~/Projects/ph-daily/context/YYYY-MM-DD-<slug>.md`（给后续积累/检索/喂模型）
- 信息图数据：`~/Projects/ph-daily/xhs/YYYY-MM-DD/data.json`（定位+一句话精华，改文案/重渲都从这改）
- 信息图 HTML：`~/Projects/ph-daily/xhs/YYYY-MM-DD/temp_html/NN-<slug>.html`（留底，不删——用于事后 diff/排查）
- **发布包**：`~/Projects/ph-daily/xhs/YYYY-MM-DD/`（最终交付：按排名命名的 PNG + caption.md）

## 迭代

- 改档案字段 → `references/context-template-v2.md`
- 改一句话精华的提取方法 → `references/framework.md`
- 改信息图版式（CSS/HTML 结构）→ `references/xhs-template.html`
- 改渲染逻辑（logo 处理、渲染参数）→ `scripts/render_xhs.py`
四者解耦，独立进化——改版式不用碰渲染脚本，改渲染逻辑不用碰版式。
