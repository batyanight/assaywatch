#!/usr/bin/env python3
"""Build docs/taxonomy-cache.json.gz: parent links, ranks, names and merges for every taxid we use.

    python scripts/build_taxonomy_cache.py            # archives + registry -> docs/taxonomy-cache.json.gz

Covers every taxid in the retrieved archives (backfill sidecar plus metadata
taxid columns) and every `target.taxid` and `scope_taxids` entry in the registry.
Run it on the Mac (needs Entrez Direct and eutils.ncbi.nlm.nih.gov) after a
retrieval brings in new taxa. assaywatch.taxonomy reads the result offline.

For each batch, `efetch -format xml` returns the taxon with its full lineage,
which gives a parent link, rank and name for every node on the path to the root.
Ranks let lineage grouping roll a no-rank strain up to its species; names are kept
only for the "unclassified ..." nodes, which mark buckets (see assaywatch/taxonomy.py). A merged taxid
comes back under its new id, so any requested id missing from the reply is
looked up with `-format docsum`, whose Status/AkaTaxId say "merged into N". An
id NCBI has deleted is listed in the output as `missing`.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch.validate import iter_files, load_assay  # noqa: E402

BATCH = 200


def archive_taxids(retrieved: Path) -> set[int]:
    out: set[int] = set()
    sidecar = retrieved / ".meta.taxid.backfill.tsv.gz"
    if sidecar.exists():
        with gzip.open(sidecar, "rt") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                if (row.get("taxid") or "").isdigit():
                    out.add(int(row["taxid"]))
    for meta in sorted(retrieved.rglob("*.meta.tsv.gz")):
        with gzip.open(meta, "rt") as fh:
            reader = csv.DictReader(fh, delimiter="\t")
            if "taxid" not in (reader.fieldnames or []):
                continue
            out.update(int(r["taxid"]) for r in reader if (r.get("taxid") or "").isdigit())
    return out


def registry_taxids(registry: Path) -> set[int]:
    out: set[int] = set()
    for path in iter_files(registry):
        a = load_assay(path)
        if a.target.taxid is not None:
            out.add(a.target.taxid)
        out.update(a.target.scope_taxids or [])
    return out


def efetch(ids: list[int], fmt: str) -> str:
    # stdin from /dev/null: Entrez Direct blocks reading a pipe otherwise.
    return subprocess.run(
        ["efetch", "-db", "taxonomy", "-id", ",".join(map(str, ids)), "-format", fmt],
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--retrieved", type=Path, default=ROOT / "data" / "retrieved")
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--out", type=Path, default=ROOT / "docs" / "taxonomy-cache.json.gz")
    args = ap.parse_args(argv)

    wanted = sorted(archive_taxids(args.retrieved) | registry_taxids(args.registry))
    print(f"{len(wanted)} taxids to resolve", file=sys.stderr)

    parent: dict[int, int] = {}
    rank: dict[int, str] = {}
    name: dict[int, str] = {}
    returned: set[int] = set()
    for i in range(0, len(wanted), BATCH):
        root = ET.fromstring(efetch(wanted[i : i + BATCH], "xml"))
        for taxon in root.findall("Taxon"):
            tid = int(taxon.findtext("TaxId"))
            returned.add(tid)
            nodes = taxon.findall("LineageEx/Taxon") + [taxon]
            path = [int(t.findtext("TaxId")) for t in nodes]
            for up, down in zip(path, path[1:], strict=False):
                parent[down] = up
            for t, node in zip(path, nodes, strict=True):
                rank[t] = node.findtext("Rank") or "no rank"
                name[t] = node.findtext("ScientificName") or ""
        if (i // BATCH) % 50 == 0:
            print(f"  {min(i + BATCH, len(wanted))}/{len(wanted)}", file=sys.stderr)

    # A record-level taxid with no species on its path to the root becomes a lineage
    # grouping key under `lineage.group_at_rank: species` -- a no-rank node NCBI files
    # beside species rather than under one -- and only a kept name can label it.
    # Keeping names for exactly these keeps the file small. (The 775 `taxid_<n>` rows
    # of the 2026-10-26 lineage report were first blamed on this and were not it:
    # every one of those 322 taxids HAS a species above it, and lineage_report.py was
    # simply not rolling up. Fixed there the same day; this set was 3 ids.)
    direct = archive_taxids(args.retrieved)

    def has_species_ancestor(t: int) -> bool:
        seen: set[int] = set()
        while t in parent and t not in seen:
            if rank.get(t) == "species":
                return True
            seen.add(t)
            t = parent[t]
        return rank.get(t) == "species"

    grouping_keys = {t for t in direct if t in rank and not has_species_ancestor(t)}

    merged: dict[int, int] = {}
    unresolved = [t for t in wanted if t not in returned and t not in parent]
    for i in range(0, len(unresolved), BATCH):
        root = ET.fromstring(efetch(unresolved[i : i + BATCH], "docsum"))
        for doc in root.iter("DocumentSummary"):
            tid, aka = doc.findtext("TaxId"), doc.findtext("AkaTaxId")
            if tid and aka and aka.isdigit() and int(aka) not in (0, int(tid)):
                merged[int(tid)] = int(aka)
    missing = sorted(t for t in unresolved if t not in merged)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(args.out, "wt") as fh:
        json.dump(
            {
                "description": "NCBI taxonomy parent links and merges; built by scripts/build_taxonomy_cache.py",
                "built": date.today().isoformat(),
                "n_requested": len(wanted),
                "parent": {str(k): v for k, v in sorted(parent.items())},
                "rank": {str(k): v for k, v in sorted(rank.items()) if v != "no rank"},
                # Species names, for per-species report tables; the "unclassified ..."
                # nodes, which in_unclassified reads; and the record-level taxids that
                # have no species above them and so are lineage keys in their own
                # right (see `grouping_keys`). Every name would quadruple the committed
                # file for nodes nothing displays; these three sets are what displays.
                "name": {
                    str(k): v
                    for k, v in sorted(name.items())
                    if rank.get(k) == "species" or v.startswith("unclassified ") or k in grouping_keys
                },
                "merged": {str(k): v for k, v in sorted(merged.items())},
                "missing": missing,
            },
            fh,
            separators=(",", ":"),
        )
    print(
        f"{len(parent)} parent links, {len(rank)} ranks, {len(merged)} merges, {len(missing)} missing -> {args.out}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
