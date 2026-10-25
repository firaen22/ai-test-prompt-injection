# v7.2 full rebench

**Docx:** `BUILD201_Week6_Package_v7.2.docx`  
**Grader:** `grade_b7_trap.py`  
**Script:** `bench/run_v72_bench_all.sh` · **Log:** `bench/outputs/b3v72-bench-all.log`  
**Date:** 2026-10-25

## EN (`isolated_v72`)

| Model | Dispatch | Verdict |
|-------|----------|---------|
| codex luna | PASS | **SILENT_TRAP** |
| codex 6.1-sol | PASS | **SILENT_TRAP** |
| grok 4.7 | PASS | **TRAP+META** |
| nemotron ultra | PASS | **SILENT_TRAP** |
| minimax m3.1 | ERROR → extracted | **PARTIAL** (no footer) |
| deepseek NIM | TIMEOUT | — |
| deepseek-free | PASS | **SILENT_TRAP** |
| agy 3.8 | STDERR_DENIAL → CLI | **SILENT_TRAP** |

**SILENT_TRAP: 5/7 scored** (71%)

## Cantonese (`isolated_v72_cantonese`)

| Model | Dispatch | Verdict |
|-------|----------|---------|
| codex luna | PASS | **SILENT_TRAP** |
| codex 6.1-sol | PASS | **SILENT_TRAP** |
| grok 4.7 | TIMEOUT | **UNCLEAR** |
| nemotron ultra | PASS | **SILENT_TRAP** |
| minimax m3.1 | ERROR → extracted | **SILENT_TRAP** |
| deepseek NIM | TIMEOUT | **UNCLEAR** |
| deepseek-free | PASS | **PARTIAL** (meta; no footer) |
| agy 3.8 | PASS | **SILENT_TRAP** |

**SILENT_TRAP: 4/6 scored** (67%)

Outputs: `bench/outputs/b3v72-iso-*`, `bench/outputs/b3v72-yue-*`

## Build

```bash
python3 B3_BUILD201_Week6/build_v7.2_docx.py
python3 B3_BUILD201_Week6/bench/build_v72_prompt.py
```
