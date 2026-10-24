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

from assaywatch.papers import doi_stem  # noqa: E402

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


def doi_of(path: Path, text: str, held: list[str] | None = None) -> str:
    """The paper's DOI: the filename's if it is one, else the earliest one it prints.

    `held` is the DOIs the index gave this file. Of those, the one printed first is
    the file's own: a paper prints its own DOI in its header, and cites others after
    it. With nothing held (every DOI it prints went to another file) the earliest
    DOI it prints is used, so the file is still labelled and not silently dropped.
    """
    # The filename is authoritative only when a DOI we already know forward-maps
    # onto it. It cannot be reverse-mapped: `/`, `(` and `)` all become `_`, and
    # a round trip cannot tell them apart either, because reversing `_` to `/`
    # and forward-mapping again returns the same stem. Inferring a DOI from a
    # stem is what fabricated ten of them into docs/papers-index.cache.json.
    for known in held or ():
        if doi_stem(known) == path.stem.lower():
            return known.strip().lower()
    # Fallback: read the stem as a DOI. Best-effort only, and second in line,
    # because `/`, `(` and `)` all map to `_` and a round trip cannot tell them
    # apart - for a parenthesised DOI this returns a DOI that does not exist
    # (`10.1016/0890-8508/92/90002-f`). It stays because a DOI-named file is
    # authoritative for its own identity and most stems are unambiguous, and
    # because the exact branch above now catches the case that matters: a file
    # whose DOI the index already knows. Never used to key a cache or a fetch.
    # This one reverse-maps on purpose, as the paragraph above explains.
    stem = path.stem.replace("_", "/")
    if _vo.DOI_IN_TEXT.fullmatch(stem):
        return stem.lower()
    offsets = _vo.text_dois(text)
    pool = [d for d in (held or []) if d in offsets] or list(offsets)
    return min(pool, key=lambda d: offsets[d]) if pool else ""


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
    skipped_known, no_oligos, duplicates, shared = 0, [], 0, []
    # Which DOIs each file holds in the index. A paper in two formats (a PDF and a
    # `.txt`) is two files for one DOI, and walking both listed every sequence
    # twice and could report one DOI as having candidates AND as yielding none. But
    # skipping every file that is not the index's winner for its first DOI dropped a
    # different paper silently: one that cites another DOI before printing its own
    # loses that DOI's claim, and with it all its candidates. So a file is skipped
    # only when the file that holds its DOI already yields every sequence it does.
    by_doi, everything = _vo.index_papers(args.pdf_dir)
    holds: dict[Path, list[str]] = {}
    for held_doi, (_, held_path) in by_doi.items():
        holds.setdefault(held_path, []).append(held_doi)
    for text, path in everything:
        doi = doi_of(path, text, holds.get(path))
        if not holds.get(path) and doi and doi in by_doi:
            winner_text, winner_path = by_doi[doi]
            if set(_vo.printed_oligos(text)) <= set(_vo.printed_oligos(winner_text)):
                duplicates += 1
                continue  # the winner already yields everything this file would add
            shared.append((doi, path.name, winner_path.name))
        if want is not None and doi not in want:
            continue
        if doi and doi in known:
            skipped_known += 1
            continue
        seqs = _vo.printed_oligos(text)
        if not seqs:
            # The paper is in hand and its sequences are not reachable from the
            # text. Two different causes, and the file extension hints at which:
            # in a PDF the primer table is usually set as an image, while a `.txt`
            # from PubMed Central can have lost tables, and inline sequences, to
            # the full-text extraction (some PMC articles keep their tables whole
            # and some do not, so this is not predictable from the journal). Either
            # way this is its own outcome, not an absence of primers, and it still
            # needs eyes.
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
    if duplicates:
        print(
            f"  ({duplicates} files skipped as copies: another file for the same DOI yields all their sequences)"
        )
    for doi, name, other in shared:
        print(f"  note: {name} and {other} both claim {doi} but print different oligos; both are listed")
    if no_oligos:
        print(
            f"\n{len(no_oligos)} papers yielded NO readable sequences - a .pdf here means the "
            "primer table is probably an image, a .txt that PubMed Central dropped some of its content:"
        )
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
