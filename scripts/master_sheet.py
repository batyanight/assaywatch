#!/usr/bin/env python3
"""One row per assay: paper, target, scope, parameters, and how well each is verified.

    python scripts/master_sheet.py
    python scripts/master_sheet.py --refresh-taxa    # re-fetch names from NCBI

Writes `docs/assay-master-sheet.tsv` (the sheet) and `docs/assay-master-sheet.md`
(a readable summary). Everything is pulled from a source of record:

    registry/*.yaml                         ids, oligos, scope, parameters
    docs/papers-index.cache.json            Crossref: author, year, journal, title
    docs/taxa-cache.json                    NCBI: scientific name, common name, rank
    results/oligo-verification-*.tsv        whether each oligo was found in its paper

Nothing is filled in from memory. In particular **common names are taken from
NCBI's own GenbankCommonName or CommonName fields and left BLANK when NCBI has
none** - a plausible-sounding common name invented to fill a cell is exactly the
kind of error this project has spent two days removing.

Why both taxon names
--------------------
ICTV renames propagate into NCBI, so a taxid keeps working while its name
changes underneath: txid10292 is now Orthoherpesviridae and was Herpesviridae,
txid11232 is Morbillivirus canis and was Canine morbillivirus. The taxid is what
retrieval actually uses, so screening is unaffected - but a report naming only
one of the two will not match what somebody else is reading. The sheet carries
`taxon_scientific_name` (NCBI's current name), `taxon_name_in_registry` (what
the entry says) and `taxon_name_differs` so the disagreement is visible rather
than silently resolved.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


from assaywatch.degeneracy import assay_degeneracy  # noqa: E402
from assaywatch.retrieve import group_slug  # noqa: E402
from assaywatch.validate import load_assay  # noqa: E402

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


def fetch_taxa(taxids: list[int], email: str) -> dict[str, dict]:
    """{taxid: {scientific_name, common_name, rank, lineage_tail}} straight from NCBI."""
    out: dict[str, dict] = {}
    for i in range(0, len(taxids), 50):
        chunk = taxids[i : i + 50]
        q = urllib.parse.urlencode(
            {
                "db": "taxonomy",
                "retmode": "xml",
                "id": ",".join(str(t) for t in chunk),
                "email": email,
                "tool": "assaywatch",
            }
        )
        try:
            with urllib.request.urlopen(f"{EUTILS}?{q}", timeout=60) as r:
                xml = r.read().decode()
        except Exception as e:  # noqa: BLE001
            print(f"  taxonomy fetch failed for {chunk[:3]}...: {e}", file=sys.stderr)
            continue
        # Each top-level <Taxon> is one requested id; nested <Taxon> blocks are its
        # lineage, so split on the outermost records only.
        for blk in re.findall(r"<Taxon>(.*?)</Taxon>\s*(?=<Taxon>|</TaxaSet>)", xml, re.S):
            tid = re.search(r"<TaxId>(\d+)</TaxId>", blk)
            if not tid:
                continue
            sci = re.search(r"<ScientificName>(.*?)</ScientificName>", blk)
            rank = re.search(r"<Rank>(.*?)</Rank>", blk)
            gcn = re.search(r"<GenbankCommonName>(.*?)</GenbankCommonName>", blk)
            cn = re.search(r"<CommonName>(.*?)</CommonName>", blk)
            lin = re.search(r"<Lineage>(.*?)</Lineage>", blk)
            out[tid.group(1)] = {
                "scientific_name": sci.group(1) if sci else "",
                # NCBI's own common name, or blank. Never invented.
                "common_name": (gcn.group(1) if gcn else (cn.group(1) if cn else "")),
                "rank": rank.group(1) if rank else "",
                "lineage_tail": (lin.group(1).split("; ")[-2:] if lin else []),
            }
        time.sleep(0.4)
    return out


def verification_summary(path: Path) -> dict[str, str]:
    """{assay_id: 'exact 2, absent 1'} from the last oligo-verification run."""
    if not path.exists():
        return {}
    per: dict[str, Counter] = defaultdict(Counter)
    with path.open() as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            per[r["assay_id"]][r["verdict"]] += 1
    return {k: ", ".join(f"{n} {v}" for v, n in c.most_common()) for k, c in per.items()}


COLS = [
    "assay_id",
    "status",
    "doi",
    "year",
    "first_author",
    "journal",
    "paper_title",
    "oligos_designed_here",
    "target_gene",
    "taxon_scientific_name",
    "taxon_common_name",
    "taxon_name_in_registry",
    "taxon_name_differs",
    "taxid",
    "taxid_rank",
    "scope_summary",
    "scope_query",
    "retrieval_group",
    "genome_type",
    "chemistry",
    "amplicon_bp",
    "forward_name",
    "forward_seq",
    "reverse_name",
    "reverse_seq",
    "probe_name",
    "probe_seq",
    "n_pool_members",
    "degeneracy_fold",
    "degeneracy_tier",
    "predict_protocol",
    "nested_round",
    "sequence_verification",
    "needs_review",
]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--papers-cache", type=Path, default=ROOT / "docs" / "papers-index.cache.json")
    ap.add_argument("--taxa-cache", type=Path, default=ROOT / "docs" / "taxa-cache.json")
    ap.add_argument(
        "--verification", type=Path, default=ROOT / "results" / "oligo-verification-2026-10-05.tsv"
    )
    ap.add_argument("--out", type=Path, default=ROOT / "docs" / "assay-master-sheet.tsv")
    ap.add_argument("--md", type=Path, default=ROOT / "docs" / "assay-master-sheet.md")
    ap.add_argument("--email", default="nightb02@nyu.edu")
    ap.add_argument("--refresh-taxa", action="store_true")
    args = ap.parse_args(argv)

    papers = json.loads(args.papers_cache.read_text()) if args.papers_cache.exists() else {}
    taxa = json.loads(args.taxa_cache.read_text()) if args.taxa_cache.exists() else {}
    verif = verification_summary(args.verification)

    assays = [load_assay(p) for p in sorted(args.registry.glob("*.yaml"))]
    want = sorted({a.target.taxid for a in assays if a.target.taxid})
    missing = [t for t in want if str(t) not in taxa]
    if missing or args.refresh_taxa:
        fresh = fetch_taxa(want if args.refresh_taxa else missing, args.email)
        taxa.update(fresh)
        args.taxa_cache.write_text(json.dumps(taxa, indent=1, sort_keys=True) + "\n")
        print(f"fetched {len(fresh)} taxa into {args.taxa_cache.name}")

    rows = []
    for a in assays:
        m = papers.get((a.citation.doi or "").lower()) or {}
        t = taxa.get(str(a.target.taxid)) or {}
        reg_name = a.target.taxon_name or ""
        sci = t.get("scientific_name", "")
        # The registry annotates names in parentheses for several reasons - a
        # rename ("Orthoherpesviridae (formerly Herpesviridae)"), a restriction
        # ("Largemouth bass virus (sensu stricto)"), a clade label ("Perkinsea
        # (NAG01)"). Only the part before the parenthesis is a claim about what
        # the taxon is called, so only that is compared; otherwise every
        # deliberate annotation reads as a disagreement with NCBI.
        reg_head = reg_name.split(" (")[0].strip()
        q = a.target.query
        scope = (
            f"whole taxon txid{a.target.taxid}"
            if not q
            else ("taxon restricted by an Entrez term" + (" using NOT" if "NOT" in q.upper() else ""))
        )
        # A name can legitimately differ from its taxid's when the entry narrows
        # the taxon by query: LMBV_dsDNA_MCP_Grizzle_2003 sits on genus Ranavirus
        # but its query restricts retrieval to the bass clade, so the taxon_name
        # describes the scoped subset rather than the taxid. Only an unscoped
        # entry whose name disagrees is reporting a rename.
        if not (sci and reg_head) or sci.lower() == reg_head.lower():
            differs = ""
        elif q:
            differs = "narrower-than-taxid"
        else:
            differs = "renamed"
        ol = a.oligos
        try:
            deg = assay_degeneracy(a)
            fold, tier = deg.total_fold, deg.tier()
        except Exception:  # noqa: BLE001
            fold, tier = "", ""
        rows.append(
            {
                "assay_id": a.id,
                "status": a.status.value,
                "doi": a.citation.doi or "",
                "year": m.get("year") or a.citation.design_year or "",
                "first_author": m.get("first_author", ""),
                "journal": m.get("journal", ""),
                "paper_title": (m.get("title") or "")[:120],
                "oligos_designed_here": ""
                if a.citation.oligos_designed_here is None
                else str(a.citation.oligos_designed_here),
                "target_gene": a.target.gene or "",
                "taxon_scientific_name": sci,
                "taxon_common_name": t.get("common_name", ""),
                "taxon_name_in_registry": reg_name,
                "taxon_name_differs": differs,
                "taxid": a.target.taxid or "",
                "taxid_rank": t.get("rank", ""),
                "scope_summary": scope,
                "scope_query": q or "",
                "retrieval_group": f"{a.target.taxid}/{group_slug(q)}" if a.target.taxid else "",
                "genome_type": a.target.genome_type or "",
                "chemistry": a.chemistry.value,
                "amplicon_bp": a.amplicon_bp or "",
                "forward_name": (ol.forward.name or "") if ol.forward else "",
                "forward_seq": (ol.forward.seq_as_written or ol.forward.seq) if ol.forward else "",
                "reverse_name": (ol.reverse.name or "") if ol.reverse else "",
                "reverse_seq": (ol.reverse.seq_as_written or ol.reverse.seq) if ol.reverse else "",
                "probe_name": (ol.probe.name or "") if ol.probe else "",
                "probe_seq": (ol.probe.seq_as_written or ol.probe.seq) if ol.probe else "",
                "n_pool_members": len(ol.alternates or []),
                "degeneracy_fold": fold,
                "degeneracy_tier": tier,
                "predict_protocol": a.source.predict_protocol or "",
                "nested_round": a.source.nested_round or "",
                "sequence_verification": verif.get(a.id, ""),
                "needs_review": "; ".join(a.needs_review or []),
            }
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, COLS, delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    n_common = sum(1 for r in rows if r["taxon_common_name"])
    n_diff = sum(1 for r in rows if r["taxon_name_differs"])
    n_scoped = sum(1 for r in rows if r["scope_query"])
    n_flag = sum(1 for r in rows if r["needs_review"])
    md = [
        "# Assay master sheet",
        "",
        f"`assay-master-sheet.tsv` has one row per assay, {len(rows)} rows and {len(COLS)} columns. "
        "Open it in a spreadsheet; this page is the key and the caveats.",
        "",
        "Regenerate after any registry change:",
        "",
        "```bash",
        "python scripts/master_sheet.py",
        "```",
        "",
        "## Where each column comes from",
        "",
        "| source | columns |",
        "|---|---|",
        "| `registry/*.yaml` | ids, gene, taxid, scope, chemistry, amplicon, oligos, flags |",
        "| Crossref (`papers-index.cache.json`) | year, first author, journal, title |",
        "| NCBI Taxonomy (`taxa-cache.json`) | scientific name, common name, rank |",
        "| last verification run | `sequence_verification` |",
        "| computed | `degeneracy_fold`, `degeneracy_tier`, `retrieval_group` |",
        "",
        "Nothing is filled in from memory.",
        "",
        "## Two columns that need reading carefully",
        "",
        f"**`taxon_common_name` is NCBI's, and is blank for most rows ({n_common} of {len(rows)} "
        "have one).** A blank means NCBI publishes no common name for that taxid, not that none "
        "exists. It is left blank on purpose: a plausible common name invented to fill the cell "
        "would be indistinguishable from a real one.",
        "",
        f"**`taxon_name_differs` marks the {n_diff} rows where NCBI's current scientific name is "
        "not the name the registry entry carries.** These are ICTV renames that propagated into "
        "NCBI - Herpesviridae became Orthoherpesviridae, Canine morbillivirus became Morbillivirus "
        "canis. The taxid is unchanged and is what retrieval uses, so screening is unaffected; both "
        "names are kept because a reader searching either one should find the assay.",
        "",
        "## Scope",
        "",
        f"`scope_query` is the Entrez term ANDed onto the taxon, i.e. which loci are actually "
        f"pulled from GenBank. {n_scoped} of {len(rows)} assays have one; the rest are screened "
        "against their whole taxon. `retrieval_group` is `taxid/slug`, and assays sharing a group "
        "share one archive, so changing a query splits an assay off into its own fetch.",
        "",
        "## Verification and flags",
        "",
        "`sequence_verification` counts how each oligo fared against its own paper: `exact` means "
        "found inside an oligo the paper lists, `in-text` means found somewhere in the paper but "
        "not in a listed oligo, `absent` means not found, and `no-full-text`/`no-doi` mean it could "
        "not be checked at all. Blank means the entry was added after the last run.",
        "",
        f"`needs_review` is non-empty for {n_flag} of {len(rows)} assays. A flag is a known, "
        "recorded caveat, not a defect to hide.",
        "",
    ]
    args.md.write_text("\n".join(md))
    print(f"wrote {args.out} ({len(rows)} rows) and {args.md}")
    print(
        f"  {n_common} taxa have an NCBI common name; {n_diff} rows have a renamed taxon; "
        f"{n_scoped} are scope-restricted; {n_flag} carry review flags"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
