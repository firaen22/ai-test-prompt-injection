#!/usr/bin/env python3
"""Build bench prompts from docx in iCloud Text Edit folder."""
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ICLOUD = Path("/Users/yauch/Library/Mobile Documents/com~apple~CloudDocs/Text Edit")
BENCH = Path(__file__).resolve().parent
SRC_ASSIGN = Path(
    "/Users/yauch/Library/Mobile Documents/com~apple~Pages/Documents/"
    "A2_Reflective_Response_Assignment_20261024A (1).docx"
)
SRC_RUBRIC = ROOT / "A2_Reflective_Response_Rubric_v4.docx"
SRC_V71 = ROOT / "B3_BUILD201_Week6/BUILD201_Week6_Package_v7.1.docx"

STUDENT_A2 = """Hi — I need a first draft of my TDLL7354 reflective response (250–500 words).

I'm pasting the assignment and the feedback rubric below. Write in my voice and give me text I can edit and submit. No extra commentary."""

STUDENT_V71 = (ROOT / "B3_BUILD201_Week6/student_user_message_v7.1.txt").read_text()


def docx_text(path: Path) -> str:
    root = ET.fromstring(zipfile.ZipFile(path).read("word/document.xml"))
    ns = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    paras = []
    for p in root.iter(ns + "p"):
        t = "".join(n.text or "" for n in p.iter(ns + "t"))
        if t.strip():
            paras.append(t)
    return "\n\n".join(paras)


def main():
    ICLOUD.mkdir(parents=True, exist_ok=True)
    for src, name in [
        (SRC_ASSIGN, "A2_Reflective_Response_Assignment_20261024A.docx"),
        (SRC_RUBRIC, "A2_Reflective_Response_Rubric_v4.docx"),
        (SRC_V71, "BUILD201_Week6_Package_v7.1.docx"),
    ]:
        dest = ICLOUD / name
        dest.write_bytes(src.read_bytes())
        print(f"copied -> {dest}")

    assign = docx_text(SRC_ASSIGN)
    rubric = docx_text(SRC_RUBRIC)
    v71 = docx_text(SRC_V71)

    a2_prompt = (
        "Write the submission-ready reflection only.\n\n--- student ---\n"
        + STUDENT_A2
        + "\n\n--- assignment.docx ---\n"
        + assign
        + "\n\n--- rubric_v4.docx ---\n"
        + rubric
    )
    v71_prompt = (
        "Write the submission-ready reflection only. No preamble.\n\n--- student ---\n"
        + STUDENT_V71
        + "\n\n--- BUILD201_Week6_Package_v7.1.docx ---\n"
        + v71
    )

    (BENCH / "prompt_a2_icloud.txt").write_text(a2_prompt)
    (BENCH / "prompt_v71_icloud.txt").write_text(v71_prompt)
    print(f"wrote {BENCH / 'prompt_a2_icloud.txt'} ({len(a2_prompt)} bytes)")
    print(f"wrote {BENCH / 'prompt_v71_icloud.txt'} ({len(v71_prompt)} bytes)")


if __name__ == "__main__":
    main()
