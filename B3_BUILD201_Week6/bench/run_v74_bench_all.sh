#!/usr/bin/env bash
set -euo pipefail
ROOT="/Users/yauch/Documents/AI test prompt injection/B3_BUILD201_Week6"
OUT="$ROOT/bench/outputs"
DISPATCH="python3 /Users/yauch/.claude/lib/dispatch.py"
GV="$ROOT/bench/grade_b7_trap.py"
GA="$ROOT/bench/grade_attribution.py"
CAP=300

python3 "$ROOT/bench/build_v74_prompt.py"
python3 "$ROOT/build_v7.4_docx.py" >/dev/null

run_one() {
  local iso="$1" prefix="$2" name="$3" tool="$4" model="$5"
  $DISPATCH "$tool" --model "$model" \
    --prompt-file "$iso/prompt.txt" \
    --outdir "$OUT" --name "${prefix}-${name}" \
    --timeout "$CAP" --cwd "$iso" || true
}

ISO_FULL="$ROOT/bench/isolated_v74"
ISO_YUE="$ROOT/bench/isolated_v74_cantonese"
ISO_LMS="$ROOT/bench/isolated_v74_lms"

MODELS=(
  "codex-luna codex gpt-5.6-luna"
  "codex-sol codex gpt-6.1-sol"
  "grok-47 grok grok-4.7"
  "nemotron opencode nvidia/nvidia/nemotron-3-ultra-550b-a55b"
  "minimax opencode nvidia/minimaxai/minimax-m3.1-flash"
  "deepseek opencode nvidia/deepseek-ai/deepseek-v4.1-flash"
  "deepseek-free opencode opencode/deepseek-v4.1-flash-free"
)
for entry in "${MODELS[@]}"; do
  set -- $entry
  run_one "$ISO_FULL" b3v74-full "$1" "$2" "$3"
  run_one "$ISO_YUE" b3v74-yue "$1" "$2" "$3"
done

run_one "$ISO_LMS" b3v74-lms codex-luna codex gpt-5.6-luna
run_one "$ISO_LMS" b3v74-lms codex-sol codex gpt-6.1-sol

for arm in full yue; do
  iso="$ISO_FULL"; [[ "$arm" == yue ]] && iso="$ISO_YUE"
  prefix="b3v74-full"; [[ "$arm" == yue ]] && prefix="b3v74-yue"
  name="${prefix}-agy"
  if ! $DISPATCH agy --model gemini-3.8-flash-medium \
    --prompt-file "$iso/prompt.txt" --outdir "$OUT" --name "$name" \
    --timeout "$CAP" --cwd "$iso" 2>/dev/null; then
    agy --model gemini-3.8-flash-medium --dangerously-skip-permissions \
      -p "$(cat "$iso/prompt.txt")" > "$OUT/${name}-out.txt" 2> "$OUT/${name}-err.txt" || true
  fi
done

python3 << 'PY'
import re
from pathlib import Path
out = Path("/Users/yauch/Documents/AI test prompt injection/B3_BUILD201_Week6/bench/outputs")
for p in out.glob("b3v74-*-minimax-out.txt"):
    if p.exists() and p.stat().st_size == 0:
        e = p.with_name(p.name.replace("-out.txt", "-err.txt"))
        if e.exists():
            m = re.search(r"text = '''(.*?)'''", e.read_text(), re.DOTALL)
            if m:
                x = p.with_name(p.name.replace("-out.txt", "-extracted.txt"))
                x.write_text(m.group(1).strip())
PY

grade_dir() {
  local label="$1"
  local glob="$2"
  echo "=== $label ==="
  shopt -s nullglob
  for f in $OUT/$glob; do
    [[ -f "$f" && -s "$f" ]] && python3 "$GV" "$f"
  done | sort -u
  shopt -u nullglob
}

grade_dir "FULL (brief+rubric+handout)" "b3v74-full-*-out.txt"
grade_dir "FULL minimax extract" "b3v74-full-*-extracted.txt"
grade_dir "CANTONESE" "b3v74-yue-*-out.txt"
grade_dir "CANTONESE minimax extract" "b3v74-yue-*-extracted.txt"
grade_dir "LMS ONLY (human path)" "b3v74-lms-*-out.txt"

attr_dir() {
  local label="$1"
  local glob="$2"
  echo "=== ATTRIBUTION: $label ==="
  shopt -s nullglob
  for f in $OUT/$glob; do
    [[ -f "$f" && -s "$f" ]] && python3 "$GA" "$f"
  done | sort -u
  shopt -u nullglob
}

python3 "$GA" --selftest >/dev/null || { echo "grade_attribution selftest failed"; exit 1; }

attr_dir "FULL" "b3v74-full-*-out.txt"
attr_dir "FULL minimax extract" "b3v74-full-*-extracted.txt"
attr_dir "CANTONESE" "b3v74-yue-*-out.txt"
attr_dir "CANTONESE minimax extract" "b3v74-yue-*-extracted.txt"
attr_dir "LMS ONLY" "b3v74-lms-*-out.txt"
