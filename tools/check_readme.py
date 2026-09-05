#!/usr/bin/env python3
"""Re-measure every figure and re-derive every count `README.md` publishes about this repository.

A skill that audits context economy publishes its own installed cost, which makes those five
numbers the most checkable claim this repository makes about itself. Until now they were checked
by whoever remembered: editing `references/judge.md` once moved three published figures at the
same time, and catching it took a script written for the occasion.

**The counts arrived later and for the same reason** (#77). The README also states how many steps
the method has, how many files are the method, how many are packaging, how many checkers live in
`tools/` and how many checks `selftest.py` runs. None was checked, and on 2026-09-05 #75 added a
seventh checker and made the fourth of them false. It was corrected by hand in the same commit,
because somebody happened to look - which is the arrangement the byte figures above stopped having.

**What a green run here does not mean.** It means every number the README states agrees with what
produces it. It does not mean the README is true: a count nobody has written a rule for is
invisible to this file, and unlike the installed-cost table - whose rows enumerate themselves, so a
row nothing can measure is reported - prose does not announce its own numbers. Scanning every digit
in the README instead was rejected: it turns each incidental figure in a sentence into a failure,
and a checker argued with is a checker switched off.

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
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
SKILL_DIR = ROOT / "skills" / "ecoctx"   # a plugin's skills live under skills/<name>/
SKILL = SKILL_DIR / "SKILL.md"

ROW_RE = re.compile(r"^\|\s*(.+?)\s*\|\s*([\d,]+)\s*\|", re.M)
# Whitespace-tolerant: both sentences wrap, and a regex that assumes single spaces reports a
# reworded sentence when all that changed was where the line broke. `possible` is optional for the
# same reason: the claim under check is the arithmetic, not the adjective in front of it.
SUM_RE = re.compile(r"largest\s+(?:possible\s+)?single-phase\s+cost\s+is\s+([\d,]+)\s+plus\s+"
                    r"([\d,]+),\s+or\s+([\d,]+)")
COMPOUND_RE = re.compile(r"([\d,]+)\s+bytes\s+is\s+the\s+only\s+figure\s+that\s+compounds")
PATH_RE = re.compile(r"`([A-Za-z0-9_./-]+\.md)`")

# The step total is `SKILL.md`'s fact, and `check_steps.py` already owns the pattern that reads it
# and the word map that turns it into a number. Both are imported rather than copied: a checker
# that enforces agreement while holding its own duplicate of what it reads is the joke it exists
# to stop. A script run puts `tools/` on the path, so this resolves from any working directory.
import check_steps  # noqa: E402

# check_steps needs only the range a step total can reach. The README also counts files, packaging
# and checkers, so the small words are added here rather than widened there.
WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
         "nine": 9, **check_steps.WORDS}


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


def word_or_digits(token: str) -> int | None:
    """The integer a README count states, or None for a word this tool cannot read."""
    bare = token.replace(",", "")
    return int(bare) if bare.isdigit() else WORDS.get(token.lower())


def shipping_tools() -> list[Path]:
    """The programs that ship with the skill: every tool that is not one of this repository's checkers."""
    return [p for p in sorted((ROOT / "tools").glob("*.py")) if not p.name.startswith("check_")]


def step_total() -> int | None:
    m = check_steps.TOTAL_RE.search(SKILL.read_text(encoding="utf-8"))
    return WORDS.get(m.group(1).lower()) if m else None


def selftest_total() -> int | None:
    """How many checks `selftest.py` runs, taken by running it.

    Counting `check(` call sites would be free and would be wrong the first time one sat inside a
    loop — and `selftest.py` carries a comment about a line that claimed ten checks while eleven
    ran, so that is not a hypothetical bug, it is one this repository has already made once.
    Measured 2026-09-05: the extra run costs the gate 0.74s of its 1.67s.
    """
    proc = subprocess.run([sys.executable, str(ROOT / "tools" / "selftest.py")],
                          capture_output=True, encoding="utf-8", cwd=ROOT)
    m = re.search(r"selftest: \d+ of (\d+) checks", proc.stdout or "")
    return int(m.group(1)) if m else None


# Each entry: a label, the README pattern whose every captured group states the count, and what
# answers it. Nothing here holds an expected number, exactly as the figures above hold none.
COUNTS: list[tuple[str, re.Pattern[str], object]] = [
    ("steps the method has", re.compile(r"^(\w+) steps, two phases", re.M), step_total),
    ("files that are the method", re.compile(r"^(\w+) files are the method", re.M),
     lambda: len(list(SKILL_DIR.rglob("*.md"))) + len(shipping_tools())),
    ("packaging files", re.compile(r"(\w+) more are packaging"),
     lambda: len([p for p in (ROOT / ".claude-plugin").iterdir() if p.is_file()])),
    ("checkers in tools/", re.compile(r"The (\w+) checkers in `tools/`"),
     lambda: len(list((ROOT / "tools").glob("check_*.py")))),
    ("checks selftest runs", re.compile(r"passes ([\d,]+) of ([\d,]+)"), selftest_total),
]


def counts(readme: str, problems: list[str]) -> None:
    """Re-derive every count the README states, and print one row each."""
    print(f"\n=== {len(COUNTS)} published count(s)")
    for label, pattern, derive in COUNTS:
        m = pattern.search(readme)
        if not m:
            problems.append(f"{label!r}: the sentence stating this count is gone or reworded")
            continue
        stated = [word_or_digits(g) for g in m.groups()]
        if None in stated:
            problems.append(f"{label!r}: the README spells it {m.group(0)!r}, which this tool "
                            f"cannot read as a number — add the word to WORDS")
            continue
        actual = derive()
        if actual is None:
            problems.append(f"{label!r}: nothing here could work out the real number")
            continue
        shown = " and ".join(str(s) for s in stated)
        agrees = all(s == actual for s in stated)
        print(f"  {'ok ' if agrees else 'OFF'} {label:<26} says {shown:>9}  counted {actual:>7}")
        if not agrees:
            problems.append(f"{label!r}: the README says {shown}, there are {actual}")


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

    counts(readme, problems)

    print(f"\ncheck_readme: {len(rows)} row(s) and {len(COUNTS)} count(s) checked, "
          f"{len(problems)} problem(s)")
    for p in problems:
        print(f"  MISMATCH  {p}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
