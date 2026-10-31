# Four influenza entries prepared, held-out set 3 opened, and one entry blocked by a rule that has never had to express this

2026-10-30, following the maintainer's four decisions on the two strict-bar drift cases.
Three of the four assays are curated, verified and waiting in `pending/`; the fourth is
blocked on a single call that no existing entry has ever needed. Nothing was promoted to
`registry/`: entering an assay affects published results and goes through review.

## What was decided, and what it was for

Both held-out sets are spent and neither demonstrates drift. Of the three rows in the whole
corpus carrying `mechanism: drift`, none meets the strict bar of 2026-10-30, and two are one
inferred event. So the tool's premise — temporal decay at primer sites — is untested. Two
papers found on 2026-10-30 clear that bar, and neither concerned a registry assay
(`docs/journal/2026-10-30-two-strict-bar-drift-cases.md`). The decisions were: prepare all
four assays (each decayed assay with its documented fix), enter the CDC H3 assay citing Shu
2026 rather than widening the Crossref rule, stop in `pending/` for sign-off, and open a
scored set 3.

## The four entries

| entry | cites | amplicon measured | published | DOI verified |
|---|---|---|---|---|
| `INFLUENZA_A_M1_Ward_2004` | Ward 2004 | **95 bp** | 104 bp | yes |
| `INFLUENZA_A_M1_Yang_2014` | Yang 2014 | **95 bp** | — | yes |
| `INFLUENZA_A_HA_H3_CDC_Shu_2026` | Shu 2026 | **147 bp** | 906-1052 | **NO, blocked** |
| `INFLUENZA_A_HA_H3_v2_Shu_2026` | Shu 2026 | **103 bp** | 906-1008 | yes |

Ward and Yang share the existing matrix retrieval group (`q2ebd5918b3`), so they add no
fetch. The two H3 entries open one new group (`q2fad34153e`), which has never been fetched.

## Ward 2004: the paper prints what it was said to print, and the size is wrong by 9 bp

All three oligos read `exact` against the open-access copy. One process note worth keeping:
a first regex pass over the PMC XML found **no sequences at all**, because the paper prints
them in spaced triplets (`5'AAG ACC AAT CCT GTC ACC TCT GA 3'`). A sequence-shaped search
that assumes contiguous bases will silently miss a 2004 methods section.

**The amplicon measures 95 bp, not the published 104.** `curate` measured it over the whole
archive: **183,773 of 183,777 products**, unimodal. The registry takes the measured value
and discloses the difference, which is what `amplicon_disagrees_with_paper` now records.

The design paper states this project's thesis in its own discussion: "This highlights the
need for regular reviews of any primer or probe sequences used diagnostically or for
quantification of viruses that are subject to genetic drift."

Two things seen and deliberately left: the paper's influenza B assay (`senseB`/`antisenseB`
and a VIC probe), which is a different target taxon and a separate curation; and any
suggestion that this duplicates `INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003`
(Spackman 2002), which it does not — different design paper, no shared sequence, different
region, MGB rather than FAM/TAMRA.

## Yang 2014: a degenerate relaxation, plus one real substitution, and an orientation note

Yang's "At" assay is Ward's with degenerate bases added; the paper says so. Position by
position, in the functional orientation:

| oligo | change |
|---|---|
| forward | pos10 C→Y, pos11 C→Y, pos20 C→Y — all widenings |
| reverse | **pos1 C→T, a fixed-base substitution**, then pos11 A→R, pos14 C→Y |
| probe | pos6 G→N |

So it is not purely a widening, and `oligos_designed_here` is false with `oligos_modified`
flagged. The 5'-terminal substitution is close to free for amplification, but it is a
substitution and the entry says so rather than calling the assay a relaxation.

**The reverse primer is stored reverse-complemented from the paper, and this is the routine
case, not a correction.** Yang prints `GGACTGCARCGYAGACGCTTTA`, which binds the *plus*
strand; its reverse complement binds the minus strand at exactly the site Ward's
`antisenseA` occupies (216-238). `printed.py`'s own verifier reads the stored form as
`revcomp` and prints "listed as its reverse complement, which is normal for a reverse
primer", so the project already treats this as ordinary. Ward happens to print the other
convention, which is the only reason it is worth a note.

It is worth a note because it is not cosmetic: the scorer's 3' window carries a penalty of
3.0 against 0.5 at the 5' end, so storing the mirrored oligo would mis-price every mismatch
in it — and on a drift case, where the question is *which positions* changed, that is the
whole measurement.

`curate` could not fetch this paper (PMC3911422 carries no full text; neither the Unpaywall
nor the OpenAlex link served a PDF), so its oligo step was skipped and the check was run
directly against the held PDF: forward `exact`, probe `exact`, reverse `revcomp`.

## The CDC H3 pair, and the one call that blocks half of it

Both read their oligos from Shu 2026 Table 1. Both reverse primers' Table 1 positions run
descending (1052-1030, 1008-988), which is already the minus-strand reading, and every
reverse site found on real records was on the minus strand — so their printed orientation is
functional and nothing is inferred.

**`INFLUENZA_A_HA_H3_CDC_Shu_2026` cannot be verified, and `curate` is right to refuse it.**
`papers.citation_matches` requires Crossref's year to be within one of `design_year`. This
entry's assay was designed in 2008 (FDA 510(k) K080570) and its citation published in 2026,
18 years apart, because the maintainer's ruling was to cite the paper that prints the oligos
rather than admit a regulatory document. **A check of all 214 live entries found no
precedent: not one has a `design_year` more than a year from its DOI's year.** The rule has
never had to express this and does not.

The two citation checks disagree about it, which is worth recording on its own:
`citation_problems`, which CI runs, **passes** this entry, because it also reads years out
of the reference text, where 2026 appears. Only `citation_matches`, which gates
`doi_verified`, refuses. One rule, two implementations, different answers.

The three ways out are a maintainer's call:

1. Set `design_year: 2026`. False, and it would corrupt the five-year clock that
   `find_retrospective_cases.py`'s `late_redesign` family runs on `citation.design_year`.
2. Teach `citation_matches` to accept a year from the reference text, as
   `citation_problems` already does. This is the principled fix and it also removes the
   disagreement above — but it changes how **any** entry becomes verified, which is not a
   curator's change to make mid-session.
3. Leave the assay out, in which case Shu 2026's drift case has nowhere to land.

**Resolved later the same day**: the maintainer took option 2, and
`docs/journal/2026-10-30-citation-year-rule.md` records the change and the before/after count
over every entry (220 compared, 0 verdicts moved). All four entries now verify and set 3 has
both drift rows, so the withheld row below has landed.

Nothing was guessed and the entry waited. `INFLUENZA_A_HA_H3_v2_Shu_2026` passed cleanly,
because Shu 2026 did design it, so its `design_year` *is* the citing paper's year.

This is not a new kind of citation, only a new size of gap: `CDV_N_gene_Elia_2006`,
`CMV_UL55_gB_Deckers_2009` and `TILV_ssRNA_segment3_ME1_ME2_Kembou_2017` already cite the
paper that prints their oligos rather than the one that designed them.

## Two curate warnings that are artifacts, measured rather than assumed

**`amplify` failed on both H3 entries** with every oligo 7-8 mismatches off. Their own
retrieval group has never been fetched, so `curate.archives_for` fell back to
`q2ebd5918b3` — the **segment 7 (matrix)** archive. H3 hemagglutinin primers finding nothing
in matrix records is the right answer to the wrong question. Measured against 3,000 real
H3N2 HA records fetched for the purpose:

| | both primers ≤2 mm | probe | amplicon |
|---|---|---|---|
| H3 (v1) | 2,940 / 3,000 | 2,692 | **147 bp, unimodal** |
| H3_v2 | 2,963 / 3,000 | 2,763 | **103 bp, unimodal** |

The warning clears itself the first time a run fetches the group.

**Both H3 probes read `absent` against the PDF**, and that is a notation limitation, not a
transcription doubt. Table 1 writes the internal quencher inside the sequence
(`CAG GAT CAC /ZEN/ATA TGG GSC CTG TCC CAG`), so `printed_oligos` never sees the 27 bases as
one run: it finds the 18-base tail and loses the 9-base head below its minimum length. Both
primers of both assays read `exact`. This will recur as double-quenched probes become
common, and it is now on the roadmap.

## Held-out set 3, opened with one row and one withheld

`docs/validation-cases-heldout-3.tsv`, sharing the header all three other case files share.

The row: `INFLUENZA_A_M1_Ward_2004`, `as_of` 2013-09-06, `expect` **fails**, `mechanism`
**drift**, `scope_taxid` **114727** (H1N1 subtype). The `as_of` date is Yang's *received*
date, which is the strictest honest statement of what its authors could have seen.

Yang names Ward as its reference 15 and as "Aw1 in this study" in the Discussion, which is
what ties the row to the entry; the paper's three reference assays are easy to confuse and
this was checked in the text rather than assumed. The evidence that clears the strict bar:
G238A in 11-12 A(H1N1)pdm09 isolates in 2010-2011, joining C154T, G225A and T228C through
2012-2013, located by the Fig. 2 alignments in the primer-binding regions, with 6 of 40
specimens negative by Aw1 and positive by the redesign and Ct shortening 3.1-14.25 cycles.

**The set is not yet scored, for a mechanical reason**: its row names an entry in `pending/`,
and a pending entry is never screened, so no calls table can contain it. It is scored when
the entry is promoted and a screen covers it.

**It is also the first genuine test of the scoped matrix.** `scope_taxid` was built on
2026-10-30 and chosen after set 2 had been read, so on set 2 it can only be a
re-description. Here the scope was filled from the source paper before any verdict existed.

The Shu 2026 row was withheld pending the citation call above, and **landed the same day** once it was taken. As written:

    INFLUENZA_A_HA_H3_CDC_Shu_2026	2026-10-29	fails	drift	10.1128/jcm.00727-26 Shu 2026 J Clin Microbiol: the FDA-cleared CDC A(H3) component losing sensitivity to reverse-primer mismatches accumulating in one lineage over time -- A21G with T23G/T23C/T23A, the 3C.2a1b.2a clade emerging in 2020 and the mutation reaching 96% of globally circulating viruses by the end of 2021 (GISAID 2020-2023), with a measurable Ct shift between H3 and the H3_v2 redesign and both oligo sets printed in Table 1. 30 of 60 non-subclade-K 2022 specimens carried A21G; 19 of 19 subclade K 2025 specimens carried A21G plus a second mismatch. Redesign entered as INFLUENZA_A_HA_H3_v2_Shu_2026	119210

## Gate

`ruff check` and `ruff format --check` clean over 345 files; `assaywatch validate registry`
214 valid, 0 problems; `assaywatch validate pending --pending` 14 valid, 0 problems;
`check_citations.py` 214 checked, 0 problems. `pytest -m slow` was not run: nothing here
touches the Snakefile or a hashed `config.yaml` section.

## What is owed

- The maintainer's sign-off on three entries, and the citation call on the fourth.
- Promotion, a screen of the new assays, and set 3's score. The H3 group needs a fetch
  first; Ward and Yang do not.
