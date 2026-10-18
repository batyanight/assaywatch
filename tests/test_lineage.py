"""Tests for assaywatch.lineage."""

import gzip

from assaywatch.lineage import (
    LineageStats,
    confidence_interval_wald,
    lineage_for_taxid,
    per_lineage_stats,
    worst_lineage_verdict,
)
from assaywatch.lineage_report import MIN_RESOLVED_SHARE, read_calls_with_taxid


def test_lineage_resolution():
    """taxid resolution to lineage names."""
    cache = {
        109871: "Batrachochytrium dendrobatidis",
        11232: "Canine distemper virus",
    }

    assert lineage_for_taxid(109871, cache) == "Batrachochytrium dendrobatidis"
    assert lineage_for_taxid(11232, cache) == "Canine distemper virus"
    assert lineage_for_taxid(999999, cache) == "taxid_999999"
    assert lineage_for_taxid(None, cache) == "unresolved"


def test_confidence_interval_perfect_detection():
    """CI for 100% detection."""
    lower, upper = confidence_interval_wald(100, 100)
    assert lower > 0.9
    assert upper == 1.0


def test_confidence_interval_no_detection():
    """CI for 0% detection."""
    lower, upper = confidence_interval_wald(0, 100)
    assert lower == 0.0
    assert upper < 0.1


def test_confidence_interval_sparse():
    """CI for a small sample."""
    lower, upper = confidence_interval_wald(1, 10)
    # With n=10, 1 success gives ~0.1 share; CI should be wide
    assert lower >= 0
    assert upper <= 1
    assert upper - lower > 0.1


def test_per_lineage_stats_grouped_by_taxid():
    """Calls are grouped by lineage derived from taxid."""
    calls = [
        {"record_id": "NZ_ACCC01.1", "call": "detect", "taxid": 109871},
        {"record_id": "NZ_ACCC02.1", "call": "detect", "taxid": 109871},
        {"record_id": "NZ_ACCC03.1", "call": "fail", "taxid": 109871},
        {"record_id": "NZ_BDDD01.1", "call": "detect", "taxid": 11232},
        {"record_id": "NZ_BDDD02.1", "call": "detect", "taxid": 11232},
        {"record_id": "NZ_BDDD03.1", "call": "detect", "taxid": 11232},
        {"record_id": "NZ_BDDD04.1", "call": "fail", "taxid": 11232},
        {"record_id": "NZ_BDDD05.1", "call": "fail", "taxid": 11232},
    ]

    cache = {
        109871: "Bd",
        11232: "CDV",
    }

    stats = per_lineage_stats(calls, cache, {}, min_records=1)

    # Should have 2 lineages
    assert len(stats) == 2

    # Sorted by share ascending (worst first)
    # Bd: 2/3 ≈ 0.667, CDV: 3/5 = 0.6 → CDV is worse
    assert stats[0].lineage_name == "CDV"
    assert stats[0].share == 3 / 5
    assert stats[1].lineage_name == "Bd"
    assert stats[1].share == 2 / 3


def test_per_lineage_stats_min_records_floor():
    """Lineages below min_records threshold are filtered."""
    calls = [
        {"record_id": "A1", "call": "detect", "taxid": 109871},
        {"record_id": "A2", "call": "detect", "taxid": 109871},
        {"record_id": "B1", "call": "detect", "taxid": 11232},  # Only 1 record
    ]

    cache = {109871: "Bd", 11232: "CDV"}
    stats = per_lineage_stats(calls, cache, {}, min_records=20)

    # Should have 0 lineages (both below 20)
    assert len(stats) == 0


def test_per_lineage_stats_taxid_sidecar_lookup():
    """Accessions without taxid can be looked up via sidecar."""
    calls = [
        {"record_id": "AB00001.1", "call": "detect", "accession": "AB00001"},
        {"record_id": "AB00002.1", "call": "detect", "accession": "AB00002"},
        {"record_id": "AB00002.1", "call": "fail", "accession": "AB00002"},
    ]

    cache = {109871: "Bd", 11232: "CDV"}
    sidecar = {
        "AB00001": 109871,
        "AB00002": 11232,
    }

    stats = per_lineage_stats(calls, cache, sidecar, min_records=1)

    assert len(stats) == 2
    assert stats[0].lineage_name == "CDV"
    assert stats[0].n_detected == 1
    assert stats[0].n_evaluable == 2
    assert stats[1].lineage_name == "Bd"
    assert stats[1].n_detected == 1
    assert stats[1].n_evaluable == 1


def test_worst_lineage_verdict_all_detecting():
    """If the worst lineage detects above threshold, verdict is detecting."""
    stats = [
        LineageStats("test", "Bd", 109871, 20, 18, 0.9, 0.75, 0.98),
        LineageStats("test", "CDV", 11232, 20, 19, 0.95, 0.80, 0.99),
    ]

    # With threshold 0.8, both lineages are well above it
    verdict, idx = worst_lineage_verdict(stats, 0.8)
    assert verdict == "detecting"
    assert idx is None


def test_worst_lineage_verdict_empty():
    """No lineages returns None."""
    assert worst_lineage_verdict([], 0.8) == (None, None)


# --- the accession join -------------------------------------------------
# Three bugs shipped in the first phase-1 cut, all of which produced a report
# of nothing but "unresolved" rather than an error: the calls table was read
# with row["accession"] when its column is "record_id"; calls carry versioned
# accessions (AB027157.1) while the sidecar is keyed unversioned (AB027157);
# and the metadata glob missed the <taxid>/<group>/ archive layout.


def _calls_file(tmp_path, rows):
    p = tmp_path / "calls.tsv.gz"
    with gzip.open(p, "wt") as f:
        f.write("assay_id\trecord_id\tcall\n")
        for rid, call in rows:
            f.write(f"A\t{rid}\t{call}\n")
    return p


def test_join_reads_record_id_not_accession(tmp_path):
    """The calls table has no `accession` column; the identifier is `record_id`."""
    calls = _calls_file(tmp_path, [("AB027157", "detect")])
    out = read_calls_with_taxid(calls, {}, {"AB027157": 11})
    assert out["A"][0]["taxid"] == 11


def test_join_strips_the_accession_version(tmp_path):
    """Calls carry AB027157.1; metadata and the sidecar are keyed AB027157."""
    calls = _calls_file(tmp_path, [("AB027157.1", "detect")])
    out = read_calls_with_taxid(calls, {}, {"AB027157": 11})
    assert out["A"][0]["taxid"] == 11, "versioned accession must match unversioned key"


def test_join_reports_none_for_an_accession_nobody_knows(tmp_path):
    calls = _calls_file(tmp_path, [("ZZ999999.9", "detect")])
    out = read_calls_with_taxid(calls, {}, {"AB027157": 11})
    assert out["A"][0]["taxid"] is None


def test_guard_threshold_is_a_real_fraction():
    """The run aborts below this share rather than writing an all-unresolved report."""
    assert 0 < MIN_RESOLVED_SHARE <= 1
