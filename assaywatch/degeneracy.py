"""What an assay's degeneracy means, and what it does to the drift signal.

A degenerate primer is a mixture. An oligo written with one Y is synthesised
as two molecules; one with ten degenerate positions can be thousands. Only the
members whose sequence matches the template amplify it, so the concentration
that actually participates in the reaction is roughly the nominal
concentration divided by the pool size. That costs sensitivity: later Cq, a
higher limit of detection, and more non-specific priming from the members that
match nothing in particular.

How the three oligos combine
----------------------------

The folds multiply, but the three terms do not mean the same thing, and the
distinction decides how to read a large number.

Primer dilution attacks amplification. Annealing is pseudo-first-order in
primer concentration, so once the matching member falls far enough below the
usual 200-900 nM the annealing step no longer goes to completion and the
per-cycle efficiency drops. Efficiency sits in the base of the exponential:
yield is proportional to (1 + E)^cycles, so a deficit compounds and in the
limit the reaction simply does not take off. That is a coverage failure.

Probe dilution attacks the readout. A hydrolysis probe is cleaved from the
amplicon and is not part of the amplification mechanism, so a diluted probe
does not slow the reaction; it reports a smaller share of the amplicons that
were made. Scaling the signal by a constant factor 1/n means the amplicon
count has to be n-fold higher to cross the threshold, and since amplicon count
doubles per cycle, that is a fixed offset of about log2(n) cycles. A 16-fold
degenerate probe costs roughly four cycles of Cq and nothing else. That is a
sensitivity cost, not a coverage failure.

So the product of all three folds is the right single number for "what
fraction of the synthesised reagent participates in detecting this template",
and its log2 is a first-order estimate of the total Cq delay, because the
log of a product is the sum of the logs. It is reported as `total_fold`, and
it is what the tiers key on. But `pair_fold` and `probe_fold` stay visible,
because an assay at 4096-fold that is all primers is in different trouble from
one that is all probe: the first may not amplify, the second amplifies fine
and reports late. In this registry that distinction is academic for now, since
only four assays have a degenerate probe and all four are 2-fold.

Two consequences for AssayWatch, and they pull in opposite directions.

1. Degeneracy must not be scored as drift. Which member of the pool binds a
   given record is not information about whether the target has changed, and
   penalising it would flag every pan-family assay as broken on day one. The
   scorer therefore charges nothing for a degenerate position that covers the
   record's base (see score.py).

2. For the same reason, a `detect` call on a heavily degenerate assay is weak
   evidence that the assay works. An oligo full of N matches everything by
   construction, so the in-silico result approaches a tautology. The drift
   metric cannot see this, which makes it the kind of thing that must be
   reported next to the metric rather than folded into it.

This module computes the accounting for (2). It deliberately produces no
penalty and feeds nothing back into the per-record call.

Inosine is counted as one molecule, not as a degenerate position. An
inosine-containing primer is a single compound that pairs promiscuously, so it
pays no concentration cost at all; that is exactly why primer designers reach
for it instead of N. The registry stores inosine positions as N in `seq`
(to keep that field strict IUPAC) and keeps the original in `seq_as_written`,
so this module reads `seq_as_written` where it exists. Counting from `seq`
instead inflates the PREDICT filovirus reverse primer from 8-fold to
8192-fold, which is the difference between a usable assay and an unusable one.

Tier boundaries are judgement calls, documented here so they can be argued
with, and they live in config.yaml so they can be changed without touching
code:

    negligible  <= 8      a few wobble positions; no practical effect
    moderate    <= 128    routine for consensus PCR; expect a modest Cq shift
    high        <= 4096   sensitivity is materially reduced; endpoint PCR territory
    severe      >  4096   each member is a trace component; an in-silico
                          `detect` says almost nothing about the bench
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any

from assaywatch.iupac import SINGLE_MOLECULE, degeneracy
from assaywatch.schema import Assay

DEFAULT_TIERS: list[tuple[int, str]] = [
    (8, "negligible"),
    (128, "moderate"),
    (4096, "high"),
]


# Why degeneracy is reported and never scored: a degenerate position is not a
# defect, it is the whole point of a consensus primer, and penalising it would
# mark every pan-family assay as broken. What it does cost is concentration —
# each pool member is a fraction of the reaction — so it travels beside every
# call as context a reader cannot miss, rather than inside the call.
def matching_sequence(oligo) -> str:
    """The sequence to compare against records: as written, inosine included, 5' tail excluded."""
    return oligo.matching_seq


def tier_for(fold: int, cfg: dict[str, Any] | None = None) -> str:
    tiers = DEFAULT_TIERS
    if cfg:
        configured = cfg.get("degeneracy", {}).get("tiers")
        if configured:
            tiers = [(int(limit), name) for limit, name in configured]
    for limit, name in tiers:
        if fold <= limit:
            return name
    return "severe"


@dataclass
class OligoDegeneracy:
    name: str
    role: str
    length: int
    fold: int
    inosine: int
    degenerate_positions: int

    @property
    def effective_fraction(self) -> float:
        """Share of the synthesised pool that matches any one template."""
        return 1.0 / self.fold


@dataclass
class AssayDegeneracy:
    assay_id: str
    oligos: list[OligoDegeneracy] = field(default_factory=list)

    @property
    def pair_fold(self) -> int:
        """Pool size of the primer pair: the amplification-side risk."""
        f = 1
        for o in self.oligos:
            if o.role in {"forward", "reverse"}:
                f *= o.fold
        return f

    @property
    def probe_fold(self) -> int:
        """Pool size of the probe, or 1 when there is none: the readout-side cost."""
        return next((o.fold for o in self.oligos if o.role == "probe"), 1)

    @property
    def total_fold(self) -> int:
        """Every oligo multiplied: the share of synthesised reagent that participates."""
        return self.pair_fold * self.probe_fold

    @property
    def expected_cq_delay(self) -> float:
        """log2(total_fold): a first-order, optimistic estimate of the Cq shift.

        Optimistic because it treats every dilution as a pure offset. That is
        about right for the probe, which only scales the signal, but primer
        dilution also degrades per-cycle efficiency, and an efficiency loss
        compounds. Read this as a lower bound on the delay, and as no
        guarantee that the reaction works at all at the high end.
        """
        return math.log2(self.total_fold)

    @property
    def max_oligo_fold(self) -> int:
        return max((o.fold for o in self.oligos), default=1)

    @property
    def inosine_positions(self) -> int:
        return sum(o.inosine for o in self.oligos)

    def tier(self, cfg: dict[str, Any] | None = None) -> str:
        return tier_for(self.total_fold, cfg)

    def note(self, cfg: dict[str, Any] | None = None) -> str:
        """One line for the report, saying how much a `detect` call is worth."""
        t = self.tier(cfg)
        if t == "negligible":
            return ""
        split = f"{self.pair_fold}-fold primers x {self.probe_fold}-fold probe"
        delay = f"~{self.expected_cq_delay:.0f} cycles of Cq delay at best"
        if t == "moderate":
            return f"{self.total_fold}-fold degenerate ({split}); {delay}"
        if t == "high":
            return (
                f"{self.total_fold}-fold degenerate ({split}); each member is "
                f"~{1 / self.total_fold:.1e} of the reaction, {delay}, and bench "
                "sensitivity is well below in-silico coverage"
            )
        return (
            f"{self.total_fold}-fold degenerate ({split}); {delay} if it amplifies at all. "
            "In-silico detection is close to a tautology here and says little about whether "
            "this assay works"
        )


def assay_degeneracy(assay: Assay) -> AssayDegeneracy:
    out = AssayDegeneracy(assay.id)
    pairs = [("forward", assay.oligos.forward), ("reverse", assay.oligos.reverse)]
    if assay.oligos.probe is not None:
        pairs.append(("probe", assay.oligos.probe))
    for role, oligo in pairs:
        seq = matching_sequence(oligo)
        out.oligos.append(
            OligoDegeneracy(
                name=oligo.name or role,
                role=role,
                length=len(seq),
                fold=degeneracy(seq),
                inosine=seq.count("I"),
                degenerate_positions=sum(1 for b in seq if b not in SINGLE_MOLECULE),
            )
        )
    return out


def main(argv: list[str] | None = None) -> int:
    """`python -m assaywatch.degeneracy registry` -> a table, worst first."""
    import argparse
    from pathlib import Path

    from assaywatch.score import load_config
    from assaywatch.validate import iter_files, load_assay

    ap = argparse.ArgumentParser(description="Report primer-pool degeneracy per assay.")
    ap.add_argument("paths", nargs="+", type=Path)
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--tier", default=None, help="only show this tier")
    ap.add_argument("--tsv", action="store_true", help="tab-separated with a header, for other programs")
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    tiers = [name for _, name in (cfg.get("degeneracy", {}).get("tiers") or DEFAULT_TIERS)] + ["severe"]
    if args.tier is not None and args.tier not in tiers:
        ap.error(f"--tier must be one of {', '.join(tiers)}")
    rows = []
    for target in args.paths:
        for path in iter_files(target):
            d = assay_degeneracy(load_assay(path))
            rows.append(
                (
                    d.total_fold,
                    d.pair_fold,
                    d.probe_fold,
                    d.expected_cq_delay,
                    d.inosine_positions,
                    d.tier(cfg),
                    d.assay_id,
                )
            )
    rows.sort(reverse=True)
    if args.tier:
        rows = [r for r in rows if r[5] == args.tier]

    if args.tsv:
        print("assay_id\ttotal_fold\tprimer_fold\tprobe_fold\texpected_cq_delay\tinosine_positions\ttier")
        for total, pair, probe, dcq, ino, tier, aid in rows:
            print(f"{aid}\t{total}\t{pair}\t{probe}\t{dcq:.1f}\t{ino}\t{tier}")
        return 0

    width = max((len(r[6]) for r in rows), default=10)
    print(f"{'assay':<{width}}  {'total':>12}  {'primers':>12}  {'probe':>5}  {'dCq':>5}  {'I':>3}  tier")
    for total, pair, probe, dcq, ino, tier, aid in rows:
        print(f"{aid:<{width}}  {total:>12}  {pair:>12}  {probe:>5}  {dcq:>5.1f}  {ino:>3}  {tier}")
    counts: dict[str, int] = {}
    for r in rows:
        counts[r[5]] = counts.get(r[5], 0) + 1
    print(f"\n{len(rows)} assays: {counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
