# TNTBLAST, the tool a reviewer names, loses on these 179 rows — and the reason is the annealing temperature

2026-10-27, late. `docs/related-work.md` has answered "why not just use PCR_strainer?"
with a feature table since it was written, and PCR_strainer wraps thermonucleotideBLAST
— so TNTBLAST is the engine the question is really about. The comparison
(`scripts/compare_thermo.py`) was built for it on 2026-10-26 and could not run it:
bioconda has TNTBLAST for osx-64 and linux-64, not osx-arm64, and the osx-64 build needs
Rosetta 2. **Rosetta was installed tonight**, so the arm the script was designed around
finally ran.

    # Rosetta 2, then the x86_64 build, which runs emulated:
    softwareupdate --install-rosetta --agree-to-license
    CONDA_SUBDIR=osx-64 conda create -n tntblast -c bioconda -c conda-forge tntblast=2.77

    python scripts/tntblast_arm.py --tsv docs/2026-10-27-tntblast-bench.tsv \
      --binary "$(conda run -n tntblast which tntblast)"
    python scripts/compare_thermo.py --tntblast docs/2026-10-27-tntblast-bench.tsv

TNTBLAST ran one record at a time, 179 invocations, at a permissive Tm floor of 20 °C,
and the temperatures it reported are committed as `docs/2026-10-27-tntblast-bench.tsv`.
Per record it reports every amplicon it finds with the melting temperature of each
primer and of the probe; this takes the warmest amplicon's limiting primer and its
probe, and the comparison fits the cut afterwards. One record per invocation because a
record that yields no hit prints nothing at all, which in a multi-record database is
indistinguishable from a record that was never searched.

## The headline

| predictor | accuracy | TP | TN | FP | FN |
|---|---|---|---|---|---|
| **penalty rule, exactly as it ships** | **92.7%** | 110 | 56 | 1 | 12 |
| primer3 nearest-neighbour, ΔTm ≥ −16.7 °C (fitted here) | 92.7% | 117 | 49 | 8 | 5 |
| TNTBLAST, `-e 0 -E 54` (both fitted here) | 64.8% | 103 | 13 | 44 | 19 |

Paired, which is the only way 179 rows can separate two predictors
(`mcnemar_exact` on the discordant rows alone):

- penalty against TNTBLAST: they differ on 66 rows, **58 the penalty rule gets right and
  TNTBLAST wrong, 8 the reverse, p < 0.0001**;
- primer3 against TNTBLAST: differ on 70, 60–10 to primer3, p < 0.0001;
- penalty against primer3: differ on 22, 11–11, p = 1.0 — the tie already recorded in
  `2026-10-27-thermo-vs-penalty-paired.md`.

TNTBLAST was given **two** free parameters, its own `-e` and `-E`, each chosen to
maximise its accuracy on these same rows, where the penalty rule ran as it ships. It
still loses. That is the comparison the related-work table could not make.

## Why it loses, which is the part worth keeping

Not because its signal is absent. Fit a **separate cut per panel** — an oracle, each
assay keeping its own best pair — and TNTBLAST reads **157 of 179 = 87.7%**:

| panel | oracle | its own best cut |
|---|---|---|
| rahn-1992-salmonella-invA | 64/64 | `-e 52` |
| ahmed-2020-leptospira | 19/19 | `-E 54` |
| barrett-1993-morbillivirus | 7/7 | `-e 0` |
| rebelo-2011-mycoplasma | 8/8 | `-e 0` |
| meyer-1997-ati | 8/9 | `-e 0` |
| meyer-1997-ati-strains | 2/2 | `-e 0` |
| forslund-1999-fap | 49/70 | `-e 0` |

On the Salmonella specificity panel the separation is total: the 23 band records carry a
limiting primer Tm of 56.8–60.8 °C and all 41 no-band records 35.6–51.9 °C, so a cut at
52 °C gets every one of the 64 rows right. The Leptospira panel separates as cleanly on
the probe. **Those same cuts applied globally are a disaster**, because a cut of 52 °C
destroys the FAP and morbillivirus panels, whose assays anneal far lower.

So TNTBLAST's weakness here is not thermodynamics. It is that **a melting temperature
only means something against the temperature the reaction ran at**, and that is a
property of each assay's protocol, not of the method. Asked for one global cut, it is
asked to be right about seven protocols at once.

That is exactly the argument `thermo: false` has rested on since it was written, and it
is now measured rather than asserted — on the tool the objection names. It is also why
the `conditions` block went in tonight: of these six bench assays the registry now
carries an annealing temperature for **one** (Meyer 1997 ATI, 40 °C), so the honest,
non-fitted version of this experiment — give each assay its own published Ta as the cut
— cannot be run yet. When five more of these six carry one, it can, and at that point
TNTBLAST's 87.7% oracle becomes a real number rather than a ceiling.

## What does not change

The penalty rule still wins even against the oracle, 166 of 179 against 157, so nothing
here argues for replacing it. And FAP is where TNTBLAST fails even with its own cut (21
wrong of 70, against the penalty rule's 6) — a degenerate pan-family consensus assay,
which is the shape this registry holds most of and the shape a Tm calculated from one
resolved oligo describes worst.

Rosetta 2 and the `tntblast` env are machine-local state, like the launchd job: the
environment cannot go in `environment.yml`, because an osx-64 package would make the
project env unsolvable on arm64 for everyone else. The two commands above are the whole
of it.
