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

# CE-03 is absent. The recorded run lost E-06 exactly this way and nobody noticed for months.
REPORT_WITH_GAP = REPORT.replace("| **CE-03** |", "| **CE-04** |")

# The same three ids, split across the two output documents the method declares. Neither half
# is contiguous on its own, which is the condition a single-document check reads as clean.
REPORT_SPLIT_A = REPORT.replace("| 2 | **CE-02** | M |\n", "")
REPORT_SPLIT_B = ("# Portable\n\n| # | id | Gain |\n"
                  "| :-- | :-- | :-- |\n| 2 | **CE-02** | M |\n")


def task(status: str, finding: str) -> str:
    return f"---\nstatus: {status}\nfinding: {finding}\n---\n\n# fixture\n"


def run(root: Path) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(FINDINGS), "--root", str(root), "--check"],
        capture_output=True, text=True,
    )
    return proc.returncode, proc.stdout + proc.stderr


def build(root: Path, report: str, tasks: dict[str, tuple[str, str]],
          second: str | None = None) -> None:
    (root / "tasks").mkdir(parents=True, exist_ok=True)
    (root / "AUDIT.md").write_text(report, encoding="utf-8")
    if second is not None:
        (root / "PORTABLE.md").write_text(second, encoding="utf-8")
        (root / ".ecoctx.json").write_text(
            '{"report": ["AUDIT.md", "PORTABLE.md"]}', encoding="utf-8")
    for name, (status, finding) in tasks.items():
        (root / "tasks" / f"{name}.md").write_text(task(status, finding), encoding="utf-8")


def main() -> int:
    failures: list[str] = []

    ran = 0

    def check(label: str, ok: bool, detail: str = "") -> None:
        # Counted here, in the one function every assertion passes through. A total written
        # down anywhere else is a second copy that goes stale the next time a fixture is
        # added - which is how this line came to claim ten checks while running eleven.
        nonlocal ran
        ran += 1
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

        gap = base / "gap"
        build(gap, REPORT_WITH_GAP, {"T-1": ("done", "CE-01")})
        code, out = run(gap)
        check("a hole in the numbering fails", code == 1, out)
        check("and names the id that is missing", "CE-03: a gap in the numbering" in out, out)

        split = base / "split"
        build(split, REPORT_SPLIT_A, {"T-1": ("done", "CE-01")}, second=REPORT_SPLIT_B)
        code, out = run(split)
        check("contiguous only across both documents passes", code == 0, out)
        check("and does not warn about a single document",
              "one document is configured" not in out, out)

        code, out = run(agree)
        check("one configured document says the other's gaps are unseen",
              "one document is configured" in out, out)

        empty = base / "unstated"
        build(empty, REPORT, {})
        code, out = run(empty)
        check("a finding with no task is listed, not an error", code == 0, out)
        check("and is marked as having none", "(no task)" in out, out)
        check("and says the glob matched nothing, so 0 is not read as a comparison",
              "matched no files" in out, out)

        # The discrimination this note exists for. Without this case, printing the note
        # unconditionally would satisfy the check above and still be wrong.
        unraised = base / "unraised"
        build(unraised, REPORT, {})
        (unraised / "tasks" / "T-7.md").write_text(
            "---\nstatus: in_progress\n---\n\n# raises nothing\n", encoding="utf-8")
        code, out = run(unraised)
        check("a populated task tree that raises nothing is clean", code == 0, out)
        check("and gets no glob note", "matched no files" not in out, out)

    print(f"\nselftest: {ran - len(failures)} of {ran} checks passed")
    for f in failures:
        print(f"  FAILED  {f.splitlines()[0]}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
