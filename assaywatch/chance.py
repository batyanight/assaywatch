"""How likely is a primer pair this good to turn up by chance? An E-value per amplicon.

The search budget (six mismatches per oligo) is generous on purpose, so that a
drifted site is still found and scored rather than missed. The price is
specificity on long records: an 18-mer has a site within six mismatches every
few kilobases of random sequence, so a multi-megabase genome holds hundreds of
facing forward/reverse pairs in amplicon range that have nothing to do with the
target. Before this column existed, a quarter of all `fail` calls in the first
full run had both primers at five or more mismatches, and for the herpesvirus,
adenovirus and lyssavirus assays their amplicon lengths matched no `detect`
call at all: they were chance pairs, and they were in the drift denominator.

The E-value is the expected number of pairs at least this good in a random
record of the same length and base composition:

    E = 2 * n * P_f(<= k_f) * min(W, n) * P_r(<= k_r)

n is the record length, W the number of reverse-primer offsets that give an
allowed amplicon length (max_bp - min_bp + 1), k the number of positions of
each primer that do not definitely match (mismatches plus undetermined bases,
the same count the search budget uses), and P(<= k) the probability that a
random site of that composition has at most k such positions, computed exactly
(a Poisson-binomial over the primer's positions, so degenerate positions count
as the easier matches they are). The factor 2 is for the two orientations.

A real site scores far below 1: a perfect 18-mer pair in a 5 Mb genome is
around 6e-12. A six-and-six pair in the same genome is around 1600, which is
the several hundred chance pairs actually seen per Yersinia chromosome. In a
1 kb gene record a six-and-six pair is around 0.1 (still not convincing) and a
five-and-five pair around 0.002. The threshold therefore does not need to know
what kind of record it is looking at: the record length carries that.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Any

from assaywatch.iupac import IUPAC

UNIFORM = (0.25, 0.25, 0.25, 0.25)


def composition(seq: str) -> tuple[float, float, float, float]:
    """A, C, G, T frequencies of the determined bases; uniform if there are none."""
    s = seq.upper()
    counts = [s.count(b) for b in "ACGT"]  # str.count runs in C; a Counter over a genome does not
    n = sum(counts)
    if not n:
        return UNIFORM
    # Rounded so the cache below gets hits across records of similar composition.
    return tuple(round(c / n, 3) for c in counts)


@lru_cache(maxsize=4096)
def tail(oligo: str, comp: tuple[float, float, float, float] = UNIFORM) -> tuple[float, ...]:
    """P(at most k positions not matched) for k = 0..len(oligo), random site of composition `comp`."""
    freq = dict(zip("ACGT", comp, strict=True))
    # Poisson-binomial by dynamic programming: each oligo position is an
    # independent coin with its OWN probability of matching (a degenerate
    # position is easier to match than a fixed one), so this is not a binomial
    # and has no closed form. dist[k] = P(exactly k misses over the positions
    # handled so far); each position convolves one more coin into it.
    dist = [1.0]
    for code in oligo.upper():
        p = min(1.0, sum(freq[b] for b in IUPAC.get(code, "ACGT") if b in freq))
        nxt = [0.0] * (len(dist) + 1)
        for k, v in enumerate(dist):
            nxt[k] += v * p
            nxt[k + 1] += v * (1 - p)
        dist = nxt
    # Return the cumulative form, P(at most k), since every caller asks whether a
    # site within its budget could have arisen by chance.
    out, acc = [], 0.0
    for v in dist:
        acc += v
        out.append(min(1.0, acc))
    return tuple(out)


def site_evalue(
    oligo: str, k: int, record_len: int, comp: tuple[float, float, float, float] = UNIFORM
) -> float:
    """Expected number of sites for ONE oligo within `k` misses, either strand.

    Used to decide whether a lone oligo hit means anything, which matters for
    records too short to carry a whole amplicon: a 15 nt probe has a chance
    match within six misses in almost any record, while a perfect match to it
    in a 257 bp record is about 5e-7. The pair E-value is the product of two of
    these and the window term.
    """
    return 2.0 * record_len * tail(oligo, comp)[min(k, len(oligo))]


def pair_evalue(
    fwd: str,
    rev: str,
    k_fwd: int,
    k_rev: int,
    record_len: int,
    cfg: dict[str, Any],
    comp: tuple[float, float, float, float] = UNIFORM,
    window_bp: int | None = None,
) -> float:
    """Expected number of pairs at least this good in a random record like this one.

    `window_bp` is how many reverse-primer offsets give an ALLOWED amplicon
    length, and it must be the window the caller will actually accept. Scoring
    narrows that window to the assay's declared product size
    (`amplicon.declared_tolerance`), so leaving it at the global 50-3000 bp
    range overstates E by the ratio of the two - 30x for a 194 bp assay at
    +/-25%, whose window is 98 bp against the global 2951 - and the
    overstatement is not harmless: the pairs it pushes past
    `max_pair_evalue` are the worst-matching ones, which are the drifted ones,
    so they leave the drift denominator instead of being scored as failures.

    Callers that work on oligo PAIRS and so have no declared size (the assembly
    pre-cut, `loci.py`) omit it and get the global window, which is the
    permissive direction: the pre-cut only decides which windows are worth
    keeping, and screening applies the real test afterwards.
    """
    amp = cfg["amplicon"]
    if window_bp is None:
        window_bp = int(amp["max_bp"]) - int(amp["min_bp"]) + 1
    window = min(max(int(window_bp), 1), max(record_len, 1))
    pf = tail(fwd, comp)[min(k_fwd, len(fwd))]
    pr = tail(rev, comp)[min(k_rev, len(rev))]
    return 2.0 * record_len * pf * window * pr
