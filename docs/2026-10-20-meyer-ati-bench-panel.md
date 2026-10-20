# Meyer's own ATI panel: 8 of 9 right, and skunkpox is a false fail (2026-10-20)

Third bench panel, after Forslund FAP (`docs/2026-10-19-fap-bench-panel.md`) and
Rebelo pan-Mycoplasma (`docs/2026-10-20-mycoplasma-bench-panel.md`). This one
answers the question `docs/2026-10-19-orthopox-ati-vaccinia.md` left open: our two
skunkpox records give a 551 bp product but score `fail`, and ATI anneals at 40 °C,
so is that band real?

Panels: `docs/bench-panels/meyer-1997-ati.tsv` (9 species, Meyer's Table 1) and
`docs/bench-panels/meyer-1997-ati-strains.tsv` (2 rows: his exact variola strain,
and monkeypox clade I). Script: `scripts/bench_panel.py`. Current `config.yaml`.

## The paper's claim

Table 1 compares nine orthopoxvirus species, giving a product size for eight and
"No amplification" for raccoonpox, which the text confirms is its only negative.
Read from the scan's OCR layer: variola Bangladesh-1975 1575, monkeypox Copenhagen
1500, cowpox Brighton 1673, vaccinia Western Reserve 1603, ectromelia Munich-1
1219, camelpox CP-1 880, volepox Jasper Ridge 510, raccoonpox Aberdeen-1964 none,
skunkpox Colfax-1978 530. The sizes 1575, 1500, 530, 510 and the 510-1673 range
are repeated in the Discussion and abstract; 1603 and 1219 rest on the table alone,
and the OCR renders a leading 1 as I, so those two are the least certain digits.

## Result

| bench | detect | reduced | fail | no_amplicon |
|---|---:|---:|---:|---:|
| band (8) | 5 | 2 | **1** | 0 |
| no band (1) | 0 | 0 | 0 | 1 |

Counting `detect` and `reduced` as "would show a band", **8 of 9 correct**.
Raccoonpox is right for the right reason: no credible site for either primer, so
`no_amplicon`, which is threshold-independent and consistent with its divergent ATI
protein. It is the one hard negative control this assay has.

## Skunkpox: the `fail` is not real

NC_031038.1 scores 3.5 against a `reduced_max` of 3.0, product 551 bp, and **no
mismatch anywhere in the 3' window** — the 3'-terminal 8 nt of both primers match
exactly. The 3.5 is five cheap mismatches 9-18 nt from the 3' end: forward A:A at
d=13, C:T at 12, A:G at 11 (0.5 each) and G:A at d=9 (1.0, mid window); reverse C:A
at d=18 and A:C at d=15 (0.5 each).

Three reasons to call this a scorer error, not a finding:

1. **Meyer amplified it**, at 530 bp, and names raccoonpox as the only negative.
2. **It is the same isolate.** The only skunkpox genome in GenBank is strain WA,
   collection date 1978, and Colfax is in Washington State. So this is not a
   strain-mismatch artefact.
3. **The geometry cannot abolish a band at 40 °C over 25 cycles.** The cleanest
   demonstration is internal to the panel: volepox and skunkpox share an
   *identical* divergent forward site (`AATTACATGAGGATCT`, same four mismatches,
   2.5), and the only difference is skunkpox's one extra reverse mismatch 15 nt
   from the 3' end of an 18-mer. That single base splits the two New World species
   across the threshold — volepox 3.0 `reduced`, skunkpox 3.5 `fail` — while the
   bench gave both a band.

Variola is the near-miss: exactly 3.0, on one mismatch 3 nt from the 3' end (T:T,
+3.0), identical in the India-1967 RefSeq and in Meyer's own Bangladesh-1975
(L22579.1). A conserved variola feature, and any additional 5'-region mismatch in
an isolate flips it to `fail` — very likely where this assay's variola non-detects
come from.

## What this adds about the scorer, and it is not the FAP knob

FAP's 14 false fails were driven by mispair *identity* inside the 3' window (G·T
wobbles). Meyer's one false fail has **no 3'-window mismatch at all**: it fails on
linear accumulation of 0.5 and 1.0 penalties 9-18 nt out, against `reduced_max: 3.0`.
So an identity-aware `score_primer`, the change the FAP panel argued for, would not
have caught this one. Two independent panels now disagree with the scorer, for two
different reasons:

- FAP: 3'-window penalties should depend on which mispair forms.
- Meyer: either `reduced_max` is too low for conventional endpoint PCR, or 0.5 per
  mismatch should not accumulate linearly that far from the 3' end.
- Rebelo: no disagreement at all, and no 3'-window mismatch anywhere, so neither
  change would disturb it.

Measured counterfactual: with the reverted `conventional` override from the comment
block in `config.yaml` (`terminal_mismatch_fails: false`, `primer_3prime_penalty: 2.0`,
`reduced_max: 5.0`) this panel goes to **9 of 9** — skunkpox `reduced` at 3.5,
variola `reduced` at 2.0, raccoonpox unchanged. The rescue comes entirely from
`reduced_max: 5.0`.

**The honest limit:** this panel cannot test that override in the other direction.
It has one `no_band` species, and raccoonpox has no primer site at all, so no
threshold can wrongly rescue it. The panel shows the override fixes a false fail and
breaks nothing here; it says nothing about false detects. That is the same in-sample
caveat the FAP write-up carries, and it is why `config.yaml` still says not to
uncomment that block without validation behind it. What has changed since it was
reverted is that there are now two independent bench panels contradicting current
`reduced_max`, where before there was only "87 -> 44 drift flags", which measured
nothing.

## `species_sizes` confirmed, and one row added

Every band this panel touches is confirmed against an independent record: cowpox
1673, vaccinia WR 1606 (in the 1587-1615 band), variola 1582 and 1576, camelpox
879, ectromelia 1220, monkeypox clade I 1067 and clade IIb 1545, volepox 542.

The paper-vs-measured discrepancy flagged in `needs_review` is now **resolved as gel
sizing, not isolate difference**, and the flag is removed. The four well-matched
species sit within 3 bp; the three outliers are all round numbers read low (1500 vs
1535-1545, 510 vs 542, 530 vs 551), and for volepox and skunkpox the records scored
*are* Meyer's own isolates, which excludes isolate difference for those two.

**Added:** skunkpox `[551, 551]`, bench-confirmed by Table 1 even though the
pipeline scores it `fail`. Two further fail-scored bands were deliberately left out,
both measured and both instructive:

- **vaccinia 1226 bp** is Modified Vaccinia Ankara — U94848 (the Ankara reference)
  plus MVA-derived constructs. A real strain with a real ATI deletion, but 6 bp from
  the ectromelia 1220 band, so admitting it makes that reading ambiguous without
  naming a new species.
- **camelpox 615 bp** rests entirely on two patent deposits titled "Modified
  Microbial Nucleic Acid", which the patent-title fallback cannot see. This is how
  that 3% blind spot was found; see `assaywatch/metadata.py`.

## Size collisions, measured

The entry's `DIFFERENTIATION_ASSAY_SIZE_AND_XBAI_DIGEST_NOT_SCREENABLE` flag in
numbers. **volepox 542 vs skunkpox 551 is 9 bp**, unresolvable on the paper's
agarose — Meyer's own 510 vs 530 was the same problem, and Fig. 2 runs them as XbaI
digests side by side for exactly this reason. Also: cowpox 1673 equals the
abatinomacacapox band and is 2 bp from a vaccinia band; 1576-1615 is a pile-up of
vaccinia, cowpox, variola and Cowpox-Vaccinia; akhmetapox 1505 equals a cowpox band;
MVA 1226 is 6 bp from ectromelia 1220. Cleanly separable: camelpox 879, monkeypox
clade I 1067, ectromelia 1220, and the ~545 bp New World pair *as a pair*.

## `scripts/measure_species_sizes.py` changes

- **De-duplication.** A RefSeq record is dropped when a non-RefSeq record of the
  same species has the same record length and the same product length — the
  original it copies. Three ATI bands (volepox, skunkpox, taterapox) looked like
  two records when they were one isolate deposited twice. 12 records collapse.
  The rule deliberately does not collapse two non-RefSeq records of equal length:
  doing that cut monkeypox from 12,539 to 4,704, because outbreak genomes share
  lengths without being the same isolate.
- `--min-records` default drops from 2 to 1, which de-duplication makes
  meaningful: after it, the rare species are one isolate each, and `--min-share`
  still keeps a one-off length out of a well-sequenced species.
- **`--include-fail`** counts a `fail`-scored record whose sites span a product,
  on the argument that a length is a property of the template rather than of the
  yield. It is not the default and did not populate the registry: as measured
  above it also admits the MVA band and the patent-derived camelpox band. It
  becomes trustworthy once the `is_patent` backfill exists.
- Each band now prints how its records scored, so a band resting on `fail` calls
  is visible rather than silent.

## Next

- The `is_patent` backfill sidecar, which `--include-fail` waits on.
- A fourth panel with real `no_band` rows that a looser `reduced_max` could wrongly
  rescue. Rahn 1992 Salmonella invA is the candidate, with the caveat recorded in
  `docs/2026-10-20-mycoplasma-bench-panel.md`.
