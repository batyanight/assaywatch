# 2026-10-22 — the supplement convention reached the verifier; three citations resolved

Prompted by a batch of PDFs fetched into `~/Downloads` in the hour before this
session. Most were duplicates of papers already in `papers/`; six were new, and
two of those were supplementary files, which is what exposed the bug below.

## The bug: only one of the two readers knew what `.supp` means

`papers_index.py` has known since 2026-10-21 that a file named
`<doi stem>.supp.<ext>` is a supplement belonging to `<doi>`.
`verify_oligos_against_paper.py` did not. It read the stem whole, and
`10.1371_journal.pone.0207365.supp` still matches a DOI pattern, so the file was
indexed under a DOI nothing cites — and, being "named", it was also barred from
the surname-and-year fallback. A supplement could therefore sit in `papers/`
holding exactly the primer table an entry needed while that entry went on
reading `no-oligos`.

`SUPPLEMENT_SUFFIX` and a new `identity_stem()` now live in
`assaywatch/papers.py`, which is where the filename convention is already
documented, and both scripts read them from there. Precedence needed no change:
article and supplement both claim the DOI as *named* files, and the existing
rule — between two named claims, more oligos wins — picks the supplement
exactly when it is the one printing the sequences.

Measured: **15 oligos across 4 entries moved from `no-oligos` to `exact`** (the
three Hermes 2018 mycobacterial assays, 9 oligos, against the PLoS One S1 Table;
POXVIRUSES Polymerase short_2, 6 oligos, against the McAloose 2016 Dis Aquat Org
supplement). Seven `supplement` rows left `docs/materials-needed.tsv`.

## Three citations resolved, each confirmed by sequence before it was entered

| entry | now cites | how it was confirmed |
|---|---|---|
| `CDV_H_gene_Mueller_2011_1..4` | 10.7589/0090-3558-47.3.725 | the old reference string already named this paper as a *candidate*; all four primer pairs verify exact against the PDF, so the candidate is now evidence |
| `Nipah_N_gene` | 10.1016/j.jviromet.2006.11.023 | NP1F/NP1R exact in Wacharapluesadee & Hemachudha 2007, which names them the first round of a duplex nested RT-PCR with NP2F/NP2R — the sibling entry's pair — as the nested round |
| `Entamoeba_18S_small_subunit_SSU` | 10.1638/2020-0148 | EntF/EntR exact in McFarland 2021, so this is the publication of the seed list's unpublished assay |

All three were paywalled, which is why `find_open_access.py` and the Europe PMC
route never found them; `Nipah_N_gene` carried an explicit NO SOURCE FOUND note
recording a search of *open* full text, and that note is now answered rather
than deleted.

`Entamoeba`'s `design_year` is deliberately **still null**. The assay is in the
2018 spreadsheet, so it was designed on or before 2018 and the 2021 publication
year is not its design year; the paper gives no design date. That `year` row
stays open, now with a DOI beside it.

13 rows left `docs/materials-needed.tsv` in total (7 supplement, 5 citation, 1
lab-record).

## What the new PDFs did NOT settle

- **Sigrist 2021 (the three `ORTHOBORNAVIRUS_XP_*` entries).** The supplement is
  now read, and it does carry the primer table (Table S4) — but none of the
  three entries' oligos is in it. One is suggestive rather than silent:
  `BornaPCA6` sits 1 edit from the printed `PaBVcon_1401+`
  (`AAGAAGAAYCCYTCCATGATCTC`) aligned end to end. Table S5 also prints a probe
  called `BornaA_A674N` where the registry has `BornaA_A647N`, which reads like a
  transposition in one of the two. These entries are flagged
  `oligos_read_from_figure`, so `materials_needed` keeps them in the `figure`
  bucket rather than `supplement`, and the near match is in
  `results/oligo-verification.tsv`. **Wants a maintainer's read**: whether these
  are Table S4's assays under other names, and in which direction.
- **Enterovirus 5'UTR-VP4/VP2 (`_round1`, `_round2`).** Coiras et al. 2004
  (10.1002/jmv.20008) is a strong provenance candidate — `EVRV1` is exact
  against its `1-EV/RV` — but it is not entered, because the other three oligos
  disagree: the paper's `2-EV/RV` is `TCIGGIARYTTCCASYACCAICC` against the
  stored `TCIGGIARYTTCCACCACCAICC`, its `3-EV/RV` is `ACCRASTACTTTGGGTRWCCGTG`
  against the stored `ACCRASTACTTTGGGTGTCCGTG` (both stored forms are the
  printed one with degeneracies collapsed), the stored `EVRV2a-new` is in the
  paper at all, and the paper's own products are 755/226 bp against the stored
  765/660. A modified descendant, not this assay. The PDF is held for whoever
  takes that up.
- **Figure-bucket entries** (Boyle 2004, Long 1993, Martín-Hernández 2007,
  Ghosh 2021). The fetched copies are text-identical to the ones already held or
  yield the same sequences; the gap there was never the text layer.

## Held but cited by nothing yet

`papers_index --check` prints `3 PDF(s) ... match no DOI in the registry or the
cache` and exits 0. Those three are the candidate-provenance papers filed by
this session: Coiras 2004 (above), Aitichou 2005 (10.1016/j.jviromet.2004.10.004,
hantavirus one-step rRT-PCR) and Khodeir 2021 (10.21608/javs.2021.84062.1088,
Egyptian CDV/CPV isolates; prints `CDVF4`/`CDVR3`/the probe of
`CDV_P_gene_Scagliarini_2007` exactly). They are candidates, not dependencies,
so none was added to `SHARED_SOURCES` — that set is for sources entries actually
rest on.

Also fetched and NOT filed, because nothing in the registry touches them: Yu
2006 Nipah serodiagnosis (10.1128/JCM.00693-06) and Hepp 2026, a broadly
reactive New World hantavirus rRT-PCR (10.1016/j.jcv.2026.105989) — the latter
is 2026 and is a candidate for `scan_literature.py`'s new-assay list.

## Gate

1481 tests (3 new), validator 208/208, `check_citations --refresh` 198 checked /
0 problems, ruff clean on every file touched here.
