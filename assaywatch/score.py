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

from bisect import bisect_left, bisect_right
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from assaywatch.chance import composition, pair_evalue, site_evalue
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
    """Weight each mismatch by its distance from the 3' end.

    The biology: Taq extends from the primer's 3'-OH, so a mismatch there
    distorts the geometry of the catalytic site itself, whereas one near the 5'
    end costs only duplex stability — and a 20-mer with 19 matches anneals fine.
    That ordering is well established (Kwok et al. 1990,
    doi:10.1093/nar/18.4.999; Stadhouders et al. 2010,
    doi:10.2353/jmoldx.2010.090035).

    Two things this does NOT capture, both of which make it optimistic in some
    cases and pessimistic in others:

    * Mismatch IDENTITY. Kwok and Stadhouders both find the effect is dominated
      by WHICH mispair forms: A:A, A:G, G:A and C:C at the 3' terminus suppress
      yield by orders of magnitude, while T:G, T:C and T:T are nearly free (a
      T:G wobble still stacks). Scoring by position alone treats those alike. A
      per-identity table is the obvious upgrade and needs a reference dataset we
      do not have; until then position is the defensible half of the story.
    * Mismatch COUNT interactions. Two adjacent mismatches are far worse than
      two spread apart, because they destroy a contiguous stretch of stacking
      rather than two isolated pairs. Penalties here add linearly, so a cluster
      is under-penalised.
    """
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
    """A probe has no 3' end that matters; the middle third is what holds it on.

    A hydrolysis probe is not extended — it is bound and then cleaved — so the
    3'-end asymmetry that governs primers does not apply. What matters is that
    the duplex survives to the extension step, and a central mismatch costs the
    most stability because it interrupts stacking on both sides, while a
    terminal one only frays an end that was already breathing.

    The thirds are a crude stand-in for a stability calculation, and they are
    length-blind: the central third of a 15-mer is 5 nt where a single mismatch
    may well abolish binding, and of a 30-mer is 10 nt where it may not. All 10
    probe assays in the registry are also MGB, whose minor-groove binder adds
    roughly 15-20 C of Tm; those probes tolerate mismatches a bare oligo of the
    same length would not, and nothing here knows that. `--thermo` computes the
    actual duplex ΔTm and is the better guide where it is available.
    """
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
            # Where each oligo sat, as start-end(strand) on the plus strand.
            "fwd_site": self.extra.get("fwd_site", ""),
            "rev_site": self.extra.get("rev_site", ""),
            "probe_site": self.extra.get("probe_site", ""),
            # For no_amplicon only: why this record could not be judged.
            "exclusion": self.extra.get("exclusion", ""),
            # Expected number of pairs this good in a random record like this one (chance.py).
            "pair_evalue": f"{self.extra['pair_evalue']:.2g}" if "pair_evalue" in self.extra else "",
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
    """Turn one summed penalty into a call.

    Two known weaknesses, both biological rather than numerical:

    * The total SUMS forward, reverse and probe, but they are serial gates, not
      a shared budget: amplification needs both primers, and detection needs
      the probe on top. Three trivial mismatches spread one per oligo land in
      the same bin as one near-lethal 3'-proximal mismatch, and a probe defect
      (which costs signal linearly) trades against a primer defect (which costs
      the exponential). Per-oligo verdicts combined logically is the right
      model; see docs/2026-10-04-pipeline-review.md.
    * `terminal` is identity-blind, so about half the 3'-terminal mismatches it
      fails are the near-neutral kind (see score_primer). It is also one
      threshold for 135 conventional PCRs and 10 probe assays, and endpoint PCR
      forgives a yield loss that a Cq cutoff does not.
    """
    s = cfg["scoring"]
    if terminal and s.get("terminal_mismatch_fails", True):
        return "fail"
    if total <= s["detect_max"]:
        return "detect"
    if total <= s["reduced_max"]:
        return "reduced"
    return "fail"


def _rank(site: Site) -> tuple[int, int, int]:
    """How good a single site is: fewest mismatches, then fewest undetermined bases, then position."""
    return (site.n_mismatches, site.n_ambiguous, site.start)


def _call_rank(call: str, reason: str) -> float:
    """Order of preference between candidate amplicons of one record.

    A primer pair with no probe site between it is a `fail` with no probe
    penalty, so on penalty alone it would beat a real amplicon whose probe is
    present but mismatched. It ranks after every amplicon that has its probe.
    """
    if call == "fail" and reason == "no probe site inside amplicon":
        return 2.5
    # no_amplicon ranks last: it only reaches here when comparing whole calls
    # across the combinations of a primer pool, where some members find nothing.
    return {"detect": 0, "reduced": 1, "fail": 2, "indeterminate": 3, "no_amplicon": 4}[call]


class SiteIndex:
    """Sites sorted by start, for range queries; results come back in _rank order."""

    def __init__(self, sites: list[Site]):
        self.sites = sorted(sites, key=lambda x: x.start)
        self.starts = [x.start for x in self.sites]

    def within(self, lo: int, hi: int, strand: str | None = None) -> list[Site]:
        """Sites with lo <= start <= hi (optionally on one strand), best first."""
        i, j = bisect_left(self.starts, lo), bisect_right(self.starts, hi)
        out = self.sites[i:j] if strand is None else [x for x in self.sites[i:j] if x.strand == strand]
        return sorted(out, key=_rank)


def facing_pairs(f_all: list[Site], r_all: list[Site], rev_len: int, amp: dict[str, Any]) -> list[tuple]:
    """Every forward/reverse pair facing each other in amplicon range, either orientation.

    Returns (forward, reverse, amplicon start, amplicon end, inner start, inner end);
    `inner` is the stretch between the primers, where a probe must sit. The
    reverse sites are found by binary search on position, so a genome with
    thousands of candidate sites pairs in near-linear time. Order is forward
    sites best first (plus strand before minus), then reverse sites best first,
    which fixes how ties between equally good amplicons are broken.
    """
    lo_bp, hi_bp = int(amp["min_bp"]), int(amp["max_bp"])
    r_index = SiteIndex(r_all)
    pairs = []

    # The two orientations, drawn on the plus strand of the record. An amplicon
    # always runs from a plus-strand site rightwards to a minus-strand site:
    #
    #   plus-strand product    5'--[F +]------------[R -]--3'   amplicon = F.start .. R.end
    #   minus-strand product   5'--[R +]------------[F -]--3'   amplicon = R.start .. F.end
    #
    # The second case is the same target read the other way round, which is every
    # minus-strand gene of a genome record and any antisense deposit. Coordinates
    # are always reported on the plus strand, so the caller never has to care.
    for f in sorted((x for x in f_all if x.strand == "+"), key=_rank):
        # Reverse site lies downstream. Its START is searched for, not its end,
        # because SiteIndex is indexed by start — hence the `- rev_len`: a product
        # of hi_bp means the reverse site starts hi_bp - rev_len past the forward.
        lo = max(f.start + 1, f.start + lo_bp - rev_len)
        for r in r_index.within(lo, f.start + hi_bp - rev_len, "-"):
            pairs.append((f, r, f.start, r.end, f.end, r.start))
    for f in sorted((x for x in f_all if x.strand == "-"), key=_rank):
        # Reverse on plus, upstream: amplicon = [r.start, f.end).
        hi = min(f.start - 1, f.end - lo_bp)
        for r in r_index.within(f.end - hi_bp, hi, "+"):
            pairs.append((f, r, r.start, f.end, r.end, f.start))
    return pairs


def oligo_pools(assay: Assay) -> tuple[list[str], list[str], list[str]]:
    """(forward, reverse, probe) sequences for one assay, pool members included.

    Several consensus protocols run more than one primer per role in the same
    tube: the PREDICT filovirus assay has four forward and four reverse
    lineage-specific primers, and the astrovirus assay two alternative
    forwards. Those extra primers live in `oligos.alternates` with an
    `orientation`, and the assay detects a record if *any* member of each pool
    does, so screening against one pair at a time understates it.
    """
    fwd = [assay.oligos.forward.matching_seq]
    rev = [assay.oligos.reverse.matching_seq]
    probe = [assay.oligos.probe.matching_seq] if assay.oligos.probe is not None else []
    for alt in assay.oligos.alternates or []:
        bucket = {"forward": fwd, "reverse": rev, "probe": probe}.get(alt.orientation or "")
        if bucket is not None and alt.matching_seq not in bucket:
            bucket.append(alt.matching_seq)
    return fwd, rev, probe


def screen_record(
    assay: Assay, record_id: str, record_seq: str, cfg: dict[str, Any], comp: tuple | None = None
) -> Call:
    """Best call for `assay` in one record, over every combination of its primer pools.

    With no pool members this is one call of `screen_one`, which is the whole
    of the scoring logic; with pools it is the best call over the cross product,
    and `extra["pool"]` names the primers that won.

    The split exists so that every pool combination goes through exactly the same
    scoring path as a plain assay: there is one implementation of the rules, and
    pooling is a loop around it rather than a second code path.
    """
    fwd, rev, probe = oligo_pools(assay)
    if len(fwd) == 1 and len(rev) == 1 and len(probe) <= 1:
        return screen_one(assay, record_id, record_seq, cfg, comp)
    if comp is None:
        comp = composition(record_seq)
    best: Call | None = None
    for f in fwd:
        for r in rev:
            cand = screen_one(assay, record_id, record_seq, cfg, comp, f, r, probe or [None])
            key = (_call_rank(cand.call, cand.reason), cand.penalty if cand.penalty is not None else 1e9)
            if best is None or key < (
                _call_rank(best.call, best.reason),
                best.penalty if best.penalty is not None else 1e9,
            ):
                best = cand
                best.extra["pool"] = f"forward={f} reverse={r}"
    assert best is not None
    return best


def _site_text(site: Site | None) -> str:
    return "" if site is None else f"{site.start}-{site.end}{site.strand}"


def classify_exclusion(
    record_seq: str,
    oligos: dict[str, str],
    found: dict[str, list[Site]],
    cfg: dict[str, Any],
    comp: tuple,
    amplicon_bp: int | None,
) -> tuple[str, str]:
    """Why a record yielded no amplicon: (label, one-line detail).

    A record with no amplicon is dropped from the drift denominator, and the
    reasons are not equivalent. If the deposit simply stops before the other
    binding site, it says nothing about the assay; if the site is there and does
    not match, that is the assay failing. Telling those apart needs the
    positions, anchored on a site good enough to trust: of 464 Bd ITS deposits
    that yield no amplicon, 392 are truncated before the probe footprint and
    none show it present and diverged.

    Labels: `no_site` (nothing credible for either primer), `truncated` (the
    missing site's window runs off the end of the record), `diverged` (the
    window is inside the record but nothing credible matches there), `no_pair`
    (both primers credible but never facing each other in range).
    """
    # Its own key: `max_pair_evalue: null` means "report the E-value, act on
    # nothing", and reusing it here silently kept filtering at 0.01.
    max_e = float(cfg["scoring"].get("max_site_evalue", 0.01))
    span = int(amplicon_bp or cfg["amplicon"]["max_bp"])
    n = len(record_seq)

    def credible(name: str) -> list[Site]:
        o = oligos[name]
        return [
            s for s in found.get(name, []) if site_evalue(o, s.n_mismatches + s.n_ambiguous, n, comp) <= max_e
        ]

    cf, cr = credible("forward"), credible("reverse")
    if cf and cr:
        return "no_pair", "both primers match credibly but never face each other in range"
    if not cf and not cr:
        return "no_site", "no credible site for either primer"
    # Which side of the anchor the missing primer should sit on depends ONLY on
    # the anchor's strand, never on which oligo is missing — see the diagram in
    # facing_pairs. Deriving it from the missing oligo's role instead labelled 382
    # truncated Bd deposits as `diverged`, i.e. asserted the forward primer had
    # failed on them, when the records simply stopped short of its site.
    anchor, missing = (cf[0], "reverse") if cf else (cr[0], "forward")
    # The partner always lies on the far side of the anchor, and which side that
    # is depends only on the anchor's strand: an amplicon runs from a plus-strand
    # site up to a minus-strand one. So from a minus-strand anchor the partner is
    # at lower coordinates, and from a plus-strand anchor at higher ones. Getting
    # this from the missing oligo's role instead of the anchor's strand labelled
    # 382 truncated Bd deposits as diverged, i.e. claimed the forward primer had
    # failed on them.
    if anchor.strand == "-":
        lo, hi = anchor.end - span, anchor.end
    else:
        lo, hi = anchor.start, anchor.start + span
    if lo < 0 or hi > n:
        return "truncated", f"the record ends before the {missing} primer's window"
    return "diverged", f"the {missing} primer's window is present but nothing credible matches it"


def screen_one(
    assay: Assay,
    record_id: str,
    record_seq: str,
    cfg: dict[str, Any],
    comp: tuple | None = None,
    fwd_seq: str | None = None,
    rev_seq: str | None = None,
    probe_seqs: list[str | None] | None = None,
) -> Call:
    """Best-scoring amplicon for one primer pair in one record, or no_amplicon.

    Geometry rule: the forward and reverse sites must face each other on
    opposite strands, and the span between the outermost bases must fall
    inside the configured amplicon range. The amplicon may lie on either strand
    of the record: forward on plus upstream of reverse on minus, or forward on
    minus downstream of reverse on plus. The second case is a target read in
    the other direction, which is every minus-strand gene of a genome record
    and any record deposited antisense; coordinates are reported on the plus
    strand either way. If a probe is defined it must sit entirely inside the
    span between the primers (either strand); an amplicon with no probe site is
    a fail. Of all valid pairs the best call, then the lowest penalty, wins.
    """
    amp = cfg["amplicon"]
    max_mm = int(cfg["scoring"].get("max_mismatches_searched", 6))
    fwd = fwd_seq or assay.oligos.forward.matching_seq
    rev = rev_seq or assay.oligos.reverse.matching_seq
    # Every probe pool member is searched, and the best site inside the amplicon
    # wins. An earlier version took `next(...)`, i.e. only the first member, while
    # its own comment claimed the pool was searched together.
    probes: list[str] = []
    if probe_seqs:
        probes = [x for x in probe_seqs if x]
    elif assay.oligos.probe is not None:
        probes = [assay.oligos.probe.matching_seq]
    probe = probes[0] if probes else None

    f_all = find_sites(fwd, record_seq, max_mm)
    r_all = find_sites(rev, record_seq, max_mm)
    if comp is None:
        comp = composition(record_seq)
    oligo_map = {"forward": fwd, "reverse": rev}
    found_map = {"forward": f_all, "reverse": r_all}
    if not f_all or not r_all:
        which = "forward" if not f_all else "reverse"
        if not f_all and not r_all:
            which = "forward and reverse"
        call = Call(assay.id, record_id, "no_amplicon", reason=f"no {which} site within {max_mm} mismatches")
        label, detail = classify_exclusion(record_seq, oligo_map, found_map, cfg, comp, assay.amplicon_bp)
        call.extra["exclusion"] = label
        call.reason = f"{call.reason}; {detail}"
        return call

    pairs = facing_pairs(f_all, r_all, len(rev), amp)
    # A pathological record (long low-complexity runs) can still produce a huge
    # number of pairs; keep the best-matched ones. This applies to pairs, never
    # to single sites: a cap on sites before pairing could drop the true site of a
    # genome in favour of fifty better-looking chance sites elsewhere.
    cap = int(cfg["scoring"].get("max_pairs_per_record", 5000))
    if len(pairs) > cap:
        pairs = sorted(pairs, key=lambda x: _rank(x[0]) + _rank(x[1]))[:cap]
    # One index per pool member, so a member's own length is available for scoring.
    p_indexes = [(o, SiteIndex(find_sites(o, record_seq, max_mm))) for o in probes]

    # Chance-pair guard (chance.py). A six-mismatch budget on a megabase record
    # finds primer pairs by luck — hundreds per genome — and before this existed
    # a quarter of all `fail` calls were such pairs, counted against the assay.
    # The E-value asks how many pairs this good a random record of the same
    # length would hold. It is always reported; pairs above `max_pair_evalue`
    # are only dropped when that is set.
    max_e = cfg["scoring"].get("max_pair_evalue")
    n_chance = 0

    # The assay's own declared product size, where it has one, with a tolerance
    # for the indels and insertions real templates carry. Without this the only
    # limit is the global 50-3000 bp window, which credited 727 calls to products
    # more than twice the declared size and one to a 1931 bp product from a
    # 194 bp assay. A product that size is not that assay amplifying: the
    # extension time, probe geometry and efficiency all belong to something else.
    tol = cfg["amplicon"].get("declared_tolerance")
    lo_bp, hi_bp = int(amp["min_bp"]), int(amp["max_bp"])
    if assay.amplicon_bp and tol is not None:
        tol = float(tol)
        lo_bp = max(lo_bp, int(assay.amplicon_bp * (1 - tol)))
        hi_bp = min(hi_bp, int(assay.amplicon_bp * (1 + tol)))

    best: Call | None = None
    for f, r, amp_start, amp_end, inner_lo, inner_hi in pairs:
        length = amp_end - amp_start
        if not lo_bp <= length <= hi_bp:
            continue
        evalue = pair_evalue(
            fwd,
            rev,
            f.n_mismatches + f.n_ambiguous,
            r.n_mismatches + r.n_ambiguous,
            len(record_seq),
            cfg,
            comp,
        )
        if max_e is not None and evalue > max_e:
            n_chance += 1
            continue
        fs = score_primer(f, len(fwd), cfg)
        rs = score_primer(r, len(rev), cfg)
        ps, p_site, reason = None, None, ""
        probe_won = probe
        if probe:
            scored = [
                (score_probe(p, len(o), cfg), p, o)
                for o, idx in p_indexes
                for p in idx.within(inner_lo, inner_hi - len(o))
            ]
            if scored:
                ps, p_site, probe_won = min(scored, key=lambda x: x[0].penalty)
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
        cand = Call(assay.id, record_id, call, total, amp_start, amp_end, length, fs, rs, ps, reason)
        cand.extra["n_ambiguous"] = n_amb
        cand.extra["pair_evalue"] = evalue
        # The sites themselves, for anything computed on the winning amplicon
        # later (thermo.py). Not written to the TSV.
        cand.extra["sites"] = {"forward": f, "reverse": r, "probe": p_site}
        # The sequences that actually won, which for a primer pool are not the
        # assay's primary oligos. thermo.annotate zips an oligo against its site
        # window, so handing it the primary oligo of a different length crashed
        # the whole screening job on any pool assay.
        cand.extra["oligos"] = {"forward": fwd, "reverse": rev}
        if probe_won:
            cand.extra["oligos"]["probe"] = probe_won
        cand.extra["fwd_site"] = _site_text(f)
        cand.extra["rev_site"] = _site_text(r)
        cand.extra["probe_site"] = _site_text(p_site)
        # Rank by call first (a probe-less amplicon never beats a real one),
        # then by penalty, then by how much of the site was undetermined, so
        # the reported site is the assay's best shot. `indeterminate` ranks
        # last: a site we can actually judge, even a failing one, is more
        # informative than one hidden behind ambiguity codes, and an N-run
        # elsewhere in the record must not masquerade as a clean amplicon.
        key = (_call_rank(call, reason), total, n_amb)
        best_key = (
            (_call_rank(best.call, best.reason), best.penalty, best.extra.get("n_ambiguous", 0))
            if best
            else None
        )
        if best is None or key < best_key:
            best = cand

    if best is None:
        reason = f"sites found but no facing pair within {lo_bp}-{hi_bp} bp"
        if n_chance:
            reason = f"{n_chance} facing pairs, none distinguishable from chance (E > {max_e:g})"
        call = Call(assay.id, record_id, "no_amplicon", reason=reason)
        label, detail = classify_exclusion(record_seq, oligo_map, found_map, cfg, comp, assay.amplicon_bp)
        call.extra["exclusion"] = "chance_only" if n_chance else label
        call.reason = f"{reason}; {detail}"
        return call
    return best
