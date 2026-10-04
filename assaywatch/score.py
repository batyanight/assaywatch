"""Score an assay against one record and make the call.

The rule set is the one in the build plan, read from config.yaml so the
numbers can change without touching code:

    primer, last `primer_3prime_window` nt of the 3' end .... primer_3prime_penalty each
    primer, next `primer_mid_window` nt ...................... primer_mid_penalty each
    primer, remaining 5' region .............................. primer_5prime_penalty each
    probe, central third ..................................... probe_center_penalty each
    probe, outer thirds ...................................... probe_outer_penalty each

Degeneracy is never penalised, in either direction:

* A degenerate oligo position that covers the record's base is a match worth
  nothing, which is what degeneracy is for.
* A record position whose true base is undetermined (an ambiguity code the
  oligo only partly covers, or an N) is `unknown`, not a mismatch. It carries
  no penalty and is counted separately. Charging for it would tax exactly the
  pan-family degenerate assays, because the sparsely sequenced taxa they
  target are where ambiguity codes are common, and it would make real drift
  indistinguishable from the submitter's sequencing quality.

When an oligo footprint carries more than `max_ambiguous_per_oligo` undetermined
positions, too little of the binding site is known to say anything, and the
record is called `indeterminate` for that assay rather than scored. Like
`no_amplicon`, that keeps a data-quality problem out of the drift numbers.

Call per record = sum over forward, reverse and (if present) probe:
    <= detect_max                     detect
    <= reduced_max                    reduced
    otherwise, or any mismatch at a primer's 3'-terminal base   fail
    too many undetermined record bases under an oligo           indeterminate
No forward/reverse pair in the right orientation and size range: no_amplicon.
Both no_amplicon and indeterminate are reported separately from fail so
sequence problems are not confused with assay problems.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from assaywatch.match import Site, find_sites
from assaywatch.schema import Assay

DEFAULT_CONFIG = Path(__file__).resolve().parents[1] / "config.yaml"


def load_config(path: Path | None = None) -> dict[str, Any]:
    return yaml.safe_load((path or DEFAULT_CONFIG).read_text())


@dataclass
class OligoScore:
    penalty: float
    terminal_mismatch: bool
    mismatches: tuple[int, ...]  # positions from the oligo's 5' end
    mismatches_from_3prime: tuple[int, ...]  # 1 = the 3'-terminal base
    ambiguous: tuple[int, ...] = ()  # undetermined record bases; no penalty


def score_primer(site: Site, oligo_len: int, cfg: dict[str, Any]) -> OligoScore:
    """Weight each mismatch by its distance from the 3' end."""
    s = cfg["scoring"]
    w3, wmid = s["primer_3prime_window"], s["primer_mid_window"]
    penalty, terminal = 0.0, False
    from3 = []
    for pos in site.mismatches:
        d = oligo_len - pos  # 1 = 3'-terminal base
        from3.append(d)
        if d == 1:
            terminal = True
        if d <= w3:
            penalty += s["primer_3prime_penalty"]
        elif d <= w3 + wmid:
            penalty += s["primer_mid_penalty"]
        else:
            penalty += s["primer_5prime_penalty"]
    return OligoScore(penalty, terminal, site.mismatches, tuple(from3), site.ambiguous)


def score_probe(site: Site, oligo_len: int, cfg: dict[str, Any]) -> OligoScore:
    """A probe has no 3' end that matters; the middle third is what holds it on."""
    s = cfg["scoring"]
    lo, hi = oligo_len / 3, 2 * oligo_len / 3
    penalty = 0.0
    for pos in site.mismatches:
        penalty += s["probe_center_penalty"] if lo <= pos < hi else s["probe_outer_penalty"]
    return OligoScore(
        penalty, False, site.mismatches, tuple(oligo_len - p for p in site.mismatches), site.ambiguous
    )


@dataclass
class Call:
    assay_id: str
    record_id: str
    call: str  # detect | reduced | fail | indeterminate | no_amplicon
    penalty: float | None = None
    amplicon_start: int | None = None
    amplicon_end: int | None = None
    amplicon_bp: int | None = None
    forward: OligoScore | None = None
    reverse: OligoScore | None = None
    probe: OligoScore | None = None
    reason: str = ""
    extra: dict[str, Any] = field(default_factory=dict)

    def as_row(self) -> dict[str, Any]:
        """Flat dict for a TSV line."""

        def mm(o: OligoScore | None) -> str:
            return "" if o is None else ",".join(str(x) for x in o.mismatches_from_3prime)

        def amb(o: OligoScore | None) -> str:
            return "" if o is None else str(len(o.ambiguous))

        return {
            "assay_id": self.assay_id,
            "record_id": self.record_id,
            "call": self.call,
            "penalty": "" if self.penalty is None else f"{self.penalty:g}",
            "amplicon_start": self.amplicon_start,
            "amplicon_end": self.amplicon_end,
            "amplicon_bp": self.amplicon_bp,
            "fwd_penalty": "" if self.forward is None else f"{self.forward.penalty:g}",
            "fwd_mm_from_3prime": mm(self.forward),
            "fwd_ambiguous": amb(self.forward),
            "rev_penalty": "" if self.reverse is None else f"{self.reverse.penalty:g}",
            "rev_mm_from_3prime": mm(self.reverse),
            "rev_ambiguous": amb(self.reverse),
            "probe_penalty": "" if self.probe is None else f"{self.probe.penalty:g}",
            "probe_mm_from_3prime": mm(self.probe),
            "probe_ambiguous": amb(self.probe),
            "degeneracy_fold": self.extra.get("degeneracy_fold", ""),
            "degeneracy_tier": self.extra.get("degeneracy_tier", ""),
            # Present only when screening ran with --thermo; see thermo.py.
            **self.extra.get("thermo", {}),
            "reason": self.reason,
        }


def too_ambiguous(scores: list[OligoScore], cfg: dict[str, Any]) -> bool:
    """Is any oligo's footprint too undetermined to judge?"""
    cap = cfg["scoring"].get("max_ambiguous_per_oligo")
    if cap is None:
        return False
    return any(len(o.ambiguous) > cap for o in scores)


def classify(total: float, terminal: bool, cfg: dict[str, Any]) -> str:
    s = cfg["scoring"]
    if terminal and s.get("terminal_mismatch_fails", True):
        return "fail"
    if total <= s["detect_max"]:
        return "detect"
    if total <= s["reduced_max"]:
        return "reduced"
    return "fail"


def screen_record(assay: Assay, record_id: str, record_seq: str, cfg: dict[str, Any]) -> Call:
    """Best-scoring amplicon for `assay` in one record, or no_amplicon.

    Geometry rule: a forward site on the plus strand must lie upstream of a
    reverse site on the minus strand, and the span between the outermost
    bases must fall inside the configured amplicon range. If a probe is
    defined it must sit entirely inside that span (either strand); an
    amplicon with no probe site is scored as if the probe mismatched everywhere.
    Of all valid pairs the lowest total penalty wins.
    """
    amp = cfg["amplicon"]
    max_mm = int(cfg["scoring"].get("max_mismatches_searched", 6))
    fwd, rev, probe = assay.oligos.forward.matching_seq, assay.oligos.reverse.matching_seq, None
    if assay.oligos.probe is not None:
        probe = assay.oligos.probe.matching_seq

    # Keep only the best few sites per oligo. Pairing is quadratic and the probe
    # search inside each pair makes it worse; a repetitive or low-complexity
    # record can produce hundreds of near-sites, and the best pair is always
    # built from sites near the top of this ranking anyway.
    keep = int(cfg["scoring"].get("max_sites_per_oligo", 50))

    def best(sites: list[Site]) -> list[Site]:
        return sorted(sites, key=lambda x: (x.n_mismatches, x.n_ambiguous, x.start))[:keep]

    f_sites = best([s for s in find_sites(fwd, record_seq, max_mm) if s.strand == "+"])
    r_sites = best([s for s in find_sites(rev, record_seq, max_mm) if s.strand == "-"])
    if not f_sites or not r_sites:
        which = "forward" if not f_sites else "reverse"
        if not f_sites and not r_sites:
            which = "forward and reverse"
        return Call(assay.id, record_id, "no_amplicon", reason=f"no {which} site within {max_mm} mismatches")

    p_sites = best(find_sites(probe, record_seq, max_mm)) if probe else []

    best: Call | None = None
    for f in f_sites:
        for r in r_sites:
            if r.start <= f.start:
                continue
            length = r.end - f.start
            if not amp["min_bp"] <= length <= amp["max_bp"]:
                continue
            fs = score_primer(f, len(fwd), cfg)
            rs = score_primer(r, len(rev), cfg)
            ps, p_site, reason = None, None, ""
            if probe:
                inside = [p for p in p_sites if p.start >= f.end and p.end <= r.start]
                if inside:
                    ps, p_site = min(
                        ((score_probe(p, len(probe), cfg), p) for p in inside), key=lambda x: x[0].penalty
                    )
                else:
                    # The primers would amplify but the probe has no binding site:
                    # a qPCR assay that produces product and reports nothing.
                    # This is a fail on its own terms, not a large penalty.
                    reason = "no probe site inside amplicon"
            total = fs.penalty + rs.penalty + (ps.penalty if ps else 0.0)
            scores = [o for o in (fs, rs, ps) if o is not None]
            n_amb = sum(len(o.ambiguous) for o in scores)
            if too_ambiguous(scores, cfg):
                call = "indeterminate"
                reason = reason or f"{n_amb} undetermined record bases under the oligos"
            elif reason:
                call = "fail"
            else:
                call = classify(total, fs.terminal_mismatch or rs.terminal_mismatch, cfg)
            cand = Call(assay.id, record_id, call, total, f.start, r.end, length, fs, rs, ps, reason)
            cand.extra["n_ambiguous"] = n_amb
            # The sites themselves, for anything computed on the winning amplicon
            # later (thermo.py). Not written to the TSV.
            cand.extra["sites"] = {"forward": f, "reverse": r, "probe": p_site}
            # Rank by call first (a probe-less amplicon never beats a real one),
            # then by penalty, then by how much of the site was undetermined, so
            # the reported site is the assay's best shot. `indeterminate` ranks
            # last: a site we can actually judge, even a failing one, is more
            # informative than one hidden behind ambiguity codes, and an N-run
            # elsewhere in the record must not masquerade as a clean amplicon.
            rank = {"detect": 0, "reduced": 1, "fail": 2, "indeterminate": 3}
            key = (rank[call], total, n_amb)
            best_key = (rank[best.call], best.penalty, best.extra.get("n_ambiguous", 0)) if best else None
            if best is None or key < best_key:
                best = cand

    if best is None:
        return Call(
            assay.id,
            record_id,
            "no_amplicon",
            reason=f"sites found but no pair in orientation within {amp['min_bp']}-{amp['max_bp']} bp",
        )
    return best
