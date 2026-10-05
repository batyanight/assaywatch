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
