# Resume point, 2026-10-05 (updated after a cloud session)

Everything is committed and pushed. This file is the short version of where to
pick up.

## Why the remaining work wants the local machine

`papers/` is gitignored - the PDFs are copyrighted and should stay out of git.
A cloud session clones from git and starts with none of them.

A cloud session on 2026-10-05 tested how far that can be worked around. It
recovered **21 papers** as open-access PubMed Central full text and got real
value out of them, but it could not advance the entry work at all, for two
reasons that are worth knowing before anyone tries again:

- **No sequence database.** The environment's egress policy denies
  `eutils.ncbi.nlm.nih.gov` and `www.ebi.ac.uk`, so `amplicon_bp` cannot be
  measured against real records. Measuring rather than quoting is the method
  this registry rests on, so no assay can honestly be entered without it.
  `api.crossref.org`, `api.unpaywall.org` and `api.openalex.org` are denied too,
  which means `scripts/find_open_access.py` cannot make a single request.
- **PMC omits table content.** The body text arrives; `table-wrap` does not. The
  primer table is exactly what is wanted, so most recovered papers yield no
  sequences at all.

Full write-up: `docs/2026-10-05-cloud-session-findings.md`.

## State

| | |
|---|---|
| assays | 164 |
| papers held locally | 60 |
| papers recoverable as PMC full text | 21 (`scripts/import_pmc_fulltext.py`) |
| oligos confirmed, local 60-paper run | 100 of 175 checkable, 384 total |
| oligos confirmed, cloud 21-paper subset | 24 of 38 checkable - NOT comparable |
| papers still wanted | 33 (`results/nyu-fetch-list.tsv`) |
| tests | 762 passing, 2 skipped |

Gates on every commit: registry schema, and every citation checked against
Crossref (`scripts/check_citations.py`, which reads the committed
`docs/papers-index.cache.json` and so still passes offline - but a NEW DOI
cannot be verified without Crossref, and must wait rather than be entered).

## Do this first

**Re-run the verifier over the full local `papers/`.** Two fixes landed on
2026-10-05 that change its answers, so the 100-of-175 figure and the 65 `absent`
rows are both stale:

    python scripts/verify_oligos_against_paper.py --pdf-dir papers --tsv results/oligo-verification.tsv

- `absent` no longer swallows "this file prints no oligos at all". That case is
  now `no-oligos`, and in the cloud run it accounted for **44 of 57** `absent`
  rows. Expect a chunk of the 65 known `absent` rows - particularly the
  image-table papers, *M. bovis*, Usutu, *Batrachochytrium* ITS - to move there.
  They were never evidence about a sequence.
- `printed_oligos` no longer drops heavily degenerate primers. It had required
  75% unambiguous bases counting inosine, which sat above two real primers in
  Atkins 2009 and reported the registry's exact copies of them as `in-text`.
  Expect some `in-text` and `absent` rows to become `exact`.
- The reader now understands `(N/I)`, the "N or inosine" notation the
  Ehlers-lab consensus-primer papers print inside a sequence. It had been
  ending the oligo run, so every stored oligo past the first bracket read
  `absent` - 4 false verdicts on Prepens 2007 alone, all 4 exact once read.
  Any entry whose paper uses that notation will move.

## Then, in value order

1. **Settle the new coronavirus finding.**
   `CORONAVIRUS_..._Lan_2010_round1` stores a reverse primer 3 nt shorter than
   the one Quan et al. 2010 prints (`...GCNACATG` against `...GCNACNACATG`).
   The stored form matches PREDICT P-005, so two published sources disagree and
   the sequence was deliberately left alone. Read the P-005 table in the Anthony
   et al. 2015 supplement, screen both forms against real RdRp records, then fix
   whichever is wrong - and check the other P-005 entries for the same deletion.
   This is the second PREDICT-vs-cited-paper mismatch after Atkins/PREDICT.
2. **Measure the two CMV gB amplicons**, and settle a fourth misattribution
   while you are there. All four CMV gB entries cite Prepens 2007, and the
   paper splits them in two:
   - `..._Virol_2007_round1` and `..._round2` hold Prepens' own CM-gB pairs and
     now verify exact - but store 320 and 230 bp where the paper's table says
     330 and 250. Same direction, so probably one spreadsheet error. Run both
     pairs against real UL55 records; the measurement decides, per the avipox
     precedent, and if it lands on 330 then correct both together.
   - `CMV_specific_HERPES_UL55_Glycoprotein_B_gB` (4007-s/4007-as) and
     `..._round2_2` (4125-s/4125-as) store primers that are **not in Prepens at
     all** - not the sequences, not a 10-base fragment, not the strings "4007"
     or "4125". Prepens numbers its own 2743-2762 and 3730-3731. Both are
     flagged with `oligos_designed_here: false`; they need the real paper found,
     most likely another Ehlers-lab primate CMV one, and re-cited.
3. **Five missing DOIs are resolved and waiting**, in
   `docs/2026-10-05-doi-candidates.md`: Pan-Flavivirus NS5, SIVdrl pol, ETEC LT,
   *E. cuniculi* PTP, and the *Encephalitozoon* 18S entry. Found on PubMed, with
   the evidence for each, but NOT written into `registry/` because Crossref was
   unreachable and the citation gate must be the thing that approves a DOI. Add
   each with `doi_verified: false`, then
   `python scripts/resolve_citations.py --registry registry --email nightb02@nyu.edu`
   followed by `python scripts/check_citations.py --refresh`. Two minutes of work
   that takes 5 entries and 11 oligos out of `DOI_MISSING`. The Müller 2011 CDV
   and Wang 1997 references are deliberately still unresolved - see that file for
   why guessing them would be the Nobach mistake again.
4. **20 List 2 papers**, oligos extracted to
   `results/candidate-oligos-2026-10-05.tsv`, awaiting verify-then-enter. The
   biggest are EEHV pol (19 oligos), deformed wing virus RdRp (19), CDV N
   (jcm.02505-21, 17), canine morbillivirus (v13081632, 15), reptarenavirus
   (14), influenza A hemagglutinin (7), monkeypox B6R (6), devil facial tumour
   (6). Method that worked: read the paper's own table, measure the amplicon on
   real GenBank records, then enter - never quote a size.
5. **4 image-only primer tables**: M. bovis (`10.1371/journal.pone.0207365`),
   Usutu (`10.2807/1560-7917.es.2020.25.41.2001732`), Batrachochytrium ITS
   (`10.3390/jof7040258`, but see below), avian orthobornavirus done already.
   Render with pymupdf at ~200 dpi and read the page as an image, as was done
   for Ghosh - that worked and the sequences verified against records afterwards.
6. **211 oligos** whose provenance is unchecked for want of full text. The
   21 recovered papers added no new composites to the three already known.

## Two things waiting on someone else

- **Elsevier institutional token.** The API key works (Scopus returns results);
  full text 403s with "Requestor configuration settings insufficient". That is a
  separate entitlement and the VPN does not change it. Ask NYU Libraries for an
  institutional token for the ScienceDirect Article Retrieval API; drop it in
  `.secrets/elsevier.insttoken` and `scripts/fetch_elsevier.py` will use it with
  no other change. Unlocks 12 papers / 42 oligos.
  Note: one Elsevier paper on that list, EEHV pol
  (`10.1016/j.vetmic.2010.05.042`), turns out to have an author manuscript in
  PMC (`PMC2976818`) and is already recoverable without the token - though its
  primer table is among the ones PMC strips.
- **The rest of the fetch list**, `results/nyu-fetch-list.tsv`, ranked by oligos
  at stake. Browser automation is a dead end for these: ScienceDirect blocks on
  User-Agent (CPE00001) and SAGE sits behind a Cloudflare human check.

## Already known, do not re-litigate

- `jof7040258` publishes NO new primers - it compares Blooi 2013 (already in the
  registry) against Spitzen-van der Sluijs 2020. It belongs in
  `docs/validation-cases.tsv`, not `registry/`.
- Three composite entries, each needing its scope read from a different paper
  than the one cited: Hellgren/Bensch, Blooi/Martel, Atkins/PREDICT.
- The VPN does not fix the Elsevier 403.
- **`10.1111/1755-0998.13299` (Ghosh 2021) is still a read-by-eye job.** Its PMC
  full text is available and its narrative is intact, but the primer table is
  not in it - the text carries no sequences and not one `5′` mark. The PDF is
  still the only route to that table.
- **ASM deposits abstracts only**, and so do PNAS and SAGE here. J Clin
  Microbiol, J Virol and Appl Environ Microbiol all return an empty body from
  PMC; mBio, born open access, returns whole, so the `10.1128` prefix does not
  predict it - the journal does. **23 of the 44 papers resolved to a PMC id came
  back as an abstract**, listed with their oligo counts in
  `docs/2026-10-05-pmc-abstract-only.tsv`: 74 oligos across 20 registry papers,
  plus 3 List 2 candidates. 21 of the 23 are ASM, so one fetch run on the NYU
  subscription clears nearly all of it. This is now the biggest single block of
  verification work and the cheapest to unblock. Do not retry them against PMC.
  (`scripts/import_pmc_fulltext.py` reported only 12 of these, because it can
  only list what is passed to it; the TSV is the complete set.)
