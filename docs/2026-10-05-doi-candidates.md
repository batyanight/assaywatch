# Candidate DOIs for five unresolved citations

2026-10-05, from a cloud session. Found via PubMed (the MCP route), which was
reachable where Crossref was not.

`DOI_MISSING` is the registry's commonest `needs_review` flag - 45 of 164
entries - and 106 oligos cannot be checked against a paper because no DOI says
which paper. Most of those 45 are genuinely unpublished: WCS in-house assays,
"Tracies unpublished", "developed in house", bare "PREDICT protocol". No DOI
exists and none should be invented.

Eleven entries were different: they carry a named reference that an earlier pass
marked "not resolved" or "DOI not confirmed". Five of those are now resolved
with high confidence. Two are not, and are left alone.

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

    python scripts/resolve_citations.py --registry registry --email you@example.org
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
*E. cuniculi* in clinical samples". This is also the Xiao paper behind the
misnamed `Ziao18SF1` oligo noted in the verifier's docstring.

### 5. `Encephalitozoon_18S_General_Encephalitoz_Muller_19`
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

## Not resolved, and left alone

### `Canine_distemper_virus_specifi_H_gene_2011` and its 3 siblings
Stored as "muller,2011", with an earlier note offering "candidate Müller A et
al. 2011 J Wildl Dis". A journal-and-date search of *J Wildl Dis* 2010-2012 for
canine distemper returns 13 papers. Picking among them on title plausibility is
exactly the move that produced the fabricated Nobach reference, so nothing was
picked. Settle it from the primer sequences - the stored H-gene walking primers
should appear in whichever paper it is - or from the lab's own records.

### `E_coli_O157_H7_hlyA_gene_unnamed_Wang_1997` and `Yersinia_pseudotuberculosis_in_unnamed_Wang_1997`
Stored as "Wang et al 1997 (O157 hlyA / Y. pseudotuberculosis inv)". A
title/abstract search for `hlyA` with *E. coli* O157 across 1996-1998 returns
three papers, none by Wang and none a PCR primer paper: Makino 1998 (plasmid
sequence), Schmidt 1996 (hly operon map), Bauer 1996 (RTX toxin). One reference
string covering two different organisms suggests a multiplex paper, but the
combination did not resolve. Needs the full citation from the lab spreadsheet.

## Update, later on 2026-10-05 (local machine, Crossref reachable)

All five resolved DOIs above passed `resolve_citations.py` and are now in
`registry/` with `doi_verified: true`.

**Wang 1997 is resolved too, from the primer sequences, the route suggested
above for Müller 2011.** A Europe PMC full-text search on O157-3/O157-4 finds
them under the same names in Shija & Nonga 2026 (Vet Med Sci), Table 1, cited
to Wang RF, Cao WW, Cerniglia CE 1997, "A universal protocol for PCR detection
of 13 species of foodborne pathogens in foods", J Appl Microbiol 83:727-736,
`10.1046/j.1365-2672.1997.00300.x`. Its abstract names both *E. coli* O157:H7
and *Y. pseudotuberculosis*, which is why one reference string covered both
entries. The O157 entry is confirmed by sequence through the citing table; the
*Y. pseudotuberculosis* entry only by reference, species list and naming scheme,
and says so. Both amplify in `check_submission.py`.

**Müller 2011 CDV is still unresolved.** None of the walking primers 1F, 1R,
2F or 2R appears in any Europe PMC full text, on either strand, so the
sequence route needs the paper or the lab's own records.

Same search, same session: the CMV gB 4007/4125 pairs, cited to Prepens 2007
but absent from it, were all four found in Deckers et al. 2009 Virol J 6:210
and re-cited. The query, for next time:
`https://www.ebi.ac.uk/europepmc/webservices/rest/search?query="<SEQ>"&format=json`.

---

## Closed out, 2026-10-17 (Crossref reachable, contact email available)

All five "Resolved" candidates above are **applied and Crossref-verified** in the registry, as
are the two Wang 1997 entries from the later update. Checked entry by entry:

| entry | DOI | `doi_verified` |
|---|---|---|
| `Pan_Flavivirus_NS5_gene` | `10.1089/vbz.2007.0206` | true |
| `RETROVIRUS_RNA_polymerase_SIV_2` | `10.1128/JVI.72.12.10305-10309.1998` | true |
| `E_coli_ETEC_enterotoxin_LT_gen_unnamed_Victor_1991` | `10.1128/jcm.29.1.158-161.1991` | true |
| `Encephalitozoon_Polar_tube_protein_E_cun_Xiao_2001` | `10.1128/JCM.39.6.2248-2253.2001` | true |
| `Encephalitozoon_18S_General_Encephalitoz_Muller_1999` | `10.1128/CDLI.6.2.243-246.1999` | true |
| `E_coli_O157_H7_hlyA_gene_unnamed_Wang_1997` + Yersinia sibling | `10.1046/j.1365-2672.1997.00300.x` | true |

`scripts/check_citations.py` reports 182 citations checked, 0 problems.

Two citations were finished on 2026-10-17 using the same route:

- **`NOSEMA_bombi_SSU_Kato_2020` re-cited to Klee 2006**, `10.1016/j.jip.2005.10.012`, verified by
  `resolve_citations.py`.
- **Both CMV gB 4007/4125 entries re-cited to Deckers 2009**, `10.1186/1743-422X-6-210`, verified
  the same way. Their `RECITE_AFTER_CROSSREF_CHECK` flag is cleared. `oligos_designed_here` is null
  on all three, not true: each cited paper is where the oligos are *printed*, and in both cases it
  points at an earlier use it does not identify.

### The Müller 2011 CDV quartet: the sequence route is now exhausted

Still unresolved, and no longer for want of trying. All eight walking primers of
`Canine_distemper_virus_specifi_H_gene_2011` and its three siblings were searched in **NCBI PMC
full text**, on both strands — a different index from the Europe PMC search recorded above, and
one that matches strings inside tables the retrievable flattened text drops (proved on the
Chlamydia primer the same day).

Fifteen of the sixteen searches return nothing. The one hit, `TCCATAATCTGGGATGTTTGAA` in
PMC4683949 (*Virol J* 2015, `10.1186/s12985-015-0445-7`), is **not** the source: that paper states
its primer sets were designed de novo with Primer 3 as ~50 bp overlapping sets giving ~1000 bp
products, cites no Müller and never uses the word "walking", and the registry entry's product is
563 bp. Two independent designs landing on one conserved 22-mer site is unremarkable.

So both full-text indexes agree the primers are not in the open literature. This needs the paper
itself or the lab's own records; no further search route is worth spending on.
