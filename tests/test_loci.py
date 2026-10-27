"""Where an assay's primers could build an amplicon: `loci.pair_spans`.

S9 in docs/journal/2026-10-20-pipeline-audit.md: 67 loc with no own test file and no
direct test reference at all, while `windows.py` and `assemblies.py` both cut
archives on its output. A span this misses is sequence thrown away before any
screen sees it, and no later stage can notice: the record simply does not
contain the locus any more. So these tests pin the coordinate convention, the
strand symmetry, and the deliberate over-generation the cut depends on.

The sequences are synthetic, built around real primer-length oligos, so every
expected coordinate is arithmetic rather than a recorded output.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from assaywatch.iupac import reverse_complement
from assaywatch.loci import pair_spans
from assaywatch.score import load_config

ROOT = Path(__file__).resolve().parent.parent

FWD = "ACGTTGCAATGCCGTAAGGT"  # 20 nt
REV = "TTGCCAGTTACGGATCCAAG"  # 20 nt
FWD2 = "GGCATTACGCATTGCAGTCA"
REV2 = "CCAATGGCATTAGCCATGGT"
MIDDLE = "AT" * 60  # 120 nt between the primer sites
AMPLICON = len(FWD) + len(MIDDLE) + len(REV)  # 160


@pytest.fixture(scope="module")
def cfg():
    return load_config(ROOT / "config.yaml")


def locus(fwd: str = FWD, rev: str = REV, pre: int = 50, post: int = 50) -> str:
    """One amplicon: `fwd` forward, `rev` reverse-complemented, flanked by filler.

    The reverse primer is stored 5'->3' on its own strand, so a record carrying
    the locus holds its reverse complement - which is what the screener matches
    on the minus strand.
    """
    return "G" * pre + fwd + MIDDLE + reverse_complement(rev) + "C" * post


def test_a_clean_pair_gives_one_span_covering_both_primers(cfg):
    """0-based half-open, from the forward site's start to the reverse site's end."""
    assert pair_spans(locus(), [(FWD, REV)], cfg, 2, 0.01, 50, 3000) == [(50, 50 + AMPLICON)]


def test_the_span_is_the_whole_amplicon_not_the_insert(cfg):
    (lo, hi) = pair_spans(locus(), [(FWD, REV)], cfg, 2, 0.01, 50, 3000)[0]
    assert hi - lo == AMPLICON
    assert locus()[lo : lo + len(FWD)] == FWD  # the primer itself is inside the span
    assert locus()[hi - len(REV) : hi] == reverse_complement(REV)


def test_the_same_locus_is_found_on_the_other_strand(cfg):
    """A locus may sit either way round in a deposit, so both orientations scan."""
    seq = locus()
    forward = pair_spans(seq, [(FWD, REV)], cfg, 2, 0.01, 50, 3000)
    reversed_record = pair_spans(reverse_complement(seq), [(FWD, REV)], cfg, 2, 0.01, 50, 3000)
    assert forward == [(50, 210)]
    # Same locus, mirrored: equal flanks here make the span land at the same offsets.
    assert reversed_record == [(50, 210)]


def test_an_asymmetric_record_mirrors_the_span_rather_than_repeating_it(cfg):
    """With unequal flanks the minus-strand span is the plus one reflected."""
    seq = locus(pre=10, post=90)
    n = len(seq)
    (lo, hi) = pair_spans(seq, [(FWD, REV)], cfg, 2, 0.01, 50, 3000)[0]
    (rlo, rhi) = pair_spans(reverse_complement(seq), [(FWD, REV)], cfg, 2, 0.01, 50, 3000)[0]
    assert (lo, hi) == (10, 10 + AMPLICON)
    assert (rlo, rhi) == (n - hi, n - lo)


def test_primers_facing_away_from_each_other_are_not_an_amplicon(cfg):
    """Back-to-back sites amplify nothing, however close they are."""
    away = "G" * 50 + reverse_complement(REV) + MIDDLE + FWD + "C" * 50
    assert pair_spans(away, [(FWD, REV)], cfg, 2, 0.01, 50, 3000) == []


def test_the_order_of_the_sites_is_what_rejects_them_not_the_product_length(cfg):
    """Isolates the `facing` test from the length window, which otherwise hides it.

    In the case above the sites are far apart in the wrong order, so the implied
    product length comes out negative and the window rejects it first - mutating
    the `facing` check away leaves every other test in this file passing. Here
    the two sites abut and `lo_bp` is 0, so the length window admits the span and
    only the ordering can refuse it.
    """
    wrong = "G" * 50 + reverse_complement(REV) + FWD + "C" * 50
    right = "G" * 50 + FWD + reverse_complement(REV) + "C" * 50
    assert pair_spans(wrong, [(FWD, REV)], cfg, 2, 0.01, 0, 3000) == []
    assert pair_spans(right, [(FWD, REV)], cfg, 2, 0.01, 0, 3000) != []


def test_a_product_outside_the_length_window_is_rejected(cfg):
    seq = locus()
    assert pair_spans(seq, [(FWD, REV)], cfg, 2, 0.01, 50, 100) == []  # 160 > 100
    assert pair_spans(seq, [(FWD, REV)], cfg, 2, 0.01, 200, 3000) == []  # 160 < 200
    assert pair_spans(seq, [(FWD, REV)], cfg, 2, 0.01, AMPLICON, AMPLICON) == [(50, 210)]  # inclusive


def test_mismatches_are_allowed_only_up_to_max_mm(cfg):
    """One substitution in the forward site: invisible at 1, fatal at 0."""
    mutated = FWD[:-1] + ("A" if FWD[-1] != "A" else "C")
    seq = locus(fwd=mutated)
    assert pair_spans(seq, [(FWD, REV)], cfg, 0, 0.01, 50, 3000) == []
    assert pair_spans(seq, [(FWD, REV)], cfg, 1, 0.01, 50, 3000) == [(50, 210)]


def test_the_chance_evalue_gate_can_reject_a_site_that_matches(cfg):
    """max_e is a second filter after the mismatch count, not a formality."""
    seq = locus()
    assert pair_spans(seq, [(FWD, REV)], cfg, 2, 0.01, 50, 3000) == [(50, 210)]
    assert pair_spans(seq, [(FWD, REV)], cfg, 2, 0.0, 50, 3000) == []


def test_every_pairing_is_returned_not_only_the_best(cfg):
    """Two copies of a locus give three spans, because the cross pairing is also
    an amplicon the screener could build. The pre-cut must keep all of them: a
    later screen at tighter settings picks one, and a cut around only the
    closest pair would have thrown the other's sequence away."""
    seq = locus() + "T" * 300 + locus()
    spans = pair_spans(seq, [(FWD, REV)], cfg, 2, 0.01, 50, 3000)
    assert spans == [(50, 210), (50, 770), (610, 770)]


def test_each_pair_in_the_list_is_searched(cfg):
    seq = locus() + "T" * 300 + locus(fwd=FWD2, rev=REV2)
    assert pair_spans(seq, [(FWD, REV), (FWD2, REV2)], cfg, 2, 0.01, 50, 3000) == [(50, 210), (610, 770)]


def test_a_pair_whose_sites_are_absent_contributes_nothing(cfg):
    seq = locus()
    assert pair_spans(seq, [(FWD2, REV2)], cfg, 2, 0.01, 50, 3000) == []


def test_no_pairs_and_no_sequence_are_both_empty_not_an_error(cfg):
    assert pair_spans(locus(), [], cfg, 2, 0.01, 50, 3000) == []
    assert pair_spans("", [(FWD, REV)], cfg, 2, 0.01, 50, 3000) == []
    assert pair_spans("A" * 400, [(FWD, REV)], cfg, 2, 0.01, 50, 3000) == []


def test_a_forward_site_with_no_reverse_partner_is_not_a_span(cfg):
    """Half a locus is not a locus; the reverse lookup short-circuits."""
    half = "G" * 50 + FWD + MIDDLE + "C" * 50
    assert pair_spans(half, [(FWD, REV)], cfg, 2, 0.01, 50, 3000) == []
