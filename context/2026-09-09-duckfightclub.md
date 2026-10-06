---
product: "DuckFightClub"
slug: "duckfightclub"
date: "2026-09-09"
rank: 7
votes: 122
comments: 10

category: "消费级硬件 + AI"
subcategory: "机器人竞技 / 实体 AI 玩具"
tags: ["实体机器人", "强化学习", "开源硬件", "Apache-2.0", "Hugging Face", "Pollen Robotics", "仿真到真机", "社区赛事"]

tech_stack: ["MuJoCo", "MuJoCo Warp (mjlab)", "PPO", "ONNX", "CUDA", "uv", "Apache-2.0", "Netlify", "Conductor"]
platform: ["Web (竞赛注册)", "YouTube 直播", "Hugging Face Hub (策略分享)", "Linux/GPU 训练"]
open_source: true
license: "Apache-2.0（机器人软件/RL 环境）；CC BY-SA-NC（3D 模型）"

business_model: "免费参赛 / 无现金奖金 / 三档赛事赞助（围裙板 $500+ / 擂台中心 $2,000+ / 背墙冠名 $15,000+）"
pricing_start: "免费参赛（机器人本体 Microduck $399 单独购买）"
funding_stage: "未披露（赛事本身独立非商业项目；机器人由 Pollen Robotics 推出）"
funding_amount: "未披露"

related_products: ["Pollen Robotics Reachy Mini", "Pollen Robotics Reachy 2", "索尼 Aibo", "Anki Cozmo / Vector", "Unitree Go 系列"]
maker_previous: ["Typeform 开发者生态建设（2018-2025）", "Red Hat / 3scale DevRel（2013-2018）", "HackBarna Barcelona AI 黑客松创始人"]

# 速览信号
key_signals:
  - "赛事只跑仿真：8 队单淘汰竞推机器鸭，10 月 2 日 YouTube 决赛，奖品是 Golden Beak Belt 实体腰带，无现金"
  - "借势 Pollen × Hugging Face 的 Microduck：25cm 双足、15 电机、800g、Apache-2.0、$399、8 月底开启预售已破 1 万台"
  - "sim-to-real 全栈开源：MuJoCo Warp 训 PPO → ONNX → 真机 50Hz 推理，含齿隙/back-EMF 建模与域随机化"
  - "非 Pollen 官方赛事：制作者是 SLNG.ai DevRel Nicolas Grenié（@picsoung），PH 上 122 票排 #7"

archived_at: "2026-09-10"
sources_count: 6
---

# DuckFightClub · 扩展阅读上下文

> PT 2026-09-09 Product Hunt 榜单第 7 · 👍 122 · 💬 10  
> 归档日期 2026-09-10 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | DuckFightClub |
| 英文 tagline | Train your MicroDuck and win the Golden Beak Belt |
| 中文 tagline | 训练你的 MicroDuck，赢得 Golden Beak Belt 金喙腰带 |
| 官网 | https://duckfight.club |
| PH 页 | https://www.producthunt.com/products/duckfightclub |
| 品类标签 | Robots · Sports · Artificial Intelligence（合计 500.1k followers） |
| 票数 / 评论 | 122 / 10 |
| 公司主体 | 独立非商业项目（个人策划），依托 Pollen Robotics × Hugging Face 的 Microduck 平台 |
| 关联站点 | https://pollen-robotics.com（机器人本体）；https://huggingface.co（策略分发/训练） |
| Hunter | Nicolas Grenié（@picsoung） |

## 是做什么的（如实复述，不评价）

DuckFightClub 是一个围绕 Pollen Robotics 开源双足机器人 **Microduck** 举办的
**仿真机器人相扑**（robot sumo）社区赛事。8 支队伍花数日训练强化学习策略，
然后在 Microduck 仿真器里单淘汰对决，争夺"Golden Beak Belt"。首场 QuackDown
决赛定于 2026 年 10 月 2 日 YouTube 直播。

赛事组织方在 PH 描述里把它类比为"想象 WWE SmackDown，但选手是可爱的、
AI 训练出来的机器人鸭"。参赛者既可以**注册一支队伍**自己训一个策略，
也可以**赞助/承办线下 Showdown**（巴黎、巴塞罗那等城市已有规划）。

DuckFightClub 与机器人硬件的关系是**完全解耦**——所有对抗都在 Microduck
仿真器里跑，**不直接操作真机**；真机出货之后才会开展线下 IRL 对战。

> 与"鸭 NFT / TON 链游戏"重名但**无关**：链上那只"Microduck"是 DuckChain 的
> 7000 个 NFT 鸭，二者项目独立。

## 解决什么问题（事实层面，不判断值不值得解）

- **强化学习的"训练数据/对手段"瓶颈**：传统 RL 训练出来的策略缺乏"被高水平
  对手检验"的环境；DuckFightClub 把"赛博斗兽场"当作公开标尺，参赛者互为
  对手，互相提供对抗样本。
- **示教/索取的中间地带**：Microduck 平台自带的 7 个预训策略（走路、坐下、
  站起、踢、抓、轮滑、起身）能跑，但用户改不了；DuckFightClub 给"想自己训
  一个动作的玩家"一个低门槛入口——不用买真机也能参与。
- **开源机器人的曝光问题**：Pollen Robotics 出硬件、Hugging Face 出云端算力，
  但需要一个"事件"才能把流量引到 RL 仓库；赛事就是这种事件。

## 怎么做的（技术原理/机制，事实层面）

- **仿真器**：基于 **MuJoCo Warp (mjlab)**，GPU 加速物理仿真，单进程可并行
  4096 个环境。
- **算法**：PPO（Proximal Policy Optimization），训练频率 50 Hz（与真机
  on-board 策略循环一致）。
- **建模细节**：
  - 14 个 Dynamixel XL330 舵机的 **BAM M6** 执行器模型，含反电动势、
    摩擦、**齿隙（backlash ±1°）** 建模，每个主任务都配"齿隙双胞胎"。
  - 域随机化（domain randomization）用于 sim-to-real 迁移。
- **部署链路**：`uv run train` → 导出 ONNX → 真机 50Hz 推理。
  提供 `uv run publish` 一键把策略上传 Hugging Face Hub（含 manifest.json schema 2）。
- **观测空间**：48 维本体感知 + 命令向量 = 61 维 actor 输入。
- **关节布局**：左腿 0-4、颈/头 5-8、右腿 9-13。

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 赛事发起人 | Nicolas Grenié（@picsoung） | PH hunter 主页 / 个人站 nicolasgrenie.com |
| 发起人当前职位 | Developer Advocate at **SLNG.ai**（自 2025-12 起） | 个人简历 |
| 发起人前职 | Typeform DevRel（2018-03 至 2025-12） | 个人简历 |
| 主办方性质 | **独立、非商业、个人项目**（CC BY-SA-NC 协议说明） | duckfight.club 文末标注 |
| 底层机器人方 | **Pollen Robotics**（Bordeaux, France；Apache-2.0；"Part of Hugging Face"） | pollen-robotics.com |
| 仿真/算力合作 | **Hugging Face**（Hugging Face Jobs / Hub 策略分发） | pollen-robotics.com / microduck_rl README |
| Pollen 创始人 | 未在官网披露（公开报道提及 Matthieu Lapeyre / Pierre Rouanet） | 未独立核实，标"待补" |
| 融资 | 未披露 | — |
| 加速器 | 无 | — |

## 定价 / 商业模式

DuckFightClub 本身：**免费**。商业模式是**赛事赞助**，三档：

| 档位 | 起价 | 名额 | 权益（节选） |
|---|---|---|---|
| Apron ring boards | $500/块 | 12 块 | 围裙板品牌位 |
| Mat center | $2,000 | 1 | 擂台中心位 |
| Back-wall marquee | $15,000 | 1 | 命名合作方，含低三/回放/胜者动画 |

**注**：未涉及任何现金投注或奖金，友好打赌可用 Codex/Claude 配额或吹牛权。

底层机器人 Microduck 单独购买：

| 配件 | 售价 |
|---|---|
| Microduck 本体（introductory） | **$399** |
| 充电包 | $39 |
| 开发者包 | $119 |
| 配件包 | $39 |

## 关联信息 / 生态

- **Pollen 产品线**：Reachy 2、Reachy Mini（"10,000+ shipped worldwide"）、Microduck。
- **开源仓库**：
  - `pollen-robotics/microduck_rl`（RL 训练环境，2.0k stars / 402 forks）
  - `pollen-robotics/microduck`（机器人本体运行时）
  - `mujocolab/mjlab`（训练框架）
  - `Rhoban/bam`（执行器模型）
- **预训练 7 个策略**（人人可重训）：走路（速度跟踪 gait）、坐下/站起、踢、抓、
  轮滑、摔倒起身。
- **同类/相关产品**：索尼 Aibo、Anki Cozmo/Vector、Unitree Go 系列（实体 AI
  小型机器人）；DuckChain 上的 Microduck NFT（同名，无业务关联）。

## 技术时间线（已查证）

| 日期 | 事件 |
|---|---|
| 2026-08-27 | Pollen × Hugging Face 开放 Microduck 预购（$399 介绍价） |
| 2026-09-09 | PH 上榜 DuckFightClub；同日开启赛事注册 |
| 2026-09-16 | 公布 8 队名单（队徽、walkout 名、策略 teaser） |
| 2026-09-19 | 开放仿真器 scrimmage |
| 2026-09-23 | 策略提交截止 |
| 2026-09-26 | Bracket reveal（直播） |
| 2026-09-30 | Battle of the Nerds：Stanford vs. Berkeley（附属赛） |
| 2026-10-02 | QuackDown 主赛，YouTube 直播决赛 |
| 2026-12-01~03 | Paris Paired Summit "Prise de bec" 线下赛 |

## 首期 8 队名单（已公布）

| 种子 | 队名 |
|---|---|
| 1 | Pollen Wildcard |
| 2 | Hugging Face Pond Ops |
| 3 | MIT WaddleWorks |
| 4 | Paris Duckworks |
| 5 | CMU Servo Squad |
| 6 | Open Source Outlaws |
| 7 | Tokyo Torque Club |
| 8 | Montreal Move Hackers |

比赛规则要点：单淘汰、Bo3、1:1 加赛；推/绊/顶出圈外即胜；裁判只在仿真器
故障、死锁、不可恢复出生状态时介入；所有选手共享同一只 25cm 开源 Microduck
本体，差异完全来自 RL 策略。

## 评论区反馈（事实摘录，不评价）

- **Gal Dayan**：把 RL 排行榜做成观赏体育是个好想法；策略每届从零训还是可以
  跨赛季微调？（创始人未在 PH 评论里直接回复此问）
- **Rabnoor Singh**："直播一个规则是'不要谈它'的赛事，是很有勇气的读解。"
- **Jorge Alcántara**："这就破了第一条规则。"
- **Maria Anosova**："鸭子是今年 PH 的符号。"
- **Nika**：造型让我想到皮克斯台灯。**Nicolas（发起人）回复**：确实，
  已经有人训出一个做皮克斯开场 Luxo Jr. 动作的策略。
- **Sacha MORARD**：Edgee 团队敢不敢打。
- **Paolo Go**：amazing。
- **Lorina Balan**：造型上的熟悉感刚才对上了。

## 信息来源

- PH 产品页：https://www.producthunt.com/products/duckfightclub  
  （拿到：tagline、票数、评论、关联产品、发起人身份、hunter 信息）
- 赛事官网：https://duckfight.club  
  （拿到：8 队名单、赛程、规则、赞助档位、本地 Showdown 计划）
- Pollen Robotics 官网：http://pollen-robotics.com（页面仅含公司基本介绍与产品线）
- Microduck 产品页：http://pollen-robotics.com/microduck  
  （拿到：硬件参数、定价、训练栈概述）
- GitHub 仓库：https://github.com/pollen-robotics/microduck_rl  
  （拿到：训练栈细节、PPO/MuJoCo Warp/BAM/齿隙建模、ONNX 部署链路）
- 发起人简历：https://www.nicolasgrenie.com/  
  （拿到：职业经历、社区活动）

## 未查到 / 待补

- **Pollen Robotics 创始人姓名**：公开报道常提 Matthieu Lapeyre / Pierre Rouanet，
  但本轮未在官方渠道独立核实，标"待补"。
- **公司成立年份 / 总部地点**：官网首页未明确披露（普遍报道为法国 Bordeaux，
  未独立核实）。
- **Microduck 实际出货日期**：预购 2026-08-27 开放，但官方未给出真机到货日期。
- **Pollen 是否被 Hugging Face 收购**：官网仅写"Part of Hugging Face"，
  未给出法律实体层面的并购/投资公告。
- **Pollen 融资历史**：未在官网或本轮搜索中披露。
- **赛事赞助商名单**：档位与价格已公布，但当前已签客户未列出。
- **是否接受现金奖金赞助**：明确不接受投注/现金奖金；赞助三档是否可定制，
  未说明。
