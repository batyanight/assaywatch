#!/usr/bin/env python3
"""Find recently published primer assays for the registry's targets. Proposes, never adds.

    python scripts/scan_literature.py --since 2024 --out results/candidates.tsv
    python scripts/scan_literature.py --taxon "Ophidiomyces ophidiicola" --since 2020

The registry's gaps are mostly things published after the source spreadsheet was
compiled, so the question "what assays exist now that we do not have" has to be
asked against the literature rather than against our own data. This searches
Europe PMC for papers that look like they publish a PCR assay for a taxon the
registry already tracks, and writes a review queue: one row per candidate, with
the DOI, whether the full text is open, and whether primer-like sequences are
actually readable in it.

It deliberately stops there. Nothing is written to registry/, because every
transcription error this project has hit came from copying a sequence out of a
secondary source: the way in is `scripts/check_submission.py`, which screens a
candidate's oligos against real records before anyone trusts them. A row in the
queue is a reading assignment, not a result.

Europe PMC is used rather than PubMed because its REST interface returns both
the open-access full text (`/{PMCID}/fullTextXML`) and a machine-readable
`received` date, which is what a retrospective validation case needs — a case
must only see sequences that existed before the paper's authors did.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch.validate import iter_files, load_assay  # noqa: E402

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"
# Terms that mark a paper as likely to contain a usable assay. Kept broad on
# purpose: a false positive costs a glance at a title, a false negative costs an
# assay the registry never learns about.
# Two filters, because one is not enough. The first tried here was just
# "taxon AND (primer OR qPCR ...)", which matched any paper mentioning PCR in
# its methods: of twenty hits for two fungal taxa, nineteen were immunology,
# metagenomics or reviews and one had readable oligos. Requiring assay language
# in the TITLE or ABSTRACT is what separates a paper that publishes an assay
# from one that merely used somebody else's.
ASSAY_TERMS = '(primer* OR "real-time PCR" OR qPCR OR "RT-PCR" OR TaqMan OR amplicon)'
DEVELOPMENT_TERMS = (
    '(TITLE:"detection" OR TITLE:"assay" OR TITLE:"primers" OR TITLE:"qPCR" OR TITLE:"PCR" '
    'OR TITLE:"diagnostic" OR TITLE:"validation" OR TITLE:"surveillance" '
    'OR ABSTRACT:"we developed" OR ABSTRACT:"newly designed primers" OR ABSTRACT:"primer set")'
)
# A run of IUPAC letters this long in running text is almost always an oligo.
OLIGO_RE = re.compile(r"\b[ACGTRYSWKMBDHVNI]{17,45}\b")


def search(query: str, page_size: int = 25) -> list[dict]:
    """One Europe PMC search, newest first. Returns [] rather than raising on a bad query."""
    import requests

    try:
        r = requests.get(
            f"{EPMC}/search",
            params={
                "query": query,
                "format": "json",
                "pageSize": page_size,
                "sort": "P_PDATE_D desc",
                "resultType": "lite",
            },
            timeout=60,
        )
        r.raise_for_status()
        return r.json().get("resultList", {}).get("result", [])
    except Exception as e:  # noqa: BLE001 - one failed search must not end the scan
        print(f"  search failed ({type(e).__name__}): {query[:70]}", file=sys.stderr)
        return []


def full_text_signals(pmcid: str) -> tuple[str, int]:
    """(received date or '', count of distinct oligo-like sequences) from the open full text."""
    import requests

    try:
        r = requests.get(f"{EPMC}/{pmcid}/fullTextXML", timeout=60)
        if r.status_code != 200:
            return "", 0
        xml = r.text
    except Exception:  # noqa: BLE001
        return "", 0
    # <date date-type="received"> is what dates a validation case honestly.
    m = re.search(r'date-type="received".*?</date>', xml, re.S)
    received = ""
    if m:
        y = re.search(r"<year>(\d{4})</year>", m.group(0))
        mo = re.search(r"<month>(\d{1,2})</month>", m.group(0))
        d = re.search(r"<day>(\d{1,2})</day>", m.group(0))
        if y:
            received = f"{y.group(1)}-{int(mo.group(1)) if mo else 1:02d}-{int(d.group(1)) if d else 1:02d}"
    # Strip tags before looking for oligos, so attribute values cannot match.
    text = re.sub(r"<[^>]+>", " ", xml)
    return received, len({s for s in OLIGO_RE.findall(text.upper())})


def registry_targets(registry: Path) -> dict[str, set[str]]:
    """{taxon name: set of genes already covered}, skipping deprecated entries."""
    out: dict[str, set[str]] = {}
    for path in iter_files(registry):
        a = load_assay(path)
        if a.status.value == "deprecated" or not a.target.taxon_name:
            continue
        name = a.target.taxon_name.split(" (")[0].strip()
        out.setdefault(name, set()).add((a.target.gene or "").lower())
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--since", default="2024", help="earliest publication year to consider")
    ap.add_argument("--taxon", action="append", help="limit to these taxon names; repeatable")
    ap.add_argument("--out", type=Path, default=None, help="write the review queue here as TSV")
    ap.add_argument("--per-taxon", type=int, default=10, help="candidates to keep per taxon")
    ap.add_argument("--full-text", action="store_true", help="also fetch open full text for dates and oligos")
    args = ap.parse_args(argv)

    targets = registry_targets(args.registry)
    if args.taxon:
        wanted = {t.lower() for t in args.taxon}
        targets = {k: v for k, v in targets.items() if k.lower() in wanted}
        if not targets:
            ap.error(f"none of {args.taxon} appear as a taxon_name in {args.registry}")

    rows: list[dict] = []
    for taxon, genes in sorted(targets.items()):
        query = (
            f'"{taxon}" AND {ASSAY_TERMS} AND {DEVELOPMENT_TERMS} AND (FIRST_PDATE:[{args.since} TO 3000])'
        )
        hits = search(query, args.per_taxon)
        print(f"{taxon:46s} {len(hits):3d} candidates", flush=True)
        for h in hits:
            received, n_oligos = ("", 0)
            if args.full_text and h.get("pmcid") and h.get("isOpenAccess") == "Y":
                received, n_oligos = full_text_signals(h["pmcid"])
                time.sleep(0.3)  # Europe PMC asks for restraint
            rows.append(
                {
                    "taxon": taxon,
                    "genes_already_covered": "; ".join(sorted(g for g in genes if g)),
                    "year": h.get("pubYear", ""),
                    "doi": h.get("doi", ""),
                    "pmcid": h.get("pmcid", ""),
                    "open_access": h.get("isOpenAccess", ""),
                    "received": received,
                    "oligo_like_sequences": n_oligos,
                    "title": (h.get("title") or "").rstrip("."),
                }
            )
        time.sleep(0.3)

    # Sort so the reading list starts with papers that demonstrably contain oligos.
    rows.sort(key=lambda r: (-int(r["oligo_like_sequences"] or 0), str(r["year"])), reverse=False)
    cols = [
        "taxon",
        "genes_already_covered",
        "year",
        "doi",
        "pmcid",
        "open_access",
        "received",
        "oligo_like_sequences",
        "title",
    ]
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", newline="") as fh:
            w = csv.DictWriter(fh, cols, delimiter="\t")
            w.writeheader()
            w.writerows(rows)
        print(f"\nwrote {len(rows)} candidates to {args.out}")
    else:
        w = csv.DictWriter(sys.stdout, cols, delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    if args.full_text:
        ready = [r for r in rows if r["oligo_like_sequences"] >= 2]
        print(
            f"{len(ready)} of {len(rows)} have readable oligo-like sequences in open full text "
            "— those are the ones worth reading first",
            file=sys.stderr,
        )
    print(
        "Nothing was added to the registry. Read a candidate, fill the template in "
        "CONTRIBUTING.md, then run scripts/check_submission.py on it.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
