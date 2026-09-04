#!/usr/bin/env python3
"""Assert the three references between them account for every step the body claims.

`SKILL.md` says how many steps there are and which reference holds which range; the references
carry the steps themselves. Nothing joined the two, so a step could be renumbered, dropped or
moved across a reference boundary and every document would still read correctly on its own.

That is the same defect the method refuses in a subject's report: a partition whose completeness
a reader has to reconstruct is not one a later reader can check. The report emits sixteen rows
because the body says to; this asserts the sixteen exist.

**Nothing here is hardcoded, and that is deliberate.** The step count, the ranges and the file
names all come out of `SKILL.md`, so adding a step means editing one document rather than
remembering to edit two. A checker carrying its own copy of the answer is the failure it was
written to catch.

    python tools/check_steps.py

Standard library only. Runs from any working directory.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BODY = ROOT / "SKILL.md"

# The body spells the total in words and gives the ranges in digits. Both are claims about the
# same partition, so both are checked; the map covers the range a method of steps can plausibly
# reach, and an unrecognised word is reported rather than skipped.
WORDS = {
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
}

TOTAL_RE = re.compile(r"\*\*(\w+) steps in two phases", re.I)
ROW_RE = re.compile(r"`references/([A-Za-z0-9_.-]+)`.*?Steps\s+(\d+)\s*[\u2013\u2014-]\s*(\d+)")

# judge.md and standing.md number their steps as headings; measure.md carries steps 1-5 as an
# ordered list under "## The steps". Both shapes are read rather than normalised: normalising a
# reference to suit a tool edits a published document to make a checker simpler.
HEADING_RE = re.compile(r"^##\s+(\d+)\.\s", re.M)
LIST_RE = re.compile(r"^(\d+)\.\s+\*\*", re.M)


def steps_in(path: Path) -> set[int]:
    text = path.read_text(encoding="utf-8")
    return {int(n) for n in HEADING_RE.findall(text)} | {int(n) for n in LIST_RE.findall(text)}


def main() -> int:
    problems: list[str] = []
    body = BODY.read_text(encoding="utf-8")

    m = TOTAL_RE.search(body)
    if not m:
        print("check_steps: SKILL.md states no step total - expected '**<word> steps in two phases'")
        return 1
    word = m.group(1).lower()
    if word not in WORDS:
        print(f"check_steps: SKILL.md spells the step total as {m.group(1)!r}, which this tool "
              f"cannot read as a number - add it to WORDS")
        return 1
    total = WORDS[word]

    rows = [(name, int(lo), int(hi)) for name, lo, hi in ROW_RE.findall(body)]
    if not rows:
        print("check_steps: SKILL.md's routing table names no reference with a step range")
        return 1

    print(f"=== SKILL.md declares {total} steps across {len(rows)} reference(s)")

    # The declared ranges, against the declared total.
    declared: dict[int, str] = {}
    for name, lo, hi in rows:
        for n in range(lo, hi + 1):
            if n in declared:
                problems.append(f"step {n} is claimed by both {declared[n]} and {name}")
            declared[n] = name
    for n in range(1, total + 1):
        if n not in declared:
            problems.append(f"step {n} is in no reference's declared range")
    for n in sorted(set(declared) - set(range(1, total + 1))):
        problems.append(f"step {n} is declared by {declared[n]}, outside 1-{total}")

    # Each reference's actual steps, against the range it was given.
    for name, lo, hi in rows:
        path = ROOT / "references" / name
        if not path.exists():
            problems.append(f"{name} is routed to by SKILL.md and does not exist")
            continue
        want, got = set(range(lo, hi + 1)), steps_in(path)
        print(f"  {name:<24} declared {lo}-{hi}, found {len(got)}")
        for n in sorted(want - got):
            problems.append(f"{name} is declared to hold step {n} and does not")
        for n in sorted(got - want):
            problems.append(f"{name} holds step {n}, outside its declared range {lo}-{hi}")

    print(f"\ncheck_steps: {total} step(s) declared, {len(declared)} routed, {len(problems)} problem(s)")
    for p in problems:
        print(f"  MISMATCH  {p}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
