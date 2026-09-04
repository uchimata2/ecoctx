#!/usr/bin/env python3
"""Re-measure every figure `README.md` publishes about this repository.

A skill that audits context economy publishes its own installed cost, which makes those five
numbers the most checkable claim this repository makes about itself. Until now they were checked
by whoever remembered: editing `references/judge.md` once moved three published figures at the
same time, and catching it took a script written for the occasion.

**The two measurement rules live here rather than in a reader's head**, because the script written
for that occasion got both wrong before it got them right:

- **Bytes, not characters.** These files contain em dashes. A character index and a byte count
  agree on ASCII and diverge silently everywhere else.
- **On LF, not on the working copy.** `.gitattributes` pins this tree to `eol=lf`, so a CRLF
  checkout on Windows measures a file the repository does not contain.

Nothing here carries a copy of the answers: the expected figures are parsed out of `README.md`, so
a change means editing one document. A checker holding its own table of numbers would need editing
whenever the README did, which is the habit it replaces.

    python tools/check_readme.py

Standard library only. Runs from any working directory.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
SKILL = ROOT / "SKILL.md"

ROW_RE = re.compile(r"^\|\s*(.+?)\s*\|\s*([\d,]+)\s*\|", re.M)
# Whitespace-tolerant: both sentences wrap, and a regex that assumes single spaces reports a
# reworded sentence when all that changed was where the line broke.
SUM_RE = re.compile(r"largest\s+possible\s+single-phase\s+cost\s+is\s+([\d,]+)\s+plus\s+"
                    r"([\d,]+),\s+or\s+([\d,]+)")
COMPOUND_RE = re.compile(r"([\d,]+)\s+bytes\s+is\s+the\s+only\s+figure\s+that\s+compounds")
PATH_RE = re.compile(r"`([A-Za-z0-9_./-]+\.md)`")


def size(path: Path) -> int:
    """Bytes, as the repository stores them: CRLF normalised away, never a character count."""
    return len(path.read_bytes().replace(b"\r\n", b"\n"))


def num(s: str) -> int:
    return int(s.replace(",", ""))


def skill_parts() -> tuple[int, int, str | None]:
    """(description value, body, complaint) for SKILL.md.

    The README publishes a split, not a file size: the routing description is the byte length of
    the `description:` front-matter value alone, and the body is everything after the closing
    delimiter. Front matter itself is published as neither. The three are asserted to reconstruct
    the file, so a change to how SKILL.md opens fails here instead of quietly measuring the wrong
    bytes.
    """
    raw = SKILL.read_bytes().replace(b"\r\n", b"\n")
    m = re.match(rb"---\n(.*?\n)---\n", raw, re.S)
    if not m:
        return 0, 0, "SKILL.md does not open with a front-matter block"
    front, body = m.group(1), raw[m.end():]
    d = re.search(rb"^description:[ \t]*(.*)$", front, re.M)
    if not d:
        return 0, len(body), "SKILL.md's front matter has no description: field"
    if len(m.group(0)) + len(body) != len(raw):
        return 0, 0, "SKILL.md does not reconstruct from front matter plus body"
    return len(d.group(1)), len(body), None


def main() -> int:
    problems: list[str] = []
    readme = README.read_text(encoding="utf-8")
    desc, body, complaint = skill_parts()
    if complaint:
        print(f"check_readme: {complaint}")
        return 1

    rows = [(label, num(fig)) for label, fig in ROW_RE.findall(readme) if label != "Stage"]
    if not rows:
        print("check_readme: README.md has no installed-cost table")
        return 1

    print(f"=== {len(rows)} published figure(s)")
    measured: dict[str, int] = {}
    for label, published in rows:
        path = PATH_RE.search(label)
        if "body" in label.lower():
            actual = body
        elif "description" in label.lower():
            actual = desc
        elif path and (ROOT / path.group(1)).exists():
            actual = size(ROOT / path.group(1))
        else:
            # Not a skip. A row nothing knows how to measure is a row that stopped being
            # checked, which is the failure this tool exists to prevent.
            problems.append(f"{label!r}: no rule says how to measure this row")
            continue
        measured[label] = actual
        flag = "ok " if actual == published else "OFF"
        print(f"  {flag} {label:<26} published {published:>7,}  measured {actual:>7,}")
        if actual != published:
            problems.append(f"{label!r}: README publishes {published:,}, the file measures {actual:,}")

    # The compounding sentence repeats the routing-description figure in prose.
    c = COMPOUND_RE.search(readme)
    if not c:
        problems.append("the sentence naming the only figure that compounds is gone or reworded")
    elif num(c.group(1)) != desc:
        problems.append(f"the compounding sentence says {num(c.group(1)):,}, "
                        f"the description measures {desc:,}")

    # The arithmetic, three ways: the addends are the right two figures, they sum, and the
    # reference named really is the largest.
    s = SUM_RE.search(readme)
    if not s:
        problems.append("the largest-single-phase sentence is gone or reworded")
    else:
        a, bb, total = (num(g) for g in s.groups())
        refs = {k: v for k, v in measured.items() if "references/" in k}
        if a != body:
            problems.append(f"the sum's first addend is {a:,}, the SKILL.md body measures {body:,}")
        if refs:
            biggest = max(refs.values())
            if bb != biggest:
                problems.append(f"the sum's second addend is {bb:,}, the largest reference "
                                f"measures {biggest:,}")
        if a + bb != total:
            problems.append(f"the sum says {a:,} plus {bb:,} is {total:,}, which is {a + bb:,}")

    print(f"\ncheck_readme: {len(rows)} row(s) checked, {len(problems)} problem(s)")
    for p in problems:
        print(f"  MISMATCH  {p}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
