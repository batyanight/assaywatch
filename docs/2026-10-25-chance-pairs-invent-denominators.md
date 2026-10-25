# Chance primer pairs are inventing denominators, and one ACTIVE entry reads 42% when it is 100%

> **Second correction, same day: every SCOPE figure below is wrong, by about a hundredfold.**
> They were measured by globbing `results/screened/*/*/*.tsv`, which keeps the screens of
> **orphan** groups that no live assay retrieves and nothing rescreens - including a
> Rhabdoviridae screen dated 2026-10-03, before `amplicon.declared_tolerance` shipped. From
> `results/2026-10-25/calls.tsv.gz`, which is what the report is built from, the true figure is
> **277 rows across 11 probe-bearing assays out of 924,755 evaluable**, not 26,691 across 6.
> **The two verdicts that move are unchanged** - those were read from the report, not the glob -
> and so is everything about the mechanism and the guards. The three `mgb` fungal assays do not
> appear in the corrected list at all. Full correction and the corrected table:
> `docs/2026-10-25-stale-orphan-screens.md`.

> **First correction, same day.** The criterion below was first written as `pair_evalue > 1e-6`
> alone. **That is invalid and the figures keyed to it were wrong.** A short amplicon in a long
> genome legitimately scores a high pair E-value, because the statistic scales with the search
> space: `RANAVIRUS_dsDNA_Major_capsid_protein_MCP_Pallister_2007` produces a real **57 bp**
> product in a **~99 kb** complete genome at `pair_evalue` 2e-5, with `fwd_penalty` 2.5,
> `rev_penalty` 2 — both inside `reduced_max` — and **the probe site present**. Those rows are
> genuine failures on penalty and must count. Keying on the E-value alone briefly suggested
> that five assays, three of them `active` ranavirus entries on `Watch`, would cross the 90%
> threshold. **They do not. That claim is withdrawn.**
>
> The sound criterion adds the primer condition and is used throughout below: a `fail` row
> whose **probe site is absent** *and* whose **both primers exceed `reduced_max: 3.0`**. The
> probe is what makes it sound — it is the target locus's signature, so its absence alongside
> two implausible primers means the record does not carry the locus. That also bounds the
> scope: **probe-bearing assays only.** A conventional assay has no probe and therefore no
> target-presence test, so for those the question is open — see "What this does not settle".

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

The separation is not subtle, though the E-value is not by itself what shows it (see the
correction above). For `ORF_VIRUS_dsDNA_RPO147_J6R_TaqMan_Zhao_2013`:

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

Probe-bearing assays, `fail` rows with the probe site absent and both primers above
`reduced_max: 3.0`. Rates are whole-archive, so they are not the report's windowed figures.

| assay | chem | artefact / evaluable | reported | artefact removed | entry | verdict effect |
|---|---|---|---|---|---|---|
| `Snake_fungus_Ophidiomyces_ophi_IGS_Bohuski_2015` | mgb | 19,618 / 21,563 | 0.1% | **1.4%** | active | none: 0 evaluable in the recent window, so "no recent data" |
| `Snake_fungus_Ophidiomyces_ophi_ITS2_28S_Bohuski_2015` | mgb | 6,450 / 6,607 | 0.8% | **31.8%** | active | none: 8 recent, under the 15 minimum |
| `B_salamandrivorans_Internal_transcribes_spa_Blooi_2013` | mgb | 435 / 524 | 4.4% | **25.8%** | active | none: 5 recent, under the minimum |
| `OPHIDIOMYCES_ophidiicola_targetD_Haynes_2023` | hydrolysis_probe | **111 / 192** | 42.2% | **100.0%** | **active** | **the one verdict that is wrong** |
| `ORF_VIRUS_dsDNA_RPO147_J6R_TaqMan_Zhao_2013` | hydrolysis_probe | 76 / 164 | 53.7% | **100.0%** | draft | 75.0% recent reported, suspect |
| `MYCOBACTERIUM_TB_complex_IS1081_Hermes_2018` | hydrolysis_probe | 1 / 1,173 | 99.9% | 100.0% | active | none |

**26,691 rows in six assays, out of 53,216 probe-bearing evaluable rows**, and only two
verdicts move, because the recent-window and minimum-evaluable gates absorb the rest. A large
artefact with a narrow consequence — and the one consequence is on an active entry.

**Removing the artefact does not rescue the three `mgb` fungal assays**, and that is worth
saying plainly: IGS goes 0.1% → 1.4%, ITS2/28S 0.8% → 31.8%, *B. sal* 4.4% → 25.8%. All three
remain far below any threshold, so they have a large genuine problem that this artefact was
merely sitting on top of. Only `targetD` and `ORF_VIRUS` are fully explained by it, and both go
to exactly 100.0%.

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
Neither is a session's to ship. **Option 1 on its own is now known to be wrong**: see the
correction at the top — a sub-cutoff pair E-value is a property of amplicon length against
search space, not of credibility, so lowering `max_pair_evalue` would discard the genuine 57 bp
ranavirus products along with the chance pairs.

## What this does not settle

**Conventional and SYBR assays cannot be assessed by this method at all.** They have no probe,
so there is no target-presence signal to pair with the penalty test, and the two blanket
criteria tried here both fail on them in opposite directions:

- `pair_evalue` alone flags genuine short amplicons in long genomes (the ranavirus case).
- "both primers above `reduced_max`" alone flags genuine divergent records that the assay
  really would miss — which for a conventional assay is the finding, not an artefact. Applied
  to conventional entries it marks 4,866 rows in `LYSSAVIRUSES_ssRNA_Nucleoprotein_gene` and
  4,524 in its round 2, and those are plausibly real coverage failures against divergent
  lyssaviruses. **No conventional-assay number in this document should be treated as an
  artefact count.**

So the general problem needs a test for *is the target locus present in this record*, which is
what `no_amplicon`/`no_site` is supposed to encode and what these rows slipped past. For
probe-bearing assays the probe supplies it. For the rest it would have to come from an anchor
inside the target region — close to the machinery `anchor_evalue` already builds for
`no_amplicon` rows, which is suggestive: **the anchor test runs on `no_amplicon` rows only, so
the adjacent failure mode in `fail` rows has no equivalent guard.** That symmetry is probably
where a real fix lives.

## Not affected, checked

The other two parapoxvirus entries screened clean on this criterion: every failure of
`Pan_PARAPOX_..._generic` (4) and `BPSV_...` (2) has a real probe site and a pair_evalue from
4e-8 to 6.6e-19. Their entry notes' hand figures stand. Across the whole run only 3 of 146
pre-existing scored assays moved at all, each by ≤0.2 points from new deposits, and no status
changed; the six rows new to the report are yesterday's six new entries.
