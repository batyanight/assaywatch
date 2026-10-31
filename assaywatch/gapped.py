"""Gapped oligo search, for measuring how much indels matter. Never used in scoring.

match.py is ungapped on purpose: a primer site with an indel in it is not a
working primer site. Whether that choice hides anything is an empirical
question, and this module exists to answer it (scripts/indel_check.py): how
many `fail` and `no_amplicon` calls would look different if a gap were allowed.

Costs are unit edit costs. A definite mismatch, an insertion and a deletion each
cost 1. An undetermined record base (iupac `unknown`) also costs 1 here, unlike
in scoring: the question is whether a clean binding site is hiding behind an
indel, and a run of Ns is not evidence of one.

`scan` is semi-global (the whole oligo, any stretch of the record) and runs in
O(len(oligo)) numpy passes over the record. Row i of the DP is

    V[j]  = min(D[i-1][j-1] + cost(i, j), D[i-1][j] + 1)
    D[i][j] = min over k <= j of (V[k] + (j - k))
            = j + cummin(V[k] - k)

so the only sequential step, the run of insertions along the record, becomes a
running minimum. `align` does the same DP in Python with a traceback, for a
short window around one site.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from assaywatch.match import MATCH, _match_tables


def _cost_rows(oligo: str, rec: np.ndarray) -> list[np.ndarray]:
    """Per oligo position, 0 where the record base definitely matches, else 1."""
    return [(table[rec] != MATCH).astype(np.int32) for table in _match_tables(oligo.upper())]


def scan(oligo: str, seq: str) -> np.ndarray:
    """best[j] = lowest edit cost of the whole oligo against a record stretch ending at j.

    j runs over 0..len(seq) as an exclusive end position.
    """
    rec = np.frombuffer(seq.upper().encode("ascii", "replace"), dtype=np.uint8)
    n = len(rec)
    idx = np.arange(n + 1, dtype=np.int32)
    prev = np.zeros(n + 1, dtype=np.int32)  # free start anywhere in the record
    for i, cost in enumerate(_cost_rows(oligo, rec), start=1):
        v = np.empty(n + 1, dtype=np.int32)
        v[0] = i
        v[1:] = np.minimum(prev[:-1] + cost, prev[1:] + 1)
        prev = idx + np.minimum.accumulate(v - idx)
    return prev


def hamming_scan(oligo: str, seq: str) -> np.ndarray:
    """Ungapped cost at every start offset, with the same cost rule as `scan`."""
    rec = np.frombuffer(seq.upper().encode("ascii", "replace"), dtype=np.uint8)
    L, n = len(oligo), len(rec)
    if n < L:
        return np.zeros(0, dtype=np.int32)
    out = np.zeros(n - L + 1, dtype=np.int32)
    for i, cost in enumerate(_cost_rows(oligo, rec)):
        out += cost[i : i + n - L + 1]
    return out


@dataclass(frozen=True)
class Alignment:
    """Best gapped placement of an oligo in a window.

    start/end are 0-based, half-open, in window coordinates. mismatches and
    indels are positions counted from the oligo's 3' end (1 = terminal base);
    an insertion in the record sits between two oligo bases and is labelled
    with the oligo base on its 5' side.
    """

    cost: int
    start: int
    end: int
    mismatches: tuple[int, ...]
    insertions: tuple[int, ...]  # extra record bases
    deletions: tuple[int, ...]  # oligo bases with no record base

    @property
    def n_indels(self) -> int:
        return len(self.insertions) + len(self.deletions)


def align(oligo: str, window: str) -> Alignment:
    """Best semi-global alignment of `oligo` in `window`, with a traceback.

    Ties go to the alignment with fewer indels, so an ungapped site that is as
    good as any gapped one is reported as ungapped.
    """
    oligo = oligo.upper()
    rec = np.frombuffer(window.upper().encode("ascii", "replace"), dtype=np.uint8)
    L, n = len(oligo), len(rec)
    cost = [c.tolist() for c in _cost_rows(oligo, rec)]
    # Each cell holds (edit cost, indels) so ties can be broken toward fewer gaps.
    INF = (10**9, 0)
    D = [[(0, 0)] * (n + 1)] + [[INF] * (n + 1) for _ in range(L)]
    for i in range(1, L + 1):
        D[i][0] = (i, i)
        row, up = D[i], D[i - 1]
        ci = cost[i - 1]
        for j in range(1, n + 1):
            d, u, lft = up[j - 1], up[j], row[j - 1]
            row[j] = min((d[0] + ci[j - 1], d[1]), (u[0] + 1, u[1] + 1), (lft[0] + 1, lft[1] + 1))
    end = min(range(n + 1), key=lambda j: (D[L][j], j))
    total = D[L][end][0]

    mism, ins, dele = [], [], []
    i, j = L, end
    while i > 0:
        here = D[i][j]
        from3 = L - i + 1
        if j > 0 and here == (D[i - 1][j - 1][0] + cost[i - 1][j - 1], D[i - 1][j - 1][1]):
            if cost[i - 1][j - 1]:
                mism.append(from3)
            i, j = i - 1, j - 1
        elif here == (D[i - 1][j][0] + 1, D[i - 1][j][1] + 1):
            dele.append(from3)
            i -= 1
        else:
            ins.append(from3)
            j -= 1
    return Alignment(total, j, end, tuple(sorted(mism)), tuple(sorted(ins)), tuple(sorted(dele)))
