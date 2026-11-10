"""The coverage map: which species each assay is predicted to detect, as of today.

    assaywatch coverage results/2026-11-01/calls.tsv.gz --out results/2026-11-01
    assaywatch coverage results/2026-11-01/calls.tsv.gz --out /tmp/c --recommend 10493

COVERAGE IS NOT DRIFT. Both are summaries of the same calls table (one row per
assay per record). Drift groups it by deposit year and asks whether an assay has got
worse. Coverage groups it by species and asks what the assay picks up today, with no
time axis at all. Neither module imports the other, and coverage is the primary
product: the sentences it exists to support are "this assay also picks up X", "this
assay fails on X" and "for X, use this other assay". Vocabulary: GLOSSARY.md,
"Coverage".

THE SHAPE. `coverage_map` is the whole of the logic and it is a pure function: it
takes rows, two lookups and a rule, and returns plain data. It opens no file and
reads no config, so a test is a handful of hand-written rows. Everything that
touches the disk is in `main`, at the bottom, and does no deciding.

WHAT A CELL IS. One assay on one species (an NCBI species taxid), in one of four
states, always carried with the count behind it:

    predicted detect   the records carry no mismatch that would block the reaction
    partial            the records split, or are detected with an expected Ct shift
    predicted fail     the locus is in the records and the oligos are predicted
                       not to amplify it
    not assessable     no record of the species is shown to hold the locus

The first is worded weakly on purpose and the third strongly. A 3'-terminal mismatch
or a missing primer site is good evidence of failure from sequence alone; a matching
primer says the oligos fit and says nothing about whether the reaction works.

HONEST LIMITS, as built on 2026-11-10:

* NO LOCUS CHECK YET. The only evidence that a record holds the locus is that the
  primers found their sites in it (a `detect`, `reduced` or `fail` call, or a
  `no_amplicon` the screen labelled `diverged`). A record of a distant species in
  which neither primer lands is therefore invisible, which blanks the map exactly
  where an assay fails hardest. `locus_present` on a row is the seam the locus check
  will write to; see `_locus_present`.
* NO WIDENED RETRIEVAL YET. A species has a row only if records of it are already in
  the assay's archive, which was fetched for the assay's own target.
* NO HOSTS YET. Archive metadata does not store GenBank's `/host` qualifier, so the
  host column is empty on real runs.
* RECORDS ARE NOT INDEPENDENT. 300 records of one outbreak are one observation
  deposited 300 times. That is why no interval and no p-value is printed, and why
  `footprints` (distinct mismatch patterns) sits beside every count.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import sys
from collections import Counter, defaultdict
from collections.abc import Callable, Iterable, Iterator, Mapping
from dataclasses import dataclass, field
from enum import StrEnum
from itertools import chain
from pathlib import Path
from typing import Any

from assaywatch.accession import strip_version

# The footprint is defined with the table it is read from (`calls`), not with the drift
# statistic: this module must not load `assaywatch.drift` (tests/test_coverage.py).
from assaywatch.calls import FOOTPRINT_COLUMNS, FOOTPRINT_REQUIRED, footprint_signature
from assaywatch.locus import read_locus
from assaywatch.nested import NestPath, _protocol_records, nest_scope
from assaywatch.nested import paths as nest_paths
from assaywatch.registry import load as load_registry
from assaywatch.score import load_config
from assaywatch.taxonomy import taxonomy_from_config

#: A call that means the reaction is predicted to give product.
DETECTED = ("detect", "reduced")
#: A call the screen could only make because both primers found their sites.
SCORED = ("detect", "reduced", "fail")
#: The `exclusion` the screen writes when a site is in the deposit and does not match.
DIVERGED = "diverged"
#: The columns the trace rule reads from a round-1 row.
TRACE_COLUMNS = ("fwd_mm_from_3prime", "rev_mm_from_3prime", "fwd_mispairs", "rev_mispairs")


class CellState(StrEnum):
    """The four things a coverage cell can say. The values are the words printed."""

    predicted_detect = "predicted detect"
    partial = "partial"
    predicted_fail = "predicted fail"
    not_assessable = "not assessable"


@dataclass(frozen=True)
class CoverageRule:
    """Where `partial` begins and ends, as shares of a cell's locus-present records.

    `frozen=True`: an instance cannot be changed after it is built, so the rule a
    cell was judged by is the rule that was read from config.yaml.

    A cell is `predicted fail` when its DETECTED share is at most `fail_max_share`,
    `predicted detect` when its CLEANLY detected share (calls of `detect`, leaving
    `reduced` out) is at least `detect_min_share`, and `partial` otherwise.
    """

    detect_min_share: float
    fail_max_share: float

    def __post_init__(self) -> None:
        # Runs once, straight after the two fields are set. A rule that cannot mean
        # anything is refused here instead of quietly mislabelling every cell.
        if not 0.0 <= self.fail_max_share < self.detect_min_share <= 1.0:
            raise ValueError(
                "coverage shares must satisfy 0 <= fail_max_share < detect_min_share <= 1, "
                f"got fail_max_share={self.fail_max_share}, detect_min_share={self.detect_min_share}"
            )

    def state(self, clean: int, detected: int, locus_present: int) -> CellState:
        if locus_present == 0:
            return CellState.not_assessable
        if detected <= self.fail_max_share * locus_present:
            return CellState.predicted_fail
        if clean >= self.detect_min_share * locus_present:
            return CellState.predicted_detect
        return CellState.partial


def rule_from_config(cfg: Mapping[str, Any]) -> CoverageRule:
    """The one place the config is read on coverage's behalf."""
    c = cfg["coverage"]
    return CoverageRule(float(c["detect_min_share"]), float(c["fail_max_share"]))


@dataclass(frozen=True)
class CoverageCell:
    """One assay on one species. `detected`/`locus_present` is the cell count."""

    assay_id: str
    species_taxid: int
    in_scope: bool
    state: CellState
    detected: int  # numerator: records called `detect` or `reduced`
    locus_present: int  # denominator: records shown to hold the locus
    footprints: int  # distinct mismatch patterns among them (0 = none recorded)
    hosts: tuple[str, ...]  # as written in the records, most common first
    reduced: int = 0  # of `detected`, how many carry an expected Ct shift

    @property
    def count(self) -> str:
        return f"{self.detected}/{self.locus_present}"


@dataclass
class _Tally:
    """What `coverage_map` accumulates for one cell before it is judged."""

    clean: int = 0
    reduced: int = 0
    locus_present: int = 0
    footprints: set[str] = field(default_factory=set)
    hosts: Counter = field(default_factory=Counter)


def _locus_present(row: Mapping[str, Any]) -> bool:
    """Is this record shown to hold the assay's target region?

    A `locus_present` key on the row wins: that is what the locus check will write.
    Without it the screen's own evidence is all there is. Both primers found a site
    (any scored call), or the screen saw a site that is present and does not match
    (`diverged`). A truncated deposit, an `indeterminate` call or a record with no
    credible site says something about GenBank and nothing about the assay.
    """
    explicit = row.get("locus_present")
    if explicit is not None:
        return bool(explicit)
    return row.get("call") in SCORED or row.get("exclusion") == DIVERGED


def coverage_map(
    calls: Iterable[Mapping[str, Any]],
    species_of: Callable[[str], int | None],
    scope_of: Callable[[str, int], bool],
    rule: CoverageRule,
) -> list[CoverageCell]:
    """Group a calls table by (assay, species) and judge each group.

    `calls`       rows in the screen's shape: `assay_id`, `record_id`, `call`,
                  `exclusion`, and optionally `footprint`, `host`, `locus_present`.
                  Any iterable, read once, so a 3.5-million-row table can be streamed.
    `species_of`  record id -> NCBI species taxid, or None when it cannot be placed.
                  A record with no species is left out; counting those is the
                  caller's job, because only the caller knows why.
    `scope_of`    (assay id, species taxid) -> is this species inside what the assay
                  was published for? Used ONLY to label the cell. Nothing is dropped.
    `rule`        where `partial` begins and ends.

    Every (assay, species) pair with at least one row gets a cell, including one
    with no locus-present record at all (`not assessable`): a blank is information.
    Returned sorted by assay, in-scope block first, then species taxid.
    """
    tallies: dict[tuple[str, int], _Tally] = defaultdict(_Tally)
    for row in calls:
        species = species_of(row["record_id"])
        if species is None:
            continue
        t = tallies[(row["assay_id"], species)]
        if host := row.get("host"):
            t.hosts[host] += 1
        if not _locus_present(row):
            continue
        t.locus_present += 1
        call = row.get("call")
        if call == "detect":
            t.clean += 1
        elif call == "reduced":
            t.reduced += 1
        if fp := row.get("footprint"):
            t.footprints.add(fp)

    cells = []
    for (assay_id, species), t in tallies.items():
        detected = t.clean + t.reduced
        cells.append(
            CoverageCell(
                assay_id=assay_id,
                species_taxid=species,
                in_scope=bool(scope_of(assay_id, species)),
                state=rule.state(t.clean, detected, t.locus_present),
                detected=detected,
                locus_present=t.locus_present,
                footprints=len(t.footprints),
                # most common first; ties broken by name so the order is reproducible
                hosts=tuple(h for h, _ in sorted(t.hosts.items(), key=lambda kv: (-kv[1], kv[0]))),
                reduced=t.reduced,
            )
        )
    cells.sort(key=lambda c: (c.assay_id, not c.in_scope, c.species_taxid))
    return cells


_RANK = {
    CellState.predicted_detect: 0,
    CellState.partial: 1,
    CellState.predicted_fail: 2,
    CellState.not_assessable: 3,
}


def recommend(
    cells: Iterable[CoverageCell],
    species_taxid: int,
    degeneracy_of: Mapping[str, float] | None = None,
) -> list[CoverageCell]:
    """The assays for one species, best first. A ranking, never a verdict.

    Ordered by cell state; then toward the less degenerate primer pool, which is the
    only place degeneracy acts (it never changes a cell); then toward the higher
    detected share and the larger count behind it; then by id, so that two runs on
    the same table print the same order.
    """
    fold = degeneracy_of or {}

    def key(c: CoverageCell) -> tuple:
        share = c.detected / c.locus_present if c.locus_present else 0.0
        return (_RANK[c.state], fold.get(c.assay_id, 0), -share, -c.locus_present, c.assay_id)

    return sorted((c for c in cells if c.species_taxid == species_taxid), key=key)


# --- nested rows ---------------------------------------------------------------------
#
# A nested protocol gets TOGETHER (round 1 then round 2, as published), ROUND 1 ALONE
# and ROUND 2 ALONE. The two "alone" rows need nothing built: each round is already a
# registry entry screened as an independent assay, and a round's own row IS that
# primer pair on raw template. Only `together` is synthesised here.
#
# TOGETHER IS SHOWN TWICE (a maintainer decision, 2026-11-10), because how much round
# 1 has to do is not known and the two readings are far apart. Under the trace rule
# round 1 only has to make a little product; under the strict rule it has to be
# detected in its own right. On the 2026-11-01 calls the trace row sat within 2 points
# of round 2 alone for 18 of 34 protocols, while the strict row follows round 1. The
# truth for a given protocol is somewhere between, and both rows stay until a bench
# panel says where.


class Together(StrEnum):
    """Which rule round 1 is held to inside a `together` row."""

    trace = "trace"  # fails only on a 3'-terminal mismatch or no site
    strict = "strict"  # must itself be called `detect` or `reduced`


def together_id(nest_id: str, rule: Together) -> str:
    """The row id of a nested protocol run as published; `nest_id` is its last round."""
    return f"{nest_id}@together-{rule.value}"


def _terminal_blocked(row: Mapping[str, Any], free_mispairs: frozenset[str]) -> bool | None:
    """Does either primer carry a 3'-terminal mismatch that blocks extension?

    None when the row does not carry the mismatch columns (an older screen), so the
    caller can tell "no terminal mismatch" from "cannot say".

    `fwd_mm_from_3prime` lists mismatch positions counted from the primer's 3' end,
    so `1` is the terminal base. `fwd_mispairs` names each as `oligo:template@position`
    (`C:A@1`). A terminal mispair the scoring config prices at zero (the G:T wobble)
    does not block, exactly as in `score.score_primer`.
    """
    if any(c not in row for c in TRACE_COLUMNS):
        return None
    for side in ("fwd", "rev"):
        if "1" not in str(row[f"{side}_mm_from_3prime"]).split(","):
            continue
        terminal = [m.split("@")[0] for m in str(row[f"{side}_mispairs"]).split(",") if m.endswith("@1")]
        if not (terminal and terminal[0] in free_mispairs):
            return True
    return False


def trace_passes(row: Mapping[str, Any], free_mispairs: frozenset[str]) -> bool:
    """The trace rule: does round 1 hand round 2 at least a trace of product?

    Round 1 of a nest runs at a forgiving anneal for many cycles and only has to
    make a little product for round 2 to amplify. So inside a `together` row it
    fails ONLY on a 3'-terminal mismatch or on no site at all, and a `fail` earned on
    accumulated penalty alone still passes. A `fail` row that cannot say why it
    failed is read strictly: it does not pass.

    Agreed in outline 2026-11-10 and NOT measured. No bench panel stands behind it.
    """
    call = row.get("call")
    if call in DETECTED:
        return True
    if call == "fail":
        return _terminal_blocked(row, free_mispairs) is False
    return False


def strict_passes(row: Mapping[str, Any]) -> bool:
    """The strict rule: round 1 must itself be detected, as `nested.nest_calls` reads it."""
    return row.get("call") in DETECTED


def with_locus(row: dict[str, Any], checked: Mapping[str, bool] | None) -> dict[str, Any]:
    """Join the locus stage's verdict onto one row of the calls table.

    `checked` is record id -> "the locus is present with room for the primers", for
    this row's assay (`locus.read_locus`), or None when the stage was not run on it.
    A record the stage did not check is returned as it came.

    A record the stage shows to hold the locus, in which the screen found no primer
    site, is relabelled `diverged`: the site is there and the primers do not fit it,
    which is what that label has always meant. That one word is what lets a nested
    protocol see the record too (`nested._protocol_records` counts a `diverged`
    round-1 record as the assay's failure and passes over an unlabelled one).
    """
    if checked is None or row["record_id"] not in checked:
        return row
    present = checked[row["record_id"]]
    row["locus_present"] = present
    if present and row.get("call") == "no_amplicon":
        row["exclusion"] = DIVERGED
    return row


def together_calls(
    path: NestPath,
    calls: Mapping[str, Mapping[str, Mapping[str, Any]]],
    free_mispairs: frozenset[str],
    rule: Together,
) -> Iterator[dict[str, Any]]:
    """One `together` row per record every round of the protocol can be judged on.

    `calls` is assay id -> record id -> row, holding at least the path's rounds.
    The row is the LAST round's own row (its call, its footprint), scored normally,
    downgraded to `fail` when any earlier round does not pass `rule`: the cell is
    the worse of the two. Which records count is `nested._protocol_records`, the
    definition the drift side of nested protocols already uses, so the two cannot
    disagree about a record, and the trace and strict rows share one denominator.
    """
    for row, upstream in _protocol_records(path, calls):
        out = dict(row)
        out["assay_id"] = together_id(path.nest_id, rule)
        passes = [
            trace_passes(r, free_mispairs) if rule is Together.trace else strict_passes(r) for r in upstream
        ]
        if not all(passes):
            out["call"] = "fail"
            out["exclusion"] = ""
        yield out


# --- everything below touches the disk and decides nothing -------------------------------


def read_rows(path: Path, degeneracy: dict[str, tuple[float, str]] | None = None) -> Iterator[dict[str, Any]]:
    """Stream a calls table as the small rows `coverage_map` reads.

    A generator (`yield`), so the table is never held in memory: each row is built,
    handed to the caller and dropped. `degeneracy`, when given, is filled as a side
    effect with each assay's (fold, tier) from the first row that carries one.
    """
    opener = gzip.open if str(path).endswith(".gz") else open
    with opener(path, "rt", newline="") as fh:
        reader = csv.reader(fh, delimiter="\t")
        header = next(reader, None)
        if header is None:
            return
        at = {name: i for i, name in enumerate(header)}
        ia, ir, ic = at["assay_id"], at["record_id"], at["call"]
        ie = at.get("exclusion")
        fp_idx = (
            [at[c] for c in FOOTPRINT_COLUMNS]
            if all(c in at for c in (*FOOTPRINT_COLUMNS, *FOOTPRINT_REQUIRED))
            else None
        )
        req_idx = [at[c] for c in FOOTPRINT_REQUIRED] if fp_idx is not None else []
        trace_idx = [(c, at[c]) for c in TRACE_COLUMNS] if all(c in at for c in TRACE_COLUMNS) else []
        deg_idx = (at["degeneracy_fold"], at["degeneracy_tier"]) if "degeneracy_fold" in at else None
        for r in reader:
            if not r:
                continue
            row: dict[str, Any] = {
                "assay_id": r[ia],
                "record_id": r[ir],
                "call": r[ic],
                "exclusion": r[ie] if ie is not None and ie < len(r) else "",
            }
            # Known only where the row's own scoring cells are filled: see calls.read_calls.
            if fp_idx is not None and all(i < len(r) and r[i] != "" for i in req_idx):
                row["footprint"] = footprint_signature(r[i] if i < len(r) else "" for i in fp_idx)
                for name, i in trace_idx:
                    row[name] = r[i] if i < len(r) else ""
            if degeneracy is not None and deg_idx is not None and row["assay_id"] not in degeneracy:
                fold, tier = (r[i] if i < len(r) else "" for i in deg_idx)
                if fold:
                    degeneracy[row["assay_id"]] = (float(fold), tier)
            yield row


def read_taxids(retrieved: Path, sidecar: Path | None = None) -> dict[str, int]:
    """Unversioned accession -> taxid, from the backfill sidecar and archive metadata."""
    out: dict[str, int] = {}
    sidecar = sidecar or retrieved / ".meta.taxid.backfill.tsv.gz"
    if sidecar.exists():
        with gzip.open(sidecar, "rt") as fh:
            next(fh, None)
            for line in fh:
                acc, _, tx = line.rstrip("\n").partition("\t")
                if tx.isdigit():
                    out[strip_version(acc)] = int(tx)
    for meta in sorted(retrieved.rglob("*.meta.tsv.gz")):
        with gzip.open(meta, "rt") as fh:
            header = (fh.readline() or "").rstrip("\n").split("\t")
            if "accession" not in header or "taxid" not in header:
                continue  # a pre-taxid archive; the sidecar covers it
            ai, ti = header.index("accession"), header.index("taxid")
            for line in fh:
                parts = line.rstrip("\n").split("\t")
                if len(parts) > max(ai, ti) and parts[ti].isdigit():
                    out[strip_version(parts[ai])] = int(parts[ti])
    return out


TSV_COLUMNS = (
    "assay_id",
    "row",
    "species_taxid",
    "species",
    "in_scope",
    "state",
    "detected",
    "reduced",
    "locus_present",
    "footprints",
    "hosts",
    "degeneracy_fold",
    "degeneracy_tier",
)


def _fold(fold: float) -> str:
    return f"{fold:g}x"


def write_tsv(
    path: Path,
    cells: Iterable[CoverageCell],
    name_of: Callable[[int], str],
    row_kind: Callable[[str], str],
    degeneracy: Mapping[str, tuple[float, str]],
) -> None:
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(TSV_COLUMNS)
        for c in cells:
            fold, tier = degeneracy.get(c.assay_id, ("", ""))
            w.writerow(
                [
                    c.assay_id,
                    row_kind(c.assay_id),
                    c.species_taxid,
                    name_of(c.species_taxid),
                    "yes" if c.in_scope else "no",
                    c.state.value,
                    c.detected,
                    c.reduced,
                    c.locus_present,
                    c.footprints,
                    "; ".join(c.hosts),
                    f"{fold:g}" if fold != "" else "",
                    tier,
                ]
            )


_CELL_CLAIMS = (
    (
        "predicted detect",
        "The records carry no mismatch that would block the reaction. It says the oligos match; "
        "it does not say the reaction works.",
    ),
    (
        "partial",
        "The records split between detected and not, or they are detected with an expected loss "
        "of efficiency (the `Ct shift` column counts those).",
    ),
    (
        "predicted fail",
        "The locus is in the records and the oligos are predicted not to amplify it. The stronger "
        "claim: a 3'-terminal mismatch or a missing site is good evidence from sequence alone.",
    ),
    (
        "not assessable",
        "No record of this species is shown to hold the locus, so the assay was never tested by "
        "the data. Not a failure.",
    ),
)

LEGEND = (
    """\
## How to read a cell

Every cell is printed with its **count**: records detected over records shown to hold
the locus. A `3/3` and a `300/300` are both shown; judging them is left to the reader.
**Footprints** is the number of distinct mismatch patterns behind that count, because
GenBank records are not independent: `300/300` from 2 footprints is one outbreak
sequenced 300 times.

| cell | what it claims |
|---|---|
"""
    + "".join(f"| `{state}` | {claim} |\n" for state, claim in _CELL_CLAIMS)
    + """
A nested protocol has each round alone on raw template, and `together` (round 1 then round
2, as published) shown twice, because how much round 1 has to do is not measured:
`together (trace rule)` lets round 1 through unless it has a 3'-terminal mismatch or no
site, and `together (strict)` needs round 1 detected in its own right. Read the pair as a
range. Where they agree the protocol's cell is not in doubt.

## What this map cannot see yet

- **No locus check.** A record counts only if the primers found their sites in it. A
  distant species in which neither primer lands is missing or `not assessable`, so the
  map is blank exactly where an assay fails hardest. Read an absent species as unknown.
- **No widened retrieval.** A species has a row only if its records were already in the
  assay's archive, which was fetched for the assay's own target.
- **No hosts.** The archives do not store GenBank's `/host` qualifier.
"""
)


def render_markdown(
    cells: Iterable[CoverageCell],
    name_of: Callable[[int], str],
    row_kind: Callable[[str], str],
    degeneracy: Mapping[str, tuple[float, str]],
    header_lines: list[str],
) -> str:
    out = ["# Coverage map", "", *header_lines, "", LEGEND]
    by_assay: dict[str, list[CoverageCell]] = defaultdict(list)
    for c in cells:
        by_assay[c.assay_id].append(c)
    for assay_id in sorted(by_assay):
        kind = row_kind(assay_id)
        title = f"## `{assay_id}`" + (f" ({kind})" if kind else "")
        out += [title, ""]
        if assay_id in degeneracy:
            fold, tier = degeneracy[assay_id]
            out += [
                f"Primer-pool degeneracy: {_fold(fold)} ({tier}). It annotates the row, never a cell.",
                "",
            ]
        for label, wanted in (("In scope", True), ("Out of scope", False)):
            everything = [c for c in by_assay[assay_id] if c.in_scope is wanted]
            # A `not assessable` cell has no count to print (it is 0/0), and a pan-family
            # archive holds thousands of them. They are summed into one line here and
            # listed one by one in coverage.tsv. No cell WITH a count is ever folded.
            block = [c for c in everything if c.state is not CellState.not_assessable]
            blank = len(everything) - len(block)
            if not everything:
                continue
            out += [f"**{label}**", ""]
            if block:
                out += [
                    "| species | cell | count | footprints | Ct shift | hosts |",
                    "|---|---|---|---|---|---|",
                ]
            # the largest count first: the rows with most behind them lead
            for c in sorted(block, key=lambda c: (-c.locus_present, c.species_taxid)):
                out.append(
                    f"| {name_of(c.species_taxid)} ({c.species_taxid}) | `{c.state.value}` | {c.count} "
                    f"| {c.footprints} | {c.reduced or ''} | {'; '.join(c.hosts)} |"
                )
            if blank:
                out += [
                    "",
                    f"{blank} more species `not assessable` (no record holds the locus); see coverage.tsv.",
                ]
            out.append("")
    return "\n".join(out) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="assaywatch coverage", description=__doc__.split("\n\n")[0])
    ap.add_argument("calls", type=Path, help="calls table (TSV or TSV.GZ)")
    ap.add_argument(
        "--retrieved", type=Path, default=Path("data/retrieved"), help="archives, for record taxids"
    )
    ap.add_argument("--registry", type=Path, default=Path("registry"))
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--out", type=Path, required=True, help="directory for coverage.tsv and coverage.md")
    ap.add_argument("--locus", type=Path, help="side file from `assaywatch locus`: joined as locus_present")
    ap.add_argument(
        "--recommend", type=int, metavar="TAXID", help="also print the assays ranked for this species"
    )
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    rule = rule_from_config(cfg)
    taxonomy = taxonomy_from_config(cfg)
    if taxonomy is None:
        print(
            "coverage needs drift.scope_taxonomy: rows are species, and species come from it", file=sys.stderr
        )
        return 2
    assays = load_registry(args.registry)
    taxids = read_taxids(args.retrieved)

    # A species row is "in scope" when it sits under a taxon the assay names, or when
    # the assay names something BELOW it (a subtype or strain assay: its species row
    # is the row its own target lives in).
    paths = nest_paths(assays)
    scope: dict[str, frozenset[int]] = {}
    for aid, a in assays.items():
        named = a.target.scope_taxids or ([a.target.taxid] if a.target.taxid else [])
        scope[aid] = frozenset(taxonomy.canonical(int(t)) for t in named)
    for p in paths:
        narrowed = nest_scope(p, assays)
        own = frozenset(taxonomy.canonical(t) for t in narrowed) if narrowed else scope.get(p.nest_id)
        for how in Together:
            scope[together_id(p.nest_id, how)] = own or frozenset()
    scope_species = {aid: {taxonomy.species_of(t) for t in s} for aid, s in scope.items()}

    def scope_of(assay_id: str, species: int) -> bool:
        s = scope.get(assay_id)
        return bool(s) and (taxonomy.within(species, s) or species in scope_species[assay_id])

    unplaced = Counter()
    species_cache: dict[int, int | None] = {}

    def species_of(record_id: str) -> int | None:
        taxid = taxids.get(strip_version(record_id))
        if taxid is None:
            unplaced["no taxid"] += 1
            return None
        if taxid not in species_cache:
            species_cache[taxid] = taxonomy.species_of(taxid)
        if species_cache[taxid] is None:
            unplaced["above species rank"] += 1
        return species_cache[taxid]

    # The locus check's verdicts, where the stage was run. A record in the file gets an
    # explicit `locus_present`, which `_locus_present` prefers to the screen's guess; a
    # record not in it keeps the screen's evidence.
    locus_of = read_locus(args.locus) if args.locus else {}

    # First pass: keep only the rows of nested rounds, which `together` has to join
    # record by record. Second pass: stream everything into the map.
    members = {r for p in paths for r in p.rounds}
    nested_rows: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
    if members:
        for row in read_rows(args.calls):
            if row["assay_id"] in members:
                nested_rows[row["assay_id"]][row["record_id"]] = with_locus(
                    row, locus_of.get(row["assay_id"])
                )
    free = frozenset(k for k, v in (cfg["scoring"].get("mispair_penalty") or {}).items() if float(v) == 0.0)
    together = chain.from_iterable(
        together_calls(p, nested_rows, free, how) for p in paths for how in Together
    )

    # An assay in the calls table that the registry no longer holds (renamed, or moved
    # to pending/ since the screen) has no declared scope, so every one of its rows
    # would read "out of scope". It is left out and named in the report's header.
    not_in_registry: set[str] = set()

    def registered(rows: Iterable[dict[str, Any]]) -> Iterator[dict[str, Any]]:
        for row in rows:
            if row["assay_id"] in assays:
                yield with_locus(row, locus_of.get(row["assay_id"]))
            else:
                not_in_registry.add(row["assay_id"])

    degeneracy: dict[str, tuple[float, str]] = {}
    screened = registered(read_rows(args.calls, degeneracy))
    cells = coverage_map(chain(screened, together), species_of, scope_of, rule)
    for p in paths:  # a protocol is as degenerate as its most degenerate round
        folds = [degeneracy[r] for r in p.rounds if r in degeneracy]
        for how in Together if folds else ():
            degeneracy[together_id(p.nest_id, how)] = max(folds)

    round_of = {aid: a.source.nested_round for aid, a in assays.items() if aid in members}

    def row_kind(assay_id: str) -> str:
        if assay_id.endswith("@together-trace"):
            return "together (trace rule)"
        if assay_id.endswith("@together-strict"):
            return "together (strict)"
        # `nested_round` is the registry's own label for the round ("round1", "round2B")
        return f"{round_of[assay_id]} alone" if round_of.get(assay_id) else ""

    def name_of(taxid: int) -> str:
        return taxonomy.name.get(taxid, "unnamed")

    states = Counter(c.state.value for c in cells)
    header = [
        f"From `{args.calls}`. {len({c.assay_id for c in cells})} rows of assays, "
        f"{len({c.species_taxid for c in cells})} species, {len(cells)} cells: "
        + ", ".join(f"{n} {s}" for s, n in sorted(states.items()))
        + ".",
        f"Cuts: `predicted detect` at {rule.detect_min_share:.0%} or more cleanly detected, "
        f"`predicted fail` at {rule.fail_max_share:.0%} or fewer detected (`config.yaml`, `coverage:`).",
    ]
    if unplaced:
        header.append(
            "Rows left out because the record could not be placed in a species: "
            + ", ".join(f"{n} {why}" for why, n in sorted(unplaced.items()))
            + "."
        )
    if not_in_registry:
        header.append(
            f"Left out: {len(not_in_registry)} assay id(s) in the calls table the registry does not hold "
            "(renamed or moved to pending/ since the screen): "
            + ", ".join(f"`{a}`" for a in sorted(not_in_registry))
            + "."
        )
    args.out.mkdir(parents=True, exist_ok=True)
    write_tsv(args.out / "coverage.tsv", cells, name_of, row_kind, degeneracy)
    (args.out / "coverage.md").write_text(render_markdown(cells, name_of, row_kind, degeneracy, header))
    print(f"{len(cells)} cells -> {args.out / 'coverage.tsv'}, {args.out / 'coverage.md'}", file=sys.stderr)

    if args.recommend is not None:
        folds = {aid: f for aid, (f, _) in degeneracy.items()}
        # Rows are species. A strain, a subtype or a taxid NCBI has since renamed is
        # rolled up to the species row it lives in, as every record's taxid is.
        wanted = taxonomy.species_of(args.recommend) or args.recommend
        print(f"Assays for {name_of(wanted)} ({wanted}), best first:")
        for c in recommend(cells, wanted, folds):
            deg = f", degeneracy {_fold(folds[c.assay_id])}" if c.assay_id in folds else ""
            scope_note = "in scope" if c.in_scope else "out of scope"
            print(
                f"  {c.state.value:<17} {c.count:>11}  {c.footprints} footprints  {c.assay_id} ({scope_note}{deg})"  # noqa: E501
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
