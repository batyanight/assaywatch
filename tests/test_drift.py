"""Drift statistics. Interval values are checked against published figures.

The Wilson and Newcombe numbers below are standard worked examples; if a
refactor changes them, the refactor is wrong, not the test.
"""

from collections import Counter
from datetime import date

import pytest

from assaywatch.drift import (
    NO_DATA,
    STATUS_ORDER,
    STATUSES,
    AssayDrift,
    YearStats,
    assess,
    coverage_gaps,
    newcombe_difference,
    recent_cutoff_year,
    wilson_interval,
)

CFG = {
    "drift": {
        "detect_fraction_threshold": 0.90,
        "recent_window_months": 24,
        "min_records_for_drift": 20,
        "min_records_for_coverage": 10,
    }
}
TODAY = date(2026, 10, 3)


@pytest.mark.parametrize(
    "k,n,lo,hi",
    [
        (0, 10, 0.0000, 0.2775),
        (10, 10, 0.7225, 1.0000),
        (3, 5, 0.2307, 0.8824),
        (45, 50, 0.7864, 0.9565),
    ],
)
def test_wilson_matches_published_values(k, n, lo, hi):
    got = wilson_interval(k, n)
    assert got[0] == pytest.approx(lo, abs=5e-4)
    assert got[1] == pytest.approx(hi, abs=5e-4)


def test_wilson_never_leaves_the_unit_interval_at_the_extremes():
    """The normal approximation can return bounds below 0 or above 1; this must not."""
    for k, n in [(0, 3), (3, 3), (1, 200), (199, 200)]:
        lo, hi = wilson_interval(k, n)
        assert 0.0 <= lo <= hi <= 1.0


def test_wilson_has_width_even_when_every_record_agrees():
    """k == n is not certainty. The normal approximation claims it is."""
    lo, hi = wilson_interval(8, 8)
    assert lo < 1.0 and hi == 1.0 and lo < 0.7


def test_empty_sample_is_maximally_uncertain():
    assert wilson_interval(0, 0) == (0.0, 1.0)
    assert newcombe_difference(0, 0, 5, 10) == (-1.0, 1.0)


def test_newcombe_difference_brackets_the_point_estimate():
    lo, hi = newcombe_difference(45, 50, 98, 100)
    assert lo < (45 / 50 - 98 / 100) < hi
    assert hi < 0  # a real drop: the interval excludes zero


def records(year_counts):
    """{year: {call: n}} -> flat call rows plus the year lookup."""
    calls, years = [], {}
    i = 0
    for year, counts in year_counts.items():
        for call, n in counts.items():
            for _ in range(n):
                rid = f"AB{i:05d}"
                calls.append({"assay_id": "A", "record_id": rid, "call": call})
                years[rid] = year
                i += 1
    return calls, years


def test_recent_window_is_derived_from_months():
    assert recent_cutoff_year(CFG, TODAY) == 2024


def test_stable_assay_is_not_flagged():
    calls, years = records({2024: {"detect": 40}, 2025: {"detect": 38, "reduced": 2}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.status == "stable" and a.recent_fraction == 1.0


def test_reduced_counts_as_detected():
    """`reduced` amplifies, just later. It is a sensitivity note, not a miss."""
    calls, years = records({2025: {"reduced": 30}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.recent_detected == 30 and a.status == "stable"


def test_clear_drift_is_flagged():
    calls, years = records({2020: {"detect": 100}, 2025: {"detect": 20, "fail": 30}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.status == "declining"
    assert a.recent_ci[1] < 0.90
    assert a.change_ci[1] < 0  # the drop excludes zero


def test_low_but_unchanged_share_is_low_coverage_not_drift():
    """An assay that never covered this pool: same low share before and after."""
    calls, years = records({2015: {"detect": 30, "fail": 70}, 2025: {"detect": 30, "fail": 70}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.status == "low coverage" and a.change_ci[0] < 0 < a.change_ci[1]
    assert "no measurable fall" in a.note


def test_below_threshold_with_no_baseline_is_low_coverage():
    calls, years = records({2025: {"detect": 10, "fail": 40}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.status == "low coverage" and "no baseline" in a.note


def test_small_sample_is_never_flagged_however_bad_it_looks():
    """Three failures out of five is 40 percent and means nothing at n = 5."""
    calls, years = records({2025: {"detect": 2, "fail": 3}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.status == "insufficient data"
    assert "too wide to act on" in a.note


def test_borderline_assay_is_watched_not_flagged():
    """Below threshold on the point estimate, but the interval still covers it."""
    calls, years = records({2025: {"detect": 22, "fail": 3}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.recent_fraction < 0.90 < a.recent_ci[1]
    assert a.status == "watch"


def test_no_amplicon_and_indeterminate_stay_out_of_the_denominator():
    """A bad sequencing year must not look like drift."""
    calls, years = records({2025: {"detect": 25, "no_amplicon": 500, "indeterminate": 80}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.recent_evaluable == 25 and a.recent_fraction == 1.0
    assert a.status == "stable"
    assert a.unevaluable() == {"no_amplicon": 500, "indeterminate": 80}


def test_records_without_a_deposit_year_are_skipped_and_reported():
    calls, years = records({2025: {"detect": 25}})
    calls.append({"assay_id": "A", "record_id": "NOYEAR", "call": "fail"})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.recent_evaluable == 25
    assert "1 records skipped" in a.note


def test_old_data_only_is_not_called_stable():
    calls, years = records({2015: {"detect": 200}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.status == "no recent data"


def test_baseline_and_recent_split_on_the_cutoff_year():
    calls, years = records({2023: {"detect": 50}, 2024: {"detect": 30, "fail": 10}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.baseline_evaluable == 50 and a.recent_evaluable == 40


def test_coverage_gap_lists_assays_with_too_little_data():
    calls, years = records({2025: {"detect": 4}})
    drifts = assess(calls, years, CFG, today=TODAY)
    taxa = {"A": (109871, "Batrachochytrium dendrobatidis"), "B": (1, "Never screened")}
    gaps = {g["assay_id"]: g for g in coverage_gaps(drifts, taxa, CFG)}
    assert gaps["A"]["evaluable"] == 4
    assert gaps["B"]["evaluable"] == 0  # an assay with no records at all is the worst gap


def test_thresholds_come_from_config():
    calls, years = records({2025: {"detect": 22, "fail": 3}})
    strict = {"drift": {**CFG["drift"], "detect_fraction_threshold": 0.99}}
    assert assess(calls, years, strict, today=TODAY)["A"].status == "low coverage"  # no baseline
    loose = {"drift": {**CFG["drift"], "min_records_for_drift": 1000}}
    assert assess(calls, years, loose, today=TODAY)["A"].status == "insufficient data"


def test_year_stats_can_be_assembled_directly():
    a = AssayDrift("A", recent_from=2024)
    a.years[2025] = YearStats(2025)
    a.years[2025].counts["detect"] = 30
    a.finalise()
    assert a.recent_evaluable == 30 and a.status == "stable"


def test_a_real_but_tiny_fall_is_not_declining():
    """1% -> 0% over thousands of records excludes zero, and still says nothing about drift."""
    cfg = {"drift": {**CFG["drift"], "min_decline": 0.05}}
    calls, years = records({2015: {"detect": 30, "fail": 2970}, 2025: {"fail": 3000}})
    a = assess(calls, years, cfg, today=TODAY)["A"]
    assert a.change_ci[1] < 0 and a.status == "low coverage"
    assert "fell less than" in a.note
    big = {"drift": {**CFG["drift"], "min_decline": 0.05}}
    calls, years = records({2015: {"detect": 90, "fail": 10}, 2025: {"detect": 40, "fail": 60}})
    assert assess(calls, years, big, today=TODAY)["A"].status == "declining"


def test_window_widens_for_a_sparsely_deposited_target():
    """Bd ITS records arrive in bursts; a fixed window makes the assay unjudgeable between them."""
    cfg = {"drift": {**CFG["drift"], "max_window_months": 60}}
    # 8 records inside 24 months, 30 more in the two years before that.
    calls, years = records({2022: {"detect": 30}, 2025: {"detect": 8}})
    fixed = assess(calls, years, CFG, today=TODAY)["A"]
    assert fixed.status == "insufficient data" and fixed.window_months == 24
    wide = assess(calls, years, cfg, today=TODAY)["A"]
    assert wide.status == "stable" and wide.window_months > 24
    assert wide.recent_evaluable == 38 and "widened" in wide.note


def test_a_dense_target_keeps_the_standard_window():
    cfg = {"drift": {**CFG["drift"], "max_window_months": 60}}
    calls, years = records({2022: {"detect": 500}, 2025: {"detect": 200, "fail": 100}})
    a = assess(calls, years, cfg, today=TODAY)["A"]
    assert a.window_months == 24 and a.recent_evaluable == 300
    assert "widened" not in a.note


def test_widening_never_drops_a_recent_record():
    cfg = {"drift": {**CFG["drift"], "max_window_months": 60}}
    calls, years = records({2021: {"fail": 40}, 2025: {"detect": 5}})
    a = assess(calls, years, cfg, today=TODAY)["A"]
    assert a.recent_evaluable >= 5 and a.recent_detected >= 5


def test_a_fall_from_a_share_that_never_worked_is_not_drift():
    """30% in 2015 and 5% now is not an assay that degraded; it never covered this pool.

    The fall is real and large, so the old rule called it `declining`, which a
    reader takes as "this assay has drifted". 31 of the 37 assays labelled
    declining in the 2026-10-07 run were this shape.
    """
    calls, years = records({2015: {"detect": 30, "fail": 70}, 2025: {"detect": 5, "fail": 95}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.change_ci[1] < 0, "the fall itself is real; that is not what is in question"
    assert a.status == "low coverage"
    assert "never reached the 90% threshold" in a.note
    old = {"drift": {**CFG["drift"], "require_working_baseline": False}}
    assert assess(calls, years, old, today=TODAY)["A"].status == "declining"


def test_a_progressive_decline_is_still_drift_though_it_dilutes_its_own_baseline():
    """The gate asks about YEARS, not the aggregate baseline, which the decline drags down.

    This assay was perfect in 2014 and is nearly gone by 2025, but its aggregate
    baseline is 56% — below the threshold. Gating on that number would throw away
    exactly the case the tool exists to find.
    """
    calls, years = records(
        {
            2014: {"detect": 30},
            2018: {"detect": 15, "fail": 15},
            2021: {"detect": 5, "fail": 25},
            2025: {"detect": 2, "fail": 48},
        }
    )
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.baseline_fraction < 0.90 and a.ever_worked
    assert a.status == "declining"


def test_one_good_year_is_not_enough_evidence_on_a_handful_of_records():
    """A year that reached the threshold on 4 records cannot establish that the assay worked."""
    calls, years = records({2015: {"detect": 4}, 2016: {"detect": 20, "fail": 76}, 2025: {"fail": 60}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert not a.ever_worked and a.status == "low coverage"


# ---------- lineage-conditional estimand (phase 2) ----------


LINEAGE_CFG = {
    **CFG,
    "lineage": {"min_records_per_lineage": 20},
}


def _records_with_taxids(year_taxid_counts):
    """Build calls, years, and taxids for lineage tests.

    year_taxid_counts: {year: {taxid: {call: n}}}
    Returns (calls, years, taxids) where taxids maps record_id -> taxid.
    """
    calls, years, taxids = [], {}, {}
    i = 0
    for year, taxa in year_taxid_counts.items():
        for taxid, counts in taxa.items():
            for call, n in counts.items():
                for _ in range(n):
                    rid = f"AB{i:05d}"
                    calls.append({"assay_id": "A", "record_id": rid, "call": call})
                    years[rid] = year
                    taxids[rid] = taxid
                    i += 1
    return calls, years, taxids


def test_lineage_override_stable_to_declining():
    """A pooled-stable assay whose worst lineage is failing becomes declining."""
    # Lineage 1 dominates with perfect detection; lineage 2 is failing badly
    # but its small size doesn't drag the pooled share below 90%.
    # Pooled: 205/220 = 93.2% → stable.  Lineage 2: 5/20 = 25% → failing.
    calls, years, taxids = _records_with_taxids(
        {
            2025: {
                100: {"detect": 200},  # lineage 1: 200/200 = 100%
                200: {"detect": 5, "fail": 15},  # lineage 2: 5/20 = 25%
            },
        }
    )
    taxa_cache = {100: "Lineage A", 200: "Lineage B"}
    a = assess(calls, years, LINEAGE_CFG, today=TODAY, taxids=taxids, taxa_cache=taxa_cache)["A"]
    assert a.lineage_override is True
    assert a.status == "declining"
    assert a.status_pooled == "stable"
    assert a.lineage_verdict == "failing"
    # lineage_worst_idx names the same lineage the note names in prose, which is
    # what scripts/lineage_override_audit.py reads instead of parsing it.
    assert a.lineage_worst_idx is not None
    worst = a.lineage_stats[a.lineage_worst_idx]
    assert worst.lineage_name == "Lineage B"
    assert f"lineage {worst.lineage_name} ({worst.n_evaluable} records)" in a.note


def test_lineage_no_override_when_all_detecting():
    """When all lineages detect above threshold, no override."""
    calls, years, taxids = _records_with_taxids(
        {
            2025: {
                100: {"detect": 25},  # 100%
                200: {"detect": 23, "fail": 2},  # 92% > 90%
            },
        }
    )
    taxa_cache = {100: "Lineage A", 200: "Lineage B"}
    a = assess(calls, years, LINEAGE_CFG, today=TODAY, taxids=taxids, taxa_cache=taxa_cache)["A"]
    assert a.lineage_override is False
    assert a.status == "stable"
    assert a.lineage_verdict == "detecting"


def test_lineage_no_override_when_already_declining():
    """If pooled status is already declining, no override needed."""
    # Need a working baseline so it's "declining" rather than "low coverage".
    calls, years, taxids = _records_with_taxids(
        {
            2020: {
                100: {"detect": 30},  # baseline: 100% — assay worked once
            },
            2025: {
                100: {"detect": 10, "fail": 15},  # lineage 1: 40%
                200: {"detect": 10, "fail": 15},  # lineage 2: 40%
            },
        }
    )
    taxa_cache = {100: "Lineage A", 200: "Lineage B"}
    a = assess(calls, years, LINEAGE_CFG, today=TODAY, taxids=taxids, taxa_cache=taxa_cache)["A"]
    # Pooled is already declining (20/50 = 40%), so lineage_override is False.
    assert a.lineage_override is False
    assert a.status == "declining"


def test_lineage_below_floor_ignored():
    """Lineages below min_records_per_lineage are not assessable."""
    calls, years, taxids = _records_with_taxids(
        {
            2025: {
                100: {"detect": 200},  # lineage 1: 200/200 = 100%, assessable
                200: {"detect": 2, "fail": 8},  # lineage 2: only 10 records < 20 floor
            },
        }
    )
    taxa_cache = {100: "Lineage A", 200: "Lineage B"}
    a = assess(calls, years, LINEAGE_CFG, today=TODAY, taxids=taxids, taxa_cache=taxa_cache)["A"]
    assert len(a.lineage_stats) == 1  # only lineage 1 passed the floor
    assert a.lineage_stats[0].lineage_name == "Lineage A"
    assert a.lineage_override is False


def test_lineage_fields_absent_without_taxids():
    """When no taxid data is passed, lineage fields stay None."""
    calls, years = records({2025: {"detect": 30}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.lineage_stats is None
    assert a.lineage_verdict is None
    assert a.lineage_override is False


def test_lineage_coverage_fraction():
    """lineage_coverage reflects what share of evaluable records are in assessable lineages."""
    calls, years, taxids = _records_with_taxids(
        {
            2025: {
                100: {"detect": 200},  # assessable (200 >= 20)
                200: {"detect": 5, "fail": 5},  # below floor (10 < 20)
            },
        }
    )
    taxa_cache = {100: "Lineage A", 200: "Lineage B"}
    a = assess(calls, years, LINEAGE_CFG, today=TODAY, taxids=taxids, taxa_cache=taxa_cache)["A"]
    # 200 of 210 evaluable records are in assessable lineages.
    assert a.lineage_coverage == pytest.approx(200 / 210, abs=1e-6)


# --- scope_taxids tests ---


def test_scope_excludes_out_of_scope_records():
    """Records whose taxid is not in scope_map don't count toward drift."""
    # Taxid 100 is in scope, taxid 200 is out. Without scope, the 20 fails
    # from taxid 200 drag the assay to declining. With scope, only the
    # in-scope records (all detect) are counted → stable.
    calls, years, taxids = _records_with_taxids(
        {
            2025: {
                100: {"detect": 30},  # in scope: 100% detection
                200: {"detect": 5, "fail": 20},  # out of scope: would drag down
            },
        }
    )
    scope_map = {"A": {100}}
    a = assess(calls, years, CFG, today=TODAY, taxids=taxids, scope_map=scope_map)["A"]
    assert a.status == "stable"
    assert a.recent_evaluable == 30
    assert a.out_of_scope == 25


def test_no_scope_counts_everything():
    """Without scope_map, all records count (unchanged behaviour)."""
    calls, years, taxids = _records_with_taxids(
        {
            2025: {
                100: {"detect": 30},
                200: {"detect": 5, "fail": 20},
            },
        }
    )
    a = assess(calls, years, CFG, today=TODAY, taxids=taxids)["A"]
    assert a.recent_evaluable == 55
    assert a.out_of_scope == 0


def test_scope_records_without_taxid_still_counted():
    """Records with no taxid are included even when scope is set, because we
    can't tell whether they're in or out of scope."""
    calls = [
        {"assay_id": "A", "record_id": "AB00001", "call": "detect"},
        {"assay_id": "A", "record_id": "AB00002", "call": "detect"},
    ]
    years = {"AB00001": 2025, "AB00002": 2025}
    # taxids maps nothing for these records
    taxids: dict[str, int] = {}
    scope_map = {"A": {100}}
    a = assess(calls, years, CFG, today=TODAY, taxids=taxids, scope_map=scope_map)["A"]
    # Both records have no taxid → not excluded → both counted.
    assert a.recent_evaluable == 2
    assert a.out_of_scope == 0


def test_scope_does_not_affect_assays_without_scope_entry():
    """An assay not in scope_map is unaffected by scope filtering."""
    calls, years, taxids = _records_with_taxids(
        {
            2025: {
                100: {"detect": 30},
                200: {"detect": 5, "fail": 20},
            },
        }
    )
    # scope_map has an entry for "B" but not "A"
    scope_map = {"B": {999}}
    a = assess(calls, years, CFG, today=TODAY, taxids=taxids, scope_map=scope_map)["A"]
    assert a.recent_evaluable == 55
    assert a.out_of_scope == 0


def test_title_chain_splits_one_taxid_and_drives_the_override():
    """Sub-lineage chain: one taxid, two title-labelled subtypes, one failing.

    Pooled per taxid the assay is stable (205/220) and there is only one
    lineage, so nothing can override it. Given a title chain, the H5N1 records
    form their own lineage at 5/20 and the verdict becomes declining.
    """
    from assaywatch.lineage import build_resolvers

    calls, years, taxids = _records_with_taxids(
        {2025: {11320: {"detect": 205, "fail": 15}}},
    )
    # The last 20 records (15 fails + 5 detects) are H5N1; the rest H1N1.
    detects = [c["record_id"] for c in calls if c["call"] == "detect"]
    h5 = {c["record_id"] for c in calls if c["call"] == "fail"} | set(detects[-5:])
    titles = {
        c[
            "record_id"
        ]: f"Influenza A virus (A/x/2025({'H5N1' if c['record_id'] in h5 else 'H1N1'})) segment 7"
        for c in calls
    }
    taxa_cache = {11320: "Influenza A virus"}

    pooled = assess(calls, years, LINEAGE_CFG, today=TODAY, taxids=taxids, taxa_cache=taxa_cache)["A"]
    assert pooled.status == "stable" and pooled.lineage_override is False

    chain = {"A": build_resolvers({"chain": ["title"], "title": {"pattern": r"\((H\d+N\d+)\)"}})}
    split = assess(
        calls,
        years,
        LINEAGE_CFG,
        today=TODAY,
        taxids=taxids,
        taxa_cache=taxa_cache,
        resolvers=chain,
        titles=titles,
    )["A"]
    assert split.lineage_override is True
    assert split.status == "declining"
    assert {s.lineage_name for s in split.lineage_stats} == {"H1N1", "H5N1"}


def test_empty_resolver_map_is_the_per_taxid_grouping():
    """resolvers={} and resolvers=None must give the same verdicts."""
    calls, years, taxids = _records_with_taxids(
        {2025: {100: {"detect": 200}, 200: {"detect": 5, "fail": 15}}},
    )
    taxa_cache = {100: "Lineage A", 200: "Lineage B"}
    a = assess(calls, years, LINEAGE_CFG, today=TODAY, taxids=taxids, taxa_cache=taxa_cache)["A"]
    b = assess(calls, years, LINEAGE_CFG, today=TODAY, taxids=taxids, taxa_cache=taxa_cache, resolvers={})[
        "A"
    ]
    assert (a.status, a.lineage_override, [s.lineage_name for s in a.lineage_stats]) == (
        b.status,
        b.lineage_override,
        [s.lineage_name for s in b.lineage_stats],
    )


def test_scope_with_taxonomy_keeps_records_below_the_listed_species():
    """Exact match drops strain/no-rank records; the tree keeps them."""
    from assaywatch.taxonomy import Taxonomy

    calls, years, taxids = _records_with_taxids(
        {2025: {3052342: {"detect": 10}, 3139435: {"detect": 30}, 99: {"detect": 15}}},
    )
    tree = Taxonomy({3139435: 3052342, 3052342: 11229, 99: 1, 11229: 1}, {11232: 3052342})
    scope = {"A": {11232}}  # the registry's merged taxid, as CDV's was
    exact = assess(calls, years, CFG, today=TODAY, taxids=taxids, scope_map=scope)
    # Every record excluded: the assay drops out of the result altogether, which is
    # how CDV P gene read "no data" with scope [11232].
    assert "A" not in exact
    tree_ = assess(calls, years, CFG, today=TODAY, taxids=taxids, scope_map=scope, taxonomy=tree)["A"]
    assert tree_.recent_evaluable == 40 and tree_.out_of_scope == 15


def _gated(on: bool) -> dict:
    return {**LINEAGE_CFG, "lineage": {**LINEAGE_CFG["lineage"], "require_working_baseline": on}}


def test_working_baseline_gate_turns_a_never_covered_lineage_into_low_coverage():
    """Lineage 200 was measured in 2018 at 0% and is 0% now: a coverage gap, not drift."""
    calls, years, taxids = _records_with_taxids(
        {
            2018: {100: {"detect": 50}, 200: {"fail": 20}},
            2025: {100: {"detect": 200}, 200: {"detect": 0, "fail": 20}},
        }
    )
    cache = {100: "Lineage A", 200: "Lineage B"}
    off = assess(calls, years, _gated(False), today=TODAY, taxids=taxids, taxa_cache=cache)["A"]
    on = assess(calls, years, _gated(True), today=TODAY, taxids=taxids, taxa_cache=cache)["A"]
    assert off.status == "declining" and off.lineage_override
    assert on.status == "low coverage" and on.status_pooled == "stable"
    # "that lineage is a coverage gap rather than drift": the clause describes the
    # LINEAGE, not the row, which the bare old wording left ambiguous.
    assert "that lineage is a coverage gap rather than drift" in on.note


def test_working_baseline_gate_still_flags_a_lineage_new_to_the_archive():
    """No earlier measured year (an emerging lineage): it must still drive declining."""
    calls, years, taxids = _records_with_taxids(
        {2018: {100: {"detect": 50}}, 2025: {100: {"detect": 200}, 200: {"detect": 5, "fail": 15}}},
    )
    cache = {100: "Lineage A", 200: "Lineage B"}
    on = assess(calls, years, _gated(True), today=TODAY, taxids=taxids, taxa_cache=cache)["A"]
    assert on.status == "declining" and on.lineage_override


def test_working_baseline_gate_flags_a_lineage_that_used_to_work():
    calls, years, taxids = _records_with_taxids(
        {
            2018: {100: {"detect": 50}, 200: {"detect": 20}},
            2025: {100: {"detect": 200}, 200: {"detect": 5, "fail": 15}},
        }
    )
    cache = {100: "Lineage A", 200: "Lineage B"}
    on = assess(calls, years, _gated(True), today=TODAY, taxids=taxids, taxa_cache=cache)["A"]
    assert on.status == "declining" and on.lineage_override


def _ranked(**lineage) -> dict:
    return {**LINEAGE_CFG, "lineage": {**LINEAGE_CFG["lineage"], "require_working_baseline": True, **lineage}}


def _jc_tree():
    from assaywatch.taxonomy import Taxonomy

    # 10632 (no rank) is the old JC polyomavirus taxid under species 1891763;
    # 1193974 sits under an "unclassified" node, 86107 is a typed species.
    return Taxonomy(
        {10632: 1891763, 1891763: 1, 1193974: 90010, 90010: 12059, 86107: 12059, 12059: 1},
        {},
        {1891763: "species", 1193974: "species", 86107: "species", 12059: "genus"},
        {90010: "unclassified Enterovirus"},
    )


def test_species_rollup_joins_a_strain_taxid_to_its_species_history():
    """The 2025 records carry the species taxid; 2018's the no-rank one. Same virus, never covered."""
    calls, years, taxids = _records_with_taxids(
        {
            2018: {100: {"detect": 50}, 10632: {"fail": 20}},
            2025: {100: {"detect": 600}, 1891763: {"fail": 40}},
        }
    )
    cache = {100: "Lineage A"}
    exact = assess(
        calls, years, _ranked(), today=TODAY, taxids=taxids, taxa_cache=cache, taxonomy=_jc_tree()
    )["A"]
    rolled = assess(
        calls,
        years,
        _ranked(group_at_rank="species"),
        today=TODAY,
        taxids=taxids,
        taxa_cache=cache,
        taxonomy=_jc_tree(),
    )["A"]
    assert exact.status == "declining"  # 1891763 has no earlier year, so it looks new
    assert rolled.status == "low coverage" and "every earlier year" in rolled.note


def test_an_unclassified_bucket_cannot_pass_as_a_new_lineage():
    calls, years, taxids = _records_with_taxids(
        {2018: {100: {"detect": 50}}, 2025: {100: {"detect": 600}, 1193974: {"fail": 40}}},
    )
    cache = {100: "Lineage A"}
    off = assess(calls, years, _ranked(), today=TODAY, taxids=taxids, taxa_cache=cache, taxonomy=_jc_tree())[
        "A"
    ]
    on = assess(
        calls,
        years,
        _ranked(unclassified_is_bucket=True),
        today=TODAY,
        taxids=taxids,
        taxa_cache=cache,
        taxonomy=_jc_tree(),
    )["A"]
    assert off.status == "declining"
    assert on.status == "low coverage" and "unclassified taxon" in on.note


def test_a_typed_new_lineage_still_drives_declining_with_buckets_on():
    calls, years, taxids = _records_with_taxids(
        {2018: {100: {"detect": 50}}, 2025: {100: {"detect": 600}, 86107: {"fail": 40}}},
    )
    on = assess(
        calls,
        years,
        _ranked(unclassified_is_bucket=True, group_at_rank="species"),
        today=TODAY,
        taxids=taxids,
        taxa_cache={100: "Lineage A"},
        taxonomy=_jc_tree(),
    )["A"]
    assert on.status == "declining" and on.lineage_override


def test_rank_options_without_ranks_in_the_tree_are_an_error():
    from assaywatch.taxonomy import Taxonomy

    calls, years, taxids = _records_with_taxids({2025: {100: {"detect": 40}}})
    with pytest.raises(ValueError, match="ranks"):
        assess(
            calls,
            years,
            _ranked(group_at_rank="species"),
            today=TODAY,
            taxids=taxids,
            taxa_cache={},
            taxonomy=Taxonomy({100: 1}, {}),
        )


def test_a_lineage_that_is_the_whole_pool_overrides_only_if_the_assay_used_to_work():
    """One lineage holding every recent record is the pooled number again (West Nile vs CDV)."""
    never = _records_with_taxids(
        {2018: {100: {"detect": 4, "fail": 4}}, 2025: {100: {"detect": 25, "fail": 15}}}
    )
    worked = _records_with_taxids({2018: {100: {"detect": 50}}, 2025: {100: {"detect": 25, "fail": 15}}})
    cache = {100: "Lineage A"}
    a = assess(*never[:2], _gated(True), today=TODAY, taxids=never[2], taxa_cache=cache)["A"]
    b = assess(*worked[:2], _gated(True), today=TODAY, taxids=worked[2], taxa_cache=cache)["A"]
    assert a.status != "declining" and not a.lineage_override
    assert b.status == "declining"


def _patent_cfg(on: bool) -> dict:
    return {**CFG, "drift": {**CFG["drift"], "exclude_patent_records": on}}


def test_patent_records_leave_the_denominator_and_are_counted():
    """Orthopox ATI's shape: the natural records all detect, the constructs fail."""
    calls, years, _ = _records_with_taxids({2025: {1: {"detect": 30}, 2: {"fail": 30}}})
    patent = {r["record_id"] for r in calls if r["call"] == "fail"}
    off = assess(calls, years, _patent_cfg(False), today=TODAY, patent=patent)["A"]
    on = assess(calls, years, _patent_cfg(True), today=TODAY, patent=patent)["A"]
    assert off.recent_evaluable == 60 and off.patent_excluded == 0
    assert on.recent_evaluable == 30 and on.patent_excluded == 30
    assert on.recent_fraction == 1.0


def test_the_patent_option_without_the_record_set_is_an_error():
    calls, years, _ = _records_with_taxids({2025: {1: {"detect": 30}}})
    with pytest.raises(ValueError, match="patent record set"):
        assess(calls, years, _patent_cfg(True), today=TODAY)


def test_a_weak_pooled_verdict_is_overridden_only_by_a_lineage_that_used_to_work():
    """Pooled low coverage means no fall was ever shown, so a new lineage cannot claim one."""
    # Pooled share stays far below the threshold throughout, so the pooled
    # verdict is `low coverage`, not `stable`. Lineage 300 is new to the recent
    # window and failing; lineage 200 worked in 2018 and fails now.
    new_only = _records_with_taxids(
        {
            2018: {100: {"detect": 20, "fail": 80}},
            2025: {100: {"detect": 20, "fail": 80}, 300: {"fail": 40}},
        }
    )
    used_to_work = _records_with_taxids(
        {
            2018: {100: {"detect": 20, "fail": 80}, 200: {"detect": 40}},
            2025: {100: {"detect": 20, "fail": 80}, 200: {"fail": 40}},
        }
    )
    cache = {100: "Lineage A", 200: "Lineage B", 300: "Lineage C"}
    a = assess(*new_only[:2], _gated(True), today=TODAY, taxids=new_only[2], taxa_cache=cache)["A"]
    b = assess(*used_to_work[:2], _gated(True), today=TODAY, taxids=used_to_work[2], taxa_cache=cache)["A"]
    assert a.status == "low coverage" and not a.lineage_override
    assert "no fall to call a decline" in a.note
    assert b.status == "declining" and b.lineage_override


def test_a_failing_lineage_still_overrides_a_pooled_stable_without_having_worked():
    """The gate is only for a weak pooled verdict; an emerging lineage must still fire."""
    calls, years, taxids = _records_with_taxids(
        {2018: {100: {"detect": 50}}, 2025: {100: {"detect": 600}, 200: {"detect": 5, "fail": 35}}},
    )
    on = assess(calls, years, _gated(True), today=TODAY, taxids=taxids, taxa_cache={100: "A", 200: "B"})["A"]
    assert on.status == "declining" and on.lineage_override


# The status vocabulary. Two consumers used to keep their own copy of this list
# (report.py's section order, scripts/report_diff.py's row parser), and the copy
# is what let report_diff promote "## Nested protocols" to a status and drop 21
# assays. drift.py now owns it; these tests are what keep the export honest,
# since a new verdict added to `assess` would otherwise not reach either consumer.
def test_every_status_assess_can_assign_is_in_the_exported_vocabulary():
    """Read the assignments out of the source: a new one has to be declared."""
    import re
    from pathlib import Path

    from assaywatch import drift as drift_module

    src = Path(drift_module.__file__).read_text()
    assigned = set(re.findall(r'self\.status = "([^"]+)"', src))
    assigned |= set(re.findall(r'self\.status = "([^"]+)" if ', src))
    assert assigned, "no status assignments found; the regex has gone stale"
    assert assigned <= STATUSES, f"assigned but not exported: {sorted(assigned - STATUSES)}"


def test_the_vocabulary_claims_nothing_the_code_cannot_produce():
    """A status in the list that nothing assigns is a section no report can fill."""
    import re
    from pathlib import Path

    from assaywatch import drift as drift_module

    src = Path(drift_module.__file__).read_text()
    producible = set(re.findall(r'self\.status = "([^"]+)"', src)) | {NO_DATA}
    assert STATUSES == producible, f"exported but never assigned: {sorted(STATUSES - producible)}"


def test_no_data_is_the_default_and_is_not_a_verdict():
    """It means `assess` never ran on the assay, so it is not in the printed order."""
    assert AssayDrift(assay_id="A").status == NO_DATA
    assert NO_DATA in STATUSES and NO_DATA not in STATUS_ORDER


def test_the_report_and_the_diff_parser_read_the_same_vocabulary():
    import assaywatch.report as report

    assert report.STATUS_ORDER == list(STATUS_ORDER)
    assert set(report.STATUS_COLOUR) == set(STATUS_ORDER)  # every printed status has a colour


# The named stages (S4/S5). `assess` was 300 lines and `_lineage_check` 161 -
# the two places the audit named where a reader cannot hold the control flow in
# mind, both on the path that produces a verdict. Each stage is now callable on
# its own, which is what these tests use; the whole-pipeline behaviour is pinned
# separately by the tests above and by a byte-identical rebuild of
# results/2026-10-20's report and all 208 AssayDrift records.
def test_settings_come_from_the_config_with_the_documented_defaults():
    """These fallbacks must equal `assaywatch.settings`, which is the one home.

    They were a SECOND home, and this test asserted the drifted values: min
    records 20 against the calibrated 15, and `min_decline` 0.0 -- not asserted
    here at all -- against 0.05, which would have flagged any statistically real
    fall as drift. A fallback only fires when its key is absent, which is what a
    typo does, so the test pinning the wrong value made the drift look intended.
    `test_settings.py::test_every_in_code_fallback_matches_the_model` now checks
    the whole set mechanically rather than one by one.
    """
    from assaywatch.drift import DriftSettings
    from assaywatch.settings import Drift

    d = Drift()
    s = DriftSettings.from_config({})
    assert (s.base_months, s.threshold, s.min_records) == (
        d.recent_window_months,
        d.detect_fraction_threshold,
        d.min_records_for_drift,
    )
    assert (s.base_months, s.threshold, s.min_records) == (24, 0.9, 15)
    assert s.min_decline == d.min_decline == 0.05
    assert s.require_working_baseline is True  # on by default
    # Both denominator switches stay OFF when the key is absent, even though the
    # shipped config.yaml turns exclude_patent_records ON: `assess` refuses to run
    # that setting without a patent record set, so a caller that never mentioned
    # it has not supplied one. Absence means off; the file is where it is turned on.
    assert s.count_diverged is False and s.exclude_patent is False


def test_the_widening_ceiling_cannot_fall_below_the_base_window():
    """max_window_months below recent_window_months would make `choose` widen downward."""
    from assaywatch.drift import DriftSettings

    s = DriftSettings.from_config({"drift": {"recent_window_months": 36, "max_window_months": 12}})
    assert s.base_months == 36 and s.max_months == 36


def test_a_window_compares_at_the_granularity_its_input_has():
    """A 2024 record is recent against an Oct 2024 cutoff by year, not by date.
    Collapsing the two silently moved 90 records between windows."""
    from assaywatch.drift import Window

    by_year = Window(anchor=date(2026, 10, 3), dated=False)
    by_date = Window(anchor=date(2026, 10, 3), dated=True)
    assert by_year.inside("2024-01-01", 24) is True
    assert by_date.inside("2024-01-01", 24) is False
    assert by_date.inside("2024-11-01", 24) is True


def test_a_window_widens_only_as_far_as_reaching_the_minimum_needs():
    from assaywatch.drift import DriftSettings, Window

    s = DriftSettings.from_config({"drift": {"recent_window_months": 24, "max_window_months": 120}})
    w = Window(anchor=date(2026, 10, 3), dated=True)
    recent = [f"2025-01-{d:02d}" for d in range(1, 26)]  # 25 inside the base window
    assert w.choose(recent, s) == 24
    old = [f"2019-01-{d:02d}" for d in range(1, 26)]  # all older than 24 months
    assert w.choose(sorted(old, reverse=True), s) == 96  # widened to reach them, not to the ceiling


def test_an_assay_too_thin_to_judge_is_never_widened():
    """Fewer than min_records in total can never reach the bar, so widening would
    only stretch the meaning of "recent" for no gain."""
    from assaywatch.drift import DriftSettings, Window

    s = DriftSettings.from_config({"drift": {"max_window_months": 120, "min_records_for_drift": 20}})
    w = Window(anchor=date(2026, 10, 3), dated=True)
    assert w.choose(["2019-01-01", "2019-01-02"], s) == 24


def test_gathering_buckets_rows_per_assay_and_keeps_the_raw_rows_only_when_asked():
    from assaywatch.drift import DriftSettings, _gather_calls

    calls = [
        {"assay_id": "A", "record_id": "R1", "call": "detect"},
        {"assay_id": "B", "record_id": "R2", "call": "fail"},
    ]
    years = {"R1": "2025-01-01", "R2": "2025-01-01"}
    s = DriftSettings.from_config({})
    bare = _gather_calls(
        calls, years, s, taxids=None, scope_map=None, taxonomy=None, patent=None, keep_raw=False
    )
    assert sorted(bare.per) == ["A", "B"] and bare.raw == {}
    kept = _gather_calls(
        calls, years, s, taxids={}, scope_map=None, taxonomy=None, patent=None, keep_raw=True
    )
    assert sorted(kept.raw) == ["A", "B"]


def test_a_patent_record_leaves_the_denominator_and_is_counted():
    from assaywatch.drift import DriftSettings, _gather_calls

    calls = [
        {"assay_id": "A", "record_id": "R1.1", "call": "detect"},
        {"assay_id": "A", "record_id": "R2.1", "call": "fail"},
    ]
    s = DriftSettings.from_config({"drift": {"exclude_patent_records": True}})
    g = _gather_calls(
        calls,
        {"R1.1": 2025, "R2.1": 2025},
        s,
        taxids=None,
        scope_map=None,
        taxonomy=None,
        patent={"R2"},  # unversioned, as read_patent_accessions gives it
        keep_raw=False,
    )
    assert len(g.per["A"]) == 1 and g.patent["A"] == 1


def test_an_undated_record_is_skipped_rather_than_bucketed():
    """An unknown year silently landing in the recent window is the kind of error
    that produces a confident wrong answer."""
    from assaywatch.drift import AssayDrift, Window, _tally_window

    a = AssayDrift("A")
    rows = [(None, "detect", "", None, False), ("2025-01-01", "detect", "", None, False)]
    _tally_window(a, rows, Window(anchor=date(2026, 10, 3), dated=True), 24)
    assert a.skipped_undated == 1
    assert sum(a.recent_counts.values()) == 1


def test_one_record_without_a_footprint_makes_the_whole_count_unknown():
    """A partial count would be a lower bound presented as fact."""
    from assaywatch.drift import AssayDrift, Window, _tally_window

    w = Window(anchor=date(2026, 10, 3), dated=True)
    known = AssayDrift("A")
    _tally_window(known, [("2025-01-01", "detect", "", "|||0|0|0", False)], w, 24)
    assert known.recent_footprints == 1
    unknown = AssayDrift("B")
    _tally_window(
        unknown,
        [("2025-01-01", "detect", "", "|||0|0|0", False), ("2025-01-02", "fail", "", None, False)],
        w,
        24,
    )
    # Left at its default, which is None and not 0: "cannot say", not "no classes".
    assert unknown.recent_footprints is None


def test_species_counts_are_detected_over_evaluable_per_taxid():
    from assaywatch.drift import _species_counts

    calls = [
        {"taxid": 10, "call": "detect"},
        {"taxid": 10, "call": "fail"},
        {"taxid": 20, "call": "reduced"},
    ]
    assert _species_counts(calls) == {10: [1, 2], 20: [1, 1]}


def test_an_unsupported_group_at_rank_is_refused_by_name():
    from assaywatch.drift import LineageOptions

    with pytest.raises(ValueError, match="group_at_rank"):
        LineageOptions.from_config({"lineage": {"group_at_rank": "genus"}}, None)


def test_rolling_up_to_species_needs_a_taxonomy_with_ranks():
    from assaywatch.drift import LineageOptions

    with pytest.raises(ValueError, match="build_taxonomy_cache"):
        LineageOptions.from_config({"lineage": {"group_at_rank": "species"}}, None)


def test_the_lineage_options_default_to_grouping_per_taxid():
    from assaywatch.drift import LineageOptions
    from assaywatch.settings import Lineage

    o = LineageOptions.from_config({}, None)
    # `rank`/`buckets_on` default off because both REQUIRE drift.scope_taxonomy
    # with ranks and `from_config` raises without it; absence cannot imply them.
    assert o.rank is None and o.buckets_on is False
    # The gate and the floor are policy, and come from the model.
    lin = Lineage()
    assert o.gate is lin.require_working_baseline is True
    assert o.min_per_lineage == lin.min_records_per_lineage == 30


def test_one_lineage_holding_every_record_is_the_pooled_measurement_again():
    """So it cannot override: its history IS the assay's. Overriding would replace
    "no measurable fall" with a drift call (West Nile Lanciotti 2001 as of 2003).
    An assay that used to work still overrides (CDV Scagliarini 2007 as of 2021).

    Mutation-checked: skipping this gate passes every other test in this file and
    is caught only by the full 2026-10-20 rebuild, so it needs its own test.
    """
    from assaywatch.lineage import LineageStats

    def drift(*, worked: bool) -> AssayDrift:
        a = AssayDrift("A", recent_year=2025, threshold=0.9, min_records_for_year=10)
        a.recent_evaluable = 50
        # `ever_worked` is derived from the year table, per year, not set directly.
        share = {"detect": 20} if worked else {"detect": 2, "fail": 18}
        a.years[2019] = YearStats(2019, Counter(share))
        assert a.ever_worked is worked
        return a

    only = [LineageStats("A", "Lineage A", 10, 50, 5, 0.1, 0.03, 0.22)]
    assert drift(worked=False)._pool_is_one_lineage(only) is True
    assert drift(worked=True)._pool_is_one_lineage(only) is False

    a = drift(worked=False)
    part = [LineageStats("A", "Lineage A", 10, 30, 3, 0.1, 0.03, 0.22)]  # 30 of 50: a real subset
    assert a._pool_is_one_lineage(part) is False
    assert a._pool_is_one_lineage(only + [LineageStats("A", "B", 20, 10, 9, 0.9, 0.6, 0.98)]) is False


def test_the_one_lineage_gate_is_actually_wired_into_the_check():
    """The predicate having the right answer does not prove `_lineage_check` asks it.

    A direct test of `_pool_is_one_lineage` still passes when the call site is
    removed, so this goes through the check and asserts the effect: one lineage
    holding every recent record, an assay that never worked, no override.
    """
    # One taxid only, failing now, and nothing earlier that cleared the threshold.
    calls, years, taxids = _records_with_taxids(
        {2019: {100: {"detect": 5, "fail": 45}}, 2025: {100: {"detect": 3, "fail": 47}}}
    )
    a = assess(calls, years, LINEAGE_CFG, today=TODAY, taxids=taxids, taxa_cache={100: "Lineage A"})["A"]
    assert not a.ever_worked
    assert a.lineage_override is False and a.status_pooled is None
    assert a.lineage_verdict is not None  # the verdict is still recorded
    # And the counterpart: a second lineage means the pool is not one lineage, so
    # the gate does not apply and the override is free to fire.
    calls2, years2, taxids2 = _records_with_taxids(
        {2019: {100: {"detect": 50}}, 2025: {100: {"detect": 600}, 200: {"detect": 5, "fail": 35}}}
    )
    b = assess(calls2, years2, LINEAGE_CFG, today=TODAY, taxids=taxids2, taxa_cache={100: "A", 200: "B"})["A"]
    assert b.lineage_override is True and b.status == "declining"


def test_every_caller_of_assess_passes_the_patent_set():
    """`drift.exclude_patent_records` makes `assess` refuse to run without the
    patent set. sitedrift.py called it without one, which was harmless only while
    the option was off -- turning it on would have crashed the `site_drift` rule.
    A source check, in the style of the other repo-consistency tests, because the
    failure only shows on a real run with the option on."""
    import ast
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    missing = []
    for path in [*(root / "assaywatch").glob("*.py"), *(root / "scripts").glob("*.py")]:
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id == "assess"
                and not any(k.arg == "patent" for k in node.keywords)
            ):
                missing.append(f"{path.relative_to(root)}:{node.lineno}")
    assert not missing, "assess() called without patent=: " + ", ".join(missing)


def test_jeffreys_reproduces_the_baseline_docs_hand_computed_figures():
    """docs/2026-10-23-baseline.md quotes three Jeffreys intervals, computed by
    hand because the function did not exist. These are those three."""
    from assaywatch.interval import jeffreys_interval

    for k, n, lo, hi in ((5, 11, 20.0, 73.0), (5, 8, 29.5, 88.1), (2, 9, 4.9, 54.4)):
        got = jeffreys_interval(k, n)
        assert (round(100 * got[0], 1), round(100 * got[1], 1)) == (lo, hi), (k, n, got)


def test_jeffreys_edges_and_empty():
    """The conventional modification: 0 at k=0, 1 at k=n, and (0,1) for n=0 as
    wilson_interval does. A bare quantile leaves a small residue instead."""
    from assaywatch.interval import jeffreys_interval

    assert jeffreys_interval(0, 20)[0] == 0.0
    assert jeffreys_interval(20, 20)[1] == 1.0
    assert jeffreys_interval(0, 0) == (0.0, 1.0)
    # Not zero-width at the edges, which is the whole complaint against Wald.
    assert jeffreys_interval(0, 20)[1] > 0.05
    assert jeffreys_interval(20, 20)[0] < 0.95


def test_jeffreys_is_narrower_as_n_grows_and_contains_the_point():
    from assaywatch.interval import jeffreys_interval

    widths = []
    for n in (10, 50, 250):
        lo, hi = jeffreys_interval(n // 2, n)
        assert lo < 0.5 < hi
        widths.append(hi - lo)
    assert widths == sorted(widths, reverse=True), widths
