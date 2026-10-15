"""Where an assay's primers could build an amplicon in one sequence.

Shared by the assembly pre-cut (`assemblies.extract_loci`) and the distributable window
archives (`windows`). Kept in its own module, importing only `chance` and `match`, so
that the screener can depend on the window format without depending on retrieval.
"""

from __future__ import annotations

from typing import Any

from assaywatch.chance import composition, pair_evalue
from assaywatch.match import find_sites


def pair_spans(
    seq: str,
    pairs: list[tuple[str, str]],
    cfg: dict[str, Any],
    max_mm: int,
    max_e: float,
    lo_bp: int,
    hi_bp: int,
) -> list[tuple[int, int]]:
    """0-based half-open spans of every amplicon the screener could build in `seq`.

    Forward and reverse sites facing each other on opposite strands (either
    orientation), `lo_bp`-`hi_bp` apart, each within `max_mm` mismatches, and the pair's
    chance E-value at most `max_e` in a record of this length and composition. Every
    such pair, not only the best: the cut around them must hold whichever one a later
    screen picks. Shared by the assembly pre-cut and the distributable window archives.
    """
    comp = composition(seq)
    sites: dict[str, dict[str, list]] = {}

    def on(oligo: str, strand: str) -> list:
        # find_sites scans both strands at once; do it once per oligo.
        if oligo not in sites:
            found = find_sites(oligo, seq, max_mm)
            sites[oligo] = {st: [x for x in found if x.strand == st] for st in "+-"}
        return sites[oligo][strand]

    spans = []
    for fwd, rev in pairs:
        # Both orientations, as in score.screen_record: the locus may sit on either strand.
        for f_strand, r_strand in (("+", "-"), ("-", "+")):
            r_sites = on(rev, r_strand)
            if not r_sites:
                continue
            for f in on(fwd, f_strand):
                for r in r_sites:
                    lo, hi = (f.start, r.end) if f_strand == "+" else (r.start, f.end)
                    facing = r.start > f.start if f_strand == "+" else f.start > r.start
                    if not (facing and lo_bp <= hi - lo <= hi_bp):
                        continue
                    e = pair_evalue(
                        fwd,
                        rev,
                        f.n_mismatches + f.n_ambiguous,
                        r.n_mismatches + r.n_ambiguous,
                        len(seq),
                        cfg,
                        comp,
                    )
                    if e <= max_e:
                        spans.append((lo, hi))
    return spans
