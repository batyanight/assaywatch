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
