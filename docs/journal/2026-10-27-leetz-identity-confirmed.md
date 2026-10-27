# The first CONFIRMED retrospective identity, and it is a `works` case

2026-10-27. Three PDFs from the fetch list arrived. Re-running
`scripts/check_candidate_identity.py` over the 9 concentrated
`mismatch`/`redesign` rows of `docs/2026-10-26-retrospective-candidates.tsv`
converted the identity question for the first time since the queue was built.

    python scripts/check_candidate_identity.py \
      --queue docs/2026-10-26-retrospective-candidates.tsv \
      --groups mismatch,redesign -v

13 (paper, assay) pairs over 9 papers: **1 CONFIRMED, 1 VARIANT, 11
UNCONFIRMABLE** (was 0 / 0 / 13).

## What each of the three papers did

| paper | assay | verdict | what it means |
|---|---|---|---|
| Leetz et al. 2007, *Parasitol Res* 101:951-962 (`10.1007/s00436-007-0567-y`) | `Cryptosporidium_18SrDNA_Xiao_1999_round2` | **CONFIRMED** | Both round-2 primers printed verbatim and read `exact` against the registry: `Xiao18SF2` GGAAGGGTTGTATTTATTAGATAAAG, `Xiao18SR2` AAGGAGTAAGGAACAACCTCCA. 42 oligos extracted from the paper. |
| same | `Cryptosporidium_18SrDNA_Xiao_1999_round1` | VARIANT | The round-1 pair it tested is not ours. Drop the row; it is a different primer, however much it cites Xiao 1999. |
| Ng et al. 2025, *J Clin Microbiol* (`10.1128/jcm.01492-22`) | `ENTEROVIRUS_ssRNA_VP3_VP1` (+round2) | UNCONFIRMABLE | The PDF settles the open question **negatively**, as the queue predicted it might: 6 oligos extracted, none ours. The paper reprints its own CDC2022 redesign and uses the Nix VP1 gold standard by citation only, so 224/222/AN88/AN89 are nowhere stated. Not a case for our entry. |
| Slomka et al. 2023, *Viruses* 15:1344 (`10.3390/v15061344`) | `INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003` | UNCONFIRMABLE | **0 oligos extracted from the PDF.** The open XML carried no primer table and neither does the PDF; Spackman is in the references only. Nothing further to fetch for this row -- it is closed as unconfirmable by content, not by access. |

So of the three, one converted, one dropped, and two are now closed on evidence
rather than left waiting on a document. That is worth as much as the conversion:
`papers/papers-fetch-list.md` can stop asking for them.

## The CONFIRMED case reads `works`, and the mechanism is why

The queue's rule is that a CONFIRMED verdict is the signal to read the paper's
reported result, and that whether it is `works` or `fails` is a maintainer's
decision. The reading, with the evidence:

**The headline number looks like a failure and is not one.** Leetz reports
**73.8% positive results** with the Xiao nested 18S primers, against 91.4% for
BCOWP, 88.2% for Chsp4 and 80.6% for the LAX pairs (Table 2). Read against this
project's `detect_fraction_threshold: 0.90` that is a miss.

**But the denominator is a dilution series, not a diversity panel.** Table 2's
positive rate is taken across oocyst concentrations of >10⁴, 10⁴, 10³, 10², 10¹
and 10⁰ of one isolate. The misses are at low template. That is a **sensitivity /
limit-of-detection** property, and this tool does not model it: the whole scoring
rule is about whether oligos still match a sequence, and a primer that matches
perfectly still fails at one oocyst.

**The study is one isolate.** *C. parvum* HNJ-1, genotype II, with a German
bovine stock as a confirmatory second (lines 17, 125, 134 of the extracted text).
There is no clade structure here to fail on.

**And on that isolate the assay worked, twice.** The Xiao round-2 product was
obtained and digested cleanly with Vsp I to 628 + 104 bp, and the procedure was
"repeated with a bovine oocyst stock isolated in Leipzig, Germany with identical
results."

So: **`works`, mechanism blank.** The low detection rate is real and is about
template concentration, which is outside what the registry's `expect` column
means. Recording it as `fails` would teach the retrospective harness that a
sensitivity result is a coverage result, which is precisely the confusion the
`mechanism` column exists to prevent.

## The decision this actually raises

Not whether to write one row, but **where to write it.**

`docs/validation-cases.tsv` is the development set, frozen 2026-10-23, and at
least seven `config.yaml` settings were accepted or rejected against its rows.
The 34-case held-out set was read on 2026-10-26 and is spent. So the project
currently has **no unread evaluation data at all**, which is why the 5/11 figure
cannot be improved on by any amount of tuning.

A case whose identity was confirmed today, from a paper the scoring rule has
never been shown, is the first brick of a *new* held-out set. Putting it into the
frozen development set spends it immediately for one row's worth of in-sample
fit. Starting `docs/validation-cases-heldout-2.tsv` with it costs nothing now and
is worth something later, but only if it stays unread until there are enough rows
to be worth reading once.

Deliberately not done here. It is a judgement about how to spend the project's
scarcest resource, and the asymmetry is bad in one direction: a dev-set row can
never be un-read.

## Still open

> *History, as of 2026-10-27. The live list is `ROADMAP.md`, the only to-do file
> in the repository; anything below that is still open was lifted into it.*

The two Priority 1 papers are **not** among these three and remain the only
oligo-identity questions blocking a decision: Mao, Hedrick & Chinchar 1997
(`10.1006_viro.1996.8435.pdf`, the ranavirus MCP 18-mer/19-mer) and Neill & Seal
1995 (`10.1016_s0890-8508_95_90962-1.pdf`, the calicivirus Hel1 3'-terminal base,
which now confirms or reverses a decision already taken on measurement). Both are
Elsevier, both need the NYU proxy.
