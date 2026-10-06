# Candidate DOIs for unresolved citations (eight, found through PubMed)

2026-10-05, from a cloud session. Found via PubMed (the MCP route), which was
reachable where Crossref was not.

`DOI_MISSING` is the registry's commonest `needs_review` flag - 45 of 164
entries - and 106 oligos cannot be checked against a paper because no DOI says
which paper. Most of those 45 are genuinely unpublished: WCS in-house assays,
"Tracies unpublished", "developed in house", bare "PREDICT protocol". No DOI
exists and none should be invented.

Eleven entries were different: they carry a named reference that an earlier pass
marked "not resolved" or "DOI not confirmed". Five of those were resolved with high
confidence on 2026-10-05. The other six were first written up as unresolvable; a
second search on 2026-10-06 found a candidate for each of the two groups (see the
end of this file): one with high confidence on the bibliography, one plausible.

## NOT WRITTEN TO `registry/`, deliberately

`scripts/check_citations.py` verifies every citation against Crossref, and it
exists because a reference was once written from memory and was wrong. Crossref
was denied by this environment's egress policy, so a DOI added here could not
have been checked by the gate that is supposed to check it. Making it pass would
have meant writing PubMed-derived rows into `docs/papers-index.cache.json`,
whose whole value is that its contents came from Crossref. Mislabelling the
provenance inside the file the gate trusts is a worse outcome than a short
worklist.

PubMed is an authoritative index, not a memory, so these are good candidates.
They are candidates all the same until Crossref agrees.

**To finish this, on the machine with network access:** add the DOI and set
`doi_verified: false` on each entry below, then run

    python scripts/resolve_citations.py --registry registry --email nightb02@nyu.edu
    python scripts/check_citations.py --refresh

`resolve_citations.py` marks a DOI verified only when Crossref's year matches
`design_year` and Crossref's first author appears in the reference string, and
reports anything that resolves to a different paper. If it rejects one of these,
the rejection is the answer and the DOI should come back out.

## Resolved

### 1. `Pan_Flavivirus_NS5_gene`
**`10.1089/vbz.2007.0206`** — PMID 18020965

Moureau G, Temmam S, Gonzalez JP, Charrel RN, Grard G, de Lamballerie X. 2007.
"A real-time RT-PCR method for the universal detection and identification of
flaviviruses." *Vector Borne Zoonotic Dis* 7(4):467-77.

Strongest of the five. The entry's stored reference already names this title and
journal verbatim; only the DOI was missing. The abstract independently confirms
the target - "a 269-272 nt region at the N terminal end of the NS5 gene" -
against an entry named for the NS5 gene.

### 2. `RETROVIRUS_RNA_polymerase_SIV_2`
**`10.1128/JVI.72.12.10305-10309.1998`** — PMID 9811781, PMC110619

Clewley JP, Lewis JC, Brown DW, Gadsby EL. 1998. "A novel simian
immunodeficiency virus (SIVdrl) pol sequence from the drill monkey, *Mandrillus
leucophaeus*." *J Virol* 72(12):10305-9.

All four authors and the full title match the stored reference string exactly,
and `pol` matches the entry's gene. `design_year` is already 1998.

### 3. `E_coli_ETEC_enterotoxin_LT_gen_unnamed_Victor_1991`
**`10.1128/jcm.29.1.158-161.1991`** — PMID 1993750, PMC269721

Victor T, du Toit R, van Zyl J, Bester AJ, van Helden PD. 1991. "Improved method
for the routine identification of toxigenic *Escherichia coli* by DNA
amplification of a conserved region of the heat-labile toxin A subunit."
*J Clin Microbiol* 29(1):158-61.

Matches on first author, year, and subject. The abstract confirms the design -
"two oligonucleotide primers ... to amplify a highly conserved region of the A
subunit of the heat-labile enterotoxin gene" - against an entry named for the
ETEC LT gene with two stored primers.

### 4. `Encephalitozoon_Polar_tube_protein_E_cun_Xiao_2001`
**`10.1128/JCM.39.6.2248-2253.2001`** — PMID 11376065, PMC88119

Xiao L, Li L, Visvesvara GS, Moura H, Didier ES, Lal AA. 2001. "Genotyping
*Encephalitozoon cuniculi* by multilocus analyses of genes with repetitive
sequences." *J Clin Microbiol* 39(6):2248-53.

First author, year and journal all match the stored reference. The abstract
confirms both the locus and that primers were published here: the polar tube
protein (PTP) gene, and "two simple PCR tests were developed to differentiate
*E. cuniculi* in clinical samples".

(An earlier version of this note said this is also the Xiao paper behind the
misnamed `Ziao18SF1` oligo. It is not. `Ziao18SF1` is stored under
`CRYPTOSPORIDIA_Need_to_order_18SrDNA_Identification_2000`, which cites Xiao L,
Alderisio K, Limor J, Royer M, Lal AA. 2000. *Appl Environ Microbiol*
66(12):5492-8, `10.1128/AEM.66.12.5492-5498.2000`, a *Cryptosporidium* SSU rRNA
paper. Same first author, different paper, journal, year, organism and locus.
Corrected 2026-10-06 against PubMed records for both papers.)

### 5. `Encephalitozoon_18S_General_Encephalitoz_Muller_1999`
**`10.1128/CDLI.6.2.243-246.1999`** — PMID 10066661, PMC95694

Müller A, Stellermann K, Hartmann P, Schrappe M, Fätkenheuer G, Salzberger B,
Diehl V, Franzen C. 1999. "A powerful DNA extraction method and PCR for
detection of microsporidia in clinical stool specimens." *Clin Diagn Lab
Immunol* 6(2):243-6.

Matches the stored "Muller, A et al. CLINICAL AND DIAGNOSTIC LABORATORY
IMMUNOLOGY 1999" on author, journal and year. The abstract settles it by naming
the primer: "PCR was performed with primer pairs **V1-PMP2**, V1-EB450 and
V1-SI500", and this entry stores PMP primers.

**The provenance question stays open.** The entry's own note already records
that PMP1/PMP2 are usually credited to an earlier paper, and nothing here
changes that - this resolves which paper the registry *cites*, not who designed
the oligos. `oligos_designed_here` should stay `false` pending that check, and
this looks like a fourth composite of the Hellgren/Bensch kind.

## Found on a second search, 2026-10-06: candidates, not resolutions

Both of these were written up above as "not resolved", and both resolve to a
candidate with the right search. Neither is written to `registry/`, for the reason
at the top: a DOI enters only through the Crossref gate.

### `Canine_distemper_virus_specifi_H_gene_2011` and its 3 siblings
**`10.7589/0090-3558-47.3.725`** — PMID 21719841 (not in PMC)

Müller A, Silva E, Santos N, Thompson G. 2011. "Domestic dog origin of canine
distemper virus in free-ranging wolves in Portugal as revealed by hemagglutinin
gene characterization." *J Wildl Dis* 47(3):725-9.

The stored reference already says "candidate Müller A et al. 2011 J Wildl Dis
47:725", and this note quoted it without the volume and page, which are what
settle it. Looked up by journal, year, volume, first page and author, PubMed
returns exactly this one record; the author, year, journal, volume, page and gene
(H) all agree. That makes the bibliographic match high-confidence and the
*primer* match untested: the paper is not in PubMed Central, so the stored
1F/1R primers (567 bp) have not been compared with its text. One soft mismatch:
the registry note says "incl. Arctic-lineage variants", which the abstract does
not mention.

### `E_coli_O157_H7_hlyA_gene_unnamed_Wang_1997` and `Yersinia_pseudotuberculosis_in_unnamed_Wang_1997`
**`10.1046/j.1365-2672.1997.00300.x`** — PMID 9449811

Wang RF, Cao WW, Cerniglia CE. 1997. "A universal protocol for PCR detection of
13 species of foodborne pathogens in foods." *J Appl Microbiol* 83(6):727-36.

Plausible, not verified. The abstract uses "13 sets of specific primers" and lists
both *E. coli* O157:H7 and *Y. pseudotuberculosis* among its 13 species, which fits
one reference string covering two organisms. The earlier search failed because
`hlyA` and `inv` are not in the abstract. A search of Wang RF with Cerniglia CE
over 1996-1998 turns up no competing foodborne multiplex paper. The primer
sequences (O157-3, O157-4 and the *Yersinia* pair) need to be read from the paper
before this is believed.

## Found 2026-10-06: the source of the CMV gB 4007/4125 primers

**`10.1186/1743-422X-6-210`**, as returned by PubMed — PMID 19941648, PMC2789067

Deckers M, Hofmann J, Kreuzer KA, Reinhard H, Edubio A, Hengel H, Voigt S, Ehlers
B. 2009. "High genotypic diversity and a novel variant of human cytomegalovirus
revealed by combined UL33/UL55 genotyping with broad-range PCR." *Virol J* 6:210.

Its Table 1 prints primer set CMV-gBp1 as a nested pair: round 1 `4007s`/`4007as`
(800 bp) and round 2 `4125s`/`4125as` (550 bp). Three of the four stored
sequences match exactly reading `(n/i)` as N; `4125s` differs at one position
(the paper prints B-or-inosine, the registry stores N). Detail, and what remains
to do, is in the `notes_curator` of
`CMV_specific_HERPES_UL55_Glycoprotein_B_gB` and `..._round2_2`. Caveat from the
paper itself: it cites an earlier reference for the first use of CMV-gBp1 in great
apes, so this may not be where the primers were first published.
