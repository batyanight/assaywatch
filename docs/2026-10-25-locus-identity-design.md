# Step 2 of the plan, designed: is this amplicon even the assay's locus?

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

## The measurement that has to come first

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

## Recommendation

Do the measurement, on the four worked cases plus at least one severely-diverged conventional
assay, and bring the identity distribution back before building anything. If the gap is wide,
build it as a cached per-assay reference with the threshold in `config.yaml`; if the gap is
narrow, this approach joins `pair_evalue` and the probe test in the record of things that
looked right and were not, and the fallback is per-entry queries plus accepting that
conventional denominators stay approximate until tier-2 validation sets them.
