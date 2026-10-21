"""Turn a table of per-record calls into a per-assay statement about drift.

The question is narrow: of the sequences that this assay could be judged
against, is the share it is predicted to detect falling, and is the fall large
enough and supported by enough records to act on?

What counts in the denominator
------------------------------
Only `detect`, `reduced` and `fail` records. Those are the ones where both
primers landed, in the right orientation, within the amplicon size range, so
the call is a statement about the assay.

`no_amplicon` and `indeterminate` are counted and shown but kept out of the
fraction. A record missing the locus entirely, or truncated, or full of
ambiguity codes, says something about GenBank rather than about the assay, and
folding it in would let a bad sequencing year look exactly like drift. The
evaluable count is printed next to every fraction so a denominator of four is
visible rather than hidden behind a percentage.

Why confidence intervals and not just the fraction
--------------------------------------------------
A new assay against a sparsely sequenced wildlife pathogen may have five
records in the last two years. Three of them failing is 60 percent detected,
which looks alarming and means almost nothing: with n = 5 the 95 percent
interval runs from roughly 15 to 95 percent. Flagging on the point estimate
alone would bury the real signals under noise from exactly the taxa this tool
exists to serve.

So an assay is flagged only when the *upper* bound of the interval for the recent
window falls below the threshold: the data must be inconsistent with the assay
still working, not merely consistent with it failing. The interval is the
Wilson score interval rather than the textbook normal approximation, because
the normal one misbehaves badly near 0 and 1 (it can produce bounds outside
[0, 1], and at k = n it collapses to zero width, claiming certainty from a
handful of records).

The change from baseline uses the Newcombe hybrid-score interval, which builds
a confidence interval for the difference of two proportions out of each one's
Wilson interval. It keeps the good behaviour at the extremes, which matters
here because baselines are usually near 100 percent.

Both are closed-form arithmetic, so there is no scipy dependency and every
number in the report can be recomputed by hand from the counts.

What the fraction is actually estimating, and what it is not
-----------------------------------------------------------
The intervals above assume the records are independent draws from the
population the assay is used on. Neither half of that is true, and a reader
has to carry the gap:

1. **GenBank is a sample of sequencing effort.** An outbreak produces hundreds
   of near-identical deposits from one transmission chain; endemic background
   produces none. So the effective sample size is the number of independent
   lineages, not the number of records, and the Wilson interval is narrower
   than the evidence warrants — sometimes by an order of magnitude. Clustering
   the records and weighting by cluster is the fix; see the review doc.

2. **Deposition is correlated with detection.** A locus is often sequenced
   *because* an assay amplified it, so matching sequences are enriched and a
   variant that escapes PCR may never be deposited at all. The bias runs toward
   optimism, which makes `declining` strong evidence and `stable` weak
   evidence. They are not symmetric and should not be read as if they were.

3. **The estimand is wrong for most real failures.** One proportion per assay
   answers "what share of deposited sequences match". Published assay failures
   are almost never that shape: they are "fails on clade B", "fails on the
   lineage circulating in West Africa", "fails on the fish ranaviruses it was
   never meant to cover". A clade that is 5 percent of deposits can be 100
   percent of a region's cases, and averaging it away is why the tool catches
   only 1 of the 12 documented failures in docs/validation-cases.tsv. Per-clade
   or per-haplotype fractions are the real fix.

Consequently: a status here is a reading assignment, not a measurement. The
report prints the counts so that a reader can disagree with the verdict.
"""

from __future__ import annotations

import math
import sys
from collections import Counter, defaultdict
from collections.abc import Iterable
from dataclasses import dataclass, field
from datetime import date
from typing import TYPE_CHECKING, Any

from assaywatch.accession import strip_version

if TYPE_CHECKING:
    from assaywatch.lineage import LineageStats
    from assaywatch.taxonomy import Taxonomy

EVALUABLE = ("detect", "reduced", "fail")
Z95 = 1.959963984540054

# The verdict vocabulary, owned here because this is the only module that assigns
# one. Worst first, which is also the order the report prints its sections in.
# `NO_DATA` is the AssayDrift default and not a verdict `assess` reaches, so it is
# kept out of the order and included in STATUSES.
#
# Exported because two consumers used to hardcode their own copy: report.py's
# section order and scripts/report_diff.py's row parser. The copies were what let
# report_diff read "## Nested protocols" as a status and drop 21 assays out of
# their real ones, so neither run's buckets summed to its own assay count.
# test_drift.py asserts this matches the literals assess actually assigns.
STATUS_ORDER = (
    "declining",
    "low coverage",
    "watch",
    "insufficient data",
    "no recent data",
    "stable",
)
NO_DATA = "no data"
STATUSES = frozenset(STATUS_ORDER) | {NO_DATA}

# The screen columns that together say how a record's binding sites differ from
# the assay: each oligo's mismatch positions (counted from its 3' end) and the
# NUMBER of its undetermined record bases (`Call.as_row` writes a count there, not
# positions). Two records that agree on all six, and on the call, are
# indistinguishable AS FAR AS THIS ASSAY IS CONCERNED - which is the only sense in
# which they can be called the same lineage here.
FOOTPRINT_COLUMNS = (
    "fwd_mm_from_3prime",
    "rev_mm_from_3prime",
    "probe_mm_from_3prime",
    "fwd_ambiguous",
    "rev_ambiguous",
    "probe_ambiguous",
)

# A row's footprint is KNOWN only if these are populated. Every evaluable call
# (detect, reduced, fail) has both primers scored, so in any schema that writes the
# footprint these four cells are non-empty; blank means the row came from a screen
# that did not write them. That matters because `collect.concatenate_screens` fills
# a column an older screen lacks with an empty string, and an empty string is also
# what a record with no mismatches puts in the mismatch columns: without this test
# an older screen's rows would be read as a real footprint that happens to be
# clean, and a claim about duplication would be invented from missing data.
FOOTPRINT_REQUIRED = ("fwd_penalty", "rev_penalty", "fwd_ambiguous", "rev_ambiguous")


def footprint_signature(values: Iterable[str]) -> str:
    """One record's footprint as a single interned string.

    Interned because the point of the exercise is that millions of records share
    a few thousand footprints - an assay with no mismatches is the same short
    string every time (`|||0|0|0` for a scored forward, reverse and probe) - and
    `report.read_calls` exists because holding two million rows in full took 3.6 GB.
    Equal signatures are then one object, not two million.

    HONEST LIMITS, both of which matter:

    - It records mismatch POSITIONS, not bases, so two records with different
      bases at the same position merge. That makes footprints fewer and the
      resulting interval wider: the safe direction.
    - A sequencing error in a primer site creates a footprint of its own, so
      noise inflates the footprint count and narrows the interval: the unsafe
      direction. With the amount of GenBank deposited from one lab's raw reads
      this will not be negligible for some assays, and it is why the count is
      reported next to the record count rather than replacing it.
    """
    return sys.intern("|".join(values))


def wilson_interval(k: int, n: int, z: float = Z95) -> tuple[float, float]:
    """Wilson score interval for a binomial proportion. (0, 1) when n == 0."""
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = (z / d) * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (max(0.0, centre - half), min(1.0, centre + half))


def newcombe_difference(k1: int, n1: int, k2: int, n2: int, z: float = Z95) -> tuple[float, float]:
    """CI for p1 - p2 (recent minus baseline) from the two Wilson intervals."""
    if n1 == 0 or n2 == 0:
        return (-1.0, 1.0)
    p1, p2 = k1 / n1, k2 / n2
    l1, u1 = wilson_interval(k1, n1, z)
    l2, u2 = wilson_interval(k2, n2, z)
    lower = (p1 - p2) - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2)
    upper = (p1 - p2) + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)
    return (max(-1.0, lower), min(1.0, upper))


@dataclass
class YearStats:
    year: int
    counts: Counter = field(default_factory=Counter)

    @property
    def evaluable(self) -> int:
        return sum(self.counts[c] for c in EVALUABLE)

    @property
    def detected(self) -> int:
        """`reduced` counts as detected: it amplifies, just later."""
        return self.counts["detect"] + self.counts["reduced"]

    @property
    def fraction(self) -> float | None:
        return self.detected / self.evaluable if self.evaluable else None


@dataclass
class AssayDrift:
    assay_id: str
    years: dict[int, YearStats] = field(default_factory=dict)
    recent_from: int | str = 0  # a year, or an ISO date when records are dated to the day
    threshold: float = 0.9
    min_records: int = 20
    min_decline: float = 0.0  # smallest fall from baseline that counts as declining
    # `declining` additionally requires the baseline to have been at or above
    # `threshold`: a fall from a baseline that never cleared it is not drift.
    require_working_baseline: bool = True
    # Evaluable records a single year needs before it can be the evidence that
    # the assay once worked (see `ever_worked`).
    min_records_for_year: int = 10
    window_months: int = 0  # the recent window actually used, after any widening
    # The first year of the recent window. `recent_from` is for display and is
    # a month name when records are dated to the day, so it cannot be parsed
    # back into a year; `finalise`'s fallback split needs the number.
    recent_year: int | None = None
    # Calls split by the recent-window cutoff as records are added (assess). When
    # empty, finalise falls back to splitting `years` at `recent_from`.
    recent_counts: Counter = field(default_factory=Counter)
    baseline_counts: Counter = field(default_factory=Counter)
    skipped_undated: int = 0
    # Why unusable records were unusable, from score.classify_exclusion.
    exclusions: Counter = field(default_factory=Counter)

    # Filled by `finalise`.
    recent_detected: int = 0
    recent_evaluable: int = 0
    baseline_detected: int = 0
    baseline_evaluable: int = 0
    recent_ci: tuple[float, float] = (0.0, 1.0)
    baseline_ci: tuple[float, float] = (0.0, 1.0)
    change_ci: tuple[float, float] = (-1.0, 1.0)
    status: str = NO_DATA
    note: str = ""

    # Lineage-level robustness, from the records' footprints (see
    # `footprint_signature`). Set by `assess`; None when the rows carried no
    # footprint, which is every hand-built test row and every calls table
    # screened before these columns were read. NEVER scored: `status` above is
    # computed without any of this, exactly as degeneracy and thermodynamics are
    # reported beside a call and never fed into it.
    recent_footprints: int | None = None  # distinct (call, footprint) among evaluable recent records
    baseline_footprints: int | None = None
    # How many of those recent classes are `detect` or `reduced`: the numerator of
    # the share you get by counting each footprint once.
    recent_footprints_detected: int | None = None
    recent_ci_clustered: tuple[float, float] = (0.0, 1.0)
    # Wilson interval on `recent_footprints_detected` of `recent_footprints`.
    recent_ci_by_footprint: tuple[float, float] = (0.0, 1.0)
    change_ci_clustered: tuple[float, float] = (-1.0, 1.0)
    # For a flagged assay only: does the flag still hold at the clustered
    # interval? None for every other status, and when footprints are unknown.
    flag_survives_clustering: bool | None = None
    # Why a flag did not survive, as codes: "too_few" (fewer distinct footprints
    # than min_records), "recent" (the recent interval, at the number of
    # footprints as its sample size, reaches the threshold), "footprint" (counting
    # each footprint once, the share amplifying reaches the threshold), "change" (a
    # declining assay's fall from baseline no longer excludes zero at that sample
    # size). Empty when it survived or was not checked.
    cluster_failures: tuple[str, ...] = ()

    # Out-of-scope records: when the assay's scope_taxids is set, records
    # whose taxid is not in the scope set are excluded from the drift
    # denominator and counted here instead.
    out_of_scope: int = 0

    # Patent-division records excluded by drift.exclude_patent_records.
    patent_excluded: int = 0

    # Recent evaluable records per species taxid, [detected, evaluable], with no
    # assessability floor. The per-lineage check above answers "is one lineage
    # failing"; this answers "what does each species read", which is the only
    # sensible reading for an assay whose product size names the species (the
    # report shows it for an assay declaring `amplicon_bp_range`). None when
    # no taxids were available.
    species_counts: dict[int | None, list[int]] | None = None

    # Per-lineage analysis. When taxids are available, each assay's
    # recent evaluable records are grouped by NCBI taxid and tested per lineage.
    # The worst assessable lineage drives the verdict when it is significantly
    # below threshold (Benjamini-Hochberg across lineages).
    lineage_stats: list[LineageStats] | None = None
    lineage_verdict: str | None = None  # "failing" or "detecting", from worst_lineage_verdict
    # The share of recent evaluable records that sit in assessable lineages
    # (those with >= min_records_per_lineage). Low means the verdict is weak.
    lineage_coverage: float | None = None
    # Whether the lineage verdict changed the pooled status.
    lineage_override: bool = False
    # The pooled status before lineage override, so the report can show both.
    status_pooled: str | None = None
    # Index into `lineage_stats` of the lineage that drove the override. The note
    # names that lineage in prose; this is the same answer without a parse, for
    # scripts/lineage_override_audit.py. Set only when lineage_override is True.
    lineage_worst_idx: int | None = None

    @property
    def total_evaluable(self) -> int:
        return sum(y.evaluable for y in self.years.values())

    @property
    def total_screened(self) -> int:
        return sum(sum(y.counts.values()) for y in self.years.values())

    @property
    def recent_fraction(self) -> float | None:
        return self.recent_detected / self.recent_evaluable if self.recent_evaluable else None

    @property
    def baseline_fraction(self) -> float | None:
        return self.baseline_detected / self.baseline_evaluable if self.baseline_evaluable else None

    def unevaluable(self) -> Counter:
        out: Counter = Counter()
        for y in self.years.values():
            for call, n in y.counts.items():
                if call not in EVALUABLE:
                    out[call] += n
        return out

    def _cut_year(self) -> int:
        """First year of the recent window. 0 if it cannot be determined."""
        if self.recent_year is not None:
            return self.recent_year
        head = str(self.recent_from)[:4]
        return int(head) if head.isdigit() else 0

    @property
    def ever_worked(self) -> bool:
        """Did this assay clear the threshold in any year before the recent window?

        `declining` is read as "this assay has drifted", which presupposes that
        it once worked. The test is deliberately per YEAR rather than on the
        aggregate baseline, because the aggregate is diluted by the decline
        itself: an assay at 100% until 2016 and failing from 2018 has an
        aggregate baseline of 72%, and gating on that would reclassify the very
        case the tool exists to find. Any single year that reached the threshold
        on at least `min_records_for_year` evaluable records is enough.

        What it excludes is the assay that never covered the pool it is measured
        against. 31 of the 37 assays labelled `declining` in the 2026-10-07 run
        had a baseline share below the threshold (median 68%) - pan-family
        assays screened against a whole taxon, whose movement is mostly in which
        clades were deposited. Those become `low coverage`, with a note saying
        they are also falling.
        """
        cut = self._cut_year()
        return any(
            year < cut
            and stats.evaluable >= self.min_records_for_year
            and (stats.fraction or 0.0) >= self.threshold
            for year, stats in self.years.items()
        )

    @property
    def records_per_footprint(self) -> float | None:
        """Evaluable recent records per distinct footprint; 1.0 means no duplication."""
        if not self.recent_footprints or not self.recent_evaluable:
            return None
        return self.recent_evaluable / self.recent_footprints

    @property
    def clustering_note(self) -> str:
        """A sentence for the report, or "" when there is nothing to say.

        Said only for a flagged assay, because that is where the question has
        consequences: a stable verdict rests on the point estimate and does not
        move with the interval. Two different reductions are reported, and the note
        says which is which, because they answer different questions:

        - the SAMPLE-SIZE one keeps the detected share as measured and gives it
          only as many independent observations as there are distinct footprints.
          It shows whether the flag survives losing the sample size duplication
          costs, and it cannot show that the share itself is dominated by one clone;
        - the FOOTPRINT one counts each distinct footprint once, which does.

        When a flag does not survive it names WHICH test failed, and says what that
        means only for the tests where it is true: a declining flag can fail on the
        change interval alone while its recent interval is still well below the
        threshold, and saying the threshold was reached then would be false.
        """
        if self.flag_survives_clustering is None or self.recent_footprints is None:
            return ""
        assert self.recent_fraction is not None and self.recent_footprints_detected is not None
        n_f, d_f = self.recent_footprints, self.recent_footprints_detected
        lo, hi = self.recent_ci_clustered
        flo, fhi = self.recent_ci_by_footprint
        clo, chi = self.change_ci_clustered
        share = pct(self.recent_fraction)
        shared = (
            f"{self.recent_evaluable} recent records share {n_f} distinct footprints "
            f"({self.records_per_footprint:.1f} per footprint)"
        )
        by_sample = (
            f"with only {n_f} independent observations (one per footprint) the interval around the "
            f"{share} detected share is {pct(lo)}-{pct(hi)}"
        )
        by_footprint = (
            f"counting each footprint once, {d_f} of {n_f} footprints amplify "
            f"({pct(d_f / n_f)}; interval {pct(flo)}-{pct(fhi)})"
        )
        if self.flag_survives_clustering:
            held = (
                f"Both reductions leave the flag in place: {by_sample}, and {by_footprint}; "
                f"each is below the {self.threshold:.0%} threshold"
            )
            if self.status == "declining":
                held += (
                    f", and the fall from baseline ({pct(clo, True)} to {pct(chi, True)}) still excludes zero"
                )
            return (
                f"{shared}. {held}. So the flag does not rest on identical footprints deposited repeatedly."
            )
        reasons = []
        if "too_few" in self.cluster_failures:
            reasons.append(
                f"only {n_f} distinct footprint(s), fewer than the {self.min_records} "
                "independent observations the record-level rule needs before it will flag anything"
            )
        if "recent" in self.cluster_failures:
            reasons.append(f"{by_sample}, which no longer rules out the {self.threshold:.0%} threshold")
        if "footprint" in self.cluster_failures:
            reasons.append(
                f"{by_footprint}, which reaches the {self.threshold:.0%} threshold: the failing records are "
                "concentrated on few footprints"
            )
        if "change" in self.cluster_failures:
            reasons.append(
                f"with only {n_f} and {self.baseline_footprints} independent observations the fall from "
                f"baseline is {pct(clo, True)} to {pct(chi, True)}, which no longer excludes zero"
            )
        text = f"{shared}. This flag does not hold up: {'; '.join(reasons)}."
        # Only where it is true. It says nothing about a flag that failed on the
        # floor or on a thin baseline alone, where the failing records may be perfectly diverse.
        if {"recent", "footprint"} & set(self.cluster_failures):
            text += (
                " The failing records may well be real; what this says is that the SHARE failing may "
                "reflect how many near-identical records were deposited rather than how much of the "
                "population the assay misses."
            )
        return text

    def _cluster_check(self) -> None:
        """Does a flag survive two ways of discounting duplicated records?

        The widest defensible readings, not the right ones. Wilson assumes every
        record is an independent draw. Two reductions each assume identical
        footprints are a perfect clone, and between them they bracket the truth:

        - SAMPLE SIZE (`recent`, `change`): keep the detected share as measured
          and give it only as many observations as there are distinct footprints.
          This shows whether a flag survives losing the sample size that
          duplication costs. It cannot show that the share itself is dominated by
          one clone, because the share is still record-weighted: 92 failures at one
          footprint beside detections spread over 19 others keep their 43% share
          here however many copies the failing footprint has.
        - FOOTPRINT (`footprint`): count each distinct footprint once. That is the
          reduction that does show it: in the same case 19 of 20 footprints amplify.
          On its own it would misjudge a healthy assay, because a sequencing error in
          a primer site is a footprint of its own and would read as mostly failures,
          so it is never used to flag or to clear anything; it can only withhold the
          label "survives" from a flag the record-level evidence already raised.

        A flag survives only if it passes every test it faces, and the first is a
        FLOOR: at least `min_records` distinct footprints. Without one the check
        reassured exactly where it was meant to warn, at every count from two up to
        nineteen. Wilson is anti-conservative at tiny n (0 of 1 gives an upper bound
        of 0.79 where the exact bound is 0.975), so 92 failures sharing ONE footprint
        plus 70 detections sharing another gave an upper bound of 88%, "below
        threshold", and the note said the flag did not depend on duplicated records.
        The record-level rule already refuses to flag on fewer than `min_records`
        records; the same evidence floor now applies to independent observations.

        It removes the duplication it can SEE and no more. Records from one clade
        that differ at a few non-primer positions are distinct here and still
        correlated, so this is not a lower bound on the effective sample size.
        """
        n_r, n_b = self.recent_footprints, self.baseline_footprints
        d_r = self.recent_footprints_detected
        if n_r is None or d_r is None or not self.recent_evaluable:
            return
        if self.baseline_evaluable and n_b is None:
            return
        p = self.recent_fraction
        assert p is not None
        self.recent_ci_clustered = wilson_interval(p * n_r, n_r)
        self.recent_ci_by_footprint = wilson_interval(d_r, n_r)
        if self.baseline_evaluable:
            assert n_b is not None  # guarded above
            self.change_ci_clustered = newcombe_difference(
                p * n_r, n_r, (self.baseline_fraction or 0.0) * n_b, n_b
            )
        if self.status in ("declining", "low coverage"):
            failures = []
            if n_r < self.min_records:
                failures.append("too_few")
            if self.recent_ci_clustered[1] >= self.threshold:
                failures.append("recent")
            if self.recent_ci_by_footprint[1] >= self.threshold:
                failures.append("footprint")
            if self.status == "declining" and self.change_ci_clustered[1] >= 0:
                failures.append("change")
            self.cluster_failures = tuple(failures)
            self.flag_survives_clustering = not failures

    def _lineage_check(
        self,
        recent_calls: list[dict],
        taxa_cache: dict[int, str],
        taxid_sidecar: dict[str, int],
        min_records_per_lineage: int,
        resolvers: list | None = None,
        baseline_calls: list[dict] | None = None,
        min_records_for_year: int = 10,
    ) -> None:
        """Per-lineage analysis: does the worst assessable lineage fail?

        Called after finalise, so the pooled status is already set. When the
        worst lineage is significantly below threshold, the status is overridden
        to ``declining`` (or stays ``declining`` if it already was). The pooled
        status is saved in ``status_pooled`` so the report can show both.

        The override runs in ONE direction only: a pooled ``stable`` can become
        ``declining`` if a lineage is failing, but a pooled ``declining`` is
        never upgraded to ``stable`` by the lineage check. This follows
        Decision 2 in docs/2026-10-17-estimand-plan.md: the worst assessable
        lineage drives the call.

        The body is a chain of gates, each of which can end the decision, and
        each named for what it refuses. Read in order:

        1. no assessable lineage, or one lineage that IS the pool -> no override;
        2. `_never_covered_gate`, which turns a failing lineage that never
           worked into a coverage gap rather than drift;
        3. `_weak_pooled_gate`, which refuses to call drift when neither the
           lineage nor the pool ever cleared the threshold;
        4. `_apply_override`, which is the only place the status changes.
        """
        if not recent_calls:
            return

        from assaywatch.lineage import per_lineage_stats, worst_lineage_verdict

        stats = per_lineage_stats(
            recent_calls, taxa_cache, taxid_sidecar, min_records=min_records_per_lineage, resolvers=resolvers
        )
        for s in stats:
            s.assay_id = self.assay_id
        self.lineage_stats = stats

        # What share of recent evaluable records sit in assessable lineages?
        n_in_assessable = sum(s.n_evaluable for s in stats)
        self.lineage_coverage = n_in_assessable / self.recent_evaluable if self.recent_evaluable > 0 else 0.0

        if not stats:
            # No assessable lineages (all below floor, or all unresolved).
            return

        if self._pool_is_one_lineage(stats):
            self.lineage_verdict = worst_lineage_verdict(stats, self.threshold)[0]
            return

        verdict, worst_idx = worst_lineage_verdict(stats, self.threshold)
        self.lineage_verdict = verdict

        if verdict == "failing" and baseline_calls is not None:
            stop, worst_idx = self._never_covered_gate(
                stats,
                worst_idx,
                recent_calls,
                baseline_calls,
                taxa_cache,
                taxid_sidecar,
                resolvers,
                min_records_for_year,
            )
            if stop:
                return
            verdict = self.lineage_verdict

        if verdict == "failing" and self.status not in ("stable", "watch", "declining"):
            if self._weak_pooled_gate(
                stats, worst_idx, baseline_calls, taxa_cache, taxid_sidecar, resolvers, min_records_for_year
            ):
                return

        if verdict == "failing" and self.status != "declining":
            self._apply_override(stats, worst_idx)

    def _pool_is_one_lineage(self, stats: list) -> bool:
        """Is the "worst lineage" just the pooled measurement wearing a hat?

        One lineage holding every recent record is the pooled measurement again,
        so its history is the assay's. If the assay never cleared the threshold
        in an earlier year, the lineage is not new to the archive, only thinly
        measured, and overriding would replace "no measurable fall" with a drift
        call (West Nile Lanciotti 2001 as of 2003, one species once
        lineage.group_at_rank rolls up). One that used to work still overrides:
        CDV Scagliarini 2007 as of 2021.
        """
        return len(stats) == 1 and stats[0].n_evaluable == self.recent_evaluable and not self.ever_worked

    def _never_covered_gate(
        self,
        stats: list,
        worst_idx: int,
        recent_calls: list[dict],
        baseline_calls: list[dict],
        taxa_cache: dict[int, str],
        taxid_sidecar: dict[str, int],
        resolvers: list | None,
        min_records_for_year: int,
    ) -> tuple[bool, int]:
        """A failing lineage that was never covered is a coverage gap, not drift.

        With lineage.require_working_baseline, a lineage measured in earlier
        years that never cleared the threshold in any of them cannot drive
        ``declining``: it was never covered, so it has not drifted. If it fails
        under a pooled stable/watch the assay becomes ``low coverage`` instead.
        A lineage with no earlier measured year (new to the archive) still can.
        See docs/2026-10-19-pan-family-cases.md.

        A recent call flagged ``bucket`` (lineage.unclassified_is_bucket) counts
        as never covered: an unclassified taxid is not a lineage, so it cannot be
        one new to the archive.

        Returns (stop, worst_idx): `stop` ends the chain, and `worst_idx` moves
        to the worst ELIGIBLE lineage when the chain continues.
        """
        from assaywatch.lineage import lineage_of, lineages_never_covered, worst_lineage_verdict

        never = lineages_never_covered(
            baseline_calls, taxa_cache, taxid_sidecar, self.threshold, min_records_for_year, resolvers
        )
        buckets = {
            lineage_of(c, taxa_cache, taxid_sidecar, resolvers) for c in recent_calls if c.get("bucket")
        }
        eligible = [s for s in stats if s.lineage_name not in never | buckets]
        gap = stats[worst_idx]
        verdict, idx = worst_lineage_verdict(eligible, self.threshold)
        self.lineage_verdict = verdict or "failing (never covered)"
        if verdict == "failing":
            return False, stats.index(eligible[idx])

        # Every failing lineage was measured earlier and never covered: a coverage gap.
        if self.status in ("stable", "watch"):
            self.status_pooled = self.status
            self.status = "low coverage"
            self.lineage_override = True
            self.lineage_worst_idx = worst_idx
        why = (
            "is an unclassified taxon, so it cannot be told from one never covered"
            if gap.lineage_name in buckets and gap.lineage_name not in never
            else "was below the threshold in every earlier year measured"
        )
        self.note += (
            f"; lineage {gap.lineage_name} ({gap.n_evaluable} records) detects only "
            f"{gap.share:.1%} and {why}: a coverage gap, not drift"
        )
        return True, worst_idx

    def _weak_pooled_gate(
        self,
        stats: list,
        worst_idx: int,
        baseline_calls: list[dict] | None,
        taxa_cache: dict[int, str],
        taxid_sidecar: dict[str, int],
        resolvers: list | None,
        min_records_for_year: int,
    ) -> bool:
        """Refuse to call drift when nothing here ever cleared the threshold.

        The pooled verdict is `low coverage` or `insufficient data`: the pool
        never showed this assay working on this denominator, so there is no fall
        for a lineage to be evidence of. `declining` claims one. The same rule
        the project already settled at the pooled level - a fall from a baseline
        that never cleared the threshold is not drift - applied to the
        denominator the override actually claims, so the lineage may overturn a
        weak pooled verdict only if that lineage itself cleared the threshold in
        an earlier measured year. A lineage new to the archive cannot: it has no
        history to have fallen from.

        Without this, pooled "fell measurably, but never reached the threshold in
        any earlier year, so this is not drift" was overturned to `declining` by
        33 records of an NCBI reclassification artefact (Enterovirus VP3/VP1
        round2 as of 2018-09-30). Tier-2: 12 -> 10 disagreements, 4/11 caught
        either way, nothing lost; 2 of 201 current statuses move. Evidence:
        docs/2026-10-20-pan-family-override.md.
        """
        if baseline_calls is None:
            return False
        from assaywatch.lineage import lineages_ever_covered

        worked = lineages_ever_covered(
            baseline_calls, taxa_cache, taxid_sidecar, self.threshold, min_records_for_year, resolvers
        )
        if stats[worst_idx].lineage_name in worked:
            return False
        self.note += (
            f"; lineage {stats[worst_idx].lineage_name} "
            f"({stats[worst_idx].n_evaluable} records) detects only "
            f"{stats[worst_idx].share:.1%}, but neither it nor the pooled share ever cleared "
            "the threshold, so there is no fall to call a decline"
        )
        return True

    def _apply_override(self, stats: list, worst_idx: int) -> None:
        """The one place a lineage changes the status. Pooled -> declining."""
        self.status_pooled = self.status
        self.status = "declining"
        self.lineage_override = True
        self.lineage_worst_idx = worst_idx
        worst = stats[worst_idx]
        # A note that accurately describes why the override happened.
        if self.status_pooled in ("stable", "watch"):
            prefix = f"pooled share {self.recent_fraction:.1%} is above the {self.threshold:.0%} threshold"
        elif self.status_pooled == "low coverage":
            prefix = f"pooled share {self.recent_fraction:.1%} has low coverage"
        else:
            prefix = f"pooled status was {self.status_pooled}"
        self.note = (
            f"{prefix}, but lineage {worst.lineage_name} "
            f"({worst.n_evaluable} records) detects only {worst.share:.1%} "
            f"({worst.ci_lower:.1%}-{worst.ci_upper:.1%}); "
            f"lineage verdict overrides to declining"
        )

    def finalise(self) -> AssayDrift:
        if self.recent_counts or self.baseline_counts:
            r, b = YearStats(0, self.recent_counts), YearStats(0, self.baseline_counts)
            self.recent_detected, self.recent_evaluable = r.detected, r.evaluable
            self.baseline_detected, self.baseline_evaluable = b.detected, b.evaluable
        else:
            # Only reached when no record carried a date, or for an object built
            # by hand with `years` alone. `recent_year` is set by `assess`;
            # otherwise `recent_from` is a bare year, as every hand-built caller
            # passes. Parsing a displayed "Oct 2024" would raise here, which is
            # why the number is carried separately rather than re-derived.
            head = str(self.recent_from)[:4]
            cut = self.recent_year if self.recent_year is not None else (int(head) if head.isdigit() else 0)
            for year, stats in self.years.items():
                if year >= cut:
                    self.recent_detected += stats.detected
                    self.recent_evaluable += stats.evaluable
                else:
                    self.baseline_detected += stats.detected
                    self.baseline_evaluable += stats.evaluable

        self.recent_ci = wilson_interval(self.recent_detected, self.recent_evaluable)
        self.baseline_ci = wilson_interval(self.baseline_detected, self.baseline_evaluable)
        self.change_ci = newcombe_difference(
            self.recent_detected,
            self.recent_evaluable,
            self.baseline_detected,
            self.baseline_evaluable,
        )

        if self.recent_evaluable == 0:
            self.status = "no recent data"
            self.note = f"no evaluable records deposited since {self.recent_from}"
        elif self.recent_evaluable < self.min_records:
            self.status = "insufficient data"
            self.note = (
                f"{self.recent_evaluable} evaluable records since {self.recent_from}, "
                f"below the minimum of {self.min_records}; "
                f"the detected share is {pct(self.recent_fraction)} "
                f"({pct(self.recent_ci[0])}-{pct(self.recent_ci[1])}), too wide to act on"
            )
        elif self.recent_ci[1] < self.threshold:
            # Below threshold is two different findings. Declining: the share has
            # fallen, and the interval for the change excludes zero; that is
            # drift. Low coverage: below threshold but not measurably lower than
            # before, which is an assay used beyond what it was designed to
            # cover (a lineage-specific assay on a whole genus, a pan-family
            # assay on a family it never fully covered), not one that drifted.
            # Declining needs both a fall that is real (the interval for the
            # change excludes zero) and one that matters (at least min_decline).
            # With thousands of records a fall from 1% to 0% is "real" and
            # says nothing about an assay that never covered this pool.
            lo, hi = self.change_ci
            fall = (self.baseline_fraction - self.recent_fraction) if self.baseline_evaluable else 0.0
            fell = self.baseline_evaluable > 0 and hi < 0 and fall >= self.min_decline
            declining = fell and (self.ever_worked or not self.require_working_baseline)
            self.status = "declining" if declining else "low coverage"
            self.note = (
                f"detected share {self.recent_fraction:.1%} "
                f"({pct(self.recent_ci[0])}-{pct(self.recent_ci[1])}) since {self.recent_from}, "
                f"upper bound below the {self.threshold:.0%} threshold"
            )
            if self.baseline_evaluable:
                self.note += f"; change from baseline {pct(lo, True)} to {pct(hi, True)}"
                if not declining:
                    if fell:
                        # The fall is real and large enough; what it is not is
                        # drift, because no year before the window ever reached
                        # the threshold. The assay is being measured against more
                        # diversity than it ever covered.
                        trend = (
                            f"fell measurably, but never reached the {self.threshold:.0%} threshold in any "
                            f"earlier year, so this is not drift — it fell from"
                        )
                    elif lo > 0:
                        trend = "rose from"
                    elif hi < 0:
                        trend = f"fell less than the {pct(self.min_decline)} that counts as declining, from"
                    else:
                        trend = "no measurable fall from"
                    self.note += f" ({trend} a baseline of {pct(self.baseline_fraction)})"
            else:
                self.note += "; no baseline records to compare with"
        elif self.recent_fraction is not None and self.recent_fraction < self.threshold:
            self.status = "watch"
            self.note = (
                f"detected share {self.recent_fraction:.1%} is below the {self.threshold:.0%} threshold, "
                f"but its interval ({pct(self.recent_ci[0])}-{pct(self.recent_ci[1])}) still reaches it"
            )
        else:
            self.status = "stable"
            self.note = (
                f"detected share {self.recent_fraction:.1%} "
                f"({pct(self.recent_ci[0])}-{pct(self.recent_ci[1])}) since {self.recent_from}"
            )
        self._cluster_check()
        return self


def pct(x: float, signed: bool = False) -> str:
    """A share as a percentage that never rounds a small number to a misleading 0%.

    Whole percent normally; one decimal below 1% (so a 0.19% bound does not
    print as 0%), and never `-0%`.
    """
    digits = 1 if 0 < abs(x) < 0.01 else 0
    if round(abs(x) * 100, digits) == 0:
        return "0%"  # never "-0%" or "-0.0%"
    return f"{x:+.{digits}%}" if signed else f"{x:.{digits}%}"


def recent_cutoff(cfg: dict[str, Any], today: date | None = None) -> date:
    """The first day of the recent window: `recent_window_months` before `today`."""
    months = int(cfg.get("drift", {}).get("recent_window_months", 24))
    today = today or date.today()
    y, m = divmod(today.year * 12 + today.month - 1 - months, 12)
    return date(y, m + 1, min(today.day, 28))


def recent_cutoff_year(cfg: dict[str, Any], today: date | None = None) -> int:
    """The year the recent window starts in (for records dated only to the year)."""
    return recent_cutoff(cfg, today).year


def months_back(anchor: date, months: int) -> date:
    y, m = divmod(anchor.year * 12 + anchor.month - 1 - months, 12)
    return date(y, m + 1, min(anchor.day, 28))


@dataclass(frozen=True)
class DriftSettings:
    """Every `drift.*` setting one `assess` call reads, in one place.

    S4 in docs/2026-10-20-pipeline-audit.md: `assess` was 300 lines and a reader
    could not hold its control flow in mind, on the path that produces a
    verdict. The settings were a dozen locals threaded through it; naming them
    is what lets the stages below take an argument instead of a closure.
    """

    base_months: int
    max_months: int
    threshold: float
    min_records: int
    min_decline: float
    require_working_baseline: bool
    min_records_for_year: int
    count_diverged: bool
    exclude_patent: bool

    @classmethod
    def from_config(cls, cfg: dict[str, Any]) -> DriftSettings:
        d = cfg.get("drift", {})
        base = int(d.get("recent_window_months", 24))
        return cls(
            base_months=base,
            max_months=max(base, int(d.get("max_window_months", base))),
            threshold=float(d.get("detect_fraction_threshold", 0.9)),
            min_records=int(d.get("min_records_for_drift", 20)),
            min_decline=float(d.get("min_decline", 0.0)),
            require_working_baseline=bool(d.get("require_working_baseline", True)),
            min_records_for_year=int(d.get("min_records_for_coverage", 10)),
            # A record whose partner binding site is present in the deposit and does
            # not match is evidence the assay would not amplify it, but it leaves the
            # denominator as no_amplicon, which biases that denominator toward the
            # sequences the assay happens to match. Counting those as failures is off
            # by default because the signal conflates two things: an assay that has
            # drifted, and a pan-family assay screened against taxa it never claimed
            # to cover. Settle it with docs/validation-cases.tsv, not by argument.
            count_diverged=bool(d.get("count_diverged_as_fail", False)),
            # A patent deposit is a construct someone designed, not a virus that is
            # circulating, so it answers a different question from the one this tool
            # asks. Off by default: it changes a denominator, which is exactly the
            # kind of change docs/validation-cases.tsv exists to approve.
            exclude_patent=bool(d.get("exclude_patent_records", False)),
        )


@dataclass(frozen=True)
class Window:
    """Which records count as recent, at the granularity the input actually has.

    `years` may hold full ISO dates (what report.read_dates gives) or bare years
    (what the tests and any year-only source give), and the two must not be
    compared the same way: a 2024 record is "recent" against an October 2024
    cutoff at year granularity but not at date granularity. Collapsing the two
    silently moved 90 records between windows.
    """

    anchor: date
    dated: bool

    def inside(self, iso: str, months: int) -> bool:
        edge = months_back(self.anchor, months)
        return iso >= edge.isoformat() if self.dated else int(iso[:4]) >= edge.year

    def choose(self, evaluable: list[str], settings: DriftSettings) -> int:
        """How many months back this assay's recent window reaches.

        Widen only when the assay could be judged at all with more history. An
        assay with fewer than `min_records` evaluable records in total can never
        reach the bar, so widening its window would just quietly stretch the
        definition of "recent" for no gain.
        """
        months = settings.base_months
        if len(evaluable) < settings.min_records:
            return months
        # Widen a year at a time, only as far as reaching min_records needs.
        while (
            months < settings.max_months
            and sum(1 for x in evaluable if self.inside(x, months)) < settings.min_records
        ):
            months += 12
        return min(months, settings.max_months)


@dataclass
class GatheredCalls:
    """Calls bucketed per assay, with what was held out of each denominator."""

    per: dict[str, list[tuple[str | None, str, str, str | None]]] = field(default_factory=dict)
    raw: dict[str, list[tuple[str | None, dict[str, Any]]]] = field(default_factory=dict)
    out_of_scope: dict[str, int] = field(default_factory=dict)
    patent: dict[str, int] = field(default_factory=dict)


def _gather_calls(
    calls,
    years: dict[str, int | str],
    settings: DriftSettings,
    *,
    taxids: dict[str, int] | None,
    scope_map: dict[str, set[int]] | None,
    taxonomy: Taxonomy | None,
    patent: set[str] | None,
    keep_raw: bool,
) -> GatheredCalls:
    """Bucket every call row per assay. The window cannot be chosen until the dates are known."""
    out = GatheredCalls()
    scope_canon: dict[str, set[int]] = {}

    def in_scope(aid: str, txid: int) -> bool:
        if taxonomy is None:
            return txid in scope_map[aid]
        if aid not in scope_canon:
            scope_canon[aid] = {taxonomy.canonical(t) for t in scope_map[aid]}
        return taxonomy.within(txid, scope_canon[aid])

    for row in calls:
        aid = row["assay_id"]
        # Scope filter: when the assay has scope_taxids and the record has a
        # taxid, skip out-of-scope records from the drift denominator.
        if scope_map and aid in scope_map and taxids is not None:
            rid = row["record_id"]
            base = strip_version(rid)
            txid = taxids.get(rid) if taxids.get(rid) is not None else taxids.get(base)
            if txid is not None and not in_scope(aid, txid):
                out.out_of_scope[aid] = out.out_of_scope.get(aid, 0) + 1
                continue
        if settings.exclude_patent and strip_version(row["record_id"]) in patent:
            out.patent[aid] = out.patent.get(aid, 0) + 1
            continue
        when = years.get(row["record_id"])
        # A bare year keeps year granularity below, so it is anchored at 1 January.
        iso = when if isinstance(when, str) else (f"{when}-01-01" if when is not None else None)
        why = row.get("exclusion") or ""
        call = "fail" if (settings.count_diverged and why == "diverged") else row["call"]
        # None when the row has no footprint, so that an unknown footprint is never
        # confused with a known one. A known footprint is never the empty string:
        # `footprint_signature` joins six fields, so even an exact match is
        # `|||0|0|0`. The all-empty `|||||` is what a row carries when it was never
        # scored, which `report.read_calls` already turns into None.
        # A record counted as a failure only because count_diverged_as_fail says
        # so was never scored: its binding site is present and does not match, but
        # nothing was recorded about HOW, so all six footprint columns are empty.
        # Treating that as a footprint collapsed every diverged record into one
        # class however different they were. It is unknown instead, which makes the
        # assay's duplication check unknown - an honest "cannot say".
        fp = None if (settings.count_diverged and why == "diverged") else row.get("footprint")
        out.per.setdefault(aid, []).append((iso, call, why, fp))
        if keep_raw:
            out.raw.setdefault(aid, []).append((iso, row))
    return out


def _tally_window(a: AssayDrift, rows: list, window: Window, months: int) -> None:
    """Fill one assay's year table, its recent/baseline counts and its footprints.

    Distinct (call, footprint) classes are counted per window. If ANY evaluable
    record lacks a footprint the count is unknown for the whole assay rather than
    partial: a partial count would be a lower bound on distinct footprints, and
    so too wide an interval, presented as fact.
    """
    recent_fp: set[tuple[str, str]] = set()
    base_fp: set[tuple[str, str]] = set()
    fp_known = True
    for iso, call, why, fp in rows:
        if why:
            a.exclusions[why] += 1
        if iso is None:
            a.skipped_undated += 1
            continue
        a.years.setdefault(int(iso[:4]), YearStats(int(iso[:4]))).counts[call] += 1
        in_recent = window.inside(iso, months)
        (a.recent_counts if in_recent else a.baseline_counts)[call] += 1
        if call in EVALUABLE:
            if fp is None:
                fp_known = False
            else:
                (recent_fp if in_recent else base_fp).add((call, fp))
    if fp_known:
        a.recent_footprints = len(recent_fp)
        a.baseline_footprints = len(base_fp)
        a.recent_footprints_detected = sum(1 for call, _ in recent_fp if call != "fail")


@dataclass(frozen=True)
class LineageOptions:
    """The `lineage.*` settings, validated once rather than per assay."""

    min_per_lineage: int
    gate: bool
    rank: str | None
    buckets_on: bool

    @classmethod
    def from_config(cls, cfg: dict[str, Any], taxonomy: Taxonomy | None) -> LineageOptions:
        lcfg = cfg.get("lineage", {})
        rank = lcfg.get("group_at_rank")
        if rank not in (None, "species"):
            raise SystemExit(f"lineage.group_at_rank is {rank!r}; only null or 'species' is supported")
        buckets_on = bool(lcfg.get("unclassified_is_bucket", False))
        if (rank or buckets_on) and (taxonomy is None or not taxonomy.rank):
            raise SystemExit(
                "lineage.group_at_rank / unclassified_is_bucket need drift.scope_taxonomy with ranks; "
                "rebuild it with `python scripts/build_taxonomy_cache.py`"
            )
        return cls(
            min_per_lineage=int(lcfg.get("min_records_per_lineage", 20)),
            gate=bool(lcfg.get("require_working_baseline", False)),
            rank=rank,
            buckets_on=buckets_on,
        )

    def taxid_of(
        self, rid: str, base: str, taxids: dict[str, int], taxonomy: Taxonomy | None
    ) -> tuple[int | None, bool]:
        """The record's taxid (rolled up to species if configured) and its bucket flag."""
        txid = taxids.get(rid) if taxids.get(rid) is not None else taxids.get(base)
        if txid is None or taxonomy is None:
            return txid, False
        bucket = self.buckets_on and taxonomy.in_unclassified(txid)
        if self.rank == "species":
            txid = taxonomy.species_of(txid) or txid
        return txid, bucket


def _lineage_calls(
    raw_rows: list[tuple[str | None, dict[str, Any]]],
    window: Window,
    months: int,
    opts: LineageOptions,
    *,
    taxids: dict[str, int],
    taxonomy: Taxonomy | None,
    titles: dict[str, str] | None,
) -> tuple[list[dict], list[dict] | None]:
    """Recent evaluable calls annotated with taxids, and with the gate the older ones too.

    Each carries only what the lineage check reads, so the full screen row is not
    held per record: the taxid, the call, the unversioned accession and its title.
    """
    recent: list[dict] = []
    baseline: list[dict] | None = [] if opts.gate else None
    for iso, row in raw_rows:
        if iso is None:
            continue
        call = row["call"]
        if call not in EVALUABLE:
            continue
        rid = row["record_id"]
        base = strip_version(rid)
        if not window.inside(iso, months):
            if baseline is not None:
                txid, _ = opts.taxid_of(rid, base, taxids, taxonomy)
                baseline.append(
                    {
                        "record_id": rid,
                        "call": call,
                        "taxid": txid,
                        "accession": base,
                        "title": titles.get(base) if titles else None,
                        "year": int(iso[:4]),
                    }
                )
            continue
        # taxids may be keyed by versioned or unversioned accession.
        txid, bucket = opts.taxid_of(rid, base, taxids, taxonomy)
        recent.append(
            {
                "record_id": rid,
                "call": call,
                "taxid": txid,
                "bucket": bucket,
                "accession": base,
                "title": titles.get(base) if titles else None,
            }
        )
    return recent, baseline


def _species_counts(recent_calls: list[dict]) -> dict[int | None, list[int]]:
    """(detected, evaluable) per taxid, for the per-species table."""
    counts: dict[int | None, list[int]] = {}
    for c in recent_calls:
        pair = counts.setdefault(c["taxid"], [0, 0])
        pair[0] += c["call"] != "fail"
        pair[1] += 1
    return counts


def assess(
    calls: list[dict[str, Any]],
    years: dict[str, int | str],
    cfg: dict[str, Any],
    today: date | None = None,
    taxids: dict[str, int] | None = None,
    taxa_cache: dict[int, str] | None = None,
    scope_map: dict[str, set[int]] | None = None,
    resolvers: dict[str, list] | None = None,
    titles: dict[str, str] | None = None,
    taxonomy: Taxonomy | None = None,
    patent: set[str] | None = None,
) -> dict[str, AssayDrift]:
    """Group calls by assay and deposit date and work out each assay's status.

    `calls` are rows from the screen stage; `years` maps record id to its
    deposit date (ISO `YYYY-MM-DD`, as report.read_dates gives) or just a year.
    A record with no date is counted as skipped, never bucketed into a default,
    because an unknown year silently landing in the recent window is the kind
    of error that produces a confident wrong answer.

    The recent window is `recent_window_months` long, but it widens per assay,
    up to `max_window_months`, when that window holds fewer than
    `min_records_for_drift` evaluable records. Without that, an assay for a
    sparsely sequenced taxon is unjudgeable except in the years right after a
    deposition burst: Bd ITS records arrive 56 in one year and then four,
    so the standard Bd assay read "stable" in 2014 and "insufficient data"
    ever since, on no change in the assay. Each assay reports the window it
    actually used, and widening can only add older records, never drop recent
    ones.

    When ``taxids`` is provided (record_id → taxid mapping), per-lineage
    analysis runs after the pooled verdict.  The worst assessable lineage can
    override a pooled "stable" or "watch" to "declining".

    When ``scope_map`` is provided (assay_id → set of in-scope taxids), records
    whose taxid falls outside the scope set are excluded from the drift
    denominator.  They are still counted on ``AssayDrift.out_of_scope``.
    With ``taxonomy`` (assaywatch.taxonomy), a record is in scope when its taxid
    or any ancestor is listed, with merged taxids followed on both sides;
    without it the match is exact, which drops strain- and no-rank-level records.

    ``patent`` (unversioned accessions of GenBank patent-division records) is
    what ``drift.exclude_patent_records`` acts on: those records are engineered
    constructs rather than circulating diversity, so with the option on they
    leave the denominator and are counted on ``AssayDrift.patent_excluded``.

    ``resolvers`` (assay_id -> sub-lineage resolver chain, from
    ``lineage.sublineage_resolvers``) splits an assay's records below the taxid
    before the per-lineage check; ``titles`` (unversioned accession -> defline)
    feeds any title resolver. An assay with no chain is grouped per taxid.
    """
    settings = DriftSettings.from_config(cfg)
    if settings.exclude_patent and patent is None:
        raise SystemExit(
            "drift.exclude_patent_records is on but no patent record set was passed; "
            "the caller must read it with assaywatch.metadata.read_patent_accessions"
        )
    if settings.count_diverged:
        calls = list(calls)
        if any((row.get("exclusion") or "") == "windowed" for row in calls):
            # Those rows came from a window archive, which cannot tell a diverged site
            # from no site at all, so this option would count an unknown as known.
            raise SystemExit(
                "drift.count_diverged_as_fail needs to know which records diverged, and these calls "
                "include rows screened from a window archive (exclusion 'windowed'). Screen whole records."
            )
    window = Window(anchor=today or date.today(), dated=any(isinstance(v, str) for v in years.values()))
    per_lineage = taxids is not None and taxa_cache is not None
    # Validated before the loop, so a bad lineage setting fails on the config
    # rather than on the first assay that happens to reach the check.
    lineage_opts = LineageOptions.from_config(cfg, taxonomy) if per_lineage else None

    gathered = _gather_calls(
        calls,
        years,
        settings,
        taxids=taxids,
        scope_map=scope_map,
        taxonomy=taxonomy,
        patent=patent,
        keep_raw=taxids is not None,
    )

    grouped: dict[str, AssayDrift] = {}
    for assay_id, rows in gathered.per.items():
        evaluable = sorted((iso for iso, call, _, _ in rows if iso and call in EVALUABLE), reverse=True)
        months = window.choose(evaluable, settings)
        cutoff = months_back(window.anchor, months)
        a = AssayDrift(
            assay_id,
            recent_from=(cutoff.strftime("%b %Y") if window.dated else cutoff.year),
            threshold=settings.threshold,
            min_records=settings.min_records,
            min_decline=settings.min_decline,
            require_working_baseline=settings.require_working_baseline,
            min_records_for_year=settings.min_records_for_year,
            window_months=months,
            recent_year=cutoff.year,
        )
        _tally_window(a, rows, window, months)
        a.finalise()
        if months > settings.base_months:
            a.note += (
                f" (window widened to {months} months to reach {settings.min_records} evaluable records)"
            )
        if a.skipped_undated:
            a.note += f" ({a.skipped_undated} records skipped: no deposit date in the metadata)"

        # Per-lineage analysis: does the worst assessable lineage fail?
        if per_lineage:
            recent_calls, baseline_calls = _lineage_calls(
                gathered.raw.get(assay_id, []),
                window,
                months,
                lineage_opts,
                taxids=taxids,
                taxonomy=taxonomy,
                titles=titles,
            )
            a.species_counts = _species_counts(recent_calls)
            a._lineage_check(
                recent_calls,
                taxa_cache,
                taxids,  # doubles as sidecar: record_id → taxid
                lineage_opts.min_per_lineage,
                resolvers.get(assay_id) if resolvers else None,
                baseline_calls,
                settings.min_records_for_year,
            )

        a.out_of_scope = gathered.out_of_scope.get(assay_id, 0)
        a.patent_excluded = gathered.patent.get(assay_id, 0)
        grouped[assay_id] = a
    return grouped


def coverage_gaps(
    drifts: dict[str, AssayDrift],
    taxa: dict[str, tuple[int | None, str | None]],
    cfg: dict[str, Any],
) -> list[dict[str, Any]]:
    """Assays whose target has too few usable records to validate anything.

    For wildlife pathogens this is frequently the finding rather than a caveat:
    an assay cannot be shown to work against diversity that nobody has
    sequenced, and saying so is more useful than reporting 100 percent
    detection of three records.
    """
    minimum = int(cfg.get("drift", {}).get("min_records_for_coverage", 10))
    out = []
    for assay_id, (taxid, taxon_name) in sorted(taxa.items()):
        a = drifts.get(assay_id)
        n = a.total_evaluable if a else 0
        if n < minimum:
            out.append(
                {
                    "assay_id": assay_id,
                    "taxid": taxid,
                    "taxon_name": taxon_name,
                    "evaluable": n,
                    "screened": a.total_screened if a else 0,
                }
            )
    return out


def by_status(drifts: dict[str, AssayDrift]) -> dict[str, list[AssayDrift]]:
    out: dict[str, list[AssayDrift]] = defaultdict(list)
    for a in drifts.values():
        out[a.status].append(a)
    for v in out.values():
        v.sort(key=lambda a: (a.recent_fraction if a.recent_fraction is not None else 1.0, a.assay_id))
    return dict(out)
