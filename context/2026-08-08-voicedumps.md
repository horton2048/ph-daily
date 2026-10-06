---
# 结构化元数据（用于索引和聚合）
product: "VoiceDumps"
slug: "voicedumps"
date: "2026-08-08"
rank: 7
votes: 0
comments: 1

# 分类标签
category: "消费级应用"
subcategory: "本地语音转文字"
tags: ["开源", "MIT", "本地优先", "离线", "Whisper", "Mac", "Apple Silicon"]

# 技术信息
tech_stack: ["Rust", "Tauri", "React", "whisper.cpp", "Swift", "SQLite", "Metal"]
platform: ["Mac", "Apple Silicon"]
open_source: true
license: "MIT"

# 商业信息
business_model: "开源免费"
pricing_start: "免费"
funding_stage: "未披露"
funding_amount: ""

# 关联信息
related_products: ["Wispr Flow", "macOS 系统听写"]
maker_previous: []

# 元信息
archived_at: "2026-08-08"
sources_count: 3
---

# VoiceDumps · 扩展阅读上下文

> PT 2026-08-08 Product Hunt 榜单第 7 名 · 👍 票数未知 · 💬 1（仅 maker launch 评论）
> 归档日期 2026-08-08 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | VoiceDumps（repo：heynaavi/voiceDump） |
| 英文 tagline | Hold the globe key. Talk. The words appear at your cursor. |
| 中文 tagline | 按住 globe 键，说话，文字出现在你的光标处 |
| 官网 | https://voicedumps.qwee.ai/ |
| PH 页 | https://www.producthunt.com/products/voicedumps |
| PH launch post | https://www.producthunt.com/posts/voicedumps |
| GitHub | https://github.com/heynaavi/voiceDump（MIT，42 commits，捕获时 ~5 stars / 1 fork） |
| 品类标签 | Mac · Productivity · Artificial Intelligence |
| 票数 / 评论 | 票数未知；评论 1（maker 仅一条，无第三方用户评论） |
| 公司主体 | 单人项目（官网页脚"a free one-person project"）；页脚品牌 KUPA（kupacreative.com），官方页面未出现"Qwee.ai"品牌 |
| 企业版/关联站点 | kupacreative.com（页脚品牌） |
| Maker | Naveen Upadhyay（PH @heynavi，GitHub heynaavi） |

## 是做什么的（如实复述，不评价）

macOS 本地语音转文字：按住 🌐（globe）键说话，松开后文字出现在任意应用的光标处（实现为剪贴板 + 模拟 ⌘V 粘贴，而非真实键入）。也可拖入音视频文件生成带时间戳的转写稿，支持随文编辑、字级播放跟随、导出 PDF/Markdown/纯文本。完全离线——两个量化 Whisper 模型打包在 app 内，"装完在飞机上都能用"。

## 解决什么问题（事实层面，不判断值不值得解）

- 云端听写有字数上限、语音要"往返别人的 GPU"（maker 自述动机）
- 需要离线/隐私场景：无账户、无 API key、不上传任何内容
- 会议/录音转写：本机两条音轨（麦克风 + 系统输出）区分"你/别人"，无需 bot 进会
- 转写稿需要检索/问答 → FTS5 全文搜索 + ASK 自然语言问答

## 怎么做的（技术原理/机制，事实层面）

- **技术栈**：Tauri v2 + React/Tailwind 前端；whisper.cpp（经 whisper-rs）Metal 加速、进程内推理；SQLite 历史；Swift `NSPanel` 辅助进程（Tauri webview 无法悬浮在全屏 Space 上）；Swift CoreAudio process tap 抓系统输出音轨；音频解码用 `symphonia`（转写路径无 ffmpeg）；Node + Rust + CMake 构建
- **模型**：两个量化 Whisper 模型打包（非 `.en`，支持多语言）——`ggml-small-q5_1`（190MB 磁盘/260MB 常驻）、`ggml-medium-q5_0`（539MB/601MB）；内存 ≥16GB 选 medium，否则 small（按内存而非芯片代数）；`VOICEDUMPS_MODEL_SIZE=small|medium` 可覆盖；首次运行下载约 720MB（或 190MB）到 `~/Library/Application Support/dev.heynaavi.voicedump/models`
- **延迟基准**（M1 Pro 16GB、macOS 27、8 线程、small 模型、12s 合成语音）：1.9s 话语中位 377ms/最差 415ms；5.8s 423/429ms；12.0s 898/974ms；冷缓存首载 9.7s，之后约 0.4s；claim 比 Wispr Flow 公布 p99（<700ms）快约 39%，但承认 >10 秒话语与困难音频云端更强；不做 LLM 重排，"给你你说的话"；独立验证脚本在 `scripts/bench.sh`
- **AI 功能**（仅 macOS 26 + Apple Intelligence）：自动标题、概览、行动项、ASK 自然语言问答（带引用，单次限 ~6 条录音 / 4096 token 设备端窗口）；其余功能 macOS 11+ 可用
- **数据/隐私**：SQLite 于 `…/voicedumps.db`；音频按月存 `…/media/`（afconvert 归一化 mono AAC）；听写草稿 WAV 在 `…/dictation/`，孤立超 1 天清理；无遥测、无崩溃上报、无更新检查；模型空闲 5 分钟释放（~512MB）
- **安装注意**：未公证（ad-hoc 签名），macOS 会提示"未验证应用"；一键 `curl | bash` 安装脚本（声称验签、免 sudo）或 `xattr -dr com.apple.quarantine /Applications/VoiceDumps.app`；需辅助功能（CGEventTap 监听 globe 键）+ 麦克风权限；需把系统"按 🌐 键"设为"无操作"，否则 emoji 面板会在 app 下方弹出

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Naveen Upadhyay（PH @heynavi），官方标注"一人项目" | PH 评论 + 官网 |
| 融资 | 未查到 | — |
| 投资方 | 未查到 | — |
| 加速器 | 未查到 | — |
| 合规认证 | 未查到 | — |

## 定价 / 商业模式

- **免费**：MIT 开源、无订阅、无账户、无 API key、无遥测、无 upsell（"没有付费层把你养上去"）
- 官方对比：Wispr Flow $15/月或 $144/年；VoiceDumps 免费且无字数限制
- 模式：开源免费（无付费层）

## 关联信息 / 生态

- 竞品对标：Wispr Flow（云端听写）
- 下载量（官网展示）：46 次（v1.0.0，5MB arm64 DMG，GitHub Releases）
- 已知缺口（README）：AI 功能需 macOS 26/Apple Intelligence；"make that an email"重排不可靠；roadmap：文件夹自动转写、音频增强、跨会议发言人识别、一键更新

## 技术时间线（官网里程碑，若有）

| 日期 | 事件 |
|---|---|
| 2026-08 上旬 | PH 上线；maker 评论时间戳约 5 天前 |

## 评论区反馈（事实摘录，不评价）

- Maker Naveen（约 5d 前）：动机 = 云端字数上限 + "语音到别人 GPU 的往返"；用 M1 Pro 三次运行最差 429ms 佐证本地延迟；向社区抛出 2 问：①720MB 下载（两个量化模型换离线）值不值；②仅 Apple Silicon 是否劝退
- 无用户评论

## 信息来源

- PH 产品页 + PH launch post：tagline、品类、maker 评论、GitHub 链接
- GitHub repo（README）：技术栈、模型选择、基准表、安装、权限、数据路径、AI 功能、roadmap
- 官网 voicedumps.qwee.ai：定价、下载量、未公证说明、KUPA 页脚、v1.0.0

## 未查到 / 待补

- 票数（archive 与 PH 页面抓取均未显示）
- Naveen Upadhyay 的公开背景/雇主
- 独立审计/第三方验证（官方未提）
- "Qwee.ai"与产品的确切关系（官方页面未出现该品牌）
