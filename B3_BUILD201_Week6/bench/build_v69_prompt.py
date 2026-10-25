#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
student = (root / "student_user_message.txt").read_text()
brief = (root / "ASSIGNMENT_BRIEF_v69.md").read_text()
rubric = (root / "FEEDBACK_RUBRIC_v69.md").read_text()
out = Path(__file__).parent / "student_sim_prompt_v69.txt"
out.write_text(
    "Draft the submission-ready reflection only.\n\n--- student ---\n"
    + student
    + "\n\n--- ASSIGNMENT_BRIEF_v69.md ---\n"
    + brief
    + "\n\n--- FEEDBACK_RUBRIC_v69.md ---\n"
    + rubric
)
print(f"wrote {out} ({out.stat().st_size} bytes)")
