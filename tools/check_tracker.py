#!/usr/bin/env python3
"""Fail when an issue's open/closed state disagrees with its `status:` label.

`.taskmd/config.md` ends with the rule this project calls *the one thing to get right*: `status`
is the fact, and an issue's open or closed state is a **rendering** of it. A status change is
therefore two writes, and the rule warns that doing the second without the first "changes the
rendering while the fact stays put, and no view will flag it."

Nothing flagged it. This is the view that does.

**Both directions, because they are one fact disagreeing with itself.** Closed with an open
status is what a `Closes #N` trailer produces on merge, silently, minutes after anyone looked
at the tracker. Open with `done` is what a label write left stranded when the close never
followed. Checking one of them is how the other stays invisible - the same argument
`findings.py` in this directory already makes about its own two directions.

**Nothing here holds a copy of the answers.** Which statuses mean closed is `.taskmd/config.md`'s
fact: the `status` row of its vocabulary table, minus `open_statuses` from its front matter.
Add a value there and this check sees it without a second edit - the discipline
`check_readme.py` and `check_steps.py` both state in their own first lines.

**The predicate is exercised before the tracker is read.** `measure.md` requires a known-good
case before any scan's output is read as a finding, after a scan in the recorded run named three
defective rows and one of them was its own regular expression. The cases below run first and
fail this tool if any of them misbehaves, so a wrong predicate cannot report a clean tracker.

    python tools/check_tracker.py

Exit 0 clean, 1 on a contradiction or a broken predicate, 2 when the tracker could not be read -
no `gh`, no credentials, no network - with the reason on the first line. `check_all.py` reads
that 2 as a skip; see its manifest.

Standard library plus `gh`. Runs from any working directory.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / ".taskmd" / "config.md"

SKIPPED = 2


def statuses() -> tuple[set[str], set[str]]:
    """(open, closed), both read out of `.taskmd/config.md` and neither written here."""
    text = CONFIG.read_text(encoding="utf-8")

    m = re.search(r"^open_statuses:\s*\[([^\]]*)\]", text, re.M)
    if not m:
        raise SystemExit("cannot find open_statuses in .taskmd/config.md")
    open_ = {v.strip() for v in m.group(1).split(",") if v.strip()}

    m = re.search(r"^\|\s*status\s*\|([^|]*)\|", text, re.M)
    if not m:
        raise SystemExit("cannot find the status vocabulary row in .taskmd/config.md")
    every = {v.strip() for v in m.group(1).split(",") if v.strip()}

    unknown = open_ - every
    if unknown:
        raise SystemExit(f"open_statuses names values the vocabulary does not: {sorted(unknown)}")
    return open_, every - open_


def verdict(state: str, labels: list[str], open_: set[str], closed: set[str]) -> str | None:
    """One issue's disagreement, or None when the fact and the rendering agree."""
    found = [l[len("status:"):] for l in labels if l.startswith("status:")]
    if len(found) != 1:
        return f"carries {len(found)} status: labels, expected exactly one"
    status = found[0]
    if status not in open_ | closed:
        return f"status:{status} is not in the vocabulary"
    if state == "CLOSED" and status in open_:
        return f"closed, but status:{status} is an open status"
    if state == "OPEN" and status in closed:
        return f"open, but status:{status} is a closed status"
    return None


# (state, labels, expect a verdict) - run before the tracker, per the docstring.
CASES: list[tuple[str, list[str], bool]] = [
    ("CLOSED", ["status:done"], False),
    ("CLOSED", ["status:cancelled", "type:fix"], False),
    ("OPEN", ["status:proposed"], False),
    ("OPEN", ["status:review", "register-row"], False),
    ("CLOSED", ["status:review"], True),          # what a Closes #N trailer leaves behind
    ("CLOSED", ["status:proposed"], True),
    ("OPEN", ["status:done"], True),              # the label write whose close never followed
    ("OPEN", ["status:cancelled"], True),
    ("OPEN", ["type:fix"], True),                 # no status: label at all
    ("OPEN", ["status:done", "status:proposed"], True),
    ("OPEN", ["status:invented"], True),
]


def self_check(open_: set[str], closed: set[str]) -> list[str]:
    bad = []
    for state, labels, expected in CASES:
        got = verdict(state, labels, open_, closed) is not None
        if got != expected:
            bad.append(f"predicate wrong on {state} {labels}: expected {expected}, got {got}")
    return bad


def issues() -> list[dict]:
    """Every issue, or exit SKIPPED saying why the tracker could not be read."""
    try:
        proc = subprocess.run(
            ["gh", "issue", "list", "--state", "all", "--limit", "1000",
             "--json", "number,state,labels"],
            cwd=ROOT, capture_output=True,
        )
    except (FileNotFoundError, OSError):
        print("gh is not on PATH, so the tracker cannot be read")
        raise SystemExit(SKIPPED)
    if proc.returncode != 0:
        first = proc.stderr.decode("utf-8", "replace").strip().splitlines()
        why = first[0] if first else f"gh exited {proc.returncode}"
        print(f"the tracker could not be read - {why}")
        raise SystemExit(SKIPPED)
    return json.loads(proc.stdout.decode("utf-8"))


def main() -> int:
    open_, closed = statuses()

    broken = self_check(open_, closed)
    if broken:
        print("check_tracker: the predicate failed its own cases, so the tracker was not read")
        for line in broken:
            print(f"  {line}")
        return 1

    rows = issues()
    problems = []
    for row in rows:
        why = verdict(row["state"], [l["name"] for l in row["labels"]], open_, closed)
        if why:
            problems.append(f"#{row['number']} {why}")

    if problems:
        print(f"check_tracker: {len(problems)} of {len(rows)} issues contradict themselves")
        for line in problems:
            print(f"  MISMATCH  {line}")
        print("\nstatus is the fact and the state is a rendering of it - .taskmd/config.md.")
        return 1

    print(f"check_tracker: {len(rows)} issues, state and status: agree on every one "
          f"({len(CASES)} predicate cases passed first)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
