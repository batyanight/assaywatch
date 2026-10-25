# Step 2: built, priced, and it DOES NOT WORK. A pan-family assay's success looks like failure to it

> **VERDICT, 2026-10-25, after building and pricing it: do not enable this.**
> `scoring.locus_identity_min` ships **null** and must stay null. The approach joins
> `pair_evalue` and the probe-only test in the record of things that looked right and were not,
> and it fails for a reason none of the earlier analysis anticipated:
>
> **For a pan-family or consensus assay, a divergent amplicon interior is what SUCCESS looks
> like.** Priced offline at 0.50 over the 2026-10-25 run it rejects **1,840 of 9,687 sampled
> failures**, and the rejections concentrate exactly where they must not.
> `Pan_HERPES_dsDNA_Polymerase` loses **47 of 47**, and those records are *Proboscivirus
> elephantidbeta5*, *Mardivirus gallidalpha2* (Marek's disease), *Equid alphaherpesvirus 1*,
> *Elephant endotheliotropic herpesvirus 5/5B* and *Macropodid alphaherpesvirus 4* — real
> cross-subfamily herpesviruses and the entire purpose of a pan-herpes assay. They score
> 0.35–0.41 only because the five reference interiors happened to be human CMV UL54 from one
> submission batch (`PZ050664`–`PZ050668`). **48 of 209 registry entries are
> pan/consensus/generic shaped.**
>
> **And it cannot reach the two cases that motivated it.** Trimming 20 bp from each end of
> Orf's 68 bp amplicon leaves 28 bases and `OPHIDIOMYCES targetD`'s 57 bp leaves 17, both under
> the 30 bp floor, so both come back *unjudgeable*. Those two are probe-bearing and are already
> handled by `drift.chance_pair_test`.
>
> **The only version with a chance of being safe is lineage-aware** — a reference per
> sublineage rather than per assay, using the machinery in `clustermaps.py` / `subcluster.py` —
> and that is unproven. The module, its 12 tests, `scripts/build_locus_references.py` and
> `scripts/price_locus_identity.py` are kept as the evidence and as the basis for that, not
> because anything here is ready.
>
> What stands from the earlier measurement: chance pairs really do sit at 0.32–0.41 and
> single-target real loci at 0.56 and above (SIV Takehisa's floor over 400 records is **0.56**,
> not the 0.65 a 60-row sample suggested, so **0.55 is not safe either** — the margin is
> 0.41–0.56). The signal is real; it just cannot be separated from pan-family divergence by one
> global threshold.



The chance-pair test shipped 2026-10-25 covers probe-bearing assays, because the probe is a
locus-presence signal independent of how well the primers matched. **155 of 208 entries are
`conventional` and have no such signal**, so the root cause named in `docs/RESUME-HERE.md` -
evaluability decided from primer placement alone - is closed for 53 entries and open for the
rest. This is the design for closing it generally. **Nothing is implemented.** It ends in a
measurement to make and a threshold to set, and both want a maintainer's call.

## What will not work, so nobody builds it twice

**`loci.pair_spans` as a validity test.** The obvious first idea, since the module already
computes "every amplicon the screener could build" and `assemblies.extract_loci` consumes it.
It cannot do this job: it selects candidate pairs by `max_mm` and `max_e`, the very criteria
the chance pairs already satisfy, so it would return the chance pairs too. It answers *where
could an amplicon form*, not *is this the assay's locus*.

**Absolute coordinates.** A locus sits at a different offset in every accession - a complete
genome, a partial CDS and a WGS scaffold of the same organism share no coordinate frame - so
there is nothing to compare a position against.

**Anything keyed on the probe.** Already stated in the chance-pair doc and repeated because it
is the easy mistake: the West African mpox assay's 2,688 probe-less failures are real.

**Anything keyed on `pair_evalue`.** Withdrawn the same day it was proposed. The statistic
scales with match quality, so a genuinely divergent real site necessarily scores weak, which is
the record a drift registry most needs to keep.

## What should work: amplicon-interior homology

The records that `detect` certainly carry the locus. So the assay's own successful amplicons
define what its locus looks like, and a questionable amplicon can be asked whether it is
homologous to them - a test on the **interior** of the amplicon, deliberately not on the primer
sites, because the primer sites are where all the confounding lives.

It separates the three cases that matter, and it separates them for the right reason:

| case | amplicon interior | verdict it should get |
|---|---|---|
| Orf B2L chance pair | B2L envelope-protein sequence; no homology to the RPO147 amplicons | **not evaluable** - the locus is absent |
| *Ophidiomyces* scaffold chance pair | arbitrary scaffold sequence; no homology to the targetD amplicons | **not evaluable** |
| Ranavirus MCP genuine failure | the MCP amplicon, homologous to the detecting records | **fail** - counts, as it must |
| West African mpox clade I | the G2R locus, homologous; only the probe window differs | **fail** - counts, as it must |

And it needs no probe, so it reaches the 155 conventional entries that decision A cannot.

## Where it has to live, and why that is expensive

**At screen time, not report time.** `Call` carries `amplicon_start` and `amplicon_end`; it
never carries the amplicon sequence, and nothing writes one to the screens table. The chance-
pair test could run at report time only because the probe site and the primer penalties were
already columns. This test needs the record's bases, which exist only inside
`score.screen_record`.

That has three consequences worth pricing before anyone starts:

1. **It forces a full rescreen** on every change to it, 425 jobs and about 30 minutes, where
   decision A could be re-priced in seconds by rendering the report twice. Iterating on the
   threshold is therefore slow, which argues for getting the measurement below done first and
   in one pass.
2. **It needs the assay's reference amplicons before it can judge any record**, which is a
   second pass over the archive: screen once to collect the detecting amplicons, then screen
   again to test the questionable ones. Either that, or the reference is built once and cached
   per assay, like `docs/taxa-cache.json` and the other caches - which is probably the right
   shape, and makes the reference an auditable artefact rather than a hidden intermediate.
3. **A cached reference is a new input to the screen rule's trigger closure**, and
   `tests/test_triggers.py` exists because that closure has been got wrong before.

## THE MEASUREMENT, DONE 2026-10-25: the gap is real and the safe window is 0.50-0.55

> **Re-run from `calls.tsv.gz` later the same day, and the result improves.** The table
> immediately below was measured by globbing `results/screened/`, which includes **orphan**
> group screens from before `amplicon.declared_tolerance` shipped
> (`docs/2026-10-25-stale-orphan-screens.md`). On current data the lyssavirus chance-pair bin
> is **empty** and its genuine failures sit at **0.86-0.99**, so the apparent overlap - and the
> six rows I explained away as mis-binned - were entirely stale. SIV's floor moves to
> **0.65-0.67**. **The gap therefore widens to 0.41-0.65** and `locus_identity_min: 0.50` sits
> in the middle of it. The stale table is kept below because the mis-binning analysis it
> prompted is still the right way to read a low-identity "genuine" row.

Measured on the real archives. For each assay, amplicon interiors were taken with 20 bp
trimmed off each end so the primer sites themselves cannot contribute, and each questionable
interior was scored as its best ungapped identity, both strands, against five interiors from
records that detect.

| assay | chemistry | detect/reduced | chance-pair shaped | genuine-failure shaped |
|---|---|---|---|---|
| `ORF_VIRUS_..._Zhao_2013` | probe | **1.00** (n=40) | **0.32-0.41** (n=60) | none |
| `LYSSAVIRUSES_ssRNA_Nucleoprotein_gene` | conventional | 0.81-1.00, p50 0.97 | **0.33-0.44** (n=17) | 0.32-0.96, p50 0.90 (n=43) |
| `RETROVIRUS_RNA_polymerase_SIV_Takehisa_2009` | conventional | 0.83-1.00, p50 0.90 | none | **0.63-0.65** (n=60) |

**The apparent overlap in the lyssavirus row is a classification error of mine, not a real
one.** Its six "genuine" failures below 0.60 all have one primer at exactly the 3.0 boundary
and the other between 3.0 and 8.5, with amplicon lengths of 143, 404, 773, 877, 1230 and 1791
bp. A real locus has one length. They are chance pairs resting on a single marginal anchor,
and my split called them genuine only because one primer scraped the bar. Thresholds of 0.50,
0.55, 0.60 and 0.70 all lose exactly those six and keep exactly zero chance pairs - identical
counts at every cut, which is what a clean gap looks like. **Nothing at all sits between 0.44
and 0.60.**

**So the test works, including on conventional assays, which was the whole point.** Chance
pairs land at 0.32-0.44, essentially the best-of-many-offsets floor for unrelated DNA. Real
loci land at 0.60 and above.

**The ceiling is set by SIV Takehisa and it is the risk this document predicted.** That assay
reads 1.1%, its target is genuinely divergent, and its 60 genuine failures sit at **0.63-0.65**.
A threshold of 0.70 destroys every one of them - precisely the "discarding real drift" failure
that killed the `pair_evalue` and probe-only approaches. So:

> **Recommended threshold: 0.50**, with the empirical margin running from 0.44 (highest chance
> pair) to 0.60 (lowest real locus). 0.55 is equally safe. **0.60 is cutting into the margin
> and 0.70 is known to be wrong.**

### Two limitations the measurement exposed

1. **Short amplicons have too little interior to score.** `RANAVIRUS_..._MCP_Pallister_2007`
   could not be measured at all: its amplicon is 57 bp, and trimming 20 bp of primer from each
   end leaves 17 bp, which is too short for a meaningful identity. Any implementation needs a
   minimum interior length below which it declines to judge rather than guessing - and it must
   decline in the direction of keeping the record evaluable, since that is the status quo.
2. **The 20 bp trim is itself a parameter** and was not calibrated; it was chosen to exceed the
   longest primer here. Too small and the primer sites leak into the score, inflating chance
   pairs; too large and short amplicons are lost.

## The measurement specification, as originally written

The threshold is an identity (or alignment-score) floor on the amplicon interior, and **it must
not be guessed.** The same shape of measurement that settled the chance-pair criterion will
settle this one: take the four worked cases above, compute interior identity against the
assay's detecting amplicons, and look for a gap.

- If the chance pairs land near background identity and the genuine failures land high, with a
  wide gap, the floor goes in the gap and the test is sound.
- **If genuine failures from a badly diverged assay land low, the gap closes and this approach
  fails too** - and that is the honest risk, because a truly drifted target is exactly a
  diverged interior. The ranavirus failures are mild (primer penalties 2.5 and 2), so they are
  a weak test of this; the strong test is an assay whose genuine failures are severe. Candidate
  probes for that: the two `LYSSAVIRUSES_ssRNA_Nucleoprotein_gene` entries, whose ~4,900
  high-penalty conventional failures are plausibly real divergence, and
  `RETROVIRUS_RNA_polymerase_SIV_Takehisa_2009` at 1.1%.

Until that measurement exists there is no honest number to ship, and `config.yaml`'s rule -
thresholds carry their justification or the admission there is none - would force the admission.

## Cheaper partial alternatives, for comparison

**Per-entry retrieval queries.** `ORF_VIRUS` and `BPSV` both carry `query: null` and so fetch
every record for their taxid, off-target genes included. A gene-restricted query fixes Orf
without any scoring change at all. It does nothing for the *Ophidiomyces* scaffolds, which are
the right organism and the right taxid, and nothing for the general case - but it is nearly
free and reduces the problem's surface. Worth doing regardless of this design.

**An annotation or title test.** Orf's chance pairs are in records whose own titles say
"major envelope protein (B2L) gene". Catching them that way is trivial and fragile, and it
reads a label where this project's rule is to measure; `scripts/check_taxids.py` exists because
labels have been wrong before. Not recommended, recorded because it is the first thing anyone
will suggest.

## Recommendation, now that the measurement exists

**Build it.** The gap is real (0.44 to 0.60), it holds on conventional assays, and the
threshold is measured rather than guessed. Shape:

- `scoring.locus_identity_min: 0.50` in `config.yaml`, with the table above as its
  justification and the SIV ceiling named, so the next person knows 0.70 is not available.
- A minimum interior length below which the test declines to judge, and declines toward
  **keeping** the record evaluable - the status quo, so an unmeasurable record cannot be
  silently dropped. Ranavirus at 57 bp is the case that forces this.
- A cached per-assay reference built from records that detect, as an auditable artefact rather
  than a hidden intermediate, and therefore a new input to the screen rule's trigger closure.
- Screen-time, so expect a full rescreen per iteration and get the threshold right in one pass.

**One cheaper signal found on the way, worth considering first or alongside.** The lyssavirus
chance pairs gave amplicon lengths of 143, 404, 773, 877, 1230 and 1791 bp for one assay. A
real locus yields one length, within the declared range; a chance pair yields whatever the
geometry allows. **Amplicon-length dispersion against the assay's declared size may separate
the same cases for almost no computation**, and unlike interior identity it works on short
amplicons. It is not a substitute - a chance pair can land at the right length - but as a first
filter it is nearly free, and `amplicon_bp` plus `amplicon_bp_range` are already on every
entry. Measuring it is the obvious next step and smaller than building the identity test.
