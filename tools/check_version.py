#!/usr/bin/env python3
"""Check that every rendering of this project's version agrees with its home.

`skills/ecoctx/SKILL.md` is the version's home, and #63 decided it tracks the tip of `master`, so
it moves on every shipping merge. Three other statements have to move with it: `README.md` states
the version in words and again as the semver the manifest carries, and `.claude-plugin/plugin.json`
carries that semver. Until now nothing checked any of them, and one had already been wrong for
three merges - `SKILL.md` claimed the manifest carried `1.1.0` while the file carried `2.2.0`,
found by reading rather than by any tool (#75).

**The mapping is computed, never stored.** `SKILL.md` states it as prose - rubric as the major,
revision as the minor, patch always zero - and this file is what makes that sentence executable. A
table of expected strings here would be the second home the whole task exists to delete.

**A pattern that stops matching is a problem, not a pass.** A checker that quietly finds nothing to
compare reports success on a document it can no longer read, which is worse than the drift it was
built to catch because it looks identical from the outside. So every read below either finds its
value or files a problem.

**What this does not cover.** It compares renderings against the home; it cannot say the home is
right. Nothing here reads a git tag, deliberately - #63 decided `master` may sit ahead of the newest
tag, so a tag that disagrees is the ordinary state and not a defect. And it knows only about the
version: every other figure, count or claim in `README.md` belongs to `check_readme.py`, to
`check_charts.py`, or to nothing at all.

    python tools/check_version.py

Standard library only. Runs from any working directory.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "ecoctx" / "SKILL.md"
README = ROOT / "README.md"
MANIFEST = ROOT / ".claude-plugin" / "plugin.json"

# Anchored on purpose. "rubric" appears four times in SKILL.md, including "predates rubric 1" in
# ordinary prose, so an unanchored pattern would match a sentence and be right only by luck.
HOME_RE = re.compile(r"^\*\*rubric (\d+), revision (\d+)\*\*", re.M)
README_WORDS_RE = re.compile(r"Version `rubric (\d+), revision (\d+)`")
README_SEMVER_RE = re.compile(r"`plugin\.json` renders it `(\d+\.\d+\.\d+)`")


def home() -> tuple[str, str] | str:
    """The version as its home states it, or a sentence saying why it could not be read."""
    if not SKILL.exists():
        return f"{SKILL.relative_to(ROOT).as_posix()} is missing"
    m = HOME_RE.search(SKILL.read_text(encoding="utf-8"))
    if not m:
        return (f"{SKILL.relative_to(ROOT).as_posix()} no longer opens its version block with "
                "**rubric N, revision M**, so nothing here knows what the version is")
    return m.group(1), m.group(2)


def main() -> int:
    read = home()
    if isinstance(read, str):
        print(f"check_version: {read}")
        return 1
    rubric, revision = read
    words = f"rubric {rubric}, revision {revision}"
    semver = f"{rubric}.{revision}.0"

    problems: list[str] = []
    rows: list[tuple[str, str, str]] = []  # label, found, expected

    readme = README.read_text(encoding="utf-8") if README.exists() else ""
    m = README_WORDS_RE.search(readme)
    if m:
        rows.append(("README.md, in words", f"rubric {m.group(1)}, revision {m.group(2)}", words))
    else:
        problems.append("README.md no longer states the version in words, so the pattern that "
                        "checked it now matches nothing")

    m = README_SEMVER_RE.search(readme)
    if m:
        rows.append(("README.md, as semver", m.group(1), semver))
    else:
        problems.append("README.md no longer names the semver the manifest renders, so the "
                        "pattern that checked it now matches nothing")

    try:
        rows.append((".claude-plugin/plugin.json", json.loads(
            MANIFEST.read_text(encoding="utf-8"))["version"], semver))
    except FileNotFoundError:
        problems.append(".claude-plugin/plugin.json is missing")
    except json.JSONDecodeError as exc:
        problems.append(f".claude-plugin/plugin.json is not valid JSON: {exc}")
    except KeyError:
        problems.append(".claude-plugin/plugin.json carries no version field")

    print(f"=== {len(rows)} rendering(s) of {words}, the home being "
          f"{SKILL.relative_to(ROOT).as_posix()}")
    for label, found, expected in rows:
        flag = "ok " if found == expected else "OFF"
        print(f"  {flag} {label:<26} states {found:>22}  expected {expected:>22}")
        if found != expected:
            problems.append(f"{label} states {found}, the home says {expected}")

    print(f"\ncheck_version: {len(rows)} rendering(s) checked, {len(problems)} problem(s)")
    for p in problems:
        print(f"  MISMATCH  {p}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
