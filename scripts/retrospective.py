#!/usr/bin/env python3
"""What would AssayWatch have said on a past date? Tier-2 validation's measuring stick.

    python scripts/retrospective.py --as-of 2014-01-01 --assay CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004
    python scripts/retrospective.py --cases docs/validation-cases.tsv

Every threshold in config.yaml was set by eye, so the statuses mean "worth
looking at" rather than anything measured. The way to calibrate them is to ask
whether the tool agrees with assays whose real-world performance the literature
later reported — using only the sequence records that existed before that
report, so the tool is not told the answer.

An "as of" run is the ordinary report pipeline with two restrictions: records
deposited on or after the cutoff are dropped, and the recent window is measured
backwards from the cutoff instead of from today. Nothing else changes, so a
retrospective verdict is directly comparable with a current one.

With --cases it reads a TSV of expected verdicts and prints a confusion matrix:

    assay_id  as_of  expect  source
    CHYTRID_..._Boyle_2004  2014-01-01  works  10.xxxx/yyy (Table 2)

`expect` is one of `works` (the literature found it detecting its target) or
`fails` (the literature reported false negatives or a redesign). Those map onto
statuses: stable/watch/insufficient data/no recent data count as "works",
declining/low coverage as "fails". `insufficient data` is reported separately
too, because an assay the tool cannot judge is not the same as one it judges
correctly, and that distinction is what sets min_records_for_drift.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch.drift import assess  # noqa: E402
from assaywatch.report import key_calls_by_accession, read_calls, read_dates  # noqa: E402
from assaywatch.score import load_config  # noqa: E402

WORKS = {"stable", "watch", "insufficient data", "no recent data"}
FAILS = {"declining", "low coverage"}


def status_as_of(calls_path: Path, retrieved: Path, cfg: dict, as_of: date, assays: set[str] | None = None):
    """{assay_id: AssayDrift} as the report would have computed it on `as_of`."""
    dates = read_dates(retrieved)
    cutoff = as_of.isoformat()
    rows = [
        r
        for r in key_calls_by_accession(read_calls(calls_path))
        if (assays is None or r["assay_id"] in assays) and (dates.get(r["record_id"], "9999") < cutoff)
    ]
    return assess(rows, dates, cfg, today=as_of), len(rows)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--calls", type=Path, default=None, help="calls.tsv.gz (default: the newest run)")
    ap.add_argument("--retrieved", type=Path, default=ROOT / "data" / "retrieved")
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--as-of", type=date.fromisoformat, default=None)
    ap.add_argument("--assay", action="append", help="limit to these assay ids; repeatable")
    ap.add_argument("--cases", type=Path, default=None, help="TSV of expected verdicts")
    args = ap.parse_args(argv)

    calls = args.calls
    if calls is None:
        runs = sorted(p for p in (ROOT / "results").glob("*/calls.tsv.gz"))
        if not runs:
            raise SystemExit("no calls.tsv.gz under results/; run the pipeline first")
        calls = runs[-1]
    cfg = load_config(args.config)

    if not args.cases:
        if not args.as_of:
            ap.error("give --as-of, or --cases")
        drifts, n = status_as_of(
            calls, args.retrieved, cfg, args.as_of, set(args.assay) if args.assay else None
        )
        print(f"{calls}, as of {args.as_of} ({n} records deposited before then)\n")
        for aid, a in sorted(drifts.items()):
            frac = "-" if a.recent_fraction is None else f"{a.recent_fraction:.1%}"
            print(f"{a.status:<18} {frac:>7} of {a.recent_evaluable:<6} recent  {aid}")
            print(f"{'':18} {a.note}")
        return 0

    # Comment lines carry each case's provenance; strip them before the header is read.
    body = [ln for ln in args.cases.read_text().splitlines() if ln.strip() and not ln.startswith("#")]
    cases = list(csv.DictReader(body, delimiter="\t"))
    tally: Counter = Counter()
    print(f"{'assay':<52} {'as of':<11} {'expect':<7} {'status':<18} verdict")
    for c in cases:
        as_of = date.fromisoformat(c["as_of"])
        drifts, _ = status_as_of(calls, args.retrieved, cfg, as_of, {c["assay_id"]})
        a = drifts.get(c["assay_id"])
        status = a.status if a else "no data"
        got = "works" if status in WORKS else "fails" if status in FAILS else "?"
        if status == "insufficient data":
            verdict = "undecided"  # the tool declined to judge
        elif got == c["expect"]:
            verdict = "agrees"
        else:
            verdict = "DISAGREES"
        tally[(c["expect"], verdict)] += 1
        print(f"{c['assay_id'][:52]:<52} {c['as_of']:<11} {c['expect']:<7} {status:<18} {verdict}")
    print("\nsummary:", ", ".join(f"{e}/{v}: {n}" for (e, v), n in sorted(tally.items())))
    undecided = sum(n for (_, v), n in tally.items() if v == "undecided")
    if undecided:
        print(f"{undecided} case(s) the tool declined to judge (insufficient data): that is what calibrating")
        print("min_records_for_drift against recent_window_months is for.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
