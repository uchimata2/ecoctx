#!/usr/bin/env python3
"""Assert every figure drawn in a chart also appears in `README.md`.

The numbers in a chart are the most quotable thing this README publishes and were the only ones
nothing re-measured. `check_readme.py` covers the five installed-cost rows because those are
sizes of files in this tree; the graded-run figures are not sizes of anything here, so no
measurement can confirm them. What *can* be confirmed is that the picture and the prose still
say the same thing, and that is what goes stale: prose gets corrected in a rewrite and the
image, being a separate file, does not.

**The check runs one way, and the direction is the whole design.** Every number drawn in a
chart must appear in the README; the reverse is false, because the README states figures no
chart draws. A checker asserting both directions would fail on its first correct sentence.

**What counts as a number here.** Any digit run in a `<text>` element, with thousands commas
and a trailing percent sign kept, because `21.8%` and `218` are different claims. Numbers in
the markup rather than in a label - coordinates, widths, viewBox - are not drawn and are not
checked. A chart whose bar geometry is wrong is a defect this cannot see; a chart whose label
contradicts the text is one it can.

    python tools/check_charts.py

Standard library only. Runs from any working directory.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
ASSETS = ROOT / "assets"

TEXT_RE = re.compile(r"<text\b[^>]*>(.*?)</text>", re.S)
NUM_RE = re.compile(r"-?\d[\d,]*(?:\.\d+)?%?")


def drawn(svg: str) -> list[str]:
    """Every number that a reader can see in the rendered chart, in order."""
    out: list[str] = []
    for label in TEXT_RE.findall(svg):
        out.extend(NUM_RE.findall(label))
    return out


def main() -> int:
    if not ASSETS.is_dir():
        print("check_charts: no assets/ directory, so no chart can disagree with anything")
        return 0

    charts = sorted(ASSETS.glob("*.svg"))
    if not charts:
        print("check_charts: assets/ holds no SVG")
        return 0

    readme = README.read_text(encoding="utf-8")
    referenced = {p.name for p in charts if f"assets/{p.name}" in readme}

    problems: list[str] = []
    print(f"=== {len(charts)} chart(s)")
    for chart in charts:
        numbers = drawn(chart.read_text(encoding="utf-8"))
        missing = [n for n in numbers if n.lstrip("-") not in readme]
        state = "ok " if not missing and chart.name in referenced else "OFF"
        print(f"  {state} {chart.name:<16} {len(numbers)} figure(s) drawn")
        if chart.name not in referenced:
            problems.append(f"{chart.name}: committed but not referenced from README.md")
        for n in dict.fromkeys(missing):
            problems.append(f"{chart.name}: draws {n!r}, which README.md does not say")

    if problems:
        print(f"\ncheck_charts: {len(problems)} problem(s)")
        for line in problems:
            print(f"  MISMATCH  {line}")
        print("\nA chart and the prose beside it are one claim. Correct whichever is wrong.")
        return 1

    print(f"\ncheck_charts: {len(charts)} chart(s) checked, 0 problem(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
