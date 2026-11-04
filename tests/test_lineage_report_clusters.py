"""The sequence-cluster view in lineage.md (ROADMAP composition step 13).

A second partition beside the taxid lineages, not a replacement for them: the per-year
blocks above it are grouped by `lineage.lineage_of`, the same function the table above
them and the verdict's own lineage check use, and that agreement is deliberate.
"""

from __future__ import annotations

from pathlib import Path

from assaywatch.composition import (
    DIVERGED,
    AssayComposition,
    Cell,
    Cluster,
    CompositionRun,
    SpeciesYear,
    Split,
)
from assaywatch.lineage_report import cluster_section, render_lineage_report


def _prose(comp) -> str:
    """The section as one line: the source wraps its sentences for width, so a prose
    assertion must not depend on where a line happens to break."""
    return " ".join("\n".join(cluster_section(comp)).split())


ROOT = Path(__file__).resolve().parents[1]


def _comp(**over) -> AssayComposition:
    """One assay whose detection fell because the mix swung, not because detection did."""
    base = {
        "assay_id": "A",
        "cut": 0.05,
        "left_bp": 9,
        "right_bp": 886,
        "clusters": (
            Cluster(0, "C. psittaci", 50, "AB1", (("Chlamydia psittaci", 50),), 115, ("avian",), 2011, False),
            Cluster(
                1, "C. trachomatis 60%", 30, "AB2", (("Chlamydia trachomatis", 18),), 813, (), 2021, True
            ),
            Cluster(DIVERGED, "diverged (no site)", 4, "AB3", (), None, (), 2019, False),
        ),
        "cells": (
            Cell(2018, 0, 40, 38, 0),
            Cell(2018, 1, 4, 1, 0),
            Cell(2025, 0, 10, 9, 10),
            Cell(2025, 1, 26, 5, 26),
            Cell(2025, DIVERGED, 4, 0, 4),
        ),
        "observed": {2018: 0.886, 2025: 0.35},
        "same_mix": {2018: 0.72, 2025: 0.70},
        "split": Split(0.886, 0.35, -0.536, -0.52, -0.016, (-0.6, -0.44), (-0.05, 0.02), 2000, (1,)),
        "species": (SpeciesYear(115, "Chlamydia psittaci", 2011, 50, False),),
        "note": "4 of 84 diverged, with no site to cluster on",
    }
    return AssayComposition(**{**base, **over})


def test_the_section_shows_both_the_year_s_own_share_and_the_same_mix_one():
    out = "\n".join(cluster_section(_comp()))
    assert "| 2018 | 44 | 39 | 88.6% | 72.0% |" in out
    assert "| 2025 | 40 | 14 | 35.0% | 70.0% |" in out


def test_the_section_says_how_much_of_the_change_was_the_mix():
    out = _prose(_comp())
    assert "-0.520 is the mix** of clusters deposited changing" in out
    assert "-0.016 is detection within** them" in out
    assert "95% CI -0.600 to -0.440" in out


def test_the_interval_says_what_it_does_not_price():
    """The bootstrap resamples records; the cut, the sample and the labels are given.
    A reader must not take the interval for uncertainty about the clustering."""
    assert "clustering itself is taken as given and carries no interval here" in _prose(_comp())


def test_a_year_whose_clusters_cover_too_little_is_not_given_a_same_mix_number():
    out = "\n".join(cluster_section(_comp(same_mix={2018: 0.72})))
    assert "| 2025 | 40 | 14 | 35.0% | -- |" in out


def test_a_lineage_in_one_period_only_is_explained_rather_than_left_odd():
    out = _prose(_comp())
    assert "1 cluster(s) appear in one period only" in out
    assert "has no detection rate to have changed" in out


def test_the_cluster_table_carries_names_tokens_and_what_is_new():
    out = "\n".join(cluster_section(_comp()))
    assert "| C. psittaci | 50 | 47 | 2011 |  | avian |" in out
    assert "| C. trachomatis 60% | 30 | 6 | 2021 | yes | -- |" in out
    assert "| diverged (no site) | 4 | 0 |" in out


def test_the_section_says_the_lineages_are_not_taxids():
    """The whole hazard of a second partition in one document: a reader who takes these
    rows for the taxid rows above them would cross-read two different groupings."""
    out = _prose(_comp())
    assert "Lineages here are SEQUENCE CLUSTERS" in out and "not taxids" in out
    assert "oligo sites masked" in out


def test_without_a_composition_run_the_report_is_what_it_was():
    calls = {"A": [{"assay_id": "A", "record_id": "AB1.1", "call": "detect"}]}
    before = render_lineage_report(calls, {}, {}, min_records=1)
    after = render_lineage_report(calls, {}, {}, min_records=1, composition=CompositionRun("2026-01-01", {}))
    assert before == after
    assert "Sequence clusters" not in before


def test_the_section_appears_under_its_own_assay_and_no_other():
    calls = {
        "A": [{"assay_id": "A", "record_id": "AB1.1", "call": "detect"}],
        "B": [{"assay_id": "B", "record_id": "AB2.1", "call": "detect"}],
    }
    run = CompositionRun("2026-01-01", {"A": _comp()})
    out = render_lineage_report(calls, {}, {}, min_records=1, composition=run)
    assert out.count("#### Sequence clusters, per deposit year") == 1
    assert out.index("## A") < out.index("#### Sequence clusters") < out.index("## B")
