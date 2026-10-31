"""The website's data layer: one run's numbers, extracted once, as plain JSON.

    python -m assaywatch.site extract results/2026-10-31/calls.tsv.gz --out website/data
    python -m assaywatch.site render --data website/data --out website

WHY THIS IS TWO PHASES. Extraction reads a 3.4M-row calls table and runs the drift
and site-drift assessments over it, which costs minutes; rendering is string
formatting and costs seconds. Splitting them means the presentation can be
iterated on without re-reading the table, and -- more importantly -- the rendered
site is a pure function of a committed JSON file, so what the pages claim can be
diffed, tested and regenerated without the archives, which are 9 GB and not
distributed.

WHERE THE NUMBERS COME FROM. `report.build` and `sitedrift.build`, the same two
calls `figures.py` makes, rather than by parsing `report.md`. An earlier prototype
of this site (2026-10-17, `assaywatch-viz`) parsed the rendered markdown with a
regex; that is a second implementation of the same arithmetic and free to
disagree with the first. Everything here is read off the `AssayDrift` and
`AssaySites` objects the report itself renders from.

WHAT IS DELIBERATELY WITHHELD. An assay whose registry entry carries a blocking
`needs_review` flag (`report.held_out_reasons`: `not_screenable`, `do_not_use`
and the rest of `review.OPEN`) gets no status here, exactly as it gets none in
the report. The reasons are shown instead. Printing a status with a caveat beside
it would be the status wearing a disclaimer, and the report decided against that;
a site that did otherwise would be the most-read surface in the project
contradicting the report on the assays most likely to be wrong.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

#: Bumped when a field changes meaning. `render` refuses data it does not know.
SCHEMA = 1


@dataclass
class YearPoint:
    """One deposit year for one assay. `share` is None when nothing was evaluable."""

    year: int
    detected: int
    evaluable: int
    share: float | None
    recent: bool  # inside the recent window this run used


@dataclass
class PositionPoint:
    """One oligo position that at least one record mismatches."""

    oligo: str  # forward | reverse | probe
    pos_3prime: int  # 1 = the terminal base
    base: str  # the oligo base as the screen used it
    n_mismatch: int
    detected_with: int
    evaluable_with: int
    detected_without: int
    evaluable_without: int
    substitutions: list[list[Any]]  # [[oligo_base, record_base, n], ...] commonest first
    in_3prime_zone: bool


@dataclass
class LineagePoint:
    lineage: str
    taxid: int | None
    evaluable: int
    detected: int
    share: float
    ci: list[float]


@dataclass
class AssayPage:
    """Everything one assay's dashboard shows."""

    assay_id: str
    name: str
    status: str  # "" when withheld
    withheld_reasons: list[list[str]]  # [[flag, note], ...]; non-empty means no status
    taxon: str
    taxid: int | None
    gene: str
    chemistry: str
    doi: str
    reference: str
    design_year: int | None
    amplicon_bp: int | None
    entry_status: str  # active | draft | deprecated
    review_flags: list[str]
    scope_taxids: list[int]
    exclusivity_taxids: list[int]
    query: str
    title_requires: list[str]
    oligos: dict[str, str]  # role -> sequence, 5'->3'
    # The verdict's arithmetic, all of it, so a reader can recompute by hand.
    recent_detected: int = 0
    recent_evaluable: int = 0
    recent_ci: list[float] = field(default_factory=lambda: [0.0, 1.0])
    baseline_detected: int = 0
    baseline_evaluable: int = 0
    baseline_ci: list[float] = field(default_factory=lambda: [0.0, 1.0])
    change_ci: list[float] = field(default_factory=lambda: [-1.0, 1.0])
    window_months: int = 0
    recent_from: str = ""
    threshold: float = 0.9
    note: str = ""
    trend: str = ""
    years: list[YearPoint] = field(default_factory=list)
    positions: list[PositionPoint] = field(default_factory=list)
    lineages: list[LineagePoint] = field(default_factory=list)
    # How much of what was screened reached the statistics at all. The site says
    # this per assay because the project's first known limitation is that the
    # denominator is drift-correlated: 65.7% of rows never reach it.
    screened_rows: int = 0
    no_amplicon_rows: int = 0
    exclusions: list[list[Any]] = field(default_factory=list)
    out_of_scope: int = 0


def _pos_in_zone(pos: int, zone: int) -> bool:
    return pos <= zone


def extract(
    calls_path: Path,
    registry_dir: Path,
    retrieved: Path,
    cfg: dict[str, Any],
    run_date: str | None = None,
) -> dict[str, Any]:
    """Everything the site needs from one run, as JSON-ready dicts.

    Runs both assessments, as `figures.build` does and for the same reason: the
    rendered documents are a view of these numbers and parsing them back would be
    a second implementation free to disagree.
    """
    from assaywatch import report as report_mod
    from assaywatch import sitedrift as sitedrift_mod
    from assaywatch.drift import STATUS_ORDER
    from assaywatch.validate import iter_files, load_assay

    run_date = run_date or calls_path.parent.name
    assays = {a.id: a for a in (load_assay(p) for p in iter_files(registry_dir))}

    _, _, drifts = report_mod.build(calls_path, registry_dir, retrieved, cfg, run_date=run_date)
    # Every status, not sitedrift's default three: a stable assay's mismatch map is
    # exactly what tells a reader WHY it is stable, and the site has room the
    # markdown report does not.
    _, _, sites = sitedrift_mod.build(
        calls_path, registry_dir, retrieved, cfg, statuses=STATUS_ORDER, run_date=run_date
    )
    by_site = {s.assay_id: s for s in sites}

    zone = int((cfg.get("scoring") or {}).get("primer_3prime_window", 5))
    pages = [
        _page(assays[aid], d, by_site.get(aid), zone) for aid, d in sorted(drifts.items()) if aid in assays
    ]
    return {
        "schema": SCHEMA,
        "run_date": run_date,
        "threshold": float((cfg.get("drift") or {}).get("detect_fraction_threshold", 0.9)),
        "assays": [asdict(p) for p in pages],
    }


def _page(assay: Any, d: Any, sites: Any, zone: int) -> AssayPage:
    from assaywatch.report import held_out_reasons

    withheld = [[f, n] for f, n in held_out_reasons(assay)]
    recent_year = d.recent_year if d.recent_year is not None else 0
    years = [
        YearPoint(
            year=y,
            detected=ys.detected,
            evaluable=ys.evaluable,
            share=ys.fraction,
            recent=bool(recent_year and y >= recent_year),
        )
        for y, ys in sorted(d.years.items())
    ]
    positions = [
        PositionPoint(
            oligo=p.oligo,
            pos_3prime=p.pos_3prime,
            base=p.base,
            n_mismatch=p.n_mismatch,
            detected_with=p.detected_with,
            evaluable_with=p.evaluable_with,
            detected_without=p.detected_without,
            evaluable_without=p.evaluable_without,
            substitutions=[list(s) for s in p.substitutions],
            in_3prime_zone=_pos_in_zone(p.pos_3prime, zone),
        )
        for p in (sites.positions if sites else [])
    ]
    lineages = [
        LineagePoint(
            lineage=ls.lineage_name,
            taxid=ls.taxid,
            evaluable=ls.n_evaluable,
            detected=ls.n_detected,
            share=ls.share,
            ci=[ls.ci_lower, ls.ci_upper],
        )
        for ls in (d.lineage_stats or [])
    ]
    oligos = {}
    for role in ("forward", "reverse", "probe"):
        o = getattr(assay.oligos, role, None)
        if o is not None:
            oligos[role] = o.seq

    return AssayPage(
        assay_id=assay.id,
        name=assay.name,
        status="" if withheld else d.status,
        withheld_reasons=withheld,
        taxon=assay.target.taxon_name or "",
        taxid=assay.target.taxid,
        gene=assay.target.gene or "",
        chemistry=assay.chemistry.value,
        doi=assay.citation.doi or "",
        reference=assay.citation.reference or "",
        design_year=assay.citation.design_year,
        amplicon_bp=assay.amplicon_bp,
        entry_status=assay.status.value,
        review_flags=[r.flag.value for r in (assay.needs_review or [])],
        scope_taxids=list(assay.target.scope_taxids or []),
        exclusivity_taxids=list(assay.target.exclusivity_taxids or []),
        query=assay.target.query or "",
        title_requires=list(assay.target.title_requires or []),
        oligos=oligos,
        recent_detected=d.recent_detected,
        recent_evaluable=d.recent_evaluable,
        recent_ci=list(d.recent_ci),
        baseline_detected=d.baseline_detected,
        baseline_evaluable=d.baseline_evaluable,
        baseline_ci=list(d.baseline_ci),
        change_ci=list(d.change_ci),
        window_months=d.window_months,
        recent_from=str(d.recent_from),
        threshold=d.threshold,
        note=d.note,
        trend=_trend_text(d),
        years=years,
        positions=positions,
        lineages=lineages,
        screened_rows=d.screened_rows,
        no_amplicon_rows=d.no_amplicon_rows,
        exclusions=[[k, v] for k, v in sorted(d.exclusions.items(), key=lambda kv: -kv[1])],
        out_of_scope=d.out_of_scope,
    )


def _p(p: float) -> str:
    """A p-value that never prints as `p=0`, which is a rounding artefact and not
    a result: the test underflows long before the probability is zero."""
    return "p < 1e-300" if p <= 0 else f"p = {p:.3g}"


def _trend_text(d: Any) -> str:
    """The Cochran-Armitage trend as one phrase, or "" when there is none.

    Both trends are reported where they exist, and the site says so when they
    disagree, because by-record is an upper bound on the evidence and
    by-footprint is nearer a lower bound (`drift.AssayDrift.trend_by_footprint`).
    """
    t, f = d.trend, d.trend_by_footprint
    if t is None and f is None:
        return ""
    bits = []
    if t is not None:
        bits.append(f"by record {t.direction} ({_p(t.p)}, {t.n_years} years)")
    if f is not None:
        bits.append(f"by footprint {f.direction} ({_p(f.p)})")
    if t is not None and f is not None and t.direction != f.direction:
        bits.append("**the two disagree on direction**")
    return "; ".join(bits)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("extract", help="read one run into website/data/run.json")
    e.add_argument("calls", type=Path)
    e.add_argument("--registry", type=Path, default=ROOT / "registry")
    e.add_argument("--retrieved", type=Path, default=ROOT / "data" / "retrieved")
    e.add_argument("--config", type=Path, default=None)
    e.add_argument("--run-date", default=None)
    e.add_argument("--out", type=Path, required=True)
    args = ap.parse_args(argv)

    from assaywatch.score import load_config

    cfg = load_config(args.config)
    data = extract(args.calls, args.registry, args.retrieved, cfg, run_date=args.run_date)
    args.out.mkdir(parents=True, exist_ok=True)
    path = args.out / "run.json"
    path.write_text(json.dumps(data, indent=1, sort_keys=False) + "\n")
    n = len(data["assays"])
    withheld = sum(1 for a in data["assays"] if a["withheld_reasons"])
    print(f"{path}: {n} assays from {data['run_date']}, {withheld} with a status withheld", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
