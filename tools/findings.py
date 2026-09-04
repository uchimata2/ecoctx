#!/usr/bin/env python3
"""Answer *which finding is which task, and what state is it in* in one small output.

The method ranks findings and never says where the link between a finding and the work item
serving it lives. Every adopting project then re-derives it, and the answer is stale by the
next closure: reconstructing thirteen of them once cost 80,721 bytes across fourteen closed
records, and the result was a hand-kept fourteenth copy of facts that already existed.

The shape that works needs no new file. The link lives on the **task**, in a structured field
a command can read without parsing English. The ranking table is parsed where it stands. The
two are checked against each other, and **the check fails in both directions**: a finding
whose task has closed while its row still reads open, and a task naming a finding that does
not exist, both stop the run. A generator without that check moves the inconsistency rather
than removing it.

Tracker-agnostic by configuration, not by assumption. Nothing here knows what a tracker is
beyond: task files are text, they open with a front-matter block of `key: value` lines, and
one of those keys names a finding. Point it at whatever your project uses.

    python tools/findings.py                 # print the listing
    python tools/findings.py --check         # listing, and exit non-zero on any disagreement

Configuration is a JSON file, `.ecoctx.json` at the root of the audited repository. Every key
has a default; a project whose shape matches them needs no file at all.

    {
      "report":             "AUDIT.md",   // or ["AUDIT.md", "AUDIT-portable.md"]
      "id_pattern":         "CE-[0-9]+",
      "tasks_glob":         "tasks/*.md",
      "task_finding_field": "finding",
      "task_status_field":  "status",
      "closed_statuses":    ["done", "cancelled"],
      "closed_marker":      "~~"
    }

`report` is one path, or a list of them. The method declares **one numbering space across both
output documents**, each finding stated in full in exactly one of them, so a hole in the sequence is
a finding that was stated and lost. Reading one document and calling the space contiguous is how
such a hole stays invisible - configure both and the gap is reported.

**A clean exit says what it compared.** Where `tasks_glob` matches no files the run notes it, because
an unraised backlog and a wrong glob produce the same silence and only one of them is a comparison.

`closed_marker` is how the report marks a row as closed — strikethrough by default. A project
that marks closure some other way sets it, or sets it to "" and the row state is never
inferred from the report, which turns off half the check and says so in the output.

Standard library only. No network. Runs from any working directory.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

DEFAULTS = {
    "report": "AUDIT.md",
    "id_pattern": "CE-[0-9]+",
    "tasks_glob": "tasks/*.md",
    "task_finding_field": "finding",
    "task_status_field": "status",
    "closed_statuses": ["done", "cancelled"],
    "closed_marker": "~~",
}


def repo_root(start: Path) -> Path:
    """The nearest ancestor holding .git, else the starting directory.

    Deliberately not `git rev-parse`: the tool must run in a repository that has not been
    initialised yet, which is exactly when an audit is most likely to be run.
    """
    for d in [start, *start.parents]:
        if (d / ".git").exists():
            return d
    return start


def load_config(root: Path, explicit: Path | None) -> dict:
    cfg = dict(DEFAULTS)
    path = explicit if explicit else root / ".ecoctx.json"
    if path.exists():
        try:
            cfg.update(json.loads(path.read_text(encoding="utf-8")))
        except json.JSONDecodeError as exc:
            sys.exit(f"findings: {path} is not valid JSON: {exc}")
    return cfg


def front_matter(text: str) -> dict[str, str]:
    """The leading `---` block as flat key/value pairs.

    Values are returned as written, including brackets and quotes. Nothing here parses YAML:
    the two fields this tool reads are scalars in every tracker seen, and a parser would be a
    dependency bought to re-read what a regular expression already answers.
    """
    m = re.match(r"---\r?\n(.*?)\r?\n---", text, re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t", "#")):
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip().strip("'\"")
    return out


def scan_tasks(root: Path, cfg: dict) -> tuple[dict[str, list[tuple[str, str]]], int]:
    """finding id -> [(task stem, status)], and how many files the glob matched.

    The count is returned rather than re-derived by the caller because two states look identical
    in the mapping and are not the same: a task tree with nothing raised yet - clean, and the case
    this tool was designed around - and a `tasks_glob` that matches nothing at all, where the
    comparison never happened. One glob, one owner, so the two cannot drift apart.
    """
    id_re = re.compile(cfg["id_pattern"])
    found: dict[str, list[tuple[str, str]]] = {}
    matched = 0
    for p in sorted(root.glob(cfg["tasks_glob"])):
        matched += 1
        fm = front_matter(p.read_text(encoding="utf-8", errors="replace"))
        raw = fm.get(cfg["task_finding_field"], "")
        if not raw:
            continue
        status = fm.get(cfg["task_status_field"], "?")
        for fid in id_re.findall(raw):
            found.setdefault(fid, []).append((p.stem, status))
    return found, matched


def report_paths(cfg: dict) -> list[str]:
    """The configured document(s), as a list however `report` was written.

    One key rather than two: the two output documents are one numbering space, and a second key
    would be a second home for the same fact.
    """
    r = cfg["report"]
    return [r] if isinstance(r, str) else list(r)


def gaps(ids: list[str]) -> tuple[list[str], str | None]:
    """Ids the sequence skips, and a reason when contiguity cannot be read at all.

    Grouped by the non-numeric prefix, so a project ranking `CE-` and `E-` in one space is checked
    per sequence rather than across two that were never one. The missing id is rebuilt at the width
    its neighbours use, because `CE-3` in a report of `CE-03`s is not a searchable string.
    """
    seqs: dict[str, list[tuple[int, int]]] = {}
    for fid in ids:
        m = re.match(r"^(.*?)(\d+)$", fid)
        if not m:
            return [], f"{fid!r} has no numeric tail"
        seqs.setdefault(m.group(1), []).append((int(m.group(2)), len(m.group(2))))
    missing: list[str] = []
    for prefix, seen in seqs.items():
        nums = {n for n, _ in seen}
        width = max((w for _, w in seen), key=lambda w: [w for _, w in seen].count(w))
        missing += [f"{prefix}{n:0{width}d}" for n in range(min(nums), max(nums) + 1) if n not in nums]
    return sorted(missing), None


def scan_report(root: Path, cfg: dict) -> dict[str, bool | None]:
    """finding id -> some table row reads closed (True/False), or None when the marker is off.

    **Only table rows are read, and closure is an OR across every row naming the id.** Both
    halves of that were bought by a known-answer run against a repository whose finding-to-task
    answer was already established by other means. Reading the *first* mention reported twelve
    disagreements out of thirteen where there were none: a finding is stated in prose before it
    is ranked, so the first line naming it is never the row carrying the marker. And a project
    that ranks in one table, records candidates in a second and grades outcomes in a third names
    the same id in all three, only one of which is struck.

    What it cannot see: a row struck for some reason other than closure. The tool reports what
    the report says; where that is wrong, the disagreement it raises is the point.
    """
    id_re = re.compile(cfg["id_pattern"])
    marker = cfg["closed_marker"]
    rows: dict[str, bool | None] = {}
    for name in report_paths(cfg):
        path = root / name
        if not path.exists():
            sys.exit(f"findings: report not found at {name} - set \"report\" in .ecoctx.json")
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            if not line.lstrip().startswith("|"):
                continue
            ids = id_re.findall(line)
            if not ids:
                continue
            struck = bool(marker) and marker in line
            for fid in ids:
                if not marker:
                    rows[fid] = None
                else:
                    rows[fid] = rows.get(fid) or struck
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description="Which finding is which task, and what state is it in.")
    ap.add_argument("--check", action="store_true", help="exit non-zero on any disagreement")
    ap.add_argument("--config", type=Path, default=None, help="path to a config file")
    ap.add_argument("--root", type=Path, default=None, help="repository root (default: discovered)")
    args = ap.parse_args()

    root = args.root.resolve() if args.root else repo_root(Path.cwd())
    cfg = load_config(root, args.config)
    tasks, matched = scan_tasks(root, cfg)
    rows = scan_report(root, cfg)
    closed_statuses = set(cfg["closed_statuses"])

    problems: list[str] = []
    lines: list[str] = []
    for fid in sorted(rows, key=lambda s: (len(s), s)):
        owners = tasks.get(fid, [])
        if not owners:
            # ASCII only: this prints to whatever console the adopter has, and a byte the
            # terminal cannot encode turns a listing into a mojibake bug report.
            lines.append(f"{fid:<8} (no task)")
            continue
        for stem, status in owners:
            lines.append(f"{fid:<8} {status:<12} {stem}")
        # Both directions. A row that reads closed while its task is open is the same
        # defect as its mirror, and only checking one of them is how it stayed invisible.
        row_closed = rows[fid]
        if row_closed is not None:
            all_done = all(s in closed_statuses for _, s in owners)
            if row_closed and not all_done:
                problems.append(f"{fid}: the report reads closed, the task does not")
            if all_done and not row_closed:
                problems.append(f"{fid}: the task is closed, the report row does not say so")

    for fid in sorted(set(tasks) - set(rows), key=lambda s: (len(s), s)):
        problems.append(f"{fid}: named by a task, stated in no report row")

    # A hole in the sequence is a finding that was stated and lost - a different defect from the
    # dangling id above, and reported in different words so the two are not read as one.
    missing, unreadable = gaps(list(rows))
    for fid in missing:
        problems.append(f"{fid}: a gap in the numbering, stated in no document")

    print("\n".join(lines))
    linked = sum(len(v) for v in tasks.values())
    print(f"\nfindings: {len(rows)} stated, {len(tasks)} with a task, {linked} task(s) linked, "
          f"{len(problems)} disagreeing")
    if not matched:
        print(f"note: {cfg['tasks_glob']} matched no files, so nothing was compared - this is a "
              f"clean exit over an absent task side, not over an agreeing one")
    if cfg["closed_marker"] == "":
        print("note: closed_marker is empty, so row state is not read and half the check is off")
    if unreadable:
        print(f"note: {unreadable}, so the numbering is not read as a sequence and gaps are not checked")
    elif len(report_paths(cfg)) == 1:
        print("note: one document is configured, so a finding stated only in the other is a gap "
              "this run cannot see")
    for p in problems:
        print(f"  MISMATCH  {p}")

    return 1 if (args.check and problems) else 0


if __name__ == "__main__":
    sys.exit(main())
