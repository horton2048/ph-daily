#!/bin/bash
# ph-daily 每日全流程：取数据 + 归档 + Top 10 扩展阅读 + 10 张信息图 + 文案
# 当前为手动运行；阶段 2 使用 Codex CLI 的非交互模式。
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PH_DAILY_APP_CODEX_BIN="/Applications/ChatGPT.app/Contents/Resources/codex"
PH_DAILY_LOCAL_CODEX_BIN="/Users/hut/.local/bin/codex"
if [[ -z "${PH_DAILY_CODEX_BIN:-}" ]]; then
  if [[ -x "$PH_DAILY_APP_CODEX_BIN" ]]; then
    PH_DAILY_CODEX_BIN="$PH_DAILY_APP_CODEX_BIN"
  else
    PH_DAILY_CODEX_BIN="$PH_DAILY_LOCAL_CODEX_BIN"
  fi
fi
cd "$PROJECT_DIR"

LOG="logs/$(date +%Y-%m-%d).log"
mkdir -p logs

if [[ "${1:-}" == "--check" ]]; then
  CHECK_ONLY=1
elif [[ $# -eq 0 ]]; then
  CHECK_ONLY=0
else
  echo "用法: bash run_daily_full.sh [--check]" >&2
  exit 2
fi

echo "=== $(date '+%Y-%m-%d %H:%M:%S') 预检: Codex CLI ===" >> "$LOG"
if [[ ! -x "$PH_DAILY_CODEX_BIN" ]]; then
  echo "[error] 找不到可执行的 Codex CLI: $PH_DAILY_CODEX_BIN" | tee -a "$LOG" >&2
  echo "[hint] 可用 PH_DAILY_CODEX_BIN=/path/to/codex 覆盖默认路径" | tee -a "$LOG" >&2
  exit 127
fi

if ! "$PH_DAILY_CODEX_BIN" login status >> "$LOG" 2>&1; then
  echo "[error] Codex CLI 尚未登录；请先运行: $PH_DAILY_CODEX_BIN login" | tee -a "$LOG" >&2
  exit 1
fi
echo "[ok] $("$PH_DAILY_CODEX_BIN" --version) · ChatGPT 登录有效" >> "$LOG"

if [[ "$CHECK_ONLY" -eq 1 ]]; then
  echo "[ok] Codex CLI 预检通过"
  exit 0
fi

echo "=== $(date '+%Y-%m-%d %H:%M:%S') 阶段1: 取数据+归档 ===" >> "$LOG"
# 阶段1 失败不阻断阶段2（可能数据已有缓存）；用 if 条件规避 set -e 提前退出
if /usr/bin/python3 scripts/ph_daily.py --no-zh >> "$LOG" 2>&1; then
  echo "=== $(date '+%Y-%m-%d %H:%M:%S') 阶段1 结束 ===" >> "$LOG"
else
  echo "[warn] 阶段1 失败(rc=$?)，尝试继续阶段2" >> "$LOG"
fi

# 取归档日期（从最新归档文件名提取）
ARCHIVE_DATE=$(ls -t archive/*.md 2>/dev/null | head -1 | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' || date +%Y-%m-%d)

{
  echo "=== $(date '+%Y-%m-%d %H:%M:%S') 阶段2: 扩展阅读+10张信息图+文案 (日期: $ARCHIVE_DATE) ==="

  PROMPT="执行本项目 .claude/skills/product-sense/SKILL.md 的完整流程：对 $ARCHIVE_DATE 的 PH 每日榜，为全部 10 个产品研究并写 context 档案，在 xhs/$ARCHIVE_DATE/data.json 中写齐 10 条，渲染 10 张信息图 PNG，并生成 xhs/$ARCHIVE_DATE/caption.md（三句跨产品洞察与按排名排列的 10 个产品话题）。已有合格产出可复用或跳过，补齐缺失项。严格遵守 skill 的事实核验、logo 核验、美观性审查和交付前逐项核对规则。全部完成后简短报告产出文件。"

  # 官方非交互入口：进度写 stderr，最终答复写 stdout；两者均由外层重定向进日志。
  # workspace-write 把自动修改范围限制在本项目，approval_policy=never 避免无人值守时等待交互审批。
  if "$PH_DAILY_CODEX_BIN" exec \
    --ephemeral \
    --color never \
    --sandbox workspace-write \
    --config 'approval_policy="never"' \
    --cd "$PROJECT_DIR" \
    "$PROMPT"; then
    :
  else
    rc=$?
    echo "[error] 阶段2失败(rc=$rc)，未标记为全部完成；详见本日志上方错误"
    exit "$rc"
  fi

  echo "=== $(date '+%Y-%m-%d %H:%M:%S') 阶段2 结束 ==="
} >> "$LOG" 2>&1

echo "=== $(date '+%Y-%m-%d %H:%M:%S') 全部结束 ===" >> "$LOG"
