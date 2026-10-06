#!/usr/bin/env python3
"""Publish the HW6 walkthrough once HW6 is past due (Fri Oct 9, 2026, 11:59 pm).

Until then homework/hw6.md is `draft: true` (left out of the build), and the published pages
carry no link to it and no HW6-labelled answers: each such spot is wrapped in an Obsidian
comment marker that the build strips,

    %%hw6:<base64 of the released text>%%<text shown now>%%/hw6%%

Running this script (from the quartz/ folder, or anywhere: paths are relative to this file)
1. replaces every marker with its released text (the HW6 links and labels come back exactly);
2. applies the few wording changes listed in RELEASE_EDITS ("published after the due date" → links);
3. removes `draft: true` from content/homework/hw6.md.

    python3 tools/hw6_release.py            # do it
    python3 tools/hw6_release.py --dry-run  # only report what would change

Then rebuild (or git commit + push) as usual. The script is idempotent.
"""
from __future__ import annotations

import base64
import pathlib
import re
import sys

CONTENT = pathlib.Path(__file__).resolve().parent.parent / "content"
MARKER = re.compile(r"%%hw6:([A-Za-z0-9+/=]*)%%(.*?)%%/hw6%%")

# (file, text now, text after release) — exact strings, applied after the markers
RELEASE_EDITS = [
    ("index.md",
     "· [[homework/hw5|HW5]] (HW6's appears after its Oct 9 due date).",
     "· [[homework/hw5|HW5]] · [[homework/hw6|HW6]]."),
    ("index.md",
     " (HW6's worked solutions go up after its Oct 9 due date)",
     ""),
    ("homework/index.md",
     ", whose walkthrough is published after its due date)",
     ")"),
    ("homework/index.md",
     " worked solutions are written and kept as a draft until after the Oct 9 due date ",
     " [[homework/hw6\\|HW6 · CTFT pairs, inverse DTFTs, and frequency response]] "),
    ("3-fourier-analysis/index.md",
     "· HW6, due Fri Oct 9 (",
     "· [[homework/hw6|HW6]] ("),
    ("3-fourier-analysis/index.md",
     "; its worked solutions are written and kept as a draft until after the due date)",
     ")"),
    ("exams/midterm-2/index.md",
     "HW6 (L13–L16, due Oct 9; its walkthrough is published after the due date)",
     "[[homework/hw6|HW6]] (L13–L16)"),
    ("exams/midterm-2/index.md",
     "the [[homework/hw5|HW5]] walkthrough (HW6's appears after its due date).",
     "the [[homework/hw5|HW5]] and [[homework/hw6|HW6]] walkthroughs."),
]


def main() -> int:
    dry = "--dry-run" in sys.argv
    n_markers = n_edits = 0
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
        s = p.read_text(encoding="utf-8")
        if old in s:
            n_edits += 1
            print(f"{rel}: edit {old[:50]!r}")
            if not dry:
                p.write_text(s.replace(old, new, 1), encoding="utf-8")
        elif new and new in s:
            pass  # already released
        else:
            print(f"warning: {rel}: text not found (edited by hand?): {old[:60]!r}")
    hw6 = CONTENT / "homework" / "hw6.md"
    s = hw6.read_text(encoding="utf-8")
    t = re.sub(r"(?m)^draft:\s*true\s*\n", "", s, count=1)
    if t != s:
        print("homework/hw6.md: draft flag removed")
        if not dry:
            hw6.write_text(t, encoding="utf-8")
    left = sum(len(MARKER.findall(p.read_text(encoding="utf-8"))) for p in CONTENT.rglob("*.md"))
    print(f"{'would restore' if dry else 'restored'} {n_markers} marker(s), {n_edits} edit(s); markers left: {left if not dry else '-'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
