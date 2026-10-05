"""Find where an oligo could bind in a target record, with mismatches.

The search is exact: every ungapped position in the record is considered, on
both strands, and a site is reported whenever at most `max_mismatches`
positions of the oligo fail to match definitely. Record positions whose true
base is not determined (an ambiguity code the oligo only partly covers, or an
N) are reported separately as `ambiguous` and never scored as mismatches; see
iupac.base_state for why.

They do, however, count against the search budget. Finding a candidate site
and scoring it are different questions: scoring asks what an undetermined base
costs (nothing), finding asks whether this stretch of record shows any
evidence of a binding site at all, and a window of Ns shows none. Without
this rule every offset in a scaffold gap is a perfect site for every oligo,
and the pairing step in score.py goes cubic: the first live run spent nine
hours on the Bd archive, whose whole-genome scaffolds carry kilobase N-gaps.
A site with a few undetermined bases is still found, and is called
`indeterminate` by the scorer if there are too many to judge. There is no position at which a
mismatch can hide the site. Gaps are not modelled, which is deliberate: a
primer binding site with an indel in it is not a working primer site, and
treating it as one would invent amplicons that do not exist.

The scan is vectorised. For each of the oligo's positions a 256-entry lookup
table maps a record byte to one of three states (_match_tables). Only one
number decides whether an offset is a candidate site, the count of positions
that are not a definite match, so the search counts just that, in two stages:

1. Dense. Record bytes fall into 16 classes by the base set they stand for, so
   four consecutive record positions pack into one 16-bit code, and a
   65,536-entry table per block of four oligo positions gives that block's
   not-match count. Four such blocks (16 positions) are summed over every
   offset in a few numpy passes, most selective blocks first.
2. Sparse. The count only grows, so offsets already over budget are dropped,
   and the remaining positions are added only for the offsets still in it.

The surviving offsets are then revisited in Python to recover which positions
were mismatches and which undetermined. Every offset is still evaluated: the
pruning removes only offsets whose count already exceeds the budget, so the
result is exactly the exhaustive one (held to brute force in tests). This is
about 5x faster than adding all L positions at every offset, which it replaced.

find_sites prepares a record once (uppercase, reverse complement, packed codes)
and remembers each oligo's sites for it, so the several oligos and assays
screened against one record, back to back, share that work.

An earlier version used two fixed k-mer seeds, one at each end of the oligo,
and missed any site whose mismatches fell inside both seeds: a 15 nt probe
edited at its centre had no clean 8-mer anywhere and vanished, and the record
was miscounted as no_amplicon instead of being scored. Seeding schemes can be
made exact (split the oligo into max_mismatches + 1 chunks and at least one
must match exactly, by the pigeonhole principle), but at a 6-mismatch budget
those chunks are 3 to 4 nt and match everywhere, so the filter earns nothing
over scanning. The exhaustive scan is both correct and fast enough; see
tests/test_match.py, which holds it to a brute-force implementation.

Phase 2 can swap in parasail for gapped local alignment without changing this
interface; `find_sites` returning a list of `Site` is the contract.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

import numpy as np

from assaywatch.iupac import IUPAC, WEAK_PAIRS, reverse_complement


@dataclass(frozen=True)
class Site:
    """One place an oligo could bind.

    start/end are 0-based, half-open, on the record's plus strand.
    strand is '+' if the oligo sequence itself matches the plus strand (a
    forward primer binding site) and '-' if its reverse complement does
    (a reverse primer binding site).
    mismatches are 0-based positions counted from the oligo's own 5' end, so
    position len(oligo)-1 is always the 3'-terminal base on either strand.
    ambiguous are positions where the record's base is not determined; they are
    not mismatches and carry no penalty.
    window is the record's bases oriented 5'->3' like the oligo, for reports.
    """

    start: int
    end: int
    strand: str
    mismatches: tuple[int, ...]
    window: str
    ambiguous: tuple[int, ...] = ()

    @property
    def n_mismatches(self) -> int:
        return len(self.mismatches)

    @property
    def n_ambiguous(self) -> int:
        return len(self.ambiguous)


# Table values. Kept as module constants so score.py and the tests can refer
# to the same encoding rather than to bare integers.
MISMATCH, MATCH, UNKNOWN = 0, 1, 2


@lru_cache(maxsize=512)
def _match_tables(oligo: str) -> tuple[np.ndarray, ...]:
    """Per oligo position, a 256-entry uint8 table of MISMATCH / MATCH / UNKNOWN.

    This is iupac.base_state compiled into an array for speed; a test holds the
    two to each other for every pair of IUPAC codes.
    """
    tables = []
    for code in oligo:
        allowed = set(IUPAC[code])
        weak = set(WEAK_PAIRS.get(code, ""))
        row = np.zeros(256, dtype=np.uint8)  # unlisted bytes stay MISMATCH
        for rb, rbases in IUPAC.items():
            bases = set(rbases)
            if bases <= allowed:
                state = MATCH
            elif bases & allowed or bases & weak:
                state = UNKNOWN
            else:
                state = MISMATCH
            row[ord(rb)] = state
            row[ord(rb.lower())] = state
        tables.append(row)
    return tuple(tables)


def _byte_classes() -> tuple[np.ndarray, np.ndarray]:
    """Record byte -> one of 16 classes by the base set it stands for (U=T, I=H, 15 = non-IUPAC).
    Every _match_tables row is constant within a class, so 4 classes fit one 16-bit index."""
    cls = np.full(256, 15, dtype=np.uint8)
    ids: dict[frozenset, int] = {}
    for code, bases in IUPAC.items():
        k = ids.setdefault(frozenset(bases), len(ids))
        cls[ord(code)] = cls[ord(code.lower())] = k
    rep = np.zeros(16, dtype=np.uint8)  # one byte standing for each class
    for b in range(255, -1, -1):
        rep[cls[b]] = b
    return cls, rep


_CLS, _REP = _byte_classes()


def _quad_codes(rec: np.ndarray) -> np.ndarray:
    """code[k] = classes of rec[k..k+3] packed 4 bits each."""
    c = _CLS[rec].astype(np.uint16)
    n = max(len(c) - 3, 0)
    return c[:n] | c[1 : n + 1] << 4 | c[2 : n + 2] << 8 | c[3 : n + 3] << 12


@lru_cache(maxsize=512)
def _scan_plan(oligo: str):
    """65536-entry tables giving the not-MATCH count of each 4-position block,
    most selective block first, and the per-position 0/1 tables for the rest.

    Cached per oligo, because building the block tables costs more than scanning
    a short record with them.
    """
    tables = _match_tables(oligo)
    # nm[i][byte] is 1 when oligo position i does NOT definitely match that byte.
    # One number per position is enough here: the search only needs the count of
    # positions that fail, and mismatch-versus-undetermined is recovered later,
    # at the few offsets that survive.
    nm = [(t != MATCH).astype(np.uint8) for t in tables]
    acgt = np.frombuffer(b"ACGT", np.uint8)
    ix = np.arange(65536)  # every possible packed code for four record positions
    quads = sorted(
        (
            # For block starting at i: a table whose entry for a packed code is
            # the block's total failure count. `ix >> 4*j & 15` unpacks class j
            # from the code, and _REP maps that class back to a representative
            # byte so the per-position table can be indexed by it.
            (i, sum(nm[i + j][_REP][(ix >> 4 * j) & 15] for j in range(4)).astype(np.uint8))
            for i in range(0, len(oligo) - 3, 4)
        ),
        # Most selective block first: a block that rejects the most random
        # sequence prunes the candidate list fastest. Summing nm over A, C, G, T
        # measures that — a fully degenerate position contributes 0.
        key=lambda q: -sum(int(nm[q[0] + j][acgt].sum()) for j in range(4)),
    )
    # Same ordering for the leftover single positions used in the sparse pass.
    singles = sorted(range(len(oligo)), key=lambda i: -int(nm[i][acgt].sum()))
    return tables, nm, quads, singles


def _search_one_strand(oligo: str, rec: np.ndarray, codes: np.ndarray, max_mm: int):
    """{start: (mismatch positions, ambiguous positions)} in one orientation.

    Every offset is evaluated. The not-MATCH count only grows with each position,
    so after a few dense 4-position blocks the offsets still within budget are
    followed sparsely; the order in which positions are added changes nothing.
    """
    L, N = len(oligo), len(rec)
    if N < L:
        return {}
    n = N - L + 1  # every alignment offset of the oligo against the record
    tables, nm, quads, singles = _scan_plan(oligo)

    # Dense pass: add whole 4-position blocks over every offset at once. Enough
    # blocks to exceed the budget comfortably — past that, pruning is cheaper
    # than another full-length pass.
    dense = quads[: (max_mm + 10) // 4]
    cnt = np.zeros(n, dtype=np.uint8)  # safe: oligos are capped well under 255 nt
    done = set()
    for i, t in dense:
        # codes[i : i + n] is the packed code of the four record positions facing
        # oligo position i, for every offset. One table lookup scores them all.
        cnt += t[codes[i : i + n]]
        done.update(range(i, i + 4))

    # Sparse pass: a count only grows as positions are added, so an offset
    # already over budget can never come back, and the rest of the oligo is
    # scored only for the survivors. This is what makes the search fast without
    # making it approximate — nothing within budget is ever discarded.
    cand = np.flatnonzero(cnt <= max_mm)
    c = cnt[cand]
    for i in singles:
        if i in done or not len(cand):
            continue
        c += nm[i][rec[cand + i]]
        keep = c <= max_mm
        cand, c = cand[keep], c[keep]

    # Only now, for the handful of surviving offsets, is it worth separating a
    # definite mismatch from an undetermined record base — the scorer charges
    # for one and not the other.
    hits = {}
    for start in cand.tolist():
        window = rec[start : start + L]
        states = [int(table[window[i]]) for i, table in enumerate(tables)]
        hits[start] = (
            tuple(i for i, st in enumerate(states) if st == MISMATCH),
            tuple(i for i, st in enumerate(states) if st == UNKNOWN),
        )
    return hits


# One record's prepared forms, reused across every oligo and assay screened
# against it. Screening runs record-outer (see screen._screen_batch), so this
# single slot is hit repeatedly before moving on; a bigger cache would hold
# whole genomes alive for no gain. Keyed on object identity, not content.
_LAST: list = [None, None]


def _prepare(record: str):
    if _LAST[0] is not record:
        up, rc = record.upper(), reverse_complement(record)
        a = np.frombuffer(up.encode("ascii", "replace"), dtype=np.uint8)
        b = np.frombuffer(rc.encode("ascii", "replace"), dtype=np.uint8)
        _LAST[:] = record, (up, a, _quad_codes(a), rc, b, _quad_codes(b), {})
    return _LAST[1]


def find_sites(oligo: str, record: str, max_mismatches: int = 6) -> list[Site]:
    """Every site with <= max_mismatches positions not definitely matched, either strand.

    The result is exhaustive within the mismatch budget: raising
    `max_mismatches` can only add sites, never move or remove one.
    """
    oligo = oligo.upper()
    up, a, qa, rc, b, qb, memo = _prepare(record)
    key = (oligo, max_mismatches)
    if key not in memo:
        L, n = len(oligo), len(up)
        sites = [
            Site(s, s + L, "+", mm, up[s : s + L], amb)
            for s, (mm, amb) in _search_one_strand(oligo, a, qa, max_mismatches).items()
        ]
        # A window at [s, s+L) on the reverse complement sits at [n-s-L, n-s) on the plus strand.
        sites += [
            Site(n - s - L, n - s, "-", mm, rc[s : s + L], amb)
            for s, (mm, amb) in _search_one_strand(oligo, b, qb, max_mismatches).items()
        ]
        memo[key] = sorted(sites, key=lambda x: (x.start, x.strand))
    return list(memo[key])
