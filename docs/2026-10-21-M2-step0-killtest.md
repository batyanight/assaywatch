# M2 Step 0 kill-test: nearest-neighbour ΔG does NOT reproduce Kwok's 3'-mispair ordering — M2 killed (2026-10-21)

M2 (`docs/2026-10-20-pipeline-audit.md` §5) proposed scoring `thermo.py`'s
nearest-neighbour ΔTm/ΔG columns as the match criterion, on the premise that
**"M1 is a hand-rolled approximation of what NN parameters give for free."** Before
building the engine (a weeks-scale project, and demoted), the gating question is
whether that premise is even true: does an NN ΔG/ΔTm reproduce the 3'-terminal
mispair **severity ordering** that motivated identity-aware scoring in the first
place — Kwok et al. 1990 and Stadhouders et al. 2010: **A:G, G:A, C:C, A:A** strongly
suppress yield (~20–100×), while **T:G, G:T, T:C, T:T** are nearly free?

**Answer: no. The premise is false, and M2 is dead on arrival as a replacement for
the M1 identity table.** The NN model measures a different physical quantity than the
one that kills these assays.

## What was tested

`primer3.calc_heterodimer`, the exact call `thermo.py` already uses (same conditions:
mv 50, dv 3, dntp 0.8, dna 250). For each of the 12 A/C/G/T mispairs placed at the
primer 3' terminus, the destabilisation vs the matched terminus, holding a fixed
19-bp core:

- ΔΔG = dg(X opposite Y) − dg(X opposite complement(X))
- ΔTm = tm(match) − tm(mismatch)   (the quantity M2 would actually score)

two unrelated moderate-GC contexts. Convention is M1's: mispair `X:Y` = primer base X
opposite template base Y.

(An earlier probe had shown `calc_end_stability` is identity-blind at the terminus —
same ΔΔG for C:C, C:T, C:A — because it simply drops the terminal pair. `calc_heterodimer`
*is* identity-sensitive, so it was the only candidate left that could carry M2. It can't.)

## Result: the classes overlap, and A:A/A:G land on the wrong side

ΔTm, fixed core, sorted most- to least-destabilising (+ = destabilised):

| mispair | class   | ΔTm (°C) |
|---------|---------|---------:|
| C:C     | SEVERE  |  **2.42** |
| C:T     |         |   2.35 |
| C:A     |         |   1.54 |
| G:T     | neutral |   1.41 |
| T:C     | neutral |   1.34 |
| G:G     |         |   1.27 |
| T:T     | neutral |   0.98 |
| G:A     | SEVERE  |   0.91 |
| T:G     | neutral |   0.83 |
| A:C     |         |  −0.62 |
| A:G     | SEVERE  | **−1.12** |
| A:A     | SEVERE  | **−1.48** |

Severe span −1.48..2.42; neutral span 0.83..1.41 — **total overlap**. ΔΔG (cal/mol)
gives the same verdict in both contexts (severe −801..1403 vs neutral 129..614,
OVERLAP). Only C:C is correctly ranked severe. **A:G and A:A come out *stabilising*** —
the opposite sign — and G:A sits in the middle of the neutral pack.

## Why: the model rewards exactly what Kwok penalises

The `calc_heterodimer` structure dump is the mechanism. It does **not** slip register:
for every mismatch it leaves the terminal base as an unpaired **dangling end** over an
identical 19-bp matched core, so the whole signal is the terminal dangling-end /
terminal-mismatch **stacking** parameter.

```
A:T (match)  tm=60.26   ...TCCAAGA / terminal A:T paired
A:A          tm=61.73   ...TCCAAG  with dangling A (primer) over A (template)
A:G          tm=61.38   dangling A over G
C:C          tm=59.48   dangling C over C
```

A dangling **purine** (A:A, A:G) stacks *more* favourably than the matched A:T
terminus, so the NN model scores these two as *more* stable — while Kwok shows Taq
cannot extend a 3' A:A or A:G at all. That is the whole point: **Kwok's severity is a
polymerase-extension (kinetic) property; the NN ΔG/ΔTm is an equilibrium melting
property.** They are orthogonal, and anti-correlated for the purine mispairs that
matter most. Duplex stability is not extension competence.

## Consequence

- **M2 is killed at Step 0.** NN parameters do not "give for free" what M1 encodes;
  they encode a different physics. Building a weeks-scale NN scoring engine would not
  reproduce — would partly invert — the one ordering (A:G/G:A/C:C/A:A severe) that the
  bench panels (FAP, Barrett) demand. Scope it closed, not deferred.
- **`thermo.py`'s "never scored" design is vindicated, in numbers.** The columns stay
  diagnostic. The module docstring's claim that absolute Tm is the useful-but-not-
  scorable number understated it: even ΔTm must not be scored as a 3'-mismatch
  severity signal, because it ranks A:A/A:G backwards.
- **M1 remains the right instrument** for identity-aware 3' scoring (an empirical
  per-mispair table from Kwok/Stadhouders + the bench panels), still HELD by Batya
  pending her decision on whether to pursue identity-based scoring at all. This result
  removes M2 as the "do NN instead" alternative that the hold was weighing M1 against.

## Reproduce (throwaway probe, not committed to `scripts/`)

```python
import primer3

COMP = {"A": "T", "T": "A", "G": "C", "C": "G"}
COND = {"mv_conc": 50.0, "dv_conc": 3.0, "dntp_conc": 0.8, "dna_conc": 250.0}
core = "GTCAGATGCCTAGTCCAAG"
rc = lambda s: "".join(COMP[c] for c in reversed(s))


def dtm(x, y):  # primer 3' x opposite template y
    mis = primer3.calc_heterodimer(core + x, y + rc(core), **COND).tm
    match = primer3.calc_heterodimer(core + x, COMP[x] + rc(core), **COND).tm
    return match - mis


for p in "ACGT":
    for t in "ACGT":
        if t != COMP[p]:
            print(f"{p}:{t}  dTm={dtm(p, t):+.2f}")
# add output_structure=True to see the dangling-end alignment
```
