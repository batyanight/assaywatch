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
from typing import Any

EVALUABLE = ("detect", "reduced", "fail")
Z95 = 1.959963984540054

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
    window_months: int = 0  # the recent window actually used, after any widening
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
    status: str = "no data"
    note: str = ""

    # Lineage-level robustness, from the records' footprints (see
    # `footprint_signature`). Set by `assess`; None when the rows carried no
    # footprint, which is every hand-built test row and every calls table
    # screened before these columns were read. NEVER scored: `status` above is
    # computed without any of this, exactly as degeneracy and thermodynamics are
    # reported beside a call and never fed into it.
    recent_footprints: int | None = None  # distinct (call, footprint) among evaluable recent records
    baseline_footprints: int | None = None
    recent_ci_clustered: tuple[float, float] = (0.0, 1.0)
    change_ci_clustered: tuple[float, float] = (-1.0, 1.0)
    # For a flagged assay only: does the flag still hold at the clustered
    # interval? None for every other status, and when footprints are unknown.
    flag_survives_clustering: bool | None = None
    # Why a flag did not survive, as codes: "too_few" (fewer distinct footprints
    # than min_records), "recent" (the clustered recent interval reaches the
    # threshold), "change" (a declining assay's fall from baseline no longer
    # excludes zero). Empty when it survived or was not checked.
    cluster_failures: tuple[str, ...] = ()

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
        move with the interval. When a flag does not survive, it names WHICH test
        failed, because a declining flag can fail on the change interval alone
        while its recent interval is still well below the threshold, and saying
        the threshold was reached then would be false.
        """
        if self.flag_survives_clustering is None or self.recent_footprints is None:
            return ""
        lo, hi = self.recent_ci_clustered
        clo, chi = self.change_ci_clustered
        shared = (
            f"{self.recent_evaluable} recent records share {self.recent_footprints} distinct footprints "
            f"({self.records_per_footprint:.1f} per footprint)"
        )
        if self.flag_survives_clustering:
            held = (
                f"Even counting each footprint once the interval is {pct(lo)}-{pct(hi)}, "
                f"still below the {self.threshold:.0%} threshold"
            )
            if self.status == "declining":
                held += (
                    f", and the fall from baseline ({pct(clo, True)} to {pct(chi, True)}) still excludes zero"
                )
            return f"{shared}. {held}, so the flag does not depend on duplicated records."
        reasons = []
        if "too_few" in self.cluster_failures:
            reasons.append(
                f"only {self.recent_footprints} distinct footprint(s), fewer than the {self.min_records} "
                "independent observations the record-level rule needs before it will flag anything"
            )
        if "recent" in self.cluster_failures:
            reasons.append(
                f"counting each footprint once the interval widens to {pct(lo)}-{pct(hi)}, which no "
                f"longer rules out the {self.threshold:.0%} threshold"
            )
        if "change" in self.cluster_failures:
            reasons.append(
                f"counting each footprint once the fall from baseline is {pct(clo, True)} to "
                f"{pct(chi, True)}, which no longer excludes zero"
            )
        return (
            f"{shared}. This flag does not hold up: {'; '.join(reasons)}. The failing footprints may "
            "well be real; what this says is that the SHARE failing may reflect how many near-identical "
            "records were deposited rather than how much of the population the assay misses."
        )

    def _cluster_check(self) -> None:
        """Interval at the number of distinct footprints, and whether a flag survives it.

        The widest defensible reading, not the right one. Wilson assumes every
        record is an independent draw; this assumes every group of records with
        an identical footprint is ONE draw, i.e. a perfect clone. The truth is
        in between, so the two intervals bracket it and a flag that holds at both
        is a flag that does not rest on duplication.

        A flag survives only if it passes every test it faces, and the first is a
        FLOOR: at least `min_records` distinct footprints. Without one the check
        reassured exactly where it was meant to warn. Wilson is anti-conservative
        at tiny n (0 of 1 gives an upper bound of 0.79 where the exact bound is
        0.975), so 92 failures sharing ONE footprint plus 70 detections sharing
        another - the malB case this check was written for - gave an upper bound
        of 88%, "below threshold", and the note said the flag did not depend on
        duplicated records. The record-level rule already refuses to flag on fewer
        than `min_records` records; the same evidence floor now applies to
        independent observations.

        It removes the duplication it can SEE and no more. Records from one clade
        that differ at a few non-primer positions are distinct here and still
        correlated, so this is not a lower bound on the effective sample size.

        The alternative the review proposes, weighting each distinct haplotype
        equally, was rejected: a sequencing error in a primer site makes a unique
        failing footprint, so on a healthy assay it would report mostly failures.
        """
        n_r, n_b = self.recent_footprints, self.baseline_footprints
        if n_r is None or not self.recent_evaluable:
            return
        if self.baseline_evaluable and n_b is None:
            return
        p = self.recent_fraction
        assert p is not None
        self.recent_ci_clustered = wilson_interval(p * n_r, n_r)
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
            if self.status == "declining" and self.change_ci_clustered[1] >= 0:
                failures.append("change")
            self.cluster_failures = tuple(failures)
            self.flag_survives_clustering = not failures

    def finalise(self) -> AssayDrift:
        if self.recent_counts or self.baseline_counts:
            r, b = YearStats(0, self.recent_counts), YearStats(0, self.baseline_counts)
            self.recent_detected, self.recent_evaluable = r.detected, r.evaluable
            self.baseline_detected, self.baseline_evaluable = b.detected, b.evaluable
        else:
            for year, stats in self.years.items():
                if year >= int(str(self.recent_from)[:4]):
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
            declining = self.baseline_evaluable > 0 and hi < 0 and fall >= self.min_decline
            self.status = "declining" if declining else "low coverage"
            self.note = (
                f"detected share {self.recent_fraction:.1%} "
                f"({pct(self.recent_ci[0])}-{pct(self.recent_ci[1])}) since {self.recent_from}, "
                f"upper bound below the {self.threshold:.0%} threshold"
            )
            if self.baseline_evaluable:
                self.note += f"; change from baseline {pct(lo, True)} to {pct(hi, True)}"
                if not declining:
                    if lo > 0:
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


def assess(
    calls: list[dict[str, Any]],
    years: dict[str, int | str],
    cfg: dict[str, Any],
    today: date | None = None,
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
    """
    d = cfg.get("drift", {})
    base_months = int(d.get("recent_window_months", 24))
    max_months = max(base_months, int(d.get("max_window_months", base_months)))
    threshold = float(d.get("detect_fraction_threshold", 0.9))
    min_records = int(d.get("min_records_for_drift", 20))
    min_decline = float(d.get("min_decline", 0.0))
    # A record whose partner binding site is present in the deposit and does not
    # match is evidence the assay would not amplify it, but it leaves the
    # denominator as no_amplicon, which biases that denominator toward the
    # sequences the assay happens to match. Counting those as failures is off by
    # default because the signal conflates two things: an assay that has drifted,
    # and a pan-family assay screened against taxa it never claimed to cover.
    # Settle it with docs/validation-cases.tsv rather than by argument.
    count_diverged = bool(d.get("count_diverged_as_fail", False))
    anchor = today or date.today()
    dated = any(isinstance(v, str) for v in years.values())

    # Gather per assay first: the window cannot be chosen until the dates are known.
    per: dict[str, list[tuple[str | None, str, str, str | None]]] = {}
    for row in calls:
        when = years.get(row["record_id"])
        # A bare year keeps year granularity below, so it is anchored at 1 January.
        iso = when if isinstance(when, str) else (f"{when}-01-01" if when is not None else None)
        why = row.get("exclusion") or ""
        call = "fail" if (count_diverged and why == "diverged") else row["call"]
        # None, not "", when the row has no footprint: an empty signature is a
        # real footprint (an exact match) and must not be confused with an
        # unknown one.
        # A record counted as a failure only because count_diverged_as_fail says
        # so was never scored: its binding site is present and does not match, but
        # nothing was recorded about HOW, so all six footprint columns are empty.
        # Treating that as a footprint collapsed every diverged record into one
        # class however different they were. It is unknown instead, which makes the
        # assay's duplication check unknown - an honest "cannot say".
        fp = None if (count_diverged and why == "diverged") else row.get("footprint")
        per.setdefault(row["assay_id"], []).append((iso, call, why, fp))

    grouped: dict[str, AssayDrift] = {}
    for assay_id, rows in per.items():
        evaluable = sorted((iso for iso, call, _, _ in rows if iso and call in EVALUABLE), reverse=True)

        def inside(iso: str, months: int) -> bool:
            """Is this record inside a window of `months`, at the input's own granularity?

            `years` may hold full ISO dates (what report.read_dates gives) or bare
            years (what the tests and any year-only source give), and the two must
            not be compared the same way: a 2024 record is "recent" against an
            October 2024 cutoff at year granularity but not at date granularity.
            Collapsing the two silently moved 90 records between windows.
            """
            edge = months_back(anchor, months)
            return iso >= edge.isoformat() if dated else int(iso[:4]) >= edge.year

        # Widen only when the assay could be judged at all with more history.
        # An assay with fewer than min_records evaluable records in total can
        # never reach the bar, so widening its window would just quietly stretch
        # the definition of "recent" for no gain.
        months = base_months
        if len(evaluable) >= min_records:
            # Widen a year at a time, only as far as reaching min_records needs.
            while months < max_months and sum(1 for x in evaluable if inside(x, months)) < min_records:
                months += 12
            months = min(months, max_months)
        cutoff = months_back(anchor, months)
        a = AssayDrift(
            assay_id,
            recent_from=(cutoff.strftime("%b %Y") if dated else cutoff.year),
            threshold=threshold,
            min_records=min_records,
            min_decline=min_decline,
            window_months=months,
        )
        # Distinct (call, footprint) classes among evaluable records, per window.
        # If ANY evaluable record lacks a footprint the count is unknown for the
        # whole assay rather than partial: a partial count would be a lower bound
        # on distinct footprints, and so too wide an interval, presented as fact.
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
            in_recent = inside(iso, months)
            (a.recent_counts if in_recent else a.baseline_counts)[call] += 1
            if call in EVALUABLE:
                if fp is None:
                    fp_known = False
                else:
                    (recent_fp if in_recent else base_fp).add((call, fp))
        if fp_known:
            a.recent_footprints = len(recent_fp)
            a.baseline_footprints = len(base_fp)
        a.finalise()
        if months > base_months:
            a.note += f" (window widened to {months} months to reach {min_records} evaluable records)"
        if a.skipped_undated:
            a.note += f" ({a.skipped_undated} records skipped: no deposit date in the metadata)"
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
