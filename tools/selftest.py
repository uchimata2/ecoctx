#!/usr/bin/env python3
"""Exercise findings.py against fixtures whose answers are known by construction.

This repository is the skill, not a repository under audit, so it holds no report for
findings.py to read. Without this, the tool would ship untested and the gate would only be
able to record that fact politely.

**The fixtures are built here, in a temporary directory, and never out of this repository's
own tracked files.** A self-test that asserts the current contents of a tracked file blocks
the next commit that changes it, which turns the gate into an obstacle to the work it exists
to protect.

Four cases, and the middle two are the ones that matter: the check has to fail in **both**
directions, because a finding whose task closed while its row still reads open and a task
naming a finding that does not exist are the same defect seen from opposite sides, and
checking only one of them is how either stays invisible.

    python tools/selftest.py

Standard library only.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

FINDINGS = Path(__file__).resolve().parent / "findings.py"

REPORT = """# Audit

| # | id | Gain |
| :-- | :-- | :-- |
| ~~1~~ | **CE-01** | L |
| 2 | **CE-02** | M |
| 3 | **CE-03** | S |
"""

# The prose mention below is the regression that the known-answer run bought: a finding is
# stated before it is ranked, so a scanner reading the first line naming an id never sees the
# row carrying the closure marker. It reported twelve disagreements out of thirteen where
# there were none.
REPORT_WITH_PROSE = "Finding CE-01 concerns the load path, and CE-02 the read path.\n\n" + REPORT


def task(status: str, finding: str) -> str:
    return f"---\nstatus: {status}\nfinding: {finding}\n---\n\n# fixture\n"


def run(root: Path) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(FINDINGS), "--root", str(root), "--check"],
        capture_output=True, text=True,
    )
    return proc.returncode, proc.stdout + proc.stderr


def build(root: Path, report: str, tasks: dict[str, tuple[str, str]]) -> None:
    (root / "tasks").mkdir(parents=True, exist_ok=True)
    (root / "AUDIT.md").write_text(report, encoding="utf-8")
    for name, (status, finding) in tasks.items():
        (root / "tasks" / f"{name}.md").write_text(task(status, finding), encoding="utf-8")


def main() -> int:
    failures: list[str] = []

    def check(label: str, ok: bool, detail: str = "") -> None:
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}")
        if not ok:
            failures.append(f"{label}{': ' + detail if detail else ''}")

    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)

        agree = base / "agree"
        build(agree, REPORT, {"T-1": ("done", "CE-01"), "T-2": ("in_progress", "CE-02")})
        code, out = run(agree)
        check("a consistent record exits 0", code == 0, out)
        check("and says nothing disagrees", "0 disagreeing" in out, out)

        forward = base / "forward"
        build(forward, REPORT, {"T-1": ("in_progress", "CE-01")})
        code, out = run(forward)
        check("a closed row over an open task fails", code == 1, out)
        check("and names that direction", "report reads closed" in out, out)

        backward = base / "backward"
        build(backward, REPORT, {"T-2": ("done", "CE-02")})
        code, out = run(backward)
        check("a closed task under an open row fails", code == 1, out)
        check("and names that direction", "task is closed" in out, out)

        dangling = base / "dangling"
        build(dangling, REPORT, {"T-9": ("done", "CE-99")})
        code, out = run(dangling)
        check("a task naming no stated finding fails", code == 1, out)
        check("and says so", "stated in no report row" in out, out)

        prose = base / "prose"
        build(prose, REPORT_WITH_PROSE, {"T-1": ("done", "CE-01")})
        code, out = run(prose)
        check("a prose mention before the ranked row is not read as the row", code == 0, out)

        empty = base / "unstated"
        build(empty, REPORT, {})
        code, out = run(empty)
        check("a finding with no task is listed, not an error", code == 0, out)
        check("and is marked as having none", "(no task)" in out, out)

    print(f"\nselftest: {6 + 4 - len(failures)} of 10 checks passed")
    for f in failures:
        print(f"  FAILED  {f.splitlines()[0]}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
