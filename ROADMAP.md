# Roadmap

**This is the only to-do list in the repository.** If work is open, it is in
`## Open work` below. Nothing else is authoritative:

- `docs/RESUME-HERE.md` says where the last session stopped and what it found. It
  no longer carries a list of its own.
- `docs/YYYY-MM-DD-*.md` are session records. Several end in "Next steps" or
  "Still open"; those were true on the date in the filename and are kept as
  history, not as a queue. Anything in them that is still live has been lifted
  into this file, with a pointer back.
- `papers/papers-fetch-list.md` is the one exception, and it is a fetch queue
  rather than a work list: PDFs that need a human and a proxy. The work those
  PDFs unblock is tier-2 validation, below.
- Two documents are plans from end to end rather than records with a tail —
  `docs/bayesian-scoring-plan.md` and
  `docs/journal/2026-10-24-scoring-strategy-test-plan.md`. They keep their detail,
  their pre-registered predictions and their kill criteria; what is OPEN in them is
  summarised under "The scoring rule's own test plan" below. The first sweep missed
  both, because it looked for forward-looking sections and these have no other kind.

New ideas go here. **There is no build plan and there is no frozen v0.1 scope**:
this line claimed both until 2026-10-30, and `v0.1` appeared exactly once in the
repository -- here. What ships in a release is recorded in `CHANGELOG.md` after the
fact, and `docs/state-of-the-project.md` says what the output is worth.

---

# Open work

## Before the next release

- **Scope verification**, the standing gate in `CONTRIBUTING.md` under "Releasing". It
  runs before every release, not once; this line stays open as the reminder. The first
  pass (2026-11-01, `docs/journal/2026-11-01-no-recent-data-scope-check.md`) covered the
  18 `no recent data` assays by hand and 61 more by script (the 30 `insufficient data`,
  the stale groups, every query naming a taxid, and `pending/`). What the next pass can
  skip re-deriving:
  - **Cleared, do not chase again.** (a) Duplicate rows: `calls.tsv.gz` (2026-10-31)
    repeats 70,095 of 3,462,260 (assay, record) pairs and some archives hold twice what
    their query returns (E. coli LT 122 vs 61), because two fetches a day apart both hold
    every record; `report.read_calls` keeps one row per accession before drift
    (`tests/test_report.py::test_calls_are_deduplicated_to_one_row_per_accession`).
    (b) Gene-titled bacterial queries that return 0-3 window records against
    31,850-3,202,443 for the taxon (E. coli LT and hlyA, Shigella ipaH, Y.
    enterocolitica): those taxa are on assembly retrieval (`config.yaml
    assemblies.taxa`), which supplies the recent records (Shigella ipaH 38 evaluable
    since Oct 2024, Y. enterocolitica 15). (c) Free-text name hits outside the taxid for
    Reptarenavirus, B. salamandrivorans, Paranannizziopsis and Ferlavirus: host genomes
    and salamander transcriptomes, not misfiled pathogen records.
  - **The watch list for test 2: queries that name a taxid inside their retrieval
    taxon**, the influenza mechanism. 11 entries outside influenza (whose four HA entries
    now share one broad query with `target.title_requires`): coronavirus RdRp x3
    (SARS-CoV-2, 2697049), LMBV x2, Mycoplasma turtles (three species), Panpox x2 (genus
    lists), EEHV3/4 x3, EEHV5 x3, EEHV6 x1. None blind on 2026-11-01. Closest: LMBV
    Grizzle's five taxids omit the species node `Ranavirus micropterus1` (3432136) that
    the Li 2025 entry names; 0 of its 59 window records sit at that node directly today,
    but a record filed there would be missed.
  - **`pending/`** (10 candidates): every query is current, 19 (Feline morbillivirus) to
    8,678 (Poxviruses polymerase) records in the window; none would enter with a blind
    retrieval. All 10 wait only on `doi_verified`.
  - **Not yet covered: scored verdicts.** The first pass checked undecided statuses
    only. In the 2026-10-31 run, 29 scored assays use `scope_taxids` (11 `declining`,
    7 `low coverage`, 11 `stable`) and 4 have a query naming a taxid (1 `declining`,
    1 `low coverage`, 2 `stable`). A `declining` or `low coverage` verdict can be made by
    a scope or query gone wrong as easily as `no recent data` can (NCBI re-filing a
    taxon moves records across a scope boundary). Test 4 at least on the 18 `declining`
    and `low coverage` with a scope, before the release that quotes them. The
    `CONTRIBUTING.md` gate says which assays; widen it to these if the test finds
    anything.
- **Narrow the Ophidiomyces query to the IGS.**
  `Ophidiomyces_ophidiicola_IGS_Bohuski_2015` targets the 28S-18S intergenic
  spacer, but its `target.query` fetches ITS, SSU and LSU titles: about 185 of the 196
  archive records (2026-11-01) can never carry the product. Change it to
  `IGS[Title] OR "intergenic spacer"[Title]`. Expected to move no result. Evidence
  (2026-11-01, `docs/journal/2026-11-01-no-recent-data-scope-check.md`):
  - Target is the IGS, not ITS: all 11 records it has ever scored (`detect`, 133 bp)
    are 28S-18S intergenic spacer sequences (KP691505-14, 2015; MT459829, 2020), and it
    has never produced a product on an ITS, SSU or LSU record. Only 11 IGS-titled records
    exist for txid1387563; none since Oct 2024, which is why the status is
    `no recent data` (its 55 recent records are all ITS/SSU, all `no_site`).
  - Genome assemblies stay excluded on purpose. The title filter excludes about 90
    (`datasets summary genome taxon 1387563`), one in the window (GCA_982397405.1,
    2026-04-10). Tiling the 1,306 bp IGS record of strain CBS 122913 (KP691505) in
    25-mers every 100 nt against that strain's own assembly (GCF_022830035.1): present
    over the first ~500 nt (28S end), absent over every IGS window; the assembly stops
    where the repeat's spacer begins. The 2026 assembly lacks even the 28S stretch.
    Neither has an exact primer match.
  A new query is a new retrieval group, so re-fetch and rescreen it, and do not change it
  during a run.

## Website and review (asked for 2026-11-04)

- [x] **Humanize the website's language.** Done 2026-11-04: the home page first, with the voice
  approved, then every other hand-written page and the sentences `site_render.py` generates. A
  script compared each page with its previous version: every number, link, code span and heading
  count is unchanged. Keep the voice when adding text; the composition sentences get read again
  when those pages go live.
- [x] **Check every assay's primer graph, then fix the broken ones.** Done 2026-11-04 over
  every assay in `website/data/run.json`. The bars themselves were right: every one lands on its own oligo and base,
  which `tests/test_site.py::test_every_bar_in_the_run_lands_on_the_oligo_it_belongs_to` now
  keeps true. Fixed: oligo names clipped at the left edge (69 of 492 names over about 12
  characters); 46 assays drawing sequences with no bars and no word about it, because the
  fallback sentence could never fire, now say why and, where relevant, how many records were
  missed (`Monkeypox_virus_G2R_Li_2010_G2R_WA_F`: 5,235 `fail` rows are `no probe site inside
  amplicon`, which have no position to draw); protocol pages now point at their rounds; and
  tooltips on the 8 pool assays whose bars come from an alternate oligo now say so.
- [x] **Check the scope of every assay with very few accessions.** Done 2026-11-04 for the 33
  under 30 evaluable records, without reopening papers:
  `docs/journal/2026-11-04-low-accession-scope-check.md`. 22 are low for honest reasons; the rest
  are below. The cut-off was a choice: 60 assays sit under 100.
- [x] **Do the Serpentovirinae PP1b entries belong, and at what scope?** Decided 2026-11-04: they stay, scoped to ball python nidovirus (1986118), with 2 moving to `insufficient data`. As first asked: The three Uccellini 2014
  entries target the subfamily, while the paper's primers are for ball python nidovirus: 13 of 14
  detected on that virus, and 96 of 114 calls elsewhere in the subfamily `fail`, which is why two
  of them read `low coverage`. These are
  genome-walking primers, so decide first whether they stay in the registry. If they do, scope
  them, reading `Serpentovirinae sp.` first, since that node may hold the same virus.
- [x] **Zimmermann round 2: score the corrected forward primer.** Entered 2026-11-05 and takes effect
  at the next screen. The status stays withheld, and the printed form shows on the page. Measured 441 bp
  in all 248 records with exact sites, against a published 444. Still open: Sorg 1995 and Kohno 1999
  might reprint the primer and have not been read.
- [x] **Francisella tul4 Long 1993: add probe FT443.** Entered 2026-11-05 and takes effect at the next
  screen, as `hybridization_probe`, because the paper reads a labelled probe by dot blot. Scored with
  penalties set for hydrolysis probes, which is an assumption and doesn't change this entry's calls.
- [ ] **Chlamydia assemblies: decide again, the check failed.** Maintainer decision of 2026-11-04 was
  conditional on genomes not being counted twice, and they would be. The `"complete genome"[Title]` term
  already reaches 379 of 493 assemblies under 810. Sampling 20 per year on top would count those again;
  dropping the term would swap all of them for a sample. Missing: 114, of which 70 are chromosome level
  and 42 *C. trachomatis*. Recommendation: leave retrieval alone. Not applied.
- [ ] **RefSeq and GenBank copies of one genome count as two records.** `NZ_CP017733` and `CP017733`
  have different accessions, so nothing dedupes them. On the 2026-11-01 calls 17 of 219 assays hold such
  pairs, 14 of them at 5% or more: *Mycoplasma* 16S 1,651 of 24,246, MTB IS1081 377 of 1,468, Messmer 127
  of 1,668. Only `complete genome` style queries reach them. Verdict effect not measured.
- [x] **Add *B. dendrobatidis* to `assemblies.taxa`, and give the Ghosh 2021 mtDNA entries a query?**
  Done 2026-11-04: neither. Tested in `docs/journal/2026-11-04-scope-reread.md`. A query would
  lose 30 of the 43 mitochondrial records, whose titles don't say so. At the current levels the
  assemblies add only JEL423, already archived. The low counts are honest; most records are
  `XM_` predicted mRNAs, not ITS.
- [ ] **Do BCV, CCV, PCV and RCV sit inside the Reid and Neill scope (3433198)?** Reread 2026-11-04:
  the one-species scope matches both papers; SMSV-8, SMSV-12 and mink failed in Reid and stay out.
  Family retrieval stays by maintainer decision: the archives are 14 and 10 MB, and the out-of-scope
  calls are what the eventual test across scope would read.
- [x] **Hellgren and `219829` "unclassified Plasmodium".** Done 2026-11-04: 1,269 lineages join the
  HaemF and HaemNFI scopes, chosen by the GenBank `/host` of all 9,159 records under the node, since
  names mislead. Left out: 117 with mammal or reptile hosts, 20 mixed, 109 mosquito-only, 295 with
  no host field, 23 unresolved. HaemNFI baseline stays near 88%; the whole node would have read 80%.
  The list goes stale as NCBI adds lineages, like the others.
- [x] **Leporipoxvirus into the Li 2010 IMV query.** Entered 2026-11-05 as `txid10270`, taking effect at
  the next fetch. Crocodilepox needs no edit: `txid1285599` is already in the RPO147 query, and the
  2026-11-04 journal line saying otherwise was wrong.
- [x] **The narrowing proposals.** Decided 2026-11-04: Uccellini narrowed; Baek, Ahmed, Steyn, Nix,
  Scaramozzino, Quan and Li left as they are, with the paper's narrower claim on the page instead.
  Tested table in `docs/journal/2026-11-04-scope-reread.md`.
- [x] **Correct the curator notes the reread contradicted.** Done 2026-11-05 for Lozano and Li IMV.
- [ ] **Messmer reports *C. trachomatis* amplified, and round 1 reads 0 of 301.** Unexplained.
- [ ] **Reread the remaining papers on scope, in batches.** Maintainer decision, 2026-11-04. About 86
  papers, starting with `declining` and `low coverage` assays. Budget about 24,000 subagent tokens
  a paper, 2 million in all, stoppable at any batch. Each batch brings claim sentences
  (`citation.claim`) for the maintainer to skim, and quotes checked against the paper.
- [ ] **Test for submission error, on unexplained `fail` clusters only.** Title against sequence was
  run on Bd, where it found one candidate (MT730717, remote BLAST never returned), and amplicon
  against label on Messmer 16S, where labels held. The method is in the same journal.
- [x] **Should withheld assays show a mismatch map?** Done 2026-11-04: yes, unless `review.MAP_HIDDEN` holds a flag of theirs, so Zimmermann round 2, Meyer ATI and *Ranavirus* Li 2025 stay hidden. As first asked: The 14 withheld assays have none, because
  `sitedrift.build` holds them out so they cannot be listed as failing, and their pages stop
  before the charts. That hides real signal (`Lyssavirus_N_Vazquez-Moron_2006_round1`: 10,588
  records differ at forward position 3), though a map drawn against an `oligo_sequence_uncertain`
  entry could mislead. Maintainer's decision, per withheld reason.
- [x] **Make assay paper titles uniform in case.** Done 2026-11-04. Some journals deposit titles
  at Crossref in capitals, 10 of 235 in `docs/papers-index.cache.json`. Those are now in normal
  case on the site rather than the other 225 in capitals, which would cost binomials and gene
  names their conventions. `site_render.TITLE_CASE` holds them, since the cache is regenerated
  from Crossref; a test checks each differs only in case, and fails on a new capitals title.
- [x] **The scope's taxid text export was broken.** Done 2026-11-04. All 48 download links were
  404s: MkDocs serves a page at `assays/<id>/` and leaves raw HTML links alone, so
  `<id>.scope.txt` resolved under the page's own directory. Protocol pages also had no files of
  their own. A test now resolves each link as the site serves it, and the built site's 4,684
  relative links all reach a file.
- [ ] **A thorough report on, and fix of, assay scope.** Goes further than the standing
  release gate above: every live assay's `scope_taxids` and query against what its paper
  says it detects, written up as a report, with the fixes made. 64 entries are done
  (`docs/journal/2026-11-04-scope-reread.md`, 21 broadened); the other live entries have not
  been reread. Two pieces belong to it:
  - **The nested malaria assay.** Read as the Hellgren 2004 haemosporidian nest; whether
    the paper behind `Plasmodium_18S_Li_1995` also describes a nest has not been checked:
    `Haemosporida_cytb_Hellgren_2004_HaemNFI`, `Haemosporida_cytb_Hellgren_2004_HaemF` and
    `Leucocytozoon_cytb_Hellgren_2004`, all three `nested_round: null`, so the site shows
    them as unrelated assays. The fix covers the three existing Hellgren items under
    "Waiting on a maintainer" (`amplicon_bp: 480`, the wording,
    the `oligos_not_in_cited_paper` flag) and has to handle one first round feeding two
    parallel second rounds with different scopes.
  - **How scope is shown on the website.** Done 2026-11-04: pages say what an assay is meant to
    detect, what it is scored against and where it was retrieved from. Entries not yet reread omit
    the first line until the batch rereads reach them. As first asked: how a page says what the
    assay is meant to detect, what it is scored against, and how that differs between
    rounds of a nest. The Chlamydia 16S query's falling share of its genus (0.4% of 2023's
    deposits, `docs/RESUME-HERE.md`) belongs in this report.
- [ ] **Assay page narrative.** At the top of each assay page, a description of the assay.
  Beside the lineage graph, a description of the lineages deposited over time and how the
  deposits may reflect outbreaks or other papers being published. Linking a deposit spike
  to an outbreak or a paper is an inference, so the page has to say what the evidence is
  (submitting study, publication, collection dates) and word it as "may". How that evidence
  is gathered, and whether by script or by hand for 200+ assays, is undecided. Depends on
  the composition stage's data (step 18 under "Lineage composition over time").
- [x] **Name gene targets uniformly across the assays.** Done 2026-11-04: 87 distinct strings to
  82, in 47 entries (the mapping is in that commit's diff). Many of the 87 were correct and stay
  different, since each virus keeps its own symbol (influenza NP, paramyxovirus N) and `ITS1` is
  not `ITS2`. What changed: the form (`symbol (product)`, `GLOSSARY.md` "gene name"), the same gene
  under two names (`terminase`, `gB`, `RPO147`, `F3L`, influenza `M1`), and coordinates and ortholog
  lists in the name, all already in each entry's `notes_curator`. A test holds the rule. Display
  only, but it edits registry files, so the next run re-screens those assays; it re-screens every
  assay anyway, because the screens' ids are stale.
- [ ] **`rule report` declares less memory than its table takes.** `mem_mb=3000`, against a
  3.17 GB peak from `load_calls_as_reported` alone on the 2026-11-01 calls (3,448,385 rows,
  measured 2026-11-04); its comment's 2.7M rows date from 2026-10-22. On SLURM that job is
  killed. Measure the whole rule and redeclare; `site_drift` reads the same table.
- [ ] **Eventually: test across scope.** Would an assay pick up what sits just outside its scope? The
  first case is the Hellgren haemosporidian pairs on gorilla and chimpanzee *Plasmodium*, which are
  left out of the bird scope on purpose. A question about cross-reactivity, reported apart from the
  drift verdict. Down the road, not for this release.
- [ ] **Per-assay composition cuts?** On the 2026-11-01 run at 0.05, 17 of 199 assays have a largest group of 3+ named
  species with no species at 80%, and the same-mix line can't see a shift inside it. Messmer gains
  from 0.02; Hellgren and *Leptospira* lose. Any override needs a stated reason in `config.yaml`,
  since tuning an assay until it looks right is the risk. Average linkage is the other thing to try.
- [x] **Security review and code review once the new lineage graphs are live.** Done 2026-11-05:
  no security finding at confidence 8 or above, 14 code review findings all fixed.
  `docs/journal/2026-11-05-review-fixes-rebuilt.md`.
- [ ] **Reconcile species names in the lineage groups.** Title names and taxonomy names don't match
  for one virus (*Human bocavirus* and *Bocaparvovirus primate1*), so a group can show a percent
  though it holds one species. Pages word this as several names until then. On the 2026-11-01 run, 42 of 201 assays have a
  largest group with a percent; how many are synonyms hasn't been counted.

## Waiting on a maintainer, minutes each

- [x] **Decided 2026-11-01: the registry stores published oligo sequences only.** Four
  oligos that no publication prints were removed and replaced with the sequences their
  cited papers print (`BORNA_VIRUS_N_gene` forward,
  `Dependoparvovirus_VP1_Gao_2002_2` both, `Mycoplasma_16S_unpublished`
  forward, `Entamoeba_18S_Garcia_2014` both). The schema now refuses
  `modified_from` without `modification_doi`. **A RESCREEN IS OWED** for the two that
  were live: the parvovirus entry's primers are narrower, so its detected share can only
  fall, and `BORNA_VIRUS_N_gene` dropped from `active` to `draft` with
  `oligo_sequence_uncertain`, because the printed primer gave 0 of 372 detections when
  tested on 2026-10-23 against 308 of 456 for the removed form. That entry now needs a
  human to re-read the 1994 scan: if the printed sequence is right, the assay fails and
  that is a real finding; if the scan is wrong, the entry has no usable published source.
- **Batravirus pan pair and Ranid herpesvirus 5.** A complete RaHV-5 genome (PV243667,
  2025-11-21, 221 kb) sits in "unclassified Herpesvirales" (taxid 3467605), outside
  txid3044671, so neither Licheri 2020 entry can see it. Found 2026-11-01 by a free-text
  search (`batravirus[All Fields]` over the window: 8 hits, 7 of them under the taxid).
  Those 7 are what the entries' query excludes from their own taxid: Bufonid
  herpesvirus 1, `UNVERIFIED`, unannotated, 90-192 bp (PV005823-29), all shorter than
  the 200 bp product, so excluding them changes nothing. Archive: 8 records, newest
  2019-02; query returns 8 all dates, 0 in the window. Does the pan pair's claim extend to it? If yes, the
  entry needs a second taxid in its retrieval, since a scope cannot reach outside the
  retrieval taxon (`docs/journal/2026-11-01-no-recent-data-scope-check.md`).
- **The G9R North American orthopox scope and borealpox.** Done 2026-11-04: borealpox (2602439)
  and the three NCBI species nodes are in scope, flagged `scope_wider_than_paper_tested`. Its one
  genome, MN240300, reads `fail`. No status moved (`docs/journal/2026-11-04-scope-reread.md`).
- **The Zimmermann 1994 Borna inner pair is entered twice.** `BORNA_VIRUS_N_gene` (live)
  and `Bornaviridae_N_Zimmermann_1994_round2` (draft) are the same inner pair (445 bp).
  The draft stores the forward primer as printed (`...TCTATCTTTC`), which the live entry
  measured on 2026-10-23 against no binding site in 1,516 Orthobornavirus records, so as
  stored it cannot detect anything. Proposed: retire the draft, rename the live entry
  `Bornaviridae_N_Zimmermann_1994_round2`, and set `nested_round` and
  `nested_family` on it and on the outer pair `Bornaviridae_N_Zimmermann_1994_round1`
  (round 1, 752 bp), which today read as two unrelated rows. A registry change: it
  changes the ids the report and website carry. Best done with the nested-protocol
  redesign under "Method debts".
- **Panpox (Li 2010): is Leporipoxvirus in the low-GC scope?** Settled 2026-11-04: yes. Table 1
  lists it as low GC, its abstract counts it among seven genera, and it amplified. The query edit
  goes in with the next fetch, listed above. Measured 2026-11-01: 36 records in the window, all
  Leporipoxvirus, would come in.
- **`Haemosporida_cytb_Hellgren_2004_HaemF` stores `amplicon_bp: 480`; the
  product measures 525** (4,269 of 4,274 products, `docs/journal/2026-10-05-amplicon-audit.md`).
  480 appears to be the length with primers excluded, the convention MalAvi and
  depositors use. The registry rule is that the measurement wins and the difference is
  disclosed (`amplicon_disagrees_with_paper`); this entry has neither. A registry change
  that may move calls, so rescreen and compare.
- **Describe the Hellgren haemosporidian assay as nested, not hemi-nested** (noted
  2026-11-03). Wording for `Haemosporida_cytb_Hellgren_2004_HaemNFI`,
  `Haemosporida_cytb_Hellgren_2004_HaemF` and `Leucocytozoon_cytb_Hellgren_2004`: "a nested
  PCR with a shared first round (HaemNFI/HaemNR3) and two parallel second-round reactions:
  HaemF/HaemR2 for *Plasmodium* and *Haemoproteus*, and HaemFL/HaemR2L for *Leucocytozoon*."
  The rounds share no oligo. The schema has no description field, so choose where it goes
  (`name` or `source.notes`). All three entries still have `nested_round: null`; declare the
  nest in the same change.
- **`Haemosporida_cytb_Hellgren_2004_HaemNFI` carries a wrong `oligos_not_in_cited_paper`
  flag** (noted 2026-11-03). Batya read Hellgren 2004 and the oligos are in it, as the entry's
  `notes_curator` already records; the flag's note is about the product size, since the paper's
  617 bp belongs to HaemNF/HaemNR2. Remove the flag, set `amplicon_bp` from 617 to the measured
  618, add `amplicon_measured_not_published` (the paper gives no size for this pair) and a dated
  correction in `notes_curator`. A size change may move calls, so rescreen and compare.
  `tests/test_report.py:522-531` uses this entry as its example of a displayed flag and fails
  once the flag is gone; switch it to `Salmonella_enterica_invA_Rahn_1992`. Do this before the
  nest above is declared, or its protocols inherit the wrong flag.
- **The `pending/` Hantavirus S-segment trio's nesting cannot be read from its ids**
  (`_S_segment_2` 532 bp, `_round2` 236, `_round2_2` 417). Declare `nested_family` and
  `nested_round` on each before any is promoted.
- **EEHV6's query names only taxid 768739** ("unclassified Proboscivirus"). When NCBI
  creates an `elephantidbeta6` species taxon, as it did for EEHV5 (3050275, which the
  EEHV5 query already names), add it to the query, or the archive stops growing silently,
  as the influenza subtype archives did. The release scope verification is what notices.
  Nothing is missed today (2026-11-01): the EEHV6 query returns 6 all dates, 0 in the
  window; the Proboscivirus genus has 49 window records, all EEHV1, EEHV1A (taxid
  759753, 43) and EEHV4 by taxid; and a free-text search for EEHV6 /
  "endotheliotropic herpesvirus 6" / `elephantidbeta6` over the window returns 0. EEHV5
  likewise: 0 by query, by taxid and by name.

- **The 34 `scope_taxid` values**, one read per row from the row's OWN source paper:
  which lineage did that paper's positives belong to? The population, the rule behind it
  and the reading order are in `docs/2026-10-30-scope-worksheet.tsv`; the column now
  exists in all three case files. A guessed lineage is worse than a pooled score, so a
  paper that does not say leaves the row blank and says so. **34 rows over 17 assays and
  34 papers** -- 17 development, 10 held-out set 1, 7 held-out set 2 -- and 11 of them are
  `fails` rows, where a scope can turn a catch into a miss.

- ~~**Four influenza entries wait in `pending/` for sign-off**~~ — **SIGNED OFF, PROMOTED AND
  SCORED 2026-10-30** (`docs/journal/2026-10-30-set3-scored.md`). All four are in `registry/`;
  the validator reads 218 live and 10 pending, both clean. The H3 group was fetched (44,627
  records, `q2fad34153e`) and the four assays screened.

- **Held-out set 3 is SCORED and SPENT, and the tool caught its first drift case.**
  `Influenza_A_virus_M1_Ward_2004` reads `declining` as of 2013-09-06 (86.2% of 5,847 recent
  records, upper bound under the 90% threshold, change from baseline -6% to -4%), which
  **agrees** with Yang 2014. **This is the first documented failure the project has ever
  caught by the drift flag itself** rather than by `low coverage`, so the premise the tool
  rests on has a confirming case. The control that makes it worth trusting: on the same
  records at the same date the documented redesign `Influenza_A_virus_M1_Yang_2014` reads `stable`
  at 91.6%, and the two entries differ in nothing but their oligos. PPV of `declining` on
  this set is 1/1 and failures caught 1/2; both intervals are one row wide and are not
  precision estimates.

- **THE INFLUENZA RETRIEVAL QUERIES NEED A DECISION, AND TWO LIVE ENTRIES ARE AFFECTED.**
  Measured 2026-10-30: every influenza group whose query names subtype taxids has an archive
  that ended years ago — H5 Tsukamoto `q6552a5c4af` newest deposit **2021** (8,490 records),
  H7 Tsukamoto `q3b4e39b708` newest **2020** (3,425) — while the title/gene groups are current
  to 2026 (matrix 187,534; NP 194,149). NCBI has stopped assigning subtype taxids to new
  influenza deposits: the seven H3Nx taxids AND HA return **0** records for 2024-2026 against
  **95,155** without that restriction. **So the H5 and H7 verdicts in every report this
  project has produced read `no recent data`, naming the Oct 2021 cutoff, so no wrong verdict
  was ever published -- but neither assay can show recent drift by construction, and the message
  reads as a fact about the taxon where it was a fact about the query.** This is what made set 3's Shu row unjudgeable.
  **The obvious fix is wrong**: broadening to `txid11320 AND HA` makes the denominator every
  influenza A hemagglutinin record, so a correctly specific subtyping assay would read as
  detecting a small share of its own archive and look like it was failing — which is the
  `scope_narrower_than_taxid` problem the subtype restriction existed to avoid. What these
  assays need is their records restricted to their subtype by something other than a taxid
  NCBI no longer assigns: the strain name in the record title, or the scope layer. A
  maintainer's call, with the measurement above attached.

- **The matrix archive's metadata mostly predates the `taxid` column**, so its lineage layer
  sees one lineage and no per-row scope on it can be honoured. 18 of 19 metadata files in
  `q2ebd5918b3` have no `taxid` column at all, and the one that does reports all 4,009 of its
  records as the parent `11320`. Refetching the group under current code is the fix for the
  missing column; whether influenza records resolve below the species at all is the question
  above. **Consequence recorded against set 3: it was opened as the first genuine test of the
  scoped matrix and could not be one.** A scoped matrix is still untested and needs a set 4 on
  an assay whose archive resolves below the species.

- ~~**ONE DECISION BLOCKS `Influenza_A_virus_HA_H3_Shu_2026`**~~ — **TAKEN AND SHIPPED
  2026-10-30** (`docs/journal/2026-10-30-citation-year-rule.md`). `papers.citation_matches`
  now reads a year from the reference text as well as `design_year`, which
  `citation_problems` already did; both share `papers.year_agrees`, so the repository no
  longer answers one question two ways — the gate that sets `doi_verified` had been refusing
  an entry the CI gate passed. **Measured before shipping (2026-10-30): over every entry whose DOI
  was in the Crossref cache that day, 220 entry-DOI pairs, no verdict moves either way.** The loosening is stated in the journal rather than
  buried: a four-digit number in a reference text that is not a year can satisfy the check by
  accident, and that was already true of CI. All four influenza entries now verify, and
  **held-out set 3 has both drift rows**.

- **`doi_verified` is held FALSE on the three entries Crossref did verify**, because "live"
  here means a verified DOI and nothing else: `not_live_because` ignores `status`, so a
  verified entry sitting in `pending/` reads as live and
  `test_nothing_in_pending_is_live_and_nothing_in_registry_is_pending` fails on it. A
  sign-off gate and a true flag are mutually exclusive. Each entry records the resolution, and
  `curate` re-sets the flag in one command at promotion.

- **Nothing else, as of 2026-10-30.** Nine calls have been taken across two sittings and
  are recorded in `docs/journal/2026-10-30-decisions.md` and
  `docs/journal/2026-10-30-decisions-round-2.md`: S7b shipped; the twelve proposed rows
  accepted and set 2 spent; `Caliciviridae_helicase_Neill_1995` stays `draft`; the
  2026-10-30 stack merged to `main`; the `scope_taxid` population fixed by registry
  property with the agreement rule left alone; **the repo is public** (2026-10-30, history
  scanned for keys and copyrighted PDFs first, both clean); the full nuccore
  collection-date backfill approved and started; and the drift-mechanism search routed to
  a fresh session.

## S3b, shipped 2026-10-27, and what it still owes

- **S3b is live: `by_chemistry.conventional.primer_3prime_penalty: 2.0`** (2026-10-27).
  `strategies/s3b-conventional-3prime-penalty.yaml` drops `primer_3prime_penalty`
  from 3.0 to 2.0 for `conventional` only. It is **priced, not proven**
  (`docs/journal/2026-10-27-terminal-mismatch-refuted-penalty-priced.md`):

  - bench panels: fixes 6 of 179 rows, breaks 0, McNemar exact p = 0.0312, and
    none of the 16 negatives that can punish a loosening moves. Nothing is fitted,
    so that is not an in-sample figure;
  - registry replay over 2.72M rows: 19,081 calls move, every one `fail` ->
    `reduced`; documented failures caught stays 6/11; the PPV of `declining` goes
    2/9 -> 3/9 and false alarms 5/32 -> 4/32, because exactly two tier-2 cases move
    and they move in opposite directions on purpose.

  Both pre-registered kill criteria survived, and the confirming rescreen covered
  **6 of the 84 affected assays, 280,818 rows, 0 call disagreements**, i.e. 14,261 of
  the 19,081 moved calls (74.7%) including both assays that carry a verdict move. The
  91 penalty differences all run pessimistic — the real screen finds a better
  candidate than a replay can see.

  **What it still owes, now that it is live:**

  - ~~The next full pipeline run has not happened yet~~ — it ran the same night
    (`results/2026-10-27/`, committed as `docs/example-run-2026-11-01/`; see Operations).
    16 statuses moved, the probe switch's and S3b's among them. Closed 2026-10-30, when the
    roadmap was reconciled against the repo.
  - ~~78 small movers were never rescreened~~ — the 2026-10-27 run rescreened
    everything, and the replay agrees with it on all but 8 of 2,679,894 shared rows
    (6 `fail` -> `no_amplicon`, 2 `fail` -> `reduced`, none on a tier-2 case). Closed.
  - **2.0 is coarser than the evidence deserves.** Kwok 1990 and Stadhouders 2010
    both report that the cost of a mismatch depends on its IDENTITY, which
    `scoring.mispair_penalty` can express per pair and a single positional number
    cannot. 2.5 was priced on the same rows and fixes only 2 of the 6.

  **Why this item no longer names `terminal_mismatch_fails`.** For three weeks it
  did, and the 23 false negatives against 1 false positive were read as its
  evidence. Scored directly, exempting conventional chemistry from it moves **0 of
  179 bench rows** — the same answer the 2026-10-26 registry-wide measurement gave
  from the other end (251 calls of 2.7M, no verdict changed), because a record whose
  primer carries a terminal mismatch almost always carries others that already
  exceed `reduced_max`. The pessimism is real; that knob is not where it lives.

  **The threshold coincidence is why the penalty is the live suspect.**
  `primer_3prime_penalty: 3.0` equals `reduced_max: 3.0`, so one mismatch anywhere
  in the last five bases lands precisely on the detect/fail boundary — and 74.7% of
  all 284,062 `fail` calls sit within one 3'-window mismatch of it (2026-10-27 run).

  **One figure from this item's history must not be quoted.**
  `Caliciviridae_helicase_Neill_1995` was read as carrying a 3'-terminal
  mismatch in Hel1 against all 16 of its own target records, and
  `terminal_mismatch_fails` alone was said to drive it to near-total failure
  against a paper reporting the assay working. That mismatch was an error in our
  stored copy of the oligo, not a chemistry effect. The 2026-10-24 correction of
  Hel1's 3'-terminal base from G to C — the form the template carries in all 16
  design targets, and the only form that reproduces the published 357 bp product
  — removed it. **Do not quote "0 of 30".**

## The scoring rule's own test plan, which this file did not list until 2026-10-27

The scoring method has a ladder of candidates and a kill criterion for each, written
down on 2026-10-24 in `docs/journal/2026-10-24-scoring-strategy-test-plan.md` Part 1,
and a three-project Bayesian plan in `docs/bayesian-scoring-plan.md`. Neither was ever
in this file — the consolidation of 2026-10-27 swept the forward-looking TAILS of
journals and missed two documents that are forward-looking from end to end. What ships
today is the **budget rule**: a position-weighted additive penalty, binned at
`detect_max` 1.0 and `reduced_max` 3.0, with `terminal_mismatch_fails: true` and, since
2026-10-27, a 2.0 3'-window penalty for conventional PCR.

- **S5 = C2: the Bayesian per-record model, and it is GATED.**
  `P(detect) = P(fwd ok) x P(rev ok) x P(probe reports)`, each logistic over identity,
  position, adjacency and length, with chemistry as a hierarchical intercept and priors
  from Kwok and Stadhouders. **The gate is at least 40 within-family negatives across
  several independent papers; there are 11.** Below 40 it is not fitted, and nothing
  fitted on 11 would be defended. So the blocker is the corpus sweep — the same
  literature pass as held-out case collection, one read per paper for both — and not
  the modelling. C2 is also what `docs/related-work.md` would need before claiming a
  probabilistic matcher.
- **Done, so that the list is not read as "no Bayes anywhere": C3**, the Bayesian
  treatment of the validation matrix, ships — every proportion `scripts/retrospective.py`
  prints carries a Jeffreys interval, which is why the tier-2 figures read "3/9 = 33%
  (95% CrI 10%-65%)" rather than a bare percentage.

- **S7b: SHIPPED 2026-10-30, `scoring.mispair_window: 10`**, priced 2026-10-29
  (`docs/journal/2026-10-29-s7b-priced.md`), decided and recorded in
  `docs/journal/2026-10-30-decisions.md`. It passed all three pre-registered criteria:
  tier-2 identical case for case, bench 166/179 -> 167/179 (PPRV Nigeria75/1), and no
  within-family negative gains a band. 31,237 calls move in the replay, all loosening. The
  maintainer took the decision on the bench row and the separation criterion, knowing that
  the report also drops 7 flags (5 assays), one of them held-out set 2's false alarm, and
  before set 2's eleven unscored rows were read. ~~**What it still owes: the confirming
  rescreen**~~ — **PERFORMED 2026-10-31** (`docs/example-run-2026-11-01/`). All 580-odd
  archives rescreened, and the one pre-registered prediction landed:
  `Monkeypox_virus_G2R_Li_2010_G2R_G_F`, held-out set 2's single false alarm, moved
  `declining -> stable`. Across the run 11 assays changed status, every one an improvement
  or an unblocking: `stable` 60 -> 72, `watch` 8 -> 5, `low coverage` 34 -> 31, `no recent
  data` 20 -> 18, `declining` unchanged at 42. S7b is closed.

Dead, and recorded so they are not re-proposed: **S1** serial per-oligo gates (no
threshold pair passed its own criterion, 2026-10-26), **S2** a smooth positional decay
replacing the 5/5/rest step (2026-10-26), **S6** the Kwok premium on severe mispairs
(breaks a bench row and adds a false alarm for no catch, 2026-10-27), **S7** halving the
mid-window penalty (identical tier-2 and identical 92.7% bench accuracy, and it newly
predicts a band on two within-family bench negatives, 2026-10-28), and the
**thermodynamic** engine, which has never been a scoring input and whose measured
advantage over the penalty rule evaporated once its register was fixed (2026-10-27,
p = 0.019 -> 0.071). **S4/M1 shipped** 2026-10-27.

## Operations

- **The weekly re-screen is installed on this machine only** (2026-10-27, live,
  Sunday 09:00, lid open; `docs/journal/2026-10-27-live-run-and-schedule.md`). It is
  machine-local state: the other MacBooks are not scheduled, and README's "re-screens
  on a schedule" is true of exactly one laptop. `scripts/weekly_run.sh --live` now
  refuses a tree with uncommitted changes under `assaywatch/`, `config.yaml`,
  `registry/` or `Snakefile` (`--allow-dirty` overrides, knowingly) — the guard the
  second failed run of 2026-10-27 needed, proved to fire on an untracked probe file.
- **The full run under today's scoring exists**: `results/2026-10-27/`, committed as
  `docs/example-run-2026-11-01/`. 16 statuses moved against 2026-10-26, the probe
  switch's and S3b's among them, and the S3b replay was checked against it row for
  row: 8 call disagreements in 2,679,894. **Owed by that run**: the groups of the 31
  entries edited afterwards (28 orientation notes, 3 renames) and the five new mpox
  entries rescreen on Sunday, because the signature hashes the registry.

  **Two runs on 2026-10-27 failed at `collect_calls`, and the second was self-inflicted.**
  The first found 461 of 482 cached screens stale against the new scoring config —
  Snakemake held no metadata record for them, so its params trigger never fired, and
  the signature guard in `collect.py` was the backstop that caught it (correctly: delete
  and rerun). The second rescreened all 461 and was refused at collect because
  `settings.py`, `config.yaml` and other modules in the screen hash's import closure
  were edited and committed WHILE IT RAN, so every fresh screen carried a signature the
  pipeline no longer expected by the time it was read. The guard cannot tell an
  innocent mid-run edit from a stale cache, and should not try. Both halves of the fix
  are in: `scripts/weekly_run.sh` refuses `--live` while any path under `assaywatch/`,
  `config.yaml`, `registry/` or `Snakefile` is dirty, so a scheduled run never starts on
  a half-edited tree; and the rule for the human is that nothing in that closure is
  touched until the run reports.
- **Two inert switches, grouped here because each is the same shape**: a mechanism
  built, tested, and shipped off for want of evidence.
  `lineage.unclassified_is_bucket: false` (tier-2 is unchanged by it, so there is
  nothing to ship it on) and `thermo: false` (needs the annealing conditions the
  registry does not carry). Two have left the list by being turned on:
  `scoring.mispair_penalty` carries the G:T / T:G discount (M1) and
  `lineage.sublineage` carries the influenza chain, both 2026-10-27. None is a
  defect. The list exists so that "the mechanism is here and the numbers are not"
  stays a count rather than a feeling.

  Two switches that were listed here on 2026-10-27 do not belong: they are not
  waiting for evidence, the evidence came in against them. `scoring.engine: serial`
  is S1, rejected 2026-10-26. `scoring.locus_identity_min: null` was built, priced at
  0.50 over the 2026-10-25 run and **rejected the same day**: it throws out 1,840 of
  9,687 sampled failures, concentrated exactly where it must not — `Pan_HERPES`
  loses 47 of 47, because for a pan-family or consensus assay a divergent amplicon
  interior is what SUCCESS looks like
  (`docs/journal/2026-10-25-locus-identity-design.md`). Both are in the dead list
  under the scoring test plan above, and `locus_identity_min` must stay null.

## Method debts

- **Plasmid and pathotype genes are screened against a random species sample.**
  Assembly retrieval takes up to 20 E. coli genomes per release year with no pathotype
  enrichment, so `Escherichia_coli_LT_Victor_1991` finds no binding site in 315 of 325 sampled
  rows and `Escherichia_coli_hlyA_Wang_1997` in 291 of 325 (2026-10-31 run). Their
  `insufficient data` (1 and 2 evaluable records) describes the sample, not deposition.
  Options: a per-assay assembly filter (serotype or pathotype in the BioSample), or a
  disclosure on the status. Design question; the same will hold for any plasmid-borne
  target on a species-level assembly sample. **NCBI can supply them, but not at the
  levels sampled** (measured 2026-11-01): BioSamples from the window with serovar O157
  link to 6,086 assemblies, of which 5,975 are contig-level, 108 scaffold, and only 3
  complete or chromosome-level. ETEC: 3 complete or chromosome-level. So the fix is a
  BioSample filter plus admitting contig-level assemblies for these assays (hlyA sits
  on the pO157 plasmid, which contigs carry), not a second database.
- **Sources beyond GenBank: add one only where a named assay needs it.** Most candidate
  databases are derived from INSDC (GenBank/ENA/DDBJ) and add no sequences; one earns a
  place by supplying sequences INSDC lacks, or curated labels that fix a known scope or
  lineage problem. Each is a second retrieval source, so the retrieve stage's interface
  changes: grill and approve the interface before any adapter. Cheap tests 2026-11-01
  (`docs/journal/2026-11-01-no-recent-data-scope-check.md`):
  - **MalAvi: no screenable sequences, possibly lineage labels.** Its standard lineage
    fragment is the HaemF-HaemR2 product with the primers trimmed, which is what
    depositors do as well: of 5,488 haemosporidian cyt b partials deposited 2023-2026
    (`txid5819[Organism:exp] AND "cytochrome b"[Title] AND 300:700[SLEN] AND
    2023:2026[PDAT]`), the commonest lengths are 477, 479, 478 and 475 bp, and only 73
    contain the 3'-terminal 12 nt of both HaemF and HaemR2 (229 forward, 218 reverse). A
    sequence without its primer sites cannot be screened against that pair. What MalAvi
    could add is its curated lineage names for `lineage.py`. Its server did not answer
    from this machine on 2026-11-01; untested beyond that.
  - **EnteroBase: not needed for E. coli selection** (see the plasmid item above; NCBI
    BioSample serovar does it). Might still matter for serotype calls where BioSample
    metadata is missing.
  - **GISAID: the biggest potential gain, for the four influenza HA entries, and a
    licence question first.** Access needs an agreement and restricts redistribution;
    whether per-record calls in a public repository are compatible must be read in its
    terms before any measurement.
  - **PR2 / SILVA** for the Perkinsea NAG01 scope (labels for environmental 18S), and
    **UNITE** for fungal ITS entries: labels, not sequences. Untested.
- **A script for the release scope verification** (`CONTRIBUTING.md`, Releasing), so
  tests 1-4 are one command rather than hand-written shell. The 2026-11-01 sweep used a
  scratch version; its lesson for the interface: the name search must be free text, since
  `"<name>"[Organism]` resolves to the same taxid and returns 0 by construction. The
  scratch version's flags, which worked: query sees 0 window records while the taxid has
  some; taxid window more than 3x the query window; archive more than 10% behind the
  query's all-dates count; newest archive deposit before the window; query names a
  taxid; scope empty in the window. The first two over-fire on gene queries under
  genome-depositing taxa and on bacteria with assembly retrieval; the third never fired,
  and the incremental archive's duplicate records make it less sensitive (count unique
  accessions instead). Read every flag; none is a verdict. The
  script's inputs, outputs and flags are the maintainer's to approve first.
- [x] **Nested protocols are evaluated as protocols** (2026-11-01, design grilled then
  built in three steps; `docs/nested-protocol-plan.md`). A nest is a PATH keyed on its
  terminal round, scored through the same assessment as an assay with the same threshold
  and words, scoped to the intersection of its rounds, withheld when any round is, and
  given its own row, page and count on both the report and the website. Declared
  parentage replaced the id-suffix guess that had mis-paired two families: 67 rounds in
  32 families, 34 protocols, nothing ambiguous. 31 publish a verdict on the 2026-11-01
  calls -- 8 declining, 5 low coverage, 11 stable, the rest undecided -- and these were
  invisible before: `Polyomaviridae_VP1_Johne_2005_round2` completes on 0.2% of 3,260
  records and `Chlamydia_trachomatis_16S_Messmer_1997_round2` on 0.0% of 363, against
  its psittaci sibling at 100%. Still open, both small: whether a nest may carry its own
  `needs_review` flags rather than only inherit them, and how `report_diff` should
  present ~31 rows appearing at once on the first run that includes them.
- **One mid-window mismatch is the boundary, and it drives 69 sites on 23 assays**
  (traced 2026-10-28, `docs/journal/2026-10-28-g2r-false-alarm-traced.md`). Held-out set
  2's one false alarm has a single mechanical cause, followed to the base: the 2022-era
  monkeypox records carry a G:T wobble at position 8 of the G2R reverse primer and an A>G
  at position 21 of the forward, which price at 1.0 + 0.5 and cross `detect_max: 1.0`, so
  8,947 records score `reduced` — and for a hydrolysis probe `reduced` is not a detection.
  M1's identity discount prices G:T at 0.0 but applies only inside the 3′ window, by the
  measured decision of 2026-10-22. Every step is deliberate; together they say a primer
  with one internal wobble detects nothing, where Mills 2022 validated the assay
  clinically.

  **The generalisation is the item.** `primer_mid_penalty: 1.0` equals `detect_max: 1.0`,
  so one mid-window mismatch sits exactly on the band boundary and a second anywhere
  pushes past it — the same coincidence already recorded for `primer_3prime_penalty: 3.0`
  against `reduced_max: 3.0`. Over the run's site table, **69 sites across 23 assays**
  show a non-3′ mismatch carried by ≥200 records where detection falls from >80% to <20%,
  split 36 on `low coverage` assays and 33 on `declining` ones.

  **What may and may not settle it.** Not the Mills row: tuning on it would make held-out
  data a second development set. The bench-panel question was MEASURED 2026-10-30
  (`docs/journal/2026-10-30-mid-window-on-the-bench.md`): sweeping `primer_mid_penalty`
  over 0.0–2.0, **8 of the 179 rows change their band/no-band prediction**, so the
  parameter is not unmeasurable as this item supposed — one bench row does turn on it. But
  **all 8 sit in `fitting` panels**, the ones a model may be tuned on; the single `control`
  panel (specificity only, never fittable) is unmoved at every value. So the bench still
  cannot *settle* the value without fitting on exactly the rows reserved for fitting:
  agreement is 162–163 of 179 flat across 0.0–1.0 and only falls above it (FN-dominated, as
  everywhere here), which rules out the high end but does not choose between 0.0, 0.5 and
  the shipped 1.0. A second held-out row is still what would settle it, and 22 of those 23
  assays are not monkeypox.

- **An archive can go quiet without anything complaining, and the guard for it is weak.**
  `scripts/check_archive_recency.py` (2026-10-30) lists every group whose newest deposit is
  older than 18 months, loudest where a SIBLING group under the same taxid is current -- the
  comparison that found the influenza case by hand. **Its value is measured and modest.** Run
  against the registry it returned four sibling-gap candidates and **all four were fine**,
  cleared by one `esearch` each: three hold exactly what their query can return (MTB
  helicase 25/25, EEHV5 20/20, EEHV6 6/6) and the fourth holds more than its query now
  returns (E. coli LT 122 against 62). A narrow gene query under a well-deposited taxon
  always looks stale beside a broad one.

  **And it would not have isolated the influenza case either**: that group held 44,627
  records against a query returning 44,633, so query and archive agreed exactly while the
  query's definition had gone blind. No comparison of a query against itself can see NCBI
  changing an annotation practice at the far end. What the script buys is a short list -- 13
  groups of 134 -- with the numbers to clear each by hand, which is how the case was found.
  A `--probe` flag was built and removed: it needed the network, and a switch that looks
  like a verdict while being unable to deliver one is worse than a documented command.

- **A lexicographic sort over `results/` picked the wrong runs, for the second time**
  (fixed 2026-10-31). `report_diff.py` took the last two of every directory holding a
  `report.md`, and letters sort after digits, so it chose `2026-10-31` as the OLD run and
  `baseline-2026-10-22` as the new one. The release run's own summary therefore diffed two
  directories it had nothing to do with and reported the four newly added influenza entries
  as having **vanished** from the report — misleading in the one direction that matters,
  since it invented a regression. It now accepts only directories named exactly
  `YYYY-MM-DD`, with a test.

  **The point worth keeping is that this was the second instance.**
  `backfill_collection_dates.newest_run()` had the identical bug and read a five-day-old
  baseline run for a whole fetch (2026-10-30); it was fixed in place and no one looked for
  siblings. `results/` holds experiment directories beside dated runs, so any code picking
  "the newest run" by sorting names is wrong here.

- **`printed.py` cannot verify a probe whose internal quencher is written inside the
  sequence** (found 2026-10-30 while curating the CDC H3 pair). Shu 2026 Table 1 prints
  `CAG GAT CAC /ZEN/ATA TGG GSC CTG TCC CAG`, so `printed_oligos` never sees the 27 bases as
  one run: it returns the 18-base tail after the marker and drops the 9-base head below
  `PRINTED_MIN_LEN`. Both probes of both H3 entries therefore read `absent` while all four
  primers read `exact`. The bases are in the paper; the scanner cannot assemble them. This
  will recur -- ZEN, BHQnova and LNA double-quenched probes all print this way -- and the fix
  is to strip bracketed or slash-delimited modification markers before scanning, which is a
  change to a verification path and wants its own test. Not built.

- **The 30 refused assays are refused on the POOLED recent count, not per lineage**, so
  the hierarchical layer cannot reach them: `min_records_for_drift` gates `finalise`
  before any lineage is looked at. **Designed 2026-10-27 as C1b** in
  `docs/bayesian-scoring-plan.md`, with its two kill tests pre-registered, the
  alternatives priced and rejected, and the cost stated — it borrows a prior across
  assays of one chemistry, which are not exchangeable in any honest sense, so the prior
  does real work where the within-assay layer's barely did. Not built. What it would be
  worth: tier-2 declines to judge 3 of its 11 documented failures, which is the whole
  difference between "6/11 caught" and "6/8 among the cases it judged at all".

- **The trend test counted clones as evidence, and 35 of 64 significant declines do not
  survive the correction** (built 2026-10-30, `docs/journal/2026-10-30-footprint-trend.md`).
  A second Cochran-Armitage trend over distinct footprints per year now prints beside the
  by-record one. On the 2026-10-27 run: 710,427 records become 39,640 footprints, assays with
  p < 0.05 go **64 -> 32**, the median |z| ratio is 3.3, and **23 of 74 disagree on
  direction** (the report says so in those rows). One assay goes from p = 0 on 90,291 records
  to p = 0.63 on 1,953 footprints. Read by-record as an upper bound on the evidence and
  by-footprint as nearer a lower bound: a sequencing error in a primer site mints a footprint,
  and clade structure beyond the sites is invisible to it. Neither feeds the verdict. **What is
  left**: nothing is owed here, but the same correction is not applied to the per-year table's
  shares or to the lineage tests, which remain per record.
- **Deposit date is not collection date, and the lens that shows it is BUILT** (2026-10-30,
  `docs/journal/2026-10-30-collection-year-lens.md`; measured 2026-10-27,
  `docs/journal/2026-10-27-deposit-vs-collection-date.md`). Not a switch: a report-wide
  section re-dates each assembly record by its collection YEAR and recomputes the recent share
  beside the deposit-clock one. On the 2026-10-27 run the share barely moves (E. coli malB
  56.7% of 60 -> 64.0% of 25, every 100% stays 100%) and the sample does: the recent
  denominator shrinks by half to two thirds once a record is dated by when its isolate
  existed, so the backlog narrows the verdict's interval rather than manufacturing a decline.
  **Priced and started 2026-10-30** (`docs/journal/2026-10-30-decisions-round-2.md`):
  nuccore keeps `/collection_date` in the flatfile's `source` feature and nowhere else, so
  `scripts/backfill_collection_dates.py` fetches records rather than summaries, one base of
  sequence each, into a gitignored sidecar that touches nothing the weekly job guards.
  The month-year regex is **fixed** (2026-10-30): `collection_year()` now reads 98.97% of
  7,687 fetched dates, and all 79 it refuses are ranges, refused on purpose.

  **Three corrections to what this item claimed on the day it was written**, all found by
  reading the fetch's own output instead of trusting its summary line:

  - The rate was never ~150 records/sec sustained, and the fetch was never throttled. The
    progress line printed a cumulative average since start, so a slow opening dominated it
    for tens of thousands of records: a run at 69 records/sec with 4.5 hours left reported
    0.8 and an ETA of 400+ hours, **and was stopped on that reading**. Fixed (PR #25) to
    report a 120-second window and print both figures.
  - `newest_run()` sorted run directories lexicographically, and `'b' > '2'`, so it read
    `results/baseline-2026-10-22` instead of `results/2026-10-27` -- the whole backfill was
    working a five-day-old run's accession list. Fixed in the same PR.
  - 425 record ids are shaped `pdb|29TK|N` and are not accessions at all; they are now
    settled unasked.

  **Left**: the fetch itself, resumed 2026-10-30 against the correct run. The date rate is
  **not** the 75% first sampled -- of 147,200 records settled so far, 50,963 carry a date
  and 96,207 do not, because the early accession blocks are patent-era deposits that carry
  none. `report.collection_sidecar` stays null until the fetch finishes.
- **`target.exclusivity_taxids`: three sets in, and the rest is one paper at a time**
  (2026-10-28). `scripts/extract_exclusivity.py` prints every sentence in which a paper
  claims its assay does NOT amplify something — **118 of the 178 papers on disk carry at
  least one** — and most are not usable as they stand: a pan-family paper's claim is
  usually about antibodies or "unrelated agents", and the 17 assays whose reports show
  out-of-scope records are showing within-family taxa and synthetic constructs that no
  paper claimed to exclude. What is usable is the species-specific assays, where the paper
  names the neighbour it must be told apart from. BPSV, the two Huo 2022 F3L mpox entries,
  the ORFV entry and the generic PAPV entry now carry them (134 retrieval groups, up from
  125); seven of the nine new groups hold nothing until the next run fetches them. What is
  left is reading, and the retrieval cost is the thing to weigh — each named taxon is a
  new archive, though the orthopox set is only 3,772 records.
- **Tier 2: retrospective validation.** Assemble assays with published
  follow-up — a paper, erratum or redesign reporting the assay failing on
  particular lineages, or reporting it still working — and ask whether
  AssayWatch flags what the literature found, using only records deposited
  before that paper. That gives a confusion matrix, and the thresholds become
  whatever optimises it rather than whatever looked sensible. **Every number in
  `config.yaml` is a placeholder set by eye**, so until this exists the
  statuses read as "worth looking at", not as measurements. It is also the
  paper's main figure.

  **The binding constraint was identity, and with every PDF in it is now CONTENT.**
  `scripts/check_candidate_identity.py` over the `mismatch`/`redesign` rows read 1
  CONFIRMED / 1 VARIANT / 11 UNCONFIRMABLE on 2026-10-27, with 6 of those waiting on a
  PDF. All six arrived 2026-10-28 and the queue now reads **2 CONFIRMED, 1 VARIANT, 10
  UNCONFIRMABLE** (`results/retro-identity-2026-10-28.tsv`) — and **not one of the newly
  readable papers prints our oligos**. Tsukamoto 2008 prints 29 and Csordas 2004 prints
  12, none ours; the second CONFIRMED (Süß 2009 on the Salmonella invA pair) is a
  synthetic-template mismatch study and not a case at all. So this queue is spent: no
  document will settle the remaining rows, and the next tier-2 rows have to come from a
  different search rather than from more fetching.

  **Where they will come from instead.** Quackenbush 1998 was in the batch as a
  *completeness* paper and turned out to be a tier-2 candidate — it uses the pan-herpes
  nest and reports what it found. That is the pattern worth exploiting: the citing-paper
  graph was searched for phrases about FAILURE, and a paper that simply USES a registry
  assay and reports a result is just as scoreable. `scripts/find_retrospective_cases.py`
  could be re-run for use-and-report language, which is a cheap change to a script and
  the only lead left that does not need new PDFs.

  **That re-run happened 2026-10-29 and it worked.** `--include use` (the opt-in phrase
  family) returned 248 candidate rows, 93 of them `use`, and
  `check_candidate_identity.py` over that family read **13 CONFIRMED (paper, assay) pairs
  over 7 papers, 3 VARIANT, 153 UNCONFIRMABLE** — against 2 CONFIRMED in the whole
  project before. Worksheet: `<scratch>/identity-use.tsv`. The seven papers, every oligo
  `exact`: Orthoherpesviridae_POL_VanDevanter_1996_round1 (+round2) in 10.5455/ovj.2024.v14.i1.48,
  10.1080/01652176.2022.2149879 and 10.1186/s12891-020-3052-8;
  CORONAVIRUS..._round2 in 10.1093/ve/veab110; Leucocytozoon_cytb_Hellgren_2004,
  Pan_Plasmodium... and Pan_hemoparasite... in 10.1186/s12936-021-04019-z;
  Astroviridae_RdRp_Chu_2008 (round1+round2) in 10.4142/jvs.2021.22.e84;
  Adenoviridae_hexon_Casas_2005_round1 (+round2) in 10.1016/j.nmni.2019.100640. **Each is now a
  reading assignment, not a row**: the works/fails call and the as-of date come from the
  paper's results. Two of the seven touch assays S7b unflags, which is what would settle
  that candidate.

  **All seven were read the same day and eleven rows are proposed**
  (`docs/journal/2026-10-29-use-family-cases.md`): 3 `fails`/`coverage` from the raptor
  paper, which locates a two-base 3'-end mismatch in HaemNFI and HaemR2L against the
  clade the Hellgren nest cannot amplify and screens every sample again with another
  protocol to cover it; 7 `works` (pan-herpes DPOL on equine samples and on a novel pudu
  gammaherpesvirus, Chu pan-astrovirus 16/16 by nest, pan-adenovirus hexon on 4 of 775
  DRC rodents); 1 `partial`, the only head-to-head in the batch, where a Cameroon survey
  ran two pan-CoV protocols on the same samples and ours produced 64 positive results
  against the other's 173. Two near-misses recorded as NOT A ROW. **Set 2 is now 14 rows,
  11 of them never scored** — the file was deliberately not run through
  `retrospective.py`, since `--cases` scores every row. Remaining: the maintainer's
  works/fails sign-off on all eleven (taken 2026-10-30), and the 93 `use` rows that did not
  reach CONFIRMED (closed 2026-10-30, below).

  **Set 2: 14 rows, ALL SPENT 2026-10-30** (`docs/journal/2026-10-30-decisions.md`). The
  maintainer accepted the twelve proposed rows as written and the set was scored, after the
  S7b decision and under both the pre-S7b calls and the S7b replay: works 3 agree / 2 weaker
  / **5 `declining`** (4 under S7b, the Mills row being the one that moves), fails 2 caught
  (both as `low coverage`) / 1 missed (Hellgren pan-hemoparasite, 98.9% `stable`: a clade
  failure the pooled share cannot see), partial 1 agrees. **False alarms 5/10 against 4/32 on
  the development set**, and four of the five are pan-family consensus assays whose paper
  reports them amplifying a divergent virus from a few positives — a `works` about field
  sensitivity scored against a status about coverage of deposited diversity. Proposed there,
  for the matrix's scoring rule and not for `config.yaml`: a pan-family `works` against
  `low coverage` is agreement, as `partial` already is. The count target (15-20) is met; the
  **drift target is not**, though not for the reason this item claimed until 2026-10-30. It
  said zero rows carry `mechanism: drift`. **Three do**: `Morbillivirus_canis_P_Scagliarini_2007`
  (`fails`) in the development set, and the two Kulesh 2004 monkeypox rows (`partial`) in
  held-out set 1. What is true is that **none of the three meets the strict bar** set that
  day, and two of them are not two cases: their own source notes say the mechanism is an
  inference rather than the paper's word, and that they are ONE EVENT. The CDV row rests on
  a proficiency test plus an alignment against current variants, which is a redesign
  motive, not a lineage tracked over time at primer sites. So the honest statement is that
  no row yet DEMONSTRATES drift. No unread evaluation data exists again; the next rows need
  a drift-mechanism search.

  **HELD-OUT SET 3 IS OPEN, with one row, and it is the first row in the project that
  demonstrates drift** (2026-10-30, `docs/validation-cases-heldout-3.tsv`,
  `docs/journal/2026-10-30-influenza-drift-entries.md`). Yang 2014 against
  `Influenza_A_virus_M1_Ward_2004`: named M-gene substitutions with years (G238A in 11-12
  A(H1N1)pdm09 isolates in 2010-2011, joining C154T, G225A and T228C through 2012-2013),
  located by the paper's own alignments in the primer-binding regions, 6 of 40 specimens
  negative by the original and positive by the degenerate redesign. It clears the Q6 strict
  bar. **It is not yet scored**, because its assay waits in `pending/` and a pending entry is
  never screened; scoring follows promotion and a screen. Set 3 is also the **first genuine
  test of the scoped matrix**, since its `scope_taxid` (114727) was read from the source paper
  before any verdict existed, where set 2's scopes could only ever be a re-description. A
  second row, Shu 2026 against the CDC H3 assay, is written and withheld on the citation
  decision above.

  **The drift-mechanism search is designed and NOT built** (2026-10-30, grilled,
  `docs/journal/2026-10-30-design-grilled.md` Q5-Q6): redesign papers first, as a new
  pre-registered phrase family in `scripts/find_retrospective_cases.py` over the citation
  graph already on disk, restricted to citing papers published some years after the design
  paper. **Strict bar for `mechanism: drift`**: the paper must show the same lineage changing
  over time at primer sites (an alignment, a table, or named substitutions with years);
  "newer isolates fail" alone is `coverage` or not a row. Fast-evolving-target literature and
  EQA reports are the second and third sources. Zero rows meeting the strict bar is a
  possible and honest outcome. **Route decided 2026-10-30: a fresh session on this task
  alone**, starting from that journal's Q5-Q6; the first attempt was interrupted and the
  content could not be reproduced in the same session.

  **The redesign family is BUILT and RUN** (2026-10-30, `docs/journal/2026-10-30-redesign-family.md`):
  `--include late_redesign`, six phrases and a five-year clock on `citation.design_year`, pre-registered
  in the script before the run. **Two rows, neither a primer redesign, zero toward a drift case.** The
  first of Q5's three sources is exhausted; the fast-evolving-target literature and EQA reports remain,
  and neither is a citation-graph phrase search.

  **The matrix takes a scope per row, and the mechanism is BUILT** (2026-10-30,
  `docs/journal/2026-10-30-scope-column-and-use-rows-closed.md`). Both case files accept an
  optional `scope_taxid`; `retrospective.py` scores that lineage's own records with the same
  binomial `worst_lineage_verdict` uses and WITHOUT its family-wise correction, since the
  lineage is named in advance, and prints which rows were scored that way and which scopes it
  could not honour. Chosen after set 2 was read, so on set 2 it is a description and not a
  score. **What is owed: the scope values themselves** — one taxid per row, read from the
  paper, which is a maintainer's read; the four pan-family rows of set 2 are where it pays.

  **The 93 `use` rows that did not reach CONFIRMED are CLOSED** (same journal), with no new
  case and a mechanical reason for each class: 126 oligo rows cite the assay without printing
  any table, 73 are behind a paywall, 49 print a table ours is not in. The 57 rows over 13
  papers that do print a table yield exactly four candidate pairs, and all four are explained
  — the pudu paper retyped VanDevanter's IYG one base short (the design PDF confirms the
  registry's 24-mer, 5 of 5 exact), and the two coronavirus entries store PREDICT
  modifications, which a paper printing the original can never confirm. **The lesson worth
  keeping**: a `near:1` on a degenerate oligo is usually the CITING paper's transcription
  error, not ours. Only the 73 paywalled rows could still move, and the yield looks low.

## Lineage composition over time (designed 2026-11-02, grilled; not built)

- [ ] **Separate "the mix of lineages sequenced changed" from "detection within lineages
  changed" in every assay's per-year detection graph.** An assay's graph can move for
  either reason (a large LGV study one year, a wave of H3N2 deposits another), and nothing
  today tells them apart. What exists: per-lineage statistics pooled over the recent window
  (`lineage.py`), per-year blocks for failing lineages only and not scope-filtered
  (`lineage_report.py`), and a clustering module (`subcluster.py`) wired into the lineage
  layer as the `cluster` resolver (Mode C, `clustermaps.py`) but switched on for no assay. Nothing records
  which lineages make up each year's records. The Messmer *C. trachomatis* finding (a
  design-era gap, not drift) is the kind of question this answers. **Report-only: no status
  changes**, like the trend, collection-year and hierarchical lenses.

  **Decisions** (grilled 2026-11-02):

  | Decision | Choice |
  |---|---|
  | What "scope over time" covers | lineage mix per year; growth of the target taxon; design era vs now; retrieval coverage |
  | Lineage | sequence clusters, every assay |
  | Region clustered | amplicon + flank each side, primer/probe sites masked |
  | Cut-off | ~~per assay: widest gap in the distances, bounded in config~~ -> **one fixed `composition.cut: 0.05`** (2026-11-03, measured; see the "Cut rule" row below) |
  | Scale | year-stratified sample (capped); every record assigned to its nearest sampled member |
  | Names | majority species + number ("C. trachomatis 1"); tooltip with species mix and title tokens |
  | Split | a "same mix" line (whole-period mix, direct standardisation) + a recent-vs-baseline Kitagawa split (mix part + within part, bootstrap intervals) |
  | Target taxon | first-deposit year of each species under the target; "new since design" after the design year |
  | Retrieval coverage | the assay's query vs all records under the target taxid, per year, by `esearch` |
  | Outputs | website: same-mix line, a CoVariants-style 100% stacked panel under the graph (8 clusters + other, undetected part lighter), a retrieval-gap band, one sentence; `composition.tsv`; a report section; `lineage.md` per-year blocks from clusters |
  | The graph's record set (finding 4) | **extracted, not rebuilt** (decided 2026-11-02): `drift.graph_records` and `report.assessment_inputs` become the one place the record set is decided, used by both `assess` and `composition`; step 10 is guarded by byte-identical report output and `pytest -m slow`, and gets full review because it touches the verdict path |
  | One clustering or two | **one** (decided 2026-11-02): composition's clustering replaces Mode C's all-pairs path; `clustermaps.cluster_maps` returns composition's labels, so the `cluster` resolver gains window archives and influenza scale. No verdict moves (no `sublineage` chain names `cluster`). Step 12 adds a test that `cluster_maps` and `composition.tsv` agree record for record |
  | Retrieval coverage counts | **one counter, two consumers** (decided 2026-11-02): `retrieve.year_counts` and its cache are the single source of per-year counts, read by the composition panel and by the release scope-verification script (whose interface is still to approve). Three series: archive on disk (free), query, and all under the target taxid; archive vs query catches a retrieval that fell behind, query vs taxid catches a blind query. Runs in the weekly pipeline: ~10,700 `esearch` calls (~18 min) once, ~540 per run after |
  | Diverged records (finding 1) | **an explicit segment, no homology placement in version 1** (decided 2026-11-02): each year's bar carries "diverged: no site found" in the failure shade, counted in the invariant and stated in the sentence; for the split it is one more lineage. Former step 11 dropped |
  | Where the panel's data lives | **a separate compact file** (decided 2026-11-02): `website/data/composition.json`, committed beside `run.json` (2.5 MB today), columnar per assay, years with records only, cluster names once; a test caps it at 1.5 MB; `site.yml`'s published-vs-data check covers both files. `run.json` keeps its shape |
  | Cut rule | **one fixed cut, 0.05, and the per-assay search deleted** (2026-11-03, `docs/journal/2026-11-03-composition-cut-measured.md`). The widest-gap rule works at Messmer's 76 windows and fails at 1,500-2,000: the MST edge weights are then a continuum (median 0.003, p99 0.077 of 1,999 edges), so the widest gap sits in the sparse upper tail and isolates one outlier (influenza M: one cluster of 1,999 holding every subtype), or there is no gap at all (pan-coronavirus: widest 0.0087, under `min_gap`, one cluster across four genera). A fixed cut is monotonic, and 0.05 is where the named taxa separate on all three assays measured. Also recorded: the influenza check was unmeetable, since subtype is an HA/NA property and the matrix gene is conserved across subtypes |
  | Window shape (found at step 4b) | **per assay, read from the archive** (decided 2026-11-03): influenza M's amplicon sits at segment 7's 5' end (left flank 9-23 bp, right 886-903 bp, p10-p90 of 89,628 records), so a symmetric ±500 bp window was full-flank in 1 record of 89,628. Each assay's left flank L is the `shape_quantile` (0.1) of what its evaluable records offer, capped at `flank_bp`; R takes the unused budget up to `2 × flank_bp − L`, capped at its own quantile. Every window in an assay has one geometry, so Jaccard compares like with like; records not covering it are placed by containment |
  | Messmer bench case | the note under "Data and curation" only; no validation row: it would score `undecided` (about seven *trachomatis* records before its 1996 `as_of`) and the development set is frozen |

  **Found while planning, each changing the design** (confirm at review):
  1. **Diverged records have no site.** With `drift.count_diverged_as_fail: true`, 68,599
     `diverged` no-amplicon rows (4% of evaluable, concentrated in a few assays such as
     Enterovirus Nix round 2) count as failures in the graph but carry no coordinates to cut
     a window from. **Decided: no placement in version 1**; they form an explicit
     "diverged: no site found" segment, drawn and counted, whose share the sentence states.
  2. **Assembly and window archives hold short flanks.** `asm` records are cut to the
     amplicon ± 100 bp (`record_min_overhang_bp`), window archives ± 300 bp. Flanks stop at
     record ends and N spacers, the flank used is recorded, and short-flank windows are
     assigned by containment and never sampled.
  3. **16S will not separate *C. trachomatis* serovars.** The ocular/urogenital/LGV split is
     in ompA and the genome; ±500 bp of 16S is near-identical. **Half right, measured
     2026-11-03 (step 4b)**: all 32 sampled *trachomatis* windows sit in one cluster, but the
     genus round-1 pair also amplifies other species, and its 76 distinct windows split into
     four species groups at a cut of 0.040 (widest gap 0.033-0.047): the *psittaci/abortus*
     complex 35, *trachomatis* + *muridarum* 34, *pecorum* 4, *pneumoniae* 3.
  4. **The panel reuses the graph's record set, never rebuilds it.** That set comes from
     accession keying, the anchor and chance-pair tests, scope/exclusivity/patent filters,
     the per-chemistry `reduced` rule and the recent window; these move into shared helpers,
     with a hard invariant: per assay and year the panel's cells sum to the graph's evaluable
     and detected counts, or the stage fails.
  5. **Pure-Python Mash comparison will not scale** (~6.5 ms per pair, hours per assay).
     Flanked windows are under `sketch_size`, so an exact vectorised Jaccard (numpy/scipy
     sparse) gives the same distance in seconds; a test pins the equality.

  **Design: one new deep module, `assaywatch/composition.py`**, entry point `build(...)`
  (+ `write`, `read_summary`, `main`), command `assaywatch composition`, a Snakefile stage
  after the screen. Reads files; writes `results/<date>/composition.tsv` (assay × year ×
  cluster) and `composition.json` (per-assay split, same-mix series, coverage, species first
  years); changes no status. **Interfaces, for the maintainer's approval before step 0**
  (internals delegated within the tested boundary):

  ```python
  # subcluster.py: region support and sample-then-assign beside the unchanged cluster()
  flanked_region(record_id, seq, amplicon, sites, *, flank_bp, mask_buffer_bp, stop_n_run) -> Region
  kmer_matrix(seqs, k) -> csr_matrix;  jaccard_matrix(a, b=None) -> ndarray
  widest_gap_cut(dist, *, lo, hi, min_gap) -> Cut        # Cut(value, gap, reason)
  components_at(dist, cut, min_size) -> list[int]
  assign_nearest(query, ref, ref_labels, k, cut, *, containment_for=None) -> list[int]

  # drift.py: the graph's own record set, shared with assess()
  graph_records(calls, years, cfg, *, today, inputs) -> dict[str, list[GraphRecord]]
  # GraphRecord(record_id, year, detected, recent, taxid)

  # composition.py
  build(calls_path, registry, retrieved, cfg, *, run_date, coverage=None, workers=1) -> CompositionRun
  write(run, out_dir) -> (composition.tsv, composition.json);  read_summary(path) -> CompositionRun
  # AssayComposition(assay_id, cut, flank_bp, clusters, cells, same_mix, split, species, coverage, note)
  # Cluster(id, name, n_records, representative, species_mix, title_tokens, first_year, new_since_design)
  # Split(baseline_share, recent_share, change, mix, within, mix_ci, within_ci, n_boot, one_period_clusters)

  # retrieve.py: owns NCBI access
  year_counts(transport, query, years, datetype) -> dict[int, int]   # cached, offline-safe
  ```

  `composition.tsv` columns: `assay_id, year, cluster_id, cluster_name, cluster_rank,
  records, detected, recent_records, top_species, top_species_taxid, species_mix,
  cluster_first_year, new_since_design, representative, cut, flank_bp`.

  **Algorithms.**
  - Sample: unique masked windows (deduplicated), ordered by `blake2b(accession)` within
    year, quota per year up to `sample_cap`; full-flank windows only. Deterministic.
  - Cut: single-linkage components at `composition.cut` (0.05), one number for every
    assay. A component under `min_cluster_size` is "other"; an assay whose windows are all
    tighter than the cut is one cluster, which needs no special case.
  - Assign: every window takes the label of its nearest sampled member within the cut
    (containment for short flanks), else unplaced; diverged records take the label `diverged`. Labels ranked by size, ties by
    representative accession.
  - Same-mix line: weights = each cluster's share of all the assay's records; a year is drawn
    only if its present clusters cover `same_mix_min_covered` of the weight.
  - Kitagawa: mix = Σ(w_r−w_b)(p_r+p_b)/2, within = Σ(p_r−p_b)(w_r+w_b)/2, summing exactly to
    the change; bootstrap by multinomial resampling of records within each period (cluster
    uncertainty not included, and said so).
  - Species first year: canonical taxid → species (`taxonomy.py`), earliest deposit in our
    archive (stated as "in our archive", not all of GenBank).
  - Coverage: `ours` = the assay's query, `all` = `txid{taxid}[Organism:exp]`, one `esearch`
    (retmax 0) per year, cached in `data/retrieved/.year-counts.json.gz`, the last 2 years
    refreshed per run, offline falls back to the cache; `asm` groups `n/a`.

  **Changes to existing modules.**

  | File | Change |
  |---|---|
  | `assaywatch/subcluster.py` | the functions above; `cluster()` (all-pairs) retired once `clustermaps` no longer calls it |
  | `assaywatch/clustermaps.py` | `cluster_maps` returns composition's labels instead of running its own all-pairs clustering |
  | `assaywatch/drift.py` | `graph_records` via a private helper shared with `assess` |
  | `assaywatch/report.py` | split `assess_as_reported` into `assessment_inputs` + assess; `load_calls_as_reported`; a section "Where the mix moved the graph" (assays with a mix part ≥ `report_min_mix` and an interval excluding 0) |
  | `assaywatch/retrieve.py` | `year_counts`, `--year-counts` mode |
  | `assaywatch/lineage_report.py` | per-year blocks read `composition.tsv` |
  | `assaywatch/site.py`, `site_render.py`, `site_svg.py` | `AssayPage.composition`; shared year axis; same-mix line and gap band in `year_chart`; a `composition_panel`; sentence and legend |
  | `assaywatch/settings.py`, `config.yaml` | a `composition:` block, every number justified in a comment (flank budget 500 + `shape_quantile` 0.1, k 15, sample cap 2000, cut 0.05, show 8, n_boot 2000, ...) |
  | `Snakefile`, `assaywatch/cli.py` | rules `retrieval_coverage` (localrule, network) and `composition`; report and lineage take its outputs; `composition` added to the hashed sections |
  | `GLOSSARY.md` | composition, cluster, same-mix line, mix part / within part, retrieval gap, new since design |

  Nested protocols are left out of version 1, and the report says so.

  **Steps** (TDD: failing test → code → `pytest -m fast`, ruff → `pytest -q`; each step
  leaves pytest, the validator, ruff and check_citations passing; one commit per step):
  - [x] 0. **Folded into step 12** (2026-11-03). Two guards make a standalone config step impossible:
        `test_config_keys` refuses a key nothing reads and `test_settings` refuses a model key
        `config.yaml` lacks, so a key, its model field and its first reader land together. Steps
        1-11 are pure functions taking values as arguments; `composition.build` (step 12) is the
        first reader. The block, its comments and the model were drafted in
        `docs/composition-config-draft.yaml`, which steps 12, 14, 15 and 17 emptied key by key;
        the file is deleted and every `composition:` key now has a reader.
  - [x] 1. `flanked_region` (clipping at ends and N runs, masking, flank recorded). Done 2026-11-03:
        `subcluster.Region` + `flanked_region`, 7 tests in `tests/test_subcluster.py`; a flank keeps
        interior N and drops N at its outer end; no reverse complement (k-mers are canonical).
        GLOSSARY: composition window.
  - [x] 2. `kmer_matrix` / `jaccard_matrix`, equal to the existing `jaccard` / `mash_distance`. Done
        2026-11-03, plus `mash_distances` (the vectorised `mash_distance`, needed by the cut). 7 tests,
        including equality with the bottom-k estimate below `sketch_size`. 2,000 synthetic 1,200 bp
        windows: k-mer matrix 2.0 s, all-pairs Jaccard 1.9 s, 32 MB dense. scipy imported lazily.
  - [x] 3. Stratified sample, deterministic and order-independent. Done 2026-11-03:
        `composition.sample_windows(regions, years, cap) -> list[int]` (new module). Round-robin
        across years so a quiet year's lineage is always clustered; identical windows count once;
        rank by blake2b of the version-less accession. 7 tests, `fast` tier.
  - [x] 4. ~~`widest_gap_cut`~~ **built 2026-11-03, measured the same day and REMOVED**, with
        `Cut` and `mst_weights` and the 8 tests that pinned them. It did what it was specified to do
        -- only gaps BETWEEN MST edges counted, each clipped to the bounds -- and the specification
        is what failed; see the "Cut rule" row above and the journal. `components_at` now takes a
        plain float, and `_clades`, the block-matrix test helper, stays.
  - [x] 4b. Calibrate the cut. **Done 2026-11-03** on Messmer 16S, Haemosporida cytb and
        pan-coronavirus RdRp, against the organism in each record's title, which the clustering
        never sees: `composition.cut: 0.05` and the window shape read per assay, both findings in
        `docs/journal/2026-11-03-composition-cut-measured.md`.
  - [x] 5. `components_at` + `assign_nearest` on a two-clade synthetic fixture. Done 2026-11-03, on
        sequences built in the tests; the `make_fixtures.py` fixture moves to step 12, which is its
        first user. Labels `0..` by size, `OTHER` (-1) under `min_size`, `UNPLACED` (-2) beyond the
        cut; short-flank queries placed by containment (-ln(c)/k). 7 tests.
  - [x] 6. Naming and title tokens. Done 2026-11-03: `composition.organism` (the name a title
        carries, as the fallback where metadata has no taxid), `species_mix`, `cluster_names`,
        `title_tokens`; 4 config keys drafted. Measured on four archives -- distinct names fall
        6,866 -> 371 (haemosporida), 3,106 -> 757 (coronavirus), 48 -> 4 (influenza) -- once the
        name ends at a qualifier, at `sp.`, or at a strain identifier. A mixed cluster's name
        carries its modal share, and a record qualifier (`clone` against `isolate`) is never a
        token. 15 tests.
  - [x] 7. Same-mix standardisation on a hand-computed table. Done 2026-11-03: `Cell`
        (year x lineage x records x detected, the panel's unit), `observed_series` and
        `same_mix_series`. Direct standardisation on each lineage's share of all the assay's
        records, renormalised over the lineages a year actually holds, and no point drawn
        where they carry under `same_mix_min_covered` of the weight. `other`, `unplaced` and
        diverged are strata like any other, or the line would disagree with the graph. 8 tests.
  - [x] 8. Kitagawa: parts sum to the change; deterministic bootstrap. Done 2026-11-03:
        `Split` and `split_change`, with the identity pinned over 50 random tables. A lineage
        present in ONE period only has no rate in the other, so its missing rate is taken to be
        the rate it has: its within term is zero, its whole effect lands in `mix`, the identity
        stays exact, and the cluster is named in `one_period_clusters`. The bootstrap resamples
        RECORDS within each period and prices deposition and detection only, NOT the clustering,
        which the report must say beside the interval. 8 tests.
  - [x] 9. Species first year with a merged taxid; design-year flag. Done 2026-11-03:
        `SpeciesYear` + `species_years`, over `taxonomy.canonical` and `species_of`, so a
        merged-away id (11232 -> 3052342) and a no-rank child (3139435 under *Morbillivirus
        canis*) are their species and not species of their own. `new_since_design` is strictly
        after `citation.design_year`, and False where the entry has none. The year is the
        earliest IN OUR ARCHIVE, which the field's comment says. 8 tests. Running it over four
        archives drove four corrections to step 6's naming: a strain code after a binomial
        ("Chlamydia psittaci NO-03"), stacked record flags ("MAG TPA_asm: ..."), a six-word
        species name (SARS-CoV-2), and a lowercase isolate code ("Pigeon coronavirus rin35").
  - [x] 10. Extract `assessment_inputs`, `load_calls_as_reported`, `graph_records`; per-year
        sums equal `assess().years`; existing report output byte-identical. **Done 2026-11-03**,
        the verdict path, so in named pieces with a guard committed first:
        `tests/test_report_golden.py` renders the fixture registry to markdown and HTML and
        compares every byte (`UPDATE_GOLDEN=1` regenerates). `_gather_calls` now yields
        `GatheredRow` objects carrying `record_id` and `taxid`, and `_window` and
        `_window_months` are shared, so `assess` and `graph_records` cannot choose different
        windows. `drift.graph_records(calls, years, cfg, today=, inputs=)` returns
        `GraphRecord(record_id, year, call, evaluable, detected, recent, taxid)` per assay, and
        two tests pin the invariant: per assay and year its evaluable and detected counts equal
        `assess().years`, its recent counts equal `recent_evaluable`/`recent_detected`, its rows
        plus `skipped_undated` equal `screened_rows`, and `reduced_not_detected` reads the same
        both sides. `report.assessment_inputs` is the one bundle both take;
        `report.load_calls_as_reported` is the one reader of the calls table. Report output
        unchanged, 2,023 tests and `pytest -m slow` green.
  - [x] 11. The "diverged" segment: diverged records counted per year as their own lineage (no
        placement). Done 2026-11-03: `GraphRecord.diverged` (from the gather's own `why`),
        `composition.DIVERGED` (-3, beside `OTHER` -1 and `UNPLACED` -2, with a test that the
        three cannot collide), `cells_from` and `pool_small_clusters`. The panel shares the
        graph's denominator, so a record outside it is in no cell; `diverged` and `unplaced`
        are never pooled into `other`, since the sentence states their share. Pooling ranks a
        cluster over ALL years, so it does not appear and vanish year by year. 9 tests.
  - [x] 12. `composition.build` / `write` on the fixture: invariant, TSV schema, JSON round-trip.
        **Done 2026-11-03.** `Options`, `Cluster`, `AssayComposition`, `CompositionRun`,
        `build_assay`, `build`, `write`, `read_summary`, `TSV_COLUMNS`. Sixteen config keys and
        their model fields moved in (own commit); `report_min_mix`, `site_max_bytes` and
        `coverage_refresh_years` stay drafted until steps 14, 15 and 17, so the draft file
        survives until then. 8 end-to-end tests on a two-clade archive generated in the test
        rather than in `make_fixtures.py`, which writes the committed fixtures `test_score`
        reads and needs none of this.
        **Two interface changes, both forced by measurement.** (a) The window's amplicon span
        and oligo sites are RECOMPUTED per record (`_place_window`, `match.pair_spans` +
        `find_sites` at `clustermaps.search_params`, 0.2 ms/record measured) rather than read
        from a table: `calls.read_calls` drops those columns on purpose (3.6 GB otherwise), and
        the per-assay screens that do hold them are a cache whose `assay_id` column was stale
        on this machine the moment the ids were renamed on 2026-11-02 -- every screen still
        carried the old ids, so matching on it found nothing. (b) `Cell` gained a `recent`
        count, which `composition.tsv` reports, and the TSV carries `left_bp`/`right_bp` in
        place of the plan's single `flank_bp`, since the shape is per assay.
        Smoke-run on the 2026-11-01 calls, two assays: Messmer 16S splits into *trachomatis*,
        *psittaci*, *pecorum*, *crocodili* and a second *trachomatis* cluster whose tokens are
        `L2f`/`LGV` -- the serovar group that assay misses; Haemosporida cytb into
        *Haemoproteus*, *Plasmodium* and two more, 2 of 2,227 records unplaced.
  - [x] 13. `lineage.md` from `composition.tsv`. **Done 2026-11-03**, as a SECOND SECTION
        rather than the rewrite the plan described: the per-year blocks above it are grouped by
        `lineage.lineage_of`, the same function the table above them and `drift._lineage_check`
        use, and that agreement is deliberate ("a row here and a row above cannot disagree
        about which lineage a record is in"). Sequence clusters are a different partition, so
        `lineage_report.cluster_section` adds the per-year mix, the same-mix column, the
        mix/within sentence with its interval and what that interval does NOT price, and a
        cluster table with tokens and `new since design`. It reads `composition.json` through
        `read_summary` (typed) rather than the TSV, and renders nothing when a run has none.
        9 tests.
        **The module split `pytest -m slow` forced.** `triggers.import_closure` walks a whole
        AST, function-local imports included, so one `from assaywatch.report import ...` inside
        `composition.build` put `report.py` into the `lineage_analysis` rule's signature and
        every edit to the report would have reread 2.7M rows of calls for a document that does
        not depend on it. The producer moved to `assaywatch/composition_build.py` (`build`,
        `build_assay`, `_place_window`, `_archive`); the model, the statistics and both file
        formats stay in `composition.py`, whose closure is 9 modules and holds no `report.py`.
        The seam `clustermaps.py` sits on, for the same reason. `build` is therefore
        `composition_build.build`, not `composition.build` as the plan's interface said.
  - [x] 14. Report section. **Done 2026-11-03**: `MixRow`, `mix_rows`, the shared
        heading/intro/columns/cells helpers and a section in BOTH serialisers, beside the
        collection-year lens and built the same way. `composition.report_min_mix` (0.05, matching
        `drift.min_decline`) moved in from the draft with its model field; the bar is that AND an
        interval excluding zero, because a large mix part whose interval straddles zero has not
        been shown to have moved. Each row names the cluster whose share of the records moved
        most. EITHER DIRECTION is named -- both real assays tried had a POSITIVE mix part, and a
        share that rose because easier lineages were sequenced has not got better, which the
        intro now says. The report reads `composition.json` through `read_summary` and never
        imports the producer. 10 tests; the golden fixture is unchanged, since a run without a
        composition file renders exactly what it did.
        **A bug this created and a test caught**: inserting `composition_mix` into `build_model`
        rebound the next positional argument at two forwarding call sites, so `nest_drifts`
        arrived as the mix rows -- the same failure a comment beside `render_html` already
        recorded for `results_dir` and `figures`. Both call sites now pass keywords.
  - [x] 15. Site: `website/data/composition.json` (columnar), chart additions, panel, sentence; a
        test that each year's cells sum to the graph's evaluable; a 1.5 MB cap on the file.
        **Done 2026-11-03.** `composition.site_data` / `write_site_data` (+ `SITE_SCHEMA`),
        `site_svg.composition_panel`, `year_chart(page, same_mix=)`,
        `site_render._composition_block`, `site.py --composition`, CSS in `extra.css`.
        `site_max_bytes` moved in from the draft; only `coverage_refresh_years` is left there.
        16 tests.
        **The cap fired on the first real measurement, which is what it is for.** At
        `json.dumps(indent=1)` two assays of the 2026-11-01 run came to 13.8 KB, about 1,491 KB
        over 216 assays against a 1,465 KB cap. The file is now ONE LINE PER ASSAY, compact
        within it (5.2 KB for the same two, about 567 KB over the registry), and the floats are
        rounded to 4 dp: a committed file's diff has to say WHICH assay moved, which `indent=1`
        makes expensive and a fully compact file makes impossible.
        **Two design decisions worth knowing.** (a) The panel encodes a cluster by ORDINAL
        LIGHTNESS of one hue, not by eight categorical colours: every colour in `palette.py`
        carries a meaning and the set is contrast-validated by a skill's validator, so eight
        invented ones would be eight unvalidated ones, and clusters are ranked by size, which is
        what makes an ordinal ramp honest. `other`, `unplaced` and `diverged` are hatched,
        because they are not lineages. (b) The plan's "undetected part lighter" is NOT drawn:
        lightness already carries cluster identity, and one channel cannot carry two meanings.
        Per-cluster detection is in each segment's tooltip and in `lineage.md`.
  - [x] 16. Snakefile rules and CLI. **Done 2026-11-03** for the `composition` rule;
        `retrieval_coverage` belongs to step 17, which needs the network. `assaywatch
        composition` (the stage whose name is NOT its module's: it runs `composition_build`,
        and `tests/test_triggers.py` now resolves a stage through `cli.resolve` rather than
        assuming the two coincide), `rule composition` with `_COMPOSITION_PARAMS` hashing
        `source_names("composition_build")` and the `composition`/`drift`/`scoring`/`amplicon`
        config blocks, and `composition.json` as a HARD INPUT of both `report` and
        `lineage_analysis`, so a section and the tables beside it always come from one run.
        `snakemake -n` plans it between `collect_calls` and the two consumers.
        **Nine trigger expectations updated, each with its reason, and one is worth knowing:**
        editing `report.py` reruns `lineage_analysis` again -- not through the stray import the
        step 13 split removed, but through a DATA dependency, since `lineage.md`'s cluster
        section reads `composition.json` and the stage imports `report` for
        `assessment_inputs`. That is the price of decision A, and it is the honest one: the
        panel under a graph has to be built from the records the graph counts.
  - [x] 17. `year_counts` with a fake transport (queries, cache, refresh, offline); then a
        network smoke test and a datetype calibration on the Mac. **Done 2026-11-03.**
        `retrieve.year_counts` (13 tests on a fake transport), `assaywatch retrieve
        --year-counts` writing `coverage.json`, `rule retrieval_coverage` (localrule, network,
        `retmax=0` so it fetches nothing and takes no lock), the series carried through
        `build(coverage=)` onto `AssayComposition.coverage` and into both file formats, and a
        retrieval-coverage line in `lineage.md`. `coverage_refresh_years` was the LAST drafted
        key: `docs/composition-config-draft.yaml` is deleted and every `composition:` key now
        has a reader.
        **The datetype is measured, not assumed:** `pdat` (publication date) reproduces the
        archive's own `created` years -- 6 of 6 exactly on the haemosporidian query and 4 of 6
        on Chlamydia 16S over 2020-2025 -- where `mdat` does not. The refresh window is
        CALENDAR years, not the top of the range asked for: anchored to the request it
        re-counted a 2020 nothing had changed while trusting a cached 2026 still filling up.
        **Found on the first real run, and it is the influenza shape again:** the Chlamydia 16S
        query returned 27.6% of its genus's 2020 deposits and 0.4% of 2023's (14 of 3,742),
        while the genus's deposits grew 568 -> 3,742. A verdict on that assay is partly a fact
        about its query, which is what the line in `lineage.md` now says. Worth a maintainer's
        read: the query is title-based (`16S[Title] OR ...`) under a genus that increasingly
        deposits genomes.
        **A calibration mistake worth recording:** the first attempt counted
        `target.query` alone and got ~964,000 Chlamydia records for 2021. That field is only
        the assay's own term; the retrieval query is `retrieve.build_query(taxid, cfg, term)`,
        which adds `txid<n>[Organism:exp]` and the length filter.
  - [x] 18. End to end on the 2026-11-01 run (below); journal entry; INDEX row; CHANGELOG; tick
        here. **Done 2026-11-04, `docs/journal/2026-11-04-composition-final.md`.** 0 invariant
        mismatches over 215 assays on the 2026-11-01 run; the Messmer species split failed as written, recorded below.
        **STARTED 2026-11-03 and stopped at 15 minutes of CPU, with two findings that are
        the reason to do this step at all.**
        (a) **THE RULE ASKS FOR TOO LITTLE MEMORY.** `rule composition` declares
        `mem_mb=4000`; the full-registry build was at **5.65 GB resident and still climbing**
        after 15 minutes. On SLURM, where `resources:` becomes the sbatch request, that job is
        killed rather than slowed -- the failure the report rule's own comment warns about. The
        suspect is `graph_records`, which materialises one `GraphRecord` per evaluable row for
        EVERY assay at once (about 930k objects on this run) while `build` also holds the
        calls table [measured 2026-11-04: 3,107,513 `GraphRecord`s adding 0.48 GB; the table
        alone peaks at 3.17 GB, so the table was the cost, and `build` now frees it and each
        assay's rows after use]; the stage processes one assay at a time and has no need of the others'
        records. Either stream it per assay or measure the peak honestly and declare that.
        Decide before the first live run: the rule is wired into `all` through `report`.
        (b) **The build prints nothing until it finishes**, so a run that takes an unknown
        number of minutes cannot be told from one that has hung. A per-assay progress line on
        stderr, as `retrieve` and the screen stage already print, is the fix.
        The verification script is written (the invariant per assay and year, statuses before
        and after, the Messmer and Haemosporida cases, the site file against its cap) and is
        NOT in the repository: a one-off analysis is a record, not a tool. Re-create it from
        this list.

  **Verification.**
  - `assaywatch composition results/2026-11-01/calls.tsv.gz --registry registry --retrieved
    data/retrieved --out <scratch>` completes; the invariant holds for every assay (a `jq`
    check joining `composition.json` to `run.json`: summed cells per year equal `years[].evaluable`, 0 mismatches).
  - `report_diff` against the run without composition: no assay changes status.
  - Messmer 16S round 1: FAILED 2026-11-04 as written, and the expectation was wrong. Step 4b's
    clean species split came from 76 sampled windows. On all 793, single linkage at 0.05 chains
    14 species into one group of 687 (*C. trachomatis* 52%). Labels were tested and hold: no
    *psittaci* record is nearer *trachomatis* by amplicon. A lower cut helps Messmer and costs
    others (`docs/journal/2026-11-04-composition-final.md`). Published at 0.05 by maintainer
    decision, with pages saying these are sequence groups and naming a mixed largest group.
  - Haemosporida cytb (`Haemosporida_cytb_Hellgren_2004_HaemF`): Haemoproteus and
    Hepatocystis each at least 90% complete in one cluster, and purity against the title
    genus at least 80% (0.05 read 83% at step 4b).
  - Influenza M (`Influenza_A_virus_M_Spackman_2002`): the biggest archive, so this is the
    COST case and not a correctness one -- the matrix gene cannot separate subtypes (step
    4b). Record runtime and peak memory, then set the rule's `resources`.
  - Coverage calibration: `esearch` `ours` per year against archive `created` counts for 3 groups.
  - Site: extract + render; three pages checked by eye (Messmer, influenza M, one
    assembly-based Leptospira); `composition.json` within its 1.5 MB cap.
  - `pytest -m slow` and `snakemake -n` show only the new and dependent jobs.

  **On a cluster:** every live assay (`assaywatch validate registry` counts them) with a 2,000-record sample each is minutes per assay
  locally. On SLURM the `composition` rule runs as one job per run (`profiles/slurm/` maps
  `threads` / `resources` to the sbatch request); splitting it per assay group is the later
  step if runtime demands it.

## Data and curation

- [x] **Messmer genus round 1 detects 0 of 39 recent *C. trachomatis* records**
  (raised 2026-11-02, explained the same day). Not new and not drift: the round 1 entry's
  note recorded it on 2026-10-24 (0 of 301). On the 2026-11-01 calls all 363 judgeable
  *trachomatis* records fail round 1. The genus sense primer carries five mismatches at
  13, 12, 8, 7 and 6 nt from its 3' end in every one, and 110 also mismatch at the
  terminal base: all ocular A-C strains (24 of 24), no LGV strain (0 of 39), half the
  urogenital D-K. The pattern is already in the 1996-1998 deposits, so it is a
  design-era gap in silico, not a change in the deposit. The reverse primer's
  penultimate T:T, in every Chlamydia record, is the printed oligo and is tolerated at
  the bench (see the entry).
- [ ] **Messmer 1997's own step-1 result as a bench case.** The paper reports that 5 IFU
  of *C. trachomatis* amplified with the genus pair, so for the 253 records with only
  the five internal mismatches (intact 3' pentamer) the screen's `fail` contradicts the
  cited paper. A `works` row in `docs/validation-cases.tsv` would make that a measured
  false negative for the scoring calibration rather than a note. Records carrying the
  extra terminal mismatch are a separate, more plausible failure. Maintainer to decide.

- **The 49 assays the website does not list, resolved one by one** (2026-10-31). The
  assay list shows 168 of 217; the rest carry no usable status and were excluded from
  the table on the maintainer's instruction, though each keeps a page stating why. They
  are not one problem but three, and only the first two are tractable:
  - **30 `insufficient data`** — fewer than `drift.min_records_for_drift` (15) evaluable
    records. Some will resolve on their own as deposits accumulate; some will not,
    because the taxon is barely sequenced, which is the condition this tool exists to
    serve and cannot fix. Worth separating those two groups: an assay two records short
    is a different case from one with none, and the split has never been counted.
    Check first whether any are short because of retrieval rather than deposition — that
    is exactly what the influenza episode was, and `scripts/check_archive_recency.py`
    produces the worklist.
    [x] **Retrieval checked 2026-11-01: none of the 30 is short because a query is
    blind** (`docs/journal/2026-11-01-no-recent-data-scope-check.md`, wider sweep). For
    each: query count all dates and over the window, bare-taxid window count, archive
    count and newest deposit. Where the query sees fewer window records than the taxid,
    the difference is a gene query under a taxon depositing whole genomes or, for
    bacteria, made up by assembly retrieval. Two are short because of SAMPLING, not
    retrieval or deposition: E. coli LT and hlyA (the plasmid-gene item under "Method
    debts"). Reptarenavirus x2: archive newest 2023-09, taxid window 0, free-text window
    hits are a plant genome, so genuinely quiet. The split the item asks for (two records
    short vs none) is still uncounted.
  - **19 with a withheld status** — the entry carries a blocking `needs_review` flag.
    `not_screenable` (an RPA chemistry the penalties do not model, an assay identified by
    product size plus a restriction digest) is permanent and should be recorded as such
    rather than left looking unfinished. `do_not_use` and the other `review.OPEN` flags
    are questions a human can close, and closing one returns its assay to the list.
  - **18 `no recent data`** — still listed, deliberately. The status is a statement about
    deposition, and after the influenza case it is the one most worth leaving in a
    reader's way. Each should nonetheless be checked against its archive's deposit-year
    distribution, because that is how a stale retrieval query presents.
    [x] **Checked 2026-11-01: all 18 are true statements about deposition, none a
    retrieval artefact** (`docs/journal/2026-11-01-no-recent-data-scope-check.md`: each
    query counted against NCBI with and without its filter, searched by organism name
    across taxids, scope taxa counted, and title-excluded assemblies tested). Two kinds:
    7 assays whose archives hold nothing since Oct 2024 (LeHV-5 5 records, newest 2021;
    tortoise intranuclear coccidium 2, newest 2018; Sunshinevirus x2, whose 3 recent
    records are patents; EEHV5 x3 and EEHV6; Batravirus x2), each confirmed at 0 by query,
    taxid and name; and 11 whose archives are current but whose recent records are not
    evaluable: Calicivirus x3 (scope Vesivirus exanthema has 4 window records, all 130 bp
    patents; outside it, recent vesiviruses are feline calicivirus, canine vesivirus 20,
    mink calicivirus 7, stoat vesivirus 3, and 2 filed only at genus level, `Vesivirus`
    95337 and `Vesivirus sp.` 2809959, which drift drops as out of scope because a genus
    node is not within the species, although either could be the scope species), G9R North American orthopox (scope species 0 in window), Perkinsea x2 (137
    in-scope window records, too short to span 287 bp: 140 `truncated`), E. furonis
    (12 records, all 437 bp `truncated`), Ophidiomyces IGS (55 recent, all ITS). What it
    raised is under "Before the next release" and "Waiting on a maintainer".

  The honest outcome may be that a third of these are permanent. Recording which, with
  the reason, is better than leaving 49 assays looking like a backlog.

- **236 `needs_review` flags sat on 158 of the 218 entries on 2026-10-31, and only 17 are open**
  (re-counted 2026-10-31 by splitting on `review.OPEN`, which is the distinction the
  code already draws and this item did not: 219 of the flags are disclosures that are
  TRUE and will never clear, and 17 are questions a reader could close. The worklist is
  the 17, not the 236. Two `retrieval_stale` flags were cleared on 2026-10-31 -- both
  said the numbers predated the 2026-10-17 query change, and both archives have since
  been re-fetched and rescreened, so the condition was false.)

  Earlier wording, kept because its measurement note still applies:
  **227 flags on 154 of the 214 entries** (re-measured 2026-10-30 with
  `registry.load_one`, superseding "216 on 207 of 209" from 2026-10-27. Two other methods
  disagreed on the same day: `grep -c 'flag:'` counted 228 flags, and an inventory pass
  reported a different entry count again, so take a registry count from the loader -- which
  is what the validator and the report read -- and not from a pattern).
  Not a backlog of errors — a flag is an honest label on a reading that could not be made
  from the source — but it is 227 open readings, and some classes are actionable
  where others are permanent. Largest: `orientation_inferred` 28,
  `amplicon_measured_not_published` 25, `oligos_from_secondary_source` 19,
  `scope_narrower_than_taxid` 17, `oligos_modified` 15,
  `pairing_is_curator_reading` 11. `oligos_modified` never clears, because it is true.
  **`orientation_inferred` is measured** (2026-10-27, `scripts/check_orientation.py`):
  the archive yields products under the stored orientation for 26 of the 28, from 20 to
  16,410 per entry, and for none does it yield zero; the two Sunshinevirus pairs yield 2
  each on 8 records. The flag records provenance and stays. ~~What is owed is a `note` on
  each of the 26 carrying its number~~ — all 28 carry one ("the archive yields N products
  and M none under this orientation (2026-10-27 run)"); verified 2026-10-30.
  `pairing_is_curator_reading` needs the paper's protocol text, one read each.
  The 20 `in-text` oligos are enumerated in `docs/2026-10-27-in-text-oligos.tsv`.
- **10 entries sit in `pending/`, every one of them for want of a verifiable DOI**
  (re-counted 2026-10-30, after the four influenza entries were promoted out).
  The three pending `Orthohantavirus_S_Anthony_2013_round1` nests (F2/R2, F3/R3, F4/R3) are the
  hard case, and the plan of 2026-10-27 was wrong about them: it proposed citing
  Aitichou 2005 with `oligos_modified`, but Aitichou prints only HANTAV1U/L, the
  ancestors of UHantaF1/R1 — and that pair is already live in `registry/` citing
  Anthony 2013, which prints it. Nothing on disk prints the three pending pairs; their
  nesting was read off amplicon geometry and one shared reverse primer, and their own
  note says to re-check that first if a source appears. They stay pending until one
  does. Of the other seven, two are `unpublished` protocol oligos (pan-parvo
  VP1, polyomavirus VP1) and stay pending by definition. The rest were searched on
  PubMed on 2026-10-27 and not found: for the feline morbillivirus L-gene pair the only
  hit is De Luca 2018 (10.1016/j.jviromet.2018.05.002), which targets P/V/C and only
  cites "a generic RT-PCR targeting the L gene"; for the enterovirus EVRV1/EVRV2 pair,
  four papers USE a 5'-UTR/VP2 assay and none designs one; for the poxvirus polymerase
  set, nothing. The design papers, if they exist, are not findable by assay description,
  which is the same wall the identity work hit.
- **Both held-out sets are spent; the drift-mechanism target is not met.** Set 1 was read
  2026-10-26, set 2's first three rows 2026-10-28 and the remaining eleven 2026-10-30 (above,
  under tier-2). Of 14 rows in set 2, 3 are `fails` and all three are `mechanism: coverage`;
  set 2 has no `mechanism: drift` row, set 1 has two (the Kulesh 2004 monkeypox pair, one
  inferred event) and the development set one, none of which meets the strict bar. `docs/journal/2026-10-24-heldout-candidates.md`
  records the first sweep. The same literature pass is the within-family negative corpus
  that gates C2, so one read per paper serves both; the search that finds a drift case is
  not the `use` family and has to be designed (see RESUME-HERE).
- **The registry is becoming an assay registry; what is left needs the maintainer, not
  another pass.** Two passes landed 2026-10-27 (`## Done`): the automatic one over the
  values a paper states once, and a reader's pass over all 64 papers the first refused.
  What remains:

  - ~~Three entries carry a value that is now disbelieved~~ — done 2026-10-28, each a
    hand deletion with a `CONDITIONS CORRECTED` note: `Cytomegalovirus_gB_Deckers_2009_round1` and the
    three Sigrist `ORTHOBORNAVIRUS_XP_*` entries lose the conventional arm's `mg_mm`;
    `Leptospira_flaB_Hsu_2013` loses an `annealing_c` that no sentence
    attributes to the flaB pair. Verified against the files 2026-10-30.
  - **The remaining rows in `docs/2026-10-27-conditions-proposals.tsv`**: the LoDs and
    master mixes, which are quoted prose rather than numbers, and the oligo
    concentrations, where only a reader can say whether a number is a stock or a final
    concentration. Both passes left them deliberately.
  - **`panels` is untouched.** Each one is a table in a paper and a read of its own.
  - **Two protocol shapes the schema cannot hold**: a touchdown or step-down (Lan 2010,
    Bocavirus, a 1998 SIV nest) has no single annealing temperature, and Ahne 1999
    deliberately varied its own between 40 and 50 °C by isolate. Each affected entry
    records the temperature its working cycles run at, or none, and says so.

  Lifting `thermo: false` is arguable for the entries that now carry an annealing
  temperature and still dishonest for the rest.

- **Registry coverage.** Audit the PREDICT consensus-PCR panel for gaps, and
  add assays in current wildlife-lab use that PREDICT never covered — fungal,
  bacterial and parasitic targets especially. Sequences only from a source that
  can be read and cited, never transcribed from a secondary list.

- **Four leftovers from the oligo adjudication** (`docs/journal/2026-10-23-oligo-adjudication.md`),
  none of them blocking: the 20 `in-text` rows, where a sequence occurs in the
  paper but in no listed oligo and may have been found inside a printed target
  rather than a primer table -- enumerated in `docs/2026-10-27-in-text-oligos.tsv`
  (this item said "never enumerated" until 2026-10-30, contradicting the
  `needs_review` item forty lines above it, which named the file);
  `Bornaviridae_N_Zimmermann_1994_round2`, which reads 0% by construction
  because storing the measured form would mean storing a sequence no paper
  prints; whether `Caliciviridae_helicase_Neill_1995` should be re-cited to
  Neill & Seal 1995 once that PDF arrives (see tier-2 validation); and
  `Orthobornavirus_XP_Sigrist_2021_aquatic`, which stores its reporter as
  "Alexa 647N" where Figure 2C labels the probe A647N, the conventional short
  form of Atto 647N — not screened, not changed, recorded.

  The lesson from that session is worth keeping: "the paper wins" is the right
  default for a *sequence* and the wrong default for a *correction*. Two of
  four changes the printed evidence supported would have destroyed a working
  assay, and only screening caught it. Any future oligo correction should be
  screened against its own archive before it is committed, with the
  before/after detected share reported.

## Architecture: fit the engineering principles (decided 2026-10-29, grilled)

The design was interviewed and settled on 2026-10-29; the decisions below are taken
and are not reopened by the steps. Vocabulary is `GLOSSARY.md`. Every step is its
own branch and PR into `main`, merged when pytest, the validator, ruff and
`check_citations` pass; the weekly run keeps using `main`. The principles this
answers are in `~/.claude/CLAUDE.md` (Engineering principles 2 to 5, Reproducibility).

Decisions:
- A one-off analysis script is a record, not a tool: once its finding is in this file
  or a journal it moves to `scripts/archive/`, untested, and git keeps the version
  that produced the number. A script is LIVE only if the Snakefile, CI, pre-commit,
  `weekly_run.sh`, or the curation workflow in `CONTRIBUTING.md` / `pending/README.md`
  calls it. About 34 live and about 70 archived; step 5f's count of 34 is the measured one.
- One `assaywatch` CLI with subcommands (`cli.py` holds parsing and nothing else);
  `python -m assaywatch.<stage>` keeps working through the same parsers during migration.
- `assaywatch curate <entry>` runs the whole curation chain and is write-through: it
  fills measured and resolved fields (`amplicon_bp`, `amplicon_disagrees_with_paper`,
  `doi_verified` when Crossref agrees, taxids) and stops only where judgement is needed
  (`status`, disagreements with the paper). Only a maintainer sets `active`, as before.
- When the PDF is missing, `curate` tries Europe PMC, Unpaywall and Elsevier (key
  present), and on failure appends the DOI to `papers/papers-fetch-list.md` and marks
  the entry waiting. It never blocks.
- `ncbi.py` owns transport (key, rate limit, retry, Entrez and Datasets) AND the two
  taxonomy caches through typed functions; it is their only writer. They stay two files.
- Renames to glossary words happen only at the new interfaces (`registry`, `ncbi`,
  `papers`, `cli`, `curate`); existing internals keep their names until touched, and
  the glossary records the aliases (`hit`, `acc`, `entry`, `n_eval`, `undetected`).
- Test tiers: `pytest -m fast` (pure functions on fixtures, under 10 s) for the
  write-test-run loop; plain `pytest` excludes `slow`; the trigger test is `slow` and
  stays in its own CI job.

Steps, in order (1 to 4 are mechanical; 5 proposes interfaces for approval first):

- [x] **1. Glossary.** `GLOSSARY.md` drafted 2026-10-29 (98 terms). The 7 the scan
      could not define (tier-2, ground truth, evaluable vs assessable, undecided,
      C-numbers vs S-ladder, the retrospective families, lineage Modes A/B/C) were
      resolved from the repo the same day, each with its source cited. Committed on
      branch `glossary` (3928be8) and merged; `CLAUDE.md` points at it. Ticked 2026-10-30.
- [x] **2. Reproducibility** (2026-10-29, PR `reproducibility`). Two scripts no longer
      hardcode `/Users/batya/assaywatch`. Of the four constants the plan named, only two
      moved to config: `THREE_PRIME_ZONE` was a second copy of
      `scoring.primer_3prime_window` (both 5), so the site table's 3' marker could have
      drifted from the scorer; it now reads that key and travels on the data
      (`PositionStat.three_prime_zone`). `LEAD_MIN_SHARE` and `MIN_RESOLVED_SHARE` became
      `sitedrift.lead_min_share` and `lineage.min_resolved_share`. `TRIM_BP` was already
      `scoring.locus_identity_trim_bp`; the settings default now reads the one constant.
      `scripts/master_sheet.py` is `assay_sheet.py` and the docs are `docs/assay-sheet.*`
      (journals and `RESUME-HERE.md` keep the old name as history). Run logs moved to
      `results/logs/` (gitignored).

- [x] **3. Test tiers** (2026-10-29, PR `test-tiers`). Default `pytest` 168 s → 43 s;
      `pytest -m fast` is 235 tests in 5 s. Two causes: the 12 Snakemake dry-run tests are
      now `slow` (CI's snakemake job runs `-m slow`; the other trigger tests stay in the
      default run), and `validate.load_assay` was re-parsing 214 YAMLs for every caller
      (a retrospective test paid 2 s each, 15 s in all), so it caches by path, size and
      mtime and hands out deep copies. The fast tier is one list in `tests/conftest.py`.
      The remaining 43 s is spread thinly: the next-largest costs are `test_match`'s
      brute-force comparison (2.5 s) and `test_score`'s screen runs (about 5 s).

- [x] **4. Hints enforced** (2026-10-29, PR `type-hints`). 29 functions annotated and
      ruff `ANN` is on for `assaywatch/` only; `ANN401` (explicit `Any`) is ignored on
      purpose. Scripts and tests stay exempt until step 5f.

- [x] **5. Deep modules and the CLI.** 5a-5g done 2026-10-29 (5g by deciding not to), one PR each, every one
      green on pytest (default and slow), the validator, ruff and check_citations.
      Interfaces are at the top of each PR and in each module docstring.
  - [x] 5a `registry.py` (PR `registry`): files / load_one / load / not_live_because /
        write / edit / archive_dir, RegistryError listing every bad file. edit() keeps
        comments, key order and quoting (ruamel.yaml round-trip; PyYAML reads) and
        validates before writing. atomic.py and groups.py are re-exports; pair_spans
        moved to match.py (not registry: it is amplicon geometry). 19 tests on a
        three-entry fixture.
  - [x] 5b `cli.py` (PR `cli`): `assaywatch <stage>`; each stage keeps its own
        parser; `python -m assaywatch <stage>` and the old `python -m assaywatch.<stage>`
        both still work. 42 call sites moved to the new spelling; the trigger test's rule
        accounting reads it.
  - [x] 5c `ncbi.py` (PR `ncbi`): eutils / datasets transports with injectable HTTP and
        sleep, TaxonRecord and the parsers, taxids_of_uids, taxids_named, the tree
        builder, and the reader/writer of the two JSON caches (two files, one writer).
        Found: a key handed to a transport was never scrubbed from errors. The
        taxa-name READER stays in lineage.py: importing ncbi there put credentials.py
        into every report rerun, which the trigger test caught.
  - [x] 5d `papers.py` (PR `papers`): Crossref + citation_matches + citation_problems,
        unpaywall / openalex / pmcid_for, europepmc_fulltext with tables legible,
        elsevier_pdf, store, queue_for_human, and obtain(doi) = the chain. Every
        network call takes a Get; 17 tests.
  - [x] 5e `curate.py` (PR `curate`, built on the four above): the chain of eight steps,
        write-through for doi_verified / target.taxid / unset amplicon_bp, TODO for
        judgement, status never touched. printed.py holds the paper-text functions the
        verifier script now imports. CONTRIBUTING and pending/README rewritten.
  - [x] 5f (2026-10-29, PR `scripts-migration`, built on `curate`). Three batches, suite
        green between each: the curation and CI scripts (check_duplicate_keys,
        check_citations, papers_index, resolve_citations; check_submission is now a shim
        over `assaywatch curate --dry-run`); the NCBI and literature callers
        (check_taxids, build_taxonomy_cache, backfill_taxids, fetch_europepmc_fulltext,
        find_open_access); and every remaining registry reader (check_amplicons,
        check_orientation, promote, and eight scripts that name registry.files /
        registry.load_one). Then twenty one-off analyses moved to `scripts/archive/`
        with an index of what each measured and where it is recorded; their seven
        test files sit in `tests/archive/`, kept and not collected. 34 live scripts.
        Kept live by judgement, not by the strict caller rule: check_candidate_identity,
        extract_conditions, extract_exclusivity, stale_screens and
        find_retrospective_cases, because the roadmap's open work or the resume point
        names them.
  - [x] 5g verified 2026-10-29, and NOT done, on purpose. `markdown_from` (287 lines) and
        `html_from` (290) share no helper: each walks the ReportModel with its own cell
        builders, and the HTML one carries widgets the Markdown cannot (sparklines, the
        timing block, slugs for anchors). A shared section list would have to carry
        format-specific payloads, which is a redesign of the report, not a cleanup. Left
        as two renderers over one model, which is what they are. The package is NOT
        reorganised into stage subpackages; the CLI gives one entry point per stage.

## Hygiene

- [x] **`registry.edit()` unfolded long quoted scalars** (found and fixed 2026-10-30,
  `docs/journal/2026-10-30-registry-edit-fold-width.md`). The dumper's width was
  `1_000_000`, so an edit re-emitted the Reid note as one 2,893-character line; it now
  folds at `_WIDTH`, the width `write()` uses. Over all 214 entries on 2026-10-30 the change
  reformats 192 on their first edit, changes the content of none and changes none twice. Prose edits
  on wrapped entries go through `registry.edit()` again.

- **The Greene SLURM profile is written and UNTESTED.** `profiles/slurm-greene/config.yaml`
  (2026-10-27) carries the partition / account / QoS stanzas, the `/scratch` filesystem
  and 60-day purge, the compute-node network question, and the `sinfo` / `sacctmgr` /
  `sacct` commands that fill each VERIFY value — written as teaching material, since
  the mechanics are new. It cannot be tested from this laptop. First submission on a
  login node closes it; until then every value marked VERIFY is a guess with the
  command that checks it beside it.

- **77 of the site's 232 mismatch charts are blank and do not say why** (found
  2026-11-03, on the 2026-11-01 run). `site_svg.mismatch_track` draws the oligo rows
  whenever an assay has oligos, even with no `positions`. All 31 drawn nest pages are
  blank, because `site.py` passes them no site data. So are 46 of 201 assay pages, because
  no position reaches `sitedrift.min_records_for_position` (20): 19 have fewer than 20
  evaluable records, and 9 of the 46 have no mismatch at all. Withheld pages draw no chart
  and are not affected.
  - [ ] **Show the fallback.** `mismatch_track` returns `""` when `positions` is empty, so
    the "No position carried..." message in `site_render._charts_block`, which no page
    shows today, can appear. Reword it to state the threshold and the highest count
    reached, and print the legend and caption only when bars are drawn. Tests that call
    `mismatch_track` in `tests/test_site.py` will probably need updating.
  - [ ] **Link nest pages to each round's map.** Replace the blank chart with those links.
    A protocol-level map would be new analysis, not a rendering fix, because the record
    sets differ (Chu 2008 astrovirus: 2,889 for the nest, 3,313 for round 2).
  - [ ] **Report failures a per-base chart cannot show**, on the page and from the calls
    table's `reason` column. `Monkeypox_virus_G2R_Li_2010_G2R_WA_F` is `declining` (9,710
    of 12,899 detected) with a blank chart: 5,235 records fail with "no probe site inside
    amplicon", 5,228 of them at zero penalty on both primers. 5,234 of the 5,235 have an
    82 bp product against 85 bp for every detected record, which suggests a 3 bp deletion
    in the probe region. Not yet checked: the alignment itself, and whether these records
    are the clade this assay is not meant to detect, which would change how to read the
    status.

## Known limitations, recorded and not work

- **`drift.anchor_fdr` cannot be settled by any evidence this project can get, and
  is closed as a stated placeholder.** 0.05 and 0.01 differ by a factor of two in
  rows moved (7,206 against 13,693; 2026-10-24 run), 0.001 is what ships, and
  tier-2 separates them on one row
  (`docs/journal/2026-10-24-archive-anchor.md`). Pricing it on the 179 bench rows
  is **impossible by construction**: `anchor_fdr` relabels records between
  `no_site` and `fail`, and a bench row is scored band / no_band, where those are
  the same answer, so no value of it can move a single bench prediction.
  `config.yaml` declares it closed and says it "stops being listed as owed work";
  it sat under `## Method debts` until 2026-10-30 anyway, which is the kind of
  disagreement between a file and this list that makes the list less trustworthy
  than the file.
- **Majority contamination.** `Enterovirus_VP3_VP1_Nix_2006_round2` cannot be
  addressed by the archive-anchor mechanism by construction
  (`docs/journal/2026-10-24-archive-anchor.md`).
- **The denominator is drift-correlated.** A record with one drifted primer
  counts as a failure; a record with both drifted leaves the denominator as
  `no_site`. 65.7% of 2.72M rows never reach the statistics, and `no_site` alone
  is 53% of every row — 357,923 of which did find a site within the mismatch
  budget and 1,085,008 of which found nothing (2026-10-27 run). The split is
  measured and printed per assay; the bias itself is not fixed, and may not be
  fixable without a different estimand.
- **Records are not independent.** The duplication check removes the duplication
  it can see (identical footprints); clade structure beyond that is unaddressed,
  so the footprint count is not a lower bound on the effective sample size.
- **ARTIC-style tiled schemes** are out of scope (2026-10-04): they would need a
  scheme object of many amplicons reporting dropout rather than one assay per
  pair, and quick-lab/primerschemes is CC BY-SA 4.0, which the registry licence
  would have to accommodate.

---

# The placeholders, for the record

`scoring` (3'/mid/5' primer penalties 3.0 / 1.0 / 0.5 over windows of 5, probe
centre/outer 2.0 / 1.0, `detect_max` 1.0, `reduced_max` 3.0,
`terminal_mismatch_fails` true, `max_ambiguous_per_oligo` 2,
`max_mismatches_searched` 6, `max_pair_evalue` 0.01); `drift`
(`detect_fraction_threshold` 0.90, `recent_window_months` 24,
`min_records_for_drift` 15, `min_records_for_coverage` 10, `min_decline` 0.05);
`degeneracy.tiers` (8 / 128 / 4096); `assemblies.per_year` 20.

One of those is no longer only eyeballed. `drift.min_decline` 0.05 has regulatory
precedent: FDA's *Policy for Evaluating Impact of Viral Mutations on COVID-19 Tests
(Revised)* (January 2023, docket FDA-2020-D-0987) tells molecular test developers to
align their primer/probe sequences against public genome databases periodically and to
act when mutations "reduce performance by 5% or more from the previously established
performance". A regulator arrived at the same floor independently, so the number is
defensible even though this project did not derive it. Two caveats are recorded beside
the setting in `config.yaml`: the policy is tied to the section 564 COVID-19
declaration, and its 5% is not stated as points or relative, where ours is percentage
points of detected share.

---

# Done

## Phase 0
- [x] repo, environment.yml, pre-commit, CI
- [x] YAML schema (pydantic) and validator
- [x] registry curated against the literature (host/barcoding/universal primers excluded as out of scope)
- [x] 5 assays promoted to `active`: Bd (Boyle 2004) done 2026-10-04 (stable, 100% of 54 recent);
      Bsal (Blooi 2013) and Oo ITS2 (Bohuski 2015) await their rDNA-query data; ranavirus MCP
      (Pallister 2007) and CDV P (Scagliarini 2007) were "watch" at ~88%.
      Satisfied; ticked 2026-10-26 after confirming all of them, plus Oo IGS and the
      Pallister intergenic pair, read `status: active`. The rDNA-query data arrived and the
      two "watch" assays were promoted on their own evidence, so the wording above is the
      state this item was WRITTEN in, not the state it closed in
- [x] run `scripts/resolve_citations.py` once (2026-10-04): 64 DOIs verified, 21 taxids filled;
      5 BAD DOIs left for review. `scripts/check_taxids.py` found and fixed 3 wrong taxids
- [x] name, license (MIT code / CC-BY registry)
- [x] only assays with a verified DOI are live; the rest wait in `pending/` (2026-10-23)

## Phase 1: core pipeline
- [x] `match`: exhaustive vectorised search, both strands, held to brute force in tests
- [x] `score`: position-weighted penalty from config.yaml, five-way call per record
- [x] three-state base comparison: degeneracy and undetermined record bases cost nothing
- [x] inosine handled as a single promiscuous molecule, not as N
- [x] degeneracy accounting reported next to the drift signal, never scored
- [x] `screen` CLI: assays x FASTA -> TSV of calls
- [x] synthetic fixture set with hand-derived expected calls (61 records, 5 assays)
- [x] `retrieve`: Entrez esearch/esummary/efetch per taxid, mdat-filtered, gzip archive + manifest
- [x] wire the stages into a Snakefile with a checkpoint; SLURM profile
- [x] first live NCBI dry run (2026-10-03): 28 taxa fetchable whole, 19 needed gene-targeted queries
- [x] first live fetch (2026-10-03): 25 taxa, ~470k records, 1.1 GB; fixed dropped connections on genome-sized pages and expired history handles
- [x] gene-targeted retrieval groups; per-group screening
- [x] dry-run the gene-targeted groups; WGS contigs excluded for bacteria; influenza opted in
- [x] first full pipeline run (2026-10-03/04): N-gaps in scaffolds made pairing cubic; fixed
- [x] manifest is state, not a Snakemake output (it was being deleted each run); atomic writes;
      archives never overwritten; `scripts/rebuild_manifest.py`
- [x] cumulative reports from cached per-archive screens
- [x] screen large archives across cores (`screen --workers`, byte-identical output); biggest archives first
- [x] `drift`: Wilson / Newcombe intervals, minimum-evidence guard, evaluable denominator
- [x] assembly-level retrieval for bacterial targets (`asm` groups, NCBI Datasets): N complete
      genomes per release year, cut to credible amplicon windows
- [x] screen amplicons on both strands (minus-strand targets were never found)
- [x] `pair_evalue` per amplicon (chance.py); scoring guard available, off by default
- [x] `scoring.max_pair_evalue: 0.01`; flagged assays split into declining / low coverage (2026-10-04)
- [x] check the two suspected oligo typos (Sarcocystis long rev, Circovirus Mankertz fwd) against
      the papers (2026-10-04, `docs/journal/2026-10-04-first-run-review.md` "Follow-up"). Sarcocystis
      P-ITSR WAS a typo, an extra C, and is corrected (98% failing -> 96%
      detected). Circovirus #174 is NOT a typo: the paper prints the extra T, so the registry
      keeps the published sequence. Both flags cleared
- [x] optional thermodynamic columns (`screen --thermo`, primer3-py): per-oligo Tm and ΔTm, never scored
- [x] `report`: markdown + self-contained HTML, per-year tables, coverage-gap table,
      degeneracy note beside the coverage trend
- [x] indel check (`scripts/indel_check.py`, 2026-10-04): across 69k sampled fail / one-primer
      no_amplicon calls, a clean single-base indel explains well under 1% of evaluable records
      for every assay but three. Gapped scoring (parasail) is not worth building. The three
      outliers are consistent same-position indels across all records, i.e. registry oligo
      typos, which makes the script a registry QA tool

## Phase 2, the parts that are closed
- [x] **18 entries on a retired taxid now carry the canonical id** (2026-10-27,
      `docs/journal/2026-10-27-retired-taxids.md`; found by the containment check in
      `docs/journal/2026-10-27-taxid-containment-and-merged-roots.md`). 11232 → 3052342
      (9 CDV), 121791 → 3052225 (2 Nipah), 11051 → 3044782 (3 flavivirus), 10292 → 3044472
      (4 herpesvirus). `data/retrieved/` was moved under the new ids and the manifest
      rebuilt in the same commit, so nothing re-fetched; each entry carries a `TAXID
      RETIRED` note. `check_taxids.py` reports 0 merged roots since (2026-10-28). The
      roadmap line for this stayed open until 2026-10-30, three days after the work.
- [x] **Per-lineage per-year rows, and the influenza verdict decomposed** (2026-10-28,
      `docs/journal/2026-10-28-influenza-decomposed.md`). `lineage.md` carries a per-year
      block under each lineage below the threshold — 252 blocks, 3,652 rows, grouped by the
      same `lineage.lineage_of` the share table uses, from deposit years read in the
      metadata pass that already ran. It answered the question it was built for on its first
      run: H3N2 has **never** been detected by the influenza matrix assay, 1.1% in 2005
      against 0.1% in 2025, so that lineage is a coverage gap of twenty years' standing and
      not drift. It also separated two effects inside one pooled 6.5%: that gap and a real
      fall in the subtypes the assay does detect (88–90% in 2009–2011 to 32–56% since 2022).
      One population proportion cannot tell those apart, which is the 2026-10-04 review's
      complaint from the other side.
- [x] **The "2026 flood of untyped influenza records" was a regex that could not read a
      partial subtype** (2026-10-28, same journal). The decomposition's apparent third
      effect was 4,729 evaluable 2026 records "whose title names no subtype", and the item
      opened on it asked for a resolver that reads the subtype from the sequence. Measuring
      the bucket first killed that: **3,857 of the 4,729 carry a subtype in the title**
      (2,220 `H1pdm09`, 1,607 `H3`), and the shipped `\((H\d+N\d+)\)` required both numbers.
      Broadened to `\((H\d+(?:N\d+v?|Nx|pdm\d+)?|Hx(?:N\d+|Nx)?)\)` and shipped under both
      of `config.yaml`'s gates (tier-2 identical, `report_diff` "No assay changed status").
      4,188 records across all years leave the residual bucket carrying 8 detections, into
      H1pdm09 (0 of 2,220), H3 (5 of 1,745), H1, HxN2, H3Nx — effect 1 again, since
      `H1pdm09` is pandemic H1N1 and `H3` is H3N2 with the N untyped. The residual
      *Alphainfluenzavirus influenzae* row goes from 9.3% to **23.1%**: the pattern was not
      only missing labels, it was halving the share of the row that means "unknown". **No
      sequence-based subtype resolver is wanted** — 872 records carry no label at all.
- [x] **A registry edit that cannot change a call no longer rescreens anything**
  (2026-10-28, `docs/journal/2026-10-28-screen-signature-projection.md`). **The claim
  this item was opened with was wrong**: the signature was already per-group, not
  whole-registry — `screen_signature(taxid, group)` hashed only that group's own assay
  files, and the "357 screen jobs" read off a stopped run were the post-checkpoint DAG's
  denominator, not a work queue. What was true is subtler: it hashed each entry's whole
  YAML, so a curator's note, a review-flag wording or a `conditions` block invalidated
  every group holding that entry. `signature.screen_key` now hashes the screen-relevant
  projection instead. Replaying the two days of curation: **108 of 125 groups and 444
  archives rescreen under the old scheme, 10 groups and 47 archives under the new one**,
  and those 10 are the ones that should — four retired-taxid roots, BPSV and its two
  neighbours gaining `exclusivity_taxids`, the calicivirus flag change, and the
  orthoreovirus pair gaining a flag.
- [x] **A published exclusivity claim is visible, and the first one tested reconciles two
      numbers this registry carried in contradiction** (2026-10-28,
      `docs/journal/2026-10-28-bpsv-exclusivity-reconciled.md`). The report has a
      status-independent `## Published exclusivity claims, tested` section, because the
      cross-reactivity table lived inside the flagged-assay detail block and BPSV is
      `insufficient data` — so its 2,692 off-target calls were computed and invisible, which
      is the usual case for an assay whose neighbour had to be fetched. Two fixes made it
      worth printing: the denominator is EVALUABLE off-target records, not everything
      screened (the orf virus claim read "0 of 2,498" where 2,413 of those records hold no
      product for anything), and `amplified` prints beside `detected`, because a mismatched
      hydrolysis probe is not a detection and the assay forms a product in 82 of 85
      evaluable orf virus records while detecting none of them. The 2026-10-24 hand screen
      and Zhao's panel were never in conflict: the primers are genus-specific and the probe
      separates the species, which is what the paper says.
- [x] **A reader's pass over the 64 papers the automatic one refused** (2026-10-27,
      `docs/journal/2026-10-27-conditions-curator-pass.md`). 236 values read by hand with
      the sentence each came from, and **twelve values an earlier pass had written
      corrected**, every one of them an attribution rather than an extraction: Xiao 1999's
      two programmes (55 °C is the nested RFLP protocol the registry holds, 60 °C the
      full-length SSU it cloned), Latimer 2010's "redundant POL PCR" against "all other
      PCR amplification", Zhao 2013 saying in its own words that BPSV is kept at 60 where
      the automatic pass had read 62.5 off the PCPV assay, and Spackman 2002's matrix set
      at 60 °C where the entry carried the H7 assay's 58. A sixth extraction bug came out
      of it: a degree sign the PDF renders as the digit 8, so "948C" matched as 48 °C —
      which is where `Orthoherpesviridae_POL_VanDevanter_1996_round1`'s 48 came from, against a paper that
      prints 46. Re-running the whole pass after the fix moved 2 of 644 proposals, both
      that entry, and recovered two values whose hand-read agrees.
- [x] **The registry knows what temperature 119 of its assays ran at** (2026-10-27,
      `docs/journal/2026-10-27-conditions-first-pass.md`). `conditions` / `performance`
      / `panels` validated empty first, then `scripts/extract_conditions.py` read the
      178 papers on disk and proposed 644 values with the sentence each came from;
      `--apply --only-sole` took the 292 that need no judgement. Five extraction bugs
      were found by looking at the numbers, four of which pass any range check — a
      spaced-out decimal point read 25 mM where the paper says 1.25, a decimal comma
      read 0 mM, and a 50 mM stock was read as a final concentration the same sentence
      states as 1.5 mM. `format` is not a block, and the reason is in the commit.
- [x] **A registry key given twice loaded silently, and one entry's note was lost for
      three days** (2026-10-27). `yaml.safe_load` takes last-wins, so two
      `notes_curator` keys left the first value in the file and in no loaded entry,
      past the validator, the screen and the report. `scripts/check_duplicate_keys.py`
      walks the node tree — by the time there is a dict the evidence is gone — and runs
      over every registry and pending file on any registry commit, where `check-yaml`
      sees only the files one commit touches. That is the second gate in two days found
      to be looking at a subset, both times through a duplicate YAML key.
- [x] **A near neighbour a paper claims to exclude is fetched on purpose** (2026-10-27).
      `target.exclusivity_taxids`: each named taxon becomes its own retrieval group on
      the assay's own query, so a published specificity claim can be screened instead of
      being represented by whatever happened to be on disk. No new group kind and no new
      cap; the scope filter already keeps those records out of the denominator and the
      cross-reactivity table already shows them, now marked `claimed` so a reader can
      tell a specificity result from a coincidence. The schema refuses the target's own
      taxid and anything also in `scope_taxids`. BPSV is the first entry: 124 retrieval
      groups become 125, because its orf virus arm shares the archive `ORF_VIRUS_...
      _Zhao_2013` already fetches and only pseudocowpox virus is new.
- [x] **The influenza matrix probe is failing on H3N2 and H1N1 and working on the avian
      subtypes** (2026-10-27, `docs/journal/2026-10-27-influenza-sublineage-enabled.md`).
      `lineage.sublineage` is on for that assay: a title regex splits one NCBI name into
      57 subtypes, and on the corrected numerator the ordering inverts against the
      pre-fix table — H3N2 1.2% of 38,771, H1N1 2.6% of 27,725, H5N1 34.0%, and thirty
      avian subtypes at 85–100%. The pooled 6.5% is the two human-circulating subtypes;
      a single proportion could not say that. Enabling it moves nothing (tier-2 identical
      case for case, 0 of 193 statuses), so it is adopted for what it reports.
- [x] **The `taxon_name` mismatches are closed at both ends, and 0 remain** (2026-10-27,
      open since 2026-10-04). Three were ICTV binomial renames where the stored name was
      the paper's (ABPV, BQCV, SBV), renamed with the paper's name kept in parentheses.
      The other eight were never wrong: a species-level name on a deliberate genus-level
      taxid narrowed by explicit organism taxids in the query (Grizzle 2003 LMBV on genus
      *Ranavirus*, seven Latimer 2010 EEHV entries on genus *Proboscivirus*), which
      `check_taxids.py` could only read as `MISMATCH`. It now has a `SCOPED` status that
      reads the query, requires every pinned organism taxid to descend from the entry's
      own taxid — a query reaching outside the root is the Mycoplasma failure again and
      still reports `MISMATCH` — and then asks whether one of them carries the stored
      name. All eight resolve, naming the species they fetch. 0 mismatched taxids.
- [x] **C1's hierarchical layer, measured on both halves of its plan** (2026-10-27).
      Built (`assaywatch/hierarchical.py`), printed beside every verdict; first kill test
      does not fire (φ 0.3–11.7 on multi-lineage assays, intraclass correlation
      0.08–0.78); second kill test does not fire either — `lineage.verdict_from: posterior`
      leaves tier-2 identical and moves 0 of 240 statuses
      (`docs/journal/2026-10-27-c1-second-kill-test.md`). As a verdict input it changes
      nothing, so it ships beside the verdict with `verdict_from: holm`. What it earns is
      honest numbers for thin lineages, not a different decision.
- [x] **`score.load_config`'s per-chemistry cache is keyed to the scoring block it came
      from** (2026-10-27), so a shallow copy that swaps the block recomputes instead of
      answering from the shipped table — the footgun that bit two callers today.
- [x] **M1 ships: `scoring.mispair_penalty: {"G:T": 0.0, "T:G": 0.0}`** (hold lifted
      2026-10-27, a maintainer decision, after S4 measured its only documented cost away:
      no catch lost, the influenza 2010 case promoted to the drift flag, PPV 3/9 -> 4/10,
      five bench rows fixed and none broken). The rule is no longer wholly identity-blind.
      **Confirmed by screen the same night** (`docs/journal/2026-10-27-m1-confirming-rescreen.md`):
      the real run agrees with the S4 replay on all but 153 of 2,679,894 rows, every
      disagreement pessimistic; 8 statuses move against the pre-M1 run. The Kwok premium — A:G, G:A, C:C at 2.0, A:A at 1.5 — was priced
      the same evening as S6 and **killed on both pre-registered criteria**: one FAP
      band row broken and nothing fixed, one false alarm added and no catch
      (`docs/journal/2026-10-27-s6-kwok-premium-killed.md`). The discount half is the
      half this registry can use.
- [x] **Five Huo 2022 entries add clade- and lineage-level mpox typing** (2026-10-27).
      Two multiplex panels designed on 138 poxvirus genomes, one entry per probe: clade
      IIa/IIb, clade I and non-MPXV orthopoxvirus on one F3L-region pair (179 bp,
      measured on 28,921 products), B.1 and non-B.1 SNP probes on a second (81 bp). 15 of
      15 oligos `exact` against the open text; DOI resolved and checked; all `draft`.
      Mills/Greninger 2022, the other candidate, designs nothing — its G2R set IS the
      registry's Li 2010 generic entry, which made it the second row of held-out set 2
      instead (`docs/validation-cases-heldout-2.tsv`, a `works` case on 2022 clinical
      specimens with identity read from the page).
- [x] **28 `orientation_inferred` flags carry the archive's answer** (2026-10-27): the
      product count under the stored orientation from the 2026-10-27 run, appended to
      each flag's note and never substituted for it. 26 confirmed by twenty or more
      products, two Sunshinevirus pairs too thin to say. Three bee-virus `taxon_name`s
      now carry NCBI's binomial with the paper's name in parentheses.
- [x] **The full run under today's scoring, published** (2026-10-27,
      `docs/example-run-2026-11-01/`, `docs/journal/2026-10-27-live-run-and-schedule.md`).
      16 statuses move against 2026-10-26; both S3b predictions checked, one of them
      corrected in the write-up (the flavivirus move was a 2017 retrospective verdict, not
      a 2026 status). S3b's replay agrees with the real screen on all but 8 of 2,679,894
      rows, which closes the 78 unrescreened movers. The weekly launchd job is installed
      live on this machine for Sunday 09:00.
- [x] **The unnamed lineages were a missing roll-up, not missing names** (2026-10-27).
      775 of the 1,390 rows in the 2026-10-26 lineage report read `taxid_<n>`. Three
      diagnoses in one day, each measured: rebuilding the taxonomy cache named 3; keeping
      names for no-rank grouping keys named 3 more; and then the cause — every one of the
      322 taxids HAS a species above it (MPXV is 10244, no rank, under species 3431483),
      and `lineage_report.py` never applied `lineage.group_at_rank: species`, which
      `drift.py` applies for report.md. So lineage.md said `taxid_10244` where report.md
      said "Orthopoxvirus monkeypox (3431483)" of the same records. The roll-up is now
      applied in both: 1,941,507 call rows roll up, **775 unnamed rows become 2**, and
      1,390 rows become 1,084 because strain-level rows merge into their species.
- [x] **The lineage layer counts a detection the way the verdict does** (2026-10-27).
      `lineage.py` hard-coded `("detect", "reduced")`; since the probe switch that is wrong
      for 51 entries, and the influenza matrix assay read 6.5% pooled and 72–100% per
      subtype from the same calls, with `worst_lineage_verdict` able to override a status
      on the wrong numerator. `per_lineage_stats`, `lineages_never_covered` and
      `lineages_ever_covered` take the assay's `detected_calls`; `drift.py` passes its own
      and `lineage_report.py` reads the chemistry map the way `report.py` does. Four tests
      pin that the numerator moves and the denominator does not.
- [x] **The window and the minimum are priced together** (2026-10-27,
      `scripts/archive/window_grid.py`, `docs/journal/2026-10-27-window-minimum-grid.md`). On the
      development set the minimum does nothing to the matrix between 10 and 20 — it only
      trades refusals (14 / 15 / 16 declined) — and at 30 it refuses 20 for no gain. The
      window does: 12 months loses a documented catch (kill), 36 months keeps all six and
      drops one false alarm (4/32, PPV 2/8). Nothing ships, because the set is spent for
      threshold-setting; 36 / 15 is the one cell a held-out read would be worth spending on.
- [x] **Triage no longer leads with a coverage gap** (2026-10-27). Degeneracy-severe
      assays were already held off the Start here list; `declining` rows whose own note
      says the failing lineage is "a coverage gap rather than drift" now sort after the
      rest of `declining` and before `low coverage`. No status changes; a test pins that
      the rows handed in are the rows handed out. `report.triage` criterion 1b.
- [x] **C1 conjugate, measured as its plan specified** (2026-10-27). Every per-lineage
      interval in the 2026-10-22 report three ways: Wilson and Jeffreys disagree on 1 of
      1,351 lineages, and the 704 zero-width Wald intervals were the only real defect,
      already fixed by Wilson on 2026-10-23. `drift.flag_rule: posterior` (P(θ < 0.90) >
      0.95, Jeffreys prior) moves 2 of 233 statuses, both `watch` -> `low coverage` at
      small n, and leaves tier-2 identical case for case. Exhaustively over 15 <= n <=
      400 the two rules disagree on 425 of 69,581 cells and the posterior always flags
      MORE. Not killed, not adopted: ships `wilson`, mechanism kept.
      `docs/journal/2026-10-27-c1-posterior-flag-rule.md`.
- [x] **A scoped taxon that leaves its retrieval root is now detected** (2026-10-27).
      `scripts/check_taxids.py` tests every `scope_taxids` entry's NCBI ancestor list for
      the assay's `target.taxid`, resolving merged ids first — its first run reported
      4,113 escapes, every one a false reading of a merged root, which is how the 18
      retired taxids above were found. Second run: 0 escapes. The Mycoplasma case that
      motivated it is rooted at a phylum and scoped by query, so it is not the shape
      this guards; nothing in the registry is, today.
- [x] **A trend statistic exists** (2026-10-27). `assaywatch/trend.py` runs the
      Cochran-Armitage test over deposit year and the report prints z and a two-sided p
      under every flagged assay's per-year table. Beside the verdict, never into it — a
      test pins that two assays with opposite trends inside the same baseline get
      identical statuses — and with no threshold, because the project has no evidence
      to set one. `related-work.md` contribution #2 now says what ships. Still owed: a
      version over distinct footprints rather than records, since the same clade
      structure that narrows every interval inflates this z.
      `docs/journal/2026-10-27-trend-statistic.md`.
- [x] **`partial` rows count as catches, scored separately** (decided 2026-10-27). The
      third of the three decisions PR #3 asked for, and the last to be settled.
      `scripts/retrospective.py` prints a `partial gaps named` line of its own and the
      `fails` numerator — the paper's main figure — never includes one. A test pins
      that the two lines move independently.
- [x] **CONTRIBUTING states best-effort review, no turnaround** (2026-10-27), and says
      what makes a submission quick to review: validator passing, a resolvable DOI, and
      oligos readable from the cited paper's own table.
- [x] **The ΔTm column is in register** (2026-10-27). `thermo.duplex_tm` called
      `primer3.calc_heterodimer`, which returns the most stable structure between two
      sequences; on a mismatched site that is a shifted, shorter, near-perfect duplex
      reporting an optimistically small ΔTm, least trustworthy on exactly the records
      the report is about. It now sums nearest-neighbour terms base-for-base
      (Biopython `MeltingTemp.Tm_NN`, SantaLucia & Hicks 2004 with the
      Allawi/SantaLucia mismatch tables), so there is no alignment search and no
      register to get wrong. **Re-running the bench comparison cost the
      thermodynamic arm half its margin: p = 0.0192 became p = 0.0708**, so the
      "thermodynamics beats the penalty rule" claim does not survive its own
      confound, while the penalty rule's 23 false negatives against 1 false positive
      do. Adjacent mismatches have no measured term, so 32 sites are withheld with
      `thermo_note: nn_unsupported` rather than scored as free.
      `docs/journal/2026-10-27-thermo-vs-penalty-paired.md`.
- [x] **`reduced_not_detected_for: [hydrolysis_probe, mgb]`** (2026-10-27). A
      mismatched hydrolysis probe is no longer counted as a detection: detection IS
      the probe, and there is no gel to look at. Measured before it was taken, by
      rendering the 2026-10-26 calls table both ways — 13 of 235 statuses move, in
      both directions, and `Influenza_A_virus_M_Spackman_2002` goes
      `stable` -> flagged at 6.5% of 30,382 recent records, which is the documented
      failure this switch exists to catch. It costs two published positives on the
      Leptospira bench panel; that cost stands and is recorded beside the setting.
- [x] **A new held-out set, opened with the first confirmed identity** (2026-10-27).
      `docs/validation-cases-heldout-2.tsv`. The development set is frozen and the
      first held-out set was read on 2026-10-26, so the project had no unread
      evaluation data; the Leetz 2007 case went there rather than into the dev set,
      because a dev-set row can never be un-read. It reads `works`: the paper's
      73.8% is an oocyst dilution series on one isolate, which is sensitivity, and
      this tool does not model sensitivity.
- [x] **The TNTBLAST arm is deferred, not forgotten** (decided 2026-10-27). No
      osx-arm64 build, and Rosetta 2 is a system change needing admin rights. It
      waits for Rosetta, an arm64 build from source, or a run on linux-64 or the
      cluster; `scripts/archive/compare_thermo.py` takes a second predictor unmodified.
- [x] **The ranavirus MCP 18/19-mer question is closed** (2026-10-26, confirmed
      2026-10-27 by re-running the verifier). Mao, Hedrick & Chinchar 1997 has been
      on disk since 2026-10-25 and its Table 2 prints both primers as 18-mers,
      byte-identical to the registry, with no 19-mer anywhere. Stöhr 2015's extra 3'
      T is a later extension, not a base this registry dropped.
- [x] the recent window now widens per assay (`max_window_months`, 60) when the
      standard window holds too few records, which is what made Bd unjudgeable;
      `scripts/retrospective.py` recomputes any past date's verdict, so the
      window and the minimum can be calibrated together against real cases
- [x] **Duplication check** (2026-10-05, review 3.3, partial). Each assay now also reports how many
      distinct binding-site footprints sit behind its recent window, the interval at that many
      independent draws, and for a flagged assay whether the flag survives it. Reported beside a
      verdict and never into one: a test pins that statuses and intervals are identical with and
      without footprints. This removes the duplication it can SEE (identical footprints); clade
      structure beyond that is still unaddressed, so it is not a lower bound on the effective
      sample size. The review's "weight each distinct haplotype equally" was rejected: one
      sequencing error in a primer site is a unique failing footprint, so a healthy assay would
      read as mostly failing. Corrected 2026-10-06 after two adversarial reviews: a flag now
      needs at least `min_records_for_drift` distinct footprints to be reported as surviving
      (it had reassured at every count below that, up to 19), must also stay below the
      threshold when each distinct footprint is counted once (the sample-size reduction alone
      cannot see one clone carrying the failures), and records with no footprint information
      make the count unknown instead of counting as one real footprint.
      Corrected again 2026-10-27: `count_diverged_as_fail` gave a promoted row no footprint, and
      one such row made the count unknown for the whole assay, so the check ran on 12 of 71 flags
      and the triage list it gates on was empty. With a coarse taxid-derived footprint, 23 of 71
      hold and `Start here` shows 10 assays. No status changed.
- [x] **What the report claims is now what it measured** (2026-10-14, from an
      external review). Three changes, none of them to a computation:
      `declining` requires the assay to have cleared the threshold in some
      earlier year (`drift.require_working_baseline`), which moves 14 of the 37
      assays flagged on 2026-10-07 — all pan-family consensus PCRs screened
      against a whole taxon — into `low coverage` with a note that they are
      also falling; the duplication result (35 of 84 flags held) is printed
      beside the flag counts at the top instead of only inside the per-assay
      detail; and both reports carry an `entry` column plus a header line
      saying how much of the registry is `draft`: on 2026-10-14, 210 of 214 entries
      were (205 of 208 on 2026-10-23), and the table had presented them exactly
      like the one `active` assay.
      Registry counts are now printed by `python -m assaywatch.validate
      registry` rather than written into prose, where they had drifted to
      164/142/21 against an actual 214/167/44.
      Extended 2026-10-27: the report named Benjamini-Hochberg where the run used Holm, so the
      label is now read from `config.yaml`; exclusion counts reconcile for all 71 assays; and
      the `claims` hook built to catch stale prose counts had been silently disabled since three
      duplicate `files:` keys landed on it, which `check-yaml` now makes an error.
- [x] **Pan-family scope logic** (`target.scope_taxids`): records outside an
      assay's declared scope leave the drift denominator and are reported as
      cross-reactivity instead. Asked for 2026-10-18, shipped; the specificity
      arm built on it 2026-10-27.
- [x] **Sequence-cluster lineages** (`assaywatch.subcluster`,
      `lineage.cluster_resolver`): assays whose target species carries
      within-taxid diversity at the primer sites can be grouped by primer-site
      homology and each cluster treated as a lineage. Asked for 2026-10-18.
- [x] **The lineage binomial no longer overflows.** `comb(n, k) * p**k * q**(n-k)`
      went to nan above n ~ 1030; it is computed through `binom.cdf` instead
      (`assaywatch/lineage.py`). Asked for 2026-10-18.
- [x] **Data integrity before any retrieval** (2026-10-27). An empty efetch page was
      accepted as zero records and the run recorded, after which the incremental cursor
      skipped records that were never written; a short page was indistinguishable from the
      legitimate WGS-master case; the cursor was keyed on the assay query only, so changing
      a length filter permanently skipped older records that newly qualified; a missing
      `.sig` wedged the pipeline unrepairably, and declaring it as an output was not enough
      because nothing requested it; and `--config` overrides moved the cache key, triggered
      a full rescreen, and never reached the subprocess.

## Review history

`docs/journal/2026-10-04-pipeline-review.md` reviews the pipeline stage by stage from a
software and a methods angle. Its short version — the estimand is wrong (one
population proportion per assay cannot see a lineage-conditional failure, which
is why validation caught 1 of 12), the denominator conditions on the outcome,
records are not independent so the intervals are too narrow, and declared
amplicon sizes are not enforced — is still the best one-paragraph statement of
what is wrong with the method. Amplicon enforcement shipped; the other three are
items 4–9 and the limitations above.

`docs/journal/2026-10-27-four-perspective-review.md` is the most recent, read from four
angles (engineering, methods, bench diagnostics, a cold newcomer read), and every
open item it raised is in this file.
