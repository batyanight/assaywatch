# Pipeline review, 2026-10-04

A review of the whole pipeline from two directions — software engineering, and
a methods reviewer's — plus the findings from a day of audit and validation
work. Every number below was recomputed here; claims I only read in the code
rather than ran are marked *(read, not run)*.

State at review: 145 assays (135 conventional, 10 MGB probe; no
hydrolysis_probe, LNA or SYBR entries), 736 tests passing, last full run
2026-10-04 producing 2,255,525 calls.

---

## 1. The stages, and what each assumes of its neighbours

| stage | in → out | the contract it assumes | enforced? |
|---|---|---|---|
| `validate` | `registry/` → `.registry-valid` | every YAML parses, `id == filename stem` | yes, `validate.py` |
| `retrieve` | `.registry-valid` → `runs/<date>.json` (+ archives, manifest as *state*) | `<stem>.fasta.gz` and `<stem>.meta.tsv.gz` co-exist with aligned rows | **no** |
| `screen_archive` | archive + `--only` → one TSV | columns fixed by `Call.as_row`; assay id resolves to `registry/<id>.yaml` | implicitly |
| `collect_calls` | every cached TSV → `calls.tsv.gz` | every TSV has a header; no embedded tabs | partly |
| `report` | `calls.tsv.gz` + metadata + registry → `report.md/html` | `assay_id`, `record_id`, `call` present; `exclusion` optional | yes/yes |

The deliberate design decision worth restating: **archives and the manifest are
never Snakemake outputs**, because Snakemake deletes a rule's outputs before
running it, which is how the first two pipeline runs each erased the fetch
history. `retrieve`'s output is a small per-day run record instead.

### Interactions that work

- **Registry changes between runs** are handled properly. The set of retrieval
  groups is hashed into `retrieve`'s params, so a re-scoped group is fetched the
  same day; dropped groups disappear from `archives()`; and `screen_archive`
  carries a signature over its group's assay files, the scoring config and the
  screening code, so exactly the affected archives are rescreened.
- **The new `exclusion` and position columns** degrade safely: every consumer
  tolerates their absence (`report.read_calls`, `drift.assess`).

### Interactions that are fragile

- **`validate` and `degeneracy_table` are keyed on the registry *directory***,
  whose mtime does not change when a file's contents are edited. So on a
  same-day rerun after editing an assay, the "fail early" gate does not re-fire.
  *(read, not run)*
- **Assembly recut reuses an archive path.** On a primer-pair change
  `assemblies.py` renames the old archive to `.superseded` and then recomputes
  the stem — so today's path is reused for different content. The screen cache
  is keyed on that path, and only mtime plus the signature rescue it.
- **Archive ordering is implemented three times** and only one handles `_10`
  before `_2` (`Snakefile.stem_order`); `rebuild_manifest.py` and
  `report.read_dates` sort lexicographically.
- **`last_run_date`'s filter `r["n_fetched"] >= 0` is always true**, so its
  docstring's "most recent *successful* run" is not what it computes.

---

## 2. Defects found and fixed today

All verified by running, then fixed, with regression tests:

1. **Amplicons were only searched on the plus strand**, so every minus-strand
   gene in a genome record was invisible. 79 of 84 fixtures changed call when
   reverse-complemented.
2. **Any non-IUPAC character in a record crashed the run** (`-`, `*`, `X`,
   digits, spaces) via `reverse_complement`. One odd deposit killed a whole
   archive.
3. **A 50-sites-per-oligo cap applied before pairing**, so on a genome the true
   site could lose to 50 chance sites.
4. **Primer pools were in the registry and ignored by scoring** — the filovirus
   assay was judged on one of four forward primers. Fixing it moved 229
   `fail`→`detect` and nothing the other way; filovirus L alone accounted for
   226, a drift signal that was an artefact.
5. **`screen --thermo` crashed** on any mixed-length primer pool, killing the
   whole job (ten assays affected).
6. **Probe pools were not searched** — only the first member, while the comment
   claimed otherwise.
7. **The screen cache could not see `schema.py`**, which owns
   `Oligo.matching_seq`, `tail_5prime` and `seq_as_written`: editing any of them
   changed every call and rescreened nothing.
8. **PDB chain records never joined to their deposit dates** (476 calls).
9. **The recent window was whole calendar years**, so 24 months meant ~33.
10. **Three wrong taxids** — Bsal pointed at a genus of moths; both lyssavirus
    assays were screened against all of Rhabdoviridae.

---

## 3. Open problems, ranked

### 3.1 The estimand is wrong (scientific, and the most serious)

Against 46 literature-derived validation cases the tool flags **1 of 12
documented failures**, while contradicting only 4 of 21 `works` cases. It is
conservative to the point of near-blindness.

This is not a threshold being a few points out. Every failure in the case set is
**lineage- or group-conditional**: ferlavirus genogroups B and C,
insect-specific flaviviruses, swine H1N1 against avian influenza,
beta-papillomaviruses, fusiform-gametocyte *Leucocytozoon*, divergent
serpentoviruses, Asian Bd haplotypes. A minority clade cannot move a population
proportion past a 90% bar, so **no setting of the existing thresholds recovers
those cases**. `count_diverged_as_fail` over all 46 cases moves failures caught
1 → 2 and works-not-contradicted 17 → 16; it is not the fix.

**What to build:** per-footprint haplotype coverage — collapse identical
footprint genotypes, report the fraction of *distinct* footprints detected with
their frequencies, and make the headline verdict **the worst-covered subgroup
above a frequency floor**, naming the variant. Validation then asks "did the
tool name the lineage the paper named?", which the 12 failures can actually
answer.

### 3.2 The denominator conditions on the outcome

Evaluable records are **695,707 of 2,255,525 (31%)**. A call needs both primer
sites present and findable, which is correlated with the thing being measured:
partial deposits — where submitters park divergent haplotypes — are dropped, so
the statistic is computed on records the assay already matches. Informative
censoring, biasing every proportion upward.

Proved on Bd: of 464 unusable ITS deposits, **357 are truncated** before the
probe footprint and only 1 has that footprint present and matching, so the
probe cannot be assessed from GenBank at all. The tool nonetheless says
`stable`.

The exclusion labels added today (`truncated` / `diverged` / `no_site` /
`chance_only` / `no_pair`) make this visible for the first time. Across the run:
1,208,057 `no_site`, 229,254 `truncated`, 81,297 `chance_only`, 39,293
`diverged`, 660 `no_pair`.

**What to build:** homology-anchored footprint scoring — align each record to
the assay's reference amplicon and read the footprints at their homologous
coordinates, scoring what is there however diverged. That retires the
6-mismatch search ceiling, the chance-pair problem and the truncation bias at
once. Plus an explicit assessability statement per oligo, and no `stable`
verdict below an assessability floor.

### 3.3 Records are not independent

Wilson and Newcombe assume independent Bernoulli records. GenBank is
phylogenetically and epidemiologically clustered: one outbreak, one lab, 500
near-identical submissions. The effective sample size is the number of distinct
lineages, not records — so the intervals are **too narrow**, the flags too
confident, and a `declining` call can be driven entirely by which clade was
deposited. This cuts against the tool's main defence, that it is conservative.

Compounding it: deposition is not sampling. The *E. coli* malB case moved 25% →
43% purely on lineage mix; the calicivirus case fell 14% → 0% on composition
and was still called `declining`.

**What to build:** collapse identical footprints, weight by distinct haplotypes,
and cluster-bootstrap the intervals.

**Partly built, 2026-10-05 and corrected twice on 2026-10-06, and one part deliberately not.**
`drift.py` counts the distinct (call, footprint) classes behind each window, where a
footprint is the six mismatch columns the screen already writes, and for a flagged
assay says whether the flag survives two ways of discounting duplicated records
(`AssayDrift.flag_survives_clustering`, the "Duplication check" line in the report).
Never scored, and a test pins that statuses and intervals are identical with and without
it. It is the widest defensible reading, not the right one: it treats every group of
identical footprints as one clone, and it cannot see clade structure among records that
differ at non-primer positions, so it is not a lower bound on the effective sample size.
A flag survives only if it passes every test it faces:

- *a floor*: at least `min_records_for_drift` distinct footprints, the same minimum the
  record-level rule needs, applied to independent observations;
- *the sample-size reduction*: the detected share as measured, but with only as many
  observations as there are footprints (`recent_ci_clustered`; for a declining flag, the
  fall from baseline as well). It shows whether a flag survives losing the sample size
  duplication costs. It keeps the record-weighted share, so it CANNOT see a share
  dominated by one clone;
- *the footprint reduction*: count each distinct footprint once and ask whether the share
  amplifying stays below the threshold (`recent_ci_by_footprint`). This is the one that
  sees the dominant clone, and it can only withhold "survives" from a flag the
  record-level evidence already raised, never raise or clear one: alone it would read a
  healthy assay with fifty one-off sequencing errors as mostly failing.

What the first version got wrong, found by adversarial review on 2026-10-06 (twice):

- *It reassured below the floor.* Wilson at small n is anti-conservative (0 of 1 gives an
  upper bound of 79%), so the malB shape below, 92 failures sharing one footprint, came out
  as "the flag does not depend on duplicated records". It did so at EVERY footprint count
  from two up to nineteen, not just one to three.
- *It invented footprints.* A footprint is known only where the screen wrote the columns.
  A cached screen from before they existed, and a record scored as a failure for being
  diverged, carry none, and used to be counted as one real all-exact footprint. They now
  make the assay's footprint count unknown, and the report says the check was not run.
- *The first fix was only patched for its own fixture.* The sample-size reduction alone
  passed 92 failures at one footprint beside 70 detections spread over 19 others (a 43%
  share, 20 footprints) and said "counting each footprint once ... does not depend on
  duplicated records", when counted once 19 of the 20 footprints amplify. The footprint
  reduction above is the repair, and the note now says which reduction is which and
  only blames duplication where a test that implies it failed.

**Not built: weighting each distinct haplotype equally.** A sequencing error in a
primer site is a footprint of its own, so on a healthy assay with one exact-match
class and fifty one-off errors it would call the assay 2% detected. The
record-weighted proportion with a duplication-aware interval does not have that
failure. A cluster bootstrap over a real phylogeny would; that needs the
alignment this pipeline does not build.

**What it says about malB.** 92 failures, all one A->G at the reverse 3'
base, are ONE footprint, and 70 detections sharing another make two footprints in all, far
below the floor. The check reports that flag as resting on two footprints, not as surviving. Read that correctly: the lineage's failure is real
and its weight in the proportion is what is in doubt, which is exactly the
25% -> 43% lineage-mix movement described above.

### 3.4 Amplicon size is not constrained to the declared product

Scoring uses the global 50–3000 bp window and **never uses the assay's declared
`amplicon_bp`**. Result: **727 `detect`/`reduced` calls on products more than
twice the declared size**, worst a **1931 bp product credited to a 194 bp
assay** (SIV pol), plus 708 more 20–100% over. 22 of 145 assays declare no size
at all.

`amplicon.declared_tolerance` now exists, default **null (off)**: enabling it at
30% rejects 4,204 of 440,582 calls and requires `tests/fixtures` regenerating,
because the synthetic fixtures were built at fixed spacings that ignore declared
sizes. **A decision, not a preference** — crediting a 10× product is not
defensible.

*Fixed 2026-10-14:* on at **0.25**, chosen from the distribution rather than by
eye — over the 610,420 calls of the 2026-10-07 run whose assay declares a size,
|observed/declared − 1| has a knee near 0.2 and flattens past it (±15% keeps
98.92%, ±25% keeps 99.32%, ±50% keeps 99.57%). `tests/make_fixtures.py` now
sizes its spacers from each assay's `amplicon_bp` instead of a fixed 20 nt,
which is what blocked it; three hand-built test records were sized the same way.
Applied to the 2026-10-07 calls it moves 59,141 rows to `no_amplicon`, **54,966
of them `fail`** — the oversized products were mostly being counted against the
assay, so the correction raises detected shares (estimated: 37 declining → 22,
63 stable → 73). Two consequences to watch. First, what the filter mostly catches is **two
products in one entry**, not a wrong number: the three assays whose measured
product sat furthest from their declared size each hold a second amplicon in
`oligos.alternates`, which `oligo_pools` treats as an interchangeable pool
member — right for a consensus cocktail, wrong for a nested round. Their
declared pairs measure 1320, 161 and 1695 bp against a declared 1319, 163 and
1694, so the stored sizes are correct and it was the alternate's product being
credited; with the filter on the screener falls back to the declared pair. 20 of
214 entries can form a second product this way, 9 with a declared size, and two
of them (`ADENOVIRUS_dsDNA_Tracies_unpublished_nest_Tracies`,
`ASTROVIRUS_ssRNA_RNA_dependent_RNA_polyme_round2`) were among the worst
oversized-product offenders. The fix is the curation this registry already
names elsewhere: one entry per round. Second, `chance.pair_evalue` had to be told
the narrowed window — left on the global range it overstated E by the ratio of
the two (2951/98 for a 194 bp assay at ±25%), and the pairs that overstatement
pushed past `max_pair_evalue` were the worst-matching, i.e. the drifted, ones.

### 3.5 The scoring model is additive where biology is serial

Penalties from forward, reverse and probe are summed into one budget and
thresholded. But amplification needs forward AND reverse; detection needs that
AND the probe. Three innocuous mismatches (1.0 + 1.0 + 1.0 = 3.0) land in the
same bin as one near-lethal 3'-proximal mismatch, and a probe defect — which
costs signal, not product — trades against a primer defect, which costs the
exponential.

The 3'-terminal automatic fail is also identity-blind, which the primary
literature contradicts: only A:G, G:A, C:C and A:A terminal mismatches strongly
suppress yield, while T:G, T:C and T:T are near-neutral
([Kwok 1990](https://doi.org/10.1093/nar/18.4.999),
[Stadhouders 2010](https://doi.org/10.2353/jmoldx.2010.090035)). And one
penalty table serves 135 conventional PCRs and 10 MGB probe assays, where a
3'-terminal mismatch costing 100-fold yield is often still a visible band after
40 cycles.

**What to build:** per-oligo verdicts combined logically
(`amplifies = fwd AND rev`, `detects = amplifies AND probe`), reporting the
limiting oligo; a mismatch-identity-aware 3' term; chemistry-specific
thresholds.

### 3.6 Thermodynamics are computed and ignored

`thermo.py` runs primer3's nearest-neighbour model and its own data separate the
classes cleanly (median worst ΔTm −5 / −12 / −17 °C for detect / reduced /
fail), yet it changes no call. A reviewer will ask why a validated biophysical
model is a spectator to a hand-tuned integer table. The honest counter is that
`resolve()` models undetermined record bases as matches and inosine as a perfect
pair, both optimistic.

### 3.7 Degeneracy is reported but not gated

The worst entries are **2,579,890,176-fold** (pan-parvovirus VP1) and
**1,811,939,328-fold** (adenovirus Pan-Pol round 1). A `detect` on a
2.6-billion-fold pool is not a weak result — each member is ~4×10⁻¹⁰ of the
reaction — yet it appears in the same status table as Boyle 2004 with the fold
as a trailing column. The `severe` tier also spans 4,096 to 2.6×10⁹, six orders
of magnitude in one bin.

**What to build:** refuse an in-silico verdict above ~10⁴–10⁵-fold, extend the
tiers, and score pools per member.

### 3.8 Smaller, concrete

- **Nested rounds are scored as independent assays** (13 `round1`, 21
  `round2`). Nothing checks that round-2 sites lie inside the round-1 amplicon,
  and nothing joins them: phlebovirus is reported as 94.4% (n=54) and 96.5%
  (n=142), two numbers for one assay on different denominators.
- **RT is unmodelled** for 73 of 145 RNA targets, where the reverse primer
  primes cDNA synthesis at a different temperature with different mismatch
  tolerance.
- **MGB chemistry is ignored**: the conjugate raises Tm 15–20 °C, so an MGB
  probe's mismatch sensitivity is not that of an unmodified oligo of the same
  length, which is what `thermo.py` models. The `Probe.lna` flag is unused.
- **Indels in a footprint cannot be scored.** `gapped.py` exists and only
  `scripts/indel_check.py` uses it — and the documented Bd probe failure
  includes a 2 bp insertion.
- **Exclusion labels are biased for the 22 assays with no `amplicon_bp`**: the
  fallback span is `max_bp` = 3000, pushing their records to `truncated` rather
  than `diverged`.
- **`drift.py`'s `status="no data"` is unreachable and absent from
  `report.STATUS_ORDER`**, so it would be silently dropped from both reports.
  *Fixed 2026-10-05:* `report.status_order` appends any status the report was not
  told about, so a new one appears as an unstyled section instead of vanishing
  (the HTML colour lookup no longer raises on it either).
- **No test touches the Snakefile**, including `collect_calls`' column
  reconciliation — written precisely for the case of a pre-`exclusion` TSV
  meeting a post-`exclusion` one.
  *Fixed 2026-10-05:* the logic moved to `assaywatch/collect.py` (`concatenate_screens`,
  `stem_order`) and the rule calls it, so it can be imported and tested. Fifteen
  tests, including the shape that actually corrupts - a column inserted in the
  MIDDLE of the row, which shifts every later value sideways - with a test that
  runs the naive version to show the test can fail. The new function matches the
  old inline block byte for byte on 60 randomised mixed-schema inputs; one
  deliberate change, the header now ends in CRLF like every row (it was a bare LF).
  A screen whose last row has no line break is now refused by name instead of
  having the next file's header glued onto it. *Run under Snakemake 9.27.0 on
  2026-10-06* (it installs in a fresh virtual environment, though not into the
  cloud container's system Python): old and new produce byte-identical screens and
  calls table (the calls table's gzip header used to carry a timestamp, so compare the
  decompressed content or, since 2026-10-06, the bytes). This note first said to check
  with `snakemake -n` and expect the same jobs as before, which is wrong: the first run
  after a code change reruns every screen, and a dry run lists the screening jobs only once
  the day's retrieval record exists. See `docs/RESUME-HERE.md` for what to do instead.
- **`retrospective.py --cases` re-parses `calls.tsv.gz` and re-globs every
  metadata file once per case.**
  *Fixed 2026-10-05:* `load_evidence` reads and deduplicates both once, grouped by
  assay, and each case touches only its own assay's rows. A test counts the two
  expensive reads over five cases (1 and 1, not 5 and 5) and was run against the
  old script to confirm it fails there. Verdicts are pinned identical to the old
  implementation over 25 (date, assay-filter) combinations on data where the
  answers genuinely differ. `status_as_of` keeps its signature.
- **The pre-commit hook pins ruff 0.6.9 while the environment has 0.16.10**, so
  the two reformat one test file differently and ping-pong. Align them.
  *Already done:* `.pre-commit-config.yaml` pins v0.16.10, matching `pyproject.toml`
  and `environment.yml`.

---

## 4. Defensibility of the choices made

Choices I would defend as they stand:

- **Inosine as one molecule**, pairing with C/A/T and `unknown` against G, read
  from `seq_as_written`. The pairing order I:C > I:A > I:T > I:G is from
  [Martin 1985](https://doi.org/10.1093/nar/13.24.8927) and the
  nearest-neighbour measurements in
  [Watkins & SantaLucia 2005](https://doi.org/10.1093/nar/gki918), which put
  dI:dC near a normal A:T pair and dI:dG about 3 kcal/mol worse — hence the
  demotion of I:G to a weak pair rather than a mismatch. Reading the PREDICT
  filovirus primer from `seq` would call it 8192-fold degenerate when it is
  8-fold.
- **Ambiguous record bases cost nothing when scoring but consume the search
  budget.** Charging them would make a submitter's sequencing quality
  indistinguishable from drift, and would be flatly wrong at the 3' base.
- **Degeneracy reported, never scored** — though §3.7 shows the consequence was
  not carried through.
- **Archives and manifest as state, not outputs** (§1).
- **`declining` versus `low coverage`.** Separating a measurable fall from an
  assay used beyond its design is what stops a scope mismatch reading as drift.
- **Scoping an assay only where the published claim is lineage-specific**, with
  the wide number kept on the record — and *not* scoping where no honest scope
  exists, as with Takehisa SIV.
- **The validation set's `as_of` discipline**: each case dated to the latest
  sequence the cited work could have seen, never its publication date.

Choices that need revisiting, in order: the estimand (§3.1), the denominator
(§3.2), independence (§3.3), declared amplicon size (§3.4), additive scoring
(§3.5), unused thermodynamics (§3.6), ungated degeneracy (§3.7).

### Where this reasoning now lives

A review doc nobody opens is not a safeguard, so the arguments above were moved
to where a reader meets the number:

- **`config.yaml`** — every threshold carries its biological justification or an
  explicit admission that it is an eyeballed placeholder, with the Kwok and
  Stadhouders citations at `terminal_mismatch_fails` and the three
  GenBank-sampling caveats at the head of the `drift:` block.
- **`score.py`** — `score_primer`, `score_probe` and `classify` each state what
  the rule assumes about polymerase extension, probe cleavage and the
  serial-gate problem, and what they are blind to.
- **`drift.py`** — the module docstring now says what the fraction estimates and
  why `stable` is weaker evidence than `declining`.
- **`iupac.py`** — the inosine pairing order carries its two citations.
- **`README.md`** — "What the scoring rule assumes about PCR, and where it is
  wrong" under Screening, and "What the fraction estimates, and what it does
  not" under the drift call.

---

## 5. What the paper must say

The investigations doc is unusually candid and the paper should inherit that
tone rather than lead with "145 assays screened":

1. The validation outcome as a disconfirmation of the scalar statistic:
   **sensitivity 1 of 12**, with the case list.
2. The truncation result — for assays whose target is deposited as short
   fragments, in-silico surveillance can confirm the primer footprints and say
   nothing about the probe.
3. The deposition-bias confound, and that GenBank composition is not sampling.
4. That every threshold in `config.yaml` was set by eye, and
   `docs/validation-cases.tsv` is the only thing calibrating them.
5. The unmodelled parts: RT, probe chemistry, secondary structure, indels.
