# Resume point, 2026-10-06 (after a second cloud session and an adversarial review)

Everything described here is on `main`. This file is the short version of where to
pick up.

## First, after `git pull`: adopt the cached screens, or the next run rescreens everything

The pull changes the screening code and the hashes that decide whether a cached
screen is still valid (`score.py`, and a Snakefile that now derives which source
files each rule depends on). Snakemake will therefore consider every cached screen
stale and rescreen all of them. At the default config nothing about the screening
*result* changed, so that work would reproduce what is already on disk. Three
commands avoid it:

    snakemake --cores 4 --config email=nightb02@nyu.edu --until retrieve
    snakemake --touch --cores 4 --config email=nightb02@nyu.edu
    snakemake --cores 4 --config email=nightb02@nyu.edu

The first fetches whatever is new, exactly as the normal run would, and stops. The
second marks the existing screens up to date and records the new hashes *without
recomputing anything*. Order matters: `--touch` can only reach the screens once
today's retrieval record exists, and it never creates an output that is missing, so
a brand-new archive is still screened in the third command, with the new code. Add
`run_date=YYYY-MM-DD` to all three if you use it.

What was verified, under real Snakemake 9.27.0 in a scratch environment, on a tree
built from the commit you last pulled (`826a905`) and then overlaid with this one:
the second and third commands, with a planted retrieval record standing in for the
first. The screens were adopted, the third command executed only `collect_calls`,
`degeneracy_table` and `report`, and every screen and the calls table came out
byte-identical to the old code's. The first command could not be run for real (it
needs NCBI); a dry run of it lists only the `retrieve` checkpoint, which is the
intent.

Do not use `snakemake -n` to check any of this. A dry run cannot list the screening
jobs at all: they sit behind the `retrieve` checkpoint, so they only appear once it
has run. An earlier version of this note said `-n` would list the same jobs as
before; that was wrong, and was written before Snakemake had ever been run on this
Snakefile.

If you would rather rescreen everything, run the third command alone. It is correct,
only slow.

## Why the remaining work wants the local machine

`papers/` is gitignored - the PDFs are copyrighted and should stay out of git. A
cloud session clones from git and starts with none of them.

Two cloud sessions have now tested how far that can be worked around. They
recovered **21 papers** as open-access PubMed Central full text and got real value
out of them, but could not advance the entry work, for two reasons worth knowing
before anyone tries again:

- **No sequence database.** The environment's egress policy denies
  `eutils.ncbi.nlm.nih.gov`, `www.ebi.ac.uk`, `api.crossref.org`,
  `api.unpaywall.org` and `api.openalex.org` (re-tested 2026-10-06: still denied,
  including after being told the network was available). `amplicon_bp` cannot be
  measured against real records, and measuring rather than quoting is the method
  this registry rests on, so no assay can honestly be entered. What *is* reachable
  is PubMed through an MCP tool: metadata, PMC ids and PMC full text.
- **PMC full text often arrives without its primer tables, but not always.** The
  text comes flattened. Prepens 2007 and Deckers 2009 came through with their primer
  tables readable; Quan 2010 and several others did not, and the avipox paper's
  tables hold only Ct values. Of the 44 papers that resolved to a PMC id, 23 came
  back as an abstract only (ASM, PNAS and SAGE deposit abstracts). So expect some
  sequences from PMC and do not expect all of them.

Full write-up: `docs/2026-10-05-cloud-session-findings.md`, including an addendum of
the statements from the first cloud session that the review below corrected.

## State

| | |
|---|---|
| assays | 164 |
| papers held locally | 60 |
| papers recoverable as PMC full text | 21 (`scripts/import_pmc_fulltext.py`) |
| oligos confirmed, local 60-paper run | 100 of 175 checkable, 384 total - STALE, see below |
| oligos confirmed, cloud 21-paper subset | 24 of 38 checkable - NOT comparable |
| papers still wanted | 33 (`results/nyu-fetch-list.tsv`) |
| tests | 942 passing, 10 skipped without Snakemake; 950 passing, 2 skipped with it |

The 8 extra tests need Snakemake (`snakemake-minimal`, which `environment.yml`
already installs, so they run on your laptop). They run the pipeline offline on a
planted archive, edit one source file at a time, and assert exactly which rules a
dry run lists. They are skipped in CI, which installs only the package.

Gates on every commit: registry schema, and every citation checked against Crossref
(`scripts/check_citations.py`, which reads the committed
`docs/papers-index.cache.json` and so still passes offline - but a NEW DOI cannot be
verified without Crossref, and must wait rather than be entered).

## The NCBI API key

Set it in ONE place and every caller picks it up. Resolution order, first hit wins:

1. `$NCBI_API_KEY`
2. `.secrets/ncbi.key` (gitignored, so it cannot be committed by accident)

Check it took, without printing it:

    python -m assaywatch.credentials

and, to also ask NCBI whether it accepts the key:

    python -m assaywatch.credentials --check

**`--check` has never been run against the real NCBI**: this environment cannot
reach it, and it is tested only against a local server. Run it once on your laptop;
if it reports anything other than "accepted", paste me the output (it never contains
the key).

In a cloud session, add `NCBI_API_KEY` under the environment's settings rather than
writing the file - that is the only route where the key never touches a filesystem, a
chat window or a diff, which is why the environment wins over the file. A new session
picks it up.

It is a rate limit, not authentication: 3 requests per second without it, 10 with.
Everything works unkeyed, three times slower. All the NCBI callers go through
`assaywatch/credentials.py` and share one sleep interval. The key travels in the
query string of the E-utilities GET requests, so exception text from `requests` would
contain it; every call site that can print one now scrubs it first, and a test drives
each of them against a local server that returns an error and checks the key is not in
the output.

## What landed in this session, and what to look at

All of it was found, fixed and tested against a review of everything after `50430bb`:
61 findings, 51 confirmed, each re-verified before being fixed. Several of the
confirmed ones were false statements of mine, listed at the end of
`docs/2026-10-05-cloud-session-findings.md`.

- **Verifier** (`scripts/verify_oligos_against_paper.py`). Five ways it could give a
  false verdict are closed. `no-oligos` now fires when a text prints fewer than two
  oligo-like runs (it used to need zero, so one stray sequence in prose turned every
  other oligo into a full-strength `absent`), and it is decided *after* looking for
  the stored oligo, so a paper that does print it is never told it prints nothing.
  Inosine-rich primers are kept. A printed oligo longer than the stored one is
  reported in full rather than as a stored-length window. Which file represents a DOI
  is decided by what it yields, not by its file type, so a table-less text cannot
  displace a good PDF. `--cap` above 4 no longer drops `near:N` rows from the
  headline. `scripts/extract_candidate_oligos.py` and
  `scripts/check_primer_provenance.py` follow the same rules.
- **Duplication check** (`drift.py`, `report.py`). It now needs at least
  `min_records_for_drift` distinct footprints before saying a flag "does not depend on
  duplicated records" (at one to three footprints the Wilson interval is too narrow to
  mean anything: the review's own malB case, 92 failures sharing one footprint, used
  to be reassured). It no longer invents a footprint for rows with none (cached
  screens from before the columns existed, and records scored as failures for being
  diverged): those make the count unknown and the report says it could not run the
  check. The note says which test failed instead of always blaming the recent share.
  Never changes a status. Worth reading the tally with this in mind: a perfect match
  is ONE footprint, so a baseline of thousands of exact matches is a single draw, and
  `declining` flags will fail the check more often than `low coverage` ones.
- **Per-chemistry scoring** (`scoring.by_chemistry`, shipped EMPTY, so every call is
  unchanged at the default config). Three places that read the scoring block
  themselves now honour an override: the assembly pre-cut searches at the widest
  mismatch budget any chemistry uses (it was cutting windows an override would have
  scored), and `scripts/indel_check.py` re-judges a `fail` and labels a missing primer
  under the chemistry's own rules, with its partner search no longer fixed at six
  mismatches. The numbers themselves are for tier-2 validation to set, not for me to
  pick. The first candidate, relaxing `terminal_mismatch_fails` for conventional PCR,
  is in `config.yaml` commented out with the literature behind it, and I checked that
  literature against PubMed on 2026-10-06: Kwok 1990 (A:G, G:A, C:C cut yield about
  100-fold, A:A about 20-fold, T with G/C/T minimal) and Stadhouders 2010 (<1.5 Cq for
  A-C, C-A, T-G, G-T against >7 Cq for A-A, G-A, A-G, C-C) say what the comment says
  they say. That was from their abstracts; I did not read the full texts.
- **Snakefile**: `collect_calls`, `report` and `degeneracy_table` now rerun when the
  code they run, the registry they read, or the config sections they read change
  (previously only an added or removed registry file did, by accident). Which source
  files each rule depends on is derived from the imports by `assaywatch/triggers.py`
  instead of kept as a hand list, which had already missed `schema.py` and
  `validate.py` once. Verified by real runs, see above.
- **`scripts/diff_printed_oligos.py`** (new). See the next section.
- **Tests that could not fail now can**: the retrospective cutoff and per-case
  verdicts, and `collect`'s copy path. Each gap was shown by a surviving mutant first.

## Do this first on the laptop

**1. Re-run the verifier over the full local `papers/`.** The reader and the verdict
logic changed in ways that move its answers, so the 100-of-175 figure and the 65
`absent` rows are both stale:

    python scripts/verify_oligos_against_paper.py --pdf-dir papers --tsv results/oligo-verification.tsv

Expect a chunk of the 65 known `absent` rows - particularly the image-table papers,
*M. bovis*, Usutu, *Batrachochytrium* ITS - to move to `no-oligos`. They were never
evidence about a sequence. Expect some `in-text` rows to become `exact`, and any entry
whose paper writes `(N/I)` ("N or inosine") inside a sequence to move.

**2. Check the new reader against your 60 PDFs, not just my 21 texts.** The
composition thresholds in `printed_oligos` were tuned on the 21 open-access texts I
could reach. On those, the whole change since `50430bb` loses nothing and gains four
oligos: two degenerate Atkins 2009 primers, the Quan 2010 reverse consensus primer, and
a Prepens 2007 primer that `(N/I)` had split. The 21 are not your 60.

    python scripts/diff_printed_oligos.py --papers papers --old-rev 826a905
    python scripts/diff_printed_oligos.py --papers papers --old-rev 50430bb --extractor-only

It reads each paper with the old and the new reader, taking the old script straight
from git, and lists oligos LOST and GAINED. Read the lost ones first. If anything is
lost on a real PDF, send me the file name and the sequence, and the threshold gets
fixed before the verdicts are trusted.

## Then, in value order

1. **Settle the coronavirus finding.**
   `CORONAVIRUS_..._Lan_2010_round1` stores a reverse primer 3 nt shorter than the one
   Quan et al. 2010 prints (`...GCNACATG` against `...GCNACNACATG`). The stored form
   matches PREDICT P-005, so two published sources disagree and the sequence was
   deliberately left alone. Read the P-005 table in the Anthony et al. 2015
   supplement, screen both forms against real RdRp records, then fix whichever is wrong
   - and check the other P-005 entries for the same deletion. This is the second
   PREDICT-vs-cited-paper mismatch after Atkins/PREDICT.
2. **Measure the two CMV gB amplicons, then re-cite the 4007/4125 pair.**
   - `..._Virol_2007_round1` and `..._round2` hold Prepens' own CM-gB pairs and verify
     exact. Prepens gives two different numbers for round 1 - 330 in Table 3 (footnoted
     "approximate values") and 320 in its Figure 1 legend - and 250 for round 2 in both
     places. The stored 320 agrees with the figure and the stored 230 agrees with
     neither, so these are not one spreadsheet error, and "correct both to 330" would
     overwrite a value the paper's own figure supports. Run both pairs against real UL55
     records and store what they measure.
   - `CMV_specific_HERPES_UL55_Glycoprotein_B_gB` (4007-s/4007-as) and `..._round2_2`
     (4125-s/4125-as) are **not in Prepens**, and their source is now known: Deckers et
     al. 2009, *Virol J* 6:210 (PMID 19941648, PMC2789067), Table 1, primer set
     CMV-gBp1, where 4007 is round 1 (800 bp) and 4125 is round 2 (550 bp) of one nested
     assay. Three of the four stored sequences match exactly; 4125-s has N where the
     paper prints B-or-inosine at one position. The DOI `10.1186/1743-422X-6-210` came
     from PubMed, not Crossref, so it is NOT written into `citation.doi`. When Crossref
     is reachable: verify it (`scripts/resolve_citations.py`), re-cite both entries
     together, decide `oligos_designed_here` from what Deckers says (it says the
     primers were designed to bind conserved sites, but cites an earlier use in great
     apes), and clear the flag. Details are in each entry's `notes_curator`.
3. **DOIs waiting on Crossref**, in `docs/2026-10-05-doi-candidates.md`. Five are
   resolved with high confidence: Pan-Flavivirus NS5, SIVdrl pol, ETEC LT, *E.
   cuniculi* PTP, and the *Encephalitozoon* 18S entry (10 oligos between them). Two
   groups first written up as unresolvable now have candidates: Müller 2011 CDV H gene
   (`10.7589/0090-3558-47.3.725`, PMID 21719841; the stored reference's volume and page
   settle it bibliographically; its primers are unchecked because the paper is not in
   PMC) and Wang 1997 (`10.1046/j.1365-2672.1997.00300.x`, PMID 9449811; plausible,
   since its abstract lists both organisms, but unverified). Add each with
   `doi_verified: false`, then
   `python scripts/resolve_citations.py --registry registry --email nightb02@nyu.edu`
   followed by `python scripts/check_citations.py --refresh`.
4. **20 List 2 papers**, oligos extracted to `results/candidate-oligos-2026-10-05.tsv`,
   awaiting verify-then-enter. The biggest are EEHV pol (19 oligos), deformed wing virus
   RdRp (19), CDV N (jcm.02505-21, 17), canine morbillivirus (v13081632, 15),
   reptarenavirus (14), influenza A hemagglutinin (7), monkeypox B6R (6), devil facial
   tumour (6). Method that worked: read the paper's own table, measure the amplicon on
   real GenBank records, then enter - never quote a size.
5. **4 image-only primer tables**: M. bovis (`10.1371/journal.pone.0207365`), Usutu
   (`10.2807/1560-7917.es.2020.25.41.2001732`), Batrachochytrium ITS
   (`10.3390/jof7040258`, but see below), avian orthobornavirus done already. Render with
   pymupdf at ~200 dpi and read the page as an image, as was done for Ghosh - that worked
   and the sequences verified against records afterwards.
6. **211 oligos** whose provenance is unchecked for want of full text.

## Two things waiting on someone else

- **Elsevier institutional token.** The API key works (Scopus returns results); full
  text 403s with "Requestor configuration settings insufficient". That is a separate
  entitlement and the VPN does not change it. Ask NYU Libraries for an institutional
  token for the ScienceDirect Article Retrieval API; drop it in
  `.secrets/elsevier.insttoken` and `scripts/fetch_elsevier.py` will use it with no other
  change. Unlocks 12 papers / 42 oligos. Note: one Elsevier paper on that list, EEHV pol
  (`10.1016/j.vetmic.2010.05.042`), has an author manuscript in PMC (`PMC2976818`) and is
  already recoverable without the token - though its primer table is among the ones PMC
  loses.
- **The rest of the fetch list**, `results/nyu-fetch-list.tsv`, ranked by oligos at
  stake. Browser automation is a dead end for these: ScienceDirect blocks on User-Agent
  (CPE00001) and SAGE sits behind a Cloudflare human check.

## Already known, do not re-litigate

- `jof7040258` publishes NO new primers - it compares Blooi 2013 (already in the
  registry) against Spitzen-van der Sluijs 2020. It belongs in `docs/validation-cases.tsv`,
  not `registry/`.
- Composite entries, each needing its scope read from a different paper than the one
  cited: Hellgren/Bensch, Blooi/Martel, Atkins/PREDICT, and now the CMV 4007/4125 pair.
  Lan/Quan is a related case (the panel's oligo is not the cited paper's).
- The VPN does not fix the Elsevier 403.
- **`10.1111/1755-0998.13299` (Ghosh 2021) is still a read-by-eye job.** Its PMC full
  text is available and its narrative is intact, but the primer table is not in it - the
  text carries no sequences and not one `5′` mark. The PDF is the only route to it.
- **The avipox 1R primer is missing from the PMC text because its parenthetical is empty
  in the Methods sentence**, not because PMC dropped a table (the paper's tables hold Ct
  values only). The entry is sound: an invariant 250 bp product across six independent
  records with the probe site present in all six cannot come from a wrong reverse primer.
- **ASM deposits abstracts only**, and so do PNAS and SAGE here. J Clin Microbiol, J Virol
  and Appl Environ Microbiol return an empty body from PMC; mBio, born open access,
  returns whole, so the `10.1128` prefix does not predict it - the journal does. **23 of
  the 44 papers resolved to a PMC id came back as an abstract**, listed with their oligo
  counts in `docs/2026-10-05-pmc-abstract-only.tsv`: 74 oligos across 20 registry papers,
  plus 3 List 2 candidates. 21 of the 23 are ASM, so one fetch run on the NYU subscription
  clears nearly all of it. Do not retry them against PMC.
