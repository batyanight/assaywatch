#!/usr/bin/env python3
"""How much sequence has arrived since each assay was designed.

    python scripts/design_era.py                       # the table
    python scripts/design_era.py --out docs/design-era.tsv

THE PREMISE, MEASURED. README's first paragraph is the argument the whole project
rests on: "Assays are designed against the handful of sequences available at
publication and then run for years while the database accumulates divergent
strains nobody re-screens them against." Nothing measured it. The registry has a
field for the authors' own number, `citation.n_sequences_at_design`, and it is
filled for 20 of 208 entries and read by no code.

This computes the measurable cousin: how many records for the assay's retrieval
taxon were already deposited in the design year, against how many exist now. Bd
(Boyle 2004) was designed when its taxon held 42 records and now faces 9,496, a
226-fold increase; West Nile (Lanciotti 2001) 83 against 9,151.

WHAT THIS IS NOT. It is NOT `n_sequences_at_design`, and the two must not be
conflated:

  * `n_sequences_at_design` is how many sequences THE AUTHORS aligned, which only
    their paper can say. It is the right field for "how thin was the design", and
    backfilling it means reading 188 papers.
  * this is how many records EXISTED for the target taxon at that time, which is
    the exposure the assay has since been subjected to. An author who aligned 8
    sequences out of 42 available is in a different position from one who aligned
    8 out of 8.

So this fills no registry field. It is a reported measurement, like degeneracy and
the thermodynamic columns, and for the same reason: it is a property of the
assay's situation rather than of any record.

THREE HONEST LIMITS.

  * The denominator is the archive, not GenBank. Each archive is what the group's
    query returned, so a gene-targeted group counts records matching that query
    and not the whole taxon. That is the right denominator for this assay, and it
    is not the number a GenBank search would print today.
  * Deposit date, not collection date. `assemblies.py:37-39` states the problem:
    an NCTC strain collected in 1952 and sequenced in 2018 is a 2018 deposit.
  * Records deposited before the design year are not necessarily records the
    authors could find, and nothing here claims they were.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch.score import load_config  # noqa: E402
from assaywatch.validate import iter_files, load_assay  # noqa: E402


def deposits_by_taxon(retrieved: Path) -> dict[int, list[int]]:
    """{taxid: [deposit year, ...]} over unique accessions in that taxon's archives."""
    out: dict[int, list[int]] = defaultdict(list)
    # `seen` is PER TAXON, not per file. Archives are stored per group and a record
    # belongs to every group whose query matches it, which README documents as
    # cross-group duplication -- taxid 77643's two query groups share 822
    # whole-genome accessions. Deduplicating per file counted those twice and
    # inflated the very denominator this script reports.
    seen_by_taxid: dict[int, set[str]] = defaultdict(set)
    for meta in sorted(retrieved.glob("*/*/*.meta.tsv.gz")):
        try:
            taxid = int(meta.parts[-3])
        except ValueError:
            continue
        seen = seen_by_taxid[taxid]
        with gzip.open(meta, "rt") as fh:
            header = fh.readline().rstrip("\n").split("\t")
            if "accession" not in header or "created" not in header:
                continue
            ai, ci = header.index("accession"), header.index("created")
            for line in fh:
                parts = line.rstrip("\n").split("\t")
                if len(parts) <= max(ai, ci):
                    continue
                acc, year = parts[ai], parts[ci][:4]
                if acc in seen or not year.isdigit():
                    continue
                seen.add(acc)
                out[taxid].append(int(year))
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--retrieved", type=Path, default=None)
    ap.add_argument("--out", type=Path, default=None, help="write the table as TSV")
    args = ap.parse_args(argv)

    cfg = load_config()
    retrieved = args.retrieved or ROOT / cfg["retrieved_dir"]
    years = deposits_by_taxon(retrieved)

    rows = []
    for assay in sorted((load_assay(p) for p in iter_files(args.registry)), key=lambda a: a.id):
        taxid, design = assay.target.taxid, assay.citation.design_year
        if taxid is None or design is None or taxid not in years:
            continue
        at_design = sum(1 for y in years[taxid] if y < design)
        now = len(years[taxid])
        rows.append(
            {
                "assay_id": assay.id,
                "taxid": taxid,
                "design_year": design,
                "records_before_design": at_design,
                "records_now": now,
                "fold_increase": (f"{now / at_design:.0f}" if at_design else ""),
                "authors_n_sequences": assay.citation.n_sequences_at_design or "",
            }
        )

    rows.sort(key=lambda r: -(float(r["fold_increase"]) if r["fold_increase"] else 0))
    print(f"{len(rows)} assays with a design year and an archived taxon\n")
    print(f"{'assay':50s} {'design':>6} {'then':>7} {'now':>8} {'x':>6}")
    for r in rows[:20]:
        print(
            f"{r['assay_id'][:50]:50s} {r['design_year']:>6} {r['records_before_design']:>7} "
            f"{r['records_now']:>8} {r['fold_increase']:>6}"
        )
    thin = [r for r in rows if r["records_before_design"] < 50]
    print(f"\n{len(thin)} were designed when their taxon held fewer than 50 archived records")
    both = [r for r in rows if r["authors_n_sequences"] != ""]
    if both:
        print(f"{len(both)} also record the authors' own count, which is a different quantity:")
        for r in both[:8]:
            print(
                f"  {r['assay_id'][:46]:48s} authors aligned {r['authors_n_sequences']}, "
                f"{r['records_before_design']} existed"
            )

    if args.out:
        with args.out.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
            w.writeheader()
            w.writerows(rows)
        print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
