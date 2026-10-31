#!/usr/bin/env python3
"""Does a retrospective candidate paper test the assay the registry holds?

    python scripts/check_candidate_identity.py --pmcid PMC12421836 --assay ENTEROVIRUS_ssRNA_VP3_VP1
    python scripts/check_candidate_identity.py --doi 10.3390/v15061344 --assay INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003
    python scripts/check_candidate_identity.py --queue docs/2026-10-26-retrospective-candidates.tsv --groups mismatch,redesign --tsv results/retro-identity.tsv

Why this exists
---------------
`scripts/find_retrospective_cases.py` searches the citation graph and writes a
reading queue of papers that cite a registry design DOI and use failure language.
It finds the right PAPERS. It cannot say whether the assay a citing paper actually
tested is the assay the registry holds, and `docs/RESUME-HERE.md` (2026-10-26)
records that this - identity, not discovery - is the bottleneck: three of the
first four hand reads died there. A citing paper names an assay by citation and
rarely reprints its oligos, so the only thing that settles identity every time is
the paper's own primer table.

So this is the cheap identity check the resume point asks for. It does one thing:
take a candidate (an assay id plus the citing paper's DOI or PMC id), get that
paper's open-access full text WITH its tables, and compare the registry assay's
stored oligos against what the paper prints. It reuses the machinery that already
exists - `verify_oligos_against_paper.check` for the per-oligo comparison (which
tries both strands, undoes codon spacing and reports the nearest printed run by
edit distance) and `fetch_europepmc_fulltext` for the text (its flatten keeps
`<table-wrap>`, which is the whole point, because the primer table is what is
being looked for).

Verdict, per assay
------------------
CONFIRMED       both primers are printed in the paper verbatim (exact or as the
                reverse complement). The paper tested this assay. If a probe is
                printed it must agree too.
VARIANT         a primer is printed but DIFFERS by one or more fixed bases - the
                paper tested a recognisably different form (the Influenza Matrix
                reverse is a redesign of Spackman's, and a paper reprinting
                Spackman's original lands here). The row is NOT ours; drop it.
UNCONFIRMABLE   the text cannot decide it: not open access, or the paper prints no
                oligo table (it cites the assay without reprinting it), or a primer
                is simply absent from a table that prints others. The `reason`
                column says which, so a reader can route it (fetch the PDF, read a
                supplement, or let it go).

The split between VARIANT and CONFIRMED is the load-bearing one: a near-miss is
NEVER read as a confirmation, because collapsing the two is exactly the error that
would let the dead candidates through.

What it does NOT do
-------------------
It writes a worksheet TSV and nothing else. No row is added to `registry/`,
`pending/` or `docs/validation-cases.tsv` - asserting identity and promoting a
case are maintainer acts, the same rule `find_retrospective_cases.py` keeps. A row
here is an instruction to go and read the named paper.
"""

from __future__ import annotations

import argparse
import csv
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

import fetch_europepmc_fulltext as epmc  # noqa: E402
import verify_oligos_against_paper as verify  # noqa: E402

from assaywatch.validate import load_assay  # noqa: E402

# Per-oligo categories, derived from a `verify.check` verdict. These exist so the
# assay-level rule below reads over meaning, not over verify's verdict strings.
PRESENT_EXACT = "present_exact"  # exact | revcomp - the paper lists this oligo verbatim
PRESENT_VARIANT = "present_variant"  # near:N, N>=1 - printed but a fixed-base difference
WEAK = "weak"  # in-text - occurs in the paper but not as a listed oligo
NOT_FOUND = "not_found"  # absent - the paper prints oligos and this is not among them


def classify_oligo(verdict: str) -> str:
    """One `verify.check` verdict -> a per-oligo identity category.

    `exact`/`revcomp` are the only verdicts that confirm; `near:N` is always a
    variant and never a confirmation, which is the one distinction this whole
    instrument turns on.
    """
    if verdict in ("exact", "revcomp"):
        return PRESENT_EXACT
    if verdict.startswith("near:"):
        return PRESENT_VARIANT
    if verdict == "in-text":
        return WEAK
    return NOT_FOUND  # "absent", or anything unexpected, is treated as not found


def assay_identity(oligo_results: list[dict], printed_count: int) -> tuple[str, str]:
    """(verdict, reason) for one assay against one paper.

    `oligo_results` is one dict per oligo with keys `slot` and `category`.
    `printed_count` is how many oligo-like runs the paper yielded, so "the table
    is missing" can be told from "the table is here and our oligos are not in it".
    """
    primers = [r for r in oligo_results if r["slot"] in ("forward", "reverse")]
    cats = {r["category"] for r in oligo_results}

    if not primers:
        return "UNCONFIRMABLE", "assay declares no forward/reverse primer to check"

    # A paper that lost its oligo table (an image, or XML without <table-wrap>)
    # says nothing about any sequence. Below the methods-paper floor, and with
    # nothing found anywhere in the running text either, there is no evidence.
    if printed_count < verify.MIN_PRINTED_FOR_ABSENT and WEAK not in cats and PRESENT_EXACT not in cats:
        return (
            "UNCONFIRMABLE",
            f"paper prints no oligo table ({printed_count} oligo-like runs); cites the assay only",
        )

    # A fixed-base difference on any primer means the paper's assay is not ours.
    if any(r["category"] == PRESENT_VARIANT for r in primers):
        return "VARIANT", "a printed primer differs by one or more fixed bases - not this registry assay"

    if all(r["category"] == PRESENT_EXACT for r in primers):
        # Both primers verbatim. A probe, if the assay has one, must not contradict.
        probe = [r for r in oligo_results if r["slot"] == "probe"]
        if probe and any(r["category"] in (PRESENT_VARIANT, NOT_FOUND) for r in probe):
            return "VARIANT", "both primers match but the probe differs or is absent"
        return "CONFIRMED", "both primers printed verbatim in the paper"

    # Some primer is only in-text or absent: the table (if any) does not reprint
    # the pair, so identity cannot be settled from the text in hand.
    absent = [r["slot"] for r in primers if r["category"] == NOT_FOUND]
    if absent and printed_count >= verify.MIN_PRINTED_FOR_ABSENT:
        return (
            "UNCONFIRMABLE",
            f"paper prints {printed_count} oligos but not its {', '.join(absent)} - likely a different assay, read the primer table",
        )
    return "UNCONFIRMABLE", "a primer occurs only in running text, not a listed oligo - check by eye"


def paper_text(doi: str | None, pmcid: str | None, papers_dir: Path) -> tuple[str | None, str]:
    """(normalised text, source) for a candidate paper, or (None, reason).

    A local PDF/XML/TXT in `papers/` wins (it is better evidence than a text
    rendering and needs no network). Otherwise Europe PMC's open-access full text,
    flattened with its tables kept. Both routes return text already run through
    `verify.normalise_notation`, so a comparison downstream is apples to apples.
    """
    if doi:
        name = epmc.held(papers_dir, doi) if papers_dir.is_dir() else None
        if name:
            return verify.file_text(papers_dir / name), f"local:{name}"

    pmcid = pmcid or (epmc.pmcid_for(doi) if doi else None)
    if not pmcid:
        return None, "no open-access PMC copy (fetch the PDF into papers/ and re-run)"
    try:
        xml = epmc.get(epmc.FULLTEXT.format(pmcid=pmcid), timeout=120)
    except Exception as exc:  # noqa: BLE001 - one paper's fetch must not end the run
        return None, f"fetch failed for {pmcid}: {exc}"
    text = verify.normalise_notation(epmc.flatten(xml))
    if len(text) < 6000:
        # An abstract-only deposit cannot confirm or deny a primer (the floor
        # fetch_europepmc_fulltext uses for the same reason).
        return None, f"only an abstract-length deposit in PMC ({len(text)} chars); needs the full PDF"
    return text, f"epmc:{pmcid}"


def check_assay(assay_id: str, text: str, registry: Path, cap: int) -> dict:
    """Compare one registry assay's oligos against one paper's text.

    Returns a dict with the assay-level verdict and a list of per-oligo rows,
    mirroring exactly the comparison `verify_oligos_against_paper` does for an
    entry's own design paper.
    """
    assay = load_assay(registry / f"{assay_id}.yaml")
    printed = verify.printed_oligos(text)
    oligo_rows = []
    for slot, o in verify.oligos_of(assay):
        seq = (o.seq_as_written or o.seq).replace("I", "N").upper()
        runs = verify.printed_runs_for(verify.is_probe_slot(slot, o), seq, text, printed)
        verdict, note = verify.check(seq, text, runs, cap)
        oligo_rows.append(
            {
                "slot": slot,
                "oligo_name": getattr(o, "name", "") or "",
                "stored_seq": seq,
                "check_verdict": verdict,
                "category": classify_oligo(verdict),
                "note": note,
            }
        )
    identity, reason = assay_identity(oligo_rows, len(printed))
    return {
        "assay_id": assay_id,
        "identity": identity,
        "reason": reason,
        "paper_oligos": len(printed),
        "oligos": oligo_rows,
    }


# One output row per (candidate, assay, oligo): the oligo detail is where the
# evidence is, and the assay verdict/reason repeat on each of its oligo rows so
# the TSV can be filtered on either without a join.
COLS = [
    "citing_doi",
    "assay_id",
    "identity",
    "reason",
    "slot",
    "oligo_name",
    "check_verdict",
    "stored_seq",
    "paper_oligos",
    "note",
    "read_from",
    "groups",
    "title",
]


def iter_queue(path: Path, groups: set[str] | None):
    """Yield candidate rows from a find_retrospective_cases.py TSV.

    Comment lines (the generated header) start with '#'. Each row's `assays`
    column may hold several ids joined by ';' (a nested assay's rounds).
    """
    with path.open() as fh:
        rows = csv.DictReader((ln for ln in fh if not ln.startswith("#")), delimiter="\t")
        for row in rows:
            if groups and row.get("groups", "") not in groups:
                continue
            yield row


def candidates_from_args(args) -> list[dict]:
    """Normalise CLI input to a list of {assays, citing_doi, pmcid, groups, title}."""
    if args.queue:
        out = []
        for row in iter_queue(args.queue, set(args.groups.split(",")) if args.groups else None):
            out.append(
                {
                    "assays": row.get("assays", ""),
                    "citing_doi": row.get("citing_doi", ""),
                    "pmcid": row.get("pmcid", "") or None,
                    "groups": row.get("groups", ""),
                    "title": row.get("title", ""),
                }
            )
            if args.limit and len(out) >= args.limit:
                break
        return out
    return [
        {
            "assays": ";".join(args.assay or []),
            "citing_doi": args.doi or "",
            "pmcid": args.pmcid,
            "groups": "",
            "title": "",
        }
    ]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument(
        "--papers",
        type=Path,
        default=ROOT / "papers",
        help="folder of local PDFs/XML/TXT, preferred over the network",
    )
    ap.add_argument("--queue", type=Path, help="a find_retrospective_cases.py candidates TSV")
    ap.add_argument("--groups", help="only these queue groups, comma-separated (e.g. mismatch,redesign)")
    ap.add_argument("--doi", help="a single citing paper's DOI")
    ap.add_argument("--pmcid", help="a single citing paper's PMC id, if already known")
    ap.add_argument("--assay", action="append", help="registry assay id(s) to check; repeatable")
    ap.add_argument("--cap", type=int, default=4, help="largest edit distance worth reporting as near:N")
    ap.add_argument("--limit", type=int, help="stop after this many queue rows, for a quick look")
    ap.add_argument("--tsv", type=Path, help="write the worksheet here (default: stdout summary only)")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)

    candidates = candidates_from_args(args)
    if not candidates or not any(c["assays"] for c in candidates):
        ap.error("give --queue, or --doi/--pmcid with --assay")

    rows: list[dict] = []
    summary: list[tuple[str, str, str, str]] = []  # (doi, assay, identity, reason)
    fetched = 0
    for c in candidates:
        assay_ids = [a for a in c["assays"].split(";") if a]
        text, src = paper_text(c["citing_doi"] or None, c["pmcid"], args.papers)
        if src.startswith(("epmc:", "fetch")):
            fetched += 1
            time.sleep(0.4)  # courteous to Europe PMC when a queue is walked
        if text is None:
            for aid in assay_ids:
                summary.append((c["citing_doi"], aid, "UNCONFIRMABLE", src))
                rows.append(
                    {
                        "citing_doi": c["citing_doi"],
                        "assay_id": aid,
                        "identity": "UNCONFIRMABLE",
                        "reason": src,
                        "slot": "",
                        "oligo_name": "",
                        "check_verdict": "",
                        "stored_seq": "",
                        "paper_oligos": 0,
                        "note": "",
                        "read_from": src,
                        "groups": c["groups"],
                        "title": c["title"],
                    }
                )
            if args.verbose:
                print(f"  {c['citing_doi']:40s} UNCONFIRMABLE  {src}")
            continue

        for aid in assay_ids:
            res = check_assay(aid, text, args.registry, args.cap)
            summary.append((c["citing_doi"], aid, res["identity"], res["reason"]))
            if args.verbose:
                print(
                    f"  {c['citing_doi']:40s} {aid:52s} {res['identity']}  ({res['paper_oligos']} paper oligos)"
                )
            for og in res["oligos"]:
                rows.append(
                    {
                        "citing_doi": c["citing_doi"],
                        "assay_id": aid,
                        "identity": res["identity"],
                        "reason": res["reason"],
                        "slot": og["slot"],
                        "oligo_name": og["oligo_name"],
                        "check_verdict": og["check_verdict"],
                        "stored_seq": og["stored_seq"],
                        "paper_oligos": res["paper_oligos"],
                        "note": og["note"],
                        "read_from": src,
                        "groups": c["groups"],
                        "title": c["title"],
                    }
                )

    if args.tsv:
        args.tsv.parent.mkdir(parents=True, exist_ok=True)
        with args.tsv.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=COLS, delimiter="\t", extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
        print(f"wrote {len(rows)} oligo rows for {len(summary)} (paper, assay) pairs to {args.tsv}")

    counts: dict[str, int] = {}
    for _doi, _aid, verdict, _reason in summary:
        counts[verdict] = counts.get(verdict, 0) + 1
    print(
        f"\n{len(summary)} (paper, assay) pairs over {len(candidates)} papers, {fetched} fetched from Europe PMC"
    )
    for verdict in ("CONFIRMED", "VARIANT", "UNCONFIRMABLE"):
        if counts.get(verdict):
            print(f"  {verdict:14s} {counts[verdict]}")
    conf = [(d, a) for d, a, v, _ in summary if v == "CONFIRMED"]
    var = [(d, a) for d, a, v, _ in summary if v == "VARIANT"]
    if conf:
        print("\n  CONFIRMED - read the paper's reported result and decide works vs fails:")
        for d, a in conf:
            print(f"    {d}  {a}")
    if var:
        print("\n  VARIANT - the assay tested is not ours; drop the row:")
        for d, a in var:
            print(f"    {d}  {a}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
