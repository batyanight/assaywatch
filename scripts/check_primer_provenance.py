#!/usr/bin/env python3
"""Does the cited paper DESIGN its primers, or did it get them from somewhere else?

    python scripts/check_primer_provenance.py --pdf-dir papers
    python scripts/check_primer_provenance.py --assay Pan_Plasmodium_sp_and_Haemopro_cytochrome_c -v
    python scripts/check_primer_provenance.py --pdf-dir papers --tsv results/primer-provenance.tsv

An assay's SCOPE comes from the paper that designed its primers, not from the
paper somebody read them in. Conflating the two scoped the ranavirus MCP assay
away from the fish ranaviruses it is documented to detect, and attributed the
avian haemosporidian primers to Hellgren et al. 2004 when that paper says, in as
many words, "we used HaemF-HaemR2 primers (Bensch et al., 2000)".

That second case is the pattern this script looks for. A paper reusing someone
else's oligos nearly always says so, in a sentence naming the oligo and a
citation within a few words of each other. So: find each stored oligo's NAME in
the paper, take the text around it, and report any citation marker there.

    attributed-elsewhere   a citation sits beside the oligo's name - the paper
                           is probably a user. Read the sentence and decide.
    claimed-here           design language sits beside it ("we designed",
                           "newly constructed", "in this study")
    name-not-found         the paper never uses that name, which is itself a
                           reason to look: the oligo may not be from this paper.
                           Only said of a paper whose text prints enough oligos
                           to be a methods paper (see no-oligos)
    no-oligos              the text held prints fewer than two oligo-like runs, so
                           it has lost its primer table or its inline sequences
                           and the names live in what was lost. NOT evidence the
                           oligo is from another paper: before this verdict
                           existed, 33 of 51 `name-not-found` rows over the 21
                           PubMed Central texts came from papers like that
    name-too-short         the stored name is a single character, which cannot be
                           searched for; nothing is concluded from it
    no-full-text           nothing readable to check

This proposes; it does not edit. Every verdict needs the sentence read, because
a citation near a primer name can equally mean "we modified the primer of X" -
and in that case the registry should cite whichever paper matches the sequence
actually stored, which only a human comparing sequences can settle.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

_spec = importlib.util.spec_from_file_location("_vo", ROOT / "scripts" / "verify_oligos_against_paper.py")
_vo = importlib.util.module_from_spec(_spec)
sys.modules["_vo"] = _vo
_spec.loader.exec_module(_vo)

from assaywatch.validate import iter_files, load_assay  # noqa: E402

# "(Bensch et al., 2000)", "(Mao et al. 1997)", "[19]", "reference 22", "ref. 10"
CITATION = re.compile(
    r"\([A-Z][A-Za-zÀ-ɏ'\-]+\s+(?:et\s+al\.?|and\s+[A-Z][A-Za-z'\-]+)[,.]?\s*\d{4}\)"
    r"|\[\d{1,3}(?:\s*[,–-]\s*\d{1,3})*\]"
    r"|\bref(?:erence)?s?\.?\s*\d{1,3}\b"
    r"|\bpreviously (?:described|published|reported)\b"
    r"|\bdescribed (?:by|in|previously)\b"
    r"|\badapted from\b|\bmodified from\b|\bbased on (?:the )?primers?\b"
)
# Language a paper uses about its own design work.
DESIGNED_HERE = re.compile(
    r"\bwe (?:designed|constructed|developed|created)\b|\bnewly (?:designed|constructed|developed)\b"
    r"|\bin this study\b|\bthis study\b|\bwere designed\b|\bwere constructed\b|\bprimers were designed\b",
    re.I,
)


def oligos_of(assay):
    out = []
    for slot in ("forward", "reverse", "probe"):
        o = getattr(assay.oligos, slot, None)
        if o is not None and o.name:
            out.append((slot, o))
    for i, o in enumerate(assay.oligos.alternates or []):
        if o.name:
            out.append((f"alt{i}", o))
    return out


find_name = _vo.find_name  # shared with the verifier, which uses it to spot a lost sequence


COLS = ["assay_id", "slot", "oligo_name", "verdict", "evidence", "doi", "oligos_designed_here", "context"]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--pdf-dir", type=Path, default=ROOT / "papers")
    ap.add_argument("--assay", action="append")
    ap.add_argument("--tsv", type=Path)
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)

    by_doi, everything = _vo.index_papers(args.pdf_dir) if args.pdf_dir.exists() else ({}, [])
    print(f"indexed {len(everything)} papers from {args.pdf_dir}\n")

    paths = list(iter_files(args.registry))
    if args.assay:
        want = set(args.assay)
        paths = [p for p in paths if p.stem in want]

    rows = []
    for path in paths:
        a = load_assay(path)
        hit = _vo.local_paper(a, by_doi, everything) if everything else None
        text = re.sub(r"\s+", " ", hit[0]) if hit else None
        # How much of the paper's primer content survived into the text we hold.
        thin = bool(hit) and len(_vo.printed_oligos(hit[0])) < _vo.MIN_PRINTED_FOR_ABSENT
        for slot, o in oligos_of(a):
            if text is None:
                rows.append(
                    {
                        "assay_id": a.id,
                        "slot": slot,
                        "oligo_name": o.name,
                        "verdict": "no-full-text",
                        "evidence": "",
                        "doi": a.citation.doi or "",
                        "oligos_designed_here": ""
                        if a.citation.oligos_designed_here is None
                        else str(a.citation.oligos_designed_here),
                        "context": "",
                    }
                )
                continue
            if _vo.name_pattern(o.name) is None:
                rows.append(
                    {
                        "assay_id": a.id,
                        "slot": slot,
                        "oligo_name": o.name,
                        "verdict": "name-too-short",
                        "evidence": "",
                        "doi": a.citation.doi or "",
                        "oligos_designed_here": ""
                        if a.citation.oligos_designed_here is None
                        else str(a.citation.oligos_designed_here),
                        "context": "",
                    }
                )
                continue
            spots = find_name(o.name, text)
            if not spots:
                # Absence of a name from a text that lost its tables is a fact
                # about the text, not about the oligo.
                verdict, ev, ctx = ("no-oligos" if thin else "name-not-found"), "", ""
            else:
                # Look at a window around each mention; a reuse citation is
                # usually in the same clause as the name.
                verdict, ev, ctx = "no-signal", "", ""
                for s in spots[:6]:
                    w = text[max(0, s - 160) : s + 200]
                    cit = CITATION.search(w)
                    des = DESIGNED_HERE.search(w)
                    if cit and not des:
                        verdict, ev, ctx = "attributed-elsewhere", cit.group(0)[:60], w[:200]
                        break
                    if des and not cit:
                        verdict, ev, ctx = "claimed-here", des.group(0)[:60], w[:200]
                    elif cit and des and verdict == "no-signal":
                        verdict, ev, ctx = "ambiguous", f"{cit.group(0)[:40]} + {des.group(0)[:30]}", w[:200]
            if len(re.sub(r"[^A-Za-z0-9]+", "", o.name)) < 4 and verdict not in (
                "no-oligos",
                "name-not-found",
            ):
                # A 2-3 character name such as `1F` can also be a figure panel.
                ev = f"{ev} [short name: may be a figure panel]".strip()
            rows.append(
                {
                    "assay_id": a.id,
                    "slot": slot,
                    "oligo_name": o.name,
                    "verdict": verdict,
                    "evidence": ev,
                    "doi": a.citation.doi or "",
                    "oligos_designed_here": ""
                    if a.citation.oligos_designed_here is None
                    else str(a.citation.oligos_designed_here),
                    "context": ctx,
                }
            )

    from collections import Counter

    c = Counter(r["verdict"] for r in rows)
    print(f"{len(rows)} named oligos across {len(paths)} assays\n")
    for k, n in c.most_common():
        print(f"  {n:4d}  {k}")

    # The actionable set: a citation beside the oligo name on an entry that
    # still claims the cited paper designed it.
    sus = [r for r in rows if r["verdict"] == "attributed-elsewhere" and r["oligos_designed_here"] != "False"]
    print(f"\n### {len(sus)} oligos look attributed to another paper, on entries not already marked False")
    seen = set()
    for r in sus:
        if r["assay_id"] in seen and not args.verbose:
            continue
        seen.add(r["assay_id"])
        print(f"  {r['assay_id'][:46]:46s} {r['oligo_name'][:18]:18s} {r['evidence']}")
        if args.verbose:
            print(f"      ...{r['context']}...")

    if args.tsv:
        args.tsv.parent.mkdir(parents=True, exist_ok=True)
        with args.tsv.open("w", newline="") as fh:
            w = csv.DictWriter(fh, COLS, delimiter="\t")
            w.writeheader()
            w.writerows(rows)
        print(f"\nwrote {args.tsv}")

    print(
        "\nNothing was edited. Each row needs the sentence read: a citation beside a primer name "
        "can mean 'we used X's primer' or 'we modified X's primer', and where it is a modification "
        "the registry must cite whichever paper matches the SEQUENCE actually stored.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
