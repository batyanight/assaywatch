# Lineage-conditional estimand: the plan before the code

Status: **design agreed 2026-10-17, not yet implemented.** This is the document
`docs/RESUME-HERE.md` item 0 asks for. Two decisions were taken by the author in this
session; everything else below is derived from them or is measured evidence.

## The problem, restated precisely

Each assay is reduced to one pooled detected share over all recent evaluable records in its
group. Every one of the 12 documented failures in `docs/validation-cases.tsv` is of the same
shape: the assay keeps detecting most of what is deposited and misses one clade. A pooled
share cannot express that, so the tool scores **1 of 12**. No threshold in `config.yaml` fixes
this, which is why calibrating thresholds is pointless until the estimand changes.

## Decision 1 — what a lineage is

**Taxonomy first, sequence clusters second.** Phase 1 assigns each record the NCBI taxon it
was deposited under and conditions on taxa below the assay's query taxid. Phase 2 replaces or
supplements that with clusters derived from sequence.

### Why phase 1 cannot be the whole answer

Measured 2026-10-17 over the archives on disk, counting unique accessions and the first two
words of each defline:

| group | records | distinct names | names with >=20 records |
|---|---|---|---|
| Bd 109871 | 9,496 | 48 | **1** |
| Influenza A 11320 | 385,546 | 17 | **1** |
| CDV 11232 | 3,998 | 109 | 4, of which 3 are synonyms |
| Papillomaviridae 151340 | 42,990 | 1,745 | 36 |
| Haemosporidia 5819 | 32,044 | 265 | 76 |
| Paramyxoviridae 11158 | 15,423 | 569 | 58 |

Where the query taxid is a single species, taxonomy yields exactly one bucket and phase 1
conditions on nothing. The Bd failure is ITS haplotypes within one species; the CDV failure is
Europe-wildlife and Arctic lineages within one species; the influenza failure is 2009 pandemic
H1N1, whose subtype lives in the strain parenthetical of the title and not in the taxonomy.
Phase 1 is structurally blind to all of these.

Where the query taxid spans many species it conditions on real structure — and that is the
pan-family consensus PCRs, which the README already identifies as the bulk of the `declining`
calls and which are exactly where pooling dilutes most. Phase 1 is therefore well aimed, not
merely cheap.

### Phase 1 specification

1. **Per-record taxid is not stored anywhere today.** `*.meta.tsv.gz` carries
   `uid, accession, created, updated, length, title`; archives are FASTA whose defline is the
   title. The registry's `taxid` is the *query* taxon, not the record's.
2. **Add `taxid` to the retrieval sidecar** for new retrievals, and **backfill the existing
   1,279,609 unique accessions** by esummary on the uids already stored — roughly 2,560 POSTs
   at 500 uids each. `eutils.ncbi.nlm.nih.gov` was confirmed reachable from the sandbox on
   2026-10-17 (HTTP 200), so this does not have to wait for the laptop. Write the backfill to a
   sidecar of its own rather than rewriting the archives, which are not re-fetchable.
3. **Resolve taxid to lineage** through `docs/taxa-cache.json`, extending it for taxids it does
   not hold. The distinct-taxid count will be in the low thousands, so this is trivial.
4. **Group by taxid, never by organism name.** NCBI renamed canine distemper virus mid-stream
   and the archive holds `Canine distemper virus`, `Morbillivirus canis` and
   `Canine morbillivirus` concurrently. Name-based grouping would split one taxon into three
   fabricated lineages; taxids merge them correctly.
5. **Unresolved taxa are a declared bucket, not a lineage.** `Plasmodium sp.` holds 7,749
   records and `Leucocytozoon sp.` 6,665. These are a junk drawer, they must be reported as
   one explicitly-named unresolved row, and they must never be judged as a clade.
6. **An assay whose query taxid yields one bucket is marked `not lineage-assessable (phase 1)`**
   and gets no lineage verdict at all. It does not fall back to the pooled number wearing a
   lineage label. This follows the house convention already pinned by a test for the nested
   table: where the prose withholds a figure, the table withholds it too.

### Phase 2 sketch, not yet specified

Cluster records by homology on sequence **outside the primer and probe footprints**, then
measure detection within clusters. Anchoring outside the footprint is the whole point: cluster
on the binding sites themselves and the lineage is defined by the quantity being measured, so
every assay shows a failing cluster by construction. Phase 2 needs its own document, covering
the flanking-region definition, the distance threshold, and how an unnamed cluster is labelled
in a report a human has to read.

## Decision 2 — how per-lineage shares become a verdict

**The worst assessable lineage drives the call, with Benjamini-Hochberg across the lineages of
that assay.** The pooled share stays in the report as a second column.

This is a deliberate departure from the standing convention that side analyses are reported
beside a call and never fed into it. The convention was right for degeneracy, thermodynamics
and footprint clustering, none of which is a measurement of detection. A per-lineage detected
share is the same measurement as the pooled one on a better-chosen denominator, and leaving it
beside the call would mean the validation harness — which reads the status — still scores
1 of 12 no matter how good the table underneath is.

BH is there because an assay with 76 assessable lineages gets 76 chances to alarm. Without
multiplicity control the specificity gained since 2026-10-14 would be given straight back.

### The assessability floor

- A lineage is **assessable** when it holds at least 20 recent evaluable records — the same
  floor the report already applies before flagging an assay, now applied per lineage.
- Lineages below the floor are summed into one `below floor` row: reported, never judged.
- Every assay prints **the share of its recent evaluable records that sit in assessable
  lineages**. This is the number that tells a reader how much of the archive the lineage
  verdict actually covers, and an assay where that share is low has a weak lineage verdict
  however confident the worst-lineage interval looks.
- The floor of 20 is inherited, not calibrated. Recalibrate it once the backfill exists and
  the real per-lineage sample sizes can be seen; 20 recent evaluable per lineage is a much
  harsher cut than 20 per assay and may leave too little assessable.

## What this predicts, so it can be falsified

Phase 1 is structurally incapable of catching 6 of the 12 documented failures: both Bd rows
(ITS haplotypes, one species), CDV (lineages, one species), influenza A M-gene (subtype, not a
taxon), and both ferlavirus rows (genogroups B and C, not taxa). It is potentially capable on
the other 6: papillomavirus FAP59/64 (beta genus is a real rank), both nidovirus rows and the
three haemosporidian rows (species-level, and 5819 shows 76 lineages above the floor).

**So phase 1's ceiling is 6 of 12, and the realistic expectation is lower.** If an
implementation of phase 1 reports much more than 6, suspect the multiplicity control before
celebrating. The remaining 6 are the measure of what phase 2 is for.

## Order of work

1. Add `taxid` to the retrieval sidecar; extend the schema and its tests.
2. Backfill taxids for the 1,279,609 stored accessions into a separate sidecar.
3. Extend `docs/taxa-cache.json` over the distinct taxids; group by taxid.
4. Per-lineage shares and the assessability floor in `drift.py`, reported only — no status
   change yet, so the table can be read against the existing calls before it is trusted.
5. Then the verdict change and BH, and only then re-run
   `scripts/retrospective.py` against `docs/validation-cases.tsv`.
6. Recalibrate the floor, and the `config.yaml` thresholds, against the new estimand.

Steps 1-4 change no call. Step 5 is the one that moves the number and the one to review hardest.
