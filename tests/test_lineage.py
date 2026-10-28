"""Tests for assaywatch.lineage."""

import gzip
from pathlib import Path

import pytest

from assaywatch.drift import wilson_interval
from assaywatch.lineage import (
    LineageStats,
    build_resolvers,
    cluster_resolver,
    confidence_interval,
    lineage_for_taxid,
    lineages_never_covered,
    per_lineage_stats,
    resolve_sublineage,
    sublineage_resolvers,
    subtaxid_resolver,
    title_assays,
    title_resolver,
    worst_lineage_verdict,
)
from assaywatch.lineage_report import MIN_RESOLVED_SHARE, read_calls_with_taxid

ROOT = Path(__file__).resolve().parents[1]


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
    lower, upper = confidence_interval(100, 100)
    assert lower > 0.9
    assert upper == 1.0


def test_confidence_interval_no_detection():
    """CI for 0% detection."""
    lower, upper = confidence_interval(0, 100)
    assert lower == 0.0
    assert upper < 0.1


def test_the_interval_is_not_degenerate_at_the_extremes():
    """0 of n and n of n must not claim certainty.

    This is the test that was missing. `test_confidence_interval_no_detection`
    below asserts `upper < 0.1` for 0/100, which a zero-width interval passes
    trivially -- and that is exactly what the Wald interval it was written
    against returned: (0.0, 0.0). The shipped 2026-10-22 report printed
    "detects only 0.0% (0.0%-0.0%)" on 428 records as the evidence for a
    `declining` call. An interval of zero width is a claim of certainty from
    the one shape of data that carries least of it, so it is asserted against
    here rather than merely bounded.
    """
    for k, n in [(0, 428), (0, 100), (0, 43), (0, 1)]:
        lower, upper = confidence_interval(k, n)
        assert lower == 0.0
        assert upper > 0.0, f"{k}/{n} gave a zero-width interval"
    for n in (1, 43, 100, 428):
        lower, upper = confidence_interval(n, n)
        assert upper == 1.0
        assert lower < 1.0, f"{n}/{n} gave a zero-width interval"


def test_the_interval_is_the_one_drift_uses():
    """Per-lineage and pooled shares are the same measurement, so one estimator.

    The report header says "Intervals are Wilson 95%". It was true of the
    pooled numbers and false of every per-lineage one. Held to drift's
    implementation rather than to a copied formula, so the two cannot drift
    apart again.
    """
    for k, n in [(0, 428), (1, 10), (302, 345), (43, 43), (50, 100)]:
        assert confidence_interval(k, n) == wilson_interval(k, n)


def test_confidence_interval_sparse():
    """CI for a small sample."""
    lower, upper = confidence_interval(1, 10)
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


# --- sub-taxid resolver chain (docs/journal/2026-10-19-subtaxid-resolution.md) ---
# The chain splits a single taxid into finer sub-lineages. Default behaviour
# (resolvers=None) must stay byte-for-byte the Phase 1 per-taxid grouping;
# the tests above already lock that, so here we exercise the chain itself.


def test_title_resolver_extracts_influenza_subtype():
    """Mode B: subtype parsed from the defline, capture group 1 is the label."""
    r = title_resolver(r"\((H\d+N\d+)\)")
    call = {
        "record_id": "CY001.1",
        "call": "detect",
        "title": "Influenza A virus (A/swine/NE/2026(H1N2)) segment 7",
    }
    assert r(call, 11320, {}) == "H1N2"


def test_title_resolver_defers_when_no_match_or_no_title():
    """No subtype in the title, or no title at all -> defer (None)."""
    r = title_resolver(r"\((H\d+N\d+)\)")
    assert r({"record_id": "x", "call": "detect", "title": "segment 7, no subtype"}, 11320, {}) is None
    assert r({"record_id": "x", "call": "detect"}, 11320, {}) is None  # title absent


def test_subtaxid_resolver_defers_at_parent_but_resolves_below():
    """Mode A: a record at the query taxid defers; a finer taxid resolves."""
    r = subtaxid_resolver(query_taxid=10260)  # Avipoxvirus
    cache = {10261: "fowlpox"}
    # Parent-level record: defer so a title/cluster resolver can try.
    assert r({"record_id": "x", "call": "detect"}, 10260, cache) is None
    # Species-level record: resolve via the cache.
    assert r({"record_id": "y", "call": "detect"}, 10261, cache) == "fowlpox"
    # Finer taxid not in cache: still resolves, as taxid_NNN.
    assert r({"record_id": "z", "call": "detect"}, 10264, cache) == "taxid_10264"
    # No taxid at all: defer.
    assert r({"record_id": "w", "call": "detect"}, None, cache) is None


def test_cluster_resolver_matches_versioned_and_unversioned():
    """Mode C: cluster map keyed by accession, with or without version."""
    r = cluster_resolver({"AY123": "cluster-01"})
    assert r({"record_id": "AY123.2", "call": "detect"}, 109871, {}) == "cluster-01"
    assert r({"record_id": "AY123", "call": "detect"}, 109871, {}) == "cluster-01"
    assert r({"record_id": "ZZ999.1", "call": "detect"}, 109871, {}) is None


def test_resolve_sublineage_first_non_none_wins_else_taxid():
    """Chain order: first resolver to return a label wins; else taxid fallback."""
    cache = {11320: "Influenza A virus"}
    chain = [subtaxid_resolver(query_taxid=11320), title_resolver(r"\((H\d+N\d+)\)")]
    # Parent taxid + title present: subtaxid defers, title wins.
    c1 = {"record_id": "a", "call": "detect", "title": "... (H5N1) ..."}
    assert resolve_sublineage(c1, 11320, cache, chain) == "H5N1"
    # Parent taxid + no subtype in title: both defer -> taxid fallback.
    c2 = {"record_id": "b", "call": "detect", "title": "no subtype here"}
    assert resolve_sublineage(c2, 11320, cache, chain) == "Influenza A virus"


def test_build_resolvers_from_config_and_rejects_bad_names():
    """build_resolvers wires a chain from config; unknown names raise."""
    cfg = {"chain": ["subtaxid", "title"], "title": {"pattern": r"\((H\d+N\d+)\)"}}
    resolvers = build_resolvers(cfg, query_taxid=11320)
    assert len(resolvers) == 2
    # Title in the chain but no pattern configured -> error.
    with pytest.raises(ValueError):
        build_resolvers({"chain": ["title"]})
    with pytest.raises(ValueError):
        build_resolvers({"chain": ["nonsense"]})
    # Empty config == subtaxid-only (Phase 1 equivalent).
    assert len(build_resolvers({})) == 1


def test_per_lineage_stats_title_chain_splits_one_taxid():
    """End to end: one taxid, two subtypes in titles -> two assessable lineages."""
    calls = []
    for i in range(30):
        calls.append(
            {
                "record_id": f"H1_{i}.1",
                "call": "detect",
                "taxid": 11320,
                "title": "Influenza A virus (A/x/2026(H1N1)) segment 7",
            }
        )
    for i in range(30):
        # H5N1 detects poorly: 6/30 = 0.2
        call = "detect" if i < 6 else "fail"
        calls.append(
            {
                "record_id": f"H5_{i}.1",
                "call": call,
                "taxid": 11320,
                "title": "Influenza A virus (A/y/2026(H5N1)) segment 7",
            }
        )

    chain = build_resolvers(
        {"chain": ["subtaxid", "title"], "title": {"pattern": r"\((H\d+N\d+)\)"}}, query_taxid=11320
    )
    stats = per_lineage_stats(calls, {}, {}, min_records=20, resolvers=chain)

    names = {s.lineage_name for s in stats}
    assert names == {"H1N1", "H5N1"}
    worst = stats[0]  # sorted worst-first
    assert worst.lineage_name == "H5N1"
    assert worst.share == 6 / 30

    # Without the chain, the same calls pool into one taxid row -> no split.
    pooled = per_lineage_stats(calls, {}, {}, min_records=20)
    assert len(pooled) == 1
    assert pooled[0].lineage_name == "taxid_11320"


def test_subtaxid_before_another_resolver_needs_the_query_taxid():
    """Without it, parent-level records never defer and the title resolver never runs."""
    cfg = {"chain": ["subtaxid", "title"], "title": {"pattern": r"\((H\d+N\d+)\)"}}
    with pytest.raises(ValueError, match="query taxid"):
        build_resolvers(cfg)
    assert len(build_resolvers(cfg, query_taxid=11320)) == 2
    # subtaxid last (or alone) is fine without it: nothing follows to defer to.
    assert len(build_resolvers({"chain": ["subtaxid"]})) == 1


def test_the_shipped_sublineage_block_labels_a_real_influenza_title():
    """The config that ships, not a fixture: the one live chain must resolve.

    `lineage.sublineage` has been a worked example in a comment for a week and is
    live for one assay since 2026-10-27. A regex in a YAML string is quoted twice
    over, so the thing worth pinning is not the mechanism (tested above) but that
    the pattern as COMMITTED still pulls a subtype out of a GenBank title.
    """
    import yaml

    cfg = yaml.safe_load((ROOT / "config.yaml").read_text())
    block = cfg["lineage"]["sublineage"]["INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003"]
    chain = build_resolvers(block, query_taxid=11320)
    call = {
        "record_id": "x",
        "call": "detect",
        "title": "Influenza A virus (A/swine/Iowa/15/1930(H1N1)) segment 7",
    }
    assert resolve_sublineage(call, 11320, {11320: "Influenza A virus"}, chain) == "H1N1"


def test_sublineage_resolvers_and_title_assays_read_the_config_block():
    lcfg = {
        "sublineage": {
            "FLU": {"chain": ["title"], "title": {"pattern": r"\((H\d+N\d+)\)"}},
            "POX": {"chain": ["subtaxid"]},
        }
    }
    chains = sublineage_resolvers(lcfg, {"FLU": 11320, "POX": 10260})
    assert set(chains) == {"FLU", "POX"}
    assert title_assays(lcfg) == {"FLU"}
    # No block: no chains, no titles to read.
    assert sublineage_resolvers({}, {}) == {}
    assert title_assays({}) == set()


def test_a_large_failing_lineage_is_still_judged_failing():
    """The lower-tail p-value must stay finite for big lineages.

    The old sum of comb(n, k) * p**k * q**(n-k) went nan above n ~ 1030, and a
    nan p-value is never rejected, so a lineage at 75% read "detecting".
    """
    for n in (200, 1000, 1100, 5000):
        d = int(n * 0.75)
        stat = LineageStats("A", "x", None, n, d, d / n, 0.0, 1.0)
        assert worst_lineage_verdict([stat], 0.9) == ("failing", 0), n
    # And one comfortably above threshold at large n still passes.
    ok = LineageStats("A", "y", None, 5000, 4900, 0.98, 0.0, 1.0)
    assert worst_lineage_verdict([ok], 0.9) == ("detecting", None)


def test_lineages_never_covered_needs_a_measured_year_below_threshold():
    """Measured and never at threshold -> in the set; worked once, or never measured -> not."""

    def calls(taxid, year, det, fail):
        return [
            {"record_id": f"{taxid}_{year}_{i}", "call": "detect", "taxid": taxid, "year": year}
            for i in range(det)
        ] + [
            {"record_id": f"{taxid}_{year}_f{i}", "call": "fail", "taxid": taxid, "year": year}
            for i in range(fail)
        ]

    base = (
        calls(1, 2015, 0, 30)  # measured, 0%: never covered
        + calls(1, 2016, 2, 20)
        + calls(2, 2015, 30, 0)  # cleared the threshold once
        + calls(2, 2016, 0, 30)
        + calls(3, 2016, 0, 5)  # too few records in any year: never measured
    )
    assert lineages_never_covered(base, {}, {}, 0.9, 10) == {"taxid_1"}


def test_holm_does_not_fail_an_assay_on_marginal_lineages_bh_would():
    """The rule is "ANY lineage significantly below threshold fails the assay".
    Five lineages each at p ~0.02-0.04 against 0.90: BH rejects all five (its
    largest p is under 0.05), so the assay fails; Holm needs the smallest p under
    0.05/5 = 0.01, so none is rejected. BH controls the expected share of false
    rejections, not the chance of at least one -- the event that decides here."""
    stats = [
        LineageStats("A", "L1", None, 50, 40, 0.80, 0.0, 0.0),  # p = 0.0245
        LineageStats("A", "L2", None, 60, 49, 0.82, 0.0, 0.0),  # p = 0.0342
        LineageStats("A", "L3", None, 80, 66, 0.83, 0.0, 0.0),  # p = 0.0267
        LineageStats("A", "L4", None, 100, 83, 0.83, 0.0, 0.0),  # p = 0.0206
        LineageStats("A", "L5", None, 40, 32, 0.80, 0.0, 0.0),  # p = 0.0419
    ]
    assert worst_lineage_verdict(stats, 0.9, "fdr_bh", 0.05)[0] == "failing"
    assert worst_lineage_verdict(stats, 0.9, "holm", 0.05) == ("detecting", None)
    # and the default is Holm, so a caller that passes nothing gets FWER control
    assert worst_lineage_verdict(stats, 0.9) == ("detecting", None)
