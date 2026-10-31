# The two citation checks gave one question two answers, and the stricter one was blocking a real entry

2026-10-30, after `docs/journal/2026-10-30-influenza-drift-entries.md`. The maintainer's call
was the second of the three options recorded there: teach `citation_matches` to read a year
from the reference text, as `citation_problems` already did. This is the record of the change
and of the measurement taken before it shipped.

## What was wrong

Two functions in `assaywatch/papers.py` implemented the same rule — "the entry's year agrees
with Crossref's" — and disagreed:

| | reads `design_year` | reads years in the reference text | gates |
|---|---|---|---|
| `citation_matches` | yes | **no** | `doi_verified`, via `curate` and `resolve_citations` |
| `citation_problems` | yes | yes | the CI check, `scripts/check_citations.py` |

So an entry could pass CI and be refused verification. That is exactly what happened to
`INFLUENZA_A_HA_H3_CDC_Shu_2026`: `check_citations.py` was content, `curate` printed
`FAIL citation`, and the entry could not leave `pending/`.

The disagreement had never surfaced because it cannot surface on an entry whose citation *is*
its design paper. **Of all 214 live entries, not one has a `design_year` more than a year from
its DOI's year.** The CDC H3 subtyping assay is the first: designed in 2008 under FDA 510(k)
K080570, which carries no Crossref DOI, and cited to the 2026 paper that prints its oligos.

## What changed

One rule, one implementation. `papers.year_agrees(crossref_year, design_year, reference)` is
now the only year rule, and both functions call it. The years an entry *offers* are its
`design_year` and any four-digit year in its reference text, because those are two different
claims: `design_year` is when the assay was designed, the reference text names the paper being
cited.

Three behaviours are preserved deliberately and each has a test:

- **Within one year**, because online-first publication straddles two.
- **An entry that offers no year at all is not refused for it.** The rule reports a
  contradiction, not an absence.
- **A reference whose years all disagree is still refused.** The rule is loosened, not removed.

## The cost, stated rather than buried

This adopts the looser of the two rules. A reference text can carry a four-digit number that
is not the paper's year — a volume, a clade name like `1990.1`, an accession — and reading
years out of it can therefore satisfy the check by accident. That looseness was already in CI,
on every entry, since `citation_problems` has always read the reference text. Having the gate
that sets `doi_verified` disagree with the gate CI runs was the worse defect, because it gave
two answers to one question and the stricter one was wrong about a real entry.

What did **not** change: a DOI still becomes `doi_verified` only when Crossref resolves it and
names the entry's first author. An FDA 510(k) is still not a citable source. The entry that
needed this records in its own notes that its citation is not its design source, and carries
`citation_is_indirect` and `oligos_from_secondary_source`.

## The measurement, taken before shipping

Old rule against new, over every entry on disk whose DOI is in
`docs/papers-index.cache.json`:

| | |
|---|---|
| entries compared | **220** (214 live, 6 pending with cached DOIs) |
| `citation_matches` verdicts that move | **0** |
| `citation_problems` year verdicts that move | **0** |
| entries with a `design_year`/DOI-year gap over 1 year | **0** |

So the change enables the new case and moves nothing already in the registry. The only four
entries not compared are the four added earlier the same day, whose DOIs the index has not yet
cached; `curate` resolves all four live against Crossref.

One process note: the first run of that comparison reported 65 uncached DOIs and was wrong.
`check_citations.py` lowercases a DOI before looking it up and the cache is keyed lowercase;
the measurement script was not. A measurement that finds a third of the registry missing
should be suspected before it is reported.

## End to end

`assaywatch curate pending/INFLUENZA_A_HA_H3_CDC_Shu_2026.yaml` now prints
`WROTE citation citation.doi_verified: true (Shu 2026: Update to the CDC influenza A(H3)
subtyping assay...)`. The flag was then **held false by hand**, as on the three sibling
entries, because `pending/` means not live whatever `status` says.

Its one remaining `curate` failure is the already-documented archive artifact: the H3
retrieval group has never been fetched, so `archives_for` falls back to the segment 7 archive
where H3 hemagglutinin primers correctly find nothing.

**Held-out set 3 now has both drift rows**, Yang 2014 against the Ward matrix assay and Shu
2026 against the CDC H3 assay, `as_of` 2026-10-27 from Crossref's issued date. Neither is
scored yet, for the same mechanical reason as before: both name assays in `pending/`.

## Gate

`pytest` 1,814 passed (three new tests in `tests/test_papers_client.py`), validator 214/214
live and 14/14 pending, `ruff` clean, `check_citations.py` 214 checked 0 problems.

## Left

`scripts/resolve_citations.py` passes `citation.reference or ""` where `curate` and
`citation_problems` both fall back to `as_written`. So an entry whose year lives only in
`as_written` is judged differently depending on which tool asks. Not touched here, because
changing it changes which entries that script will verify, and it wants its own measurement.
