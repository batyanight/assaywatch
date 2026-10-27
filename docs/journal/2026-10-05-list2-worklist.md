# List 2 worklist: 34 candidate papers, 8 assays added

2026-10-05. From the 34 papers in `papers/` that are not already cited by a
registry entry. Extraction: `scripts/extract_candidate_oligos.py` →
198 candidate oligos from 29 papers.

## Added (8 entries, 22 oligos, all `exact` against their own papers)

| entry | pathogen | evidence |
|---|---|---|
| `PD_WNS_ITS1_Shuey_2014` | white-nose syndrome | 140-141 bp, probe inside |
| `FRANCISELLA_tularensis_tul4_Long_1993` | tularemia | 0 mismatches on a tul4 contig, 250 bp |
| `PARANANNIZZIOPSIS_ITS_Lorch_2023` | snake fungal disease | 82 bp, probe inside |
| `PERKINSEA_NAG01_18S_cladeD_Smilansky_2021` | pathogenic Perkinsea | 287 bp on the paper's own accession |
| `PERKINSEA_NAG01_18S_cladeAC_Smilansky_2021` | non-pathogenic clades | same amplicon, different probe |
| `AVIPOXVIRUS_dsDNA_4b_core_Farias_2010` | avian pox | 6/40 records, all 250 bp, probe in 6/6 |
| `LEPTOSPIRA_lipL32_Ahmed_2020` | pathogenic Leptospira | 6/24 records, all 114 bp, probe in 6/6 |
| `TILV_ssRNA_segment3_ME1_ME2_Kembou_2017` | tilapia lake virus | 1/24, exactly the paper's stated 250 bp |

**Every `amplicon_bp` is measured on real records, not quoted.** Only Perkinsea
and TiLV also have a stated size, and in both cases the measurement agrees.
Avipox is the one case where it does not: measured 250 against a stated 234, and
the measurement wins because it was invariant across six records.

## Deliberately not entered, and why

These are judgements, not omissions. Each one would have made the tool report
something false.

- **The Pd congener probe.** Shuey's assay runs two probes on one primer pair:
  `CTTGCCAGAGGACTAA` (P. destructans) and `CTTGCCAGAGGACCTA` (harmless
  *Pseudogymnoascus*/*Geomyces* spp.), differing by one inserted C. Pooling them
  would report detection of the wrong organism, when telling the two apart is the
  entire point.
- **Long's TUL4 hybridisation probe.** The sequence as read from the 1993 scan
  carries 8 mismatches against a contig where both primers match perfectly, so
  the OCR mangled it. It is a conventional PCR, so no probe is needed.
- **The Leptospira internal-control oligos.** `IntoF2`, `IntoR2`, `IntoP1`,
  `PlasintS1` target a synthetic control, not Leptospira. Entering them would
  have the tool screening a plasmid against Leptospira records and calling the
  guaranteed non-detection drift. The table labels them, which is the only reason
  it was visible.
- **TiLV beta-actin.** A tilapia HOST control, not a virus assay.
- **TiLV F1/VR3.** No product in 8 strided segment-3 records. Unresolved, not
  confirmed; entering it would be guessing.
- **Chlamydia psittaci nested 16S (Messmer 1997).** Both rounds found no product
  in 8 strided 16S records. The source text is badly OCR-damaged, so the
  transcription is suspect and this needs a clean primer table before it can be
  added. Worth pursuing - psittacosis is a real gap.

## Still to work through (20 papers)

Oligos extracted and in `results/candidate-oligos-2026-10-05.tsv`, awaiting the
same verify-then-enter treatment:

EEHV pol (19 oligos), deformed wing virus RdRp (19), canine distemper N
(jcm.02505-21, 17), canine morbillivirus (v13081632, 15), reptarenavirus (14),
Vairimorpha/Nosema bombi SSU (10), Mycoplasma gallisepticum (8), influenza A
hemagglutinin (7), monkeypox B6R (6), devil facial tumour (6), canine
morbillivirus (pone.0232044, 6), leporid gammaherpesvirus (6), pan-pox
(jcm.01697-09, 4), batrachovirus (4), Mycobacterium microti (4), Vibrio
coralliilyticus (two papers, 3 and 4), Trichomonas gallinae (2), and one
unlabelled 1996 J Virol Methods paper (2).

## Five papers whose primer tables are images

No text extraction is possible; these need the table read by eye:

- `10.1111/1755-0998.13299` — **Ghosh 2021, Bd lineage discrimination.** The
  highest-priority paper in the whole sweep, because it speaks directly to the
  estimand problem in the pipeline review, and the one that cannot be automated.
- `10.1371/journal.pone.0207365` — *Mycobacterium bovis*
- `10.2807/1560-7917.es.2020.25.41.2001732` — Usutu virus
- `10.3390/jof7040258` — *Batrachochytrium* ITS
- `10.3390/v13071358` — avian orthobornavirus

## The pattern worth keeping

The sequence was never the hard part. Every judgement above turned on the words
around the sequence: which oligo is a control, which is a congener probe, which
came from an earlier paper, which is a host gene. That is why the extractor
reports 90 characters either side of every match, and why nothing here was added
without screening it against real records first.
