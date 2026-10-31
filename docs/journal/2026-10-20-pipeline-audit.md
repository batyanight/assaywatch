# Pipeline audit: findings, proposed changes, and what has to come from a human (2026-10-20)

Baseline: `9b40949`, 209 registry entries, 23,395 lines of Python over 101 files.
Companion file: `docs/materials-needed.tsv`, 95 gaps across 85 entries, regenerated
by `scripts/materials_needed.py`.

## 1. Why this audit, and what it is not

A day of bug-hunting found six defects that all had the same shape: **a silent
fallback reporting "no match" as "no data."** None of them crashed. Each degraded a
measurement while leaving output that still looked like data. One of them —
`retrospective.py` scoring a renamed assay as `no data` — had quietly removed the
single validation case the shipped lineage-override rule depends on, so three
candidates the override doc rejected *for dropping that catch* would have looked free.
The rule survives. That is luck, not process.

The lesson is structural, not about those six: **this project holds its scientific
claims to a far higher standard than the plumbing between its files.** "Measure, never
quote", thresholds carrying their own justification in comments, `--fail-on-loss` on
the oligo reader, reverting the conventional-PCR override when tier-2 contradicted the
headline — that culture is why any of this was reconstructible. It stops at the file
boundaries. Nobody had asked "what would make this wrong?" of a filename convention or
an id lookup.

**Not audited line by line:** `drift.py` (1,121 loc) and `report.py` (985 loc) were
read structurally, for shape and duplication, not statement by statement. `sitedrift.py`,
`timing.py`, `nested.py` and `subcluster.py` were read only where today's work touched
them. Everything asserted about another tool carries a source link; everything asserted
about this repo names the file or the measurement behind it.

**Worth stating up front, because the rest of this document is critical:** there are
**zero** `TODO`, `FIXME`, `XXX` or `HACK` markers in 23k lines. Of 72 config keys,
exactly one is dead. CI runs two jobs, pins Snakemake deliberately with the reason
written down, and checks citations offline against a committed Crossref cache. That is
better hygiene than most published bioinformatics pipelines.

## 2. The pipeline, stage by stage

| stage | module | solid | thin |
|---|---|---|---|
| retrieve | `retrieve.py` 782 loc | incremental manifests, atomic writes, archives never overwritten, rate limits tied to one shared constant, key scrubbing in every error path | `retrieve_taxon` is 146 loc and `main` 107; one failed group fails the whole run (correct, but see S1) |
| assemblies | `assemblies.py` 523 loc | now paged by `next_page_token` rather than bisecting dates | `per_year: 20` sampling is uncalibrated; `sample_per_year`'s hash order is arbitrary by design but never validated against a biased deposit pattern |
| screen | `screen.py` 276, `score.py` 787, `match.py` 280 | exhaustive vectorised search held to brute force in tests; three-state base comparison; inosine as a distinct molecule; degeneracy reported, never scored | `screen_one` is 195 loc; **the penalty table is the project's weakest link** (§3) |
| windows | `windows.py` 389, `loci.py` 67 | archives cut to credible pair windows, 6.6 GB → ~160 MB, with a sidecar so length-scaled E-values stay honest | `loci.py` has **no direct test reference at all** despite computing the spans the cutting depends on |
| collect | `collect.py` 119 | concatenates cached per-archive screens, unifies columns, detects truncation | **never sees the registry**, so it will merge rows for assays that no longer exist (§4) |
| drift | `drift.py` 1,121 loc | Wilson/Newcombe intervals, minimum-evidence guards, evaluable denominator, working-baseline gates, lineage-conditional estimand, duplication check reported beside a verdict and never into one | `assess` is **300 loc**, the largest function in the package; `AssayDrift` is a 565-loc class that computes *and* writes its own prose |
| report | `report.py` 985 loc | self-contained HTML, per-year tables, coverage gaps, honesty fixes from the 2026-10-14 review | `render_markdown` 165 + `render_html` 187 = **352 loc of parallel layout** |

## 3. Methods: thermodynamics versus the alternatives

This is the centre of the audit.

### Three families, and where this project sits

| approach | used by | captures | blind to |
|---|---|---|---|
| position-weighted mismatch penalty | **AssayWatch**, UGENE in-silico PCR | position along the primer | **which bases mispair** |
| nearest-neighbour ΔG / Tm | LANL [`thermonucleotideBLAST`](https://public.lanl.gov/jgans/tntblast/tntblast_doc.html), [MFEprimer](https://academic.oup.com/nar/article/40/W1/W205/1751577), [openPrimeR](https://bioc.r-universe.dev/openPrimeR/doc/openPrimeR_vignette.html) | identity **and** sequence context, from per-dinucleotide parameters | nothing relevant here |
| coverage / set-cover under constraints | [openPrimeR](https://bioc.r-universe.dev/openPrimeR/doc/openPrimeR_vignette.html) | how many templates a primer set covers | longitudinal change |

### The field's standard engine for this exact task is thermodynamic

The closest published analogue to AssayWatch's screening step is
[**PCR_strainer**](https://pmc.ncbi.nlm.nih.gov/articles/PMC7441044), which assesses
PCR diagnostic assays against circulating strains. It does not implement its own
matcher: it runs **`tntblast`** with a 30 °C minimum annealing temperature and parses
the gaps and mismatches out of the output. `tntblast` (LANL, J. D. Gans, v2.04)
"scores matches by free energy and melting temperature" rather than BLAST heuristics,
accepts primer pairs, primer+TaqMan triplets or single probes, returns predicted
amplicons for a given annealing temperature, reports hairpin and dimer values, is
MPI/OpenMP parallel, reads FASTA and GenBank, and ships as a Docker image.

MFEprimer makes the case against counting plainly: a G–C and an A–T match score
identically in BLAST, and the G–C is more stable. Published in-silico PCR work reports
that **free energy is a more sensitive and specific match criterion than hybridization
temperature**, and that both beat the mismatch-and-gap heuristics most tools rely on.

### The primary literature says identity dominates exactly where this project is blind

[**Kwok et al. 1990**](https://pmc.ncbi.nlm.nih.gov/articles/PMC330356) — already cited
in `scripts/bench_panel.py`'s own docstring — tested primer-template mismatches on an
HIV-1 *gag* amplicon:

- single **internal** mismatches: no significant effect on yield
- **3'-terminal** mismatches: A:G, G:A and C:C cut yield **~100-fold**; A:A ~20-fold
- **"mismatches involving T were minimally disruptive"**
- double mismatches in the last four bases were usually fatal — **except** a 3'-terminal
  mismatched T, which still amplified

Bru et al. 2008 (AEM) qualifies the first line: in real-time PCR a single mismatch in
the primer's second half can underestimate copy number up to 1,000-fold, worsening
toward the 3' end. So AssayWatch's **position weighting is directionally right**, and
its **identity-blindness is precisely the known weak point**.

`config.yaml` currently charges every 3'-window mismatch `primer_3prime_penalty: 3.0`
regardless of which bases are involved, with `terminal_mismatch_fails: true` on top.
Kwok says a terminal T mismatch is among the least disruptive there is.

### Three of this project's own bench panels independently agree

| panel | result | what it points at |
|---|---|---|
| Forslund FAP | 14 false fails of 60 bench-amplified HPV types; **12 rest only on T:G** | 3'-window mispair identity |
| Barrett morbillivirus | 4 of 7 correct; **all 3 false fails carry a G·T wobble in the 3' window**; `rev5 T:G` in 4 of 7 rows including measles, the design reference, at exactly 3.0 | same |
| Rahn invA | 64/64 correct; the 3 chance pairings that reach scoring carry **no G·T at all** | **the specificity cost of discounting G·T is zero across 41 bench negatives** |
| Meyer ATI | 8 of 9; its one false fail has **no 3'-window mismatch** | `reduced_max`, a different knob |
| Rebelo Mycoplasma | 8/8, no 3'-window mismatch anywhere | neither knob disturbed |

Two panels converge on one change, a third prices it at zero, and the primary
literature predicts it. That is a stronger evidential chain than anything tier-2 has
produced.

### What AssayWatch does that none of the comparators do

This matters for the recommendation, because it says what is worth protecting:

- `tntblast` / PCR_strainer emit a **mismatch tally per genome**.
- [NEB's Primer Monitor](https://primer-monitor.neb.com/about) emits **variant
  frequencies with threshold alerts by geographic region**.
- openPrimeR answers **"which primer set covers most templates"**.

**Nobody asks "has this assay's coverage fallen, against a baseline, with a confidence
interval, conditioned on lineage."** The longitudinal framing, the lineage-conditional
estimand and a retrospective validation set scored against published follow-up are this
project's actual contribution — **and all three are independent of the scoring engine.**
That is the strongest argument for replacing the engine rather than defending it: the
novelty does not live there.

### Regulatory precedent, currently uncited

FDA's COVID-era policy for molecular test developers recommends **periodic alignment of
primer and probe sequences against public genome databases**, and assessing whether
performance **drops by 5% or more**
([coverage](https://www.hoganlovells.com/en/publications/fda-issues-new-policy-for-evaluating-impact-of-viral-mutations-on-covid-19-tests),
[RAPS](https://www.raps.org/resource/covid-test-developers-get-variant-related-fda-guid.html)).
NEB built Primer Monitor in response to it.

`drift.min_decline` is **0.05**, and `ROADMAP.md` lists it among the placeholders "set
by eye". It is the same number a regulator reached independently. Cite it — it converts
an eyeballed floor into a defensible one, and it establishes this project's whole
premise as recommended practice rather than a novelty. (Caveat: that policy was issued
for the COVID-19 emergency; confirm current status before citing it as live guidance.)

## 4. Inconsistencies and gaps, measured

1. **A run's calls table can hold assay ids the registry no longer has.**
   `results/2026-10-20/calls.tsv.gz` holds 3 — `CRYPTOSPORIDIA_…_2000`, `…_2000_round2`,
   `Salmonella_invA_gene_unnamed_Rahn_1992` — beside their renamed counterparts, so the
   report's "208 assays screened" double-counts. A cached per-archive screen was reused
   without its `params.only` being re-checked:
   `results/screened/28901/q22fdd7bbec/2026-10-18.tsv` still dates from 2026-10-18 while
   the other two archives in its group were rescreened at 21:50, and
   `.tmp/run-2026-10-17.log` shows those archives were screened by a different snakemake
   install, so the metadata that would invalidate them is absent here. **Open.**
2. **`needs_review` is an uncontrolled vocabulary.** 99 distinct values over 260 uses;
   **69 used exactly once**; **16 contain spaces or exceed 60 characters** — they are
   prose sentences masquerading as machine-readable flags, e.g. *"DOI found 2026-10-06
   by a Crossref title search, not printed in either citing paper; the top hit matches
   title…"*. Typed `list[str] | None` at `schema.py:389`. **FIXED 2026-10-21 (S7):**
   `list[ReviewItem]`, 98 distinct strings down to 30 flags from `assaywatch/review.py`.
   The counts above are off by one against the final measurement (98 strings over 243
   instances on 208 entries, 69 singletons, 5 strings holding spaces) because the audit
   read `needs_review` as flat text; the finding stands either way.
3. **Four schema fields are set in exactly one entry**: `submitted_by`,
   `amplicon_bp_range`, `species_sizes`, `oligos.probe.seq_as_written`. The last three
   are load-bearing for ATI and the Deckers probe and should stay with that noted;
   `submitted_by` is abandoned — 208 of 209 entries leave it null.
4. **`lineage.taxid_backfill`** is declared in `config.yaml` and read nowhere. The only
   dead key of 72.
5. **`loci.py`** (67 loc) has no own test file and **no direct test reference at all**,
   while `windows.py` and `assemblies.py` both depend on it to compute the pair spans
   they cut archives on. `fasta.py`, `screen.py`, `validate.py` and `lineage_report.py`
   also lack own test files, but are exercised transitively.
6. **Oligo provenance**: of 209 entries, **146** have every oligo confirmed against the
   cited paper, **12** partly, **13** have a paper on disk that confirms nothing, and
   **38** have no paper to check against at all.
7. **Only 1 of 209 entries is `active`**, against `ROADMAP.md` Phase 0's five — and that
   one, `CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004`, reads `absent` against an
   image-table paper. The sole promoted assay is the one whose oligos cannot be
   confirmed from its source.
8. **28 of 209 carry `doi_verified: false`.**
10. **Ordering status had leaked into the pipeline.** `NEED_TO_ORDER` was derived by
   the seed-list importer (since removed) from the phrase "need to order" in the 2018 source
   spreadsheet — a stock position on one day, not a property of an assay — and had
   reached 13 entries, two display names, and two assay ids as a truncated `_ne_`.
   Removed 2026-10-20: the flag, the importer's pattern for it, the names, and the
   two ids (renamed to `Pan_reptilian_paramyxovirus_L_Ahne_1999`/`_2` through
   `docs/rename-mapping.tsv`). The registry is not the spreadsheet's inventory.

9. **`docs/papers-index.md` is the provenance of record** for a gitignored `papers/`,
   and until today it listed ten DOIs that no publisher ever issued. Nothing regenerates
   it automatically.

## 5. Proposed changes

Approval wanted **per item**, not as a block.

### Methods

**M1 — make the 3'-window penalty identity-aware.** Add `scoring.mispair_penalty` to
`config.yaml`, keyed by (primer base, template base), read by `score.score_primer`
(`assaywatch/score.py`, 40 loc — the only function that must change). The minimal
version discounts G·T/T·G in the 3' window; Kwok 1990 justifies it, two bench panels
demand it, and Rahn's 41 negatives price its specificity cost at zero. Gate it through
all five panels **and** tier-2 before shipping, one knob at a time, as
`docs/journal/2026-10-19-conventional-override-validation.md` requires. *This is the single
highest-value change in the project.*

**M2 — evaluate nearest-neighbour ΔG as the match criterion. KILLED at Step 0,
2026-10-21** (`docs/journal/2026-10-21-M2-step0-killtest.md`): `calc_heterodimer`'s terminal
ΔΔG/ΔTm does not reproduce Kwok's 3'-mispair severity ordering (A:A/A:G come out
stabilising; severe and neutral classes overlap). NN ΔG is equilibrium melting, not
polymerase-extension competence — the premise below ("what NN parameters give for
free") is false. Scoped closed; M1's empirical table stays the instrument. `thermo.py`
already
wraps `primer3-py` to compute Tm and ΔTm columns that are deliberately never scored;
the proposal is to score them, and to compare against the penalty table on the five
panels as a held-out set. Scope it as its own project. The honest framing: M1 is a
hand-rolled approximation of what NN parameters give for free, and the reason to do M1
first is that it is one function and one config block, not that it is better.

**M3 — cite the FDA policy** beside `drift.min_decline` in `config.yaml` and in
`ROADMAP.md`'s placeholder list, with the emergency-status caveat.

**M4 — note the absent geographic dimension.** GenBank records carry country and
Primer Monitor alerts by region; AssayWatch has no geography at all. For a wildlife
surveillance tool that is a real gap. Future work, not a change.

### Structure and simplification

**S1 — `collect.py` must check assay ids against the registry**, drop the orphans and
say how many. It only concatenates and never sees the registry, which is why finding 1
survives. **Recommend a hard error**, given that today's worst bug was a silent drop.
This is the fix that does not depend on understanding Snakemake's invalidation.

**S2 — export the status vocabulary once** from `assaywatch/drift.py` as a frozenset.
`report.py` and `scripts/report_diff.py` each hardcode it, and that is exactly what let
`report_diff` promote a section heading to a status and swallow 21 assays.

**S3 — collapse `render_markdown` and `render_html`** onto one intermediate report
model plus two thin serialisers. 352 loc of parallel layout means every report change
is made twice, and drift between the two renderers is what `report_diff` was parsing.

**S4 — decompose `drift.assess` (300 loc)** and `AssayDrift._lineage_check` (161 loc)
into named stages. These are the two places where a reader cannot hold the whole
control flow in mind, and both are on the path that produces a verdict.

**S5 — separate computation from prose in `AssayDrift`.** Verdict notes are built
inside `_lineage_check`, which is why `lineage_worst_idx` had to be added today purely
so a script could learn which lineage fired without parsing English.

**S6 — one accession-version helper.** 29 open-coded `split(".")[0]` against
`report.strip_version` / `version_of`; move them to a shared module, because an
accession is not a reporting concern.

**S7 — controlled vocabulary for `needs_review`**: an enum of flags plus a free-text
`notes` field, so the 16 prose entries stop pretending to be flags and the 69
singletons can be consolidated or retired. This is a schema change and a registry-wide
migration; it is listed here because the flag list is now unusable as a filter, which
is the whole point of having one. **DONE 2026-10-21.** Two things this entry did not
anticipate: four of the flags restated fields on the same entry and 6 of their 39
instances already contradicted those fields, so they were dropped rather than renamed;
and the `active` gate's "no review flags" rule had to be split, because it was refusing
settled disclosures and holding 146 of 208 entries at `draft`.

**S8 — delete or implement `lineage.taxid_backfill`.**

**S9 — tests for `loci.py` first**, then `screen.py` and `validate.py` directly.

### Reproducibility

**R1 — no container, no lockfile.** conda `environment.yml` plus a deliberately pinned
Snakemake in CI beats most academic pipelines, but a Dockerfile or `conda-lock` would
meet the project's own "reproducible across machines" goal. nf-core-style conventions
(container per workflow, schema-validated params) are the reference point.

**R2 — stamp the config and code hash into the calls table.** The stale
`results/2026-10-18/calls.tsv.gz` was identifiable only by inferring from a commit
timestamp three minutes after a run finished. A calls file should carry the settings it
was produced under.

**R3 — regenerate `docs/papers-index.md` in CI or pre-commit**, since it is the durable
provenance record for a directory that is deliberately not in git.

## 6. Materials that have to come from a human

Full detail in `docs/materials-needed.tsv` (95 rows, 85 entries, `bucket` sorts it).
Ordered by leverage.

| bucket | rows | what it is |
|---|---:|---|
| `predict-supplement` | **35** | **one CC-BY document closes all of them** |
| `paper-pdf` | 16 | full text of a cited, Crossref-verified DOI |
| `citation` | 8 | a DOI for an assay that names a reference only in prose |
| `provenance` | 8 | no DOI **and** no reference recorded at all |
| `supplement` | 8 | paper on disk yields no sequences |
| `figure` | 6 | sequences were read off an image |
| `lab-record` | 6 | genuinely in-house, needs the original record |
| `oligos-not-in-paper` | 5 | the cited paper prints oligos, but not these |
| `decision` | 3 | flagged `DO_NOT_USE`, awaiting keep-or-delete |

**1. The Anthony et al. 2015 PREDICT supplement** — Nat Commun 6:8147, Supplementary
Methods, **CC-BY**, so it can be stored and redistributed. **35 entries record their
oligos as read from it**, 46 mention PREDICT, and it is **not in `papers/`**. The
provenance of the entire PREDICT panel currently rests on a document the repo cannot
re-check. One PDF is the highest-leverage item in the project.

**2. Sixteen PDFs for cited, verified DOIs** (13 distinct), e.g. Klee 2006
`10.1016/j.jip.2005.10.012`, Martín-Hernández 2007 `10.1128/AEM.00270-07` (2 entries),
Chua 2000 `10.1126/science.288.5470.1432`. **Regenerate `results/nyu-fetch-list.tsv`
before any library trip** — that list was 13 entries too long until today's
`find_open_access` fix.

**3. Eight entries with no provenance whatsoever.** Both
`HANTAVIRUS_ssRNA_S_segment_round2*`, both `ENTEROVIRUS_ssRNA_5_UTR_VP4_VP2` rounds,
`LEPTOSPIROSIS_Flagillar_filiment_Prote`, `Pan_mycoplasma_16S_23S_intergenic_space_2`,
`RETROVIRUS_RNA_polymerase_SIV_3`, `Tortoise_intranuclear_coccidia_18SrDNA`. **Six of
these also fire lineage overrides or sit on the blocked list** — unverifiable *and*
producing verdicts, which is the worst combination in the registry.

**4. Eight supplements**: Mycobacterium ×3 (the PLOS S1 Table, already read once via
the browser), Sigrist ×3, SIV/Nature ×2.

**5. Five provenance questions, not missing files.** `Pan_HERPES_dsDNA_Terminase` ×2
(cited paper yields 14 oligo-like runs, none within the edit cap of either stored
sequence), `FILOVIRUS_ssRNA_L_gene_2`, `PARVOVIRUS_…_dependovirus_2002`, and
`CHYTRID_Bd_…_Boyle_2004` — the one `active` entry.

**6. The Elsevier institutional token** — unchanged, the one external blocker: 12
papers / 42 oligos, from NYU Libraries, into `.secrets/elsevier.insttoken`.

## 7. What I would do, in order

1. **M1**, the identity-aware 3' penalty. Three panels agree, the literature predicts
   it, the specificity cost is measured at zero, and it would move real statuses. It is
   no longer blocked on anything.
2. **S1**, the `collect.py` registry guard. Today proved the calls table can lie about
   which assays exist, and every count downstream inherits that.
3. **The Anthony supplement.** One CC-BY PDF makes 35 entries re-verifiable — a better
   return than any code change on this list.
4. ~~**M2** as its own project, with the five bench panels as its test set.~~
   **KILLED at Step 0, 2026-10-21** — the NN model does not reproduce Kwok's 3'-mispair
   ordering (`docs/journal/2026-10-21-M2-step0-killtest.md`); never reached the bench panels.

Everything else is real but can wait. The one thing I would *not* do is add validation
cases to chase the `< pooled` gate: §3 says the scorer is the weak link, and tier-2
with 12 `fails` cases cannot adjudicate what is already being asked of it.
