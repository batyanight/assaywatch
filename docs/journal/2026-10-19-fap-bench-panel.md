# FAP59/64 on Forslund's own type panel (2026-10-19)

Follow-up to `docs/journal/2026-10-19-pan-family-cases.md`, which left "score FAP59/64
against the HPV16 reference genome by hand" open. Script:
`scripts/bench_panel.py`. Panel: `docs/bench-panels/forslund-1999-fap.tsv`.
Current `config.yaml` (no `by_chemistry` override).

## HPV16 fails on one G·T wobble

NC_001526.4 has a full FAP site: FAP59 at 4901-4922 (+), FAP64 at 5362-5385 (-),
484 bp, the size Forslund reports (~480 bp). Mismatches:

| oligo | from 3' end | primer:template | penalty |
|---|---|---|---:|
| FAP59 | 20, 19 | A:A, A:C | 0.5 + 0.5 |
| FAP59 | 5 | W opposite G = A:G / T:G | 3.0 |
| FAP64 | 20 | | 0.5 |

Total 4.5 > `reduced_max` 3.0, so the call is `fail`. All but 1.5 of that is the
position-5 mismatch, and half the degenerate pool forms a T:G wobble there, the
mispair Kwok 1990 found almost free. The same pattern (fwd 20,19,5) is on 4,682 of
the HPV16-titled records in the archive, so it is a conserved type feature, not
drift. Forslund amplified HPV16.

The 2026-10-18 archive shows this pattern as `reduced` at 3.5. That run was scored
with the reverted c15a3b7 override (3' penalty 2.0, `reduced_max` 5.0); see
`docs/journal/2026-10-19-conventional-override-validation.md`. Do not read 2026-10-18 calls
as current scoring.

## The panel: 70 of the 75 types

Forslund tested 75 types and got a band from 65 (abstract, PMID 10501499). One
genome per type 1-75, RefSeq first (sourcing and gaps in the TSV header). Call vs bench:

| | detect | reduced | fail | no_amplicon |
|---|---:|---:|---:|---:|
| band (60) | 25 | 21 | **14** | 0 |
| no band (10) | 0 | 1 | 8 | 1 |

The scorer gets the no-band types right (9 of 10; HPV71 reads `reduced`). It
fails 14 of 60 types the bench amplified (23%). Every one of the 14 has a mismatch
2-5 nt from the 3' end. So do six of the ten no-band types, which is why position
alone cannot separate them. Identity can:

| | 3'-window mispairs |
|---|---|
| band, called fail | HPV15, 16, 29, 34, 40, 51, 52, 56, 61, 67, 69, 72: **only T:G or A:G/T:G**. HPV17: A:A at 3. HPV60: A:C at 3. |
| no band | HPV1: A:A, T:C. HPV2: A:C. HPV35: T:G **and** A:C. HPV41: A:A, C:C. HPV66: A:C. HPV74: A:G/T:G at 5, plus four other mismatches (5.5). HPV44, 55: no 3'-window mismatch; fail on the mid/5' total (3.5). HPV63: no site. |

12 of the 14 false fails rest on a G·T wobble and nothing else in the 3' window.
Only one no-band type (HPV74) has a wobble-only 3' window, and it has enough other
mismatches to fail anyway. This matches the split that `config.yaml` already
describes from Kwok 1990 and Stadhouders 2010 and does not yet use.

## What this does and does not show

- It is the first type-level bench truth in the repo. It supports making the
  3'-window penalty depend on mispair identity, at least down-weighting T:G (and a
  degenerate pool that contains T:G). It does **not** give a number. Re-scoring by
  eye (e.g. T:G at 1.0) moves band-fails from 14 to 3 and keeps all 9 no-band
  fails, but that is one assay and 70 genomes fitted in-sample, which is exactly
  what the top of `config.yaml` warns against. A rule needs more panels, then a
  tier-2 run.
- Caveats: one genome per type, and several are recent isolates rather than the
  clones Forslund used. The no-band list was read from the paper in the earlier
  session; the PDF is not in `papers/`, so it has not been re-read since. Endpoint
  PCR, so "band" says nothing about yield.
- For the Forslund validation row (`fails`, coverage, Michael 2011): the tool's
  catch rests on HPV16, which the bench amplified, so it is a catch for the wrong
  reason. Michael 2011's claim, that FAP's spectrum is mainly beta, is about the
  same mismatches. The panel says the bench tolerates the G·T ones.

## Next

- More bench panels. Any design paper with a per-strain band/no-band table is
  one: same TSV format, same script.
- Then an identity-aware `score_primer` with the table in `config.yaml`, checked on
  the panels and on tier-2 before shipping.
