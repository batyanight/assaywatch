# Rahn's invA panel: 64 of 64 both ways, and the first measured specificity headroom (2026-10-20)

Fourth bench panel with a real negative set, after Forslund FAP
(`docs/2026-10-19-fap-bench-panel.md`), Rebelo pan-Mycoplasma
(`docs/2026-10-20-mycoplasma-bench-panel.md`), Meyer ATI
(`docs/2026-10-20-meyer-ati-bench-panel.md`) and Barrett morbillivirus
(`docs/2026-10-20-scope-curation.md`). Panel:
`docs/bench-panels/rahn-1992-salmonella-invA.tsv`. Script: `scripts/bench_panel.py`,
which gained a `--config` flag here so a counterfactual can be measured without
editing the real `config.yaml`.

It was wanted for one reason: FAP and Barrett both argue the 3'-window penalty should
depend on which mispair forms, and Meyer argues `reduced_max` is too low, and no panel
so far could price the specificity cost of either change. Rahn's Table 2 is 142
non-Salmonella strains across 21 genera, all negative — the first substantial negative
set in the set of panels.

## The registry does not hold Rahn's primers

Found while reading the paper for this panel; the full account is in
`docs/2026-10-20-scope-curation.md`. Table 3 prints `139`
(`gtgaaattatcgccacgttcgggcaa`, invA 287–312) and `141`
(`tcatcgcaccgtcaaaggaacc`, 571–550), both in lower case.
`Salmonella_invA_Rahn_1992` holds the 3'-terminal **19 of 26** nt of 139 and the
3'-terminal **19 of 22** nt of 141. The 3' ends match, so the sites are the same and
the truncation can only lower the penalty an oligo carries. `amplicon_bp: 275` follows
the truncation (285 from Table 3's locations, less the 7 and 3 dropped bases; the text
says 284), and the 2026-10-17 calls measure 275 bp in 467 of 468 detected-or-reduced
records. Flagged `OLIGOS_TRUNCATED_VS_PAPER`, sequences unchanged.

So the panel is scored twice: with the stored pair, which measures the registry, and
with 139/141, which measures the paper's claim.

## Result

23 `band` rows (one RefSeq genome per Salmonella serovar or subspecies) and 41
`no_band` rows (one per non-Salmonella taxon, 20 of Rahn's 21 genera).

| pair | band (23) | no_band (41) | correct |
|---|---|---|---:|
| registry `Sal-3`/`Sal-4` (truncated) | 23 `detect` | 38 `no_amplicon`, 3 `fail` | **64/64** |
| Rahn `139`/`141` (as published) | 22 `detect`, 1 `reduced` | 41 `no_amplicon` | **64/64** |

Both pairs get every row right, and the band side is emphatic: every one of the 20
*S. enterica* subsp. *enterica* serovars scores penalty **0** with the stored pair, and
only the three non-*enterica* subspecies (*salamae*, *arizonae*, *diarizonae*) carry
anything at all, 0.5–1.5. That matches Rahn's 99.4% sensitivity across 630 strains.

## What the negatives can and cannot price

Rahn attributes every negative to the invA gene being **absent**, not to primer
mismatch — for the four Salmonella failures, "the failure to amplify invA homologous
sequences was most likely due to the absence of the invA gene in these Salmonella
strains, since Southern hybridization analysis with a probe containing the whole invA
gene also failed to detect any homology", and the same hybridisation was negative for
every non-Salmonella strain. A gene-absent negative scores `no_amplicon`, which is
threshold-independent, so 38 of the 41 price nothing at all.

**The three that do are the panel's whole value.** With the stored pair, three
non-Salmonella genomes carry a credible pair of sites at a credible spacing and reach
scoring:

| taxon | penalty | 3'-window mispairs |
|---|---:|---|
| *Hafnia alvei* | 10.5 | `fwd4 G:A`, `fwd1 A:G` |
| *Providencia rettgeri* | 11.0 | `rev5 G:G`, `rev1 C:T` |
| *Providencia stuartii* | 13.5 | `fwd4 G:A`, `fwd3 C:C`, `fwd1 A:C` |

These are chance pairings that the `max_pair_evalue` guard and the declared-size filter
let through to the scorer, and the **penalty** is what rejects them. Rahn saw the same
thing on the bench: "Non-specific amplification of a few non-Salmonella strains
resulted in a product that was distinctly different in size."

**With 139/141 all three disappear** — 41 of 41 `no_amplicon`. The seven extra 5' bases
on the forward and three on the reverse make the chance site implausible. So the
truncation has a measured cost even though it changes no call: it manufactures three
spurious candidate amplicons in 41 non-target genomes, and only the penalty margin
stands between them and a false detect.

## The measurement the other panels were waiting for

**Not one of the seven mispairs in those three rows is a G·T or T·G wobble.** They are
G:A, A:G, G:G, C:T, C:C and A:C. So the change FAP and Barrett both argue for — an
identity-aware `score_primer` that stops charging a G·T wobble in the 3' window the
full `primer_3prime_penalty` — has **zero specificity cost on this panel**. That is the
first time the cost side of that knob has been priced against bench negatives rather
than assumed.

Measured counterfactual for the other knob, with the reverted `by_chemistry.conventional`
override (`terminal_mismatch_fails: false`, `primer_3prime_penalty: 2.0`,
`reduced_max: 5.0`, `--config`):

| taxon | current | with the override |
|---|---:|---:|
| *Hafnia alvei* | 10.5 | 8.5 |
| *Providencia rettgeri* | 11.0 | 9.0 |
| *Providencia stuartii* | 13.5 | 10.5 |

Still **64/64**, with the nearest false positive 3.5 points above a `reduced_max` of
5.0. So this panel does not discriminate the reverted override either, but it does fix
a number nobody had: the specificity headroom at the most permissive threshold anyone
has proposed is about 3.5 penalty points.

## Limits

- **No primer-mismatch negatives.** Every true negative here lacks the target gene, so
  the panel cannot show a false detect arising from tolerated mismatches, only one
  arising from a chance pairing. A panel whose negatives carry the gene and diverge at
  the primer sites is still missing, and is what would price the knob properly.
- **The four Salmonella negatives are not representable.** Two *S. litchfield* and two
  *S. senftenberg* isolates failed on gene absence in those specific strains; the
  isolates cannot be identified in GenBank and arbitrary genomes of those serovars
  carry invA. Senftenberg is a `band` row here, 9 of its 11 strains having amplified;
  litchfield is left out at 0 of 2.
- **One genome per taxon** understates within-species variation, and four of Rahn's
  taxa have no RefSeq complete genome at all (*Actinobacillus lignieresii*, *Aeromonas
  sobria*, *Serratia liquefaciens*, *S. enterica* subsp. *houtenae*).
