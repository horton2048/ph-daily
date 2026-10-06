# Screen Awesome · 扩展阅读上下文

> PT 2026-08-04 Product Hunt 榜单第 7 名 · 👍 138 · 💬 6
> 归档日期 2026-08-05 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Screen Awesome（Chrome 商店名：Screen Awesome — Record, Capture & Annotate） |
| 英文 tagline | The free screen recorder that cannot upload your video |
| 中文 tagline | 无法上传视频的免费屏幕录制器 |
| 官网 | https://screenawesome.com |
| PH 页 | https://www.producthunt.com/products/screen-awesome-record-annotate |
| 品类标签 | Screenshots and screen recording apps · Chrome Extensions（商店分类：Workflow & Planning） |
| 票数 / 评论 | 138 / 6 |
| 公司主体 | 个人开发者 Nitinbhai Viras（Chrome 商店发布者名 "helpinbox"，版权 © 2026 Nitinbhai Viras） |
| 企业版/关联站点 | 无；Chrome 商店页 https://chromewebstore.google.com/detail/screen-awesome-—record-c/pnaekpbijadjfajodhbjimodnmnnfdik |
| logo | https://ph-files.imgix.net/2d5c8747-3e74-4c0b-944e-e226b30472f8.png |

## 是做什么的（如实复述，不评价）

Screen Awesome 是一个 Chrome 扩展屏幕录制 / 截图工具，核心卖点是"无法上传"：扩展的 manifest 中 `host_permissions` 为空，Chrome 在架构层面阻止扩展向任何服务器发出请求，因此录制内容没有上传统路。所有录制/截图都写入用户自己浏览器的 IndexedDB，无账号、无同步、无遥测。

功能覆盖：录制标签页 / 窗口 / 整屏 / 摄像头；导出 MP4（Chrome 支持编码时）、WebM（兜底）或 GIF；录制时可记录点击位置、用"虚拟相机"自动缩放跟随点击（auto-zoom）；矢量标注工具（箭头、画笔、荧光笔、图形、任意系统字体文字、对话气泡、步骤计数器、emoji 印章、裁剪、插入图片）全部保持可编辑、可撤销；截图支持可视区、拖选区域、滚动拼接全页（处理固定头部/侧边栏）、桌面捕获、定时捕获；另有麦克风混音、标签页音频、可移动摄像头小窗、暂停/倒计时/录制长度上限、页面上实时绘制。全部功能免费且解锁，无水印，无账号，无录制时长限制（开发端不设限）。

## 解决什么问题（事实层面，不判断值不值得解）

- **录屏的隐私不透明**：创始人自述——录一个满是客户数据的 bug 报告时，意识到自己"完全不知道这段视频去了哪里"。这成为做这个产品的直接动机（PH 开场评论）。
- **让"信任"变成"可验证"**：现有录屏工具要求用户信任其隐私政策（trust us）；Screen Awesome 用零 host 权限让 Chrome 直接阻止联网，用户可在安装前打开 `chrome://extensions` 自己验证 Site access 为 none。
- **录制后处理繁琐**：评论者 Asad M. 的痛点——一句话录错要整段重录；创始人点出的痛点——录完要转换格式才能发进 Slack / Docs / Premiere（因此做 MP4 直出，无需转码）。
- **全页截图不可靠**：滚动拼接时固定头部/侧边栏容易错位。
- **标注工具被锁在付费版**：多数录屏工具把标注/去水印放在付费墙后；本产品所有工具免费解锁。

## 怎么做的（技术原理/机制，事实层面）

来源：官网 screenawesome.com + Chrome 商店页 + PH 创始人评论

- **零 host 权限**：manifest 中 `host_permissions` 为空，Chrome 自身阻止扩展联系任何服务器，上传在架构上"不可能而非仅仅被禁止"（impossible rather than merely disallowed）。
- **本地存储**：录制内容写入浏览器 IndexedDB，全部留在本机；无账号、无同步、无分析。卸载扩展会删除所有本地录制，故提供批量下载（bulk download）功能。
- **按需注入**：平时不在用户浏览的页面上运行 content script——仅在请求录制某个页面的那一刻才注入代码，导航离开时 Chrome 撤销访问权，因此正常浏览页面无性能影响。
- **auto-zoom 机制**：录制标签页时记录点击位置，studio 用虚拟相机回放画面、逐个点击"滑入"缩放；可实时预览、可关闭、可烘焙进导出文件。
- **导出格式**：MP4（Chrome 支持的编码处）直出，WebM 兜底，另支持 GIF 动图。
- **版本/环境要求**：Manifest V3；要求 Chrome 116+；Chromium 系浏览器（Edge、Brave、Opera）理论上可装但未测试；Firefox / Safari 版未开发。
- **隐私可验证**：`chrome://extensions` → Screen Awesome → Site access 显示 none；扩展设置页内置"Check its permissions"按钮直达 `chrome://extensions`。
- 商店数据披露：开发者声明"不会收集或使用你的数据"，数据不出售给第三方、不用于不相关目的、不用于信用评估/借贷。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Nitinbhai Viras（PH @nitin_viras），solo maker；联系邮箱 nitinbhaiviras@gmail.com | PH 产品页、官网版权行 |
| 发布者主体 | Chrome 商店发布者名 "helpinbox"（是否为注册公司未查到） | Chrome 商店页 |
| 融资 | 未查到 | — |
| 投资方 | 未查到 | — |
| 加速器 | 未查到 | — |
| 合规认证 | Chrome 商店隐私披露"不收集或使用你的数据"；开发者未标识为欧盟意义上的 trader | Chrome 商店页 |

## 定价 / 商业模式

来源：官网 + PH 创始人评论 + Chrome 商店页

- **完全免费**：全功能解锁，无水印，无账号，无试用，无录制时长上限，无付费档。
- 创始人明确："It's free, there's no paid tier, and I'm not planning one"（免费，无付费档，也不计划做）。
- 模式：免费软件，无 upsell，无可见商业模式。

## 关联信息 / 生态

- **竞品**（PH 相似产品列表）：Loom、CleanShot、Tella、Screenity、Zight。
- **差异化定位**：官网对比表宣称相对"typical capture extension"——无页面读取、无上传能力、无账号、无分析、标注工具不设付费墙。
- **商店状态**：v1.0.1，2026-08-04 更新，包体 171KiB，安装量显示 "1 user"，0 条评分（0 reviews）。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-08-04 | Chrome 商店更新至 v1.0.1；同日 PH 发布（PH 页面无更早里程碑） |

## 评论区反馈（事实摘录，不评价）

- **Nitin Viras（创始人，开场评论）**：隐私由代码而非承诺强制——`host_permissions` 为空，Chrome 本身阻止扩展连服务器；"不是因为我不承诺，而是因为代码里根本没有能这么做的部分"。全部功能解锁；三个引以为傲的亮点：auto-zoom（采样点击、虚拟相机滑入）、MP4 直出（+WebM/GIF）、全页滚动截图（处理固定头部/侧边栏）。诚实说明：仅 Chrome/Chromium、主要在 Windows 测试、卸载会删本地录制需先批量下载。向社区抛出两个问题："verifiable 是否比 trust us 更能打动你？"以及"现有录屏工具还有哪些操作必须手工做？"
- **Asad M.（@asadmalik901）**：verifiable 更好，但"这个声明有保质期"——Chrome 会自动更新扩展，未来某版可能悄悄加回权限；建议每次发布都公开 manifest diff 并链接到商店页，让用户持续可查。手动痛点：一句话录错就要整段重录。
- **Shahriar Hasan（@shahriardgm）**：报告 bug——在 Mac 上多次尝试都无法开始录制，附了截图。
- **Amberlin Waxman（@launch_p）**：赞赏"安装前就能在 chrome://extensions 验证零权限声明"；评价 auto-zoom 跟随点击"是真正的用心工艺，不是勾选框功能"。
- **Narcis Mirandes（@narcismirandes）**：指出 Mac 用户已有 QuickTime（免费且易用），Apple 也强调安全——问 Screen Awesome 与 QuickTime 有何不同。
- **Chirag Chamoli（@chirag_chamoli）**：称是"非常深思熟虑的隐私处理方式"，同意"verifiable 确实比 trust us 更好"，并恭喜发布。
- **Natalia Iankovych（@natalia_iankovych）**：问"它能录制屏幕视频吗？"
- 注：抓取时未见创始人对上述单条评论的回复（页面仅含开场评论）。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/screen-awesome-record-annotate（产品描述、创始人开场评论、6 条评论全文、logo URL、相似产品列表、品类）
- 官网：https://screenawesome.com（技术机制：零权限/IndexedDB/按需注入/auto-zoom、FAQ、功能清单、版权行）；隐私页 https://screenawesome.com/privacy.html
- Chrome 商店页：https://chromewebstore.google.com/detail/screen-awesome-—record-c/pnaekpbijadjfajodhbjimodnmnnfdik（发布者 helpinbox、v1.0.1、2026-08-04 更新、安装量 1、0 评分、171KiB、隐私声明）
- GitHub：搜索无 Screen Awesome 公开仓库；候选账号 nitinviras / iamnitinviras 均无本产品仓库（记"无公开仓库"）
- WebSearch：关键词 "Screen Awesome screen recorder Chrome extension privacy" 等无有效第三方报道结果

## 未查到 / 待补

- **融资 / 投资方 / 加速器**：任何公开信息均未查到
- **公司注册主体**：Chrome 商店发布者名为 "helpinbox"，该主体是否为注册公司、注册地未查到；官网版权归个人 Nitinbhai Viras
- **创始人 GitHub 账号归属**：GitHub 存在 nitinviras（PHP 项目）与 iamnitinviras（Laravel 项目）两个候选账号，均无本产品仓库，无法确认哪个是本人，扩展为闭源
- **录制引擎实现细节**：编码器/MediaRecorder 等具体实现未披露
- **创始人评论回复**：抓取时未见创始人对单条评论的回复
- **真实用户量**：商店显示 "1 user"，大概率仅开发者本人；无法获取真实安装数
- **第三方报道 / 媒体评测**：WebSearch 无结果
- **未来浏览器支持时间表**：Firefox/Safari 版"尚未构建"，无时间表
