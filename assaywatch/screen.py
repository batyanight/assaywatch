"""Screen one or more registry assays against a FASTA and write a TSV of calls.

    python -m assaywatch.screen registry/CHYTRID_Bd_*.yaml records.fasta -o calls.tsv
    python -m assaywatch.screen registry/ records.fasta.gz --config config.yaml

One row per (assay, record). Columns are defined by Call.as_row().
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

from assaywatch.degeneracy import assay_degeneracy
from assaywatch.fasta import read_fasta
from assaywatch.score import load_config, screen_record
from assaywatch.validate import iter_files, load_assay


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("assays", type=Path, help="a registry YAML file or a directory of them")
    ap.add_argument("fasta", type=Path)
    ap.add_argument("-o", "--out", type=Path, default=None, help="TSV path (default: stdout)")
    ap.add_argument("--config", type=Path, default=None)
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    assays = [load_assay(p) for p in iter_files(args.assays)]
    records = list(read_fasta(args.fasta))

    out = args.out.open("w", newline="") if args.out else sys.stdout
    writer = None
    tally: Counter = Counter()
    for assay in assays:
        # Degeneracy is a property of the assay, not of any record, and it is
        # never scored. It rides along on every row so that a reader of the TSV
        # cannot see a `detect` without seeing how much the pool was diluted.
        deg = assay_degeneracy(assay)
        for rid, seq in records:
            call = screen_record(assay, rid, seq, cfg)
            call.extra["degeneracy_fold"] = deg.total_fold
            call.extra["degeneracy_tier"] = deg.tier(cfg)
            row = call.as_row()
            if writer is None:
                writer = csv.DictWriter(out, fieldnames=list(row), delimiter="\t")
                writer.writeheader()
            writer.writerow(row)
            tally[(assay.id, row["call"])] += 1
    if args.out:
        out.close()
        for (aid, call), n in sorted(tally.items()):
            print(f"{aid}\t{call}\t{n}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
