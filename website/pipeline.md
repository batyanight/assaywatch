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
Sequence flows left to right and is never re-retrieved in order to re-score:
archives are retained complete, so a threshold change re-reads local storage.
Dashed edges denote influence rather than data flow — the thresholds governing
verdicts, the single reverse path by which one failing clade overrides an
otherwise reassuring pooled figure, and the degeneracy table, computed from the
oligonucleotide sequences alone.
</figcaption>
</figure>

<div class="aw-stage-detail" markdown>

## <span class="aw-stage-title">The registry</span> {: #stage-registry .aw-stage }

One YAML file per assay; 218 in total. Each records the oligonucleotide
sequences, target organism, chemistry, product size and source publication.

Entries are not accepted on assertion:

- **No citation is entered from memory.** A DOI is recorded as unverified and
  only Crossref can promote it. An assay whose citation cannot be confirmed is
  held and is neither screened nor published.
- **Sequences and product sizes are measured rather than transcribed.** Where
  a measured product length disagrees with the published value, the entry
  retains the measured value and records the discrepancy. A published size is
  typically a band read against a ladder; the measured value is computed from
  primer binding positions.
- **Known problems are recorded in a controlled vocabulary** rather than prose,
  so that they can be filtered. Nineteen assays carry a flag sufficient to
  withhold any verdict.

**Output:** validated entries and the set of organisms and genes to retrieve.

## <span class="aw-stage-title">validate</span> {: #stage-validate .aw-stage }

Executes before any other stage and halts the pipeline on a registry that does
not parse, contains a duplicate key, or holds an entry without a confirmed
citation.

It also runs on every commit, so a malformed entry does not reach a run. The
schema is strict: an unrecognised field is an error rather than being ignored,
which prevents a mistyped field name from silently disabling a setting.

**Input:** `registry/*.yaml` · **Output:** clearance to proceed, or every
invalid file reported at once rather than only the first.

## <span class="aw-stage-title">retrieve</span> {: #stage-retrieve .aw-stage }

Retrieves nucleotide records from GenBank for each target and archives them.

Assays sharing a target and gene search share one archive: 218 assays map onto
**145 archives**, so a shared target is retrieved once rather than once per
assay.

Retrieval is **incremental**. Each archive records when it was last updated and
requests only records modified since. Complete records are retained rather than
only the primer-binding regions, which is what makes re-scoring inexpensive: a
threshold change re-reads local storage rather than re-querying GenBank.

!!! warning "Failure mode concealed by this stage"
    A search is a claim about the population against which an assay is
    evaluated, and it can cease to be true without producing an error. Four
    influenza assays used searches naming subtype identifiers that NCBI ceased
    assigning; those archives stopped growing years before the problem was
    identified, while the reports stated something true and misleading — "no
    recent records" — about the organism rather than about the search.
    [Scope and retrieval](scoping.md) documents the case.

**Output:** compressed FASTA archives and a record of each archive's last
retrieval date.

## <span class="aw-stage-title">screen</span> {: #stage-screen .aw-stage }

The computationally dominant stage, and the only one operating on sequence at
scale.

Every oligonucleotide of every assay is searched against every record of its
archive, on both strands, allowing up to six mismatches. Where forward and
reverse sites face each other at a plausible product size, mismatches are
converted to a penalty and the penalty to a call. See
[scoring methods](scoring.md).

On the run underlying this site, that comprised **3.0 million assay–record
pairs**. Execution is parallelised across cores and the output is independent
of core count, so a faster run is not a different run.

**Results are cached per archive** and reused until an input that could change
them changes. The scoring configuration and the stage's module import closure
are both hashed into the cache key, so modifying a penalty invalidates every
cached screen automatically rather than depending on manual invalidation.

**Output:** one row per (assay, record) giving the call, the penalty, the
product coordinates, and each oligonucleotide's mismatch positions measured
from its 3′ terminus.

## <span class="aw-stage-title">collect</span> {: #stage-collect .aw-stage }

Consolidates the cached per-archive results into a single table for the run.

Each cached screen is checked against a record of the configuration that
produced it, so a screen remaining from earlier settings is detected here
rather than being combined with current results. The check exists because
stale cached screens once inflated three separate measurements by
approximately two orders of magnitude.

**Output:** `calls.tsv.gz` — 3.0 million rows, approximately 22 MB compressed;
the sole input to every downstream stage.

## <span class="aw-stage-title">The calls table</span> {: #stage-calls .aw-stage }

Every subsequent stage reads this file and nothing else. This is deliberate:
the four analyses below cannot disagree about the data, because a single copy
exists.

Of the 3.0 million rows in this run, **1.57 million were evaluable** — both
primers bound in the correct orientation and size range, so the result is a
statement about the assay. The remaining 1.47 million produced no product.

That division is the principal weakness of the method: a record in which one
primer has diverged is scored as a failure, whereas a record in which *both*
have diverged is excluded from the denominator entirely. Each assay page
reports its own figures.

## <span class="aw-stage-title">drift + report</span> {: #stage-report .aw-stage }

Groups calls by deposit year, compares recent detection against all earlier
records, and assigns a status.

An assay is flagged only where the **upper** bound of its recent confidence
interval falls below the threshold: the data must be inconsistent with
continued function, not merely compatible with failure. Where records are
scarce the window extends to a maximum of five years, and each assay reports
the window applied.

**Output:** `report.md` for reading on GitHub, and a self-contained
`report.html` with no external dependencies, which opens from a local file path
without specialist software.

## <span class="aw-stage-title">lineage</span> {: #stage-lineage .aw-stage }

Divides each assay's records by organism below the target and recomputes
detection per clade.

A single pooled proportion conceals the relevant signal: published failures are
almost always specific to one lineage, and a clade representing 5% of deposits
may represent 100% of cases in one region.

This is the only stage that can alter a verdict rather than describe one. Where
one adequately sampled clade is significantly below the threshold after
correction for multiple comparisons, it overrides an otherwise reassuring
pooled figure.

## <span class="aw-stage-title">site drift</span> {: #stage-sitedrift .aw-stage }

For flagged assays, identifies **which base** is responsible.

For each oligonucleotide position it compares detection among records carrying
a mismatch at that position against records that do not, groups records sharing
a mismatch pattern, and identifies the degenerate base that would cover most of
the observed variation.

This stage produces the directly actionable output: the base to substitute in a
redesigned primer.

## <span class="aw-stage-title">figures</span> {: #stage-figures .aw-stage }

Draws the overview plots and embeds them in the HTML report.

The assessments are recomputed rather than parsed from the rendered report, so
figures and tables cannot diverge: reading values back out of rendered text
would constitute a second implementation of the same arithmetic, free to
disagree with the first.

## <span class="aw-stage-title">degeneracy</span> {: #stage-degeneracy .aw-stage }

Computed from the oligonucleotide sequences alone, with no sequence database
involved, which is why it derives from the registry rather than the calls
table.

A degenerate primer is a mixture, and the number of distinct molecules in that
mixture dilutes the species matching any given template. This stage reports
pool size per assay and flags extreme cases; the largest in the registry
exceeds 10⁹ combinations.

It is **reported and never scored**. A degenerate base covering the record's
base is counted as a match, which is the purpose of degeneracy.

## <span class="aw-stage-title">config.yaml</span> {: #stage-config .aw-stage }

Nineteen thresholds determine every verdict; all but one were set by
inspection. None are embedded in code.

Each is annotated at its definition with its justification, or with an explicit
statement that none exists — including the detection threshold itself, which
expresses a judgement about tolerable surveillance loss rather than a property
of PCR.

Settings affecting scoring are hashed into the screening cache, so modifying
one forces a complete re-screen rather than producing a report combining old
and new rules.

[Known limitations](limitations.md) summarises what the output will bear.

</div>

*A complete run takes approximately 50 minutes on eight cores, excluding retrieval.*
