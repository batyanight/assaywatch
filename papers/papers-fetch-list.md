# Fetch list — EMPTY as of 2026-10-28

**Every paper this list asked for is now in `papers/`.** The seven priority rows were
fetched on 2026-10-28 (two of them renamed out of `~/Downloads` into their `doi_stem`
names) and the ten Priority-2 open-access papers came in the same batch. What each one
settled is in `docs/journal/2026-10-28-papers-arrived.md`; the short version:

- **Neill & Seal 1995** — the Hel1 question is settled, the other way: the paper prints a
  3' **G**, so the stored C is a deliberate modification and not a typo fix. Entry
  reflagged `oligos_modified`.
- **10.1016/j.mimet.2008.12.003** — identity CONFIRMED and **not a case**: Süß et al.
  2009 is a synthetic-template mismatch study, not a field report. Recorded instead as a
  prior source in `docs/bayesian-scoring-plan.md`.
- **Tsukamoto 2008** (29 oligos printed) and **Csordas 2004** (12) — neither prints ours.
  Closed on content; no document will change them.

Nothing is waiting on a human and a proxy. The 22 genuinely paywalled papers in
`papers-still-needed-2026-10-24.md` are completeness reading and were never on this list.

The sections below are kept as the record of what was asked for and why.

---

## Priority 1 — ONE LEFT, and the copy on disk is unusable (updated 2026-10-27)

**Mao is done and the question is closed.** `10.1006_viro.1996.8435.pdf` has been in
`papers/` since 2026-10-25 16:00 and nobody re-ran the verifier against it until
2026-10-27. Its Table 2 prints both primers directly — `GACTTGGCCACTTATGAC` and
`GTCTCTGGAGAAGAAGAA`, both 18 nt, byte-identical to the registry — and nowhere prints
a 19-mer. So the 18/19-mer question is settled in the registry's favour at three
transcriptions to one, Stöhr 2015's extra 3' T is an extension a later paper added,
and `RANAVIRUS_dsDNA_Major_capsid_protein_MCP_Johnson_2008` records it. The amplicon
531 bp is unaffected: both forms share the same 5' end.

**Neill & Seal is still open, and a file under its name is NOT a copy of it.**
`10.1016_s0890-8508_95_90962-1.pdf` exists (64 KB, 2026-10-25) and yields 488 words
of front matter with **no nucleotide run of 10 bases or more anywhere in it** — the
primer table is not in the extracted text. So the Hel1 3'-terminal base is exactly as
unverified as it was. A better copy may be saved under the same name: the verifier
indexes on what a file yields, so a readable PDF replacing that one wins the DOI.

| paper | save as | proxy link | what it settles |
|---|---|---|---|
| Neill & Seal 1995, *Mol Cell Probes* 9:33-38 | `10.1016_s0890-8508_95_90962-1.pdf` | [NYU](https://proxy.library.nyu.edu/login?url=https://doi.org/10.1016/S0890-8508(95)90962-1) | the Hel1 3'-terminal base; see the note below, the decision is already taken on measurement |

### The original Priority 1 entry, kept for its reasoning

These are the only two papers in the project whose absence is blocking a question rather than
a completeness read. Both are Elsevier with no PMCID, reconfirmed unreachable via
PMC/PubMed/Wiley on 2026-10-24, and confirmed absent from the ~148-PDF Downloads batch by
content-searching every file for each paper's distinctive primer run. **Two open questions,
one trip through the proxy.**

| paper | save as | proxy link | what it settles |
|---|---|---|---|
| Mao, Hedrick & Chinchar 1997, *Virology* 229:212-220 | `10.1006_viro.1996.8435.pdf` | [NYU](https://proxy.library.nyu.edu/login?url=https://doi.org/10.1006/viro.1996.8435) | The ranavirus MCP reverse: the registry's 18-mer against Stöhr 2015's 19-mer. **The only oligo-identity question still open anywhere in the held-out set.** The registry's form currently stands on two transcriptions to one; this is the design paper and would close it outright. Elsevier's API returns a body-less reply for this DOI — 110 KB of metadata, abstract and references, no sequence anywhere — which is the case that earned the `%PDF`/`<body>` guard in `scripts/fetch_elsevier.py`. |
| Neill & Seal 1995, *Mol Cell Probes* 9:33-38 | `10.1016_s0890-8508_95_90962-1.pdf` | [NYU](https://proxy.library.nyu.edu/login?url=https://doi.org/10.1016/S0890-8508(95)90962-1) | The calicivirus Hel1 3'-terminal base. We hold only an OCR'd Elsevier backfile deposit that puts a spurious space inside **three of its four** printed oligos, so a single-character misread in the fourth is plausible and unverifiable. |

**On Neill & Seal, read this before you fetch it.** The Hel1 question was *decided* on
2026-10-24 without the PDF, on measurement: Kolesnikovas 2017 prints the base as **C**; over
the whole 152,379-record Caliciviridae archive the stored G-form yields **no product in any
record** while the C-form yields **16, every one 357 bp**, exactly the size both papers state.
The entry was corrected G→C, flagged `oligo_sequence_uncertain`, and demoted active→draft.
So the PDF now **confirms or reverses a decision already taken** rather than unblocking one.
If it prints C, the flag comes off and the entry can be reconsidered for active. If it prints
G, the correction stands anyway on the measurement — but then the published primer genuinely
carries a terminal mismatch and that is a different, more interesting finding.

Also note the asymmetry that makes the *other* pair fine: Neill & Seal's RdRp pair Pol1/Pol2,
entered 2026-10-24, comes from the same corrupt deposit, but closing the spurious spaces gives
two 25-mers that match 11 and 19 real records **exactly** and reproduce the paper's stated
520 bp. Exact matches to real records cannot come from a mistranscription, so those two need
no clean PDF. Hel1's disputed base matches nothing, which is the whole difference.

## Priority 2 — ten open papers behind a bot-check or a landing page

All ten are open access per Unpaywall; none needs the proxy. They are completeness and
cross-reactivity reading (List 2), so none can move a stored oligo — **List 1 is complete.**
Details and per-paper reasons are in `papers/papers-still-needed-2026-10-24.md`; the short
version is six publisher bot-checks (Sage ×2, Taylor & Francis, Wiley, Allen Press ×2) and
four landing pages that do not expose their bitstream to a fetcher.

| save as | DOI | link |
|---|---|---|
| `10.1177_1040638715573983.pdf` | 10.1177/1040638715573983 | [Sage](https://journals.sagepub.com/doi/pdf/10.1177/1040638715573983) |
| `10.1006_viro.1998.9207.pdf` | 10.1006/viro.1998.9207 | [doi.org](https://doi.org/10.1006/viro.1998.9207) |
| `10.1080_03079450802216629.pdf` | 10.1080/03079450802216629 | [T&F](https://www.tandfonline.com/doi/pdf/10.1080/03079450802216629) |
| `10.1111_tbed.12607.pdf` | 10.1111/tbed.12607 | [Wiley](https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/tbed.12607) |
| `10.1177_104063870101300610.pdf` | 10.1177/104063870101300610 | [Sage](https://journals.sagepub.com/doi/pdf/10.1177/104063870101300610) |
| `10.3354_dao03239.pdf` | 10.3354/dao03239 | [UCF STARS](https://stars.library.ucf.edu/scopus2015/10380) |
| `10.7589_2013-09-231.pdf` | 10.7589/2013-09-231 | [Allen Press](https://meridian.allenpress.com/jwd/article-pdf/50/4/757/2245647/2013-09-231.pdf) |
| `10.1016_j.vetmic.2012.12.031.pdf` | 10.1016/j.vetmic.2012.12.031 | [DIGITAL.CSIC](http://hdl.handle.net/20.500.12792/3906) |
| `10.1016_j.vetpar.2011.01.038.pdf` | 10.1016/j.vetpar.2011.01.038 | [CONICET](http://hdl.handle.net/11336/95064) |
| `10.7589_2012-07-175.pdf` | 10.7589/2012-07-175 | [Allen Press](https://meridian.allenpress.com/jwd/article-pdf/49/4/1052/2243806/2012-07-175.pdf) |

Four of these are Unpaywall **submittedVersion** — preprints: `10.3354/dao03239`,
`10.1016/j.vetmic.2012.12.031`, `10.1016/j.vetpar.2011.01.038`, and the already-held
Makkonen 2018. A primer table read from a preprint must say so, since it may differ from the
published paper.

## Not on this list

The 22 genuinely paywalled papers in `papers/papers-still-needed-2026-10-24.md` under
"Genuinely paywalled, NYU proxy". They are List 2 as well, and worth a batch through the
proxy only if you are already there for the two in Priority 1.

---

## Retrospective-case identity (2026-10-26) — the concentrated-signal queue

These are the 9 `mismatch`/`redesign` rows of `docs/2026-10-26-retrospective-candidates.tsv`
— the queue's richest rows for a documented FAILURE. `scripts/check_candidate_identity.py`
ran over all 9 and **none could be settled from open-access text**: the two reachable in
Europe PMC do not reprint the registry assay's oligos (see the `why` column), and the rest
have no open PMC copy. So identity needs the PDF and, where the oligos sit in a supplement,
the supplement. This is the resume point's thesis made a measurement: a citing paper names an
assay by citation and rarely reprints its primers.

Fetch into `papers/` under the exact `save as` name, then re-run:

```bash
python scripts/check_candidate_identity.py --queue docs/2026-10-26-retrospective-candidates.tsv \
  --groups mismatch,redesign --tsv results/retro-identity-concentrated-2026-10-26.tsv -v
```

The script prefers a local file over the network, so a PDF in `papers/` is picked up
automatically on the re-run. A `CONFIRMED` verdict is the signal to read the paper's reported
result; only then does a maintainer decide whether it is a `works` or a `fails` case and add a
row to `docs/validation-cases.tsv`.

| group | year | assay (first of a nested pair) | save as | proxy link | why text was not enough |
|---|---|---|---|---|---|
| mismatch | 2009 | `Salmonella_invA_Rahn_1992` | `10.1016_j.mimet.2008.12.003.pdf` | [NYU](https://proxy.library.nyu.edu/login?url=https://doi.org/10.1016/j.mimet.2008.12.003) | No open-access PMC copy. |
| mismatch | 2013 | `INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003` | `10.1016_j.vetmic.2012.11.013.pdf` | [NYU](https://proxy.library.nyu.edu/login?url=https://doi.org/10.1016/j.vetmic.2012.11.013) | No open-access PMC copy. |
| mismatch | 2022 | `ENTEROVIRUS_ssRNA_VP3_VP1` (+round2) | `10.1101_2022.10.06.511205.pdf` | [bioRxiv](https://doi.org/10.1101/2022.10.06.511205) | Preprint, no open PMC copy; a table read from it must be flagged as a preprint. |
| ~~mismatch~~ | 2023 | `INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003` | `10.3390_v15061344.pdf` | **DONE 2026-10-27** | **CLOSED, do not refetch.** PDF held; `check_candidate_identity.py` extracted **0 oligos** from it. The PDF carries no primer table either, so this row is unconfirmable by CONTENT, not by access. |
| ~~mismatch~~ | 2025 | `ENTEROVIRUS_ssRNA_VP3_VP1` (+round2) | `10.1128_jcm.01492-22.pdf` | **DONE 2026-10-27** | **CLOSED, not a case.** PDF held; 6 oligos extracted, none ours. It reprints its own CDC2022 redesign and uses the Nix VP1 standard by citation only, so 224/222/AN88/AN89 are never stated. |
| mismatch | 2026 | `INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003` | `10.64898_2026.02.23.707407.pdf` | [preprint](https://doi.org/10.64898/2026.02.23.707407) | Preprint, no open PMC copy. |
| redesign | 2004 | `E_coli_O157_hlyA_Wang_1997` (+Yersinia) | `10.1111_j.1472-765x.2004.01559.x.pdf` | [NYU](https://proxy.library.nyu.edu/login?url=https://doi.org/10.1111/j.1472-765x.2004.01559.x) | No open-access PMC copy. |
| ~~redesign~~ | 2007 | `Cryptosporidium_18SrDNA_Xiao_1999_round1` (+round2) | `10.1007_s00436-007-0567-y.pdf` | **DONE 2026-10-27** | **CONFIRMED on round2** (both primers verbatim, `exact`), VARIANT on round1 (drop). Reads `works`, not `fails`: its 73.8% is a dilution series on ONE isolate, i.e. sensitivity, and the assay amplified and RFLP-typed cleanly in two independent stocks. See `docs/journal/2026-10-27-leetz-identity-confirmed.md`. |
| redesign | 2008 | `INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003` | `10.1128_jcm.02386-07.pdf` | [NYU](https://proxy.library.nyu.edu/login?url=https://doi.org/10.1128/jcm.02386-07) | In PMC (PMC2546769) but `fullTextXML` returns HTTP 500 persistently; fetch the PDF. |

**Watch the Influenza Matrix rows especially.** The stored reverse (`AIMatrixR`) is a
*redesign* of Spackman's, not a relaxation (two fixed-base substitutions; see the entry's
`needs_review: oligos_modified`). A paper reprinting Spackman's **original** reverse will read
`VARIANT`, correctly — it is testing a different primer from ours, so it is not a case for
this assay however much it cites it.
