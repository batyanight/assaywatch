"""Report rendering, including the accession join that is easy to get silently wrong."""

import gzip
from datetime import date
from pathlib import Path

from test_drift import CFG, TODAY, records

from assaywatch.drift import assess
from assaywatch.report import (
    build,
    key_calls_by_accession,
    read_years,
    render_html,
    render_markdown,
    sparkline,
    strip_version,
)

ROOT = Path(__file__).resolve().parents[1]


def test_version_suffix_is_stripped_but_a_dotted_name_is_not():
    """FASTA ids carry a version; esummary captions do not. The join needs both forms."""
    assert strip_version("AB123456.2") == "AB123456"
    assert strip_version("AB123456") == "AB123456"
    assert strip_version("AB123456.1 Bd isolate 5 ITS") == "AB123456"
    assert strip_version("NC_001.2.3") == "NC_001.2"
    assert strip_version("scaffold.contig") == "scaffold.contig"  # not a version


def test_calls_are_deduplicated_to_one_row_per_accession():
    rows = [
        {"assay_id": "A", "record_id": "AB1.1", "call": "fail"},
        {"assay_id": "A", "record_id": "AB1.2", "call": "detect"},
        {"assay_id": "B", "record_id": "AB1.2", "call": "detect"},
    ]
    out = key_calls_by_accession(rows)
    assert len(out) == 2  # one per (assay, accession)
    assert {r["record_id"] for r in out} == {"AB1"}


def test_read_years_prefers_the_latest_revision(tmp_path):
    d = tmp_path / "109871"
    d.mkdir(parents=True)

    def write(name, rows):
        with gzip.open(d / name, "wt") as fh:
            fh.write("uid\taccession\tcreated\tupdated\tlength\ttitle\n")
            for r in rows:
                fh.write("\t".join(r) + "\n")

    write("2025-01-01.meta.tsv.gz", [("1", "AB1", "2014-01-01", "2014-01-01", "500", "old")])
    write("2026-01-01.meta.tsv.gz", [("1", "AB1", "2014-01-01", "2026-01-01", "500", "revised")])
    assert read_years(tmp_path) == {"AB1": 2014}  # creation year, not revision year


def test_read_years_skips_rows_with_no_usable_date(tmp_path):
    d = tmp_path / "1"
    d.mkdir(parents=True)
    with gzip.open(d / "2026-01-01.meta.tsv.gz", "wt") as fh:
        fh.write("uid\taccession\tcreated\tupdated\tlength\ttitle\n")
        fh.write("1\tAB1\t\t2026-01-01\t500\tno date\n")
    assert read_years(tmp_path) == {}


def _drifting():
    calls, years = records({2019: {"detect": 120}, 2025: {"detect": 15, "fail": 35}})
    return assess(calls, years, CFG, today=TODAY)


def test_markdown_puts_drifting_assays_first_and_shows_the_interval():
    md = render_markdown(_drifting(), {}, [], "2026-10-03")
    assert md.index("## Declining") < md.index("## Coverage gaps")
    assert "95% CI" in md and "upper bound below" in md


def test_markdown_explains_the_denominator():
    md = render_markdown(_drifting(), {}, [], "2026-10-03")
    assert "evaluable records only" in md
    assert "cannot look like drift" in md


def test_html_is_self_contained():
    page = render_html(_drifting(), {}, [], "2026-10-03")
    assert "<svg" in page and "<style>" in page
    for forbidden in ("http://", "https://", "<script"):
        assert forbidden not in page, f"report must not depend on {forbidden}"


def test_html_escapes_assay_text():
    drifts = _drifting()
    drifts["A"].note = "<script>alert(1)</script>"
    page = render_html(drifts, {}, [], "2026-10-03")
    assert "<script>alert(1)" not in page and "&lt;script&gt;" in page


def test_sparkline_needs_two_years():
    calls, years = records({2025: {"detect": 30}})
    one = assess(calls, years, CFG, today=TODAY)["A"]
    assert "not enough years" in sparkline(one)
    assert "<polyline" in sparkline(_drifting()["A"])


def test_build_end_to_end_against_the_real_registry(tmp_path):
    """A full render over fixture calls, joined to fabricated deposit years."""
    retrieved = tmp_path / "retrieved" / "109871"
    retrieved.mkdir(parents=True)
    calls_path = tmp_path / "calls.tsv"

    assay_id = "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004"
    rows = [("assay_id", "record_id", "call")]
    meta = []
    for i in range(60):
        acc = f"AB{i:05d}"
        year = 2019 if i < 30 else 2025
        call = "detect" if (year == 2019 or i % 5 == 0) else "fail"
        rows.append((assay_id, f"{acc}.1", call))
        meta.append((str(i), acc, f"{year}-03-01", f"{year}-03-01", "500", "t"))
    calls_path.write_text("\n".join("\t".join(r) for r in rows) + "\n")
    with gzip.open(retrieved / "2026-10-03.meta.tsv.gz", "wt") as fh:
        fh.write("uid\taccession\tcreated\tupdated\tlength\ttitle\n")
        for m in meta:
            fh.write("\t".join(m) + "\n")

    md, page, drifts = build(
        calls_path,
        ROOT / "registry",
        tmp_path / "retrieved",
        CFG,
        run_date="2026-10-03",
        today=date(2026, 10, 3),
    )
    a = drifts[assay_id]
    assert a.status == "declining" and a.recent_evaluable == 30
    assert assay_id in md and assay_id in page
    assert "Boyle" in md or "ITS1" in md  # the assay's name reached the report
    assert "deposit year" in md  # the per-year detail table rendered


def test_coverage_gap_section_names_the_taxon(tmp_path):
    md, page, _ = build(
        _write_empty_calls(tmp_path),
        ROOT / "registry",
        tmp_path / "retrieved_empty",
        CFG,
        run_date="2026-10-03",
        today=date(2026, 10, 3),
    )
    assert "Coverage gaps" in md
    assert "Batrachochytrium dendrobatidis" in md


def _write_empty_calls(tmp_path: Path) -> Path:
    p = tmp_path / "calls.tsv"
    p.write_text("assay_id\trecord_id\tcall\n")
    (tmp_path / "retrieved_empty").mkdir(exist_ok=True)
    return p


def test_gap_table_separates_unsearched_assays_and_skips_deprecated():
    from assaywatch.report import render_markdown

    gaps = [
        {"assay_id": "A_searched", "taxid": 5, "taxon_name": "X", "evaluable": 0, "screened": 3},
        {"assay_id": "B_no_taxid", "taxid": None, "taxon_name": "Y", "evaluable": 0, "screened": 0},
    ]
    md = render_markdown({}, {}, gaps, "2026-10-04")
    assert "| `A_searched` | X | 5 | 0 | 3 |" in md
    assert "| `B_no_taxid` | Y | - | 0 | not searched (no taxid) |" in md


def test_identical_oligo_sets_are_named_and_html_has_the_year_detail():
    from assaywatch.report import oligo_twins
    from assaywatch.validate import load_assay

    root = Path(__file__).resolve().parents[1]
    assays = {a.id: a for a in (load_assay(p) for p in (root / "registry").glob("POLYOMAVIRUS_dsDNA_*.yaml"))}
    twins = oligo_twins(assays)
    assert "POLYOMAVIRUS_dsDNA_VP1_Johne_2005" in twins.get("POLYOMAVIRUS_dsDNA_PREDICT_VP1_round2", [])
    page = render_html(_drifting(), {}, [], "2026-10-03")
    assert "<details>" in page and "deposit year" in page and "baseline (n)" in page


def test_an_unlisted_status_still_appears_in_both_reports():
    """A status missing from STATUS_ORDER is not an error, it is an assay that
    silently vanishes from the report while the headline still counts it.

    `AssayDrift` defaults to "no data", unreachable through `assess` today but
    exactly what a future status would look like, and until now it would have
    been dropped from the markdown, the HTML and the stderr summary alike.
    """
    from assaywatch.drift import AssayDrift
    from assaywatch.report import STATUS_ORDER, status_order

    odd = AssayDrift("ODD_assay")
    assert odd.status == "no data" and odd.status not in STATUS_ORDER
    drifts = {"ODD_assay": odd, **_drifting()}

    md = render_markdown(drifts, {}, [], "2026-10-05")
    assert "ODD_assay" in md and "No Data (1)" in md
    page = render_html(drifts, {}, [], "2026-10-05")  # must not KeyError on the colour lookup
    assert "ODD_assay" in page

    # Listed statuses keep their order, unknown ones follow, and the list is stable.
    order = status_order({"zzz": [], "no data": [], "stable": []})
    assert order[: len(STATUS_ORDER)] == STATUS_ORDER
    assert order[len(STATUS_ORDER) :] == ["no data", "zzz"]


def test_the_headline_count_matches_the_sections_beneath_it():
    """The symptom of a dropped status: "N assays screened" with fewer than N
    appearing below."""
    from assaywatch.drift import AssayDrift

    odd = AssayDrift("ODD_assay")
    drifts = {"ODD_assay": odd, **_drifting()}
    md = render_markdown(drifts, {}, [], "2026-10-05")
    headline = md.splitlines()[2]
    assert f"{len(drifts)} assays screened" in headline
    assert "1 no data" in headline, headline


def _registry_assays(ids):
    from assaywatch.validate import load_assay

    return {i: load_assay(ROOT / "registry" / f"{i}.yaml") for i in ids}


def test_the_header_says_how_much_of_the_registry_is_draft():
    """210 of 214 entries are drafts, and the table presented them like the one active assay."""
    calls, years = records({2015: {"detect": 100}, 2025: {"detect": 20, "fail": 30}})
    bd = "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004"
    drifts = {bd: assess(calls, years, CFG, today=TODAY)["A"]}
    drifts[bd].assay_id = bd
    assays = _registry_assays([bd])
    md = render_markdown(drifts, assays, [], "2026-10-07", CFG)
    page = render_html(drifts, assays, [], "2026-10-07", CFG)
    assert "Registry status:" in md and f"1 {assays[bd].status.value}" in md
    assert "Registry status:" in page
    # and the per-assay row carries it too
    assert f"| {assays[bd].status.value} |" in md


def test_the_duplication_result_is_beside_the_flag_counts_not_only_below_them():
    """The counts a reader takes away are at the top; so is the caveat that qualifies them."""
    calls, years = records({2015: {"detect": 100}, 2025: {"detect": 20, "fail": 30}})
    bd = "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004"
    a = assess(calls, years, CFG, today=TODAY)["A"]
    a.assay_id = bd
    assert a.status == "declining"
    md = render_markdown({bd: a}, _registry_assays([bd]), [], "2026-10-07", CFG)
    head = md.split("## ")[0]
    assert "Duplication check:" in head


def test_a_family_that_does_not_nest_gets_no_conditional_figure():
    """The note refuses to report one; the table must not print it either.

    The coronavirus pair's amplicons are about 2.7 kb apart, so a 'run as a
    nest' percentage for it would be exactly the invented number the note says
    it is withholding.
    """
    from assaywatch.nested import NestedFamily
    from assaywatch.report import nested_section

    f = NestedFamily(
        "CORONA",
        ["CORONA", "CORONA_round2"],
        outer="CORONA",
        inner="CORONA_round2",
        records=100,
        outer_detected=39,
        inner_detected=70,
        both_detected=22,
        containment={("CORONA", "CORONA_round2"): (0, 100)},
    )
    out = "\n".join(nested_section({"CORONA": f}, {}, 0.90))
    assert f.nests is False
    assert "22%" not in out, "no conditional coverage for a family that does not nest"
    assert "not a nest" in out
    assert "do not nest" in out


def test_lineage_override_shows_pooled_status():
    """When lineage analysis overrides a status, both renderers show the pooled status."""
    drifts = _drifting()
    a = drifts["A"]
    a.lineage_override = True
    a.status_pooled = "stable"
    md_text = render_markdown(drifts, {}, [], "2026-10-03")
    page = render_html(drifts, {}, [], "2026-10-03")
    # Main table: pooled tag next to assay id
    assert "(pooled: stable)" in md_text
    assert "pooled: stable" in page
    # Detail section
    assert "pooled status was stable" in md_text
    assert "Lineage override:" in page


def test_no_pooled_tag_without_lineage_override():
    md_text = render_markdown(_drifting(), {}, [], "2026-10-03")
    assert "(pooled:" not in md_text
    assert "Lineage override:" not in md_text


def test_species_table_lists_every_species_biggest_first_with_no_floor():
    """A size-differentiating assay's rare species are the point, so nothing is dropped."""
    from assaywatch.report import species_table_rows
    from assaywatch.schema import SpeciesSize
    from assaywatch.taxonomy import Taxonomy

    a = assess(*records({2025: {"detect": 1}}), CFG, today=TODAY)["A"]
    a.species_counts = {3431483: [4143, 4334], 10245: [93, 112], 3431480: [1, 1], None: [2, 5]}
    tree = Taxonomy({}, {}, {}, {10245: "Orthopoxvirus vaccinia", 3431483: "Orthopoxvirus monkeypox"})
    # Two bands for one species (monkeypox by clade) and a single-length band.
    sizes = [
        SpeciesSize(taxid=3431483, bp=[1535, 1545], n_records=9113),
        SpeciesSize(taxid=3431483, bp=[1067, 1067], n_records=1981),
        SpeciesSize(taxid=3431480, bp=[879, 879], n_records=12),
    ]
    assert species_table_rows(a, tree, sizes) == [
        ("Orthopoxvirus monkeypox (3431483)", 4143, 4334, "96%", "1535-1545, 1067"),
        # Measured records but no declared band: the column says so.
        ("Orthopoxvirus vaccinia (10245)", 93, 112, "83%", "-"),
        ("unresolved (no taxid)", 2, 5, "40%", "-"),
        # Named by nothing in the tree, and a single record: still listed.
        ("taxid 3431480", 1, 1, "100%", "879"),
    ]


def test_species_table_is_empty_without_lineage_counts():
    from assaywatch.report import species_table_rows

    a = assess(*records({2025: {"detect": 1}}), CFG, today=TODAY)["A"]
    assert a.species_counts is None and species_table_rows(a) == []


# The report model (S3). Both renderers were 356 lines of parallel layout, so
# every change was made twice and the two drifted - which is what
# scripts/report_diff.py was left parsing. The model decides a row's CONTENT
# once; each serialiser only formats it. These tests assert on the content
# without parsing any markup, which is what neither renderer allowed before.
def test_the_model_carries_values_not_formatted_text():
    """A share is a float here. `-` for "nothing to show" is a format's business."""
    from assaywatch.report import build_model

    m = build_model(_drifting(), {}, [], "2026-10-03")
    (status, rows) = m.sections[0]
    assert status == "declining"
    assert isinstance(rows[0].fraction, float)
    assert isinstance(rows[0].ci, tuple) and len(rows[0].ci) == 2
    assert isinstance(rows[0].evaluable, int)


def test_a_row_with_nothing_recent_carries_none_not_a_dash():
    from assaywatch.drift import AssayDrift
    from assaywatch.report import build_model

    m = build_model({"ODD": AssayDrift("ODD")}, {}, [], "2026-10-03")
    row = m.sections[0][1][0]
    assert row.ci is None and row.baseline is None and row.degeneracy is None


def test_both_serialisers_render_the_same_model_and_agree_on_the_numbers():
    """The drift the model exists to prevent: one report saying 30.0% and the
    other 30%, or one counting an assay the other dropped."""
    from assaywatch.report import build_model, html_from, markdown_from

    m = build_model(_drifting(), {}, [], "2026-10-03")
    md, page = markdown_from(m, {}), html_from(m)
    for status, rows in m.sections:
        assert f"({len(rows)})" in md or status.title() in md
        for r in rows:
            assert r.assay_id in md and r.assay_id in page
            assert f"{r.fraction:.1%}" in md and f"{r.fraction:.1%}" in page
            assert str(r.evaluable) in md and str(r.evaluable) in page


def test_the_renderers_are_the_model_plus_formatting():
    """render_markdown / render_html are now thin wrappers; same output either way."""
    from assaywatch.report import build_model, html_from, markdown_from, render_html, render_markdown

    drifts = _drifting()
    args = (drifts, {}, [], "2026-10-03")
    m = build_model(*args)
    assert render_markdown(*args) == markdown_from(m, {})
    assert render_html(*args) == html_from(m)


def test_the_note_is_assembled_once_for_both_formats():
    """Out-of-scope and patent exclusions used to be appended to the note in each
    renderer separately, in text that had to match."""
    from assaywatch.report import build_model, html_from, markdown_from

    drifts = _drifting()
    a = next(iter(drifts.values()))
    a.out_of_scope, a.patent_excluded = 7, 3
    m = build_model(drifts, {}, [], "2026-10-03")
    row = m.sections[0][1][0]
    assert "7 out-of-scope records excluded." in row.note
    assert "3 patent records excluded." in row.note
    assert row.note in markdown_from(m, {}) and row.note in html_from(m)


def test_the_withheld_nested_share_rule_is_shared_by_both_tables():
    """`not a nest` where the amplicons do not nest, and the bold `no` cell: one
    rule, two emphasis markups."""
    from assaywatch.report import NestedRow, _nested_cells

    not_nesting = NestedRow("FAM", 0.9, 0.8, 0.7, False, 100, (3, 100))
    nesting = NestedRow("FAM", 0.9, 0.8, 0.7, True, 100, (100, 100))
    assert _nested_cells(not_nesting, bold="**no**") == ("**no** (3/100)", "not a nest")
    assert _nested_cells(not_nesting, bold="<b>no</b>") == ("<b>no</b> (3/100)", "not a nest")
    assert _nested_cells(nesting, bold="**no**") == ("yes", "70%")
    # Containment not measured: no record was scored by both rounds. The share is
    # still printed, because a row only reaches either table when records > 0 and
    # every share is then a float (NestedFamily._share is None only for 0 records).
    unmeasured = NestedRow("FAM", 0.9, 0.8, 0.7, None, 100, None)
    assert _nested_cells(unmeasured, bold="**no**") == ("-", "70%")


def test_the_model_counts_match_what_the_headline_claims():
    from assaywatch.report import build_model

    m = build_model(_drifting(), {}, [], "2026-10-03")
    assert sum(n for _, n in m.counts) == m.n_assays
    assert sum(len(rows) for _, rows in m.sections) == m.n_assays
