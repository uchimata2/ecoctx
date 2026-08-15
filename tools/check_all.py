#!/usr/bin/env python3
"""Run every checker this repository ships, and end with a partition that has no fourth outcome.

Each tool discovered is reported as exactly one of **ran**, **skipped with a stated reason**, or
**failed**. A tool in none of the three fails the run. That is the whole point: a hand-kept list
of checks goes stale silently, and the failure mode is a tool that stopped being called rather
than a tool that started failing.

The manifest below names every tool. Discovery is the filesystem, so the two can disagree, and
when they do this exits non-zero — a new tool is `UNDECLARED` until it is added here, and a
declared tool that has been deleted is `MISSING`. Neither is a judgement about the tool; both
say the manifest and the tree stopped agreeing.

    python tools/check_all.py

Standard library only. Runs from any working directory.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# name -> (argv after the interpreter, or None) and a reason when it is not run.
# A tool that cannot run here states why, in one sentence, checkable by a reader.
MANIFEST: dict[str, tuple[list[str] | None, str]] = {
    "selftest.py": (
        ["tools/selftest.py"],
        "",
    ),
    "findings.py": (
        None,
        "no audit report lives here - this repository is the skill, not a subject. "
        "selftest.py exercises it against fixtures in all four directions",
    ),
    "check_all.py": (
        None,
        "this tool - running it from itself would recurse",
    ),
}


def main() -> int:
    on_disk = {p.name for p in (ROOT / "tools").glob("*.py")}
    declared = set(MANIFEST)

    ran: list[str] = []
    skipped: list[tuple[str, str]] = []
    failed: list[tuple[str, str]] = []
    unpartitioned: list[tuple[str, str]] = []

    for name in sorted(on_disk - declared):
        unpartitioned.append((name, "UNDECLARED - on disk, not in the manifest"))
    for name in sorted(declared - on_disk):
        unpartitioned.append((name, "MISSING - in the manifest, not on disk"))

    for name in sorted(declared & on_disk):
        argv, reason = MANIFEST[name]
        if argv is None:
            skipped.append((name, reason))
            continue
        proc = subprocess.run(
            [sys.executable, *argv], cwd=ROOT, capture_output=True, text=True
        )
        if proc.returncode == 0:
            ran.append(name)
        else:
            tail = (proc.stdout + proc.stderr).strip().splitlines()
            failed.append((name, tail[-1] if tail else f"exit {proc.returncode}"))

    print(f"=== {len(on_disk | declared)} tool(s)")
    for name in ran:
        print(f"  ran      {name}")
    for name, reason in skipped:
        print(f"  skipped  {name} - {reason}")
    for name, why in failed:
        print(f"  FAILED   {name} - {why}")
    for name, why in unpartitioned:
        label, _, detail = why.partition(" - ")
        print(f"  {label:<8} {name} - {detail}")

    total = len(ran) + len(skipped) + len(failed) + len(unpartitioned)
    print(f"\n{len(ran)} ran, {len(skipped)} skipped with a reason, {len(failed)} failed, "
          f"{len(unpartitioned)} in no partition, {total} accounted for")

    if unpartitioned:
        print("\nA tool in none of the three partitions fails the run. Fix the manifest.")
    return 1 if (failed or unpartitioned) else 0


if __name__ == "__main__":
    sys.exit(main())
