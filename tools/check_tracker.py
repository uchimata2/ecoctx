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

**A `related` edge written at one end only is the other fact nothing rendered** (#81). The same
config says this backend derives no inverse for `related`, so the field is written at both ends or
it does not exist, and "a pair written once is a half-edge that reads as absent from the other
side". One existed: #50 was named by #63 and named nothing back, through a phase that asserted the
opposite, and it was found by re-reading rather than by any view.

**Only the property block is read for it.** `related` lives in the fenced block at the top of a body
and nowhere else, and a body's prose can discuss the field - #27 does, at length. A checker that
swept whole bodies would report edges nobody wrote, which is worse than the gap it fills.

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


BLOCK_RE = re.compile(r"\A\s*```[^\n]*\n(.*?)\n```", re.S)
RELATED_RE = re.compile(r"^Related:\s*(.+)$", re.M)
REF_RE = re.compile(r"#(\d+)")


def related_edges(body: str) -> set[int]:
    """The issues a body's property block names as related.

    The fenced block at the top, and nothing else. `related` lives there per `.taskmd/config.md`,
    while a body's prose may discuss the field at length - so a body-wide search would read those
    sentences as edges and report links nobody wrote.
    """
    m = BLOCK_RE.match(body or "")
    if not m:
        return set()
    line = RELATED_RE.search(m.group(1))
    return {int(n) for n in REF_RE.findall(line.group(1))} if line else set()


def asymmetries(edges: dict[int, set[int]]) -> list[str]:
    """One line per edge written at a single end, or naming an issue this tracker does not hold."""
    out = []
    for near in sorted(edges):
        for far in sorted(edges[near]):
            if far not in edges:
                out.append(f"#{near} names #{far} as related, and no such issue is in this tracker")
            elif near not in edges[far]:
                out.append(f"#{near} names #{far} as related and #{far} does not name #{near} back "
                           f"- the Related line is missing from #{far}")
    return out


# (body, the edges it holds) - the parser is exercised because a parser that matches nothing
# reports a perfectly symmetric backlog, which is this check's own version of the scan whose
# defect was its regular expression.
PARSE_CASES: list[tuple[str, set[int]]] = [
    ("```\nwork_package: F-tooling\norder: 46\nRelated: #27\n```\n\nbody text", {27}),
    ("```\nRelated: #8, #11, #81\n```", {8, 11, 81}),
    ("```\nwork_package: outside-ranking\n```\n\nprose", set()),
    ("no property block, and a line saying\nRelated: #99\nin ordinary prose", set()),
    ("```\norder: 1\n```\n\nRelated: #99 mentioned after the block", set()),
    ("", set()),
]

# (edges, how many lines the pass must produce)
EDGE_CASES: list[tuple[dict[int, set[int]], int]] = [
    ({1: {2}, 2: {1}}, 0),                    # written at both ends: quiet
    ({1: {2}, 2: set()}, 1),                  # the half-edge this check exists for
    ({1: set(), 2: set()}, 0),                # no edges is not a finding
    ({1: {2}, 2: {1, 3}, 3: {2}}, 0),         # more than one edge on an issue
    ({1: {9}}, 1),                            # naming an issue the tracker does not hold
]


def edge_self_check() -> list[str]:
    bad = []
    for body, expected in PARSE_CASES:
        got = related_edges(body)
        if got != expected:
            bad.append(f"parser wrong on {body[:34]!r}: expected {expected or 'no edges'}, got "
                       f"{got or 'no edges'}")
    for edges, expected in EDGE_CASES:
        got = len(asymmetries(edges))
        if got != expected:
            bad.append(f"symmetry wrong on {edges}: expected {expected} line(s), got {got}")
    return bad


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
             "--json", "number,state,labels,body"],
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

    broken = self_check(open_, closed) + edge_self_check()
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

    edges = {row["number"]: related_edges(row.get("body") or "") for row in rows}
    problems += asymmetries(edges)

    if problems:
        print(f"check_tracker: {len(problems)} problem(s) across {len(rows)} issues")
        for line in problems:
            print(f"  MISMATCH  {line}")
        print("\nstatus is the fact and the state is a rendering of it; related is written at "
              "both ends or it does not exist - .taskmd/config.md.")
        return 1

    total = sum(len(v) for v in edges.values())
    print(f"check_tracker: {len(rows)} issues, state and status: agree on every one, and all "
          f"{total} related edge(s) are written at both ends "
          f"({len(CASES) + len(PARSE_CASES) + len(EDGE_CASES)} predicate cases passed first)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
