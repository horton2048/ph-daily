# Gemini Robotics 2 · 扩展阅读上下文

> PT 2026-07-31 Product Hunt 榜单第 10 · 👍 116 · 💬 2
> 归档日期 2026-08-01 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | Gemini Robotics 2 |
| 英文 tagline | Google's AI brain for the next generation of robots |
| 中文 tagline | 谷歌为下一代机器人打造的 AI 大脑 |
| 官网 | https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/ |
| PH 页 | https://www.producthunt.com/products/gemini-robotics-2 |
| 品类标签 | Robots · Artificial Intelligence · AI Infrastructure Tools |
| 票数 / 评论 | 116 / 2（榜单快照值；PH 页当前显示 131 points） |
| 公司主体 | Google DeepMind（Google 内部研究机构） |
| 企业版/关联站点 | Google AI Studio（ai.dev）、Gemini Enterprise Agent Platform、Trusted Tester Program |

## 是做什么的（如实复述，不评价）

Gemini Robotics 2 是 Google DeepMind 面向机器人推出的"智能层"，由一组 Gemini 多模态模型驱动，让机器人能感知环境、推理任务、并把指令转化为全身动作。本次发布包含三个模型：

1. **Gemini Robotics 2**（VLA，vision-language-action）：把视觉+语言输入转化为电机控制，能驱动全身人形机器人（从脚到指尖）和双臂机器人，对手部（多指）和夹爪都支持灵巧操作。
2. **Gemini Robotics ER 2**（embodied reasoning，VLM）：作为机器人"高层大脑"，与人沟通、理解物理世界、规划多步任务（可持续数分钟、数百个决策），并新增多机器人协作能力。
3. **Gemini Robotics On-Device 2**（端侧 VLA）：本地运行、低延迟，几小时数据（官方称典型 <200 条样本）即可适配到全新形态的机器人本体。

整体定位：从上一代的"桌面级上半身操作"扩展到"全身运动 + 灵巧操作 + 多机协作 + 快速端侧适配"，是 DeepMind 走向"物理世界 AGI"的一个里程碑。

## 解决什么问题（事实层面，不判断值不值得解）

- 传统机器人多为预编程或遥操作，只能执行狭窄、重复的任务序列，无法自主学习或适应不可预测的环境。（来源：DeepMind 博客原文）
- 把已学技能从一个机器人本体迁移到另一个形态不同的机器人，长期是难题。（来源：DeepMind 博客）
- 真实世界任务通常需要多步、持续数分钟，单机器人无法独立完成时缺乏协作机制。（来源：DeepMind 博客）
- 许多机器人应用场景对网络延迟/断网敏感，需要端侧本地推理。（来源：DeepMind 博客）

## 怎么做的（技术原理/机制，事实层面）

- **VLA 架构**：把视觉+语言输入直接转化为电机控制信号，是"vision-language-action"模型；同一 checkpoint 可跨多种本体运行——官方演示中同一模型控制 Apptronik Apollo 2（配 SharpaWave 五指 22 自由度手）、Apollo 2（配 Inspire 手）和 Franka Duo（配 Robotiq 夹爪）三种硬件。（来源：DeepMind 博客 + 配图说明）
- **全身控制**：上一代只控制人形上半身做桌面任务，本代首次控制整个人形，可执行"走—蹲—伸—抓—放"链式动作。示例：让 Apollo 2 把浇水壶放进底层货架的绿色箱子里——机器人走过去、抓起、走到货架、精确放置。（来源：DeepMind 博客）
- **灵巧操作**：可控制 22-DOF SharpaWave 五指手完成打结、封 ziplock 袋等精细动作；也可控制标准两指平行夹爪在 Franka Duo 上做紧密打包等任务。（来源：DeepMind 博客）
- **Agentic 推理 + 多机协作**：ER 2 作为高层大脑，观察场景、推理步骤、调度 VLA 执行、跟踪进度，失败时自我纠正；新增"任务起止判断"和"关键事件定位"能力；引入多机器人协作，不同类型机器人可通信分工。（来源：DeepMind 博客）
- **端侧快速适配**：On-Device 2 继承自 1.5 的 motion transfer 技术，原生多本体，对新双臂本体只需几小时、官方称 <200 条样本即可适配，即使形态/传感器/自由度差异很大（Dexmate、SO101、Trossen 等平台演示）。（来源：DeepMind 博客）
- **安全机制**：引入 ASIMOV-Agentic 基准，评测 ER agent 拒绝不安全 VLA 工具调用、判断任务可行性、不确定时主动请求人工介入的能力；ER 2 在安全约束遵循和人机接近度基准上是"DeepMind 至今最安全的机器人模型"，能检测附近人类并触发安全停机。安全细节见 Gemini Robotics 2 Safety Technical Report。（来源：DeepMind 博客）

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 公司主体 | Google DeepMind（Google 内部 AI 研究机构） | DeepMind 博客页头品牌 |
| 发布署名作者 | Carolina Parada（博客署名） | DeepMind 博客 |
| 领导层致谢 | Jean-Baptiste Alayrac、Zoubin Ghahramani、Koray Kavukcuoglu、Demis Hassabis | DeepMind 博客 Acknowledgements |
| 团队规模 | Gemini Robotics team，致谢名单列名 200+ 人 | DeepMind 博客 Acknowledgements |
| 合作硬件伙伴 | Apptronik、Boston Dynamics、Agile Robots | DeepMind 博客致谢段 |
| 融资 | Google DeepMind 内部项目（非独立创业公司，无外部融资） | 本任务约定 |
| 投资方 | 无（Google 内部） | — |
| 加速器 | 无 | — |
| 合规认证 | 安全技术报告（Gemini Robotics 2: Safety Technical Report）；ASIMOV-Agentic 安全基准 | DeepMind 博客 |

## 定价 / 商业模式

- PH 产品页标注 **Free**。
- **Gemini Robotics ER 2**（推理模型）：已在 Google AI Studio 公开可用（preview），并在 Gemini Enterprise Agent Platform 上以 private preview 提供。（来源：DeepMind 博客）
- **Gemini Robotics 2 VLA** 与 **On-Device 2**：面向 early-access partners / Trusted Tester Program 提供，未公开定价。（来源：DeepMind 博客）
- 商业模式本质：模型作为"机器人智能层"授权/开放给硬件厂商与开发者，自身不卖硬件；盈利路径走 Google 的 API/平台分发（AI Studio / Gemini Enterprise Agent Platform）+ 深度合作（Apptronik、Boston Dynamics、Agile Robots）。具体计费未公开，未查到。

## 关联信息 / 生态

- **同系产品**：Gemini Robotics（v1，2025-03）、Gemini Robotics 1.5（2025-09，引入 motion transfer）、Gemini Robotics-ER 1.6（2026-04，增强 embodied reasoning）、Gemini Robotics ER 2（2026-07，相关发布）、Gemini Robotics 2（2026-07-30，本代）。（来源：DeepMind 博客底部 Related posts）
- **跨本体能力**：同一 checkpoint 跨 Apollo 2 + SharpaWave 手 / Apollo 2 + Inspire 手 / Franka Duo + Robotiq 夹爪三种硬件，whole-body 和夹爪类灵巧任务官方称达到中到高成功率，多指灵巧操作仍是难点。（来源：DeepMind 博客配图说明）
- **定位语**："path toward solving AGI in the physical world"——把通用智能从数字世界推进到物理世界。（来源：DeepMind 博客）
- **PH Similar Products**：Gemini Robotics、OpenAI、Hugging Face、Mistral AI、Eden AI（PH 页 Similar Products 列表）。

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2025-03 | Gemini Robotics 发布——首次把 Gemini 多模态理解转化为真实世界动作 |
| 2025-09 | Gemini Robotics 1.5 发布——引入 motion transfer，把 AI agent 带入物理世界 |
| 2026-04 | Gemini Robotics-ER 1.6 发布——增强 embodied reasoning，支撑真实世界任务 |
| 2026-07 | Gemini Robotics ER 2 相关发布（视频理解、任务编排、多机协作） |
| 2026-07-30 | Gemini Robotics 2 正式发布——全身控制 + 灵巧操作 + 多机协作 + 端侧快速适配 |

## 评论区反馈（事实摘录，不评价）

- **Hunter（Justin Jincaid，3 天前）**："Discovered this while following Google DeepMind's latest AI research... Physical AI feels like the next major chapter of artificial intelligence." 立场：定位式介绍，未给具体技术数字。
- **Gal Dayan（2 天前）**：批评性提问——"post itself doesn't give me much to react to beyond 'physical AI is the next frontier'... what would actually change my mind is something concrete: task success rate on an unseen environment, how it handles a failed grasp instead of just a clean demo reel, or latency from perception to actuation. without that it reads more like a positioning statement than a product I can form an opinion on. is there a technical writeup somewhere with actual numbers, or is this purely a research preview at this stage?" 诉求：要未见环境下的任务成功率、失败抓取处理、感知到执行的延迟等技术数据。官方未在该评论下回复（截至抓取时）。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/gemini-robotics-2 （拿到了 tagline、产品描述、Launch Team、评论区两条、Similar Products、logo URL）
- 官网/DeepMind 博客：https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/ （拿到了三个模型定义、全身控制/灵巧操作/多机协作/端侧适配/ASIMOV-Agentic 安全机制/合作伙伴/致谢名单/Related posts 时间线）
- 公开报道：未额外搜索（DeepMind 官方博客为一手源，已充分）
- GitHub：未查（Google DeepMind 闭源，无公开仓库——符合预期）

## 未查到 / 待补

- **具体任务成功率数字**：DeepMind 博客配图说明提到"medium to high success rate for whole-body and gripper-based dexterous tasks"，但未给绝对百分比数值；多指灵巧操作"remains challenging"。详细数字未在博客正文给出，可能存在于 Safety Technical Report 或后续论文中，未查到。
- **感知到执行的延迟数据**：未查到（PH 评论区 Gal Dayan 也在追问此项）。
- **定价**：未公开定价，VLA/On-Device 走 early-access，AI Studio preview 免费，Enterprise Agent Platform private preview 计费未公开。
- **PH 官方创始人评论**：本产品由 hunter Justin Jincaid 提交，非 Google DeepMind 官方下场发评论，DeepMind 团队未在 PH 评论区互动（截至抓取时）。
- **与 v1 的量化对比**：博客定性说"上一代只控制上半身桌面任务"，但未给 v1 vs v2 的成功率/速度对比数字。
