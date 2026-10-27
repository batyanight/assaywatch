"""Which oligo positions are failing, and in which groups of accessions.

    python -m assaywatch.sitedrift results/2026-10-17/calls.tsv.gz \
        --registry registry --retrieved data/retrieved --out results/2026-10-17

What this answers that the main report does not
-----------------------------------------------
`report.md` says an assay is declining and by how much. It does not say *where*
on the primer the problem is, or *which* sequences carry it. Those are the two
things that decide what to do next: a substitution one base from the 3' end is
a different problem from one in the middle, and a substitution fixed in a
single clade is a different problem from one scattered across the whole target.

So for each failing assay this report gives:

1. **Per-position statistics.** For every base of every oligo, how many
   evaluable records mismatch there, and the detected share among records that
   mismatch there versus records that do not. The gap between those two shares
   is what makes a position worth acting on. Positions are reported in both
   conventions - counted from the 3' end (the screen's own convention, where 1
   is the 3'-terminal base) and from the 5' end (how a primer is written and
   ordered) - because confusing the two is how a redesign fixes the wrong base.

2. **Footprint groups.** Records sharing an identical mismatch pattern,
   counted, with their deposit years and (heuristically) their organism names.
   One pattern carrying thousands of records is a fixed substitution in
   something; many singleton patterns are background variability or sequencing
   noise, and the two call for different responses.

Honest limits, which the rendered report repeats
------------------------------------------------
- **Bases ARE named, since 2026-10-27.** `score.py` has recorded the substituted
  base since 2026-10-26 (`fwd_mispairs` / `rev_mispairs` / `probe_mispairs`, as
  `A:G@12`), and this module now aggregates them per position, so a row reads
  `G->A 749` and names the code covering both. Two things remain true. The
  FOOTPRINT groups still key on positions alone, so two records differing in
  base at one position are one group there. And score.py records the TEMPLATE
  base, which `parse_mispairs` complements back to the record's own base --
  done once, there, because getting that direction wrong would name the wrong
  replacement.
- **Organism names are a heuristic** parsed from the deposit title, not from a
  taxonomy lookup. They are a navigation aid for finding the affected records,
  not a clade assignment.
- **Association, not causation.** A position whose mismatches coincide with
  failure may be the cause, or may simply travel with the real cause elsewhere
  in the same diverged lineage. The footprint table is printed next to the
  position table so that covariation is visible rather than hidden.
- **No host or country breakdown.** The retrieval metadata carries only
  accession, dates, length and title, so records can be grouped by deposit
  year and by title-derived organism and by nothing else. Host and geography
  would need a different metadata source.

Denominators match the main report exactly: only `detect`, `reduced` and `fail`
rows count, and only the newest version of each accession, so a number here can
be compared with a number there without adjustment.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import sys
from collections import Counter, defaultdict
from collections.abc import Iterable, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from assaywatch import atomic
from assaywatch.drift import EVALUABLE, wilson_interval
from assaywatch.iupac import COMPLEMENT, IUPAC, code_for
from assaywatch.metadata import read_titles

# Statuses whose assays are worth a site breakdown. "watch" is included because
# it is the category an assay passes through on its way to declining, and the
# site table is most useful before the assay has failed outright.
DEFAULT_STATUSES = ("declining", "low coverage", "watch")

MM_COLUMNS = {
    "forward": "fwd_mm_from_3prime",
    "reverse": "rev_mm_from_3prime",
    "probe": "probe_mm_from_3prime",
}

# The columns that carry the SUBSTITUTED BASE, written by score.py since
# 2026-10-26 and not read by anything until 2026-10-27. Each cell is a
# comma-separated list of `OLIGOBASE:TEMPLATEBASE@DISTANCE`, e.g. `G:T@7`.
MISPAIR_COLUMNS = {
    "forward": "fwd_mispairs",
    "reverse": "rev_mispairs",
    "probe": "probe_mispairs",
}

# Short labels for footprint patterns. Spelled out rather than sliced, because
# `"forward"[:3]` is `"for"`, which reads as a typo in the rendered table.
_ABBREV = {"forward": "fwd", "reverse": "rev", "probe": "prb"}

# A mismatch this close to the 3' end blocks extension far more effectively
# than one further back, so the report marks them rather than leaving the
# reader to count. Not a threshold used in any calculation.
THREE_PRIME_ZONE = 5


def _open(path: Path):
    return gzip.open(path, "rt", newline="") if str(path).endswith(".gz") else open(path, newline="")


def parse_positions(cell: str | None) -> tuple[int, ...]:
    """`"14,6,2"` -> `(2, 6, 14)`. Blank or malformed gives `()`."""
    if not cell:
        return ()
    out = []
    for part in str(cell).split(","):
        part = part.strip()
        if part.lstrip("-").isdigit():
            out.append(int(part))
    return tuple(sorted(out))


def parse_mispairs(cell: str | None) -> tuple[tuple[str, str, int], ...]:
    """`"G:T@7,A:C@2"` -> `(("G", "A", 7), ("A", "G", 2))`.

    Returns (oligo base, RECORD base, distance from the oligo's 3' end), and the
    complement in the middle term is the whole subtlety. score.py records the
    TEMPLATE base -- `COMPLEMENT[record_base]` -- because a mispair multiplier is
    defined on the primer base opposite the template base it physically faces
    (a G:T wobble). But a redesign needs the base the RECORD carries in the
    oligo's own sense, because that is what the replacement oligo has to pair
    with. Complementing it back is the difference between "order R" and ordering
    the wrong base entirely, so it is done once, here, and not at each caller.

    The oligo base comes from the mispair cell and NOT from the registry entry,
    which makes this pool-safe: score.py wrote whichever alternate actually won
    the record, so for the ~87 entries carrying `alternates` the base named here
    belongs to the primer that was really scored. The existing `base` column on
    PositionStat is read off the PRIMARY oligo and does not have that property.
    """
    if not cell:
        return ()
    out: list[tuple[str, str, int]] = []
    for part in str(cell).split(","):
        part = part.strip()
        if not part or ":" not in part or "@" not in part:
            continue
        pair, _, dist = part.rpartition("@")
        oligo_base, _, template = pair.partition(":")
        if not dist.lstrip("-").isdigit():
            continue
        oligo_base, template = oligo_base.strip().upper(), template.strip().upper()
        if not oligo_base or not template:
            continue
        out.append((oligo_base, COMPLEMENT.get(template, "N"), int(dist)))
    return tuple(out)


def read_site_calls(path: Path, assay_ids: set[str]) -> list[dict[str, Any]]:
    """Rows for the named assays, keeping the mismatch columns.

    `report.read_calls` folds the six mismatch columns into one interned
    footprint string to hold two million rows in memory; that is the right
    trade for the drift statistic and the wrong one here, where the positions
    are the subject. Restricting to the failing assays keeps the cost small:
    the whole table is streamed, but only the rows asked for are kept.
    """
    wanted = set(assay_ids)
    rows: list[dict[str, Any]] = []
    with _open(path) as fh:
        reader = csv.reader(fh, delimiter="\t")
        header = next(reader, None)
        if header is None:
            return []
        idx = {name: i for i, name in enumerate(header)}
        need = ["assay_id", "record_id", "call"]
        if any(c not in idx for c in need):
            raise ValueError(f"calls table is missing {[c for c in need if c not in idx]}")
        mm_idx = {k: idx.get(v) for k, v in MM_COLUMNS.items()}
        mp_idx = {k: idx.get(v) for k, v in MISPAIR_COLUMNS.items()}
        for row in reader:
            if row[idx["assay_id"]] not in wanted:
                continue
            rec = {
                "assay_id": row[idx["assay_id"]],
                "record_id": row[idx["record_id"]],
                "call": row[idx["call"]],
            }
            for oligo, i in mm_idx.items():
                rec[oligo] = parse_positions(row[i]) if i is not None and i < len(row) else ()
            for oligo, i in mp_idx.items():
                rec[f"{oligo}_mispairs"] = parse_mispairs(row[i]) if i is not None and i < len(row) else ()
            rows.append(rec)
    return rows


# --------------------------------------------------------------------------
# Deposit titles, for naming the affected records
# --------------------------------------------------------------------------

_TITLE_PREFIXES = ("UNVERIFIED_ORG:", "UNVERIFIED:", "TPA_asm:", "TPA:", "MAG:")


def organism_from_title(title: str) -> str:
    """Best-effort organism name from a deposit title.

    A GenBank title starts with the organism and then describes the deposit
    ("Leptospira interrogans strain X lipL32 gene, partial cds"). Taking the
    first two tokens recovers a usable genus/species label for grouping. It is
    a heuristic and is labelled as one everywhere it is shown: "Uncultured
    Leptospira sp." becomes "Leptospira sp.", and a title that does not follow
    the convention gives whatever its first tokens are.
    """
    t = (title or "").strip()
    for p in _TITLE_PREFIXES:
        if t.startswith(p):
            t = t[len(p) :].strip()
    if t[:11].lower() == "uncultured ":
        t = t[11:].strip()
    tokens = t.replace(",", " ").split()
    if not tokens:
        return "unknown"
    if len(tokens) >= 2 and tokens[1][:1].islower():
        return f"{tokens[0]} {tokens[1]}"
    return tokens[0]


# --------------------------------------------------------------------------
# Statistics
# --------------------------------------------------------------------------


@dataclass
class PositionStat:
    oligo: str
    pos_3prime: int
    pos_5prime: int
    base: str
    n_mismatch: int
    detected_with: int
    evaluable_with: int
    detected_without: int
    evaluable_without: int
    # (oligo base, record base, n records), commonest first, from the mispair
    # columns. Empty when the screen predates them (2026-10-26) or when no row
    # recorded one.
    substitutions: tuple[tuple[str, str, int], ...] = ()
    #: Share of the mismatching records a recommended replacement must cover
    #: (`sitedrift.replacement_covers`). 1.0 here so a PositionStat built in a
    #: test recommends the code covering every base seen.
    cover: float = 1.0

    @property
    def scored_bases(self) -> tuple[str, ...]:
        """The oligo bases the SCREEN actually used at this position.

        More than one means a pool assay whose alternates differ here, in which
        case `base` (read off the primary oligo) is not the whole story.
        """
        return tuple(sorted({o for o, _, _ in self.substitutions}))

    @property
    def base_disagrees(self) -> bool:
        """Does the primary oligo's base differ from what was scored?

        True for a pool assay whose winning alternate carries a different base
        here. The old `base` column is read off the primary oligo regardless of
        which alternate won the record, so this is the flag that says so.
        """
        scored = self.scored_bases
        return bool(scored) and (len(scored) > 1 or scored[0] != self.base.upper())

    @property
    def replacement(self) -> str | None:
        """The IUPAC code covering the oligo's base plus every base the records
        carry here -- what you would order to restore inclusivity.

        None when there is no honest single code: an ambiguous record position,
        or a pool whose alternates disagree so that "the" oligo base is not one
        thing. Deliberately not widened to N in that case, because printing N
        would read as advice to order a fully degenerate position.
        """
        if not self.substitutions:
            return None
        scored = self.scored_bases
        if len(scored) != 1:
            return None
        # Only DEFINITE record bases drive a recommendation. An ambiguous record
        # position (or an unrecognised character, which score.py also writes as
        # "N") is not evidence that the target has drifted to anything in
        # particular, and expanding it would union all four bases and recommend
        # ordering `N` -- the one answer this must never give. If that leaves no
        # evidence at all, there is nothing to recommend.
        seen = self._covered_bases()
        if not seen:
            return None
        want: set[str] = set(IUPAC.get(scored[0], scored[0])) | seen
        code = code_for(want)
        if code is None or code == scored[0]:
            return None
        return code

    def _covered_bases(self) -> set[str]:
        """The record bases a replacement has to cover, commonest first until
        `cover` of the mismatching records is accounted for.

        Only DEFINITE bases count. An ambiguous record position (or an
        unrecognised character, which score.py also writes as "N") is not
        evidence that the target has drifted to anything in particular, and
        expanding it would union all four bases and recommend ordering `N` --
        the one answer this must never give.
        """
        definite = [(rb, n) for _, rb, n in self.substitutions if rb in ("A", "C", "G", "T")]
        if not definite:
            return set()
        total = sum(n for _, n in definite)
        out: set[str] = set()
        acc = 0
        for rb, n in sorted(definite, key=lambda x: -x[1]):
            if acc / total >= self.cover:
                break
            out.add(rb)
            acc += n
        return out

    @property
    def replacement_share(self) -> float | None:
        """Share of the mismatching records the recommended code actually covers."""
        definite = [(rb, n) for _, rb, n in self.substitutions if rb in ("A", "C", "G", "T")]
        if not definite:
            return None
        keep = self._covered_bases()
        total = sum(n for *_, n in self.substitutions)
        return sum(n for rb, n in definite if rb in keep) / total if total else None

    @property
    def hypervariable(self) -> bool:
        """Is every base seen here, so that no single oligo covers the position?

        Printed as a word rather than as `N` in the order column: "order N" is
        not an instruction anyone can act on, and the real reading is that the
        assay is being screened against more diversity than one oligo spans.
        """
        scored = self.scored_bases
        if len(scored) != 1 or not self.substitutions:
            return False
        want = set(IUPAC.get(scored[0], scored[0])) | self._covered_bases()
        return want >= set("ACGT")

    @property
    def share_with(self) -> float | None:
        return self.detected_with / self.evaluable_with if self.evaluable_with else None

    @property
    def share_without(self) -> float | None:
        return self.detected_without / self.evaluable_without if self.evaluable_without else None

    @property
    def ci_with(self) -> tuple[float, float]:
        return wilson_interval(self.detected_with, self.evaluable_with)

    @property
    def ci_without(self) -> tuple[float, float]:
        return wilson_interval(self.detected_without, self.evaluable_without)

    @property
    def gap(self) -> float | None:
        """How much worse a record does when it mismatches here. None if undefined."""
        a, b = self.share_without, self.share_with
        return None if a is None or b is None else a - b

    @property
    def three_prime(self) -> bool:
        return self.pos_3prime <= THREE_PRIME_ZONE


@dataclass
class FootprintGroup:
    positions: dict[str, tuple[int, ...]]
    n: int
    calls: Counter = field(default_factory=Counter)
    years: Counter = field(default_factory=Counter)
    organisms: Counter = field(default_factory=Counter)

    @property
    def dominant_call(self) -> str:
        return self.calls.most_common(1)[0][0] if self.calls else "?"

    @property
    def clean(self) -> bool:
        return not any(self.positions.values())

    def describe(self) -> str:
        bits = []
        for oligo in ("forward", "reverse", "probe"):
            p = self.positions.get(oligo) or ()
            if p:
                bits.append(f"{_ABBREV[oligo]} {','.join(str(x) for x in p)}")
        return "; ".join(bits) if bits else "no mismatches"


@dataclass
class AssaySites:
    assay_id: str
    taxon: str
    taxid: int | None
    status: str
    oligo_seqs: dict[str, str]
    positions: list[PositionStat]
    footprints: list[FootprintGroup]
    n_evaluable: int
    n_rows: int
    skipped_no_sequence: list[str] = field(default_factory=list)


def _detected(call: str) -> bool:
    """`reduced` counts as detected, exactly as `drift.YearStats.detected` does."""
    return call in ("detect", "reduced")


def position_stats(
    rows: Sequence[dict[str, Any]],
    oligo: str,
    seq: str,
    min_records: int,
    cover: float = 1.0,
) -> list[PositionStat]:
    """Per-base statistics for one oligo over the evaluable rows given."""
    length = len(seq)
    if not length:
        return []
    # counts[k] = (n_mismatch, n_detected_among_them)
    counts: dict[int, list[int]] = defaultdict(lambda: [0, 0])
    # subs[k][(oligo_base, record_base)] = n records. Tallied from the mispair
    # columns, which name the base the record carries; the position table above
    # can only say THAT a position differs, never to what.
    subs: dict[int, Counter] = defaultdict(Counter)
    total = 0
    total_detected = 0
    for r in rows:
        total += 1
        det = _detected(r["call"])
        total_detected += det
        for k in r.get(oligo) or ():
            if 1 <= k <= length:
                counts[k][0] += 1
                counts[k][1] += det
        for oligo_base, rec_base, k in r.get(f"{oligo}_mispairs") or ():
            # No length guard beyond the shared one: the distance is measured
            # from the 3' end of the oligo that was actually scored, which for a
            # pool assay may be a different length from the primary. Positions
            # past the primary's length are dropped by the same `1 <= k <= length`
            # rule the counts use, so the two tables stay on one axis.
            if 1 <= k <= length:
                subs[k][(oligo_base, rec_base)] += 1

    out: list[PositionStat] = []
    for k, (n_mm, det_mm) in sorted(counts.items()):
        if n_mm < min_records:
            continue
        out.append(
            PositionStat(
                oligo=oligo,
                pos_3prime=k,
                pos_5prime=length - k + 1,
                base=seq[length - k],
                n_mismatch=n_mm,
                detected_with=det_mm,
                evaluable_with=n_mm,
                detected_without=total_detected - det_mm,
                evaluable_without=total - n_mm,
                substitutions=tuple((ob, rb, n) for (ob, rb), n in subs.get(k, Counter()).most_common()),
                cover=cover,
            )
        )
    # Largest gap first: the position that costs the most detection, not the
    # one that happens to vary most often.
    out.sort(key=lambda s: (-(s.gap if s.gap is not None else -1), -s.n_mismatch))
    return out


def footprint_groups(
    rows: Sequence[dict[str, Any]],
    dates: dict[str, str],
    titles: dict[str, str],
    top: int,
) -> list[FootprintGroup]:
    """Records grouped by identical mismatch pattern, commonest first."""
    buckets: dict[tuple, FootprintGroup] = {}
    for r in rows:
        key = tuple((o, r.get(o) or ()) for o in ("forward", "reverse", "probe"))
        g = buckets.get(key)
        if g is None:
            g = buckets[key] = FootprintGroup(positions={o: p for o, p in key}, n=0)
        g.n += 1
        g.calls[r["call"]] += 1
        acc = r["record_id"]
        d = dates.get(acc)
        if d:
            g.years[str(d)[:4]] += 1
        t = titles.get(acc)
        if t:
            g.organisms[organism_from_title(t)] += 1
    ordered = sorted(buckets.values(), key=lambda g: -g.n)
    return ordered[:top]


def analyse_assay(
    assay: Any,
    rows: Sequence[dict[str, Any]],
    status: str,
    dates: dict[str, str],
    titles: dict[str, str],
    *,
    min_records: int = 20,
    top_footprints: int = 8,
    cover: float = 1.0,
) -> AssaySites:
    """Site statistics for one assay from its already-deduplicated rows."""
    evaluable = [r for r in rows if r["call"] in EVALUABLE]
    seqs: dict[str, str] = {}
    missing: list[str] = []
    for name in ("forward", "reverse", "probe"):
        o = getattr(assay.oligos, name, None)
        if o is None:
            continue
        try:
            seqs[name] = o.matching_seq
        except (AttributeError, TypeError):
            missing.append(name)

    positions: list[PositionStat] = []
    for name, seq in seqs.items():
        positions.extend(position_stats(evaluable, name, seq, min_records, cover=cover))
    positions.sort(key=lambda s: (-(s.gap if s.gap is not None else -1), -s.n_mismatch))

    return AssaySites(
        assay_id=assay.id,
        taxon=assay.target.taxon_name or "",
        taxid=assay.target.taxid,
        status=status,
        oligo_seqs=seqs,
        positions=positions,
        footprints=footprint_groups(evaluable, dates, titles, top_footprints),
        n_evaluable=len(evaluable),
        n_rows=len(rows),
        skipped_no_sequence=missing,
    )


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------


def _pct(x: float | None) -> str:
    return "-" if x is None else f"{100 * x:.1f}%"


def _ci(ci: tuple[float, float]) -> str:
    return f"{100 * ci[0]:.0f}-{100 * ci[1]:.0f}%"


def render_markdown(results: Sequence[AssaySites], run_date: str, min_records: int) -> str:
    out = [
        f"# AssayWatch site drift — {run_date}",
        "",
        f"{len(results)} assays with a site breakdown. For each, the oligo positions where "
        f"records differ from the primer, and the groups of accessions that carry each pattern.",
        "",
        "**How to read this.** `pos(3')` counts from the 3' end, where 1 is the 3'-terminal "
        "base — the screen's own convention, and the one that matters for extension. "
        "`pos(5')` counts from the 5' end, which is how the oligo is written and ordered. "
        "`detected|mm` is the detected share among records that mismatch at that position; "
        "`detected|clean` is the share among records that do not. The `gap` between them is "
        "how much detection that position costs. Positions with fewer than "
        f"{min_records} mismatching records are not shown.",
        "",
        "**Reading the base columns.** `base` is the oligo's own base there, from the registry "
        "entry. `records carry` is what the deposits hold instead, tallied from the scored "
        "mismatches, and `order` is the IUPAC code covering both — the base you would order to "
        "restore inclusivity. A star on `base` means the screen scored a different base at that "
        "position, which happens on a pool assay when the winning alternate differs from the "
        "primary oligo; `records carry` then names the primer actually used and `base` does not. "
        "`order` is left blank where no single code is honest, rather than widened to `N`. "
        "**What this cannot tell you.** The footprint groups below key on positions alone, so "
        "two records differing in base at one position are still one group there. Organism "
        "names are parsed from deposit titles as a "
        "navigation aid, not a taxonomy lookup. And a position associated with failure may be "
        "travelling with the real cause elsewhere in the same diverged lineage rather than "
        "causing it — the footprint table below each assay is there so that covariation stays "
        "visible.",
        "",
        "**Which records are counted.** Evaluable records only (`detect`, `reduced`, `fail`), "
        "newest version of each accession — the same record set `report.md` uses. But note "
        "the time span differs: `report.md` headlines the *recent window*, whereas the "
        "position tables below pool **every year**, because a site pattern needs all the "
        "records it can get to be characterised. The per-footprint `deposit years` column is "
        "where the temporal signal lives: a pattern confined to recent years is emerging "
        "drift, one spread evenly across years is long-standing scope mismatch. So a "
        "percentage here will not equal the recent-window percentage in `report.md`, and is "
        "not meant to.",
        "",
    ]
    for r in results:
        out += _render_assay(r)
    return "\n".join(out) + "\n"


def _render_assay(r: AssaySites) -> list[str]:
    taxid = f" (taxid {r.taxid})" if r.taxid else ""
    out = [
        f"## {r.assay_id}",
        "",
        f"{r.taxon}{taxid} — status **{r.status}** — {r.n_evaluable:,} evaluable "
        f"of {r.n_rows:,} screened records",
        "",
    ]
    for name, seq in r.oligo_seqs.items():
        out.append(f"- {name}: `5'-{seq}-3'` ({len(seq)} nt)")
    out.append("")

    if not r.n_evaluable:
        out += ["No evaluable records, so no site statistics.", ""]
        return out

    if r.positions:
        out += [
            "| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | "
            "detected\\|mm | 95% CI | n clean | detected\\|clean | 95% CI | gap | 3' zone |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
        ]
        for p in r.positions:
            out.append(
                f"| {p.oligo} | {p.pos_3prime} | {p.pos_5prime} | `{_base_cell(p)}` | "
                f"{_subs_cell(p)} | {_order_cell(p)} | "
                f"{p.n_mismatch:,} | {_pct(p.share_with)} | {_ci(p.ci_with)} | "
                f"{p.evaluable_without:,} | {_pct(p.share_without)} | {_ci(p.ci_without)} | "
                f"{_pct(p.gap)} | {'yes' if p.three_prime else ''} |"
            )
        out += [
            "",
            "_Both denominators are shown because a large `gap` can rest on a handful of "
            "clean records: when almost every record mismatches at a position, the "
            "comparison group is tiny and the interval, not the point estimate, is the "
            "honest summary. A position mismatching in nearly all records usually means "
            "the assay is being screened against a wider group than it was designed for, "
            "rather than that the group recently changed._",
            "",
        ]
    else:
        out += [
            "No single position reaches the reporting threshold: the mismatches are spread "
            "thinly rather than concentrated. The footprint table below is the informative "
            "view for this assay.",
            "",
        ]

    out += [
        "**Footprint groups** (records sharing one mismatch pattern)",
        "",
        "| pattern | records | dominant call | deposit years | organisms (heuristic) |",
        "|---|---|---|---|---|",
    ]
    for g in r.footprints:
        years = ", ".join(f"{y}×{n}" for y, n in sorted(g.years.items())[-4:]) or "-"
        orgs = ", ".join(f"{o}×{n}" for o, n in g.organisms.most_common(3)) or "-"
        label = "no mismatches" if g.clean else g.describe()
        out.append(f"| {label} | {g.n:,} | {g.dominant_call} | {years} | {orgs} |")
    out.append("")
    return out


def _base_cell(p: PositionStat) -> str:
    """The oligo base, starred when the screen used a different one.

    `PositionStat.base` is read off the PRIMARY oligo, but the screen scored
    whichever alternate won each record. For a pool assay those can differ, and
    silently printing the primary's base would name a base from a different
    primer. A star says the scored base is in the next column.
    """
    return f"{p.base}*" if p.base_disagrees else p.base


def _order_cell(p: PositionStat) -> str:
    """The replacement code and how much of the drift it covers.

    `hypervariable` rather than `N` when every base is seen: "order N" is not an
    instruction, and the honest reading is that the assay is screened against
    more diversity than one oligo spans, which is a coverage story and not a
    redesign.
    """
    if p.hypervariable:
        return "hypervariable"
    if not p.replacement:
        return "-"
    share = p.replacement_share
    # One decimal, not zero: 749 of 754 is 99.6% and `:.0%` renders it as "100%",
    # which claims the code covers every drifted record when it does not.
    return f"`{p.replacement}`" + (f" ({share:.1%})" if share is not None and share < 1 else "")


def _subs_cell(p: PositionStat) -> str:
    """`G->A 749, G->T 5` -- what the records actually carry here."""
    if not p.substitutions:
        return "-"
    shown = p.substitutions[:3]
    cell = ", ".join(f"{ob}&rarr;{rb} {n:,}" for ob, rb, n in shown)
    rest = len(p.substitutions) - len(shown)
    return cell + (f", +{rest} more" if rest else "")


def render_tsv(results: Sequence[AssaySites]) -> str:
    cols = [
        "assay_id",
        "status",
        "taxon",
        "taxid",
        "oligo",
        "pos_3prime",
        "pos_5prime",
        "base",
        # The base the SCREEN used (the winning alternate's, which for a pool
        # assay can differ from `base`), what the records carry, and the code
        # covering both.
        "scored_base",
        "substitutions",
        "replacement",
        "replacement_covers_share",
        "hypervariable",
        "n_mismatch",
        "detected_with",
        "evaluable_with",
        "detected_without",
        "evaluable_without",
        "share_with",
        "share_without",
        "gap",
        "three_prime_zone",
    ]
    lines = ["\t".join(cols)]
    for r in results:
        for p in r.positions:
            lines.append(
                "\t".join(
                    str(x)
                    for x in [
                        r.assay_id,
                        r.status,
                        r.taxon,
                        r.taxid if r.taxid is not None else "",
                        p.oligo,
                        p.pos_3prime,
                        p.pos_5prime,
                        p.base,
                        "/".join(p.scored_bases),
                        ";".join(f"{ob}>{rb}:{n}" for ob, rb, n in p.substitutions),
                        p.replacement or "",
                        "" if p.replacement_share is None else f"{p.replacement_share:.4f}",
                        "yes" if p.hypervariable else "no",
                        p.n_mismatch,
                        p.detected_with,
                        p.evaluable_with,
                        p.detected_without,
                        p.evaluable_without,
                        "" if p.share_with is None else f"{p.share_with:.6f}",
                        "" if p.share_without is None else f"{p.share_without:.6f}",
                        "" if p.gap is None else f"{p.gap:.6f}",
                        "yes" if p.three_prime else "no",
                    ]
                )
            )
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------


def build(
    calls_path: Path,
    registry: Path,
    retrieved: Path,
    cfg: dict[str, Any],
    statuses: Iterable[str] = DEFAULT_STATUSES,
    run_date: str | None = None,
) -> tuple[str, str, list[AssaySites]]:
    """Site-drift report for every assay in the given statuses."""
    from assaywatch.drift import by_status
    from assaywatch.report import apply_anchor_fdr, key_calls_by_accession, read_calls, read_dates
    from assaywatch.validate import iter_files, load_assay

    sd = cfg.get("sitedrift", {}) if isinstance(cfg, dict) else {}
    min_records = int(sd.get("min_records_for_position", 20))
    top_footprints = int(sd.get("top_footprints", 8))
    cover = float(sd.get("replacement_covers", 0.95))

    assays = {}
    for path in iter_files(registry):
        a = load_assay(path)
        assays[a.id] = a

    dates = read_dates(retrieved)
    run_date = run_date or calls_path.parent.name

    # Statuses come from the same assessment the main report uses, so the two
    # documents cannot disagree about which assays are failing.
    from datetime import date as _date

    try:
        today = _date.fromisoformat(run_date[:10])
    except ValueError:
        today = None
    # The report's own assessment, not a stripped-down copy: lineage check, scope
    # filter, patent exclusion and all (see `report.assess_as_reported`). And the
    # same quarantine: an assay the report holds out as not scoreable gets no
    # status here either, so it cannot be listed as failing.
    from assaywatch.report import assess_as_reported, held_out_reasons

    calls = key_calls_by_accession(read_calls(calls_path))
    apply_anchor_fdr(calls, cfg)  # the same relabel report.build applies, so the two cannot disagree
    drifts, _ = assess_as_reported(calls, dates, assays, retrieved, cfg, today)
    drifts = {aid: d for aid, d in drifts.items() if not held_out_reasons(assays.get(aid))}
    grouped = by_status(drifts)

    wanted = {s.lower() for s in statuses}
    selected = [d for status, items in grouped.items() if status.lower() in wanted for d in items]
    selected.sort(key=lambda d: (d.recent_fraction if d.recent_fraction is not None else 1.0, d.assay_id))
    ids = {d.assay_id for d in selected if d.assay_id in assays}

    rows = key_calls_by_accession(read_site_calls(calls_path, ids))
    by_assay: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in rows:
        by_assay[r["assay_id"]].append(r)

    needed = {r["record_id"] for r in rows}
    titles = read_titles(retrieved, needed)

    results = [
        analyse_assay(
            assays[d.assay_id],
            by_assay.get(d.assay_id, []),
            d.status,
            dates,
            titles,
            min_records=min_records,
            top_footprints=top_footprints,
            cover=cover,
        )
        for d in selected
        if d.assay_id in assays
    ]
    return render_markdown(results, run_date, min_records), render_tsv(results), results


def main(argv: list[str] | None = None) -> int:
    from assaywatch.score import load_config

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("calls", type=Path)
    ap.add_argument("--registry", type=Path, default=Path("registry"))
    ap.add_argument("--retrieved", type=Path, default=Path("data/retrieved"))
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--run-date", default=None)
    ap.add_argument(
        "--statuses",
        default=",".join(DEFAULT_STATUSES),
        help="comma-separated drift statuses to include",
    )
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    statuses = [s.strip() for s in args.statuses.split(",") if s.strip()]
    md, tsv, results = build(args.calls, args.registry, args.retrieved, cfg, statuses, run_date=args.run_date)
    args.out.mkdir(parents=True, exist_ok=True)
    atomic.write_text(args.out / "site-drift.md", md)
    atomic.write_text(args.out / "site-drift.tsv", tsv)
    n_pos = sum(len(r.positions) for r in results)
    print(
        f"{len(results)} assays, {n_pos} reported positions -> {args.out / 'site-drift.md'}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
