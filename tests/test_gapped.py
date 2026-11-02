"""The gapped scan is held to a plain dynamic programme, as match.py is held to brute force."""

import random

from assaywatch.gapped import align, hamming_scan, scan
from assaywatch.match import MATCH, _match_tables


def _cost(oligo, a, b):
    return int(_match_tables(oligo)[a][ord(b)] != MATCH)


def _brute_best(oligo, seq):
    """Textbook semi-global edit distance, min over every end position."""
    L, n = len(oligo), len(seq)
    prev = [0] * (n + 1)
    for i in range(1, L + 1):
        cur = [i] + [0] * n
        for j in range(1, n + 1):
            cur[j] = min(prev[j - 1] + _cost(oligo, i - 1, seq[j - 1]), prev[j] + 1, cur[j - 1] + 1)
        prev = cur
    return prev


def test_scan_matches_textbook_dp():
    rng = random.Random(7)
    for _ in range(200):
        oligo = "".join(rng.choice("ACGTRYN") for _ in range(rng.randint(4, 12)))
        seq = "".join(rng.choice("ACGTN") for _ in range(rng.randint(0, 40)))
        assert scan(oligo, seq).tolist() == _brute_best(oligo, seq)


def test_align_cost_equals_scan_minimum_and_traceback_is_consistent():
    rng = random.Random(11)
    for _ in range(200):
        oligo = "".join(rng.choice("ACGT") for _ in range(rng.randint(5, 15)))
        seq = "".join(rng.choice("ACGT") for _ in range(rng.randint(5, 40)))
        a = align(oligo, seq)
        assert a.cost == int(scan(oligo, seq).min())
        assert a.cost == len(a.mismatches) + a.n_indels
        # Oligo bases used = record bases used, adjusted for gaps.
        assert (a.end - a.start) == len(oligo) - len(a.deletions) + len(a.insertions)


def test_single_deletion_near_three_prime_is_found_and_located():
    oligo = "ACGTTGCAGGTCCATGA"
    site = oligo[:-4] + oligo[-3:]  # record lacks the 4th base from the 3' end
    window = "TTTTT" + site + "CCCCC"
    a = align(oligo, window)
    assert (a.cost, a.mismatches, a.insertions) == (1, (), ())
    assert len(a.deletions) == 1 and a.deletions[0] in (4, 5)  # either base of the GG run
    assert hamming_scan(oligo, window).min() > 1  # invisible without gaps


def test_ungapped_site_is_reported_ungapped():
    oligo = "ACGTTGCAGGTCCATGA"
    window = "GGG" + oligo[:5] + "T" + oligo[6:] + "GGG"
    a = align(oligo, window)
    assert a.n_indels == 0 and len(a.mismatches) == 1


def test_hamming_scan_matches_direct_count():
    oligo, seq = "ACGRT", "ACGATTACGGTACGCT"
    want = [sum(_cost(oligo, i, seq[s + i]) for i in range(5)) for s in range(len(seq) - 4)]
    assert hamming_scan(oligo, seq).tolist() == want
