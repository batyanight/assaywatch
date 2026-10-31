#!/usr/bin/env python3
"""Print the sentences in which each paper claims its assay does NOT amplify something.

    python scripts/extract_exclusivity.py --out .tmp/exclusivity.txt
    python scripts/extract_exclusivity.py --assay BPSV_dsDNA_RPO147_J6R_TaqMan_Zhao_2013

`target.exclusivity_taxids` (2026-10-27) retrieves a near neighbour a paper claims to
exclude, so the pipeline can test that claim instead of reporting whatever off-target
records happened to be on disk. Populating it is per-paper reading: a specificity claim
is a sentence or a table, it names organisms in prose rather than by taxid, and whether
a named organism is a NEIGHBOUR THE ASSAY MUST DISTINGUISH or a far-off negative control
is a judgement. So this finds and prints the candidate sentences, with the entries that
cite the paper, and writes nothing.

WHAT IT LOOKS FOR, and what each pattern is worth:

  "did not cross-react", "no cross-reactivity"   the strongest form, and usually the
                                                 sentence that lists the panel
  "was/were negative", "no amplification",       next strongest, but also how a paper
  "not detected", "no product"                   reports a failed sample, so read it
  "specific for", "specificity"                  weakest: often about the design intent
                                                 rather than a tested exclusion

A taxid is never guessed here. Look each organism up with `esearch -db taxonomy` before
it goes in a registry file, the way the BPSV entry's two were.
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

import yaml  # noqa: E402

from assaywatch.papers import paper_for_doi  # noqa: E402

CLAIM = (
    (r"cross[- ]react", "cross-reaction"),
    (r"\bno amplification\b|\bnot amplif|\bfailed to amplif", "no amplification"),
    (r"\bwere negative\b|\bwas negative\b|\bnegative for\b", "negative"),
    (r"\bnot detect|\bno product\b|\bno signal\b", "not detected"),
    (r"\bspecific(?:ity)? (?:for|to)\b|\bdid not detect\b", "specificity"),
)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=REPO / "registry")
    ap.add_argument("--papers", type=Path, default=REPO / "papers")
    ap.add_argument("--assay", action="append", help="only these entries (repeatable)")
    ap.add_argument("--out", type=Path, help="write here instead of stdout")
    args = ap.parse_args(argv)

    # `scripts/` is not a package, so the two readers this shares with
    # extract_conditions.py -- pdftotext/JATS text, and a rough sentence split that
    # repairs the degree signs a PDF loses -- are loaded from that file by path.
    spec = importlib.util.spec_from_file_location(
        "extract_conditions", REPO / "scripts" / "extract_conditions.py"
    )
    assert spec and spec.loader
    ec = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ec)
    sentences, text_of = ec.sentences, ec.text_of

    by_paper: dict[Path, list[tuple[str, dict]]] = {}
    for path in sorted(args.registry.glob("*.yaml")):
        if args.assay and path.stem not in args.assay:
            continue
        doc = yaml.safe_load(path.read_text()) or {}
        doi = ((doc.get("citation") or {}).get("doi") or "").strip()
        paper = paper_for_doi(doi, args.papers) if doi else None
        if paper is None:
            continue
        by_paper.setdefault(paper, []).append((path.stem, doc))

    out = args.out.open("w") if args.out else sys.stdout
    for paper, entries in sorted(by_paper.items()):
        text = text_of(paper)
        hits = []
        for s in sentences(text):
            for pattern, label in CLAIM:
                if re.search(pattern, s, re.I):
                    hits.append((label, s))
                    break
        if not hits:
            continue
        print("=" * 100, file=out)
        print(f"PAPER {paper.name}", file=out)
        for aid, doc in entries:
            t = doc.get("target") or {}
            print(
                f"  ENTRY {aid}\n"
                f"        taxid={t.get('taxid')} {t.get('taxon_name')!r} "
                f"scope={t.get('scope_taxids')} excl={t.get('exclusivity_taxids')}",
                file=out,
            )
        for label, s in hits:
            print(f"  [{label}] {s[:400]}", file=out)
    if args.out:
        out.close()
        print(f"{len(by_paper)} papers scanned -> {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
