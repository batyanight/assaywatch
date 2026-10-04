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
"""

from __future__ import annotations

import math
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date
from typing import Any

EVALUABLE = ("detect", "reduced", "fail")
Z95 = 1.959963984540054


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
    # Calls split by the recent-window cutoff as records are added (assess). When
    # empty, finalise falls back to splitting `years` at `recent_from`.
    recent_counts: Counter = field(default_factory=Counter)
    baseline_counts: Counter = field(default_factory=Counter)
    skipped_undated: int = 0

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
            lo, hi = self.change_ci
            declining = self.baseline_evaluable > 0 and hi < 0
            self.status = "declining" if declining else "low coverage"
            self.note = (
                f"detected share {self.recent_fraction:.1%} "
                f"({pct(self.recent_ci[0])}-{pct(self.recent_ci[1])}) since {self.recent_from}, "
                f"upper bound below the {self.threshold:.0%} threshold"
            )
            if self.baseline_evaluable:
                self.note += f"; change from baseline {pct(lo, True)} to {pct(hi, True)}"
                if not declining:
                    trend = "rose from" if lo > 0 else "no measurable fall from"
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
        return self


def pct(x: float, signed: bool = False) -> str:
    """A share as a percentage that never rounds a small number to a misleading 0%.

    Whole percent normally; one decimal below 1% (so a 0.19% bound does not
    print as 0%), and never `-0%`.
    """
    digits = 1 if 0 < abs(x) < 0.01 else 0
    text = f"{x:+.{digits}%}" if signed else f"{x:.{digits}%}"
    return text.replace("-0%", "0%").replace("+0%", "0%") if text in ("-0%", "+0%") else text


def recent_cutoff(cfg: dict[str, Any], today: date | None = None) -> date:
    """The first day of the recent window: `recent_window_months` before `today`."""
    months = int(cfg.get("drift", {}).get("recent_window_months", 24))
    today = today or date.today()
    y, m = divmod(today.year * 12 + today.month - 1 - months, 12)
    return date(y, m + 1, min(today.day, 28))


def recent_cutoff_year(cfg: dict[str, Any], today: date | None = None) -> int:
    """The year the recent window starts in (for records dated only to the year)."""
    return recent_cutoff(cfg, today).year


def assess(
    calls: list[dict[str, Any]],
    years: dict[str, int | str],
    cfg: dict[str, Any],
    today: date | None = None,
) -> dict[str, AssayDrift]:
    """Group calls by assay and deposit date and work out each assay's status.

    `calls` are rows from the screen stage; `years` maps record id to its
    deposit date (ISO `YYYY-MM-DD`, as report.read_dates gives) or just a year.
    With dates the recent window is exactly `recent_window_months` long; with
    bare years it starts on 1 January of the cutoff year. A record with no
    date is counted as skipped, never bucketed into a default, because an
    unknown year silently landing in the recent window is the kind of error
    that produces a confident wrong answer.
    """
    d = cfg.get("drift", {})
    cutoff = recent_cutoff(cfg, today)
    cutoff_iso = cutoff.isoformat()
    threshold = float(d.get("detect_fraction_threshold", 0.9))
    min_records = int(d.get("min_records_for_drift", 20))

    grouped: dict[str, AssayDrift] = {}
    dated = any(isinstance(v, str) for v in years.values())
    label: int | str = cutoff.strftime("%b %Y") if dated else cutoff.year
    for row in calls:
        # Created before the date check, so an assay whose records are all
        # undated still appears (as no recent data) with its skipped count.
        a = grouped.setdefault(
            row["assay_id"],
            AssayDrift(row["assay_id"], recent_from=label, threshold=threshold, min_records=min_records),
        )
        when = years.get(row["record_id"])
        if when is None:
            a.skipped_undated += 1
            continue
        if isinstance(when, str):
            year, recent = int(when[:4]), when >= cutoff_iso
        else:
            year, recent = int(when), int(when) >= cutoff.year
        a.years.setdefault(year, YearStats(year)).counts[row["call"]] += 1
        (a.recent_counts if recent else a.baseline_counts)[row["call"]] += 1

    for a in grouped.values():
        a.finalise()
        if a.skipped_undated:
            a.note += f" ({a.skipped_undated} records skipped: no deposit date in the metadata)"
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
