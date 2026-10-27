# M1 is proposed for shipping, and the confirming rescreen measured the replay's one approximation

**Maintainer decision, 2026-10-26: M1 is proposed for shipping.** The change is on the
branch `experiment/2026-10-26-m1-proposed` and **not on `main`**, because the protocol in
`docs/journal/2026-10-24-scoring-strategy-test-plan.md` reads `docs/validation-cases-heldout.tsv`
once, by the maintainer, when a strategy is proposed for shipping — and that read has not
happened. `main` still ships `mispair_penalty: {}`.

M1 is the identity-aware 3'-window discount, `mispair_penalty: {G:T: 0.0, T:G: 0.0}`. It
shipped on 2026-10-21 and was reverted on 2026-10-22. The case for re-taking that decision
is in `docs/journal/2026-10-26-s4-m1-no-longer-refuted.md`; this document records the confirming
rescreen that the decision was made conditional on.

## What needed confirming, and why it was not a formality

Every candidate on the 2026-10-26 ladder was priced by replay, and a replay has exactly
one approximation: **candidate selection is frozen.** The screen evaluates every facing
primer pair in a record and writes only the winner, so a scoring change that would make a
different amplicon win cannot be seen in a replay. For S3a that risk was nil, because it
moves a call between classes without touching a penalty. **For M1 it was live**, because
M1 changes penalties and penalties decide which candidate wins.

So M1 was **really rescreened**, not replayed, over every tier-2 assay whose calls it
moves: 17 assays, 18 retrieval groups, 462 MB of archives, **514,096 records**.

## The result: 0.0004%, and every disagreement is in the safe direction

| | |
|---|---|
| rows compared | 514,096 |
| `call` disagreements | **2** |
| `penalty` disagreements | **11** |
| `reason` disagreements | **0** |
| rows M1 moves, real screen | 494 |
| rows M1 moves, replay | 492 |

**All 13 disagreements run the same way: the real screen finds a better candidate than
the replay could see.** Both call disagreements are `reduced` in reality where the replay
said `fail`, and every penalty disagreement has the replay higher (8 against 5.5, 11
against 10, 9 against 7). That direction is not a coincidence — a replay is stuck
re-scoring the amplicon the *shipped* rule chose, and a loosening candidate would have
picked a better one.

So the approximation is **pessimistic**. A candidate priced by replay is never flattered
by it, which means every rejection in the ladder stands without qualification, and the two
survivors are if anything slightly under-credited.

## Neither disagreement can move a verdict

Both fall on `ENTEROVIRUS_ssRNA_VP3_VP1` (`NC_034267.1` and `KU297674.1`). Its tier-2 case
is `works` at 2018-09-30, and the verdict there is:

| | detected share | interval | status |
|---|---|---|---|
| shipped | 97.6% of 755 | 96%–98% | `stable` / agrees |
| M1, replayed | 97.9% of 755 | 97%–99% | `stable` / agrees |

The threshold is 90%. Two more `reduced` records, which count as detected, could take
97.9% to at most 98.2%. The verdict is nowhere near its boundary.

**So M1's headline result survives the confirming rescreen: zero tier-2 verdict changes
under real screening, exactly as under the replay.**

## What this adds to the harness

`scripts/rescore.py`'s boundary statement said the effect of frozen candidate selection
"is bounded by how many records hold more than one candidate and is unmeasured". It is
measured now, and the module and its printed boundary both say so. That matters beyond M1:
every future candidate priced by replay inherits a known, bounded, one-directional error
rather than an open question.

It is also the fourth independent validation of the harness, and the first to find a
disagreement at all:

| check | rows | disagreements |
|---|---:|---|
| S0 over the full table | 2,724,036 | 0 |
| a real `engine: serial` rescreen of one archive | 3,971 | 0 |
| a real M1 rescreen of taxid 195944 | 7,904 | 0 |
| **a real M1 rescreen of every tier-2 assay it moves** | **514,096** | **2 call, 11 penalty** |

The first three all returned zero, which is reassuring and slightly misleading: the
approximation is real, it just needed 514,096 rows and a penalty-changing strategy to show
itself.

## What is left for the maintainer

1. **Read `docs/validation-cases-heldout.tsv` once**, against the M1 branch. This is its
   designated use and it has not been spent.
2. If it holds, merge `experiment/2026-10-26-m1-proposed` and run a full pipeline, which
   will rescreen everything because `scoring` is in the screen signature.
3. If it does not hold, the branch is the record of what was tried and the revert stays.

Two cautions that belong with the decision and are not resolved by anything above. The
reason M1 is no longer refuted is that one assay's recent window grew, not that new
evidence arrived about the G:T wobble — so this re-takes a decision on the back of a
**denominator** change, in the layer this project has repeatedly found to be its weakest.
And the panels that favour M1 are two papers, Forslund and Barrett, with 7 rescued rows
between them.
