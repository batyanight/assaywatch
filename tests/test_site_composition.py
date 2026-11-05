"""The composition panel on the website (ROADMAP composition step 15).

Its own file beside `run.json`, its own cap, and a panel whose columns sit under the
detection chart's points. Report-only: no status on a page comes from any of it.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from assaywatch import site_svg
from assaywatch.composition import (
    DIVERGED,
    SITE_SCHEMA,
    AssayComposition,
    Cell,
    Cluster,
    CompositionRun,
    Split,
    site_data,
    write_site_data,
)
from assaywatch.site_render import _composition_block, _same_mix

ROOT = Path(__file__).resolve().parents[1]
CFG = yaml.safe_load((ROOT / "config.yaml").read_text())


def _assay(**over) -> AssayComposition:
    base = {
        "assay_id": "A",
        "cut": 0.05,
        "left_bp": 9,
        "right_bp": 886,
        "clusters": (
            Cluster(0, "C. psittaci", 50, "AB1", (("Chlamydia psittaci", 50),), 115, ("avian",), 2011, False),
            Cluster(1, "C. trachomatis", 30, "AB2", (("Chlamydia trachomatis", 30),), 813, (), 2021, True),
            Cluster(DIVERGED, "diverged (no site)", 4, "AB3", (), None, (), 2025, False),
        ),
        "cells": (
            Cell(2018, 0, 40, 38, 0),
            Cell(2018, 1, 4, 1, 0),
            Cell(2025, 0, 10, 9, 10),
            Cell(2025, 1, 26, 5, 26),
            Cell(2025, DIVERGED, 4, 0, 4),
        ),
        "observed": {2018: 0.886, 2025: 0.35},
        "same_mix": {2018: 0.72},
        "split": Split(0.886, 0.35, -0.536, -0.52, -0.016, (-0.6, -0.44), (-0.05, 0.02), 2000, ()),
        "species": (),
        "note": "4 of 84 diverged, with no site to cluster on",
    }
    return AssayComposition(**{**base, **over})


def _run(*assays: AssayComposition) -> CompositionRun:
    return CompositionRun("2026-11-01", {a.assay_id: a for a in assays})


# ---- the file ----


def test_the_site_file_is_columnar_and_aligned_by_index():
    d = site_data(_run(_assay()))["assays"]["A"]
    assert d["years"] == [2018, 2025]
    assert d["ids"] == [0, 1, DIVERGED]
    assert d["names"] == ["C. psittaci", "C. trachomatis", "diverged (no site)"]
    # one row per year, one column per cluster, in both grids
    assert d["records"] == [[40, 4, 0], [10, 26, 4]]
    assert d["detected"] == [[38, 1, 0], [9, 5, 0]]
    assert len(d["same_mix"]) == len(d["years"])


def test_a_year_that_could_not_be_standardised_is_null_not_missing():
    """Aligned by index, so a hole has to be a hole: a reader of the file can see which
    year was not drawn, where a shorter list would just be shorter."""
    d = site_data(_run(_assay()))["assays"]["A"]
    assert d["same_mix"] == [0.72, None]


def test_every_year_s_columns_sum_to_that_year_s_evaluable_and_detected():
    """The invariant, at the last place it could still break: what the site draws."""
    run = _run(_assay())
    d = site_data(run)["assays"]["A"]
    for row, year in enumerate(d["years"]):
        cells = [c for c in run.assays["A"].cells if c.year == year]
        assert sum(d["records"][row]) == sum(c.records for c in cells)
        assert sum(d["detected"][row]) == sum(c.detected for c in cells)


def test_the_file_carries_its_schema_so_the_renderer_can_refuse_an_old_one():
    assert site_data(_run(_assay()))["schema"] == SITE_SCHEMA


def test_the_cap_is_a_refusal_and_not_a_warning(tmp_path):
    """It is committed on every run, so a file that grew unnoticed would be noticed only
    in the repository's size."""
    run = _run(_assay())
    with pytest.raises(ValueError, match="site_max_bytes"):
        write_site_data(run, tmp_path, max_bytes=200)
    path = write_site_data(run, tmp_path, max_bytes=1_500_000)
    assert json.loads(path.read_text())["run_date"] == "2026-11-01"
    assert path.stat().st_size < 1_500_000


# ---- the panel ----


def _panel(comp=None) -> str:
    return site_svg.composition_panel(comp or site_data(_run(_assay()))["assays"]["A"], {})


def test_the_panel_draws_a_column_per_year_under_the_chart_s_own_axis():
    svg = _panel()
    assert svg.count("<rect") == 5  # one per non-empty cell
    assert "2018" in svg and "2025" in svg
    # the same plot box as year_chart, so a column sits under its year's point
    assert 'viewBox="0 0 720' in svg and 'viewBox="0 0 720' in site_svg.year_chart(
        {
            "years": [{"year": 2018, "detected": 38, "evaluable": 44, "share": 0.86, "recent": False}],
            "threshold": 0.9,
            "status": "stable",
            "window_months": 24,
            "recent_from": "Nov 2024",
        }
    )


def test_a_segment_says_what_it_is_and_how_much_of_the_year_it_was():
    svg = _panel()
    assert "2018 — C. psittaci: 40 of 44 records (91%), 38 detected" in svg
    assert "2025 — C. trachomatis: 26 of 40 records (65%), 5 detected" in svg


def test_what_the_clustering_could_not_place_is_hatched_rather_than_shaded():
    """It is not a lineage, and a shade would read as one."""
    svg = _panel()
    assert "aw-unplaced" in svg and "url(#aw-unplaced)" in svg


def test_an_assay_with_no_years_draws_nothing():
    assert _panel({"years": [], "records": []}) == ""


def test_the_panel_does_not_encode_detection_twice():
    """Lightness carries which cluster a segment is; asking a reader to read detection
    from the same channel would make both unreadable. Detection is the chart above, the
    tooltip here, and lineage.md."""
    svg = _panel()
    assert "opacity" in svg
    # no second geometry inside a segment
    assert svg.count("<rect") == 5


# ---- the chart and the page ----


def test_the_same_mix_line_is_drawn_only_where_the_year_could_be_standardised():
    page = {
        "years": [
            {"year": 2018, "detected": 38, "evaluable": 44, "share": 0.864, "recent": False},
            {"year": 2025, "detected": 14, "evaluable": 40, "share": 0.35, "recent": True},
        ],
        "threshold": 0.9,
        "status": "declining",
        "window_months": 24,
        "recent_from": "Nov 2024",
    }
    assert "aw-same-mix" not in site_svg.year_chart(page)
    assert "aw-same-mix" not in site_svg.year_chart(page, {2018: 0.72})  # one point is no line
    svg = site_svg.year_chart(page, {2018: 0.72, 2025: 0.70})
    assert "aw-same-mix" in svg
    assert "the mix moved rather than detection within it" in svg


def test_the_same_mix_helper_drops_the_years_it_could_not_standardise():
    comp = site_data(_run(_assay()))["assays"]["A"]
    assert _same_mix(comp) == {2018: 0.72}
    assert _same_mix(None) == {}


def test_the_page_block_says_the_lineages_are_sequence_clusters_and_moves_no_status():
    comp = site_data(_run(_assay()))["assays"]["A"]
    out = " ".join(" ".join(_composition_block(comp)).split())
    assert "sequence groups, not species or taxids" in out
    assert "come from sequence this assay does not measure" in out
    assert "it takes the clustering as given" in out
    assert "-0.520 is the mix" in out and "-0.016 is detection within" in out
    assert "| C. trachomatis | 30 | 36% | yes |" in out
    assert "4 of 84 diverged" in out


def test_a_mixed_largest_group_is_named_as_a_mix_on_the_page():
    """Single linkage chains species together: Messmer 16S at the 0.05 cut holds 14 species
    in one group, with detection differing between them (2026-11-04)."""
    comp = {
        "years": [2020],
        "cut": 0.05,
        "ids": [0, 1],
        "names": ["C. trachomatis 52%", "C. pecorum"],
        "records": [[687, 10]],
    }
    out = " ".join(" ".join(_composition_block(comp)).split())
    assert "The largest group here, C. trachomatis 52%, mixes species" in out
    assert "can't separate a shift between them" in out


def test_a_pure_largest_group_gets_no_warning_even_beside_a_mixed_small_one():
    comp = {
        "years": [2020],
        "cut": 0.05,
        "ids": [0, 1],
        "names": ["C. pecorum", "C. trachomatis 52%"],
        "records": [[687, 10]],
    }
    assert "mixes species" not in " ".join(_composition_block(comp))


def test_without_a_composition_file_the_page_block_is_empty():
    assert _composition_block(None) == []
    assert _composition_block({"years": []}) == []


def test_the_file_is_one_line_per_assay_so_its_diff_is_readable(tmp_path):
    """It is committed every run. A line per assay means a changed assay is a changed
    line; `indent=1` (what run.json uses) costs 2.6x the bytes on a dense numeric grid,
    and a fully compact file has a diff that says only "something changed"."""
    path = write_site_data(_run(_assay(), _assay(assay_id="B")), tmp_path, max_bytes=1_500_000)
    text = path.read_text()
    assert json.loads(text)["assays"].keys() == {"A", "B"}
    assert '  "A": {' in text and '  "B": {' in text
    assert sum(1 for line in text.splitlines() if line.startswith('  "')) == 2


def test_the_numbers_are_rounded_so_a_diff_is_about_a_change(tmp_path):
    run = _run(_assay(same_mix={2018: 0.7216666666666667}))
    d = json.loads(write_site_data(run, tmp_path, max_bytes=1_500_000).read_text())
    assert d["assays"]["A"]["same_mix"][0] == 0.7217


def test_the_table_says_which_species_each_group_holds():
    comp = {
        "years": [2020],
        "cut": 0.05,
        "ids": [0],
        "names": ["C. trachomatis 52%"],
        "records": [[687]],
        "mix": [
            [["Chlamydia trachomatis", 354], ["uncultured Chlamydia sp.", 104], ["Chlamydia psittaci", 66]]
        ],
    }
    out = " ".join(_composition_block(comp))
    assert "| Species |" in out
    assert "Chlamydia trachomatis 354, uncultured Chlamydia sp. 104, Chlamydia psittaci 66" in out
    assert "The table below shows which species each group holds" in out


def test_the_site_file_carries_each_group_s_top_species():
    d = site_data(_run(_assay()))["assays"]["A"]
    assert len(d["mix"]) == len(d["ids"])
    assert all(len(m) <= 3 for m in d["mix"])


def test_group_and_species_names_are_escaped_where_the_panel_already_escapes_them():
    """GenBank titles can reach here through `organism`, and Markdown passes raw HTML."""
    bad = '<img src=x onerror="location=name">'
    comp = {
        "years": [2020],
        "cut": 0.05,
        "ids": [0],
        "names": [bad + " 50%"],
        "records": [[10]],
        "mix": [[[bad, 5]]],
        "tokens": [[]],
    }
    out = " ".join(_composition_block(comp))
    assert "<img" not in out
    assert "&lt;img" in out


def test_a_pipe_in_a_name_does_not_break_the_table():
    comp = {"years": [2020], "cut": 0.05, "ids": [0], "names": ["A|B"], "records": [[10]]}
    assert "A&#124;B" in " ".join(_composition_block(comp))


def test_a_mixed_largest_group_keeps_its_warning_when_it_is_numbered():
    comp = {"years": [2020], "cut": 0.05, "ids": [0, 1], "names": ["X 38% 1", "X 38% 2"], "records": [[9, 1]]}
    assert "mixes species" in " ".join(_composition_block(comp))


def test_the_page_says_how_much_of_the_taxon_the_query_saw():
    comp = {
        "years": [2020],
        "cut": 0.05,
        "ids": [0],
        "names": ["X"],
        "records": [[10]],
        "coverage_years": [2020, 2023],
        "coverage_query": [157, 14],
        "coverage_taxon": [568, 3742],
    }
    out = " ".join(" ".join(_composition_block(comp)).split())
    assert "2020 28%" in out and "2023 0%" in out
    assert "the share its own retrieval query returned" in out


def test_a_cluster_s_shade_follows_its_rank_not_how_many_strata_precede_it():
    comp = {
        "years": [2020],
        "cut": 0.05,
        "ids": [-3, -2, -1, 0, 1],
        "names": ["d", "u", "o", "first", "second"],
        "records": [[1, 1, 1, 5, 2]],
        "detected": [[0, 0, 0, 0, 0]],
    }
    svg = site_svg.composition_panel(comp, {})
    assert f'opacity="{site_svg._CLUSTER_STEPS[0]:.2f}"' in svg
