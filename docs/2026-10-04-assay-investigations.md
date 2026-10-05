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

## Scoping an assay: when it is the finding and when it hides one

Scoping an assay to the lineage it was designed against makes it stable almost
by definition, so each scope has to be argued one of two ways:

* **The published claim is lineage-specific.** The assay was never offered as
  broader, so the narrow denominator is the one its claim is about, and the
  wide number is specificity rather than drift. Scope it, and record the wide
  number so the limit stays visible.
* **The published claim is broader than the lineage.** Then the miss is the
  finding and scoping buries it: someone working where the other lineage
  circulates needs to see it. Do not scope; record the breakdown instead.

A scope must also restrict by *organism*. An untagged Entrez term searches
every field, so a keyword scope silently changes the denominator without
isolating anything — both first attempts here did exactly that and had to be
redone (below).

### Feldman 2006, chelonian Mycoplasma 16S — scoped (claim is lineage-specific)

The paper describes a novel Mycoplasma of free-ranging eastern box turtles and
the source sheet says "turtles only", so the claim is chelonian. Scoped to the
three named chelonian mycoplasmas by taxid: **Mycoplasmopsis agassizii**
(33922), **Mycoplasma testudineum** (244584), **Mycoplasmoides testudinis**
(33924) — 534 records.

* Retrieval root is the **phylum** (Mycoplasmatota, 544448), not genus
  *Mycoplasma*: two of the three species have been reclassified out of that
  genus, so a query under txid2093 reached only 94 of the 534 records. Any
  genus-level taxid in this registry can rot the same way, and
  `scripts/check_taxids.py` would not catch it — it checks that a taxid still
  means what the registry says, not that the species an assay targets are still
  inside it.
* First attempt (reverted) used keywords (`turtle OR tortoise OR …`): 103
  records, mostly assembly contigs and uncultured clones, missing most of the
  real ones.
* **Wide number, kept on the record:** against the whole genus (24,523 records)
  it detected 0–4% in every year. That is the assay being specific.
* After scoping: 9 of 10 evaluable records detected, nothing deposited in the
  last 24 months, so `no recent data`.

### Takehisa 2009, SIV pol — not scoped (no honest scope exists)

The paper is about SIV in wild-living western gorillas, so a SIVgor scope would
be defensible in principle. It cannot be built: **SIVgor has no NCBI taxon**,
and SIVcpz (388909) has only 7 pol/genome records. The keyword scope tried
first returned 596 records of which 181 of 219 evaluable were neither clearly
SIVcpz nor SIVgor — it shrank the denominator without isolating the lineage, so
it was reverted.

The assay stays on all SIV, and the breakdown is recorded instead:

| lineage (from record titles) | evaluable | detected |
|---|---|---|
| gorilla (SIVgor) | 8 | 8 (100%) |
| chimpanzee (SIVcpz) | 30 | 15 (50%) |
| other / unclear | 181 | 5 (3%) |

Read that way the report's low share is not drift and not a scoping artefact:
the assay does what the paper claims on SIVgor, covers about half of SIVcpz,
and does not cover the rest of the genus. Anyone using it outside SIVgor needs
that table, which is the case where scoping would have hidden the finding.

## The four new PREDICT families, first results (2026-10-04)

| assay | status | recent | note |
|---|---|---|---|
| Phlebovirus L round 1 | stable | 94.4% (54) | works |
| Phlebovirus L round 2 | stable | 96.5% (142) | works |
| Rhabdovirus L round 1 | low coverage | 11.1% (1307) | pan-family assay on all Rhabdoviridae |
| Rhabdovirus L round 2 | declining | 25.5% (1368) | change −10% to −5% |
| Calicivirus capsid | declining | 0% (27) | scope: marine-calicivirus assay on mostly norovirus |
| Orthobunyavirus S | coverage gap | 0 of 2056 | primer tails, see below |
| Orthobunyavirus M | coverage gap | 2 of 2056 | primer tails, see below |

* **Phlebovirus** is the clean result: the nested assay detects 94–96% of
  phlebovirus L records, and both rounds are stable.
* **Rhabdovirus** at 11–25% of all Rhabdoviridae is the pan-family scope
  pattern again, not necessarily drift. These are the panel's
  degeneracy-increased primers (221,184× and 36,864× — "severe"), which makes
  an in-silico `detect` weak evidence on its own. Round 2 is called `declining`
  on a 5–10 point fall; worth watching, not acting on before validation.
* **Calicivirus** shows the limit of the declining / low-coverage split. The
  entry predicted this would be scope rather than drift, and it is — a marine
  calicivirus assay screened against a group that is mostly norovirus — but the
  fall from 14% to 0% is larger than `min_decline`, so it is reported as
  `declining` anyway. A fall caused by which lineages were deposited recently
  still reads as drift. Either the assay is scoped to vesiviruses or the split
  needs a scope-aware term.
* **Orthobunyavirus: my entries are at fault, not the data.** Both assays use
  the conserved genome termini, and the terminal primers appear to carry
  non-templated cloning tails. The full BUNS-5-U-6 finds no site within six
  mismatches in records that demonstrably contain the terminus; dropping its
  first seven bases (`CGGCGCC`, containing the KasI/NarI site `GGCGCC`) matches
  perfectly in 6 of 6. The sequences are left as the panel prints them, flagged
  `PRIMER_TAIL_SUSPECTED`, because the tail boundary is inferred from data and
  needs Briese et al. 2007 to confirm. Note the conserved terminus is present
  in only ~4% of deposits anyway, so even with the tails marked this pair will
  be assessable against few records.

## Tier-2 validation, first cases: the Bd assays (2026-10-04)

`docs/validation-cases.tsv` + `scripts/retrospective.py`. Result: **3 agree,
1 disagrees, 1 undecided.**

| as of | expect | tool says | |
|---|---|---|---|
| 2012-12-31 | works | stable | agrees (Longo 2013 found the binding sites conserved) |
| 2017-03-31 | fails | stable | **disagrees** (Mutnale 2018) |
| 2020-11-01 | works | stable | agrees (Ghosh 2021 used it as the pan-lineage screen) |
| 2023-01-03 | fails | insufficient data | undecided (Sreedharan 2023 redesigned it) |
| Annis 2004, now | works | stable | agrees |

The one disagreement is the informative one. Mutnale et al. 2018
(10.1038/s41598-018-28304-1) found 30 GenBank ITS haplotypes with mutations in
the TaqMan probe footprint and 15 in the reverse-primer footprint, mostly
Asian, and got 33 qPCR positives against 119 by nested PCR on the same swabs.
The tool says stable and cannot see it, for two structural reasons:

1. **The denominator excludes the records that carry the diversity.** An
   amplicon call needs both primer sites in one record. Bd ITS submissions have
   a median length of 257 bp and **464 of 543 do not span the amplicon**, so
   they are `no_amplicon` and dropped. Those partial haplotype deposits are
   exactly where a submitter records a divergent ITS sequence. Of the 112
   evaluable records, 79 are ITS-titled, 31 are genome or assembly records and 2
   are something else — so this is not fixable by a narrower retrieval query
   either (an ITS-only query would *lose* 33 of the 112).
2. **A population proportion cannot see a lineage-specific failure.** Even with
   those records included, a few per cent of haplotypes failing reads as
   "stable" against a 90% threshold. The verdict the literature supports is
   lineage-conditional: fine for BdGPL and BdCAPE, degraded for Asian
   haplotypes. The tool has no notion of lineage.

Neither is a bug to patch by moving a threshold, and moving one to make this
case pass would be fitting to a single case. What they point to:

* **Score single oligos against partial records**, reported separately from
  amplicon calls. A 257 bp ITS deposit can still say whether the probe
  footprint matches, which is where the documented failure lives.
* **Stratify by lineage or clade** where the records support it, so a minority
  blind spot is visible instead of averaged away.

Also noted: the Mutnale failures include a 2 bp insertion in the probe
footprint, and the matcher is ungapped by design, so that case cannot be scored
as an indel at all — `assaywatch/gapped.py` exists but only
`scripts/indel_check.py` uses it.
