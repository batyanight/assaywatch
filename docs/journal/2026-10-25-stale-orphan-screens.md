# Stale orphan screens inflated three of today's measurements about a hundredfold

`results/screened/` keeps the screens of **orphan groups** - archives no live assay retrieves
any more (`docs/journal/2026-10-24-orphan-archives.md`). Because nothing asks for them, nothing
rescreens them, so their TSVs sit on disk at whatever date they were last written, under
whatever scoring rules were in force then. **Any analysis that globs
`results/screened/*/*/*.tsv` and takes the newest file per group reads those as current.**
Three measurements I made today did exactly that, and their counts were wrong by about two
orders of magnitude.

`collect_calls` is what the report is built from, and it collects only the groups the current
registry asks for. **`results/<run>/calls.tsv.gz` is the authoritative table.** A number quoted
beside a report number has to come from there.

## The case that exposed it

`LYSSAVIRUSES_ssRNA_Nucleoprotein_gene` declares `amplicon_bp: 373`, and
`amplicon.declared_tolerance: 0.25` has been on since 2026-10-14, so the screener cannot
produce a product outside 279-466 bp. Yet a length measurement showed its failures spanning
**51-2996 bp across 1,166 distinct lengths**. Both facts cannot be true of the same screen.

They were not the same screen. Lyssa appears in two groups:

| group | screen date | rows | amplicon lengths |
|---|---|---|---|
| `11286/all` | **2026-10-25** | 248 | 374-374, **1 distinct** |
| `11270/all` | **2026-10-03** | 46,404 | 51-2996, 1,166 distinct |

`11270/all` is the **Rhabdoviridae orphan group**, 16 MB, identified this morning: "both live
L-gene entries now retrieve under `qdb266b171e`". Its screen predates `declared_tolerance` by
eleven days. The current screen behaves exactly as the config says.

## What has to be corrected

**1. The chance-pair scope.** `docs/journal/2026-10-25-chance-pairs-invent-denominators.md` reported
26,691 rows across 6 probe-bearing assays (and, before a correction, 28,751). From
`calls.tsv.gz` the true figure is **277 rows across 11 assays, out of 924,755 evaluable**:

| assay | artefact rows / evaluable | reported | corrected |
|---|---|---|---|
| `OPHIDIOMYCES_ophidiicola_targetD_Haynes_2023` | **111 / 192** | 42.2% | **100.0%** |
| `ORF_VIRUS_dsDNA_RPO147_J6R_TaqMan_Zhao_2013` | **76 / 164** | 53.7% | **100.0%** |
| `LEPTOSPIRA_lipL32_Ahmed_2020` | 42 / 1,969 | 93.0% | 95.0% |
| `ORTHOBORNAVIRUS_XP_aquatic / passerine / psittacine_Sigrist_2021` | 13 / 538 each | 8.7 / 4.3 / 17.7% | 9.0 / 4.4 / 18.1% |
| `MONKEYPOX_dsDNA_G2R_WestAfrican_TaqMan_Li_2010` | 4 / 13,239 | 73.3% | 73.4% |
| `MONKEYPOX_dsDNA_C3L_CongoBasin_TaqMan_Li_2010` | 2 / 1,430 | 99.4% | 99.6% |
| `NA_ORTHOPOX_dsDNA_G9R_..._Gallardo_Romero` | 1 / 15,085 | 0.0% | 0.0% |
| `AVIPOXVIRUS_dsDNA_4b_core_Farias_2010` | 1 / 251 | 80.9% | 81.2% |
| `MYCOBACTERIUM_TB_complex_IS1081_Hermes_2018` | 1 / 1,450 | 99.9% | 100.0% |

**The two verdicts that move are unchanged**, because those were read from the report rather
than from my glob. Everything that changes is the *scope* claim. And the guard holds where it
matters most: of West African mpox's 13,239 evaluable rows only **4** are touched, so its 2,688
clade-I failures - the finding the test must not break - are untouched, as their `fwd_penalty`
0 / `rev_penalty` 0 signature requires.

**2. The three `mgb` fungal assays.** `docs/journal/2026-10-25-fungal-assays-diagnosed.md` was built on
whole-archive rates of 1.4%, 31.8% and 25.8% and on tens of thousands of artefact rows. Those
rows are in the Ophidiomyces (`1387563/all`, 530 MB) and *B. salamandrivorans*
(`1357716/all`, 90 MB) **orphan** groups. **None of those three assays appears in
`calls.tsv.gz`'s artefact list at all.** The doc's conclusion - that nothing is wrong with them
and the report's "no recent data" / "insufficient data" is correct - survives, and now has a
second reason: most of the records I was reasoning about are not in the current denominator
either. The *B. sal* probe-divergence watch item stands, because those five 2024 records were
checked individually against the sequences.

**3. The locus-identity measurement**, re-run from `calls.tsv.gz`, and it comes out **cleaner**:

| assay | detect/reduced | chance-pair shaped | genuine-failure shaped |
|---|---|---|---|
| `ORF_VIRUS_..._Zhao_2013` | **1.00** (n=40) | **0.32-0.41** (n=60) | none |
| `LYSSAVIRUSES_ssRNA_Nucleoprotein_gene` | 0.86-0.99 | **none** | **0.86-0.99**, p50 0.89 |
| `RETROVIRUS_..._SIV_Takehisa_2009` | 0.87-1.00, p50 0.93 | none | **0.65-0.67** (n=60) |

The lyssavirus overlap I reported, and the six rows I had to explain away as mis-binned, were
**entirely stale data**. On current screens that assay has no chance pairs and its genuine
failures sit at 0.86 and above. **The gap widens from 0.41-0.65**, and SIV remains the ceiling:
0.70 still deletes all 60 of its genuinely divergent failures.

> **`scoring.locus_identity_min: 0.50` stands, better supported than before** - it now sits in
> the middle of a 24-point gap rather than a 16-point one.

## The length signal: not a safe gate, and now mostly explained

The cheap signal was amplicon-length dispersion. On clean data most of its apparent power was
the stale screens: the 1,166 scattered lengths were pre-tolerance rows, and the current screen
gives one length. What remains is a mixed result, and it argues against using length as a gate:

- **Orf's chance pairs are all at exactly 62 bp** against a declared 68 - one distinct length,
  not scatter. So "dispersion" is not what identifies them; being 6 bp off is, and that is
  inside the 25% tolerance by design.
- **`OPHIDIOMYCES targetD`'s chance pairs span 56-69 bp against a declared 57, and 63% are
  within 5 bp.** A length rule would keep most of them - and that is the one active entry whose
  verdict was wrong.
- **West African mpox's genuine clade-I failures are all 82 bp against a declared 85.** A strict
  length-equality rule would exclude the finding the whole design is built to protect.
- **SIV Takehisa's severe genuine failures are 100% at exactly the declared 285 bp**, which is
  informative in the opposite direction: it says those rows are at the real locus, and so
  confirms they are genuine rather than chance.

So **length is a diagnostic, not a filter.** `amplicon.declared_tolerance: 0.25` already does
the coarse version of this job and is the one number in `config.yaml` with a measured defence.
Interior identity remains the test.

**One small finding on the way:** Lyssa declares 373 bp and its current screens measure **374**
in 99% of detects. One base, and the registry's own policy is that the measurement wins, so it
is worth a look rather than a correction on this evidence alone - an inclusive/exclusive
convention would explain it exactly.

## The rule this earns

**Measure from `results/<run>/calls.tsv.gz`, never from a glob over `results/screened/`.** The
second is run state spanning months of scoring rules; the first is what the report says. Three
wrong numbers today came from that one substitution, and each looked entirely plausible -
which, as with the `read_calls` no-op earlier, is the part worth remembering.
