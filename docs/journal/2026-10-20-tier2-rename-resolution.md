# The calibration harness was silently dropping 13 of 49 cases (2026-10-20)

`scripts/retrospective.py` looked each validation case's `assay_id` up in the
calls table and fell back to `"no data"` when it missed, which `classify()` reads
as `undecided` — "the tool declined to judge". An id that matches nothing is
indistinguishable from an assay that genuinely has no records, and nothing said
so.

The assay-ID renames (`docs/rename-mapping.tsv`, 27 RENAME rows) were applied to
the registry and to `docs/validation-cases.tsv` but not to the archives, so any
calls table from before them stopped matching. Measured:

| calls table | cases matching directly | matching only through a rename |
|---|---:|---:|
| `results/2026-10-17/` | 36 | **13** |
| `results/2026-10-20/` | 49 | 0 |

Thirteen of the 49 case rows, 4 of them `fails` cases, were scored `undecided`
on the 2026-10-17 table for a bookkeeping reason.

## What it cost, and what it did not

**The published numbers were right.** With ids resolved, both tables now give
exactly the same confusion matrix:

| | `fails` caught | disagreements | undecided |
|---|---:|---:|---:|
| `results/2026-10-17/`, before this fix | 3 / 11 | 9 | 22 |
| `results/2026-10-17/`, after | **4 / 11** | **10** | **17** |
| `results/2026-10-20/`, after | **4 / 11** | **10** | **17** |

4/11 and 10 is what `docs/journal/2026-10-20-pan-family-override.md` already claims for
the shipped rule, so that doc was measured on a consistent basis — before the
renames landed in the cases file. The damage was never to the recorded figures.
It was to **re-measurement**: anyone re-running the comparison after the renames
got 3/11 and 9 and had no way to tell why. (On the 2026-10-18 table, which was
also screened under the reverted conventional override, the same run read 0/11.)

Note the two tables agreeing to the digit: the 3/11 → 4/11 and 22 → 17 movement
between them was **entirely this bug**, not the extra records the newer run
retrieved.

## Why that mattered more than the arithmetic

The case the renames hid includes **`CDV_P_gene_Scagliarini_2007` as of
2021-07-06** — and of the four `fails` the tool catches, it is the only one the
override rule touches at all:

| caught case | status | from override? |
|---|---|---|
| Paramyxovirinae L round1, 2019-02-01 | `declining` | no — pooled 18.5% of 1,056 |
| Paramyxovirinae L round2, 2019-02-01 | `low coverage` | no — pooled 4.5% of 755 |
| Forslund L1, 2011-06-14 | `low coverage` | no — pooled 79.3% of 715 |
| **CDV_P Scagliarini, 2021-07-06** | `declining` | **yes** — pooled `low coverage` 80.7% of 83, overridden on *Morbillivirus canis* at 67/83 = 80.7% |

So the entire empirical case for the shipped override rule rests on one
validation case, and that case was reading `undecided` to anyone who
re-measured. `docs/journal/2026-10-20-pan-family-override.md` rejected three candidates
precisely *because* they drop this catch; on a post-rename re-measurement those
candidates would have looked free, and the rule would likely have been reverted
on evidence that had quietly disappeared.

Its `mechanism` column is `drift`, confirmed in the cases file, so the coverage
excusal in `classify()` does not apply: without the override its `low coverage`
scores `partial` against an expected `fails` and the catch is lost outright.
That is the doc's argument, and it holds.

Note also what this case is: the firing lineage holds all 83 records at exactly
the pooled share, so it is an **above-pooled** override — the pattern
`docs/journal/2026-10-20-pan-family-override.md` point 2 wants to gate out. The one case
justifying the rule is an instance of the pattern the proposed `< pooled` gate
would suppress. That tension is now on the record in both docs.

## Verdict on the shipped rule

**It stands, unchanged.** Its claimed figures reproduce exactly on corrected
evidence, and the reason it beat the more principled alternatives — that they
drop the CDV_P catch — is verified structurally: that catch is the only one any
override candidate can move, and its `drift` mechanism means losing the override
loses it.

**What was verified here, and what was not.** The shipped row (4/11, 10) is
re-measured. The decisive mechanism is verified case by case. The six
alternative rows were **not** re-run: each is a different predicate inside
`AssayDrift._lineage_check`, reachable only by changing `assaywatch/drift.py`,
and their internal arithmetic is consistent with the shipped row and with the
catch structure above. If those rows are ever to be re-derived rather than
trusted, the right move is a selectable candidate in the `lineage` config block
so the comparison is reproducible instead of hand-made — which is also what
would have caught this.

## The fix

`scripts/retrospective.py` now resolves ids through `docs/rename-mapping.tsv` in
**both** directions (a case may name the old id or the new one, and a table may
hold either, so neither side is canonical), reports on stderr which cases were
bridged and that the table therefore predates a rename, and **refuses to print a
confusion matrix at all** when an id matches nothing and no rename reaches one —
naming the ids rather than averaging them in as `undecided`. A REMOVE'd entry
gets its own `removed` verdict instead of inflating the undecided count.

`rename_map` now lives in `retrospective.py`, and
`scripts/lineage_override_audit.py` imports it rather than carrying a second
copy.

Tests in `tests/test_retrospective.py`: an unmatched id raises and names itself;
a rename bridges in each direction; a removed entry reads `removed`; an exact hit
beats an alias. The old test that asserted a ghost id reads `no data` is gone —
that was the bug, pinned. The status-to-verdict test reached `undecided` through
a ghost id and now does it honestly, by asking about an assay before any of its
records existed.
