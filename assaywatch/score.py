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

How those penalties become a call depends on `scoring.engine`:

`budget` (the default, and what every number in config.yaml was set against)
sums forward, reverse and (if present) probe into one total:
    <= detect_max                     detect
    <= reduced_max                    reduced
    otherwise, or any mismatch at a primer's 3'-terminal base   fail

`serial` judges each oligo on its own penalty and combines the verdicts
logically, because amplification needs the forward AND the reverse primer and
detection needs the probe on top - they are serial gates, not a shared budget:
    every oligo ok                    detect
    any oligo weak                    reduced
    any oligo blocked                 fail
See `oligo_verdict`, `combine` and `decide`. Measured on results/2026-10-20,
the two engines disagree on 182,185 of the 912,111 calls `decide` makes; the
shared budget, not identity-blindness, decides most of the current call set.
`serial`'s own thresholds are not yet calibrated - config.yaml says so.

Either way:
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
from assaywatch.iupac import COMPLEMENT
from assaywatch.match import Site, find_sites
from assaywatch.schema import Assay, Chemistry

# Re-exported: `check_chemistry_overrides` lived here, and moved to settings.py so
# the `Scoring` model could be its only enforcer without importing this module.
from assaywatch.settings import check_chemistry_overrides as check_chemistry_overrides
from assaywatch.settings import validated

#: Where `load_config(None)` looks: the repo root, one level above this package.
#: This resolves correctly for a clone and for `pip install -e .`, and NOT for a
#: wheel, where `parents[1]` is site-packages. `load_config` says so rather than
#: raising a bare FileNotFoundError on a path the caller never chose -- see its
#: docstring for why the file is not bundled into the wheel instead.
DEFAULT_CONFIG = Path(__file__).resolve().parents[1] / "config.yaml"

# Where load_config stashes one fully-resolved config per chemistry that has
# overrides. Private, and absent entirely when nothing is overridden.
RESOLVED = "_config_by_chemistry"


def scoring_for(chemistry: Chemistry | str, cfg: dict[str, Any]) -> dict[str, Any]:
    """The scoring block that applies to one chemistry.

    `scoring` in config.yaml holds the numbers that apply to every assay, and an
    optional `scoring.by_chemistry` map overrides individual keys for one of
    them.

    WHY THIS EXISTS. One penalty table was applied to every assay, and they are
    not one kind of assay: most are conventional or consensus PCR and the rest
    are probe-based, SYBR or RPA (161 / 44 / 2 / 1 of 208 on 2026-10-23;
    `python -m assaywatch.validate registry` prints the current
    counts, which is where they now live - written by hand here they had
    drifted to 164/142/21). Conventional PCR tolerates
    mismatches far better than a hydrolysis probe - a 100-fold yield loss is
    often still a visible band after 40 cycles - so a qPCR-grade rule like
    `terminal_mismatch_fails` is too harsh for most of this registry, and too
    harsh means `fail` calls that are not failures and a flagged count that is
    inflated.

    WHAT THIS DELIBERATELY DOES NOT DO. It ships with no overrides, so every
    chemistry gets today's numbers and every call is unchanged. The fix for
    "these numbers are wrong" is tier-2 validation setting them against known
    answers, not an author choosing new ones; this is the mechanism that makes
    such a change expressible and auditable, and the numbers come later.

    Returns the base block ITSELF, not a copy, when a chemistry overrides
    nothing, so the common path allocates nothing and cannot drift from the
    behaviour that preceded it.
    """
    base = cfg.get("scoring") or {}
    override = (base.get("by_chemistry") or {}).get(str(chemistry)) or {}
    # `by_chemistry` is left inside the merged block; nothing reads it, and
    # removing it would cost the identity fast-path above for no benefit.
    return {**base, **override} if override else base


def max_mismatches_searched(cfg: dict[str, Any]) -> int:
    """The largest `max_mismatches_searched` any chemistry could use.

    For callers that work on oligo PAIRS and so have no chemistry to resolve: the
    assembly pre-cut (`assemblies.extract_loci`) receives only (forward, reverse)
    sequences. Using the base value there meant a `by_chemistry` override that
    RAISED the budget reached the screener but not the pre-cut, so a site the
    screener would have scored was cut away before it ever saw it, and the asm
    group reported no locus where the override said the assay should score one.

    Taking the maximum over the base value and every override is safe by
    construction: the pre-cut only decides which windows are worth keeping, and
    keeping a window the screener then finds a smaller budget rejects costs a
    little disk, while dropping one loses a call. Screening applies each assay's
    own budget afterwards, so no call changes.
    """
    base = cfg.get("scoring") or {}
    values = [int(base.get("max_mismatches_searched", 6))]
    for override in (base.get("by_chemistry") or {}).values():
        if override and "max_mismatches_searched" in override:
            values.append(int(override["max_mismatches_searched"]))
    return max(values)


def config_for(chemistry: Chemistry | str, cfg: dict[str, Any]) -> dict[str, Any]:
    """`cfg` with its `scoring` block resolved for one chemistry.

    Returns `cfg` itself when that chemistry overrides nothing, which is the
    shipped default - so the scoring path is identical to the one that existed
    before per-chemistry scoring rather than merely equivalent to it.
    """
    # The cache is trusted only while it was computed from THIS `scoring` block. A
    # shallow copy that swaps the block -- tests clearing mispair_penalty, a pricing
    # script overlaying by_chemistry -- carried the stale cache and was answered
    # from the shipped table; it bit twice on 2026-10-27, the day a table stopped
    # being empty. Identity, not equality: a deepcopy preserves the relation and so
    # keeps its own cache; a swap breaks it and recomputes.
    pre = cfg.get(RESOLVED)
    if pre is not None and pre.get("scoring") is cfg.get("scoring") and str(chemistry) in pre["resolved"]:
        return pre["resolved"][str(chemistry)]
    scoring = scoring_for(chemistry, cfg)
    return cfg if scoring is cfg.get("scoring") else {**cfg, "scoring": scoring}


def load_config(path: Path | None = None) -> dict[str, Any]:
    """The scoring config: `path`, or `config.yaml` beside the repo root.

    WHY THE DEFAULT CAN BE ABSENT, AND WHY THAT IS NOT FIXED BY BUNDLING IT.
    `DEFAULT_CONFIG` is `parents[1] / "config.yaml"`, which is the repo root for
    a clone or an editable install and `site-packages/config.yaml` for a wheel.
    Every documented command and all of CI use an editable install, so a wheel
    installed from PyPI would `import assaywatch` fine and then fail here on a
    path the caller never named -- previously as a bare FileNotFoundError.

    The file is deliberately NOT shipped inside the package. A wheel cannot run
    the pipeline anyway: that needs `registry/`, `Snakefile`, `data/retrieved/`
    and `results/`, all repo-relative. And `registry/` is CC-BY-4.0 data
    (LICENSE-registry) versioned as the project's data product, while the wheel
    is MIT code; bundling one into the other would blur a licence split that
    exists on purpose. So a wheel is a library install, and a library caller
    passes its own config path.
    """
    target = path or DEFAULT_CONFIG
    if not target.exists():
        raise SystemExit(
            f"no config at {target}.\n"
            + (
                "This looks like a non-editable install: assaywatch ships code, not "
                "config.yaml or registry/. Pass an explicit path -- load_config(Path(...)) "
                "or --config -- or work from a clone (`pip install -e .`), which is what "
                "running the pipeline needs.\n"
                if path is None and not DEFAULT_CONFIG.exists()
                else ""
            )
        )
    # Validated against assaywatch.settings: unknown keys are refused, every
    # default is filled from the models, and `scoring.by_chemistry` is checked.
    # Verified on 2026-10-23 that this changes no value in the committed
    # config.yaml, so no cached screen is invalidated by introducing it.
    cfg = validated(yaml.safe_load(target.read_text()))
    # Resolved once here rather than per record. Only chemistries that override
    # something are stored, so every other one falls through to `config_for`'s
    # identity path and costs nothing.
    resolved = {}
    for chem in Chemistry:
        scoring = scoring_for(chem, cfg)
        if scoring is not cfg.get("scoring"):
            resolved[str(chem)] = {**cfg, "scoring": scoring}
    if resolved:
        # Keyed to the scoring block it came from; see `config_for`.
        cfg[RESOLVED] = {"scoring": cfg["scoring"], "resolved": resolved}
    return cfg


@dataclass
class OligoScore:
    penalty: float
    terminal_mismatch: bool
    mismatches: tuple[int, ...]  # positions from the oligo's 5' end
    mismatches_from_3prime: tuple[int, ...]  # 1 = the 3'-terminal base
    ambiguous: tuple[int, ...] = ()  # undetermined record bases; no penalty
    #: Each definite mismatch as `oligo:template@distance_from_3prime`, e.g.
    #: `A:G@2`. The identity Kwok 1990 and Stadhouders 2010 find dominates the
    #: 3'-end effect, and the one thing the screen computed and then threw away:
    #: `mismatches_from_3prime` kept where, `mispair_multiplier` used what, and
    #: nothing wrote what down. Recording it is what lets a scoring candidate be
    #: REPLAYED over the calls table instead of costing a full rescreen
    #: (docs/journal/2026-10-24-scoring-strategy-test-plan.md Part 0.1).
    #:
    #: Definite mismatches only. An ambiguity code in the record names no single
    #: mispair, as `mispair_multiplier` explains, so those stay counted in
    #: `ambiguous` and appear here not at all.
    mispairs: tuple[str, ...] = ()


def mispair_multiplier(oligo_base: str, template_base: str, table: dict[str, Any]) -> float:
    """Multiplier on a mismatch's position penalty for the mispair that forms.

    `oligo_base` is the primer base and `template_base` is the base it faces on
    the strand it binds — the complement of the record base, because `Site.window`
    reads the record in the oligo's own 5'->3' orientation. The key is
    `"{oligo}:{template}"`, e.g. a primer G opposite a template T is `"G:T"`.

    Looked up only when both are definite A/C/G/T. A degenerate primer base (Y,
    R, ...) or an ambiguity code in the record names no single mispair, so those
    keep the full position penalty — the conservative choice, and the one that
    matches `base_state`'s rule that a mismatch is only definite when the codes
    share no base at all. An empty table returns 1.0 for everything, which is
    why `mispair_penalty: {}` scores byte-identically to no table at all.
    """
    if not table:
        return 1.0
    if oligo_base not in "ACGT" or template_base not in "ACGT":
        return 1.0
    return float(table.get(f"{oligo_base}:{template_base}", 1.0))


def score_primer(site: Site, oligo: str, cfg: dict[str, Any]) -> OligoScore:
    """Weight each mismatch by its distance from the 3' end, then by identity.

    The biology of position: Taq extends from the primer's 3'-OH, so a mismatch
    there distorts the geometry of the catalytic site itself, whereas one near
    the 5' end costs only duplex stability — and a 20-mer with 19 matches anneals
    fine. That ordering is well established (Kwok et al. 1990,
    doi:10.1093/nar/18.4.999; Stadhouders et al. 2010,
    doi:10.2353/jmoldx.2010.090035).

    IDENTITY (M1, 2026-10-21; scoped to the 3' window 2026-10-22). Position alone
    treats every mispair at a given distance alike, but Kwok and Stadhouders both
    find the 3'-end effect is dominated by WHICH mispair forms: A:A, A:G, G:A and
    C:C suppress yield by orders of magnitude, while T:G, G:T, T:C and T:T are
    nearly free (a T:G wobble still stacks). `scoring.mispair_penalty` multiplies
    a definite mismatch's position penalty by the value for its primer:template
    mispair (see `mispair_multiplier`) WHEN the mismatch is in the 3' window, and
    a multiplier of 0 also exempts a 3'-terminal mismatch from
    `terminal_mismatch_fails`, since a mispair declared free does not impede
    extension. It is scoped to the window on purpose: both papers measure the
    effect at the 3' end, and when the discount ran unscoped it erased internal
    G:T wobbles across whole record sets and cost three documented tier-2 catches
    (docs/journal/2026-10-22-M1-tier2.md). Beyond the window, position alone decides.
    How far it reaches is `scoring.mispair_window`, null meaning the 3' window;
    the scope is a config number like every other, not a constant in here.

    The table ships EMPTY, so by default this does nothing. The G:T/T:G wobble is
    the one candidate that has been tried: three bench panels (FAP, Barrett,
    Meyer) argue for discounting it and Rahn's negatives price it at zero
    specificity cost, but at 0.0 it lost a documented tier-2 catch both unscoped
    and scoped, so it was reverted (docs/journal/2026-10-22-M1-tier2.md). No value ships
    without a tier-2 run behind it.

    Still NOT captured: mismatch COUNT interactions. Two adjacent mismatches are
    far worse than two spread apart, because they destroy a contiguous stretch of
    stacking rather than two isolated pairs. Penalties here add linearly, so a
    cluster is under-penalised.
    """
    s = cfg["scoring"]
    w3, wmid = s["primer_3prime_window"], s["primer_mid_window"]
    table = s.get("mispair_penalty") or {}
    # How far identity reaches. Null = the 3' window, which is what M1 shipped;
    # `scoring.mispair_window` exists so S7b can price a longer reach without the
    # scope living in code. See the config comment for why the default is w3.
    wmis = s.get("mispair_window")
    wmis = w3 if wmis is None else wmis
    oligo_len = len(oligo)
    penalty, terminal = 0.0, False
    from3: list[int] = []
    mispairs: list[str] = []
    for pos in site.mismatches:
        d = oligo_len - pos  # 1 = 3'-terminal base
        from3.append(d)
        if d <= w3:
            base = s["primer_3prime_penalty"]
        elif d <= w3 + wmid:
            base = s["primer_mid_penalty"]
        else:
            base = s["primer_5prime_penalty"]
        # The record base the primer faces, complemented into the template base;
        # out-of-range window (defensive, should not happen) keeps the full penalty.
        rec = site.window[pos] if pos < len(site.window) else "N"
        # Identity acts only within the 3' window. Kwok and Stadhouders measure
        # the mispair effect at the 3' end, where it is about extension geometry,
        # not duplex melting. Applied to a 5'/mid mismatch the same discount
        # erased internal G:T wobbles across whole record sets and masked real
        # coverage drops - three documented tier-2 catches fell when it ran
        # unscoped (docs/journal/2026-10-22-M1-tier2.md), 5498 of 5499 Paramyxovirinae
        # flips resting on mismatches outside the window. Beyond it, position
        # alone decides.
        template = COMPLEMENT.get(rec.upper(), "N")
        # Recorded for every mismatch, not only those inside the 3' window where
        # the multiplier acts: a replay may weight identity differently, or at a
        # different distance, and it cannot invent what was not written down.
        mispairs.append(f"{oligo[pos].upper()}:{template}@{d}")
        mult = 1.0
        if d <= wmis:
            mult = mispair_multiplier(oligo[pos].upper(), template, table)
        penalty += base * mult
        if d == 1 and mult != 0:
            terminal = True
    return OligoScore(penalty, terminal, site.mismatches, tuple(from3), site.ambiguous, tuple(mispairs))


def score_probe(site: Site, oligo: str, cfg: dict[str, Any]) -> OligoScore:
    """A probe has no 3' end that matters; the middle third is what holds it on.

    A hydrolysis probe is not extended — it is bound and then cleaved — so the
    3'-end asymmetry that governs primers does not apply. What matters is that
    the duplex survives to the extension step, and a central mismatch costs the
    most stability because it interrupts stacking on both sides, while a
    terminal one only frays an end that was already breathing.

    The thirds are a crude stand-in for a stability calculation, and they are
    length-blind: the central third of a 15-mer is 5 nt where a single mismatch
    may well abolish binding, and of a 30-mer is 10 nt where it may not. Of the 44
    probe assays in the registry (2026-10-14), 22 are MGB, whose minor-groove binder
    adds roughly 15-20 C of Tm, and the other 22 are plain hydrolysis probes. The MGB
    probes tolerate mismatches a bare oligo of the same length would not, and
    nothing here knows that. `--thermo` computes the actual duplex ΔTm and is the
    better guide where it is available.

    Takes the oligo rather than its length (it did take the length until
    2026-10-26) so that it can record the mispair identities for replay, the same
    as `score_primer`. The `@distance` in a probe's mispair is still measured from
    its 3' end, for one format across all three oligos, and means less here: a
    probe has no 3' asymmetry, which is this function's whole premise.
    """
    s = cfg["scoring"]
    oligo_len = len(oligo)
    lo, hi = oligo_len / 3, 2 * oligo_len / 3
    penalty = 0.0
    mispairs: list[str] = []
    for pos in site.mismatches:
        penalty += s["probe_center_penalty"] if lo <= pos < hi else s["probe_outer_penalty"]
        rec = site.window[pos] if pos < len(site.window) else "N"
        template = COMPLEMENT.get(rec.upper(), "N")
        mispairs.append(f"{oligo[pos].upper()}:{template}@{oligo_len - pos}")
    return OligoScore(
        penalty,
        False,
        site.mismatches,
        tuple(oligo_len - p for p in site.mismatches),
        site.ambiguous,
        tuple(mispairs),
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

        def pairs(o: OligoScore | None) -> str:
            # Same shape as `mm`: empty for an unscored oligo AND for a clean one,
            # which is why `drift.FOOTPRINT_REQUIRED` tests the penalty cells
            # rather than these to tell "no mismatches" from "column absent".
            return "" if o is None else ",".join(o.mispairs)

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
            # For no_amplicon only: the best lone primer site's per-record E-value, so
            # the archive-scale anchor test (calls.apply_anchor_fdr) can run at report time.
            "anchor_evalue": f"{self.extra['anchor_evalue']:.2g}" if "anchor_evalue" in self.extra else "",
            "fwd_penalty": "" if self.forward is None else f"{self.forward.penalty:g}",
            "fwd_mm_from_3prime": mm(self.forward),
            "fwd_ambiguous": amb(self.forward),
            "rev_penalty": "" if self.reverse is None else f"{self.reverse.penalty:g}",
            "rev_mm_from_3prime": mm(self.reverse),
            "rev_ambiguous": amb(self.reverse),
            "probe_penalty": "" if self.probe is None else f"{self.probe.penalty:g}",
            "probe_mm_from_3prime": mm(self.probe),
            "probe_ambiguous": amb(self.probe),
            # WHAT each mismatch is, beside WHERE: `A:G@2,T:C@14`, oligo base to
            # template base at distance from the 3' end. The screen computed this
            # and discarded it, which is why every scoring candidate so far cost a
            # full rescreen to price; with it a candidate is a replay over this
            # table (docs/journal/2026-10-24-scoring-strategy-test-plan.md Part 0.1).
            #
            # DELIBERATELY NOT in `drift.FOOTPRINT_COLUMNS`. That signature
            # records positions and not bases on purpose - "two records with
            # different bases at the same position merge. That makes footprints
            # fewer and the resulting interval wider: the safe direction" - and
            # adding identity to it would regroup the duplication analysis and
            # move published intervals. These columns are additive and read only
            # by a replay. Making the footprint identity-aware is a separate
            # decision, which that docstring's "honest limits" already anticipates.
            "fwd_mispairs": pairs(self.forward),
            "rev_mispairs": pairs(self.reverse),
            "probe_mispairs": pairs(self.probe),
            "degeneracy_fold": self.extra.get("degeneracy_fold", ""),
            "degeneracy_tier": self.extra.get("degeneracy_tier", ""),
            # For multiplex assays with alternates: which F/R primer names won.
            "winning_pair": self.extra.get("winning_pair", ""),
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
    """Turn one summed penalty into a call. `scoring.engine: budget` only.

    Two known weaknesses, both biological rather than numerical:

    * The total SUMS forward, reverse and probe, but they are serial gates, not
      a shared budget: amplification needs both primers, and detection needs
      the probe on top. Three trivial mismatches spread one per oligo land in
      the same bin as one near-lethal 3'-proximal mismatch, and a probe defect
      (which costs signal linearly) trades against a primer defect (which costs
      the exponential). Per-oligo verdicts combined logically is the right
      model; see docs/journal/2026-10-04-pipeline-review.md. That model now exists as
      `scoring.engine: serial` (`oligo_verdict` + `combine`), and the two
      disagree on 182,185 of 912,111 calls - but it is `budget` that
      `detect_max` and `reduced_max` were set against, so it stays the default
      until the per-oligo thresholds are calibrated.
    * `terminal` is identity-blind, so about half the 3'-terminal mismatches it
      fails are the near-neutral kind (see score_primer). It is also one
      threshold for 167 conventional PCRs and 44 probe assays (2026-10-14), and endpoint PCR
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


# The order `combine` reports a blocked or weak oligo in, so a reason string is
# deterministic and reads the way the assay does.
ROLES = ("forward", "reverse", "probe")


def oligo_verdict(score: OligoScore, cfg: dict[str, Any]) -> str:
    """One oligo's own verdict: `ok`, `weak` or `blocked`.

    This is half of what `classify`'s docstring says the right model is. The
    other half is `combine`. Neither is used unless `scoring.engine` is
    `serial`.

    A 3'-terminal mismatch blocks the oligo that carries it rather than failing
    the whole call from outside, which is the same outcome with the oligo named.
    `score_probe` never sets `terminal_mismatch`, so this reads the same for a
    probe without needing to know it is one.
    """
    s = cfg["scoring"]
    if score.terminal_mismatch and s.get("terminal_mismatch_fails", True):
        return "blocked"
    if score.penalty <= s["oligo_ok_max"]:
        return "ok"
    if score.penalty <= s["oligo_weak_max"]:
        return "weak"
    return "blocked"


def combine(verdicts: dict[str, str], cfg: dict[str, Any]) -> tuple[str, str]:
    """Per-oligo verdicts into one call and the reason for it.

    Serial gates, not a shared budget: PCR needs the forward AND the reverse
    primer to anneal, and a probe assay needs the probe on top of both. So one
    blocked oligo fails the call however well the others match, and three
    trivial mismatches spread one per oligo are three `ok`s rather than a
    summed 3.0 - which under `engine: budget` lands in the same bin as one
    near-lethal 3'-proximal mismatch.

    `cfg` is unused today and is taken anyway: every other decision function
    here reads its thresholds from it, and a caller should not have to know
    that this one happens not to.
    """
    del cfg  # see the docstring
    blocked = [r for r in ROLES if verdicts.get(r) == "blocked"]
    if blocked:
        return "fail", f"{', '.join(blocked)} blocked"
    weak = [r for r in ROLES if verdicts.get(r) == "weak"]
    if weak:
        return "reduced", f"{', '.join(weak)} weak"
    return "detect", ""


def decide(
    fs: OligoScore, rs: OligoScore, ps: OligoScore | None, cfg: dict[str, Any]
) -> tuple[str, str, float]:
    """One candidate amplicon's call, its reason, and the scalar standing for it.

    The single place the two engines differ, so the `budget` path is the one
    that existed before `serial` was added rather than a reimplementation of it.

    The third value is what `Call.penalty` carries and what breaks ties between
    the candidate amplicons of one record. Under `budget` it is the sum, which
    is the quantity the call was made from. Under `serial` it is the WORST
    single oligo, for the same reason: it is what decided the call, it is still
    monotone in badness, and summing it would rank a candidate by a number no
    threshold in the config compares against.
    """
    s = cfg["scoring"]
    if s.get("engine", "budget") == "serial":
        scored = zip(ROLES, (fs, rs, ps), strict=True)  # ROLES is forward, reverse, probe
        verdicts = {r: oligo_verdict(o, cfg) for r, o in scored if o is not None}
        call, reason = combine(verdicts, cfg)
        return call, reason, max(o.penalty for o in (fs, rs, ps) if o is not None)
    total = fs.penalty + rs.penalty + (ps.penalty if ps else 0.0)
    return classify(total, fs.terminal_mismatch or rs.terminal_mismatch, cfg), "", total


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

    def __init__(self, sites: list[Site]) -> None:
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


def oligo_pool_names(assay: Assay) -> tuple[dict[str, str], dict[str, str]]:
    """Sequence-to-name maps for forward and reverse pool members.

    Returns ({fwd_seq: name, ...}, {rev_seq: name, ...}). The primary oligos
    come first; alternates are added by orientation. Names come from the
    ``name`` field on each Oligo. An oligo with no name gets an empty string.
    """
    fwd_names: dict[str, str] = {
        assay.oligos.forward.matching_seq: assay.oligos.forward.name or "",
    }
    rev_names: dict[str, str] = {
        assay.oligos.reverse.matching_seq: assay.oligos.reverse.name or "",
    }
    for alt in assay.oligos.alternates or []:
        bucket = {"forward": fwd_names, "reverse": rev_names}.get(alt.orientation or "")
        if bucket is not None and alt.matching_seq not in bucket:
            bucket[alt.matching_seq] = alt.name or ""
    return fwd_names, rev_names


def screen_record(
    assay: Assay,
    record_id: str,
    record_seq: str,
    cfg: dict[str, Any],
    comp: tuple | None = None,
    *,
    record_len: int | None = None,
) -> Call:
    """Best call for `assay` in one record, over every combination of its primer pools.

    With no pool members this is one call of `screen_one`, which is the whole
    of the scoring logic; with pools it is the best call over the cross product,
    and `extra["pool"]` names the primers that won.

    The split exists so that every pool combination goes through exactly the same
    scoring path as a plain assay: there is one implementation of the rules, and
    pooling is a loop around it rather than a second code path.

    This is where the chemistry's scoring block is resolved for SCREENING, and it
    is the only place: `screen_one` is called from here and nowhere else, so every
    caller that screens reaches the right numbers without knowing they exist. Code
    that reads `cfg["scoring"]` itself does NOT get that for free and has to call
    `config_for` (as `scripts/indel_check.py` now does per assay) or, where it has
    no assay, `max_mismatches_searched` (as the assembly pre-cut does). With no
    overrides configured `config_for` hands back the same cfg object, so the
    default path is unchanged.
    """
    cfg = config_for(assay.chemistry, cfg)
    fwd, rev, probe = oligo_pools(assay)
    if len(fwd) == 1 and len(rev) == 1 and len(probe) <= 1:
        return screen_one(assay, record_id, record_seq, cfg, comp, record_len=record_len)
    if comp is None:
        comp = composition(record_seq)
    fwd_names, rev_names = oligo_pool_names(assay)
    best: Call | None = None
    for f in fwd:
        for r in rev:
            cand = screen_one(
                assay, record_id, record_seq, cfg, comp, f, r, probe or [None], record_len=record_len
            )
            key = (_call_rank(cand.call, cand.reason), cand.penalty if cand.penalty is not None else 1e9)
            if best is None or key < (
                _call_rank(best.call, best.reason),
                best.penalty if best.penalty is not None else 1e9,
            ):
                best = cand
                best.extra["pool"] = f"forward={f} reverse={r}"
                fn = fwd_names.get(f, "")
                rn = rev_names.get(r, "")
                best.extra["winning_pair"] = f"{fn}/{rn}" if fn or rn else ""
    assert best is not None
    return best


def _site_text(site: Site | None) -> str:
    return "" if site is None else f"{site.start}-{site.end}{site.strand}"


def declared_ends(assay: Assay) -> list[int] | None:
    """The assay's declared product size as `[lo, hi]`, or None if it declares none.

    A scalar becomes `[bp, bp]`, so one expression serves both shapes: an assay
    may declare a point size or, where its product size is genuinely a range it
    is designed to read apart, two ends.

    Shared rather than open-coded because the two readers disagreed. `screen_one`
    had this derivation inline and handled a range correctly; `classify_exclusion`
    was handed `assay.amplicon_bp` alone, so a range-declaring assay fell through
    to `amplicon.max_bp` and had its truncated-versus-diverged geometry judged
    against 3000 bp rather than its own ceiling - ORTHOPOXVIRUS ATI, whose range
    tops out at 1700, and every entry converted from a scalar after 2026-10-21.
    """
    rng = getattr(assay, "amplicon_bp_range", None)
    if rng:
        return [int(rng[0]), int(rng[1])]
    return [assay.amplicon_bp, assay.amplicon_bp] if assay.amplicon_bp else None


def classify_exclusion(
    record_seq: str,
    oligos: dict[str, str],
    found: dict[str, list[Site]],
    cfg: dict[str, Any],
    comp: tuple,
    amplicon_span: int | None,
    record_len: int | None = None,
) -> tuple[str, str, float | None]:
    """Why a record yielded no amplicon: (label, one-line detail, best lone-site E).

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

    The third value is the lowest per-record E-value among every site found for
    either primer, or None when nothing was found within the search budget. It is
    written to the row (`anchor_evalue`) because the per-record credibility test
    below cannot see multiplicity: a 22-mer six mismatches off has E of about 0.005
    in a 900 bp record, which passes 0.01, and an archive of 9,496 such records is
    expected to produce dozens of them - 55 of Bd's 63 `diverged` records are
    protein-coding mRNAs anchored that way (docs/journal/2026-10-23-wave2-diverged-and-patent.md).
    The archive-scale test that corrects this needs every row's E first, so it
    runs at report time over the calls table (`calls.apply_anchor_fdr`,
    `drift.anchor_fdr`), and this function only records the number.
    """
    # Its own key: `max_pair_evalue: null` means "report the E-value, act on
    # nothing", and reusing it here silently kept filtering at 0.01.
    max_e = float(cfg["scoring"].get("max_site_evalue", 0.01))
    # The declared upper end, from `declared_ends`, NOT `assay.amplicon_bp`: a
    # range-declaring assay has no scalar and used to fall through to max_bp.
    span = int(amplicon_span or cfg["amplicon"]["max_bp"])
    n = record_len or len(record_seq)

    def with_evalue(name: str) -> list[tuple[Site, float]]:
        o = oligos[name]
        return [(s, site_evalue(o, s.n_mismatches + s.n_ambiguous, n, comp)) for s in found.get(name, [])]

    ef, er = with_evalue("forward"), with_evalue("reverse")
    best_e = min((e for _, e in ef + er), default=None)
    cf = [s for s, e in ef if e <= max_e]
    cr = [s for s, e in er if e <= max_e]
    if cf and cr:
        return "no_pair", "both primers match credibly but never face each other in range", best_e
    if not cf and not cr:
        return "no_site", "no credible site for either primer", best_e
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
        return "truncated", f"the record ends before the {missing} primer's window", best_e
    return "diverged", f"the {missing} primer's window is present but nothing credible matches it", best_e


def screen_one(
    assay: Assay,
    record_id: str,
    record_seq: str,
    cfg: dict[str, Any],
    comp: tuple | None = None,
    fwd_seq: str | None = None,
    rev_seq: str | None = None,
    probe_seqs: list[str | None] | None = None,
    *,
    record_len: int | None = None,
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
    # Both the size window below and `classify_exclusion`'s truncated-versus-
    # diverged geometry need the declared size, and the early no-site return
    # reaches the latter first, so it is resolved once here.
    declared = declared_ends(assay)
    _declared_hi = declared[1] if declared else None
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
        label, detail, anchor_e = classify_exclusion(
            record_seq, oligo_map, found_map, cfg, comp, _declared_hi, record_len
        )
        call.extra["exclusion"] = label
        if anchor_e is not None:
            call.extra["anchor_evalue"] = anchor_e
        call.reason = f"{call.reason}; {detail}"
        return call

    pairs = facing_pairs(f_all, r_all, len(rev), amp)
    # A pathological record (long low-complexity runs) can still produce a huge
    # number of pairs; keep the best-matched ones. This applies to pairs, never
    # to single sites: a cap on sites before pairing could drop the true site of a
    # genome in favour of fifty better-looking chance sites elsewhere.
    cap = int(cfg["scoring"].get("max_pairs_per_record", 5000))
    # Always in rank order, not only when over the cap. Candidates that tie on call,
    # penalty and ambiguity (two copies of a multicopy target, say) go to the first one
    # evaluated, and sorting only above the cap made that depend on how many chance
    # pairs the REST of the record held: a genome reported one copy and the same
    # stretch cut out of it reported another.
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
    # An assay may declare a point size or, where its product size is genuinely
    # a range it is designed to read apart, two ends. The tolerance applies
    # outward from each end either way.
    if declared and tol is not None:
        tol = float(tol)
        lo_bp = max(lo_bp, int(declared[0] * (1 - tol)))
        hi_bp = min(hi_bp, int(declared[1] * (1 + tol)))
    # The chance guard has to ask its question about the window this screen will
    # actually accept. Left at the global range it counts reverse-primer offsets
    # the size filter has already ruled out, overstating E by the ratio of the
    # two windows (30x for a 194 bp assay at +/-25%: 2951 bp against 98) and
    # pushing the
    # worst-matching - that is, the drifted - pairs out of the denominator.
    window_bp = hi_bp - lo_bp + 1

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
            record_len or len(record_seq),
            cfg,
            comp,
            window_bp=window_bp,
        )
        if max_e is not None and evalue > max_e:
            n_chance += 1
            continue
        fs = score_primer(f, fwd, cfg)
        rs = score_primer(r, rev, cfg)
        ps, p_site, reason = None, None, ""
        probe_won = probe
        if probe:
            scored = [
                (score_probe(p, o, cfg), p, o)
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
        call, verdict_reason, total = decide(fs, rs, ps, cfg)
        scores = [o for o in (fs, rs, ps) if o is not None]
        n_amb = sum(len(o.ambiguous) for o in scores)
        if too_ambiguous(scores, cfg):
            call = "indeterminate"
            reason = reason or f"{n_amb} undetermined record bases under the oligos"
        elif reason:
            # A probe-less amplicon: already decided, and `_call_rank` matches
            # this exact string, so it must survive whatever `decide` said.
            call = "fail"
        else:
            reason = verdict_reason
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
        label, detail, anchor_e = classify_exclusion(
            record_seq, oligo_map, found_map, cfg, comp, _declared_hi, record_len
        )
        call.extra["exclusion"] = "chance_only" if n_chance else label
        if anchor_e is not None:
            call.extra["anchor_evalue"] = anchor_e
        call.reason = f"{reason}; {detail}"
        return call
    return best
