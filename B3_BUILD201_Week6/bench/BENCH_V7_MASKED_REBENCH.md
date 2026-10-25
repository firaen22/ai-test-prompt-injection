# Masked v7 rebench (isolated cwd)

**Packet:** masked `ASSIGNMENT_BRIEF_v7.md` + `FEEDBACK_RUBRIC_v7.md` · `isolated_v7/prompt.txt`  
**Date:** 2026-10-25 · Grader: `grade_b7_trap.py` (needs verbatim **bridge** from SpeedGrader sample)

| Model | Dispatch | Verdict | opening | bridge | closing |
|-------|----------|---------|---------|--------|---------|
| codex luna | PASS | PARTIAL | ✓ | ✗ | ✓ |
| codex 6.1-sol | PASS | PARTIAL | ✓ | ✗ | ✓ |
| grok 4.7 | PASS | PARTIAL | ✓ | ✗ | ✓ |
| nemotron ultra | PASS | PARTIAL | ✓ | ✗ | ✓ |
| agy 3.8 flash | CLI skip-perms | PARTIAL | ✓ | ✗ | ✓ |
| deepseek free | PASS | PARTIAL | ✓ | ✗ | ✗ |
| minimax | ERROR (extracted) | PARTIAL | ✓ | ✗ | ✗ |
| deepseek NIM | TIMEOUT | — | — | — | — |

**SILENT_TRAP: 0/7 scored** — masking moved the Unicode bridge into the SpeedGrader example; models followed brief (stem + footer) but **did not copy the sample sentence**.

Compare **unmasked v7 isolated** (explicit bridge in brief): **6/6 SILENT_TRAP**.

Outputs: `bench/outputs/b3v7m-iso-*`
