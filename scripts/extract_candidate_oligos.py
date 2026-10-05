#!/usr/bin/env python3
"""Pull candidate oligos out of downloaded papers, with enough context to curate them.

    python scripts/extract_candidate_oligos.py --pdf-dir papers --out results/candidate-oligos.tsv
    python scripts/extract_candidate_oligos.py --pdf-dir papers --doi 10.1111/1755-0998.13299 -v

This is the step between "the PDF is downloaded" and "an entry exists". It does
not write to registry/, and it is not meant to be trusted on its own: a primer
table set as an image yields nothing here, and a paper that prints its target
gene yields sequences that are not primers at all. What it produces is a
worksheet - every oligo-like sequence a paper prints, with the words either side
of it, so the name, orientation and product size can be read off instead of
guessed.

Why the context matters more than the sequence
----------------------------------------------
The sequence is the easy part. Everything that has gone wrong in this registry
went wrong in the surrounding detail: a reverse primer stored without being
reverse-complemented, an undeclared cloning tail, a primer attributed to the
paper that used it rather than the one that designed it, an amplicon of 500 bp
where the paper says 531. So each row carries the 90 characters before and after
the match, which is usually enough to see the oligo's name and whether the paper
calls it forward, reverse or probe.

Skipping what is already known
------------------------------
Any DOI already present in registry/ is skipped unless --all is passed, so the
output is candidates rather than a re-run of the verification pass.
"""

from __future__ import annotations

import argparse
import csv
import glob
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import yaml  # noqa: E402

# Reuse the extractor and PDF reader from the verification script rather than
# keeping a second copy: the case and base-composition tests there were tuned
# against real papers and a hostile 596-page report, and two copies would drift.
_spec = importlib.util.spec_from_file_location("_vo", ROOT / "scripts" / "verify_oligos_against_paper.py")
_vo = importlib.util.module_from_spec(_spec)
sys.modules["_vo"] = _vo
_spec.loader.exec_module(_vo)

# Words near a sequence that say what it is. Read off, never inferred.
ROLE_WORDS = re.compile(
    r"\b(forward|reverse|fwd|rev|sense|antisense|probe|outer|inner|nested|primer|F\d|R\d|"
    r"[A-Za-z0-9]+-?F\b|[A-Za-z0-9]+-?R\b|TaqMan|FAM|HEX|VIC|MGB|BHQ|TAMRA|NFQ)\b",
    re.I,
)
# A stated product size, which is the one number worth having from a paper.
SIZE_RE = re.compile(r"\b(\d{2,4})\s*[-–]?\s*(?:bp|base pairs?|nt)\b", re.I)


def registry_dois() -> set[str]:
    out = set()
    for f in glob.glob(str(ROOT / "registry" / "*.yaml")):
        d = yaml.safe_load(Path(f).read_text())
        doi = (d.get("citation") or {}).get("doi")
        if doi:
            out.add(doi.lower())
    return out


def doi_of(path: Path, text: str) -> str:
    """The paper's DOI: from the filename if it is one, else read from the text."""
    stem = path.stem.replace("_", "/")
    if _vo.DOI_IN_TEXT.fullmatch(stem):
        return stem.lower()
    for d in _vo.DOI_IN_TEXT.findall(text[:4000]):
        return d.rstrip(".,;)").lower()
    return ""


COLS = ["doi", "pdf", "sequence", "length", "degenerate", "role_words", "sizes_nearby", "context"]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pdf-dir", type=Path, default=ROOT / "papers")
    ap.add_argument("--doi", action="append", help="only these DOIs; repeatable")
    ap.add_argument("--all", action="store_true", help="include papers already cited in registry/")
    ap.add_argument("--out", type=Path)
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)

    known = set() if args.all else registry_dois()
    want = {d.lower() for d in args.doi} if args.doi else None

    rows: list[dict] = []
    skipped_known, no_oligos = 0, []
    for path in sorted(args.pdf_dir.glob("*.pdf")):
        text = _vo.pdf_text(path)
        if not text:
            continue
        doi = doi_of(path, text)
        if want is not None and doi not in want:
            continue
        if doi and doi in known:
            skipped_known += 1
            continue
        seqs = _vo.printed_oligos(text)
        if not seqs:
            # Almost always a primer table set as an image. Worth reporting as
            # its own outcome: the paper is in hand but still needs human eyes.
            no_oligos.append((doi or path.name, path.name))
            continue
        flatish = re.sub(r"\s+", " ", text)
        for s in seqs:
            # Find the sequence in the readable text to recover its surroundings.
            loose = r"[\s'’-]*".join(re.escape(c) for c in s)
            m = re.search(loose, flatish, re.I)
            ctx = flatish[max(0, m.start() - 90) : m.end() + 90] if m else ""
            rows.append(
                {
                    "doi": doi,
                    "pdf": path.name,
                    "sequence": s,
                    "length": len(s),
                    "degenerate": sum(c not in "ACGTU" for c in s),
                    "role_words": "; ".join(sorted({w.group(0) for w in ROLE_WORDS.finditer(ctx)}))[:90],
                    "sizes_nearby": "; ".join(sorted({w.group(1) for w in SIZE_RE.finditer(ctx)}))[:40],
                    "context": re.sub(r"\s+", " ", ctx)[:200],
                }
            )
        if args.verbose:
            print(f"{doi or path.name:46s} {len(seqs):3d} oligo-like sequences")

    bydoi: dict[str, int] = {}
    for r in rows:
        bydoi[r["doi"]] = bydoi.get(r["doi"], 0) + 1
    print(f"\n{len(rows)} candidate oligos from {len(bydoi)} papers")
    if skipped_known:
        print(f"  ({skipped_known} papers skipped as already cited in registry/; --all includes them)")
    if no_oligos:
        print(f"\n{len(no_oligos)} papers yielded NO readable sequences - primer table is probably an image:")
        for doi, name in no_oligos:
            print(f"  {doi or '(no DOI)':46s} {name}")
    print()
    for doi, n in sorted(bydoi.items(), key=lambda kv: -kv[1]):
        print(f"  {n:3d}  {doi}")

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", newline="") as fh:
            w = csv.DictWriter(fh, COLS, delimiter="\t")
            w.writeheader()
            w.writerows(rows)
        print(f"\nwrote {len(rows)} rows to {args.out}")

    print(
        "\nNothing was added to registry/. A row is a candidate: read the paper's own table to "
        "settle each oligo's name, orientation and product size, then run "
        "scripts/check_submission.py, which screens the pair against real records before anyone "
        "trusts it.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
