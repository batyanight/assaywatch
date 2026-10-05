# Resume point, 2026-10-05

Everything is committed and pushed. This file is the short version of where to
pick up.

## Why this work cannot run in the cloud

`papers/` is gitignored - the PDFs are copyrighted and should stay out of git.
A cloud session clones from git and would therefore start with none of the 60
papers. Nearly all the remaining work reads those files, so it has to run on the
machine that holds them. That is a constraint, not a problem: nothing is lost by
stopping, and everything resumes by opening this repo.

## State

| | |
|---|---|
| assays | 164 |
| oligos confirmed against their own paper | 100 of 175 checkable, 384 total |
| papers held locally | 60 |
| papers still wanted | 33 (`results/nyu-fetch-list.tsv`) |
| tests | 765 passing |

Gates that now run on every commit: registry schema, and every citation checked
against Crossref (`scripts/check_citations.py`).

## Next, in value order

1. **20 List 2 papers already in `papers/`**, oligos extracted to
   `results/candidate-oligos-2026-10-05.tsv`, awaiting verify-then-enter. The
   biggest are EEHV pol (19 oligos), deformed wing virus RdRp (19), CDV N (17),
   reptarenavirus (14), influenza A hemagglutinin (7), monkeypox B6R (6), devil
   facial tumour (6). Method that worked: read the paper's own table, measure the
   amplicon on real GenBank records, then enter - never quote a size.
2. **4 image-only primer tables**: M. bovis (`10.1371/journal.pone.0207365`),
   Usutu (`10.2807/1560-7917.es.2020.25.41.2001732`), Batrachochytrium ITS
   (`10.3390/jof7040258`, but see below), avian orthobornavirus done already.
   Render with pymupdf at ~200 dpi and read the page as an image, as was done for
   Ghosh - that worked and the sequences verified against records afterwards.
3. **65 `absent` oligos** in `results/oligo-verification-2026-10-05.tsv`: the
   paper is in hand but the sequence is not in it. Per the Blooi case this often
   means the oligos came from a DIFFERENT paper than the one cited.
4. **211 oligos** whose provenance is unchecked for want of full text.

## Two things waiting on someone else

- **Elsevier institutional token.** The API key works (Scopus returns results);
  full text 403s with "Requestor configuration settings insufficient". That is a
  separate entitlement and the VPN does not change it. Ask NYU Libraries for an
  institutional token for the ScienceDirect Article Retrieval API; drop it in
  `.secrets/elsevier.insttoken` and `scripts/fetch_elsevier.py` will use it with
  no other change. Unlocks 12 papers / 42 oligos.
- **The rest of the fetch list**, `results/nyu-fetch-list.tsv`, ranked by oligos
  at stake. Browser automation is a dead end for these: ScienceDirect blocks on
  User-Agent (CPE00001) and SAGE sits behind a Cloudflare human check.

## Already known, do not re-litigate

- `jof7040258` publishes NO new primers - it compares Blooi 2013 (already in the
  registry) against Spitzen-van der Sluijs 2020. It belongs in
  `docs/validation-cases.tsv`, not `registry/`.
- Three composite entries found so far, each needing its scope read from a
  different paper than the one cited: Hellgren/Bensch, Blooi/Martel,
  Atkins/PREDICT.
- The VPN does not fix the Elsevier 403.
