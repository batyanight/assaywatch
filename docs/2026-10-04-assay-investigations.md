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

### Are per-oligo binding positions worth recording? (2026-10-04)

Not fetched from NCBI — the matcher computes them locally in milliseconds, and
a remote search would need the sequence anyway. But recording the positions we
already compute is worth it, for one reason: anchored on a credible site, they
separate a **truncated deposit** from a **diverged binding site**, and nothing
else does.

Measured on the 464 Bd ITS records that yield no amplicon for Boyle 2004,
gating single-oligo hits with the chance E-value (≤ 0.01) so that chance
matches of the 15 nt probe are not counted:

| | |
|---|---|
| credible reverse-primer site | 393 (375 of them a perfect match) |
| credible probe site | 40 (37 perfect) |
| probe "hits" that are chance, correctly rejected | 411 |

Then anchoring on the best credible reverse site and asking whether the probe's
expected window is even inside the record:

| | |
|---|---|
| probe window runs off the end — truncated deposit | **392** |
| no credible anchor at all | 71 |
| probe window present and the probe matches | 1 |
| probe window present but no credible probe match (i.e. divergence) | **0** |

So the answer on both counts:

* **Yes, record them.** They turn "464 records excluded" into 392 truncated, 71
  unanchored, 1 usable — and the first number is the one that matters, because
  a `stable` verdict resting on 54 of 518 ITS records is resting on a biased
  11%. The report currently gives the evaluable count but never says that most
  exclusions are truncations rather than failures.
* **No, they will not catch the Bd drift.** Zero records show the probe window
  present with no credible match. The Mutnale 2018 haplotypes are deposited as
  fragments that stop before the probe footprint, so neither amplicon screening
  nor anchored single-oligo screening can judge them. The honest verdict for
  Boyle 2004 is therefore not "stable" but **"the probe footprint cannot be
  assessed from GenBank: 392 of 464 ITS deposits are truncated before it"**.

That is a limit of the data, not of the thresholds, and it is worth stating
plainly in the paper: for assays whose target is deposited as short fragments,
in-silico drift surveillance can confirm the primer footprints and say nothing
about the probe.

### Should a `diverged` record count as a failure? (2026-10-04)

Once exclusions are labelled, the question becomes concrete: a record whose
partner binding site is **present in the deposit and does not match** is
evidence the assay would not amplify it, yet it leaves the denominator as
`no_amplicon`. Dropping those biases the denominator toward the sequences the
assay happens to match — the same bias that hides the Bd probe problem.

Across the 2026-10-04 run the labels are: 1,208,057 `no_site`, 229,254
`truncated`, 81,297 `chance_only`, **39,293 `diverged`**, 660 `no_pair`.
Counting the diverged ones as failures moves **16 assays**: stable 45 → 37,
declining 29 → 35.

Tested against the validation cases rather than argued (`drift.count_diverged_as_fail`):

| case | expect | flag off | flag on |
|---|---|---|---|
| Boyle, as of 2012 (Longo: sites conserved) | works | stable ✓ | stable ✓ |
| Boyle, as of 2017 (Mutnale: probe/primer mutations) | fails | stable ✗ | **declining ✓** |
| Boyle, as of 2020 (Ghosh: works as pan-lineage screen) | works | stable ✓ | **low coverage ✗** |
| Boyle, as of 2023 (Sreedharan: redesigned) | fails | undecided | **low coverage ✓** |
| Annis, now | works | stable ✓ | stable ✓ |

Off: 3 agree, 1 disagrees, 1 undecided. On: 4 agree, 1 disagrees, 0 undecided.

It fixes the two cases where the literature reported failure and breaks the one
where a paper used the assay successfully — and that is not a contradiction:
Ghosh 2021 used it on South African samples (BdGPL and BdCAPE), which it does
cover, while the tool judges it against all Bd records including the Asian
haplotypes it does not. Both are right at different scopes, and the tool has no
lineage resolution to say so.

**Left off.** Four agreements against three, on five cases with one moving each
way, is noise; flipping a default that moves 16 assays on that evidence would be
fitting to a sample of five. Revisit when the case set reaches 15-20.

## Tier-2 validation, 46 cases: the tool misses most documented failures

`docs/validation-cases.tsv` now holds 46 cases over ~30 assays, drawn from
independent follow-up literature and dated to the latest sequence each cited
work could have seen. Scored by `scripts/retrospective.py`:

| | caught | total |
|---|---|---|
| documented **failures** the tool flags | **1** | 12 |
| `works` cases the tool does not contradict | 17 | 21 |

That is the headline result, and it is not flattering: **the tool is
conservative to the point of near-blindness on real failures.** It rarely cries
wolf — only 4 of 21 `works` cases are contradicted, and 8 more are called `low
coverage`, which is defensible rather than wrong — but of twelve failures
reported in the literature it flags one, disagrees with seven and declines to
judge four.

That follows from how the thresholds were chosen. Flagging requires the *upper*
bound of the recent interval to fall below 90% on at least 20 evaluable
records, which was deliberately set to avoid false alarms on sparsely sequenced
taxa. The validation says the dial is far too conservative, and more precisely
that the failure modes the literature reports are mostly **lineage- or
group-conditional** (ferlavirus genogroups B and C, insect-specific
flaviviruses, swine H1N1 against avian influenza, beta-papillomaviruses,
fusiform-gametocyte Leucocytozoon, divergent serpentoviruses) while the tool
computes one population proportion per assay. A minority lineage cannot move
that proportion past a 90% bar.

Turning on `count_diverged_as_fail` over all 46 cases: failures caught 1 → 2,
works not contradicted 17 → 16. It is not the fix.

**What the validation says to build next**, in order: a per-lineage or
per-clade breakdown rather than one proportion per assay; and a verdict that
reports the worst-covered subgroup, not the average. Threshold tuning alone
cannot close a 1-in-12 gap.
