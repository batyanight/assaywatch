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
  degeneracy column repeats what `assaywatch degeneracy` says.
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


from assaywatch import registry  # noqa: E402
from assaywatch.collect import stem_order  # noqa: E402
from assaywatch.fasta import read_fasta  # noqa: E402
from assaywatch.match import modal_amplicon  # noqa: E402
from assaywatch.retrieve import group_slug  # noqa: E402
from assaywatch.schema import Assay  # noqa: E402
from assaywatch.score import oligo_pools  # noqa: E402


def archives_for(taxid: int | None, query: str | None) -> tuple[list[Path], str]:
    """EVERY FASTA archive for this assay's own retrieval group, oldest first.

    A taxid can hold several groups - 14 do, and E. coli holds four - because a
    group is a (taxid, query) pair. Picking among them arbitrarily measures an
    assay against records chosen for a different assay's query, which is how the
    first run of this script reported no product at all for the two Wang 1997
    entries that check_submission.py had just amplified happily.

    WHY ALL OF THEM, not the newest. Retrieval is incremental: a day's archive
    holds only what was added or revised since the last run, and the pipeline
    screens every archive ever fetched and reconciles them (see the Snakefile).
    Measuring the newest file alone therefore measures whatever happened to
    arrive last. By 2026-10-14 that had quietly emptied this script: 105 of its
    155 measurements had fallen to a different modal product or to no product at
    all against the 2026-10-05 run - ADENOVIRUS hexon from 4,714 products to
    zero - purely because a small incremental archive had become the newest one.
    Order is `stem_order`'s, the same the pipeline collects in, so `--limit`
    samples the earliest records of a group rather than an arbitrary slice.
    """
    if not taxid:
        return [], ""
    base = ROOT / "data" / "retrieved" / str(taxid)
    # The assay's own group first, then the whole-taxon one, then the assembly
    # sample bacterial targets get, then anything rather than nothing.
    for slug in (group_slug(query), "all", "asm"):
        hits = sorted(glob.glob(str(base / slug / "*.fasta.gz")))
        if hits:
            return [Path(h) for h in sorted(hits, key=lambda x: stem_order(Path(x)))], slug
    hits = sorted(glob.glob(str(base / "*" / "*.fasta.gz")))
    if hits:
        group = Path(hits[0]).parent.name
        same = [Path(h) for h in hits if Path(h).parent.name == group]
        return sorted(same, key=stem_order), group + " (fallback)"
    return [], ""


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


def pairs_of(doc: dict | Assay) -> list[tuple[str, str, str]]:
    """Every (label, forward, reverse) this entry can amplify with, declared pair first.

    WHY EVERY COMBINATION. This script measured `oligos.forward` against
    `oligos.reverse` and nothing else, while the screener builds a POOL from
    `oligos.alternates` (score.oligo_pools) and takes the best product over the
    cross product, so the audit and the screener were measuring different assays.
    An alternate that makes a DIFFERENT PRODUCT is a second assay in one record.
    Sequences come from the schema (`matching_seq`), not from raw YAML: `seq` writes
    inosine as N, which would search a four-fold degenerate base where the screener
    uses a single promiscuous one.
    """
    assay = doc if isinstance(doc, Assay) else Assay.model_validate(doc)
    fwd, rev, _ = oligo_pools(assay)
    out = []
    for i, f in enumerate(fwd):
        for j, r in enumerate(rev):
            label = "declared" if (i, j) == (0, 0) else f"fwd[{i}]xrev[{j}]"
            out.append((label, f, r))
    return out


def measure(paths, fwd: str, rev: str, max_mm: int, max_len: int, limit: int | None):
    """Modal product over every archive of the group: match.modal_amplicon over `_records`.

    `paths` is a list because retrieval is incremental and one day's file is not
    the group (see archives_for). A record seen in two archives is a revision of
    the same accession and is measured once, the latest version winning.
    """
    return modal_amplicon(_records(paths), fwd, rev, max_mm=max_mm, max_len=max_len, limit=limit)


def _records(paths):
    """Every (id, sequence) across the archives, newest archive first.

    Newest first so that `measure`'s deduplication keeps the latest version of a
    revised accession, as `report.key_calls_by_accession` does.
    """
    for path in reversed(list(paths)):
        yield from read_fasta(path)


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
    ap.add_argument(
        "--tolerance",
        type=float,
        default=0.25,
        help="an alternate pair's product this far from the stored size is a SECOND PRODUCT, "
        "not a variant of the declared one (default 0.25, matching amplicon.declared_tolerance)",
    )
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)

    rows = []
    for assay in registry.load(args.registry).values():
        if args.assay and args.assay.lower() not in assay.id.lower():
            continue
        stored = assay.amplicon_bp
        taxid = assay.target.taxid
        archive, group = archives_for(taxid, assay.target.query)
        try:
            combinations = pairs_of(assay)
        except Exception as e:  # noqa: BLE001 - skip the entry, keep auditing the rest
            print(f"  skipped {assay.id}: {e}", file=sys.stderr)
            continue
        if not (combinations and archive):
            continue
        label, fwd, rev = combinations[0]
        n_records, n_products, lengths = measure(archive, fwd, rev, args.max_mm, args.max_len, args.limit)

        # Each alternate combination measured on its own, so a second product is
        # visible instead of being averaged into the declared pair's spread.
        others = []
        for label, f, r in combinations[1:]:
            _, alt_products, alt_lengths = measure(archive, f, r, args.max_mm, args.max_len, args.limit)
            if alt_products >= args.min_records and alt_lengths:
                alt_modal = alt_lengths.most_common(1)[0][0]
                off = abs(alt_modal - stored) / stored if stored else None
                others.append((label, alt_modal, alt_products, off))
        # A combination whose product is outside the window scoring will accept is
        # a different amplicon, not a worse copy of the same one.
        # Not `second`: that name already holds the runner-up LENGTH of the declared pair.
        second_products = [o for o in others if o[3] is not None and o[3] > args.tolerance]

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
                "assay_id": assay.id,
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
                "n_pair_combinations": len(combinations),
                "second_product": ";".join(f"{lab}={bp}bp(n={n})" for lab, bp, n, _ in second_products),
                "verdict": verdict,
            }
        )
        if args.verbose:
            print(
                f"  {verdict:<10} {assay.id[:52]:<52} stored {stored} measured {modal} ({modal_n}/{n_products})"
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
    flagged = [r for r in rows if r["second_product"]]
    if flagged:
        print(f"\n{len(flagged)} entries hold a SECOND PRODUCT in oligos.alternates:")
        print("  (the screener pools alternates with the declared pair, so before")
        print("  amplicon.declared_tolerance these products were credited to the assay;")
        print("  with it on they are rejected and the entry is judged on its declared pair)")
        for r in sorted(flagged, key=lambda r: str(r["assay_id"])):
            print(f"  {str(r['assay_id'])[:52]:<52} declared {r['stored_bp']:>6}  also {r['second_product']}")
        print("  The fix is curation: one entry per round, as the CMV gB and adenovirus")
        print("  polymerase assays already are.")

    print(f"\nwrote {args.out}")
    print("Nothing was written back to registry/: changing a stored amplicon is a curation")
    print("decision, and this measurement is one input to it rather than the verdict.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
