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

### A mechanic that constrains every fix: taxid is ANDed with query

`retrieve.build_query` (`retrieve.py:175`) emits
`txid<N>[Organism:exp] AND <length> AND (<query_suffix>) AND (<target.query>)`. So
**narrowing `target.taxid` below any taxid named in an existing `target.query` union
silently empties that part of the union.** Several entries' queries name
`unclassified …` taxids that sit outside the species node one would otherwise pick, which
is a second reason to prefer `scope_taxids` — a post-retrieval denominator filter — over a
taxid edit.

### Caliciviridae — Reid 1999, two entries: the worst case in the registry

Current scope is family Caliciviridae, **85,628 records, overwhelmingly norovirus.**
Genuinely in scope: **129.** A 664-fold over-breadth, both counts verified live.

The paper is titled "…detection of marine caliciviruses" and says it directly: "No RT-PCR
products or contaminating bands were observed when any of the serotypes of FMDV, SVDV, VSV
or FCV were tested by either 1F/1R or Hel1/Hel2 primer sets. The RT-PCR method with these
primers would appear to be specific for members of the marine calicivirus group."
Validated positives are VESV serotypes, SMSV-1–7, 9–11, 13, bovine Tillamook, cetacean,
primate (Pan-1) and reptile caliciviruses; validated negatives are SMSV-8, SMSV-12, mink
calicivirus and feline calicivirus.

Proposal for both: taxid **3433198 `Vesivirus exanthema`** (species, 129 records, verified).
NCBI's current taxonomy maps the paper's group almost exactly — it holds VESV, SMSV and
the bovine, cetacean, primate, reptile, skunk and walrus caliciviruses, and it **excludes**
`Vesivirus felis` (FCV, 2,249 records — the paper's negative), mink calicivirus, and
SMSV-8 and -12, all three of which NCBI has moved to `unclassified Vesivirus`, mirroring
the paper's own inference that those "may belong to a different group". Genus `Vesivirus`
would be the wrong intermediate, since 2,249 of its 2,474 records are the FCV shown
negative.

**This explains an existing artefact**: the Helicase entry's "0 of 30 detected" and the
Capsid entry's low coverage are a denominator that is almost entirely norovirus.

Two side findings. The two entries' `reference` strings disagree about page range under one
DOI — 82:63-73 on Helicase against 82:99-107 on Capsid. And Hel1/Hel2 are footnoted in
Reid's Table 2 as "Originally described by Neill and Seal (1995)", which independently
supports the standing re-cite question; the scope conclusion survives either way, since
that paper names the same organisms. The `needs_review` flag saying Hel1 "reads 22 nt by
OCR" is now stale — the table prints both at 25 nt. Printed product is 357 bp against the
registry's measured 360, so `amplicon_disagrees_with_paper` applies.

### Perkinsea — Smilansky 2021, two entries

Designed for NAG01, an amphibian-infecting clade, with the two probes separating clades
A–C from clade D: "there was no detection of pPPC with the NAG01a-c probe, and no
detection of pNAG01a-c with the PPC probe." **No NAG01, PPC or clade-level taxid exists** —
the whole `txid27997[Subtree]` is 133 taxa and none of them names NAG01; the rest is
*Perkinsus* (oyster parasites), Xcellidae (fish X-cell parasites) and relatives.

The smallest node holding the targets is **373149 `uncultured Perkinsea`** (species, 537
records), where both the NAG01a-c clone library (KP122572) and the PPC libraries are
filed. Against today's 1,931 records that removes ~72% of the denominator, which is
*Perkinsus*/Xcellidae 18S the assay was never built to detect. It is an improvement, not a
clean fit: 373149 is an environmental-samples bucket and will hold non-NAG01 clones.

The clade-D entry has a harder problem: its own design reference EF675616 is filed as
taxid 453764 `Rana sphenocephala pathogen MJY-2007`, whose lineage is `unclassified
Alveolata` — **not under Perkinsea at all**, so neither the current scope nor 373149
retrieves it. Disclose that rather than chase it; its only common ancestor with 373149 is
Alveolata.

### Tortoise intranuclear coccidian — a taxid does exist, and it makes the entry screenable

This entry has **no taxid**, so it has never been screened. The paper itself gives nothing
to resolve against — "Although a genus has not been assigned to this organism" — but the
earlier TINC work it cites does: NCBI holds **293274 `Intranuclear coccidium JW-2004`**
(species, verified, 2 records: AY728896.2 and KY683841.1). "JW-2004" is the senior author
of this very paper.

Identity was confirmed by sequence rather than by name: all three oligos are exact on
AY728896.2 — forward at position 607, probe at 634, reverse as reverse-complement at 672 —
giving a **measured amplicon of 84 bp**, which also fills this entry's null `amplicon_bp`
on real sequence as the registry's rules require.

Note the lineage is `unclassified Coccidia`, **not** Eimeriorina, so the entry's current
`taxon_name` ("unclassified Eimeriorina") is wrong too. A 2-record denominator is as thin
as it gets and will report thin evidence rather than drift; the value is that the entry
becomes screenable at all.

### LMBV — two entries, same answer, different mechanism

Grizzle 2003 is explicitly sub-species: the primer region "was selected to match a portion
of the LMBV genome that was distinct from the sequence of doctorfish virus and guppy
virus", and the pair "did not amplify DNA from 4 other ranaviruses or from red seabream
iridovirus". Genus Ranavirus is too broad as a declared scope. Proposal: **3432136
`Ranavirus micropterus1`** (species, 113 records) rather than the tighter 176656
`Largemouth bass virus`, because the paper's own Table 1 reports positives from smallmouth
bass, spotted bass, bluegill, crappie and chain pickerel, so the validated set is wider
than the LMBV node. Check 3045951 (*M. salmoides* ranavirus, in `unclassified Ranavirus`)
before applying — it is in the entry's query union but outside 3432136.

Li 2025 validated against no other ranavirus at all (only bacteria and unrelated fish
viruses), so the genus is likewise unsupported. Here the recommendation is **`scope_taxids:
[3432136]` with `target.taxid` left at the genus**, because this entry's query deliberately
names six `unclassified Ranavirus` taxids that the curator recorded as empirically detected
— exactly the cross-reactivity the registry wants visible — and the AND mechanic above
would delete them.

### Apicoplast 23S — Zhu 2000: NO CHANGE

Genuinely phylum-wide by design, and in fact broader: Table 1's specificity column for
this PCR reads Api = yes, **Chl = yes**, and it was validated on *Eimeria bovis*,
*Toxoplasma gondii*, *Allium stellatum* and *Spinacia oleracea* — it amplifies plant
chloroplasts too. Keeping the scope at the phylum is right for a pathogen registry.
*Cryptosporidium* has no apicoplast and can never amplify, but the entry's title query
returns 0 *Cryptosporidium* records of 329, so it costs nothing. The "2005" in the entry id
is a cosmetic leftover — the citation block already correctly says Zhu 2000.

### Paramyxoviridae — Tong 2008: NO CHANGE to the taxid, but its scope list breaks convention

The name/taxid discrepancy is nomenclatural drift, not a scope error: NCBI moved
Pneumovirinae out to its own family Pneumoviridae (11244), so modern Paramyxoviridae
(11158) already excludes the one group Tong deliberately carved out with separate primers.
The 2018 subfamily `Orthoparamyxovirinae` would be too narrow — it drops Rubulavirinae and
Avulavirinae, and mumps and NDV are among Tong's validated targets.

The real defect is this entry's **`scope_taxids`: roughly 900 enumerated species and strain
ids**, against the schema's own instruction at `schema.py:258` to "name the smallest set of
taxa whose subtrees cover the design paper's stated range — a genus or a subfamily, not an
enumerated species list". `[2560076, 2560080, 2560069]` says the same thing in three ids
and does not go stale with every new deposit. Its provenance could not be traced in
`docs/`, so check whether it was built empirically from a screen before replacing it.

## What to do, in order

Nothing below was applied. Ranked by evidence strength times size of the error.

1. **Caliciviridae, two entries** — `scope_taxids: [3433198]`. 85,628 records against 129
   genuinely in scope, and it explains an existing "0 of 30" artefact. Biggest error,
   cleanest taxonomic fit.
2. **Bornaviridae, three entries** — `scope_taxids: [1714619, 12455]`. 66% of the
   denominator is the wrong virus, and this is the case that started the audit. 12455 is
   mandatory or 49 genuine BoDV-1 deposits vanish.
3. **Tortoise intranuclear coccidian** — `taxid: 293274`, `taxon_name: Intranuclear
   coccidium JW-2004`, and `amplicon_bp: 84` measured on AY728896.2. Turns an entry that
   has never been screenable into one that can be screened.
4. **Helicobacter Conley 2021** — `taxid: 290433`. The assay cannot currently reach the
   reference sequence its own authors deposited. A workaround, and disclose it as one.
5. **Orthobornavirus Sigrist, three entries** — `[1548713]`, `[1548720, 1548721]`,
   `[1548722]`. Expect the passerine entry to stop reporting 3.8% and start reporting
   "cannot assess", which is the honest answer.
6. **The four PREDICT sibling groups** — copy each sibling's existing list so the two
   rounds of one protocol are comparable. No paper needed.
7. **Perkinsea, two entries** — `[373149]`, plus a note that clade D's own reference is
   unreachable.
8. **LMBV** — `3432136`: as a taxid for Grizzle, as `scope_taxids` for Li 2025.
9. **Tong 2008** — replace ~900 enumerated ids with `[2560076, 2560080, 2560069]`, after
   tracing where the long list came from.
10. **Leptospira lipL32** — the 16-species pathogenic list, if you want it; no clade node
    exists, and two species have been renamed since the paper.

Not scope, found on the way, cheap: two stale entry ids (`Characterization_2001` is
Clewley 1998; `Casas_2005` is Roy 2009), the misspelled `Flagillar filiment` gene string,
a stale OCR flag on Reid's Hel1, and the `target_annotation_uncertain` flag on Feldman,
which can be closed because the paper's own coordinates put the product inside 16S and
state 993 bp against the registry's measured 994.

Deliberately NOT proposed: anything for `RETROVIRUS_RNA_polymerase_SIV_Keele_2009`, whose
primers are not in the cited paper and were not found anywhere, so the citation has to be
settled first; and a `scope_taxids` list for the Roy 2009 adenovirus entries, where the
direction is right but the excess measured only 98 records of 30,167 and building the
host-clade mapping properly is its own task.
