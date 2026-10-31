# S6: charging the severe mispairs a premium is killed on both of its pre-registered criteria

2026-10-27, late. M1 shipped the free half of the Kwok table this evening — a G:T/T:G
wobble inside the 3' window costs nothing — and the roadmap said at once that two
discount entries are not an identity table. S6 priced the other half: the mispairs Kwok
1990 and Stadhouders 2010 found to suppress yield, charged as penalty INCREASES. A:G,
G:A and C:C at twice the position penalty (so one in the 3' window of a conventional
primer costs 4.0, over `reduced_max`), A:A at one and a half times.

    python scripts/rescore.py --calls results/2026-10-26/calls.tsv.gz \
        --strategy strategies/s6-kwok-premium.yaml --out .tmp/s6

Control: the S4 replay, which is the shipped scoring (M1 plus S3b plus the probe switch)
on the same table.

## It tightens, as predicted, and tightening is what kills it

| | shipped (S4 replay) | S6 |
|---|---|---|
| documented failures caught | 6/11 | 6/11 — **no catch added** |
| PPV of `declining` | 4/10 | 4/11 |
| false alarms | 4/32 | **5/32** |
| bench rows wrong, `forslund-1999-fap` | 6 | **7** |
| every other panel | unchanged | unchanged |

One tier-2 case moves: `Pan_flavivirus_NS5_3_round2` at 2017-03-31, a `works` case,
from `low coverage` to `declining` — a false alarm added, with no catch to show for it.
On the bench a premium can only break band rows and fix no_band rows, and it broke one
FAP band row and fixed nothing; 41 of the 57 negatives are Rahn's other-genus rows that
no scoring change reaches, and the 16 informative ones already fail.

Both kill criteria fired: "breaks a bench band row the shipped rule gets right without
fixing an informative no_band row", and "adds a false alarm on tier-2 without adding a
catch". Either alone would have done.

## What this does and does not say

It does not say Kwok and Stadhouders are wrong. It says that, on this registry, the
severe-mispair records inside the 3' window are already failing under the position
penalty — the premium had nothing to catch — and that where it does bite, it bites a
published positive and a working assay. The asymmetry the two papers measured is real;
the half of it this project could use is the discount, and that half is shipped.

What would be a different experiment: a premium applied only at the 3'-TERMINAL
position rather than the whole 5-base window, since that is where Kwok's suppression is
measured and where `terminal_mismatch_fails` already acts (and was shown inert for
conventional chemistry this afternoon). It has not been run, and after this result it is
not the next thing to run.

The replay moved 34,929 calls: 19,963 `fail → reduced` and 14,745 toward `detect` are
M1's, inherited from the shipped table; the premium itself adds 221 `reduced → fail`.
That is the measure of how little it had to work on.

`scoring.mispair_penalty` stays `{"G:T": 0.0, "T:G": 0.0}`.
