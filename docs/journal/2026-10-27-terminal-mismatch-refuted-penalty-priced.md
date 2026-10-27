# The terminal-mismatch rule is not what makes the scoring pessimistic. The 3'-window penalty is

2026-10-27, later the same day. The morning's bench comparison measured **23 false
negatives against 1 false positive** for the shipped penalty rule
(`2026-10-27-thermo-vs-penalty-paired.md`) and this project has spent three weeks
naming one culprit for that: `terminal_mismatch_fails: true`, a qPCR-strength rule
applied to a registry that is 155 of 209 conventional PCR (2026-10-27). ROADMAP said
exempting conventional chemistry was "the single change this result most supports".

    python scripts/price_terminal_mismatch.py
    python scripts/rescore.py --calls results/2026-10-26/calls.tsv.gz \
        --strategy strategies/s3b-conventional-3prime-penalty.yaml --out .tmp/s5

**It is not. On the bench panels that exemption moves 0 of 179 predictions.**

## What the bench rows say

Four fixed config blocks, each applied to `conventional` assays only, scored over the
same 179 labelled rows (160 conventional, 19 another chemistry; 122 band, 57 no_band).
**No parameter is fitted**, unlike the thermodynamic arm of the morning's comparison,
whose cutoff was chosen on these same rows — so none of these accuracies is an
in-sample upper bound.

| arm | accuracy | TP | TN | FP | FN | rows moved |
|---|---:|---:|---:|---:|---:|---:|
| shipped | 86.6% | 99 | 56 | 1 | 23 | — |
| `terminal_mismatch_fails: false` | 86.6% | 99 | 56 | 1 | 23 | **0** |
| `primer_3prime_penalty: 2.5` | 87.7% | 101 | 56 | 1 | 21 | 2 |
| `primer_3prime_penalty: 2.0` | 89.9% | 105 | 56 | 1 | 17 | **6** |
| both of the above | 89.9% | 105 | 56 | 1 | 17 | 6 |

The penalty drop to 2.0 fixes 6 rows and breaks none: **McNemar exact two-sided
p = 0.0312**. Adding the terminal exemption on top changes nothing, row for row. Of the
6 it fixes, 5 are in `forslund-1999-fap` and 1 in `barrett-1993-morbillivirus`, so
this is about two independent events, not six.

**Why the terminal switch is inert, in one sentence:** a record whose primer carries a
3'-terminal mismatch almost always carries others that already exceed `reduced_max` on
their own, so removing the automatic fail changes the reason and not the call. That is
the same mechanism the 2026-10-26 registry-wide measurement found from the other end —
251 calls of 2.7 M moved and no verdict anywhere changed
(`2026-10-26-s3-chemistry-switches.md`). Two measurements, two directions, same answer.
The difference is what they license: the archive measurement says the rule is rarely
load-bearing, and the bench rows say that where it *is*, it is not the thing getting
the answer wrong.

**Why the penalty is the live suspect.** `primer_3prime_penalty: 3.0` equals
`reduced_max: 3.0` exactly, so one mismatch anywhere in the last five bases lands on
the detect/fail boundary, and 74.7% of all 284,062 `fail` calls sit within one
3'-window mismatch of it. At 2.0 one such mismatch is `reduced` and two still fail.
The literature supports a split by identity rather than a single number — Kwok 1990
has only A:G, G:A, C:C and A:A strongly suppressing yield — so 2.0 is a coarser
statement than the evidence deserves, and it is the one `config.yaml` already writes
out as a worked example.

## A loosening cannot be judged on a band-heavy panel alone, so count the negatives

Lowering a penalty can only turn a predicted no_band into a band. It can only fix
false negatives and only break false positives, and these panels are 122 band to 57
no_band, so they are structurally generous to it. Of the 57 negatives, **41 are
Rahn's** — other genera with no target gene, where nothing anchors and no scoring
change can reach them. **16 negatives can punish a loosening, and none of them moves**
under any of the four arms. That is the panel set's whole capacity to say no, and it
said nothing.

## What it does to the registry: 19,081 calls, and both tier-2 moves are improvements

Priced by replay over the 2026-10-26 calls table (2.72 M rows), against an S0 control
replayed from the same table on the same day, so the probe switch shipped this morning
is in both arms and cannot be credited here.

| | S0 (shipped) | S3b (penalty 2.0) |
|---|---|---|
| calls moved | 0 | **19,081, every one `fail` -> `reduced`** |
| documented failures caught | 6/11 | 6/11 — **unchanged** |
| caught by the `declining` flag itself | 2/11 | **3/11** |
| PPV of `declining` | 2/9 = 22% | **3/9 = 33%** |
| working assays called `declining` (false alarms) | 5/32 = 16% | **4/32 = 12%** |

Exactly two cases move, and they move in opposite directions on purpose:

- `Pan_flavivirus_NS5_3_round2` at 2017-03-31, a `works` case, goes `declining` ->
  `low coverage`. **A false alarm removed.**
- `PAPILLOMAVIRUS_dsDNA_L1_gene_Forslund_1999` at 2011-06-14, a `fails` case, goes
  `low coverage` -> `declining`. It was already counted as caught; now it is caught by
  the drift flag rather than by the coverage flag.

**The second one needs its mechanism stated, because a loosening gaining a drift flag
looks impossible.** `drift.require_working_baseline` only calls an assay `declining` if
it cleared the threshold in some earlier year. Loosening lifts the earlier-year share
above the threshold, the assay qualifies as having once worked, and the same present-day
shortfall is then readable as a decline instead of as a gap it never covered. So this
is not a new detection; it is the same failure, correctly attributed.

And it is the same assay. The FAP pair is where 5 of the 6 bench rows were fixed and
where the tier-2 case moved — one assay's false fails, visible from the bench and from
the literature at once.

## The confirming rescreen, for the two assays whose verdicts moved

The replay's one approximation is that candidate selection is frozen: the table holds
only the amplicon the screen chose per record, so a scoring change that would make a
different candidate win is invisible to it. That matters most where a verdict moved, so
both of those assays were really rescreened — every archive of their retrieval groups,
under the replay's own `config-used.yaml`, 25 archives in all.

    python -m assaywatch.screen registry <archive> \
      --only PAPILLOMAVIRUS_dsDNA_L1_gene_Forslund_1999,Pan_flavivirus_NS5_3_round2 \
      --config .tmp/s5/config-used.yaml --workers 4

**104,188 rows compared, 0 call disagreements.** Every row the replay produced for
these two assays was reproduced by a real screen, call for call, and no replayed row
was missing from the rescreen. 63 rows (0.06%) disagree on the penalty with the same
call, and **all 63 run the same way: the real screen finds a LOWER penalty**, i.e. a
better candidate amplicon than the replay could see. 40 of those rows are
`indeterminate` and 22 `fail`. That is the direction the replay boundary predicts, and
it means the approximation is pessimistic here rather than flattering: nothing in this
comparison was credited to S3b that a real screen does not also give it.

**Then the four largest remaining movers, for the same reason.** 19,081 calls move
across 84 assays, but they concentrate: six assays hold three-quarters of them. The
flavivirus, lyssavirus and rhabdovirus groups were rescreened the same way, 36
archives, 62 MB on disk.

**176,630 rows compared, 0 call disagreements, 28 penalty differences and all 28 again
pessimistic.** So the confirming rescreen now covers **6 of the 84 assays and 14,261 of
the 19,081 moved calls — 74.7%** — with not one call differing from the replay. The
largest assay still priced moves 395 calls
(`CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme`), then 374
(`PARVOVIRUS_ssDNA_VP1_gene_dependovirus`) and 333 (`HANTAVIRUS_ssRNA_S_segment`); the
remaining 78 together hold 4,820.

Two things follow. The replay is exact here on 280,818 rows, which is a far stronger
check than the 514,096-row M1 comparison that found 2 call disagreements — and S3b's
two tier-2 verdict moves rest entirely on assays that were really screened. What is
still unproven is a long tail of small movers, none of which can move a verdict on its
own at these counts.

## Shipped, the same day, on the maintainer's call

`config.yaml` now carries the first entry `scoring.by_chemistry` has ever held:

    by_chemistry:
      conventional:
        primer_3prime_penalty: 2.0

Two things changed shape when it shipped, and both are recorded rather than tidied
away:

**The test that guarded this block was inverted, not deleted.**
`test_the_shipped_config_overrides_nothing` existed because an entry here would once
have meant somebody set a threshold by eye. One entry is now measured, so what needs
guarding is the edge of the decision: exactly one chemistry, exactly one key, and
`terminal_mismatch_fails` explicitly absent — it was priced on the same rows the same
day and moves none of them.

**And the pricing script had a latent bug that only shipping could expose.**
`load_config` precomputes `_config_by_chemistry` whenever `by_chemistry` is non-empty.
`with_override` deep-copied the config and the copy carried that cache, so once the
shipped config had an override of its own, every arm would have resolved to the
SHIPPED conventional penalty and all the arms would have agreed — which reads exactly
like a clean null result. The arm isolation was already pinned by a test, so the test
failed the moment the config changed, and the fix is one `pop`. The measurement above
was taken while `by_chemistry` was still `{}`, so no cache existed and the arms were
independent; re-running after the fix reproduces it exactly, with the sign flipped
(`revert_3.0` now loses 6 rows to the shipped rule, p = 0.0312).

The arms are also named absolutely now — `revert_3.0`, `penalty_2.5`, `penalty_2.0` —
because "shipped" stopped meaning 3.0 and a relative name would quietly change
meaning under the reader.

## Status at the time of the decision: PRICED, NOT PROVEN

`config.yaml` still carries `by_chemistry: {}`. Three reasons, in order:

1. **A replay freezes candidate selection, and 6 of the 84 affected assays have now
   been rescreened** — 280,818 rows, 0 call disagreements, 74.7% of every moved call,
   including both assays that carry a verdict move. What is left unproven is a tail of
   78 assays holding 4,820 moved calls between them, the largest moving 395. That is
   thin enough that none of them can move a verdict alone, and it is still not the
   same as having checked.
2. **It moves every status in every report**, which is a maintainer's call and not a
   script's.
3. **The evidence is two independent bench events and two tier-2 cases.** It is the
   best-evidenced scoring candidate this project has produced — the first that
   improves precision without losing a catch — and it is still that thin.

What it is not is a guess. The kill criteria were pre-registered in
`strategies/s3b-conventional-3prime-penalty.yaml` before the run: lose a documented
catch, or newly predict a band on one of the 16 informative bench negatives. Neither
happened.

## What this corrects

- ROADMAP's "the single change this result most supports" named the wrong knob. The 23
  false negatives are real; `terminal_mismatch_fails` is not what causes them.
- `config.yaml`'s `by_chemistry` comment named `terminal_mismatch_fails: false` as
  "the first candidate, once validation can test it". Validation can now test it, and
  it is inert. The comment records that.
- The morning's write-up closed by saying the next question was whether that exemption
  fixes the 23 false negatives. It does not fix any of them.
