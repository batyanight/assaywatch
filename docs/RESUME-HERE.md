# Resume point, 2026-10-18 (scope_taxids end-to-end, 14→9 disagreements)

Everything described here is on `main` at `0a3802c`, working tree clean. This file is the
short version of where to pick up. Verify claims against the repo (`git log`, `results/`
dates, `python -m assaywatch.validate registry`) before acting on them; it goes stale fast.

## scope_taxids: DONE end-to-end (2026-10-18)

`scope_taxids` is an optional field on `Target` in the registry schema. When set, only records
whose taxid is in the list count toward the drift denominator. Out-of-scope records are excluded
and tallied in `AssayDrift.out_of_scope`. Records with no taxid are kept (conservative). This is
exact-match v1 — no NCBI taxonomy ancestry expansion yet.

Code touches: `schema.py` (field), `drift.py` (filtering + counter), `report.py` (scope_map
construction + out_of_scope rendering), `retrospective.py` (builds scope_map from registry
YAMLs). Four new tests in `test_drift.py`.

**Completed 2026-10-18:**

1. ~~Populate `scope_taxids` in 10 assay YAMLs.~~ DONE (`0a3802c`). Species-rank taxids from
   NCBI taxonomy subtree queries via `scripts/populate_scope_taxids.sh`. Counts: Coronaviridae
   1494, Adenoviridae 769, Polyomaviridae 424, Paramyxoviridae 931, Enterovirus 520, CDV 1
   (species-level, used directly). **Three assays got placeholder taxids** (parent only):
   Orthoflavivirus (11051) and Orthoherpesviridae (10292) returned 0 species from NCBI —
   likely ICTV reclassification; investigate with `esearch` on the Mac.
2. ~~Wire `retrospective.py` to build scope_map from registry.~~ DONE (`62cbdc4`).
3. ~~Re-run retrospective with scope.~~ DONE. Disagreements dropped from **14 to 9**. Five
   removed by scope filtering. Remaining 9: 2 non-scope (Chytrid, Influenza — taxid-resolution
   ceiling), 7 genuine calibration signals.
4. ~~Add out_of_scope counts to report rendering.~~ DONE (`62cbdc4`). Markdown and HTML
   reporters show "Out of scope: N records excluded (taxid not in scope_taxids)."
5. **Later:** ancestry expansion for scope_taxids; sequence-cluster lineages (2 remaining FNs).

## The estimand: implemented and recalibrated

The lineage-conditional estimand is live. Per-lineage detection analysis groups records by
NCBI taxid, runs a one-sided binomial test per lineage, applies Benjamini-Hochberg FDR
correction, and overrides a pooled stable/watch to declining when the worst assessable lineage
fails. Design: `docs/2026-10-17-estimand-plan.md`. Implementation:
`docs/2026-10-18-phase2-handoff.md`. The import is lazy (scipy/statsmodels stay optional for
rules that don't use lineage analysis).

Recalibration (`docs/2026-10-18-recalibration.md`, run 2026-10-18) against 50 validation
cases: the tool now catches **6 of 12** documented failures (was 1 of 12). After scope_taxids
population, **9 disagree** (was 14) — a 27% error rate (was 42%). The 5 resolved disagreements
were pan-family scope cases removed by scope filtering. The remaining 9:

- **7 are pan-family scope** — scope_taxids resolved the clearest cases; the remaining ones
  need either ancestry expansion, broader taxid lists, or are genuinely ambiguous.
- **2 are taxid-resolution ceiling** — Bd haplotypes and influenza subtypes share a taxid, so
  per-lineage analysis cannot see the within-taxid divergence. Fix: sequence-cluster lineages
  (phase 2 future work).

**No threshold change.** The errors are in what the tool measures, not where it draws the line.

The ranked work list from the 2026-10-09 assessment, updated:

1. ~~**Lineage-conditional verdicts.**~~ DONE (2026-10-18). 6 of 12 failures caught.
2. ~~**Pan-family scope logic.**~~ DONE (2026-10-18). Code + registry populated. 14→9 disagreements.
3. Homology-anchored footprint scoring, so the duplication check sees clade structure and not
   only identical footprints.
4. Serial scoring logic (nested rounds now have a joint-coverage table, see below; the same
   idea applies wherever one reaction feeds another).
5. **Sequence-cluster lineages** (phase 2 of the estimand). Would resolve the 2 FNs where
   lineages share a taxid (Bd, influenza).
6. Treat the validation set with caution: re-check each case's `as_of` date and expected
   outcome before using it to fit anything.

## The post-PR#1 rescreen is done — do not run it again on this file's say-so

It ran 2026-10-15, finishing 13:40, and its output is `results/2026-10-15/` (`calls.tsv.gz`,
`report.md`, `report.html`). `results/` is gitignored, so it exists only on the laptop: a clean
checkout elsewhere has no run at all, which is the one case where rerunning is right.

The gap against the estimate, which is what the previous edition asked for and nobody recorded.
The estimate came from re-filtering the 2026-10-07 calls at `declared_tolerance: 0.25` rather
than from a run, and lived in this file (the README carries the row-level half of it — 59,141
rows to `no_amplicon`, 54,966 of them former `fail` — but not the status counts):

| | estimate | 2026-10-15 actual |
|---|---|---|
| declining | 22 | **20** |
| stable | 73 | **69** |

Directionally right, mildly optimistic at both ends: four assays it placed in `stable` did not
arrive there. The full run is 213 assays — 20 declining, 58 low coverage, 11 watch, 41
insufficient data, 14 no recent data, 69 stable. The gap was not chased down. A re-filter of
2026-10-07 calls cannot see records retrieved on the eight days between the two dates, which is
the obvious candidate, but nobody has checked whether those four assays are the ones that
gained records — do that before reading the gap as anything else.

When a run *is* needed:

    caffeinate -i snakemake --cores 4 --config email=nightb02@nyu.edu

**Never the `--touch` shortcut from the 2026-10-06 note** across a scoring change; it marks
every screen current at the old setting with nothing to say so. A dry run (`snakemake -n`) is
no check either: it lists the screening jobs only once today's retrieval record exists, and
before that it plans just `validate` and `retrieve`, which needs the network.

## What landed 2026-10-07 to 2026-10-15

- **Mycobacterium** (`f319917`, `bf829bc`): three assays were screening nothing; now
  gene-scoped queries plus genomes via assemblies, and they produce call rows.
- **Nosema** (`68c466b`, `d8a63d2`): *N. ceranae* 218MITOC and *N. apis* 321APIS entered from
  the paper that prints them (Higes 2007 traced as the source).
- **Packaging and docs** (`20d8144`, `2502199`, `5dec3f2`, `8246eb6`, `82471db`, `3bdf993`):
  MIT licence, CITATION.cff, installation doc, offline worked example, `requests` as a core
  dependency.
- **Window archives** (`9acec03`, `assaywatch/windows.py`): records cut to the stretches around
  every possible pair plus 300 bp, so the data can ship (~160 MB vs 6.6 GB). A window is scored
  on its source record's length via a `.windows.tsv.gz` sidecar; without it, the length-scaled
  pair E-value let chance pairs through (71 of 6,356 rows flipped in the 10292 group).
- **Declared amplicon size enforced** (`b08a46a`): `declared_tolerance: 0.25`, chosen from
  the knee of |observed/declared - 1|. 13 entries that declared no size got a measured one
  (flagged `AMPLICON_BP_MEASURED_NOT_PUBLISHED`), 8 left unset; see
  `docs/2026-10-14-amplicon-sizes-measured.md`. A mistranscribed `amplicon_bp` now voids an
  assay's calls, so run `scripts/check_amplicons.py` when an assay's numbers collapse.
- **Nested protocols** (`b08a46a`, `assaywatch/nested.py`): the report adds each nested
  family's joint coverage (both rounds succeed) beside each round's own share. Lyssavirus N
  round 2 reads 99.5% alone, 32.4% as a nest. Statuses unchanged. Three families fail the
  containment check; the coronavirus RdRp "rounds" are disjoint and are really two assays.
  Three entries were split into one entry per round (adenovirus, Cryptosporidium 18S,
  orthoreovirus).
- **Report honesty** (`b08a46a`): `drift.require_working_baseline` moves assays that never
  cleared the threshold from `declining` to `low coverage` (14 of 37 on 2026-10-07); the
  duplication result is printed at the top; an `entry` column shows draft status.
- **`scripts/storage_report.py`**: measures disk use and what is safe to delete. Never delete
  `data/retrieved/` archives or `.meta.tsv.gz`; they cannot be re-fetched.

## State

| | |
|---|---|
| registry | **217 valid, 0 problems**: 213 draft, 3 deprecated, 1 active (`python -m assaywatch.validate registry` prints current counts) |
| chemistry | conventional 170, hydrolysis probe 22, MGB 22, SYBR 2, RPA 1; 44 with a probe, 173 primers only |
| tests | 1205 passed, 11 skipped (primer3-py absent); ruff clean; 182 citations, 0 Crossref problems |
| validation | **50 cases** (32 `works`, 12 `fails`, 6 `partial`); catches **6 of 12** documented failures; **9 disagreements** (was 14 before scope_taxids, 1/12 before lineage estimand) |
| last full run | **2026-10-18**, with lineage estimand active; 213 assays — 66 stable, 63 declining, 12 watch, 17 low coverage, 41 insufficient data, 14 no recent data |

Verified against the repo 2026-10-18.

## Why the remaining work wants the local machine

`papers/` is gitignored (copyrighted PDFs), and cloud sessions are denied
`eutils.ncbi.nlm.nih.gov`, `www.ebi.ac.uk`, `api.crossref.org`, `api.unpaywall.org` and
`api.openalex.org`, so they cannot measure `amplicon_bp`, verify a DOI or retrieve. A cloud
session can read and review code, and PubMed/PMC through an MCP tool. Full write-up:
`docs/2026-10-05-cloud-session-findings.md`.

## The NCBI API key

Set it in ONE place and every caller picks it up. Resolution order, first hit wins:

1. `$NCBI_API_KEY`
2. `.secrets/ncbi.key` (gitignored, so it cannot be committed by accident)

Check it took, without printing it:

    python -m assaywatch.credentials

and, to also ask NCBI whether it accepts the key:

    python -m assaywatch.credentials --check

**`--check` has never been run against the real NCBI**: this environment cannot reach it. It
is tested against fake responses and against a local HTTP server standing in for NCBI, which
exercises the real urllib path but not NCBI's actual answer. Run it once on your laptop; if it
reports anything other than "accepted", paste me the output (it never contains the key).

In a cloud session, add `NCBI_API_KEY` under the environment's settings rather than writing
the file - that is the only route where the key never touches a filesystem, a chat window or a
diff, which is why the environment wins over the file. A new session picks it up.

It is a rate limit, not authentication: 3 requests per second without it, 10 with. Everything
works unkeyed, three times slower. The E-utilities scripts take their sleep interval from
`assaywatch/credentials.py`; the pipeline's two transports keep their own numbers (the same
0.11/0.34 for E-utilities, and Datasets' own 0.11/0.21), and a test ties them to the shared
values. A key that is unusable (more than one line, control characters from UTF-16 or UTF-32
without a byte-order mark, an empty or unreadable file) is ignored with a reason, in the
environment as in the file, and never sent. The key travels in the query string of the
E-utilities GET requests, so exception text from `requests` would contain it; every place that
prints a request error or an error body now scrubs it first (before truncating, since a key cut
in half by a 200-character limit would otherwise survive), and tests drive each of them against
a server that echoes the key back.

## Flagged decisions (from the 2026-10-06 agents, awaiting user judgment)

Resolved since: the LeHV-5 `_evagreen` duplicate was dropped (`a8d4742`), and *N. ceranae* is
entered from Higes 2007's 218MITOC pair (`d8a63d2`).

**Herpesviruses:**
- EEHV6 round2: rests on 1 spanning record (flag `SINGLE_SPANNING_RECORD`). Keep or delete?

**Bees/bumblebee/reptile:**
- *Nosema bombi*: keep under Kato's DOI or move to Klee 2006 (not local)?
- DWV-A/-B: use variant-node taxids or species taxid? (80% of records unlabeled; flagged `VARIANT_SCOPE`)
- Reptarenavirus: multiplex as one pooled entry? S-segment-only query or broaden?

**Mixed (Tsukamoto, Baek, Haynes, Meyer):**
- Ophidiomyces target-D: panel member as species marker. Keep (as entered) or delete?
- Orthopoxvirus ATI: differentiation assay, size 540–1700 bp by species. Keep (as entered) or delete?
  (2026-10-14: its products are genuinely multimodal, so it was left without a declared size and
  is exempt from `declared_tolerance`; constraining it would need a per-entry range.)
- Tasman-PCR (Kwon): transmissible cancer, host-genome. In scope? (4 ready drafts in scratchpad.)
- Clade/lineage scoping: H5, H7, NP, hummingbird avipox. Add scoping or flag for review?

**Bacteria:**
- Chlamydia genus 16S round1: printed primer has T where all records have A. Enter as printed (hypothesis) or correct?
- *C. trachomatis* serovar polymorphism: three serovars have mismatches. Flag, scope, or accept reduced detection?
- *C. psittaci* and *C. abortus*: cross-reaction detected. Note or narrow scope?
- *M. gallisepticum* vaccine pairs: exact on own genomes, >90% non-detect under species taxid. Enter if strain scoping added?

## Also on the laptop (open since 2026-10-06)

**1. Re-run the verifier over the full local `papers/` with the new probe floor.** The reader and the verdict logic
changed in ways that move its answers, and the probe floor is now separate, so some 13-14 nt probes that read `in-text` before will now read `exact`:

    python scripts/verify_oligos_against_paper.py --pdf-dir papers --tsv results/oligo-verification.tsv

Expect a chunk of the 65 known `absent` rows - particularly the image-table papers, *M. bovis*,
Usutu, *Batrachochytrium* ITS - to move to `no-oligos`. They were never evidence about a
sequence. Expect some `in-text` rows to become `exact`, and any entry whose paper writes
`(N/I)` or a similar "X or inosine" notation inside a sequence to move.

**2. Check the new reader against your 60 PDFs, not just my 21 texts.** The composition rule in
`printed_oligos` was calibrated against all 357 registry oligos as written, each placed in a
one-line sentence, and against the 21 open-access texts. Neither is a real PDF's layout. On the
21, comparing the current reader with the one in `826a905` finds 21 identical papers, and the
composition rule alone (`--extractor-only`, which gives both versions the same reading) against
`50430bb` loses nothing and gains four oligos: two degenerate Atkins 2009 primers, the Quan 2010
reverse consensus primer, and a Prepens 2007 primer. (`--extractor-only` excludes the
`(N/I)` reading change by design, so the Prepens gain is the composition rule, not the notation.)

    python scripts/diff_printed_oligos.py --papers papers --old-rev 826a905
    python scripts/diff_printed_oligos.py --papers papers --old-rev 50430bb --extractor-only --fail-on-loss

It reads each paper with the old and the new reader, taking the old script straight from git, and
lists oligos LOST and GAINED. Read the lost ones first. `--fail-on-loss` exits 1 on a loss and 2
if nothing was compared, since an empty comparison proves nothing. If anything is lost on a real
PDF, send me the file name and the sequence, and the threshold gets fixed before the verdicts are
trusted.

## Then, in value order

0. ~~**The lineage-conditional estimand.**~~ **DONE (2026-10-18).** Design:
   `docs/2026-10-17-estimand-plan.md`. Implementation: `docs/2026-10-18-phase2-handoff.md`.
   Recalibration: `docs/2026-10-18-recalibration.md`. Catches 6 of 12 documented failures.
   Remaining disagreements are structural (pan-family scope and taxid resolution), not threshold.
   **Pan-family scope logic code done (`24ca7a7`); populate registry on Mac.**
1. **Nested families — mostly DONE 2026-10-17, see `docs/2026-10-17-nested-family-key.md`.**
   The id base was not a sufficient family key, and it had manufactured two of the three
   "non-nesting" findings: the coronavirus RdRp rounds are a real nest (6,667 of the 6,671
   records both rounds can be judged on), and so are both CMV gB nests once each paper's own
   rounds are paired. **The report's claim that the coronavirus rounds are "two assays, not
   two rounds" is withdrawn.** `source.nested_family` now declares membership; registry
   families 23 → 27, of which those with per-record data 21 → 24; unpaired 15 → 3; failing
   containment 3 → 1, then → **0**: the last survivor, the enterovirus pair, failed on the
   criterion rather than on biology. Its rounds share their reverse SITE and round 2's primer
   is 8 nt longer at the 5' end, so its amplicon ended 8 bp past round 1's while priming from
   the same base. Containment now asks whether the inner primers' **3' ends** lie inside the
   outer product. All 26 families with per-record data nest; nothing fails. Treat that with
   suspicion rather than satisfaction — the check has so far caught two bookkeeping faults and
   one error of its own, and no protocol error.

   Also settled 2026-10-17: the two **Hantavirus** nests declared from geometry and a shared
   reverse primer (A = 250 + 236, B = 532 + 417, all four flagged
   `NESTED_FAMILY_FROM_GEOMETRY`; nest B shows a 27-point nest gap, 44.8% → 17.6%);
   **EEHV6 round 2 kept** with its `SINGLE_SPANNING_RECORD` flag; and **ATI** given
   `amplicon_bp_range: [540, 1700]` via a new optional schema field. Note that range is
   540–1700, *not* the 1067/1535/1538 in earlier notes — those are monkeypox clade modes only.

   Left over: EEHV6's round 1 is still not in the registry (needs Latimer 2010); the
   Hantavirus assignment has no source; and round order for five outer rounds rests on
   declared product size rather than a protocol.

   **Two re-runs owed.** `results/2026-10-15/report.md` still shows the old nested table and
   the withdrawn coronavirus sentence, so it needs a re-render; and the ATI range is a
   *scoring* change (window 50–3000 → 405–2125 bp), so that one assay's calls are stale until
   it is rescreened. Nothing else here touches a call.
2. **Flagged decisions — nine settled 2026-10-17, see `docs/2026-10-17-flagged-decisions.md`.**
   Bacteria: Chlamydia genus primer KEPT as printed (PMC finds that form in two later wet studies
   and the corrected form in none — the defect is the penalty table, not the sequence); C.
   trachomatis serovar split ACCEPTED as a true finding; psittaci/abortus cross-reaction NOTED only;
   the three M. gallisepticum vaccine pairs HELD. Then: PANPOX pair re-scoped to measured GC genera
   (**both now need re-retrieval and rescreen**); Nosema bombi re-cited to Klee 2006
   (`10.1016/j.jip.2005.10.012`, in the Crossref cache; **run `scripts/resolve_citations.py` to flip
   doi_verified**); Ophidiomyces target-D KEPT; Tasman-PCR ruled OUT OF SCOPE.
   Still open: ~~Reptarenavirus winning-pair column~~ **DONE** (2026-10-18): `oligo_pool_names()`
   returns `{seq: name}` maps, `screen_record()` stores `extra["winning_pair"]` as `"F6/R2"`,
   `Call.as_row()` emits the column (empty for non-pool assays). Three tests added. The
   ORTHOBUNYAVIRUS Cac serogroup enumeration; and five entries (Bd BdCAPE/BdGPL, hummingbird
   avipox, DWV-A, DWV-B) whose denominators provably cannot be defined from NCBI metadata and so
   wait on phase-2 clustering. **`DWVA_polyprotein_Rossi_2024` sits in the Declining list on 28
   records drawn from the 16% of DWV that carries a variant label — treat that call as unsafe.**
   CROSSREF IS REACHABLE from the sandbox (checked 2026-10-17), which unblocks items 4 and 5 below.
3. **Settle the coronavirus finding.**
   `CORONAVIRUS_..._Lan_2010_round1` stores a reverse primer 3 nt shorter than the one Quan et
   al. 2010 prints (`...GCNACATG` against `...GCNACNACATG`). The stored form matches PREDICT
   P-005, so two published sources disagree and the sequence was deliberately left alone. Read
   the P-005 table in the Anthony et al. 2015 supplement, screen both forms against real RdRp
   records, then fix whichever is wrong - and check the other P-005 entries for the same
   deletion. This is the second PREDICT-vs-cited-paper mismatch after Atkins/PREDICT.
4. **Measure the two CMV gB amplicons, then re-cite the 4007/4125 pair.**
   - `..._Virol_2007_round1` and `..._round2` hold Prepens' own CM-gB pairs and verify exact.
     Prepens gives two different numbers for round 1 - 330 in Table 3 (footnoted "approximate
     values") and 320 in its Figure 1 legend, which does not name the primer set (250 appears
     in Table 3 only for CM-gB round 2, so reading the legend as this pair is an inference) -
     and 250 for round 2 in both places. The stored 320 agrees with the figure if it describes
     this pair, and the stored 230 agrees with neither, so these are not one spreadsheet error,
     and "correct both to 330" would overwrite a value the paper's own figure supports. Run both
     pairs against real UL55 records and store what they measure.
   - `CMV_specific_HERPES_UL55_Glycoprotein_B_gB` (4007-s/4007-as) and `..._round2_2`
     (4125-s/4125-as) are **not in Prepens**, and their source is now known: Deckers et al.
     2009, *Virol J* 6:210 (PMID 19941648, PMC2789067), Table 1, primer set CMV-gBp1, where 4007
     is round 1 (800 bp) and 4125 is round 2 (550 bp) of one nested assay. Three of the four
     stored sequences match exactly; 4125-s has N where the paper prints B-or-inosine at one
     position, which is a defensible reading since inosine pairs with any base. The DOI
     `10.1186/1743-422X-6-210` came from PubMed, not Crossref, so it is NOT written into
     `citation.doi`. When Crossref is reachable: verify it (`scripts/resolve_citations.py`),
     re-cite both entries together, decide `oligos_designed_here` from what Deckers says (it
     says the primers were designed to bind conserved sites, but cites an earlier use in great
     apes), and clear the flag. Details are in each entry's `notes_curator`.
5. **DOIs: the 2026-10-05 candidate list is CLOSED (2026-10-17).** All five candidates in
   `docs/2026-10-05-doi-candidates.md` plus the two Wang 1997 entries are applied and
   Crossref-verified; `check_citations.py` reports 182 checked, 0 problems. Also finished that
   day: Nosema bombi re-cited to Klee 2006 and both CMV gB 4007/4125 entries to Deckers 2009
   (`10.1186/1743-422X-6-210`), all verified through `resolve_citations.py`.
   **Only the Müller 2011 CDV quartet remains, and the sequence route is exhausted**: all eight
   walking primers were searched in NCBI PMC full text on both strands (a different index from
   the earlier Europe PMC pass), and the single hit is a 2015 paper that designed its primers de
   novo with Primer 3. It needs the paper or the lab's records, not another search.
   35 entries still carry no DOI; most are genuinely unpublished in-house assays.
6. **4 image-only primer tables**: M. bovis (`10.1371/journal.pone.0207365`), Usutu
   (`10.2807/1560-7917.es.2020.25.41.2001732`), Batrachochytrium ITS (`10.3390/jof7040258`, but
   see below), avian orthobornavirus done already. Render with pymupdf at ~200 dpi and read the
   page as an image, as was done for Ghosh - that worked and the sequences verified against
   records afterwards.
7. **211 oligos** whose provenance is unchecked for want of full text.
8. **`POLYOMAVIRUS_dsDNA_PREDICT_VP1_round1` is called `fail` on every product it forms**
   (2,074 records, ~1,000-1,100 bp, all 5'-half mismatches with intact 3' ends). Not dead, as
   first reported: see the correction in `docs/2026-10-14-amplicon-sizes-measured.md`. A test
   case for conventional-PCR scoring under `scoring.by_chemistry`.
9. **Primer-name audit against published papers.** The `name` fields on oligos (forward, reverse,
   probe, alternates) should match the names used in the cited paper's primer table when possible.
   Some registry entries were bulk-imported from a spreadsheet and carry generic or abbreviated
   names. Audit each entry's oligo names against the paper's own table (PDF or full text) and
   correct mismatches. Low priority but improves traceability, especially now that `winning_pair`
   surfaces oligo names in the calls output.

## Two things waiting on someone else

- **Elsevier institutional token.** The API key works (Scopus returns results); full text 403s
  with "Requestor configuration settings insufficient". That is a separate entitlement and the
  VPN does not change it. Ask NYU Libraries for an institutional token for the ScienceDirect
  Article Retrieval API; drop it in `.secrets/elsevier.insttoken` and `scripts/fetch_elsevier.py`
  will use it with no other change. Unlocks 12 papers / 42 oligos. Note: one Elsevier paper on
  that list, EEHV pol (`10.1016/j.vetmic.2010.05.042`), has an author manuscript in PMC
  (`PMC2976818`) and is already recoverable without the token - though its primer table is among
  the ones PMC loses.
- **The rest of the fetch list**, `results/nyu-fetch-list.tsv`, ranked by oligos at stake.
  Browser automation is a dead end for these: ScienceDirect blocks on User-Agent (CPE00001) and
  SAGE sits behind a Cloudflare human check.

## Already known, do not re-litigate

- `jof7040258` publishes NO new primers - it compares Blooi 2013 (already in the registry)
  against Spitzen-van der Sluijs 2020. It belongs in `docs/validation-cases.tsv`, not
  `registry/`.
- Composite entries, each needing its scope read from a different paper than the one cited:
  Hellgren/Bensch, Blooi/Martel, Atkins/PREDICT, and now the CMV 4007/4125 pair. Lan/Quan is a
  related case (the panel's oligo is not the cited paper's).
- The VPN does not fix the Elsevier 403.
- **`10.1111/1755-0998.13299` (Ghosh 2021) is still a read-by-eye job.** Its PMC full text is
  available and its narrative is intact, but the primer table is not in it - the text carries no
  sequences and not one `5′` mark. The PDF is the only route to it.
- **The avipox 1R primer is missing from the PMC text because its parenthetical is empty in the
  Methods sentence**, not because PMC dropped a table (the paper's tables hold Ct values only);
  whether PMC's own XML or the flattening we read lost it is not established. The verifier now
  reads that as `no-oligos`. The entry is sound: an invariant 250 bp product across six
  independent records with the probe site present in all six cannot come from a wrong reverse
  primer.
- **ASM deposits abstracts only**, and so do PNAS and SAGE here. J Clin Microbiol, J Virol and
  Appl Environ Microbiol return an empty body from PMC; mBio, born open access, returns whole, so
  the `10.1128` prefix does not predict it - the journal does. **23 of the 44 papers resolved to
  a PMC id came back as an abstract**, listed with their oligo counts in
  `docs/2026-10-05-pmc-abstract-only.tsv`: 74 oligos across 20 registry papers, plus 3 List 2
  candidates. 21 of the 23 are ASM, so one fetch run on the NYU subscription clears nearly all of
  it. Do not retry them against PMC.
