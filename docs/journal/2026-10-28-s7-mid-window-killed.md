# S7, the mid-window penalty, is killed on the criterion it registered — and it bought nothing

2026-10-28. The held-out false alarm traced to a single internal mismatch
(`2026-10-28-g2r-false-alarm-traced.md`), and the generalisation was that
`primer_mid_penalty: 1.0` equals `detect_max: 1.0`, so one mid-window mismatch sits on the
detect/reduced boundary and a second anywhere crosses it — 69 sites across 23 assays. S7
halved that penalty to 0.5 and was registered first, with S3b's kill criteria
(`strategies/s7-mid-window-penalty.yaml`).

    python scripts/rescore.py --calls results/2026-10-27/calls.tsv.gz \
        --strategy strategies/s7-mid-window-penalty.yaml --out <scratch>

## It moves a great deal and changes nothing

**45,797 of 2,811,794 calls move** — 30,673 `reduced` → `detect` and 15,124 `fail` →
`reduced`, every one a loosening, as predicted, and more than twice S3b's 19,081.

Tier-2, on the development set, is **identical to the shipped rule, case for case**:

| | shipped | S7 |
|---|---|---|
| documented failures caught | 6/11 | 6/11 |
| PPV of `declining` | 4/10 | 4/10 |
| false alarms | 4/32 | 4/32 |
| partial gaps named | 2/6 | 2/6 |

## And on the bench panels it trades two errors for two others

179 labelled rows, **166 right = 92.7% — the same accuracy as the shipped rule** — with
the errors moved rather than removed: **12 false negatives become 10, and 1 false positive
becomes 3.**

The three false positives are the kill:

| panel | record | label | S7 call | penalty |
|---|---|---|---|---|
| forslund-1999-fap | NC_039089.1 | HPV71 | reduced | 1.5 |
| forslund-1999-fap | LR861883.1 | **HPV55** | reduced | 3.0 |
| forslund-1999-fap | OP971071.1 | **HPV44** | reduced | 3.0 |

Under the shipped rule the same panel has exactly one, HPV71 at penalty 1.5 (checked
directly with `scripts/bench_panel.py`). So **HPV55 and HPV44 are new**, they are
papillomaviruses the FAP consensus assay is reported not to amplify, and they are
therefore within-family negatives — which is word for word what the registered criterion
named:

> it newly predicts a band on any of the 16 bench negatives that are within-family rather
> than other-genus, which are the only rows that can punish a loosening

**S7 dies here.** Not on a close call: it buys no tier-2 catch, no accuracy, and it
breaks two of the few rows in the whole panel set that can punish exactly this kind of
change.

## What the two false negatives it fixed were, because that is the honest other half

The five remaining FAP false negatives sit at penalties 3.5 to 4.5 and the five Leptospira
ones at 3.5 to 11 — too far above `reduced_max: 3.0` for a halved mid penalty to reach.
The two S7 rescued were nearer the line, and rescuing them is what dragged HPV55 and HPV44
across it from the other side. That is the shape of the problem: **on these panels the
positives and the within-family negatives are not separated by the mid-window penalty**,
so no value of it can fix one without breaking the other. A threshold cannot do what only
identity can.

## Which leaves S7b, and a sharper statement of the question

`scoring.mispair_penalty` already expresses identity and `score.penalty_for` applies it
only inside the 3′ window, by the measured decision of 2026-10-22. **S7b** — extend it to
the mid window *alone* — is the candidate the literature actually supports, and it is a
different experiment: it would discount the G:T wobble that costs the monkeypox G2R assay
its verdict while leaving the A:A and A:C mispairs in the FAP negatives at full price. It
needs a `mispair_window` setting rather than a config overlay, so it stays registered and
unpriced.

**And the general claim about the mid window survives the death of this candidate.** 69
sites on 23 assays still turn on a single non-3′ mismatch, and the panels now say
something stronger than before: the mid-window penalty is not merely unpriced, it is
**unpriceable on this evidence** — the rows that would reward loosening it and the rows
that punish loosening it move together. What would separate them is identity, or data
this project does not have. That belongs in `config.yaml` beside the setting, where the
admission of "no evidence" is the house style.
