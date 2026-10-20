# Orthopox ATI on vaccinia: the lineage is 90% patent constructs (2026-10-19)

Follow-up to `docs/2026-10-19-taxid-artefacts.md`, where the species roll-up turned
ORTHOPOXVIRUS_dsDNA_ATI_Meyer_1997 from `stable` to `declining` on a vaccinia
lineage at 83.0% of 112, and left it to be read by hand. **Evidence:**
`results/2026-10-17/calls.tsv.gz` with current IDs, as of 2026-10-17, species
roll-up on.

## The lineage, by hand

112 recent evaluable records roll up to vaccinia (10245). Split by what the
deposit is:

| | detected | records | share |
|---|---:|---:|---:|
| GenBank patent division | 83 | 101 | 82.2% |
| ordinary deposits | 10 | 11 | 90.9% |
| **all** | **93** | **112** | **83.0%** |

The 101 patent records are vaccinia vectors from patent applications: "SYNTHETIC
CHIMERIC VACCINIA VIRUS", "RECOMBINANT POXVIRUSES FOR CANCER IMMUNOTHERAPY",
"MODIFIED ORTHOPOXVIRUS VECTORS", "CHIMERIC POXVIRUSES" (JP and KR filings).

The 11 ordinary records are 8 natural isolates and 3 clones, and **the one failure
among them is also engineered**: `PV358350.1`, "UNVERIFIED: Mutant Orthopoxvirus
vaccinia isolate MVA-syn4-contig1_pilon", a synthetic MVA. Its mismatch pattern
(forward 14,13,9,6,3,2 from the 3' end, amplicon 1226 bp) is identical to the
patent MVA constructs, so it is the same construct family deposited outside the
patent division.

Every genuinely natural vaccinia record detects: Cantagalo isolates (5, 1547 bp),
Buffalopox (3, 1587 bp), VG9 (1615 bp), CEPHR_IRE_2026 (1606 bp). **10 of 10.**

## Why the constructs fail, and why that is uninformative

The failures carry amplicons of 891, 1001 and 1226 bp. Natural vaccinia measures
1594-1606 bp (the registry entry's own species-size table). The ATI gene is a
standard insertion and deletion site in poxvirus vectors, so these are records
where the amplified region has been engineered away or replaced. By the assay's
own logic — species identified by product length — such a product is not
interpretable anyway: it matches no species size.

An assay that fails to amplify a laboratory construct has told us nothing about
whether it detects circulating vaccinia. The `declining` verdict was a false
positive, and the pooled 95.3% that the lineage overrode was the better number.

## Scale: patent records across the archive

21,769 of 1,530,526 archived records (1.4%) are patent deposits, but they
concentrate in exactly the assays whose targets are used as vectors:

| assay | patent share of recent evaluable | patent fails | natural fails |
|---|---:|---:|---:|
| PARVOVIRUS_ssDNA_VP1_gene_dependovirus | 2182/2456 (88.8%) | 344 | 143 |
| PARVOVIRUS_ssDNA_VP1_gene_dependovirus_2002 | 2184/2459 (88.8%) | 10 | 3 |
| PARVOVIRUS_ssDNA_VP1_gene_pan_parvo | 2009/2958 (67.9%) | 3 | 222 |
| ARENAVIRUS_ssRNA_S_gene | 20/51 (39.2%) | 3 | 21 |
| CMV_UL55_gB_Deckers_2009_round2 | 11/36 (30.6%) | 3 | 0 |
| ORTHOPOXVIRUS ATI (vaccinia lineage) | 101/112 (90.2%) | 18 | 1 |

AAV is the extreme: the dependoparvovirus assays are measured almost entirely on
capsid-engineering patents.

## Identifying them

`esummary`'s `<Extra>` field carries GenBank's own division marker
(`gi|2896609882|dbj|PC415960.1||pat|JP|2021522784|5` against `|gb|` for an
ordinary record). `retrieve.py` now reads it into an `is_patent` column.

Archives fetched before that column existed are covered by the deposit title,
which for a patent record usually names the patent. `assaywatch/metadata.py` holds
the patterns and `read_patent_accessions`; the column wins where it exists.

**Correction, 2026-10-20.** This section first claimed the title pattern agreed
with `<Extra>` on all 300 sampled records, which was true but measured the wrong
thing: a random sample over 1.5M records tests false positives well and false
negatives hardly at all. Counted properly, the archive holds 21,769 records whose
title is the patent citation, plus two classes the first pattern missed — 152
titled "Patent application sequence for WO ...", now matched, and about 517 whose
title is only the invention name ("Modified Microbial Nucleic Acid",
"RESEQUENCING PATHOGEN MICROARRAY"), of which all 114 sampled came back `|pat|`.
No pattern can catch that last class, so the fallback undercounts patents by
roughly 3% and never over-counts. The clean fix is a one-off `is_patent` backfill
sidecar, as `data/retrieved/.meta.taxid.backfill.tsv.gz` already does for taxids;
a targeted one over the taxa where patents concentrate would be far cheaper than
the whole archive. Found via camelpox, where two of the ATI assay's `fail` records
are patent deposits titled "Modified Microbial Nucleic Acid".

## `drift.exclude_patent_records`, shipped off

The switch drops patent records from the drift denominator and counts them on
`AssayDrift.patent_excluded`, as `out_of_scope` already does.

**Tier-2 is unchanged** with it on or off (4/11 caught, 12 disagreements): no
validation case names an affected assay, so the validation set cannot approve a
denominator change here. That is why it ships off, even though the ATI case above
is a hand-checked false positive.

Six current statuses would move:

| assay | off -> on | reading |
|---|---|---|
| ORTHOPOXVIRUS ATI Meyer 1997 | declining -> **stable** | the case above; 11 natural records fall below `min_records_per_lineage`, so no override |
| CMV_UL55_gB_Deckers_2009 | watch -> stable | |
| PARVOVIRUS dependovirus | declining -> low coverage | |
| ARENAVIRUS_ssRNA_S_gene_2 | declining -> low coverage | now "fell measurably, but never reached the threshold" |
| ARENAVIRUS_ssRNA_S_gene | low coverage -> **declining** | the patents were detected; without them the fall is measurable (-39% to -6%) |
| Yersinia_pseudotuberculosis_Wang_1997 | stable -> insufficient data | 19 records, below the minimum of 20 |

The two arenavirus moves go in opposite directions and neither has been read by
hand. They are what a validation case for this option would have to settle.

## Per-species shares in the report (added 2026-10-19)

The entry's `needs_review` already said to read this assay by species, not by a
genus-wide share, so the report now does. An assay declaring `amplicon_bp_range`
— ATI is the only one, and the field means its product size varies by species by
design — gets a per-species table in its report detail section, markdown and HTML:

| species | detected | evaluable | share |
|---|---:|---:|---:|
| Orthopoxvirus monkeypox (3431483) | 4143 | 4334 | 96% |
| Orthopoxvirus vaccinia (10245) | 93 | 112 | 83% |
| Orthopoxvirus cowpox (3431481) | 18 | 18 | 100% |
| Orthopoxvirus camelpox (3431480) | 1 | 1 | 100% |
| Orthopoxvirus ectromelia (3431482) | 1 | 1 | 100% |
| Orthopoxvirus variola (3431487) | 1 | 1 | 100% |

**No assessability floor**, unlike the per-lineage check: the species this assay is
rarely asked about are the ones a size-differentiating readout exists for, and
`min_records_per_lineage: 30` would drop four of these six. A share of one record
is left to speak for itself next to its denominator. Counts come from
`AssayDrift.species_counts`, the recent window's evaluable records rolled up to
species by `lineage.group_at_rank`, so the table and the lineage verdict are the
same numbers.

Lineages are also named now. `docs/taxa-cache.json` holds ten hand-entered names,
so almost every label read `taxid_10245`; the taxonomy cache names 23,593 species
for free, and `lineage.name_lineages_from_taxonomy` fills the gaps as
"Name (taxid)" without overwriting a hand-written label. Tier-2 and all 201
current statuses are byte-identical before and after, as they must be: the label
is a display string and a grouping key, and nothing reads `LineageStats.taxid`.
The cache keeps species names as well as the "unclassified" ones, 394 KB -> 606 KB.

## `species_sizes`, measured (added 2026-10-19)

The entry now carries the per-species product length as data, not prose, and the
report's table shows it beside each share:

| species | product bp | detected | evaluable | share |
|---|---|---:|---:|---:|
| Orthopoxvirus monkeypox (3431483) | 1535-1545, 1067 | 4143 | 4334 | 96% |
| Orthopoxvirus vaccinia (10245) | 1587-1615, 1547, 1671, 1573 | 93 | 112 | 83% |
| Orthopoxvirus cowpox (3431481) | 1598-1601, 1673, 1505 | 18 | 18 | 100% |
| Orthopoxvirus camelpox (3431480) | 879 | 1 | 1 | 100% |
| Orthopoxvirus ectromelia (3431482) | 1220 | 1 | 1 | 100% |
| Orthopoxvirus variola (3431487) | 1576-1583 | 1 | 1 | 100% |

Measured by `scripts/measure_species_sizes.py` over the whole archive (the table
above is the recent window, so a species' bands can rest on more records than its
share does), not copied from the paper or from the earlier hand pass: the rule is
measure, never quote, and this assay's paper sizes are already known to differ by
1-32 bp. Patent records are excluded, which matters here more than anywhere —
their 891, 1001 and 1226 bp products would have entered the registry as vaccinia
bands. Schema: `SpeciesSize` (taxid, bp [min, max], n_records, note), several rows
per species allowed, and the validator requires `amplicon_bp_range`, which is the
declaration that makes per-species bands mean anything.

**Clustering.** A length is kept at >= 2 records and >= 2% of the species'
records; the survivors cluster where a step exceeds 12 bp. Dropping thin lengths
*before* clustering is what makes the bands honest: across 12,539 monkeypox
records the rare lengths form a continuum, and clustering them too chains 1520
through 1590 into one band that swallows variola and vaccinia, where the real
clade IIb band is 1535-1545.

**What the bands show about the assay.** They are not a key. Vaccinia 1587-1615,
cowpox 1598-1601, variola 1576-1583, Cowpox-Vaccinia 1601 and monkeypox clade IIb
1535-1545 all crowd the same stretch, so a band near 1600 bp names no single
species — which is why Meyer's protocol also ran an XbaI digest, and what the
entry's `DIFFERENTIATION_ASSAY_SIZE_AND_XBAI_DIGEST_NOT_SCREENABLE` flag means in
numbers. Cleanly separated: camelpox 879, ectromelia 1220, volepox 542,
monkeypox clade I 1067.

The remeasurement agrees with the 2026-10-06 hand pass and adds bands it missed
(vaccinia 1547 and 1671, cowpox 1598-1601 and 1505, akhmetapox 1505, taterapox
1628). It drops skunkpox, whose two 551 bp records score `fail`.

## Next

- Validation cases for the arenavirus S gene assays and for an AAV/dependoparvovirus
  assay, which is what would let the patent option ship on.
- Skunkpox has no band because its two records score `fail`. `fail` is this
  pipeline's judgement at one threshold, not a bench result, and ATI runs at 40 °C
  annealing, so the 551 bp product may well be real. A bench panel
  (`scripts/bench_panel.py`) from Meyer's own species set would settle it.
