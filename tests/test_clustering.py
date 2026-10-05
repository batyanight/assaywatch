"""The duplication check: does a flag survive counting each footprint once?

`drift.py` documents that Wilson assumes independent records and that GenBank
records are not. These tests pin the response to that, and, as importantly, what
it is NOT allowed to do: it is reported beside a verdict and never feeds one, so
the first test asserts that statuses and intervals are identical with and
without footprints.
"""

from datetime import date

from assaywatch.drift import FOOTPRINT_COLUMNS, assess, footprint_signature

CFG = {
    "drift": {
        "detect_fraction_threshold": 0.90,
        "recent_window_months": 24,
        "min_records_for_drift": 20,
        "min_records_for_coverage": 10,
    }
}
TODAY = date(2026, 10, 3)


def rows(spec, with_footprint=True):
    """spec: [(year, call, footprint, n)] -> (calls, years)."""
    calls, years = [], {}
    i = 0
    for year, call, fp, n in spec:
        for _ in range(n):
            rid = f"AB{i:05d}"
            row = {"assay_id": "A", "record_id": rid, "call": call}
            if with_footprint:
                row["footprint"] = fp
            calls.append(row)
            years[rid] = year
            i += 1
    return calls, years


# 80 records match exactly and 20 fail, the failures sharing 4 footprints.
# p = 0.80 at n = 100 puts the Wilson upper bound near 0.88: below 0.90, so
# flagged. Counted once per footprint it is 4 detections in 5 draws, whose
# upper bound is near 0.96: the flag evaporates.
DUPLICATED = [
    (2025, "detect", "", 80),
    (2025, "fail", "1|||||", 5),
    (2025, "fail", "2|||||", 5),
    (2025, "fail", "3|||||", 5),
    (2025, "fail", "4|||||", 5),
]


def test_footprints_never_change_a_status_or_an_interval():
    """The load-bearing property. Reported beside a verdict, never into one."""
    with_fp = assess(*rows(DUPLICATED), CFG, today=TODAY)["A"]
    without = assess(*rows(DUPLICATED, with_footprint=False), CFG, today=TODAY)["A"]
    assert with_fp.status == without.status
    assert with_fp.recent_ci == without.recent_ci
    assert with_fp.change_ci == without.change_ci
    assert with_fp.note == without.note


def test_rows_without_footprints_report_nothing_rather_than_guessing():
    """Every hand-built row, and every table screened before these columns
    existed, lands here. Unknown must not read as "all identical"."""
    a = assess(*rows(DUPLICATED, with_footprint=False), CFG, today=TODAY)["A"]
    assert a.recent_footprints is None and a.baseline_footprints is None
    assert a.flag_survives_clustering is None
    assert a.clustering_note == ""


def test_one_row_without_a_footprint_makes_the_whole_assay_unknown():
    """A partial count is a lower bound on distinct footprints, hence an interval
    that is too wide, presented as a measurement."""
    calls, years = rows(DUPLICATED)
    del calls[0]["footprint"]
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.recent_footprints is None
    assert a.flag_survives_clustering is None


def test_a_flag_that_rests_on_duplicated_records_is_marked_as_not_surviving():
    a = assess(*rows(DUPLICATED), CFG, today=TODAY)["A"]
    assert a.status == "low coverage"
    assert a.recent_footprints == 5  # one exact match plus four failing footprints
    assert a.recent_evaluable == 100
    assert a.recent_ci[1] < 0.90 <= a.recent_ci_clustered[1]
    assert a.flag_survives_clustering is False
    assert "the SHARE failing may reflect how many near-identical" in a.clustering_note
    # Must not claim the failure itself is spurious: 92 identical failures is
    # one real lineage failing, and only its weight in the proportion is in doubt.
    assert "may well be real" in a.clustering_note
    assert "20.0 per footprint" in a.clustering_note


def test_a_flag_with_genuinely_distinct_failures_survives():
    """Every failing record has a footprint of its own, so there is nothing to
    collapse and the clustered interval is no wider than it should be."""
    spec = [(2025, "detect", "", 10)] + [(2025, "fail", f"{i}|||||", 1) for i in range(40)]
    a = assess(*rows(spec), CFG, today=TODAY)["A"]
    assert a.status == "low coverage"
    assert a.recent_footprints == 41
    assert a.flag_survives_clustering is True
    assert "does not depend on duplicated records" in a.clustering_note


def test_the_clustered_interval_is_never_narrower_than_the_record_level_one():
    """Fewer independent draws cannot make an estimate more certain."""
    for spec in (
        DUPLICATED,
        [(2025, "detect", "", 30), (2025, "fail", "x|||||", 30)],
        [(2025, "detect", "", 50), (2025, "detect", "1|||||", 50)],
    ):
        a = assess(*rows(spec), CFG, today=TODAY)["A"]
        (lo, hi), (clo, chi) = a.recent_ci, a.recent_ci_clustered
        assert clo <= lo + 1e-9 and chi >= hi - 1e-9, (spec, a.recent_ci, a.recent_ci_clustered)


def test_it_says_nothing_about_a_stable_assay():
    """A stable verdict rests on the point estimate, which clustering does not
    move, so there is no flag to defend and nothing to report."""
    a = assess(*rows([(2025, "detect", "", 100)]), CFG, today=TODAY)["A"]
    assert a.status == "stable"
    assert a.flag_survives_clustering is None
    assert a.clustering_note == ""


def test_declining_must_survive_on_both_intervals_not_just_the_recent_one():
    """`declining` needs the change interval to exclude zero as well. A recent
    interval that stays below threshold is not enough if the baseline was itself
    only a few clones."""
    spec = [
        (2020, "detect", "", 100),
        (2025, "detect", "", 20),
        (2025, "fail", "1|||||", 15),
        (2025, "fail", "2|||||", 15),
    ]
    a = assess(*rows(spec), CFG, today=TODAY)["A"]
    assert a.status == "declining"
    # Baseline: 100 identical exact matches is ONE footprint, so a single draw.
    assert a.baseline_footprints == 1
    assert a.change_ci_clustered[1] >= 0  # the drop no longer excludes zero
    assert a.flag_survives_clustering is False


def test_the_footprint_is_the_call_and_the_mismatch_pattern_together():
    """Two records with the same mismatches but different calls are different
    footprints: the call is a function of more than the positions."""
    spec = [(2025, "detect", "1|||||", 30), (2025, "fail", "1|||||", 30)]
    a = assess(*rows(spec), CFG, today=TODAY)["A"]
    assert a.recent_footprints == 2


def test_the_signature_is_built_from_the_six_screen_columns():
    assert len(FOOTPRINT_COLUMNS) == 6
    assert FOOTPRINT_COLUMNS[0] == "fwd_mm_from_3prime"
    assert footprint_signature(["", "", "", "", "", ""]) == "|||||"
    assert footprint_signature(["1", "", "", "", "", ""]) != footprint_signature(["", "1", "", "", "", ""])


def test_equal_signatures_are_one_object():
    """Interned, so two million exact matches are one string, not two million."""
    a = footprint_signature(["1,2", "", "", "", "", ""])
    b = footprint_signature(["1,2", "", "", "", "", ""])
    assert a is b


def test_the_footprint_count_cannot_exceed_the_record_count():
    """n_footprints <= n_records by construction, and is clamped regardless:
    claiming more independent draws than records would narrow the interval."""
    a = assess(*rows([(2025, "detect", f"{i}|||||", 1) for i in range(25)]), CFG, today=TODAY)["A"]
    assert a.recent_footprints == a.recent_evaluable == 25
    assert a.recent_ci_clustered == a.recent_ci


def test_read_calls_folds_the_six_columns_into_one_footprint(tmp_path):
    """The path real data takes: a screen TSV in, one interned string per row out.

    Two exact matches must share a footprint object and a mismatched record must
    differ, and a table lacking the columns must yield rows with NO footprint key
    at all - unknown, which `assess` treats differently from all-identical.
    """
    from assaywatch.report import read_calls

    header = ["assay_id", "record_id", "call", "exclusion", *FOOTPRINT_COLUMNS]
    good = tmp_path / "calls.tsv"
    good.write_text(
        "\t".join(header)
        + "\n"
        + "\t".join(["A", "R1", "detect", "", "", "", "", "", "", ""])
        + "\n"
        + "\t".join(["A", "R2", "detect", "", "", "", "", "", "", ""])
        + "\n"
        + "\t".join(["A", "R3", "fail", "", "1", "", "", "", "", ""])
        + "\n"
    )
    rows = read_calls(good)
    assert rows[0]["footprint"] == rows[1]["footprint"] and rows[0]["footprint"] is rows[1]["footprint"]
    assert rows[2]["footprint"] != rows[0]["footprint"]

    old = tmp_path / "old.tsv"
    old.write_text("assay_id\trecord_id\tcall\texclusion\nA\tR1\tdetect\t\n")
    assert "footprint" not in read_calls(old)[0]


def test_a_partial_set_of_footprint_columns_is_treated_as_none(tmp_path):
    """All six or none. A partial footprint would compare unequal to a full one
    that agrees with it, inflating the distinct count and narrowing the interval."""
    from assaywatch.report import read_calls

    p = tmp_path / "calls.tsv"
    p.write_text("assay_id\trecord_id\tcall\texclusion\tfwd_mm_from_3prime\nA\tR1\tdetect\t\t1\n")
    assert "footprint" not in read_calls(p)[0]


def test_the_report_states_how_many_flags_survive():
    from assaywatch.report import duplication_summary

    dup = assess(*rows(DUPLICATED), CFG, today=TODAY)["A"]
    distinct = assess(
        *rows([(2025, "detect", "", 10)] + [(2025, "fail", f"{i}|||||", 1) for i in range(40)]),
        CFG,
        today=TODAY,
    )["A"]
    text = duplication_summary([dup, distinct])
    assert text.startswith("1 of 2 flagged assays still hold"), text
    assert duplication_summary([]) == ""


def test_an_unchecked_flag_is_not_counted_as_a_surviving_one():
    """A table screened before the footprint columns existed must not read as a
    clean bill of health."""
    from assaywatch.report import duplication_summary

    unchecked = assess(*rows(DUPLICATED, with_footprint=False), CFG, today=TODAY)["A"]
    assert unchecked.status == "low coverage"
    assert duplication_summary([unchecked]) == ""

    checked = assess(
        *rows([(2025, "detect", "", 10)] + [(2025, "fail", f"{i}|||||", 1) for i in range(40)]),
        CFG,
        today=TODAY,
    )["A"]
    text = duplication_summary([checked, unchecked])
    assert "1 of 1 flagged assays still hold" in text and "1 could not be checked" in text, text


def test_the_duplication_check_reaches_the_rendered_report():
    from assaywatch.report import render_html, render_markdown

    drifts = assess(*rows(DUPLICATED), CFG, today=TODAY)
    md = render_markdown(drifts, {}, [], "2026-10-05", CFG)
    assert "Duplication check" in md and "0 of 1 flagged assays" in md, md
    assert "20.0 per footprint" in md
    page = render_html(drifts, {}, [], "2026-10-05", CFG)
    assert "Duplication check" in page


def test_a_clean_sweep_does_not_mention_a_remainder():
    from assaywatch.report import duplication_summary

    distinct = assess(
        *rows([(2025, "detect", "", 10)] + [(2025, "fail", f"{i}|||||", 1) for i in range(40)]),
        CFG,
        today=TODAY,
    )["A"]
    text = duplication_summary([distinct])
    assert text.startswith("1 of 1 flagged assays still hold"), text
    assert "remainder" not in text, text
    dup = assess(*rows(DUPLICATED), CFG, today=TODAY)["A"]
    assert "remainder rest on a few footprints" in duplication_summary([dup])
