# Resume point, 2026-10-06 (after List 2 entry, schema changes, and key rotation)

Everything described here is on `main` (commit `7a7fdcd`). This file is the short version of where to
pick up.

## After `git pull`: the next run rescreens everything, unless you say otherwise

The pull changes the screening code and the hashes that decide whether a cached screen is
still valid (`score.py`, and a Snakefile that now derives which source files each rule
depends on). Snakemake therefore treats every cached screen as stale and the next run
rescreens all of them. That is correct and slow, and it is the safe default: **if you are
not sure of the precondition below, just run**

    snakemake --cores 4 --config email=nightb02@nyu.edu

**The shortcut, only if you have changed no assay and no setting since your last complete
run** (`git status` showed `registry/` and `config.yaml` clean before you pulled). At the
default config nothing about the screening *result* changed in this pull, so the existing
screens are still right and can be marked current first:

    snakemake $(ls results/screened/*/*/*.tsv) --touch --cores 4 --config email=nightb02@nyu.edu
    snakemake --cores 4 --config email=nightb02@nyu.edu

The targets go BEFORE `--config`, which swallows every argument after it as a `name=value`
pair. The first command marks the existing screens current without recomputing them and
records the new hashes. It touches nothing else, so the second command rebuilds the calls
table, the report and the degeneracy table with the new code, screens any archive that has
no screen yet, and runs retrieval as it always does. Add `run_date=YYYY-MM-DD` to both if
you use it.

Why the precondition matters: `--touch` marks a screen current whatever made it stale. In a
test, changing `terminal_mismatch_fails` and then taking the shortcut left every screen as
the old setting made it, with nothing to say so. If you have edited an assay or a threshold
since the last run, skip the first command.

What was verified, under real Snakemake 9.27.0 in a scratch environment, on a tree built
from the commit you last pulled (`826a905`) and overlaid with this one: the shortcut on a
new day, on the same day, and on the same day with a new archive. In each, the existing
screens were adopted, the second command executed only `collect_calls`, `degeneracy_table`
and `report` (plus `screen_archive` for the new archive alone), and the existing screens and
the calls table's content were identical to the old code's. With a setting changed first, the
same commands adopted the stale screens, which is the precondition above. (An earlier version
of this note gave a different three-command recipe, `--until retrieve`, `--touch`, then run;
a second review showed that on a day when results already exist it never screens a new
archive and leaves the old report in place, and it was withdrawn.)

A dry run (`snakemake -n`) is no check on any of this. It lists the screening jobs only once
today's retrieval record exists; before that it plans just `validate` and `retrieve`, which
needs the network.

## Why the remaining work wants the local machine

`papers/` is gitignored - the PDFs are copyrighted and should stay out of git. A cloud
session clones from git and starts with none of them.

Two cloud sessions have now tested how far that can be worked around. They recovered **21
papers** as open-access PubMed Central full text and got real value out of them, but could
not advance the entry work, for two reasons worth knowing before anyone tries again:

- **No sequence database.** The environment's egress policy denies
  `eutils.ncbi.nlm.nih.gov`, `www.ebi.ac.uk`, `api.crossref.org`, `api.unpaywall.org` and
  `api.openalex.org` (re-tested 2026-10-06: still denied, including after being told the
  network was available). `amplicon_bp` cannot be measured against real records, and
  measuring rather than quoting is the method this registry rests on, so no assay can
  honestly be entered. What *is* reachable is PubMed through an MCP tool: metadata, PMC ids
  and PMC full text.
- **PMC full text often arrives without its primer tables, but not always.** The text comes
  flattened. Prepens 2007 and Deckers 2009 came through with their primer tables readable;
  Quan 2010 and several others did not, and the avipox paper's tables hold only Ct values. Of
  the 44 papers that resolved to a PMC id, 23 came back as an abstract only (ASM, PNAS and
  SAGE deposit abstracts). So expect some sequences from PMC and do not expect all of them.

Full write-up: `docs/2026-10-05-cloud-session-findings.md`, including an addendum of the
statements from the first cloud session that the reviews corrected.

## State

| | |
|---|---|
| assays | **213** (172 at session start, +36 from List 2, +5 CMV from concurrent work) |
| papers held locally | 60+ (grew during List 2) |
| papers recoverable as PMC full text | 21 (`scripts/import_pmc_fulltext.py`) |
| oligos verified vs paper | 235 of 266 checkable (88%), 511 total |
| papers still wanted | 33 (`results/nyu-fetch-list.tsv`) |
| tests | 857 passing (all gates: pytest, ruff, validate, check_citations) |

The 9 extra tests need Snakemake (`environment.yml` installs `snakemake-minimal` from conda,
so they run on your laptop; on PyPI the package is just `snakemake`). They run the pipeline offline on a planted archive, edit
one source file at a time, and assert exactly which rules a dry run lists. CI's main job does
not install Snakemake, so it skips them; a separate `snakemake` job in the workflow installs it
and runs them, and is allowed to fail without turning the build red (check it when it does).

Gates on every commit: registry schema, and every citation checked against Crossref
(`scripts/check_citations.py`, which reads the committed `docs/papers-index.cache.json` and so
still passes offline - but a NEW DOI cannot be verified without Crossref, and must wait rather
than be entered).

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

## What landed in this session (2026-10-06)

**36 new draft entries from 5 parallel agents** (herpes, bees, mixed, bacteria groups):
- EEHV, LeHV-5, Batravirus (herpes): 13 entries, measured sizes differ from papers by up to 50 bp
- Honeybee viruses, *Nosema*, reptarenavirus (Rossi 2024, Kato 2020, Baggio 2023): 8 entries
- Influenza A, avipox, Ophidiomyces, orthopoxvirus (Tsukamoto, Baek, Haynes, Meyer): 6 entries
- *M. gallisepticum*, Chlamydia genus/species, TB complex, *V. coralliilyticus* (Kang, Messmer, Boniotti, Wilson): 9 entries

**Schema and verifier changes:**
- **Probe floor lowered to 12 nt** (from 15) where papers use MGB/LNA. Primers still 15. Validator role-aware via `orientation` tag.
- **Verifier role-aware harvest floor**: probes now found at their own floor, so published 13-14 nt MGB probes reach `exact` instead of `in-text`.
- **Pre-commit hooks fixed** to use conda Python (had been using system Python where yaml wasn't available).

**Verification:**
- All 36 DOIs verified with Crossref (doi_verified: true). Citation cache refreshed (110 papers, 64 local, 104 cited).
- All gates passed: 857 tests, 0 Crossref problems, 0 validation problems.

**NCBI key rotated** to a new key in `.secrets/ncbi.key` (old key exposed in agent transcripts, now replaced).

- **Verifier** (`scripts/verify_oligos_against_paper.py`). `no-oligos` fires when a text prints
  fewer than two oligo-like runs, decided *after* looking for the stored oligo, and also when a
  name is followed by an empty bracket (`primer 1R ()`, the avipox primer). Every "X or inosine"
  notation is read, `(n/i)` but also `(b/i)`, `(r/i)` and `(y/i)`, which Deckers 2009 prints;
  before that, 4125s and 4125as would have read `absent` once re-cited. Which file holds a DOI
  is decided by what it yields for a named file and by which prints the DOI EARLIER for an
  unnamed one, so a review cannot take a paper's DOI by sorting first. A printed run longer
  than the stored oligo is aligned end to end and the note says whether the extra bases are at
  an end (possibly table text) or inside (evidence). `scripts/extract_candidate_oligos.py` no
  longer drops a paper that cites another DOI before its own, and
  `scripts/check_primer_provenance.py` finds two and three-character oligo names and says so
  when a name is one character.
- **Duplication check** (`drift.py`, `report.py`). A flag survives only if it has at least
  `min_records_for_drift` distinct footprints, stays below the threshold when the sample is cut
  to the number of footprints, AND stays below it when each distinct footprint is counted once
  (the last is what sees one clone carrying all the failures; the first version could not, and
  said a flag "does not depend on duplicated records" for 92 failures at one footprint beside
  detections on 19 others). Footprints that are unknown (older cached screens, diverged
  records) make the check say it was not run. The note names which test failed and blames
  duplication only where a test implying it failed. Never changes a status. Worth reading the
  tally with this in mind: a perfect match is ONE footprint, so a baseline of thousands of exact
  matches is a single draw, and `declining` flags will fail the check more often than
  `low coverage` ones.
- **Per-chemistry scoring** (`scoring.by_chemistry`, shipped EMPTY, so every call is unchanged
  at the default config). Every place that reads the scoring block itself now honours an
  override: the assembly pre-cut searches at the widest budget any chemistry uses, and
  `scripts/indel_check.py` re-judges a `fail` and labels a missing primer under the chemistry of
  the assay it is given. The numbers themselves are for tier-2 validation to set. The first
  candidate, relaxing `terminal_mismatch_fails` for conventional PCR, is in `config.yaml`
  commented out with the literature behind it. I checked that literature against PubMed's
  abstracts on 2026-10-06: Kwok 1990 supports the comment (A:G, G:A, C:C about 100-fold, A:A about
  20-fold, T with G/C/T minimal); Stadhouders 2010 reports the same split by example, not as an
  exhaustive rule, and its abstract does not mention T:C or T:T. I did not read either full text.
- **Assembly archives** are cut with settings (`max_mismatches_searched`, the amplicon size
  range, the overhang, `max_pair_evalue`). They are now recorded beside the archive and a
  change re-cuts every genome (re-downloading them); before, only a change to the primer pairs
  did, so archives cut at the old settings sat beside new ones cut at the new. A group cut
  before this existed is adopted at the current settings rather than re-cut. The settings are
  also hashed into the `retrieve` rule so that changing one reruns retrieval at all.
- **Snakefile**: `collect_calls`, `report` and `degeneracy_table` rerun when the code they run,
  the registry they read, or the config sections they read change. Which source files each rule
  depends on is derived from the imports (read from the syntax tree, so the parenthesised and
  `as` forms the formatter produces are seen) by `assaywatch/triggers.py` instead of kept as a
  hand list, which had already missed `schema.py` and `validate.py` once.
- **The calls table's gzip is deterministic** (no timestamp or file name in the header), so
  "unchanged" can be checked with a hash.
- **`retrospective.py`**: the status-to-verdict mapping is one function, `classify`, pinned over
  every status and expectation. **`scripts/diff_printed_oligos.py`** (new): see the next section.
- **Tests that could not fail now can.** Each gap was shown by a surviving mutant first, and the
  tests were then run against mutants of the fix: well over a hundred across the two rounds, all killed.

## Flagged decisions (from agents, awaiting user judgment)

**Herpesviruses:**
- LeHV-5 taqman + evagreen: same primer pair in two entries (flag `SHARED_PRIMERS_WITH_SIBLING_ENTRY`). Drop `_evagreen`?
- EEHV6 round2: rests on 1 spanning record (flag `SINGLE_SPANNING_RECORD`). Keep or delete?

**Bees/bumblebee/reptile:**
- *Nosema bombi*: keep under Kato's DOI or move to Klee 2006 (not local)?
- DWV-A/-B: use variant-node taxids or species taxid? (80% of records unlabeled; flagged `VARIANT_SCOPE`)
- Reptarenavirus: multiplex as one pooled entry? S-segment-only query or broaden?
- Not entered: *N. ceranae* pair has mismatches on all references.

**Mixed (Tsukamoto, Baek, Haynes, Meyer):**
- Ophidiomyces target-D: panel member as species marker. Keep (as entered) or delete?
- Orthopoxvirus ATI: differentiation assay, size 540–1700 bp by species. Keep (as entered) or delete?
- Tasman-PCR (Kwon): transmissible cancer, host-genome. In scope? (4 ready drafts in scratchpad.)
- Clade/lineage scoping: H5, H7, NP, hummingbird avipox. Add scoping or flag for review?

**Bacteria:**
- Chlamydia genus 16S round1: printed primer has T where all records have A. Enter as printed (hypothesis) or correct?
- *C. trachomatis* serovar polymorphism: three serovars have mismatches. Flag, scope, or accept reduced detection?
- *C. psittaci* and *C. abortus*: cross-reaction detected. Note or narrow scope?
- *M. gallisepticum* vaccine pairs: exact on own genomes, >90% non-detect under species taxid. Enter if strain scoping added?

## Do this first on the laptop

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

1. **Settle the flagged decisions above** (8 groups awaiting user judgment on entries or scope).
2. **Settle the coronavirus finding.**
   `CORONAVIRUS_..._Lan_2010_round1` stores a reverse primer 3 nt shorter than the one Quan et
   al. 2010 prints (`...GCNACATG` against `...GCNACNACATG`). The stored form matches PREDICT
   P-005, so two published sources disagree and the sequence was deliberately left alone. Read
   the P-005 table in the Anthony et al. 2015 supplement, screen both forms against real RdRp
   records, then fix whichever is wrong - and check the other P-005 entries for the same
   deletion. This is the second PREDICT-vs-cited-paper mismatch after Atkins/PREDICT.
2. **Measure the two CMV gB amplicons, then re-cite the 4007/4125 pair.**
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
3. **DOIs now verified** via Crossref (all 36 List 2 entries + CMV entries). Previous
   unresolved candidates in `docs/2026-10-05-doi-candidates.md` may still need attention
   (Pan-Flavivirus NS5, SIVdrl pol, ETEC LT, *E. cuniculi* PTP, *Encephalitozoon* 18S, and two
   CDV/coronavirus entries) once those papers are in hand locally or via PMC.
5. **4 image-only primer tables**: M. bovis (`10.1371/journal.pone.0207365`), Usutu
   (`10.2807/1560-7917.es.2020.25.41.2001732`), Batrachochytrium ITS (`10.3390/jof7040258`, but
   see below), avian orthobornavirus done already. Render with pymupdf at ~200 dpi and read the
   page as an image, as was done for Ghosh - that worked and the sequences verified against
   records afterwards.
6. **211 oligos** whose provenance is unchecked for want of full text.

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
