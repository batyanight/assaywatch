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
which for a patent record is the patent citation: `^[A-Z]{2} [\d/]+-[A-Z]\d*/\d+:`.
Checked against `<Extra>` on 300 records sampled from the archive (150 title
matches, 150 not): **agreement on all 300**. `assaywatch/metadata.py` holds the
pattern and `read_patent_accessions`; the column wins where it exists.

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

## Next

- Validation cases for the arenavirus S gene assays and for an AAV/dependoparvovirus
  assay, which is what would let this option ship on.
- The ATI entry's `needs_review` already says to interpret it by species, not by a
  genus-wide share. The species roll-up is what made that bite; the registry entry
  and the report should probably carry per-species shares for a size-differentiating
  assay.
