#!/usr/bin/env python3
"""What is on disk, what of it is regenerable, and what deleting any of it would cost.

    python scripts/storage_report.py
    python scripts/storage_report.py --tsv results/storage-report.tsv

NOTHING IS EVER DELETED BY THIS SCRIPT. It measures and reports; every removal
is a judgement about what evidence the project can afford to lose, and that
belongs to a person with the context, not to a tool with a size threshold.

Why this exists
---------------
`data/retrieved/` grows without bound by design - every archive ever fetched is
kept, because that is what makes a past report reproducible - and the obvious
reaction to a full disk is to delete the biggest thing. The biggest thing here
is the one that cannot be recovered. So the report sorts by RECOVERABILITY
rather than by size:

* **Archives and their `.meta.tsv.gz` sidecars cannot be re-fetched.** Retrieval
  is incremental (`datetype=mdat`), so each archive is the set of records that
  changed since the previous run - a snapshot that NCBI will not reproduce on
  request. Records are also revised and withdrawn. Delete an archive and the
  deposits it held are gone from every future report, silently, as a gap in the
  per-year table rather than an error. The sidecars are worse per byte: they
  carry the deposit dates, which are the drift statistic's whole x-axis, and
  they are about 0.2% of the volume.
* **Screens and reports are regenerable** from the archives, deterministically,
  at a CPU cost this script states in minutes rather than in the abstract.

Between those sits the material this report exists to surface, which is neither
irreplaceable nor free:

* **Orphaned groups.** A retrieval group is a (taxid, query) pair taken from the
  registry. Re-scope a query or retire an assay and the old group's archives
  stay on disk, screened by nothing and reported in nothing. They are still the
  only copy of those records, so they are a decision, not garbage - but they are
  the first thing to look at.
* **Cross-group duplication.** Archives are stored per group, while a record
  belongs to as many groups as match it. A record matching three gene queries on
  one taxon is stored three times. That is the design doing exactly what it says,
  and on gene-sized records it is cheap; on the multi-megabase assemblies of the
  Mycobacterium groups it is not.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from assaywatch.accession import strip_version  # noqa: E402
from assaywatch.retrieve import targets_from_registry  # noqa: E402
from assaywatch.score import load_config  # noqa: E402

# Measured on 2026-10-14: 139 archives, 6.3 GB gzipped, screened in about 35
# minutes on 10 cores at 6 workers per archive. Used only to turn a byte count
# into the sentence a reader actually needs ("this costs an afternoon, or it
# costs the evidence").
MINUTES_PER_GB_SCREENED = 35 / 6.3


def human(n: float) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if abs(n) < 1024 or unit == "GB":
            return f"{n:,.1f} {unit}" if unit != "B" else f"{n:,.0f} B"
        n /= 1024
    return f"{n:,.1f} GB"


def dir_size(path: Path) -> int:
    return sum(f.stat().st_size for f in path.rglob("*") if f.is_file())


def accessions(meta: Path) -> set[str]:
    """Accessions in one metadata sidecar, version stripped (the join key elsewhere)."""
    out = set()
    with gzip.open(meta, "rt") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            acc = strip_version(row.get("accession") or "")
            if acc:
                out.add(acc)
    return out


def survey(retrieved: Path, registry: Path, cfg: dict) -> tuple[dict, dict, set]:
    """({(taxid, group): bytes}, {(taxid, group): accessions}, groups the registry wants)."""
    wanted = set(targets_from_registry([registry], cfg))
    size: dict[tuple[int, str], int] = defaultdict(int)
    accs: dict[tuple[int, str], set[str]] = defaultdict(set)
    for fasta in retrieved.rglob("*.fasta.gz"):
        rel = fasta.relative_to(retrieved)
        if len(rel.parts) < 3 or not rel.parts[0].isdigit():
            continue
        key = (int(rel.parts[0]), rel.parts[1])
        size[key] += fasta.stat().st_size
    for meta in retrieved.rglob("*.meta.tsv.gz"):
        rel = meta.relative_to(retrieved)
        if len(rel.parts) < 3 or not rel.parts[0].isdigit():
            continue
        accs[(int(rel.parts[0]), rel.parts[1])] |= accessions(meta)
    return dict(size), dict(accs), wanted


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--retrieved", type=Path, default=ROOT / "data" / "retrieved")
    ap.add_argument("--results", type=Path, default=ROOT / "results")
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--tsv", type=Path, default=None, help="also write the per-group table here")
    ap.add_argument(
        "--min-overlap-mb",
        type=float,
        default=10.0,
        help="report cross-group duplication only above this size (default 10)",
    )
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    size, accs, wanted = survey(args.retrieved, args.registry, cfg)
    total = sum(size.values())
    meta_total = sum(f.stat().st_size for f in args.retrieved.rglob("*.meta.tsv.gz"))

    print("CANNOT BE RE-FETCHED (incremental snapshots; NCBI revises and withdraws records)")
    print(f"  {human(total):>12}  sequence archives, {len(size)} groups")
    print(
        f"  {human(meta_total):>12}  deposit-date sidecars - the drift statistic's x-axis, "
        f"{meta_total / max(total, 1):.1%} of the volume"
    )

    screened = args.results / "screened"
    reports = [d for d in args.results.glob("*") if d.is_dir() and d.name[:2] == "20"]
    screened_b = dir_size(screened) if screened.exists() else 0
    reports_b = sum(dir_size(d) for d in reports)
    print("\nREGENERABLE from the archives, at a CPU cost")
    print(
        f"  {human(screened_b):>12}  results/screened - rescreening all of it is about "
        f"{total / 1e9 * MINUTES_PER_GB_SCREENED:.0f} min on 10 cores"
    )
    print(
        f"  {human(reports_b):>12}  results/<date> reports, {len(reports)} runs - minutes, from the screens"
    )

    orphans = {k: v for k, v in size.items() if k not in wanted}
    print(f"\nORPHANED: the registry no longer asks for these groups ({len(orphans)})")
    if not orphans:
        print("  none - every archive on disk belongs to a group the registry still requests")
    for k, v in sorted(orphans.items(), key=lambda x: -x[1]):
        live = sorted(g for g in wanted if g[0] == k[0])
        covered = ""
        if live and accs.get(k):
            union: set[str] = set()
            for g in live:
                union |= accs.get(g, set())
            if union:
                share = len(accs[k] & union) / len(accs[k])
                only = len(accs[k] - union)
                covered = f"; {share:.0%} of its accessions are in live groups, {only:,} are not"
        print(f"  {human(v):>12}  {k[0]}/{k[1]}{covered}")
    if orphans:
        print("  Still the only copy of those records. Re-scoping a query brings the group back,")
        print("  but not the deposits that have changed or gone since.")

    print(
        f"\nCROSS-GROUP DUPLICATION above {args.min_overlap_mb:g} MB "
        "(archives are per group; a record belongs to every group that matches it)"
    )
    by_taxid: dict[int, list[tuple[int, str]]] = defaultdict(list)
    for k in size:
        by_taxid[k[0]].append(k)
    rows, found = [], False
    for taxid, keys in sorted(by_taxid.items()):
        keys = sorted(keys, key=lambda k: -size[k])
        for i, a in enumerate(keys):
            for b in keys[i + 1 :]:
                if not (accs.get(a) and accs.get(b)):
                    continue
                shared = accs[a] & accs[b]
                if not shared:
                    continue
                smaller = min(len(accs[a]), len(accs[b]))
                # Bytes are not per accession, so attribute the shared share of
                # the smaller archive: an estimate, and labelled as one.
                est = size[b] * len(shared) / max(len(accs[b]), 1)
                if est / 1e6 < args.min_overlap_mb:
                    continue
                found = True
                print(
                    f"  ~{human(est):>11}  {taxid}/{a[1]} and {taxid}/{b[1]} share "
                    f"{len(shared):,} accessions ({len(shared) / smaller:.0%} of the smaller)"
                )
                rows.append(
                    {
                        "taxid": taxid,
                        "group_a": a[1],
                        "group_b": b[1],
                        "shared_accessions": len(shared),
                        "share_of_smaller": f"{len(shared) / smaller:.3f}",
                        "estimated_duplicate_bytes": int(est),
                    }
                )
    if not found:
        print("  none above the threshold")
    else:
        print("  Deduplicating means storing each record once and having groups reference it,")
        print("  which changes the archive format. Nothing here is safe to delete on its own:")
        print("  each group's archive is what makes that group's past screens reproducible.")

    if args.tsv:
        args.tsv.parent.mkdir(parents=True, exist_ok=True)
        cols = ["taxid", "group", "bytes", "accessions", "status"]
        with args.tsv.open("w", newline="") as fh:
            w = csv.DictWriter(fh, cols, delimiter="\t")
            w.writeheader()
            for k, v in sorted(size.items(), key=lambda x: -x[1]):
                w.writerow(
                    {
                        "taxid": k[0],
                        "group": k[1],
                        "bytes": v,
                        "accessions": len(accs.get(k, ())),
                        "status": "orphaned" if k not in wanted else "live",
                    }
                )
        print(f"\nwrote {args.tsv}")

    print("\nNothing was deleted. To reclaim space, the order that loses the least is:")
    print("  1. results/<date>/ for runs you no longer cite - regenerable from the screens")
    print("  2. results/screened/ - regenerable from the archives, at the CPU cost above")
    print("  3. orphaned groups - only after deciding their records are not wanted again")
    print("  The archives and their sidecars are the evidence; they are last, not first.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
