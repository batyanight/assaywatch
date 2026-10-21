# Four design papers read for scope; none of the four cases was a scope error (2026-10-20)

`docs/2026-10-20-pan-family-override.md` point 3 proposed curating `scope_taxids`
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
  resting only on T:G mispairs (`docs/2026-10-19-fap-bench-panel.md`).
- **Barrett morbillivirus**: 3 false fails of 7, all three with a G·T wobble in the
  3' window.
- **Meyer ATI** is the other knob — its one false fail has no 3'-window mismatch at
  all (`docs/2026-10-20-meyer-ati-bench-panel.md`).
- **Rebelo Mycoplasma** disagrees nowhere and has no 3'-window mismatch anywhere, so
  neither change disturbs it.

And it reinterprets one of the override cases: PPRV at **0/83** looked like a
coverage finding, and Barrett's own PPRV reference scores `fail` on `rev3 G:T` plus
`fwd4 C:C`. The 0% is at least partly the 3'-window penalty. **No config change
here** — an identity-aware `score_primer` is a threshold decision and goes through
tier-2 first.

## What this leaves

1. **Scope curation is not the lever point 3 took it for.** Four for four, the firing
   lineage was in range. The lineages that fire are the assays' own targets, so the
   override's problem is what it measures, not which records are in the denominator.
2. **Two more worked examples for the `< pooled` gate**, from design papers rather
   than from published follow-up: BFDV detects 27.6 points better than the pool and
   is one of three design sequences; LCM detects 9 points better and is the family
   prototype. In both the override names as "failing" the taxon its paper most
   directly demonstrates. That is not a validation case in the `docs/validation-cases.tsv`
   sense and will not move the confusion matrix, but it is direct evidence against
   letting an above-pooled lineage drive `declining`.
3. **Still untriaged, papers on disk**: `ADENOVIRUS_dsDNA_Hexon_gene` round1/2
   (**held** — Casas 2005's own range is human adenovirus A–F on 47 prototype
   serotypes, but `as_written` is `PREDICT PROTOCOL` and the lab uses ADHEX as a
   pan-adenovirus wildlife screen, so this is an Atkins/PREDICT-style composite and
   the call is the maintainer's), `ADENOVIRUS_dsDNA_Polymerase_Primate_speci_Casas_2005`,
   `CORONAVIRUS` Lan 2010 round1 and round2, `ENTEROVIRUS_ssRNA_VP3_VP1_round2`,
   `PARVOVIRUS_ssDNA_VP1_gene_dependovirus`, `Pan_flavivirus_NS5_3` round1/2,
   `ORTHOPOXVIRUS_dsDNA_ATI_Meyer_1997` (already explained by patent records).
4. **Blocked, no identified source**: `CDV_H_gene_Mueller_2011_2`,
   `CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme`, both `HANTAVIRUS_ssRNA_S_segment`
   entries (the nest assignment has no source at all),
   `PARVOVIRUS_ssDNA_VP1_gene_pan_parvo`. Scope cannot be curated from a paper that
   is not identified.
5. **A full run is owed on the current config.** The newest valid calls table is
   2026-10-17, three days and several drift-time changes old, and the 2026-10-18 one
   should not be read again.
