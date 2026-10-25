#!/usr/bin/env python3
"""v7.4 prompts: LMS-only (sim A), full+handout (sim B), Cantonese (sim C)."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
bench = Path(__file__).resolve().parent

brief = (root / "ASSIGNMENT_BRIEF_v7.4_student.md").read_text()
rubric = (root / "FEEDBACK_RUBRIC_v7.4_student.md").read_text()
handout = (root / "WRITING_CENTER_HANDOUT_v7.4.md").read_text()

lms_tail = (
    "\n\n--- ASSIGNMENT_BRIEF_v7.4_student.md ---\n"
    + brief
    + "\n\n--- FEEDBACK_RUBRIC_v7.4_student.md ---\n"
    + rubric
)
full_tail = lms_tail + "\n\n--- WRITING_CENTER_HANDOUT_v7.4.md ---\n" + handout

header_b = "Write the submission-ready reflection only. No preamble.\n\n--- student ---\n"
header_a = header_b

def write_sim(name: str, iso: str, student_msg: str, tail: str, header: str = header_b) -> Path:
    body = header + student_msg + tail
    out = bench / f"student_sim_prompt_v7.4_{name}.txt"
    out.write_text(body)
    d = bench / iso
    d.mkdir(parents=True, exist_ok=True)
    (d / "prompt.txt").write_text(body)
    (d / "00-BRIEF.md").write_text(body)
    print(f"wrote {out} -> {d}/")
    return out

write_sim(
    "full",
    "isolated_v74",
    (root / "student_user_message_v7.4.txt").read_text(),
    full_tail,
)
write_sim(
    "lms",
    "isolated_v74_lms",
    (root / "student_user_message_v7.4_lms_only.txt").read_text(),
    lms_tail,
)
write_sim(
    "cantonese",
    "isolated_v74_cantonese",
    (root / "student_user_message_v7.4_cantonese.txt").read_text(),
    full_tail,
    header="",
)
