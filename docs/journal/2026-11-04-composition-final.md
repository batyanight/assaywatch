# 2026-11-04 — composition over all 215 assays, and the species split it did not deliver

**Finding: the graphs are live on every assay and sum to the detection chart exactly, but step
4b's clean species split does not survive the full data.** Single linkage at the 0.05 cut chains
species together: Messmer 16S puts 14 species in one group of 687 records. Labels were tested and
hold, so this is the clustering and not the deposits. Published at 0.05 by the maintainer's
decision, with pages calling these sequence groups, naming each group's species, and saying so
where the largest group is mixed. Composition moves no status.

## The build

`assaywatch composition` on the 2026-11-01 calls with `--coverage`: 219 assays, 3 h 55 min, 12.1 GB
peak resident (11.4 GB on the earlier run without coverage), sharing the machine. `rule composition`
now reads `mem_mb=13000, runtime=300`. The 4 GB first set counted the calls table and one assay's
k-mer matrix. Per-assay time is not logged, so influenza M has no time of its own; the record count
is 184,887.

**Merged, not one command.** The final build read the registry before the day's scope edits. The
26 changed entries were rebuilt and swapped in, by the maintainer's decision, since a rebuild would
have gone stale with each later scope choice. The condition held: the four Bd assays rebuilt alone
equal the full build field for field. The next scheduled run replaces this with a single build.

## Step 18's checks

| check | result |
|---|---|
| cells per year against the graph's evaluable | 0 mismatches over 215 assays, after the merge |
| status against the run without composition | only the two Uccellini changes, which are scope decisions |
| `website/data/composition.json` | 492 KB against the 1.5 MB cap |
| coverage against archive `created` counts | Messmer 1,668 and 1,668; HaemF 32,073 and 32,060; Wellehan 39,027 and 39,067; one year off by over 20%, 1993 in Wellehan, 113 and 73 |
| Messmer species split | **failed as written** |
| Haemosporida | **partly**, below |
| three pages by eye | done, and they found two faults, below |

**Messmer.** Expected *psittaci*/*abortus*, *trachomatis* + *muridarum*, *pecorum*, *pneumoniae*.
Found: one group of 687 holding *trachomatis* 354, unnamed *Chlamydia* 104, *psittaci* 66,
*muridarum* 57 and others. That group merges two populations, *trachomatis* all `fail` and
*psittaci* all `reduced`, so the same-mix line sees a shift between them as change within one
lineage. The expectation came from 76 sampled windows; the cut journal of 2026-11-03 warned that
a rule found on a small sample failed at size, and step 18 still carried the small sample's result.

**Is it mislabelling?** No. Each record's amplicon against each species' commonest amplicon: all
362 *trachomatis* nearest *trachomatis*, and 104 of 112 *psittaci* nearest *psittaci* with the other
8 nearest *abortus*. No *psittaci* record is nearest *trachomatis*. The amplicons are about 88%
identical, and the window is about 1,360 bp of conserved 16S, where records link across species.

**Haemosporida.** Among the species each group lists, genus purity is 100%. The listing is the top
species only, so that is an upper bound. *Plasmodium* is 86% in one group and *Haemoproteus* 79%
on the same listing, under the 90% asked. No *Hepatocystis* appears, so that half of the check
can't be read on this scope. Step 4b's 83% was measured differently and is not comparable.

## A lower cut is not a clean fix

Purity, the share of a group's named records in its top species, and completeness, the share of a
species in one group:

| assay | at 0.05 | at 0.02 |
|---|---|---|
| Messmer 16S | purity 0.64, 5 groups | 0.76, 7 groups, *trachomatis* + *muridarum* clean |
| HaemF | purity 0.31, 2% pooled as other | 0.74, 24% pooled as other |
| *Leptospira* lipL32 | purity 0.60, completeness 1.00 | 0.90, completeness 0.64 |
| Quan coronavirus | purity 0.82, completeness 0.80 | 0.88, completeness 0.76 |
| Fox *Helicobacter* 16S | purity 0.37, 2 groups | unchanged |
| Ranavirus MCP | purity 0.34 | 0.41 |

In 17 of the 199 assays with named groups, the largest holds 3 or more named species with none at
80%. Per-assay cuts and average linkage are on the roadmap.

## What the pages showed

- **"Every evaluable record is one lineage"** was false on Messmer, 814 records across many species.
  The sentence ran whenever one lineage had enough recent records to report. It now says that.
- **The species table did not exist.** The published choice relied on one. The site file now carries
  each group's top three species and the table prints them.
- **A withheld page with nothing to draw went silent.** *Francisella* detects all 1,021 evaluable
  records. It now says no position stands out. Withheld pages show the map unless the entry's oligos
  are in doubt or its readout isn't an amplicon (`review.MAP_HIDDEN`).

## Also found while checking withheld pages

**Zimmermann round 2.** The page prints `GCC TTG TGT TTC TAT CTT TC`, by eye and in the text layer.
All 303 records with the site read otherwise, 260 of them `GTTTG`, including the design source's own
deposit M99375. Two G to C changes in the last 5 bases, one terminal, and the paper's nested PCR
worked. Probably a print error, which is an inference: nothing shows what was synthesized. Next run
scores the corrected form, keeps the status withheld, and warns that the printed primer fails.

**Francisella FT443.** The probe is `TCGTAATGTTAGCTGTATCATCATT`, exact in all 1,021 products at
product position 50, which is gene position 443. The entry's "8 mismatches" does not hold up. It goes
in at the next screen.

## Not done

- Per-assay composition time.
- MT730717's species: the remote BLAST ran for hours without returning and was stopped.
- The `limitations.md` counts stay dated 2026-10-31. They say so, and the date is what makes them true.
