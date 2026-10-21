#!/usr/bin/env python3
"""What changed between two runs' reports. For the weekly run's summary.

    python scripts/report_diff.py                     # the two newest under results/
    python scripts/report_diff.py results/2026-10-04 results/2026-10-11

Reads each run's `report.md` rather than recomputing anything, so the summary
says exactly what the reports say. Prints the status counts of both runs, then
one line per assay whose status changed, then assays that appeared or
disappeared. Exits 0 whether or not anything changed; `--quiet` prints nothing
when nothing did, so a weekly job can stay silent on a quiet week.

Assay ids are resolved through docs/rename-mapping.tsv (same loader as
scripts/lineage_override_audit.py): a RENAME is followed, so an assay renamed
between the two runs is one assay and not a disappearance plus an arrival, and
a REMOVE is reported as removed. Comparing 2026-10-17 with 2026-10-20 across
the 27 renames and 13 removals printed 56 gone and 33 new without this; with
it, 12 removed, 0 gone and 7 new.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HEADING = re.compile(r"^## ([A-Za-z ]+?)(?: \(\d+\))?$")
# The id column is "`id`", or "`id` (pooled: low coverage)" where a lineage
# verdict overrode the pooled status. 21 of the 208 rows in the 2026-10-20
# report carry that tag; ignoring it parsed 187 ids out of 208 and lost exactly
# the 17 declining and 4 low coverage assays the lineage rules had moved.
ROW = re.compile(r"^\| `([^`]+)`(?: \([^)]*\))? \|")
# The statuses assaywatch/drift.py can produce: report.py's STATUS_ORDER plus
# the "no data" default of AssayDrift. An allowlist because the set is closed
# and the report's other sections are not: the denylist this replaces
# ({"coverage gaps", "detail for flagged assays"}) went stale when
# "## Nested protocols" was added, which was then read as a status and took 20
# assays out of their real ones, so neither run's buckets summed to its own
# assay count.
STATUSES = frozenset(
    {
        "stable",
        "watch",
        "declining",
        "low coverage",
        "insufficient data",
        "no recent data",
        "no data",
    }
)


def statuses(report: Path) -> dict[str, str]:
    """{assay id: status} from a report.md.

    Rows under a heading that is not a status belong to a section that lists
    assays for another reason (Nested protocols, Coverage gaps) and are
    skipped. Plain assignment rather than `setdefault`: with the allowlist in
    place, section order no longer decides an assay's status, because
    report.py groups the assays by status and prints each one in exactly one
    status section - 0 of the 213 ids in the 2026-10-17 report and 0 of the 208
    in 2026-10-20 appear under two status headings.
    """
    out: dict[str, str] = {}
    status = None
    for line in report.read_text().splitlines():
        h = HEADING.match(line)
        if h:
            name = h.group(1).strip().lower()
            status = name if name in STATUSES else None
            continue
        r = ROW.match(line)
        if r and status:
            out[r.group(1)] = status
    return out


def rename_map(path: Path) -> tuple[dict[str, str], set[str]]:
    """({old id: new id} for RENAME, {old id} for REMOVE) from docs/rename-mapping.tsv."""
    renamed: dict[str, str] = {}
    removed: set[str] = set()
    if not path.exists():
        return renamed, removed
    with path.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row["action"] == "RENAME" and row["new_id"]:
                renamed[row["old_id"]] = row["new_id"]
            elif row["action"] == "REMOVE":
                removed.add(row["old_id"])
    return renamed, removed


def resolve(
    s: dict[str, str], renamed: dict[str, str], removed: set[str]
) -> tuple[dict[str, str], dict[str, str], list[str]]:
    """(statuses under current ids, {current id: the old id it was}, ids removed).

    A report that holds both an old id and its new id keeps them apart: they
    are two rows with two statuses, and folding one onto the other would pick a
    status at random. `stale_ids` reports that case instead.
    """
    out: dict[str, str] = {}
    was: dict[str, str] = {}
    dropped: list[str] = []
    for assay_id, status in s.items():
        if assay_id in removed:
            dropped.append(assay_id)
            continue
        new_id = renamed.get(assay_id)
        if new_id and new_id not in s:
            was[new_id] = assay_id
            out[new_id] = status
        else:
            out[assay_id] = status
    return out, was, sorted(dropped)


def stale_ids(s: dict[str, str], renamed: dict[str, str]) -> list[str]:
    """Ids a report lists under their old name while also listing the new one.

    Three in the 2026-10-20 report (the two Cryptosporidium rounds and
    Salmonella invA): the run screened a calls table older than the rename, the
    flaw docs/RESUME-HERE.md flags, so the same assay was scored twice under
    both names. Not a diff artefact - a run to re-screen.
    """
    return sorted(k for k in s if k in renamed and renamed[k] in s)


def counts(s: dict[str, str]) -> str:
    tally: dict[str, int] = {}
    for v in s.values():
        tally[v] = tally.get(v, 0) + 1
    return ", ".join(f"{n} {k}" for k, n in sorted(tally.items(), key=lambda kv: -kv[1]))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("runs", nargs="*", type=Path, help="two run directories (default: the two newest)")
    ap.add_argument("--results", type=Path, default=Path("results"))
    ap.add_argument("--renames", type=Path, default=ROOT / "docs" / "rename-mapping.tsv")
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

    old_raw, new_raw = statuses(old_dir / "report.md"), statuses(new_dir / "report.md")
    renamed, removed = rename_map(args.renames)
    old, old_was, old_dropped = resolve(old_raw, renamed, removed)
    new, new_was, new_dropped = resolve(new_raw, renamed, removed)
    was = {**old_was, **new_was}
    dropped = sorted(set(old_dropped) | set(new_dropped))
    stale = stale_ids(new_raw, renamed)

    changed = sorted(a for a in old.keys() & new.keys() if old[a] != new[a])
    gone = sorted(old.keys() - new.keys())
    added = sorted(new.keys() - old.keys())

    if args.quiet and not (changed or gone or added or dropped):
        return 0

    # The counts are of the reports as written, so they match each report's own
    # headline; the lists below are of assays, after renames are followed.
    print(f"{old_dir.name}: {counts(old_raw)}")
    print(f"{new_dir.name}: {counts(new_raw)}")
    if was:
        print(f"{len(was)} id(s) followed through {args.renames.name}")
    if stale:
        print(
            f"\n{len(stale)} assay(s) scored twice in {new_dir.name}, under both the old and new id: {', '.join(stale)}"
        )
    if not (changed or gone or added or dropped):
        print("\nNo assay changed status.")
        return 0
    if changed:
        print(f"\n{len(changed)} assays changed status:")
        # Worsening first: the reason anyone reads this.
        rank = {"stable": 0, "watch": 1, "low coverage": 2, "declining": 3}
        for a in sorted(changed, key=lambda x: -(rank.get(new[x], 0) - rank.get(old[x], 0))):
            print(f"  {old[a]} -> {new[a]}: {a}" + (f" (was `{was[a]}`)" if a in was else ""))
    for label, ids in (
        ("removed from the registry", dropped),
        ("no longer in the report", gone),
        ("new in the report", added),
    ):
        if ids:
            print(f"\n{len(ids)} {label}: {', '.join(ids)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
