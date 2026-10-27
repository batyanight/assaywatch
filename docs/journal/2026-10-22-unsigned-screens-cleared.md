# The 20 unsigned screens are gone, and collect now refuses them (2026-10-22)

The 2026-10-21 full run found it and wrote it down: 20 of 316 screens had **no
`.snakemake/metadata` record**, so Snakemake saw the output present, its only
input (the FASTA) unchanged, and had no stored params to compare a new code hash
against. The conclusion recorded then was exactly right, including the part that
mattered most:

> Nothing is wrong *today*: rescreening `11229/all` by hand and diffing column by
> column gives **every shared column identical on every row** ... But "editing a
> scoring threshold rescreens the affected archives" is not true for these 20,
> and that matters the moment a threshold really changes.

A threshold really changed the next day. M1 moved `_code_hash`, every other
archive rescreened, and these 20 did not — so both tables the M1 tier-2 verdict
was taken from (`results/2026-10-21/`, `results/2026-10-22/`) carried 20 archives
scored under 2026-10-18 code. The verdict survives it (below), but it should not
have been a question anyone had to answer after the fact.

## Cleared

The M1 revert forced a full rescreen on its own — reverting `mispair_penalty`
changed `_SCREEN_CFG`, hence `_code_hash`, hence every screen's signature param —
and the 20 rode along under `--forcerun`, which they needed because their params
check structurally cannot fire:

    jq -r '.screen_inventory[] | select((.stored_signature // "") == "") | .path' \
        results/2026-10-22/calls.provenance.json > /tmp/unsigned.txt
    caffeinate -i snakemake --cores 4 --forcerun $(tr '\n' ' ' < /tmp/unsigned.txt)

`snakemake-2026-10-22-revert-fullrun.txt`, **337/337 steps, 15m 11s**, exit 0.
Afterwards:

| check | before | after |
|---|---:|---:|
| screens storing no signature | 20 of 330 | **0 of 330** |
| `signature_verified: true` | 310 | **330** |
| screens last written 2026-10-18 | 20 | **0** |
| `WARNING: ... store no signature` in the log | present | **absent** |

Deleting the stale outputs was the obvious route and is **not** what was done:
`--forcerun` regenerates them in place, which needs no deletion at all. Worth
remembering as the cheaper and safer habit — the inputs are all local, so a
forced rescreen of a named archive costs seconds.

## The tier-2 baseline, re-measured on one scoring generation

    python scripts/retrospective.py --cases docs/validation-cases.tsv

**Identical to the pre-M1 table on all 49 cases** — `fails` 5 agrees / 3
DISAGREES / 3 undecided, `works` 10 / 5 / 6 weaker / 11 undecided, `partial`
2 / 2 / 1 weaker / 1 undecided. So the revert is complete and the 20 stale
screens never changed a tier-2 verdict, which is the same answer the 2026-10-21
by-hand diff got. **5 of 11 documented failures caught is the baseline every
future one-knob test is measured against**, and it now rests on 330 screens all
written on the same day under the same settings and all signature-verified.

## Hardened, so it cannot recur quietly

`collect` warned about unsigned screens and exited 0. The warning fired in every
run since 2026-10-21 and in the M1 re-screen log at line 5895, and it changed
nothing, because a warning in a 300,000-line log is not a control.

`_raise_for_unverifiable_signatures` now refuses them, as a sibling of
`_raise_for_stale_signatures`. The argument for warning was sound when it was
made — "does not say" is a different fact from "says something else", and these
20 held correct calls — but it depended on a condition that has now expired:
every screen on disk carries a signature, and every new screen writes its own, so
an unsigned screen from here on is a stale file restored from somewhere rather
than a legacy artefact. The refusal names the files and says to use
`--forcerun`.

The sidecar still records `stored_signature: null` / `signature_verified: null`
rather than `false` for a caller that passes no expected signatures — "cannot
say" and "says something wrong" stay different facts there, because that
distinction is what made this visible in the first place.
