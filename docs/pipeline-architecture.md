# Pipeline Architecture

Snakemake pipeline for continuous primer-drift surveillance. Each run
re-screens published PCR/qPCR assay primers against newly deposited NCBI
sequences, computes drift statistics, and generates reports.

## Pipeline overview

```mermaid
flowchart TD
    subgraph registry ["Registry & validation"]
        R[("registry/*.yaml")] --> V["validate"]
        V --> S[".registry-valid\n(sentinel)"]
    end

    subgraph retrieval ["Retrieval (checkpoint)"]
        S --> RET["retrieve\n(checkpoint)"]
        RET --> G1["gene (q*)"]
        RET --> G2["all"]
        RET --> G3["asm"]
        G1 & G2 & G3 --> AR[("archives +\nmanifest")]
    end

    subgraph screening ["Screening"]
        AR --> SC["screen_archive\n(per-archive, cached)"]
        SC --> CC["collect_calls"]
        CC --> CALLS[("calls.tsv.gz")]
        TRG["_code_hash\ninvalidation"] -.-> SC
    end

    subgraph analysis ["Analysis"]
        CALLS --> RPT["report\n(drift assessment)"]
        CALLS --> LIN["lineage_analysis"]
        LIN -. "one-direction\noverride" .-> RPT
    end

    subgraph reporting ["Reporting"]
        CALLS --> FIG["figures"]
        FIG --> |"inlined"| RPT
        RPT --> O1["report.md\n+ report.html"]
        FIG --> O5["forest.svg\nsite-positions.svg\nfigures.html"]
        CALLS --> SD["site_drift"]
        SD --> O2["site-drift.md\n+ site-drift.tsv"]
        LIN --> O3["lineage.md"]
        S --> DG["degeneracy_table"]
        DG --> O4["degeneracy.tsv"]
    end

    CFG[("config.yaml")] -.-> SC & RPT & LIN

    style R fill:#f3f4f6,stroke:#6b7280
    style AR fill:#f3f4f6,stroke:#6b7280
    style CALLS fill:#f3f4f6,stroke:#6b7280
    style CFG fill:#fef3c7,stroke:#d97706
    style V fill:#e0f5f0,stroke:#2a9d8f
    style S fill:#e0f5f0,stroke:#2a9d8f
    style RET fill:#dbeafe,stroke:#3b82f6
    style G1 fill:#e0f5f0,stroke:#2a9d8f
    style G2 fill:#e0f5f0,stroke:#2a9d8f
    style G3 fill:#e0f5f0,stroke:#2a9d8f
    style SC fill:#ffe4e6,stroke:#e11d48
    style CC fill:#e0f5f0,stroke:#2a9d8f
    style TRG fill:#f3f4f6,stroke:#6b7280
    style RPT fill:#dbeafe,stroke:#3b82f6
    style LIN fill:#dbeafe,stroke:#3b82f6
    style SD fill:#d1fae5,stroke:#059669
    style DG fill:#d1fae5,stroke:#059669
    style O1 fill:#d1fae5,stroke:#059669
    style O2 fill:#d1fae5,stroke:#059669
    style O3 fill:#d1fae5,stroke:#059669
    style O4 fill:#d1fae5,stroke:#059669
    style FIG fill:#ede9fe,stroke:#7c3aed
    style O5 fill:#d1fae5,stroke:#059669
```

---

## Step-by-step

### 1. Validate

Each YAML file in `registry/` defines one assay: its taxid, primer sequences,
and probe. The rule checks that taxids resolve in NCBI, primer sequences are
valid IUPAC, and no two assays share a name. Output is a sentinel file (empty
file whose existence means "validation passed") — Snakemake uses its timestamp
to know whether to re-validate.

```mermaid
flowchart LR
    A[("registry/*.yaml")] --> B["validate\n(python -m assaywatch.validate)"]
    B --> C[".registry-valid\n(sentinel touch file)"]
    B -- "fails on" --> D["bad taxid\ninvalid IUPAC\nduplicate name"]

    style A fill:#f3f4f6,stroke:#6b7280
    style B fill:#e0f5f0,stroke:#2a9d8f
    style C fill:#e0f5f0,stroke:#2a9d8f
    style D fill:#fee2e2,stroke:#dc2626
```

### 2. Retrieve (checkpoint)

`targets_from_registry()` reads the validated YAML and builds a map of
`(taxid, group)` → query parameters. Three group types fan out to NCBI Entrez:
gene-targeted queries (`q*` groups scoped to specific genes), broad nucleotide
(`all`), and genome assemblies (`asm`). An exclusive file lock prevents
concurrent runs from corrupting the manifest. This rule is a Snakemake
*checkpoint* — its outputs aren't known until it finishes, so downstream rules
re-evaluate after it runs. Archives and manifest are deliberately kept outside
Snakemake's output tracking so Snakemake never deletes them before re-running.

```mermaid
flowchart TD
    VALID[".registry-valid"] --> TFR["targets_from_registry()"]
    TFR --> MAP["(taxid, group) → query map"]
    MAP --> Q1["gene (q*)\nesearch | efetch"]
    MAP --> Q2["all\nesearch | efetch"]
    MAP --> Q3["asm\nncbi datasets"]
    Q1 & Q2 & Q3 --> FASTA[("FASTA archives\ndata/retrieved/")]
    Q1 & Q2 & Q3 --> MAN[("manifest.json")]
    LOCK["file lock\n(exclusive)"] -.-> MAN
    REC["run record\n(Snakemake output)"] --> |"only declared output"| CP["checkpoint\nre-evaluates DAG"]

    style VALID fill:#e0f5f0,stroke:#2a9d8f
    style TFR fill:#dbeafe,stroke:#3b82f6
    style MAP fill:#dbeafe,stroke:#3b82f6
    style Q1 fill:#e0f5f0,stroke:#2a9d8f
    style Q2 fill:#e0f5f0,stroke:#2a9d8f
    style Q3 fill:#e0f5f0,stroke:#2a9d8f
    style FASTA fill:#f3f4f6,stroke:#6b7280
    style MAN fill:#f3f4f6,stroke:#6b7280
    style LOCK fill:#fef3c7,stroke:#d97706
    style REC fill:#f3f4f6,stroke:#6b7280
    style CP fill:#dbeafe,stroke:#3b82f6
```

### 3. Screen archive

The molecular core. For each FASTA archive, every sequence is tested against
every assay's primer pair. The rule aligns forward and reverse primers to the
target, records per-position match/mismatch calls, Tm shifts from mismatches,
and the amplicon boundaries. Results are cached per-archive under
`results/screened/` — once an archive is screened, it's never re-screened
unless the code hash changes (via `triggers.py`). This is what makes cumulative
screening feasible: new runs only screen new archives.

```mermaid
flowchart TD
    FA[("FASTA archive")] --> SA["screen_archive"]
    REG[("registry/*.yaml\nassay definitions")] --> SA
    SA --> |"per sequence × per assay"| ALIGN["align F + R primers"]
    ALIGN --> CALLS["match/mismatch per position\nTm shift\namplicon boundaries"]
    CALLS --> CACHE[("results/screened/\n(cached per-archive)")]

    subgraph invalidation ["Cache invalidation"]
        CODE["assaywatch/*.py"] --> TRIG["triggers.py\n(AST walk)"]
        TRIG --> HASH["_code_hash\n(SHA-1)"]
        CFG2["config.yaml\nscoring settings"] --> HASH
    end

    HASH -. "hash changed →\nrescreen" .-> SA

    style FA fill:#f3f4f6,stroke:#6b7280
    style REG fill:#f3f4f6,stroke:#6b7280
    style SA fill:#ffe4e6,stroke:#e11d48
    style ALIGN fill:#ffe4e6,stroke:#e11d48
    style CALLS fill:#ffe4e6,stroke:#e11d48
    style CACHE fill:#f3f4f6,stroke:#6b7280
    style CODE fill:#f3f4f6,stroke:#6b7280
    style TRIG fill:#fef3c7,stroke:#d97706
    style HASH fill:#fef3c7,stroke:#d97706
    style CFG2 fill:#fef3c7,stroke:#d97706
```

### 4. Collect calls

Straightforward merge: concatenates every cached per-archive TSV from
`results/screened/`, joins deposit dates (mapping accessions to when they were
deposited in NCBI), and compresses the result into `calls.tsv.gz`. This single
file is the input for all downstream analysis — drift, lineage, sitedrift.
Because screening is cumulative, `calls.tsv.gz` contains every screen ever run,
not just the latest.

```mermaid
flowchart LR
    C1[("screened/\narchive_1.tsv")] --> CC["collect_calls\n(concatenate_screens)"]
    C2[("screened/\narchive_2.tsv")] --> CC
    C3[("screened/\n...")] --> CC
    CC --> |"join deposit dates\ncompress"| OUT[("calls.tsv.gz")]

    style C1 fill:#f3f4f6,stroke:#6b7280
    style C2 fill:#f3f4f6,stroke:#6b7280
    style C3 fill:#f3f4f6,stroke:#6b7280
    style CC fill:#e0f5f0,stroke:#2a9d8f
    style OUT fill:#f3f4f6,stroke:#6b7280
```

### 5. Drift assessment (inside `report`)

The statistical engine. Deposits in `calls.tsv.gz` are split into baseline
(older) and recent (newer) time windows. For each assay, the mismatch fraction
is computed for each window, and a Wilson score interval gives the uncertainty
around each proportion. The Newcombe interval then quantifies the *difference*
between the two fractions — if the lower bound of the difference CI exceeds the
configured threshold, the assay is **declining**. If the CI spans the
threshold, it's **watch**. If the upper bound stays below, **stable**.
Minimum-evidence guards catch assays with too few deposits to assess.

```mermaid
flowchart TD
    CALLS[("calls.tsv.gz")] --> SPLIT["split by deposit date"]
    SPLIT --> BAS["baseline window\n(older deposits)"]
    SPLIT --> REC["recent window\n(newer deposits)"]
    BAS --> WB["Wilson CI\nbaseline mismatch fraction"]
    REC --> WR["Wilson CI\nrecent mismatch fraction"]
    WB & WR --> NC["Newcombe difference CI\nΔ = recent − baseline"]
    NC --> VL{"verdict logic"}
    VL --> |"CI lower > threshold"| DEC["declining ⚠️"]
    VL --> |"CI spans threshold"| WAT["watch 👀"]
    VL --> |"CI upper < threshold"| STA["stable ✓"]
    VL --> |"too few deposits"| INS["insufficient data"]
    TAX[("scope_taxonomy")] --> |"which records\ncount"| SPLIT

    style CALLS fill:#f3f4f6,stroke:#6b7280
    style SPLIT fill:#dbeafe,stroke:#3b82f6
    style BAS fill:#dbeafe,stroke:#3b82f6
    style REC fill:#dbeafe,stroke:#3b82f6
    style WB fill:#dbeafe,stroke:#3b82f6
    style WR fill:#dbeafe,stroke:#3b82f6
    style NC fill:#dbeafe,stroke:#3b82f6
    style VL fill:#dbeafe,stroke:#3b82f6
    style DEC fill:#fee2e2,stroke:#dc2626
    style WAT fill:#fef3c7,stroke:#d97706
    style STA fill:#d1fae5,stroke:#059669
    style INS fill:#f3f4f6,stroke:#6b7280
    style TAX fill:#f3f4f6,stroke:#6b7280
```

### 6. Lineage analysis

Calls are split by NCBI taxonomy lineage. Each lineage with enough records gets
its own drift assessment. Benjamini-Hochberg correction across all lineage
tests for a given assay controls the false discovery rate — without it, testing
dozens of lineages would produce spurious "declining" calls. The worst
*assessable* lineage (after BH filtering) drives the final verdict through a
one-direction override: it can downgrade a verdict to `declining`, but never
upgrade one. The rationale: a pathogen lineage expanding where primers have
mismatches is a real clinical risk even if global numbers look fine.

The override is not unconditional. From a pooled `stable` or `watch` it fires
on the failing lineage alone. From any other pooled verdict — in practice `low
coverage`, which says the assay was never shown to work on this denominator at
all — it fires only if that lineage itself cleared the threshold in an earlier
measured year. `declining` claims a fall, and an assay that never cleared the
threshold has no fall to claim; without the gate the override was flipping
verdicts on lineages that detected at or above the pooled share. The gate is
`require_working_baseline`, the rule the project already settled at the pooled
level, applied to the denominator the override actually claims.

```mermaid
flowchart TD
    CALLS[("calls.tsv.gz")] --> SPLIT["split by\ntaxonomy lineage"]
    SPLIT --> L1["lineage A\ndrift assessment"]
    SPLIT --> L2["lineage B\ndrift assessment"]
    SPLIT --> L3["lineage ...\ndrift assessment"]
    L1 & L2 & L3 --> BH["Benjamini-Hochberg\nFDR correction"]
    BH --> WORST["worst assessable\nlineage verdict"]
    WORST --> POOL{"pooled verdict?"}
    POOL --> |"stable / watch"| DOWN["declining\n(downgraded)"]
    POOL --> |"anything else\ne.g. low coverage"| GATE{"did this lineage\never clear the threshold?"}
    GATE --> |"yes"| DOWN
    GATE --> |"no - no fall to claim"| KEEP["pooled verdict\n(kept)"]

    style CALLS fill:#f3f4f6,stroke:#6b7280
    style SPLIT fill:#dbeafe,stroke:#3b82f6
    style L1 fill:#dbeafe,stroke:#3b82f6
    style L2 fill:#dbeafe,stroke:#3b82f6
    style L3 fill:#dbeafe,stroke:#3b82f6
    style BH fill:#ede9fe,stroke:#7c3aed
    style WORST fill:#ede9fe,stroke:#7c3aed
    style POOL fill:#ede9fe,stroke:#7c3aed
    style GATE fill:#ede9fe,stroke:#7c3aed
    style DOWN fill:#fee2e2,stroke:#dc2626
    style KEEP fill:#d1fae5,stroke:#059669
```

### 7. Figures

Two plots that the four documents otherwise leave to the reader's arithmetic.
`forest.svg` puts every assay with an evaluable recent window on one axis: the
left panel is where its recent detected share sits against the threshold, the
right panel how far it has moved from baseline, so a verdict is something you
read off the page rather than reconstruct from three table columns. Where
footprint clustering widens the change interval, the clustered interval is drawn
behind the unclustered one, which makes pseudoreplication visible instead of
leaving it in a footnote. `site-positions.svg` plots, for each flagged assay,
how much detection falls when a record mismatches at each oligo position, with
the base letters as the x-axis, the 3'-terminal zone shaded, and already-degenerate
bases in amber — the figure a redesign decision actually comes from.

The rule runs the drift and site assessments itself rather than parsing the
rendered markdown, so a figure cannot disagree with the document beside it. It
is separate from `report` so that adjusting a plot re-renders the figures and
the page and screens nothing; the expensive work is upstream of both. Threshold
lines are read off the assessment, never written in the plotting code, for the
same reason scoring numbers live in `config.yaml`: a hardcoded line can silently
disagree with the verdict logic it claims to draw.

```mermaid
flowchart TD
    CALLS[("calls.tsv.gz")] --> FB["figures.build()"]
    FB --> RB["report.build()\ndrift verdicts"]
    FB --> SB["sitedrift.build()\nposition stats"]
    RB --> F1["forest.svg\nWilson + Newcombe CIs\nvs threshold"]
    SB --> F2["site-positions.svg\npenalty per position\n3' zone, degenerate bases"]
    F1 & F2 --> PAGE["figures.html\n(standalone)"]
    F1 & F2 --> |"inlined as input"| RPT["report.html"]

    style CALLS fill:#f3f4f6,stroke:#6b7280
    style FB fill:#ede9fe,stroke:#7c3aed
    style RB fill:#dbeafe,stroke:#3b82f6
    style SB fill:#dbeafe,stroke:#3b82f6
    style F1 fill:#ede9fe,stroke:#7c3aed
    style F2 fill:#ede9fe,stroke:#7c3aed
    style PAGE fill:#d1fae5,stroke:#059669
    style RPT fill:#d1fae5,stroke:#059669
```

### 8. Reporting

Four documents, each serving a different audience question:

- **report** (`report.md` + `report.html`) — the main deliverable. Per-assay
  drift verdicts with confidence intervals, pooled and lineage-conditional.
  The HTML version is self-contained with inline SVGs, no CDN dependencies.
- **site_drift** (`site-drift.md` + `site-drift.tsv`) — per-position mismatch
  rates across primer/probe binding sites.
- **lineage_analysis** (`lineage.md`) — per-lineage statistics, coverage
  fractions, and individual verdicts with override flags.
- **degeneracy_table** (`degeneracy.tsv`) — pool dilution from degenerate IUPAC
  bases in primer sequences. Reported alongside drift but never scored — it's a
  property of the assay design, not of sequence evolution.

```mermaid
flowchart LR
    CALLS[("calls.tsv.gz")] --> FIG["figures"]
    FIG --> RPT["report"]
    CALLS --> RPT
    CALLS --> SD["site_drift"]
    CALLS --> LIN["lineage_analysis"]
    REG[(".registry-valid")] --> DG["degeneracy_table"]

    RPT --> O1["report.md\nreport.html"]
    SD --> O2["site-drift.md\nsite-drift.tsv"]
    LIN --> O3["lineage.md"]
    DG --> O4["degeneracy.tsv"]

    style CALLS fill:#f3f4f6,stroke:#6b7280
    style REG fill:#f3f4f6,stroke:#6b7280
    style FIG fill:#ede9fe,stroke:#7c3aed
    style RPT fill:#dbeafe,stroke:#3b82f6
    style SD fill:#d1fae5,stroke:#059669
    style LIN fill:#dbeafe,stroke:#3b82f6
    style DG fill:#d1fae5,stroke:#059669
    style O1 fill:#d1fae5,stroke:#059669
    style O2 fill:#d1fae5,stroke:#059669
    style O3 fill:#d1fae5,stroke:#059669
    style O4 fill:#d1fae5,stroke:#059669
```

---

## Design decisions

These are the non-obvious ones; the Snakefile comments cover the rest.

| Decision | Why |
|---|---|
| Archives and manifest are never Snakemake outputs | Snakemake deletes outputs before re-running. Deleting fetched archives means re-downloading everything. |
| `retrieve` is a checkpoint | Which archives exist isn't known until the fetch finishes. Downstream rules re-evaluate after. |
| Screening is cached per-archive | A group with 200 archives and 3 new ones this week screens only the 3. |
| Code-hash tracking via AST (`triggers.py`) | Editing screening code or scoring thresholds invalidates exactly the affected caches — no manual `-R` flag to remember. |
| Wilson score CIs, not Wald | Wilson is accurate at small sample sizes where Wald CIs can go negative. |
| Newcombe interval for the difference | Proper CI for the difference of two proportions; doesn't assume normality. |
| One-direction override for lineage verdicts | A lineage-specific decline is a real clinical risk even when global numbers look fine. Upgrading a global decline because one lineage looks okay would hide problems. |
| The override is gated below `stable`/`watch` on the lineage's own working baseline | `declining` claims a fall. An assay that never cleared the threshold has none to claim, and ungated the override was flipping `low coverage` verdicts on lineages detecting at or above the pooled share. |
| BH correction per assay | Without FDR control, testing many lineages produces spurious "declining" calls. |
| Degeneracy reported but never scored | Pool dilution is an assay design property, not drift. Scoring it would penalize assays for being deliberately broad. |
| Run date pinned once | Avoids the midnight-crossing bug where a run that starts before midnight and finishes after it creates mismatched date references. |
| Figures are their own rule, consumed by `report` | Adjusting a plot re-renders the figures and the page and screens nothing. As a hard input, the page can never be published with a figure from an earlier run beside this run's tables. |
| Figures recompute rather than parse the reports | Reading numbers back out of rendered markdown would be a second implementation of the same arithmetic, free to drift from the first. |
| Threshold lines read from the assessment, never written in plotting code | Same reason scoring numbers live in `config.yaml`: a hardcoded line can silently disagree with the verdict logic it claims to draw. |
