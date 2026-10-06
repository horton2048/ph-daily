# Vibe Buddy · 扩展阅读上下文

> PT 2026-08-04 Product Hunt 榜单第 6 名 · 👍 157 · 💬 8
> 归档日期 2026-08-05 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Vibe Buddy |
| 英文 tagline | Hardware for AI coding |
| 中文 tagline | 你的 AI，终于有了实体（官网中文版：你的 AI，終於有了實體） |
| 官网 | https://vibe-buddy.byvova.com/ |
| PH 页 | https://www.producthunt.com/products/vibe-buddy |
| 品类标签 | Robots · Developer Tools · Vibe coding |
| 票数 / 评论 | 157 / 8（PH 页实时抓取显示 159 票，任务口径 157） |
| 公司主体 | 未查到（无注册公司信息，官网页脚未列） |
| logo | https://ph-files.imgix.net/f3cf230a-82aa-41c8-bfc2-b371b3c498dc.png |

## 是做什么的（如实复述，不评价）

Vibe Buddy 是一个小巧的橙色桌面机器人（81 × 54 × 25 mm / 3.2 × 2.1 × 1.0 in），通过蓝牙与电脑连接，用内置小屏幕实时显示 **Codex** 和 **Claude Code** 两个 AI 编程代理的用量上限（usage limits，显示用量百分比与重置时间）和任务状态（工作中、等待回应、已完成、额度用尽）。其定位是"为 AI 编程而生的硬件"——把原本需要开另一个标签页/终端才能确认的代理用量与状态信息，变成桌面上扫一眼就能感知的物理设备。机器人会在 AI 需要用户回复/审批或完成任务时改变表情。当前为工作原型机，官网在接受预售登记。

## 解决什么问题（事实层面，不判断值不值得解）

- **用量/状态监控需反复切窗口**：Codex / Claude Code 这类 CLI 代理运行期间，用户需另开标签页或终端确认"是否跑完、是否需要输入、是否撞上额度上限"。Vibe Buddy 把四个状态（working / needs input / finished / usage limit）变成桌面上无需命令即可一瞥得知的物理反馈（来源：PH 产品页描述）。
- **额度用完才后知后觉**：AI coding 时用量上限（quota）耗尽会中断工作流。Vibe Buddy 实时显示用量百分比与重置时间（reset time），让用户提前掌握剩余额度（来源：官网）。
- **缺少"需要输入/审批"的被动提醒**：机器人会在 AI 需要用户回应或任务完成时改变表情，无需主动查看（来源：官网 FAQ）。
- **目标场景**：桌面开发者、vibe coding 用户，使用 Codex 或 Claude Code 的 personal / business 账户（来源：官网 FAQ）。

## 怎么做的（技术原理/机制，事实层面）

- **本地 CLI 读取数据**：Vibe Buddy CLI 在用户电脑本地读取 Codex 与 Claude Code 的用量及活动（来源：官网 FAQ）。
- **蓝牙传输，数据留本机**：仅通过蓝牙把"用量上限、任务数量、显示状态"传给机器人；提示词、密钥、token 及账户数据均保留在用户电脑上，不出本机（来源：官网 FAQ）。
- **单程序双工具**：一个本地程序即可在同一块小屏幕上同时显示两款工具的状态（来源：官网）。
- **硬件**：ESP32 桌面机器人（来源：创始人个人站 byvova.com 项目列表，注明技术栈 ESP32 / Python / SvelteKit）。内置电池，可连接 USB-C 持续使用，也可拔线后置于桌面（来源：官网）。
- **状态显示**：用量百分比 + 重置时间；状态四态（工作中、等待回应、已完成、额度用尽）；AI 需回复/审批或任务完成时改变表情（来源：官网）。
- **原型状态与生产**：目前为运作中的原型机，软件与生产、零部件、包装、配送规划仍在进行，预计 2026 年 9 月开始出货；设计、3D 打印、组装、测试均在加拿大温哥华完成，内置电子模块于中国制造（来源：官网 FAQ）。
- **账号支持**：支持 personal 与 business 账户（来源：官网 FAQ）。
- **PH 页面 "Built With"**：Codex 3.0 by OpenAI（来源：PH 产品页）。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Volodymyr Pytsiuk（Vova），温哥华软件工程师。现任职 DeviantArt（2022–今，构建高性能 API、ML 模型训练与部署、A/B 测试系统）；此前 SoftServe/Cisco 波兰格但斯克（邮件垃圾检测，Talos 平台）、GoBoutique 乌克兰利沃夫（交易算法、ML Kubeflow 管道）。计算机科学硕士（乌克兰 Vasyl Stefanyk PNU）。 | 创始人个人站 byvova.com |
| 联合制作者 | Alize（GitHub: aalizelau，21 个仓库，AI 相关如 Live2D 数字人项目） | 官网页脚 + GitHub |
| 团队 | 官网明确"由 Vova 与 Alize 于温哥华制作"，两人为公开署名 | 官网 |
| 融资 | 未查到（无任何融资报道；产品处于预售登记阶段，非正式发售） | — |
| 投资方 | 未查到 | — |
| 加速器 | 未查到 | — |
| 合规认证 | 未查到 | — |

## 定价 / 商业模式

- **预售价 HK$459（不含运费）**：官网 FAQ 明确"预计售价为 HK$459（未包括运费）"。
- **预售登记制**：现阶段无需付款，表单收集邮箱 + 数量（1–5+）+ 国家/地区；之后先收到原型进度更新，再邮件通知供应、付款与配送信息，最后确认订单（来源：官网 FAQ）。
- **运费另计**：配送国家/地区含 US、Canada、UK、Japan、Singapore、South Korea、Hong Kong 等 27+ 项；创始人 PH 评论中表示不同亚洲国家运费差异可能很大（来源：官网 + PH 评论区）。
- **出货时间**：预计 2026 年 9 月开始出货（来源：官网 FAQ）。
- 模式：硬件一次性购买 + 运费，无订阅（目前信息未见订阅收费）。

## 关联信息 / 生态

- **PH "Built With"**：Codex 3.0 by OpenAI（来源：PH 产品页）。
- **PH 相似产品列表**：opencode、Pieces for Developers、Claude for Desktop、Notchcode、Code Snippets AI（来源：PH 产品页）。
- **创始人其他项目**（来源：byvova.com）：My Days in Canada（iOS 加籍居留天数追踪，数据留设备/iCloud）、Played in Russia（在俄演出艺术家公开数据库）、The Shy Dock（macOS menu bar 自动隐藏 Dock）、Potato Classifier（土豆识别 ML 应用）。
- **隐私声明**：提示词、密钥、token、账户数据均留本机，蓝牙仅传用量上限/任务数/显示状态（来源：官网 FAQ）。
- **官网素材说明**：展示照片/视频为真实原型，非 AI 生成。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-08-04 | 登上 Product Hunt 日榜（第 6 名，158 票量级），maker 置顶"接受预售中" |
| 2026-09 | 预计开始出货（官网 FAQ） |
| — | 无更早公开里程碑（官网为单页落地页，无时间线/新闻页） |

## 评论区反馈（事实摘录，不评价）

- **Gal Dayan（质疑）**：menu bar 图标或终端通知就能免费显示同样的四个状态，不需要桌面空间或充电线……好奇人们会不会第一周之后还继续用它。/ 创始人未回复。
- **Jie Yang（提问）**：看起来可爱，需要充电吗还是自带铅酸电池？寄到亚洲国家的大概运费是多少？/ 创始人回复：哪个国家？我可以帮你查，但不同亚洲国家价格可能差异很大。（注：关于充电/电池部分未正面回答。）
- **Pragati Tripathi（评论）**：太可爱了，觉得我孩子会在它放在我桌边时把它偷走。
- **Henry Habib（评论）**：这个小机器人太可爱了……把用量上限保持在视野里是很实用的想法。/ 创始人回复：很乐意给你寄第一批。
- **xinyuanwei（评论）**：基本上是 AI 时代的桌面闹钟——只不过不是告诉你 9 点了，而是告诉你 agent 额度用完了。
- **Ruiying Mai（评论）**：太可爱了！确实让 vibe coding 更有趣。/ 创始人回复：谢谢，会很高兴寄你一个首批样品。
- **Maker 置顶评论**：Volodymyr Pytsiuk（Vova）——"接受预售中"（Accepting pre-orders now）。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/vibe-buddy（产品描述、tagline、品类标签、logo URL、maker 置顶评论、评论区 6 条用户互动、Built With、相似产品列表）
- 官网：https://vibe-buddy.byvova.com/（产品描述、FAQ 8 条、预售价 HK$459、出货 2026-09、规格 81×54×25mm、蓝牙与隐私机制、制造地、团队 Vova + Alize）
- 创始人个人站：https://byvova.com/（身份、工作经历、教育、Vibe Buddy 技术栈 ESP32/Python/SvelteKit、其他项目）
- GitHub：https://github.com/vovapyc 与 https://github.com/aalizelau（均无公开 vibe-buddy 仓库，闭源硬件产品）
- 公开报道/融资：WebSearch 多组关键词（"Vibe Buddy hardware AI coding" / "Vibe Buddy Pytsiuk pre-order" / "Vibe Buddy funding" / "Vibe Buddy desk robot news"）均无相关结果

## 未查到 / 待补

- **融资金额/轮次/投资方/加速器**：未查到（无任何融资报道）
- **公司注册主体/注册地**：官网无公司信息，未查到
- **运费具体金额**：未公布（仅"不含运费"，按国家/地区不同）
- **最终零售价换算其他币种**：仅有 HK$459 预售口径
- **电池容量/续航时长/充电规格细节**：未公布（Jie Yang 询问，创始人未正面回答）
- **除 Codex 与 Claude Code 外支持的工具**：官网仅列这两款，未查到更多
- **媒体测评/第三方报道**：未查到
- **GitHub**：无公开仓库（闭源）
