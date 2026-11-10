# The coverage map, built and run on the 2026-11-01 calls (2026-11-10)

A record of one session. What is still open from it is in `ROADMAP.md`, "Coverage map".

## What was decided before any code

A design review on 2026-11-10 separated two things the project had been treating as one.
**Drift** is a fall in detected share over deposit years. **Coverage** is which species an
assay is predicted to detect today, including species its paper never claimed. The
maintainer's own use is coverage: "this assay also picks up X", "this assay fails on X",
"for X, use this other assay". Coverage became the primary product and drift a second
summary of the same calls table. The vocabulary is in `GLOSSARY.md`, "Coverage".

Decisions taken, each by the maintainer:

- A row is an NCBI species taxid. Host is a column and never defines a row.
- A cell is `predicted detect`, `partial`, `predicted fail` or `not assessable`, always
  printed with its count, and no minimum record count hides a cell.
- "Fail" is the stronger claim and the wording keeps that asymmetry.
- A locus check, independent of the primers, decides whether a record with no primer site
  is a failure or does not count. Not built yet.
- Degeneracy annotates a row and breaks ties in a recommendation. It never changes a cell.
- A nested protocol gets three rows: together, round 1 alone, round 2 alone, because with
  all the primers in hand round 2 can be run directly when round 1 misses a species.
- Cuts: `predicted detect` at 95% or more, `predicted fail` at 5% or fewer.

## What was built

`assaywatch/coverage.py` and the `assaywatch coverage` stage, tests first
(`tests/test_coverage.py`, in the fast tier). `coverage_map(calls, species_of,
scope_of, rule)` is a pure function: rows in, cells out, no file and no config. It does
not import `drift`. Four things differ from the interface as first proposed, and each is
the maintainer's to accept or reverse:

1. `scope_of` is `(assay id, species taxid) -> bool`, not a set of taxids, so that
   `coverage_map` needs no taxonomy.
2. A fourth argument, `rule` (`CoverageRule`), carries the two cuts from `config.yaml`,
   because no scoring number may live in code.
3. `CoverageCell` gained `reduced`: of the detected records, how many carry an expected
   Ct shift. `predicted detect` is judged on the cleanly detected share, so a species
   whose records are all `reduced` reads `partial` with a full count.
4. `recommend` takes an optional `degeneracy_of`, which it needs to break ties.

The report is its own pair of files (`coverage.tsv`, `coverage.md`), not a section of
`report.md`. The stage is not yet a Snakemake rule.

## What the 2026-11-01 calls say

Run on `results/2026-11-01/calls.tsv.gz` (3,519,074 rows) with the registry at `3381234`.
A price, not a release: the registry is newer than that screen, and four assay ids in the
table are no longer in it and were left out.

- 50,223 cells over 249 rows of assays and 20,993 species. 30,169 are `not assessable`.
  Of the 20,054 with a count: 6,224 `predicted detect`, 5,520 `partial`, 8,310
  `predicted fail`.
- 18,686 of those 20,054 are in scope and 1,368 out of scope. Out-of-scope cells are few
  because nothing is retrieved for them on purpose yet.
- The sentence the map was built for comes out of it. For *Ranavirus micropterus1*
  (largemouth bass virus): `Ranavirus_micropterus1_MCP_Li_2025` is `predicted detect` at
  28/28, while `Ranavirus_MCP_Pallister_2007` is `partial` at 57/86,
  `Ranavirus_VIR_Pallister_2007` 55/64 and `Largemouth_bass_virus_MCP_Grizzle_2003` 12/33.
  For *Ranavirus epinephelus1* (the grouper iridoviruses) `Ranavirus_MCP_Pallister_2007` is
  `predicted fail` at 0/6 and `Ranavirus_MCP_Johnson_2008` is `partial` at 12/16.
- 132 in-scope cells with 20 or more records are `predicted fail`. The largest are
  pan-family assays on species inside their declared scope, e.g.
  `Chordopoxvirinae_POL_Bracht_2006` on *Orthopoxvirus monkeypox*, 0/15867 from 5 footprints.
  Not examined further in this session.
- 136 cells with 50 or more records rest on a single footprint, which is the
  non-independence of GenBank records made visible.

## Two things the run showed about the design

**The trace rule is permissive.** Inside a `together` row, round 1 fails only on a
3'-terminal mismatch or no site. Across the 34 protocols with both rows assessed, the
`together` detected share differs from round 2 alone by a median of 0.0 points and is
within 2 points for 18 of them. For `Lyssavirus_N_Vazquez-Moron_2006`: round 1 alone
59.8% (8387/14027), round 2 alone 96.7% (14135/14614), together 99.3% (13487/13583). The
strict reading in `nested.py` (round 1 must itself be detected) would put together near
round 1's 60%. Nothing measured says which is right; the rule was agreed in outline and
has no bench panel behind it.

**Most cells are blank.** 60% of cells are `not assessable`, concentrated in pan-family
archives (`Haemosporida_cytb_Hellgren_2004_HaemNFI`: 4,713 of 5,236). Without a locus
check a blank cannot be told from a failure in which neither primer lands, so the map
under-reports failure on distant species. The report sums blanks per assay into one line
and `coverage.tsv` lists them.

## Later the same day: both `together` rows, and the locus check as a function

**Both rules are shown.** The maintainer chose to print `together` twice, trace rule and
strict, until a bench panel decides. On the same calls: the median protocol differs by 0.4
points of detected share between the two, six of 34 differ by more than 10, and 511 of
3,462 `together` cells change their word. The widest: `Chlamydia_trachomatis_16S_Messmer_1997`
258/363 under the trace rule and 0/363 strict; `Lyssavirus_N_Vazquez-Moron_2006` 13487/13583
and 7988/13583; `Astroviridae_RdRp_Chu_2008` 2285/2929 and 1101/2929. The run is 53,685
cells with the extra rows.

**The locus check is built and not wired in** (`assaywatch/locus_check.py`,
`tests/test_locus_check.py`, 15 tests). It is a local, gapped alignment (Smith-Waterman) of
a reference amplicon against a record on both strands, reporting `identity` (of aligned
columns, the share that match) and `covered` (the share of the reference spanned). The
first version was a semi-global edit-distance search and was dropped before it was
committed: it must place the whole reference, so a record ending mid-locus scored as a
poor full match instead of a good half, and `covered` meant nothing.

The scoring scheme was chosen by simulation, at thresholds 0.70 identity and 0.80 covered.
"Found" is how many of 40 true 200 bp loci with that share of substitutions were called
present. "Chance" is the longest stretch of the reference matched in random records.

| mismatch, gap | found at 20% | 25% | 30% | 35% | chance, 200 bp ref in 3 kb | 100 bp ref | 200 bp ref in 100 kb |
|---|---|---|---|---|---|---|---|
| -1, -2 | 40 | 40 | 40 | 0 | 0.56 | 0.86 | 0.69 |
| -2, -3 | 40 | 35 | 11 | 0 | 0.10 | 0.23 | 0.15 |
| -1, -3 (used) | 40 | 40 | 40 | 0 | 0.23 | 0.49 | 0.28 |

No random record was called present under any scheme (172 trials each). The limits of
this: simulated substitutions are spread evenly and real divergence is not; nothing was
run on a real archive, because the archives are on the maintainer's Mac and the session
was not linked to it at the time; and 100 bp references have the least room (0.49 against
a threshold of 0.80). Speed: 0.8 s for a 300 bp reference against a 200 kb record.

`config.yaml` records why 0.70 identity is suspect. Wiring it in waits on a decision about
where it runs, which is on the roadmap.

## The locus stage, and the first run on real archives

The maintainer chose a stage of its own over a change to the screen. `assaywatch locus`
(`locus.py`) checks the unjudged records (`no_amplicon` not labelled `diverged`) and writes
`locus.tsv.gz`; `assaywatch coverage --locus` joins it. Three things were added that the
plan did not have, each forced by a real archive:

**The flank rule.** The references in `docs/locus-references.json` are amplicon interiors
with the primer sites trimmed off, so an interior can be whole in a deposit that stops
before a primer site. A record counts only when the locus is present AND the record runs
at least `scoring.locus_identity_trim_bp` past where the whole reference would sit, on both
sides. It is not a refinement: for `Ranavirus_MCP_Johnson_2008`, 314 unjudged records hold
the locus and 311 of them have no room. Without the rule the assay would read 83/397 on
its own species instead of 83/88.

**Seeding.** Five 491 bp references against a 105 kb ranavirus genome took seconds per
record aligned whole. Records over 5 kb are now aligned only where 7-base words shared
with the reference pile up on one diagonal, up to twelve stretches per reference and
strand. Measured on a 200 bp locus at 30% substitution in 100 kb of random sequence
(40 of 40 found when aligned whole): words of 8 and 3 stretches, 35; 8 and 30, 37; 7 and
12, 39; 6 and 30, 40. 7 and 12 is used. Evenly spread substitutions are the worst case.

**A minimum reference length.** Interiors of short amplicons are useless: 17 bp for
`Ranavirus_MCP_Pallister_2007`, 28 for `Orf_virus_RPO147_Zhao_2013`, 87 for
`Ranavirus_micropterus1_MCP_Li_2025`. Under `coverage.locus_min_reference_bp` (100) a
reference is not used and the assay is left alone.

### Controls, 2026-11-01 calls, thresholds 0.70 identity and 0.80 covered

Up to 150 records per group, sampled with a fixed seed, the references' own source
records left out. "Present at 0.60" recomputes the same alignments at the lower identity.

| assay (reference bp) | group, as the screen called it | n | present at 0.70 | at 0.60 | identity of those covered |
|---|---|---|---|---|---|
| Ranavirus MCP Johnson 2008 (491) | detect | 150 | 150 | 150 | 0.73 to 0.99 |
| | fail | 9 | 8 | 8 | |
| | no_site | 150 | 38 | 38 | median 1.00 |
| Ranavirus VIR Pallister 2007 (172, 188) | detect | 150 | 92 | 92 | 0.87 to 0.98 |
| Largemouth bass virus MCP Grizzle 2003 (208) | detect | 10 | 10 | 10 | 1.00 |
| | fail | 22 | 22 | 22 | 0.99 |
| | no_site | 79 | 56 | 56 | median 0.82 |
| Avipoxvirus 4b Farias 2010 (210) | detect | 150 | 150 | 150 | 0.94 to 1.00 |
| | fail | 46 | 46 | 46 | median 0.88 |
| | diverged | 21 | 20 | 20 | median 0.87 |
| | no_site | 150 | 81 | 81 | median 0.79 |
| SIV pol Takehisa 2009 HahnF1 (478) | detect | 150 | 141 | 150 | from 0.67 |
| | reduced | 116 | 96 | 116 | from 0.66 |
| SIV pol Takehisa 2009 HahnF2 (245) | detect | 147 | 147 | 147 | from 0.82 |
| | fail | 150 | 5 | 150 | 0.66 to 0.68 |
| | diverged | 150 | 34 | 144 | 0.64 to 0.69 |

Negative control, references of one family against 200 records of an unrelated one
(ranavirus against avipox and back, ranavirus against SIV and back): 0 of 800 present,
longest chance match 0.38 of a reference.

What follows from it:

- **0.70 identity was wrong and is now 0.60.** The SIV `fail` records have both primer
  sites, so the locus is certainly there, and 145 of 150 were refused at 0.70. This is the
  population `scoring.locus_identity_min` already warned about. Coverage does the
  excluding, so the lower identity admitted no negative.
- **A length-variable locus is missed.** VIR Pallister amplifies a repeat region (products
  of 212, 228, 244, 260, 276 and 308 bp). 78 of its 218 detected records are not shown to
  hold the locus, at 0.64 covered and 0.99 identity, and the whole-record alignment gives
  the same answer, so it is the gap score and not the seed. A blank, not a false failure.

### The stage on six assays

9,870 unjudged records in 8 min 41 s on one core. 1,472 hold the locus at 0.70 and 1,644
at 0.60; 680 of those have room for both primer sites. By assay at 0.60, present with
room / present without: Avipox Farias 616 / 220; Grizzle 56 / 1; Johnson 3 / 311; VIR
Pallister 0 / 19; SIV HahnF1 0 / 167; SIV HahnF2
5 / 246.

Joined into the coverage map, 63 cells change: 42 go from `not assessable` to
`predicted fail`, 9 from `predicted detect` to `partial`, 1 from `partial` to
`predicted fail`, and 11 keep their word with a larger count. The largest:

| assay | species | before | after |
|---|---|---|---|
| Avipoxvirus 4b Farias 2010 | *Avipoxvirus fowlpox* | partial 14/17 | predicted fail 14/333 |
| | *Avipoxvirus pigeonpox* | not assessable | predicted fail 0/78 |
| | *Avipoxvirus turkeypox* | not assessable | predicted fail 0/21 |
| | Avipoxvirus sp. | partial 56/77 | partial 56/167 |
| | Avipoxvirus isolate Hawaii | predicted detect 36/36 | partial 36/41 |
| Largemouth bass virus MCP Grizzle 2003 | *Ranavirus micropterus1* | partial 12/33 | partial 12/89 |

The Farias assay was published for avipoxvirus in Hawaiian birds and reads 36/36 on the
Hawaii isolates, so a failure on fowlpox-clade 4b sequences at about 79% identity is what
its design predicts. It has not been checked by eye, and it is the first finding this
stage has produced: treat it as a lead.

## Probe scoring, held the same day

Improvement 1 of the review (probes scored by mismatch count per chemistry) is on branch
`probe-rule-by-chemistry`, unmerged. Replayed against the four case sets it left every
summary figure unchanged and traded one documented catch for another: it gains
`Influenza_A_virus_HA_H3_Shu_2026` (`low coverage` to `declining`) and loses
`Influenza_A_virus_M1_Ward_2004` (`declining` to `stable`). Both hinge on one mismatch at
position 15 of a standard probe (T:G in 76% of H3 records, G:A in 32% of Ward's), which a
count cannot tell apart. Held by the maintainer, to be picked up later.
