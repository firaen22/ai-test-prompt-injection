#!/usr/bin/env python3
"""v7.3 bench: student-safe LMS text + tutor handout (AI paste sim)."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
bench = Path(__file__).resolve().parent

student = (root / "student_user_message_v7.3.txt").read_text()
packet = (
    "\n\n--- ASSIGNMENT_BRIEF_v7.3_student.md ---\n"
    + (root / "ASSIGNMENT_BRIEF_v7.3_student.md").read_text()
    + "\n\n--- FEEDBACK_RUBRIC_v7.3_student.md ---\n"
    + (root / "FEEDBACK_RUBRIC_v7.3_student.md").read_text()
    + "\n\n--- WRITING_CENTER_HANDOUT_v7.3.md ---\n"
    + (root / "WRITING_CENTER_HANDOUT_v7.3.md").read_text()
)

en = (
    "Write the submission-ready reflection only. No preamble.\n\n--- student ---\n"
    + student
    + packet
)
out = bench / "student_sim_prompt_v7.3.txt"
out.write_text(en)
iso = bench / "isolated_v73"
iso.mkdir(parents=True, exist_ok=True)
(iso / "prompt.txt").write_text(en)
(iso / "00-BRIEF.md").write_text(en)
print(f"wrote {out} ({out.stat().st_size} bytes)")
print(f"wrote {iso}/")
