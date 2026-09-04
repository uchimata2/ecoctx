#!/usr/bin/env python3
"""Enforce the mechanical half of `README.md`'s prose conventions.

A humanising pass over this file was a rule somebody remembered, and on 2026-09-05 it was
forgotten across three rewrites and two releases (#70). Half of that pass is string matching
with no judgement in it, so it stops being a rule here and becomes a check.

**This covers the mechanical half only, and saying which half is the point.** It finds an em
dash, a curly quote, and a handful of words this README's register does not use. It cannot see
a sentence that announces its point instead of making it, a fragment tacked onto a claim that
already stood, or a not-X-but-Y - which are the four that #70 actually found. **A green run here
is not a document that has had a pass**, and reading it as one is the failure this docstring
exists to prevent.

**`README.md` alone, deliberately.** The three references use em dashes heavily and on purpose;
the README has used spaced hyphens since long before any of this. A check applied to the whole
tree would fail on the method's own house style, so the scope is the one file whose convention
this is.

**Fenced code blocks are skipped.** A command or a sample may legitimately contain any character,
and a checker that cannot tell prose from a transcript will eventually be argued with rather than
obeyed.

    python tools/check_prose.py

Standard library only. Runs from any working directory.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

# Each entry: a name, a pattern, and what to do instead. The advice is half the value: a checker
# that only says "no" gets worked around at the next inconvenient moment.
RULES: list[tuple[str, str, str]] = [
    ("em or en dash", r"[–—]",
     "use a spaced hyphen, a comma, a colon or a full stop"),
    ("curly quote", r"[“”‘’]",
     "use straight quotes; an editor inserted these"),
    ("inflated word", r"\b(?:delve|delves|delving|showcase|showcases|showcasing|testament|"
                      r"tapestry|pivotal|vibrant|intricate|intricacies|seamless|seamlessly|"
                      r"holistic|garner|garners|garnered|underscores|underscoring|fostering|"
                      r"realm|crucial|boasts|stands as|serves as|it is important to note)\b",
     "say the specific thing instead; this register does not use these"),
]

FENCE_RE = re.compile(r"^```", re.M)


def prose_lines(text: str) -> list[tuple[int, str]]:
    """Every line outside a fenced code block, with its 1-based number."""
    out: list[tuple[int, str]] = []
    fenced = False
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            out.append((n, line))
    return out


def scan(text: str) -> list[tuple[str, int, str, str]]:
    """(rule, line number, what was found, what to do) for every violation in prose."""
    out: list[tuple[str, int, str, str]] = []
    for name, pattern, advice in RULES:
        rx = re.compile(pattern, re.I if name == "inflated word" else 0)
        for n, line in prose_lines(text):
            for m in rx.finditer(line):
                out.append((name, n, m.group(0), advice))
    return out


# Known-good and known-bad, run before the file is read. `measure.md` requires a scan to prove it
# fires before its silence is read as a result, after one in the recorded run named three defective
# rows and one of them was its own regular expression.
CASES: list[tuple[str, bool]] = [
    ("a plain sentence with a spaced hyphen - like this", False),
    ("straight \"quotes\" and an apostrophe's tail", False),
    ("```\nan em dash — inside a fence\n```", False),
    ("the key insight, underscored by a check_readme.py run", False),
    ("a sentence with an em dash — in prose", True),
    ("an en dash – in prose", True),
    ("a “curly quoted” phrase", True),
    ("this delves into the topic", True),
    ("a vibrant, seamless showcase", True),
    ("it serves as the entry point", True),
]


def self_check() -> list[str]:
    bad = []
    for text, expect in CASES:
        got = bool(scan(text))
        if got != expect:
            bad.append(f"expected {expect}, got {got}, on {text!r}")
    return bad


def main() -> int:
    if not README.exists():
        print("check_prose: README.md is missing")
        return 1

    broken = self_check()
    if broken:
        print("check_prose: the rules failed their own cases, so README.md was not read")
        for line in broken:
            print(f"  {line}")
        return 1

    text = README.read_text(encoding="utf-8")
    found = scan(text)
    problems: list[str] = []

    print(f"=== {len(RULES)} rule(s) over {len(prose_lines(text))} prose line(s), "
          f"{len(CASES)} case(s) passed first")
    for name, _, _ in RULES:
        hits = [f for f in found if f[0] == name]
        print(f"  {'ok ' if not hits else 'OFF'} {name:<14} {len(hits)} hit(s)")
    for name, n, what, advice in found:
        problems.append(f"README.md:{n} {name}: {what!r} - {advice}")

    if problems:
        print(f"\ncheck_prose: {len(problems)} problem(s)")
        for line in problems:
            print(f"  {line}")
        return 1

    print("\ncheck_prose: the mechanical half is clean. The structural half is not checked here "
          "and has not been checked by this run.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
