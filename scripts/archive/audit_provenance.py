#!/usr/bin/env python3
"""Audit the registry for provenance problems: does each citation DESIGN its oligos?

    python scripts/audit_provenance.py
    python scripts/audit_provenance.py --class name-vs-author --verbose
    python scripts/audit_provenance.py --tsv results/provenance-audit.tsv

Why this exists
---------------
On 2026-10-04 the ranavirus MCP assay was scoped away from the fish ranaviruses
because its citation was Johnson et al. 2008, a box-turtle and tortoise study.
The oligos turned out to be byte-identical to FV3-54F / FV3-584R of Mao et al.
1997, which Grizzle et al. 2003 reports amplifying every ranavirus tested, fish
included. The citation recorded where the sequences were READ FROM; an assay's
scope follows from where they were DESIGNED. Conflating those produced a
confident, wrong, published-looking result.

That mistake has a signature, and it is cheap to look for: the oligo NAMES
usually carry the design lab's convention. `RanaFWD` sat under Johnson 2008 but
the same sequences are Mao's `FV3-54F`; `HahnF2` sits under Takehisa 2009.
Whenever a name encodes a person or a virus that is not the cited paper's, the
entry deserves a second look.

Most of this registry's entries were seeded from one primer list, which names
a primer alongside whoever supplied it rather than who designed it. So this is
a population-level risk, not one bad row.

What the classes mean
---------------------
name-vs-author   An oligo name contains a capitalised personal-looking token
                 that is not the cited first author. The Johnson signature.
                 Highest yield; also the noisiest, since plenty of names
                 legitimately encode a gene, strain or position.
modified         The name says mod/new/corrected/variant, so the stored
                 sequence may not be the published one. With a DOI attached
                 this is worse than the Johnson case: the citation asserts a
                 sequence the paper never printed.
lab-designed     A `TS...` prefix, the seed list's convention for oligos made
                 or altered in-house. Fine when no DOI claims otherwise.
unestablished    citation.oligos_designed_here is still null. Not a defect,
                 a to-do: it is the honest default.
no-citation      No reference and no DOI. Cannot be scope-checked at all, and
                 cannot be validated against the literature.
id-mismatch      The id's trailing Author_Year disagrees with the citation.
                 Usually a bad id rather than a bad citation, but it is how the
                 `Lancotti`/`Lanciotti` typo surfaced.

This proposes and never edits. Resolving a row means reading the paper.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from assaywatch.validate import iter_files, load_assay  # noqa: E402

# Name fragments saying the stored sequence may differ from the printed one.
MODIFIED = re.compile(r"(?:\b|_|-)(mod|modified|new|corrected|variant|same)(?:\b|_|-)|-MOD\b|\bMOD-", re.I)
# The seed list's prefix for in-house oligos.
LAB_PREFIX = re.compile(r"^TS[-\s]?[A-Za-z0-9]")
# A reference that names no paper.
NO_PAPER = re.compile(r"^\s*(developed|predict|unpublished|in[-\s]house|\?)", re.I)
# A capitalised token inside an oligo name that looks like a surname: four or
# more letters, initial capital, not an all-caps acronym and not a known
# non-personal word. Deliberately loose; the output is a reading list.
PERSONISH = re.compile(r"\b([A-Z][a-z]{3,})\b")
# Words that look like surnames to the regex but are not. Stored as one string
# so the formatter leaves it alone and it stays readable.
#
# The last line is confirmed false positives from the first run, 2026-10-04:
# `Fouter`/`Router` are "F-outer" and "R-outer" run together, `Pythin` is a typo
# for Python, `Matrix` is the influenza gene. A regex loose enough to catch
# `Hahn` and `Rebelo` is worth a handful of names on a list like this.
NOT_A_SURNAME = frozenset(
    """
    Probe Forward Reverse Outer Inner Fwd Rvs Sense Antisense Gene Hemi Short Long
    Group Parapox Corrected Mod New Same Rev Primer Round Borna Helico Myco Pox Nido
    Python Sunshine Chytr Alpha Astr Cac Term Filo Flavi Phlebo Hanta Morb Rana Lepto
    Ento Furonis Ferlaq Dependovirus
    Fouter Router Matrix Pythin Nodo
    """.split()
)


def surname_of(ref: str) -> str | None:
    """First author's surname from a free-text reference, if one can be read."""
    m = re.match(r"\s*([A-Z][A-Za-z'\-]+)", ref or "")
    return m.group(1) if m else None


def oligos_of(assay) -> list:
    """Every oligo on an assay, including probe and pool members."""
    out = []
    for slot in ("forward", "reverse", "probe"):
        o = getattr(assay.oligos, slot, None)
        if o is not None:
            out.append(o)
    out.extend(assay.oligos.alternates or [])
    return out


def audit(path: Path) -> list[dict]:
    """Every provenance flag for one entry. Several classes can fire at once."""
    a = load_assay(path)
    c, src = a.citation, a.source
    ref = (c.reference or "") or (c.as_written or "")
    author = surname_of(ref)
    names = [o.name or "" for o in oligos_of(a)]
    rows: list[dict] = []

    def add(cls, detail):
        rows.append(
            {
                "assay_id": a.id,
                "class": cls,
                "detail": detail,
                "doi": c.doi or "",
                "cited_author": author or "",
                "design_year": c.design_year or "",
                "designed_here": "" if c.oligos_designed_here is None else str(c.oligos_designed_here),
                "read_from": "predict" if src.predict_protocol else "",
                "oligo_names": "|".join(n for n in names if n),
            }
        )

    # The Johnson signature: a surname-shaped token in a name that is not the cited author.
    for n in names:
        for tok in PERSONISH.findall(n):
            if tok in NOT_A_SURNAME:
                continue
            if author and tok.lower()[:4] == author.lower()[:4]:
                continue  # name agrees with the citation, which is reassuring
            add("name-vs-author", f"oligo '{n}' contains '{tok}'; citation names {author or 'nobody'}")

    mod = [n for n in names if MODIFIED.search(n)]
    if mod:
        add("modified", f"{'; '.join(mod)}" + ("  [and a DOI is attached]" if c.doi else ""))

    if any(LAB_PREFIX.match(n) for n in names):
        add("lab-designed", "TS prefix: made or altered in-house per the seed list")

    if not ref.strip() or NO_PAPER.match(ref):
        add("no-citation", (ref.strip() or "(empty)")[:60])

    if c.oligos_designed_here is None and c.doi:
        add("unestablished", "citation.oligos_designed_here is null but a DOI is attached")

    im = re.search(r"_([A-Z][a-z]+)_((?:19|20)\d\d)$", a.id)
    if im:
        ida, idy = im.group(1), int(im.group(2))
        if author and ida.lower()[:5] != author.lower()[:5]:
            add("id-mismatch", f"id says {ida} {idy}; citation says {author} {c.design_year}")
        elif c.design_year and idy != c.design_year:
            add("id-mismatch", f"id says {idy}; design_year is {c.design_year}")
    return rows


COLS = [
    "assay_id",
    "class",
    "detail",
    "doi",
    "cited_author",
    "design_year",
    "designed_here",
    "read_from",
    "oligo_names",
]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--class", dest="only", help="show one class only")
    ap.add_argument("--tsv", type=Path, help="write all rows here")
    ap.add_argument("--verbose", action="store_true", help="print every row, not just the counts")
    args = ap.parse_args(argv)

    rows: list[dict] = []
    n = 0
    for path in iter_files(args.registry):
        n += 1
        rows.extend(audit(path))
    if args.only:
        rows = [r for r in rows if r["class"] == args.only]

    order = ["name-vs-author", "modified", "no-citation", "id-mismatch", "lab-designed", "unestablished"]
    counts = {k: sum(1 for r in rows if r["class"] == k) for k in order}
    print(f"{n} entries audited\n")
    for k in order:
        if counts[k]:
            print(f"  {counts[k]:3d}  {k}")
    flagged = {r["assay_id"] for r in rows}
    print(f"\n  {len(flagged)} of {n} entries carry at least one flag")

    if args.verbose or args.only:
        for k in order:
            sel = [r for r in rows if r["class"] == k]
            if not sel:
                continue
            print(f"\n### {k} ({len(sel)})")
            for r in sel:
                print(f"  {r['assay_id'][:52]:52s} {r['detail'][:88]}")

    if args.tsv:
        args.tsv.parent.mkdir(parents=True, exist_ok=True)
        with args.tsv.open("w", newline="") as fh:
            w = csv.DictWriter(fh, COLS, delimiter="\t")
            w.writeheader()
            w.writerows(rows)
        print(f"\nwrote {len(rows)} rows to {args.tsv}")

    print(
        "\nNothing was edited. A row is a reading assignment: find the design paper, "
        "then set citation.oligos_designed_here and record the reasoning in "
        "source.notes_curator.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
