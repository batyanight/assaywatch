#!/usr/bin/env python3
"""What the registry is missing that a person, not a script, has to supply.

    python scripts/materials_needed.py --out docs/materials-needed.tsv

One row per gap per assay, so an assay with two gaps appears twice and the file
sorts and filters by bucket. The buckets are deliberately about WHO can close the
gap - a librarian, the paper's publisher, the WCS lab, or Batya deciding - because
that is the only axis along which this list is actionable.

Every assay_id written here is a current registry id, because the ids come from
`load_assay` rather than from a calls table. That is not a stylistic choice: a
calls table can hold ids the registry no longer has (results/2026-10-20 holds
three), and assaywatch/collect.py concatenating screens without checking them
against the registry is the open bug this script must not reproduce.

Oligo verdicts come from results/oligo-verification.tsv, which
scripts/verify_oligos_against_paper.py writes. Regenerate that first, or the
`supplement` and `oligos-not-in-paper` buckets will be stale:

    python scripts/verify_oligos_against_paper.py --pdf-dir papers --tsv results/oligo-verification.tsv
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from assaywatch.papers import paper_for_doi  # noqa: E402
from assaywatch.validate import iter_files, load_assay  # noqa: E402

COLUMNS = ["bucket", "assay_id", "doi", "what_is_needed", "blocks", "notes"]

# A verdict that means the paper said something about the oligo. Anything else
# means the paper is on disk and silent, which is a different request.
CONFIRMING = {"exact", "revcomp", "in-text"}

# The PREDICT panel's oligos were read from this supplement, which is CC-BY and
# is not in papers/. Counted separately because one document closes all of them.
PREDICT_SUPPLEMENT = "Anthony et al. 2015, Nat Commun 6:8147, Supplementary Methods (CC-BY)"


def verdicts_by_assay(path: Path) -> dict[str, list[dict[str, str]]]:
    out: dict[str, list[dict[str, str]]] = defaultdict(list)
    if not path.exists():
        print(f"{path} missing; the paper-content buckets will be empty", file=sys.stderr)
        return out
    with path.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            out[row["assay_id"]].append(row)
    return out


def rows_for(assay, doc: dict, verdicts: list[dict[str, str]], papers: Path) -> list[dict[str, str]]:
    """Every gap this one entry has, as TSV rows."""
    out = []
    cite = assay.citation
    doi = (cite.doi if cite else None) or ""
    ref = ((cite.reference or cite.as_written or "") if cite else "").strip()
    flags = set(doc.get("needs_review") or [])
    notes = ((doc.get("source") or {}).get("notes_curator") or "") if doc.get("source") else ""
    paper = paper_for_doi(doi, papers) if doi else None

    def add(bucket, need, blocks, note=""):
        out.append(
            {
                "bucket": bucket,
                "assay_id": assay.id,
                "doi": doi,
                "what_is_needed": need,
                "blocks": blocks,
                "notes": note,
            }
        )

    if doi and not paper:
        add("paper-pdf", "the full text of this DOI", "oligo verification against the source")
    elif not doi and ref:
        inhouse = any(w in ref.lower() for w in ("in house", "in-house", "unpublished", "wcs", "cii"))
        if "PREDICT" in ref:
            add(
                "citation",
                "the PREDICT protocol sheet this came from",
                "citation + oligo verification",
                ref[:90],
            )
        elif inhouse:
            add(
                "lab-record",
                "the lab's own record of who designed these and when",
                "any citation at all",
                ref[:90],
            )
        else:
            add("citation", f"a DOI or the paper for: {ref[:70]}", "citation verification", ref[:90])
    elif not doi and not ref:
        add(
            "provenance",
            "any provenance at all - no DOI and no reference is recorded",
            "everything downstream",
        )

    if paper and verdicts:
        vs = {r["verdict"] for r in verdicts}
        if not (vs & CONFIRMING) and not any(v.startswith("near:") for v in vs):
            if "no-oligos" in vs:
                add(
                    "supplement",
                    "the supplementary table or a text-layer copy; this PDF yields no sequences",
                    "oligo verification",
                    paper.name,
                )
            else:
                add(
                    "oligos-not-in-paper",
                    "which source these oligos actually came from; the cited paper prints others",
                    "citation correctness",
                    paper.name,
                )

    if "NEED_TO_ORDER" in flags:
        add(
            "lab-oligos",
            "confirmation these oligos were ordered and exist in the freezer",
            "promotion past draft",
        )
    if flags & {
        "SEQUENCES_READ_FROM_FIGURE_IMAGE",
        "REVERSE_PRIMER_RC_FROM_FIGURE",
        "PROBE_OMITTED_OCR_UNRELIABLE",
    }:
        add("figure", "a legible copy of the figure the sequences were read off", "sequence confidence")
    if "DO_NOT_USE" in flags:
        add("decision", "a keep-or-delete decision; the entry is flagged DO_NOT_USE", "registry hygiene")
    if PREDICT_SUPPLEMENT.split(",")[0] in notes or "Anthony et al. 2015" in notes:
        add(
            "predict-supplement",
            f"one document closes this and every other row in this bucket: {PREDICT_SUPPLEMENT}",
            "oligo verification for the whole PREDICT panel",
        )
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--papers", type=Path, default=ROOT / "papers")
    ap.add_argument("--verification", type=Path, default=ROOT / "results" / "oligo-verification.tsv")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args(argv)

    ver = verdicts_by_assay(args.verification)
    rows: list[dict[str, str]] = []
    for path in sorted(iter_files(args.registry)):
        assay = load_assay(path)
        rows += rows_for(assay, yaml.safe_load(path.read_text()), ver.get(assay.id, []), args.papers)

    rows.sort(key=lambda r: (r["bucket"], r["assay_id"]))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    tally = Counter(r["bucket"] for r in rows)
    print(f"{len(rows)} gaps across {len({r['assay_id'] for r in rows})} entries")
    for bucket, n in sorted(tally.items(), key=lambda kv: -kv[1]):
        print(f"  {n:4d}  {bucket}")
    print(f"written: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
