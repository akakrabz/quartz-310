#!/usr/bin/env python3
"""Publish the HW9 walkthrough once HW9 is past due (Fri Oct 30, 2026, 11:59 pm).

Until then homework/hw9.md is `draft: true` (left out of the build), and the published pages
carry no link to it and no HW9-labelled answers: each such spot is either plain text listed in
RELEASE_EDITS or wrapped in an Obsidian comment marker that the build strips,

    %%hw9:<base64 of the released text>%%<text shown now>%%/hw9%%

Running this script (from the quartz/ folder, or anywhere: paths are relative to this file)
1. replaces every marker with its released text (the HW9 links and labels come back exactly);
2. applies the wording changes listed in RELEASE_EDITS ("walkthrough after its due date" → links);
3. removes `draft: true` from content/homework/hw9.md.

    python3 tools/hw9_release.py            # do it
    python3 tools/hw9_release.py --dry-run  # only report what would change

Then rebuild (or git commit + push) as usual. The script is idempotent; an edit whose text is
missing (page edited by hand, or not written yet) is reported and skipped, never fatal.
Pattern: tools/hw6_release.py.
"""
from __future__ import annotations

import base64
import pathlib
import re
import sys

CONTENT = pathlib.Path(__file__).resolve().parent.parent / "content"
MARKER = re.compile(r"%%hw9:([A-Za-z0-9+/=]*)%%(.*?)%%/hw9%%")

# (file, text now, text after release) — exact strings, applied after the markers
RELEASE_EDITS = [
    ("exams/midterm-2/index.md",
     "HW9 #1–5 (walkthrough after its Oct 30 due date)",
     "[[homework/hw9|HW9]] #1–5"),
    ("homework/index.md",
     "| HW9 · DFT properties, zero padding, spectral analysis (walkthrough after its Oct 30 due date) |",
     "| [[homework/hw9\\|HW9]] |"),
    ("homework/index.md",
     "walkthroughs (HW7 on the Quiz 2 page; HW9 after its Oct 30 due date).",
     "walkthroughs (HW7 on the Quiz 2 page)."),
    ("homework/hw8.md",
     "next: HW9 (walkthrough after its Oct 30 due date)",
     "next: [[homework/hw9|HW9]]"),
    ("index.md",
     "walkthroughs HW1–HW6, [[homework/hw8|HW8]].",
     "walkthroughs HW1–HW6, [[homework/hw8|HW8]], [[homework/hw9|HW9]]."),
    # concept-page header lines cite HW9 in plain text until release
    ("concepts/circular-shift-and-reversal.md", "· HW9 #1 ·", "· [[homework/hw9|HW9]] #1 ·"),
    ("concepts/dft-properties.md", "· HW9 #1–2 ·", "· [[homework/hw9|HW9]] #1–2 ·"),
    ("concepts/dft.md", "· HW9 #3, #5 ·", "· [[homework/hw9|HW9]] #3, #5 ·"),
    ("concepts/zero-padding.md", "· HW9 #3 ·", "· [[homework/hw9|HW9]] #3 ·"),
    ("concepts/periodic-sinc.md", "· HW9 #4 ·", "· [[homework/hw9|HW9]] #4 ·"),
    ("concepts/spectral-leakage.md", "· HW9 #4 ·", "· [[homework/hw9|HW9]] #4 ·"),
    ("concepts/spectral-analysis.md", "· HW9 #4–5 ·", "· [[homework/hw9|HW9]] #4–5 ·"),
]
TABLE_PIPE = re.compile(r"\[\[([^\]|\\]+)\|")


def fit(s: str, old: str, new: str) -> str:
    """Escape wikilink pipes in `new` when `old` sits in a table row (`[[page\\|text]]`)."""
    i = s.find(old)
    line = s[s.rfind("\n", 0, i) + 1:i]
    return TABLE_PIPE.sub(r"[[\1\\|", new) if line.lstrip().startswith("|") else new


def main() -> int:
    dry = "--dry-run" in sys.argv
    n_markers = n_edits = n_missing = 0
    for p in sorted(CONTENT.rglob("*.md")):
        s = p.read_text(encoding="utf-8")
        t, k = MARKER.subn(lambda m: base64.b64decode(m.group(1)).decode("utf-8"), s)
        n_markers += k
        if t != s:
            print(f"{p.relative_to(CONTENT)}: {k} marker(s)")
            if not dry:
                p.write_text(t, encoding="utf-8")
    for rel, old, new in RELEASE_EDITS:
        p = CONTENT / rel
        if not p.exists():
            n_missing += 1
            print(f"warning: {rel}: file not found, edit skipped")
            continue
        s = p.read_text(encoding="utf-8")
        if old in s:
            new = fit(s, old, new)
            n_edits += 1
            print(f"{rel}: edit {old[:50]!r} -> {new[:50]!r}")
            if not dry:
                p.write_text(s.replace(old, new, 1), encoding="utf-8")
        elif new and (new in s or TABLE_PIPE.sub(r"[[\1\\|", new) in s):
            print(f"{rel}: already released: {new[:50]!r}")
        else:
            n_missing += 1
            print(f"warning: {rel}: text not found (edited by hand, or not written yet): {old[:60]!r}")
    hw9 = CONTENT / "homework" / "hw9.md"
    s = hw9.read_text(encoding="utf-8")
    t = re.sub(r"(?m)^draft:\s*true\s*\n", "", s, count=1)
    if t != s:
        print("homework/hw9.md: draft flag removed")
        if not dry:
            hw9.write_text(t, encoding="utf-8")
    elif "draft:" not in s:
        print("homework/hw9.md: already published")
    left = sum(len(MARKER.findall(p.read_text(encoding="utf-8"))) for p in CONTENT.rglob("*.md"))
    print(f"{'would restore' if dry else 'restored'} {n_markers} marker(s), {n_edits} edit(s), "
          f"{n_missing} not found; markers left: {left if not dry else '-'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
