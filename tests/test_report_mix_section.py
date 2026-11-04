"""The report's "Where the mix moved the graph" section (ROADMAP composition step 14).

A lens beside the verdict, like the collection-year rows: it names the assays whose
per-year graph moved because a different mix of lineages was deposited, and it moves no
status. The bar is `composition.report_min_mix` AND an interval excluding zero.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from assaywatch.composition import AssayComposition, Cell, Cluster, CompositionRun, Split
from assaywatch.report import (
    MixRow,
    build_model,
    html_from,
    markdown_from,
    mix_rows,
    mix_section_md,
)

ROOT = Path(__file__).resolve().parents[1]
CFG = yaml.safe_load((ROOT / "config.yaml").read_text())


def _assay(mix: float, within: float, ci: tuple[float, float] | None, **over) -> AssayComposition:
    base = {
        "assay_id": "A",
        "cut": 0.05,
        "left_bp": 9,
        "right_bp": 886,
        "clusters": (
            Cluster(0, "C. psittaci", 44, "AB1", (("Chlamydia psittaci", 44),), 115, (), 2011, False),
            Cluster(1, "C. trachomatis", 30, "AB2", (("Chlamydia trachomatis", 30),), 813, (), 2021, True),
        ),
        # cluster 0 is most of the baseline, cluster 1 most of the recent window
        "cells": (
            Cell(2018, 0, 40, 38, 0),
            Cell(2018, 1, 4, 1, 0),
            Cell(2025, 0, 10, 9, 10),
            Cell(2025, 1, 26, 5, 26),
        ),
        "observed": {2018: 0.886, 2025: 0.389},
        "same_mix": {2018: 0.72, 2025: 0.70},
        "split": Split(0.886, 0.389, -0.497, mix, within, ci, (-0.05, 0.02), 2000, ()),
        "species": (),
        "note": "",
    }
    return AssayComposition(**{**base, **over})


def _run(*assays: AssayComposition) -> CompositionRun:
    return CompositionRun("2026-11-01", {a.assay_id: a for a in assays})


def test_an_assay_whose_mix_moved_is_named():
    rows = mix_rows(_run(_assay(-0.48, -0.017, (-0.60, -0.36))), CFG)
    assert [r.assay_id for r in rows] == ["A"]
    assert rows[0].mix == -0.48


def test_a_mix_part_below_the_threshold_is_not_named():
    """`report_min_mix` is 0.05, matching `drift.min_decline`: the size of change the
    verdict already treats as worth naming."""
    assert mix_rows(_run(_assay(-0.02, -0.4, (-0.03, -0.01))), CFG) == []


def test_a_mix_part_whose_interval_straddles_zero_is_not_named():
    """It has not been shown to have moved, and saying so anyway is the mistake this
    whole document exists not to make."""
    assert mix_rows(_run(_assay(-0.48, -0.017, (-0.60, 0.04))), CFG) == []
    assert mix_rows(_run(_assay(-0.48, -0.017, None)), CFG) == []


def test_an_assay_with_no_split_is_not_named():
    assert mix_rows(_run(_assay(0, 0, None, split=None)), CFG) == []


def test_the_worst_mix_part_comes_first():
    small = _assay(-0.10, 0.0, (-0.14, -0.06))
    big = _assay(-0.40, 0.0, (-0.50, -0.30), assay_id="B")
    assert [r.assay_id for r in mix_rows(_run(small, big), CFG)] == ["B", "A"]


def test_the_row_names_the_cluster_that_moved_most():
    """What a reader should go and look at: the baseline was 91% cluster 0, the recent
    window is 72% cluster 1."""
    row = mix_rows(_run(_assay(-0.48, -0.017, (-0.60, -0.36))), CFG)[0]
    assert row.mover == "C. trachomatis"
    assert (round(row.mover_from, 2), round(row.mover_to, 2)) == (0.09, 0.72)


def test_an_assay_with_one_cluster_says_so_rather_than_inventing_a_mover():
    one = _assay(
        -0.48,
        -0.017,
        (-0.60, -0.36),
        clusters=(Cluster(0, "C. psittaci", 80, "AB1", (), None, (), 2011, False),),
    )
    row = mix_rows(_run(one), CFG)[0]
    assert row.mover == ""
    assert "one cluster only" in " ".join(mix_section_md([row], 0.05))


def test_both_serialisers_print_the_section_and_say_what_it_is_not():
    rows = mix_rows(_run(_assay(-0.48, -0.017, (-0.60, -0.36))), CFG)
    model = build_model({}, {}, [], "2026-11-01", cfg=CFG, composition_mix=rows)
    md = markdown_from(model, {}, CFG)
    page = html_from(model)
    for out in (" ".join(md.split()), " ".join(page.split())):
        assert "Where the mix moved the graph" in out
        assert "Nothing in this section moves a status" in out
        assert "not the clustering, which is taken as given" in out
        # content, not escaping: html_from escapes the quotes and the arrow
        assert "C. trachomatis" in out and "9%" in out and "72% of records" in out


def test_without_a_composition_run_neither_serialiser_mentions_it():
    model = build_model({}, {}, [], "2026-11-01", cfg=CFG)
    assert "mix moved" not in markdown_from(model, {}, CFG)
    assert "composition-mix" not in html_from(model)


def test_the_two_parts_printed_still_add_to_the_change():
    """The identity is what makes the row readable; a reader adds the two columns."""
    row = mix_rows(_run(_assay(-0.48, -0.017, (-0.60, -0.36))), CFG)[0]
    assert round(row.mix + row.within, 3) == round(row.change, 3)
    assert isinstance(row, MixRow)
