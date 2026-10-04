"""Render the per-assay drift report.

    python -m assaywatch.report results/2026-10-03/calls.tsv.gz \
        --registry registry --retrieved data/retrieved --out results/2026-10-03

Writes `report.md` (reads on GitHub without anything being built) and
`report.html` (self-contained, no CDN, suitable for GitHub Pages). The HTML
charts are inline SVG rather than a plotting library: the whole point of the
report is that a vet lab with no bioinformatician can open one file and read
it, and a page that fetches a megabyte of JavaScript from somewhere fails that
in exactly the environments that matter.

Joining calls to deposit years is the one fiddly part. The screen stage keys on
the FASTA record id, which from NCBI is an accession with a version suffix
(`AB123456.1`). The metadata written by the retrieve stage keys on the
esummary Caption, which is the accession without the version (`AB123456`). The
join therefore strips the version from both sides, and where several versions
of one accession appear, the one with the latest update date wins: a revised
record supersedes its predecessor rather than being counted twice.

Degeneracy is printed beside each assay's coverage, not in a footnote. A
coverage figure for a billion-fold degenerate pan-family primer set is close to
a tautology, and a reader who sees the number without the caveat has been
misled by the report rather than informed by it.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import html
import sys
from datetime import date
from pathlib import Path
from typing import Any

from assaywatch.degeneracy import assay_degeneracy
from assaywatch.drift import AssayDrift, assess, by_status, coverage_gaps, pct
from assaywatch.schema import Assay

STATUS_ORDER = ["declining", "low coverage", "watch", "insufficient data", "no recent data", "stable"]
STATUS_COLOUR = {
    "declining": "#b3261e",
    "low coverage": "#8a4b9c",
    "watch": "#b26a00",
    "insufficient data": "#5f6368",
    "no recent data": "#5f6368",
    "stable": "#1e6b3a",
}


def _open(path: Path):
    return gzip.open(path, "rt") if str(path).endswith(".gz") else open(path)


def strip_version(accession: str) -> str:
    """`AB123456.2` -> `AB123456`. Leaves anything without a version alone.

    PDB chains come back from efetch as `pdb|29WD|T` in the FASTA but as
    `29WD_T` in esummary; both are mapped to the latter so they join.
    """
    head = accession.split()[0] if accession.split() else accession
    if head.startswith("pdb|"):
        parts = head.split("|")
        return "_".join(p for p in parts[1:3] if p)
    stem, _, tail = head.rpartition(".")
    return stem if stem and tail.isdigit() else head


def version_of(accession: str) -> int:
    """The `.N` version of an accession, 0 when there is none."""
    tail = accession.split()[0].rpartition(".")[2] if accession.split() else ""
    return int(tail) if tail.isdigit() else 0


def read_calls(path: Path) -> list[dict[str, Any]]:
    """The three columns the drift statistic needs, one small dict per row.

    Loading every column of a two-million-row calls table as dicts took 3.6 GB;
    nothing downstream reads the other columns.
    """
    with _open(path) as fh:
        reader = csv.reader(fh, delimiter="\t")
        header = next(reader, None)
        if header is None:
            return []
        ia, ir, ic = header.index("assay_id"), header.index("record_id"), header.index("call")
        return [{"assay_id": r[ia], "record_id": r[ir], "call": r[ic]} for r in reader if r]


def read_dates(retrieved_dir: Path) -> dict[str, str]:
    """{accession without version: deposit date (YYYY-MM-DD)}, newest revision winning."""
    best: dict[str, tuple[str, str]] = {}
    for meta in sorted(retrieved_dir.rglob("*.meta.tsv.gz")):
        with gzip.open(meta, "rt") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                acc = strip_version(row["accession"])
                created = (row.get("created") or "")[:10]
                if not created[:4].isdigit():
                    continue
                updated = row.get("updated") or ""
                if acc not in best or updated > best[acc][0]:
                    best[acc] = (updated, created)
    return {acc: created for acc, (_, created) in best.items()}


def read_years(retrieved_dir: Path) -> dict[str, int]:
    """{accession without version: deposit year}, newest revision winning."""
    return {acc: int(d[:4]) for acc, d in read_dates(retrieved_dir).items()}


def key_calls_by_accession(calls: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Normalise record ids so they join against the metadata, newest version only.

    Newest means the highest `.N` version, not the last row: the pipeline
    concatenates archives group by group, so an older version can come last.
    """
    seen: dict[tuple[str, str], tuple[int, dict[str, Any]]] = {}
    for row in calls:
        acc = strip_version(row["record_id"])
        v = version_of(row["record_id"])
        key = (row["assay_id"], acc)
        if key not in seen or v >= seen[key][0]:
            seen[key] = (v, {**row, "record_id": acc})
    return [row for _, row in seen.values()]


def oligo_twins(assays: dict[str, Assay]) -> dict[str, list[str]]:
    """{assay id: other assays with exactly the same primers and probe}.

    The WCS sheet lists some primer sets more than once (a published name and a
    lab name, or two rounds that share a primer pair); their rows in the report
    are identical, and the reader should be told so rather than count them twice.
    """
    by_oligos: dict[tuple, list[str]] = {}
    for aid, a in assays.items():
        if a.status.value == "deprecated":
            continue
        probe = a.oligos.probe.matching_seq if a.oligos.probe else ""
        key = (a.oligos.forward.matching_seq, a.oligos.reverse.matching_seq, probe)
        by_oligos.setdefault(key, []).append(aid)
    out: dict[str, list[str]] = {}
    for ids in by_oligos.values():
        if len(ids) > 1:
            for aid in ids:
                out[aid] = sorted(i for i in ids if i != aid)
    return out


def md(text: Any) -> str:
    """Make text safe inside a markdown table cell."""
    return str(text).replace("|", "\\|").replace("\n", " ")


def sparkline(drift: AssayDrift, width: int = 220, height: int = 34) -> str:
    """Detected share by deposit year, as inline SVG. No axis: it is a shape, not a plot."""
    years = sorted(y for y, s in drift.years.items() if s.evaluable)
    if len(years) < 2:
        return '<span class="muted">not enough years</span>'
    lo, hi = years[0], years[-1]
    pts = []
    for y in years:
        frac = drift.years[y].fraction or 0.0
        x = (y - lo) / max(1, hi - lo) * (width - 4) + 2
        pts.append(f"{x:.1f},{(1 - frac) * (height - 6) + 3:.1f}")
    thresh_y = (1 - drift.threshold) * (height - 6) + 3
    colour = STATUS_COLOUR.get(drift.status, "#5f6368")
    return (
        f'<svg width="{width}" height="{height}" role="img" '
        f'aria-label="detected share {lo} to {hi}">'
        f'<line x1="0" y1="{thresh_y:.1f}" x2="{width}" y2="{thresh_y:.1f}" '
        f'stroke="#bbb" stroke-dasharray="3 3"/>'
        f'<polyline fill="none" stroke="{colour}" stroke-width="2" points="{" ".join(pts)}"/>'
        f"</svg>"
    )


def year_table_rows(drift: AssayDrift) -> list[tuple[int, int, int, str]]:
    rows = []
    for year in sorted(drift.years):
        s = drift.years[year]
        frac = pct(s.fraction) if s.fraction is not None else "-"
        rows.append((year, s.detected, s.evaluable, frac))
    return rows


def render_markdown(
    drifts: dict[str, AssayDrift],
    assays: dict[str, Assay],
    gaps: list[dict[str, Any]],
    run_date: str,
    cfg: dict[str, Any] | None = None,
) -> str:
    grouped = by_status(drifts)
    twins = oligo_twins(assays)
    out = [f"# AssayWatch report — {run_date}", ""]
    counts = ", ".join(f"{len(grouped.get(s, []))} {s}" for s in STATUS_ORDER if grouped.get(s))
    out += [f"{len(drifts)} assays screened: {counts}.", ""]
    if drifts:
        a0 = next(iter(drifts.values()))
        out += [
            f"Recent window: records deposited since {a0.recent_from}; "
            f"threshold {a0.threshold:.0%} detected; at least {a0.min_records} recent evaluable "
            "records to flag. Deprecated assays are not screened.",
            "",
        ]
    out += [
        "`detected` means predicted to amplify (`detect` or `reduced`). The denominator is",
        "evaluable records only: those where both primers landed in the right orientation and",
        "size range. Records with no amplicon, or too many undetermined bases to judge, are",
        "counted separately and excluded, so a bad sequencing year cannot look like drift.",
        "Intervals are Wilson 95%; an assay is flagged only when the upper bound of the recent",
        "interval falls below the threshold. **Declining** means the share has also fallen",
        "from the baseline (the interval for the change excludes zero): that is drift.",
        "**Low coverage** means below threshold without a measurable fall: usually an assay",
        "screened against more diversity than it was designed for.",
        "",
    ]

    for status in STATUS_ORDER:
        items = grouped.get(status)
        if not items:
            continue
        out += [f"## {status.title()} ({len(items)})", ""]
        out += [
            "| assay | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | note |",
            "|---|---|---|---|---|---|---|",
        ]
        for a in items:
            assay = assays.get(a.assay_id)
            deg = assay_degeneracy(assay) if assay else None
            deg_text = f"{deg.total_fold}x {deg.tier(cfg)}" if deg else "-"
            frac = f"{a.recent_fraction:.1%}" if a.recent_fraction is not None else "-"
            ci = f"{pct(a.recent_ci[0])}-{pct(a.recent_ci[1])}" if a.recent_evaluable else "-"
            base = pct(a.baseline_fraction) + f" ({a.baseline_evaluable})" if a.baseline_evaluable else "-"
            note = a.note + (
                f" Same oligos as {', '.join(twins[a.assay_id])}." if a.assay_id in twins else ""
            )
            out.append(
                f"| `{md(a.assay_id)}` | {frac} | {ci} | {a.recent_evaluable} | {base} "
                f"| {deg_text} | {md(note)} |"
            )
        out.append("")

    flagged = grouped.get("declining", []) + grouped.get("low coverage", [])
    if flagged:
        out += ["## Detail for flagged assays", ""]
        for a in flagged:
            assay = assays.get(a.assay_id)
            out += [f"### `{a.assay_id}`", ""]
            if assay:
                out.append(f"{assay.name}  ")
                if assay.citation.doi:
                    out.append(f"Designed {assay.citation.design_year or '?'}, doi:{assay.citation.doi}  ")
                deg = assay_degeneracy(assay)
                if deg.note(cfg):
                    out.append(f"**Degeneracy:** {deg.note(cfg)}  ")
            out += ["", "| deposit year | detected | evaluable | share |", "|---|---|---|---|"]
            for year, det, ev, frac in year_table_rows(a):
                out.append(f"| {year} | {det} | {ev} | {frac} |")
            un = a.unevaluable()
            if un:
                out.append("")
                out.append("Excluded: " + ", ".join(f"{n} {k}" for k, n in sorted(un.items())))
            out.append("")

    out += ["## Coverage gaps", ""]
    if not gaps:
        out += ["Every assay has enough evaluable records to say something.", ""]
    else:
        out += [
            "These assays cannot be validated against sequence data because the sequence data",
            "does not exist. For wildlife pathogens this is usually the finding, not a caveat.",
            "An assay with no taxid was never searched: that is a registry gap, not a data gap.",
            "",
            "| assay | taxon | taxid | evaluable | screened |",
            "|---|---|---|---|---|",
        ]
        for g in gaps:
            out.append(
                f"| `{md(g['assay_id'])}` | {md(g['taxon_name'] or '-')} | {g['taxid'] or '-'} "
                f"| {g['evaluable']} | {g['screened'] if g['taxid'] else 'not searched (no taxid)'} |"
            )
        out.append("")
    return "\n".join(out)


CSS = """
:root { --fg:#1b1b1b; --muted:#5f6368; --line:#e3e3e3; }
body { font: 15px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
       color: var(--fg); max-width: 1100px; margin: 2rem auto; padding: 0 1rem; }
h1 { margin-bottom: .2rem; }
h2 { margin-top: 2rem; border-bottom: 1px solid var(--line); padding-bottom: .3rem; }
table { border-collapse: collapse; width: 100%; margin: .6rem 0 1.4rem; }
th, td { text-align: left; padding: .35rem .5rem; border-bottom: 1px solid var(--line); vertical-align: top; }
th { font-weight: 600; font-size: .85rem; color: var(--muted);
     text-transform: uppercase; letter-spacing: .03em; }
code { font-size: .9em; background: #f5f5f5; padding: .05rem .25rem; border-radius: 3px; }
.muted { color: var(--muted); }
.pill { display: inline-block; padding: .05rem .5rem; border-radius: 999px; color: #fff; font-size: .8rem; }
.lead { color: var(--muted); max-width: 62ch; }
@media (prefers-color-scheme: dark) {
  :root { --fg:#e8e8e8; --muted:#a0a0a0; --line:#333; }
  body { background:#121212; } code { background:#222; }
}
"""


def render_html(
    drifts: dict[str, AssayDrift],
    assays: dict[str, Assay],
    gaps: list[dict[str, Any]],
    run_date: str,
    cfg: dict[str, Any] | None = None,
) -> str:
    grouped = by_status(drifts)
    twins = oligo_twins(assays)
    e = html.escape
    parts = [
        "<!doctype html><html lang='en'><head><meta charset='utf-8'>",
        "<meta name='viewport' content='width=device-width, initial-scale=1'>",
        f"<title>AssayWatch — {e(run_date)}</title><style>{CSS}</style></head><body>",
        f"<h1>AssayWatch report</h1><p class='muted'>{e(run_date)}</p>",
        "<p class='lead'>Detected means predicted to amplify. The denominator is evaluable "
        "records only: both primers landed in the right orientation and size range. Records "
        "with no amplicon, or too many undetermined bases to judge, are excluded and counted "
        "separately. Intervals are Wilson 95%; an assay is flagged only when the upper "
        "bound of the recent interval falls below the threshold. Declining means the share has "
        "also fallen from the baseline (that is drift); low coverage means below threshold "
        "without a measurable fall.</p>",
    ]
    for status in STATUS_ORDER:
        items = grouped.get(status)
        if not items:
            continue
        colour = STATUS_COLOUR[status]
        parts.append(
            f"<h2><span class='pill' style='background:{colour}'>{e(status)}</span> {len(items)}</h2>"
        )
        parts.append(
            "<table><tr><th>assay</th><th>trend</th><th>detected</th><th>95% CI</th>"
            "<th>evaluable</th><th>baseline (n)</th><th>degeneracy</th><th>note</th></tr>"
        )
        for a in items:
            assay = assays.get(a.assay_id)
            deg = assay_degeneracy(assay) if assay else None
            deg_text = f"{deg.total_fold}&times; {deg.tier(cfg)}" if deg else "-"
            frac = f"{a.recent_fraction:.1%}" if a.recent_fraction is not None else "-"
            ci = f"{pct(a.recent_ci[0])}&ndash;{pct(a.recent_ci[1])}" if a.recent_evaluable else "-"
            base = f"{pct(a.baseline_fraction)} ({a.baseline_evaluable})" if a.baseline_evaluable else "-"
            note = a.note + (
                f" Same oligos as {', '.join(twins[a.assay_id])}." if a.assay_id in twins else ""
            )
            parts.append(
                f"<tr><td><code>{e(a.assay_id)}</code><br><span class='muted'>"
                f"{e(assay.name) if assay else ''}</span></td>"
                f"<td>{sparkline(a)}</td><td>{frac}</td><td>{ci}</td>"
                f"<td>{a.recent_evaluable}</td><td>{base}</td><td>{deg_text}</td>"
                f"<td class='muted'>{e(note)}</td></tr>"
            )
        parts.append("</table>")

    # The same per-year detail the markdown report has, folded away by default.
    flagged = grouped.get("declining", []) + grouped.get("low coverage", [])
    if flagged:
        parts.append("<h2>Detail for flagged assays</h2>")
        for a in flagged:
            assay = assays.get(a.assay_id)
            parts.append(f"<details><summary><code>{e(a.assay_id)}</code></summary>")
            if assay:
                bits = [e(assay.name)]
                if assay.citation.doi:
                    bits.append(f"designed {assay.citation.design_year or '?'}, doi:{e(assay.citation.doi)}")
                deg = assay_degeneracy(assay)
                if deg.note(cfg):
                    bits.append(f"degeneracy: {e(deg.note(cfg))}")
                parts.append("<p class='muted'>" + "<br>".join(bits) + "</p>")
            parts.append(
                "<table><tr><th>deposit year</th><th>detected</th><th>evaluable</th><th>share</th></tr>"
            )
            for year, det, ev, frac in year_table_rows(a):
                parts.append(f"<tr><td>{year}</td><td>{det}</td><td>{ev}</td><td>{frac}</td></tr>")
            parts.append("</table>")
            un = a.unevaluable()
            if un:
                parts.append(
                    "<p class='muted'>Excluded: "
                    + ", ".join(f"{n} {e(k)}" for k, n in sorted(un.items()))
                    + "</p>"
                )
            parts.append("</details>")

    parts.append("<h2>Coverage gaps</h2>")
    if not gaps:
        parts.append("<p class='muted'>Every assay has enough evaluable records to say something.</p>")
    else:
        parts.append(
            "<p class='lead'>These assays cannot be validated against sequence data because the "
            "sequence data does not exist. For wildlife pathogens this is usually the finding. An assay "
            "with no taxid was never searched: that is a registry gap, not a data gap.</p>"
            "<table><tr><th>assay</th><th>taxon</th><th>taxid</th><th>evaluable</th><th>screened</th></tr>"
        )
        for g in gaps:
            parts.append(
                f"<tr><td><code>{e(g['assay_id'])}</code></td><td>{e(str(g['taxon_name'] or '-'))}</td>"
                f"<td>{g['taxid'] or '-'}</td><td>{g['evaluable']}</td>"
                f"<td>{g['screened'] if g['taxid'] else 'not searched (no taxid)'}</td></tr>"
            )
        parts.append("</table>")
    parts.append("</body></html>")
    return "\n".join(parts)


def build(
    calls_path: Path,
    registry: Path,
    retrieved: Path,
    cfg: dict[str, Any],
    run_date: str | None = None,
    today: date | None = None,
) -> tuple[str, str, dict[str, AssayDrift]]:
    from assaywatch.validate import iter_files, load_assay

    assays = {}
    taxa: dict[str, tuple[int | None, str | None]] = {}
    for path in iter_files(registry):
        a = load_assay(path)
        assays[a.id] = a
        # A deprecated assay is not screened, so it is not a coverage gap either.
        if a.status.value != "deprecated":
            taxa[a.id] = (a.target.taxid, a.target.taxon_name)

    calls = key_calls_by_accession(read_calls(calls_path))
    dates = read_dates(retrieved)
    run_date = run_date or calls_path.parent.name
    if today is None:
        # The recent window is anchored to the run, so re-rendering an old run
        # later gives the same answer rather than sliding the window forward.
        try:
            today = date.fromisoformat(run_date[:10])
        except ValueError:
            today = None
    drifts = assess(calls, dates, cfg, today=today)
    gaps = coverage_gaps(drifts, taxa, cfg)
    return (
        render_markdown(drifts, assays, gaps, run_date, cfg),
        render_html(drifts, assays, gaps, run_date, cfg),
        drifts,
    )


def main(argv: list[str] | None = None) -> int:
    from assaywatch.score import load_config

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("calls", type=Path)
    ap.add_argument("--registry", type=Path, default=Path("registry"))
    ap.add_argument("--retrieved", type=Path, default=Path("data/retrieved"))
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--run-date", default=None)
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    md, page, drifts = build(args.calls, args.registry, args.retrieved, cfg, run_date=args.run_date)
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "report.md").write_text(md)
    (args.out / "report.html").write_text(page)

    grouped = by_status(drifts)
    for status in STATUS_ORDER:
        if grouped.get(status):
            print(f"{status:<18} {len(grouped[status])}", file=sys.stderr)
    print(f"wrote {args.out / 'report.md'} and {args.out / 'report.html'}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
