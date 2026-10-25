"""The locus-identity test (assaywatch.locus_identity), 2026-10-25.

The generalisation of the chance-pair test to conventional assays. These pin the
safety properties rather than the arithmetic: off by default, unknown keeps the
record, a short amplicon is never judged, an assay with no reference is never
judged, and the measured separation (chance pairs 0.32-0.41, real loci 0.65+)
falls on the right side of the recommended 0.50.
"""

from __future__ import annotations

import random

from assaywatch.locus_identity import (
    LOCUS_MISMATCH,
    best_identity,
    identity,
    interior,
    is_locus,
    revcomp,
)

ON = {"scoring": {"locus_identity_min": 0.50}}
OFF: dict = {"scoring": {}}


def _dna(n, seed):
    r = random.Random(seed)
    return "".join(r.choice("ACGT") for _ in range(n))


def test_the_label_is_distinct_from_the_chance_pair_one():
    """Two tests, two labels: one acts on probe absence at report time, this on
    sequence at screen time, and a report must be able to tell them apart."""
    from assaywatch.calls import CHANCE_PAIR

    assert LOCUS_MISMATCH != CHANCE_PAIR


def test_off_unless_the_threshold_is_set():
    unrelated = _dna(200, 1)
    assert is_locus(unrelated, [_dna(200, 2)], OFF) is True
    assert is_locus(unrelated, [_dna(200, 2)], {}) is True


def test_identity_is_1_for_the_same_sequence_and_finds_the_reverse_complement():
    s = _dna(120, 3)
    assert identity(s, s) == 1.0
    assert identity(s, revcomp(s)) == 1.0


def _substituted(seq, fraction):
    """`seq` with the first `fraction` of its bases each changed to a different base.

    Deterministic and exact: every substituted base differs, so identity is exactly
    1 - fraction. A random re-draw would not do - it leaves a quarter of the
    substituted bases matching by chance, so a "33% mutation" scores 0.75 and not
    0.67, which is how two of these tests were wrong on their first writing.
    """
    nxt = {"A": "C", "C": "G", "G": "T", "T": "A"}
    k = int(len(seq) * fraction)
    return "".join(nxt[c] if i < k else c for i, c in enumerate(seq))


def test_unrelated_dna_scores_near_the_chance_floor():
    """Measured chance pairs sit at 0.32-0.41; unrelated DNA lands in that region,
    which is what makes 0.50 a threshold rather than a coin flip."""
    scores = [identity(_dna(150, i), _dna(150, 1000 + i)) for i in range(5)]
    assert all(s < 0.50 for s in scores), scores
    assert max(scores) < 0.45, scores


def test_a_real_locus_with_heavy_divergence_still_passes_at_the_recommended_threshold():
    """The case that decides the threshold. SIV Takehisa's genuine failures measured
    0.65-0.67, and 35% substitution reproduces exactly 0.65. Such a record is real
    drift and must stay evaluable - discarding it is the failure that killed the two
    approaches tried before this one."""
    ref = _dna(300, 4)
    drifted = _substituted(ref, 0.35)
    assert identity(drifted, ref) == 0.65
    assert is_locus(drifted, [ref], ON) is True


def test_an_unrelated_amplicon_is_rejected():
    assert is_locus(_dna(300, 6), [_dna(300, 7)], ON) is False


def test_a_short_amplicon_is_never_judged():
    """RANAVIRUS_..._MCP_Pallister_2007 is 57 bp: 17 bases survive the 20 bp trim,
    too few to mean anything. Unknown keeps the record evaluable."""
    assert interior("A" * 57) is not None  # 17 bases remain
    assert best_identity("A" * 57, [_dna(300, 8)]) is None
    assert is_locus(_dna(57, 9), [_dna(300, 10)], ON) is True


def test_an_amplicon_shorter_than_the_trim_is_never_judged():
    assert interior("A" * 40) is None
    assert is_locus(_dna(40, 11), [_dna(300, 12)], ON) is True


def test_an_assay_with_no_reference_is_never_judged():
    """Nothing defines the locus, so inventing one from a failure would make the
    test agree with whatever it was handed."""
    assert best_identity(_dna(300, 13), []) is None
    assert is_locus(_dna(300, 13), [], ON) is True


def test_the_best_reference_wins():
    ref_bad, ref_good = _dna(300, 14), _dna(300, 15)
    assert is_locus(ref_good, [ref_bad, ref_good], ON) is True


def test_the_threshold_is_inclusive_and_configurable():
    ref = _dna(300, 16)
    assert is_locus(ref, [ref], {"scoring": {"locus_identity_min": 1.0}}) is True


def test_070_is_the_value_the_measurement_rules_out():
    """Pinned so the known-wrong setting's effect stays visible: an SIV-shaped
    record at exactly 0.65 survives 0.50 and is destroyed by 0.70."""
    ref = _dna(300, 16)
    siv_shaped = _substituted(ref, 0.35)
    assert identity(siv_shaped, ref) == 0.65
    assert is_locus(siv_shaped, [ref], ON) is True
    assert is_locus(siv_shaped, [ref], {"scoring": {"locus_identity_min": 0.70}}) is False
