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

`expect` is `works` (the literature found it detecting its target), `fails`
(false negatives or a redesign were reported) or `partial` (it covers some of
the diversity and not the rest). Statuses map on as: stable/watch -> works,
declining -> fails, low coverage -> partial, and insufficient data / no recent
data -> undecided, counted separately because an assay the tool declines to
judge is not the same as one it judges correctly — that distinction is what
calibrates min_records_for_drift.

A `partial` result against a `works` expectation is reported as `weaker`, not
as a disagreement: a pan-family assay detecting 71% of a genus is consistent
with a paper that used it successfully on the isolates it had.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch.drift import assess  # noqa: E402
from assaywatch.lineage import load_taxa_cache  # noqa: E402
from assaywatch.report import key_calls_by_accession, read_calls, read_dates  # noqa: E402
from assaywatch.score import load_config  # noqa: E402

# `low coverage` is its own outcome, not a failure: it says the assay is below
# threshold with no measurable fall, i.e. it never covered all of this diversity.
# That is compatible with a paper reporting successful use on the samples it had,
# so scoring it as "fails" turned four honest `works` cases into disagreements.
WORKS = {"stable", "watch"}
FAILS = {"declining"}
PARTIAL = {"low coverage"}
# Statuses the tool declines to judge. Anything not named above is undecided too, so a new
# status added to drift.py reads as "declined" until someone decides what it means, rather
# than being scored as one of the three outcomes by accident.
UNDECIDED = {"insufficient data", "no recent data", "no data"}


def classify(status: str, expect: str) -> tuple[str, str]:
    """(what the tool said, how that compares with the paper) for one case.

    `got` is `works`, `fails`, `partial` or `undecided`. The verdict is `undecided` when the
    tool declined to judge (that is not a disagreement, and counting it separately is what
    calibrates `min_records_for_drift`), `agrees` when it matches, `weaker` for a `works` /
    `partial` mismatch in EITHER direction (incomplete coverage is not a contradiction), and
    `DISAGREES` otherwise.
    """
    got = (
        "works"
        if status in WORKS
        else "fails"
        if status in FAILS
        else "partial"
        if status in PARTIAL
        else "undecided"
    )
    if got == "undecided":
        return got, "undecided"
    if got == expect:
        return got, "agrees"
    if {got, expect} == {"works", "partial"}:
        return got, "weaker"
    return got, "DISAGREES"


@dataclass
class Evidence:
    """Everything a retrospective verdict reads, loaded once.

    The calls table is millions of rows and the metadata is every
    `*.meta.tsv.gz` under data/retrieved, and neither depends on the case being
    asked about. `--cases` used to reload and re-deduplicate both for each of the
    46 validation cases, so the dominant cost of a calibration run was parsing
    the same files 46 times. Held here instead, with the calls already
    deduplicated to the newest version of each accession and grouped by assay,
    so a case touches only its own assay's rows.
    """

    dates: dict[str, str]
    by_assay: dict[str, list[dict[str, Any]]]
    taxids: dict[str, int] | None = None
    taxa_cache: dict[int, str] | None = None


def load_evidence(calls_path: Path, retrieved: Path, cfg: dict | None = None) -> Evidence:
    """Read and deduplicate the calls table and the deposit dates, once.

    Deduplication is keyed on (assay, accession), so doing it before grouping by
    assay gives the same rows a per-assay pass would.

    When lineage config is present, also loads the taxid backfill sidecar and
    the taxa cache so per-lineage analysis runs during retrospective verdicts.
    """
    by_assay: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in key_calls_by_accession(read_calls(calls_path)):
        by_assay[r["assay_id"]].append(r)

    taxids: dict[str, int] | None = None
    taxa_cache: dict[int, str] | None = None
    if cfg:
        lcfg = cfg.get("lineage", {})
        taxa_cache_path = lcfg.get("taxa_cache")
        if taxa_cache_path:
            taxa_cache = load_taxa_cache(taxa_cache_path)
            taxids = {}
            sidecar_path = retrieved / ".meta.taxid.backfill.tsv.gz"
            if sidecar_path.exists():
                with gzip.open(sidecar_path, "rt") as f:
                    next(f, None)  # skip header
                    for line in f:
                        acc, _, tx = line.rstrip("\n").partition("\t")
                        if tx.isdigit():
                            taxids[acc.split(".")[0]] = int(tx)
            # Also read taxids from archive metadata (new-style with taxid column)
            for meta_path in sorted(retrieved.rglob("*.meta.tsv.gz")):
                with gzip.open(meta_path, "rt") as f:
                    hdr = (f.readline() or "").rstrip("\n").split("\t")
                    if "taxid" not in hdr or "accession" not in hdr:
                        continue
                    ai, ti = hdr.index("accession"), hdr.index("taxid")
                    for line in f:
                        parts = line.rstrip("\n").split("\t")
                        if len(parts) > max(ai, ti) and parts[ti].isdigit():
                            taxids[parts[ai].split(".")[0]] = int(parts[ti])
            if not taxids:
                taxids = None

    return Evidence(read_dates(retrieved), dict(by_assay), taxids, taxa_cache)


def status_from_evidence(
    evidence: Evidence,
    cfg: dict,
    as_of: date,
    assays: set[str] | None = None,
    scope_map: dict[str, set[int]] | None = None,
):
    """{assay_id: AssayDrift} as the report would have computed it on `as_of`."""
    cutoff = as_of.isoformat()
    wanted = (
        evidence.by_assay
        if assays is None
        else {a: evidence.by_assay[a] for a in assays if a in evidence.by_assay}
    )
    rows = [r for rs in wanted.values() for r in rs if evidence.dates.get(r["record_id"], "9999") < cutoff]
    return assess(
        rows,
        evidence.dates,
        cfg,
        today=as_of,
        taxids=evidence.taxids,
        taxa_cache=evidence.taxa_cache,
        scope_map=scope_map,
    ), len(rows)


def status_as_of(
    calls_path: Path,
    retrieved: Path,
    cfg: dict,
    as_of: date,
    assays: set[str] | None = None,
    scope_map: dict[str, set[int]] | None = None,
):
    """{assay_id: AssayDrift} as the report would have computed it on `as_of`.

    Loads the evidence each call, so it is right for one question. Anything
    asking several should call `load_evidence` once and `status_from_evidence`
    per question, which is what `--cases` does.
    """
    return status_from_evidence(load_evidence(calls_path, retrieved, cfg), cfg, as_of, assays, scope_map)


def _build_scope_map(registry: Path) -> dict[str, set[int]] | None:
    """Build assay_id → set of in-scope taxids from registry YAMLs, same as report.py."""
    from assaywatch.validate import iter_files, load_assay

    scope_map: dict[str, set[int]] | None = None
    for path in iter_files(registry):
        a = load_assay(path)
        if a.target.scope_taxids:
            if scope_map is None:
                scope_map = {}
            scope_map[a.id] = set(a.target.scope_taxids)
    return scope_map


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--calls", type=Path, default=None, help="calls.tsv.gz (default: the newest run)")
    ap.add_argument("--retrieved", type=Path, default=ROOT / "data" / "retrieved")
    ap.add_argument("--registry", type=Path, default=ROOT / "registry", help="registry dir for scope_taxids")
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
    scope_map = _build_scope_map(args.registry) if args.registry.is_dir() else None

    if not args.cases:
        if not args.as_of:
            ap.error("give --as-of, or --cases")
        drifts, n = status_as_of(
            calls, args.retrieved, cfg, args.as_of, set(args.assay) if args.assay else None,
            scope_map=scope_map,
        )  # one question, so one load
        print(f"{calls}, as of {args.as_of} ({n} records deposited before then)\n")
        for aid, a in sorted(drifts.items()):
            frac = "-" if a.recent_fraction is None else f"{a.recent_fraction:.1%}"
            print(f"{a.status:<18} {frac:>7} of {a.recent_evaluable:<6} recent  {aid}")
            print(f"{'':18} {a.note}")
        return 0

    # Comment lines carry each case's provenance; strip them before the header is read.
    body = [ln for ln in args.cases.read_text().splitlines() if ln.strip() and not ln.startswith("#")]
    cases = list(csv.DictReader(body, delimiter="\t"))
    evidence = load_evidence(calls, args.retrieved, cfg)  # once, not once per case
    tally: Counter = Counter()
    print(f"{'assay':<52} {'as of':<11} {'expect':<7} {'status':<18} verdict")
    for c in cases:
        as_of = date.fromisoformat(c["as_of"])
        drifts, _ = status_from_evidence(evidence, cfg, as_of, {c["assay_id"]}, scope_map=scope_map)
        a = drifts.get(c["assay_id"])
        status = a.status if a else "no data"
        _, verdict = classify(status, c["expect"])
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
