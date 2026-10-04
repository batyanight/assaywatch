"""Duplex melting temperature of each oligo on its actual binding site. Never scored.

The mismatch penalty in score.py is a positional rule of thumb. What a mismatch
does to binding depends on which mismatch it is and what surrounds it: a G:T
wobble in a GC-rich stretch costs a degree, an A:C next to the 3' end can cost
ten. This module puts a number on that with primer3's nearest-neighbour model
(SantaLucia 1998, with its mismatch parameters), as an extra column beside the
call, the same way degeneracy rides along: shown, never folded into the call.

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

from typing import Any

from assaywatch.iupac import IUPAC, reverse_complement

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


def _primer3():
    try:
        import primer3
    except ImportError as e:  # pragma: no cover - depends on the environment
        raise SystemExit("thermodynamic columns need primer3-py: conda install -c bioconda primer3-py") from e
    return primer3


def resolve(oligo: str, site: str) -> tuple[str, str, bool]:
    """(oligo bases, record bases, used inosine) with every IUPAC code made concrete.

    `site` is the record's bases oriented 5'->3' like the oligo (Site.window), so
    position i of each is the same position of the duplex.
    """
    o_out, t_out, inosine = [], [], False
    for o, t in zip(oligo.upper(), site.upper(), strict=True):
        t_set = IUPAC.get(t, "ACGT")
        if o == "I":
            inosine = True
            base = t if len(t_set) == 1 else "A"
            o_out.append(base)
            t_out.append(base)
            continue
        pool = IUPAC.get(o, "ACGT")
        if len(t_set) == 1 and t_set in pool:
            ob = t_set
        else:
            ob = pool[0]
        o_out.append(ob)
        t_out.append(t_set if len(t_set) == 1 else ob)
    return "".join(o_out), "".join(t_out), inosine


def duplex_tm(oligo: str, site: str, cfg: dict[str, Any]) -> tuple[float, float, bool]:
    """(Tm on the site, Tm on a perfect site, used inosine)."""
    p3 = _primer3()
    cond = {**DEFAULTS, **(cfg.get("thermo_conditions") or {})}
    cond = {k: float(cond[k]) for k in DEFAULTS}
    o, t, inosine = resolve(oligo, site)
    # The oligo pairs with the strand complementary to `site`, read 5'->3'.
    tm = p3.calc_heterodimer(o, reverse_complement(t), **cond).tm
    perfect = p3.calc_heterodimer(o, reverse_complement(o), **cond).tm
    return tm, perfect, inosine


def annotate(call, oligos: dict[str, str], cfg: dict[str, Any]) -> dict[str, str]:
    """Thermo columns for one Call; empty strings when there is no amplicon."""
    out = dict.fromkeys(COLUMNS, "")
    sites = call.extra.get("sites") or {}
    dtms, notes = [], set()
    for key, prefix in (("forward", "fwd"), ("reverse", "rev"), ("probe", "probe")):
        site = sites.get(key)
        if site is None or key not in oligos:
            continue
        tm, perfect, inosine = duplex_tm(oligos[key], site.window, cfg)
        dtm = tm - perfect
        out[f"{prefix}_tm"] = f"{tm:.1f}"
        out[f"{prefix}_dtm"] = f"{dtm:.1f}"
        dtms.append(dtm)
        if inosine:
            notes.add("inosine")
    if dtms:
        out["thermo_min_dtm"] = f"{min(dtms):.1f}"
    out["thermo_note"] = ",".join(sorted(notes))
    return out
