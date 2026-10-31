"""Duplex melting temperature of each oligo on its actual binding site. Never scored.

The mismatch penalty in score.py is a positional rule of thumb. What a mismatch
does to binding depends on which mismatch it is and what surrounds it: a G:T
wobble in a GC-rich stretch costs a degree, an A:C next to the 3' end can cost
ten. This module puts a number on that with a nearest-neighbour model
(SantaLucia & Hicks 2004, with the Allawi/SantaLucia mismatch parameters), as an
extra column beside the call, the same way degeneracy rides along: shown, never
folded into the call.

THE REGISTER IS THE WHOLE POINT, and it is why this does not use
`primer3.calc_heterodimer`. That function returns the MOST STABLE structure
between two sequences, which on a heavily mismatched site is a shifted, shorter,
near-perfect duplex -- so it reports an optimistically small |ΔTm| exactly where
the mismatches are worst, which is exactly the record the report is about. It was
measured on 2026-10-27: 99 of 179 bench rows came back out of register, a
majority, and because the bench panels are band-heavy (122 of 179) an
optimistic predictor is flattered by them, so part of primer3's measured
advantage over the penalty rule may be this artefact rather than thermodynamics
(docs/journal/2026-10-27-thermo-vs-penalty-paired.md).

Biopython's `MeltingTemp.Tm_NN` takes the alignment as given -- it walks the two
strands position by position and sums the nearest-neighbour terms, using the
internal-mismatch and terminal-mismatch tables where a pair is not Watson-Crick.
There is no search, so there is no register to get wrong. The two engines agree
to about a degree where primer3 does align in register (63.45 against 62.42 on a
perfect 21-mer; 49.81 against 49.49 with two internal mismatches), so this is a
change of register and not of scale. primer3-py stays a dependency: `screen.py`
uses it elsewhere.

For each oligo of an amplicon it reports

    <oligo>_tm    Tm (deg C) of the oligo on the record's site
    <oligo>_dtm   that Tm minus the Tm of the same oligo on a perfect site

and `thermo_min_dtm`, the worst ΔTm across the assay's oligos. ΔTm is the
useful number: absolute Tm depends on salt, Mg2+ and oligo concentration,
which vary between protocols and are set once in config.yaml, while the shift
caused by the record's mismatches is much less sensitive to them.

Which sequence is modelled
--------------------------
primer3 needs concrete bases on both strands, so the IUPAC codes are resolved
position by position, in the same spirit as the scorer:

* A degenerate oligo position becomes the record's base when the pool contains
  it. The pool member that fits a record best is the one that amplifies it, so
  that is the molecule whose Tm matters. When the record's base is outside the
  pool, the first pool base is used and the mismatch stays a mismatch.
* An undetermined record base (an ambiguity code or N) becomes the oligo's
  base. It is not evidence of a mismatch, so it is not modelled as one.
* Inosine has no nearest-neighbour parameters in primer3. It is modelled as the
  base it faces (or A if that is undetermined), which overstates stability:
  real inosine pairs are weaker than Watson-Crick pairs. `thermo_note` says
  `inosine` on any row where this was done, so those Tm values can be read as
  an upper bound.
"""

from __future__ import annotations

from types import ModuleType
from typing import TYPE_CHECKING, Any

from assaywatch.iupac import IUPAC

if TYPE_CHECKING:
    from assaywatch.score import Call

COLUMNS = (
    "fwd_tm",
    "fwd_dtm",
    "rev_tm",
    "rev_dtm",
    "probe_tm",
    "probe_dtm",
    "thermo_min_dtm",
    "thermo_note",
)

DEFAULTS = {"mv_conc": 50.0, "dv_conc": 3.0, "dntp_conc": 0.8, "dna_conc": 250.0}


def _melting_temp() -> ModuleType:
    try:
        from Bio.SeqUtils import MeltingTemp
    except ImportError as e:  # pragma: no cover - depends on the environment
        raise SystemExit(
            "thermodynamic columns need biopython: conda install -c conda-forge biopython"
        ) from e
    return MeltingTemp


#: Salt correction 5 is Owczarzy et al. 2008, the one of Biopython's seven that
#: accounts for Mg2+ and dNTPs rather than monovalent salt alone. A PCR buffer is
#: Mg-dominated, so the alternatives would price the wrong ion.
SALT_CORRECTION = 5


def resolve(oligo: str, site: str) -> tuple[str, str, bool]:
    """(oligo bases, record bases, used inosine) with every IUPAC code made concrete.

    `site` is the record's bases oriented 5'->3' like the oligo (Site.window), so
    position i of each is the same position of the duplex.
    """
    o_out, t_out, inosine = [], [], False
    for o, t in zip(oligo.upper(), site.upper(), strict=True):
        pool = IUPAC.get(o, "ACGT")
        if t not in IUPAC:
            # Not a base at all ('-', '*', 'X'): the matcher scores it as a
            # mismatch, so model it as one rather than as a perfect pair.
            ob = pool[0]
            o_out.append(ob)
            t_out.append("C" if ob == "A" else "A")
            continue
        t_set = IUPAC[t]  # U reads as T
        if o == "I":
            inosine = True
            base = t_set if len(t_set) == 1 else "A"
            o_out.append(base)
            t_out.append(base)
            continue
        ob = t_set if len(t_set) == 1 and t_set in pool else pool[0]
        o_out.append(ob)
        t_out.append(t_set if len(t_set) == 1 else ob)
    return "".join(o_out), "".join(t_out), inosine


def _in_register_tm(oligo: str, template: str, cond: dict[str, float]) -> float | None:
    """Tm of `oligo` paired base-for-base with `template`, no alignment search.

    `template` is the same-sense strand, so the oligo's actual partner is its
    complement -- which is what `c_seq` wants: the complement positionally
    aligned with `seq`, NOT the reverse complement.

    None when the model cannot do the arithmetic. The mismatch tables are
    published for a mismatch FLANKED BY MATCHES (Allawi & SantaLucia), and two
    ADJACENT mismatches have no measured nearest-neighbour term -- Biopython
    raises on, say, `GC/TT`. Biopython will silently drop the unknown term if
    asked (`strict=False`), and dropping it means scoring that step as costing
    nothing, which overstates stability on precisely the most mismatched sites.
    That is the same optimism in the same place as the registration bug this
    function exists to remove, so the number is withheld instead and
    `thermo_note` says `nn_unsupported`.
    """
    mt = _melting_temp()
    tables = {
        "nn_table": mt.DNA_NN3,  # SantaLucia & Hicks 2004
        "imm_table": mt.DNA_IMM1,  # internal mismatches and inosine pairs
        "tmm_table": mt.DNA_TMM1,  # a mismatch at either terminus
        "de_table": mt.DNA_DE1,  # dangling ends; unused at equal lengths
    }
    salt = {
        "Na": cond["mv_conc"],
        "Mg": cond["dv_conc"],
        "dNTPs": cond["dntp_conc"],
        "dnac1": cond["dna_conc"],
        "dnac2": cond["dna_conc"],
        "saltcorr": SALT_CORRECTION,
    }
    try:
        return float(mt.Tm_NN(oligo, c_seq=template.translate(_COMPLEMENT), **tables, **salt))
    except ValueError:
        return None


_COMPLEMENT = str.maketrans("ACGT", "TGCA")


def duplex_tm(oligo: str, site: str, cfg: dict[str, Any]) -> tuple[float | None, float, bool]:
    """(Tm on the site, Tm on a perfect site, used inosine).

    Both numbers are in-register by construction, so their difference is the shift
    the record's own mismatches cause at the position they actually sit. The first
    is None where the nearest-neighbour tables cannot price the site (adjacent
    mismatches); the perfect reference is all matches and always computable.
    """
    cond = {**DEFAULTS, **(cfg.get("thermo_conditions") or {})}
    cond = {k: float(cond[k]) for k in DEFAULTS}
    o, t, inosine = resolve(oligo, site)
    perfect = _in_register_tm(o, o, cond)
    assert perfect is not None, "a perfectly matched duplex is always in the tables"
    return _in_register_tm(o, t, cond), perfect, inosine


def annotate(call: Call, oligos: dict[str, str], cfg: dict[str, Any]) -> dict[str, str]:
    """Thermo columns for one Call; empty strings when there is no amplicon."""
    out = dict.fromkeys(COLUMNS, "")
    sites = call.extra.get("sites") or {}
    dtms, notes = [], set()
    for key, prefix in (("forward", "fwd"), ("reverse", "rev"), ("probe", "probe")):
        site = sites.get(key)
        if site is None or key not in oligos:
            continue
        tm, perfect, inosine = duplex_tm(oligos[key], site.window, cfg)
        if inosine:
            notes.add("inosine")
        if tm is None:
            # Adjacent mismatches: no measured term, so no number rather than an
            # optimistic one. The row still carries its call and its mismatches.
            notes.add("nn_unsupported")
            continue
        dtm = tm - perfect
        out[f"{prefix}_tm"] = f"{tm:.1f}"
        out[f"{prefix}_dtm"] = f"{dtm:.1f}"
        dtms.append(dtm)
    if dtms:
        out["thermo_min_dtm"] = f"{min(dtms):.1f}"
    out["thermo_note"] = ",".join(sorted(notes))
    return out
