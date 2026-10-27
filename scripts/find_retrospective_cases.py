#!/usr/bin/env python3
"""Find papers that report how a registry assay PERFORMED. Proposes, never adds.

    python scripts/find_retrospective_cases.py --out results/retro-candidates-2026-10-26.tsv

A tier-2 retrospective case needs a paper reporting how an assay ALREADY IN THE
REGISTRY actually performed — not a paper publishing a new assay, and not an assay's
own design-and-validation paper, which `docs/validation-cases.tsv` excludes by rule.

WHY THIS INSTRUMENT AND NOT THE OLD ONE. The 2026-10-24 sweep searched Europe PMC for
papers that PRINT a registry oligo, and `docs/RESUME-HERE.md` records that seam as
spent: "every searchable registry oligo has been tried", and the degenerate ones cannot
be searched literally at all. That instrument could only ever find papers that reprint a
sequence, which is a small and biased subset — a group that uses someone else's
published assay usually cites it and does not retype its primers.

So this searches the CITATION GRAPH instead. Europe PMC's `CITES:` field asks "which
papers cite this one", and ANDing it with failure language asks the question a
retrospective case is made of: did anyone who used this assay report it missing things?
On the Li 2010 mpox paper that takes 429 citing papers down to 7 candidates.

WHAT IT IS LOOKING FOR, in priority order. The registry's shortfall is specific: the
development set holds ONE `fails` + `drift` row against a target of five, and the
held-out set added none and is now spent. `works` cases are plentiful and cheap; a
documented FAILURE is what is scarce. So the phrase groups below are failure-weighted,
and each hit records which group matched, because the group predicts what kind of case
it could become.

WHAT IT DELIBERATELY DOES NOT DO. It writes a reading queue and nothing else. No row is
added to any case file, because a case asserts what a paper REPORTED and that cannot be
read off an abstract: the as-of date has to be the paper's own, the expectation has to be
what its results section says rather than what its abstract advertises, and the assay has
to be the one the registry holds rather than a modified version of it. Every one of those
has gone wrong in this project before. A row here is a reading assignment.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from assaywatch.validate import iter_files, load_assay

REPO = Path(__file__).resolve().parents[1]
BASE = "https://www.ebi.ac.uk/europepmc/webservices/rest"

# Phrase groups, failure-weighted. Each is a list of exact phrases searched in the
# abstract; the group name is recorded per hit so the queue says what to expect.
#
# `miss` and `mismatch` are the ones that could yield a `fails` row, which is the
# scarce kind. `redesign` is indirect but strong: a group that publishes a modified
# version of an assay usually says why the original was not enough. `works` is included
# at low weight because the matrix needs negatives too - an assay the literature says
# still works is a real case and the development set has 32 of them.
GROUPS: dict[str, list[str]] = {
    "miss": [
        "failed to detect",
        "failed to amplify",
        "false negative",
        "false-negative",
        "false negatives",
        "went undetected",
        "escape detection",
        "missed by",
        "detection failure",
        "assay failure",
    ],
    "mismatch": [
        "primer mismatch",
        "primer mismatches",
        "probe mismatch",
        "probe mismatches",
        "mismatches in the primer",
        "mismatch in the primer",
        "mismatches in the probe",
        "mismatch in the probe",
    ],
    "weakened": [
        "reduced sensitivity",
        "decreased sensitivity",
        "loss of sensitivity",
        "underestimated",
        "underestimate the",
    ],
    "redesign": [
        "modified primer",
        "redesigned primer",
        "updated primer",
        "revised assay",
        "new primer set",
    ],
}

# WHY THE API FILTER IS NOT THE FILTER, measured 2026-10-26. Europe PMC's
# `ABSTRACT:"..."` does NOT enforce adjacency: on one design paper it took 131 citing
# papers to 58, and none of the first three returned abstracts contained any phrase at
# all - it had matched the words separately. That is lossy in the SAFE direction, since
# an exact phrase match is also a loose match, so the query is kept as a cheap way to
# avoid downloading every citation. But the decision is made locally, on the abstract
# text, by exact substring. A row whose abstract does not contain a phrase is dropped,
# not recorded as "unconfirmed": a queue padded with 154 unconfirmed rows out of 161 is
# not a queue, it is the citation list again.
#
# The phrases are failure-weighted on purpose. `works` cases are plentiful - the
# development set has 32 - and what is scarce is a documented FAILURE: one `fails`+`drift`
# row against a target of five, and the held-out set is spent.


def get(url: str, params: dict[str, str], tries: int = 3) -> dict:
    q = urllib.parse.urlencode(params)
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(f"{url}?{q}", timeout=40) as fh:
                return json.loads(fh.read().decode())
        except Exception as exc:  # noqa: BLE001 - a transient API is not a reason to lose the run
            if attempt == tries - 1:
                print(f"    give up: {exc}", file=sys.stderr)
                return {}
            time.sleep(2 * (attempt + 1))
    return {}


def resolve(doi: str) -> dict | None:
    """A DOI -> its Europe PMC id, source and citation count."""
    d = get(
        f"{BASE}/search", {"query": f'DOI:"{doi}"', "format": "json", "resultType": "core", "pageSize": "1"}
    )
    hits = (d.get("resultList") or {}).get("result") or []
    return hits[0] if hits else None


def citing_with_phrases(source: str, pmid: str, phrases: list[str], page: int = 100) -> list[dict]:
    """Every paper citing `pmid` that the API's loose filter admits, fully paginated.

    Paginated with `cursorMark`, because a design paper with 400 citations can leave
    tens of candidates after the loose filter and a single page would silently truncate
    the queue - the failure mode that would make this instrument look cleaner than it is.
    """
    clause = " OR ".join(f'ABSTRACT:"{p}"' for p in phrases)
    query = f"CITES:{pmid}_{source} AND ({clause})"
    out: list[dict] = []
    cursor = "*"
    for _ in range(20):  # 2,000 candidates for one design paper would be a different problem
        d = get(
            f"{BASE}/search",
            {
                "query": query,
                "format": "json",
                "resultType": "core",
                "pageSize": str(page),
                "cursorMark": cursor,
            },
        )
        hits = (d.get("resultList") or {}).get("result") or []
        out += hits
        nxt = d.get("nextCursorMark")
        if not hits or not nxt or nxt == cursor:
            break
        cursor = nxt
    return out


def matched_groups(abstract: str) -> list[str]:
    low = (abstract or "").lower()
    return [g for g, ps in GROUPS.items() if any(p in low for p in ps)]


def matched_phrases(abstract: str) -> list[str]:
    low = (abstract or "").lower()
    return [p for ps in GROUPS.values() for p in ps if p in low]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--registry", type=Path, default=REPO / "registry")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--delay", type=float, default=0.34, help="seconds between API calls")
    ap.add_argument(
        "--limit", type=int, default=None, help="only the first N design papers (for a smoke test)"
    )
    args = ap.parse_args(argv)

    # One design paper can back several entries (nested rounds, renamed siblings), so
    # the search is per DOI and the result is mapped back to every assay that cites it.
    by_doi: dict[str, list[str]] = {}
    for path in iter_files(args.registry):
        a = load_assay(path)
        doi = (a.citation.doi or "").strip()
        if doi and a.citation.doi_verified:
            by_doi.setdefault(doi, []).append(a.id)
    dois = sorted(by_doi)
    if args.limit:
        dois = dois[: args.limit]
    all_phrases = [p for ps in GROUPS.values() for p in ps]
    print(f"{len(by_doi)} verified design DOIs behind {sum(len(v) for v in by_doi.values())} entries")
    print(f"searching {len(dois)} of them, {len(all_phrases)} phrases in {len(GROUPS)} groups\n")

    rows: list[dict] = []
    unresolved: list[str] = []
    for n, doi in enumerate(dois, 1):
        assays = sorted(by_doi[doi])
        meta = resolve(doi)
        time.sleep(args.delay)
        if not meta or not meta.get("pmid"):
            unresolved.append(doi)
            print(f"[{n}/{len(dois)}] {doi}: not in Europe PMC", flush=True)
            continue
        cited_by = meta.get("citedByCount") or 0
        hits = citing_with_phrases(meta.get("source", "MED"), meta["pmid"], all_phrases)
        time.sleep(args.delay)
        kept = 0
        for h in hits:
            # The design paper citing itself, or a self-citation of the same record.
            if h.get("doi") == doi:
                continue
            groups = matched_groups(h.get("abstractText") or "")
            if not groups:
                # The API's loose match, not a real one. Dropped rather than recorded:
                # see the note above GROUPS.
                continue
            rows.append(
                {
                    "assays": ";".join(assays),
                    "design_doi": doi,
                    "design_cited_by": cited_by,
                    "citing_pmid": h.get("pmid") or h.get("id") or "",
                    "citing_doi": h.get("doi") or "",
                    "year": h.get("pubYear") or "",
                    "open_access": h.get("isOpenAccess") or "",
                    "pmcid": h.get("pmcid") or "",
                    "groups": ",".join(sorted(groups)),
                    "phrases": "; ".join(matched_phrases(h.get("abstractText") or "")),
                    "journal": h.get("journalTitle") or h.get("journalAbbreviation") or "",
                    "title": (h.get("title") or "").replace("\t", " ").strip(),
                }
            )
            kept += 1
        print(f"[{n}/{len(dois)}] {doi}: cited by {cited_by}, {kept} candidate(s)", flush=True)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0]) if rows else ["assays", "design_doi", "citing_doi", "year", "groups", "title"]
    with args.out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        for r in sorted(rows, key=lambda r: (r["groups"] == "works", -int(r["year"] or 0))):
            w.writerow(r)

    print(f"\n{len(rows)} candidate rows -> {args.out}")
    print(f"{len(unresolved)} design DOIs are not in Europe PMC and cannot be searched this way")
    counts: dict[str, int] = {}
    for r in rows:
        for g in r["groups"].split(","):
            counts[g] = counts.get(g, 0) + 1
    print("by group:", dict(sorted(counts.items(), key=lambda x: -x[1])))
    print("\nNOTHING HAS BEEN ADDED TO ANY CASE FILE. Each row is a reading assignment:")
    print("  the as-of date must be the paper's own, the expectation must come from its")
    print("  results rather than its abstract, and the assay must be the one the registry")
    print("  holds rather than a modified version of it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
