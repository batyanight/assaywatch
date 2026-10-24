# The `count_diverged_as_fail` + `anchor_fdr` pair, priced on the whole report

Branch `experiment/2026-10-24-diverged-and-anchor-fdr`. **Not for merge.**

`docs/2026-10-24-archive-anchor.md` closed with a recommendation: turn
`drift.count_diverged_as_fail: true` together with `drift.anchor_fdr: 0.01`, because
that pair gives wave 2 what it wanted (divergence counted as failure) with both of its
false alarms gone and the tier-2 matrix restored row for row. This is that
recommendation priced on the whole registry instead of on 49 cases. **It does not
survive the pricing.** Tier-2 is silent, but the pair rewrites the headline share for
72 of 183 assays, and its largest single movement is not drift.

## Method

One calls table, three configs, nothing else different. `results/2026-10-24/calls.tsv.gz`
rendered three times through `python -m assaywatch.report ... --run-date 2026-10-24`, so
the comparison is config-only: same code, same records, same date.

Both settings live in the `drift:` block, which is not part of `_code_hash`
(`Snakefile:_SCREEN_CFG` covers `scoring`, `amplicon`, `degeneracy`,
`thermo_conditions`). A dry run confirms it: 9 jobs, **zero `screen_archive`**. The pair
costs no rescreen, which is why it can be priced this cheaply at all.

| | shipped (off) | q = 0.01 | q = 0.001 |
|---|---|---|---|
| tier-2 development set | - | **identical, row for row** | **identical, row for row** |
| assays changing status | - | 14 | 9 |
| headline share unchanged | 183 | 111 | 118 |
| share fell >20 points | - | 9 | 7 |
| share fell 5-20 points | - | 8 | 6 |
| share rose | - | 5 | 7 |

Tier-2 rules out q = 0.05, which leaves the CMV row disagreeing (the archive doc's
table), and then says nothing at all: 0.01 and 0.001 both reproduce the shipped matrix
exactly. **Tier-2 cannot choose q.** 49 cases are too few, and this is the clearest
demonstration yet of why `docs/2026-10-24-scoring-strategy-test-plan.md` asks for a
bigger evaluation set before any scoring candidate is judged.

## Why 0.001 beats 0.01, which is the opposite of the usual direction

BH's bar for the kth smallest E is `(k/m) * q`, so a SMALLER q relabels MORE rows, not
fewer. Lowering q therefore makes the anchor test more aggressive about calling a lone
site a coincidence, and that is the direction that removes false alarms here.

What each q does to the ten biggest movers. `weak%` is the share of that assay's
`diverged` anchors above E = 1e-3; `left` is how many `diverged` rows survive to be
counted as failures.

| assay | family m | diverged | weak% | median E | left @0.01 | left @0.001 |
|---|---|---|---|---|---|---|
| `TRICHOMONAS_gallinae_18S_Renteria_Solis_2020` | 278 | 241 | **100%** | 7.0e-03 | **235** | **0** |
| `PHLEBOVIRUS_ssRNA_L_segment_round1` | 780 | 39 | 5% | 3.7e-04 | 37 | 1 |
| `BORNA_VIRUS_N_gene_Zimmermann_1994` | 1,198 | 209 | 12% | 1.1e-05 | 209 | 182 |
| `RETROVIRUS_RNA_polymerase_SIV_Keele_2009` | 7,918 | 3,927 | 10% | 4.3e-04 | 3,908 | 3,508 |
| `Pan_mycoplasma_16S_23S_intergenic_space_Rebelo_2011` | 24,032 | 346 | 13% | 2.8e-05 | 298 | 296 |
| `ARENAVIRUS_ssRNA_S_gene` | 5,697 | 520 | 16% | 1.8e-07 | 473 | 436 |
| `CIRCOVIRUSES_..._Rep_Gene_Mankertz_2000_round1` | 17,882 | 3,131 | 4% | 2.5e-08 | 3,119 | 2,895 |
| `Pan_coccidia_SSU_rDNA_..._Garner_2006` | 51,979 | 7,484 | 2% | 2.3e-08 | 7,434 | 7,324 |
| `Cryptosporidium_18SrDNA_Xiao_1999_round2` | 13,757 | 490 | 1% | 7.5e-11 | 484 | 470 |
| `MONKEYPOX_dsDNA_N3R_MGB_Kulesh_2004` | 2,950 | 1,654 | **0%** | 4.3e-10 | **1,654** | **1,654** |

The two ends of that table are the argument. Monkeypox N3R's anchors sit at E = 4e-10
and not one of them moves at either q: those are real primer sites carrying real
mismatches, and no FDR should touch them. Trichomonas `gallinae`'s 241 anchors sit at
E = 7e-3 — Bd's coincidence range — and **235 of them survive q = 0.01**, because they
are 241 of a family of 278 and so raise their own bar. That is exactly the relative-
threshold weakness `docs/2026-10-24-archive-anchor.md` wrote down against Enterovirus,
except here it changes a status and drops an assay from 100.0% to 13.6%. At q = 0.001
all 241 are relabelled and the assay returns to 100%, while Monkeypox keeps all 1,654.

So if the pair ever ships, it ships at **0.001, not the 0.01 the archive doc
recommended**, and the archive doc's recommendation is superseded here.

## Why it should not ship yet: Bornaviridae

At q = 0.001 the biggest remaining fall is `BORNA_VIRUS_N_gene_Zimmermann_1994`,
**98.2% -> 16.4%, `stable` -> `declining`**. Its 209 `diverged` anchors are mostly
strong (median 1.1e-05), so the FDR correctly leaves them alone. They are real sites.
They are in the wrong organisms:

    PZ133663.1  UNVERIFIED: Parrot bornavirus 5 isolate AoF cRNA sequence
    BK075415.1  TPA_asm: Orthobornavirus serini cRNA sequence
    BK075409.1  TPA_asm: Orthobornavirus alphapsittaciforme cRNA sequence
    BK075408.1  TPA_asm: Southern pacific rattlesnake bornavirus cRNA sequence
    BK064873.1  TPA_asm: Crotalus molossus bornavirus cRNA sequence
    PQ231665.1  Parrot bornavirus 5 isolate PaBV-5/HS45, complete genome

Zimmermann 1994 designed BornaF/BornaR against Borna disease virus in horses and sheep.
The registry entry's `target.taxid` is **178830, the whole family Bornaviridae**, so the
screen measures that assay against avian and reptilian bornaviruses it was never meant
to detect, and several of the records are `UNVERIFIED:` submissions or `TPA_asm:`
third-party annotations rather than primary deposits.

With the switch off those records are dropped and the assay reads 98.2%. With it on they
are counted as failures and it reads 16.4% and `declining`. **Neither number is a lie
about the arithmetic, and the label is still wrong**: this is a coverage statement about
a family-wide screen, not evidence that anything drifted. It is the same
coverage-versus-drift distinction the project already enforces elsewhere, arriving
through a new door.

`require_working_baseline: true` is the guard that should have caught this, and it
cannot: turning the switch on moves the baseline as well as the recent window, so the
baseline still looks like a working assay. The same reading probably applies to
`Pan_coccidia` and `Pan_mycoplasma`, where congeneric breadth IS the design intent, so
a mismatched site in a relative is a genuine coverage gap — and still not drift.

## A second consequence, found by a test rather than by looking

`tests/test_windows.py::test_drift_refuses_count_diverged_on_windowed_rows` failed on
the flip, and it was right to. A window archive (`assaywatch.windows`, the
distributable) labels its `no_amplicon` rows `windowed`, because why a record gave no
amplicon depends on sequence outside the kept windows, and `drift.assess` refuses those
rows when `count_diverged_as_fail` is on. So **with this pair shipped, a recipient of
the distributable cannot re-run drift under the shipped config.**

Nothing live is affected: the 2026-10-24 calls table holds **0** `windowed` rows and
there are **0** `*.windows.tsv.gz` sidecars on disk, because windowing is an explicit
export step. But it is a real promise to break, and the test now names both directions
explicitly instead of leaning on the shipped value.

## Recommendation

Do not merge this branch. The pair is sound where it was measured and the anchor test
does its job, but `count_diverged_as_fail` turns out to be entangled with a question
nobody has settled: whether a real primer site, carrying real mismatches, in an organism
the assay was never designed for, is a failure of the assay. Three things to settle
first, in order:

1. **Scope.** `BORNA_VIRUS_N_gene_Zimmermann_1994` carries a family-level taxid for a
   species-specific assay. That is worth fixing whatever happens to this pair, and it is
   a maintainer's call. How many other entries have a taxid broader than their design
   has been asked about but not counted.
2. **Whether `diverged` in a non-target congener counts at all.** If the answer is no,
   the switch needs a scope test and not only an FDR, and the per-lineage machinery is
   probably where it belongs.
3. **The distributable guard**, which is a documentation change if the pair ships.

If the pair ships after that, it ships at `anchor_fdr: 0.001`.

What is NOT in doubt, and is worth keeping from this exercise: tier-2 could not tell
0.01 from 0.001 even though they differ by 5 status moves and a 100%-to-13.6% swing on
one assay. The evaluation set is the bottleneck, exactly as the scoring-strategy plan
argues.
