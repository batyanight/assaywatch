"""The locus check: does a record hold an assay's target region, primers aside?

Improvement 3 of the 2026-11-10 review. When no primer site is found in a record, the
coverage map has to know whether that is a failure (the gene is there and the primers
no longer fit) or nothing at all (the record is a fragment of some other gene). The
locus check answers it without looking at the primers: it aligns a reference amplicon
against the record, allowing mismatches AND gaps, and reports how much of the
reference was found and how well it matched.

Sequences are made here from a fixed random seed, so every run sees the same bases.
Each test is one step of the plan, in the order written.
"""

from __future__ import annotations

import random

import pytest

from assaywatch.locus_check import LocusResult, locus_check, rule_from_config
from assaywatch.score import load_config

pytestmark = pytest.mark.fast

MIN_IDENTITY, MIN_COVERED = 0.70, 0.80  # the approved starting thresholds


def dna(n: int, seed: int) -> str:
    rng = random.Random(seed)  # a private generator: the same seed gives the same bases
    return "".join(rng.choice("ACGT") for _ in range(n))


def substitute(seq: str, share: float, seed: int) -> str:
    """Change `share` of the positions, each to a base that is certainly different."""
    rng = random.Random(seed)
    out = list(seq)
    for pos in rng.sample(range(len(seq)), round(share * len(seq))):
        out[pos] = rng.choice([b for b in "ACGT" if b != out[pos]])
    return "".join(out)


def revcomp(seq: str) -> str:
    return seq.translate(str.maketrans("ACGT", "TGCA"))[::-1]


AMPLICON = dna(200, seed=1)  # the reference amplicon: cut from a record the assay detects
LEFT, RIGHT = dna(600, seed=2), dna(600, seed=3)  # the rest of the genome around it


def check(record: str, references=(AMPLICON,)) -> LocusResult:
    return locus_check(record, list(references), MIN_IDENTITY, MIN_COVERED)


# --- step 1 --------------------------------------------------------------------------


def test_a_record_holding_the_exact_amplicon_has_the_locus():
    got = check(LEFT + AMPLICON + RIGHT)
    assert got.present
    assert got.identity == 1.0
    assert got.covered == 1.0


# --- step 2 --------------------------------------------------------------------------


def test_an_unrelated_record_does_not():
    """Unrelated DNA always shares SOME short stretch by chance. It is a sliver.

    So the identity of that sliver can be high, and it is `covered` that says no.
    """
    got = check(dna(2000, seed=9))
    assert not got.present
    assert got.covered < 0.25


# --- step 3 --------------------------------------------------------------------------


def test_a_locus_that_has_diverged_by_a_fifth_is_still_the_locus():
    """The case the check exists for: a distant lineage the primers no longer fit."""
    got = check(LEFT + substitute(AMPLICON, 0.20, seed=4) + RIGHT)
    assert got.present
    assert 0.78 <= got.identity <= 0.86  # 20% changed; a local alignment may trim a ragged end
    assert got.covered >= 0.95


# --- step 4 --------------------------------------------------------------------------


def test_a_deletion_in_the_locus_does_not_hide_it():
    """An ungapped search loses the frame after an indel. A gapped one steps over it.

    This is what turns "a primer site with a 3 bp deletion" from a blank into a failure.
    """
    deleted = AMPLICON[:90] + AMPLICON[93:]
    got = check(LEFT + deleted + RIGHT)
    assert got.present
    assert got.identity >= 0.98
    assert got.covered == 1.0


def test_an_insertion_in_the_locus_does_not_hide_it():
    got = check(LEFT + AMPLICON[:90] + "GATTACA" + AMPLICON[90:] + RIGHT)
    assert got.present
    assert got.identity >= 0.96


# --- step 5 --------------------------------------------------------------------------


def test_a_record_that_ends_halfway_through_the_amplicon_does_not_count():
    """Half a locus cannot say whether the assay would have amplified it."""
    got = check(LEFT + AMPLICON[:100])
    assert not got.present
    assert got.identity >= 0.95  # what is there matches...
    assert 0.45 <= got.covered <= 0.55  # ...and it is half of what is needed


def test_a_record_that_starts_inside_the_amplicon_is_judged_on_what_it_holds():
    got = check(AMPLICON[30:] + RIGHT)
    assert got.present  # 85% of the reference is there, above the 80% asked for
    assert 0.84 <= got.covered <= 0.86


# --- step 6 --------------------------------------------------------------------------


def test_the_locus_is_found_on_the_other_strand():
    got = check(revcomp(LEFT + AMPLICON + RIGHT))
    assert got.present
    assert got.identity == 1.0


# --- the edges ---------------------------------------------------------------------------


def test_the_best_of_several_reference_amplicons_decides():
    """An assay's references are cut from several records; the nearest one speaks."""
    other_lineage = substitute(AMPLICON, 0.45, seed=5)
    record = LEFT + other_lineage + RIGHT
    assert not check(record, [AMPLICON]).present
    got = check(record, [AMPLICON, other_lineage])
    assert got.present and got.identity == 1.0


def test_no_reference_means_no_answer_rather_than_a_guess():
    got = check(LEFT + AMPLICON + RIGHT, references=())
    assert got == LocusResult(present=False, identity=0.0, covered=0.0)


def test_an_empty_record_is_absent():
    assert not check("").present


def test_undetermined_record_bases_count_against_the_match():
    """A run of N is not evidence that the locus is there.

    80 of 200 bases are N, so the aligner is left with the 60 bp either side and
    reports the better one: a perfect match over less than a third of the reference.
    """
    masked = AMPLICON[:60] + "N" * 80 + AMPLICON[140:]
    got = check(LEFT + masked + RIGHT)
    assert not got.present
    assert got.covered <= 0.31


def test_both_thresholds_are_inclusive():
    record = LEFT + AMPLICON + RIGHT
    assert locus_check(record, [AMPLICON], 1.0, 1.0).present
    half = LEFT + AMPLICON[:100]
    covered = locus_check(half, [AMPLICON], 0.0, 0.0).covered
    assert locus_check(half, [AMPLICON], 0.0, covered).present
    assert not locus_check(half, [AMPLICON], 0.0, covered + 0.01).present


def test_unrelated_dna_stays_far_under_the_coverage_threshold():
    """The chance floor, measured, because a gapped aligner flatters unrelated sequence.

    `locus_identity.identity` is ungapped on purpose for exactly that reason. Here 40
    random 3 kb records are searched for a 200 bp reference they do not hold. The
    longest chance match among them must stay far from the 80% asked for, or the
    threshold is inside the noise.
    """
    worst = max(locus_check(dna(3000, seed=100 + i), [AMPLICON], 0.0, 0.0).covered for i in range(40))
    assert worst < MIN_COVERED / 2, worst


def test_the_shipped_config_carries_the_approved_starting_thresholds():
    assert rule_from_config(load_config()) == (MIN_IDENTITY, MIN_COVERED)
