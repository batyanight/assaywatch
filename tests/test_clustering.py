"""The duplication check: does a flag survive counting each footprint once?

`drift.py` documents that Wilson assumes independent records and that GenBank
records are not. These tests pin the response to that, and, as importantly, what
it is NOT allowed to do: it is reported beside a verdict and never feeds one.

Footprints here are built two ways. `rows()` makes them by hand, which is fast and
lets a test choose exactly how many distinct ones exist. `real_table()` builds them
from `Call.as_row()`, the thing the pipeline actually writes, so a test that
depends on what a screen row contains is tested against what a screen row contains
rather than against what its author remembered.
"""

import csv
import random
from datetime import date

from assaywatch.drift import (
    FOOTPRINT_COLUMNS,
    FOOTPRINT_REQUIRED,
    assess,
    footprint_signature,
)
from assaywatch.score import Call, OligoScore

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


def fp(i: int) -> str:
    """The i-th distinct footprint."""
    return f"{i}|||0|0|"


# 80 records match exactly and 20 fail, the failures sharing 4 footprints. p = 0.80
# at n = 100 puts the Wilson upper bound near 0.87: below 0.90, so flagged. Counted
# once per footprint it is 4 detections in 5 draws, whose upper bound is near 0.96.
DUPLICATED = [
    (2025, "detect", fp(0), 80),
    (2025, "fail", fp(1), 5),
    (2025, "fail", fp(2), 5),
    (2025, "fail", fp(3), 5),
    (2025, "fail", fp(4), 5),
]

# The malB case this check was written for: one lineage fails, 92 times, at one
# footprint, against 70 detections sharing another.
MALB = [(2025, "detect", fp(0), 70), (2025, "fail", fp(1), 92)]

# Every failing record has a footprint of its own: nothing to collapse.
DISTINCT = [(2025, "detect", fp(0), 10)] + [(2025, "fail", fp(i), 1) for i in range(1, 41)]


# --------------------------------------------------------------------------
# The load-bearing property: never a verdict
# --------------------------------------------------------------------------

DATASETS = {
    "low-coverage-duplicated": DUPLICATED,
    "low-coverage-distinct": DISTINCT,
    "malb": MALB,
    "stable": [(2025, "detect", fp(0), 60)],
    "declining": [
        (2020, "detect", fp(0), 100),
        (2025, "detect", fp(0), 20),
        (2025, "fail", fp(1), 15),
        (2025, "fail", fp(2), 15),
    ],
    "watch": [(2025, "detect", fp(0), 22), (2025, "fail", fp(1), 3)],
    "insufficient": [(2025, "detect", fp(0), 3), (2025, "fail", fp(1), 2)],
    "no-recent": [(2015, "detect", fp(0), 40)],
    "with-baseline": [
        (2015, "detect", fp(0), 40),
        (2015, "fail", fp(5), 40),
        (2025, "detect", fp(0), 40),
        (2025, "fail", fp(5), 40),
    ],
}


def test_footprints_never_change_a_status_an_interval_or_a_note():
    """The load-bearing property, over EVERY status the pipeline can emit.

    It used to run on one dataset whose only status was `low coverage`, with no
    baseline, so a mutation that let footprints influence `declining`, `watch` or
    `stable` survived it.
    """
    statuses = set()
    for name, spec in DATASETS.items():
        with_fp = assess(*rows(spec), CFG, today=TODAY).get("A")
        without = assess(*rows(spec, with_footprint=False), CFG, today=TODAY).get("A")
        assert with_fp is not None and without is not None, name
        statuses.add(with_fp.status)
        assert with_fp.status == without.status, name
        assert with_fp.recent_ci == without.recent_ci, name
        assert with_fp.baseline_ci == without.baseline_ci, name
        assert with_fp.change_ci == without.change_ci, name
        assert with_fp.note == without.note, name
        assert (with_fp.recent_detected, with_fp.recent_evaluable) == (
            without.recent_detected,
            without.recent_evaluable,
        ), name
    # The datasets really do span the statuses, or the loop above proves little.
    assert {"stable", "declining", "low coverage", "watch", "insufficient data", "no recent data"} <= statuses


# --------------------------------------------------------------------------
# Unknown is not "all identical"
# --------------------------------------------------------------------------


def test_rows_without_footprints_report_nothing_rather_than_guessing():
    a = assess(*rows(DUPLICATED, with_footprint=False), CFG, today=TODAY)["A"]
    assert a.recent_footprints is None and a.baseline_footprints is None
    assert a.flag_survives_clustering is None
    assert a.clustering_note == ""


def test_one_evaluable_row_without_a_footprint_makes_the_whole_assay_unknown():
    """A partial count is a lower bound on distinct footprints, hence an interval
    that is too wide, presented as a measurement."""
    calls, years = rows(DUPLICATED)
    del calls[0]["footprint"]
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.recent_footprints is None and a.flag_survives_clustering is None


def test_non_evaluable_rows_do_not_affect_the_footprint_count():
    """Real calls tables are mostly no_amplicon and indeterminate. They carry no
    footprint and must neither count as one nor make the assay unknown. Every
    fixture used to be detect or fail only, so deleting the `call in EVALUABLE`
    guard survived."""
    spec = [*DUPLICATED, (2025, "no_amplicon", fp(99), 500), (2025, "indeterminate", fp(98), 30)]
    base = assess(*rows(DUPLICATED), CFG, today=TODAY)["A"]
    noisy = assess(*rows(spec), CFG, today=TODAY)["A"]
    assert noisy.recent_footprints == base.recent_footprints == 5
    assert noisy.recent_evaluable == base.recent_evaluable == 100
    # ...and non-evaluable rows with NO footprint do not poison it either.
    calls, years = rows(DUPLICATED)
    extra, extra_years = rows([(2025, "no_amplicon", None, 200)], with_footprint=False)
    for row in extra:
        row["record_id"] = "X" + row["record_id"]
    extra_years = {"X" + k: v for k, v in extra_years.items()}
    mixed = assess(calls + extra, {**years, **extra_years}, CFG, today=TODAY)["A"]
    assert mixed.recent_footprints == 5


def test_diverged_records_counted_as_failures_have_no_footprint():
    """With count_diverged_as_fail, a diverged record becomes a `fail` but was never
    scored, so all six footprint columns are empty. They used to be read as ONE
    footprint, collapsing 30 different diverged records into a single class and
    producing a duplication verdict out of a placeholder."""
    cfg = {"drift": {**CFG["drift"], "count_diverged_as_fail": True}}
    calls, years = rows([(2025, "detect", fp(0), 70)])
    # These rows CARRY the all-empty signature, as the review reproduced: any caller
    # that hands assess() a footprint for an unscored record must not have it
    # counted. read_calls no longer produces one (see the blank-cell tests below), so
    # this guards assess() as a public function, not just as read_calls' consumer.
    div, div_years = rows([(2025, "no_amplicon", "|||||", 30)])
    for row in div:
        row["record_id"] = "D" + row["record_id"]
        row["exclusion"] = "diverged"
    div_years = {"D" + k: v for k, v in div_years.items()}
    a = assess(calls + div, {**years, **div_years}, cfg, today=TODAY)["A"]
    assert a.status == "low coverage"  # the diverged records really were counted as failures
    assert a.recent_footprints is None
    assert a.flag_survives_clustering is None and a.clustering_note == ""

    # Switched off, the same records are simply not evaluable and the check works.
    off = assess(calls + div, {**years, **div_years}, CFG, today=TODAY)["A"]
    assert off.recent_footprints == 1


# --------------------------------------------------------------------------
# The verdict
# --------------------------------------------------------------------------


def test_a_flag_that_rests_on_duplicated_records_is_marked_as_not_surviving():
    a = assess(*rows(DUPLICATED), CFG, today=TODAY)["A"]
    assert a.status == "low coverage"
    assert a.recent_footprints == 5 and a.recent_evaluable == 100
    assert a.recent_ci[1] < 0.90 <= a.recent_ci_clustered[1]
    assert a.flag_survives_clustering is False
    assert "the SHARE failing may reflect how many near-identical" in a.clustering_note
    # Must not claim the failure itself is spurious: 92 identical failures is one
    # real lineage failing, and only its weight in the proportion is in doubt.
    assert "may well be real" in a.clustering_note
    assert "20.0 per footprint" in a.clustering_note


def test_a_flag_with_genuinely_distinct_failures_survives():
    a = assess(*rows(DISTINCT), CFG, today=TODAY)["A"]
    assert a.status == "low coverage"
    assert a.recent_footprints == 41
    assert a.flag_survives_clustering is True and a.cluster_failures == ()
    assert "does not depend on duplicated records" in a.clustering_note


def test_the_malb_case_is_reported_as_resting_on_two_footprints_not_as_surviving():
    """The case this check was written for, and the one it got backwards.

    92 identical failures against 70 identical detections: two footprints. The
    clustered Wilson upper bound at n = 2 is 88%, 'below the 90% threshold', so
    with no floor the check said the flag 'does not depend on duplicated records'.
    docs/2026-10-04-pipeline-review.md says it will report this flag as resting on
    a single footprint deposited 92 times.
    """
    a = assess(*rows(MALB), CFG, today=TODAY)["A"]
    assert a.status == "low coverage" and a.recent_footprints == 2
    assert a.recent_ci_clustered[1] < a.threshold  # the interval alone WOULD have passed it
    assert a.flag_survives_clustering is False
    assert "too_few" in a.cluster_failures
    assert "only 2 distinct footprint(s)" in a.clustering_note
    assert "does not depend on duplicated records" not in a.clustering_note


def test_a_single_footprint_cannot_survive():
    a = assess(*rows([(2025, "fail", fp(0), 100)]), CFG, today=TODAY)["A"]
    assert a.recent_footprints == 1 and a.recent_ci_clustered[1] < a.threshold
    assert a.flag_survives_clustering is False and "too_few" in a.cluster_failures


def test_the_footprint_floor_is_the_record_level_floor_exactly():
    """19 distinct footprints cannot carry a flag and 20 can, because
    min_records_for_drift is 20 and the record-level rule will not flag on fewer."""

    def spec(distinct_failures):
        return [(2025, "detect", fp(0), 30)] + [
            (2025, "fail", fp(i), 1) for i in range(1, distinct_failures + 1)
        ]

    below = assess(*rows(spec(18)), CFG, today=TODAY)["A"]  # 1 + 18 = 19 footprints
    at = assess(*rows(spec(19)), CFG, today=TODAY)["A"]  # 1 + 19 = 20 footprints
    assert (below.recent_footprints, at.recent_footprints) == (19, 20)
    assert below.status == at.status == "low coverage"
    assert below.flag_survives_clustering is False and "too_few" in below.cluster_failures
    assert at.flag_survives_clustering is True


def test_the_floor_follows_the_configured_minimum():
    cfg = {"drift": {**CFG["drift"], "min_records_for_drift": 5}}
    a = assess(*rows(MALB), cfg, today=TODAY)["A"]
    assert a.flag_survives_clustering is False  # 2 footprints < 5
    # 10 detections sharing one footprint plus 10 distinct failures: flagged at the
    # record level, 11 footprints, comfortably above a floor of 5.
    spec = [(2025, "detect", fp(0), 10)] + [(2025, "fail", fp(i), 1) for i in range(1, 11)]
    ok = assess(*rows(spec), cfg, today=TODAY)["A"]
    assert ok.status == "low coverage" and ok.recent_footprints == 11
    assert ok.flag_survives_clustering is True
    # The same table under the default floor of 20 does not survive.
    assert assess(*rows(spec), CFG, today=TODAY)["A"].flag_survives_clustering is False


# --------------------------------------------------------------------------
# The note names the test that failed
# --------------------------------------------------------------------------


def test_a_declining_flag_that_fails_only_on_the_change_interval_says_so():
    """A homogeneous baseline is ONE footprint however many records it holds, so a
    fall from it is a drop from a single draw. Here the recent window has plenty of
    footprints (21) and its interval stays far below the 90% threshold, so the
    recent interval is not the problem; only the change from baseline no longer
    excludes zero. The note used to say the threshold was no longer ruled out, which
    was false, and never gave the real reason."""
    spec = (
        [(2020, "detect", fp(0), 100)]
        + [(2025, "detect", fp(0), 12)]
        + [(2025, "fail", fp(i), 1) for i in range(1, 21)]
    )
    a = assess(*rows(spec), CFG, today=TODAY)["A"]
    assert a.status == "declining" and a.baseline_footprints == 1 and a.recent_footprints == 21
    assert a.recent_ci_clustered[1] < a.threshold  # the recent interval is NOT the problem
    assert a.cluster_failures == ("change",), a.cluster_failures
    assert "no longer excludes zero" in a.clustering_note
    assert "no longer rules out the 90% threshold" not in a.clustering_note
    assert "only" not in a.clustering_note.split("This flag does not hold up:")[1].split(";")[0]


def test_every_failing_reason_is_named_when_several_apply():
    """Two footprints is too few AND its widened interval reaches the threshold."""
    a = assess(*rows([(2025, "detect", fp(0), 80), (2025, "fail", fp(1), 20)]), CFG, today=TODAY)["A"]
    assert a.status == "low coverage"
    assert {"too_few", "recent"} <= set(a.cluster_failures), a.cluster_failures
    assert "only 2 distinct footprint(s)" in a.clustering_note
    assert "no longer rules out the 90% threshold" in a.clustering_note


def test_a_surviving_declining_flag_reports_both_intervals():
    """Many distinct footprints on both sides: the recent interval stays low and
    the fall from baseline still excludes zero."""
    spec = (
        [(2020, "detect", fp(i), 1) for i in range(60)]
        + [(2025, "detect", fp(100), 5)]
        + [(2025, "fail", fp(200 + i), 1) for i in range(60)]
    )
    a = assess(*rows(spec), CFG, today=TODAY)["A"]
    assert a.status == "declining" and a.flag_survives_clustering is True, (a.status, a.cluster_failures)
    assert "still excludes zero" in a.clustering_note


def test_the_clustered_interval_is_never_narrower_than_the_record_level_one():
    """Fewer independent draws cannot make an estimate more certain."""
    for name, spec in DATASETS.items():
        a = assess(*rows(spec), CFG, today=TODAY).get("A")
        if a is None or not a.recent_evaluable or a.recent_footprints is None:
            continue
        (lo, hi), (clo, chi) = a.recent_ci, a.recent_ci_clustered
        assert clo <= lo + 1e-9 and chi >= hi - 1e-9, (name, a.recent_ci, a.recent_ci_clustered)


def test_it_says_nothing_about_a_stable_assay():
    a = assess(*rows(DATASETS["stable"]), CFG, today=TODAY)["A"]
    assert a.status == "stable" and a.flag_survives_clustering is None and a.clustering_note == ""


def test_the_footprint_is_the_call_and_the_mismatch_pattern_together():
    a = assess(*rows([(2025, "detect", fp(1), 30), (2025, "fail", fp(1), 30)]), CFG, today=TODAY)["A"]
    assert a.recent_footprints == 2


def test_footprints_never_outnumber_the_records_that_carry_them():
    """The clamp that used to guard this was unreachable, and the test of it passed
    with the clamp removed. The invariant is real, so it is checked as one: over
    many random tables, distinct footprints never exceed evaluable records."""
    rng = random.Random(7)
    for _ in range(200):
        spec = [
            (2025, rng.choice(["detect", "reduced", "fail"]), fp(rng.randint(0, 12)), rng.randint(1, 6))
            for _ in range(rng.randint(1, 12))
        ]
        a = assess(*rows(spec), CFG, today=TODAY)["A"]
        assert a.recent_footprints <= a.recent_evaluable
        assert a.baseline_footprints == 0 or a.baseline_footprints <= a.baseline_evaluable


# --------------------------------------------------------------------------
# What a real screen row contains
# --------------------------------------------------------------------------


def scored(penalty, mm_from_3prime=(), ambiguous=()):
    return OligoScore(
        penalty=penalty,
        terminal_mismatch=1 in mm_from_3prime,
        mismatches=(),
        mismatches_from_3prime=tuple(mm_from_3prime),
        ambiguous=tuple(ambiguous),
    )


def real_row(call="detect", **kw):
    return Call("A", kw.pop("rid", "R1"), call, **kw).as_row()


def write_tsv(path, rows_):
    keys = list(rows_[0])
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, keys, delimiter="\t")
        w.writeheader()
        w.writerows(rows_)
    return path


def test_the_footprint_columns_and_their_prerequisites_are_what_a_screen_writes():
    """Replaces a test that asserted a tuple had length 6 and a first element equal
    to its own literal. This one fails if Call.as_row stops writing a column the
    footprint is built from, or renames one."""
    written = set(real_row())
    assert set(FOOTPRINT_COLUMNS) <= written, set(FOOTPRINT_COLUMNS) - written
    assert set(FOOTPRINT_REQUIRED) <= written, set(FOOTPRINT_REQUIRED) - written


def test_read_calls_builds_the_footprint_from_a_real_screen_row(tmp_path):
    from assaywatch.report import read_calls

    exact = real_row("detect", rid="R1", forward=scored(0.0), reverse=scored(0.0))
    same = real_row("detect", rid="R2", forward=scored(0.0), reverse=scored(0.0))
    other = real_row(
        "fail", rid="R3", forward=scored(5.5, (7, 1)), reverse=scored(0.0), probe=scored(1.0, (4,))
    )
    got = read_calls(write_tsv(tmp_path / "calls.tsv", [exact, same, other]))
    assert got[0]["footprint"] == "|||0|0|"  # an exact match is NOT the all-empty string
    assert got[0]["footprint"] is got[1]["footprint"]  # interned: one object
    assert got[2]["footprint"] == "7,1||4|0|0|0"
    assert got[2]["footprint"] != got[0]["footprint"]


def test_a_row_the_screen_did_not_score_has_no_footprint(tmp_path):
    """no_amplicon rows have every scoring column blank. They are not evaluable, so
    it does not matter to the count, but they must not be handed a signature."""
    from assaywatch.report import read_calls

    got = read_calls(write_tsv(tmp_path / "calls.tsv", [real_row("no_amplicon", rid="R1")]))
    assert "footprint" not in got[0]


def test_a_table_without_the_columns_yields_no_footprint_at_all(tmp_path):
    from assaywatch.report import read_calls

    old = tmp_path / "old.tsv"
    old.write_text("assay_id\trecord_id\tcall\texclusion\nA\tR1\tdetect\t\n")
    assert "footprint" not in read_calls(old)[0]


def test_blank_filled_rows_from_an_older_screen_are_unknown_not_a_clean_footprint(tmp_path):
    """THE CASE concatenate_screens EXISTS FOR, meeting the duplication check.

    An older screen lacks the footprint columns. concatenate_screens unions the
    headers and blank-fills them, so the older rows arrive with all six columns
    present and empty - the same cells a clean record has. Unchecked, 60 old rows
    became ONE real footprint and the report said 'these records may reflect how
    many near-identical records were deposited' about data that carried no
    information at all."""
    from assaywatch.collect import concatenate_screens
    from assaywatch.report import duplication_summary, read_calls

    old_cols = ["assay_id", "record_id", "call", "exclusion"]
    old = tmp_path / "old.tsv"
    with open(old, "w", newline="") as fh:
        w = csv.DictWriter(fh, old_cols, delimiter="\t")
        w.writeheader()
        for i in range(30):
            w.writerow({"assay_id": "A", "record_id": f"OLD{i:03d}", "call": "detect", "exclusion": ""})
        for i in range(30):
            w.writerow({"assay_id": "A", "record_id": f"OLF{i:03d}", "call": "fail", "exclusion": ""})
    new = write_tsv(
        tmp_path / "new.tsv",
        [real_row("detect", rid="NEW1", forward=scored(0.0), reverse=scored(0.0))],
    )
    merged = tmp_path / "calls.tsv.gz"
    concatenate_screens([old, new], merged)
    calls = read_calls(merged)
    assert sum("footprint" in r for r in calls) == 1  # only the genuinely new row
    years = {r["record_id"]: 2025 for r in calls}
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.status == "low coverage"
    assert a.recent_footprints is None and a.flag_survives_clustering is None
    assert duplication_summary([a]) == ""  # "could not be checked", never "still holds"


def test_an_intermediate_schema_with_scores_but_no_mismatch_columns_is_unknown(tmp_path):
    """Some older screens have fwd_penalty but not the mismatch or ambiguous
    columns. After concatenation those cells are blank beside a populated penalty,
    so checking the penalty alone would still have invented a footprint."""
    from assaywatch.collect import concatenate_screens
    from assaywatch.report import read_calls

    mid = tmp_path / "mid.tsv"
    mid.write_text(
        "assay_id\trecord_id\tcall\tfwd_penalty\trev_penalty\nA\tR1\tdetect\t0\t0\nA\tR2\tfail\t5\t0\n"
    )
    new = write_tsv(
        tmp_path / "new.tsv", [real_row("detect", rid="NEW1", forward=scored(0.0), reverse=scored(0.0))]
    )
    merged = tmp_path / "calls.tsv.gz"
    concatenate_screens([mid, new], merged)
    got = {r["record_id"]: r for r in read_calls(merged)}
    assert "footprint" not in got["R1"] and "footprint" not in got["R2"]
    assert "footprint" in got["NEW1"]


# --------------------------------------------------------------------------
# The signature
# --------------------------------------------------------------------------


def test_the_signature_keeps_each_columns_position():
    assert footprint_signature(["1", "", "", "", "", ""]) != footprint_signature(["", "1", "", "", "", ""])
    assert footprint_signature(["", "", "", "", "", ""]) == "|||||"


def test_equal_signatures_are_one_object():
    """Interned, so two million exact matches are one string, not two million."""
    a = footprint_signature(["1,2", "", "", "0", "0", ""])
    b = footprint_signature(["1,2", "", "", "0", "0", ""])
    assert a is b


# --------------------------------------------------------------------------
# The report
# --------------------------------------------------------------------------


def test_the_report_states_how_many_flags_survive():
    from assaywatch.report import duplication_summary

    dup = assess(*rows(DUPLICATED), CFG, today=TODAY)["A"]
    distinct = assess(*rows(DISTINCT), CFG, today=TODAY)["A"]
    text = duplication_summary([dup, distinct])
    assert text.startswith("1 of 2 flagged assays still hold"), text
    assert duplication_summary([]) == ""


def test_an_unchecked_flag_is_not_counted_as_a_surviving_one():
    from assaywatch.report import duplication_summary

    unchecked = assess(*rows(DUPLICATED, with_footprint=False), CFG, today=TODAY)["A"]
    assert unchecked.status == "low coverage" and duplication_summary([unchecked]) == ""
    checked = assess(*rows(DISTINCT), CFG, today=TODAY)["A"]
    text = duplication_summary([checked, unchecked])
    assert "1 of 1 flagged assays still hold" in text and "1 could not be checked" in text, text


def test_a_clean_sweep_does_not_mention_a_remainder():
    from assaywatch.report import duplication_summary

    distinct = assess(*rows(DISTINCT), CFG, today=TODAY)["A"]
    text = duplication_summary([distinct])
    assert text.startswith("1 of 1 flagged assays still hold") and "remainder" not in text, text
    dup = assess(*rows(DUPLICATED), CFG, today=TODAY)["A"]
    assert "remainder rest on a few footprints" in duplication_summary([dup])


def test_the_duplication_check_reaches_the_rendered_report():
    from assaywatch.report import render_html, render_markdown

    drifts = assess(*rows(DUPLICATED), CFG, today=TODAY)
    md = render_markdown(drifts, {}, [], "2026-10-05", CFG)
    assert "Duplication check" in md and "0 of 1 flagged assays" in md, md
    assert "20.0 per footprint" in md
    assert "Duplication check" in render_html(drifts, {}, [], "2026-10-05", CFG)
