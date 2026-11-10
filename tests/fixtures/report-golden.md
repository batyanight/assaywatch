# AssayWatch report — 2026-11-01

3 assays screened: 1 declining, 1 no recent data, 1 stable.

**In one line:** of 3 published assays re-checked against GenBank records deposited up to 2026-11-01, 1 appear to be detecting measurably less of their target than they once did, and 0 have never covered much of the taxon they are screened against. None cleared every confirmation check, so the Start here list below is empty -- which means the flags need looking at, not that nothing was found.

**What cannot be said at all:** 1 of 3 screened assays carry no usable verdict -- 0 with too few recent records, 1 with nothing newly deposited, and 0 not scoreable at all. Sparsely sequenced targets are exactly the ones this tool is for, and they are the ones it can say least about.

**What this is not.** Every number here is a prediction from sequence alone: whether each oligo still matches what has been deposited, never whether the reaction still works at the bench. No assay was run in a laboratory. There is no thermodynamic model and no limit of detection, so this cannot tell a missed cycle-threshold cutoff from a faint band. A flag is a reason to pull an assay's records and look, never a result.

**The verdicts.** `declining` -- detection has fallen from a level that previously cleared the threshold. `low coverage` -- detection is below the threshold but was never measurably higher, usually an assay screened against more diversity than it was designed for. `watch` -- below the threshold, but the interval still reaches it, so there are too few records to be sure. `insufficient data` -- too few recent evaluable records to judge; never flagged. `no recent data` -- nothing new deposited in the window. `stable` -- no evidence of loss. `not scoreable` -- a registry problem, such as an unresolved product size, rather than anything about the assay.

Registry status: 2 active, 1 draft. `draft` is a maintainer sign-off, not a data check: 0 of the 1 drafts here already carry a verified DOI, a taxid and a design year with no open review question. What does vary between entries is oligo provenance, flagged in the note column of every row below.

**Duplication check:** not run for this flagged assay: their binding-site footprints are unknown (the calls table includes screens from before the footprint columns were written, or counts diverged records as failures), so nothing can be said about whether the flags rest on duplicated records.

Recent window: 24 months; earliest shown Nov 2024; threshold 90% detected; at least 15 recent evaluable records to flag. Deprecated assays are not screened.

## Start here (0)

No flagged assay met the bar for this list.

Kept off this list but unchanged in the tables below: 1 carry a flag the duplication check did not confirm.

`detected` means predicted to amplify (`detect` or `reduced`). The denominator is
evaluable records only: those where both primers landed in the right orientation and
size range. Records with no amplicon, or too many undetermined bases to judge, are
counted separately and excluded, so a bad sequencing year cannot look like drift.
Intervals are Wilson 95%, pooled and per lineage alike. A **pooled** flag needs the
upper bound of the recent interval to fall below the threshold. **Declining** means the
share has also fallen from the baseline (the interval for the change excludes zero):
that is drift. **Low coverage** means below threshold without a measurable fall: usually
an assay screened against more diversity than it was designed for.

A **lineage** can also flag an assay whose pooled share clears the threshold, and that
is the point of measuring per lineage: a pan-family assay can miss one clade entirely
while detecting most of what is deposited. Such a row is marked `pooled: <status>` and
its note names the lineage, its share and its own earlier share. The lineage rule is
not the pooled one: it is an exact binomial test against the threshold,
Holm-adjusted across that assay's lineages, so it is the looser of
the two and nothing controls error across assays. Read a lineage override as a reason to look at
that clade, not as a measurement of the assay.

## Declining (1)

| assay | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `Encephalitozoon_cuniculi_PTP_Xiao_2001` | active | 20.0% | 10%-37% | 30 | 100% (20) | 1x negligible | unchecked | detected share 20.0% (10%-37%) since Nov 2024, upper bound below the 90% threshold; change from baseline -90% to -56%. Entry flags: amplicon_multimodal, thin_evidence. |

## No Recent Data (1)

| assay | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `Enterovirus_5UTR_VP4_VP2_Wray_2016_round1` | draft | - | - | 0 | 100% (3) | 16x moderate | - | no evaluable records deposited since Nov 2024. Entry flags: orientation_inferred. |

## Stable (1)

| assay | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `Aparavirus_apisacutum_capsid_Rossi_2024` | active | 100.0% | 84%-100% | 20 | 100% (18) | 4608x severe | - | detected share 100.0% (84%-100%) since Nov 2024. |

## Detail for flagged assays

**Duplication check:** not run for this flagged assay: their binding-site footprints are unknown (the calls table includes screens from before the footprint columns were written, or counts diverged records as failures), so nothing can be said about whether the flags rest on duplicated records.

### `Encephalitozoon_cuniculi_PTP_Xiao_2001`

Encephalitozoon cuniculi — polar tube protein (Xiao 2001)  
Designed 2001, doi:10.1128/JCM.39.6.2248-2253.2001  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 2018 | 20 | 20 | 100% |
| 2025 | 6 | 30 | 20% |

*trend over deposit year: not tested (fewer than 3 years with evaluable records, or no variation); by footprint: not available, the footprints are unknown for this calls table*

*hierarchical fit over 1 lineages: mu = 20.0%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Per species** (product size names the species here, 275-373 bp, so the share above pools readouts that mean different things; Nov 2024 on, no assessability floor):

| species | product bp | detected | evaluable | share |
|---|---|---|---|---|
| unresolved (no taxid) | - | 6 | 30 | 20% |

**Denominator:** 50 of 50 screened records are evaluable (100.0%); 0 are not. Every share above is taken over the evaluable ones.

## Coverage gaps

These assays cannot be validated against sequence data because the sequence data
does not exist. For wildlife pathogens this is usually the finding, not a caveat.
An assay with no taxid was never searched: that is a registry gap, not a data gap.

| assay | taxon | taxid | evaluable | screened |
|---|---|---|---|---|
| `Enterovirus_5UTR_VP4_VP2_Wray_2016_round1` | Enterovirus | 12059 | 3 | 5 |
