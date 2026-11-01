# Four design papers read for scope; none of the four cases was a scope error (2026-10-20)

`docs/journal/2026-10-20-pan-family-override.md` point 3 proposed curating `scope_taxids`
from the design papers as the way to shrink the lineage-override cases "rather than
adjudicate them", naming *Papillomaviridae* sp. and *Mycoplasma ovis* as lineages
outside their assay's stated range. This session built the audit that enumerates
those cases and read four of the design papers. **The proposal does not survive
contact with the papers: in all four cases the firing lineage is inside the stated
range, and in three of the four it is a virus the paper itself amplified.**

## First: the newest calls table is not the current scorer's output

`results/2026-10-18/calls.tsv.gz` was screened under the `by_chemistry.conventional`
override that `df5356f` reverted the next day. Paramyxovirinae L round1 goes 5,131
`fail` / 1,884 `reduced` on 2026-10-17 to 33 / 6,984 on 2026-10-18, while the
hydrolysis-probe assay `INFLUENZA_A_ssRNA_NP_Tsukamoto_2010` is identical across the
two runs apart from 24 new records. The config commit `c15a3b7` lands at 22:10:57,
three minutes after that run finished at 22:07:26, so the working tree carried the
relaxed numbers while it ran.

Tier-2 measured on it reads **0 of 11** failures caught against **3 of 11** on
2026-10-17, and all three lost catches (Paramyxovirinae round1, round2, Forslund L1)
are assays whose verdict moves to `stable` under the relaxation. **Everything below
is measured on `results/2026-10-17/calls.tsv.gz`**, which is the newest valid
evidence. This is the trap `docs/RESUME-HERE.md` warns about for `--touch` across a
scoring change, arriving by a different route.

## The audit

`scripts/lineage_override_audit.py` replaces the hand count that three docs in a row
re-derived from a calls table. It lists every assay whose status comes from a lineage
override with the firing lineage's name, rank, share, whether that lineage is inside
the entry's `scope_taxids`, and whether the design paper is on disk. Ids are resolved
through `docs/rename-mapping.tsv`, which drops four rows for assays since removed
from the registry — the counting flaw `RESUME-HERE` flags against every status count
taken off these calls.

At 2026-10-17, with the shipped override rule: **21 overrides, 15 on a pooled `low
coverage`, 5 on `stable`, 1 on `watch`, and 6 on a lineage at or above the pooled
share** — the "6 of 17" that point 2 of the override doc wants cases for.

`drift.py` now stores `lineage_worst_idx` so the firing lineage is readable without
parsing the note.

## The four papers

| assay | firing lineage | what the paper says | verdict |
|---|---|---|---|
| `RHABDOVIRUS_ssRNA_L_gene` round1/2 | *Lyssavirus rabies*, 82/968 = 8.5% and 171/939 = 18.2% | Bourhy 2005 gives PVO3's coordinates **on the Rabies virus PV genome**; RV PV and SAB-B19 are two of its ten design sequences; RABV 9911/PV/SADB19 were amplified there (AY854660-662) | in range; **scoped** to the animal rhabdoviruses |
| `ARENAVIRUS_ssRNA_S_gene_2` | *Mammarenavirus choriomeningitidis*, 41/78 = 52.6% vs pooled 43.5% | Lozano 1997 calls LCM "the prototype of the family" and amplified LCM WE among ten isolates | in range, **above pooled**; scoped to the mammarenaviruses |
| `CIRCOVIRUSES_ssDNA_vertebrate_Rep_Gene_round2` | *Circovirus parrot* (BFDV), 69/95 = 72.6% vs pooled 45.0% | Mankertz 2000 built the primers on an alignment of PCV1, PCV2 **and BFDV**, and BFDV-infected parrot liver is one of four DNAs tested | in range, **above pooled**; not scoped |
| `Morbillivirus_including_CDV_P_gene` ×2 | *Morbillivirus caprinae* (PPRV), 0/83 | Barrett 1993 amplified "all known members of the group", naming RPV, **PPRV**, CDV, PDV, DMV, PMV | in range; not scoped, and the 0% is a scorer artefact (below) |

Two scopes were shipped and two were not, on the same standard: ship when the
excluded taxa are a group the paper framed out, skip when the exclusion would be
cosmetic.

- **Rhabdovirus, shipped.** `scope_taxids: [35303, 2842407, 2842415, 3152207]` —
  *Rhabdoviridae* minus the plant subfamily *Betarhabdovirinae*. Bourhy's primers
  were predicted "to be broadly reactive among the **animal** rhabdoviruses", and
  every isolate he amplified carries an AY854xxx accession generated in that study
  while all six plant entries in his Table 1 carry pre-existing accessions. 35303
  *unclassified Rhabdoviridae* is in deliberately: it holds the novel rhabdoviruses
  PREDICT found with this very assay (`Rhabdovirus PREDICT_RbdV-21`, `-27`) and 255
  `Rhabdoviridae sp.` records, and an allow-list without it would exclude the assay's
  own successes. 769 of 9,879 records go out of scope; 302 of them were evaluable in
  round1 and 469 in round2.
- **Arenavirus, shipped.** `scope_taxids: [208898, 1653394]` — *Mammarenavirus* plus
  *unclassified Arenaviridae*. "Family-specific" in 1997 meant the mammarenaviruses;
  *Reptarenavirus*, *Hartmanivirus*, *Antennavirus* and *Innmovirus* were all
  described later, and snake reptarenaviruses have their own registry entry, so
  leaving them here scored them twice. 473 records out of scope, 45 of them evaluable
  in `_S_gene` at 0% detected.
- **Circovirus, not shipped.** The narrower scope the paper supports ("conserved in
  **vertebrate** circoviruses") would exclude genus *Cyclovirus*, which holds 741
  records but only **4 evaluable** ones against 7,752 under *Circovirus*. An
  allow-list would also have to re-admit the 434 unclassified Circoviridae records
  (bat, rodent, fur seal) that are vertebrate circoviruses.
- **Morbillivirus, not shipped.** PPRV is a bench positive, so there is nothing to
  exclude.

**Measured effect of both shipped scopes: none.** No status moves, no override
disappears, and the audit is byte-identical except that the newly scoped entries now
report their firing lineage as `in_current_scope: yes` — which is the point, since it
rules scope out as the explanation. The rhabdovirus denominator shrinks 1,289 → 1,243
and its share moves 11.64% → 11.67%. Tier-2 is unchanged: 3 of 11 caught, 9
disagreements, before and after. The excluded records are overwhelmingly old
deposits, outside every assay's recent window; expect this to matter later rather
than now.

## The Barrett panel, which is the session's real finding

Barrett 1993's PDF is an image scan with no text layer, read here from a 400 dpi
tesseract OCR of its three pages. The two primer sequences in that OCR match the
registry base for base, and the paper's "429 nucleotide DNA fragment" matches the
measured 429 bp in 4,326 of 4,347 detected-or-reduced records — so the
`_Barrett_2003` entry's `amplicon_bp: 430` was corrected to 429, where its twin
already read 429. Inside `declared_tolerance` either way, so no call moves.

`docs/bench-panels/barrett-1993-morbillivirus.tsv` is the fourth bench panel: the six
viruses Barrett's Methods name as amplified, plus measles, which the primer
coordinates are given on. Current config, `scripts/bench_panel.py`:

| accession | label | call | penalty | 3'-window mispairs |
|---|---|---|---:|---|
| KF650727.1 | porpoise morbillivirus 53/90 | detect | 0 | – |
| NC_001921.1 | CDV Onderstepoort | detect | 0 | – |
| NC_028249.1 | PDV Wadden Sea 1988 | reduced | 2.5 | – |
| NC_001498.1 | measles | reduced | 3.0 | rev5 T:G |
| NC_006296.2 | rinderpest Kabete O | **fail** | 4.0 | rev5 T:G |
| NC_005283.1 | dolphin morbillivirus | **fail** | 5.0 | rev5 T:G |
| NC_006383.2 | PPRV Nigeria 75/1 | **fail** | 9.5 | fwd4 C:C; rev3 G:T |

Counting `detect` and `reduced` as a band, **4 of 7 correct**. No negatives: the paper
reports no virus that failed, so this panel can show false fails and not false
detects, the same limitation as the Rebelo panel.

**All three false fails carry a G·T wobble inside the 3' window**, and that `rev5
T:G` is in four of the seven rows including measles, the design reference — so it is
a fixed feature of MorbR against the genus, and Barrett amplified them all anyway.
Measles sits at exactly 3.0, one point from failing.

This makes two independent panels on the same knob:

- **Forslund FAP**: 14 false fails of 60 types the bench amplified, 12 of them
  resting only on T:G mispairs (`docs/journal/2026-10-19-fap-bench-panel.md`).
- **Barrett morbillivirus**: 3 false fails of 7, all three with a G·T wobble in the
  3' window.
- **Meyer ATI** is the other knob — its one false fail has no 3'-window mismatch at
  all (`docs/journal/2026-10-20-meyer-ati-bench-panel.md`).
- **Rebelo Mycoplasma** disagrees nowhere and has no 3'-window mismatch anywhere, so
  neither change disturbs it.

And it reinterprets one of the override cases: PPRV at **0/83** looked like a
coverage finding, and Barrett's own PPRV reference scores `fail` on `rev3 G:T` plus
`fwd4 C:C`. The 0% is at least partly the 3'-window penalty. **No config change
here** — an identity-aware `score_primer` is a threshold decision and goes through
tier-2 first.

## The rest of the set, triaged (2026-10-20, second pass)

Every remaining override case whose design paper is on disk was read. **Not one is a
scope error.** Each entry carries the finding in its `notes_curator`.

| assay | firing lineage | paper's own range | verdict |
|---|---|---|---|
| `Pan_flavivirus_NS5_3` round1/2 | *Orthoflavivirus usutuense*, **0/428** and 0/429 | Usutu is in Scaramozzino 2001's test panel (Table 3, Fig. 2 lane 5) and MAMD/FS 778 are that paper's own primers, which "detected all of the tick- and mosquito-borne flaviviruses tested" | in range; the largest never-detected block in the set, and a finding |
| `ENTEROVIRUS_ssRNA_VP3_VP1_round2` | *Enterovirus betacoxsackie*, 719/1063 = 67.6% vs pooled 26.3% | titled "…Direct Identification of **All Enterovirus Serotypes**" | in range, **above pooled** by 41 points |
| `CORONAVIRUS_…_Lan_2010_round1` | *Gammacoronavirus galli* (IBV), 159/221 = 72.0% vs pooled 52.2% | Quan 2010 frames all three genera; the stored pair was screened here in 2026-10-05 against 884 genomes spanning alpha-, beta-, gamma- and deltacoronaviruses | in range, **above pooled** |
| `CORONAVIRUS_…_round2` | *Betacoronavirus* sp. (1928434), 47 records | — | **not a scope question**: `in_unclassified` is True, it sits under 696098 *unclassified Betacoronavirus*. The `lineage.unclassified_is_bucket` class |
| `PARVOVIRUS_…_dependovirus` | *Adeno-associated virus*, 1329/1525 = 87.2% vs pooled 80.2% | Gao 2002's "universal AAV signature-region primers" | in range, **above pooled** |
| `ADENOVIRUS_…_Polymerase_Primate_speci_Casas_2005` | *Mastadenovirus faecale* (= Human mastadenovirus F), 52/114 = 45.6% | Roy 2009's nested *pol* PCR across "the adenoviruses that infect primates"; HAdV-F is one | in range **by claim, not demonstrated** — Roy's own isolates were species B, C, E. Check at the oligo level before reading 45.6% as drift |
| `ADENOVIRUS_dsDNA_Hexon_gene` round1 | *Mastadenovirus caesari* (= Human mastadenovirus **C**), 146/212 = 68.9% | Casas 2005 typed species A–F | in range **even under the narrow human-only reading** |
| `ADENOVIRUS_dsDNA_Hexon_gene_round2` | *Aviadenovirus hepatitidis* (fowl adenovirus), **0/49** | out of Casas's human range, inside PREDICT's pan-adenovirus remit | the **only** case that turns on the composite question; **held** |

That splits the held adenovirus decision usefully: whichever way it goes, round 1's
override survives, because the lineage driving it is a human adenovirus species Casas
explicitly typed. Only round 2's turns on whether Casas or PREDICT is the operative
source.

**Five worked examples of the above-pooled pattern** now, all from design papers
rather than published follow-up: Enterovirus B (+41 points, 1,063 records), BFDV
(+27.6), IBV (+19.8), AAV (+7.0, 1,525 records) and LCM (+9.1). In every one the
override names as "failing" a lineage the paper demonstrates, or targets, and which
detects better than the pool it is being compared against. That is not a validation
case and will not move the confusion matrix, but as evidence against letting an
above-pooled lineage drive `declining` it is now five independent papers rather than
one row.

## Rahn 1992: the registry does not hold the published primers

Read for the Salmonella bench panel; the finding came first. Rahn's Table 3 prints
exactly two primers, **both in lower case**:

    139   gtgaaattatcgccacgttcgggcaa    invA 287-312
    141   tcatcgcaccgtcaaaggaacc        invA 571-550

`Salmonella_invA_Rahn_1992` holds `Sal-3` = the 3'-terminal **19 of 26** nt of 139
(missing `GTGAAAT`) and `Sal-4` = the 3'-terminal **19 of 22** nt of 141 (missing
`TCA`). The 3' ends are identical, so the binding sites are the same, and the
truncation can only lower the penalty an oligo accumulates — **the entry is a more
permissive assay than the paper's.**

The sizes confirm the reading rather than contradict it. Table 3's locations give
571 − 287 + 1 = 285 bp and the text says "the specific 284 bp product", while 285
minus the 7 and 3 dropped bases is **275** — exactly the stored `amplicon_bp`, and the
2026-10-17 calls measure 275 bp in **467 of 468** detected-or-reduced records. So
`amplicon_bp: 275` is right for the oligos as stored and wrong for the citation.

Not changed: substituting 139/141 changes every call for this assay and is a
maintainer's decision, as with the Chlamydia genus 16S primer kept as printed on
2026-10-17. Flagged `OLIGOS_TRUNCATED_VS_PAPER`. Note that the validation case
backing this entry — Malorny 2003, 99.6% inclusivity on 364 strains — validated
139/141, not this pair.

### Why eight months of verification missed it: two bugs in the verifier

The paper has been on disk all along, and
`results/oligo-verification.tsv` says `no-full-text`, "no local PDF; needs the PDF".
Two independent causes, both in `scripts/verify_oligos_against_paper.py`:

1. **Parenthesised DOIs are unreachable.** The `papers/` convention maps `/`, `(` and
   `)` all to `_`, and the reverse mapping at line 409 undoes only `/`. This file's
   stem reconstructs as `10.1016/0890-8508/92/90002-f`, which still `fullmatch`es the
   DOI pattern — so the paper is indexed under a DOI nothing asks for, *and* counts as
   "named", which bars it from the surname-and-year fallback. Doubly unreachable.
   **Ten PDFs on disk, covering 20 registry entries, have parenthesised DOIs**,
   including Meyer 1997 ATI and Lozano 1997, both of which this session read by hand.
   The fix is to forward-map each registry DOI to a filename rather than reverse-map
   filenames, which is unambiguous.
2. **All-lowercase sequences are invisible.** `printed_oligos` requires ≥60% upper
   case on the stated premise that "papers set sequences in capitals and use lower
   case only for degenerate codes". Rahn sets both primers entirely in lower case, so
   the reader extracts **0 oligos** from a text that contains both. Relaxing the case
   rule is a reader re-calibration and belongs in `scripts/diff_printed_oligos.py`,
   which exists to measure LOST/GAINED against an old revision — not in a patch made
   on one paper's evidence.

Either bug alone hides this entry; together they guarantee it. Bug 1 is the bigger
one, because it silences 20 entries' verification against papers that are present.

## What this leaves

1. **Scope curation is not the lever point 3 took it for.** Thirteen override cases
   with a readable design paper were triaged and the firing lineage was in range in
   every one of them. Three of the thirteen fire on a lineage the paper amplified on
   the bench (rabies, BFDV, PPRV), two on its prototype or design species (LCM,
   AAV). The lineages that fire are the assays' own targets, so the override's
   problem is what it measures, not which records are in the denominator. Only two
   scopes were worth shipping, and both move nothing today.
2. **Five worked examples for the `< pooled` gate**, from design papers rather than
   published follow-up: Enterovirus B (+41 points on 1,063 records), BFDV (+27.6),
   IBV (+19.8), LCM (+9.1), AAV (+7.0 on 1,525 records). None is a case in the
   `docs/validation-cases.tsv` sense, so none moves the confusion matrix, but as
   evidence against letting an above-pooled lineage drive `declining` this is now
   five independent papers rather than the single row the gate was refused on.
3. **One decision held for the maintainer**: `ADENOVIRUS_dsDNA_Hexon_gene`
   round1/2. Casas 2005's own range is human adenovirus (47 prototype HAdV serotypes,
   species A–F, clinical samples, no non-human adenovirus tested), but `as_written` is
   `PREDICT PROTOCOL`, a pan-adenovirus wildlife screening protocol, so the scope
   belongs to whichever source is operative. The triage narrows what hangs
   on it: round 1's override survives either way, since it fires on Human
   mastadenovirus C; only round 2's, firing on fowl adenovirus at 0/49, depends on the
   answer.
4. **Blocked, no identified source**: `CDV_H_gene_Mueller_2011_2`,
   `CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme`, both `HANTAVIRUS_ssRNA_S_segment`
   entries (the nest assignment has no source at all),
   `PARVOVIRUS_ssDNA_VP1_gene_pan_parvo`. Scope cannot be curated from a paper that
   is not identified.
5. **Two mechanisms, not scope, explain what is left.** `CORONAVIRUS_…_round2` fires
   on an NCBI holding pen (`lineage.unclassified_is_bucket`, shipped off),
   `ORTHOPOXVIRUS_dsDNA_ATI_Meyer_1997` on patent constructs
   (`drift.exclude_patent_records`, shipped off), and both flags exist already and are
   off for want of a tier-2 case. The remaining above-pooled cases want the `< pooled`
   gate. None of the three is a curation problem.
6. **The verifier needs the parenthesised-DOI fix** before any claim that an entry's
   oligos are unverifiable: 20 entries are currently reported `no-full-text` against
   papers that are on disk.
7. **`Pan_flavivirus_NS5_3`'s 0/428 on Usutu is the biggest unexplained number in the
   set** and is not scope, not a bucket and not patents. Scaramozzino's Table 3 would
   make a bench panel for it: six published genus primer pairs across about twelve
   viruses.
