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
import gzip
import html
import json
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import TYPE_CHECKING, Any

from assaywatch.accession import strip_version

# Re-exported since accession.py was split out; tests/test_accession.py pins it.
# `ruff --fix` removes an unused import, re-export or not, so the `as` form says so.
from assaywatch.accession import version_of as version_of

# Re-exported: these moved to calls.py so the renderer is not also the project's
# calls-table I/O library, and `report.read_calls` is where every caller and six
# test files already look for them.
from assaywatch.calls import key_calls_by_accession as key_calls_by_accession
from assaywatch.calls import read_calls as read_calls
from assaywatch.calls import read_dates as read_dates
from assaywatch.calls import read_years as read_years
from assaywatch.degeneracy import assay_degeneracy
from assaywatch.drift import STATUS_ORDER as DRIFT_STATUS_ORDER
from assaywatch.drift import (
    AssayDrift,
    assess,
    by_status,
    coverage_gaps,
    pct,
)
from assaywatch.nested import NestedFamily, unpaired
from assaywatch.nested import assess as assess_nested
from assaywatch.review import OLIGO_DOUBT, ReviewFlag
from assaywatch.schema import Assay, SpeciesSize, Status
from assaywatch.timing import format_duration, read_screen_benchmarks

if TYPE_CHECKING:
    from assaywatch.taxonomy import Taxonomy

STATUS_ORDER = list(DRIFT_STATUS_ORDER)  # drift.py owns the vocabulary; see its comment there
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


def oligo_twins(assays: dict[str, Assay]) -> dict[str, list[str]]:
    """{assay id: other assays with exactly the same primers and probe}.

    The registry holds some primer sets more than once (a published name and a
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


def species_table_rows(
    drift: AssayDrift,
    taxonomy: Taxonomy | None = None,
    sizes: list[SpeciesSize] | None = None,
) -> list[tuple[str, int, int, str, str]]:
    """(species, detected, evaluable, share, product bp) for the recent window, biggest first.

    For an assay whose product length names the species — one declaring
    `amplicon_bp_range` — a single genus-wide share is the wrong number: ATI
    Meyer 1997 read 95.3% while one of its species sat at 83%, and the species
    it is rarely asked about (volepox, skunkpox) carry too few records to appear
    in the per-lineage analysis at all. So there is no floor here: every species
    is listed, however thin, and the share of a handful of records is left to
    speak for itself next to its denominator.

    `sizes` is the assay's `species_sizes`, so the table can also say which
    product length each species gives — the thing this kind of assay actually
    reads. A species with no measured band shows `-`.
    """
    bands: dict[int, list[str]] = {}
    for s in sizes or []:
        lo, hi = s.bp
        bands.setdefault(s.taxid, []).append(str(lo) if lo == hi else f"{lo}-{hi}")
    counts = drift.species_counts or {}
    rows = []
    for taxid, (det, n) in counts.items():
        if taxid is None:
            label = "unresolved (no taxid)"
        else:
            name = taxonomy.name.get(taxid) if taxonomy else None
            label = f"{name} ({taxid})" if name else f"taxid {taxid}"
        band = ", ".join(bands.get(taxid, [])) or "-"
        rows.append((label, det, n, pct(det / n) if n else "-", band))
    # Biggest denominator first; a tie reads alphabetically rather than by dict order.
    return sorted(rows, key=lambda r: (-r[2], r[0]))


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

    THIS SENTENCE USED TO BE FALSE. It read "A draft entry has been checked for
    structure and valid IUPAC oligos only — not for a verified citation, taxid or
    submitter — so read its numbers as provisional." Of the 205 drafts screened
    on 2026-10-22, 173 carried a Crossref-verified DOI, a taxid and a design year
    with no open review question: everything `active` mechanically asks for. They
    are drafts because only a maintainer sets `active` and no promotion pass has
    been run, which is a fact about the maintainer's queue and not about the
    entry.

    Saying it that way mattered twice over. A reader who believed the old
    sentence discounted every number in the report for the wrong reason, and the
    right reason went unsaid: what varies between entries is oligo PROVENANCE —
    whether the sequences were read from the cited paper's own table, inferred,
    modified or taken from a secondary list — and that lives in `needs_review`,
    which is now printed per row. So the status line stops standing in for a
    data-quality measure it never was, and points at the one that exists.

    Counted rather than asserted, through `Assay.missing_for_active`, so this
    cannot describe a different rule from the one the validator enforces.
    """
    screened = [assays[a] for a in drifts if a in assays]
    counts = Counter(a.status.value for a in screened)
    if not counts:
        return ""
    listed = ", ".join(f"{n} {name}" for name, n in sorted(counts.items(), key=lambda x: (-x[1], x[0])))
    text = f"Registry status: {listed}."
    drafts = [a for a in screened if a.status is Status.draft]
    if drafts:
        eligible = sum(1 for a in drafts if not a.missing_for_active)
        text += (
            f" `draft` is a maintainer sign-off, not a data check: {eligible} of the {len(drafts)}"
            " drafts here already carry a verified DOI, a taxid and a design year with no open"
            " review question. What does vary between entries is oligo provenance, flagged in the"
            " note column of every row below."
        )
    return text


def freshness_line(results_dir: Path, run_date: str) -> str:
    """When the last run that finished actually finished, said on the page.

    README and CITATION.cff both describe this project as re-screening "on a
    schedule", and until 2026-10-23 there was none: every run was started by
    hand. A report carries its run date in the title, but nothing told a reader
    whether that date was last week or six weeks ago, and a drift monitor whose
    last look was six weeks ago is making a different claim from one that ran on
    Sunday. `profiles/launchd/` is the schedule; this is how a reader sees it
    held -- or sees that it did not.

    Read from the previous runs' `run-timing.json`, which already records
    `finished` and `status` (assaywatch.timing), so nothing new is written.
    Silent when there is no earlier run to compare with, which is the honest
    answer for a first run rather than a claim about freshness.
    """
    from datetime import date

    previous = []
    for timing in sorted(results_dir.glob("*/run-timing.json")):
        try:
            data = json.loads(timing.read_text())
        except (OSError, ValueError):
            continue
        # Keyed on the run_date INSIDE the file, not the directory name. A run
        # can be copied (results/baseline-2026-10-22/ is wave 0's frozen copy)
        # or re-run under a suffix (2026-10-22-tmf-false), and a copy of this
        # run is not a previous run. Both carry their real run_date.
        if data.get("run_date") == run_date:
            continue
        if data.get("status") == "success" and data.get("finished"):
            previous.append((data["finished"][:10], data["run_date"]))
    if not previous:
        return ""
    finished, _ = max(previous)
    try:
        days = (date.fromisoformat(run_date[:10]) - date.fromisoformat(finished)).days
    except ValueError:
        return ""
    if days < 0:
        return ""
    ago = "the same day" if days == 0 else "1 day earlier" if days == 1 else f"{days} days earlier"
    return f"Previous successful run: {finished} ({ago})."


def timing_lines(results_dir: Path, run_date: str, top: int = 10) -> list[str]:
    """Per-stage wall times and the slowest screening groups, for the footer.

    Item 7 of docs/2026-10-18-pipeline-timekeeping-todo.md, and the last one
    outstanding. The run that prompted that list stalled for hours on one
    retrieval group and the log gave no way to tell slow from stuck; items 1-6
    fixed the live signals, and this is the record left behind afterwards, so the
    next run's cost can be anticipated from the last one's rather than guessed.

    Both halves are read, never recomputed: stage times from `run-timing.json`
    (assaywatch.timing.RunManifest writes it) and per-archive wall times from
    Snakemake's `benchmark:` files under `<results>/benchmarks/`.

    **The stage table usually describes the PREVIOUS run, and says so.** The
    Snakefile closes its `workflow` stage in `onsuccess`, which fires after the
    report rule, so while this report is being written this run's own stages have
    no duration yet -- a footer that insisted on them would print an empty table
    in every run forever. So this run's stages are used when they are complete
    (a report re-rendered afterwards, which is the common case by hand) and the
    most recent completed run's otherwise.

    **Only benchmarks written inside this run's own window are counted.** A
    benchmark is keyed by archive rather than by run date, deliberately, so a
    cached screen keeps its last measurement -- which means a bare directory read
    mixes runs, and Snakemake's wall clock keeps advancing while the machine is
    suspended. Filtering to the window is what stops the table from ranking a
    group by how long the laptop was asleep. A run whose screens were all cached
    measured nothing, and the footer then says so rather than showing stale rows.
    """
    this = _read_timing(results_dir / run_date / "run-timing.json")
    if this is None:
        return []

    out = ["## Run timing", ""]
    stages = _complete_stages(this)
    source = this
    if not stages:
        source = _last_completed_run(results_dir, run_date) or this
        stages = _complete_stages(source)
    if stages:
        if source is this and this.get("finished"):
            elapsed = this.get("elapsed_seconds")
            status = this.get("status", "unknown")
            when = f"Run {run_date} finished {status} after {format_duration(elapsed)}."
        elif source is this:
            when = f"Stage times for run {run_date} as far as it had got when this report was written."
        else:
            when = (
                f"Stage times below are the last completed run, {source.get('run_date')} "
                f"({format_duration(source.get('elapsed_seconds'))} in all): this run's own "
                "stages are still open while its report is being written."
            )
        out += [when, "", "| stage | wall time |", "|---|---:|"]
        out += [f"| {s['name']} | {format_duration(s['seconds'])} |" for s in stages]
        out.append("")

    costs = read_screen_benchmarks(
        results_dir / "benchmarks",
        since=_parse_iso(this.get("started")),
        until=_parse_iso(this.get("finished")),
    )
    if not costs:
        out += [
            "No screening benchmarks were written during this run, so there is no "
            "per-group cost to show: every archive's screen was cached. The figures "
            "appear again on a run that rescreens.",
            "",
        ]
        return out

    total = sum(c.seconds for c in costs)
    shown = costs[:top]
    out += [
        f"{len(costs)} retrieval groups were screened in this run, {format_duration(total)} "
        f"of job time in all. The {len(shown)} slowest:",
        "",
        "| group | archives | wall time | share |",
        "|---|---:|---:|---:|",
    ]
    out += [
        f"| `{c.taxid}/{c.group}` | {c.archives} | {format_duration(c.seconds)} | {c.seconds / total:.0%} |"
        for c in shown
    ]
    out += [
        "",
        "Wall time per archive, summed per group, from Snakemake's `benchmark:` files. "
        "On macOS this is the only column that exists - `max_rss` and `cpu_time` read "
        "`NA` there - so these are elapsed times, not CPU, and a job that spanned a "
        "machine sleep would be inflated by it. Only benchmarks written during this "
        "run are counted.",
        "",
    ]
    return out


def _read_timing(path: Path) -> dict[str, Any] | None:
    try:
        data = json.loads(path.read_text())
    except (OSError, ValueError):
        return None
    return data if isinstance(data, dict) else None


def _complete_stages(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Stages that have a duration. An open stage has `seconds: None`."""
    return [s for s in data.get("stages", []) if isinstance(s, dict) and s.get("seconds") is not None]


def _last_completed_run(results_dir: Path, run_date: str) -> dict[str, Any] | None:
    """The most recently finished successful run that is not this one.

    Keyed on the `run_date` INSIDE each file, not the directory name, for the
    reason `freshness_line` gives: a run directory can be a frozen copy.
    """
    best = None
    for path in sorted(results_dir.glob("*/run-timing.json")):
        data = _read_timing(path)
        if data is None or data.get("run_date") == run_date:
            continue
        if data.get("status") != "success" or not data.get("finished"):
            continue
        if best is None or str(data["finished"]) > str(best["finished"]):
            best = data
    return best


def _parse_iso(value: object) -> datetime | None:
    try:
        return datetime.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None


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


def _nested_cells(r: NestedRow, *, bold: str) -> tuple[str, str]:
    """A nested row's two judgement cells: containment, and the conditional share.

    The share is WITHHELD where the amplicons do not nest, for the same reason
    the note gives: conditioning round 2 on a round 1 that does not feed it
    would invent a number, and printing it in the table beside the sentence
    refusing it is the one place a reader would believe it.
    """
    cont = "-"
    if r.containment:
        seen, total = r.containment
        cont = "yes" if r.nests else f"{bold} ({seen:,}/{total:,})"
    return cont, ("not a nest" if r.nests is False else pct(r.nested_share))


def _round1_cell(r: NestedRow) -> str:
    """Round-1 failures and how many of them are only `diverged`. "-" when none."""
    if not r.round1_failed or not r.round1_failed[0]:
        return "-"
    failed, diverged = r.round1_failed
    return f"{failed:,} ({diverged:,} diverged)"


def nested_section(
    fams: dict[str, NestedFamily],
    assays: dict[str, Assay],
    threshold: float,
    rows: list[NestedRow] | None = None,
) -> list[str]:
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
    # The model's rows when there is a model. Building them again here made this a
    # second decider: the HTML table read `ReportModel.nested_rows` while this one
    # rebuilt its own, so a fact added to the model (a round being not scoreable)
    # reached one report and not the other.
    if rows is None:
        rows = [_nested_row(f) for f in sorted(have, key=nested_sort_key)]
    out = [f"## Nested protocols ({len(have)})", ""]
    out += [
        "Rounds are scored separately above, and that stands: either product can be read on a gel.",
        "This section adds what neither row can say alone — the share of records **both** rounds",
        "reach, which is what the protocol delivers when it is run as published. Round 2's own",
        "figure is what it would do as a direct PCR; where round 1 has drifted, part of that",
        "coverage is unreachable because the inner reaction gets no enriched template.",
        "",
        "A round-1 failure is either a scored `fail` or a record labelled `diverged`: one primer",
        "site found, the partner's window present, nothing credible in it. That label is",
        "reliable for some assays and mostly chance for others (a lone primer hit in an",
        "unrelated record clears the per-record bar), so the last column says how many of each",
        "family's round-1 failures rest on it. Where most of them do, read the nest loss as",
        "an upper bound.",
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
        "| protocol | round 1 | round 2 alone | run as a nest | records | inner inside outer "
        "| round 1 failures (diverged) |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        # The containment and withheld-share rules live in `_nested_cells`, which
        # the HTML table uses too; only the emphasis markup differs.
        cont, nested_cell = _nested_cells(r, bold="**no**")
        out.append(
            f"| `{md(r.family)}`{' (not scoreable)' if r.held_out else ''} | {pct(r.outer_share)} "
            f"| {pct(r.inner_share)} | {nested_cell} | {r.records:,} | {cont} | {_round1_cell(r)} |"
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


# --- The report model -------------------------------------------------------
#
# S3 in docs/2026-10-20-pipeline-audit.md: `render_markdown` and `render_html`
# were 377 lines of parallel layout, so every report change was made twice and
# the two drifted - which is what `scripts/report_diff.py` was left parsing.
#
# What was actually duplicated is the VALUE extraction: assembling each row's
# note, its degeneracy text, its confidence interval, its baseline, the nested
# table's containment cell. The markup was never the problem. So the model holds
# values and each serialiser does nothing but format them: markdown writes an
# en dash as `-` and HTML as `&ndash;`, markdown `x` and HTML `&times;`, and
# neither has an opinion about what belongs in the row.
#
# The two reports are NOT the same document, and this does not make them one.
# Markdown carries a status-count line, the recent-window line, the `Why:`
# exclusion breakdown and the unpaired-nest paragraph; HTML carries a sparkline
# column and folds each detail into a `<details>`. Those are content
# differences, left in their own serialiser deliberately rather than unified,
# because unifying them changes both published reports and that is a decision
# for a maintainer, not a refactor. What the model guarantees is that a row's
# CONTENT is decided once.


@dataclass(frozen=True)
class StatusRow:
    """One assay in one status table. Values, not text."""

    assay_id: str
    assay_name: str
    entry: str
    pooled: str  # the pooled status a lineage override replaced, else ""
    fraction: float | None
    ci: tuple[float, float] | None  # None when there is nothing recent to bound
    evaluable: int
    baseline: tuple[float, int] | None  # (share, n)
    degeneracy: tuple[int, str] | None  # (fold, tier)
    duplication: str  # "holds" / "fails: recent,change" / "unchecked" / "" if unflagged
    note: str
    drift: AssayDrift  # HTML draws a sparkline over the whole year series


@dataclass(frozen=True)
class HeldOutRow:
    """One assay the registry says cannot be scored, and why."""

    assay_id: str
    assay_name: str
    entry: str
    reasons: tuple[tuple[str, str], ...]  # (flag, note) in the order the entry gives


def held_out_reasons(assay: Assay | None) -> tuple[tuple[str, str], ...]:
    """The review items that mean this assay's status would not be a statement.

    `report.py` read `needs_review` nowhere at all, so the registry's own
    warnings never reached the page. Two kinds did real damage on 2026-10-22:

    - `not_screenable` means the readout is not an amplicon this pipeline can
      model. `LMBV_dsDNA_MCP_RPA_Li_2025` says "the chemistry is RPA; the
      penalties are calibrated on PCR" and was reported **Stable, 100.0%** -- a
      false all-clear. `ORTHOPOXVIRUS_dsDNA_ATI_Meyer_1997` says identification
      is by product size plus an XbaI digest, which the screen cannot model, and
      was reported **Declining**. One unenforced flag, a false alarm in one
      direction and a false reassurance in the other.
    - `do_not_use` and the other OPEN questions (`assaywatch.review.OPEN`) are
      things a human still has to answer. `Pan_mycoplasma_16S_All_Van_1992`
      carries `do_not_use` and was reported **Low Coverage, 78.3%**, while
      docs/validation-cases.tsv records van Kuppeveld 1994 finding it working on
      104 cell cultures with no false negatives.

    An assay here keeps its screen -- the calls table is unchanged, and the
    nested, degeneracy and per-lineage tables still use it -- but it gets no
    status, and the withheld status is NOT printed. That follows the convention
    the nested table already set and a test already pins: where the prose
    withholds a figure, the table withholds it too. Printing "would have been
    declining" would simply be the status wearing a caveat.

    Recorded caveats are deliberately NOT here. `orientation_inferred`,
    `oligos_modified`, `amplicon_measured_not_published` and the rest are
    disclosures about perfectly scoreable entries; they go in the note column of
    the row instead, which is what `review_flag_note` is for. Holding them out
    would empty the report: 149 of 208 entries carry at least one.
    """
    if assay is None:
        return ()
    out = [
        (i.flag.value, i.note or "")
        for i in (assay.needs_review or [])
        if i.is_open or i.flag in (ReviewFlag.not_screenable, ReviewFlag.do_not_use)
    ]
    # One flag can be both open and unscoreable (`do_not_use` is), so de-duplicate
    # on the flag while keeping the first note given for it.
    seen: dict[str, str] = {}
    for flag, note in out:
        seen.setdefault(flag, note)
    return tuple(seen.items())


def review_flag_note(assay: Assay | None) -> str:
    """The entry's recorded caveats, for the note column of a scored row.

    24 of the 38 assays called `declining` on 2026-10-22 carried a flag casting
    doubt on the very oligos the claim rests on -- 9 `orientation_inferred`,
    6 `oligos_modified`, 5 `oligos_from_secondary_source`,
    4 `oligos_not_in_cited_paper`, 3 `pairing_is_curator_reading`,
    1 `oligo_source_unresolved` -- and the report showed none of them. The flag
    names are terse on purpose: `assaywatch/review.py` defines each one, and a
    reader who needs the specifics has `source.notes_curator` in the entry.
    """
    if assay is None:
        return ""
    flags = [i.flag.value for i in (assay.needs_review or []) if not i.is_open]
    return f"Entry flags: {', '.join(sorted(flags))}" if flags else ""


@dataclass(frozen=True)
class SpeciesBlock:
    """Per-species detail, for an assay whose product size names the species."""

    lo: int
    hi: int
    recent_from: int | str
    rows: list[tuple[str, int, int, str, str]]


@dataclass(frozen=True)
class DetailRow:
    """The expanded entry for one flagged assay."""

    assay_id: str
    pooled: str
    assay_name: str
    design_year: object
    doi: str
    degeneracy_note: str
    years: list[tuple[int, int, int, str]]
    species: SpeciesBlock | None
    out_of_scope: int
    patent_excluded: int
    clustering_note: str
    unevaluable: dict[str, int]
    exclusions: list[tuple[str, int]]


@dataclass(frozen=True)
class NestedRow:
    """One nested protocol. `containment` is (seen, total) or None."""

    family: str
    outer_share: float | None
    inner_share: float | None
    nested_share: float | None
    nests: bool | None
    records: int
    containment: tuple[int, int] | None
    held_out: bool = False  # one of its rounds is in the Not scoreable table
    # (round-1 failures, of which `diverged`): how much of the loss rests on a label
    # that is reliable for some assays and chance for others. See NestedFamily.
    round1_failed: tuple[int, int] | None = None


@dataclass(frozen=True)
class GapRow:
    assay_id: str
    taxon_name: str
    taxid: object
    evaluable: int
    screened: object


@dataclass(frozen=True)
class ReportModel:
    """Everything both reports say, decided once."""

    run_date: str
    n_assays: int
    counts: list[tuple[str, int]]
    registry_line: str
    confidence_line: str
    freshness_line: str
    window_months: int
    widened: int
    earliest: int | str
    threshold: float
    min_records: int
    sections: list[tuple[str, list[StatusRow]]]
    triage: Triage
    held_out: list[HeldOutRow]
    duplication: str
    details: list[DetailRow]
    nested_rows: list[NestedRow]
    nested_families: list[NestedFamily]
    nested_threshold: float
    gaps: list[GapRow]
    timing: list[str]


def _terminated(fragment: str) -> str:
    """One note fragment, ending in sentence punctuation. Empty stays empty.

    The note column is assembled from pieces written in four places, and none of
    them can know whether the previous piece ended. `drift.py` ends its verdict
    sentence without a full stop, so the 2026-10-22 report printed "...a
    coverage gap, not drift 20251 out-of-scope records excluded." -- two
    sentences run together at the exact point a reader is being told what was
    left out of the denominator. Terminate each fragment where it is joined
    rather than asking every writer to remember.
    """
    fragment = fragment.strip()
    if fragment and fragment[-1] not in ".!?;:":
        fragment += "."
    return fragment


def _note_for(a: AssayDrift, twins: dict[str, list[str]], assay: Assay | None = None) -> str:
    """The note column: the assay's own note, plus what was held out of it."""
    parts = [a.note]
    if caveats := review_flag_note(assay):
        parts.append(caveats)
    if a.assay_id in twins:
        parts.append(f"Same oligos as {', '.join(twins[a.assay_id])}")
    if a.out_of_scope:
        parts.append(f"{a.out_of_scope} out-of-scope records excluded")
    if a.patent_excluded:
        parts.append(f"{a.patent_excluded} patent records excluded")
    return " ".join(p for p in (_terminated(x) for x in parts) if p)


#: Degeneracy tiers where in-silico detection says little about the assay. README:
#: "an oligo full of N matches everything by construction, so a heavily degenerate
#: assay can never be seen to drift and its `detect` calls approach a tautology."
UNJUDGEABLE_TIERS = ("high", "severe")


@dataclass(frozen=True)
class Triage:
    """The few assays worth opening first, and what was held back from the list."""

    rows: list[StatusRow]
    total_flagged: int
    held_degenerate: int
    held_unconfirmed: int
    shown: int


def triage(rows_by_status: list[tuple[str, list[StatusRow]]], assays: dict[str, Assay], limit: int) -> Triage:
    """Flagged assays ordered by how much a reader can act on them.

    THE PROBLEM. The 2026-10-22 report flagged 93 of 204 assays and ordered each
    section by ascending detected share, so what led the report was whichever
    assay had the lowest number -- which for this registry is a pan-family
    consensus PCR screened against a whole family, every time. A monitor that
    flags 46% of its registry and sorts by severity-of-number gives a reader no
    way in. The audience is stated in README as "a lab with no bioinformatician".

    NO WEIGHTED SCORE. The order is lexicographic over criteria whose direction
    is individually obvious, because a composite score would need weights, and
    numbers set by eye are what `config.yaml`'s own header warns about. In order:

    1. `declining` before `low coverage` -- a measured fall from a level that
       worked is actionable; never having covered a clade is a scope question;
    2. entries with no provenance doubt first -- 24 of the 38 assays called
       declining carried a flag doubting the very oligos the claim rests on, and
       re-reading a paper is a different job from redesigning an assay;
    3. larger shortfall below the threshold first;
    4. more evaluable records first -- same shortfall, more evidence;
    5. assay id, so the list is stable between runs.

    TWO EXCLUSIONS, BOTH THE PROJECT'S OWN CAVEATS, NEITHER A STATUS CHANGE.
    The rows stay in their status tables; they are only kept from LEADING.

    * Degeneracy `high` or `severe`: detection is near-tautological there, and
      degeneracy is "reported alongside the drift numbers rather than folded
      into them" (README). Folding it into a verdict would break that; keeping
      such an assay off the front page does not.
    * A flag the duplication check did not confirm: `_cluster_check` is explicit
      that it "can only withhold the label 'survives'", never flag or clear, so
      it cannot gate a status -- but "this flag held when duplicated records were
      discounted" is exactly what makes a flag worth acting on first.

    Both counts are printed, so a reader can see what was held back and why.
    """
    flagged = [
        (s, r) for s, rows in rows_by_status for r in rows if s.lower() in ("declining", "low coverage")
    ]
    degenerate = sum(1 for _, r in flagged if r.degeneracy and r.degeneracy[1] in UNJUDGEABLE_TIERS)
    unconfirmed = sum(
        1
        for _, r in flagged
        if not (r.degeneracy and r.degeneracy[1] in UNJUDGEABLE_TIERS) and r.duplication != "holds"
    )

    def doubted(assay_id: str) -> bool:
        """Does a flag cast doubt on this entry's OLIGOS? See review.OLIGO_DOUBT.

        Not "does it carry any caveat": that counted
        `amplicon_measured_not_published` as doubt, which is the project's
        preferred practice, and `cross_reactive`, which is a specificity
        disclosure about a correct entry.
        """
        assay = assays.get(assay_id)
        return bool(assay and any(i.flag in OLIGO_DOUBT for i in (assay.needs_review or [])))

    eligible = [
        (s, r)
        for s, r in flagged
        if not (r.degeneracy and r.degeneracy[1] in UNJUDGEABLE_TIERS) and r.duplication == "holds"
    ]
    eligible.sort(
        key=lambda sr: (
            sr[0].lower() != "declining",
            doubted(sr[1].assay_id),
            sr[1].fraction if sr[1].fraction is not None else 1.0,
            -sr[1].evaluable,
            sr[1].assay_id,
        )
    )
    return Triage(
        rows=[r for _, r in eligible[:limit]],
        total_flagged=len(flagged),
        held_degenerate=degenerate,
        held_unconfirmed=unconfirmed,
        shown=min(limit, len(eligible)),
    )


def _duplication_cell(a: AssayDrift) -> str:
    """Whether this assay's flag survived the duplication check, in the row itself.

    The result was computed per assay and printed in two places that a reader
    cannot hold together: one sentence at the top of the report ("33 of 72
    flagged assays still hold") and a paragraph inside each assay's folded
    detail. So the counts a reader takes away -- "Declining (38)" -- stood alone,
    while 39 of the 72 checked flags had in fact failed the check.

    It is NOT a gate, and this column does not make it one. `_cluster_check`'s
    docstring is explicit that the footprint reduction "is never used to flag or
    to clear anything; it can only withhold the label 'survives' from a flag the
    record-level evidence already raised" -- a sequencing error in a primer site
    is a footprint of its own, so a healthy assay would read as mostly failing.
    Moving these rows out of `Declining` would therefore be the check doing
    something it is documented not to do. Showing the verdict beside the flag is
    the honest version: the flag stands, and the reader can see what it rests on.
    """
    if a.status not in ("declining", "low coverage"):
        return ""
    if a.flag_survives_clustering is None:
        return "unchecked"
    if a.flag_survives_clustering:
        return "holds"
    return "fails: " + ",".join(a.cluster_failures)


def _status_row(a: AssayDrift, assays: dict[str, Assay], twins: dict[str, list[str]], cfg) -> StatusRow:
    assay = assays.get(a.assay_id)
    deg = assay_degeneracy(assay) if assay else None
    return StatusRow(
        assay_id=a.assay_id,
        assay_name=assay.name if assay else "",
        entry=assay.status.value if assay else "-",
        pooled=a.status_pooled if (a.lineage_override and a.status_pooled) else "",
        fraction=a.recent_fraction,
        ci=a.recent_ci if a.recent_evaluable else None,
        evaluable=a.recent_evaluable,
        baseline=(a.baseline_fraction, a.baseline_evaluable) if a.baseline_evaluable else None,
        degeneracy=(deg.total_fold, deg.tier(cfg)) if deg else None,
        duplication=_duplication_cell(a),
        note=_note_for(a, twins, assay),
        drift=a,
    )


def _detail_row(a: AssayDrift, assays: dict[str, Assay], cfg, taxonomy) -> DetailRow:
    assay = assays.get(a.assay_id)
    deg = assay_degeneracy(assay) if assay else None
    species = None
    if assay and assay.amplicon_bp_range and a.species_counts:
        lo, hi = assay.amplicon_bp_range
        species = SpeciesBlock(lo, hi, a.recent_from, species_table_rows(a, taxonomy, assay.species_sizes))
    return DetailRow(
        assay_id=a.assay_id,
        pooled=a.status_pooled if (a.lineage_override and a.status_pooled) else "",
        assay_name=assay.name if assay else "",
        design_year=(assay.citation.design_year or "?") if assay and assay.citation.doi else None,
        doi=assay.citation.doi if assay and assay.citation.doi else "",
        degeneracy_note=(deg.note(cfg) or "") if deg else "",
        years=year_table_rows(a),
        species=species,
        out_of_scope=a.out_of_scope,
        patent_excluded=a.patent_excluded,
        clustering_note=a.clustering_note,
        unevaluable=a.unevaluable(),
        exclusions=a.exclusions.most_common() if a.exclusions else [],
    )


def _nested_row(f: NestedFamily, held_ids: frozenset[str] = frozenset()) -> NestedRow:
    """One nested protocol's row.

    `held_out` is why this takes the held-out set at all. A round whose entry
    carries an open question or an unmodellable readout gets no status above, and
    then its per-round shares appeared here with nothing said:
    `LYSSAVIRUSES_ssRNA_Nucleoprotein_gene` is `not_validated` and led this table
    at "32% / 100% / 32%". These shares are coverage measurements rather than
    verdicts, which is why they are still computed -- but a number a reader will
    act on must carry the same warning the status did.
    """
    c = f.containment.get((f.outer, f.inner))
    return NestedRow(
        family=f.family,
        outer_share=f.outer_share,
        inner_share=f.inner_share,
        nested_share=f.nested_share,
        nests=f.nests,
        records=f.records,
        containment=c if (c and c[1]) else None,
        held_out=bool({f.outer, f.inner} & held_ids),
        round1_failed=(f.records - f.outer_detected, f.outer_diverged) if f.records else None,
    )


def nested_sort_key(f: NestedFamily):
    """Largest coverage loss first, families with no computable gap last."""
    return (f.gap is None, -(f.gap or 0))


def build_model(
    drifts: dict[str, AssayDrift],
    assays: dict[str, Assay],
    gaps: list[dict[str, Any]],
    run_date: str,
    cfg: dict[str, Any] | None = None,
    nested: dict[str, NestedFamily] | None = None,
    taxonomy: Taxonomy | None = None,
    results_dir: Path | None = None,
) -> ReportModel:
    """Decide what the report says. Neither serialiser decides anything else."""
    # Assays the registry says cannot be scored leave every status table before
    # anything is counted, so the headline counts, the duplication summary and
    # the flagged details are all over scoreable assays only. Their screens are
    # untouched: the nested, degeneracy and per-lineage tables still use them.
    # Keyed on `a.assay_id`, not on the dict key, because that is what every
    # other row builder here looks the assay up by.
    held = {}
    for key, a in drifts.items():
        if why := held_out_reasons(assays.get(a.assay_id)):
            held[key] = (a.assay_id, why)
    held_out = [
        HeldOutRow(
            assay_id=aid,
            assay_name=(assays[aid].name if aid in assays else ""),
            entry=(assays[aid].status.value if aid in assays else "?"),
            reasons=why,
        )
        for aid, why in sorted(held.values())
    ]
    drifts = {key: a for key, a in drifts.items() if key not in held}
    grouped = by_status(drifts)
    twins = oligo_twins(assays)
    drift_cfg = (cfg or {}).get("drift", {})
    window = drift_cfg.get("recent_window_months", 24)
    # The base window comes from the config, not from whichever assay happens
    # to be first: 28 assays widened theirs, and the header claimed Oct 2024
    # for all 141.
    a0 = next(iter(drifts.values()), None)
    flagged = grouped.get("declining", []) + grouped.get("low coverage", [])
    have = [f for f in (nested or {}).values() if f.records]
    # Built once and handed to both the status tables and the triage list, so the
    # two cannot describe the same assay differently.
    sections = [
        (status, [_status_row(a, assays, twins, cfg) for a in grouped[status]])
        for status in status_order(grouped)
        if grouped.get(status)
    ]
    return ReportModel(
        run_date=run_date,
        n_assays=len(drifts),
        counts=[(s, len(grouped[s])) for s in status_order(grouped) if grouped.get(s)],
        registry_line=registry_status_line(drifts, assays),
        confidence_line=flag_confidence_line(grouped),
        freshness_line=freshness_line(results_dir, run_date) if results_dir else "",
        timing=timing_lines(results_dir, run_date) if results_dir else [],
        window_months=window,
        widened=sum(1 for a in drifts.values() if a.window_months > window),
        earliest=a0.recent_from if a0 else 0,
        threshold=a0.threshold if a0 else 0.0,
        min_records=a0.min_records if a0 else 0,
        sections=sections,
        triage=triage(sections, assays, int((cfg or {}).get("report", {}).get("max_triage_rows", 10))),
        held_out=held_out,
        duplication=duplication_summary(flagged),
        details=[_detail_row(a, assays, cfg, taxonomy) for a in flagged],
        nested_rows=[
            _nested_row(f, frozenset(aid for aid, _ in held.values()))
            for f in sorted(have, key=nested_sort_key)
        ],
        nested_families=have,
        nested_threshold=drift_cfg.get("detect_fraction_threshold", 0.9),
        gaps=[
            GapRow(g["assay_id"], g["taxon_name"] or "-", g["taxid"], g["evaluable"], g["screened"])
            for g in gaps
        ],
    )


def render_markdown(
    drifts: dict[str, AssayDrift],
    assays: dict[str, Assay],
    gaps: list[dict[str, Any]],
    run_date: str,
    cfg: dict[str, Any] | None = None,
    nested: dict[str, NestedFamily] | None = None,
    taxonomy: Taxonomy | None = None,
    results_dir: Path | None = None,
) -> str:
    """Markdown, so the report reads on GitHub with nothing built."""
    model = build_model(drifts, assays, gaps, run_date, cfg, nested, taxonomy, results_dir)
    return markdown_from(model, assays, cfg)


def _md_cells(r: StatusRow) -> tuple[str, str, str, str]:
    """A status row's four formatted numbers: share, interval, baseline, degeneracy."""
    frac = f"{r.fraction:.1%}" if r.fraction is not None else "-"
    ci = f"{pct(r.ci[0])}-{pct(r.ci[1])}" if r.ci else "-"
    base = f"{pct(r.baseline[0])} ({r.baseline[1]})" if r.baseline else "-"
    deg = f"{r.degeneracy[0]}x {r.degeneracy[1]}" if r.degeneracy else "-"
    return frac, ci, base, deg


def markdown_from(m: ReportModel, assays: dict[str, Assay], cfg: dict[str, Any] | None = None) -> str:
    out = [f"# AssayWatch report — {m.run_date}", ""]
    counts = ", ".join(f"{n} {s}" for s, n in m.counts)
    held = (
        f" {len(m.held_out)} further screened assays are not scoreable and carry no status."
        if m.held_out
        else ""
    )
    out += [f"{m.n_assays} assays screened: {counts}.{held}", ""]
    if m.registry_line:
        out += [m.registry_line, ""]
    if m.confidence_line:
        out += [m.confidence_line, ""]
    if m.freshness_line:
        out += [m.freshness_line, ""]
    if m.n_assays:
        out += [
            f"Recent window: {m.window_months} months"
            + (f", widened for {m.widened} assays that held too few records" if m.widened else "")
            + f"; earliest shown {m.earliest}; "
            f"threshold {m.threshold:.0%} detected; at least {m.min_records} recent evaluable "
            "records to flag. Deprecated assays are not screened.",
            "",
        ]
    if m.triage.total_flagged:
        tr = m.triage
        out += [f"## Start here ({tr.shown})", ""]
        if tr.rows:
            out += [
                f"Of {tr.total_flagged} flagged assays, these are ordered by how much can be acted",
                "on: a measured fall before a scope gap, entries whose oligo provenance is not in",
                "doubt first, then the largest shortfall below the threshold on the most records.",
                "",
                "| assay | status | detected (recent) | 95% CI | evaluable | baseline (n) |",
                "|---|---|---|---|---|---|",
            ]
            status_of = {r.assay_id: s for s, rows in m.sections for r in rows}
            for r in tr.rows:
                frac, ci, base, _ = _md_cells(r)
                out.append(
                    f"| `{md(r.assay_id)}` | {status_of.get(r.assay_id, '')} | {frac} | {ci} "
                    f"| {r.evaluable} | {base} |"
                )
            out.append("")
        else:
            out += ["No flagged assay met the bar for this list.", ""]
        withheld = []
        if tr.held_degenerate:
            withheld.append(
                f"{tr.held_degenerate} are degeneracy high or severe, where in-silico detection is "
                "close to a tautology"
            )
        if tr.held_unconfirmed:
            withheld.append(f"{tr.held_unconfirmed} carry a flag the duplication check did not confirm")
        if withheld:
            out += [
                "Kept off this list but unchanged in the tables below: " + "; ".join(withheld) + ".",
                "",
            ]

    out += [
        "`detected` means predicted to amplify (`detect` or `reduced`). The denominator is",
        "evaluable records only: those where both primers landed in the right orientation and",
        "size range. Records with no amplicon, or too many undetermined bases to judge, are",
        "counted separately and excluded, so a bad sequencing year cannot look like drift.",
        "Intervals are Wilson 95%, pooled and per lineage alike. A **pooled** flag needs the",
        "upper bound of the recent interval to fall below the threshold. **Declining** means the",
        "share has also fallen from the baseline (the interval for the change excludes zero):",
        "that is drift. **Low coverage** means below threshold without a measurable fall: usually",
        "an assay screened against more diversity than it was designed for.",
        "",
        "A **lineage** can also flag an assay whose pooled share clears the threshold, and that",
        "is the point of measuring per lineage: a pan-family assay can miss one clade entirely",
        "while detecting most of what is deposited. Such a row is marked `pooled: <status>` and",
        "its note names the lineage, its share and its own earlier share. The lineage rule is",
        "not the pooled one: it is an exact binomial test against the threshold, Benjamini-",
        "Hochberg-adjusted across that assay's lineages, so it is the looser of the two and",
        "nothing controls error across assays. Read a lineage override as a reason to look at",
        "that clade, not as a measurement of the assay.",
        "",
    ]

    for status, rows in m.sections:
        out += [f"## {status.title()} ({len(rows)})", ""]
        out += [
            "| assay | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy "
            "| duplication | note |",
            "|---|---|---|---|---|---|---|---|---|",
        ]
        for r in rows:
            frac, ci, base, deg = _md_cells(r)
            pooled_tag = f" (pooled: {r.pooled})" if r.pooled else ""
            out.append(
                f"| `{md(r.assay_id)}`{pooled_tag} | {r.entry} | {frac} | {ci} | {r.evaluable} | {base} "
                f"| {deg} | {r.duplication or '-'} | {md(r.note)} |"
            )
        out.append("")

    if m.held_out:
        out += [
            f"## Not scoreable ({len(m.held_out)})",
            "",
            "These assays were screened, and their records still count in the nested,",
            "degeneracy and per-lineage tables, but their entry carries a review item that",
            "means a status would not be a statement about the assay: either an open question",
            "a human has to answer, or a readout this pipeline cannot model. No status is shown",
            "for them, including the one they would otherwise have had.",
            "",
            "| assay | entry | why | note |",
            "|---|---|---|---|",
        ]
        for h in m.held_out:
            for i, (flag, note) in enumerate(h.reasons):
                aid = f"`{md(h.assay_id)}`" if i == 0 else ""
                out.append(f"| {aid} | {h.entry if i == 0 else ''} | `{flag}` | {md(note)} |")
        out.append("")

    if m.details:
        out += ["## Detail for flagged assays", ""]
        if m.duplication:
            out += [f"**Duplication check:** {m.duplication}", ""]
        for d in m.details:
            out += [f"### `{d.assay_id}`", ""]
            if d.pooled:
                out.append(f"**Lineage override:** pooled status was {d.pooled}.  ")
            if d.assay_name:
                out.append(f"{d.assay_name}  ")
            if d.doi:
                out.append(f"Designed {d.design_year}, doi:{d.doi}  ")
            if d.degeneracy_note:
                out.append(f"**Degeneracy:** {d.degeneracy_note}  ")
            out += ["", "| deposit year | detected | evaluable | share |", "|---|---|---|---|"]
            for year, det, ev, frac in d.years:
                out.append(f"| {year} | {det} | {ev} | {frac} |")
            if d.species:
                sp = d.species
                out += [
                    "",
                    f"**Per species** (product size names the species here, {sp.lo}-{sp.hi} bp, so the "
                    f"share above pools readouts that mean different things; {sp.recent_from} on, no "
                    "assessability floor):",
                    "",
                    "| species | product bp | detected | evaluable | share |",
                    "|---|---|---|---|---|",
                ]
                for label, det, ev, frac, band in sp.rows:
                    out.append(f"| {md(label)} | {band} | {det} | {ev} | {frac} |")
            if d.out_of_scope:
                out += [
                    "",
                    f"**Out of scope:** {d.out_of_scope} records excluded (taxid not in scope_taxids).",
                ]
            if d.patent_excluded:
                out += [
                    "",
                    f"**Patent records:** {d.patent_excluded} excluded "
                    "(GenBank patent division; drift.exclude_patent_records).",
                ]
            if d.clustering_note:
                out += ["", f"**Duplication check:** {d.clustering_note}"]
            if d.unevaluable:
                out.append("")
                out.append("Excluded: " + ", ".join(f"{n} {k}" for k, n in sorted(d.unevaluable.items())))
                # Markdown only: the HTML report prints the excluded counts but not
                # this breakdown. A content difference, not an oversight of layout.
                if d.exclusions:
                    out.append("")
                    out.append(
                        "Why: "
                        + ", ".join(f"{n} {k}" for k, n in d.exclusions)
                        + ". `truncated` means the deposit stops before the other primer's site, so it"
                        + " says nothing about the assay; `diverged` means that site is present and does"
                        + " not match."
                    )
            out.append("")

    if m.nested_families:
        # `nested_section` returns [] when no family has records, so passing only
        # the families that do is the same output the `nested is not None` check gave.
        out += nested_section(
            {f.family: f for f in m.nested_families}, assays, m.nested_threshold, m.nested_rows
        )

    out += ["## Coverage gaps", ""]
    if not m.gaps:
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
        for g in m.gaps:
            out.append(
                f"| `{md(g.assay_id)}` | {md(g.taxon_name)} | {g.taxid or '-'} "
                f"| {g.evaluable} | {g.screened if g.taxid else 'not searched (no taxid)'} |"
            )
        out.append("")
    # Last, because it is about the run rather than the assays.
    out += m.timing
    return "\n".join(out)


CSS = """
:root { --fg:#1b1b1b; --muted:#5f6368; --line:#e3e3e3; }
body { font: 15px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
       color: var(--fg); max-width: 1100px; margin: 2rem auto; padding: 0 1rem; }
h1 { margin-bottom: .2rem; }
h2 { margin-top: 2rem; border-bottom: 1px solid var(--line); padding-bottom: .3rem; }
/* Figures are written at a fixed point size so they stay valid SVG files for
   any rasteriser; the page is what makes them fit a narrow window. */
figure { margin: 1.2rem 0; }
figure svg { max-width: 100%; height: auto; }
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
    taxonomy: Taxonomy | None = None,
    results_dir: Path | None = None,
    figures: dict[str, str] | None = None,
) -> str:
    """One self-contained file: no CDN, inline SVG charts, opens anywhere."""
    model = build_model(drifts, assays, gaps, run_date, cfg, nested, taxonomy, results_dir)
    return html_from(model, figures)


def _html_cells(r: StatusRow) -> tuple[str, str, str, str]:
    """The same four numbers `_md_cells` formats, with HTML entities."""
    frac = f"{r.fraction:.1%}" if r.fraction is not None else "-"
    ci = f"{pct(r.ci[0])}&ndash;{pct(r.ci[1])}" if r.ci else "-"
    base = f"{pct(r.baseline[0])} ({r.baseline[1]})" if r.baseline else "-"
    deg = f"{r.degeneracy[0]}&times; {r.degeneracy[1]}" if r.degeneracy else "-"
    return frac, ci, base, deg


def _assay_cell(assay_id: str, has_detail: set[str]) -> str:
    """An assay id, linked to its detail block when it has one."""
    code = f"<code>{html.escape(assay_id)}</code>"
    return f"<a href='#detail-{_slug(assay_id)}'>{code}</a>" if assay_id in has_detail else code


def _slug(text: str) -> str:
    """A fragment id from a heading or an assay id. Stable between runs."""
    return "".join(c if c.isalnum() else "-" for c in text.lower()).strip("-")


def _timing_html(lines: list[str]) -> str:
    """Render the timing footer's markdown lines as HTML.

    `timing_lines` is written once, in markdown, because both renderers want the
    same words; this turns its two shapes - a heading and a pipe table - into
    HTML rather than duplicating the text. Everything is escaped except the
    backticks, which become <code>.
    """
    e = html.escape
    out, rows = [], []

    def flush() -> None:
        if not rows:
            return
        head, body = rows[0], rows[2:]
        cells = "".join(f"<th>{e(c)}</th>" for c in head)
        out.append(f"<table><tr>{cells}</tr>")
        for r in body:
            out.append("<tr>" + "".join(f"<td>{_md_code(c)}</td>" for c in r) + "</tr>")
        out.append("</table>")
        rows.clear()

    for line in lines:
        if line.startswith("|"):
            rows.append([c.strip() for c in line.strip("|").split("|")])
            continue
        flush()
        if line.startswith("## "):
            out.append(f"<h2 id='timing'>{e(line[3:])}</h2>")
        elif line:
            out.append(f"<p class='muted'>{_md_code(line)}</p>")
    flush()
    return "\n".join(out)


def _md_code(text: str) -> str:
    """Escape `text`, then turn its `backticked` spans into <code>."""
    parts = html.escape(text).split("`")
    return "".join(p if i % 2 == 0 else f"<code>{p}</code>" for i, p in enumerate(parts))


def html_from(m: ReportModel, figures: dict[str, str] | None = None) -> str:
    e = html.escape
    parts = [
        "<!doctype html><html lang='en'><head><meta charset='utf-8'>",
        "<meta name='viewport' content='width=device-width, initial-scale=1'>",
        f"<title>AssayWatch — {e(m.run_date)}</title><style>{CSS}</style></head><body>",
        f"<h1>AssayWatch report</h1><p class='muted'>{e(m.run_date)}</p>",
        f"<p class='lead'>{e(m.registry_line)}</p>",
        (f"<p class='muted'>{e(m.freshness_line)}</p>" if m.freshness_line else ""),
        "<p class='lead'>Detected means predicted to amplify. The denominator is evaluable "
        "records only: both primers landed in the right orientation and size range. Records "
        "with no amplicon, or too many undetermined bases to judge, are excluded and counted "
        "separately. Intervals are Wilson 95%, pooled and per lineage alike. A pooled flag "
        "needs the upper bound of the recent interval to fall below the threshold. Declining "
        "means the share has also fallen from the baseline (that is drift); low coverage means "
        "below threshold without a measurable fall.</p>",
        "<p class='lead'>A lineage can also flag an assay whose pooled share clears the "
        "threshold \u2014 that is the point of measuring per lineage. Such a row is marked "
        "with its pooled status and its note names the lineage, its share and its own earlier "
        "share. The lineage rule is an exact binomial test against the threshold, "
        "Benjamini-Hochberg-adjusted within the assay, so it is looser than the pooled rule, "
        "and nothing controls error across assays: read an override as a reason to look at that "
        "clade rather than as a measurement of the assay.</p>",
    ]
    # Gated on the confidence line but printing the duplication summary. Kept as
    # it was: changing which of the two appears here changes the published page.
    if m.confidence_line:
        parts.append(f"<p class='lead'><b>Duplication check:</b> {e(m.duplication)}</p>")
    if figures and figures.get("forest.svg"):
        parts.append(
            "<h2 id='figures'>Detection against threshold</h2>"
            "<p class='lead'>Every assay with an evaluable recent window, worst first. Left: where the "
            "recent detected share sits against the threshold. Right: how far it has moved from "
            "baseline. A flag rests on the two together, so the tables below are this figure read "
            "row by row.</p>"
            f"<figure>{figures['forest.svg']}</figure>"
        )
    # Which assays have a detail block, so a row only links where there is
    # somewhere to land.
    has_detail = {d.assay_id for d in m.details}

    # A contents list, because the page has ten sections, 91 tables and no way to
    # get to one. Anchors and links only: a <details> whose fragment is targeted
    # is opened by the browser, so a reader can be sent straight to one assay's
    # year table without any script running.
    toc = [("start-here", f"Start here ({m.triage.shown})")] if m.triage.total_flagged else []
    toc += [(_slug(s), f"{s.title()} ({len(rows)})") for s, rows in m.sections]
    if m.held_out:
        toc.append(("not-scoreable", f"Not scoreable ({len(m.held_out)})"))
    if m.details:
        toc.append(("detail", "Detail for flagged assays"))
    if m.nested_rows:
        toc.append(("nested", "Nested protocols"))
    toc.append(("coverage-gaps", "Coverage gaps"))
    parts.append(
        "<p class='lead'>" + " &middot; ".join(f"<a href='#{i}'>{e(label)}</a>" for i, label in toc) + "</p>"
    )

    if m.triage.total_flagged:
        tr = m.triage
        parts.append(f"<h2 id='start-here'>Start here <span class='muted'>{tr.shown}</span></h2>")
        if tr.rows:
            parts.append(
                f"<p class='lead'>Of {tr.total_flagged} flagged assays, these are ordered by how "
                "much can be acted on: a measured fall before a scope gap, entries whose oligo "
                "provenance is not in doubt first, then the largest shortfall below the threshold "
                "on the most records.</p>"
            )
            parts.append(
                "<table><tr><th>assay</th><th>status</th><th>detected</th><th>95% CI</th>"
                "<th>evaluable</th><th>baseline (n)</th></tr>"
            )
            status_of = {r.assay_id: s for s, rows in m.sections for r in rows}
            for r in tr.rows:
                frac, ci, base, _ = _html_cells(r)
                parts.append(
                    f"<tr><td>{_assay_cell(r.assay_id, has_detail)}<br><span class='muted'>"
                    f"{e(r.assay_name)}</span></td><td>{e(status_of.get(r.assay_id, ''))}</td>"
                    f"<td>{frac}</td><td>{ci}</td><td>{r.evaluable}</td><td>{base}</td></tr>"
                )
            parts.append("</table>")
        else:
            parts.append("<p class='lead'>No flagged assay met the bar for this list.</p>")
        withheld = []
        if tr.held_degenerate:
            withheld.append(
                f"{tr.held_degenerate} are degeneracy high or severe, where in-silico detection "
                "is close to a tautology"
            )
        if tr.held_unconfirmed:
            withheld.append(f"{tr.held_unconfirmed} carry a flag the duplication check did not confirm")
        if withheld:
            parts.append(
                "<p class='muted'>Kept off this list but unchanged in the tables below: "
                + e("; ".join(withheld))
                + ".</p>"
            )

    for status, rows in m.sections:
        colour = STATUS_COLOUR.get(status, DEFAULT_COLOUR)
        parts.append(
            f"<h2 id='{_slug(status)}'><span class='pill' style='background:{colour}'>"
            f"{e(status)}</span> {len(rows)}</h2>"
        )
        parts.append(
            "<table><tr><th>assay</th><th>entry</th><th>trend</th><th>detected</th><th>95% CI</th>"
            "<th>evaluable</th><th>baseline (n)</th><th>degeneracy</th><th>duplication</th>"
            "<th>note</th></tr>"
        )
        for r in rows:
            frac, ci, base, deg = _html_cells(r)
            pooled_html = (
                f"<br><span class='muted' style='font-size:.8rem'>pooled: {e(r.pooled)}</span>"
                if r.pooled
                else ""
            )
            parts.append(
                f"<tr><td>{_assay_cell(r.assay_id, has_detail)}<br><span class='muted'>"
                f"{e(r.assay_name)}</span>{pooled_html}</td>"
                f"<td>{e(r.entry)}</td>"
                f"<td>{sparkline(r.drift)}</td><td>{frac}</td><td>{ci}</td>"
                f"<td>{r.evaluable}</td><td>{base}</td><td>{deg}</td>"
                f"<td>{e(r.duplication) or '-'}</td>"
                f"<td class='muted'>{e(r.note)}</td></tr>"
            )
        parts.append("</table>")

    if m.held_out:
        parts.append(
            f"<h2 id='not-scoreable'><span class='pill' style='background:{DEFAULT_COLOUR}'>"
            "not scoreable</span> "
            f"{len(m.held_out)}</h2>"
        )
        parts.append(
            "<p class='lead'>Screened, and still counted in the nested, degeneracy and "
            "per-lineage tables, but the entry carries a review item that means a status would "
            "not be a statement about the assay: an open question a human has to answer, or a "
            "readout this pipeline cannot model. No status is shown, including the one the assay "
            "would otherwise have had.</p>"
        )
        parts.append("<table><tr><th>assay</th><th>entry</th><th>why</th><th>note</th></tr>")
        for h in m.held_out:
            for i, (flag, note) in enumerate(h.reasons):
                first = i == 0
                parts.append(
                    "<tr><td>"
                    + (
                        f"<code>{e(h.assay_id)}</code><br><span class='muted'>{e(h.assay_name)}</span>"
                        if first
                        else ""
                    )
                    + f"</td><td>{e(h.entry) if first else ''}</td>"
                    f"<td><code>{e(flag)}</code></td>"
                    f"<td class='muted'>{e(note)}</td></tr>"
                )
        parts.append("</table>")

    # The same per-year detail the markdown report has, folded away by default.
    if m.details:
        parts.append("<h2 id='detail'>Detail for flagged assays</h2>")
        if m.duplication:
            parts.append(f"<p class='lead'><b>Duplication check:</b> {e(m.duplication)}</p>")
        for d in m.details:
            # An id so the tables above can link here. A <details> whose
            # fragment is targeted is opened by the browser, which is why this
            # needs no JavaScript to work.
            parts.append(
                f"<details id='detail-{_slug(d.assay_id)}'><summary><code>{e(d.assay_id)}</code></summary>"
            )
            if d.pooled:
                pooled_colour = STATUS_COLOUR.get(d.pooled, DEFAULT_COLOUR)
                parts.append(
                    f"<p><b>Lineage override:</b> pooled status was "
                    f"<span class='pill' style='background:{pooled_colour}'>{e(d.pooled)}</span></p>"
                )
            if d.assay_name:
                bits = [e(d.assay_name)]
                if d.doi:
                    bits.append(f"designed {d.design_year}, doi:{e(d.doi)}")
                if d.degeneracy_note:
                    bits.append(f"degeneracy: {e(d.degeneracy_note)}")
                parts.append("<p class='muted'>" + "<br>".join(bits) + "</p>")
            parts.append(
                "<table><tr><th>deposit year</th><th>detected</th><th>evaluable</th><th>share</th></tr>"
            )
            for year, det, ev, frac in d.years:
                parts.append(f"<tr><td>{year}</td><td>{det}</td><td>{ev}</td><td>{frac}</td></tr>")
            parts.append("</table>")
            if d.species:
                sp = d.species
                parts.append(
                    f"<p class='muted'><b>Per species</b> (product size names the species here, "
                    f"{sp.lo}-{sp.hi} bp, so the share above pools readouts that mean different things; "
                    f"{e(str(sp.recent_from))} on, no assessability floor):</p>"
                )
                parts.append(
                    "<table><tr><th>species</th><th>product bp</th><th>detected</th>"
                    "<th>evaluable</th><th>share</th></tr>"
                )
                for label, det, ev, frac, band in sp.rows:
                    parts.append(
                        f"<tr><td>{e(label)}</td><td>{e(band)}</td><td>{det}</td>"
                        f"<td>{ev}</td><td>{frac}</td></tr>"
                    )
                parts.append("</table>")
            if d.out_of_scope:
                parts.append(
                    f"<p class='muted'><b>Out of scope:</b> {d.out_of_scope} records excluded"
                    " (taxid not in scope_taxids).</p>"
                )
            if d.patent_excluded:
                parts.append(
                    f"<p class='muted'><b>Patent records:</b> {d.patent_excluded} excluded"
                    " (GenBank patent division; drift.exclude_patent_records).</p>"
                )
            if d.clustering_note:
                parts.append(f"<p class='muted'><b>Duplication check:</b> {e(d.clustering_note)}</p>")
            if d.unevaluable:
                # No `Why:` breakdown here, unlike the markdown report.
                parts.append(
                    "<p class='muted'>Excluded: "
                    + ", ".join(f"{n} {e(k)}" for k, n in sorted(d.unevaluable.items()))
                    + "</p>"
                )
            parts.append("</details>")

    if m.nested_rows:
        parts.append("<h2 id='nested'>Nested protocols</h2>")
        parts.append(
            "<p class='lead'>Rounds are scored separately above, and that stands: either product can "
            "be read on a gel. This adds the share of records <b>both</b> rounds reach — what the "
            "protocol delivers run as published. Round 2's own figure is what it would do as a direct "
            "PCR.</p>"
            "<table><tr><th>protocol</th><th>round 1</th><th>round 2 alone</th><th>run as a nest</th>"
            "<th>records</th><th>inner inside outer</th><th>round 1 failures (diverged)</th></tr>"
        )
        for r in m.nested_rows:
            cont, nested_cell = _nested_cells(r, bold="<b>no</b>")
            parts.append(
                f"<tr><td><code>{e(r.family)}</code>"
                + (
                    "<br><span class='muted' style='font-size:.8rem'>not scoreable</span>"
                    if r.held_out
                    else ""
                )
                + f"</td><td>{pct(r.outer_share)}</td>"
                f"<td>{pct(r.inner_share)}</td><td>{nested_cell}</td>"
                f"<td>{r.records:,}</td><td>{cont}</td><td>{_round1_cell(r)}</td></tr>"
            )
        parts.append("</table>")
        # Ordered by gap only, where the markdown section lists the non-nesting
        # families first and then the warned ones. Another content difference.
        for f in sorted(m.nested_families, key=lambda f: -(f.gap or 0)):
            if f.nests is False or f.warns(m.nested_threshold):
                note = e(f.note(m.nested_threshold))
                parts.append(f"<p class='muted'><b><code>{e(f.family)}</code></b> — {note}</p>")

    parts.append("<h2 id='coverage-gaps'>Coverage gaps</h2>")
    if not m.gaps:
        parts.append("<p class='muted'>Every assay has enough evaluable records to say something.</p>")
    else:
        parts.append(
            "<p class='lead'>These assays cannot be validated against sequence data because the "
            "sequence data does not exist. For wildlife pathogens this is usually the finding. An assay "
            "with no taxid was never searched: that is a registry gap, not a data gap.</p>"
            "<table><tr><th>assay</th><th>taxon</th><th>taxid</th><th>evaluable</th><th>screened</th></tr>"
        )
        for g in m.gaps:
            parts.append(
                f"<tr><td><code>{e(g.assay_id)}</code></td><td>{e(str(g.taxon_name))}</td>"
                f"<td>{g.taxid or '-'}</td><td>{g.evaluable}</td>"
                f"<td>{g.screened if g.taxid else 'not searched (no taxid)'}</td></tr>"
            )
        parts.append("</table>")
    if figures and figures.get("site-positions.svg"):
        parts.append(
            "<h2 id='penalty'>Detection penalty per position</h2>"
            "<p class='lead'>For the flagged assays, how much detection falls when a record "
            "mismatches at each oligo position - the cost of the mismatch, not how often it "
            "happens. The shaded band is the 3'-terminal zone, where a mismatch blocks extension "
            "rather than shifting Tm; an amber base is already degenerate. Full numbers, and the "
            "accession groups behind them, are in <code>site-drift.md</code>.</p>"
            f"<figure>{figures['site-positions.svg']}</figure>"
        )
    if m.timing:
        parts.append(_timing_html(m.timing))
    parts.append("</body></html>")
    return "\n".join(parts)


def read_figures(figures_dir: Path | None) -> dict[str, str]:
    """{filename: SVG} from a figures directory, or {} when there is none.

    Missing figures are not an error: `python -m assaywatch.report` is run by
    hand without them, and the tests render the page with no figure directory
    at all. The pipeline supplies the directory; the page is complete either way.
    """
    if figures_dir is None or not figures_dir.is_dir():
        return {}
    return {p.name: p.read_text() for p in sorted(figures_dir.glob("*.svg"))}


def assess_as_reported(
    calls: list[dict[str, Any]],
    dates: dict[str, Any],
    assays: dict[str, Assay],
    retrieved: Path,
    cfg: dict[str, Any],
    today: date | None,
) -> tuple[dict[str, AssayDrift], Taxonomy | None]:
    """Every assay's status, assessed exactly as report.md assesses it.

    Split out of `build` because a second document needs the same answer.
    sitedrift.py claimed its statuses "come from the same assessment the main
    report uses, so the two documents cannot disagree", but it called `assess`
    with the calls, the dates and the config and nothing else: no taxids, so no
    lineage check; no scope map, so no scope filter; and, until it crashed on
    it, no patent set. On the frozen 2026-10-22 table site-drift.md covered 87
    assays against the report's 74 flagged -- 17 the report did not flag and 4
    lineage overrides it missed. One function, two callers, and the claim is
    true by construction.

    Returns the taxonomy too, which `build` needs for rendering.
    """
    # Load taxid data for per-lineage analysis (phase 2).
    taxid_map: dict[str, int] | None = None
    taxa_cache_data: dict[int, str] | None = None
    lineage_cfg = cfg.get("lineage", {})
    taxa_cache_path = lineage_cfg.get("taxa_cache")
    if taxa_cache_path:
        from assaywatch.lineage import load_taxa_cache

        taxa_cache_data = load_taxa_cache(taxa_cache_path)
        # Build accession -> taxid from the backfill sidecar + archive metadata.
        taxid_map = {}
        # `lineage.taxid_backfill` was declared in config.yaml and read nowhere,
        # while this path and lineage_report.py's copy were hardcoded - a setting
        # that looked configurable and was not. The config value wins; the literal
        # stays as the default so an older config still resolves the same file.
        sidecar_path = Path(lineage_cfg.get("taxid_backfill") or retrieved / ".meta.taxid.backfill.tsv.gz")
        if sidecar_path.exists():
            with gzip.open(sidecar_path, "rt") as f:
                next(f, None)  # skip header
                for line in f:
                    acc, _, tx = line.rstrip("\n").partition("\t")
                    if tx.isdigit():
                        taxid_map[strip_version(acc)] = int(tx)
        for meta_path in sorted(retrieved.rglob("*.meta.tsv.gz")):
            with gzip.open(meta_path, "rt") as f:
                hdr = (f.readline() or "").rstrip("\n").split("\t")
                if "taxid" not in hdr or "accession" not in hdr:
                    continue
                ai, ti = hdr.index("accession"), hdr.index("taxid")
                for line in f:
                    parts = line.rstrip("\n").split("\t")
                    if len(parts) > max(ai, ti) and parts[ti].isdigit():
                        taxid_map[strip_version(parts[ai])] = int(parts[ti])
        if not taxid_map:
            taxid_map = None
            taxa_cache_data = None

    # Build scope map from registry: assay_id → set of in-scope taxids.
    scope_map: dict[str, set[int]] | None = None
    for aid, assay in assays.items():
        if assay.target.scope_taxids:
            if scope_map is None:
                scope_map = {}
            scope_map[aid] = set(assay.target.scope_taxids)

    # Sub-lineage resolver chains (lineage.sublineage), and titles for the
    # assays whose chain parses them. Empty config: both stay None.
    resolvers = titles = None
    if taxid_map is not None and lineage_cfg.get("sublineage"):
        from assaywatch.lineage import sublineage_resolvers, title_assays
        from assaywatch.metadata import read_titles

        resolvers = sublineage_resolvers(lineage_cfg, {aid: a.target.taxid for aid, a in assays.items()})
        wanted = title_assays(lineage_cfg)
        titles = read_titles(
            retrieved, {strip_version(r["record_id"]) for r in calls if r["assay_id"] in wanted}
        )

    # The tree does three jobs now — scope ancestry, the species roll-up in
    # lineage grouping, and species names for the per-species table — so it is
    # loaded whenever drift.scope_taxonomy names it, not only when an assay
    # declares a scope. Unset, taxonomy_from_config returns None.
    from assaywatch.taxonomy import taxonomy_from_config

    taxonomy = taxonomy_from_config(cfg)
    if taxa_cache_data is not None:
        from assaywatch.lineage import name_lineages_from_taxonomy

        taxa_cache_data = name_lineages_from_taxonomy(taxa_cache_data, taxonomy)

    # Patent-division records, only when the option that acts on them is on.
    patent = None
    if (cfg.get("drift") or {}).get("exclude_patent_records"):
        from assaywatch.metadata import read_patent_accessions

        patent = read_patent_accessions(retrieved, {strip_version(r["record_id"]) for r in calls})

    drifts = assess(
        calls,
        dates,
        cfg,
        today=today,
        taxids=taxid_map,
        taxa_cache=taxa_cache_data,
        scope_map=scope_map,
        resolvers=resolvers,
        titles=titles,
        taxonomy=taxonomy,
        patent=patent,
    )
    return drifts, taxonomy


def build(
    calls_path: Path,
    registry: Path,
    retrieved: Path,
    cfg: dict[str, Any],
    run_date: str | None = None,
    today: date | None = None,
    figures_dir: Path | None = None,
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

    rounds = {i for v in families(assays).values() for i in v}
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
    drifts, taxonomy = assess_as_reported(calls, dates, assays, retrieved, cfg, today)
    if taxonomy is not None and taxonomy.unknown:
        print(
            f"warning: {len(taxonomy.unknown)} taxids not in the taxonomy cache were matched exactly; "
            "rebuild it with scripts/build_taxonomy_cache.py",
            file=sys.stderr,
        )
    gaps = coverage_gaps(drifts, taxa, cfg)
    # Nested families are read from the SAME deduplicated calls the drift
    # statistic uses, so the two never disagree about which records exist.
    nested = assess_nested(assays, calls)
    # The run directories live beside this one, which is where the previous run's
    # run-timing.json is, so the freshness line reads from the calls path rather
    # than needing the config's results_dir threaded in.
    results_dir = calls_path.parent.parent
    return (
        render_markdown(drifts, assays, gaps, run_date, cfg, nested, taxonomy, results_dir),
        # Keyword arguments: `results_dir` was added before `figures` in the
        # signature, and a positional call silently handed the figures dict to it.
        render_html(
            drifts,
            assays,
            gaps,
            run_date,
            cfg,
            nested,
            taxonomy,
            results_dir=results_dir,
            figures=read_figures(figures_dir),
        ),
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
    ap.add_argument(
        "--figures",
        type=Path,
        default=None,
        help="directory of SVGs from assaywatch.figures to inline into the HTML",
    )
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    md, page, drifts = build(
        args.calls, args.registry, args.retrieved, cfg, run_date=args.run_date, figures_dir=args.figures
    )
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
