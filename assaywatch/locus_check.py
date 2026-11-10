"""The locus check: does a record hold an assay's target region, primers aside?

THE QUESTION. The screen finds no primer site in a record. Either the gene is there
and the primers no longer fit it (a failure of the assay, and the most interesting
kind), or the record is a fragment of something else and never tested the assay at
all. The primers cannot tell these apart, because in both cases they found nothing.
The locus check asks the record directly: it takes a reference amplicon, cut from a
record the assay does detect, and looks for it in the new record with an alignment
that tolerates mismatches and gaps.

It is NOT `locus_identity`. That module judges an amplicon the primers DID find
("is this product the assay's locus, or two primers that met by chance?"), ungapped,
on the stretch between the primer sites. This one searches a whole record for a
locus the primers did NOT find.

THE METHOD is a local alignment (Smith-Waterman). "Local" means the alignment may
start and stop anywhere in both sequences, and is the best-scoring stretch they
share. That is what makes the two reported numbers mean what they say:

    covered    how much of the reference amplicon the shared stretch spans
    identity   of the aligned columns in that stretch, the share that match

A record that ends halfway through the locus gives identity 1.0 over covered 0.5. A
diverged lineage gives covered 1.0 at identity 0.8. Unrelated DNA gives a short
chance match: high identity over a sliver. The locus is PRESENT when both numbers
clear their thresholds, so it takes a good match over most of the amplicon.

THE SCORES are +1 for a match, -1 for a mismatch and -3 for each gapped base. They
decide which stretch is "best", and two properties were wanted of them:

* Substitutions break even at 50% identity, so a locus at the 70% threshold still
  scores +0.4 a column and the alignment runs its whole length instead of breaking
  into pieces.
* A gap costs three matches, so the aligner steps over a real indel and cannot buy a
  better-looking alignment between unrelated sequences by opening gaps everywhere,
  which is the objection `locus_identity.identity` raises to gapped alignment.

MEASURED 2026-11-10 on simulated sequence, three schemes, at thresholds 0.70 / 0.80
(`docs/journal/2026-11-10-coverage-map.md` has the table). "Found" is how many of 40
true 200 bp loci carrying that share of substitutions were called present; "chance"
is the longest stretch of a 200 bp reference matched in random 3 kb records.

    mismatch, gap    found at 20%  25%  30%  35%     chance (covered)
    -1, -2           40   40   40   0                0.56
    -2, -3           40   35   11   0                0.10
    -1, -3  (used)   40   40   40   0                0.23

The BLAST-like -2 breaks even near 67% identity and fragments exactly the diverged
loci this check exists to find. -1 with a cheap gap finds them and also stretches
chance matches over half the reference. -1 with gap -3 finds as many and keeps
chance matches short. No random record was called present under any scheme (172
trials each). Nothing above 30% substitution is found at an identity threshold of
0.70, by construction: that is the threshold doing its job, not the aligner failing.

They are constants here and not in config.yaml because they are not thresholds on a
call: the two numbers that decide (`coverage.locus_min_identity`,
`coverage.locus_min_covered`) are in config.

COST. Aligning a whole record is len(reference) numpy sweeps along it: 0.8 s for a
300 bp reference against a 200 kb record on both strands (measured 2026-11-10), and
five references of 490 bp against a 105 kb ranavirus genome is several seconds, which
no archive of genomes can afford. So a record over EXHAUSTIVE_MAX_BP is SEEDED first:
shared 7-base words pick out stretches of it, every reference and strand proposing
its own, and only the twelve fullest of them all are aligned (`_windows`). A short
record is aligned whole, but an assay can carry eight references, which is sixteen
alignments on two strands: the same shared words rank them and only the WHOLE_TOP
fullest are aligned. With one or two references nothing is dropped. Both are
heuristics and are tested against the exhaustive answer.

WHO CALLS IT. `assaywatch locus` (`locus.py`) runs it on the records the screen
could not judge and writes a side file; `assaywatch coverage --locus` joins that as
`locus_present`. The screen never calls it, so adding it rescreened nothing.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

import numpy as np

MATCH, MISMATCH, GAP = 1, -1, 3  # GAP is a cost: each gapped base subtracts it

#: Seeding, for records too long to align whole. See `_windows`.
SEED_K = 7  # word length
SEED_BIN = 16  # diagonals per bin: how much indel drift one bin forgives
SEED_TOP = 12  # stretches of a long record aligned, over all references and strands
EXHAUSTIVE_MAX_BP = 5000  # at or under this a record is aligned whole
WHOLE_TOP = 4  # references-and-strands a short record is aligned against, fullest first

_COMPLEMENT = str.maketrans("ACGT", "TGCA")


@dataclass(frozen=True)
class LocusResult:
    """Whether the locus is in the record, and the two numbers that decided it."""

    present: bool
    identity: float  # share of aligned columns that match
    covered: float  # share of the reference amplicon the alignment spans
    #: How many record bases lie beyond each end of where the WHOLE reference would
    #: sit, left and right in the record's own order (negative when the reference
    #: would run off that end). The reference is usually an amplicon's interior with
    #: the primer sites trimmed off, so these say whether the record goes on far
    #: enough to have held the primer sites at all. See `locus.judge`.
    flank_left: int = 0
    flank_right: int = 0
    #: Which strand of the record the winning reference matched: "+" as written, "-"
    #: reverse-complemented. "" when nothing matched.
    strand: str = ""
    #: Which of the reference amplicons won, as an index into the list that was given.
    reference: int = -1
    #: The stretch of the winning reference the alignment spans, as positions on the
    #: reference IN THE ORIENTATION THAT MATCHED (reverse-complemented when `strand`
    #: is "-"). `covered` is its length over the reference's; `locus.judge` uses the
    #: positions to ask how much of the AMPLICON part was reached.
    ref_start: int = 0
    ref_end: int = 0


ABSENT = LocusResult(present=False, identity=0.0, covered=0.0)


def rule_from_config(cfg: Mapping[str, Any]) -> tuple[float, float]:
    """(min_identity, min_covered) from `coverage:`; the only config this module reads."""
    c = cfg["coverage"]
    return float(c["locus_min_identity"]), float(c["locus_min_covered"])


def _clean(seq: str) -> str:
    return seq.upper().replace("U", "T")


def _revcomp(seq: str) -> str:
    """Reverse complement; anything that is not A, C, G or T becomes N and matches nothing."""
    return "".join(b if b in "ACGT" else "N" for b in seq.translate(_COMPLEMENT)[::-1])


def _sweep(reference: str, rec: np.ndarray, keep: bool) -> tuple[int, int, int, list[np.ndarray]]:
    """Fill the local-alignment table one reference base at a time.

    H[i][j] is the best score of any alignment ENDING at reference base i and record
    base j, never below zero (zero means "start afresh here", which is what makes
    the alignment local). Each cell is the best of three moves:

        diagonal   pair reference base i with record base j   (+1 or -1)
        up         skip reference base i                       (-GAP)
        left       skip record base j                          (-GAP)

    The first two depend only on the row above, so a whole row is computed at once
    with numpy. The third depends on the cell to the LEFT in the same row, which
    looks sequential, but a run of k skipped record bases costs exactly GAP * k, so

        H[i][j] = max over k <= j of (V[k] - GAP * (j - k))
                = cummax(V[k] + GAP * k) - GAP * j

    and a running maximum does the whole row in one pass. This is the trick
    `gapped.scan` uses for edit distance, with max in place of min.

    Returns (best score, i, j) for the best cell, and every row when `keep` is true
    (needed for the traceback, and only ever asked for on a short window).
    """
    n = len(rec)
    idx = np.arange(n + 1, dtype=np.int32) * GAP
    prev = np.zeros(n + 1, dtype=np.int32)
    rows = [prev] if keep else []
    best, best_i, best_j = 0, 0, 0
    for i, base in enumerate(reference, start=1):
        # A base outside ACGT (in either sequence) pairs with nothing: an undetermined
        # base is not evidence that the locus is there.
        pair = np.where(rec == ord(base), MATCH, MISMATCH).astype(np.int32) if base in "ACGT" else MISMATCH
        v = np.zeros(n + 1, dtype=np.int32)
        np.maximum(prev[:-1] + pair, prev[1:] - GAP, out=v[1:])
        np.maximum(v, 0, out=v)
        cur = np.maximum.accumulate(v + idx) - idx
        top = int(cur.max())
        if top > best:
            best, best_i, best_j = top, i, int(cur.argmax())
        if keep:
            rows.append(cur)
        prev = cur
    return best, best_i, best_j, rows


def _kmer_codes(rec: np.ndarray) -> np.ndarray:
    """Every K-base word of a sequence as one integer; -1 where the word holds a non-ACGT base.

    Each base is two bits (A=0, C=1, G=2, T=3), so a 7-base word is a number below
    16,384 and two words are equal exactly when their numbers are. Built with K
    shifted additions over the whole array, so there is no Python loop over the record.
    """
    base = np.full(256, -1, dtype=np.int64)
    for value, letter in enumerate("ACGT"):
        base[ord(letter)] = value
    c = base[rec]
    n = len(c) - SEED_K + 1
    if n <= 0:
        return np.empty(0, dtype=np.int64)
    code = np.zeros(n, dtype=np.int64)
    bad = np.zeros(n, dtype=bool)
    for offset in range(SEED_K):
        part = c[offset : offset + n]
        bad |= part < 0
        code = code * 4 + np.where(part < 0, 0, part)
    code[bad] = -1
    return code


def _windows(reference: str, record_codes: np.ndarray, record_len: int) -> list[tuple[int, int, int]]:
    """Where in a long record is this reference worth aligning? Up to SEED_TOP stretches,
    each as (shared words, start, end), fullest first.

    THE IDEA is BLAST's. Two sequences that share a locus share short exact words
    (k-mers) even when they differ at a third of their bases, and they share them IN
    ORDER: a word at reference position i sits at record position j with j - i about
    constant. That difference is the DIAGONAL of the alignment table. Chance word
    matches scatter over every diagonal; a real locus piles them onto one. So: find
    every shared word, count them per diagonal (in bins of SEED_BIN, to forgive
    indels), and align only around the fullest bins.

    This makes a 100 kb record cost what a 600 bp one does. It is a HEURISTIC and can
    miss: a locus that shares too few intact K-base words with every reference is
    never aligned. `tests/test_locus_check.py` checks the seeded answer against the
    exhaustive one, and the word length and the number of stretches were set by
    measurement (2026-11-10): a 200 bp locus with 30% of its bases substituted, the
    hardest case the identity threshold still admits, in 100 kb of random sequence,
    found 40 of 40 times when the record is aligned whole.

        words of 8, 3 stretches    35 of 40     words of 7, 12 stretches   39 of 40
        words of 8, 30 stretches   37 of 40     words of 6, 30 stretches   40 of 40

    7 and 12 is used: one miss in 40 at the very edge, at half the time of 6 and 30.
    Evenly spread substitutions are the worst case for a seed, because real loci
    diverge in patches and keep long words in their conserved blocks. A record at or
    under EXHAUSTIVE_MAX_BP skips all this and is aligned whole.
    """
    ref_codes = _kmer_codes(np.frombuffer(reference.encode("ascii", "replace"), dtype=np.uint8))
    ref_codes_ok = np.flatnonzero(ref_codes >= 0)
    if len(ref_codes_ok) == 0 or len(record_codes) == 0:
        return []
    # Sort the reference's words once, then look every record word up by binary search.
    order = ref_codes_ok[np.argsort(ref_codes[ref_codes_ok], kind="stable")]
    sorted_codes = ref_codes[order]
    at = np.searchsorted(sorted_codes, record_codes)
    at[at == len(sorted_codes)] = 0
    hit = np.flatnonzero((sorted_codes[at] == record_codes) & (record_codes >= 0))
    if len(hit) == 0:
        return []
    diagonal = hit - order[at[hit]]  # record position minus reference position
    bins, counts = np.unique(diagonal // SEED_BIN, return_counts=True)
    # A locus whose diagonal falls on a bin edge splits its words between two bins, so
    # each bin is ranked by its own count plus its right-hand neighbour's.
    neighbour = np.zeros_like(counts)
    adjacent = np.flatnonzero(np.diff(bins) == 1)
    neighbour[adjacent] = counts[adjacent + 1]
    pad = 2 * SEED_BIN + len(reference) // 4  # room for indels and for the two bins' width
    weight = counts + neighbour
    spans = []
    for k in np.argsort(-weight, kind="stable")[:SEED_TOP]:
        start = int(bins[k]) * SEED_BIN  # where reference base 0 would sit in the record
        spans.append((int(weight[k]), max(0, start - pad), min(record_len, start + len(reference) + pad)))
    return spans


def _traceback(reference: str, record: str, i_end: int, j_end: int) -> tuple[int, int, int, int]:
    """Walk the best alignment backwards. Returns (matches, columns, reference start, record start).

    The sweep over the whole record keeps only one row at a time, so it knows where
    the best alignment ENDS and not where it began. This refills the table for just
    the window that alignment can occupy, keeps every row, and steps back from the
    end cell: at each cell, whichever of the three moves produces the stored score
    is the one that was taken. It stops at a zero, where the alignment started.
    """
    # The alignment ends at (i_end, j_end) and uses at most i_end reference bases, so
    # its record stretch is at most that long plus the record bases it skipped; twice
    # over is more than a positive-scoring alignment can afford at GAP per base.
    lo = max(0, j_end - 2 * i_end - 8)
    ref, window = reference[:i_end], record[lo:j_end]
    rec = np.frombuffer(window.encode("ascii", "replace"), dtype=np.uint8)
    _, _, _, rows = _sweep(ref, rec, keep=True)
    i, j = len(ref), len(window)
    matches = columns = 0
    while i > 0 and j > 0 and rows[i][j] > 0:
        here = int(rows[i][j])
        same = ref[i - 1] == window[j - 1] and ref[i - 1] in "ACGT"
        if here == int(rows[i - 1][j - 1]) + (MATCH if same else MISMATCH):
            matches += same
            i, j = i - 1, j - 1
        elif here == int(rows[i - 1][j]) - GAP:
            i -= 1  # a reference base the record lacks
        else:
            j -= 1  # a record base the reference lacks
        columns += 1
    return matches, columns, i, lo + j


def locus_check(
    record: str,
    reference_amplicons: Sequence[str],
    min_identity: float,
    min_covered: float,
) -> LocusResult:
    """Is any of the assay's reference amplicons in this record, on either strand?

    `record`               the sequence to search, any length.
    `reference_amplicons`  amplicons cut from records the assay detects. Several,
                           because one assay's locus varies across the lineages it
                           covers; the best-scoring one decides.
    `min_identity`         the least share of aligned columns that must match.
    `min_covered`          the least share of the reference the alignment must span.

    Both thresholds are inclusive. With no reference the answer is `ABSENT`: there
    is nothing to define the locus with, and a record must never be counted as a
    failure on a guess.
    """
    record = _clean(record)
    references = [_clean(r) for r in reference_amplicons]
    if not record or not any(references):
        return ABSENT
    rec = np.frombuffer(record.encode("ascii", "replace"), dtype=np.uint8)

    # Every reference on both strands (reverse-complementing the short sequence instead
    # of the long one) proposes stretches of the record to align, each weighted by the
    # words it shares with the reference (`_windows`). A long record keeps the SEED_TOP
    # fullest stretches over ALL the references: with eight references on two strands,
    # twelve stretches for each was 192 alignments a record where a dozen decide it. A
    # short record is one stretch, itself, for each reference and strand, and keeps the
    # WHOLE_TOP fullest of those.
    seeded = len(record) > EXHAUSTIVE_MAX_BP
    codes = _kmer_codes(rec)
    proposals: list[tuple[int, int, str, str, int, int]] = []
    for index, ref in enumerate(references):
        if not ref:
            continue
        for sign, strand in (("+", ref), ("-", _revcomp(ref))):
            spans = _windows(strand, codes, len(record))
            if not seeded:  # the whole record, carrying the weight of its fullest stretch
                spans = [(spans[0][0] if spans else 0, 0, len(record))]
            proposals += [(words, index, sign, strand, lo, hi) for words, lo, hi in spans]
    proposals.sort(key=lambda p: -p[0])  # stable: ties keep reference order
    proposals = proposals[: SEED_TOP if seeded else WHOLE_TOP]
    best: tuple[int, str, int, int, str, int] | None = None
    for _, index, sign, strand, lo, hi in proposals:
        score, i_end, j_end, _ = _sweep(strand, rec[lo:hi], keep=False)
        if score > 0 and (best is None or score > best[0]):
            best = (score, strand, i_end, lo + j_end, sign, index)
    if best is None:
        return ABSENT

    _, ref, i_end, j_end, sign, index = best
    matches, columns, i_start, j_start = _traceback(ref, record, i_end, j_end)
    identity = matches / columns if columns else 0.0
    covered = (i_end - i_start) / len(ref)
    return LocusResult(
        present=identity >= min_identity and covered >= min_covered,
        identity=identity,
        covered=covered,
        # `ref` is already on the strand that matched, so its start is to the LEFT in
        # the record whichever strand that was: the unaligned reference bases before
        # the alignment need that many record bases before it, and likewise after.
        flank_left=j_start - i_start,
        flank_right=(len(record) - j_end) - (len(ref) - i_end),
        strand=sign,
        reference=index,
        ref_start=i_start,
        ref_end=i_end,
    )
