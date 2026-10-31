# M1's confirming rescreen: the replay was right to 153 rows in 2.68 million, and the hierarchical layer's first read says the lineages are nothing like independent

2026-10-27, night. The hold on M1 was lifted on the strength of a replay. A replay freezes
candidate selection, so it is priced and not proven until a real screen under the shipped
config agrees with it. Run 4 — the fourth full run of the day, the third to complete — is
that screen: 487 jobs, 2,753,840 call rows, 193 assays (the five Huo 2022 entries screen
for the first time), 1 h 37 min.

## The replay against the real screen

2,679,894 rows appear in both the S4 replay and the real table. They disagree on 110,759,
and **110,606 of those are not scoring disagreements**: they are rows the replay rewrote
`reduced → fail` for probe chemistries, because a replay can express the probe switch only
by rewriting calls, where the shipped pipeline leaves the call as `reduced` and lets
`drift.reduced_not_detected_for` refuse to count it. Same rule, two places to apply it;
72,578 of them are the influenza matrix assay alone.

**Net of that artefact: 153 call disagreements in 2,679,894 rows**, every one in the
pessimistic direction — 143 where the real screen found `detect` and the replay `reduced`,
6 where it found no amplicon at all, 4 `fail → detect`. The real screen finds a better
candidate than a frozen table can see; it never finds a worse one. M1 is confirmed by
screen, not by replay, and the replay boundary's caveat was correct and small.

## What the run says, against run 3

Headline: **193 assays screened: 42 declining, 34 low coverage, 8 watch, 30 insufficient
data, 19 no recent data, 60 stable**, 10 on Start here. Against run 3 (same day, before
M1), 234 assays appear in both and **8 move**:

| from | to | assay |
|---|---|---|
| declining | watch | `CDV_H_gene_Mueller_2011_2` |
| declining | stable | `CDV_H_gene_Mueller_2011_4`, `PARVOVIRUS_ssDNA_VP1_gene_dependovirus`, `RHABDOVIRUS_ssRNA_L_gene_round2` |
| declining | low coverage | `Pan_HERPES_dsDNA_Polymerase_round2` |
| low coverage | stable | `Encephalitozoon_18S_General_Encephalitoz_Muller_1999` |
| low coverage | declining | `ORTHOREOVIRUS_dsRNA_RNA_polymerase_Landolfi_2010_round1`, `RETROVIRUS_RNA_polymerase_SIV_Takehisa_2009` |

Five flags relax and two tighten, with `declining` holding at 42 only because the two
promotions offset the losses. The two promotions are the `require_working_baseline`
mechanism again: a discount lifts an assay's earlier years over the threshold, so its
present shortfall reads as a decline rather than a gap it never covered. Whether those
two are right is a tier-2 question; neither is a tier-2 case.

## The hierarchical layer's first real lines

58 assays carry a fit; most have one lineage, where the line correctly says there is
nothing to shrink across. Where there are several, the fitted concentration is small:

| assay (lineages) | μ | φ | intraclass correlation | worst lineage after shrinkage |
|---|---:|---:|---:|---|
| enterovirus VP3/VP1 round 2 (3) | 27.1% | 0.9 | 0.54 | *Enterovirus alphacoxsackie* 0.2% (raw 0.2% on 1,815) |
| pan-flavivirus NS5 round 1 (10) | 26.9% | 4.0 | 0.20 | *Orthoflavivirus zikaense* 1.3% (raw 0.0% on 77) |
| pan-flavivirus NS5 round 2 (10) | 36.8% | 11.7 | 0.08 | *Orthoflavivirus usutuense* 1.0% (raw 0.0% on 428) |
| circovirus Rep round 2 (3) | 69.2% | 0.3 | 0.78 | *Circovirus goose* 0.3% (raw 0.0% on 63) |

**The first half of the plan's kill test does not fire.** It dies "if the fitted φ implies
no overdispersion (records really are independent)". φ between 0.3 and 11.7 is intraclass
correlation between 0.08 and 0.78: the lineages of a pan-family assay are far more spread
than binomial sampling allows, which is the formal version of what the duplication check
has been saying by hand. The shrinkage itself is visible and modest — a 77-record lineage
at raw 0.0% is pulled to 1.3% with an interval that reaches 4.7%, which is a more honest
number than "0.0% (0.0%–0.0%)" ever was. The second half — "shrinkage removes a documented
catch" — needs tier-2 re-run with the shrunk worst lineage driving the override in place
of the Holm one, and that is a config switch not yet built. It is the next thing C1 needs.
