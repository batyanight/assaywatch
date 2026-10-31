#!/usr/bin/env python3
"""Build docs/taxonomy-cache.json.gz: parent links, ranks, names and merges for every taxid we use.

    python scripts/build_taxonomy_cache.py            # archives + registry -> docs/taxonomy-cache.json.gz

Covers every taxid in the retrieved archives (backfill sidecar plus metadata
taxid columns) and every `target.taxid` and `scope_taxids` entry in the registry.
Run it on the Mac (needs eutils.ncbi.nlm.nih.gov; the client is assaywatch.ncbi) after a
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
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch import ncbi, registry  # noqa: E402
from assaywatch.credentials import contact_email  # noqa: E402

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


def registry_taxids(registry_dir: Path) -> set[int]:
    out: set[int] = set()
    for a in registry.load(registry_dir).values():
        if a.target.taxid is not None:
            out.add(a.target.taxid)
        out.update(a.target.scope_taxids or [])
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--retrieved", type=Path, default=ROOT / "data" / "retrieved")
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--out", type=Path, default=ROOT / "docs" / "taxonomy-cache.json.gz")
    ap.add_argument("--email", default=None, help="contact address for NCBI (default: the configured one)")
    args = ap.parse_args(argv)
    email = args.email or contact_email()
    if not email:
        ap.error("--email is required (or set ASSAYWATCH_EMAIL / .secrets/email)")

    wanted = sorted(archive_taxids(args.retrieved) | registry_taxids(args.registry))
    print(f"{len(wanted)} taxids to resolve", file=sys.stderr)
    transport = ncbi.eutils(email, ncbi.api_key())
    records = ncbi.taxon_records(wanted, transport, batch=BATCH)
    tree = ncbi.taxonomy_tree(records)

    direct = archive_taxids(args.retrieved)

    def has_species_ancestor(t: int) -> bool:
        seen: set[int] = set()
        while t in tree.parent and t not in seen:
            if tree.rank.get(t) == "species":
                return True
            seen.add(t)
            t = tree.parent[t]
        return tree.rank.get(t) == "species"

    # Record-level taxids with no species above them are lineage keys in their own
    # right, so their names are kept (see save_taxonomy_cache).
    grouping_keys = {t for t in direct if t in tree.rank and not has_species_ancestor(t)}

    unresolved = [t for t in wanted if t not in records]
    merged = ncbi.merged_taxids(unresolved, transport, batch=BATCH)
    missing = sorted(t for t in unresolved if t not in merged)
    ncbi.save_taxonomy_cache(
        args.out, records, merged=merged, n_requested=len(wanted), missing=missing, name_keys=grouping_keys
    )
    print(
        f"wrote {args.out}: {len(tree.parent)} parent links, {len(merged)} merged, {len(missing)} missing",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
