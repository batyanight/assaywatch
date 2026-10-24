# Scope audit: which entries are judged against organisms they were never designed for

Branch `experiment/2026-10-24-diverged-and-anchor-fdr`. Read-only audit; no registry
entry changed. Opened by `docs/2026-10-24-anchor-pair-counterfactual.md`, where the
`count_diverged_as_fail` pair turned `BORNA_VIRUS_N_gene_Zimmermann_1994` from `stable`
to `declining` on records belonging to parrot and rattlesnake bornaviruses.

## The count

All 200 entries, `target.taxid` resolved to a rank by live `efetch`:

| scope rank | entries |
|---|---|
| species / no-rank-virus-species | 54 |
| genus | 82 |
| family | 30 |
| no rank (strain-level virus nodes) | 16 |
| subfamily | 8 |
| phylum | 3 |
| species group | 3 |
| clade | 2 |
| order | 2 |
| **no taxid at all** | **1** |

**146 are scoped broader than species, and that is mostly correct**: a pan-adenovirus or
pan-coronavirus consensus PCR should carry a family taxid. Breadth is not the bug. The
bug is a single-organism assay under a multi-organism denominator.

## The registry already has the mechanism, and it is applied unevenly

`Target.scope_taxids` (`schema.py:261`) exists for exactly this: out-of-scope records are
still retrieved and screened, so cross-reactivity stays measurable, but they drop out of
the drift denominator (`drift.py:252` and `:1052`, ancestral matching via
`taxonomy.within`). The ancestry lookup is fed by
`data/retrieved/.meta.taxid.backfill.tsv.gz`, 1.28M accessions, present.

Of the 146 broad-scoped entries:

| state | entries |
|---|---|
| `scope_taxids` set | 12 |
| `target.query` pins `txid…[Organism:exp]` | 13 |
| flagged `scope_narrower_than_taxid` but NO mechanism | 3 |
| neither, and mostly pan- by design | 118 |

So the fix for a real case is normally **adding `scope_taxids`, not editing
`target.taxid`**. Re-keying the taxid splits the retrieval group, orphans
`data/retrieved/<taxid>/`, and destroys the cross-reactivity measurement.

### Three entries the registry already knows about and still mis-scores

`needs_review: scope_narrower_than_taxid` records the problem; nothing acts on it.

| entry | scope | records | dominant organism share |
|---|---|---|---|
| `AVIPOXVIRUS_dsDNA_4b_core_Baek_2020` | genus | 1,735 | 36.0% |
| `CHLAMYDIA_genus_16S_Messmer_1997_round1` | genus | 1,668 | 30.7% |
| `BATRAVIRUS_terminase_Licheri_2020_european_FW2_RV1` | genus | 8 | 25.0% |

The Batravirus note says in as many words "Flagged so a low genus-level share is not read
as drift" — but the share is still computed that way.

### Four sibling groups that disagree with themselves

Same taxid, same DOI, nested rounds of one protocol, one round scope-filtered and the
other not — so the two rounds' percentages are not comparable. All four are PREDICT panel
entries and none records a reason for the asymmetry.

| group | has `scope_taxids` | has none |
|---|---|---|
| Adenovirus Pan Polymerase (10.1128/JVI.78.23.13366-13369.2004) | `round1` (769 taxa) | `round2` |
| Paramyxovirinae L gene (10.1128/JCM.00192-08) | `Tong_2008_round1` (931) | `round2` |
| Enterovirus VP3/VP1 (10.1128/JCM.00542-06) | `round2` (520) | `VP3_VP1` |
| Polyomavirus VP1 (10.1128/JVI.79.6.3883-3887.2005) | `Johne_2005` (424) | both `PREDICT` entries |

Copying the sibling's list is a one-line change per entry and needs no paper.

## Per-paper findings

Oligo identity was confirmed against each paper's own printed table before scope was
considered. **No identity failures in any entry audited.**

### Bornaviridae — Zimmermann 1994, three entries

Designed on one BoDV-1 cDNA clone (Methods p. 135, oligos "designed according to
published sequences from the cDNA clone pAB5"), validated on BoDV-1 only: "32 horses, 1
donkey and 3 sheep" (Results §3.2). Avian bornaviruses were not described until 2008, so
the paper could not have claimed more.

Measured: the `178830/all` archive holds 1,517 accessions, **509 BoDV, 1,008 (66%)
something else** — 450 PaBV-4, 159 PaBV-2, 80 ABBV-1, 64 legacy "Avian bornavirus", 42
CnBV-1, 31 variegated squirrel bornavirus 1, plus rattlesnake and cottonmouth
bornaviruses.

Proposal: `scope_taxids: [1714619, 12455]`, taxid unchanged. **12455 is not optional.**
Verified by efetch: taxid 12455 "Borna disease virus" (species) sits in
`Bornaviridae > unclassified Bornaviridae`, i.e. NOT under Orthobornavirus, so a scope
list built only on 1714619/1714621 silently drops 49 genuine BoDV-1 deposits. Whether
BoDV-2 (3 records, inside *Orthobornavirus bornaense*, described six years after the
paper) belongs is a maintainer's call.

### Orthobornavirus — Sigrist 2021, three entries

These are not the shape they look like: the triplex split per probe is correct, and the
primers are genuinely pan-genus. The *probes* are species-group specific by the paper's
own measurement (§2.2, §3.2: each probe detected only its own group, and "BoDV-1 and
BoDV-2 were not detected when using any of the three probes"). The genus denominator
scores each entry against the other two's targets.

Of the 1,360-accession archive the in-scope counts are psittacine 637, passerine 85,
aquatic 82. So the passerine entry's reported 3.8% and the aquatic entry's 0.0% are
computed with ~94% of the denominator out of scope: cross-reactivity numbers wearing a
drift number's clothes.

Proposals, taxid unchanged: psittacine `[1548713]`; passerine `[1548720, 1548721]` — two
are needed, because CnBV-1/-2/-3 are *Orthobornavirus serini* while EsBV-1 is
*O. estrildidae*; aquatic `[1548722]`. Expect the passerine entry to fall below the
15-record minimum and report "cannot assess" instead of 3.8%, which is the honest outcome.

Separately, 64 legacy "Avian bornavirus" (675389) records sit in *unclassified
Bornaviridae*, so all three entries never see them — a retrieval gap, not a scope one.

### Helicobacter — Conley 2021: the assay cannot reach its own reference sequence

The sharpest finding in the audit. The paper is explicit that the assay is "specific for
*Helicobacter* sp. Grand Cayman Blue Iguana 1 (GCBI1)" with "the Taqman probe targeted a
14bp insertion unique to" it.

The reference the authors deposited, **MG910456**, carries taxid **290433**, whose lineage
I verified is `… Campylobacterales; Helicobacteraceae; environmental samples` — **not
under genus *Helicobacter* 209**. The entry's scope is 209. So the one sequence the assay
is built to amplify is unreachable from the taxon the pipeline screens, and the entry
duly reports **0.0% detected on 18 evaluable records against a 0% baseline of 777**.

Proposal: taxid **290433** (species, `uncultured Helicobacteraceae bacterium`). Stated
plainly, this is a workaround: 290433 is an environmental wastebasket node, no taxon for
GCBI1 exists, and it will pull in unrelated uncultured Helicobacteraceae. It turns a
meaningless 0% into a real measurement.

Also: the standing "`209/all` Helicobacter has never been screened" item is **stale**.
Taxid 209 has 6,008 screened records across three archives. The entry with no records is
`Helicobacter_Pan_Helicobacter_16S_short_Fox_1998`, a different one of the three.

### Leptospira — two entries, and no taxid fits either

`LEPTOSPIRA_lipL32_Ahmed_2020`: the paper designed on "10 pathogenic *Leptospira*
species" and its 73-strain Table 1 scores **all 6 intermediate and all 6 saprophytic
species negative** (*L. biflexa* Patoc I, *L. meyeri* Semaranga, and the rest). Genus 171
therefore puts ~12 species into the denominator the assay is designed never to detect.
**No usable taxid exists**: `Leptospira[Subtree]` has no clade, species-group, subgenus or
no-rank node; all 1,364 children are species, serovars or strains. P1/P2 are literature
concepts with no NCBI node. The fix is an explicit 16-species list (two of which NCBI has
since renamed: *L. dzianensis* → *yasudae* 2202201, *L. putramalaysiae* → *stimsonii*
2202203, so a curator checking by name will not find them). Note 171 is also in
`config.yaml` `assemblies.taxa` and would need the same treatment.

`LEPTOSPIROSIS_Flagillar_filiment_Prote`: **leave 171; do not narrow.** The entire mention
of Leptospira in the cited paper is one row of a MassTag panel table labelled
*L. interrogans* flaB; the organism was never detected and never discussed, and both
primers carry degeneracies, which is what you do to cover several species. Narrowing to
173 on a panel label would be a guess. Consistent with the entry's existing
`citation_is_indirect` flag; the real design source is still unfound. Cosmetic: the gene
field reads `Flagillar filiment Protein B gene` — two misspellings of "flagellar
filament".

### Mycoplasma — Feldman 2006: the phylum taxid is less wrong than it looks

The designed target is "the box turtle *Mycoplasma* sp.", a new unnamed species whose 16S
is "closely related to, but distinct from, *M. agassizii*" at 98.2–98.4% identity. So
*M. agassizii* is the paper's nearest **non-target**. The organism was never deposited and
has no NCBI taxon, so no narrowing is possible — and the phylum root is unavoidable for
retrieval, because the three species in the query sit in three families and two orders
(lowest common node is class Mollicutes, 98,524 records). The `taxon_name` field already
discloses this.

Two things worth changing, neither the taxid: the query asserts three target species the
paper never cultured (*[Mycoplasma] testudinis* 33924 appears nowhere in the paper and
should come out; *M. agassizii* should stay but be read as cross-reactivity); and the open
`target_annotation_uncertain` flag can be closed — Feldman's own *E. coli* coordinates
449→1466 are both inside 16S and the paper states "The amplified products (993
nucleotides)", so it is 16S, not the 16S-23S spacer, and the measured 994 bp sits 1 bp
from the source. Cacciotto's "16S-23S intergenic, 996 bp" is wrong about someone else's
assay.

### Cytomegalovirus — Deckers 2009 and Prepens 2007, four entries: NO CHANGE

Both papers are pan-primate by design, so the genus taxid is right and narrowing to HCMV
would be the opposite error. Deckers: primers "designed to bind conserved sites in the
genomes of HCMV variants and great ape CMVs" from "a multiple alignment of all human and
primate CMV gB genes available in Genbank", described in the Discussion as "universal
primate CMV primers". Prepens is the clearer case, and answers the question directly: the
CM-gB set was "used for amplification of members of the genera Rhadinovirus,
Lymphocryptovirus and Cytomegalovirus", is called "genus-specific" in the Figure 1
legend, and was validated beyond great apes — two distinct gB sequences from a black-and-
white colobus (an Old World monkey), differing 18% from each other.

Residual, too small to act on: NCBI's genus has since absorbed muroid, shrew, bat and
suid CMVs, which are outside "human and primate CMV". That is ~21 records against 13,831
under the genus, 12,513 of them HCMV. A note at most.

### SIV — three entries, three different answers, and one of them is not about scope

`RETROVIRUS_RNA_polymerase_SIV_Keele_2009`: **stopped on identity, which outranks scope.**
PTS-spol-F2 / PTS-pol-R2 do not appear in Keele 2009 and could not be found anywhere —
0 hits across `papers/`, 0 in a Europe PMC full-text search of both sequences and both
primer names. The repo's own `results/oligo-verification-2026-10-23.tsv` already records
the sibling pair as `no-oligos`: "the text held for this paper prints 0 oligo-like
run(s)". Keele 2009 says only that infection "was confirmed by RT-PCR" and cites Santiago
et al. 2003 (J Virol 77:7545), which is paywalled. The "PTS" prefix is
*Pan troglodytes schweinfurthii*, consistent with that being the true source. **No scope
proposal is made for this entry until the citation is settled**, and the same defect
affects the round-1 sibling under the same DOI.

`RETROVIRUS_RNA_polymerase_SIV_Takehisa_2009`: identity exact against the paper's
"degenerate HIV-1/SIVcpz/SIVgor consensus primers". The designed scope is that clade, not
the polyphyletic whole of SIV, so this IS the Borna pattern — but it **cannot be fixed by
taxid**: SIVgor has no NCBI taxon at all (Takehisa's own FJ424863/FJ424864 are filed
directly under 11723), and `Simian immunodeficiency virus - cpz` (388909) returns 7
records under the entry's own query against 8,252 for 11723. Narrowing would collapse the
denominator and exclude the paper's own sequences. What is needed is a record-level clade
filter on strain name plus sequence assignment. The entry's curator note already does this
informally — "SIVgor 8/8 detected, SIVcpz 15/30, everything else 5/181" — and that 5/181
on out-of-clade SIV is exactly the drift that is not drift. It should be a structured
field rather than prose.

`RETROVIRUS_RNA_polymerase_SIV_Characterization_2001`: **no scope change** — Clewley 1998
is a pan-primate-lentivirus consensus nested PCR, designed from "a multiple alignment of
HIV-1, HIV-2, and SIV sequences" and shown to amplify both HIV-1 and a novel SIVdrl from a
drill monkey. If anything 11723 is marginally narrow. Its primers are also unread from the
source (printed in an image), though the chain through the PREDICT supplement is
documented.

### Influenza H5 and H7 — Tsukamoto 2010: not taxid-fixable, and the existing workaround leaks

Correcting my own interim note, which filed these as already correct. The paper is
explicit about breadth — "broad detection of diverse H5 and H7 genes in Eurasian and
American lineages" — and about specificity: "The H5 and H7 assays did not detect any of
the 275 HA genes of other subtypes". So each assay's true target is one HA subtype, which
is **strictly narrower than taxid 11320 and is not a taxonomic rank at all.** NCBI's
subtype nodes are `no rank` serotype children keyed on the H+N *pair*, and most records
never get one.

The entries' `target.query` already ORs seven H5Nx (resp. H7Nx) serotype taxids, which is
the right instinct and provably leaky: **183 GenBank records with "H5" in the title sit
under 11320 and outside all seven queried H5 taxids.** Both entries already carry
`retrieval_scope_incomplete`. The fix is a subtype-aware record filter layered on 11320 —
the source feature's `/serotype=` qualifier first, then a strain-name regex, then
sequence assignment of the HA segment for records with no subtype metadata anywhere.
Make the workaround robust; do not touch the taxid.

### Adenovirus polymerase — Roy 2009, two entries: over-broad in direction, small in size

"Primate-specific" is the seed list's wording, not the paper's. Roy's only statement about
this assay is the one Methods sentence giving the outer and inner primers (both match the
registry base for base), and it makes no taxonomic claim; the demonstrated range has to be
read off the study design, which is great-ape, macaque and human stool, with recovered
genomes "clustered into species corresponding to human adenovirus species B, C, and E".
No cross-reactivity panel was run. Genus Mastadenovirus is broader than that.

**But I measured the excess in the screened set rather than in GenBank, and it is small:
98 records of 30,167 (0.3%) sit at named non-primate mastadenovirus taxids** — 83 porcine,
11 guinea pig, 3 mouse, 1 cervine, and **no canine at all**, because the entry's
`target.query` filters them out. My 98 is a floor, since I could only enumerate the
non-primate species I could name and the genus has been renamed wholesale to binomials.
So the direction is real and the magnitude is closer to the CMV case than to Borna.

No single taxid fixes it — the human and simian species are siblings of the bovine,
canine and equine ones directly under the genus — so it would need `scope_taxids`. That
list was deliberately not built here: mapping each new binomial (`Mastadenovirus adami`,
`blackbeardi`, `chlorocebi`, …) to a host clade needs a careful pass, and a half-verified
list is worse than none. Note the existing 2026-10-20 note closed this question on the
wrong test: it asked only whether HAdV-F was in range, never whether non-primate hosts
were in the screened set.

### Two stale entry ids, both leftovers of withdrawn attributions

Not scope, but found on the way and cheap to fix:

- `RETROVIRUS_RNA_polymerase_SIV_Characterization_2001` — the citation is Clewley **1998**
  (`design_year: 1998`, DOI `10.1128/JVI.72.12.10305-10309.1998`). The "2001" is a
  leftover from the withdrawn Courgnaud 2001 attribution. The id is wrong; the citation is
  right.
- `ADENOVIRUS_dsDNA_Polymerase_Primate_speci_Casas_2005` — the paper is Roy 2009
  (`10.1371/journal.ppat.1000503`). `citation.doi` and `citation.reference` were already
  repaired, but the entry **id**, `source.nested_family` on both entries, and
  `citation.as_written` ("Casas, I (2005). Journal of Clinical Microbiology. 43:
  6176-6182") still say Casas.

### Already correct, no change

`PROBOSCIVIRUS_POL_Latimer_2010` EEHV3/4, EEHV5, EEHV6 and the two panEEHV entries; both
LMBV entries; `MYCOPLASMA_16S_Turtles_only` as a retrieval root;
`BATRAVIRUS_..._pan_FW4_RV4`. Each narrows through `target.query` already, or is genuinely
genus-wide. The EEHV entries only looked wrong because
`target.taxon_name: "Elephant endotheliotropic herpesvirus 5"` sits next to
`target.taxid: 548689` (the genus) — internally inconsistent labelling, harmless.

### Unscreenable

`Tortoise_intranuclear_coccidia_18SrDNA` has **no taxid at all**, so it has never been
screened and cannot be. One of only three entries with zero records.
