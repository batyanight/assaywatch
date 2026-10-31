# Repo-wide audit for fabricated or unverifiable content

2026-10-05. Prompted by a real failure: I wrote a reference into three new
entries from memory, recording doi:10.3390/v13071358 as *Nobach et al.* when
Crossref gives **Sigrist, Geers, Albini, Rubbenstroth & Wolfrum**. It was caught
only because the DOI happened to be checked afterwards. That is luck, and luck
does not scale to 164 entries. This is the audit that followed, plus the gates
that now make it a build failure rather than a hope.

## What was checked, and what was found

| check | scope | result |
|---|---|---|
| registry citations vs Crossref | 119 entries with a resolvable DOI | **1 real problem**, since fixed |
| validation-case claims vs Crossref | 49 rows, 47 naming an author | **0 mismatches**, 0 dead DOIs |
| every DOI cited in docs | 197 distinct | **0 fail to resolve** |
| registry taxids vs NCBI | 69 distinct taxids | **0 invalid**; 23 carried superseded names |
| oligos vs their own papers | 384 oligos | 87 confirmed, 173 checkable |

**No fabricated citation existed in the registry before today.** The single
fabrication was mine and never reached a commit.

### The one real citation problem

`Snake_arenavirus_..._Nachweis_2015` had a reference naming **no author at
all** - just `Tierärztl Prax Ausg K 2015;43:239-247`. Crossref gives Aqrawi,
Stöhr, Knauf-Witzens, Krengel, Heckers & Marschang. Now complete. The id's
"Nachweis" is not a surname but the first word of the German title, which is how
the id was generated; it is left alone to avoid breaking references, with a note.

### Eight false alarms worth recording

My first checker flagged 9. Eight were its own fault: four diacritic
differences (`Vazquez-Moron` vs `Vázquez-Morón`, `Sanchez-Seco` vs
`Sánchez‐Seco` with a non-breaking hyphen) and four year-formatting cases where
online-first and issue publication straddle two years. Both are now handled -
accents folded, dashes normalised, a one-year tolerance - because **a check that
cries wolf gets switched off**, and a switched-off check is worse than none.

### Taxon renames, not errors

23 entries carried taxon names NCBI has superseded: Herpesviridae →
Orthoherpesviridae, Flavivirus → Orthoflavivirus, Canine morbillivirus →
Morbillivirus canis, Nipah henipavirus → Henipavirus nipahense, Tilapia
tilapinevirus → Tilapinevirus tilapiae. **Every taxid was valid** - only the
names had moved. All now carry both names, so a search on either finds the
assay, and the master sheet marks the disagreement explicitly rather than
silently resolving it.

## The gates now in place

- **`scripts/check_citations.py`** - fails if any reference disagrees with
  Crossref on first author or year. In pre-commit and CI, running against the
  committed Crossref cache so it needs no network. It deliberately does not try
  to match whole reference strings: journal and author-list conventions vary too
  much for that to mean anything, while first author and year are cheap to
  verify and catastrophic to invent.
- **`scripts/verify_oligos_against_paper.py`** - the same idea for sequences.
- **`docs/papers-index.cache.json`** - committed, so a DOI that starts resolving
  to a *different* paper shows up as a diff rather than silently.

## What remains unverifiable, stated plainly

This is the honest part of the audit and it is not small.

- **106 oligos sit in 45 entries with no DOI at all.** Mostly honest "in-house,
  unpublished" lab assays. They cannot be checked against a source,
  now or ever, unless provenance is recovered.
- **105 oligos are in papers behind paywalls**, listed in
  `docs/journal/2026-10-05-papers-needed.md`.
- **65 are `absent`**: the paper is in hand but the sequence was not found in
  it. Usually an image-only primer table or a supplement; sometimes a sign the
  oligos come from a different paper than the one cited.
- **18 are `in-text`**: present in the paper but not inside a listed oligo, so
  possibly matched against the printed target gene rather than a primer table.

So **87 of 384 oligos are confirmed against their own paper**, and 173 are
checkable at all. The rest are an honest backlog, not a claim.

## What this does not cover

Prose. The numbers in these documents are re-derivable from the TSVs in
`results/` and were re-derived while writing this, but there is no automated
check that a sentence in a Markdown file is true. The defence there is that
every quantitative claim names the file it came from.
