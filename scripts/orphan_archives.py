#!/usr/bin/env python
"""Report retrieval archives that no live assay asks for any more.

    python scripts/orphan_archives.py
    python scripts/orphan_archives.py --tsv results/orphan-archives.tsv

A retrieval group is `(taxid, group)`, where `group` is `all` or a hash of the
assays' shared `target.query` (`assaywatch.retrieve.group_slug`). The live set is
whatever `registry/` asks for today. An archive on disk whose group is not in
that set is an orphan: nothing screens it, nothing reports it, and it still
occupies disk and still has entries in `data/retrieved/manifest.json` that look
like ordinary retrieval state.

Two ways a group goes dead, both routine:

  * **an assay leaves `registry/`** -- deprecated, removed, or moved to
    `pending/` because it has no verified DOI. On 2026-10-23 that move alone
    orphaned three groups and 74 manifest runs.
  * **a `target.query` changes.** The group name is a hash of the query, so
    editing one retires the old group and starts a new one. The old archives stay.

This was found the hard way: a forced rescreen of every archive on disk died at
DAG construction with `KeyError: (2093, 'q4185828e3e')`, because that archive's
group no longer exists in the registry. Nothing else reports it, which is why
this script exists.

**It proposes and never deletes.** An orphan is not necessarily rubbish: an assay
in `pending/` may come back the day its DOI resolves, and its archives are then
exactly the history that makes a baseline possible. Deleting is a judgement about
whether that assay is coming back, so it stays with the maintainer. `--tsv`
writes the list for whoever makes that call.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch.retrieve import targets_from_registry  # noqa: E402
from assaywatch.validate import iter_files, load_assay  # noqa: E402

COLS = ["taxid", "group", "archives", "bytes", "manifest_runs", "explained_by"]


def live_groups(registry: Path, cfg: dict) -> set[tuple[int, str]]:
    """`(taxid, group)` for every retrieval group the registry asks for."""
    return {(int(t), g) for t, g in targets_from_registry([registry], cfg)}


def archives_on_disk(retrieved: Path) -> dict[tuple[int, str], list[Path]]:
    """`(taxid, group) -> [archive paths]` for everything under `retrieved`.

    A non-numeric taxid directory is skipped rather than raising: `data/retrieved/`
    also holds `runs/` and the manifest, which are not archives.
    """
    out: dict[tuple[int, str], list[Path]] = {}
    for fasta in sorted(retrieved.glob("*/*/*.fasta.gz")):
        taxid_dir, group = fasta.parent.parent.name, fasta.parent.name
        if not taxid_dir.isdigit():
            continue
        out.setdefault((int(taxid_dir), group), []).append(fasta)
    return out


def manifest_runs(path: Path) -> dict[tuple[int, str], int]:
    """How many manifest runs name each group. Missing manifest -> empty."""
    try:
        runs = json.loads(path.read_text()).get("runs", [])
    except (OSError, ValueError):
        return {}
    counts: dict[tuple[int, str], int] = {}
    for run in runs:
        try:
            key = (int(run["taxid"]), run.get("group") or "all")
        except (KeyError, TypeError, ValueError):
            continue
        counts[key] = counts.get(key, 0) + 1
    return counts


def pending_by_taxid(pending: Path) -> dict[int, list[str]]:
    """`taxid -> [assay ids]` for entries waiting on a verified DOI."""
    out: dict[int, list[str]] = {}
    if not pending.is_dir():
        return out
    for path in iter_files(pending):
        try:
            assay = load_assay(path)
        except Exception:  # noqa: BLE001 - a malformed pending entry is validate's business
            continue
        if assay.target.taxid is not None:
            out.setdefault(assay.target.taxid, []).append(assay.id)
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--pending", type=Path, default=ROOT / "pending")
    ap.add_argument("--config", type=Path, default=ROOT / "config.yaml")
    ap.add_argument("--retrieved", type=Path, default=None, help="default: the config's retrieved_dir")
    ap.add_argument("--tsv", type=Path)
    args = ap.parse_args(argv)

    cfg = yaml.safe_load(args.config.read_text()) or {}
    retrieved = args.retrieved or ROOT / cfg.get("retrieved_dir", "data/retrieved")
    live = live_groups(args.registry, cfg)
    on_disk = archives_on_disk(retrieved)
    counts = manifest_runs(retrieved / "manifest.json")
    pending = pending_by_taxid(args.pending)

    rows = []
    for (taxid, group), files in sorted(on_disk.items()):
        if (taxid, group) in live:
            continue
        rows.append(
            {
                "taxid": taxid,
                "group": group,
                "archives": len(files),
                "bytes": sum(f.stat().st_size for f in files),
                "manifest_runs": counts.get((taxid, group), 0),
                "explained_by": " ".join(pending.get(taxid, [])),
            }
        )

    print(f"{len(live)} live retrieval groups; {len(on_disk)} groups have archives on disk")
    if not rows:
        print("no orphans: every archive belongs to a group the registry still asks for")
        return 0

    total = sum(r["bytes"] for r in rows)
    print(
        f"\n{len(rows)} orphan group(s), {sum(r['archives'] for r in rows)} archives, {total / 1e6:,.0f} MB"
    )
    width = max(len(f"{r['taxid']}/{r['group']}") for r in rows)
    for r in rows:
        where = f"{r['taxid']}/{r['group']}"
        why = f"  <- pending: {r['explained_by']}" if r["explained_by"] else ""
        print(
            f"  {where:<{width}}  {r['archives']:3d} archives  {r['bytes'] / 1e6:7,.0f} MB"
            f"  {r['manifest_runs']:3d} manifest runs{why}"
        )

    explained = [r for r in rows if r["explained_by"]]
    if explained:
        print(
            f"\n{len(explained)} of these belong to assays in pending/, which come back if their DOI "
            "resolves. Their archives are that assay's history; keep them unless the entry is being dropped."
        )
    # A live group with no archive is the mirror-image gap and is cheap to say here.
    missing = sorted(k for k in live if k not in on_disk)
    if missing:
        print(f"\nAlso: {len(missing)} live group(s) have no archive yet, so they have never been screened:")
        for taxid, group in missing:
            print(f"  {taxid}/{group}")

    if args.tsv:
        args.tsv.parent.mkdir(parents=True, exist_ok=True)
        with args.tsv.open("w", newline="") as fh:
            w = csv.DictWriter(fh, COLS, delimiter="\t")
            w.writeheader()
            w.writerows(rows)
        print(f"\nwrote {len(rows)} rows to {args.tsv}")

    print("\nNothing was deleted. This script only reports.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
