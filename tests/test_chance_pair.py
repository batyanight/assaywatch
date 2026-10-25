"""The chance-pair test (calls.apply_chance_pair_test), 2026-10-25.

`apply_anchor_fdr` guards the record where ONE primer anchored by chance. When BOTH
do and face each other in range, the record gets an amplicon, joins the EVALUABLE
set, and fails for want of a probe site in a locus that is not there - so that test
never sees it (docs/2026-10-25-chance-pairs-invent-denominators.md).

These pin the shape of the correction rather than its arithmetic, because it has no
arithmetic: off is a no-op; the two headline cases move; and above all the two rows
it must NOT touch stay put - the West African mpox failures (probe-less but with
perfectly matching primers, so real amplification) and anything in a conventional
assay, which has no probe and therefore no locus-presence test at all.
"""

from __future__ import annotations

from assaywatch.calls import CHANCE_PAIR, apply_chance_pair_test

ON = {"drift": {"chance_pair_test": True}, "scoring": {"oligo_weak_max": 3.0}}
OFF = {"drift": {}, "scoring": {"oligo_weak_max": 3.0}}


def _row(aid, rid, *, call="fail", probe="", fwd=6.5, rev=6.5):
    """A row in the shape `read_calls` produces it.

    `probeless_penalties` is present only on a `fail` row whose probe site was
    absent - that is where read_calls does the probe half of the test - so a row
    with a probe, or any non-fail row, simply has no key.
    """
    r = {"assay_id": aid, "record_id": rid, "call": call, "exclusion": ""}
    if call == "fail" and probe in ("", "-"):
        r["probeless_penalties"] = (fwd, rev)
    return r


#: Each probe-bearing assay with its own `oligo_weak_max`, as `report.build`
#: resolves them. A bare set used to be passed here and the bar read from
#: `cfg["scoring"]`, which ignored `scoring.by_chemistry`.
PROBE_BARS = {"targetD": 3.0, "Orf": 3.0, "WestAfrican": 3.0, "TB": 3.0}


def test_off_by_default_changes_nothing_and_reports_nothing():
    rows = [_row("targetD", f"scaffold{i}") for i in range(111)]
    before = [dict(r) for r in rows]
    assert apply_chance_pair_test(rows, OFF, PROBE_BARS) == {}
    assert apply_chance_pair_test(rows, {"scoring": {"oligo_weak_max": 3.0}}, PROBE_BARS) == {}
    assert rows == before


def test_the_targetd_shaped_chance_pairs_move_and_the_detects_do_not():
    """81 detect + 111 probe-less pairs at penalties well past the bar: the measured case,
    where the published 42.2% should be 100%."""
    rows = [_row("targetD", f"det{i}", call="detect", probe="100-120+", fwd=0.0, rev=0.0) for i in range(81)]
    rows += [_row("targetD", f"scaffold{i}", fwd=6.5, rev=9.0) for i in range(111)]
    assert apply_chance_pair_test(rows, ON, PROBE_BARS) == {"targetD": 111}
    moved = [r for r in rows if r["record_id"].startswith("scaffold")]
    assert all(r["call"] == "no_amplicon" and r["exclusion"] == CHANCE_PAIR for r in moved)
    kept = [r for r in rows if r["record_id"].startswith("det")]
    assert all(r["call"] == "detect" and r["exclusion"] == "" for r in kept)


def test_the_west_african_mpox_failures_are_untouched():
    """THE guard. Probe-less, but fwd/rev penalty 0: conserved primers that genuinely
    amplify clade I against a clade-II probe that genuinely does not bind it. Real
    amplification, real failure. Relabelling these would delete the finding."""
    rows = [_row("WestAfrican", f"cladeI{i}", fwd=0.0, rev=0.0) for i in range(2688)]
    assert apply_chance_pair_test(rows, ON, PROBE_BARS) == {}
    assert all(r["call"] == "fail" and r["exclusion"] == "" for r in rows)


def test_one_good_primer_is_not_enough_to_move_a_row():
    """Conjunctive on BOTH primers: one real placement means the locus may well be there."""
    rows = [_row("Orf", "half", fwd=0.5, rev=6.5), _row("Orf", "other", fwd=6.5, rev=0.5)]
    assert apply_chance_pair_test(rows, ON, PROBE_BARS) == {}
    assert all(r["call"] == "fail" for r in rows)


def test_exactly_at_the_bar_does_not_move():
    """`oligo_weak_max` is the last penalty that is still `weak` rather than `blocked`,
    so the test is strictly above it."""
    rows = [_row("Orf", "atbar", fwd=3.0, rev=3.0)]
    assert apply_chance_pair_test(rows, ON, PROBE_BARS) == {}
    assert rows[0]["call"] == "fail"


def test_a_by_chemistry_override_of_the_bar_is_honoured():
    """The bar is per assay because `scoring.by_chemistry` can move it.

    The screener resolves `oligo_weak_max` per chemistry (`score.config_for`).
    This test read `cfg["scoring"]` directly until 2026-10-26, so an `mgb` or
    `hydrolysis_probe` override would have meant one thing in the screen and
    another here - a live, shipped test silently disagreeing with the screener
    about what "blocked" means. The table ships empty, so this pins the contract
    before ROADMAP Phase 2 fills it in.
    """
    # Penalties 4.0 are above the shipped 3.0 but below an mgb override of 5.0.
    rows = [_row("mgbAssay", f"r{i}", fwd=4.0, rev=4.0) for i in range(3)]
    at_shipped = [dict(r) for r in rows]
    assert apply_chance_pair_test(at_shipped, ON, {"mgbAssay": 3.0}) == {"mgbAssay": 3}
    relaxed = [dict(r) for r in rows]
    assert apply_chance_pair_test(relaxed, ON, {"mgbAssay": 5.0}) == {}
    assert all(r["call"] == "fail" for r in relaxed)


def test_an_assay_absent_from_the_bars_is_never_touched():
    """Membership and bar arrive together: no entry means not probe-bearing."""
    rows = [_row("unknown", "r", fwd=9.0, rev=9.0)]
    assert apply_chance_pair_test(rows, ON, {}) == {}
    assert rows[0]["call"] == "fail"


def test_a_conventional_assay_is_never_touched_however_bad_its_primers():
    """No probe means no locus-presence test. Applied to these, the penalty half alone
    marks real coverage failures - ~4,900 rows in the two LYSSAVIRUS entries."""
    rows = [_row("Lyssa", f"divergent{i}", fwd=6.5, rev=6.5) for i in range(100)]
    assert apply_chance_pair_test(rows, ON, PROBE_BARS) == {}
    assert all(r["call"] == "fail" for r in rows)


def test_a_probe_bearing_row_that_found_its_probe_is_not_touched():
    rows = [_row("Orf", "real", probe="50-70-", fwd=6.5, rev=6.5)]
    assert apply_chance_pair_test(rows, ON, PROBE_BARS) == {}
    assert rows[0]["call"] == "fail"


def test_a_dash_counts_as_no_probe_site():
    """The TSV writes `-` for an absent site; an empty string arrives from a dict row."""
    rows = [_row("Orf", "dash", probe="-"), _row("Orf", "empty", probe="")]
    assert apply_chance_pair_test(rows, ON, PROBE_BARS) == {"Orf": 2}


def test_only_fail_rows_can_move():
    """A reduced or detect row has its probe by definition; no_amplicon is already out."""
    for call in ("detect", "reduced", "no_amplicon", "indeterminate"):
        rows = [_row("Orf", "r", call=call)]
        assert apply_chance_pair_test(rows, ON, PROBE_BARS) == {}
        assert rows[0]["call"] == call


def test_an_older_screen_without_penalty_columns_is_left_alone():
    """Unknown is not the same as chance - the rule `apply_anchor_fdr` already follows.

    Such a row reaches here with no `probeless_penalties` key, because `read_calls`
    only sets it when both penalty cells are populated.
    """
    rows = [{"assay_id": "Orf", "record_id": "old", "call": "fail", "exclusion": ""}]
    assert apply_chance_pair_test(rows, ON, PROBE_BARS) == {}
    assert rows[0]["call"] == "fail"


def test_read_calls_carries_the_penalties_on_exactly_the_rows_that_can_move(tmp_path):
    """The half of the test that lives in `read_calls`. This is what the first
    implementation got wrong: read_calls keeps only the columns drift needs, so a
    function reading `probe_site` off these rows silently did nothing at all."""
    import gzip

    from assaywatch.calls import read_calls

    header = "assay_id\trecord_id\tcall\texclusion\tprobe_site\tfwd_penalty\trev_penalty\n"
    body = (
        "A\tchance\tfail\t\t-\t6.5\t9\n"  # probe-less fail: carried
        "A\treal\tfail\t\t50-70+\t6.5\t9\n"  # has its probe: not carried
        "A\thit\tdetect\t\t50-70+\t0\t0\n"  # not a fail: not carried
        "A\tnopen\tfail\t\t-\t\t\n"  # older screen, blank cells: not carried
    )
    p = tmp_path / "calls.tsv.gz"
    with gzip.open(p, "wt") as fh:
        fh.write(header + body)
    rows = {r["record_id"]: r for r in read_calls(p)}
    assert rows["chance"]["probeless_penalties"] == (6.5, 9.0)
    assert "probeless_penalties" not in rows["real"]
    assert "probeless_penalties" not in rows["hit"]
    assert "probeless_penalties" not in rows["nopen"]
    # And end to end: only the first row moves.
    assert apply_chance_pair_test(list(rows.values()), ON, {"A": 3.0}) == {"A": 1}
    assert rows["chance"]["call"] == "no_amplicon"
    assert rows["chance"]["exclusion"] == CHANCE_PAIR
