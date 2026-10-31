# A worked example: screening one assay, offline, in a second

This runs AssayWatch's screening step on a small FASTA and shows how to read the
result. It needs no network, no NCBI key and no Snakemake — just the installed
package.

```bash
python examples/make_example_fasta.py
python -m assaywatch.screen \
  registry/CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004.yaml \
  examples/bd-example.fasta \
  -o calls.tsv
```

The assay is **Boyle et al. 2004**'s *Batrachochytrium dendrobatidis* ITS TaqMan
assay, taken from the registry: a 29 nt forward primer, a 22 nt reverse primer, a
15 nt MGB probe and a 146 bp product.

## The records are synthetic, and that is the point

`make_example_fasta.py` builds each record from the assay's **own oligos** — the
146 bp amplicon with one defect introduced — and names it after the defect. They
are not GenBank sequences. Real records give you whichever verdicts those
particular records happen to produce; these are chosen so that every verdict the
screener can reach appears exactly once or twice, so you can see what each one
means.

Nothing here is evidence about the Boyle assay. For that, screen it against
GenBank: see the Snakefile and `docs/` in the repository root.

## What the screen reports

Running the two commands above produces, verbatim:

```
CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004	detect	3
CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004	fail	1
CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004	no_amplicon	3
CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004	reduced	2
```

and `calls.tsv`, one row per (assay, record), of which the interesting columns
are:

| record | call | penalty | amplicon_bp | why |
|---|---|---|---|---|
| `perfect` | `detect` | 0 | 146 | both primers and the probe match exactly |
| `fwd_5prime_mismatch` | `detect` | 0.5 | 146 | mismatch at the forward primer's 5' end, far from where extension starts |
| `probe_mismatch` | `detect` | 1 | 146 | primers match; one mismatch in the probe's outer third |
| `both_primers_mid_mismatch` | `reduced` | 2 | 146 | one mismatch 6–10 nt from the 3' end of *each* primer |
| `probe_centre_mismatch` | `reduced` | 2 | 146 | one mismatch in the probe's central third, where a duplex is least stable |
| `fwd_3prime_mismatch` | `fail` | 3 | 146 | mismatch at the forward primer's **3'-most base** |
| `no_reverse_site` | `no_amplicon` | — | — | the reverse primer's site is replaced, so there is no pair |
| `truncated_inside_amplicon` | `no_amplicon` | — | — | the record ends inside the product: a coverage limit, not a primer failure |
| `unrelated` | `no_amplicon` | — | — | neither primer has a site |

## How to read that

**Position matters more than count.** All three of `fwd_5prime_mismatch`,
`probe_mismatch` and `fwd_3prime_mismatch` carry exactly one mismatch, and they
land on three different verdicts. A polymerase extends from a primer's 3' end, so
a mismatch there obstructs extension itself, while one near the 5' end costs only
a little duplex stability. The weights live in `config.yaml` under `scoring:`,
with the literature behind them — and an explicit note that the shape is
plausible rather than measured.

**`fail` here is not a penalty threshold.** `config.yaml` sets `detect_max: 1.0`
and `reduced_max: 3.0`, so a penalty of exactly 3 would be `reduced`. It reads
`fail` because `terminal_mismatch_fails: true` is a separate rule: any mismatch
at the 3'-most base fails regardless of the total. `fwd_mm_from_3prime` in the
TSV is `1` for that record, which is how you spot it.

**`no_amplicon` is not a failure of the assay.** Three records produce it for
three unrelated reasons — a missing site, a record too short to span the product,
and an irrelevant sequence. Only the first says anything about the assay. This
distinction is why coverage is reported separately from detection: a share
computed over records that cannot physically contain the product would be
meaningless. The pipeline's drift step only counts records that span the site.

**A probe mismatch does not by itself disqualify a call.** `probe_mismatch` is
still `detect`. The probe is scored (`probe_penalty`, `probe_site`) and reported,
but a single mismatch in its outer third is not treated as loss of detection. The
`scoring:` comments flag a known gap here: 13 of the registry's 21 probe assays
are MGB, whose minor-groove binder raises Tm substantially, and the two probe
weights do not know an MGB 15-mer from a bare 32-mer.

## Next

- `python -m assaywatch.screen --help` — `--workers` for large archives, and
  `--thermo` for duplex Tm beside each call (needs primer3-py)
- the repository `Snakefile` — the full retrieve → screen → drift → report
  pipeline against live GenBank, which needs the network and an NCBI key
- `python -m assaywatch.validate registry` — schema-check the registry
