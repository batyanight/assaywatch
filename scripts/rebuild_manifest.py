#!/usr/bin/env python3
"""Rebuild data/retrieved/manifest.json from the archives actually on disk.

    python scripts/rebuild_manifest.py              # from the repo root
    python scripts/rebuild_manifest.py --dry-run    # show what it would write

The archives are the source of truth; the manifest is an index of them. If the
index is lost or damaged, this walks `data/retrieved/<taxid>/<group>/` and
writes one manifest entry per archive, so incremental retrieval knows where
each group left off and the pipeline knows what there is to screen.

Each entry gets the run date from the archive's file name, the record count
from its metadata table (much cheaper to read than the FASTA), and the query
and assay list from the current registry. Groups no longer in the registry
are still indexed, with an empty assay list, so their archives are not
orphaned. Leftover `.part` files from interrupted fetches are deleted: by
construction they are incomplete. The previous manifest, if any, is kept as
`manifest.json.bak`.
"""

from __future__ import annotations

import argparse
import gzip
import shutil
import sys
from pathlib import Path

from assaywatch.retrieve import build_query, manifest_path, targets_from_registry, write_manifest
from assaywatch.score import load_config


def count_rows(meta: Path) -> int:
    with gzip.open(meta, "rt") as fh:
        return max(0, sum(1 for _ in fh) - 1)  # minus the header


def rebuild(cfg: dict, registry: Path) -> tuple[dict, list[Path]]:
    root = Path(cfg.get("retrieved_dir", "data/retrieved"))
    groups = targets_from_registry([registry])
    runs, partials = [], []

    for taxdir in sorted(p for p in root.iterdir() if p.is_dir() and p.name.isdigit()):
        taxid = int(taxdir.name)
        for groupdir in sorted(p for p in taxdir.iterdir() if p.is_dir()):
            group = groupdir.name
            partials += sorted(groupdir.glob(".*.part"))
            info = groups.get((taxid, group), {"name": None, "query": None, "assays": []})
            archives = sorted(groupdir.glob("*.fasta.gz"))
            for i, fasta in enumerate(archives):
                stem = fasta.name[: -len(".fasta.gz")]
                meta = groupdir / f"{stem}.meta.tsv.gz"
                if not meta.exists():
                    print(f"WARNING {fasta}: no metadata beside it; skipped", file=sys.stderr)
                    continue
                n = count_rows(meta)
                runs.append(
                    {
                        "taxid": taxid,
                        "taxon_name": info["name"],
                        "run_date": stem[:10],
                        "query": build_query(taxid, cfg, info["query"]),
                        "mode": "full" if i == 0 else "incremental",
                        "since": None,
                        "n_available": n,
                        "n_fetched": n,
                        "fasta": str(fasta),
                        "metadata": str(meta),
                        "assays": info["assays"],
                        "note": "rebuilt from archive",
                        "group": group,
                        "assay_query": info["query"],
                    }
                )
    return {"runs": runs}, partials


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=Path("registry"))
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    manifest, partials = rebuild(cfg, args.registry)
    runs = manifest["runs"]
    groups = {(r["taxid"], r["group"]) for r in runs}
    print(
        f"{len(runs)} archives across {len(groups)} groups, "
        f"{sum(r['n_fetched'] for r in runs):,} records; {len(partials)} partial files"
    )
    if args.dry_run:
        return 0

    for p in partials:
        p.unlink()
    path = manifest_path(cfg)
    if path.exists():
        shutil.copy2(path, path.with_name(path.name + ".bak"))
    write_manifest(cfg, manifest)
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
