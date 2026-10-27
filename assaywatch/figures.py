"""Figures for the drift report.

Two plots, each answering a question the tables answer only by arithmetic the
reader has to do themselves.

`forest` puts every assay on one axis against the detection threshold, with the
Wilson interval for the recent window beside the Newcombe interval for the change
from baseline. The verdict logic becomes something you read off the page: an
interval clear of the threshold line is stable, one straddling it is watch, one
below it with a change interval clear of `min_decline` is declining.

`site_positions` plots the detection penalty per oligo position, 5' to 3', with
the base letters on the axis and the 3'-terminal zone shaded. This is the figure
a bench decision comes from: it names the position to degenerate or redesign,
which `site-drift.tsv` holds but does not show.

Both read their numbers from `report.build` and `sitedrift.build` rather than
recomputing anything, so a figure cannot disagree with the document beside it.
Thresholds are read off the assessment (which reads `config.yaml`); none are
written here.
"""

from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Any

import matplotlib

# A compute node has no display, so the backend is chosen before pyplot is
# imported and tries to find one. Must stay above the pyplot import.
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

from assaywatch import atomic
from assaywatch.drift import newcombe_difference
from assaywatch.report import DEFAULT_COLOUR, STATUS_COLOUR, STATUS_ORDER

if TYPE_CHECKING:
    from assaywatch.drift import AssayDrift
    from assaywatch.sitedrift import AssaySites

# Oligos in the order a protocol lists them, not alphabetically.
OLIGO_ORDER = ("forward", "reverse", "probe")

# Deterministic output: the same calls table gives a byte-identical SVG, so a
# figure committed or diffed only changes when the numbers do.
matplotlib.rcParams["svg.hashsalt"] = "assaywatch"
matplotlib.rcParams["svg.fonttype"] = "path"
matplotlib.rcParams["font.size"] = 8


def _svg(fig: plt.Figure) -> str:
    """Render a figure to inline-ready SVG: no XML declaration, no DOCTYPE, no date."""
    buf = io.StringIO()
    fig.savefig(buf, format="svg", bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    out = buf.getvalue()
    start = out.find("<svg")
    # The root tag is left exactly as matplotlib writes it: width and height in
    # points beside a viewBox. An inline `style="max-width:100%"` makes the file
    # responsive in a browser but renders blank in cairosvg and other non-browser
    # rasterisers, and these are pipeline outputs that get converted. Pages that
    # embed the figure constrain it with their own CSS instead.
    return out[start:] if start > 0 else out


def _empty(message: str, width: float = 7.0) -> str:
    """A valid figure saying there is nothing to plot.

    A run with no evaluable records still has to produce its declared outputs,
    and an empty file is not a valid SVG.
    """
    fig, ax = plt.subplots(figsize=(width, 1.2))
    ax.text(0.5, 0.5, message, ha="center", va="center", color=DEFAULT_COLOUR)
    ax.set_axis_off()
    return _svg(fig)


def _share(detected: int, evaluable: int) -> float | None:
    return detected / evaluable if evaluable else None


def forest_rows(drifts: dict[str, AssayDrift], limit: int = 0) -> list[AssayDrift]:
    """Assays with a recent window to show, worst first.

    Ordered by status (the report's own order, declining first) and then by
    recent detected share ascending, so the assays a reader is looking for are
    at the top and the eye travels down to the ones that are fine. `limit` caps
    the rows for legibility; the cut keeps the worst.
    """
    rank = {s: i for i, s in enumerate(STATUS_ORDER)}
    rows = [d for d in drifts.values() if d.recent_evaluable]
    rows.sort(
        key=lambda d: (
            rank.get(d.status, len(rank)),
            _share(d.recent_detected, d.recent_evaluable) or 0.0,
            d.assay_id,
        )
    )
    return rows[:limit] if limit else rows


def forest(drifts: dict[str, AssayDrift], limit: int = 40) -> str:
    """Recent detected share and change from baseline, one row per assay.

    Two panels sharing the assay axis because the verdict rests on two
    quantities and one axis cannot carry both: where the assay sits now
    (against `threshold`) and whether it has moved (against `min_decline`).
    Where footprint clustering widens the change interval, the clustered
    interval is drawn behind the unclustered one, so pseudoreplication is
    visible rather than described in a footnote.
    """
    rows = forest_rows(drifts, limit)
    if not rows:
        return _empty("no assay has an evaluable recent window")

    # The footer is reserved in inches rather than as a figure fraction: the
    # figure grows with the number of rows, and a fraction that suits ten assays
    # puts the legend through the axis labels at forty.
    footer_in, title_in = 0.90, 0.42
    height = max(2.0, 0.26 * len(rows)) + footer_in + title_in
    fig, (ax_now, ax_chg) = plt.subplots(
        1, 2, figsize=(9.5, height), sharey=True, gridspec_kw={"width_ratios": [1.0, 1.0], "wspace": 0.08}
    )
    fig.subplots_adjust(bottom=footer_in / height, top=1 - title_in / height)
    y = range(len(rows))

    thresholds = {d.threshold for d in rows}
    min_declines = {d.min_decline for d in rows}

    for i, d in enumerate(rows):
        colour = STATUS_COLOUR.get(d.status, DEFAULT_COLOUR)

        share = _share(d.recent_detected, d.recent_evaluable)
        lo, hi = d.recent_ci
        ax_now.plot([lo, hi], [i, i], color=colour, lw=1.3, solid_capstyle="butt", zorder=2)
        if share is not None:
            ax_now.plot([share], [i], "o", color=colour, ms=3.6, zorder=3)

        base = _share(d.baseline_detected, d.baseline_evaluable)
        change = None if share is None or base is None else share - base
        clo, chi = d.change_ci
        kcl, kch = d.change_ci_clustered
        if (kcl, kch) != (clo, chi) and d.baseline_evaluable:
            # Drawn first and thicker, so the unclustered interval reads as the
            # inner bar of a wider one rather than as a separate estimate.
            ax_chg.plot([kcl, kch], [i, i], color=colour, lw=3.4, alpha=0.22, solid_capstyle="butt", zorder=1)
        ax_chg.plot([clo, chi], [i, i], color=colour, lw=1.3, solid_capstyle="butt", zorder=2)
        if change is not None:
            ax_chg.plot([change], [i], "o", color=colour, ms=3.6, zorder=3)
        if d.flag_survives_clustering is False:
            ax_chg.plot([chi], [i], "x", color=colour, ms=4.5, mew=1.1, zorder=4)

    labels = []
    for d in rows:
        mark = "*" if d.lineage_override else ""
        labels.append(f"{d.assay_id}{mark}  n={d.recent_evaluable}")
    ax_now.set_yticks(list(y))
    ax_now.set_yticklabels(labels, fontsize=6.5)
    ax_now.invert_yaxis()

    # One threshold is a line; several assays with different thresholds get a
    # band, because a single line would be wrong for most of the rows.
    if len(thresholds) == 1:
        t = next(iter(thresholds))
        ax_now.axvline(t, color="#444", ls="--", lw=0.9, zorder=1)
        ax_now.annotate(
            f"threshold {t:.0%}",
            xy=(t, 1.0),
            xycoords=("data", "axes fraction"),
            xytext=(2, 2),
            textcoords="offset points",
            fontsize=6.5,
            color="#444",
        )
    else:
        ax_now.axvspan(min(thresholds), max(thresholds), color="#444", alpha=0.08, zorder=0)
        for t in sorted(thresholds):
            ax_now.axvline(t, color="#444", ls="--", lw=0.6, alpha=0.6, zorder=1)
        ax_now.annotate(
            f"thresholds {min(thresholds):.0%}-{max(thresholds):.0%}",
            xy=(0.02, 1.0),
            xycoords="axes fraction",
            xytext=(0, 2),
            textcoords="offset points",
            fontsize=6.5,
            color="#444",
        )

    ax_now.set_xlim(-0.02, 1.02)
    ax_now.set_xlabel("detected share, recent window (Wilson 95% CI)")
    ax_now.grid(axis="x", color="#eee", lw=0.6, zorder=0)
    ax_now.set_axisbelow(True)

    ax_chg.axvline(0.0, color="#444", lw=0.9, zorder=1)
    for mdv in sorted(d for d in min_declines if d > 0):
        ax_chg.axvline(-mdv, color="#444", ls=":", lw=0.9, zorder=1)
        ax_chg.annotate(
            f"-{mdv:.0%} min decline",
            xy=(-mdv, 1.0),
            xycoords=("data", "axes fraction"),
            xytext=(-2, 2),
            textcoords="offset points",
            fontsize=6.5,
            color="#444",
            ha="right",
        )
    ax_chg.set_xlabel("change from baseline (Newcombe 95% CI)")
    ax_chg.grid(axis="x", color="#eee", lw=0.6, zorder=0)
    ax_chg.set_axisbelow(True)

    seen = [s for s in STATUS_ORDER if any(d.status == s for d in rows)]
    handles = [Patch(facecolor=STATUS_COLOUR.get(s, DEFAULT_COLOUR), label=s) for s in seen]
    notes = []
    if any(d.lineage_override for d in rows):
        notes.append("* verdict set by a lineage")
    if any(d.flag_survives_clustering is False for d in rows):
        notes.append("x flag does not survive clustering")
    fig.legend(
        handles=handles,
        loc="lower center",
        ncol=len(handles),
        frameon=False,
        fontsize=6.5,
        bbox_to_anchor=(0.5, 0.21 / height),
    )
    if notes:
        fig.text(0.5, 0.06 / height, "    ".join(notes), ha="center", va="bottom", fontsize=6.5, color="#444")
    fig.suptitle(f"Detection against threshold, {len(rows)} assays", fontsize=9, y=1 - 0.1 / height)
    return _svg(fig)


def _degenerate_positions(seq: str) -> set[int]:
    """1-based 5' positions in `seq` whose base stands for more than one molecule."""
    from assaywatch.iupac import degeneracy

    return {i for i, b in enumerate(seq, start=1) if degeneracy(b) > 1}


def site_positions(results: list[AssaySites], limit: int = 6) -> str:
    """Detection penalty per oligo position, 5' to 3', one panel row per assay.

    The bar is `PositionStat.gap`: detected share among records that match here
    minus the share among records that mismatch here. So the height is how much
    a mismatch at this position actually costs detection, which is the quantity
    a redesign turns on - not how often the position mismatches, which says
    nothing about whether the assay minds.

    The interval is Newcombe, the same one the verdicts use, because the bar is
    a difference of two proportions and a Wilson interval on either side alone
    would understate it. The 3'-terminal zone is shaded: a mismatch there blocks
    extension rather than merely shifting Tm, so a small bar in the shaded band
    can matter more than a large one outside it. A caret marks a position that
    is already degenerate, which answers the question neither table answers
    alone - whether the drifting position is one the design already covers.
    """
    shown = [r for r in results if r.positions][:limit]
    if not shown:
        return _empty("no position met the minimum record count")

    from assaywatch.sitedrift import THREE_PRIME_ZONE

    panels: list[tuple[AssaySites, str, list]] = []
    for r in shown:
        for oligo in OLIGO_ORDER:
            pos = sorted((p for p in r.positions if p.oligo == oligo), key=lambda p: p.pos_5prime)
            if pos:
                panels.append((r, oligo, pos))
    if not panels:
        return _empty("no position met the minimum record count")

    # Panel and gap sized in inches so a two-panel figure and a twelve-panel one
    # have the same spacing; the gap holds each panel's title and base letters.
    # bot_in holds the last panel's base letters as well as the footnote; at 0.34
    # the footnote was drawn through them.
    panel_in, gap_in, top_in, bot_in = 0.95, 0.58, 0.45, 0.56
    height = len(panels) * panel_in + (len(panels) - 1) * gap_in + top_in + bot_in
    fig, axes = plt.subplots(
        len(panels), 1, figsize=(9.5, height), squeeze=False, gridspec_kw={"hspace": gap_in / panel_in}
    )
    fig.subplots_adjust(top=1 - top_in / height, bottom=bot_in / height)
    for ax, (r, oligo, pos) in zip((a[0] for a in axes), panels, strict=True):
        seq = r.oligo_seqs.get(oligo, "")
        degen = _degenerate_positions(seq)
        colour = STATUS_COLOUR.get(r.status, DEFAULT_COLOUR)

        xs = [p.pos_5prime for p in pos]
        gaps = [p.gap if p.gap is not None else 0.0 for p in pos]
        ax.bar(xs, gaps, width=0.72, color=colour, alpha=0.85, zorder=3)

        for p in pos:
            if p.gap is None:
                continue
            lo, hi = newcombe_difference(
                p.detected_without, p.evaluable_without, p.detected_with, p.evaluable_with
            )
            ax.plot([p.pos_5prime, p.pos_5prime], [lo, hi], color="#333", lw=0.9, zorder=4)

        # The 3' zone is counted from the 3' end, so its 5' coordinates depend on
        # the oligo's length rather than being a fixed span.
        if seq:
            ax.axvspan(
                len(seq) - THREE_PRIME_ZONE + 0.5, len(seq) + 0.5, color="#b3261e", alpha=0.07, zorder=0
            )

        ax.axhline(0.0, color="#444", lw=0.8, zorder=2)
        if seq:
            ax.set_xlim(0.5, len(seq) + 0.5)
            ax.set_xticks(range(1, len(seq) + 1))
            ax.set_xticklabels(list(seq), fontsize=6)
            for i, lab in enumerate(ax.get_xticklabels(), start=1):
                if i in degen:
                    lab.set_color("#b26a00")
                    lab.set_fontweight("bold")
        ax.set_ylabel("penalty", fontsize=7)
        ax.grid(axis="y", color="#eee", lw=0.6, zorder=1)
        ax.set_axisbelow(True)
        ax.set_title(
            f"{r.assay_id} - {oligo} ({r.taxon}, {r.status}, n={r.n_evaluable})",
            fontsize=7.5,
            loc="left",
            pad=3,
        )

    fig.suptitle(
        "Detection penalty per position, 5' to 3' (Newcombe 95% CI)", fontsize=9, y=1 - 0.11 / height
    )
    fig.text(
        0.5,
        0.07 / height,
        f"shaded: 3'-terminal {THREE_PRIME_ZONE} bases     amber base: already degenerate",
        ha="center",
        va="bottom",
        fontsize=6.5,
        color="#444",
    )
    return _svg(fig)


PAGE = """<!doctype html>
<meta charset="utf-8">
<title>AssayWatch figures {run_date}</title>
<style>
  body {{ font: 14px/1.5 -apple-system, system-ui, sans-serif; margin: 2rem auto; max-width: 1100px;
          padding: 0 1rem; color: #202124; }}
  h1 {{ font-size: 1.3rem; margin-bottom: 0.2rem; }}
  h2 {{ font-size: 1rem; margin-top: 2.2rem; }}
  p.note {{ color: #5f6368; font-size: 0.86rem; max-width: 60ch; }}
  figure {{ margin: 0.6rem 0 0; }}
  svg {{ max-width: 100%; height: auto; }}
</style>
<h1>AssayWatch figures</h1>
<p class="note">Run {run_date}. Numbers come from the same assessment as
<code>report.md</code> and <code>site-drift.md</code>.</p>
<h2>Detection against threshold</h2>
<p class="note">Left: where each assay's recent window sits against its detection threshold.
Right: how far it has moved from baseline. An assay is flagged on both together, so the two
panels are the verdict.</p>
<figure>{forest}</figure>
<h2>Detection penalty per position</h2>
<p class="note">Bar height is how much detection falls when a record mismatches at that
position - the cost of the mismatch, not its frequency. The shaded band is the 3'-terminal
zone, where a mismatch blocks extension rather than shifting Tm.</p>
<figure>{sites}</figure>
"""


def build(
    calls_path: Path,
    registry: Path,
    retrieved: Path,
    cfg: dict[str, Any],
    run_date: str | None = None,
) -> dict[str, str]:
    """{filename: contents} for every figure output.

    Both assessments are run here rather than read back from their rendered
    documents: the markdown is a view of the numbers, and parsing it back would
    be a second, divergent implementation of the same arithmetic.
    """
    from assaywatch import report as report_mod
    from assaywatch import sitedrift as sitedrift_mod

    run_date = run_date or calls_path.parent.name
    fig_cfg = cfg.get("figures", {}) if isinstance(cfg, dict) else {}
    max_rows = int(fig_cfg.get("max_forest_rows", 40))
    max_assays = int(fig_cfg.get("max_site_assays", 6))

    _, _, drifts = report_mod.build(calls_path, registry, retrieved, cfg, run_date=run_date)
    _, _, sites = sitedrift_mod.build(calls_path, registry, retrieved, cfg, run_date=run_date)

    forest_svg = forest(drifts, limit=max_rows)
    sites_svg = site_positions(sites, limit=max_assays)
    return {
        "forest.svg": forest_svg,
        "site-positions.svg": sites_svg,
        "figures.html": PAGE.format(run_date=run_date, forest=forest_svg, sites=sites_svg),
    }


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
    figures = build(args.calls, args.registry, args.retrieved, cfg, run_date=args.run_date)
    out = args.out / "figures"
    out.mkdir(parents=True, exist_ok=True)
    for name, contents in figures.items():
        atomic.write_text(out / name, contents)
    print(f"wrote {len(figures)} figures to {out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
