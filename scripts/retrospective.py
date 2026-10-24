#!/usr/bin/env python3
"""What would AssayWatch have said on a past date? Tier-2 validation's measuring stick.

    python scripts/retrospective.py --as-of 2014-01-01 --assay CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004
    python scripts/retrospective.py --cases docs/validation-cases.tsv

Every threshold in config.yaml was set by eye, so the statuses mean "worth
looking at" rather than anything measured. The way to calibrate them is to ask
whether the tool agrees with assays whose real-world performance the literature
later reported — using only the sequence records that existed before that
report, so the tool is not told the answer.

An "as of" run is the ordinary report pipeline with two restrictions: records
deposited on or after the cutoff are dropped, and the recent window is measured
backwards from the cutoff instead of from today. Nothing else changes, so a
retrospective verdict is directly comparable with a current one.

With --cases it reads a TSV of expected verdicts and prints a confusion matrix:

    assay_id  as_of  expect  source
    CHYTRID_..._Boyle_2004  2014-01-01  works  10.xxxx/yyy (Table 2)

`expect` is `works` (the literature found it detecting its target), `fails`
(false negatives or a redesign were reported) or `partial` (it covers some of
the diversity and not the rest). Statuses map on as: stable/watch -> works,
declining -> fails, low coverage -> partial, and insufficient data / no recent
data -> undecided, counted separately because an assay the tool declines to
judge is not the same as one it judges correctly — that distinction is what
calibrates min_records_for_drift.

A `partial` result against a `works` expectation is reported as `weaker`, not
as a disagreement: a pan-family assay detecting 71% of a genus is consistent
with a paper that used it successfully on the isolates it had.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch.accession import strip_version  # noqa: E402
from assaywatch.drift import assess  # noqa: E402
from assaywatch.lineage import (  # noqa: E402
    load_taxa_cache,
    name_lineages_from_taxonomy,
    sublineage_resolvers,
    title_assays,
)
from assaywatch.metadata import read_patent_accessions, read_titles  # noqa: E402
from assaywatch.report import apply_anchor_fdr, key_calls_by_accession, read_calls, read_dates  # noqa: E402
from assaywatch.score import load_config  # noqa: E402
from assaywatch.taxonomy import Taxonomy, taxonomy_from_config  # noqa: E402

# `low coverage` is its own outcome, not a failure: it says the assay is below
# threshold with no measurable fall, i.e. it never covered all of this diversity.
# That is compatible with a paper reporting successful use on the samples it had,
# so scoring it as "fails" turned four honest `works` cases into disagreements.
WORKS = {"stable", "watch"}
FAILS = {"declining"}
PARTIAL = {"low coverage"}
# Statuses the tool declines to judge. Anything not named above is undecided too, so a new
# status added to drift.py reads as "declined" until someone decides what it means, rather
# than being scored as one of the three outcomes by accident.
UNDECIDED = {"insufficient data", "no recent data", "no data"}


def precision_lines(rows: list[tuple[str, str, str, str]]) -> list[str]:
    """What the confusion matrix means for someone reading a flag. Rows are
    (expect, mechanism, status, verdict), one per case.

    The summary line above reports only cell counts, and every statement of this
    tool's performance until 2026-10-23 was sensitivity: "flags 5 of 11
    documented failures". Nobody had computed the other direction, which is the
    one a lab acting on a `declining` row needs: of the assays the tool calls
    declining, how many had actually failed? On the frozen 2026-10-22 table the
    answer was 2 of 9.

    Three further facts the headline hid are printed with it, because each changes
    how the headline reads:

    - which status earned each `fails` agreement. `classify` credits `low
      coverage` for a coverage-mechanism failure, defensibly, but then a "catch"
      may not be the drift flag at all (3 of the 5 were not);
    - how many `fails` cases are drift-mechanism at all (1 of 11), i.e. how much
      ground truth the drift flag actually has;
    - an interval on each proportion, because with ~7 independent failure events
      a one-case change is inside the noise and the number should look like it.

    Wilson, from `assaywatch.interval`, the estimator the report uses; it needs
    no scipy, which this script must not depend on for a summary.
    """
    from assaywatch.interval import wilson_interval

    def frac(k: int, n: int) -> str:
        if not n:
            return f"{k}/{n}"
        lo, hi = wilson_interval(k, n)
        return f"{k}/{n} = {k / n:.0%} (95% CI {lo:.0%}-{hi:.0%})"

    out = ["", "precision:"]
    dec = [r for r in rows if r[2] == "declining"]
    out.append(
        f"  declining calls that were documented failures (PPV): {frac(sum(r[0] == 'fails' for r in dec), len(dec))}"
    )
    fails = [r for r in rows if r[0] == "fails"]
    caught = [r for r in fails if r[3] == "agrees"]
    by_status = Counter(r[2] for r in caught)
    out.append(f"  documented failures caught: {frac(len(caught), len(fails))}")
    if caught:
        out.append("    credited to: " + ", ".join(f"{s} {n}" for s, n in by_status.most_common()))
        out.append(
            f"    caught by the drift flag itself (declining): {frac(by_status.get('declining', 0), len(fails))}"
        )
    mech = Counter((r[1] or "unrecorded") for r in fails)
    out.append("  failure cases by mechanism: " + ", ".join(f"{m} {n}" for m, n in sorted(mech.items())))
    works = [r for r in rows if r[0] == "works"]
    alarms = sum(1 for r in works if r[2] == "declining")
    out.append(f"  working assays called declining (false alarms): {frac(alarms, len(works))}")
    return out


def classify(status: str, expect: str, mechanism: str | None = None) -> tuple[str, str]:
    """(what the tool said, how that compares with the paper) for one case.

    `got` is `works`, `fails`, `partial` or `undecided`. The verdict is `undecided` when the
    tool declined to judge (that is not a disagreement, and counting it separately is what
    calibrates `min_records_for_drift`), `agrees` when it matches, `weaker` for a `works` /
    `partial` mismatch in EITHER direction (incomplete coverage is not a contradiction), and
    `DISAGREES` otherwise.

    `mechanism` is the case's: for a `fails` whose source documents a coverage gap
    (lineages the primers never matched), `low coverage` is the tool reporting that same gap
    and agrees. A drift-type `fails`, or one with no mechanism recorded, still needs `declining`.
    """
    got = (
        "works"
        if status in WORKS
        else "fails"
        if status in FAILS
        else "partial"
        if status in PARTIAL
        else "undecided"
    )
    if got == "undecided":
        return got, "undecided"
    if got == expect:
        return got, "agrees"
    if expect == "fails" and mechanism == "coverage" and got == "partial":
        return got, "agrees"
    if {got, expect} == {"works", "partial"}:
        return got, "weaker"
    return got, "DISAGREES"


@dataclass
class Evidence:
    """Everything a retrospective verdict reads, loaded once.

    The calls table is millions of rows and the metadata is every
    `*.meta.tsv.gz` under data/retrieved, and neither depends on the case being
    asked about. `--cases` used to reload and re-deduplicate both for each of the
    46 validation cases, so the dominant cost of a calibration run was parsing
    the same files 46 times. Held here instead, with the calls already
    deduplicated to the newest version of each accession and grouped by assay,
    so a case touches only its own assay's rows.
    """

    dates: dict[str, str]
    by_assay: dict[str, list[dict[str, Any]]]
    taxids: dict[str, int] | None = None
    taxa_cache: dict[int, str] | None = None
    resolvers: dict[str, list] | None = None  # sub-lineage chains, lineage.sublineage
    titles: dict[str, str] | None = None  # for the assays whose chain parses titles
    taxonomy: Taxonomy | None = None  # scope_taxids ancestry, drift.scope_taxonomy
    patent: set[str] | None = None  # patent-division accessions, drift.exclude_patent_records


def load_evidence(
    calls_path: Path, retrieved: Path, cfg: dict | None = None, query_taxids: dict[str, int] | None = None
) -> Evidence:
    """Read and deduplicate the calls table and the deposit dates, once.

    Deduplication is keyed on (assay, accession), so doing it before grouping by
    assay gives the same rows a per-assay pass would.

    When lineage config is present, also loads the taxid backfill sidecar and
    the taxa cache so per-lineage analysis runs during retrospective verdicts.
    """
    by_assay: dict[str, list[dict[str, Any]]] = defaultdict(list)
    rows = key_calls_by_accession(read_calls(calls_path))
    apply_anchor_fdr(rows, cfg or {})  # the report-time relabel report.build applies; off unless configured
    for r in rows:
        by_assay[r["assay_id"]].append(r)

    taxids: dict[str, int] | None = None
    taxa_cache: dict[int, str] | None = None
    if cfg:
        lcfg = cfg.get("lineage", {})
        taxa_cache_path = lcfg.get("taxa_cache")
        if taxa_cache_path:
            taxa_cache = load_taxa_cache(taxa_cache_path)
            taxids = {}
            sidecar_path = retrieved / ".meta.taxid.backfill.tsv.gz"
            if sidecar_path.exists():
                with gzip.open(sidecar_path, "rt") as f:
                    next(f, None)  # skip header
                    for line in f:
                        acc, _, tx = line.rstrip("\n").partition("\t")
                        if tx.isdigit():
                            taxids[strip_version(acc)] = int(tx)
            # Also read taxids from archive metadata (new-style with taxid column)
            for meta_path in sorted(retrieved.rglob("*.meta.tsv.gz")):
                with gzip.open(meta_path, "rt") as f:
                    hdr = (f.readline() or "").rstrip("\n").split("\t")
                    if "taxid" not in hdr or "accession" not in hdr:
                        continue
                    ai, ti = hdr.index("accession"), hdr.index("taxid")
                    for line in f:
                        parts = line.rstrip("\n").split("\t")
                        if len(parts) > max(ai, ti) and parts[ti].isdigit():
                            taxids[strip_version(parts[ai])] = int(parts[ti])
            if not taxids:
                taxids = None

    resolvers = titles = None
    if taxids is not None and cfg.get("lineage", {}).get("sublineage"):
        lcfg = cfg["lineage"]
        resolvers = sublineage_resolvers(lcfg, query_taxids or {})
        wanted = title_assays(lcfg)
        titles = read_titles(retrieved, {r["record_id"] for a in wanted for r in by_assay.get(a, [])})

    taxonomy = taxonomy_from_config(cfg) if cfg else None
    if taxa_cache is not None:
        taxa_cache = name_lineages_from_taxonomy(taxa_cache, taxonomy)
    patent = None
    if cfg and (cfg.get("drift") or {}).get("exclude_patent_records"):
        patent = read_patent_accessions(retrieved, {r["record_id"] for rs in by_assay.values() for r in rs})
    return Evidence(
        read_dates(retrieved), dict(by_assay), taxids, taxa_cache, resolvers, titles, taxonomy, patent
    )


def status_from_evidence(
    evidence: Evidence,
    cfg: dict,
    as_of: date,
    assays: set[str] | None = None,
    scope_map: dict[str, set[int]] | None = None,
):
    """{assay_id: AssayDrift} as the report would have computed it on `as_of`."""
    cutoff = as_of.isoformat()
    wanted = (
        evidence.by_assay
        if assays is None
        else {a: evidence.by_assay[a] for a in assays if a in evidence.by_assay}
    )
    rows = [r for rs in wanted.values() for r in rs if evidence.dates.get(r["record_id"], "9999") < cutoff]
    return assess(
        rows,
        evidence.dates,
        cfg,
        today=as_of,
        taxids=evidence.taxids,
        taxa_cache=evidence.taxa_cache,
        scope_map=scope_map,
        resolvers=evidence.resolvers,
        titles=evidence.titles,
        taxonomy=evidence.taxonomy,
        patent=evidence.patent,
    ), len(rows)


def status_as_of(
    calls_path: Path,
    retrieved: Path,
    cfg: dict,
    as_of: date,
    assays: set[str] | None = None,
    scope_map: dict[str, set[int]] | None = None,
    query_taxids: dict[str, int] | None = None,
):
    """{assay_id: AssayDrift} as the report would have computed it on `as_of`.

    Loads the evidence each call, so it is right for one question. Anything
    asking several should call `load_evidence` once and `status_from_evidence`
    per question, which is what `--cases` does.
    """
    return status_from_evidence(
        load_evidence(calls_path, retrieved, cfg, query_taxids), cfg, as_of, assays, scope_map
    )


def _query_taxids(registry: Path) -> dict[str, int]:
    """assay_id -> target.taxid, which a `subtaxid` resolver defers at."""
    from assaywatch.validate import iter_files, load_assay

    return {a.id: a.target.taxid for a in map(load_assay, iter_files(registry))}


def _build_scope_map(registry: Path) -> dict[str, set[int]] | None:
    """Build assay_id → set of in-scope taxids from registry YAMLs, same as report.py."""
    from assaywatch.validate import iter_files, load_assay

    scope_map: dict[str, set[int]] | None = None
    for path in iter_files(registry):
        a = load_assay(path)
        if a.target.scope_taxids:
            if scope_map is None:
                scope_map = {}
            scope_map[a.id] = set(a.target.scope_taxids)
    return scope_map


def rename_map(path: Path) -> tuple[dict[str, str], set[str]]:
    """({old id: new id} for RENAME, {old id} for REMOVE) from docs/rename-mapping.tsv."""
    renamed: dict[str, str] = {}
    removed: set[str] = set()
    if not path.exists():
        return renamed, removed
    with path.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row["action"] == "RENAME" and row["new_id"]:
                renamed[row["old_id"]] = row["new_id"]
            elif row["action"] == "REMOVE":
                removed.add(row["old_id"])
    return renamed, removed


def id_aliases(renamed: dict[str, str]) -> dict[str, set[str]]:
    """Every assay id mapped to the ids that may stand for the same assay.

    Both directions on purpose. A case in docs/validation-cases.tsv may name
    either the old id or the new one, and a calls table may hold either
    depending on whether it predates the rename, so neither side can be assumed
    canonical.
    """
    out: dict[str, set[str]] = {}
    for old, new in renamed.items():
        for k in (old, new):
            out.setdefault(k, set()).update({old, new})
    return out


def resolve_assay_id(
    assay_id: str, present: set[str], aliases: dict[str, set[str]], removed: set[str]
) -> tuple[str | None, str | None]:
    """(the id this assay's rows are under in the calls table, why that differs).

    A case whose id matches nothing used to read `no data` and be counted as
    "the tool declined to judge", which is indistinguishable from an assay that
    genuinely has no records. On the 2026-10-17 calls that silently swallowed 13
    of the 49 cases, 4 of them `fails` cases, because the assay-ID renames had
    landed in the registry and in docs/validation-cases.tsv but not in that
    archive. Every tier-2 figure measured on it was wrong as a result.
    """
    if assay_id in present:
        return assay_id, None
    for alt in sorted(aliases.get(assay_id, set()) - {assay_id}):
        if alt in present:
            return alt, f"renamed; rows are under {alt}"
    if assay_id in removed or any(a in removed for a in aliases.get(assay_id, set())):
        return None, "removed from the registry"
    return None, "absent from the calls table"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--calls", type=Path, default=None, help="calls.tsv.gz (default: the newest run)")
    ap.add_argument("--retrieved", type=Path, default=ROOT / "data" / "retrieved")
    ap.add_argument("--registry", type=Path, default=ROOT / "registry", help="registry dir for scope_taxids")
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--as-of", type=date.fromisoformat, default=None)
    ap.add_argument("--assay", action="append", help="limit to these assay ids; repeatable")
    ap.add_argument("--cases", type=Path, default=None, help="TSV of expected verdicts")
    ap.add_argument(
        "--renames",
        type=Path,
        default=ROOT / "docs" / "rename-mapping.tsv",
        help="assay-ID rename mapping, so a case still matches a calls table from before a rename",
    )
    args = ap.parse_args(argv)

    calls = args.calls
    if calls is None:
        runs = sorted(p for p in (ROOT / "results").glob("*/calls.tsv.gz"))
        if not runs:
            raise SystemExit("no calls.tsv.gz under results/; run the pipeline first")
        calls = runs[-1]
    cfg = load_config(args.config)
    scope_map = _build_scope_map(args.registry) if args.registry.is_dir() else None
    query_taxids = _query_taxids(args.registry) if args.registry.is_dir() else None

    if not args.cases:
        if not args.as_of:
            ap.error("give --as-of, or --cases")
        drifts, n = status_as_of(
            calls,
            args.retrieved,
            cfg,
            args.as_of,
            set(args.assay) if args.assay else None,
            scope_map=scope_map,
            query_taxids=query_taxids,
        )  # one question, so one load
        print(f"{calls}, as of {args.as_of} ({n} records deposited before then)\n")
        for aid, a in sorted(drifts.items()):
            frac = "-" if a.recent_fraction is None else f"{a.recent_fraction:.1%}"
            print(f"{a.status:<18} {frac:>7} of {a.recent_evaluable:<6} recent  {aid}")
            print(f"{'':18} {a.note}")
        return 0

    # Comment lines carry each case's provenance; strip them before the header is read.
    body = [ln for ln in args.cases.read_text().splitlines() if ln.strip() and not ln.startswith("#")]
    cases = list(csv.DictReader(body, delimiter="\t"))
    evidence = load_evidence(calls, args.retrieved, cfg, query_taxids)  # once, not once per case

    # Resolve every case id BEFORE scoring any of them, and refuse to report a
    # confusion matrix that silently omits cases. An id matching nothing is a
    # bookkeeping fault, not evidence about an assay, so it must not reach the
    # tally as `undecided`.
    present = set(evidence.by_assay)
    renamed, removed = rename_map(args.renames)
    aliases = id_aliases(renamed)
    resolved: dict[int, tuple[str | None, str | None]] = {}
    absent: list[str] = []
    for i, c in enumerate(cases):
        rid, why = resolve_assay_id(c["assay_id"], present, aliases, removed)
        resolved[i] = (rid, why)
        if rid is None and why == "absent from the calls table":
            absent.append(c["assay_id"])
    if absent:
        raise SystemExit(
            f"{len(absent)} validation case(s) name an assay with no rows in {calls} and no "
            "rename that reaches one:\n  "
            + "\n  ".join(sorted(set(absent)))
            + "\nFix the id in the cases file, add it to docs/rename-mapping.tsv, or screen "
            "the assay. Scoring these as `no data` would hide them inside the undecided count."
        )
    bridged = {
        c["assay_id"]: resolved[i][0] for i, c in enumerate(cases) if resolved[i][1] and resolved[i][0]
    }
    if bridged:
        print(
            f"{len(bridged)} case(s) matched through docs/rename-mapping.tsv, so {calls} predates a rename:",
            file=sys.stderr,
        )
        for aid, rid in sorted(bridged.items()):
            print(f"  {aid} -> {rid}", file=sys.stderr)

    tally: Counter = Counter()
    scored: list[tuple[str, str, str, str]] = []
    print(f"{'assay':<52} {'as of':<11} {'expect':<7} {'status':<18} verdict")
    for i, c in enumerate(cases):
        as_of = date.fromisoformat(c["as_of"])
        rid, why = resolved[i]
        if rid is None:  # removed from the registry: not judgeable, and not `undecided`
            tally[(c["expect"], "removed")] += 1
            print(f"{c['assay_id'][:52]:<52} {c['as_of']:<11} {c['expect']:<7} {'-':<18} removed")
            continue
        drifts, _ = status_from_evidence(evidence, cfg, as_of, {rid}, scope_map=scope_map)
        a = drifts.get(rid)
        status = a.status if a else "no data"
        _, verdict = classify(status, c["expect"], c.get("mechanism") or None)
        tally[(c["expect"], verdict)] += 1
        scored.append((c["expect"], c.get("mechanism") or "", status, verdict))
        print(f"{c['assay_id'][:52]:<52} {c['as_of']:<11} {c['expect']:<7} {status:<18} {verdict}")
    print("\nsummary:", ", ".join(f"{e}/{v}: {n}" for (e, v), n in sorted(tally.items())))
    print("\n".join(precision_lines(scored)))
    undecided = sum(n for (_, v), n in tally.items() if v == "undecided")
    if undecided:
        print(f"{undecided} case(s) the tool declined to judge (insufficient data): that is what calibrating")
        print("min_records_for_drift against recent_window_months is for.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
