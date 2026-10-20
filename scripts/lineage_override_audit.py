#!/usr/bin/env python3
"""Enumerate the assays whose status comes from a lineage override, one row each.

    python scripts/lineage_override_audit.py --calls results/2026-10-18/calls.tsv.gz \
        --out /tmp/overrides.tsv

Three docs in a row re-derived "the 17 overrides" by hand from a calls table
(docs/2026-10-19-taxid-artefacts.md, docs/2026-10-19-pan-family-cases.md,
docs/2026-10-20-pan-family-override.md), and the set moves with every rule
change, so it is worth a script. Read-only: it writes one TSV and touches
nothing else.

The row answers the question curation has to ask before any threshold rule
does — is the firing lineage one the assay's design paper ever claimed? — so it
carries the lineage's name and rank, whether it is already inside the entry's
`scope_taxids`, and whether that paper is on disk to read.

`above_pooled` marks the pattern docs/2026-10-20-pan-family-override.md point 2
is about: the "failing" lineage detects at or above the pooled share, so the
override is calling a better-than-average slice of the pool a decline.

A calls table older than the last registry rename carries assay ids the registry
no longer holds, which is the flaw docs/RESUME-HERE.md flags against every status
count taken off the 2026-10-17 calls. Ids are resolved through
docs/rename-mapping.tsv: a REMOVE is dropped and counted, a RENAME is followed,
and anything in neither the registry nor the mapping is reported rather than
silently given blank columns.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from retrospective import (  # noqa: E402
    _build_scope_map,
    _query_taxids,
    load_evidence,
    status_from_evidence,
)

from assaywatch.score import load_config  # noqa: E402
from assaywatch.taxonomy import taxonomy_from_config  # noqa: E402
from assaywatch.validate import iter_files, load_assay  # noqa: E402

COLUMNS = [
    "assay_id",
    "calls_assay_id",
    "status",
    "status_pooled",
    "pooled_share",
    "pooled_n",
    "lineage_label",
    "lineage_taxid",
    "lineage_name",
    "lineage_rank",
    "lineage_share",
    "lineage_n",
    "above_pooled",
    "has_scope_taxids",
    "in_current_scope",
    "citation_doi",
    "paper_on_disk",
]

# "Orthopoxvirus vaccinia (10245)" or the bare "taxid_10245" fallback; a
# hand-entered name from docs/taxa-cache.json carries no taxid at all.
LABEL_TAXID = re.compile(r"^taxid_(\d+)$|\((\d+)\)$")


def taxid_of(stats) -> int | None:
    """The firing lineage's taxid, from the stats or out of its display label."""
    if stats.taxid is not None:
        return stats.taxid
    m = LABEL_TAXID.search(stats.lineage_name)
    if not m:
        return None
    return int(m.group(1) or m.group(2))


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


def paper_path(doi: str | None) -> Path | None:
    """papers/<doi with slash and brackets as underscores>, if present.

    The convention in papers/ keeps the DOI's dots and lower-cases the whole
    thing: 10.1016/S0166-0934(96)02155-6 is 10.1016_s0166-0934_96_02155-6.pdf.
    """
    if not doi:
        return None
    stem = re.sub(r"[/()]", "_", doi.lower())
    for p in (ROOT / "papers").glob("*"):
        if p.stem.lower() == stem:
            return p
    return None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--calls", type=Path, required=True, help="calls.tsv.gz from a full run")
    ap.add_argument("--retrieved", type=Path, default=ROOT / "data" / "retrieved")
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--config", type=Path, default=ROOT / "config.yaml")
    ap.add_argument("--as-of", type=date.fromisoformat, default=None, help="default: today")
    ap.add_argument("--renames", type=Path, default=ROOT / "docs" / "rename-mapping.tsv")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    taxonomy = taxonomy_from_config(cfg)
    scope_map = _build_scope_map(args.registry) or {}
    entries = {a.id: a for a in map(load_assay, iter_files(args.registry))}
    renamed, removed = rename_map(args.renames)

    evidence = load_evidence(args.calls, args.retrieved, cfg, _query_taxids(args.registry))
    drifts, _ = status_from_evidence(evidence, cfg, args.as_of or date.today(), scope_map=scope_map)

    rows = []
    dropped: list[str] = []
    unknown: list[str] = []
    for calls_id, d in drifts.items():
        if not d.lineage_override or d.lineage_worst_idx is None:
            continue
        assay_id = calls_id if calls_id in entries else renamed.get(calls_id, calls_id)
        if assay_id not in entries:
            (dropped if calls_id in removed else unknown).append(calls_id)
            continue
        worst = d.lineage_stats[d.lineage_worst_idx]
        taxid = taxid_of(worst)
        scope = scope_map.get(assay_id)
        in_scope = ""
        if scope and taxid is not None:
            in_scope = "yes" if taxonomy and taxonomy.within(taxid, scope) else "no"
        entry = entries.get(assay_id)
        doi = entry.citation.doi if entry and entry.citation else None
        pooled = d.recent_fraction
        rows.append(
            {
                "assay_id": assay_id,
                "calls_assay_id": calls_id,
                "status": d.status,
                "status_pooled": d.status_pooled or "",
                "pooled_share": f"{pooled:.4f}" if pooled is not None else "",
                "pooled_n": d.recent_evaluable,
                "lineage_label": worst.lineage_name,
                "lineage_taxid": taxid if taxid is not None else "",
                "lineage_name": (taxonomy.name.get(taxid, "") if taxonomy and taxid else ""),
                "lineage_rank": (taxonomy.rank.get(taxid, "") if taxonomy and taxid else ""),
                "lineage_share": f"{worst.share:.4f}",
                "lineage_n": worst.n_evaluable,
                "above_pooled": ("yes" if pooled is not None and worst.share >= pooled else "no"),
                "has_scope_taxids": "yes" if scope else "no",
                "in_current_scope": in_scope,
                "citation_doi": doi or "",
                "paper_on_disk": (paper_path(doi).name if paper_path(doi) else ""),
            }
        )

    rows.sort(key=lambda r: (r["status_pooled"], r["assay_id"]))
    with args.out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    above = sum(1 for r in rows if r["above_pooled"] == "yes")
    by_pooled: dict[str, int] = {}
    for r in rows:
        by_pooled[r["status_pooled"]] = by_pooled.get(r["status_pooled"], 0) + 1
    print(f"{len(rows)} lineage overrides, {above} on a lineage at or above the pooled share")
    if dropped:
        print(f"  dropped, removed from the registry: {', '.join(sorted(dropped))}")
    if unknown:
        print(f"  NOT IN REGISTRY OR RENAME MAP, excluded: {', '.join(sorted(unknown))}")
    for pooled_status, n in sorted(by_pooled.items()):
        print(f"  pooled {pooled_status}: {n}")
    print(f"written: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
