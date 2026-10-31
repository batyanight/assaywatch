# Sub-taxid lineage resolution (estimand Phase 2)

**Date:** 2026-10-19
**Status:** design, not yet implemented
**Supersedes:** the "Phase 2 sketch, not yet specified" section of
`docs/journal/2026-10-17-estimand-plan.md`

## Naming note

`docs/journal/2026-10-18-phase2-handoff.md` is titled "Phase 2" but documents the
*per-taxid* verdict wiring — what the estimand plan and the recalibration doc
call **Phase 1**. This document is the estimand plan's actual "Phase 2 sketch":
resolving lineages **below** the taxid the record carries. To avoid the
collision, everything here is called **sub-taxid resolution**, never "Phase 2"
unqualified.

## The problem, restated precisely

The recalibration (`docs/journal/2026-10-18-recalibration.md`) left two false negatives at
the "taxid-resolution ceiling": the Boyle 2004 *Batrachochytrium dendrobatidis*
assay and the 2003 Influenza A Matrix-gene assay. Both are cases where
biologically distinct lineages that an assay should be judged against separately
collapse into one group because per-taxid analysis has nothing finer to group on.

Investigating the archives turned up the important result: **these two cases do
not share a mechanism, and neither does the wider set of "waiting" entries.** The
ceiling is not one problem. It is four, and only one of them is a sequence-homology
problem. Building a clustering engine for all of them would be wrong — three of
the four are resolved by cheaper, more exact information already sitting in the
records.

### The four modes (measured, not assumed)

All counts below are from `data/retrieved/` on 2026-10-03 archives joined to
`.meta.taxid.backfill.tsv.gz`.

**Mode A — the sub-taxon is already a distinct taxid, just not wired in.**
Avipoxvirus (query txid 10260, 1,733 records) resolves cleanly by per-record
taxid: 10261 fowlpox (625), 1928336 (298), 10264 canarypox (131), 44088 (101),
462818 (60), and a long tail — each a real NCBI species-level taxon. Titles
corroborate (fowlpox 624, pigeonpox 135, canarypox 76). The Influenza subtype
layer partly lives here too: 24% of Matrix-gene records (43,531 / 182,556) carry
a subtype-level taxid in the backfill. **No new science.** The fix is to resolve
each record to the most specific taxid at or below the query taxid, which the
sidecar already contains; the per-lineage machinery then works unchanged.

**Mode B — the sub-taxon is named in the title but has no usable taxid.**
Influenza A Matrix gene: 97.5% of titles (177,988 / 182,556) carry a parenthetical
subtype — H3N2 (66,501), H1N1 (51,838), H5N1 (26,743), H9N2 (7,543), down a long
well-populated tail — every major subtype far above any sane `min_records`. Yet
76% of these records (139,035) sit at the parent taxid 11320 in the sidecar, so
Mode A alone leaves them pooled. **The Matrix FN is a title-parsing problem, not a
homology problem.** Clustering segment 7 would be the wrong tool twice over: it is
conserved across subtypes so clusters would not track subtype, and it is 182k
records so it would be the most expensive possible way to recover a label that is
already written in the defline.

**Mode C — the sub-taxon has neither a taxid nor a title label.**
*B. dendrobatidis* (query txid 109871, 9,496 records). Per-record taxids give only
strain-level reference genomes — 684364 (JAM81, 8,511), 403673 (JEL423, 69), both
of which are **BdGPL** strains — plus 916 records at the bare species level, which
is exactly where the field isolates that matter for the assay sit. Title scan for
any lineage token (`GPL|CAPE|BdGPL|BdCAPE|lineage|global panzootic|...`): **zero
hits** across all 9,496. Titles give isolate and strain names (`Kihansi-KST-2022`,
`RTP6`) that map to a lineage only through an external, incomplete curation table.
**This is the only case where sequence homology is the sole remaining signal**, and
it is what the estimand plan's Phase 2 sketch was really about.

**Measured afterwards (2026-10-19): Mode C does not hold for the Boyle assay. The
Bd false negative is a denominator problem, like Mode D.** From the 2026-10-18 calls
(`results/2026-10-18/calls.tsv.gz`) joined to the 2026-10-03 archive metadata:

- Of the 9,496 records, **173 are evaluable** (172 detect, 1 fail). 9,320 are
  `no_amplicon`, mostly genome contigs and loci that don't carry the ITS target.
  A cluster can only reveal a failing lineage if the failures are in the evaluable
  set, and there is one fail in it.
- The evaluable records come in two shapes, and neither suits strategy A. There
  are 94 WGS contigs from a few strains (`RTP6 contig3` etc.), each 5 kb to 1.8 Mb;
  different contigs of one genome share almost no flank, so they would not link
  to each other. The other 76 are amplicon-only ITS deposits (145–149 bp, flank
  < 500 bp, mostly < 100 bp); masking the amplicon leaves almost nothing to
  sketch. Under strategy A nearly every record ends up `unresolved`.
- The documented failure is not BdGPL vs BdCAPE. The validation cases
  (`docs/validation-cases.tsv`, Boyle rows) say it is Asian ITS haplotypes with
  probe- and reverse-primer-site substitutions and indels (Mutnale 2018: 30
  GenBank haplotypes; Sreedharan 2023). Ghosh 2021 found the assay works where
  BdGPL and BdCAPE co-occur. The lineage framing above was the wrong target.
- Those haplotypes are most likely in the `no_amplicon` pool. Of 472 ITS-titled
  records, 395 are `no_amplicon`. 343 of those end before the forward primer's
  window: partial deposits that can't be assessed, not failures. 36 have the
  window present with nothing credible matching it. They are the only candidates
  for real site divergence, and they are excluded from the denominator rather
  than counted as `fail`.

So the Bd entry moves to the Mode D carve-out under "Out of scope". The question is
whether the 36 window-present `no_amplicon` records are genuine binding-site loss
(indels the mismatch-only matcher can't align would read this way; see
`results/indel_check/`), and if so, whether they should count against the assay.
That is a scope/scoring decision, not a within-taxon split.

**Mode D — not a sub-taxid problem at all; a denominator problem.**
DWV-A (txid 2951794, 223 records) and DWV-B (txid 2498590, 737 records) are already
clean, distinct taxa — all 223 DWV-A records carry taxid 2951794 and titles saying
"Deformed wing virus A". Phase 1 already separates them. The flagged concern
(`DWVA_polyprotein_Rossi_2024` declining on 28 records, "treat that call as unsafe")
is the opposite of a collapse: the assay is scored only against the ~16% of DWV
records that carry an explicit A/B label, while the bulk of DWV sits under the
parent taxon (txid 302420) unlabelled and excluded. That is a **scope/denominator
bias**, and no within-taxon split fixes it. Forcing it into the clustering path
would manufacture a confident number on a biased sample. It must be carved out and
handled as a scope decision (classify-or-exclude the unlabelled parent pool), or
left marked not-assessable — see "Out of scope" below.

## Design decision 1 — a resolver chain, cheapest signal first

Replace the single grouping key in `lineage.per_lineage_stats()` —

```python
lineage = lineage_for_taxid(taxid, taxa_cache)
```

— with a per-assay **resolver chain** that returns a sub-lineage label for a
record from the most specific signal available, trying mechanisms in increasing
order of cost and decreasing order of reliability:

1. **`subtaxid`** — most specific per-record taxid at or below the query taxid
   (Mode A). Pure lookup against the sidecar + taxa-cache.
2. **`title`** — a configured, named regex capturing a label from the defline
   (Mode B). Validated per assay; the capture group *is* the label.
3. **`cluster`** — sequence-homology cluster id on masked flanking regions
   (Mode C). Only computed when the first two yield nothing and the assay opts in.

A record resolves at the first mechanism that returns a label; the chain is
configured per assay (or per query taxon) so clustering never runs where a title
or a sub-taxid already answers. The unresolved bucket (estimand plan decision 1,
rule 5) is unchanged: anything that falls through every enabled mechanism is the
explicitly-named `unresolved` row and is **never judged as a clade**.

### Config schema (per assay, in `config.yaml`)

```yaml
sublineage:
  INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003:
    chain: [title]                  # title-only, NOT [subtaxid, title]: see note
    title:
      pattern: '\((H\d+N\d+)\)'      # capture group 1 is the label
      min_records: 20
  AVIPOXVIRUS_dsDNA_4b_core_Baek_2020:
    chain: [subtaxid]
  Boyle_2004_Bd_ITS:                  # example id
    chain: [subtaxid, cluster]
    cluster:
      mask: footprint                 # mask every amplicon span + probe, both strands
      buffer_bp: 20                   # extend the mask this far past each binding site
      method: mash
      sketch_size: 10000
      kmer: 21
      threshold: 0.05                 # Mash distance; see decision 3
      min_cluster_records: 20
```

An assay with no `sublineage` entry keeps today's behaviour exactly
(`chain: [subtaxid]` with `subtaxid` degrading to the query taxid = current
per-taxid grouping).

**Why influenza is `[title]`, not `[subtaxid, title]`.** The first resolver to
return a label wins. For influenza, 24% of records carry a subtype-level taxid
(H5N1 = 102793, etc.) and 76% sit at the parent 11320. If `subtaxid` ran first it
would label the 24% `taxid_102793` while `title` labelled the other H5N1 records
`H5N1` -- one subtype split across two group keys, each at risk of dropping below
`min_records`. Title is canonical and covers 97.5% of records, so it runs alone;
the 2.5% with no parseable subtype fall through to the taxid label (the lumped
parent). `subtaxid`-first is correct only where the sub-taxid and any later signal
share one label space, as in avipox (`[subtaxid]`: the species taxids are
themselves the canonical label).

## Design decision 2 — the flanking-region definition for the cluster resolver

The estimand plan pinned the one hard constraint: **cluster on sequence outside
the primer and probe footprints.** Clustering on the binding sites defines the
lineage by the very quantity the assay measures, so every assay would show a
failing cluster by construction — circular and useless.

Concretely, for each record fed to the `cluster` resolver:

1. Call `loci.pair_spans()` to get every amplicon span the screener could build
   on that record (it already returns 0-based half-open spans).
2. Mask each amplicon span **plus `buffer_bp` on each side**, on both strands.
   `pair_spans` returns the whole amplicon (forward-primer start to
   reverse-primer end), so this masks the primers, the probe and the
   inter-primer body together — everything the assay touches.
3. Cluster on the **remaining** sequence: the record's flanks outside the
   amplicon. Masking the whole amplicon (**strategy A**, chosen 2026-10-19) is
   the conservative, unambiguously non-circular choice. The alternative —
   masking only the individual primer/probe footprints to keep the inter-primer
   body (strategy B) — risks partial circularity near a probe-defined lineage
   and is not used. `subcluster.mask_regions` stays agnostic about what the
   spans are, so B remains reachable by passing footprint spans instead, should
   too many records fall to `unresolved` for lack of flank.

This uses the **full retrieved archives**, not the window archives. Window archives
(`assaywatch/windows.py`, not yet cut) deliberately keep only binding-site
neighbourhoods and would starve the clusterer of exactly the flanking sequence it
needs. The full records in `data/retrieved/<taxid>/<group>/` are the correct input
and have the most flank available.

A record with no unmasked sequence left (short amplicon-only deposit) cannot be
clustered and falls through to `unresolved` — it does not get a fabricated cluster.

## Design decision 3 — distance metric, method, and threshold

**Method: Mash (MinHash) distances, single-linkage clustering.** The Bd case is
9,496 records; the influenza case never reaches the clusterer (resolved by title).
Mash sketches each masked record in linear time, but the single-linkage step in
`subcluster.cluster()` is all-pairs. Measured 2026-10-19: one pure-Python sketch
comparison at sketch size 10,000 takes 6.45 ms, so 9,496 records would need about
81 hours. Feed the clusterer **only the evaluable records** of the assay (the only
ones `per_lineage_stats` groups); for Bd that is 173 records, about 15k pairs,
about 1.5 minutes. Past a few thousand evaluable records, replace the double loop
with LSH banding or `mash dist` (bioconda) before using it. An all-vs-all
alignment would be worse still. Defaults: k=21, sketch size 10,000 — standard for
genome/amplicon-scale nucleotide comparison.

**Threshold is the open risk and must be validated, not guessed.** The honest
difficulty: we have no clean BdGPL/BdCAPE truth labels in the archive (that is the
whole reason we are here). Validation plan, in order:

1. Seed with the reference strains we *can* label — JEL423 and JAM81 (both BdGPL,
   taxids 403673 / 684364) must land in the same cluster at the chosen threshold.
   If a threshold splits two known-same-lineage genomes, it is too tight.
2. Pull a small set of published BdCAPE and BdGPL isolate accessions from the Bd
   phylogenomics literature (O'Hanlon 2018 and the lineage-defining papers in
   `papers/`), confirm the threshold places them in different clusters.
3. Sweep the Mash distance in [0.01, 0.10] and report the cluster count and the
   two seed checks at each step; pick the loosest threshold that still separates
   the known lineages, to avoid shattering one lineage into many thin clusters.

Until (1) and (2) both pass, the Bd cluster verdict is reported but **not** fed
into the override — same discipline Phase 1 used before recalibration.

## Design decision 4 — how an unnamed cluster is labelled in the report

A human reads this table, so a cluster needs a stable, honest label that never
pretends to a name it has not earned:

- Label: `cluster-NN` where NN is assigned by **descending record count** (the
  largest cluster is `cluster-01`), so the ordering is deterministic across runs.
- Each cluster row also prints `n=<records>` and a **representative accession**
  (the sketch medoid, or lexically-smallest accession as a stable tiebreak) so a
  curator can BLAST it and attach a real lineage name later.
- The label is explicitly provisional in the prose: "unnamed sequence cluster,
  not a named lineage." A cluster is never rendered as if it were a taxon.
- Determinism requirement: the same input archive must yield the same cluster ids
  on re-run. Mash sketching with a fixed seed + the count-then-accession ordering
  gives this. A test must pin it, because an unstable label would make the drift
  report diff noisily run to run.

If a provisional cluster is later curated to a real lineage, the mapping lives in
`docs/taxa-cache.json`-style config, not in code.

## Integration points (where the code changes)

- **`assaywatch/lineage.py`** — the grouping key in `per_lineage_stats()` becomes
  `resolve_sublineage(call, resolvers)`. New `resolve_sublineage()` + three small
  resolver callables (`subtaxid`, `title`, `cluster`). `lineage_for_taxid()` stays
  as the `subtaxid` resolver's tail. `worst_lineage_verdict()` is untouched — it
  already operates on whatever grouping it is handed.
- **New `assaywatch/subcluster.py`** — the Mash pipeline: mask via
  `loci.pair_spans()`, sketch, distance, single-linkage, stable labelling. Kept
  separate so the heavy import (Mash/screed) is only pulled when an assay enables
  `cluster`.
- **`assaywatch/report.py`** — `read_calls()` already can load
  `amplicon_start/amplicon_end` (`with_spans`); the cluster resolver needs the
  record sequence too, so `build()` gains an opt-in path that reads the masked
  sequence for assays whose chain includes `cluster`. Title and subtaxid need no
  sequence read.
- **`config.yaml`** — the `sublineage` block above.
- **`Snakefile`** — if clustering is expensive enough to want caching, the cluster
  assignment becomes its own rule writing a `record_id -> cluster` sidecar that the
  lineage/report rules consume, so it is not recomputed every report. For the Bd
  scale it can start inline and be promoted to a rule only if runtime demands it.

## Out of scope for this document

- **DWV-A/B denominator bias (Mode D).** Needs a scope decision about the
  unlabelled parent DWV pool (txid 302420), not a within-taxon split. Track
  separately; until then `DWVA_polyprotein_Rossi_2024` stays flagged unsafe and is
  not "fixed" by anything here.
- **Bd Boyle 2004 (moved here from Mode C, 2026-10-19).** Also a denominator
  problem: the failing Asian ITS haplotypes are probably among the 36
  window-present `no_amplicon` records, outside the evaluable set. See the
  measurement under Mode C.
- **Cutting the window archives** (`windows.py`). Unrelated distribution concern;
  the clusterer uses full archives regardless.

## What this resolves

| Entry | Mode | Mechanism | New science? |
|---|---|---|---|
| Influenza A Matrix 2003 | B | title regex `(HxNy)` | no |
| Avipoxvirus 4b (Baek/Farias) | A | per-record sub-taxid | no |
| Bd Boyle 2004 (Asian ITS haplotypes) | D | scope decision, not here (measured 2026-10-19) | n/a |
| DWV-A / DWV-B Rossi 2024 | D | scope decision, not here | n/a |

Two of the four "waiting" entries are recovered by the resolver chain without any
homology computation. The other two are denominator problems that no grouping can
fix. `assaywatch/subcluster.py` (Mode C) is built and tested but has no consumer:
measured, Bd turned out not to be a Mode C case. It stays parked until a taxon
shows a failing lineage inside its evaluable set that neither taxid nor title can
label.
