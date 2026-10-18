"""Tests for assaywatch.lineage."""

import pytest
from assaywatch.lineage import (
    LineageStats,
    lineage_for_taxid,
    confidence_interval_wald,
    per_lineage_stats,
    worst_lineage_verdict,
)


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
    verdict = worst_lineage_verdict(stats, 0.8)
    assert verdict == "detecting"


def test_worst_lineage_verdict_empty():
    """No lineages returns None."""
    assert worst_lineage_verdict([], 0.8) is None
