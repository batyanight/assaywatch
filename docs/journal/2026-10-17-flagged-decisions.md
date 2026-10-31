# Flagged decisions settled, 2026-10-17 (bacteria group)

Four of the decisions left open by the 2026-10-06 agents, with the evidence each rests on.
The remaining six (Nosema bombi, DWV variant scope, Reptarenavirus, Ophidiomyces target-D,
Tasman-PCR, clade scoping for H5/H7/NP/avipox) are not covered here.

## 1. Chlamydia genus 16S round 1 — keep the printed primer

**Decision: keep the sequence exactly as printed. The flag was wrong and has been rewritten.**

The antisense primer is printed `TACCTGGTACGCTCAATT`; every real record reads `...CAAAT` at
the penultimate 3' base, a T:T mismatch. The entry previously flagged this as a likely typo
and the corrected form as a hypothesis.

A PMC full-text search settles it the other way. The printed form appears in two later
papers; the corrected form appears in none, and neither does either form of the sense-strand
site. Both hits are independent wet studies that obtained product:

| source | what it did |
|---|---|
| Iran J Microbiol 2021, [10.18502/ijm.v13i4.6972](https://doi.org/10.18502/ijm.v13i4.6972) (PMID 34557276) | 360 sheep and goat milk samples, 31 positive for *Chlamydia* spp., 31 of those on 16S. Prints this reverse primer, the forward `ACGGAATAATGACTTCGG`, and Messmer's 436/127 bp sizes. |
| Microorganisms 2021, [10.3390/microorganisms9050935](https://doi.org/10.3390/microorganisms9050935) (PMID 33925646) | A validated nested PCR that amplified *Chlamydia* DNA in 31% of sputum samples, confirmed by sequencing. PMC's index matches the primer string; the flattened full text drops the primer table, the table-loss already documented here. |

Three groups have run this oligo and got product, so a T:T mismatch one base in from the 3'
end is tolerated at the bench.

**What is actually wrong is the score, not the sequence.** The penalty table charges 3 on the
238 of 243 product-bearing records carrying only this mismatch, so no record can read
`detect` and the entry's coverage is capped at `reduced` for reasons unrelated to drift.
Whether a penultimate-3' mismatch of a demonstrably tolerated kind should cost that much is a
`config.yaml` question, **logged for the scoring calibration and not fixed off one case**.

Flag renamed `ANTISENSE_PRINTED_T_WHERE_ALL_RECORDS_HAVE_A_AT_PENULTIMATE_3PRIME_BASE` ->
`ANTISENSE_PENULTIMATE_3PRIME_MISMATCH_VS_ALL_RECORDS_BUT_FORM_CORROBORATED_BY_TWO_LATER_STUDIES`,
because the old wording invited exactly the correction the literature does not support.

**Provenance lead, not run down:** the Iranian paper attributes its 16S primers to *Creelan et
al.*, not Messmer. If an earlier source prints them, this entry's citation may need to move.

## 2. C. trachomatis serovar polymorphism — accept it as a true finding

**Decision: change nothing. The reduced detection is the finding.**

The inner pair is exact on LGV and some genital genomes and carries two forward-site
mismatches in many others: of 42 genomes all give a product but 11 fail with both sites
different (A/363, D/UW-3/CX, G/SotonG1 among them), and detection is 43% across the 72
records that span the site. Verified as a real sequence polymorphism, not a scoring artefact
— both rrn operons of D/UW-3/CX carry the variant and neither carries the primer form.

A published assay that underdetects part of its target population is precisely what this tool
exists to surface. Narrowing the scope to the serovars that work would define the failure out
of existence by redefining the denominator. The pooled figure does mix working and failing
serovars, which reads as mediocre coverage rather than a clean split — that is the estimand
problem, and it is not fixable in this entry.

## 3. C. psittaci / C. abortus cross-reaction — note it, leave the scope

**Decision: keep the `CROSS_DETECTS_C_ABORTUS_IN_SILICO` flag, change nothing else.**

The pair has 0-penalty matches on *C. abortus* (7 of 7 records) and on many uncultured
*Chlamydia* 16S records, so it does not separate the two. It does correctly fail *C. pecorum*,
*C. felis*, *C. muridarum* and *C. pneumoniae*, consistent with the paper, which tested only
the latter two plus non-chlamydial respiratory flora.

Cross-reaction is a specificity problem; this pipeline measures coverage. A false positive on
a sister species does not change the *C. psittaci* coverage number, so there is nothing for
the pipeline to act on. Broadening the declared scope to both species was considered and
rejected: it would misrepresent an assay that is the psittaci arm of a size-discriminating
multiplex, and change the denominator for a reason that is not about coverage.

## 4. M. gallisepticum vaccine pairs — hold until strain scoping exists

**Decision: do not enter the three vaccine-strain pairs yet.**

Kang 2023 (already the source of `MYCOPLASMA_gallisepticum_parE_Kang_2023`) is a
vaccine-differentiation multiplex: one species pair on parE, which is entered, plus three
vaccine-strain-specific pairs (ts-11, 6/85, F strain), which are not. The three are exact on
their own strain genomes and over 90% non-detect under the species taxid — because failing to
detect wild-type strains is what they are for.

Entered now, each would report catastrophic drift while working perfectly. This is the
lineage-conditional estimand problem in miniature: the denominator is a species when the
assay's target is a strain. They are therefore blocked on the sub-species scoping in
`docs/journal/2026-10-17-estimand-plan.md`, not on curation effort — the curation is done.

Note the species pair itself is in good shape and unaffected: 95 of 95 records long enough to
span the site give a product, every one at exactly 245 bp, 93 with zero mismatches.

---

# Second group, 2026-10-17

## 5. Specific-by-design entries — fix denominators case by case

**Decision: fix each case; what follows is how far that reaches.**

Twelve entries are narrower than their retrieval taxon by design, and they are scattered across
every section of the 2026-10-15 report — including `DWVA_polyprotein_Rossi_2024` in **Declining**,
which is the headline output. Measured feasibility of a per-entry denominator:

| entry | definable from NCBI metadata? |
|---|---|
| `PANPOX_..._highGC` / `..._lowGC` | **yes** — done below |
| `INFLUENZA_..._H5` / `..._H7` | already right: only **109 of 8,601** H5-titled HA records fall outside the subtype nodes (1.3%). The flag overstates it; no query change made |
| `BATRAVIRUS_..._european` | definable (RaHV-3 + BfHV-1 = 13 records) but futile — the genus holds **17** records, unassessable either way |
| `ORTHOBUNYAVIRUS_..._Cac` | definable by enumerating CE + BUN serogroup members; a curation job, not done |
| Bd `BdCAPE`, Bd `BdGPL`, avipox hummingbird, `DWVA`, `DWVB` | **no** |
| `CDV_P_gene_panCDV` | not this problem — its scope is *broader* than its taxid (also detects PDV) |

The five marked no are not a shortfall of effort. Bd is one taxid with one organism name across
9,496 records; the hummingbird avipox clade is not a taxon; and of 5,999 DWV records on the
species node only 960 sit under the A or B variant nodes, so **84.0% carry no variant label**.
DWV is already scoped to the variant nodes, which is the best available denominator — its
`declining` call rests on 28 recent evaluable records drawn from the labelled 16%. These five
need the phase-2 sequence clustering in `docs/journal/2026-10-17-estimand-plan.md`; no query can reach them.

### PANPOX, done

The pair partitions the subfamily by GC content, so its share against the whole subfamily was
never coverage — it was the design. NCBI lists **18** genera in Chordopoxvirinae (a hand-written
list had 11 and would have dropped 494 records silently). One 100–400 kb record per genus was
fetched and its GC computed, reproducing the paper's stated ~25–64% span:

- **above 60%** — Sciuripoxvirus 66.7, Parapoxvirus 64.4, Molluscipoxvirus 63.5, Crocodylidpoxvirus 61.9
- *intermediate* — Macropopoxvirus 53.9, Leporipoxvirus 43.2
- **below 40%** — Salmonpox 37.4, Pteropopox 33.8, Orthopox 33.0, Mustelpox 31.3, Avipox 30.8, Centapox 29.5, Suipox 27.4, Yatapox 27.0, Cervidpox 26.8, Capripox 25.9, Oryzopox 23.6, Vespertilionpox 23.5

High-GC is scoped to the four above 60% — which contains the three the earlier screen actually
hit, plus Sciuripoxvirus, which sits in the same band and simply had no record in that
measurement. Low-GC is scoped to the twelve below 40%. **Leporipoxvirus and Macropopoxvirus
(783 records) are in neither query**: Li 2010 does not say where the crossover between its two
pairs sits, so assigning them could hide a real failure or invent one.

Both entries are flagged `STALE_UNTIL_RERETRIEVED_QUERY_CHANGED_2026_10_17` — **a query change
means the group must be re-retrieved and rescreened.**

## 6. Nosema bombi — re-cited to Klee 2006

**Decision: move the citation to the paper that published the primers.**

Kato 2020 attributes Nbombi-SSU-Jf1/Jr1 to Klee et al. 2006 but prints no DOI. Crossref returns
`10.1016/j.jip.2005.10.012` — Klee, Tek Tay & Paxton, *J Invertebr Pathol* 91:98–104, 2006
(PMID 16376373) — matching Kato's attribution on authors, journal, volume and pages. `citation.doi`,
`design_year` and `reference` now point at Klee, and the DOI was added to the Crossref cache so
`check_citations.py` passes (182 citations, 0 problems).

Two things deliberately left: `doi_verified` is **false**, because the house path for that flag is
`scripts/resolve_citations.py`, which requires a contact email this session had none for — run it
to flip the flag normally. And `oligos_designed_here` is **null**, not true: Klee 2006 is still not
in `papers/`, so nothing here has confirmed it prints these oligos; the sequences remain as read
from Kato's Table 1 and verified against AY008373.1. The entry id still says `Kato_2020`; renaming
touches every reference to it and deserves its own pass.

## 7. Ophidiomyces target-D — keep

**Decision: keep, with the curator's reading stated as an inference.** No change needed: the
`PANEL_MEMBER_USED_AS_SPECIES_MARKER_ON_CURATOR_READING_OF_TABLE_1` flag already says this is the
curator's reading of Table 1 and not a claim the paper makes. D is genuinely the only one of the
eleven panel targets the paper shows amplifying in all six lineages, which is what makes it
meaningful as presence/absence where the other ten are not. It carries no published specificity
data of its own, and the flags say so.

## 8. Tasman-PCR — out of scope

**Decision: do not enter the four Kwon drafts.** The registry is for assays whose target is a
pathogen genome. A host-genome marker for transmissible cancer drifts with host population
genetics, which this pipeline's retrieval, taxid scoping and scoring were not built to model — the
coverage number would be noise. Recorded here so the question is not reopened from scratch; the
drafts remain in the scratchpad.

## 9. Reptarenavirus — keep the pooled entry, record the winning pair

**Decision: keep one entry; add the winning forward/reverse combination to the calls output.**

Baggio 2023 runs 6 forward and 7 reverse primers in one tube with no designated pairing, and the
scorer takes the best of all 42 combinations, which is what the tube does. The gap is that a call
can be won by a combination nobody designed together (F6 with R2) and nothing records which one
won, so it cannot be audited. **Not yet implemented** — it needs the winning pair carried through
`score.py` into the calls writer, and it will populate for every assay with alternates, not just
this one.
