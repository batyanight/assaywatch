"""The chance E-value: exact tails, sensible orders of magnitude, and the guard in the screener."""

import random
from math import comb

import pytest
from test_score import ASSAYS, CFG, RECORDS

from assaywatch.chance import UNIFORM, composition, pair_evalue, tail
from assaywatch.score import screen_record


def test_tail_matches_the_binomial_for_a_plain_oligo():
    t = tail("ACGTACGTACGTACGTAC")
    for k in (0, 3, 6):
        want = sum(comb(18, j) * 0.75**j * 0.25 ** (18 - j) for j in range(k + 1))
        assert t[k] == pytest.approx(want)
    assert t[-1] == pytest.approx(1.0)


def test_degenerate_positions_are_easier_to_match():
    assert tail("ACGTNCGTAC")[0] > tail("ACGTACGTAC")[0]


def test_composition_counts_determined_bases_only():
    assert composition("AAAANNNN") == (1.0, 0.0, 0.0, 0.0)
    assert composition("NNN") == UNIFORM


def test_orders_of_magnitude():
    f = r = "CTTGGCTGATGGCACGAT"
    assert pair_evalue(f, r, 0, 0, 5_000_000, CFG) < 1e-10  # perfect pair in a genome
    assert pair_evalue(f, r, 6, 6, 5_000_000, CFG) > 100  # six-and-six in a genome: chance
    assert pair_evalue(f, r, 5, 5, 1_000, CFG) < 0.01  # five-and-five in a gene record: real
    # The record length carries the difference.
    assert pair_evalue(f, r, 6, 6, 1_000, CFG) < pair_evalue(f, r, 6, 6, 5_000_000, CFG) / 1e4


def test_guard_turns_a_chance_pair_into_no_amplicon_but_keeps_a_real_one():
    bd = "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004"
    assay = ASSAYS[bd]
    rng = random.Random(3)
    genome = "".join(rng.choice("ACGT") for _ in range(400_000))
    strict = {**CFG, "scoring": {**CFG["scoring"], "max_pair_evalue": 0.01}}
    real = genome[:200_000] + RECORDS[f"{bd}__perfect"] + genome[200_000:]
    assert screen_record(assay, "g", real, strict).call == "detect"
    noisy = screen_record(assay, "g", genome, CFG)
    guarded = screen_record(assay, "g", genome, strict)
    assert guarded.call == "no_amplicon"
    if noisy.call != "no_amplicon":
        assert float(noisy.as_row()["pair_evalue"]) > 0.01 and "chance" in guarded.reason


def test_evalue_column_is_always_present():
    bd = "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004"
    row = screen_record(ASSAYS[bd], "x", RECORDS[f"{bd}__perfect"], CFG).as_row()
    assert float(row["pair_evalue"]) < 1e-6
    assert screen_record(ASSAYS[bd], "x", "ACGT" * 50, CFG).as_row()["pair_evalue"] == ""


def test_the_window_term_follows_the_window_the_caller_accepts():
    """E counts reverse-primer offsets that give an ALLOWED length, so the caller's window decides it.

    Scoring narrows the window to the assay's declared product size, and leaving
    the E-value on the global 50-3000 bp range overstates E by the ratio of the
    two — 2951/98 for a 194 bp assay at +/-25%. The pairs that overstatement
    pushes past `max_pair_evalue` are the worst-matching ones, which is the
    drifted end, so they leave the denominator instead of being scored.
    """
    cfg = {"amplicon": {"min_bp": 50, "max_bp": 3000}}
    fwd, rev = "GTCGACTAGCTAGCTAGCT", "ACGTACGTTGCATGCATGC"
    wide = pair_evalue(fwd, rev, 5, 5, 200_000, cfg)
    narrow = pair_evalue(fwd, rev, 5, 5, 200_000, cfg, window_bp=98)
    assert wide / narrow == pytest.approx(2951 / 98, rel=1e-6)
    # The window can never exceed the record, however wide the caller's range.
    assert pair_evalue(fwd, rev, 0, 0, 120, cfg, window_bp=5000) == pair_evalue(
        fwd, rev, 0, 0, 120, cfg, window_bp=120
    )
