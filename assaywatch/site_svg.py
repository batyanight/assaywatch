"""The per-assay figures, hand-drawn as inline SVG.

Replaces a Bokeh implementation on 2026-10-31. Three reasons, in order of how
much they mattered:

1. **The mismatch map was unreadable.** It plotted only the positions that
   carried a mismatch, so a 23-mer primer with defects at 18, 17, 2 and 1 drew
   four boxes and a void, and nothing said where along the oligo they sat or
   what the bases were. The figure that matters most in this project was the
   worst one on the site. Here the whole oligo is drawn, base by base, with the
   3' window marked, so a position is read against the sequence it belongs to.
2. **A chart library pinned three versions that had to agree** -- the installed
   renderer, a constant, and a CDN script tag -- and on the first deploy they
   did not, which would have rendered every chart on 217 pages as nothing.
   Inline SVG has no runtime to match.
3. Pages are about a quarter the size, work with JavaScript off, need no
   network, and follow the page theme through `currentColor` and the palette's
   CSS variables rather than a second color configuration.

What was given up is pan and zoom, and a tooltip richer than the browser's own.
Each mark carries a `<title>`, which is a native tooltip and is read out by
screen readers; the numbers behind every figure are also printed as text on the
same page, so nothing is only available by hovering.

Color comes from `assaywatch.palette` through CSS classes rather than literal
hexes, so light and dark are one definition and a color change is one edit.

There is no per-lineage figure here. It was drawn as a forest plot and removed:
70 of the 125 assays with lineage data have exactly ONE lineage, so the usual
page carried an axis, a grid, a threshold line and a single dot. That view is a
table now (`site_render._lineage_block`), which is denser where there are
several lineages and becomes one sentence where there is one.
"""

from __future__ import annotations

import html
import math
from typing import Any

#: Geometry. Chosen so a 30-mer fits a phone in landscape and a 23-mer is
#: comfortable on a laptop; past about 40 the track scrolls rather than shrinks,
#: because an unreadable base is worse than a scrollbar.
CELL = 15.0  # px per oligo position
GUTTER = 104.0  # left label column: the role name plus the 5′ marker
BAR_H = 34.0  # tallest mismatch bar
ROW_GAP = 16.0
#: The oligo name under the role label. Monospace at 10px is about 6.2 px a character.
#: Longer names are cut rather than given all the room they ask for: the gutter is taken
#: from the bases, and the page's oligo table and the tooltip both carry the full name.
NAME_CHAR_PX = 6.2
NAME_MAX_CHARS = 22


def _esc(s: Any) -> str:
    return html.escape(str(s), quote=True)


def _severity(detected_with: int, evaluable_with: int, detected_without: int, evaluable_without: int) -> str:
    """How much detection falls among the records that mismatch here.

    This, not the mismatch count, is what says a position matters: a base that
    half the records differ at but which costs nothing is a polymorphism, and a
    base that few records differ at but which always kills the reaction is a
    design problem. The class names map onto the status palette, so "this
    position behaves like a failure" and "this assay is declining" are the same
    red on purpose.
    """
    if not evaluable_with or not evaluable_without:
        return "aw-bar-weak"
    with_pct = 100 * detected_with / evaluable_with
    without_pct = 100 * detected_without / evaluable_without
    drop = without_pct - with_pct
    if drop >= 25:
        return "aw-bar-strong"
    if drop >= 10:
        return "aw-bar-mid"
    return "aw-bar-weak"


def mismatch_track(page: dict[str, Any], names: dict[str, str] | None = None) -> str:
    """Each oligo drawn base by base, with a bar per position showing how many
    records differ there and how much that costs."""
    oligos = page.get("oligos") or {}
    positions = page.get("positions") or []
    if not oligos:
        return ""
    by_oligo: dict[str, dict[int, dict]] = {}
    for p in positions:
        by_oligo.setdefault(p["oligo"], {})[p["pos_3prime"]] = p

    roles = [r for r in ("forward", "reverse", "probe") if r in oligos]
    longest = max(len(oligos[r]) for r in roles)
    row_h = BAR_H + 18 + 14
    drawn_names = {r: (names or {}).get(r) or "" for r in roles}
    widest = max(min(len(v), NAME_MAX_CHARS) for v in drawn_names.values())
    gutter = max(GUTTER, 30 + (widest + 1) * NAME_CHAR_PX)
    width = gutter + longest * CELL + 18
    height = len(roles) * (row_h + ROW_GAP) + 12

    out = [
        f'<svg class="aw-track" viewBox="0 0 {width:.0f} {height:.0f}" role="img" '
        f'xmlns="http://www.w3.org/2000/svg" aria-label="'
        f"Mismatch map: each oligo drawn base by base with a bar showing the share of records "
        f'differing at that position.">'
    ]

    for i, role in enumerate(roles):
        seq = oligos[role]
        n = len(seq)
        top = 10 + i * (row_h + ROW_GAP)
        base_y = top + BAR_H
        # The role, and under it the name the paper gave the oligo. The label
        # ends well short of the 5' marker: at gutter - 10 the two overlapped
        # once the theme's larger type replaced Material's.
        out.append(f'<text class="aw-track-label" x="{gutter - 30:.0f}" y="{base_y + 8:.0f}">{role}</text>')
        oligo_name = drawn_names[role]
        if oligo_name:
            shown = oligo_name
            tooltip = ""
            if len(oligo_name) > NAME_MAX_CHARS:
                shown = oligo_name[: NAME_MAX_CHARS - 1] + "\u2026"
                tooltip = f"<title>{_esc(oligo_name)}</title>"
            out.append(
                f'<text class="aw-track-name" x="{gutter - 30:.0f}" '
                f'y="{base_y + 20:.0f}">{tooltip}{_esc(shown)}</text>'
            )

        # The shaded region is the one the SCORER penalizes more heavily, and it
        # is not the same region for a primer and a probe. It carries no drawn
        # label: the caption says what is shaded and each bar's tooltip names the
        # region it falls in, which keeps the track itself free of words.
        #
        # For a primer it is the last five bases. A polymerase extends from the
        # 3'-OH, so a mismatch there sits in the catalytic site.
        #
        # For a probe it is the CENTRAL THIRD. A hydrolysis probe is never
        # extended -- its 3' end carries the quencher or the minor-groove binder
        # -- and it is cleaved by the polymerase's 5'->3' exonuclease, so its 3'
        # terminus has no special status. What matters is duplex stability,
        # which a central mismatch disturbs most. `config.yaml` says the same
        # thing in numbers: `probe_center_penalty` 2.0 over the central third,
        # `probe_outer_penalty` 1.0 elsewhere, and no 3' window for probes at
        # all. Shading the last five bases of a probe drew a region the scorer
        # does not use.
        if role == "probe":
            lo, hi = n // 3, n - n // 3
        else:
            lo, hi = max(n - 5, 0), n
        if hi > lo:
            out.append(
                f'<rect class="aw-zone" x="{gutter + lo * CELL:.1f}" y="{top:.1f}" '
                f'width="{(hi - lo) * CELL:.1f}" height="{BAR_H + 18:.1f}"/>'
            )

        out.append(
            f'<line class="aw-axis" x1="{gutter:.1f}" y1="{base_y:.1f}" '
            f'x2="{gutter + n * CELL:.1f}" y2="{base_y:.1f}"/>'
        )

        for idx in range(n):
            pos3 = n - idx  # 1 is the 3'-terminal base
            x = gutter + idx * CELL
            stat = by_oligo.get(role, {}).get(pos3)
            if stat:
                denom = (stat["evaluable_with"] or 0) + (stat["evaluable_without"] or 0)
                share = stat["n_mismatch"] / denom if denom else 0.0
                # Square root, so a position 4% of records differ at is still
                # visible beside one at 60%. Linear height made every real signal
                # on a well-conserved oligo invisible.
                h = max(1.5, min(BAR_H, BAR_H * math.sqrt(min(share, 1.0))))
                cls = _severity(
                    stat["detected_with"],
                    stat["evaluable_with"],
                    stat["detected_without"],
                    stat["evaluable_without"],
                )
                with_pct = (
                    100 * stat["detected_with"] / stat["evaluable_with"] if stat["evaluable_with"] else 0
                )
                without_pct = (
                    100 * stat["detected_without"] / stat["evaluable_without"]
                    if stat["evaluable_without"]
                    else 0
                )
                subs = (
                    ", ".join(f"{a}>{b} in {c:,}" for a, b, c in stat["substitutions"][:3]) or "not recorded"
                )
                if role == "probe":
                    in_zone = n // 3 <= (n - pos3) < n - n // 3
                    zone_text = "in the central third" if in_zone else "outside the central third"
                else:
                    zone_text = (
                        "inside the 3\u2032 window"
                        if stat["in_3prime_zone"]
                        else "outside the 3\u2032 window"
                    )
                # `base` is the primary oligo's, which is the one drawn; the substitutions
                # name the oligo the record was actually scored against.
                alternates = sorted({a for a, _, _ in stat["substitutions"]} - {stat["base"]})
                alternate_text = (
                    f"\nscored against a pool alternate with {'/'.join(alternates)} here"
                    if alternates
                    else ""
                )
                tip = (
                    f"{role} position {pos3} from the 3' end, base {stat['base']}\n"
                    f"{stat['n_mismatch']:,} of {denom:,} records differ here ({100 * share:.1f}%)\n"
                    f"detected when it differs: {with_pct:.0f}% of {stat['evaluable_with']:,}\n"
                    f"detected when it does not: {without_pct:.0f}% of {stat['evaluable_without']:,}\n"
                    f"substitutions: {subs}\n"
                    f"{zone_text}{alternate_text}"
                )
                # 1px inset each side is the gap the eye needs between adjacent
                # filled bars; without it two neighbors read as one wide block.
                out.append(
                    f'<g class="{cls}"><title>{_esc(tip)}</title>'
                    f'<rect x="{x + 1:.1f}" y="{base_y - h:.1f}" '
                    f'width="{CELL - 2:.1f}" height="{h:.1f}"/></g>'
                )
            out.append(
                f'<text class="aw-base" x="{x + CELL / 2:.1f}" y="{base_y + 13:.0f}">{_esc(seq[idx])}</text>'
            )

        # Tick every fifth position, counting from the 3' end, plus the ends.
        for pos3 in sorted({1, 5, 10, 15, 20, 25, 30, 35, 40, n} & set(range(1, n + 1))):
            x = gutter + (n - pos3) * CELL + CELL / 2
            out.append(f'<text class="aw-tick" x="{x:.1f}" y="{base_y + 27:.0f}">{pos3}</text>')

        out.append(f'<text class="aw-end" x="{gutter - 4:.0f}" y="{base_y + 13:.0f}">5′</text>')
        out.append(
            f'<text class="aw-end aw-end-3" x="{gutter + n * CELL + 4:.0f}" y="{base_y + 13:.0f}">3′</text>'
        )

    out.append("</svg>")
    return "".join(out)


#: The year chart's plot box. Shared with `composition_panel` so a column of the panel
#: sits under the point of the year it belongs to; a panel on its own axis would invite
#: exactly the misreading it exists to prevent.
_W, _L, _R = 720.0, 44.0, 14.0


def year_chart(page: dict[str, Any], same_mix: dict[int, float] | None = None) -> str:
    """Detected share by deposit year, with the recent window and the threshold.

    `same_mix` (year -> share, from the composition stage) draws a second, dashed line:
    what each year would have read on the whole period's mix of lineages. Where the two
    lines part, the mix of what was deposited moved rather than detection within it.
    """
    years = [y for y in page.get("years", []) if y["evaluable"] > 0]
    if not years:
        return ""
    W, H = _W, 230.0
    L, R, T, B = _L, _R, 12.0, 38.0
    xs = [y["year"] for y in years]
    lo, hi = min(xs), max(xs)
    span = max(hi - lo, 1)

    def px(year: int) -> float:
        # One year of data draws a single centered point rather than being
        # jammed against the left edge. Returning nothing here left four
        # assays with a blank panel and no explanation.
        if len(years) == 1:
            return L + (W - L - R) / 2
        return L + (year - lo) / span * (W - L - R)

    #: The drawn range runs a little past both ends, so a series sitting at 0%
    #: is above the axis rather than on top of it. Seven assays detect nothing
    #: in any year and five are flat zero; with 0% mapped to the baseline their
    #: line coincided with the axis, which reads as a chart that failed to draw.
    PAD = 5.0

    def py(pct: float) -> float:
        return T + (100 + PAD - pct) / (100 + 2 * PAD) * (H - T - B)

    out = [
        f'<svg class="aw-chart" viewBox="0 0 {W:.0f} {H:.0f}" role="img" '
        f'xmlns="http://www.w3.org/2000/svg" aria-label="Predicted detection by deposit year, '
        f'{lo} to {hi}, against a {100 * page["threshold"]:.0f} percent threshold.">'
    ]
    recent = [y["year"] for y in years if y["recent"]]
    if recent:
        x0 = px(min(recent))
        out.append(
            f'<rect class="aw-window" x="{x0:.1f}" y="{T:.1f}" '
            f'width="{W - R - x0:.1f}" height="{H - T - B:.1f}"><title>'
            f"the recent window: {page['window_months']} months "
            f"from {_esc(page['recent_from'])}</title></rect>"
        )
    for pct in (0, 25, 50, 75, 100):
        y = py(pct)
        out.append(f'<line class="aw-grid" x1="{L:.1f}" y1="{y:.1f}" x2="{W - R:.1f}" y2="{y:.1f}"/>')
        out.append(f'<text class="aw-tick aw-tick-y" x="{L - 7:.1f}" y="{y + 3.5:.1f}">{pct}</text>')
    ty = py(100 * page["threshold"])
    out.append(f'<line class="aw-threshold" x1="{L:.1f}" y1="{ty:.1f}" x2="{W - R:.1f}" y2="{ty:.1f}"/>')
    out.append(
        f'<text class="aw-threshold-label" x="{W - R:.1f}" y="{ty - 5:.1f}">'
        f"{100 * page['threshold']:.0f}% threshold</text>"
    )

    drawn_same = sorted(
        (y["year"], same_mix[y["year"]]) for y in years if (same_mix or {}).get(y["year"]) is not None
    )
    if len(drawn_same) > 1:
        pts = " ".join(f"{px(year):.1f},{py(100 * share):.1f}" for year, share in drawn_same)
        out.append(
            f'<polyline class="aw-same-mix" points="{pts}"><title>'
            "each year on the whole period's mix of lineages: where this parts from the "
            "line above, the mix moved rather than detection within it</title></polyline>"
        )

    status_cls = "aw-" + (page["status"] or "no data").replace(" ", "-")
    if len(years) > 1:
        pts = " ".join(f"{px(y['year']):.1f},{py(100 * y['share']):.1f}" for y in years)
        out.append(f'<polyline class="aw-line {status_cls}" points="{pts}"/>')
    for y in years:
        r = max(2.5, min(7.0, 1.6 * math.log10(y["evaluable"] + 1) + 1.6))
        tip = f"{y['year']}: {y['detected']:,} of {y['evaluable']:,} detected ({100 * y['share']:.1f}%)" + (
            " — recent window" if y["recent"] else ""
        )
        out.append(
            f'<g class="aw-point {status_cls}"><title>{_esc(tip)}</title>'
            f'<circle cx="{px(y["year"]):.1f}" cy="{py(100 * y["share"]):.1f}" r="{r:.1f}"/></g>'
        )

    if len(years) == 1:
        out.append(f'<text class="aw-tick" x="{px(lo):.1f}" y="{H - B + 16:.0f}">{lo}</text>')
    else:
        step = max(1, round(span / 7))
        for year in range(lo, hi + 1, step):
            out.append(f'<text class="aw-tick" x="{px(year):.1f}" y="{H - B + 16:.0f}">{year}</text>')
    caption = (
        "one year holds every evaluable record"
        if len(years) == 1
        else "deposit year · marker size is the number of records"
    )
    out.append(f'<text class="aw-axis-label" x="{(L + W - R) / 2:.0f}" y="{H - 6:.0f}">{caption}</text>')
    out.append("</svg>")
    return "".join(out)


#: Ordinal lightness for the clusters, largest first. One hue, because lightness is the
#: only free channel here: the palette's colours all carry meaning (a verdict, a call) and
#: are contrast-validated as a set, so eight invented categorical colours would be eight
#: unvalidated ones. Ordering is meaningful -- clusters are ranked by size -- which is what
#: makes an ordinal ramp honest for them.
_CLUSTER_STEPS = (0.85, 0.72, 0.60, 0.50, 0.41, 0.33, 0.26, 0.20)


def composition_panel(comp: dict[str, Any], page: dict[str, Any]) -> str:
    """The lineage mix per deposit year, as 100% stacked columns under the year chart.

    It answers one question: did the mix of lineages being deposited change? Detection is
    the chart above and the tooltips here, deliberately NOT a second encoding on these
    columns -- lightness already carries which cluster a segment is, and a reader cannot
    be asked to read two meanings from one channel. Per-cluster detection is in the
    tooltip and in lineage.md.

    `other`, `unplaced` and `diverged` are hatched rather than shaded, because they are
    not lineages: they say what the clustering could not do.
    """
    years = comp.get("years") or []
    records = comp.get("records") or []
    if not years or not records:
        return ""
    ids, names = comp.get("ids") or [], comp.get("names") or []
    detected = comp.get("detected") or records
    W, H = _W, 132.0
    L, R, T, B = _L, _R, 10.0, 30.0
    span = max(max(years) - min(years), 1)
    inner = W - L - R
    width = min(26.0, max(6.0, inner / max(len(years), 1) * 0.72))

    def px(year: int) -> float:
        if len(years) == 1:
            return L + inner / 2
        return L + (year - min(years)) / span * inner

    out = [
        f'<svg class="aw-chart aw-panel" viewBox="0 0 {W:.0f} {H:.0f}" role="img" '
        f'xmlns="http://www.w3.org/2000/svg" aria-label="The mix of sequence clusters by '
        f'deposit year, {min(years)} to {max(years)}.">',
        '<defs><pattern id="aw-unplaced" width="5" height="5" patternUnits="userSpaceOnUse" '
        'patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" '
        'stroke="currentColor" stroke-width="1.6" opacity="0.5"/></pattern></defs>',
    ]
    for row, year in enumerate(years):
        total = sum(records[row])
        if not total:
            continue
        x = px(year) - width / 2
        y = T
        for col, cid in enumerate(ids):
            n = records[row][col]
            if not n:
                continue
            h = (H - T - B) * n / total
            got = detected[row][col] if col < len(detected[row]) else 0
            name = names[col] if col < len(names) else str(cid)
            if cid < 0:
                fill = 'fill="url(#aw-unplaced)"' if cid != -1 else 'fill="currentColor" opacity="0.12"'
            else:
                fill = (
                    f'fill="currentColor" opacity="{_CLUSTER_STEPS[min(col, len(_CLUSTER_STEPS) - 1)]:.2f}"'
                )
            tip = f"{year} — {name}: {n:,} of {total:,} records ({n / total:.0%}), {got:,} detected"
            out.append(
                f'<g class="aw-seg"><title>{_esc(tip)}</title>'
                f'<rect x="{x:.1f}" y="{y:.1f}" width="{width:.1f}" height="{h:.1f}" {fill}/></g>'
            )
            y += h
    if len(years) == 1:
        out.append(f'<text class="aw-tick" x="{px(years[0]):.1f}" y="{H - B + 15:.0f}">{years[0]}</text>')
    else:
        step = max(1, round(span / 7))
        for year in range(min(years), max(years) + 1, step):
            out.append(f'<text class="aw-tick" x="{px(year):.1f}" y="{H - B + 15:.0f}">{year}</text>')
    out.append(
        f'<text class="aw-axis-label" x="{(L + W - R) / 2:.0f}" y="{H - 6:.0f}">'
        "share of each year's records, by sequence cluster</text>"
    )
    out.append("</svg>")
    return "".join(out)
