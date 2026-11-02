"""The figures must render from the same numbers the documents carry, and must
still render when there is nothing to draw: a run with no evaluable record still
has to produce its declared outputs, and an empty file is not a valid SVG."""

import re

import pytest

from assaywatch.drift import AssayDrift, newcombe_difference, wilson_interval
from assaywatch.figures import forest, forest_rows, site_positions
from assaywatch.report import read_figures, render_html
from assaywatch.sitedrift import AssaySites, PositionStat

FWD = "ACCAKGGMTGCAATRGGTTT"  # K, M and R are degenerate
REV = "TTGTCRCCGTAGATGGTCAT"


def mk_drift(aid, status, rd, rn, bd, bn, *, threshold=0.9, min_decline=0.05, clustered=None):
    d = AssayDrift(assay_id=aid)
    d.status = status
    d.threshold = threshold
    d.min_decline = min_decline
    d.recent_detected, d.recent_evaluable = rd, rn
    d.baseline_detected, d.baseline_evaluable = bd, bn
    d.recent_ci = wilson_interval(rd, rn)
    d.baseline_ci = wilson_interval(bd, bn)
    d.change_ci = newcombe_difference(rd, rn, bd, bn)
    d.change_ci_clustered = clustered if clustered is not None else d.change_ci
    if clustered is not None:
        d.flag_survives_clustering = False
    return d


def mk_sites(assay_id="A1", status="declining", seqs=None):
    seqs = seqs or {"forward": FWD, "reverse": REV}
    positions = []
    for oligo, seq in seqs.items():
        for p5, (dw, ew, dwo, ewo) in {4: (70, 90, 92, 95), len(seq): (9, 44, 96, 99)}.items():
            positions.append(
                PositionStat(
                    oligo=oligo,
                    pos_3prime=len(seq) - p5 + 1,
                    pos_5prime=p5,
                    base=seq[p5 - 1],
                    n_mismatch=ew,
                    detected_with=dw,
                    evaluable_with=ew,
                    detected_without=dwo,
                    evaluable_without=ewo,
                )
            )
    return AssaySites(
        assay_id=assay_id,
        taxon="Canine morbillivirus",
        taxid=11232,
        status=status,
        oligo_seqs=seqs,
        positions=positions,
        footprints=[],
        n_evaluable=420,
        n_rows=460,
    )


def test_forest_renders_one_row_per_assay_with_its_status_colour():
    from assaywatch.report import STATUS_COLOUR

    drifts = {
        "D": mk_drift("D", "declining", 61, 100, 94, 100),
        "S": mk_drift("S", "stable", 980, 1000, 1180, 1200),
    }
    svg = forest(drifts)
    assert svg.startswith("<svg")
    for aid in drifts:
        assert aid in svg
    # Colours come from the report's map, so the figure and the tables cannot
    # disagree about what declining looks like.
    for status in ("declining", "stable"):
        assert STATUS_COLOUR[status].lstrip("#").lower() in svg.lower()


def test_the_svg_root_is_left_plain_so_any_rasteriser_can_read_it():
    """These are declared pipeline outputs, so they get converted to PNG and PDF.
    An inline `style="max-width:100%"` makes the file responsive in a browser and
    renders it blank in cairosvg; the pages that embed it size it with their own
    CSS instead. A viewBox has to survive for that CSS to have an aspect ratio to
    work from."""
    svg = forest({"D": mk_drift("D", "declining", 61, 100, 94, 100)})
    assert "viewBox" in svg
    assert "max-width" not in svg.split(">", 1)[0]


def test_the_figure_carries_no_build_date():
    """A date would make every run's HTML differ even when the numbers do not,
    which would make a committed figure impossible to diff."""
    svg = forest({"D": mk_drift("D", "declining", 61, 100, 94, 100)})
    assert not re.search(r"<dc:date>|metadata.*\d{4}-\d{2}-\d{2}T", svg)


def test_forest_rows_put_the_worst_first_and_the_cap_keeps_them():
    drifts = {
        "stable1": mk_drift("stable1", "stable", 99, 100, 99, 100),
        "declining1": mk_drift("declining1", "declining", 50, 100, 95, 100),
        "watch1": mk_drift("watch1", "watch", 85, 100, 95, 100),
    }
    assert [d.assay_id for d in forest_rows(drifts)] == ["declining1", "watch1", "stable1"]
    # The cut keeps the rows a reader opened the figure for, not an arbitrary slice.
    assert [d.assay_id for d in forest_rows(drifts, limit=1)] == ["declining1"]


def test_an_assay_with_no_recent_window_is_not_a_row():
    """Plotting a Wilson interval on a zero denominator would draw the full axis
    and read as an assay that detects anything, which is the opposite of the truth."""
    drifts = {"none": mk_drift("none", "no recent data", 0, 0, 90, 100)}
    assert forest_rows(drifts) == []
    assert forest(drifts).startswith("<svg")  # still a valid figure


@pytest.mark.parametrize(
    "call, args",
    [(forest, ({},)), (site_positions, ([],))],
)
def test_nothing_to_draw_still_gives_a_valid_figure(call, args):
    svg = call(*args)
    assert svg.startswith("<svg") and svg.rstrip().endswith("</svg>")


def test_site_positions_labels_the_axis_with_the_oligo_sequence():
    """The base letters are the axis: a position is actionable only if you can
    read which base it is without going back to the registry."""
    svg = site_positions([mk_sites()])
    assert svg.startswith("<svg")
    assert "A1" in svg and "forward" in svg
    # The degenerate bases are called out in amber, which is how the figure says
    # "the design already covers this one".
    assert "#b26a00" in svg.lower() or "b26a00" in svg.lower()


def test_site_positions_skips_an_assay_with_no_reported_position():
    bare = mk_sites()
    bare.positions = []
    assert site_positions([bare]).startswith("<svg")


def test_read_figures_tolerates_a_missing_directory(tmp_path):
    """`python -m assaywatch.report` is run by hand without figures, and the
    tests render the page with none; a missing directory is not an error."""
    assert read_figures(None) == {}
    assert read_figures(tmp_path / "nope") == {}
    (tmp_path / "forest.svg").write_text("<svg/>")
    assert read_figures(tmp_path) == {"forest.svg": "<svg/>"}


def test_the_page_inlines_the_figures_it_is_given_and_is_complete_without_them():
    drifts = {"D": mk_drift("D", "declining", 61, 100, 94, 100)}
    without = render_html(drifts, {}, [], "2026-10-20")
    assert "Detection against threshold" not in without
    assert without.rstrip().endswith("</html>")

    with_figs = render_html(drifts, {}, [], "2026-10-20", figures={"forest.svg": "<svg id='forest'/>"})
    assert "<svg id='forest'/>" in with_figs
    assert "Detection against threshold" in with_figs
