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


def test_a_case_for_an_assay_with_no_calls_reads_as_no_data(tmp_path, capsys):
    """An assay absent from the table must not raise now that rows are grouped."""
    calls, retrieved = build_dataset(tmp_path)
    cfg_path = tmp_path / "config.yaml"
    cfg_path.write_text(yaml.safe_dump(CFG))
    cases = tmp_path / "cases.tsv"
    cases.write_text("assay_id\tas_of\texpect\tsource\nGHOST\t2020-01-01\tworks\tdoi:x\n")
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
    assert rc == 0
    assert "no data" in capsys.readouterr().out


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
    agree, contradict, half-agree, and with an assay that has no calls at all.
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
        "GHOST\t2020-01-01\tworks\tdoi:7\n"
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
        ("GHOST", "2020-01-01", "works", "no data", "undecided"),
    ]
    assert (
        "summary: fails/DISAGREES: 1, fails/agrees: 1, partial/weaker: 1, "
        "works/DISAGREES: 1, works/agrees: 2, works/undecided: 1"
    ) in out
    assert "1 case(s) the tool declined to judge" in out


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
