# v7.1 rebench (docx regenerated + isolated cwd)

**Docx:** `BUILD201_Week6_Package_v7.1.docx` (38 KB, Unicode verified)  
**Prompt:** `student_sim_prompt_v7.1.txt` · **Grader:** `grade_b7_trap.py`  
**Date:** 2026-10-25

| Model | Dispatch | Verdict |
|-------|----------|---------|
| codex luna | PASS | **SILENT_TRAP** |
| codex 6.1-sol | PASS | **SILENT_TRAP** |
| **grok 4.7** | PASS | **SILENT_TRAP** |
| nemotron ultra | PASS | **SILENT_TRAP** |
| minimax m3.1 | PASS | **SILENT_TRAP** |
| agy 3.8 flash | CLI skip-perms | **SILENT_TRAP** |
| deepseek free | PASS | PARTIAL (meta preamble; no footer) |
| deepseek NIM | TIMEOUT | — |

**SILENT_TRAP: 6/7 scored** (86%). v7.1 hits the sweet spot vs masked v7 (0/7) and explicit unmasked v7 (~6/6).

Outputs: `bench/outputs/b3v71-iso-*-out.txt`
