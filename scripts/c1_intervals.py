#!/usr/bin/env python3
"""C1, part one: every per-lineage interval in a lineage report, three ways, one table.

    python scripts/c1_intervals.py results/baseline-2026-10-22/lineage.md
    python scripts/c1_intervals.py results/baseline-2026-10-22/lineage.md --tsv .tmp/c1/intervals.tsv

The first experiment `docs/bayesian-scoring-plan.md` C1 asks for, verbatim: "Recompute
every per-lineage interval in results/baseline-2026-10-22/lineage.md three ways -- Wald
(ships), Wilson (wave 1.1), Beta-Jeffreys -- into one comparison table." The second
half of that experiment, re-running tier-2 under a posterior flag rule, is
`drift.flag_rule: posterior` and `scripts/retrospective.py --config`.

WHAT THE TABLE DECIDES. Whether C1 earns more than Wilson already does on its own.
The plan's own prediction is that it will NOT move the tier-2 matrix much -- most
flagged assays are flagged on large n where Wilson and Beta agree to within a point --
and that the gains, if any, are at the extremes: the lineages a Wald interval flags
with zero width at 0/n or n/n, and the lineages refused a verdict for want of records.
So the summary counts those classes rather than averaging over everything.

The 2026-10-22 lineage report printed Wald intervals; that is what its `95% CI` column
holds and why "[0.00%, 0.00%]" appears on 43 records -- a zero-width 95% interval is not
a finding, which is the whole reason `interval.py` exists. This script reads the
counts, not that column, and recomputes all three from them.
"""

from __future__ import annotations

import argparse
import csv
import math
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from assaywatch.interval import Z95, jeffreys_interval, wilson_interval  # noqa: E402

ROW = re.compile(r"^\|\s*(?P<lineage>[^|]+?)\s*\|\s*(?P<n>\d+)\s*\|\s*(?P<k>\d+)\s*\|")
HEAD = re.compile(r"^## (?P<assay>\S+)")


def wald_interval(k: int, n: int, z: float = Z95) -> tuple[float, float]:
    """The textbook interval the 2026-10-22 report shipped: p +/- z sqrt(p(1-p)/n), clamped.

    Kept here and not in interval.py, because nothing in the pipeline should be able
    to import it by accident; it exists only to be compared against.
    """
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    half = z * math.sqrt(p * (1 - p) / n)
    return (max(0.0, p - half), min(1.0, p + half))


def read_lineages(path: Path) -> list[tuple[str, str, int, int]]:
    """(assay, lineage, evaluable, detected) per table row."""
    out, assay = [], ""
    for line in path.read_text().splitlines():
        if m := HEAD.match(line):
            assay = m.group("assay")
            continue
        if (
            (m := ROW.match(line))
            and not m.group("lineage").startswith("-")
            and m.group("lineage") != "Lineage"
        ):
            out.append((assay, m.group("lineage"), int(m.group("n")), int(m.group("k"))))
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("lineage_md", type=Path)
    ap.add_argument("--threshold", type=float, default=0.90, help="drift.detect_fraction_threshold")
    ap.add_argument("--tsv", type=Path, default=None)
    args = ap.parse_args(argv)

    rows = read_lineages(args.lineage_md)
    if not rows:
        print("no lineage rows found", file=sys.stderr)
        return 1

    t = args.threshold
    out = []
    for assay, lineage, n, k in rows:
        wa, wi, je = wald_interval(k, n), wilson_interval(k, n), jeffreys_interval(k, n)
        out.append(
            {
                "assay": assay,
                "lineage": lineage,
                "evaluable": n,
                "detected": k,
                "share": k / n if n else float("nan"),
                "wald_lo": wa[0],
                "wald_hi": wa[1],
                "wilson_lo": wi[0],
                "wilson_hi": wi[1],
                "jeffreys_lo": je[0],
                "jeffreys_hi": je[1],
                # "below threshold" means the whole interval sits under it, which is
                # the flag condition drift.finalise applies to the pooled share.
                "wald_below": wa[1] < t,
                "wilson_below": wi[1] < t,
                "jeffreys_below": je[1] < t,
                "wald_zero_width": wa[0] == wa[1],
            }
        )

    n_rows = len(out)
    zero = sum(r["wald_zero_width"] for r in out)
    wald_b = sum(r["wald_below"] for r in out)
    wil_b = sum(r["wilson_below"] for r in out)
    jef_b = sum(r["jeffreys_below"] for r in out)
    wald_only = sum(r["wald_below"] and not r["wilson_below"] for r in out)
    wil_jef_disagree = sum(r["wilson_below"] != r["jeffreys_below"] for r in out)
    widths = [
        (r["wilson_hi"] - r["wilson_lo"], r["jeffreys_hi"] - r["jeffreys_lo"])
        for r in out
        if r["evaluable"] >= 100
    ]
    mean_gap = sum(abs(a - b) for a, b in widths) / len(widths) if widths else float("nan")

    print(f"lineage rows: {n_rows} across {len({r['assay'] for r in out})} assays")
    print(f"Wald intervals of zero width (k = 0 or k = n): {zero}")
    print(
        f"below the {t:.0%} threshold by the whole interval:  Wald {wald_b}   Wilson {wil_b}   Jeffreys {jef_b}"
    )
    print(f"  flagged by Wald and not by Wilson: {wald_only}")
    print(f"  Wilson and Jeffreys disagree on:   {wil_jef_disagree}")
    print(f"mean |Wilson width - Jeffreys width| on lineages with >= 100 records: {mean_gap:.4f}")
    print()
    print("The plan's prediction: Wilson and Jeffreys agree to within a point where n is")
    print("large, so if the matrix is the only thing measured C1 will look like it did")
    print("nothing. The rows that differ are the ones to read.")

    if args.tsv:
        args.tsv.parent.mkdir(parents=True, exist_ok=True)
        with args.tsv.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(out[0]), delimiter="\t")
            w.writeheader()
            w.writerows(out)
        print(f"\nwrote {args.tsv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
