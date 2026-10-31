"""Bokeh charts for the website, one function per chart, each taking plain dicts.

Separate from `site.py` so the data layer has no plotting dependency: `extract`
runs in the pipeline environment, `render` runs where Bokeh is installed. Each
function returns `(script, div)` from `bokeh.embed.components`, and the page
template loads BokehJS once from a pinned CDN rather than inlining it 218 times.

THE RULES THESE FOLLOW, from the `dataviz` skill, because a chart that misleads
is worse than a table:

* **One axis per chart, never two scales.** Detection share and record count are
  different measures, so they are two charts sharing an x range, not one chart
  with a second y axis. The count chart is what stops a reader trusting a 100%
  built on three records.
* **Colour comes from `assaywatch.palette`** and is validated there. A status is
  never carried by colour alone: every chart that shows one writes it out.
* **Sequential magnitude gets one hue, light to dark.** The mismatch map is a
  magnitude, so it ramps one hue rather than running through a rainbow.
* **Hover is not optional.** Every mark carries a tooltip with the counts behind
  it, because the whole argument of this project is that a share without its
  denominator is not evidence.
"""

from __future__ import annotations

from typing import Any

from assaywatch import palette

#: Pinned, and at least two weeks old. The page template must load the same version.
BOKEH_VERSION = "3.6.2"

_TOOLS = "pan,box_zoom,wheel_zoom,reset,save"


def _figure(**kw: Any) -> Any:
    from bokeh.plotting import figure

    f = figure(tools=_TOOLS, toolbar_location="above", **kw)
    f.toolbar.logo = None
    f.background_fill_color = None
    f.border_fill_color = None
    f.outline_line_color = None
    f.xgrid.grid_line_color = None
    f.ygrid.grid_line_color = palette.GRID_LIGHT
    f.axis.axis_line_color = palette.GRID_LIGHT
    f.axis.major_tick_line_color = palette.GRID_LIGHT
    f.axis.minor_tick_line_color = None
    f.axis.axis_label_text_font_style = "normal"
    f.title.text_font_style = "normal"
    return f


def share_by_year(page: dict[str, Any]) -> tuple[str, str]:
    """Detected share per deposit year: the chart the verdict is read from.

    The threshold line and the recent window are both drawn, because the status
    is a statement about where the recent window's interval sits relative to
    that line and a reader should be able to see the same thing the rule saw.
    Years with no evaluable record are a gap in the line rather than a zero: 0%
    of nothing is not 0%.
    """
    from bokeh.embed import components
    from bokeh.models import BoxAnnotation, ColumnDataSource, HoverTool, Span

    years = [y for y in page["years"] if y["evaluable"] > 0]
    if not years:
        return "", '<p class="aw-empty">No evaluable records, so there is nothing to plot.</p>'

    src = ColumnDataSource(
        dict(
            year=[y["year"] for y in years],
            share=[100 * y["share"] for y in years],
            detected=[y["detected"] for y in years],
            evaluable=[y["evaluable"] for y in years],
            window=["recent" if y["recent"] else "baseline" for y in years],
            size=[_marker_size(y["evaluable"]) for y in years],
        )
    )
    f = _figure(
        height=300,
        sizing_mode="stretch_width",
        x_axis_label="deposit year",
        y_axis_label="predicted detection (%)",
        y_range=(-3, 103),
    )
    recent = [y["year"] for y in years if y["recent"]]
    if recent:
        f.add_layout(
            BoxAnnotation(
                left=min(recent) - 0.5,
                fill_color=palette.NEUTRAL,
                fill_alpha=0.07,
                line_color=None,
            )
        )
    thr = Span(
        location=100 * page["threshold"],
        dimension="width",
        line_color=palette.NEUTRAL,
        line_dash="dashed",
        line_width=1,
    )
    f.add_layout(thr)
    colour = palette.status_colour(page["status"] or "no data")
    f.line("year", "share", source=src, line_width=2, color=colour)
    marks = f.scatter(
        "year", "share", source=src, size="size", color=colour, line_color=palette.SURFACE_LIGHT, line_width=2
    )
    f.add_tools(
        HoverTool(
            renderers=[marks],
            tooltips=[
                ("year", "@year"),
                ("detected", "@detected of @evaluable"),
                ("share", "@share{0.0}%"),
                ("window", "@window"),
            ],
        )
    )
    return components(f)


def _marker_size(evaluable: int) -> float:
    """Marker area carries the denominator, so a share on 3 records cannot look
    like a share on 3,000. Area, not radius: a radius proportional to n would
    exaggerate by the square. Floored at 8px, the skill's minimum hit target."""
    import math

    return max(8.0, min(26.0, 5.0 * math.sqrt(math.log10(max(evaluable, 1) + 1) + 1) + 3))


def records_by_year(page: dict[str, Any]) -> tuple[str, str]:
    """Evaluable records per year, under the share chart and on the same x.

    Its own chart rather than a second axis on the one above. This is the chart
    that shows an assay judged on a deposition burst in one year and nothing
    since, which is the commonest reason a share is not evidence.
    """
    from bokeh.embed import components
    from bokeh.models import ColumnDataSource, HoverTool

    years = [y for y in page["years"] if y["evaluable"] > 0]
    if not years:
        return "", ""
    src = ColumnDataSource(
        dict(
            year=[y["year"] for y in years],
            evaluable=[y["evaluable"] for y in years],
            detected=[y["detected"] for y in years],
            colour=[palette.status_colour(page["status"]) if y["recent"] else palette.NEUTRAL for y in years],
        )
    )
    f = _figure(
        height=130, sizing_mode="stretch_width", x_axis_label="deposit year", y_axis_label="evaluable records"
    )
    bars = f.vbar(x="year", top="evaluable", width=0.72, source=src, color="colour", line_color=None)
    f.add_tools(
        HoverTool(
            renderers=[bars],
            tooltips=[("year", "@year"), ("evaluable", "@evaluable"), ("detected", "@detected")],
        )
    )
    f.y_range.start = 0
    return components(f)


def mismatch_map(page: dict[str, Any]) -> tuple[str, str]:
    """Where the mismatches sit on each oligo, and what they cost.

    One row per oligo, one cell per position, 3' end at the right because that is
    the end the penalty rule cares about and the end a reader is looking for. The
    fill is a magnitude -- the share of evaluable records mismatching here -- so
    it is one hue light to dark, not a rainbow. The 3' window is marked, since a
    mismatch inside it is the one that fails an assay.

    The number worth reading is in the tooltip: detection among records that
    mismatch here against detection among records that do not. That contrast,
    not the mismatch count, is what says the position matters.
    """
    from bokeh.embed import components
    from bokeh.models import ColumnDataSource, HoverTool

    positions = page["positions"]
    if not positions:
        return "", '<p class="aw-empty">No position carried a mismatch in enough records to report.</p>'

    oligos = [r for r in ("forward", "reverse", "probe") if any(p["oligo"] == r for p in positions)]
    xs, ys, alphas, tips = [], [], [], []
    for p in positions:
        n_with = p["evaluable_with"] or 1
        share_mm = p["n_mismatch"] / max(page["recent_evaluable"] + page["baseline_evaluable"], 1)
        xs.append(-p["pos_3prime"])
        ys.append(p["oligo"])
        alphas.append(min(1.0, 0.15 + 0.85 * min(share_mm * 4, 1.0)))
        det_with = 100 * p["detected_with"] / n_with
        det_without = 100 * p["detected_without"] / (p["evaluable_without"] or 1)
        tips.append(
            dict(
                pos=p["pos_3prime"],
                base=p["base"],
                n=p["n_mismatch"],
                with_=f"{det_with:.0f}% of {p['evaluable_with']}",
                without=f"{det_without:.0f}% of {p['evaluable_without']}",
                subs=", ".join(f"{a}>{b} {n}" for a, b, n in p["substitutions"][:4]) or "-",
                zone="yes" if p["in_3prime_zone"] else "no",
            )
        )
    src = ColumnDataSource(
        dict(
            x=xs,
            y=ys,
            alpha=alphas,
            pos=[t["pos"] for t in tips],
            base=[t["base"] for t in tips],
            n=[t["n"] for t in tips],
            det_with=[t["with_"] for t in tips],
            det_without=[t["without"] for t in tips],
            subs=[t["subs"] for t in tips],
            zone=[t["zone"] for t in tips],
        )
    )
    f = _figure(
        height=70 + 42 * len(oligos),
        sizing_mode="stretch_width",
        y_range=list(reversed(oligos)),
        x_axis_label="position from the 3' end (1 = the terminal base)",
    )
    cells = f.rect(
        x="x",
        y="y",
        width=0.9,
        height=0.62,
        source=src,
        color=palette.STATUS_LIGHT["declining"],
        alpha="alpha",
        line_color=None,
    )
    f.add_tools(
        HoverTool(
            renderers=[cells],
            tooltips=[
                ("oligo", "@y, position @pos from 3'"),
                ("oligo base", "@base"),
                ("records mismatching", "@n"),
                ("detected when mismatched", "@det_with"),
                ("detected when not", "@det_without"),
                ("substitutions", "@subs"),
                ("inside the 3' window", "@zone"),
            ],
        )
    )
    f.ygrid.grid_line_color = None
    f.xaxis.ticker = sorted({x for x in xs})
    f.xaxis.major_label_overrides = {x: str(-x) for x in xs}
    return components(f)


def lineage_bars(page: dict[str, Any]) -> tuple[str, str]:
    """Detected share per lineage, with its interval.

    Here because a pooled share is the wrong estimand for most real failures: a
    clade that is 5% of deposits can be 100% of a region's cases, and the pooled
    figure averages it away. Intervals are drawn, not implied, since most
    lineages are small enough that the interval is the finding.
    """
    from bokeh.embed import components
    from bokeh.models import ColumnDataSource, HoverTool, Span, Whisker

    lins = sorted(page["lineages"], key=lambda item: item["share"])
    if not lins:
        return "", ""
    labels = [f"{item['lineage']}" for item in lins]
    src = ColumnDataSource(
        dict(
            y=labels,
            share=[100 * item["share"] for item in lins],
            lo=[100 * item["ci"][0] for item in lins],
            hi=[100 * item["ci"][1] for item in lins],
            n=[item["evaluable"] for item in lins],
            det=[item["detected"] for item in lins],
            colour=[
                palette.STATUS_LIGHT["declining"]
                if item["ci"][1] < page["threshold"]
                else palette.STATUS_LIGHT["stable"]
                for item in lins
            ],
        )
    )
    f = _figure(
        height=80 + 26 * len(lins),
        sizing_mode="stretch_width",
        y_range=labels,
        x_axis_label="predicted detection (%), bar = 95% interval",
        x_range=(0, 103),
    )
    f.add_layout(
        Whisker(
            base="y",
            lower="lo",
            upper="hi",
            source=src,
            dimension="width",
            line_color=palette.NEUTRAL,
            upper_head=None,
            lower_head=None,
        )
    )
    dots = f.scatter(
        "share", "y", source=src, size=9, color="colour", line_color=palette.SURFACE_LIGHT, line_width=1.5
    )
    f.add_layout(
        Span(
            location=100 * page["threshold"],
            dimension="height",
            line_color=palette.NEUTRAL,
            line_dash="dashed",
            line_width=1,
        )
    )
    f.add_tools(
        HoverTool(
            renderers=[dots],
            tooltips=[
                ("lineage", "@y"),
                ("detected", "@det of @n"),
                ("share", "@share{0.0}%"),
                ("95% interval", "@lo{0.0}-@hi{0.0}%"),
            ],
        )
    )
    f.ygrid.grid_line_color = None
    return components(f)
