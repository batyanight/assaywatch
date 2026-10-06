# Cloud session, 2026-10-05: what a locked-down environment could and could not do

This session ran in a cloud container rather than on the machine that holds
`papers/`. It set out to rebuild `papers/` from open-access sources and then work
the verification backlog. It rebuilt part of `papers/`, found and fixed a real
defect in the verifier, and found one new registry discrepancy. It could not
touch the List 2 entry work at all, for a reason worth recording.

## The network, which decided most of this

The environment's egress policy allows package registries and GitHub and denies
everything else. Every host this project's scripts depend on is denied:

| host | used for | result |
|---|---|---|
| `api.crossref.org` | citation gate | denied |
| `api.unpaywall.org`, `api.openalex.org` | `find_open_access.py` | denied |
| `www.ebi.ac.uk` | Europe PMC full text | denied |
| `eutils.ncbi.nlm.nih.gov` | GenBank records, PMC id conversion | denied |

So `scripts/find_open_access.py` - the intended route in the handoff note -
could not make a single request. What *was* reachable is PubMed Central through
an MCP tool, which returns open-access full text as JSON. That is the same
corpus Europe PMC's `fullTextXML` serves, over a different transport, so a
sequence read from it is still read from the publisher's deposited text.
`scripts/import_pmc_fulltext.py` was written to turn that JSON into the per-DOI
files `papers/` expects.

**`check_citations.py` still passes**, because `docs/papers-index.cache.json` is
committed and the gate reads the cache unless asked to refresh. No new DOI was
introduced, so nothing needed a Crossref lookup. Had one been needed, it could
not have been verified, and the entry would have had to wait.

## What came back: 21 of 70 papers

34 of the registry's 70 distinct DOIs have a PMC id, as do all 10 candidate
papers whose DOIs were known. Of those 44, **21 returned usable full text**.

The 23 failures are not random, and they are almost one publisher:

| | abstract only |
|---|---|
| ASM - J Clin Microbiol, J Virol, Appl Environ Microbiol (`10.1128`) | 21 |
| PNAS (`10.1073`) | 1 |
| SAGE - J Vet Diagn Invest (`10.1177`) | 1 |

ASM's mBio, born open access, returned whole, so the prefix alone does not
predict it - the journal does. This is deposit policy, not availability, and no
amount of retrying changes it. Those 23 still need the PDF.

All 23 are listed in **`docs/2026-10-05-pmc-abstract-only.tsv`**, with the PMC
id, whether the registry cites it, and the oligos at stake: **74 oligos across
20 registry papers**, plus 3 List 2 candidates (CDV/PDV N, pan-pox, and the
batrachovirus paper). That is the single largest tranche of blocked verification
work and most of it is one publisher, so an ASM PDF run via the NYU subscription
would clear it.

A caution on that number if you re-derive it from the importer: the importer can
only report on the JSON it is handed, and its own "no full text" list counted 12,
not 23. The other 11 were a batch of ASM papers whose response came back small
enough to arrive inline rather than as a file, so no dump ever reached the
importer. The TSV above is the complete list; the importer's figure is not.

The importer **skips an empty body rather than writing an abstract-only file**,
which matters more than it looks: an abstract-only file would be indexed as if
the paper were in hand, and every sequence checked against it would come back
`absent` - indistinguishable from the finding `absent` is supposed to carry.

## The defect this turned up, which outlives the session

Two of them, both in `verify_oligos_against_paper.py`.

### 1. `absent` was being manufactured wholesale

**PMC full text often arrives without its primer tables, though not always.** The
body text arrives flattened, and what happens to a table varies by paper: Prepens
2007 and (checked 2026-10-06) Deckers 2009 came through with their primer tables
intact, the avipox paper's tables came through but hold only Ct values, and the
avian orthobornavirus paper came back as 31,202 readable characters containing zero
oligo-like runs, so the first run reported all 12 of its stored oligos `absent`.
Across the run, **44 of 57 `absent` verdicts were artifacts of extraction** -
statements about the file masquerading as statements about the sequence. (This
section first said PMC "omits `table-wrap` content" outright. That was too
general, and it was also given as the reason one avipox primer was missing, which
was wrong; see the addendum.)

Fixed by giving that case its own verdict, `no-oligos`, excluded from the
checkable denominator, plus a `paper_oligos` column recording how many oligo-like
runs the matched text held. An `absent` against a paper that printed 2 oligos
deserves far less weight than one against a paper that printed 40.

This is not a cloud-only problem. It applies identically to the image-only
primer tables already known in `papers/` - *M. bovis*, Usutu, *Batrachochytrium*
ITS - which were producing the same false `absent` from PDFs all along.

### 2. The composition test dropped heavily degenerate primers

`printed_oligos` required 75% of a candidate's letters to be unambiguous bases,
counting inosine as one. Atkins 2009 prints `Astr4380F`
(`GAYTGGRCNCGNTWYGATGGNACIAT`, 0.73) and `Astr4722R` (`ARNCKRTCATCNCCATA`,
0.71). Both fell below the threshold, so neither was extracted, and the
registry's **exact** copies of them were reported as the much weaker `in-text`.

The fix turns on one detail: **inosine should never have been in that
numerator.** `I` is among the commonest letters in English and a rare one in
oligos, so counting it scores all-caps prose nearly as high as a real primer.
`INDINGS IN BATS IN THAI`, the PREDICT-report false positive the test exists to
block, scores 0.53 with inosine counted and 0.26 without, while a real primer
barely moves. Measured over the 21 papers in hand:

| | unambiguous fraction, inosine excluded |
|---|---|
| all-caps prose | 0.26 |
| most degenerate real primer | 0.69 |
| typical degenerate consensus primer | 0.71 - 0.85 |
| non-degenerate primer | 1.00 |

So the numerator dropped inosine and the threshold dropped to 0.65, which has
clear air on both sides where the old rule sat *above* two real primers. Pan-viral
consensus primers are degenerate by design and are most of what this registry
holds, so they cannot be edge cases.

Effect: 3 astrovirus oligos corrected from `in-text` to `exact`, no paper lost a
sequence, and a coronavirus discrepancy surfaced that the old threshold had
hidden completely.

## The new registry finding: Quan 2010 vs PREDICT P-005

`CORONAVIRUS_..._Lan_2010_round1`, reverse primer `CoV-RVS1(L1150)`:

- Quan et al. 2010 (the cited paper) prints `GGTCATKATAGCRTCAVMASWWGCNACNACATG`, 33 nt
- the registry stores `GGTCATKATAGCRTCAVMASWWGCNACATG`, 30 nt

Identical for 27 bases, then the stored form lacks `NAC` before the `ATG` tail.

**The sequence was not changed.** The 2026-10-04 note on that entry records the
stored form matching PREDICT P-005 in the Anthony et al. 2015 supplement, so
this is two published sources disagreeing, not a slip made here. It cannot be
adjudicated from this environment: Anthony 2015 keeps its primer tables in
Supplementary Information, which PMC does not carry, and no sequence database
was reachable to ask which form has a binding site. Recorded in
`notes_curator` with `needs_review: REVERSE_PRIMER_DISAGREES_WITH_QUAN_2010_BY_3NT_DELETION`.

Worth noting as a pattern rather than an incident: this is the **second** case,
after Atkins/PREDICT on the astrovirus entries, where the panel's oligo is not
the oligo the panel's cited paper printed. Citing the source paper while storing
the panel's sequence misattributes it either way, and the other P-005 entries
deserve the same check.

## Why the List 2 entry work did not advance

Two independent blocks, either of which is sufficient.

**No sequence database.** The method that earns this registry its trust is to
measure `amplicon_bp` against real GenBank records and never quote a size. NCBI
and EBI are both denied, so no amplicon can be measured. Entering an assay here
would mean quoting a size, which is the one thing the method forbids.

**Few primer tables.** Even setting that aside, the tables are what PMC often loses.
`extract_candidate_oligos.py` recovered 9 candidate oligos from 3 papers against
the ~110 expected from the 10 known candidate DOIs - EEHV pol, canine
morbillivirus, monkeypox B6R and *pone.0232044* each yielded zero, their
sequences having been in tables.

**Ghosh 2021 is still blocked, contrary to a hope early in this session.** Its
full text came through - 18,292 characters, readable narrative, the SNP-screening
and Primer Express methods intact - but the primer table did not, and the text
contains no `5′` marks and no sequences at all. It remains a read-by-eye job on
the PDF.

## State after this session

| | |
|---|---|
| assays | 164 (unchanged) |
| papers recovered into `papers/` | 21, all open-access PMC full text |
| oligos confirmed against their own paper | 20 of 38 checkable **in this 21-paper subset** |
| tests | 762 passing, 2 skipped |

**The 20-of-38 figure does not supersede the local 100-of-175.** It is a
different and much smaller sample - 21 papers against 60, many of them without
their primer tables. Re-run on the machine that holds the PDFs to get a
comparable number; the two sharpened verdicts mean the local figure will also
move, and some of its 65 `absent` rows should become `no-oligos`.

## For the next session on the local machine

1. **Re-run the verifier over the full `papers/`.** The degeneracy fix and the
   `no-oligos` verdict both change the answer, and some of the 65 known `absent`
   rows are the artifact described above rather than findings.
2. **Settle the Quan 2010 / P-005 three-base question**, then check the other
   P-005 entries for the same deletion.
3. **The 23 papers PMC holds as an abstract only**, in
   `docs/2026-10-05-pmc-abstract-only.tsv` - 74 registry oligos at stake. 21 of
   the 23 are ASM (J Clin Microbiol, J Virol, Appl Environ Microbiol), which the
   NYU subscription covers, so one fetch run clears nearly all of it.
4. **List 2 entry work** is unchanged and still needs the local machine, for the
   amplicon measurement if nothing else.

## Addendum, 2026-10-06: what an adversarial review of this session's work corrected

A review of everything committed after `50430bb` (61 findings, 51 confirmed, each
re-verified before any fix) found several statements in this session's notes that
were wrong. They are corrected in place where they were made; collected here so
nobody has to rediscover them:

- **"PMC strips tables."** Too general (see above). Some primer tables survive,
  some do not, and the avipox 1R primer was missing from the PMC text because its
  parenthetical is empty in the Methods sentence, not because a table was dropped.
- **"The source of CMV 4007/4125 is not answerable here."** It was: Deckers et al.
  2009 prints all four as a nested pair, and one PubMed search finds it. The
  registry notes had also said there was no round 1 for the 4125 series (the 4007
  pair is that round 1), that Prepens prints 13 oligos (it prints 16; 13 was the
  count before the `(N/I)` notation was normalised), and that no 10-base fragment of
  either 4125 sequence is in Prepens (the reverse complement of 4125-as shares an
  exact 11-base stretch with one of its primers, which is two primers designed on
  one conserved site, not identity).
- **"The Prepens amplicons are probably one spreadsheet error."** The paper states
  330 in its table (footnoted approximate) and 320 in its Figure 1 legend for
  round 1, and 250 in both places for round 2. The stored 320 agrees with the
  figure (which does not name the primer set; 250 appears in Table 3 only for CM-gB
  round 2, so the pairing is an inference); only the stored 230 contradicts the paper.
- **"Müller 2011 and Wang 1997 cannot be resolved."** Both resolve to a candidate
  with the right search; see `docs/2026-10-05-doi-candidates.md`.
- **"`snakemake -n` should list the same jobs as before."** It will not: the first
  run after pulling re-screens everything, because the screening code and its
  hashes changed. A dry run does list the screening jobs once today's retrieval record
  exists, and before that it plans only validate and retrieve; it was never a way to
  check the pull. See `docs/RESUME-HERE.md` for what to do instead.
- **"The adoption recipe is `--until retrieve`, `--touch`, then run."** Wrong: a second
  review showed it skips the screening of a new archive when today's results folder
  already exists, and `--touch` with no targets blesses stale screens whatever made them
  stale. The recipe in RESUME-HERE.md touches the existing screens only, and says when not
  to use it.
- **"Prepens prints 13 oligos (it prints 16)."** It prints 16 PCR primers in Table 3 and 7
  LNA oligonucleotides in Table 2; 13 was a count of extractor fragments.

None of the corrected statements changed a registry sequence, a DOI or a stored
amplicon.
