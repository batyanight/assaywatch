# Pipeline

Nine stages transform a directory of assay descriptions into a report. Select
any stage for detail.

<figure class="aw-pipeline">
<svg viewBox="0 0 1000 400" role="img" xmlns="http://www.w3.org/2000/svg"
     aria-label="Pipeline flow: the registry is validated, sequences retrieved from GenBank, every oligo screened against every record, calls collected into one table, and that table read by the report, lineage, site-drift and figure stages. The degeneracy table is built from the registry alone.">
  <defs>
    <marker id="aw-arrow" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
    </marker>
  </defs>

  <!-- spine -->
  <g class="aw-node" data-stage="registry" tabindex="0" role="button" aria-label="Open: the registry">
    <rect x="14" y="100" width="104" height="48" rx="6"/>
    <text x="66" y="120">registry</text><text x="66" y="136" class="sub">218 YAML</text>
  </g>
  <g class="aw-node" data-stage="validate" tabindex="0" role="button" aria-label="Open: validate">
    <rect x="150" y="100" width="104" height="48" rx="6"/>
    <text x="202" y="120">validate</text><text x="202" y="136" class="sub">schema + DOI</text>
  </g>
  <g class="aw-node" data-stage="retrieve" tabindex="0" role="button" aria-label="Open: retrieve">
    <rect x="286" y="100" width="104" height="48" rx="6"/>
    <text x="338" y="120">retrieve</text><text x="338" y="136" class="sub">145 archives</text>
  </g>
  <g class="aw-node" data-stage="screen" tabindex="0" role="button" aria-label="Open: screen">
    <rect x="422" y="100" width="104" height="48" rx="6"/>
    <text x="474" y="120">screen</text><text x="474" y="136" class="sub">oligos × records</text>
  </g>
  <g class="aw-node" data-stage="collect" tabindex="0" role="button" aria-label="Open: collect">
    <rect x="558" y="100" width="104" height="48" rx="6"/>
    <text x="610" y="120">collect</text><text x="610" y="136" class="sub">one table</text>
  </g>
  <g class="aw-node aw-store" data-stage="calls" tabindex="0" role="button" aria-label="Open: the calls table">
    <rect x="694" y="100" width="104" height="48" rx="6"/>
    <text x="746" y="120">calls table</text><text x="746" y="136" class="sub">3.0M rows</text>
  </g>

  <!-- spine arrows, labelled -->
  <g class="aw-edge">
    <line x1="118" y1="124" x2="146" y2="124" marker-end="url(#aw-arrow)"/>
    <line x1="254" y1="124" x2="282" y2="124" marker-end="url(#aw-arrow)"/>
    <text x="268" y="114">targets</text>
    <line x1="390" y1="124" x2="418" y2="124" marker-end="url(#aw-arrow)"/>
    <text x="404" y="114">FASTA</text>
    <line x1="526" y1="124" x2="554" y2="124" marker-end="url(#aw-arrow)"/>
    <text x="540" y="114">per archive</text>
    <line x1="662" y1="124" x2="690" y2="124" marker-end="url(#aw-arrow)"/>
  </g>

  <!-- fan-out -->
  <g class="aw-node" data-stage="report" tabindex="0" role="button" aria-label="Open: drift and report">
    <rect x="854" y="18" width="132" height="44" rx="6"/>
    <text x="920" y="36">drift + report</text><text x="920" y="52" class="sub">the verdicts</text>
  </g>
  <g class="aw-node" data-stage="lineage" tabindex="0" role="button" aria-label="Open: lineage analysis">
    <rect x="854" y="78" width="132" height="44" rx="6"/>
    <text x="920" y="96">lineage</text><text x="920" y="112" class="sub">per clade</text>
  </g>
  <g class="aw-node" data-stage="sitedrift" tabindex="0" role="button" aria-label="Open: site drift">
    <rect x="854" y="138" width="132" height="44" rx="6"/>
    <text x="920" y="156">site drift</text><text x="920" y="172" class="sub">which base</text>
  </g>
  <g class="aw-node" data-stage="figures" tabindex="0" role="button" aria-label="Open: figures">
    <rect x="854" y="198" width="132" height="44" rx="6"/>
    <text x="920" y="216">figures</text><text x="920" y="232" class="sub">SVG, inlined</text>
  </g>
  <g class="aw-node" data-stage="degeneracy" tabindex="0" role="button" aria-label="Open: degeneracy">
    <rect x="854" y="300" width="132" height="44" rx="6"/>
    <text x="920" y="318">degeneracy</text><text x="920" y="334" class="sub">pool size</text>
  </g>

  <g class="aw-edge">
    <path d="M 798 118 C 830 118 826 40 850 40" fill="none" marker-end="url(#aw-arrow)"/>
    <path d="M 798 122 C 830 122 826 100 850 100" fill="none" marker-end="url(#aw-arrow)"/>
    <path d="M 798 126 C 830 126 826 160 850 160" fill="none" marker-end="url(#aw-arrow)"/>
    <path d="M 798 130 C 830 130 826 220 850 220" fill="none" marker-end="url(#aw-arrow)"/>
  </g>

  <!-- lineage can override the pooled verdict; the only backward edge -->
  <g class="aw-edge aw-dashed">
    <path d="M 920 78 L 920 62" fill="none" marker-end="url(#aw-arrow)"/>
    <text x="996" y="72" text-anchor="end">worst clade can override</text>
  </g>

  <!-- degeneracy is built from the registry alone, never from sequence -->
  <g class="aw-edge aw-dashed">
    <path d="M 66 148 L 66 322 L 850 322" fill="none" marker-end="url(#aw-arrow)"/>
    <text x="300" y="312">from the oligos alone — no sequence involved</text>
  </g>

  <!-- config feeds the three stages that make judgements -->
  <g class="aw-edge aw-dashed">
    <path d="M 474 190 L 474 152" fill="none" marker-end="url(#aw-arrow)"/>
    <path d="M 500 190 C 700 190 700 60 850 42" fill="none" marker-end="url(#aw-arrow)"/>
  </g>
  <g class="aw-node aw-config" data-stage="config" tabindex="0" role="button" aria-label="Open: the thresholds">
    <rect x="408" y="190" width="132" height="42" rx="6"/>
    <text x="474" y="207">config.yaml</text><text x="474" y="223" class="sub">19 thresholds</text>
  </g>
</svg>
<figcaption>
Sequence flows left to right and is never re-fetched to re-score: every archive
is kept whole, so changing a threshold re-reads what is already on disk.
Dashed edges are influences rather than data — the thresholds that decide
verdicts, the one backward path where a single bad clade overrides an otherwise
reassuring overall figure, and the degeneracy table, which is computed from the
oligo sequences alone.
</figcaption>
</figure>

<div class="aw-stage-detail" markdown>

## <span class="aw-stage-title">The registry</span> {: #stage-registry .aw-stage }

One YAML file per assay, 218 of them. Each carries the oligo sequences, the
target organism, the chemistry, the product size, and the paper it came from.

Entries are not accepted on trust:

- **Nothing is cited from memory.** A DOI is entered unverified and only
  Crossref can promote it. An assay whose citation cannot be confirmed waits in
  a holding area and is never screened or published.
- **Sequences and product sizes are measured, not copied.** Where a measured
  product length disagrees with the published one, the entry keeps the measured
  value and records the disagreement. A published size is usually a band read
  against a ladder; this one is computed from where the primers actually sit.
- **Problems are recorded in a controlled vocabulary** rather than in prose, so
  they can be filtered on. Nineteen assays carry a flag serious enough that no
  verdict is published for them at all.

**Out:** validated entries, plus the list of organisms and genes to fetch.

## <span class="aw-stage-title">validate</span> {: #stage-validate .aw-stage }

Runs before anything else and refuses to let the pipeline start on a registry
that does not parse, has a duplicate key, or contains an entry without a
confirmed citation.

This also runs on every commit, so a broken entry never reaches a run in the
first place. The schema is strict: an unrecognised field is an error rather
than being quietly ignored, which is what stops a typo in a field name from
silently disabling a setting.

**In:** `registry/*.yaml` · **Out:** a go-ahead, or a list of every bad file at
once rather than just the first.

## <span class="aw-stage-title">retrieve</span> {: #stage-retrieve .aw-stage }

Fetches nucleotide records from GenBank for each target and stores them.

Assays that share a target and a gene search share one archive — 218 assays map
onto **145 archives**, so a shared target is fetched once rather than once per
assay.

Fetching is **incremental**: each archive remembers when it was last updated and
asks only for records modified since. Whole records are kept rather than just
the primer-binding regions, which is what makes re-scoring free — changing a
threshold re-reads the disk instead of re-downloading GenBank.

!!! warning "The failure this stage can hide"
    A search is a claim about what population you are judging an assay against,
    and it can stop being true without erroring. Four influenza assays here used
    searches naming subtype identifiers that NCBI stopped assigning; their
    archives quietly stopped growing years before anyone noticed, while the
    reports said something true and misleading — "no recent records" — about the
    organism rather than about the search. [Scope and retrieval](scoping.md) documents the case.

**Out:** compressed FASTA archives plus a record of when each was last fetched.

## <span class="aw-stage-title">screen</span> {: #stage-screen .aw-stage }

The expensive stage, and the only one that touches sequence at scale.

Every oligo of every assay is searched against every record of its archive, on
both strands, allowing up to six mismatches. Where a forward and reverse site
face each other at a plausible product size, mismatches become a penalty and the
penalty becomes a call. [Scoring methods](scoring.md).

On the run this site is built from, that was **3.0 million assay-record pairs**.
It runs across cores and the output is identical whatever the core count, so a
faster run is never a different run.

**Results are cached per archive** and re-used until something that could change
them changes. The scoring settings and the set of modules the stage imports are
both hashed into that cache key, so editing a penalty invalidates every screen
automatically rather than relying on anyone remembering to clear it.

**Out:** one row per (assay, record): the call, the penalty, the product
coordinates, and each oligo's mismatch positions measured from its 3' end.

## <span class="aw-stage-title">collect</span> {: #stage-collect .aw-stage }

Gathers the cached per-archive results into one table for the run.

It also checks each cached screen against a record of what produced it, so a
screen left over from older settings is detected here rather than being silently
mixed with current ones. That check exists because stale cached screens from
months earlier once inflated three separate measurements by around a hundredfold.

**Out:** `calls.tsv.gz` — 3.0 million rows, about 22 MB compressed, the single
input to everything downstream.

## <span class="aw-stage-title">The calls table</span> {: #stage-calls .aw-stage }

Everything after this point reads this one file and nothing else. That is
deliberate: the four analyses below cannot disagree about what the data say,
because there is only one copy of it.

Of the 3.0 million rows on this run, **1.57 million were evaluable** — both
primers landed in the right orientation and size range, so the result is a
statement about the assay. The other 1.47 million produced no product at all.

That split is the method's honest weak point: a record where one primer has
drifted counts as a failure, while a record where *both* have drifted leaves the
denominator entirely. Every assay page reports its own split.

## <span class="aw-stage-title">drift + report</span> {: #stage-report .aw-stage }

Groups calls by the year each record was deposited, compares recent detection
against everything earlier, and assigns a status.

An assay is flagged only when the **upper** bound of its recent confidence
interval falls below the threshold — the data must be inconsistent with the
assay still working, not merely compatible with it failing. Where records are
scarce the window widens, up to five years, and each assay reports the window it
used.

**Out:** `report.md` for reading on GitHub, and a self-contained `report.html`
with no external dependencies, so it opens from a file path in a lab with no
bioinformatician.

## <span class="aw-stage-title">lineage</span> {: #stage-lineage .aw-stage }

Splits each assay's records by organism below the target and recomputes
detection per clade.

This matters because a single pooled percentage hides exactly what you care
about: published failures are nearly always specific to one lineage, and a clade
that is 5% of deposits can be 100% of one region's cases.

It is the only stage that can change a verdict rather than just describe one. If
one well-sampled clade is significantly below the threshold after correcting for
multiple comparisons, it overrides an otherwise reassuring overall figure.

## <span class="aw-stage-title">site drift</span> {: #stage-sitedrift .aw-stage }

For assays with a problem, works out **which base** is responsible.

For each oligo position it compares detection among records that mismatch there
against records that do not, groups the records sharing a mismatch pattern, and
names the degenerate base that would cover most of the variation observed.

This is the stage whose output is directly actionable: it names the base to
change if you were to re-order the primer.

## <span class="aw-stage-title">figures</span> {: #stage-figures .aw-stage }

Draws the overview plots and inlines them into the HTML report.

It recomputes the assessments rather than parsing the written report, so the
figures and the tables cannot drift apart — reading numbers back out of rendered
text would be a second implementation of the same arithmetic, free to disagree
with the first.

## <span class="aw-stage-title">degeneracy</span> {: #stage-degeneracy .aw-stage }

Computed from the oligo sequences alone — no sequence database involved, which
is why it hangs off the registry rather than the calls table.

A degenerate primer is a mixture, and the number of distinct molecules in that
mixture dilutes the one that matches your template. This reports pool size per
assay and flags the extreme cases; the largest in the registry exceeds a billion
combinations.

It is **reported and never scored**. A degenerate base covering the record's
base counts as a match, because that is what degeneracy is for.

## <span class="aw-stage-title">config.yaml</span> {: #stage-config .aw-stage }

Nineteen thresholds decide every verdict and all but one were set by eye. None
of them live in code.

Each is annotated in place with its reasoning, or with an explicit admission
that it has none — including the detection threshold itself, which is a
judgement about tolerable surveillance loss rather than a property of PCR.

The settings that affect scoring are hashed into the screening cache, so
changing one of them forces a complete re-screen rather than producing a report
that mixes old and new rules.

[Known limitations](limitations.md) summarises what the output will bear.

</div>

*A complete run takes approximately 50 minutes on eight cores, excluding retrieval.*
