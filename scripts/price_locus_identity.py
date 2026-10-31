#!/usr/bin/env python3
"""What would `scoring.locus_identity_min` cost, per assay, without rescreening.

    python scripts/price_locus_identity.py --run results/2026-10-25 [--threshold 0.5]

The test lives at screen time, so pricing it the usual way - render the report
twice - is not available: it would take two full rescreens. This applies the same
module offline to the run's own calls and archives, which gives the per-assay
effect for the cost of one pass over the FASTA files.

Reads `results/<run>/calls.tsv.gz`, never a glob over `results/screened/`; see
docs/journal/2026-10-25-stale-orphan-screens.md for what that mistake cost.
"""

from __future__ import annotations

import argparse
import collections
import csv
import glob
import gzip
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from assaywatch.accession import strip_version  # noqa: E402
from assaywatch.locus_identity import best_identity  # noqa: E402

CAP = 80  # fail rows sampled per assay; sequence loading is the cost, not the maths


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", type=Path, default=ROOT / "results" / "2026-10-25")
    ap.add_argument("--refs", type=Path, default=ROOT / "docs" / "locus-references.json")
    ap.add_argument("--threshold", type=float, default=0.50)
    args = ap.parse_args(argv)

    refs = json.loads(args.refs.read_text())
    fails: dict[str, list[dict]] = collections.defaultdict(list)
    ev: collections.Counter = collections.Counter()
    det: collections.Counter = collections.Counter()
    with gzip.open(args.run / "calls.tsv.gz", "rt") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            c = r["call"]
            if c not in ("detect", "reduced", "fail"):
                continue
            ev[r["assay_id"]] += 1
            if c != "fail":
                det[r["assay_id"]] += 1
            elif len(fails[r["assay_id"]]) < CAP:
                fails[r["assay_id"]].append(r)

    wanted = {strip_version(r["record_id"]) for rows in fails.values() for r in rows}
    seqs: dict[str, str] = {}
    for fp in sorted(glob.glob(str(ROOT / "data" / "retrieved" / "*" / "*" / "*.fasta.gz"))):
        if not wanted - seqs.keys():
            break
        try:
            fh2 = gzip.open(fp, "rt")
        except OSError:
            continue
        with fh2:
            acc = None
            buf: list[str] = []
            for line in fh2:
                if line.startswith(">"):
                    if acc in wanted and acc not in seqs:
                        seqs[acc] = "".join(buf)
                    acc = strip_version(line[1:].split()[0])
                    buf = []
                else:
                    buf.append(line.strip())
            if acc in wanted and acc not in seqs:
                seqs[acc] = "".join(buf)

    print(
        f"threshold {args.threshold}; {len(refs)} assays have references; sampling <= {CAP} fail rows each\n"
    )
    print(f"{'assay':54s} {'samp':>5} {'rej':>4} {'keep':>5} {'unjud':>6}  rej%  id range")
    tot = collections.Counter()
    for assay in sorted(fails):
        R = refs.get(assay, {}).get("interiors", [])
        rej = keep = unj = 0
        scores = []
        for r in fails[assay]:
            s = seqs.get(strip_version(r["record_id"]))
            if not s:
                continue
            try:
                lo, hi = int(r["amplicon_start"]), int(r["amplicon_end"])
            except (KeyError, TypeError, ValueError):
                continue
            if lo > hi:
                lo, hi = hi, lo
            sc = best_identity(s[max(0, lo) : hi], R)
            if sc is None:
                unj += 1
            else:
                scores.append(sc)
                if sc >= args.threshold:
                    keep += 1
                else:
                    rej += 1
        n = rej + keep + unj
        if not n:
            continue
        tot["rej"] += rej
        tot["keep"] += keep
        tot["unjud"] += unj
        if rej:
            rng = f"{min(scores):.2f}-{max(scores):.2f}" if scores else "-"
            print(f"{assay[:54]:54s} {n:5d} {rej:4d} {keep:5d} {unj:6d}  {100 * rej / n:4.0f}  {rng}")
    print(f"\nsampled rows: rejected {tot['rej']}, kept {tot['keep']}, unjudgeable {tot['unjud']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
