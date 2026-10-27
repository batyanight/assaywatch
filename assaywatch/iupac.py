"""Sequence helpers the matcher will need: IUPAC expansion, complement, matching.

Kept dependency-free and tiny so the scoring rules can be unit-tested with
known answers before any alignment library is involved.
"""

from __future__ import annotations

import itertools

IUPAC: dict[str, str] = {
    "A": "A",
    "C": "C",
    "G": "G",
    "T": "T",
    "U": "T",
    "R": "AG",
    "Y": "CT",
    "S": "CG",
    "W": "AT",
    "K": "GT",
    "M": "AC",
    "B": "CGT",
    "D": "AGT",
    "H": "ACT",
    "V": "ACG",
    "N": "ACGT",
    # Inosine is a single nucleotide that pairs promiscuously, not a mixture.
    # The pairing order is I:C > I:A > I:T > I:G (Martin et al. 1985, Nucleic
    # Acids Res 13:8927, doi:10.1093/nar/13.24.8927, the paper that introduced
    # inosine for probe design; the nearest-neighbour measurements in Watkins &
    # SantaLucia 2005, doi:10.1093/nar/gki918, put dI:dC near a normal A:T pair
    # and dI:dG a full ~3 kcal/mol worse). So I:C/I:A/I:T are listed as pairs
    # here and I:G is demoted to a weak pair below. Inosine is excluded from
    # degeneracy counting because an inosine-containing oligo is one molecule,
    # not 3^n — it pays no concentration cost, which is why designers use it.
    # Records never contain I.
    "I": "ACT",
}

# The inverse of IUPAC: a frozenset of bases -> the single code that stands for
# exactly those. Built from IUPAC so the two can never disagree, and restricted
# to the eleven true degeneracy codes: "U" is dropped so a set resolves to "T",
# and "I" is dropped because inosine is one molecule that pairs promiscuously,
# not a mixture, so it is never the right answer to "which code covers these
# bases". Used to name the replacement base when a primer position has drifted:
# given the oligo's base and the bases the records actually carry, the code
# covering the union is what you would order.
CODE_FOR: dict[frozenset[str], str] = {}
for _code, _bases in IUPAC.items():
    if _code in ("U", "I"):
        continue
    CODE_FOR.setdefault(frozenset(_bases), _code)
del _code, _bases


def code_for(bases) -> str | None:
    """The IUPAC code covering exactly *bases*, or None if there is not one.

    None rather than "N" for an uncoverable set: anything containing a base
    outside ACGT (an ambiguous record position, say) has no honest code, and
    silently widening it to N would read as a recommendation to order a fully
    degenerate position.
    """
    want = frozenset(b.upper() for b in bases)
    return CODE_FOR.get(want) if want <= frozenset("ACGT") else None


# Pairings that are real but poor. A weak pair reports as `unknown`: neither
# evidence that the oligo binds nor evidence that the target has drifted. I:G is
# the only entry: it forms, so calling it a mismatch would assert drift that may
# not exist, but it is destabilising enough (Watkins & SantaLucia 2005) that
# calling it a match would assert binding we cannot support either.
WEAK_PAIRS: dict[str, str] = {"I": "G"}

# Codes standing for one physical molecule, however many bases they pair with.
SINGLE_MOLECULE = frozenset("ACGTUI")

COMPLEMENT: dict[str, str] = {
    "A": "T",
    "C": "G",
    "G": "C",
    "T": "A",
    "U": "A",
    "R": "Y",
    "Y": "R",
    "S": "S",
    "W": "W",
    "K": "M",
    "M": "K",
    "B": "V",
    "V": "B",
    "D": "H",
    "H": "D",
    "N": "N",
    "I": "I",  # no Watson-Crick complement; reverse-complementing an inosine
    # oligo is not meaningful, but the identity keeps the operation total.
}


# str.translate table for reverse_complement. Characters outside IUPAC (a gap
# '-', '*', 'X', digits, stray spaces in a submitter's FASTA) map to themselves:
# the matcher's lookup tables already score any unlisted byte as a mismatch, so
# they need no special case, and one odd record must not crash a whole archive.
_RC_TABLE = str.maketrans(
    "".join(COMPLEMENT) + "".join(COMPLEMENT).lower(),
    "".join(COMPLEMENT.values()) + "".join(COMPLEMENT.values()),
)


def reverse_complement(seq: str) -> str:
    """Reverse complement, uppercased. Twenty times faster than a per-base dict lookup on a genome."""
    return seq[::-1].translate(_RC_TABLE).upper()


def degeneracy(seq: str) -> int:
    """How many distinct oligos this sequence stands for, i.e. the pool size.

    This is a count of molecules, not of pairing options, so inosine counts as
    one. Writing I as N (which the registry's `seq` field does, to keep that
    field strict IUPAC) and then counting degeneracy from it would inflate a
    7-inosine primer by 4^7; use `seq_as_written` where it exists.
    """
    n = 1
    for b in seq.upper():
        if b not in SINGLE_MOLECULE:
            n *= len(IUPAC[b])
    return n


def expand(seq: str, limit: int = 4096) -> list[str]:
    """All non-degenerate sequences covered by `seq`. Refuses absurd expansions."""
    # Count expansions, not molecules: inosine is one molecule but expands to three bases here.
    n = 1
    for b in seq.upper():
        n *= len(IUPAC[b])
    if n > limit:
        raise ValueError(f"{seq} expands to {n} sequences (> {limit})")
    return ["".join(p) for p in itertools.product(*(IUPAC[b] for b in seq.upper()))]


MATCH, MISMATCH, UNKNOWN = "match", "mismatch", "unknown"


def base_state(oligo_base: str, target_base: str) -> str:
    """Compare one oligo base to one record base. Three outcomes, not two.

    A record base is often an ambiguity code rather than a single base, because
    the record is a Sanger consensus or a low-coverage assembly. Those codes
    carry three different meanings and must not be collapsed:

      match     every base the record code stands for is covered by the oligo.
                Primer Y against a record C or T is a match and costs nothing;
                degeneracy in the primer is what the primer is for.
      mismatch  the record code and the oligo code share no base at all, so
                whatever the true base is, the primer does not bind it.
                Primer A against a record S (C or G) is a real mismatch.
      unknown   they overlap but the record code is not fully covered, so the
                true base may or may not match. Primer A against a record R
                (A or G) is unknown, and so is anything against an N.

    Treating `unknown` as a mismatch is what penalises degenerate assays: the
    pan-family primers that need degeneracy target exactly the sparsely and
    poorly sequenced taxa whose records are full of ambiguity codes, so the
    assay gets charged for the submitter's sequencing quality and real drift
    becomes indistinguishable from missing information. The scorer therefore
    charges nothing for `unknown` and counts it separately; see score.py.
    """
    ob = oligo_base.upper()
    o = set(IUPAC[ob])
    t = set(IUPAC.get(target_base.upper(), ""))
    if not t:
        return MISMATCH  # a gap or junk character, not a base
    if t <= o:
        return MATCH
    if t & o:
        return UNKNOWN
    if t & set(WEAK_PAIRS.get(ob, "")):
        return UNKNOWN  # a real but poor pair, e.g. inosine opposite G
    return MISMATCH


def base_matches(oligo_base: str, target_base: str) -> bool:
    """True only for a definite match. `unknown` is not a match."""
    return base_state(oligo_base, target_base) == MATCH


def compare(oligo: str, target: str) -> tuple[list[int], list[int]]:
    """(mismatch positions, unknown positions), 0-based from the oligo's 5' end."""
    if len(oligo) != len(target):
        raise ValueError("oligo and target window must be the same length")
    mm, amb = [], []
    for i, (o, t) in enumerate(zip(oligo, target, strict=True)):
        state = base_state(o, t)
        if state == MISMATCH:
            mm.append(i)
        elif state == UNKNOWN:
            amb.append(i)
    return mm, amb


def mismatch_positions(oligo: str, target: str) -> list[int]:
    """Definite mismatches only. Ambiguous record bases are not counted here."""
    return compare(oligo, target)[0]
