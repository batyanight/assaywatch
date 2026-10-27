#!/usr/bin/env python3
"""Can the archive clear an `orientation_inferred` flag? Measure, never edit.

    python scripts/check_orientation.py --calls results/<run>/calls.tsv.gz
    python scripts/check_orientation.py --calls ... --min-amplicons 50 --tsv .tmp/orientation.tsv

WHAT THE FLAG MEANS. `orientation_inferred`: which oligo is the forward and which the
reverse was read off coordinates or the source's labels, not stated by the source. It
is the largest `needs_review` class in the registry (28 entries, 2026-10-27) and the
one a measurement can actually speak to, because the screen already settles the
question every time it finds an amplicon: `score.py` draws both orientations on the
plus strand and an amplicon only forms when a plus-strand site runs rightwards to a
minus-strand site. If the stored pair were the wrong way round, the two oligos would
face away from each other and no record in the archive would yield a product.

WHAT THIS REPORTS, per flagged entry: how many records produced an amplicon under the
stored orientation (any of detect / reduced / fail -- a `fail` is still a product the
primers would have made, scored badly) against how many produced none. An entry with
hundreds of amplicons has had its orientation confirmed by the archive; an entry with
none has not, and the flag is doing its job.

WHAT IT DOES NOT DO. It does not clear flags. `needs_review` is curated, and the
curator decides whether "the archive yields N products" is the evidence the flag asked
for; this prints the number beside each one. It also cannot distinguish a wrong
orientation from a pair that simply has no target in the archive -- both read as zero
amplicons -- which is why the no-amplicon count is printed too and not folded into a
verdict.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]

PRODUCT = {"detect", "reduced", "fail"}


def flagged_entries(registry: Path, flag: str) -> list[str]:
    out = []
    for path in sorted(registry.glob("*.yaml")):
        doc = yaml.safe_load(path.read_text()) or {}
        for item in doc.get("needs_review") or []:
            if isinstance(item, dict) and item.get("flag") == flag:
                out.append(doc["id"])
                break
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--calls", type=Path, required=True)
    ap.add_argument("--registry", type=Path, default=REPO / "registry")
    ap.add_argument("--flag", default="orientation_inferred")
    ap.add_argument("--min-amplicons", type=int, default=20, help="the bar printed beside each count")
    ap.add_argument("--tsv", type=Path, default=None)
    args = ap.parse_args(argv)

    wanted = set(flagged_entries(args.registry, args.flag))
    if not wanted:
        print(f"no entry carries {args.flag}")
        return 0
    products: Counter[str] = Counter()
    none: Counter[str] = Counter()
    with gzip.open(args.calls, "rt") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            a = r["assay_id"]
            if a not in wanted:
                continue
            if r["call"] in PRODUCT:
                products[a] += 1
            else:
                none[a] += 1

    rows = []
    for a in sorted(wanted):
        p, n = products[a], none[a]
        verdict = (
            "archive yields products"
            if p >= args.min_amplicons
            else "no product in archive"
            if p == 0
            else "few products"
        )
        rows.append({"assay_id": a, "amplicons": p, "no_amplicon": n, "reading": verdict})
    width = max(len(r["assay_id"]) for r in rows)
    print(
        f"{len(rows)} entries carry {args.flag}; bar for 'confirmed by the archive' = {args.min_amplicons} products\n"
    )
    for r in rows:
        print(
            f"  {r['assay_id']:{width}s}  {r['amplicons']:7d} products  {r['no_amplicon']:8d} none   {r['reading']}"
        )
    confirmed = sum(1 for r in rows if r["amplicons"] >= args.min_amplicons)
    zero = sum(1 for r in rows if r["amplicons"] == 0)
    print(
        f"\n{confirmed} of {len(rows)} entries produce >= {args.min_amplicons} amplicons under the stored orientation;"
    )
    print(
        f"{zero} produce none, which is either a wrong orientation or no target in the archive -- this cannot say which."
    )
    print("Nothing was edited. The flag is curated; this is the number a curator can clear it on.")

    if args.tsv:
        args.tsv.parent.mkdir(parents=True, exist_ok=True)
        with args.tsv.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
            w.writeheader()
            w.writerows(rows)
        print(f"wrote {args.tsv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
