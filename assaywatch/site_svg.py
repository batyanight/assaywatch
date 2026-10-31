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
   CSS variables rather than a second colour configuration.

What was given up is pan and zoom, and a tooltip richer than the browser's own.
Each mark carries a `<title>`, which is a native tooltip and is read out by
screen readers; the numbers behind every figure are also printed as text on the
same page, so nothing is only available by hovering.

Colour comes from `assaywatch.palette` through CSS classes rather than literal
hexes, so light and dark are one definition and a colour change is one edit.
"""

from __future__ import annotations

import html
import math
from typing import Any

#: Geometry. Chosen so a 30-mer fits a phone in landscape and a 23-mer is
#: comfortable on a laptop; past about 40 the track scrolls rather than shrinks,
#: because an unreadable base is worse than a scrollbar.
CELL = 15.0  # px per oligo position
GUTTER = 78.0  # left label column
BAR_H = 34.0  # tallest mismatch bar
ROW_GAP = 16.0


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


def mismatch_track(page: dict[str, Any]) -> str:
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
    width = GUTTER + longest * CELL + 18
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
        out.append(f'<text class="aw-track-label" x="{GUTTER - 10:.0f}" y="{base_y + 12:.0f}">{role}</text>')

        # The 3' window, shaded under the last five bases: a mismatch inside it
        # is the one that fails an assay, so the eye should find it without
        # counting backwards from the end.
        zone_positions = [p for p in range(1, 6) if p <= n]
        if zone_positions:
            x0 = GUTTER + (n - max(zone_positions)) * CELL
            out.append(
                f'<rect class="aw-zone" x="{x0:.1f}" y="{top:.1f}" '
                f'width="{len(zone_positions) * CELL:.1f}" height="{BAR_H + 18:.1f}"/>'
            )

        out.append(
            f'<line class="aw-axis" x1="{GUTTER:.1f}" y1="{base_y:.1f}" '
            f'x2="{GUTTER + n * CELL:.1f}" y2="{base_y:.1f}"/>'
        )

        for idx in range(n):
            pos3 = n - idx  # 1 is the 3'-terminal base
            x = GUTTER + idx * CELL
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
                tip = (
                    f"{role} position {pos3} from the 3' end, base {stat['base']}\n"
                    f"{stat['n_mismatch']:,} of {denom:,} records differ here ({100 * share:.1f}%)\n"
                    f"detected when it differs: {with_pct:.0f}% of {stat['evaluable_with']:,}\n"
                    f"detected when it does not: {without_pct:.0f}% of {stat['evaluable_without']:,}\n"
                    f"substitutions: {subs}"
                )
                # 1px inset each side is the gap the eye needs between adjacent
                # filled bars; without it two neighbours read as one wide block.
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
            x = GUTTER + (n - pos3) * CELL + CELL / 2
            out.append(f'<text class="aw-tick" x="{x:.1f}" y="{base_y + 27:.0f}">{pos3}</text>')

        out.append(f'<text class="aw-end" x="{GUTTER - 4:.0f}" y="{base_y + 13:.0f}">5′</text>')
        out.append(
            f'<text class="aw-end aw-end-3" x="{GUTTER + n * CELL + 4:.0f}" y="{base_y + 13:.0f}">3′</text>'
        )

    out.append("</svg>")
    return "".join(out)


def year_chart(page: dict[str, Any]) -> str:
    """Detected share by deposit year, with the recent window and the threshold."""
    years = [y for y in page.get("years", []) if y["evaluable"] > 0]
    if len(years) < 2:
        return ""
    W, H = 720.0, 230.0
    L, R, T, B = 44.0, 14.0, 12.0, 38.0
    xs = [y["year"] for y in years]
    lo, hi = min(xs), max(xs)
    span = max(hi - lo, 1)

    def px(year: int) -> float:
        return L + (year - lo) / span * (W - L - R)

    def py(pct: float) -> float:
        return T + (100 - pct) / 100 * (H - T - B)

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

    pts = " ".join(f"{px(y['year']):.1f},{py(100 * y['share']):.1f}" for y in years)
    status_cls = "aw-" + (page["status"] or "no data").replace(" ", "-")
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

    step = max(1, round(span / 7))
    for year in range(lo, hi + 1, step):
        out.append(f'<text class="aw-tick" x="{px(year):.1f}" y="{H - B + 16:.0f}">{year}</text>')
    out.append(
        f'<text class="aw-axis-label" x="{(L + W - R) / 2:.0f}" y="{H - 6:.0f}">'
        f"deposit year · marker size is the number of records</text>"
    )
    out.append("</svg>")
    return "".join(out)


def lineage_chart(page: dict[str, Any]) -> str:
    """One row per lineage: detected share and its interval, worst first."""
    lins = sorted(page.get("lineages", []), key=lambda item: item["share"])
    if not lins:
        return ""
    ROW = 24.0
    W = 720.0
    L, R, T, B = 230.0, 16.0, 10.0, 32.0
    H = T + len(lins) * ROW + B

    bot = T + len(lins) * ROW

    def px(pct: float) -> float:
        return L + pct / 100 * (W - L - R)

    out = [
        f'<svg class="aw-chart" viewBox="0 0 {W:.0f} {H:.0f}" role="img" '
        f'xmlns="http://www.w3.org/2000/svg" aria-label="Predicted detection per lineage, '
        f'{len(lins)} lineages, with 95 percent intervals.">'
    ]
    for pct in (0, 25, 50, 75, 100):
        out.append(
            f'<line class="aw-grid" x1="{px(pct):.1f}" y1="{T:.1f}" x2="{px(pct):.1f}" y2="{bot:.1f}"/>'
        )
        out.append(f'<text class="aw-tick" x="{px(pct):.1f}" y="{H - B + 16:.0f}">{pct}</text>')
    tx = px(100 * page["threshold"])
    out.append(f'<line class="aw-threshold" x1="{tx:.1f}" y1="{T:.1f}" x2="{tx:.1f}" y2="{bot:.1f}"/>')

    for i, item in enumerate(lins):
        y = T + i * ROW + ROW / 2
        below = item["ci"][1] < page["threshold"]
        cls = "aw-dot-fail" if below else "aw-dot-ok"
        label = item["lineage"]
        shown = label if len(label) <= 32 else label[:31] + "…"
        tip = (
            f"{label}\n{item['detected']:,} of {item['evaluable']:,} detected "
            f"({100 * item['share']:.1f}%)\n95% interval {100 * item['ci'][0]:.1f}"
            f"–{100 * item['ci'][1]:.1f}%"
        )
        out.append(f'<text class="aw-row-label" x="{L - 10:.0f}" y="{y + 3.5:.1f}">{_esc(shown)}</text>')
        out.append(
            f'<g class="{cls}"><title>{_esc(tip)}</title>'
            f'<line class="aw-ci" x1="{px(100 * item["ci"][0]):.1f}" y1="{y:.1f}" '
            f'x2="{px(100 * item["ci"][1]):.1f}" y2="{y:.1f}"/>'
            f'<circle cx="{px(100 * item["share"]):.1f}" cy="{y:.1f}" r="4.5"/></g>'
        )
    out.append(
        f'<text class="aw-axis-label" x="{(L + W - R) / 2:.0f}" y="{H - 4:.0f}">'
        f"predicted detection (%), bar = 95% interval</text>"
    )
    out.append("</svg>")
    return "".join(out)
