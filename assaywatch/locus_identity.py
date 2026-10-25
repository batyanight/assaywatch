"""Is this amplicon the assay's locus, or two primers that met by chance?

The generalisation of `calls.apply_chance_pair_test` to every chemistry. That test
asks whether the probe site is there, which is a locus-presence signal only an
assay with a probe has - 155 of 209 entries are `conventional` and have none. This
one asks the question the probe was standing in for: does the amplicon's INTERIOR
look like the interiors of the amplicons this assay actually works on?

The records that `detect` certainly carry the locus, so they define it. The test
deliberately ignores the primer sites and reads only what lies between them,
because the primer sites are where all the confounding lives: a chance pair has
primer-shaped matches by construction, and a genuinely divergent real site has
poor ones.

MEASURED 2026-10-25 over `results/2026-10-25/calls.tsv.gz`
(`docs/2026-10-25-locus-identity-design.md`, corrected in
`docs/2026-10-25-stale-orphan-screens.md`):

    ORF_VIRUS ... Zhao 2013      detect 1.00        chance pairs 0.32-0.41
    LYSSAVIRUSES N gene (conv.)  detect 0.86-0.99   no chance pairs; genuine fails 0.86-0.99
    SIV Takehisa (conventional)  detect 0.87-1.00   genuine fails 0.65-0.67

Chance pairs sit at the best-of-many-offsets floor for unrelated DNA. Real loci sit
at 0.65 and above. Nothing sits between 0.41 and 0.65, which is why
`scoring.locus_identity_min` is recommended at 0.50 and why **0.70 is known to be
wrong**: it would delete all 60 of SIV Takehisa's genuinely divergent failures,
and discarding real drift is the failure that killed the two approaches tried
before this one (a `pair_evalue` cut, and Benjamini-Hochberg over pairs - see
`calls.apply_chance_pair_test` for why an E-value cannot do this job).

TWO THINGS IT REFUSES TO DO, both deliberate:

- **It never judges a short amplicon.** `RANAVIRUS_..._MCP_Pallister_2007` is 57 bp
  and leaves 17 bases after the primer trim, too little for an identity to mean
  anything. Below `min_interior_bp` the answer is "unknown", and unknown keeps the
  record evaluable, because that is the status quo and a test that cannot see must
  not remove evidence.
- **It never judges a record against itself**, and never runs at all for an assay
  with no reference. An assay whose records all fail has nothing to define its
  locus with, and inventing one from a failure would make the test agree with
  whatever it was given.
"""

from __future__ import annotations

from typing import Any

#: Bases trimmed from each end of an amplicon before comparing, so that the primer
#: sites cannot contribute to the score. 20 exceeds the longest oligo in the
#: registry. NOT calibrated - see the design doc; too small leaks primer match into
#: the identity and flatters a chance pair, too large loses short amplicons.
TRIM_BP = 20

#: The label a record gets when its amplicon is not this assay's locus. Distinct
#: from `chance_pair` so the two tests stay distinguishable in a report: that one
#: acts on probe absence at report time, this one on sequence at screen time.
LOCUS_MISMATCH = "locus_mismatch"

_COMPLEMENT = str.maketrans("ACGTNRYSWKMBDHV", "TGCANYRSWMKVHDB")


def revcomp(seq: str) -> str:
    return seq.translate(_COMPLEMENT)[::-1]


def interior(amplicon: str, trim: int = TRIM_BP) -> str | None:
    """The amplicon minus `trim` bases at each end, or None if too little is left.

    None means "do not judge this", not "no match": see the module docstring.
    """
    if not amplicon or len(amplicon) <= 2 * trim:
        return None
    return amplicon[trim:-trim].upper()


def identity(query: str, reference: str) -> float:
    """Best ungapped identity of the shorter sequence against the longer, both strands.

    Ungapped on purpose. An alignment that may open gaps will find a respectable
    score between unrelated sequences of this length, which is the opposite of what
    this test needs; the question is whether the same locus is present, not how
    charitably two strings can be lined up.
    """
    if not query or not reference:
        return 0.0
    best = 0.0
    for ref in (reference, revcomp(reference)):
        short, long = (query, ref) if len(query) <= len(ref) else (ref, query)
        for off in range(len(long) - len(short) + 1):
            matches = sum(1 for a, b in zip(short, long[off : off + len(short)], strict=True) if a == b)
            score = matches / len(short)
            if score > best:
                best = score
                if best == 1.0:
                    return best
    return best


def best_identity(
    amplicon: str, references: list[str], trim: int = TRIM_BP, min_interior_bp: int = 30
) -> float | None:
    """How much this amplicon's interior looks like the assay's own, or None if unjudgeable.

    None when the amplicon is too short to leave `min_interior_bp` after trimming,
    or when the assay has no references. The caller must treat None as "keep the
    record", never as a low score.
    """
    if not references:
        return None
    query = interior(amplicon, trim)
    if query is None or len(query) < min_interior_bp:
        return None
    scores = [identity(query, r) for r in references if r]
    return max(scores) if scores else None


def is_locus(
    amplicon: str,
    references: list[str],
    cfg: dict[str, Any],
) -> bool:
    """False only when the amplicon is confidently NOT this assay's locus.

    Off (always True) unless `scoring.locus_identity_min` is set. True whenever the
    answer is unknown, which is the whole safety property: this function may only
    ever remove a record from the denominator on positive evidence that the locus
    is absent.
    """
    s = cfg.get("scoring") or {}
    threshold = s.get("locus_identity_min")
    if threshold is None:
        return True
    score = best_identity(
        amplicon,
        references,
        trim=int(s.get("locus_identity_trim_bp", TRIM_BP)),
        min_interior_bp=int(s.get("locus_identity_min_interior_bp", 30)),
    )
    if score is None:
        return True
    return score >= float(threshold)
