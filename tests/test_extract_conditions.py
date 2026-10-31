"""`scripts/extract_conditions.py`: every reading bug found by looking at the numbers.

Six defects were found on 2026-10-27 while reading the proposals it produced, and five
of them produced a plausible value that no range check could have caught. They are
pinned here one test each, with the paper that exposed them, because a regex that reads
a methods paragraph will be edited again and these are the ways it goes wrong.

What is NOT tested here is attribution -- which assay in a multi-assay paper a sentence
belongs to. No pattern can do that, which is why `--apply --only-sole` refuses a paper
that prints more than one protocol and leaves it to a reader.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _module():
    spec = importlib.util.spec_from_file_location(
        "extract_conditions", ROOT / "scripts" / "extract_conditions.py"
    )
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_annealing_temperature_is_the_one_next_to_the_word():
    """Rossi 2024: the first temperature in range was the reverse-transcription step."""
    m = _module()
    s = (
        "The PCR program was unique for all the targets and comprised 15 min at 50 °C for "
        "reverse transcription, 2 min of denaturation at 95 °C and 50 cycles of denaturation "
        "at 95 °C for 15 s and annealing at 54 °C for 30 s."
    )
    assert m._temp_near_anneal(s) == 54.0


def test_a_parenthesised_label_beats_proximity():
    """The label sat nearer the elongation temperature than the one it labels."""
    m = _module()
    s = (
        "Further 40 PCR cycles were then undertaken using 94°C for 30 s (denaturation), "
        "52°C for 1 min (annealing) and 68°C for 30 s (elongation)."
    )
    assert m._temp_near_anneal(s) == 52.0


def test_a_lost_degree_sign_is_not_a_temperature():
    """Chmielewicz 2001 renders every degree sign as the digit 8: "948C" is 94 C.

    A two-digit match inside "948C" is "48", which is how a pan-herpes assay came to
    carry an annealing temperature of 48 from a paper that prints 46.
    """
    m = _module()
    raw = (
        "Reactions were cycled 35 times with 30 s of denaturation at 948C, 60 s of annealing "
        "at 468C, and 3 min of strand extension at 728C."
    )
    (s,) = m.sentences(raw)
    assert m._temp_near_anneal(s) == 46.0
    assert 48.0 not in m._temps(s)


def test_a_spaced_out_decimal_point_is_read_whole():
    """Rahn 1992 prints "1 . 25 mm MgCl 2"; a plain pattern read 25 mM."""
    m = _module()
    s = "The 25 pl PCR mixture contained : 50 mm KCI; 0 . 075 pm of each primer; 1 . 25 mm MgCl 2 ."
    assert m._amount_before(s, r"mM\s*MgCl") == 1.25


def test_a_decimal_comma_is_read_whole():
    """Deckers 2009 prints "2,0 mM MgCl2"; a dot-only pattern read 0 mM, which no range
    check can catch, because zero magnesium is a number."""
    m = _module()
    s = "PCR mix (12,7 μl; containing 1x AmpliTaq buffer, 2,0 mM MgCl2, 2-5% DMSO)"
    assert m._amount_before(s, r"mM\s*MgCl") == 2.0


def test_a_stated_final_concentration_beats_the_stock():
    """Kuno 1998 prints "3 ul of 50 mM MgCl2 (final concentration, 1.5 mM)"."""
    m = _module()
    s = (
        "The PCRs were performed in 100 ul containing 10 ul of 10x Taq buffer, 3 ul of 50 mM "
        "MgCl2 (final concentration, 1.5 mM), 2 ul of 10 mM dNTP."
    )
    assert m._amount_before(s, r"mM\s*MgCl") == 1.5


def test_a_final_concentration_for_another_reagent_does_not_answer():
    """Long 1993's digestion buffer says "final concentration: 10 mM Tris", which an
    unanchored search read as the magnesium."""
    m = _module()
    s = (
        "Whole blood was digested at 60 C by the addition of proteinase K and 10x digestion "
        "buffer (final concentration: 10 mM Tris, pH 8.0) and 2 mM MgCl2 was present."
    )
    assert m._amount_before(s, r"mM\s*MgCl") == 2.0


def test_a_three_temperature_cycling_sentence_falls_back_to_the_middle():
    m = _module()
    rows = m.propose_for(
        "Temperature and time profiles were as follows: 94C for 1 min, 50C for 1 min, "
        "and 68C for 1 min for 30 cycles."
    )
    got = {(f, v) for _, f, v, _, _ in rows}
    assert ("annealing_c", "50.0") in got
    assert ("cycles", "30") in got
    assert any("middle-of-three" in how for _, f, _, how, _ in rows if f == "annealing_c")


def test_a_paper_with_two_annealing_temperatures_is_marked_ambiguous():
    """The guard that keeps --only-sole off a multi-protocol paper."""
    m = _module()
    rows = m.propose_for(
        "The first PCR used annealing at 53 C for 1 min. The nested PCR used annealing at 60 C for 30 s."
    )
    (row,) = [r for r in rows if r[1] == "annealing_c"]
    assert "AMBIGUOUS" in row[3] and "53.0" in row[3] and "60.0" in row[3]
