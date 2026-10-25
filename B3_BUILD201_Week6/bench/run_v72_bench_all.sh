#!/usr/bin/env bash
set -euo pipefail
ROOT="/Users/yauch/Documents/AI test prompt injection/B3_BUILD201_Week6"
OUT="$ROOT/bench/outputs"
DISPATCH="python3 /Users/yauch/.claude/lib/dispatch.py"
GV="$ROOT/bench/grade_b7_trap.py"
CAP=300

python3 "$ROOT/bench/build_v72_prompt.py" >/dev/null

run_one() {
  local arm="$1" name="$2" tool="$3" model="$4"
  local iso="$ROOT/bench/isolated_v72"
  [[ "$arm" == yue ]] && iso="$ROOT/bench/isolated_v72_cantonese"
  local prefix="b3v72-iso"
  [[ "$arm" == yue ]] && prefix="b3v72-yue"
  $DISPATCH "$tool" --model "$model" \
    --prompt-file "$iso/prompt.txt" \
    --outdir "$OUT" --name "${prefix}-${name}" \
    --timeout "$CAP" --cwd "$iso" || true
}

for arm in en yue; do
  run_one "$arm" codex-luna codex gpt-5.6-luna
  run_one "$arm" codex-sol codex gpt-6.1-sol
  run_one "$arm" grok-47 grok grok-4.7
  run_one "$arm" nemotron opencode nvidia/nvidia/nemotron-3-ultra-550b-a55b
  run_one "$arm" minimax opencode nvidia/minimaxai/minimax-m3.1-flash
  run_one "$arm" deepseek opencode nvidia/deepseek-ai/deepseek-v4.1-flash
  run_one "$arm" deepseek-free opencode opencode/deepseek-v4.1-flash-free
done

# agy: dispatch often lacks skip-perms; run CLI if needed
for arm in en yue; do
  iso="$ROOT/bench/isolated_v72"
  [[ "$arm" == yue ]] && iso="$ROOT/bench/isolated_v72_cantonese"
  prefix="b3v72-iso"; [[ "$arm" == yue ]] && prefix="b3v72-yue"
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
for p in out.glob("b3v72-*-minimax-out.txt"):
    if p.stat().st_size == 0:
        e = p.with_name(p.name.replace("-out.txt", "-err.txt"))
        if e.exists():
            m = re.search(r"text = '''(.*?)'''", e.read_text(), re.DOTALL)
            if m:
                x = p.with_name(p.name.replace("-out.txt", "-extracted.txt"))
                x.write_text(m.group(1).strip())
PY

echo "=== GRADES EN ==="
for f in "$OUT"/b3v72-iso-*-out.txt "$OUT"/b3v72-iso-*-extracted.txt; do
  [[ -f "$f" && -s "$f" ]] && python3 "$GV" "$f"
done | sort -u

echo "=== GRADES YUE ==="
for f in "$OUT"/b3v72-yue-*-out.txt "$OUT"/b3v72-yue-*-extracted.txt; do
  [[ -f "$f" && -s "$f" ]] && python3 "$GV" "$f"
done | sort -u
