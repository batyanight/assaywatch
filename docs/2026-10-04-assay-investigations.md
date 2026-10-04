# Why three flagged assays are flagged (2026-10-04)

Follow-up to the first-run review. Each assay below was below threshold or
"declining". Their failures were broken down by mismatch pattern, record source
and year, and the records behind the dominant pattern were identified. In all
three, the failures come from one consistent variant in particular lineages, not
from a gradual change over time.

## E. coli malB promoter, Candrain 1991: lineage variant, not drift

* All 92 failures in the assembly sample carry the same single change: the
  record has **G where the reverse primer's 3'-terminal base is A**
  (`CACACGCTGACGCTGACCA`). All 231 detects carry the A. The config treats any
  mismatch at the 3'-terminal base as a fail.
* The variant is old and steady. It is present every year from 2007 on, at 3–11
  sampled genomes a year, in long-studied commensal strains (HS, SE11, IAI1).
  No O157 genome carries it.
* The share rose from 25% of baseline genomes to 43% of recent ones because
  recent years' samples include more of those lineages. This is sampling
  composition, not a primer site changing over time.
* **What it means:** the assay misses roughly a quarter to a third of *E. coli*
  genomes because of a lineage-specific variant under its 3' end. That is a
  coverage limit worth stating. Treat it as "declining" only if the lineage mix
  of real samples is shifting the same way.

## Ranavirus MCP, Pallister 2007: a different clade, not drift

* 36 of the 37 failures share one pattern (5 forward and 3 reverse mismatches),
  and every one is a **Santee-Cooper clade fish ranavirus**: largemouth bass
  virus, smallmouth bass virus, Santee-Cooper ranavirus, mandarin fish ranavirus.
* On FV3-like amphibian and reptile ranaviruses, its design target, the assay
  detects essentially everything.
* **Decision for the curator:** if fish ranaviruses are out of scope for this
  assay's use, scope it (as was done for Takehisa and Feldman) and it reads as
  stable. If they are in scope, "watch" is the right status and the reason is
  this clade.

## CDV P gene, Scagliarini 2007: one sporadic variant

* 35 failures share one pattern: a mismatch **2 bases from the forward primer's
  3' end** plus one far upstream. The 3'-window penalty pushes them to `fail`.
* They are ordinary CDV isolates spread across 2010–2026, with no trend by year.
  Record titles do not give genotypes, so the lineage is not identified here; a
  phylogenetic placement of these 35 records would name it.
* **What it means:** "watch" at ~88% is accurate. The cause is one recurring
  variant, not a decline.
