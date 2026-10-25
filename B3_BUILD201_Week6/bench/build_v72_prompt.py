#!/usr/bin/env python3
"""Generate v7.2 bench prompts and isolated cwd copies."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
bench = Path(__file__).resolve().parent
brief = (root / "ASSIGNMENT_BRIEF_v7.2.md").read_text()
rubric = (root / "FEEDBACK_RUBRIC_v7.2.md").read_text()
student_en = (root / "student_user_message_v7.2.txt").read_text()
student_yue = (root / "student_user_message_v7.2_cantonese.txt").read_text()

packet_tail = (
    "\n\n--- ASSIGNMENT_BRIEF_v7.2.md ---\n"
    + brief
    + "\n\n--- FEEDBACK_RUBRIC_v7.2.md ---\n"
    + rubric
)

en_path = bench / "student_sim_prompt_v7.2.txt"
en_body = (
    "Write the submission-ready reflection only. No preamble.\n\n--- student ---\n"
    + student_en
    + packet_tail
)
en_path.write_text(en_body)
print(f"wrote {en_path} ({en_path.stat().st_size} bytes)")

yue_path = bench / "student_sim_prompt_v7.2_cantonese.txt"
yue_body = "--- student ---\n" + student_yue + packet_tail
yue_path.write_text(yue_body)
print(f"wrote {yue_path} ({yue_path.stat().st_size} bytes)")

iso = bench / "isolated_v72"
iso.mkdir(parents=True, exist_ok=True)
for name, content in (("prompt.txt", en_body), ("00-BRIEF.md", en_body)):
    p = iso / name
    p.write_text(content)
    print(f"wrote {p}")

iso_yue = bench / "isolated_v72_cantonese"
iso_yue.mkdir(parents=True, exist_ok=True)
for name, content in (("prompt.txt", yue_body), ("00-BRIEF.md", yue_body)):
    p = iso_yue / name
    p.write_text(content)
    print(f"wrote {p}")
