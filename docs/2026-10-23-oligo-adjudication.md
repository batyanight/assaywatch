# Adjudicating 21 near-misses and 32 absent oligos (2026-10-23)

`docs/2026-10-23-wave5-elsevier-and-oligo-flags.md` left 15 candidate oligo errors
after removing the 4 CDV arctic variants and 2 `Mod` oligos, and noted that the 32
`absent` oligos had never been enumerated. This is that adjudication: every
`near:` and `absent` row read against the paper itself, by eye where the
extraction had failed — and then, for every sequence that changed, **screened
against real records before being kept**.

That last step is the finding. Four sequences looked like transcription errors on
the printed evidence; two of them were, and two were the registry being right and
the paper being wrong. **The rescreen is what told them apart**, and it only
happened because the changes were screened before being trusted.

## The policy decision: keep both

A published panel often reprints a published primer with the degeneracy widened.
Asked whether the registry should hold the panel's form or the original paper's,
the maintainer's answer was **keep both**: store the form actually run, and record
what it was modified from and where that modification is published.

That is `Oligo.modified_from` plus `Oligo.modification_doi`. The verifier reads it:
an oligo whose `modified_from` the paper prints reads `modified` and counts as
agreeing, rather than as a transcription error against a sequence nobody claimed.
An empty `modification_doi` is itself a finding — the modification is unpublished
and exists only here. 16 oligos now carry it.

## Two corrections survived; two were reverted by measurement

Each changed oligo was screened against its own archive, counting exact binding
sites on both strands:

| oligo | stored form | the printed form | verdict |
|---|---|---|---|
| Hel2 (calicivirus) | 0 records | **17** | corrected |
| Hel1 (calicivirus) | 16 (22-mer) | **0** (25-mer) | corrected anyway — see below |
| Borna-NF | **260** | 0 | **reverted** |
| CoV-RVS3 | **215** | 88 (panel) / 204 (Watanabe) | **reverted** |

### Kept: the calicivirus pair was one mis-split table cell

Reid 1999 Table 2 wraps each 25-mer after a hyphen and its own nt column says 25.
The registry held Hel1 truncated to its first line (22 nt) and Hel2 as Hel1's
wrapped continuation `GCG` glued onto Hel2's first line (18 nt) — one primer's
tail had become the next primer's head. Both are now the printed 25-mers, and
**the design paper confirms them independently**: Reid's footnote credits Neill &
Seal 1995, which is `10.1016/S0890-8508(95)90962-1`, fetched over the Elsevier API,
and whose Methods print Hel1 `GTCCCAGTATTCGGATTTGTCTGCG` and Hel2
`AGCGGGTAGTTCAGTCAAGTTCACC` verbatim. `oligos_designed_here` is now false.

Hel2 gained 17 binding sites. Hel1 lost all 16, and that is **a scoring finding,
not a sequence problem**: on all 16 matching records — the designers' own targets,
the VESV / San Miguel sea lion virus / skunk calicivirus U146xx series — the
template base under Hel1's 3'-terminal position is `C` where both papers print
`G`. The published primer carries one 3'-terminal mismatch against its own
targets. `terminal_mismatch_fails: true` makes that fatal by itself, so the
detected share moved 5/18 → 0/30; but this is a conventional PCR and Reid reports
the assay working. It is now a worked example under ROADMAP Phase 2's
per-chemistry scoring item, and must not be read as coverage loss.

The sequences stay as published, per the Circovirus precedent: where a paper and
the records disagree, the registry keeps the published sequence and discloses.

### Reverted: Borna-NF

Zimmermann 1994 prints its internal sense primer as `GCCTTGTGTTTCTATCTTTC`, and
the registry held `GCCTTGTGTTTCTATGTTTG` — two differences, one at the
3'-terminal base. Changing it to the printed form took the assay from **308/456
detected (67.5%) to 0/372 (0.0%)**.

Across all 1,516 records in the Orthobornavirus archive, the template following
the shared 15-mer `GCCTTGTGTTTCTAT` reads:

| continuation | records |
|---|---|
| `GTTTG` (the stored form) | 260 |
| `GCTTG` | 42 |
| `GTCTG` | 1 |
| `CTTTC` (the printed form) | **0** |

A nested primer that never matched its own target is less likely than a
transcription or OCR error in a 1994 scan. The stored form is restored and the
printed one recorded as `modified_from`.

**This exposed a pre-existing false signal.** The sibling
`BORNA_VIRUS_N_gene_Zimmermann_1994_round2` stores the *printed* form as
BornaNestF, and it reads **0/369 = 0.0% in the 2026-10-22 baseline** — it has
never detected anything, for exactly this reason, and nobody had explained why.
It is now flagged. Aligning it with the measured form would mean storing a
sequence no paper prints, so that is left as a maintainer decision.

### Reverted: CoV-RVS3, and the stored form vindicated

Three forms exist, and the stored one is none of the published two:

| form | binding sites in 25,506 records |
|---|---|
| stored `CCATCATCASWYR**G**AATCATCATA` (24) | **215** |
| Watanabe 2010 `CCATCATCAGATAGAATCATCATA` (24) | 204 |
| PREDICT P-006 `CCATCATCASWYRAATCATCATA` (23) | 88 |

The stored sequence is Watanabe's primer with the panel's degeneracy *and*
Watanabe's length: the panel dropped a base. Replacing it with P-006's 23-mer took
the assay from **40.0% to 2.2% detected**. Calling it "a hybrid nobody printed"
was right about its provenance and wrong about its quality — it binds better than
either published form. This is the same pattern already recorded for CoV-RVS1 in
the Lan 2010 sibling, where the stored 30-mer hits 685 of 884 genomes and the
paper's 33-mer never gets below 4 mismatches.

## Why the `absent` oligos were mostly not errors

Six mechanisms, none a defect in the registry:

- **The oligos are only in a figure.** Boyle 2004 (Bd), Pallister 2007
  (ranavirus), Hellgren 2004 (HaemF/HaemR2) and Sigrist 2021 (nine oligos across
  three entries). These will read `absent` forever.
- **Degeneracies written as parenthesised alternatives.** Zhu 2000 prints
  `TTT(C/T)(C/T)G(A/G)TCCTCTCGTACT`.
- **A cocktail consolidated into one degenerate pair.** Zhai 2007 prints four
  forwards and four reverses; the stored MOD-FWD/MOD-RVS cover all eight with no
  mismatch, and are published in that consolidated form in three later protocols.
- **Glued table text.** Deckers 2009's run came out ending `AGCMVGB` — the name
  column plus the next column's label.
- **Hyphen-wrapped table rows.** Lozano 1997's ARS3V and ARS16V, and the
  calicivirus pair above — the one case where the wrap had corrupted the entry.
- **A comparator primer, not the assay's own.** Sigrist's BornaPCA6 read `near:1`
  against PaBVcon_1401+ from supplementary Table S4, one of the *previously
  published* assays that paper compares itself to.

**Bd, the one `active` assay, was the urgent case** and is clean: all three oligos
match AY598034.1, the accession its figure cites, with a 146 bp product equal to
the stored `amplicon_bp`.

The flagging rule, so it is not decided per entry: `oligos_read_from_figure` goes
on an entry whose oligos' only primary source is an image. Bd does not get it,
because the figure names a GenBank accession and the sequences were confirmed
against that accession rather than by eye.

## Sources found elsewhere

**EcoLT-1/EcoLT-2 — resolved, and the citation stays.** Both read `absent`
against Victor 1991, which prints LT51/LT31 and names no EcoLT; both are printed
in Wang 1997 Table 2 (`10.1046/j.1365-2672.1997.00300.x`) with these names and the
117 bp this entry stores. But measuring against 146 GenBank `eltA` records showed
the two pairs sit on the **same two sites**, shifted a few bases:

```
genome   GGAATATAGAGACCGGTATTACAGAAATCTGAATATA
EcoLT-1          GAGACCGGTATTACAGAAATC      (122 records exact)
LT51                CCCGTATTACAGAAATCTGA    (0 — one mismatch at its 5' position 3)
```

So Wang's "Victor et al. (1991)" credit records real design lineage, and the
Victor citation is not wrong. Under keep-both, Victor's printed primers are now
`modified_from` with Wang as the `modification_doi`; **no re-citation and no
rename**. The `oligos_from_secondary_source` and `citation_is_indirect` flags stay,
because the sequences are still read from Wang's table. EcoLT-2 carries one
mismatch at its own 5' position 2 (`GAG` against the template `GTG`), about 19
bases from its 3' end and so close to free under a 3'-weighted penalty.

**PVOnstF — left as it was.** It is printed in Wray 2016 Table 1
(`10.1007/s10393-016-1183-z`), paired with PVO3 as this same hemi-nested assay, and
that table's own citation column for the pair reads "Unpublished". It resembles
none of Bourhy's printed primers, so the entry is a genuine composite: PVO3 is
Bourhy's exactly, and the nested forward has no publication that designed it.
Repointing the DOI would credit Wray with PVO3 and attach a DOI to a primer Wray
calls unpublished. Flagged, not re-cited.

## Three oligos have no source at all

`Pan_mycoplasma_16S_23S_intergenic_space` 16-23-R1, `..._3` 16-23-F3, and
`Pan_mycoplasma_16S_All_Van_1992` MycoRev1: not in the cited paper and not in
Europe PMC full text. `oligo_source_unresolved` is **not** a to-do here.

## One non-oligo removed from screening

`Entamoeba_18S_small_subunit_SSU_2014` held a second GEI18SR under `alternates` —
the form the paper prints verbatim, which is the *target strand* at the reverse
primer's site, not the oligo. Against AF149905 both printed strings lie on the
sense strand (1308 and 1799, a 511 bp product inside the paper's stated 450-535),
so the primary reverse slot is the correct molecule. Removed. The entry is
`deprecated`, so nothing downstream changes.

## The numbers

| | 2026-10-22 | after wave 5 | now |
|---|---|---|---|
| checkable oligos agreeing | 393 / 466 (84%) | 395 / 460 (86%) | **415 / 462 (90%)** |
| `near:` | 21 | 13 | **5**, all documented artefacts |
| `absent` | 31 | 32 | **22**, all documented |
| `sibling` | — | 6 | 4 |
| `modified` | — | 2 | 16 |

Current output: `results/oligo-verification-2026-10-23.tsv` and its `.log`.

## The rescreen

Run on the four groups the changes touched, targeted so no dated run was
overwritten (screens are not date-keyed):

    snakemake results/screened/{178830/all,11974/all,11118/q4d4730ef3b,39733/all}/*.tsv \
        --config run_date=2026-10-23 --cores 4

18 jobs, 42 s, exit 0; then 10 jobs, 38 s for the two reverts.
`snakemake-2026-10-23-rescreen.txt` and `-revert.txt`.

Both reverted assays are back to the baseline to the record: Borna 308/456 =
67.5%, coronavirus 3171/7920 = 40.0%. Net call changes that remain:

| assay | before | after |
|---|---|---|
| `CALICIVIRUS_ssRNA_Helicase_Reid_1999` | 5/18 = 27.8% | 0/30 = 0.0% (scoring, see above) |
| `ASTROVIRUS_RdRp_Chu_2008_round1` | new entry | 1021/2962 = 34.5% |
| `ASTROVIRUS_RdRp_Chu_2008_round2` | new entry | 2623/3358 = 78.1% |

## A correction to an earlier commit

The commit that split the Chu entries said the astrovirus alternates are in
neither Atkins 2009 nor the PREDICT book. The first half holds; the second does
not. The book has a **second** astrovirus protocol, **P-002**, whose REFERENCE line
reads "Chu, D.K.W. et al (2008)" and which prints all five oligos at ~436 bp
(round 1) and ~421 bp (round 2) — agreeing with the measured medians of 437 and
410. Both new entries carry `predict_protocol: P-002`.

## Still open

- The **20 `in-text`** rows: the sequence occurs in the paper but not in any
  listed oligo, so it may have been found inside a printed target sequence rather
  than a primer table. Never enumerated.
- **`BORNA_VIRUS_N_gene_Zimmermann_1994_round2`** reads 0% by construction. Storing
  the measured form would mean storing a sequence no paper prints.
- Whether `CALICIVIRUS_ssRNA_Helicase_Reid_1999` should be re-cited to Neill &
  Seal 1995, now that the design paper is readable and prints both oligos. Same
  rename trade-off as the two above.
- `ORTHOBORNAVIRUS_XP_aquatic_Sigrist_2021` stores its reporter as "Alexa 647N"
  while Figure 2C labels the probe A647N, the conventional short form of Atto
  647N. Not screened, not changed, recorded.

## The lesson worth keeping

"The paper wins" is the right default for a *sequence* and the wrong default for a
*correction*. Two of four changes that the printed evidence supported would have
destroyed a working assay, and only screening caught it. Any future oligo
correction should be screened against its own archive before it is committed, and
the before/after detected share reported — which is what
`scripts/retrospective.py` and a targeted `snakemake` on
`results/screened/<group>` make cheap.
