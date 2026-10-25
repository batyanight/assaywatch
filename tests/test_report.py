"""Report rendering, including the accession join that is easy to get silently wrong."""

import gzip
import json
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
    # `<details id='detail-...'>` now, so a row above can link to it; a targeted
    # fragment opens the block, which is how the page is navigable with no script.
    assert "<details id='detail-" in page and "deposit year" in page and "baseline (n)" in page


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


def test_chance_pair_exclusions_are_disclosed_in_the_note():
    """A chance-pair removal has to show up where a reader sees the share.

    The per-assay `Why:` breakdown that names `chance_anchor` is only written for
    assays with a detail section, so when
    OPHIDIOMYCES_ophidiicola_targetD_Haynes_2023 went 42.2% -> 100.0% on
    2026-10-25 it became `stable` and printed as a bare "100.0%, 81 evaluable" -
    the largest correction in that report was the least visible thing in it.
    """
    from assaywatch.report import build_model, html_from, markdown_from

    drifts = _drifting()
    a = next(iter(drifts.values()))
    a.exclusions["chance_pair"] = 111
    m = build_model(drifts, {}, [], "2026-10-03")
    row = m.sections[0][1][0]
    assert "111 chance-pair records excluded (drift.chance_pair_test)." in row.note
    assert row.note in markdown_from(m, {}) and row.note in html_from(m)


def test_no_chance_pair_note_when_none_were_excluded():
    """The knob ships on, so every assay's note would otherwise carry a zero."""
    from assaywatch.report import build_model

    drifts = _drifting()
    m = build_model(drifts, {}, [], "2026-10-03")
    assert "chance-pair" not in m.sections[0][1][0].note


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


def _assay(assay_id: str):
    """One real registry entry, by id."""
    from assaywatch.validate import load_assay

    return load_assay(ROOT / "registry" / f"{assay_id}.yaml")


def test_an_unscoreable_chemistry_gets_no_status_in_either_report():
    """`not_screenable` was defined, carried by two entries, and honoured nowhere.

    `LMBV_dsDNA_MCP_RPA_Li_2025` says "the chemistry is RPA; the penalties are
    calibrated on PCR" and the 2026-10-22 report called it Stable, 100.0%: a
    false all-clear on an assay the registry says cannot be scored. The withheld
    status must not be printed either, or the caveat is just decoration.
    """
    drifts = _drifting()
    drifts["LMBV_dsDNA_MCP_RPA_Li_2025"] = drifts.pop("A")
    drifts["LMBV_dsDNA_MCP_RPA_Li_2025"].assay_id = "LMBV_dsDNA_MCP_RPA_Li_2025"
    assays = {"LMBV_dsDNA_MCP_RPA_Li_2025": _assay("LMBV_dsDNA_MCP_RPA_Li_2025")}

    md = render_markdown(drifts, assays, [], "2026-10-03")
    assert "## Not scoreable (1)" in md
    assert "`not_screenable`" in md
    assert "calibrated on PCR" in md
    assert "## Declining" not in md, "an unscoreable assay must not reach a status table"
    assert "100.0%" not in md, "the withheld status must not be printed either"

    page = render_html(drifts, assays, [], "2026-10-03")
    assert "not scoreable" in page and "not_screenable" in page


def test_an_open_review_question_also_holds_the_status_back():
    """OPEN flags are questions a human has to answer, not disclosures.

    `Pan_mycoplasma_16S_All_Van_1992` carries `do_not_use` and was reported Low
    Coverage, 78.3%, while docs/validation-cases.tsv records van Kuppeveld 1994
    finding it working on 104 cell cultures with no false negatives.
    """
    drifts = _drifting()
    drifts["Pan_mycoplasma_16S_All_Van_1992"] = drifts.pop("A")
    drifts["Pan_mycoplasma_16S_All_Van_1992"].assay_id = "Pan_mycoplasma_16S_All_Van_1992"
    assays = {"Pan_mycoplasma_16S_All_Van_1992": _assay("Pan_mycoplasma_16S_All_Van_1992")}
    md = render_markdown(drifts, assays, [], "2026-10-03")
    assert "## Not scoreable (1)" in md
    assert "`do_not_use`" in md
    assert "## Declining" not in md


def test_a_recorded_caveat_does_not_hold_the_status_back_but_is_printed():
    """The complement, and it is what keeps the report usable.

    149 of 208 entries carry at least one review item, so holding them all back
    would empty the report. A recorded caveat is a disclosure about a scoreable
    entry -- but 24 of the 38 assays called `declining` on 2026-10-22 carried
    one casting doubt on the very oligos the claim rests on, and the report
    showed none of them.
    """
    drifts = _drifting()
    drifts["Pan_hemoparasite_cytochrome_c_Hellgren_2004"] = drifts.pop("A")
    drifts[
        "Pan_hemoparasite_cytochrome_c_Hellgren_2004"
    ].assay_id = "Pan_hemoparasite_cytochrome_c_Hellgren_2004"
    assay = _assay("Pan_hemoparasite_cytochrome_c_Hellgren_2004")
    caveats = {i.flag.value for i in assay.needs_review or [] if not i.flag.value.endswith("unresolved")}
    assert "oligos_not_in_cited_paper" in caveats, "fixture no longer carries the flag under test"

    md = render_markdown(drifts, {"Pan_hemoparasite_cytochrome_c_Hellgren_2004": assay}, [], "2026-10-03")
    assert "## Not scoreable" not in md, "a recorded caveat is a disclosure, not a defect"
    assert "## Declining" in md
    assert "Entry flags:" in md and "oligos_not_in_cited_paper" in md


def test_the_note_column_does_not_run_two_sentences_together():
    """The 2026-10-22 report printed "...a coverage gap, not drift 20251
    out-of-scope records excluded." -- at the exact point a reader is being told
    what was left out of the denominator."""
    from assaywatch.report import _note_for

    class A:
        note = "a coverage gap, not drift"
        assay_id = "X"
        out_of_scope = 20251
        patent_excluded = 0

    assert _note_for(A(), {}) == "a coverage gap, not drift. 20251 out-of-scope records excluded."


def test_the_draft_line_does_not_claim_drafts_are_unchecked():
    """It said a draft had not been checked "for a verified citation, taxid or
    submitter", which was false for 173 of the 205 drafts screened on
    2026-10-22. Counted through the validator's own gate so the report cannot
    describe a different rule from the one it enforces."""
    from assaywatch.report import registry_status_line

    # Forced to `draft` rather than picked by id. This read a specific entry on the
    # assumption it was a draft; the 2026-10-24 promotion made it active and the test
    # failed although the wording it guards had not changed. The rule under test is
    # about how a draft is DESCRIBED, so the fixture states the status it needs.
    from assaywatch.schema import Status

    assay = _assay("CDV_N_gene_Elia_2006").model_copy(update={"status": Status.draft})
    assert assay.status is Status.draft
    line = registry_status_line({assay.id: None}, {assay.id: assay})
    assert "not for a verified citation" not in line
    assert "maintainer sign-off" in line


def test_the_header_does_not_claim_a_rule_the_override_breaks():
    """It said "an assay is flagged only when the upper bound of the recent
    interval falls below the threshold", and three of the 38 declining rows on
    2026-10-22 had pooled intervals of 91-93%, 95-96% and 99-99%. They were
    lineage overrides, which is the point of measuring per lineage -- so the
    sentence had to change, not the rule."""
    md = render_markdown(_drifting(), {}, [], "2026-10-03")
    assert "an assay is flagged only when the upper bound" not in md
    assert "A **pooled** flag needs the" in md
    assert "can also flag an assay whose pooled share clears the threshold" in md
    assert "nothing controls error across assays" in md


def test_a_flagged_row_carries_its_own_duplication_verdict():
    """ "33 of 72 flagged assays still hold" sat at the top of the report while
    the headings said Declining (38), and the per-assay verdict was folded away
    in the detail section. The flag stands either way -- the check is documented
    as never gating one -- but the reader can now see what it rests on."""
    drifts = _drifting()
    a = drifts["A"]
    a.recent_footprints, a.recent_footprints_detected, a.baseline_footprints = 40, 10, 40
    a._cluster_check()
    md = render_markdown(drifts, {}, [], "2026-10-03")
    assert "| duplication |" in md
    assert a.flag_survives_clustering is not None
    assert ("holds" in md) or ("fails:" in md)


def test_a_nested_row_says_when_one_of_its_rounds_is_not_scoreable():
    """The nested table reports coverage, not a verdict, so a held-out round
    still appears there -- but `LYSSAVIRUSES_ssRNA_Nucleoprotein_gene` is
    `not_validated` and led the table at "32% / 100% / 32%" with nothing said. A
    number a reader will act on carries the same warning its status did."""
    from assaywatch.report import NestedRow, _nested_row

    class F:
        family = "FAM"
        outer, inner = "OUT", "IN"
        outer_share = inner_share = nested_share = 0.5
        nests = True
        records = 10
        outer_detected = 5
        outer_diverged = 0
        containment = {("OUT", "IN"): (5, 5)}

    assert _nested_row(F(), frozenset({"IN"})).held_out is True
    assert _nested_row(F(), frozenset({"OTHER"})).held_out is False
    assert isinstance(_nested_row(F()), NestedRow)


def test_markdown_and_html_get_the_same_nested_rows():
    """The HTML table read `ReportModel.nested_rows` while the markdown one
    rebuilt its own, so the not-scoreable marker reached the HTML and not the
    markdown. One decider: `nested_section` takes the model's rows."""
    from assaywatch.nested import NestedFamily
    from assaywatch.report import _nested_row, nested_section

    f = NestedFamily(
        "LYSSA",
        ["LYSSA", "LYSSA_round2"],
        outer="LYSSA",
        inner="LYSSA_round2",
        records=100,
        outer_detected=32,
        inner_detected=100,
        both_detected=32,
        containment={("LYSSA", "LYSSA_round2"): (100, 100)},
    )
    rows = [_nested_row(f, frozenset({"LYSSA"}))]
    out = "\n".join(nested_section({"LYSSA": f}, {}, 0.90, rows))
    assert "`LYSSA` (not scoreable)" in out
    # and with no rows passed it still builds its own, unmarked
    assert "(not scoreable)" not in "\n".join(nested_section({"LYSSA": f}, {}, 0.90))


def test_site_drift_assesses_through_the_report_not_a_copy():
    """sitedrift.py promised its statuses "come from the same assessment the main
    report uses, so the two documents cannot disagree", then called `assess` with
    no taxids, scope, resolvers or taxonomy -- no lineage check, no scope filter.
    On the frozen 2026-10-22 table it listed 17 assays the report did not flag and
    missed 4 it did. The promise is kept by construction: one function, two
    callers, and sitedrift never calls `assess` itself."""
    import ast

    src = (ROOT / "assaywatch" / "sitedrift.py").read_text()
    called = {
        n.func.id if isinstance(n.func, ast.Name) else getattr(n.func, "attr", "")
        for n in ast.walk(ast.parse(src))
        if isinstance(n, ast.Call)
    }
    assert "assess_as_reported" in called
    assert "assess" not in called, "sitedrift must not assess on its own"
    assert "held_out_reasons" in called, "and must hold back what the report holds back"


def test_the_html_is_navigable_without_any_script():
    """1 MB, ten sections, 91 tables and -- until now -- zero anchors: a reader
    could not jump to a section or be sent to one assay.

    DELIBERATELY NOT JAVASCRIPT, which is what the plan proposed. README states
    "no JavaScript" as a property of this file with a reason ("opens from a
    file:// path or GitHub Pages in a lab with no bioinformatician"), and the
    status tables are already open, so the browser's own find reaches every
    assay row. What was missing was navigation, and anchors are enough: a
    <details> whose fragment is targeted is opened by the browser, so a link
    lands a reader inside one assay's year table with nothing running.
    """
    drifts = _drifting()
    bd = "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004"
    drifts[bd] = drifts.pop("A")
    drifts[bd].assay_id = bd
    page = render_html(drifts, _registry_assays([bd]), [], "2026-10-03", CFG)

    assert "<script" not in page, "the no-script property is deliberate; see the docstring"
    for frag in ("id='start-here'", "id='declining'", "id='detail'", "id='coverage-gaps'"):
        assert frag in page, f"missing anchor {frag}"
    # the contents list points at them
    assert "<a href='#declining'>" in page
    # and a flagged assay's row links through to its own detail block
    assert f"<a href='#detail-{bd.lower().replace('_', '-')}'>" in page
    assert f"<details id='detail-{bd.lower().replace('_', '-')}'>" in page


def test_the_report_says_when_the_previous_run_finished(tmp_path):
    """README and CITATION.cff both say this re-screens "on a schedule", and
    until 2026-10-23 there was none. A report carries its run date in the title,
    but nothing told a reader whether that date was last week or six weeks ago --
    and a drift monitor whose last look was six weeks ago is making a different
    claim from one that ran on Sunday."""
    import json

    from assaywatch.report import freshness_line

    def run(name, run_date, status, finished):
        d = tmp_path / name
        d.mkdir()
        (d / "run-timing.json").write_text(
            json.dumps({"run_date": run_date, "status": status, "finished": finished})
        )

    assert freshness_line(tmp_path, "2026-10-23") == "", "a first run claims nothing"

    run("2026-10-11", "2026-10-11", "success", "2026-10-11T20:00:00")
    run("2026-10-18", "2026-10-18", "failed", "2026-10-18T20:00:00")
    # A failed run is not a previous look at the data.
    assert "2026-10-11" in freshness_line(tmp_path, "2026-10-23")

    run("2026-10-22", "2026-10-22", "success", "2026-10-22T16:17:50")
    assert freshness_line(tmp_path, "2026-10-23") == "Previous successful run: 2026-10-22 (1 day earlier)."
    assert "40 days earlier" in freshness_line(tmp_path, "2026-12-01")

    # A COPY of this run is not a previous run: keyed on the run_date inside the
    # file, not the directory name, because results/baseline-2026-10-22/ exists.
    run("baseline-2026-10-22", "2026-10-22", "success", "2026-10-22T16:17:50")
    assert "2026-10-22" in freshness_line(tmp_path, "2026-10-23")
    assert freshness_line(tmp_path, "2026-10-22").startswith("Previous successful run: 2026-10-11")


# --- the run-timing footer (timekeeping item 7) ----------------------------


def _timing_json(results: Path, run_date: str, **over):
    d = results / run_date
    d.mkdir(parents=True, exist_ok=True)
    payload = {
        "run_date": run_date,
        "started": "2026-10-23T21:00:00",
        "finished": "2026-10-23T21:20:00",
        "status": "success",
        "stages": [{"name": "retrieve", "seconds": 600.0}, {"name": "screen", "seconds": 540.0}],
        "elapsed_seconds": 1200.0,
    }
    payload.update(over)
    (d / "run-timing.json").write_text(json.dumps(payload))
    return d


def _bench_tsv(results: Path, taxid: str, group: str, stem: str, seconds: float, when: str):
    import os
    from datetime import datetime as _dt

    p = results / "benchmarks" / "screen" / taxid / group / f"{stem}.tsv"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(f"s\th:m:s\tmax_rss\n{seconds}\t0:00:01\tNA\n")
    ts = _dt.fromisoformat(when).timestamp()
    os.utime(p, (ts, ts))


def test_the_footer_reports_stages_and_the_slowest_groups(tmp_path):
    from assaywatch.report import timing_lines

    _timing_json(tmp_path, "2026-10-23")
    _bench_tsv(tmp_path, "10241", "all", "a", 100.0, "2026-10-23T21:05:00")
    _bench_tsv(tmp_path, "11118", "qabc", "a", 20.0, "2026-10-23T21:06:00")
    md = "\n".join(timing_lines(tmp_path, "2026-10-23"))
    assert "## Run timing" in md
    assert "finished success after 20m" in md
    assert "| retrieve | 10m 00s |" in md
    assert "`10241/all`" in md and "83%" in md
    assert md.index("10241/all") < md.index("11118/qabc"), "slowest first"
    assert "max_rss" in md and "cpu_time" in md, "the macOS caveat must travel with the numbers"


def test_a_benchmark_from_an_earlier_run_is_not_in_the_footer(tmp_path):
    """The stale-generation trap: benchmarks are keyed by archive, so a cached
    screen keeps a measurement taken under conditions this run did not have."""
    from assaywatch.report import timing_lines

    _timing_json(tmp_path, "2026-10-23")
    _bench_tsv(tmp_path, "10241", "all", "a", 1180.0, "2026-10-22T15:30:00")
    _bench_tsv(tmp_path, "11118", "qabc", "a", 20.0, "2026-10-23T21:06:00")
    md = "\n".join(timing_lines(tmp_path, "2026-10-23"))
    assert "11118/qabc" in md
    assert "10241/all" not in md, "a benchmark older than this run must not be ranked"


def test_an_all_cached_run_says_so_instead_of_showing_stale_rows(tmp_path):
    from assaywatch.report import timing_lines

    _timing_json(tmp_path, "2026-10-23")
    _bench_tsv(tmp_path, "10241", "all", "a", 1180.0, "2026-10-22T15:30:00")
    md = "\n".join(timing_lines(tmp_path, "2026-10-23"))
    assert "every archive's screen was cached" in md
    assert "10241/all" not in md


def test_an_open_run_borrows_the_last_completed_runs_stages(tmp_path):
    """The real shape of every report: the Snakefile closes its `workflow` stage
    in `onsuccess`, which fires AFTER the report rule, so this run's stage has no
    duration yet. Insisting on it printed an empty table in every run."""
    from assaywatch.report import timing_lines

    _timing_json(tmp_path, "2026-10-21", stages=[{"name": "workflow", "seconds": 900.0}])
    _timing_json(
        tmp_path,
        "2026-10-23",
        finished=None,
        status="running",
        elapsed_seconds=0.0,
        stages=[{"name": "workflow", "seconds": None}],
    )
    md = "\n".join(timing_lines(tmp_path, "2026-10-23"))
    assert "finished running" not in md, "an unfinished run must not be called finished"
    assert "last completed run, 2026-10-21" in md
    assert "| workflow | 15m 00s |" in md


def test_a_completed_run_prefers_its_own_stages(tmp_path):
    from assaywatch.report import timing_lines

    _timing_json(tmp_path, "2026-10-21", stages=[{"name": "workflow", "seconds": 900.0}])
    _timing_json(tmp_path, "2026-10-23")
    md = "\n".join(timing_lines(tmp_path, "2026-10-23"))
    assert "finished success after 20m 00s" in md
    assert "last completed run" not in md
    assert "| retrieve | 10m 00s |" in md


def test_no_timing_file_means_no_footer(tmp_path):
    from assaywatch.report import timing_lines

    assert timing_lines(tmp_path, "2026-10-23") == []


def test_the_footer_reaches_both_rendered_reports(tmp_path):
    from assaywatch.report import render_html, render_markdown

    _timing_json(tmp_path, "2026-10-03")
    _bench_tsv(tmp_path, "10241", "all", "a", 100.0, "2026-10-23T21:05:00")
    drifts = _drifting()
    md = render_markdown(drifts, {}, [], "2026-10-03", results_dir=tmp_path)
    assert "## Run timing" in md and "10241/all" in md
    page = render_html(drifts, {}, [], "2026-10-03", results_dir=tmp_path)
    assert "id='timing'" in page and "<code>10241/all</code>" in page
    assert "| stage |" not in page, "the markdown table must be rendered as HTML, not pasted"
