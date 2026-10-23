# Related work and references

Where AssayWatch sits, and the papers the method rests on.

**Provenance of this file.** Every DOI below was resolved against `api.crossref.org`
on 2026-10-23 and the author, year, title and venue recorded here are Crossref's, not
transcribed from memory — the same rule `CLAUDE.md` sets for registry citations. Two
entries carry no DOI and say so. Nothing here has been entered into `registry/`; the
registry's own citations go through `scripts/resolve_citations.py` and
`scripts/check_citations.py` as usual.

## 1. What already exists

In-silico PCR — matching oligos against sequence and counting mismatches — is solved,
and in two cases solved thermodynamically rather than positionally. AssayWatch's
contribution is not the engine.

| tool | what it does | what it does not do |
|---|---|---|
| **PCR_strainer** | Assesses the inclusivity of primer and probe oligos from diagnostic qPCR assays and amplicon schemes against large genome sets. Wraps `thermonucleotideBLAST` (TNTBLAST), so matching is thermodynamic, not a positional penalty table. Installable as `pcr-strainer`. | No curated assay registry; no longitudinal axis; run on demand against a genome set you supply. |
| **Primer Monitor** (NEB) | **Continuous** monitoring: users register primer sets and the service tracks overlapping variants in new GenBank/GISAID sequences and alerts when variation crosses a threshold. The closest thing in existence to AssayWatch's premise. | SARS-CoV-2 and RSV only. Not a registry of published assays — each user registers their own. |
| **ViralPrimer** | Web server monitoring primer efficiency for nucleic-acid amplification tests during outbreaks. | SARS-CoV-2 and Mpox. |
| **PCRv** | Automates in-silico validation of a PCR test against public databases, integrating freely available tools. Defines in-silico sensitivity as the share of hits with <= 1 mismatch per oligo. The paper's own motivation is that database growth and pathogen drift make periodic re-validation necessary; the authors name incremental analysis as future work. | Single assay at a time; no registry; no deposit-year axis. |
| **GoPrime** | **Fits a model** of real-time PCR performance from sequence, rather than asserting a penalty table — a linear model predicting primer/probe performance, developed on foot-and-mouth disease virus. The methodological precedent for calibrating `config.yaml`'s penalties against measured Cq rather than by eye. | One virus; a prediction tool, not a monitor. |
| **openPrimeR** | R/Bioconductor package for designing and evaluating multiplex primer sets. Reports a coverage ratio — the share of template sequences covered — at a chosen mismatch allowance. | Design-oriented; no registry, no time axis, no drift statistic. |

**References**

- Kuchinski KS, Nguyen J, Lee TD, Hickman R, Jassem AN, Hoang LMN, Prystajecky NA,
  Tyson JR. *Assessing oligonucleotide designs from early lab developed PCR diagnostic
  tests for SARS-CoV-2 using the PCR_strainer pipeline.* Journal of Clinical Virology,
  2020. [10.1016/j.jcv.2020.104581](https://doi.org/10.1016/j.jcv.2020.104581).
  Source: <https://github.com/BCCDC-PHL/PCR_strainer>
- Campbell M, Bei Y, Nichols NM, Langhorst BW. *Primer Monitor: an online tool to
  track SARS-CoV-2 variants that may impact primers used in diagnostic assays.*
  New England Biolabs, January 2021. **No peer-reviewed venue and no DOI found**, via
  Crossref or web search on 2026-10-23: this is a vendor application note and should be
  cited as software plus whitepaper, not as a paper.
  Tool: <https://primer-monitor.neb.com/> · Source:
  <https://github.com/nebiolabs/primer_monitor>
- Deutsch L, et al. *ViralPrimer: a web server to monitor viral nucleic acid
  amplification tests' primer efficiency during pandemics, with emphasis on SARS-CoV-2
  and Mpox.* Bioinformatics 40(11), 2024.
  [10.1093/bioinformatics/btae657](https://doi.org/10.1093/bioinformatics/btae657)
- van Weezep E, Kooi EA, van Rijn PA. *PCR diagnostics: In silico validation by an
  automated tool using freely available software programs.* Journal of Virological
  Methods, 2019.
  [10.1016/j.jviromet.2019.05.002](https://doi.org/10.1016/j.jviromet.2019.05.002)
- Howson ELA, et al. *GoPrime: Development of an In Silico Framework to Predict the
  Performance of Real-Time PCR Primers and Probes Using Foot-and-Mouth Disease Virus as
  a Model.* Pathogens 9(4):303, 2020.
  [10.3390/pathogens9040303](https://doi.org/10.3390/pathogens9040303)
- Kreer C, Döring M, Lehnen N, Ercanoglu MS, Gieselmann L, Luca D, Jain K, Schommers P,
  Pfeifer N, Klein F. *openPrimeR for multiplex amplification of highly diverse
  templates.* Journal of Immunological Methods, 2020.
  [10.1016/j.jim.2020.112752](https://doi.org/10.1016/j.jim.2020.112752).
  Preprint: [10.1101/847574](https://doi.org/10.1101/847574)

## 2. Where AssayWatch is different

Three things, and it is worth being precise because only the first two are defensible
today:

1. **A curated registry of published wildlife and One-Health pathogen assays** — 208
   entries with citations verified against Crossref, amplicon sizes measured against
   real records rather than quoted from a gel band, and a controlled vocabulary of
   provenance caveats (`assaywatch/review.py`). Every comparable tool either targets
   one pathogen of pandemic interest or asks the user to supply their own oligos.
   Nothing covers chytrid, ranavirus, *Ophidiomyces*, haemosporidians, or the PREDICT
   consensus panels.
2. **Detection indexed by deposit year**, which makes decay visible as a trend rather
   than as a single pass/fail against today's database. Primer Monitor alerts on
   crossing a threshold; AssayWatch reports the series.
3. **A lineage-conditional estimand.** Designed (`docs/2026-10-17-estimand-plan.md`),
   partly implemented, and the part that reached production is the part that design
   document predicted would be least capable. Not yet a contribution.

## 3. The problem, in the literature

Periodic in-silico re-assessment of established assays is recommended practice and is
almost never done. The canonical demonstration:

- Nagy A, Černíková L, Kunteová K, Dirbáková Z, Thomas SS, Slomka MJ, Dán Á, Varga T,
  Máté M, Jiřincová H, Brown IH. *In silico re-assessment of a diagnostic RT-qPCR assay
  for universal detection of Influenza A viruses.* Scientific Reports, 2019.
  [10.1038/s41598-018-37869-w](https://doi.org/10.1038/s41598-018-37869-w)

  Re-assessing the EU-recommended influenza A RT-qPCR against public sequence confirmed
  high inclusivity for avian, swine and pandemic H1N1 — and found human H3N2 strains
  carrying a probe-interfering mutation **circulating since 2010**, at a fluctuating
  prevalence. This is the paper AssayWatch should be measured against: the same
  analysis, done once, by hand, for one assay. It is also a ready-made tier-2
  validation case and a model for the paper's framing.

- Mutnale MC, Anand S, Eluvathingal LM, Roy JK, Reddy GS, Vasudevan K. *Enzootic frog
  pathogen* Batrachochytrium dendrobatidis *in Asian tropics reveals high ITS haplotype
  diversity and low prevalence.* Scientific Reports, 2018.
  [10.1038/s41598-018-28304-1](https://doi.org/10.1038/s41598-018-28304-1)

  The Bd failure case in `docs/validation-cases.tsv`: 30 GenBank ITS haplotypes with
  TaqMan probe-site mutations and 15 with reverse-primer-site mutations; 33 qPCR
  positives against 119 by nested PCR on the same swabs. The assay AssayWatch was built
  to watch, failing in the way AssayWatch currently cannot see — its records sit in the
  `no_amplicon`/`diverged` pool that the drift denominator excludes.

## 4. The scoring model

Already cited at the penalties in `config.yaml` and in README's "What the scoring rule
assumes about PCR"; repeated here so the reference list is in one place.

- Kwok S, Kellogg DE, McKinney N, Spasic D, Goda L, Levenson C, Sninsky JJ. *Effects of
  primer-template mismatches on the polymerase chain reaction: human immunodeficiency
  virus type 1 model studies.* Nucleic Acids Research 18(4):999, 1990.
  [10.1093/nar/18.4.999](https://doi.org/10.1093/nar/18.4.999)
- Stadhouders R, Pas SD, Anber J, Voermans J, Mes THM, Schutten M. *The effect of
  primer-template mismatches on the detection and quantification of nucleic acids using
  the 5' nuclease assay.* Journal of Molecular Diagnostics 12(1), 2010.
  [10.2353/jmoldx.2010.090035](https://doi.org/10.2353/jmoldx.2010.090035)

  Both establish that mismatch **identity** dominates at the 3' terminus: A:A, A:G, G:A
  and C:C suppress yield by orders of magnitude while T:G, T:C and T:T are nearly free.
  Both measure that effect *at the 3' end*, which is why `docs/2026-10-22-M1-tier2.md`
  scoped the discount to `primer_3prime_window` and why a 5'/mid wobble discount is
  unsupported. Their quantitative tables are the natural **priors** for the identity
  coefficients in `docs/bayesian-scoring-plan.md` C2.

## 5. Statistics

- Wilson EB. *Probable Inference, the Law of Succession, and Statistical Inference.*
  Journal of the American Statistical Association 22(158), 1927.
  [10.1080/01621459.1927.10502953](https://doi.org/10.1080/01621459.1927.10502953)
  — the score interval used by `drift.wilson_interval`.
- Newcombe RG. *Interval estimation for the difference between independent proportions:
  comparison of eleven methods.* Statistics in Medicine 17(8):873–890, 1998.
  [10.1002/(SICI)1097-0258(19980430)17:8<873::AID-SIM779>3.0.CO;2-I](https://doi.org/10.1002/%28SICI%291097-0258%2819980430%2917%3A8%3C873%3A%3AAID-SIM779%3E3.0.CO%3B2-I)
  — method 10 (square-and-add / MOVER-W), used by `drift.newcombe_difference`.
  `tests/test_drift.py` pins both against this paper's worked example.
- Brown LD, Cai TT, DasGupta A. *Interval Estimation for a Binomial Proportion.*
  Statistical Science 16(2), 2001.
  [10.1214/ss/1009213286](https://doi.org/10.1214/ss/1009213286)
  — the standard reference for why the Wald interval is unacceptable near 0 and 1, and
  the citation for replacing `lineage.confidence_interval_wald`. Also gives the
  Jeffreys-prior interval, which is the conjugate Bayesian answer to the same problem.
- Benjamini Y, Hochberg Y. *Controlling the False Discovery Rate: A Practical and
  Powerful Approach to Multiple Testing.* Journal of the Royal Statistical Society
  Series B 57(1), 1995.
  [10.1111/j.2517-6161.1995.tb02031.x](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x)
  — what `lineage.worst_lineage_verdict` currently applies.
- Holm S. *A simple sequentially rejective multiple test procedure.* Scandinavian
  Journal of Statistics 6(2):65–70, 1979. **No Crossref DOI** (checked 2026-10-23);
  JSTOR stable id 4615733. — FWER control, which is what an "any rejected lineage flags
  the assay" rule requires. BH controls the expected *share* of false rejections among
  rejections; it does not control the probability of **at least one**, which is the
  event that decides an assay's status.

## 6. Bayesian alternatives

For the exploration in `docs/bayesian-scoring-plan.md`.

- Gelman A, Hill J, Yajima M. *Why We (Usually) Don't Have to Worry About Multiple
  Comparisons.* Journal of Research on Educational Effectiveness 5(2), 2012.
  [10.1080/19345747.2011.618213](https://doi.org/10.1080/19345747.2011.618213)
  — the argument that partial pooling does the work multiplicity correction exists to
  do. Directly relevant to the 1,512 per-lineage tests a run performs.
- Gelman A, Jakulin A, Grazia Pittau M, Su Y-S. *A weakly informative default prior
  distribution for logistic and other regression models.* The Annals of Applied
  Statistics 2(4), 2008.
  [10.1214/08-AOAS191](https://doi.org/10.1214/08-aoas191)
  — why a small, partly separable logistic fit (the 166 bench-panel rows) needs priors
  rather than maximum likelihood.
- Prentice RL. *Binary Regression Using an Extended Beta-Binomial Distribution, with
  Discussion of Correlation Induced by Covariate Measurement Errors.* Journal of the
  American Statistical Association 81(394), 1986.
  [10.1080/01621459.1986.10478275](https://doi.org/10.1080/01621459.1986.10478275)
  — beta-binomial overdispersion, i.e. estimating the pseudo-replication the footprint
  check currently reports and then ignores.
- Efron B. *Large-Scale Simultaneous Hypothesis Testing.* Journal of the American
  Statistical Association 99(465), 2004.
  [10.1198/016214504000000089](https://doi.org/10.1198/016214504000000089)
  — empirical-Bayes treatment of many simultaneous tests: the deterministic alternative
  to MCMC for a hierarchical lineage layer.

## 7. Regulatory

- U.S. Food and Drug Administration. *Policy for Evaluating Impact of Viral Mutations
  on COVID-19 Tests (Revised).* January 2023, docket FDA-2020-D-0987. Tells molecular
  test developers to align primer/probe sequences against public genome databases
  periodically and to act when mutations "reduce performance by 5% or more from the
  previously established performance" — the external precedent for
  `drift.min_decline: 0.05`, with the two caveats recorded beside that setting in
  `config.yaml`.
