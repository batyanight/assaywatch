# Plan: lineage-conditional verdicts

2026-10-15. A plan, not a record of work done. Nothing here is built yet. It is
written before any code because the last attempt at this problem (the
duplication check, review 3.3) needed two adversarial reviews to correct, and
most of what went wrong was decided before the first line was written.

## The problem, in one example

Against the validation cases the tool flags **1 of 12** documented failures
(`docs/2026-10-04-pipeline-review.md` §3.1). Every one of the 12 is a failure on
part of the target: ferlavirus genogroups B and C, beta-papillomaviruses only,
swine H1N1 against an avian-designed M-gene primer, divergent serpentoviruses,
fusiform-gametocyte *Leucocytozoon*, Asian Bd haplotypes.

The tool reduces each assay to one number, the share of recent records it
detects, and flags it below 90%. Suppose a taxon's recent records are 900 of a
lineage the assay detects and 100 of one it misses completely. The pooled share
is 90%. The assay is blind to a whole lineage and the tool calls it stable. No
threshold fixes that: lower the bar to catch it and you flag every pan-family
PCR that is mediocre everywhere; the information that one group fails *entirely*
is gone once the records are pooled.

So the fix is a different **estimand**, meaning the quantity the tool is trying
to estimate. Instead of "what share of the taxon does the assay detect", ask
"what is the worst-covered subgroup of the taxon, and how badly". The
review's wording: make the headline verdict the worst-covered subgroup above a
frequency floor, and name it. Validation then asks a question the 12 cases can
actually answer: *did the tool name the lineage the paper named?*

## What decides whether this works: how a record gets a lineage

Everything below is easy except this. There are three sources of a subgroup
label, and they catch different cases.

**A. NCBI taxonomy.** Every GenBank record has an organism taxid, and the
registry's `Organism:exp` query already pulls in the whole subtree under the
assay's root taxid. A subgroup is a taxonomy node in that subtree (a genus,
species, or a below-species node such as an influenza subtype). Cheap, exact,
already curated. Its weakness: it only sees lineages someone has made into a
taxon. Genogroups, haplotypes and named clades usually are not.

**B. Footprint groups.** The screen already writes each record's footprint (the
mismatch pattern at every oligo site, `drift.footprint_signature`). Records
that share a primer-site variant share a footprint. Grouping by footprint sees
a lineage defined by the very bases that matter, with no external labels: the
*E. coli* malB case is one footprint of 92 failures. Its weaknesses: a
sequencing error is a footprint of its own (the reason equal weighting was
rejected in review 3.3), and a record whose sites were not found at all
(`no_site`, `diverged`) has no footprint, so the most divergent lineages are
invisible to it.

**C. Sequence clustering of the amplicon region.** Cluster records by identity
across the whole amplicon, not just the primer sites. This sees genogroups and
haplotypes that taxonomy does not name and that a footprint misses. It needs
each record placed on the assay's reference amplicon, which is the
homology-anchored scoring of review §3.2. That is the expensive one, and it is
also the fix for the denominator problem, so it is worth building once, later.

My reading of which of the 12 each source could catch, **to be checked in
Phase 0, not assumed**:

| case | named lineage | A taxonomy | B footprint | C clustering |
|---|---|---|---|---|
| Papillomavirus FAP59/64 | non-beta genera | likely | maybe | yes |
| Nidovirus PP1b ×2 | divergent serpentoviruses | likely | unlikely (no sites found) | yes |
| Influenza A M gene | swine / pdm09 H1N1 | partly (subtype nodes; "swine" is host, not taxon) | likely (~5 shared mismatches) | yes |
| Bd ITS (Boyle) ×2 | Asian haplotypes | no | likely (probe/reverse-site mutations) | yes |
| Ferlavirus (Tong) ×2 | genogroups B, C | probably not | unlikely | yes |
| CDV P gene (Scagliarini) | field lineages | no | maybe | yes |
| *Leucocytozoon* cyt b ×3 | fusiform-gametocyte species | only if those records predate `as_of` | — | — |

Two things follow if that reading is right. First, taxonomy alone moves the
score from 1 to perhaps 3 or 4 of 12; footprints add the Bd and influenza
shapes; clustering is needed for the rest. Second, the three *Leucocytozoon*
rows may be **uncatchable by any in-silico method**: Lotta 2019 found the
missed species by whole-mitogenome amplification, and if their cyt b sequences
were not in GenBank before the 2016-12-31 cutoff, no tool screening GenBank
could have seen them. Those rows would then be a statement about GenBank, and
the honest ceiling is 9 of 12, not 12.

## Phases

### Phase 0: ground truth and a ceiling (no scoring change)

1. **Add a `lineage` column to `docs/validation-cases.tsv`**: for each `fails`
   and `partial` row, the lineage the paper named, and its taxid where one
   exists. For `works` rows it stays empty. This is what makes "did the tool
   name the lineage" checkable, and filling it is reading, not inference.
2. **Store the organism taxid per record.** `retrieve.esummary` already gets a
   DocSum per record that carries `TaxId`; add it to `RecordMeta` and the
   `.meta.tsv.gz` columns. Existing archives need a one-off backfill (esummary
   on their accessions), which needs NCBI, so it runs on the Mac. Archives are
   never rewritten: the backfill writes a sidecar, as `windows.tsv.gz` does.
3. **Measure the ceiling.** For each of the 18 `fails`/`partial` rows: using
   only records deposited before `as_of`, are there records of the named
   lineage in the archive at all, how many, from how many distinct footprints,
   and what calls did they get? One table, written up as a dated doc. This
   replaces the reading in the table above with measurements, and it says how
   much each of A, B and C could possibly recover before anything is built.

Phase 0 is the go/no-go. If the named lineages are mostly absent before
`as_of`, no grouping scheme helps and the validation set itself needs
re-dating.

### Phase 1: subgroup coverage, reported and never scored

Build the subgroup table the way the duplication check was built: computed
beside the verdict, printed in the report, and pinned by a test to change no
status and no interval.

- **Units**: every taxonomy node (source A) and every footprint group (source
  B) under the assay's root that clears the evidence floor.
- **Evidence floor** (a new `drift.subgroup` block in `config.yaml`, with its
  justification or the admission there is none): at least *n* evaluable records
  **and** at least *k* distinct footprints **and** records from at least *s*
  distinct deposit dates or submitters. The last two are what stop one
  outbreak's 500 near-identical submissions, or one sequencing error repeated
  by one lab, from becoming a "lineage".
- **Per unit**: detected share with a Wilson interval, the same interval the
  tool already uses for the pooled share.
- **The report line**: the worst-covered unit above the floor, named, with its
  share, its interval and its size, beside the existing pooled verdict.

**The statistics that need care here.** With many subgroups, the lowest one
will look bad partly by luck: test twenty subgroups at the usual 95% and about
one will fall outside its interval by chance alone. This is the multiple
comparisons problem. The standard, conservative answer is to widen each
interval so that *all* of them hold together at 95% (a Bonferroni correction:
use 1 - 0.05/K confidence for K subgroups). It costs sensitivity on small
groups, which is the right direction for a tool whose reports people act on.
And the independence problem from review 3.3 applies inside each subgroup too,
so the footprint-count interval already built for the pooled share is reused
per subgroup, not reinvented.

**The scope question, which is a domain decision, not a statistical one.** A
pan-flavivirus PCR missing insect-specific flaviviruses is recorded as
`partial`, not `fails`, because the gap is outside what most users run it for.
A ferlavirus PCR missing genogroups B and C is a failure, because those are
ferlaviruses. The tool cannot tell these apart from sequences: something has
to record which subgroups an assay is *meant* to cover. See the decisions
below.

### Phase 2: validate, then decide whether the verdict changes

1. Run `scripts/retrospective.py --cases` with the subgroup table, and score
   each failure case as caught only if the worst-covered unit **is** the named
   lineage (or contains it). Report the confusion matrix beside the current
   1-of-12, and the `works` cases contradicted beside the current count.
2. **Choose the floors before looking**, run once, and report what came out.
   With 12 failures, 6 partials and 32 works, there is no room for a held-out
   set, so every threshold tuned on these cases is fitted, not validated. The
   defence is to fix *n*, *k* and *s* from first principles in Phase 1, change
   them only for a reason written down beforehand, and say how many runs it
   took.
3. Only if the subgroup view catches materially more failures **without**
   contradicting more `works` cases does it become part of the headline
   verdict, as a new status (e.g. `lineage gap`) rather than by redefining
   `declining`, so old and new reports stay comparable.

### Phase 3: clustering (source C), with homology anchoring

Deferred until Phase 2 says how much A and B recover. Built together with
review §3.2's homology-anchored scoring, since both need each record aligned
to the assay's reference amplicon. On a cluster this is the first genuinely
parallel job in the project (one alignment job per retrieval group), so it is
where the SLURM profile earns its keep.

## Decisions needed from you before Phase 1

1. **Intended scope per assay.** Options: (a) a new optional registry field
   listing the taxa an assay is meant to cover, filled in only where the paper
   says so; (b) treat the root taxid as the scope and accept that pan-family
   assays will show gaps that are out of scope; (c) scope only the assays in
   the validation set for now. I'd do (c) then (a): it unblocks validation
   without a registry-wide curation pass, which the pause on registry growth
   argues against anyway.
2. **Which taxonomy ranks count as units.** Every node with enough records
   (most sensitive, most comparisons) or only species and below-species nodes
   (fewer comparisons, misses genus-level gaps like papillomavirus). I'd start
   with every node and let the Bonferroni correction pay for it, because the
   genus-level case is one of the 12.
3. **Whether `partial` rows count as successes when the tool names their gap.**
   I'd say yes, and score them separately from `fails` so the two are not
   mixed.

## What this plan does not do

- It does not touch scoring of individual records. The penalty table, the
  chemistry question (`scoring.by_chemistry`, e.g. the PREDICT polyomavirus VP1
  round 1 case) and the declared-size filter are separate work.
- It does not fix the denominator (§3.2). Records with no findable site are
  still excluded until Phase 3, which means a lineage whose sites are too
  diverged to find is still invisible to sources A and B within that lineage.
  Phase 1 should therefore report, per unit, the share of its records that were
  excluded as `no_site` or `diverged` on full-length records, so an all-excluded
  lineage is shown as a gap rather than silently missing.
