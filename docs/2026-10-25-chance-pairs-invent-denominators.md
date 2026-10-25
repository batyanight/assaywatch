# Chance primer pairs are inventing denominators, and one ACTIVE entry reads 42% when it is 100%

Found while confirming that the three parapoxvirus entries added 2026-10-24 would be screened
by the pipeline rather than by hand. They were (full run 2026-10-25, 434/434 steps, 29m 09s,
exit 0). The Orf entry came back at 75.0% where its entry note recorded 100%, and chasing that
gap found a scoring artefact that is **not specific to Orf** and that currently misstates the
verdict of an **active** assay.

**Nothing was changed.** The lever is a scoring threshold in `config.yaml`, and a denominator
change is a maintainer decision. This prices it.

## The mechanism

`drift.max_pair_evalue: 0.01` keeps any amplicon whose pair E-value is below 0.01, and
`max_mismatches_searched: 6` lets an oligo be placed with up to 6 mismatches. Together they
admit a record that does **not carry the assay's target** as long as the two primers can be
placed somewhere in it by chance. The record then becomes `EVALUABLE`, the probe is absent
because the target region is absent, and the row scores `fail`.

That is a denominator the pipeline would never knowingly use. It is the same lesson the Congo
Basin assay taught on 2026-10-24 — *a gene that is not there is silent, not negative* — reached
by a different route: not gene absence correctly seen as `no_site`, but gene absence disguised
as a weak site.

The separation is not subtle. For `ORF_VIRUS_dsDNA_RPO147_J6R_TaqMan_Zhao_2013`:

| | pair_evalue | fwd / rev penalty | probe site |
|---|---|---|---|
| 88 genuine `detect` | 1.6e-19 .. 7.7e-15 | low | present |
| 76 artefact `fail` | 4.1e-5 .. 8.4e-4 | 6.5 / 6.5 | absent |

**Ten orders of magnitude**, and every artefact row still passes a 0.01 cutoff. All 76 are
genuine *Orf virus* records, but they are **B2L (major envelope protein) partial sequences**,
395–1557 bp, and this assay targets **RPO147 (J6R)**. The gene is not in the record.

For `OPHIDIOMYCES_ophidiicola_targetD_Haynes_2023` the same shape with worse numbers: penalties
`(6.5, 9)`, `(7, 9)`, `(6, 8.5)` against a `reduced_max` of **3.0**, and pair_evalues 2.5e-4 to
9.7e-3 — within a factor of four of the cutoff. These records are the right organism, *O.
ophidiicola* whole-genome-shotgun **scaffolds**; a scaffold either carries targetD or it does
not, and 25,401 correctly score `no_amplicon`. These 111 chance-paired instead.

## What it costs, measured over every latest screen (134 groups)

Counting only **probe-chemistry** assays (a probe-less row says nothing about an assay that has
no probe — `ORTHOPOXVIRUS_dsDNA_ATI_Meyer_1997` is `conventional` and its 114 such rows are not
this), with an absent probe site and `pair_evalue > 1e-6`:

| assay | artefact rows / evaluable | entry | verdict effect |
|---|---|---|---|
| `OPHIDIOMYCES_ophidiicola_targetD_Haynes_2023` | **111 / 192** | **active** | **42.2% reported vs 100.0% genuine** |
| `Snake_fungus_Ophidiomyces_ophi_IGS_Bohuski_2015` | 21,536 / 21,563 | active | none: 0 evaluable in the recent window, so "no recent data" |
| `Snake_fungus_Ophidiomyces_ophi_ITS2_28S_Bohuski_2015` | 6,552 / 6,607 | active | none: 8 recent, under the 15 minimum |
| `B_salamandrivorans_Internal_transcribes_spa_Blooi_2013` | 475 / 524 | active | none: 5 recent, under the minimum |
| `ORF_VIRUS_dsDNA_RPO147_J6R_TaqMan_Zhao_2013` | 76 / 164 | draft | 75.0% recent reported; 100% genuine over the whole archive |
| `MYCOBACTERIUM_TB_complex_IS1081_Hermes_2018` | 1 / 1,173 | active | none |

**28,751 rows in six assays**, but only two verdicts move, because the recent-window and
minimum-evaluable gates absorb the rest. That is the honest summary: a large artefact with a
narrow consequence — and the one consequence is on an active entry.

### The active entry, exactly

`OPHIDIOMYCES_ophidiicola_targetD_Haynes_2023`, over all its latest screens:

    all calls      no_amplicon 25,401   fail 111   detect 81
    as reported    81 detected of 192 evaluable  =  42.2%   ("upper bound below the 90% threshold")
    artefact out   81 detected of  81 evaluable  = 100.0%

**Every one of its 111 non-detections is a chance pair. It has no genuine failure.** It is
reported under *Low Coverage* at 42.2%, which is wrong in a direction that matters: it describes
a working assay as one that misses more than half of what it should find.

For Orf the whole-archive figure is likewise 88 of 88 genuine evaluable, **100%**, which
reproduces the entry note's hand screen ("64 evaluable, 100% `detect`, not one reduced or
failed") exactly. The hand screen was right. It used complete genomes, which carry RPO147; the
pipeline's archive adds B2L partials, which do not. I have **not** checked how many of the 9
non-detections inside Orf's *recent window* are artefacts, so treat its 75.0% as suspect rather
than as a known 100%.

## The guard any fix must not break

The obvious reading — "an evaluable row with no probe site is not evaluable" — is **wrong**, and
this project already holds the counterexample. `MONKEYPOX_dsDNA_G2R_WestAfrican_TaqMan_Li_2010`
has 2,688 failures with `fwd_penalty` **0**, `rev_penalty` **0**, no probe site, and an 82 bp
product instead of 85 bp. Those are clade I records that the conserved primers genuinely
amplify and the clade-II-specific probe genuinely does not bind. The record *is* evaluable and
the failure *must* count; `docs/RESUME-HERE.md` calls that the broken denominator worth keeping.

So the discriminator is **never the probe's absence**. It is whether the primer placement is
real: penalty and `pair_evalue`. A fix keyed on the probe would silently repair Ophidiomyces and
destroy the one finding the mpox pair exists to show.

## Options, unpriced beyond this document

1. **Lower `drift.max_pair_evalue`.** The gap is enormous (7.7e-15 vs 4.1e-5 in Orf), so
   anything from 1e-6 to 1e-10 separates genuine from chance in every case here. It is a
   registry-wide denominator change and wants the same treatment `drift.anchor_fdr` got: a
   full re-price against the scoped registry before shipping.
2. **Require a plausible primer placement, not just a sub-cutoff pair.** A penalty of 9 against
   `reduced_max: 3.0` is not a site. This is narrower than (1) and closer to the actual defect.
3. **Per-entry retrieval queries.** `ORF_VIRUS` and `BPSV` both carry `query: null`, so they
   fetch every record for their taxid including off-target-gene partials; most entries that hit
   this problem earlier gained a query. This fixes Orf without touching a threshold, but does
   nothing for the Ophidiomyces scaffolds, which are the right organism and the right taxid.

Option 2 looks like the defect and option 1 is the blunt instrument that certainly works.
Neither is a session's to ship.

## Not affected, checked

The other two parapoxvirus entries screened clean on this criterion: every failure of
`Pan_PARAPOX_..._generic` (4) and `BPSV_...` (2) has a real probe site and a pair_evalue from
4e-8 to 6.6e-19. Their entry notes' hand figures stand. Across the whole run only 3 of 146
pre-existing scored assays moved at all, each by ≤0.2 points from new deposits, and no status
changed; the six rows new to the report are yesterday's six new entries.
