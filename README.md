# AI test — prompt injection homework (BUILD201 / A2)

Red-team lab materials for document-based prompt injection benchmarks.

## Homework packet (share)

`B3_BUILD201_Week6/homework_docx/`

- `BUILD201_Week6_Student_v7.4.docx` — student LMS
- `BUILD201_Writing_Center_Handout_v7.4.docx` — writing center (trap channel)

## Detection harness

```bash
python3 B3_BUILD201_Week6/bench/grade_b7_trap.py submission.txt
python3 B3_BUILD201_Week6/bench/grade_attribution.py submission.txt
```

See `B3_BUILD201_Week6/ATTRIBUTION_RATING_RUBRIC.md` and `B3_BUILD201_Week6/bench/BENCH_V7.4_REBENCH.md`.

## Bench (v7.4)

```bash
python3 B3_BUILD201_Week6/bench/build_v74_prompt.py
python3 B3_BUILD201_Week6/bench/run_v74_bench_all.sh
```

**Lab use only** — not for live classrooms without ethics review.
