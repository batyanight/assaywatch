"""The `papers/` filename convention, in the one direction that is well defined.

A paper on disk is named after its DOI with the characters a filename cannot
hold replaced by underscores, lowercased:

    10.1016/S0166-0934(96)02155-6   ->   10.1016_s0166-0934_96_02155-6.pdf

Going that way is exact. Coming back is not, because three different characters
map onto `_`, and five call sites tried anyway with `stem.replace("_", "/")`:

- `verify_oligos_against_paper.index_papers` indexed such a paper under
  `10.1016/0890-8508/92/90002-f`, which still matches a DOI pattern, so the file
  was filed under a DOI nothing asks for AND counted as "named", which barred it
  from the surname-and-year fallback. Twenty registry entries read
  `no-full-text`, "no local PDF", against papers that were on disk. Fixed
  2026-10-20; measured in isolation, 38 oligos moved off `no-full-text`, 8 of
  them onto a discrepancy verdict, three of those genuine.
- `find_open_access.needed_dois` built its "already held" set the same way and
  so reported 10 of 26 missing papers as missing while they sat in `papers/`.
  That list is what `results/nyu-fetch-list.tsv` is built from.
- `papers_index`, `extract_candidate_oligos` and `import_pmc_fulltext` each had
  their own copy.

So nothing reverse-maps any more. A caller with a DOI forward-maps it and looks
for that name; a caller holding only a filename treats the stem as an opaque
key, never as a DOI.

MEASURED over the registry, 2026-10-20: 187 DOIs, 104 distinct, and the only
characters outside `[A-Za-z0-9.-/]` are `(` and `)`, 20 of each. No DOI contains
an underscore and no two DOIs share a stem, so the map is injective on the real
data. `<` and `>` are replaced too, for the old Wiley SICI DOIs that
`import_pmc_fulltext` warned about, though none is in the registry today.
"""

from __future__ import annotations

import re
from pathlib import Path

# `/` always; `(` and `)` because the registry has 40 of them; `<` and `>`
# against SICI DOIs. Anything else a DOI may legally hold is filename-safe.
UNSAFE_IN_FILENAME = re.compile(r"[/()<>]")


def doi_stem(doi: str) -> str:
    """The `papers/` filename stem for a DOI: lowercased, unsafe characters as `_`.

    Lowercasing is not cosmetic. PMC echoes a DOI in the publisher's casing, so
    the same paper arrives as `10.1128/JCM.00192-08` and is stored in the
    registry as `10.1128/jcm.00192-08`; 60 of the registry's 187 DOIs are not
    already lower case.
    """
    return UNSAFE_IN_FILENAME.sub("_", doi.strip().lower())


def paper_for_doi(doi: str, paper_dir: Path, suffixes: tuple[str, ...] = ()) -> Path | None:
    """The file in `paper_dir` named after this DOI, or None.

    `suffixes` restricts the search (`(".pdf",)` for a PDF-only caller); empty
    means any extension. Compares stems rather than globbing a pattern, because
    a DOI stem contains `.` and would otherwise need escaping.
    """
    if not doi:
        return None
    want = doi_stem(doi)
    for p in sorted(paper_dir.glob("*")) if paper_dir.is_dir() else []:
        if p.stem.lower() == want and (not suffixes or p.suffix.lower() in suffixes):
            return p
    return None


def held_dois(dois: list[str] | set[str], paper_dir: Path) -> set[str]:
    """The subset of `dois` (lowercased) whose paper is in `paper_dir`.

    Forward-mapped, so the answer does not depend on recovering a DOI from a
    filename. Reads the directory once rather than per DOI.
    """
    stems = {p.stem.lower() for p in paper_dir.glob("*")} if paper_dir.is_dir() else set()
    return {d.strip().lower() for d in dois if doi_stem(d) in stems}


# After mapping, a stem should hold only these. Anything else either cannot be
# written portably (`:` on Windows, from the old SICI DOIs) or has no business in
# a filename (`%`, `;`).
SAFE_STEM = re.compile(r"^[a-z0-9._-]+$")


def unstorable_reason(doi: str) -> str | None:
    """Why this DOI cannot be stored under the papers/ convention, or None.

    Reversibility used to be the test: `import_pmc_fulltext` asked whether
    turning every `_` back into `/` returned the DOI, because readers inferred a
    DOI from a filename. None does now, so the question is no longer "can it be
    read back" but "does the name identify it, and can it be written".

    Two ways it cannot:

    - The stem is ambiguous. A DOI holding `_` maps to the same stem as one
      holding `/` or `(` in that position, so the name no longer names one paper.
      No registry DOI contains `_` (checked over all 187 on 2026-10-20), so this
      refuses a hypothetical rather than anything in hand.
    - The stem holds a character that does not belong in a filename: `%`, `;`,
      or the `:` of a SICI DOI such as
      `10.1002/(SICI)1096-9071(199908)58:4<363::AID-JMV7>3.0.CO;2-2`.
    """
    if not doi or not doi.strip():
        return "empty DOI"
    if "_" in doi:
        return (
            "contains an underscore, which the filename convention also produces, "
            "so the stem would be ambiguous"
        )
    stem = doi_stem(doi)
    if not SAFE_STEM.fullmatch(stem):
        bad = sorted({c for c in stem if not SAFE_STEM.fullmatch(c)})
        return f"maps to a stem holding {''.join(bad)!r}, which does not belong in a filename"
    return None


# A supplement held beside its article: `<doi stem>.supp.<ext>`. Both readers
# that identify a file by its name have to agree on this marker. When only
# `papers_index` knew it, `verify_oligos_against_paper` read the stem whole:
# `10.1371_journal.pone.0207365.supp` still matches a DOI pattern, so the
# supplement was filed under a DOI nothing cites, and three Hermes entries kept
# reading `no-oligos` against a table that was on disk.
SUPPLEMENT_SUFFIX = ".supp"


def identity_stem(path: Path) -> str:
    """The stem that says WHICH paper a file belongs to, `.supp` marker removed.

    A supplement is not a different paper, so it answers to its article's stem.
    Which of the two is held is a separate question, answered by the real
    filename (`papers_index` prints it as `suppl`).
    """
    stem = path.stem
    if stem.lower().endswith(SUPPLEMENT_SUFFIX):
        stem = stem[: -len(SUPPLEMENT_SUFFIX)]
    return stem
