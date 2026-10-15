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
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any

from assaywatch.degeneracy import assay_degeneracy
from assaywatch.drift import (
    FOOTPRINT_COLUMNS,
    FOOTPRINT_REQUIRED,
    AssayDrift,
    assess,
    by_status,
    coverage_gaps,
    footprint_signature,
    pct,
)
from assaywatch.nested import NestedFamily, unpaired
from assaywatch.nested import assess as assess_nested
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
DEFAULT_COLOUR = "#5f6368"


def status_order(grouped: dict[str, Any]) -> list[str]:
    """The listed statuses in order, then any the report was not told about.

    The report walks STATUS_ORDER and prints only what it finds there, so a
    status that is absent from the list is not an error - it is an assay that is
    quietly missing from both reports, with a headline count ("164 assays
    screened") that no longer adds up to the sections beneath it. The review
    found one such status in the code (`AssayDrift` defaults to "no data", which
    is unreachable through `assess` today but is exactly what a future status
    would look like). Appending the unknown ones, sorted so the output is
    stable, makes a new status show up as an unstyled section instead of
    disappearing.
    """
    return [*STATUS_ORDER, *sorted(s for s in grouped if s not in STATUS_ORDER)]


def _open(path: Path):
    return gzip.open(path, "rt") if str(path).endswith(".gz") else open(path)


def strip_version(accession: str) -> str:
    """`AB123456.2` -> `AB123456`. Leaves anything without a version alone.

    This is the join key between two things NCBI names differently: the FASTA
    header (what screening sees) and the esummary caption (what carries the
    deposit date). Get it wrong and records silently lose their date and drop out
    of the drift denominator, which is how 476 PDB-derived calls went missing.

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


def read_calls(path: Path, with_spans: set[str] | None = None) -> list[dict[str, Any]]:
    """The columns the drift statistic needs, one small dict per row.

    Loading every column of a two-million-row calls table as dicts took 3.6 GB;
    nothing downstream reads the other columns. The six mismatch columns are
    folded into ONE interned `footprint` string per row rather than carried as
    six, so the cost is a pointer per row and millions of identical exact-match
    footprints are a single object. A row has no `footprint` key when the columns
    are absent from the table OR the row's own scoring cells are blank (a row from
    an older screen that `collect.concatenate_screens` blank-filled), which
    `drift.assess` reads as "unknown" and not as "all the same".
    """
    with _open(path) as fh:
        reader = csv.reader(fh, delimiter="\t")
        header = next(reader, None)
        if header is None:
            return []
        ia, ir, ic = header.index("assay_id"), header.index("record_id"), header.index("call")
        span_idx = (
            [header.index(c) for c in ("amplicon_start", "amplicon_end")]
            if with_spans and all(c in header for c in ("amplicon_start", "amplicon_end"))
            else None
        )
        # `exclusion` says why an unusable record was unusable (score.classify_exclusion).
        ie = header.index("exclusion") if "exclusion" in header else None
        # The footprint is known only where the row's own scoring columns are
        # populated (see drift.FOOTPRINT_REQUIRED). Having the six mismatch
        # columns in the HEADER is not enough: `collect.concatenate_screens` unions
        # the headers of old and new screens and blank-fills the cells an older
        # screen never had, so an older screen's rows arrive with all six columns
        # present and empty - indistinguishable from a clean record unless the
        # scoring cells beside them are checked. All six columns or none: a partial
        # footprint would compare unequal to a full one that agrees with it.
        fp_idx = (
            [header.index(c) for c in FOOTPRINT_COLUMNS]
            if all(c in header for c in (*FOOTPRINT_COLUMNS, *FOOTPRINT_REQUIRED))
            else None
        )
        req_idx = [header.index(c) for c in FOOTPRINT_REQUIRED] if fp_idx is not None else []
        rows = []
        for r in reader:
            if not r:
                continue
            row = {
                "assay_id": r[ia],
                "record_id": r[ir],
                "call": r[ic],
                "exclusion": (r[ie] if ie is not None and ie < len(r) else ""),
            }
            if fp_idx is not None and all(i < len(r) and r[i] != "" for i in req_idx):
                row["footprint"] = footprint_signature(r[i] if i < len(r) else "" for i in fp_idx)
            if span_idx is not None and row["assay_id"] in with_spans:
                a, b = (r[i] if i < len(r) else "" for i in span_idx)
                if a and b:
                    row["amplicon_start"], row["amplicon_end"] = a, b
            rows.append(row)
        return rows


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
    colour = STATUS_COLOUR.get(drift.status, DEFAULT_COLOUR)
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


def duplication_summary(flagged: list[AssayDrift]) -> str:
    """One line on how many flags survive the duplication check; "" only if nothing is flagged.

    Counts only the assays it could check, and says so, because an unchecked flag
    is not a surviving one: a calls table screened before the footprint columns
    existed would otherwise read as a clean bill of health. When NONE could be
    checked it says that instead of going quiet, since silence there reads exactly
    like "nothing to report".
    """
    if not flagged:
        return ""
    checked = [a for a in flagged if a.flag_survives_clustering is not None]
    if not checked:
        n = len(flagged)
        return (
            f"not run for {'this flagged assay' if n == 1 else f'any of the {n} flagged assays'}: "
            "their binding-site footprints are unknown (the calls table includes screens from before "
            "the footprint columns were written, or counts diverged records as failures), so nothing "
            "can be said about whether the flags rest on duplicated records."
        )
    held = sum(1 for a in checked if a.flag_survives_clustering)
    tail = f" ({len(flagged) - len(checked)} could not be checked)" if len(checked) < len(flagged) else ""
    text = (
        f"{held} of {len(checked)} flagged assays still hold when duplicated records are discounted "
        f"(each distinct binding-site footprint counted once, and the sample size cut to the number "
        f"of footprints){tail}."
    )
    # Only when something failed the check: a sentence about the remainder after a
    # clean 5 of 5 is a sentence about nothing. Which test each failed is in its own note.
    if held < len(checked):
        text += " The note on each assay that did not hold says which test it failed."
    return text


def registry_status_line(drifts: dict[str, AssayDrift], assays: dict[str, Assay]) -> str:
    """How many of the screened assays are drafts, said at the top of the report.

    A `draft` entry needs only correct structure and valid IUPAC oligos; `active`
    is what requires a verified DOI, a checked taxid and a named submitter. The
    table beneath presented all of them with identical authority, which for a
    registry that is 210 drafts and one active assay is the report overstating
    what it knows. The oligo and provenance audits in `scripts/` exist because
    transcription errors were found, so this is not a hypothetical difference.
    """
    counts = Counter(assays[a].status.value for a in drifts if a in assays)
    if not counts:
        return ""
    listed = ", ".join(f"{n} {name}" for name, n in sorted(counts.items(), key=lambda x: (-x[1], x[0])))
    text = f"Registry status: {listed}."
    if counts.get("draft"):
        text += (
            " A draft entry has been checked for structure and valid IUPAC oligos only — not for"
            " a verified citation, taxid or submitter — so read its numbers as provisional."
        )
    return text


def flag_confidence_line(grouped: dict[str, list[AssayDrift]]) -> str:
    """The duplication result, beside the flag counts rather than below them.

    `duplication_summary` already said this, but only inside the per-assay detail
    section, while the counts a reader takes away are at the top. In the
    2026-10-07 run 35 of 84 flags survived the check: a headline of "37
    declining, 47 low coverage" with that fact two screens down is the report
    leading with its least reliable number.
    """
    flagged = grouped.get("declining", []) + grouped.get("low coverage", [])
    summary = duplication_summary(flagged)
    return f"**Duplication check:** {summary}" if summary else ""


def nested_section(fams: dict[str, NestedFamily], assays: dict[str, Assay], threshold: float) -> list[str]:
    """What a nested protocol does, which its per-round rows cannot say.

    Each round keeps the score it earned - either product can be read on a gel,
    so a round whose primers still match is a usable assay on its own. What is
    added here is the protocol's own coverage: the share of records BOTH rounds
    reach, which is what the published nest delivers, and how far that sits
    below round 2 read alone.
    """
    have = [f for f in fams.values() if f.records]
    if not have:
        return []
    warned = [f for f in have if f.warns(threshold)]
    broken = [f for f in have if f.nests is False]
    out = [f"## Nested protocols ({len(have)})", ""]
    out += [
        "Rounds are scored separately above, and that stands: either product can be read on a gel.",
        "This section adds what neither row can say alone — the share of records **both** rounds",
        "reach, which is what the protocol delivers when it is run as published. Round 2's own",
        "figure is what it would do as a direct PCR; where round 1 has drifted, part of that",
        "coverage is unreachable because the inner reaction gets no enriched template.",
        "",
    ]
    if warned:
        nonnesting = len([f for f in have if f.nests is False])
        line = f"**{len(warned)} of {len(have)}** lose coverage this way."
        if nonnesting:
            line += (
                f" A further {nonnesting} are labelled as rounds but do not nest, so no conditional"
                " coverage is computed for them."
            )
        out += [line, ""]
    out += [
        "| protocol | round 1 | round 2 alone | run as a nest | records | inner inside outer |",
        "|---|---|---|---|---|---|",
    ]
    for f in sorted(have, key=lambda f: (f.gap is None, -(f.gap or 0))):
        c = f.containment.get((f.outer, f.inner))
        cont = "-"
        if c and c[1]:
            cont = "yes" if f.nests else f"**no** ({c[0]:,}/{c[1]:,})"
        # Withheld where the amplicons do not nest, for the same reason the note
        # gives: conditioning round 2 on a round 1 that does not feed it would
        # invent a number, and printing it in the table beside the sentence
        # refusing it is the one place a reader would believe it.
        nested_cell = "not a nest" if f.nests is False else pct(f.nested_share)
        out.append(
            f"| `{md(f.family)}` | {pct(f.outer_share)} | {pct(f.inner_share)} | "
            f"{nested_cell} | {f.records:,} | {cont} |"
        )
    out.append("")
    for f in sorted(broken, key=lambda f: f.family) + sorted(warned, key=lambda f: -(f.gap or 0)):
        out += [f"**`{f.family}`** — {f.note(threshold)}", ""]
    loose = unpaired(assays)
    if loose:
        out += [
            f"{len(loose)} further entries declare a `source.nested_round` but have no sibling by id, so "
            "their protocol could not be assembled and nothing is reported for them: "
            + ", ".join(f"`{md(i)}`" for i in loose[:6])
            + (f", and {len(loose) - 6} more" if len(loose) > 6 else "")
            + ". Which entries belong together is a curation question — the Chlamydia nest, for one, "
            "runs a genus-level round 1 into three species-specific round 2 entries on three taxids.",
            "",
        ]
    return out


def render_markdown(
    drifts: dict[str, AssayDrift],
    assays: dict[str, Assay],
    gaps: list[dict[str, Any]],
    run_date: str,
    cfg: dict[str, Any] | None = None,
    nested: dict[str, NestedFamily] | None = None,
) -> str:
    grouped = by_status(drifts)
    twins = oligo_twins(assays)
    out = [f"# AssayWatch report — {run_date}", ""]
    counts = ", ".join(f"{len(grouped.get(s, []))} {s}" for s in status_order(grouped) if grouped.get(s))
    out += [f"{len(drifts)} assays screened: {counts}.", ""]
    if registry_status_line(drifts, assays):
        out += [registry_status_line(drifts, assays), ""]
    headline = flag_confidence_line(grouped)
    if headline:
        out += [headline, ""]
    if drifts:
        # The base window comes from the config, not from whichever assay happens
        # to be first: 28 assays widened theirs, and the header claimed Oct 2024
        # for all 141.
        a0 = next(iter(drifts.values()))
        widened = sum(
            1
            for a in drifts.values()
            if a.window_months > (cfg or {}).get("drift", {}).get("recent_window_months", 24)
        )
        out += [
            f"Recent window: {(cfg or {}).get('drift', {}).get('recent_window_months', 24)} months"
            + (f", widened for {widened} assays that held too few records" if widened else "")
            + f"; earliest shown {a0.recent_from}; "
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

    for status in status_order(grouped):
        items = grouped.get(status)
        if not items:
            continue
        out += [f"## {status.title()} ({len(items)})", ""]
        out += [
            "| assay | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | note |",
            "|---|---|---|---|---|---|---|---|",
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
            entry = assay.status.value if assay else "-"
            out.append(
                f"| `{md(a.assay_id)}` | {entry} | {frac} | {ci} | {a.recent_evaluable} | {base} "
                f"| {deg_text} | {md(note)} |"
            )
        out.append("")

    flagged = grouped.get("declining", []) + grouped.get("low coverage", [])
    if flagged:
        out += ["## Detail for flagged assays", ""]
        if duplication_summary(flagged):
            out += [f"**Duplication check:** {duplication_summary(flagged)}", ""]
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
            if a.clustering_note:
                out += ["", f"**Duplication check:** {a.clustering_note}"]
            un = a.unevaluable()
            if un:
                out.append("")
                out.append("Excluded: " + ", ".join(f"{n} {k}" for k, n in sorted(un.items())))
                if a.exclusions:
                    out.append("")
                    out.append(
                        "Why: "
                        + ", ".join(f"{n} {k}" for k, n in a.exclusions.most_common())
                        + ". `truncated` means the deposit stops before the other primer's site, so it"
                        + " says nothing about the assay; `diverged` means that site is present and does"
                        + " not match."
                    )
            out.append("")

    if nested is not None:
        thr = (cfg or {}).get("drift", {}).get("detect_fraction_threshold", 0.9)
        out += nested_section(nested, assays, thr)

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
    nested: dict[str, NestedFamily] | None = None,
) -> str:
    grouped = by_status(drifts)
    twins = oligo_twins(assays)
    e = html.escape
    parts = [
        "<!doctype html><html lang='en'><head><meta charset='utf-8'>",
        "<meta name='viewport' content='width=device-width, initial-scale=1'>",
        f"<title>AssayWatch — {e(run_date)}</title><style>{CSS}</style></head><body>",
        f"<h1>AssayWatch report</h1><p class='muted'>{e(run_date)}</p>",
        f"<p class='lead'>{e(registry_status_line(drifts, assays))}</p>",
        "<p class='lead'>Detected means predicted to amplify. The denominator is evaluable "
        "records only: both primers landed in the right orientation and size range. Records "
        "with no amplicon, or too many undetermined bases to judge, are excluded and counted "
        "separately. Intervals are Wilson 95%; an assay is flagged only when the upper "
        "bound of the recent interval falls below the threshold. Declining means the share has "
        "also fallen from the baseline (that is drift); low coverage means below threshold "
        "without a measurable fall.</p>",
    ]
    if flag_confidence_line(grouped):
        parts.append(
            "<p class='lead'><b>Duplication check:</b> "
            f"{e(duplication_summary(grouped.get('declining', []) + grouped.get('low coverage', [])))}</p>"
        )
    for status in status_order(grouped):
        items = grouped.get(status)
        if not items:
            continue
        colour = STATUS_COLOUR.get(status, DEFAULT_COLOUR)
        parts.append(
            f"<h2><span class='pill' style='background:{colour}'>{e(status)}</span> {len(items)}</h2>"
        )
        parts.append(
            "<table><tr><th>assay</th><th>entry</th><th>trend</th><th>detected</th><th>95% CI</th>"
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
                f"<td>{e(assay.status.value) if assay else '-'}</td>"
                f"<td>{sparkline(a)}</td><td>{frac}</td><td>{ci}</td>"
                f"<td>{a.recent_evaluable}</td><td>{base}</td><td>{deg_text}</td>"
                f"<td class='muted'>{e(note)}</td></tr>"
            )
        parts.append("</table>")

    # The same per-year detail the markdown report has, folded away by default.
    flagged = grouped.get("declining", []) + grouped.get("low coverage", [])
    if flagged:
        parts.append("<h2>Detail for flagged assays</h2>")
        if duplication_summary(flagged):
            parts.append(f"<p class='lead'><b>Duplication check:</b> {e(duplication_summary(flagged))}</p>")
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
            if a.clustering_note:
                parts.append(f"<p class='muted'><b>Duplication check:</b> {e(a.clustering_note)}</p>")
            un = a.unevaluable()
            if un:
                parts.append(
                    "<p class='muted'>Excluded: "
                    + ", ".join(f"{n} {e(k)}" for k, n in sorted(un.items()))
                    + "</p>"
                )
            parts.append("</details>")

    if nested:
        thr = (cfg or {}).get("drift", {}).get("detect_fraction_threshold", 0.9)
        have = [f for f in nested.values() if f.records]
        if have:
            parts.append("<h2>Nested protocols</h2>")
            parts.append(
                "<p class='lead'>Rounds are scored separately above, and that stands: either product can "
                "be read on a gel. This adds the share of records <b>both</b> rounds reach — what the "
                "protocol delivers run as published. Round 2's own figure is what it would do as a direct "
                "PCR.</p>"
                "<table><tr><th>protocol</th><th>round 1</th><th>round 2 alone</th><th>run as a nest</th>"
                "<th>records</th><th>inner inside outer</th></tr>"
            )
            for f in sorted(have, key=lambda f: (f.gap is None, -(f.gap or 0))):
                c = f.containment.get((f.outer, f.inner))
                cont = "-"
                if c and c[1]:
                    cont = "yes" if f.nests else f"<b>no</b> ({c[0]:,}/{c[1]:,})"
                nested_cell = "not a nest" if f.nests is False else pct(f.nested_share)
                parts.append(
                    f"<tr><td><code>{e(f.family)}</code></td><td>{pct(f.outer_share)}</td>"
                    f"<td>{pct(f.inner_share)}</td><td>{nested_cell}</td>"
                    f"<td>{f.records:,}</td><td>{cont}</td></tr>"
                )
            parts.append("</table>")
            for f in sorted(have, key=lambda f: -(f.gap or 0)):
                if f.nests is False or f.warns(thr):
                    parts.append(f"<p class='muted'><b><code>{e(f.family)}</code></b> — {e(f.note(thr))}</p>")

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

    # Which assays are rounds of a protocol is known from the registry alone, so
    # the spans the nested check needs are read for those and no others.
    from assaywatch.nested import families

    rounds = {i for v in families(list(assays)).values() for i in v}
    calls = key_calls_by_accession(read_calls(calls_path, with_spans=rounds))
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
    # Nested families are read from the SAME deduplicated calls the drift
    # statistic uses, so the two never disagree about which records exist.
    nested = assess_nested(assays, calls)
    return (
        render_markdown(drifts, assays, gaps, run_date, cfg, nested),
        render_html(drifts, assays, gaps, run_date, cfg, nested),
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
    for status in status_order(grouped):
        if grouped.get(status):
            print(f"{status:<18} {len(grouped[status])}", file=sys.stderr)
    print(f"wrote {args.out / 'report.md'} and {args.out / 'report.html'}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
