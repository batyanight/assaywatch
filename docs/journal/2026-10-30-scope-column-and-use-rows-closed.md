# A case may now name the lineage its paper tested; and the 93 unconfirmed `use` rows are closed without a new case

2026-10-30, two items in one branch because the second is the answer to a question the first
raises: whether more reading would improve the tier-2 matrix.

## 1. `scope_taxid`: a case row may name the lineage the paper tested

Decided the same evening (`2026-10-30-design-grilled.md` Q7) after held-out set 2 put **four
pan-family nests among its five false alarms**. Those papers report the assay amplifying a
divergent virus from a handful of positives. That `works` is about the lineage they tested;
the pooled status is about every deposit for the family. The matrix was scoring one against
the other.

Both case files gain an optional `scope_taxid` column. Where it is given and per-lineage
statistics exist, `scripts/retrospective.py` scores that lineage's own records; the run
prints which rows were scored that way and, separately, every scope it could not honour.

**The test, and why it carries no correction.** The same binomial `worst_lineage_verdict`
uses: P(X <= detected | n, threshold). That function corrects family-wise across every
lineage of an assay because it asks "is ANY lineage failing". Here the lineage is named in
advance, from the paper, before any share is computed, so there is no family of tests and no
correction applies. A lineage below the threshold reads `fails`, above it `works`; there is
no per-lineage `partial`, because "some of the diversity and not the rest" is a statement
about an assay across lineages and cannot be made about one. A `partial` expectation
therefore ignores its scope, and so does a lineage with fewer evaluable records than
`drift.min_records_for_coverage`, which reads `undecided` rather than being scored.

**No scope value was filled in.** The taxid has to come from the paper, the same rule every
other column obeys, and that is a maintainer's read. **And the rule was chosen after set 2
was read**, so on set 2's rows it can only ever be a description; its first honest test is on
rows not yet collected. Both file headers say so.

## 2. The 93 `use` rows that did not reach CONFIRMED: closed, no new case

`docs/2026-10-29-use-identity.tsv` holds 294 oligo-level rows, 31 CONFIRMED. Of the 257 that
are not, the reasons are mechanical and mostly final:

| why it missed | oligo rows |
|---|---|
| the paper prints no oligo table at all; it cites the assay only | 126 |
| no open-access PMC copy (a PDF would have to be fetched) | 73 |
| the paper prints a table of 3 to 14 oligos and ours is not among them | 49 |
| a printed primer differs by one or more fixed bases | 6 |
| fetch failed (Europe PMC HTTP 500) | 7 |
| a primer occurs only in running text | 2 |

The re-read targeted the only class that could still turn: **57 rows over 13 papers that DO
print a table**. At the oligo level they are 49 `absent`, 4 `exact`, 3 `near:1`, 1 `in-text`,
so exactly **four candidate pairs** have any slot the paper prints. Each was chased to its own
design paper:

- **Pan-herpes DPOL round 2 in the pudu paper** (10.1080/01652176.2022.2149879): HV-TGV
  exact, HV-IYG one edit away, because that paper prints a **23-mer**,
  `CACAGAGTCCGRTCNCCRTADAT`. VanDevanter 1996's own PDF prints
  `CACAGAGTCCGTRTCNCCRTADAT`, the 24-mer the registry stores, and
  `verify_oligos_against_paper.py` reads **5 of 5 oligos exact** against it. So the citing
  paper dropped a base when it retyped a degenerate primer. The registry is right, the row is
  not confirmable from that table, and the paper's round-1 `works` row in set 2 stands.
- **The two coronavirus RdRp entries** in the Cameroon survey (10.1093/ve/veab110) and
  10.1186/s13104-021-05880-6: CoV-FWD3 exact with CoV-RVS3 one edit away, and CoV-RVS1 exact
  with CoV-FWD1 in-text. Both entries store a deliberate PREDICT modification: the verifier
  reads `modified` against their own papers, which print the `modified_from` form exactly. An
  entry that stores a modification can never be CONFIRMED by a paper printing the original —
  that is the VARIANT rule working, not a miss.

**So the `use` family is spent too, and for a reason rather than for want of effort.** No new
(paper, assay) pair is confirmable, and the one pattern worth remembering is that a `near:1`
on a degenerate oligo is usually the CITING paper's transcription error: two unrelated papers
here each dropped exactly one base from a published degenerate primer. The 73 rows behind a
paywall remain the only class a human with a proxy could still move, and on this evidence the
yield would be low.

**What this says about the matrix.** More reading of this shape will not improve it. The
remaining levers are the scope column above, which asks the papers already in hand a fairer
question, and a search for a drift-mechanism case, which is a different search.
