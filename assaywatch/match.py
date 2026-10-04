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
table maps a record byte to one of three states; applying the table to the
record as a numpy array gives, in one C-level pass per oligo position, the
state at every alignment offset at once. Summing those L arrays gives the
mismatch and ambiguity counts at every offset, and only the offsets within
budget are revisited in Python to recover which positions were which. Cost is
O(len(oligo) x len(record)) element operations, but they happen inside numpy,
so a 25 nt oligo against a 30 kb record takes a couple of milliseconds.

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


def _search_one_strand(
    oligo: str, seq: str, max_mm: int
) -> dict[int, tuple[tuple[int, ...], tuple[int, ...]]]:
    """{start: (mismatch positions, ambiguous positions)} in one orientation.

    Every offset is evaluated; nothing is filtered out beforehand.
    """
    L, N = len(oligo), len(seq)
    if N < L:
        return {}
    tables = _match_tables(oligo)
    rec = np.frombuffer(seq.encode("ascii", "replace"), dtype=np.uint8)
    n_windows = N - L + 1

    mm_counts = np.zeros(n_windows, dtype=np.int16)
    amb_counts = np.zeros(n_windows, dtype=np.int16)
    for i, table in enumerate(tables):
        states = table[rec[i : i + n_windows]]
        mm_counts += states == MISMATCH
        amb_counts += states == UNKNOWN

    hits = {}
    # Undetermined positions consume the search budget (see module docstring);
    # they are still reported separately so the scorer charges nothing for them.
    for start in np.flatnonzero(mm_counts + amb_counts <= max_mm):
        start = int(start)
        window = rec[start : start + L]
        states = [int(table[window[i]]) for i, table in enumerate(tables)]
        hits[start] = (
            tuple(i for i, st in enumerate(states) if st == MISMATCH),
            tuple(i for i, st in enumerate(states) if st == UNKNOWN),
        )
    return hits


def find_sites(oligo: str, record: str, max_mismatches: int = 6) -> list[Site]:
    """Every site with <= max_mismatches positions not definitely matched, either strand.

    The result is exhaustive within the mismatch budget: raising
    `max_mismatches` can only add sites, never move or remove one.
    """
    oligo = oligo.upper()
    record = record.upper()
    L = len(oligo)
    sites: list[Site] = []

    for start, (mm, amb) in _search_one_strand(oligo, record, max_mismatches).items():
        sites.append(Site(start, start + L, "+", mm, record[start : start + L], amb))

    rc = reverse_complement(record)
    n = len(record)
    for start_rc, (mm, amb) in _search_one_strand(oligo, rc, max_mismatches).items():
        # A window at [s, s+L) on the reverse complement sits at [n-s-L, n-s) on the plus strand.
        start = n - start_rc - L
        sites.append(Site(start, start + L, "-", mm, rc[start_rc : start_rc + L], amb))

    return sorted(sites, key=lambda s: (s.start, s.strand))
