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

COST. One pass is len(reference) numpy sweeps along the record: 0.8 s for a 300 bp
reference against a 200 kb record on both strands (measured 2026-11-10), so
milliseconds for a 10 kb virus and tens of seconds for a 5 Mb bacterial genome, per
reference. A k-mer seed to pick candidate windows
first is the known fix and is not built (ROADMAP, "Coverage map").

NOT YET WIRED IN. Nothing calls this on real records. `coverage._locus_present`
reads a `locus_present` key that a future stage will write from it.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

import numpy as np

MATCH, MISMATCH, GAP = 1, -1, 3  # GAP is a cost: each gapped base subtracts it

_COMPLEMENT = str.maketrans("ACGT", "TGCA")


@dataclass(frozen=True)
class LocusResult:
    """Whether the locus is in the record, and the two numbers that decided it."""

    present: bool
    identity: float  # share of aligned columns that match
    covered: float  # share of the reference amplicon the alignment spans


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


def _traceback(reference: str, record: str, i_end: int, j_end: int) -> tuple[int, int, int]:
    """Walk the best alignment backwards. Returns (matches, columns, reference start).

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
    return matches, columns, i


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
    references = [_clean(r) for r in reference_amplicons if r]
    if not record or not references:
        return ABSENT
    rec = np.frombuffer(record.encode("ascii", "replace"), dtype=np.uint8)

    # Search with the reference on both strands (reverse-complementing the short
    # sequence instead of the long one), and trace back only the single best.
    best: tuple[int, str, int, int] | None = None
    for ref in references:
        for strand in (ref, _revcomp(ref)):
            score, i_end, j_end, _ = _sweep(strand, rec, keep=False)
            if score > 0 and (best is None or score > best[0]):
                best = (score, strand, i_end, j_end)
    if best is None:
        return ABSENT

    _, ref, i_end, j_end = best
    matches, columns, i_start = _traceback(ref, record, i_end, j_end)
    identity = matches / columns if columns else 0.0
    covered = (i_end - i_start) / len(ref)
    return LocusResult(identity >= min_identity and covered >= min_covered, identity, covered)
