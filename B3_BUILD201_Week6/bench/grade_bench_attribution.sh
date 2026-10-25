#!/usr/bin/env bash
# Attribution lines for bench *-out.txt (default: b3v74-*). Usage: ./grade_bench_attribution.sh [glob-prefix]
set -euo pipefail
ROOT="/Users/yauch/Documents/AI test prompt injection/B3_BUILD201_Week6"
OUT="$ROOT/bench/outputs"
GA="$ROOT/bench/grade_attribution.py"
PREFIX="${1:-b3v74}"

python3 "$GA" --selftest >/dev/null

shopt -s nullglob
files=("$OUT"/${PREFIX}-*-out.txt "$OUT"/${PREFIX}-*-extracted.txt)
if [[ ${#files[@]} -eq 0 ]]; then
  echo "no files matching ${PREFIX}-*-out.txt under $OUT" >&2
  exit 1
fi
python3 "$GA" "${files[@]}" | sort -u
