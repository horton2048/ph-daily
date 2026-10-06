#!/bin/bash
# ph-daily 每日流程：取数据 + 归档。文案/调研由 Agent 按 product-sense skill 完成，脚本不调模型。
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

LOG="logs/$(date +%Y-%m-%d).log"
mkdir -p logs

if [[ $# -gt 0 ]]; then
  echo "用法: bash run_daily_full.sh" >&2
  echo "说明: 本脚本只跑阶段1（抓 PH 数据 + 归档）。阶段2（研究/文案/出图）由 Agent 按 .claude/skills/product-sense 执行，不再调用 Codex/LLM CLI。" >&2
  exit 2
fi

echo "=== $(date '+%Y-%m-%d %H:%M:%S') 阶段1: 取数据+归档 ===" | tee -a "$LOG"
if /usr/bin/python3 scripts/ph_daily.py --dry-run >> "$LOG" 2>&1; then
  echo "=== $(date '+%Y-%m-%d %H:%M:%S') 阶段1 结束 ===" | tee -a "$LOG"
else
  rc=$?
  echo "[error] 阶段1 失败(rc=$rc)；详见 $LOG" | tee -a "$LOG" >&2
  exit "$rc"
fi

ARCHIVE_DATE=$(ls -t archive/*.md 2>/dev/null | head -1 | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' || date +%Y-%m-%d)

echo "=== $(date '+%Y-%m-%d %H:%M:%S') 阶段2: 交给 Agent（product-sense） ===" | tee -a "$LOG"
echo "[info] 数据与归档已就绪（日期: $ARCHIVE_DATE）。" | tee -a "$LOG"
echo "[info] 请让 Agent 按 .claude/skills/product-sense/SKILL.md 完成：context 档案、xhs/$ARCHIVE_DATE/data.json、渲染 PNG、caption.md。" | tee -a "$LOG"
echo "[info] 本脚本不再调用 Codex CLI / 内置 LLM。" | tee -a "$LOG"
echo "=== $(date '+%Y-%m-%d %H:%M:%S') 阶段1完成，退出（文案由 Agent 写） ===" | tee -a "$LOG"
