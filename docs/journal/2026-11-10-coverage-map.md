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
(`tests/test_coverage.py`, 38 tests, in the fast tier). `coverage_map(calls, species_of,
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

## Probe scoring, held the same day

Improvement 1 of the review (probes scored by mismatch count per chemistry) is on branch
`probe-rule-by-chemistry`, unmerged. Replayed against the four case sets it left every
summary figure unchanged and traded one documented catch for another: it gains
`Influenza_A_virus_HA_H3_Shu_2026` (`low coverage` to `declining`) and loses
`Influenza_A_virus_M1_Ward_2004` (`declining` to `stable`). Both hinge on one mismatch at
position 15 of a standard probe (T:G in 76% of H3 records, G:A in 32% of Ward's), which a
count cannot tell apart. Held by the maintainer, to be picked up later.
