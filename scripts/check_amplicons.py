#!/usr/bin/env python
"""Measure every assay's amplicon against real records and compare with what it stores.

    python scripts/check_amplicons.py --out results/amplicon-audit.tsv
    python scripts/check_amplicons.py --assay WEST_NILE --verbose

Why
---
`amplicon_bp` looks like a harmless annotation and is not. It is the only thing
that says how far apart the two primers should land, and `score.py` is ready to
use it to reject a product of the wrong length once
`config.yaml: amplicon.declared_tolerance` is turned on. A wrong value there
will then throw away real amplifications, or keep spurious ones.

Most of these numbers were transcribed from a spreadsheet or quoted from a
paper's abstract, and spot checks on 2026-10-05 found more wrong than right:
adenovirus inner 281 against a measured 258, adenovirus outer 1560 against 1512,
the two pan-adenovirus rounds 550 and 330 against 556 and 324, enterovirus 992
against 760, CMV 4125 550 against 599, West Nile 161 against 162, AAV 316
against 255. A paper's stated size is a claim; this script measures it.

Method
------
For each entry with a `target.taxid` that has a local archive under
`data/retrieved/<taxid>/`, find every site for the forward and reverse primer
with up to `--max-mm` mismatches, pair them on opposite strands in the right
orientation, take the pair with the fewest total mismatches per record, and
report the modal product length.

Caveats the output carries, rather than hiding:

* **A mode is not the whole story.** Several assays are genuinely bimodal - both
  pan-adenovirus rounds split almost evenly three bases apart, which is an indel
  between adenovirus species. `second_bp` and `spread` are reported so a reader
  can see that.
* **Heavily degenerate primers match loosely.** A 16,384-fold pool will find a
  site somewhere in most records, and the resulting "product" can be spurious.
  `--min-records` and the reported `n_products` are there to judge this; the
  degeneracy column repeats what `python -m assaywatch.degeneracy` says.
* **Partial deposits cannot give a product** even when the primers are perfect,
  so a low `n_products` against a large `n_records` is usually the archive's
  composition rather than the assay's failure.

Nothing is written back to `registry/`. Changing a stored amplicon is a curation
decision that belongs in an entry's `notes_curator` alongside the evidence, and
the measurement is one input to it, not the verdict.
"""

from __future__ import annotations

import argparse
import collections
import glob
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import yaml  # noqa: E402

from assaywatch.fasta import read_fasta  # noqa: E402
from assaywatch.match import find_sites  # noqa: E402


def archive_for(taxid: int | None) -> Path | None:
    """Newest FASTA archive for this taxid, over any retrieval group."""
    if not taxid:
        return None
    hits = sorted(glob.glob(str(ROOT / "data" / "retrieved" / str(taxid) / "*" / "*.fasta.gz")))
    return Path(hits[-1]) if hits else None


def pool_size(seq: str) -> int:
    """How many distinct oligos this degenerate sequence stands for."""
    sizes = {
        "A": 1,
        "C": 1,
        "G": 1,
        "T": 1,
        "U": 1,
        "R": 2,
        "Y": 2,
        "S": 2,
        "W": 2,
        "K": 2,
        "M": 2,
        "B": 3,
        "D": 3,
        "H": 3,
        "V": 3,
        "N": 4,
    }
    n = 1
    for base in seq.upper():
        n *= sizes.get(base, 1)
        if n > 10**9:
            return n
    return n


def measure(path: Path, fwd: str, rev: str, max_mm: int, max_len: int, limit: int | None):
    lengths: collections.Counter = collections.Counter()
    n_records = n_products = 0
    for i, (_rid, seq) in enumerate(read_fasta(path)):
        if limit and i >= limit:
            break
        n_records += 1
        seq = seq.upper()
        f_sites = find_sites(fwd, seq, max_mm)
        if not f_sites:
            continue
        r_sites = find_sites(rev, seq, max_mm)
        if not r_sites:
            continue
        best = None
        for f in f_sites:
            for r in r_sites:
                if f.strand == r.strand:
                    continue
                # The forward primer must sit upstream of the reverse one.
                if f.strand == "+" and not f.start < r.start:
                    continue
                if f.strand == "-" and not r.start < f.start:
                    continue
                length = max(f.end, r.end) - min(f.start, r.start)
                if not 20 <= length <= max_len:
                    continue
                key = (f.n_mismatches + r.n_mismatches, length)
                if best is None or key < best:
                    best = key
        if best:
            n_products += 1
            lengths[best[1]] += 1
    return n_records, n_products, lengths


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--out", type=Path, default=ROOT / "results" / "amplicon-audit.tsv")
    ap.add_argument("--assay", help="only entries whose id contains this")
    ap.add_argument("--max-mm", type=int, default=3)
    ap.add_argument("--max-len", type=int, default=4000)
    ap.add_argument("--limit", type=int, help="screen at most this many records per archive")
    ap.add_argument(
        "--min-records", type=int, default=5, help="below this many products, report but do not judge"
    )
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)

    rows = []
    paths = sorted(args.registry.glob("*.yaml"))
    for path in paths:
        doc = yaml.safe_load(path.read_text()) or {}
        if args.assay and args.assay.lower() not in doc.get("id", "").lower():
            continue
        oligos = doc.get("oligos") or {}
        fwd, rev = (oligos.get("forward") or {}).get("seq"), (oligos.get("reverse") or {}).get("seq")
        stored = doc.get("amplicon_bp")
        taxid = (doc.get("target") or {}).get("taxid")
        archive = archive_for(taxid)
        if not (fwd and rev and archive):
            continue
        n_records, n_products, lengths = measure(archive, fwd, rev, args.max_mm, args.max_len, args.limit)
        top = lengths.most_common(3)
        modal, modal_n = top[0] if top else (0, 0)
        second, second_n = top[1] if len(top) > 1 else (0, 0)
        if not n_products:
            verdict = "no-product"
        elif n_products < args.min_records:
            verdict = "too-few"
        elif stored is None:
            verdict = "unset"
        elif stored == modal:
            verdict = "agrees"
        elif abs(stored - modal) <= 3:
            verdict = "within-3"
        else:
            verdict = "DISAGREES"
        rows.append(
            {
                "assay_id": doc.get("id", path.stem),
                "taxid": taxid,
                "stored_bp": stored or "",
                "measured_bp": modal or "",
                "measured_n": modal_n,
                "second_bp": second or "",
                "second_n": second_n,
                "n_products": n_products,
                "n_records": n_records,
                "spread": ";".join(f"{bp}x{c}" for bp, c in top),
                "pool": pool_size(fwd) * pool_size(rev),
                "verdict": verdict,
            }
        )
        if args.verbose:
            print(
                f"  {verdict:<10} {doc.get('id', '')[:52]:<52} stored {stored} measured {modal} ({modal_n}/{n_products})"
            )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    cols = list(rows[0].keys()) if rows else []
    with args.out.open("w") as fh:
        fh.write("\t".join(cols) + "\n")
        for r in rows:
            fh.write("\t".join(str(r[c]) for c in cols) + "\n")

    counts = collections.Counter(r["verdict"] for r in rows)
    print(f"\n{len(rows)} assays measured against a local archive")
    for verdict in ("agrees", "within-3", "DISAGREES", "unset", "too-few", "no-product"):
        if counts.get(verdict):
            print(f"  {counts[verdict]:>4}  {verdict}")
    bad = [r for r in rows if r["verdict"] == "DISAGREES"]
    if bad:
        print("\nStored and measured disagree by more than 3 bp:")
        for r in sorted(bad, key=lambda r: -abs((r["stored_bp"] or 0) - (r["measured_bp"] or 0)))[:25]:
            print(
                f"  {r['assay_id'][:56]:<56} stored {r['stored_bp']:>6}  measured {r['measured_bp']:>6}"
                f"  ({r['measured_n']}/{r['n_products']} products)  pool {r['pool']}"
            )
    print(f"\nwrote {args.out}")
    print("Nothing was written back to registry/: changing a stored amplicon is a curation")
    print("decision, and this measurement is one input to it rather than the verdict.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
