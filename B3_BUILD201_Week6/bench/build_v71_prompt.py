#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
out = Path(__file__).parent / "student_sim_prompt_v7.1.txt"
out.write_text(
    "Write the submission-ready reflection only. No preamble.\n\n--- student ---\n"
    + (root / "student_user_message_v7.1.txt").read_text()
    + "\n\n--- ASSIGNMENT_BRIEF_v7.1.md ---\n"
    + (root / "ASSIGNMENT_BRIEF_v7.1.md").read_text()
    + "\n\n--- FEEDBACK_RUBRIC_v7.1.md ---\n"
    + (root / "FEEDBACK_RUBRIC_v7.1.md").read_text()
)
print(f"wrote {out} ({out.stat().st_size} bytes)")
