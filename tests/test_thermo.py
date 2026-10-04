"""Thermodynamic columns: concrete sequences chosen as documented, Tm shifts in the right direction."""

import csv
import subprocess
import sys

import pytest

from assaywatch.thermo import COLUMNS, duplex_tm, resolve

primer3 = pytest.importorskip("primer3")

from test_score import ASSAYS, CFG, FIX, RECORDS, ROOT  # noqa: E402

from assaywatch.score import screen_record  # noqa: E402
from assaywatch.thermo import annotate  # noqa: E402


def test_degenerate_position_takes_the_record_base_when_the_pool_has_it():
    o, t, ino = resolve("ACRT", "ACGT")
    assert (o, t, ino) == ("ACGT", "ACGT", False)


def test_degenerate_position_outside_the_pool_stays_a_mismatch():
    o, t, _ = resolve("ACRT", "ACTT")  # R = A/G, record has T
    assert o[2] in "AG" and t[2] == "T"


def test_undetermined_record_base_is_modelled_as_a_match():
    o, t, _ = resolve("ACGT", "ANGT")
    assert o == t == "ACGT"


def test_inosine_is_flagged():
    o, t, ino = resolve("ACIT", "ACGT")
    assert ino and o[2] == t[2] == "G"


def test_perfect_site_has_zero_shift_and_a_mismatch_lowers_tm():
    oligo = "GACCTTGGAGCATCAGGTTCAGC"
    tm, perfect, _ = duplex_tm(oligo, oligo, CFG)
    assert tm == pytest.approx(perfect)
    site = oligo[:11] + ("A" if oligo[11] != "A" else "C") + oligo[12:]
    tm_mm, _, _ = duplex_tm(oligo, site, CFG)
    assert tm_mm < perfect - 2


def test_annotate_fills_columns_for_an_amplicon_and_blanks_otherwise():
    row = next(
        r
        for r in csv.DictReader((FIX / "manifest.tsv").open(), delimiter="\t")
        if r["expected_call"] == "detect"
    )
    assay = ASSAYS[row["assay_id"]]
    oligos = {"forward": assay.oligos.forward.matching_seq, "reverse": assay.oligos.reverse.matching_seq}
    if assay.oligos.probe is not None:
        oligos["probe"] = assay.oligos.probe.matching_seq
    call = screen_record(assay, row["record_id"], RECORDS[row["record_id"]], CFG)
    cols = annotate(call, oligos, CFG)
    assert set(cols) == set(COLUMNS)
    assert float(cols["fwd_tm"]) > 40 and cols["thermo_min_dtm"] != ""
    none = screen_record(assay, "x", "ACGT" * 100, CFG)
    assert annotate(none, oligos, CFG)["fwd_tm"] == ""


def test_screen_thermo_flag_adds_columns_to_every_row(tmp_path):
    out = tmp_path / "calls.tsv"
    subprocess.run(
        [
            sys.executable,
            "-m",
            "assaywatch.screen",
            str(ROOT / "registry"),
            str(FIX / "records.fasta"),
            "--only",
            ",".join(sorted(ASSAYS)),
            "--thermo",
            "-o",
            str(out),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    rows = list(csv.DictReader(out.open(), delimiter="\t"))
    assert all(c in rows[0] for c in COLUMNS)
    amplified = [r for r in rows if r["call"] in ("detect", "reduced", "fail") and r["fwd_tm"]]
    assert amplified and all(r["thermo_min_dtm"] for r in amplified)
    # Perfect-match fixtures sit at (or within rounding of) zero shift.
    perfect = [r for r in rows if r["record_id"].endswith("__perfect") and r["call"] == "detect"]
    assert perfect and all(abs(float(r["thermo_min_dtm"])) < 0.05 for r in perfect)
