#!/usr/bin/env python3
"""What changed between two runs' reports. For the weekly run's summary.

    python scripts/report_diff.py                     # the two newest under results/
    python scripts/report_diff.py results/2026-10-04 results/2026-10-11

Reads each run's `report.md` rather than recomputing anything, so the summary
says exactly what the reports say. Prints the status counts of both runs, then
one line per assay whose status changed, then assays that appeared or
disappeared. Exits 0 whether or not anything changed; `--quiet` prints nothing
when nothing did, so a weekly job can stay silent on a quiet week.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

HEADING = re.compile(r"^## ([A-Za-z ]+?)(?: \(\d+\))?$")
ROW = re.compile(r"^\| `([^`]+)` \|")
# Section headings that are statuses, not other parts of the report.
SKIP = {"coverage gaps", "detail for flagged assays"}


def statuses(report: Path) -> dict[str, str]:
    """{assay id: status} from a report.md."""
    out: dict[str, str] = {}
    status = None
    for line in report.read_text().splitlines():
        h = HEADING.match(line)
        if h:
            name = h.group(1).strip()
            status = None if name.lower() in SKIP else name.lower()
            continue
        r = ROW.match(line)
        if r and status:
            out.setdefault(r.group(1), status)
    return out


def counts(s: dict[str, str]) -> str:
    tally: dict[str, int] = {}
    for v in s.values():
        tally[v] = tally.get(v, 0) + 1
    return ", ".join(f"{n} {k}" for k, n in sorted(tally.items(), key=lambda kv: -kv[1]))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("runs", nargs="*", type=Path, help="two run directories (default: the two newest)")
    ap.add_argument("--results", type=Path, default=Path("results"))
    ap.add_argument("--quiet", action="store_true", help="print nothing when no status changed")
    args = ap.parse_args(argv)

    if args.runs:
        if len(args.runs) != 2:
            ap.error("give two run directories, or none")
        old_dir, new_dir = args.runs
    else:
        dirs = sorted(d for d in args.results.glob("*") if (d / "report.md").exists())
        if len(dirs) < 2:
            print("only one run so far, nothing to compare" if dirs else "no reports found")
            return 0
        old_dir, new_dir = dirs[-2], dirs[-1]

    old, new = statuses(old_dir / "report.md"), statuses(new_dir / "report.md")
    changed = sorted(a for a in old.keys() & new.keys() if old[a] != new[a])
    gone = sorted(old.keys() - new.keys())
    added = sorted(new.keys() - old.keys())

    if args.quiet and not (changed or gone or added):
        return 0

    print(f"{old_dir.name}: {counts(old)}")
    print(f"{new_dir.name}: {counts(new)}")
    if not (changed or gone or added):
        print("\nNo assay changed status.")
        return 0
    if changed:
        print(f"\n{len(changed)} assays changed status:")
        # Worsening first: the reason anyone reads this.
        rank = {"stable": 0, "watch": 1, "low coverage": 2, "declining": 3}
        for a in sorted(changed, key=lambda x: -(rank.get(new[x], 0) - rank.get(old[x], 0))):
            print(f"  {old[a]} -> {new[a]}: {a}")
    for label, ids in (("no longer in the report", gone), ("new in the report", added)):
        if ids:
            print(f"\n{len(ids)} {label}: {', '.join(ids)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
