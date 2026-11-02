# A second bench panel: Rebelo 2011 pan-Mycoplasma, and the scorer agrees (2026-10-20)

`docs/journal/2026-10-19-fap-bench-panel.md` found the FAP59/64 scorer failing 14 of 60 HPV
types the design paper amplified, almost all on G·T wobbles near the 3' end, and said
the next step was more panels. This is the second one. Panel:
`docs/bench-panels/rebelo-2011-mycoplasma.tsv`. Script: `scripts/bench_panel.py`.
Current `config.yaml`.

## Result: 8 of 8 species amplify, no false fails

Rebelo et al. 2011 reports that all 10 Mycoplasma reference strains in its panel
amplified ("All 10 Mycoplasma reference strains tested generated HRM profiles with
2 melting peaks"). Scored against one GenBank record per species:

| bench | detect | reduced | fail |
|---|---:|---:|---:|
| band (8) | 7 | 1 | 0 |

**No disagreements, and not one mismatch inside the 3' window** on either oligo
across all 8 species. The one `reduced` is *M. iowae* (U29676.1) at penalty 3.0,
from three mismatches per oligo, all of them 11 or more bases from the 3' end
(forward 19,16,12; reverse 25,19,11). Those are the cheap positions, 0.5 each, and
the call sits exactly on `reduced_max`; the paper amplified it.

## Why this matters for the FAP finding

It is the control the FAP panel needed. If the 3'-window penalty were simply too
harsh in general, this panel would have produced false fails too: these are
degenerate consensus primers (Y, W) against a genus spanning wide 16S-23S
divergence. It produced none. So FAP's 14 false fails are not a generic
over-strictness — they trace to a specific combination, a heavily degenerate
inosine-containing pair whose W positions sit opposite template G 2-5 nt from the
3' end, which the position-only score charges at full rate.

That makes the case for mispair-identity-aware penalties narrower and better
founded than one panel could show: the change needs to move T:G and the degenerate
pools containing it, and it must leave assays like this one alone, which it would,
because nothing here lands in the 3' window at all.

## Two species cannot be assessed at all

*M. spumans* and *M. canadense* were on Rebelo's bench but have **no GenBank record
spanning the 16S-23S spacer** (checked 2026-10-20: no complete genome, and no 16S,
23S or spacer record covering the region). The tool cannot judge this assay against
them at any threshold. That is the archive's gap, not the assay's, and it is the
same shape as the Bd and DWV denominator problems: a sequence-based tool is silent
where nobody has deposited the sequence. Worth remembering when a pan-genus assay
reads `stable` — the species it was never asked about may be missing rather than
covered.

## Candidate panels surveyed

Scanned the 98 local PDFs for inclusivity-panel language. Most design papers do not
report per-strain results in a form that maps to accessions. The ones that do:

- **Rebelo 2011 pan-Mycoplasma** — done, above. 10 named reference species.
- **Rahn 1992 Salmonella invA** (`10.1016/0890-8508(92)90002-f`): 630 strains over
  100+ serovars, 99.4% detected. A large all-band panel, feasible because serovars
  map to RefSeq genomes. **Caveat that matters:** the 4 failures were two
  *S. litchfield* and two *S. senftenberg* strains, and the paper attributes them to
  the **absence of the invA gene**, confirmed by Southern hybridisation — not to
  mismatches. So those `no_band` labels are strain-specific and must not be carried
  onto modern genomes of the same serovars, which do carry invA. In our terms the
  right call for such a strain is `no_amplicon`, not `fail`, which is a distinction
  the panel format cannot currently express.
- **Ibrahim 1992 Yersinia** (`10.1128/jcm.30.8.1942-1947.1992`): a specificity
  panel — which non-target species must *not* amplify, with two *Y. kristensenii*
  strains giving a same-size product. That tests false positives, which this
  pipeline does not screen for at all (it scores only in-scope records), so it needs
  a different question, not a different panel file.

## Next

- Rahn 1992 Salmonella as a third panel, with the gene-absence rows left out or the
  panel format extended to carry a `no_target` label distinct from `no_band`.
- Only then an identity-aware `score_primer`, fitted on the panels together and
  checked on tier-2 before shipping.
