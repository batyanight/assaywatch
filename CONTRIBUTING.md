# Contributing an assay

The registry is a set of published PCR assays with enough provenance that each
one can be checked against sequence data. An entry is only as good as its
traceability, so a submission needs a source anyone can read, not just a pair of
sequences.

Every error this registry has had was a transcription or provenance error, never
a modelling one: a *Sarcocystis* primer with one extra C that failed on 98% of
records, two orthobunyavirus primers carrying undeclared cloning tails that
matched nothing, three taxids pointing at the wrong organism (one at a genus of
moths), five DOIs resolving to other papers. The process below exists to catch
exactly those before an entry reaches a report.

## 1. Fill in the template

Copy this to `registry/<YOUR_ASSAY_ID>.yaml`. The id must equal the filename
stem, and by convention reads `TAXON_genome_target_source`.

```yaml
id: EXAMPLE_ssRNA_L_gene_Author_2024
name: EXAMPLE VIRUS (ssRNA) — L gene (Author 2024)
target:
  taxid: 12345                  # NCBI Taxonomy id; the assay is screened against this taxon
  gene: L                       # the locus, as the paper names it
  genome_type: ssRNA-           # dsDNA | ssDNA | dsRNA | ssRNA+ | ssRNA- | ssRNA-RT | mtDNA
  taxon_name: Example virus
  query: null                   # optional Entrez terms, ANDed onto the taxon (see below)
chemistry: conventional         # conventional | sybr | hydrolysis_probe | mgb | lna
oligos:
  forward:
    name: EX-F1
    seq: ACGTACGTACGTACGTACGT    # strict IUPAC; write inosine as N here
    seq_as_written: null         # the original with I, if the primer contains inosine
    tail_5prime: null            # 5' bases that do NOT bind the target (see below)
  reverse:
    name: EX-R1
    seq: TTGCATTGCATTGCATTGCA
  probe: null                    # required for hydrolysis_probe / mgb / lna
  alternates: []                 # pool members; each needs `orientation`
amplicon_bp: 320                 # the product size the paper reports
citation:
  doi: 10.1000/example
  design_year: 2024
  n_sequences_at_design: null    # how many sequences the design was based on, if stated
  as_written: null               # the citation as your source wrote it, for provenance
  reference: 'Author A et al. Title. Journal 1, 1-10 (2024).'
  doi_verified: false            # left false; scripts/resolve_citations.py sets it
use_context: [wildlife]
submitted_by: Your Name
status: draft                    # only a maintainer sets `active`
source:
  spreadsheet: null
  predict_protocol: null         # P-001..P-041 if this is a PREDICT panel assay
  rows: null
  positive_control: null
  nested_round: null             # round1 | round2 for a nested assay
  notes: null
  notes_curator: null            # anything a later reader needs to know
needs_review: null               # see below; null when there is nothing to flag
```

A flagged entry looks like this instead:

```yaml
needs_review:
- flag: oligos_read_from_figure
- flag: amplicon_disagrees_with_paper
  note: measured 83 bp in 663 of 663 records; both citing papers say 87 bp
```

`flag` must be one of the values in `assaywatch/review.py`; the validator
rejects anything else, and that module's docstring says why the field is a
controlled vocabulary rather than free text. Pick the flag that a *filter* would
ask for and put the entry's own specifics in `note`; one item per flag, so two
findings about the same flag are one item with both in the note. If no flag
fits, say what is pending under `curation_decision_pending` (which requires a
note) rather than inventing a flag — and then the vocabulary is probably missing
a category, which is worth raising.

Four flags that existed before 2026-10-21 are deliberately absent: `DOI_MISSING`,
`DOI_UNVERIFIED`, `NO_YEAR` and `TAXID_MISSING` only restated `citation.doi`,
`citation.doi_verified`, `citation.design_year` and `target.taxid` on the same
document. Do not re-add them in any form. Leave the field null and let the
consumer ask the field.

Three fields deserve care:

- **`seq` versus `seq_as_written`.** `seq` is strict IUPAC, so inosine is written
  as `N`; `seq_as_written` keeps the `I`. Matching and degeneracy both use
  `seq_as_written` where it exists, because an inosine is one molecule that pairs
  with C, A and T, not a 4-fold degenerate position. Reading the PREDICT
  filovirus reverse primer from `seq` would call it 8192-fold degenerate when it
  is 8-fold.
- **`tail_5prime`.** If the printed primer begins with bases that do not bind the
  target — a restriction site and clamp for cloning, an M13 or sequencing
  adapter — declare them. An undeclared tail makes the assay appear to match
  nothing: the CDV F-gene primers carry SalI and NotI tails and matched 0 of
  3,990 records until they were declared.
- **`query`.** Without one, the assay is screened against every record for its
  taxon, most of which will not carry the locus. That is only a cost in noise,
  except where the taxon is huge. With one, records the query misses are records
  the assay is never judged against — a coverage cost, not a scoring error. Use
  `--dry-run` on retrieval to see the counts before deciding.

## 2. Check it

```bash
python scripts/check_submission.py registry/YOUR_ASSAY.yaml --email you@example.org
```

This runs, in increasing cost: schema and oligo validity; a scan for restriction
sites sitting at an oligo's 5' end; the degeneracy of the primer pool; whether
the DOI resolves to the paper the entry names; whether the taxid still means
what the entry says; and then the decisive one — whether the oligos actually
find their amplicon in real records for that target.

That last check is the one that matters. **An assay whose primers match nothing
in their own target taxon is far more likely to be mistyped than to be a
discovery.** It is what catches a dropped base, a reverse primer stored without
being reverse-complemented, and an undeclared tail. It samples across the
archive rather than from the front of it, because archives are ordered by
accession and the head of one is never representative.

A `WARN` is not a blocker: a newly described pathogen with three deposited
sequences will warn, and is still a good submission. A `FAIL` needs an answer
before the entry is trusted.

If the target has no archive yet, fetch one first:

```bash
python -m assaywatch.retrieve registry/YOUR_ASSAY.yaml --email you@example.org --dry-run
python -m assaywatch.retrieve registry/YOUR_ASSAY.yaml --email you@example.org
```

## 2b. Check the sequences against the paper, not against a spreadsheet

```bash
python scripts/verify_oligos_against_paper.py --assay YOUR_ASSAY --pdf-dir ~/Downloads
```

**The literature is the truth. A lab spreadsheet is a place to start.** 138 of
the 151 entries here were transcribed from one spreadsheet, and that spreadsheet
has already been caught in a *Sarcocystis* primer carrying an extra C, two
undeclared cloning tails, three taxids naming the wrong organism, five DOIs
resolving to other papers, an amplicon of 500 bp where the paper says 531, and
an oligo named `Ziao18SF1` for a paper by Xiao.

This fetches the paper's open-access full text — or reads a PDF you have
downloaded — and looks for each stored sequence in it. Papers print reverse
primers in either orientation and break sequences into codon groups, both of
which it handles. When a sequence is **not** found it reports the closest
printed oligo by edit distance, so `near:1` arrives with the correction already
attached.

Where the registry and the paper disagree, **the paper wins**. If the stored
sequence was a deliberate lab modification, record it as a modification rather
than as the published assay, and set `citation.oligos_designed_here`
accordingly.

## 3. Open a pull request

Include the paper's table or figure the sequences came from, or a quotation of
it. Sequences transcribed from a secondary source — a review, another
registry, a lab spreadsheet — are the main source of error here, so say which
you used. CI runs the registry validator on every push.

## Finding assays to add

```bash
python scripts/scan_literature.py --since 2024 --full-text --out results/candidates.tsv
```

This searches Europe PMC for recent papers that look like they publish an assay
for a taxon the registry already tracks, and writes a review queue sorted so
that papers with readable oligo sequences in their open full text come first.
It proposes and never adds: a row is a reading assignment. Precision is modest
even with title and abstract filtering — expect roughly one paper in five to
actually contain a usable primer table.

For a target the registry does not cover yet, pass `--taxon` with the name you
want searched.

## What makes an entry `active`

`draft` is the default and means the entry is believed correct but unproven.
`active` additionally requires a taxid, a verified DOI, a design year, no *open*
review flag, and that the schema's own checks pass — the validator enforces
this. A recorded caveat such as `nested_protocol` or `cross_reactive` is no bar:
it is a permanent, disclosed property of a sound entry, and refusing those here
is what kept 146 of 208 entries permanently unactivatable before 2026-10-21.

**`submitted_by` is not required, as of 2026-10-21.** Every other precondition is
evidence about the assay; authorship is not. Once the review-flag rule was fixed,
`submitted_by` was the only thing blocking 167 of 208 entries — including all
four remaining Phase 0 candidates — because the registry was bulk-imported by one
curator and 207 of 208 entries leave the field null. Setting it 207 times to one
name would have been a rubber stamp. Fill it in if you are submitting an entry;
do not treat it as a step on the way to `active`.

What that leaves is judgement, and only a maintainer sets `active`. In practice a
maintainer wants the assay to have been screened against real records with a
defensible result, and its orientation confirmed rather than inferred from the
order of rows in a spreadsheet. A `watch` status is not automatically a bar —
`active` means the assay can be screened and cited, not that it performs well,
and the report says `watch` either way — but a maintainer should say so
deliberately rather than by default.

`deprecated` means do not use: kept so that reports and past analyses still
resolve the id.

## Reviewing a submission

Maintainers: run `scripts/check_submission.py` on the entry, then
`scripts/check_taxids.py` and `scripts/resolve_citations.py` over the registry,
and screen the assay's group before merging. If the assay's performance has been
reported anywhere in the literature, add a row to `docs/validation-cases.tsv` —
that file is the only thing calibrating the thresholds in `config.yaml`, and it
is dated to the latest sequence each cited paper could have seen so that the
tool is never shown the answer. A `fails` row also records its `mechanism`, `drift` or
`coverage`, from the source's own account of why the assay missed (see the
header of that file); it decides whether `low coverage` counts as agreement.
