"""Retrospective validation: same verdicts as before, loaded once instead of per case.

`--cases` used to reload and re-deduplicate the whole calls table and every
metadata file for each of the 46 validation cases. The fix restructures where
that happens, which is exactly the kind of change that can quietly alter an
answer, so the first job here is to pin that it does not.
"""

from __future__ import annotations

import csv
import gzip
import importlib.util
import sys
from datetime import date
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("retro", ROOT / "scripts" / "retrospective.py")
retro = importlib.util.module_from_spec(_spec)
sys.modules["retro"] = retro
_spec.loader.exec_module(retro)

CFG = {
    "drift": {
        "detect_fraction_threshold": 0.90,
        "recent_window_months": 24,
        "min_records_for_drift": 5,
        "min_records_for_coverage": 3,
    }
}


def reference_status_as_of(calls_path, retrieved, cfg, as_of, assays=None):
    """The implementation this replaced, verbatim, kept here as the oracle."""
    dates = retro.read_dates(retrieved)
    cutoff = as_of.isoformat()
    rows = [
        r
        for r in retro.key_calls_by_accession(retro.read_calls(calls_path))
        if (assays is None or r["assay_id"] in assays) and (dates.get(r["record_id"], "9999") < cutoff)
    ]
    return retro.assess(rows, dates, cfg, today=as_of), len(rows)


def build_dataset(tmp_path: Path):
    """Two assays over several years, with a re-versioned accession in the mix."""
    retrieved = tmp_path / "retrieved" / "562" / "all"
    retrieved.mkdir(parents=True)
    meta_rows, calls_rows = [], []
    i = 0
    # Assay A: solid until 2018, then increasingly failing. Assay B: always fine.
    for year, a_fail in ((2012, 0), (2014, 0), (2016, 0), (2018, 8), (2020, 12), (2022, 14)):
        for k in range(15):
            acc = f"AB{i:06d}"
            i += 1
            meta_rows.append(
                {"accession": f"{acc}.1", "created": f"{year}-03-01", "updated": f"{year}-03-01"}
            )
            fails = k < a_fail
            calls_rows.append(
                {
                    "assay_id": "A",
                    "record_id": f"{acc}.1",
                    "call": "fail" if fails else "detect",
                    "exclusion": "",
                }
            )
            calls_rows.append({"assay_id": "B", "record_id": f"{acc}.1", "call": "detect", "exclusion": ""})
    # One accession revised: version 2 supersedes version 1 and must win.
    meta_rows.append({"accession": "REV001.2", "created": "2019-05-01", "updated": "2020-01-01"})
    calls_rows.append({"assay_id": "A", "record_id": "REV001.1", "call": "detect", "exclusion": ""})
    calls_rows.append({"assay_id": "A", "record_id": "REV001.2", "call": "fail", "exclusion": ""})

    with gzip.open(retrieved / "2026-10-04.meta.tsv.gz", "wt", newline="") as fh:
        w = csv.DictWriter(fh, ["accession", "created", "updated"], delimiter="\t")
        w.writeheader()
        w.writerows(meta_rows)
    calls = tmp_path / "calls.tsv.gz"
    with gzip.open(calls, "wt", newline="") as fh:
        w = csv.DictWriter(fh, ["assay_id", "record_id", "call", "exclusion"], delimiter="\t")
        w.writeheader()
        w.writerows(calls_rows)
    return calls, tmp_path / "retrieved"


def summarise(drifts):
    return {
        aid: (a.status, a.recent_detected, a.recent_evaluable, a.baseline_detected, a.baseline_evaluable)
        for aid, a in drifts.items()
    }


def test_the_restructured_path_gives_the_same_verdicts_as_the_old_one(tmp_path):
    """Every (date, assay-filter) combination, old implementation against new."""
    calls, retrieved = build_dataset(tmp_path)
    ev = retro.load_evidence(calls, retrieved)
    checked = 0
    for as_of in (date(2014, 1, 1), date(2017, 6, 1), date(2019, 1, 1), date(2021, 1, 1), date(2023, 1, 1)):
        for assays in (None, {"A"}, {"B"}, {"A", "B"}, {"NOT_THERE"}):
            want, n_want = reference_status_as_of(calls, retrieved, CFG, as_of, assays)
            got, n_got = retro.status_from_evidence(ev, CFG, as_of, assays)
            assert n_got == n_want, (as_of, assays)
            assert summarise(got) == summarise(want), (as_of, assays)
            checked += 1
    assert checked == 25


def test_the_public_wrapper_still_answers_one_question(tmp_path):
    calls, retrieved = build_dataset(tmp_path)
    want, n_want = reference_status_as_of(calls, retrieved, CFG, date(2021, 1, 1), {"A"})
    got, n_got = retro.status_as_of(calls, retrieved, CFG, date(2021, 1, 1), {"A"})
    assert n_got == n_want and summarise(got) == summarise(want)


def test_the_dataset_actually_exercises_the_verdicts_it_compares(tmp_path):
    """An equivalence test over data where every answer is the same proves
    nothing, so check the cases differ and the revised accession matters."""
    calls, retrieved = build_dataset(tmp_path)
    ev = retro.load_evidence(calls, retrieved)
    early, _ = retro.status_from_evidence(ev, CFG, date(2017, 6, 1), {"A"})
    late, _ = retro.status_from_evidence(ev, CFG, date(2023, 1, 1), {"A"})
    assert early["A"].status != late["A"].status, (early["A"].status, late["A"].status)
    # REV001 appears twice in the calls and must count once, as its newest version.
    assert len(ev.by_assay["A"]) == len({r["record_id"] for r in ev.by_assay["A"]})
    rev = [r for r in ev.by_assay["A"] if r["record_id"] == "REV001"]
    assert len(rev) == 1 and rev[0]["call"] == "fail"


def test_cases_load_the_evidence_once_not_once_per_case(tmp_path, monkeypatch, capsys):
    """The point of the change. Counted at the two expensive reads."""
    calls, retrieved = build_dataset(tmp_path)
    cfg_path = tmp_path / "config.yaml"
    cfg_path.write_text(yaml.safe_dump(CFG))
    cases = tmp_path / "cases.tsv"
    cases.write_text(
        "assay_id\tas_of\texpect\tsource\n"
        "A\t2017-06-01\tworks\tdoi:x\n"
        "A\t2023-01-01\tfails\tdoi:y\n"
        "B\t2019-01-01\tworks\tdoi:z\n"
        "B\t2023-01-01\tworks\tdoi:w\n"
        "A\t2014-01-01\tworks\tdoi:v\n"
    )
    loads = {"calls": 0, "dates": 0}
    real_calls, real_dates = retro.read_calls, retro.read_dates

    def counting_calls(*a, **k):
        loads["calls"] += 1
        return real_calls(*a, **k)

    def counting_dates(*a, **k):
        loads["dates"] += 1
        return real_dates(*a, **k)

    monkeypatch.setattr(retro, "read_calls", counting_calls)
    monkeypatch.setattr(retro, "read_dates", counting_dates)
    rc = retro.main(
        [
            "--calls",
            str(calls),
            "--retrieved",
            str(retrieved),
            "--config",
            str(cfg_path),
            "--cases",
            str(cases),
        ]
    )
    out = capsys.readouterr().out
    assert rc == 0
    assert loads == {"calls": 1, "dates": 1}, loads  # five cases, one load each
    assert "summary:" in out and out.count("\n") >= 7


def _cases_argv(calls, retrieved, cfg_path, cases, renames):
    return [
        "--calls",
        str(calls),
        "--retrieved",
        str(retrieved),
        "--config",
        str(cfg_path),
        "--cases",
        str(cases),
        "--renames",
        str(renames),
    ]


def test_a_case_naming_an_assay_the_table_does_not_hold_is_an_error(tmp_path):
    """It used to read `no data` and land in the undecided count, which is where 13
    of the 49 real cases hid on the 2026-10-17 calls after the assay-ID renames -
    4 of them `fails` cases, so every tier-2 figure taken off that table was wrong.
    An id that matches nothing is a bookkeeping fault, not evidence, so it stops
    the run and names itself instead of being averaged into a confusion matrix."""
    calls, retrieved = build_dataset(tmp_path)
    cfg_path = tmp_path / "config.yaml"
    cfg_path.write_text(yaml.safe_dump(CFG))
    cases = tmp_path / "cases.tsv"
    cases.write_text("assay_id\tas_of\texpect\tsource\nGHOST\t2020-01-01\tworks\tdoi:x\n")
    renames = tmp_path / "renames.tsv"
    renames.write_text("old_id\taction\tnew_id\treason\n")

    with pytest.raises(SystemExit) as e:
        retro.main(_cases_argv(calls, retrieved, cfg_path, cases, renames))
    assert "GHOST" in str(e.value)


def test_a_renamed_case_still_matches_a_calls_table_from_before_the_rename(tmp_path, capsys):
    """The table holds `A`; the case names the id `A` was renamed to. It must be
    scored, not declined."""
    calls, retrieved = build_dataset(tmp_path)
    cfg_path = tmp_path / "config.yaml"
    cfg_path.write_text(yaml.safe_dump(CFG))
    cases = tmp_path / "cases.tsv"
    cases.write_text("assay_id\tas_of\texpect\tsource\nA_renamed\t2023-01-01\tworks\tdoi:x\n")
    renames = tmp_path / "renames.tsv"
    renames.write_text("old_id\taction\tnew_id\treason\nA\tRENAME\tA_renamed\ttidier\n")

    assert retro.main(_cases_argv(calls, retrieved, cfg_path, cases, renames)) == 0
    cap = capsys.readouterr()
    assert "undecided" not in cap.out
    assert "A_renamed -> A" in cap.err  # says plainly that the table predates the rename


def test_the_bridge_works_in_the_other_direction_too(tmp_path, capsys):
    """A case naming the OLD id against a table that holds the NEW one."""
    calls, retrieved = build_dataset(tmp_path)
    cfg_path = tmp_path / "config.yaml"
    cfg_path.write_text(yaml.safe_dump(CFG))
    cases = tmp_path / "cases.tsv"
    cases.write_text("assay_id\tas_of\texpect\tsource\nA_old\t2023-01-01\tworks\tdoi:x\n")
    renames = tmp_path / "renames.tsv"
    renames.write_text("old_id\taction\tnew_id\treason\nA_old\tRENAME\tA\ttidier\n")

    assert retro.main(_cases_argv(calls, retrieved, cfg_path, cases, renames)) == 0
    assert "A_old -> A" in capsys.readouterr().err


def test_a_case_for_a_removed_assay_is_reported_as_removed_not_undecided(tmp_path, capsys):
    """A removed entry cannot be judged, but it is not the tool declining to judge
    either, so it gets its own verdict rather than inflating the undecided count."""
    calls, retrieved = build_dataset(tmp_path)
    cfg_path = tmp_path / "config.yaml"
    cfg_path.write_text(yaml.safe_dump(CFG))
    cases = tmp_path / "cases.tsv"
    cases.write_text("assay_id\tas_of\texpect\tsource\nGONE\t2020-01-01\tworks\tdoi:x\n")
    renames = tmp_path / "renames.tsv"
    renames.write_text("old_id\taction\tnew_id\treason\nGONE\tREMOVE\t\tno provenance\n")

    assert retro.main(_cases_argv(calls, retrieved, cfg_path, cases, renames)) == 0
    out = capsys.readouterr().out
    assert "removed" in out and "undecided" not in out


def test_resolve_assay_id_prefers_an_exact_hit_over_an_alias():
    """Both ids in the table: the case's own id wins, so a rename that has already
    been applied to the archive does not silently redirect to the stale rows."""
    aliases = retro.id_aliases({"old": "new"})
    assert retro.resolve_assay_id("new", {"old", "new"}, aliases, set()) == ("new", None)
    rid, why = retro.resolve_assay_id("new", {"old"}, aliases, set())
    assert rid == "old" and "renamed" in why


def write_dataset(tmp_path: Path, deposited: dict[str, str | None]):
    """{accession: created date, or None for no usable date} -> (calls path, retrieved dir).

    One assay, one `detect` call per accession. An accession given `None` has a
    metadata row with an empty date; one missing from `deposited` altogether would
    have no row at all, and both must read as undated.
    """
    retrieved = tmp_path / "retrieved" / "562" / "all"
    retrieved.mkdir(parents=True)
    with gzip.open(retrieved / "2026-10-04.meta.tsv.gz", "wt", newline="") as fh:
        w = csv.DictWriter(fh, ["accession", "created", "updated"], delimiter="\t")
        w.writeheader()
        for acc, created in deposited.items():
            w.writerow({"accession": f"{acc}.1", "created": created or "", "updated": created or ""})
    calls = tmp_path / "calls.tsv.gz"
    with gzip.open(calls, "wt", newline="") as fh:
        w = csv.DictWriter(fh, ["assay_id", "record_id", "call", "exclusion"], delimiter="\t")
        w.writeheader()
        for acc in [*deposited, "NOMETA"]:  # NOMETA has calls and no metadata row at all
            w.writerow({"assay_id": "A", "record_id": f"{acc}.1", "call": "detect", "exclusion": ""})
    return calls, tmp_path / "retrieved"


def test_the_cutoff_keeps_records_deposited_strictly_before_it_and_drops_the_undated(tmp_path):
    """The cutoff comparison is the line the restructuring rewrote, and the
    old-against-new test above cannot guard it: its oracle reads the same
    comparison, and its dataset has no record on the cutoff day and none undated.
    So the rule is pinned here against a hand-built answer instead.

    A record deposited ON the cutoff was not known the day before, so it is
    excluded; the day after it is in. A record with no usable deposit date cannot
    be shown to predate any cutoff, so it is never in, however late the cutoff.
    """
    calls, retrieved = write_dataset(
        tmp_path,
        {"P": "2020-05-31", "Q": "2020-06-01", "R": "2020-06-02", "BLANK": None},
    )
    ev = retro.load_evidence(calls, retrieved)
    counts = {
        as_of: retro.status_from_evidence(ev, CFG, as_of, {"A"})[1]
        for as_of in (
            date(2020, 5, 31),
            date(2020, 6, 1),
            date(2020, 6, 2),
            date(2020, 6, 3),
            date(2035, 1, 1),
        )
    }
    assert counts == {
        date(2020, 5, 31): 0,  # P itself is on the cutoff
        date(2020, 6, 1): 1,  # P; Q is on the cutoff
        date(2020, 6, 2): 2,  # P, Q
        date(2020, 6, 3): 3,  # P, Q, R
        date(2035, 1, 1): 3,  # still not BLANK, and not NOMETA
    }


def test_cases_print_the_verdict_each_status_implies(tmp_path, capsys):
    """Every verdict the loop can reach, asserted per case.

    The statuses follow from how `build_dataset` is built: assay A is solid
    until 2018 and then failing, so it is `stable` in 2017 and `declining` in
    2023; assay B always detects. The cases pair those with expectations that
    agree, contradict and half-agree, and the last asks about A before any of
    its records existed, which is the honest way to reach `undecided` - an id
    the table does not hold at all is an error now, not a verdict.
    """
    calls, retrieved = build_dataset(tmp_path)
    cfg_path = tmp_path / "config.yaml"
    cfg_path.write_text(yaml.safe_dump(CFG))
    cases = tmp_path / "cases.tsv"
    cases.write_text(
        "# provenance comments are stripped before the header is read\n"
        "assay_id\tas_of\texpect\tsource\n"
        "A\t2017-06-01\tworks\tdoi:1\n"
        "A\t2023-01-01\tfails\tdoi:2\n"
        "A\t2023-01-01\tworks\tdoi:3\n"
        "B\t2019-01-01\tworks\tdoi:4\n"
        "B\t2023-01-01\tfails\tdoi:5\n"
        "B\t2023-01-01\tpartial\tdoi:6\n"
        "A\t2011-01-01\tworks\tdoi:7\n"
    )
    rc = retro.main(
        [
            "--calls",
            str(calls),
            "--retrieved",
            str(retrieved),
            "--config",
            str(cfg_path),
            "--cases",
            str(cases),
        ]
    )
    out = capsys.readouterr().out
    assert rc == 0

    # A row is `assay as_of expect status... verdict`, space-padded; status is the
    # middle, which can be two words ("no data").
    rows = []
    for line in out.splitlines():
        parts = line.split()
        if len(parts) >= 5 and parts[1][:2] == "20":
            rows.append((parts[0], parts[1], parts[2], " ".join(parts[3:-1]), parts[-1]))
    assert rows == [
        ("A", "2017-06-01", "works", "stable", "agrees"),
        ("A", "2023-01-01", "fails", "declining", "agrees"),
        ("A", "2023-01-01", "works", "declining", "DISAGREES"),
        ("B", "2019-01-01", "works", "stable", "agrees"),
        ("B", "2023-01-01", "fails", "stable", "DISAGREES"),
        ("B", "2023-01-01", "partial", "stable", "weaker"),
        ("A", "2011-01-01", "works", "no data", "undecided"),
    ]
    assert (
        "summary: fails/DISAGREES: 1, fails/agrees: 1, partial/weaker: 1, "
        "works/DISAGREES: 1, works/agrees: 2, works/undecided: 1"
    ) in out
    assert "1 case(s) the tool declined to judge" in out
    # `partial` rows are scored on their own line and NEVER join the `fails` numerator
    # (decided 2026-10-27). The one partial row here reads `stable`, i.e. weaker, so
    # the named-gap count is 0 of 1 and the fails line is untouched at 1/2.
    assert "documented failures caught: 1/2" in out
    assert "partial gaps named (scored separately, never pooled with fails): 0/1" in out
    assert "read as working (weaker, not a contradiction): 1 of 1" in out


# --------------------------------------------------------------------------
# The whole status -> verdict table, not just the two statuses the fixture reaches.
# --------------------------------------------------------------------------

# What each drift status means to the calibration, from the module's own documentation:
# stable and watch say the assay works, declining says it fails, low coverage says it never
# covered all the diversity (partial), and the three "cannot judge" statuses are undecided.
STATUS_TO_GOT = {
    "stable": "works",
    "watch": "works",
    "declining": "fails",
    "low coverage": "partial",
    "insufficient data": "undecided",
    "no recent data": "undecided",
    "no data": "undecided",
}


def test_every_status_maps_to_the_outcome_the_documentation_gives_it():
    for status, want in STATUS_TO_GOT.items():
        assert retro.classify(status, "works")[0] == want, status


def test_every_status_against_every_expectation():
    """21 combinations, written out from the rules rather than derived from the code."""
    for status, got in STATUS_TO_GOT.items():
        for expect in ("works", "fails", "partial"):
            if got == "undecided":
                verdict = "undecided"  # the tool declined to judge: neither agreement nor error
            elif got == expect:
                verdict = "agrees"
            elif {got, expect} == {"works", "partial"}:
                verdict = "weaker"  # incomplete coverage, in either direction
            else:
                verdict = "DISAGREES"
            assert retro.classify(status, expect) == (got, verdict), (status, expect)


def test_low_coverage_is_never_scored_as_a_failure():
    """The bug the module comment records: scoring it as `fails` turned four honest `works`
    cases into disagreements. A low-coverage assay against a `works` paper is `weaker`."""
    assert retro.classify("low coverage", "works") == ("partial", "weaker")
    assert retro.classify("low coverage", "fails") == ("partial", "DISAGREES")


def test_a_status_nobody_has_classified_is_undecided_not_silently_scored():
    assert retro.classify("some new status", "works") == ("undecided", "undecided")
    assert retro.classify("some new status", "fails") == ("undecided", "undecided")


def test_the_cases_loop_prints_what_classify_says(tmp_path, capsys, monkeypatch):
    """The loop and the table must agree: a `low coverage` status against a `partial`
    expectation, printed through main(), reads `agrees` and tallies as partial/agrees."""
    calls, retrieved = build_dataset(tmp_path)
    cfg_path = tmp_path / "config.yaml"
    cfg_path.write_text(yaml.safe_dump(CFG))
    cases = tmp_path / "cases.tsv"
    cases.write_text("assay_id\tas_of\texpect\tsource\nA\t2023-01-01\tpartial\tdoi:1\n")
    real = retro.status_from_evidence

    def forced(evidence, cfg, as_of, assays=None, **kwargs):
        drifts, n = real(evidence, cfg, as_of, assays, **kwargs)
        drifts["A"].status = "low coverage"
        return drifts, n

    monkeypatch.setattr(retro, "status_from_evidence", forced)
    argv = [
        "--calls",
        str(calls),
        "--retrieved",
        str(retrieved),
        "--config",
        str(cfg_path),
        "--cases",
        str(cases),
    ]
    retro.main(argv)
    out = capsys.readouterr().out
    assert "low coverage" in out and "agrees" in out and "partial/agrees: 1" in out, out


def test_a_coverage_failure_agrees_with_low_coverage_and_a_drift_failure_does_not():
    """`mechanism` is the source's account of the failure. A coverage gap is what
    `low coverage` reports; drift (adapted to current variants) needs `declining`."""
    assert retro.classify("low coverage", "fails", "coverage") == ("partial", "agrees")
    assert retro.classify("declining", "fails", "coverage") == ("fails", "agrees")
    assert retro.classify("low coverage", "fails", "drift") == ("partial", "DISAGREES")
    assert retro.classify("declining", "fails", "drift") == ("fails", "agrees")
    assert retro.classify("stable", "fails", "coverage") == ("works", "DISAGREES")
    # The mechanism only qualifies a `fails`: it changes nothing for the other expectations.
    for status in STATUS_TO_GOT:
        for expect in ("works", "partial"):
            assert retro.classify(status, expect, "coverage") == retro.classify(status, expect)


def test_the_shipped_cases_give_every_fails_row_a_mechanism_and_no_other_row_one():
    body = [
        ln
        for ln in (ROOT / "docs" / "validation-cases.tsv").read_text().splitlines()
        if ln and not ln.startswith("#")
    ]
    rows = list(csv.DictReader(body, delimiter="\t"))
    assert rows and "mechanism" in rows[0]
    for r in rows:
        if r["expect"] == "fails":
            assert r["mechanism"] in ("drift", "coverage"), r["assay_id"]
        else:
            assert r["mechanism"] == "", r["assay_id"]


def test_precision_is_reported_beside_sensitivity():
    """Every statement of performance until 2026-10-23 was sensitivity. This is
    the frozen baseline's own matrix, reduced to the rows that matter, and the
    numbers in docs/journal/2026-10-23-baseline.md must come out of it."""
    rows = (
        # the two declining calls that were real failures
        [("fails", "coverage", "declining", "agrees"), ("fails", "drift", "declining", "agrees")]
        # three catches credited to low coverage
        + [("fails", "coverage", "low coverage", "agrees")] * 3
        # three misses and three undecided
        + [("fails", "coverage", "stable", "DISAGREES")] * 3
        + [("fails", "coverage", "insufficient data", "undecided")] * 3
        # seven false alarms: five working assays and two partial ones called declining
        + [("works", "", "declining", "DISAGREES")] * 5
        + [("partial", "", "declining", "DISAGREES")] * 2
        + [("works", "", "stable", "agrees")] * 27
    )
    out = "\n".join(retro.precision_lines(rows))
    assert "(PPV): 2/9 = 22%" in out
    assert "documented failures caught: 5/11 = 45%" in out
    assert "credited to: low coverage 3, declining 2" in out
    assert "caught by the drift flag itself (declining): 2/11 = 18%" in out
    assert "failure cases by mechanism: coverage 10, drift 1" in out
    assert "working assays called declining (false alarms): 5/32 = 16%" in out
    assert "95% CrI" in out, "a proportion on ~7 independent events must carry its interval"
    # The estimator is named, and CI vs CrI distinguishes them. The shipped
    # 2026-10-22 report said "Intervals are Wilson 95%" over numbers half of which
    # were Wald, which is how a zero-width interval reached a verdict.
    assert "intervals: jeffreys" in out
    wilson = "\n".join(retro.precision_lines(rows, "wilson"))
    assert "intervals: wilson" in wilson and "95% CI " in wilson
    assert "CrI" not in wilson
    # `undecided` is missing data, not a miss: both denominators are printed.
    assert "among the cases it judged at all: 5/8" in out
    assert "declined to judge: 3 of 11" in out


def test_nothing_reads_the_holdout_file_by_default():
    """A held-out set is spent the first time a threshold decision reads it, so
    the rule has to be written where the file is, not only in a doc.

    This replaced an assertion that the file was EMPTY, which was the right
    tripwire only while it was empty: the 2026-10-24 sweep populated it
    (docs/journal/2026-10-24-heldout-candidates.md), which is what wave 4 asked for. What
    has to hold now is not emptiness but that no default code path consults it,
    so the two scripts that score cases are pinned to a non-held-out default.
    """
    p = ROOT / "docs" / "validation-cases-heldout.tsv"
    text = p.read_text()
    assert "no threshold decision may consult this file" in text
    dev = (ROOT / "docs" / "validation-cases.tsv").read_text()
    assert "THIS IS THE DEVELOPMENT SET" in dev, "the development set must say so"

    # retrospective.py scores nothing unless --cases is given; holdout.py defaults
    # to the development set. Neither may name the held-out file as a default.
    for script in ("retrospective.py", "holdout.py"):
        src = (ROOT / "scripts" / script).read_text()
        assert "validation-cases-heldout" not in src, (
            f"{script} names the held-out file; it must be reachable only by an explicit --cases"
        )
    import re

    retro = (ROOT / "scripts" / "retrospective.py").read_text()
    assert re.search(r'"--cases",\s*type=Path,\s*default=None', retro), (
        "retrospective.py --cases must default to None, so a bare run scores no case file"
    )


def test_the_holdout_rows_have_the_development_sets_shape():
    """Rows are only useful if retrospective.py can read them unchanged, and only
    honest if every id is a real assay and every row cites a source."""
    import csv

    def body(path):
        return [ln for ln in path.read_text().splitlines() if ln.strip() and not ln.startswith("#")]

    held = ROOT / "docs" / "validation-cases-heldout.tsv"
    dev = ROOT / "docs" / "validation-cases.tsv"
    hrows = list(csv.DictReader(body(held), delimiter="\t"))
    assert body(held)[0] == body(dev)[0], "held-out and development sets must share one header"
    if not hrows:  # empty is a legitimate state; the rest only applies to rows
        return
    ids = {q.stem for q in (ROOT / "registry").glob("*.yaml")}
    for r in hrows:
        assert r["assay_id"] in ids, f"{r['assay_id']} is not a live registry entry"
        assert r["expect"] in {"works", "fails", "partial"}, r["expect"]
        assert r["mechanism"] in {"", "drift", "coverage"}, r["mechanism"]
        assert "10." in (r["source"] or ""), f"{r['assay_id']} cites no DOI"
    # A held-out case must not rest on a paper the development set already used.
    dev_src = dev.read_text()
    shared = [r["assay_id"] for r in hrows if (r["source"].split()[0]) in dev_src]
    assert not shared, f"held-out rows citing a development-set DOI: {sorted(set(shared))}"


def test_holdout_objective_ignores_weaker_and_undecided():
    """The selection rule counts disagreements only. `weaker` is not a
    disagreement (a pan-family assay detecting most of a genus is consistent
    with a paper that used it on the isolates it had), and counting `undecided`
    would make the rule prefer whatever decides the most cases rather than
    whatever is right."""
    import importlib.util

    spec = importlib.util.spec_from_file_location("holdout", ROOT / "scripts" / "holdout.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert mod.objective(["DISAGREES", "agrees", "weaker", "undecided", "removed"]) == 1
    assert mod.objective(["weaker"] * 9) == 0
    # ties break on the cell, never toward the shipped value
    grid = {(24, 15): ["DISAGREES"], (18, 10): ["DISAGREES"], (60, 30): ["agrees"]}
    assert mod.best_cell(grid) == (60, 30)
    assert mod.best_cell({(24, 15): ["DISAGREES"], (18, 10): ["DISAGREES"]}) == (18, 10)


def test_the_default_run_is_the_newest_by_date_not_by_name(tmp_path):
    """`sorted(...)[-1]` picked the frozen baseline over the newest run.

    `results/baseline-2026-10-22/` sorts after `results/2026-10-25/` because
    `b` > `2`, so a bare `--cases` run scored a table four days stale under
    different scoring rules while printing "the newest run". Every candidate
    priced without an explicit `--calls` would have been measured against it.
    """
    from scripts.retrospective import newest_run

    results = tmp_path / "results"
    for name in ("2026-10-22", "baseline-2026-10-22", "2026-10-25", "2026-10-25-experiment"):
        (results / name).mkdir(parents=True)
        (results / name / "calls.tsv.gz").write_bytes(b"")
    # The exact pair that caused the bug, and the bare date preferred over a suffix.
    assert newest_run(results).parent.name == "2026-10-25"


def test_an_undated_run_directory_never_wins_the_default(tmp_path):
    """It stays reachable with --calls; it just cannot be "the newest"."""
    from scripts.retrospective import newest_run

    results = tmp_path / "results"
    for name in ("scratch", "2026-10-01"):
        (results / name).mkdir(parents=True)
        (results / name / "calls.tsv.gz").write_bytes(b"")
    assert newest_run(results).parent.name == "2026-10-01"


def test_no_runs_at_all_is_a_clear_exit(tmp_path):
    import pytest as _pytest

    from scripts.retrospective import newest_run

    with _pytest.raises(SystemExit, match="no calls.tsv.gz"):
        newest_run(tmp_path / "results")
