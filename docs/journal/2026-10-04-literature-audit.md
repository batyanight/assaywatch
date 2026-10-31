# Literature audit, 2026-10-04 — assays the registry is missing

A sweep of the wildlife-disease, zoological-medicine, virology and
molecular-methods literature for published PCR/qPCR assays that the registry
does not have, scoped deliberately wider than `scripts/scan_literature.py`,
which can only search taxa already present.

**Proposals only.** Nothing here has been written to `registry/`, and no
sequence below was transcribed. The route in is `scripts/check_submission.py`,
as CONTRIBUTING.md sets out. Each row of
`results/literature-audit-2026-10-04.tsv` is a reading assignment.

## Method, and what it cost

The registry's 150 entries were first inventoried by taxon, gene and DOI. Those
150 entries resolve to roughly 60 distinct targets, and the inventory showed the
shape of the problem: the collection is overwhelmingly **pan-family viral
consensus PCR** — pan-herpes, pan-pox, pan-flavivirus, pan-paramyxovirus,
pan-adenovirus — with very little at species or lineage level, and almost
nothing outside viruses and a handful of bacteria and apicomplexans.

Searching was done with NCBI E-utilities (`esearch`/`esummary`, db=pubmed) over
84 topic queries built from the wildlife/zoo pathogen priority list, then
Europe PMC for open-access full text. **Of 84 searches, exactly one returned
zero hits** (sea star wasting disease, below). The 84 queries returned 1,601
records, 1,443 of them distinct; candidate selection then worked down a
relevance-ordered digest of those.

Every DOI in the TSV was then checked against Crossref and the returned title
and first author compared to what the candidate claimed. **99 of 99 candidates
resolved, and all 99 matched** — no candidate had to be dropped for a DOI
pointing at the wrong paper, which given this project's history with five
misresolving DOIs is worth recording as a negative result. The titles and first
authors in the TSV are the Crossref strings, not mine.

Primer readability was established by fetching the open-access full text
(Europe PMC `fullTextXML`, falling back to NCBI `efetch` on `db=pmc`) and
scanning for runs of 17–45 IUPAC characters. **14 candidates have sequences
actually readable now; 85 do not** and are marked accordingly.

## The 15 largest gaps, ranked

| # | gap | best candidate | status |
|---|---|---|---|
| 1 | *Batrachochytrium dendrobatidis* lineages | Ghosh 2021, `10.1111/1755-0998.13299` | Bd present, lineage-blind |
| 2 | Influenza A HA (H5/H7) | Tsukamoto 2010, `10.1128/JCM.01264-10` | matrix gene only |
| 3 | Avian haemosporidian genus bias | Pacheco 2018, `10.1016/j.ijpara.2018.02.003` | Hellgren 2004 only |
| 4 | White-nose syndrome (*P. destructans*) | Muller 2013, `10.3852/12-242` | absent entirely |
| 5 | Crayfish plague (*A. astaci*) | Vrålstad 2009, `10.1016/j.vetmic.2008.12.022` | absent entirely |
| 6 | *Ophidiomyces* second assay + genotyping | Allender 2015 `10.1177/1040638715573983`; Haynes 2023 `10.1371/journal.pone.0289159` | Bohuski 2015 only |
| 7 | West Nile lineage 2 | Vázquez 2016, `10.1016/j.jviromet.2016.07.026` | Lanciotti 2001 envelope only |
| 8 | EEHV subtypes | Pursell 2016, `10.1016/j.jviromet.2016.08.010` | pan-herpes only |
| 9 | Avian bornaviruses | Sigrist 2021, `10.3390/v13071358` | Zimmermann 1994 only |
| 10 | Cetacean + phocine morbillivirus | Groch 2020 `10.1016/j.jviromet.2020.113964`; Geiselhardt 2022 `10.1128/jcm.02505-21` | pan-morbillivirus P only |
| 11 | Sea turtle fibropapillomatosis (ChHV5) | Kelley 2026, `10.3354/dao03932` | absent entirely |
| 12 | Devil facial tumour disease | Kwon 2018, `10.1098/rsos.180870` | absent entirely |
| 13 | Bee pathogens (DWV, *Vairimorpha*) | Rossi 2024, `10.3390/microorganisms12061105` | absent entirely |
| 14 | Amphibian *Perkinsea* | Karwacki 2018, `10.3354/dao03239` | absent entirely |
| 15 | Chelonian herpes + *Mycoplasma* | Braun 2014, `10.7589/2013-09-231` | pan-herpes / pan-mycoplasma |

## The five that matter most

**1. Bd lineage discrimination (Ghosh 2021).** This is the one candidate that
speaks directly to §3.1 of the pipeline review. The review's central finding is
that the tool catches 1 of 12 documented assay failures because every failure in
the case set is lineage- or group-conditional, and a minority clade cannot move
a population proportion past a 90% bar — "Asian Bd haplotypes" is named
explicitly in that list. Ghosh et al. publish a qPCR scheme that *discriminates*
Bd lineages rather than detecting the species, which makes it both a registry
addition and the natural reference for the per-footprint haplotype coverage the
review proposes building. It also gives the validation set something it can
actually answer: did the tool name the lineage the paper named? Caveat: the
paper is open access but its oligo table is not in the machine-readable text, so
the PDF is still needed before anything is transcribed.

**2. Influenza A hemagglutinin (Tsukamoto 2010; An 2024).** The registry's only
influenza entries target the matrix gene, and one of them is annotated in its
own id as `DID_NOT_WORK` with positives. Meanwhile the validation set already
carries a swine-H1N1-versus-avian failure case against the matrix assay, and the
current H5N1 clade 2.3.4.4b panzootic is a subtype problem that a matrix assay
is constitutionally unable to see. Tsukamoto's assay was designed for broad H5
and H7 coverage using mixed-base primers — which also makes it an interesting
degeneracy case for §3.7 — and An 2024 adds a recent H5/H7/H9 multiplex. Adding
HA is the single biggest functional capability the registry is missing for its
most-surveilled pathogen.

**3. Avian haemosporidian differential amplification (Pacheco 2018).** The
registry rests its entire avian-malaria coverage on Hellgren 2004 cytochrome b,
across four separate entries. Pacheco et al. demonstrate that the standard
primers amplify *Plasmodium*, *Haemoproteus* and *Leucocytozoon* with
systematically different efficiency, and propose replacements. That is a
published, dated, genus-conditional failure of an assay the registry already
holds — so this paper belongs in `docs/validation-cases.tsv` regardless of
whether its primers are ever added. It is open access with 19 readable oligos,
so it is submittable immediately. It also pairs with the review's note that
fusiform-gametocyte *Leucocytozoon* is already a known failure case.

**4. White-nose syndrome and crayfish plague — two complete absences.**
*Pseudogymnoascus destructans* and *Aphanomyces astaci* are among the most
consequential wildlife pathogens in the Northern Hemisphere, both have
nationally coordinated surveillance programmes built on a small number of named
assays, and neither appears anywhere in the registry. For Pd the operative
assays are Muller 2013 (IGS TaqMan, the USGS standard) and Shuey 2014
(discriminating Pd from congeners). For *A. astaci* the reference method is
Vrålstad 2009 — notable also for being TaqMan MGB, a chemistry the registry has
only ten entries of — and Strand 2023, which was published explicitly to fix
specificity problems in Vrålstad's assay and is therefore a dated failure claim
as well as a candidate. Makkonen 2018 adds mtDNA haplotyping, again relevant to
the haplotype estimand.

**5. *Ophidiomyces*: a second assay and a genotyping assay.** Snake fungal
disease is already in the registry, but only through Bohuski 2015, both of whose
entries come from one paper. Allender 2015 is the other assay in routine
ophidiomycosis diagnostics, and having both in the registry would let each be
screened against the other's claimed coverage — the cheapest kind of
cross-validation available here. Haynes 2023 then adds qPCR genotyping of the
*O. ophidiicola* clades now known to differ in host range, is open access, and
has 28 readable oligos, making it the most immediately actionable row in the
whole table.

## Where the coverage is thin, honestly

- **Sea star wasting disease returned zero hits** on an assay-language query,
  and a follow-up search found only the Hewson 2014 densovirus association paper
  (`10.1073/pnas.1416625111`) and subsequent ecological work. The aetiology is
  still contested and there may be no validated published PCR assay to add. I
  did not propose one.
- **Coral disease** is represented here only by *Vibrio coralliilyticus*. Stony
  coral tissue loss disease has no agreed agent and therefore no target assay;
  black-band disease yielded only community-profiling primers, which are not
  diagnostic assays in this registry's sense.
- **Toxoplasma, Giardia, Borrelia/Anaplasma, Babesia/Theileria and
  Leptospira** returned hundreds of hits each, almost entirely prevalence
  surveys reusing other people's primers rather than assay-development papers.
  I took only the clearest method papers (lipL32 and rrs for *Leptospira*,
  *Neospora* and *Besnoitia* for the apicomplexans) and left these areas
  deliberately under-sampled; they would repay a dedicated pass with tighter
  "development of" title filtering.
- **Aspergillus** yielded almost nothing usable: two hits, neither a wildlife
  assay-development paper. Avian aspergillosis diagnosis is still largely
  serological and this may be a genuine absence rather than a search failure.
- **SARS-CoV-2 in wildlife, Lassa, monkeypox and *M. bovis*** are dominated by
  surveillance and serology papers. For these the registry's existing
  pan-family assays may genuinely be the state of the art for wildlife work,
  and the species-level candidates I kept are the few with real primer tables.
- **Mpox/orthopox and Brucella** candidates are older papers (1996–2009)
  because the recent literature is overwhelmingly serological or
  isothermal/CRISPR formats the pipeline does not model.
- I did not search non-English literature, preprint servers, or the grey
  literature where several national wildlife-health programmes publish their
  protocols — the Pd and *A. astaci* standard operating procedures in
  particular exist as agency documents as well as papers.

## Candidates whose PDFs are needed

**85 of 99 candidates cannot have their primers read right now** — 73 are
paywalled or absent from PMC, 11 are open access but print their oligo tables as
images or in supplementary files that the full-text XML does not carry, and 1
(`10.1371/journal.pone.0241584`) exposes only a single oligo. Per CONTRIBUTING.md
none of these should be transcribed from a secondary source, so each needs the
PDF or the publisher's HTML before it can become an entry.

The 14 that are readable now, and so could be drafted today:
`10.1098/rsos.180870`, `10.1371/journal.pone.0289159`,
`10.1016/j.ijpara.2018.02.003`, `10.3390/v15122313`,
`10.3390/microorganisms12061105`, `10.1038/s41598-020-57909-8`,
`10.3390/pathogens12010111`, `10.3390/v13040715`, `10.1098/rsos.202150`,
`10.3389/fmicb.2023.1302586`, `10.1371/journal.pone.0232044`,
`10.1016/j.vetmic.2010.05.042`, `10.1007/s00436-020-06887-x`,
`10.1371/journal.pone.0230701`.

The full list needing the PDF, in priority order:

- **P1** Aphanomyces astaci — Vrålstad, Trude, *Veterinary Microbiology* 2009. `10.1016/j.vetmic.2008.12.022` (paywalled)
- **P1** Aphanomyces astaci — Strand, David A., *Journal of Invertebrate Pathology* 2023. `10.1016/j.jip.2023.108008` (paywalled)
- **P1** Batrachochytrium dendrobatidis — Ghosh, Pria N., *Molecular Ecology Resources* 2021. `10.1111/1755-0998.13299` (OA but table not machine-readable)
- **P1** Canine/phocine distemper virus — Geiselhardt, Franziska, *Journal of Clinical Microbiology* 2022. `10.1128/jcm.02505-21` (paywalled)
- **P1** Cetacean morbillivirus — Groch, Kátia R., *Journal of Virological Methods* 2020. `10.1016/j.jviromet.2020.113964` (paywalled)
- **P1** Chelonid alphaherpesvirus 5 — Kelley, Jake Ryan, *Diseases of Aquatic Organisms* 2026. `10.3354/dao03932` (paywalled)
- **P1** Elephant endotheliotropic herpesvirus — Pursell, Taylor, *Journal of Virological Methods* 2016. `10.1016/j.jviromet.2016.08.010` (paywalled)
- **P1** Influenza A virus (H5/H7 HA) — Tsukamoto, Kenji, *Journal of Clinical Microbiology* 2010. `10.1128/JCM.01264-10` (paywalled)
- **P1** Ophidiomyces ophidiicola — Allender, Matthew C., *Journal of Veterinary Diagnostic Investigation* 2015. `10.1177/1040638715573983` (paywalled)
- **P1** Orthobornavirus (avian) — Sigrist, Brigitte, *Viruses* 2021. `10.3390/v13071358` (OA but table not machine-readable)
- **P1** Pseudogymnoascus destructans — Muller, Laura K., *Mycologia* 2013. `10.3852/12-242` (paywalled)
- **P1** Pseudogymnoascus destructans — Shuey, Megan M., *Applied and Environmental Microbiology* 2014. `10.1128/AEM.02897-13` (paywalled)
- **P1** West Nile virus — Linke, Sonja, *Journal of Virological Methods* 2007. `10.1016/j.jviromet.2007.05.021` (paywalled)
- **P1** West Nile virus — Vázquez, Ana, *Journal of Virological Methods* 2016. `10.1016/j.jviromet.2016.07.026` (paywalled)
- **P2** Amphibian Perkinsea — Karwacki, EE, *Diseases of Aquatic Organisms* 2018. `10.3354/dao03239` (paywalled)
- **P2** Aphanomyces astaci — Oidtmann, B, *Diseases of Aquatic Organisms* 2006. `10.3354/dao072053` (paywalled)
- **P2** Aphanomyces astaci — Makkonen, Jenny, *Parasitology* 2018. `10.1017/S0031182018000227` (paywalled)
- **P2** Avian orthoavulavirus 1 (pigeon PMV-1) — Barbezange, C, *Journal of Virological Methods* 2002. `10.1016/s0166-0934(02)00148-9` (paywalled)
- **P2** Avipoxvirus — Farias, Margaret E. M., *PLoS ONE* 2010. `10.1371/journal.pone.0010745` (OA but table not machine-readable)
- **P2** Avipoxvirus — Jarmin, Susan, *Journal of General Virology* 2006. `10.1099/vir.0.81738-0` (paywalled)
- **P2** Batrachovirus (amphibian herpesvirus) — Licheri, Matthias, *Journal of Veterinary Diagnostic Investigation* 2020. `10.1177/1040638720951134` (paywalled)
- **P2** Baylisascaris procyonis — Dangoudoubiyam, Sriveny, *Journal of Parasitology* 2009. `10.1645/GE-1905.1` (paywalled)
- **P2** Bd / Bsal / ranavirus — Standish, I, *Diseases of Aquatic Organisms* 2018. `10.3354/dao03230` (paywalled)
- **P2** Beak and feather disease virus — Černíková, Lenka, *Journal of Virological Methods* 2017. `10.1016/j.jviromet.2017.02.017` (paywalled)
- **P2** Brucella canis — Kauffman, L. K., *Zoonoses and Public Health* 2013. `10.1111/zph.12041` (paywalled)
- **P2** Brucella ceti — Wu, Q, *Diseases of Aquatic Organisms* 2016. `10.3354/dao03034` (paywalled)
- **P2** Cetacean morbillivirus — Grant, Rebecca J., *Journal of Virological Methods* 2009. `10.1016/j.jviromet.2008.11.008` (paywalled)
- **P2** Chelonid alphaherpesvirus 5 — Quackenbush, Sandra L., *Virology* 1998. `10.1006/viro.1998.9207` (paywalled)
- **P2** Chlamydia (avian) — Lee, O.-Mi, *Avian Pathology* 2022. `10.1080/03079457.2022.2031882` (paywalled)
- **P2** Chlamydia psittaci — Messmer, T O, *Journal of Clinical Microbiology* 1997. `10.1128/jcm.35.8.2043-2046.1997` (paywalled)
- **P2** Chlamydia psittaci — Ménard, Armelle, *Journal of Medical Microbiology* 2006. `10.1099/jmm.0.46335-0` (paywalled)
- **P2** Chordopoxvirinae — Li, Yu, *Journal of Clinical Microbiology* 2010. `10.1128/JCM.01697-09` (paywalled)
- **P2** Francisella tularensis — Long, G W, *Journal of Clinical Microbiology* 1993. `10.1128/jcm.31.1.152-154.1993` (paywalled)
- **P2** Hendra virus — Foord, Adam J., *Journal of Virological Methods* 2012. `10.1016/j.jviromet.2012.01.020` (paywalled)
- **P2** Influenza A virus (H5/H7/H9 HA) — An, Se-Hee, *Journal of Virological Methods* 2024. `10.1016/j.jviromet.2024.114942` (paywalled)
- **P2** Lagovirus (RHDV2/RHDVb) — Dalton, K. P., *Transboundary and Emerging Diseases* 2017. `10.1111/tbed.12607` (paywalled)
- **P2** Leptospira — Levett, Paul N, *Journal of Medical Microbiology* 2005. `10.1099/jmm.0.45860-0` (paywalled)
- **P2** Lyssavirus — Hayman, David T.S., *Journal of Virological Methods* 2011. `10.1016/j.jviromet.2011.07.002` (OA but table not machine-readable)
- **P2** Monkeypox virus — Kulesh, David A, *Laboratory Investigation* 2004. `10.1038/labinvest.3700143` (OA but table not machine-readable)
- **P2** Mycobacterium bovis — Hermes, Robert, *PLOS ONE* 2018. `10.1371/journal.pone.0207365` (OA but table not machine-readable)
- **P2** Mycobacterium microti — Boniotti, M. Beatrice, *Journal of Clinical Microbiology* 2014. `10.1128/JCM.00440-14` (paywalled)
- **P2** Mycoplasma gallisepticum — Grodio, Jessica L., *Avian Pathology* 2008. `10.1080/03079450802216629` (paywalled)
- **P2** Myxoma virus — Kwit, Ewa, *Journal of Virological Methods* 2019. `10.1016/j.jviromet.2019.113709` (paywalled)
- **P2** Neospora caninum — Bartley, P.M., *Veterinary Parasitology* 2013. `10.1016/j.vetpar.2012.10.001` (paywalled)
- **P2** Nipah henipavirus — Guillaume, Vanessa, *Journal of Virological Methods* 2004. `10.1016/j.jviromet.2004.05.018` (paywalled)
- **P2** Nosema ceranae — Higes, Mariano, *Journal of Invertebrate Pathology* 2008. `10.1016/j.jip.2007.06.002` (paywalled)
- **P2** Orbivirus (Toggenburg) — Hofmann, Martin A., *Journal of Virological Methods* 2010. `10.1016/j.jviromet.2010.02.027` (paywalled)
- **P2** Orthobornavirus (avian) — de Kloet, Arne H., *Journal of Veterinary Diagnostic Investigation* 2011. `10.1177/1040638711403406` (paywalled)
- **P2** Orthopoxvirus — Meyer, Hermann, *Journal of Virological Methods* 1997. `10.1016/s0166-0934(96)02155-6` (OA but table not machine-readable)
- **P2** Ostreid herpesvirus 1 — Pepin, J.F., *Journal of Virological Methods* 2008. `10.1016/j.jviromet.2008.01.022` (paywalled)
- **P2** Phocine distemper virus — Hammond, John A., *Journal of General Virology* 2005. `10.1099/vir.0.80962-0` (paywalled)
- **P2** Phocine distemper virus — Bogomolni, Andrea L., *Journal of Wildlife Diseases* 2015. `10.7589/2014-05-142` (paywalled)
- **P2** Pseudogymnoascus destructans — Chaturvedi, Sudha, *Mycopathologia* 2011. `10.1007/s11046-011-9435-5` (paywalled)
- **P2** Psittacine DNA viruses — Katoh, Hiroshi, *Journal of Virological Methods* 2008. `10.1016/j.jviromet.2008.08.015` (paywalled)
- **P2** Testadenovirus/Atadenovirus — Salzmann, Ekaterina, *Journal of Zoo and Wildlife Medicine* 2021. `10.1638/2020-0078` (paywalled)
- **P2** Testudinid herpesvirus — Murakami, Masaru, *Journal of Veterinary Diagnostic Investigation* 2001. `10.1177/104063870101300610` (paywalled)
- **P2** Testudinid herpesvirus 2 / Mycoplasma — Braun, Josephine, *Journal of Wildlife Diseases* 2014. `10.7589/2013-09-231` (paywalled)
- **P2** Tilapia tilapinevirus — Kembou Tsofack, Japhette Esther, *Journal of Clinical Microbiology* 2017. `10.1128/JCM.01808-16` (paywalled)
- **P2** Tilapia tilapinevirus — Chengula, Augustino Alfred, *Journal of Virological Methods* 2022. `10.1016/j.jviromet.2022.114567` (paywalled)
- **P2** Usutu virus — Folly, Arran J, *Eurosurveillance* 2020. `10.2807/1560-7917.ES.2020.25.41.2001732` (OA but table not machine-readable)
- **P2** Vibrio coralliilyticus — Pollock, F. Joseph, *Applied and Environmental Microbiology* 2010. `10.1128/AEM.00330-10` (paywalled)
- **P3** Aphanomyces astaci + aquatic pathogens — Rieder, Jessica, *Journal of Microbiological Methods* 2022. `10.1016/j.mimet.2022.106594` (paywalled)
- **P3** Avian orthoavulavirus 1 — Reid, Scott M, *Veterinary Record* 2022. `10.1002/vetr.2057` (paywalled)
- **P3** Batrachochytrium spp. — Lastra González, David, *Journal of Fungi* 2021. `10.3390/jof7040258` (OA but table not machine-readable)
- **P3** Baylisascaris schroederi — Zhou, Xuan, *Journal of Wildlife Diseases* 2013. `10.7589/2012-07-175` (paywalled)
- **P3** Baylisascaris transfuga — De Ambrogi, M., *Veterinary Parasitology* 2011. `10.1016/j.vetpar.2011.02.025` (paywalled)
- **P3** Besnoitia besnoiti — Schares, G., *Veterinary Parasitology* 2011. `10.1016/j.vetpar.2011.01.038` (paywalled)
- **P3** Brucella — Huber, Birgit, *International Journal of Medical Microbiology* 2009. `10.1016/j.ijmm.2009.05.002` (paywalled)
- **P3** Canine morbillivirus — Halecker, Sabrina, *Viruses* 2021. `10.3390/v13081632` (OA but table not machine-readable)
- **P3** Cetacean morbillivirus — Centelleghe, Cinzia, *Journal of Virological Methods* 2016. `10.1016/j.jviromet.2016.05.005` (paywalled)
- **P3** Cetacean morbillivirus — Rubio-Guerri, Consuelo, *Veterinary Microbiology* 2013. `10.1016/j.vetmic.2012.12.031` (paywalled)
- **P3** Crithidia/Lotmaria (bumble bee) — Tripodi, Amber D., *Journal of Invertebrate Pathology* 2018. `10.1016/j.jip.2018.03.009` (paywalled)
- **P3** Flavobacterium psychrophilum — Fujiwara‐Nagata, E, *Journal of Fish Diseases* 2009. `10.1111/j.1365-2761.2009.01066.x` (paywalled)
- **P3** Francisella tularensis — Kevin, Maëllys, *Infection, Genetics and Evolution* 2021. `10.1016/j.meegid.2021.104741` (paywalled)
- **P3** Haliotid herpesvirus 1 — Chen, M.H., *Journal of Virological Methods* 2012. `10.1016/j.jviromet.2012.03.024` (paywalled)
- **P3** Helicobacter (gopher tortoise) — Desiderio, Tasha M., *Veterinary Microbiology* 2021. `10.1016/j.vetmic.2021.109136` (paywalled)
- **P3** Mycoplasma agassizii — duPre', S.A., *Journal of Microbiological Methods* 2011. `10.1016/j.mimet.2011.04.017` (paywalled)
- **P3** Myxoma virus — Dalton, Kevin P., *Journal of Virological Methods* 2009. `10.1016/j.jviromet.2009.06.026` (paywalled)
- **P3** Orthobornavirus (PaBV-4) — Komorizono, Ryo, *Journal of Virological Methods* 2020. `10.1016/j.jviromet.2019.113749` (paywalled)
- **P3** Ostreid herpesvirus 1 — Liu, O, *Diseases of Aquatic Organisms* 2020. `10.3354/dao03445` (paywalled)
- **P3** Plasmodium (avian) — Schoener, E. R., *Parasitology Research* 2017. `10.1007/s00436-017-5452-8` (paywalled)
- **P3** Pseudogymnoascus destructans — Lindner, Daniel L., *Mycologia* 2011. `10.3852/10-262` (paywalled)
- **P3** Ranavirus (LMBV) — Getchell, R. G., *Journal of Aquatic Animal Health* 2007. `10.1577/H07-009.1` (paywalled)
- **P3** Vibrio coralliilyticus — Wilson, Bryan, *PLoS ONE* 2013. `10.1371/journal.pone.0081800` (OA but table not machine-readable)

---

Full table with all 99 DOI-verified candidates:
`results/literature-audit-2026-10-04.tsv`

## A note on provenance, in light of commit 8ddd251

While this sweep was running, the registry gained
`citation.oligos_designed_here` and `scripts/audit_provenance.py`, on the
finding that 138 of 151 entries were transcribed from a lab spreadsheet that
records *where a primer was read from* rather than *who designed it*.

That distinction bears directly on how these 99 proposals should be recorded.
The large majority of the rows here were selected precisely because they are
**design papers** — titles of the form "development and validation of…",
"generation and validation of…", "a novel qPCR assay for…" — so for most of
them `oligos_designed_here: true` should be defensible once the PDF is read.
But a minority were kept for their *coverage* claim rather than their design
claim, and for those the primers are very likely someone else's:

- Surveillance and first-detection papers: `10.2807/1560-7917.ES.2020.25.41.2001732`
  (Usutu in UK birds), `10.1016/j.vetpar.2012.10.001` (Neospora in wild
  carnivorans), `10.1638/2020-0078` (chelonian adenoviruses),
  `10.7589/2013-09-231` (desert tortoise methods comparison).
- Assay-performance papers whose value here is the *failure* they report, not a
  new oligo: `10.3354/dao03932` (ChHV5 qPCR underpredicts),
  `10.1016/j.ijpara.2018.02.003` (differential amplification across
  haemosporidian genera).

For that second group the right outcome may well be a row in
`docs/validation-cases.tsv` and no registry entry at all — which is the more
valuable contribution anyway, given that the review names that file as the only
thing calibrating `config.yaml`. None of these should be entered with
`oligos_designed_here` left defaulted and unexamined.
