#!/usr/bin/env python3
"""Move an entry off a taxid NCBI has merged away. Proposes by default.

    python scripts/retire_merged_taxids.py                 # dry
    python scripts/retire_merged_taxids.py --write

WHY THIS IS NOT A SED. `data/retrieved/` is keyed by `target.taxid`, so changing one
moves the entry's retrieval group: the archive directory has to move with it and the
manifest has to be rebuilt, or the next run re-fetches everything under a new key.
That makes this a three-step operation with an order, and the order is in the
roadmap entry and in `docs/journal/2026-10-27-retired-taxids.md`.

WHY IT MATTERS AT ALL, since retrieval resolves a merged id today and nothing has
noticed: an entry on a retired id is one taxonomy release from an empty archive, and
the failure mode is silence. `scripts/check_taxids.py` found these 18 on 2026-10-27
while reporting 4,113 false scope escapes, every one of them a child whose ancestor
list carries the NEW root.

The mapping is NOT inferred here. It is what `check_taxids.py --quiet` printed on its
MERGED lines against NCBI on 2026-10-27, pasted in so this script is a record of the
move rather than a second guess at it; `--check-ncbi` re-asks NCBI and refuses to run
if any pair has changed since.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

#: old taxid -> (canonical taxid, NCBI's current scientific name for it)
MERGED: dict[int, tuple[int, str]] = {
    11232: (3052342, "Morbillivirus canis"),
    121791: (3052225, "Henipavirus nipahense"),
    11051: (3044782, "Orthoflavivirus"),
    10292: (3044472, "Orthoherpesviridae"),
}

NOTE = (
    "TAXID RETIRED {date}: NCBI has merged {old} into {new} ({name}), so this entry now "
    "carries the canonical id. Retrieval resolved the old id and nothing had noticed, which "
    "is the point -- an entry on a retired id is one taxonomy release from an empty archive. "
    "data/retrieved/{old}/ moved to data/retrieved/{new}/ and the manifest was rebuilt in the "
    "same commit, so no archive was re-fetched. Found by scripts/check_taxids.py's containment "
    "check; see docs/journal/2026-10-27-retired-taxids.md."
)


def check_ncbi(email: str) -> None:
    """Refuse the move if NCBI no longer says what the pasted mapping says."""
    from scripts.check_taxids import fetch_taxa

    taxa = fetch_taxa(sorted(MERGED), email)
    for old, (new, name) in MERGED.items():
        if old not in taxa:
            raise SystemExit(f"NCBI does not know taxid {old}")
        canonical, sci = taxa[old][4], taxa[old][0]
        if (canonical, sci) != (new, name):
            raise SystemExit(f"NCBI now says {old} -> {canonical} ({sci}), not {new} ({name})")
    print(f"NCBI agrees with all {len(MERGED)} pairs")


def remap_manifest(path: Path, write: bool) -> int:
    """Point every manifest run at the new taxid, its moved archive and its new query.

    NOT `scripts/rebuild_manifest.py`, which is the right tool for a LOST manifest and
    the wrong one here. A rebuild indexes the archives on disk, one entry per file: 497
    entries where this manifest holds 3,409, because 2,910 of them are incremental runs
    that fetched nothing. Those carry the cursor -- the last date each group was ASKED --
    and `last_run_date` reads it to decide what to request next. Rebuilding would set
    every cursor back to the date of the group's newest archive and re-ask NCBI for the
    window in between, across all 132 groups, for no gain. A remap keeps the history.

    The query string is rewritten too, because that is what the cursor is keyed on:
    `txid11232[Organism:exp] AND ...` has to become `txid3052342[...]` or the group
    reads as never fetched.
    """
    import json

    manifest = json.loads(path.read_text())
    touched = 0
    for run in manifest.get("runs", []):
        old = run.get("taxid")
        if old not in MERGED:
            continue
        new, _ = MERGED[old]
        run["taxid"] = new
        for key in ("fasta", "metadata"):
            if run.get(key):
                run[key] = run[key].replace(f"data/retrieved/{old}/", f"data/retrieved/{new}/")
        if run.get("query"):
            run["query"] = run["query"].replace(f"txid{old}[", f"txid{new}[")
        touched += 1
    print(f"{touched} manifest runs {'remapped' if write else 'would be remapped'}")
    if write:
        path.with_suffix(".json.bak").write_text(path.read_text())
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(manifest, indent=1, sort_keys=True))
        tmp.replace(path)
    return touched


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=REPO / "registry")
    ap.add_argument("--date", default="2026-10-27")
    ap.add_argument("--check-ncbi", metavar="EMAIL", help="re-ask NCBI before writing")
    ap.add_argument("--write", action="store_true")
    ap.add_argument(
        "--manifest",
        type=Path,
        help="also remap this manifest's runs (data/retrieved/manifest.json); "
        "the archive directories must already have been moved",
    )
    args = ap.parse_args(argv)

    if args.check_ncbi:
        check_ncbi(args.check_ncbi)

    if args.manifest:
        remap_manifest(args.manifest, args.write)

    changed = 0
    for path in sorted(args.registry.glob("*.yaml")):
        doc = yaml.safe_load(path.read_text()) or {}
        old = (doc.get("target") or {}).get("taxid")
        if old not in MERGED:
            continue
        new, name = MERGED[old]
        doc["target"]["taxid"] = new
        # Appended, never replacing: the existing note is the entry's provenance and
        # this is one more sentence of it.
        note = NOTE.format(date=args.date, old=old, new=new, name=name)
        source = doc.setdefault("source", {}) or {}
        doc["source"] = source
        existing = (source.get("notes_curator") or "").rstrip()
        source["notes_curator"] = f"{existing}\n\n{note}" if existing else note
        changed += 1
        print(f"{'WRITE' if args.write else 'would write'} {path.stem}: {old} -> {new}")
        if args.write:
            # A full round-trip, the way resolve_citations.py writes: pyyaml is what
            # the environment has, so a structural edit normalises the file's wrapping.
            # The validator and the fixture hook gate the result.
            path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=120))
    print(f"\n{changed} entries {'updated' if args.write else 'would be updated'} of 18 expected.")
    # 0 is fine on a re-run: the registry is already migrated and only the manifest
    # or the NCBI check is wanted. Any other count means the mapping and the registry
    # disagree, which is worth a non-zero exit.
    return 0 if changed in (0, 18) else 1


if __name__ == "__main__":
    sys.exit(main())
