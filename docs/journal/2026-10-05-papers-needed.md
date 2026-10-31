# Papers needed, 2026-10-05

Two lists. The first is the one that matters for *correctness*: papers behind
assays already in the registry, whose stored sequences cannot be checked until
the PDF is in hand. The second is papers for assays the registry does not have
yet, which would *add* coverage.

Drop PDFs anywhere and run:

```bash
python scripts/verify_oligos_against_paper.py --pdf-dir <folder> --tsv results/oligo-verification.tsv
```

The script matches a PDF to an entry by a DOI printed in its text, or by the
cited first author and design year in its opening pages, so filenames do not
matter.

## List 1 — verify sequences already in the registry (54 papers, 195 oligos)

Current state: of 344 stored oligos, only 59 were checkable and **40 agreed with
their paper**. 179 are behind paywalls and 106 have no DOI at all. Every row
below converts unverifiable sequences into verified ones.

`2-recheck` means the open-access full text was readable but the sequence was
not found in it, usually because the primer table is an image or sits in a
supplement. Those need the PDF too, and are more suspicious than the paywalled
ones because something is already known not to match.

| # oligos | priority | DOI | taxon | paper |
|---|---|---|---|---|
| 10 | 1-verify | [10.1128/Jcm.01893-06](https://doi.org/10.1128/Jcm.01893-06) | Filoviridae | Zhai, J. H. et al. Rapid molecular strategy for filovirus detection and characterization. Journ |
| 8 | 1-verify | [10.1128/JCM.43.12.6176-6182.2005](https://doi.org/10.1128/JCM.43.12.6176-6182.2005) | Mastadenovirus | Casas I et al. 2005. J Clin Microbiol 43:6176-6182 (round 1) |
| 8 | 2-recheck | [10.1186/1743-422X-4-84](https://doi.org/10.1186/1743-422X-4-84) | Cytomegalovirus | Prepens S et al. 2007. Virol J 4:84 |
| 6 | 2-recheck | [10.1016/j.vetmic.2008.10.035](https://doi.org/10.1016/j.vetmic.2008.10.035) | Astroviridae | Atkins, A. et al. Characterization of an outbreak of astroviral diarrhea in a group of cheetahs |
| 6 | 1-verify | [10.1016/j.vetmic.2012.07.030](https://doi.org/10.1016/j.vetmic.2012.07.030) | Sunshinevirus | Hyndman TH et al. 2012. Vet Microbiol 161:77-87 |
| 6 | 1-verify | [10.1128/JVI.79.6.3883-3887.2005](https://doi.org/10.1128/JVI.79.6.3883-3887.2005) | Polyomaviridae | Johne R et al. 2005. J Virol 79:3883-3887 (VP1 outer primers) |
| 6 | 1-verify | [10.1177/1040638711416846](https://doi.org/10.1177/1040638711416846) | Mycoplasma | Rebelo AR et al. 2011. J Vet Diagn Invest 23:932-936 |
| 6 | 1-verify | [10.1645/GE-184R1](https://doi.org/10.1645/GE-184R1) | Haemosporida | Hellgren O et al. 2004. J Parasitol 90:797-802 (HaemF/HaemR2 nested round) |
| 5 | 1-verify | [10.1111/j.1365-2761.2007.00828.x](https://doi.org/10.1111/j.1365-2761.2007.00828.x) | Ranavirus | Pallister J et al. 2007. J Fish Dis 30:427-438 |
| 5 | 1-verify | [10.1128/jcm.34.7.1666-1671.1996](https://doi.org/10.1128/jcm.34.7.1666-1671.1996) | Herpesviridae | VanDevanter DR et al. 1996. J Clin Microbiol 34:1666-1671 (DFA/ILK/KG1 nested pan-herpesvirus D |
| 4 | 1-verify | [10.1002/jmv.10465](https://doi.org/10.1002/jmv.10465) | Phlebovirus | Sanchez-Seco, M. P. et al. Detection and identification of Toscana and other phleboviruses by R |
| 4 | 1-verify | [10.1006/viro.1993.1217](https://doi.org/10.1006/viro.1993.1217) | Morbillivirus | Barrett T et al. 1993. Virology 193:1010-1012 (Grosh F/R are the same sequences as MorbF/MorbR) |
| 4 | 1-verify | [10.1007/s00436-010-1945-4](https://doi.org/10.1007/s00436-010-1945-4) | Sarcocystis | Kutkienė L et al. 2010. Parasitol Res 107:879-888 |
| 4 | 1-verify | [10.1007/s00705-005-0679-6](https://doi.org/10.1007/s00705-005-0679-6) | Chordopoxvirinae | Bracht, A. J. et al. Genetic identification of novel poxviruses of cetaceans and pinnipeds. Arc |
| 4 | 1-verify | [10.1007/s11259-007-0020-9](https://doi.org/10.1007/s11259-007-0020-9) | Canine morbillivirus | Scagliarini A et al. 2007. Vet Res Commun 31(Suppl 1):261-263 |
| 4 | 1-verify | [10.1016/0166-0934(94)90098-1](https://doi.org/10.1016/0166-0934(94)90098-1) | Bornaviridae | Zimmermann W et al. 1994. J Virol Methods 46:133-143 (nested round) |
| 4 | 1-verify | [10.1016/S0166-0934(01)00306-8](https://doi.org/10.1016/S0166-0934(01)00306-8) | Alphavirus | Sánchez-Seco MP et al. 2001. J Virol Methods 95:153-161 (Alpha1/Alpha2 nsP4 nested PCR) |
| 4 | 1-verify | [10.1016/S0168-1702(00)00252-5](https://doi.org/10.1016/S0168-1702(00)00252-5) | Herpesviridae | TERM_707/708 terminase primers: Chmielewicz B et al. (Ehlers group, Robert Koch Institute) — no |
| 4 | 1-verify | [10.1016/S0168-1702(97)01458-5](https://doi.org/10.1016/S0168-1702(97)01458-5) | Arenaviridae | Lozano, M. E. et al. Characterization of arenaviruses using a family-specific primer set for RT |
| 4 | 1-verify | [10.1016/S0168-1702(99)00059-3](https://doi.org/10.1016/S0168-1702(99)00059-3) | Ferlavirus | Ahne W et al. 1999. Virus Res 63:65-74 |
| 4 | 1-verify | [10.1016/j.jviromet.2006.03.008](https://doi.org/10.1016/j.jviromet.2006.03.008) | Lyssavirus | Vazquez-Moron, S., Avellon, A. & Echevarria, J. E. RT-PCR for detection of all seven genotypes  |
| 4 | 1-verify | [10.1038/nature08200](https://doi.org/10.1038/nature08200) | Simian immunodeficiency virus | Keele BF et al. 2009. Nature 460:515-519 |
| 4 | 1-verify | [10.1099/vir.0.81128-0](https://doi.org/10.1099/vir.0.81128-0) | Rhabdoviridae | Bourhy, H., Cowley, J. A., Larrous, F., Holmes, E. C. & Walker, P. J. Phylogenetic relationship |
| 4 | 1-verify | [10.1128/AEM.66.12.5492-5498.2000](https://doi.org/10.1128/AEM.66.12.5492-5498.2000) | Cryptosporidium | Xiao L et al. 2000. Appl Environ Microbiol 66:5492-5498 |
| 4 | 1-verify | [10.1128/JCM.00192-08](https://doi.org/10.1128/JCM.00192-08) | Paramyxoviridae | Tong S et al. 2008. J Clin Microbiol 46:2652-2658 |
| 4 | 1-verify | [10.1128/JCM.00542-06](https://doi.org/10.1128/JCM.00542-06) | Enterovirus | Nix WA, Oberste MS, Pallansch MA. 2006. J Clin Microbiol 44:2698-2704 (222/224 VP3-VP1 primers) |
| 4 | 1-verify | [10.1128/JCM.39.5.1922-1927.2001](https://doi.org/10.1128/JCM.39.5.1922-1927.2001) | Flavivirus | Scaramozzino N et al. 2001 (cFD2); FS778 hemi-nested forward also from this paper |
| 4 | 1-verify | [10.1128/JVI.78.23.13366-13369.2004](https://doi.org/10.1128/JVI.78.23.13366-13369.2004) | Adenoviridae | Wellehan JF et al. 2004. J Virol 78:13366-13369 (pan-adenovirus pol nested PCR) |
| 3 | 1-verify | [10.1099/jmm.0.061820-0](https://doi.org/10.1099/jmm.0.061820-0) | Entamoeba | García G et al. 2014. J Med Microbiol 63:271-283 |
| 3 | 1-verify | [10.1128/JCM.02313-13](https://doi.org/10.1128/JCM.02313-13) | Batrachochytrium salamandrivorans | Blooi M et al. 2013. J Clin Microbiol 51:4173-4177 |
| 3 | 1-verify | [10.1128/JCM.40.9.3256-3260.2002](https://doi.org/10.1128/JCM.40.9.3256-3260.2002) | Influenza A virus | Spackman E et al. 2002. J Clin Microbiol 40:3256-3260 (matrix primers/probe); 2003 Avian Dis 47 |
| 3 | 1-verify | [10.1177/104063871002200106](https://doi.org/10.1177/104063871002200106) | Orthoreovirus | Landolfi JA et al. 2010. J Vet Diagn Invest 22:37-43 |
| 3 | 1-verify | [10.3354/dao060141](https://doi.org/10.3354/dao060141) | Batrachochytrium dendrobatidis | Boyle DG et al. 2004. Dis Aquat Org 60:141-148 |
| 2 | 1-verify | [10.1016/0168-1605(91)90148-I](https://doi.org/10.1016/0168-1605(91)90148-I) | Escherichia coli | Candrian U et al. 1991. Int J Food Microbiol 12:339-351 (spreadsheet spells it Candrain) |
| 2 | 1-verify | [10.1016/0890-8508(92)90002-F](https://doi.org/10.1016/0890-8508(92)90002-F) | Salmonella enterica | Rahn K et al. 1992. Mol Cell Probes 6:271-279 |
| 2 | 1-verify | [10.1016/S0016-5085(98)70589-X](https://doi.org/10.1016/S0016-5085(98)70589-X) | Helicobacter | Fox JG et al. 1998. Gastroenterology 114:755-763 |
| 2 | 1-verify | [10.1016/S0166-0934(99)00088-9](https://doi.org/10.1016/S0166-0934(99)00088-9) | Caliciviridae | Reid, S. M. et al. Development of a reverse transcription polymerase chain reaction procedure f |
| 2 | 1-verify | [10.1073/pnas.182412299](https://doi.org/10.1073/pnas.182412299) | Dependoparvovirus | Gao GP et al. 2002. Proc Natl Acad Sci USA 99:11854-11859 |
| 2 | 1-verify | [10.1093/infdis/167.2.458](https://doi.org/10.1093/infdis/167.2.458) | Shigella | Sethabutr O et al. 1993. J Infect Dis 167:458-461 |
| 2 | 1-verify | [10.1099/0022-1317-80-9-2437](https://doi.org/10.1099/0022-1317-80-9-2437) | Papillomaviridae | Forslund O et al. 1999. J Gen Virol 80:2437-2443 (FAP59/FAP64) |
| 2 | 1-verify | [10.1128/JCM.39.12.4506-4513.2001](https://doi.org/10.1128/JCM.39.12.4506-4513.2001) | West Nile virus | Lanciotti RS, Kerst AJ. 2001. J Clin Microbiol 39:4506-4513 |
| 2 | 1-verify | [10.1128/JVI.02311-08](https://doi.org/10.1128/JVI.02311-08) | Simian immunodeficiency virus | Takehisa J et al. 2009. J Virol 83:1635-1648 |
| 2 | 1-verify | [10.1128/JVI.75.2.857-866.2001](https://doi.org/10.1128/JVI.75.2.857-866.2001) | Simian immunodeficiency virus | Courgnaud V et al. 2001. J Virol 75:857-866 |
| 2 | 1-verify | [10.1128/aem.58.8.2606-2615.1992](https://doi.org/10.1128/aem.58.8.2606-2615.1992) | Mycoplasma | van Kuppeveld FJ et al. 1992. Appl Environ Microbiol 58:2606-2615 |
| 2 | 1-verify | [10.1128/jcm.30.8.1942-1947.1992](https://doi.org/10.1128/jcm.30.8.1942-1947.1992) | Yersinia enterocolitica | Ibrahim A, Liesack W, Stackebrandt E. 1992. J Clin Microbiol 30:1942-1947 |
| 2 | 2-recheck | [10.1128/mBio.00208-10](https://doi.org/10.1128/mBio.00208-10) | Coronaviridae | Quan PL et al. 2010. mBio 1:e00208-10 (PREDICT pan-CoV RdRp nested PCR; sheet says 'Lan et al 2 |
| 2 | 1-verify | [10.1354/vp.43-3-311](https://doi.org/10.1354/vp.43-3-311) | Apicomplexa | Garner MM et al. 2006. Vet Pathol 43:311-320 |
| 2 | 1-verify | [10.15654/TPK-140743](https://doi.org/10.15654/TPK-140743) | Reptarenavirus | Tierärztl Prax Ausg K 2015;43:239-247 |
| 2 | 1-verify | [10.1638/02-070](https://doi.org/10.1638/02-070) | Plasmodium | Grim KC et al. 2003. J Zoo Wildl Med 34:250-255 |
| 2 | 1-verify | [10.1645/ge-3310](https://doi.org/10.1645/ge-3310) | Apicomplexa | Schrenzel MD et al. 2005. J Parasitol 91:635-647 |
| 2 | 1-verify | [10.2460/javma.239.12.1584](https://doi.org/10.2460/javma.239.12.1584) | Eimeria furonis | Sledge DG et al. 2011. J Am Vet Med Assoc 239:1584-1588 |
| 2 | 1-verify | [10.7589/0090-3558-40.3.420](https://doi.org/10.7589/0090-3558-40.3.420) | Batrachochytrium dendrobatidis | Annis SL et al. 2004. J Wildl Dis 40:420-428 |
| 2 | 1-verify | [10.7589/0090-3558-42.2.279](https://doi.org/10.7589/0090-3558-42.2.279) | Mycoplasmatota (scoped by query to | Feldman SH et al. 2006. J Wildl Dis 42:279-288 |
| 2 | 1-verify | [10.7589/0090-3558-44.4.851](https://doi.org/10.7589/0090-3558-44.4.851) | Ranavirus | Johnson AJ et al. 2008. J Wildl Dis 44:851-863 |

## List 2 — papers for assays the registry does not have (99)

From the journal sweep in `docs/journal/2026-10-04-literature-audit.md`. All DOIs there
were Crossref-verified by that pass and four were independently spot-checked
here; every one matched its claimed title and first author. Nothing from this
list has been added to `registry/`, and some of it should not be: a paper that
reports another group's assay failing belongs in `docs/validation-cases.tsv`
with no registry entry at all, which is the more valuable contribution.

Ordered by the sweep's own priority. P1 first.

| pri | taxon | gene | DOI | journal | year | paper |
|---|---|---|---|---|---|---|
| P1 | Aphanomyces astaci | ITS | [10.1016/j.vetmic.2008.12.022](https://doi.org/10.1016/j.vetmic.2008.12.022) | Veterinary Microbiolog | 2009 | A quantitative TaqMan® MGB real-time polymerase chain reaction based a |
| P1 | Aphanomyces astaci | ITS | [10.1016/j.jip.2023.108008](https://doi.org/10.1016/j.jip.2023.108008) | Journal of Invertebrat | 2023 | Molecular detection of Aphanomyces astaci – An improved species specif |
| P1 | Batrachochytrium dendrobat | lineage marker | [10.1111/1755-0998.13299](https://doi.org/10.1111/1755-0998.13299) | Molecular Ecology Reso | 2021 | Discriminating lineages of Batrachochytrium dendrobatidis using quanti |
| P1 | Canine/phocine distemper v | N | [10.1128/jcm.02505-21](https://doi.org/10.1128/jcm.02505-21) | Journal of Clinical Mi | 2022 | Development and Validation of a Pan-Genotypic Real-Time Quantitative R |
| P1 | Cetacean morbillivirus | N/P | [10.1016/j.jviromet.2020.113964](https://doi.org/10.1016/j.jviromet.2020.113964) | Journal of Virological | 2020 | A novel real-time PCR to detect Cetacean morbillivirus in Atlantic cet |
| P1 | Chelonid alphaherpesvirus  | pol/UL30 | [10.3354/dao03932](https://doi.org/10.3354/dao03932) | Diseases of Aquatic Or | 2026 | Chelonid alphaherpesvirus 5 qPCR of archived blood and skin samples un |
| P1 | Devil facial tumour diseas | marker | [10.1098/rsos.180870](https://doi.org/10.1098/rsos.180870) | Royal Society Open Sci | 2018 | Tasman-PCR: a genetic diagnostic assay for Tasmanian devil facial tumo |
| P1 | Elephant endotheliotropic  | terminase/pol | [10.1016/j.jviromet.2016.08.010](https://doi.org/10.1016/j.jviromet.2016.08.010) | Journal of Virological | 2016 | Generation and validation of new quantitative real time PCR assays to  |
| P1 | Haemosporida (avian) | mito cytb/COI | [10.1016/j.ijpara.2018.02.003](https://doi.org/10.1016/j.ijpara.2018.02.003) | International Journal  | 2018 | Primers targeting mitochondrial genes of avian haemosporidians: PCR de |
| P1 | Influenza A virus (H5/H7 H | HA | [10.1128/JCM.01264-10](https://doi.org/10.1128/JCM.01264-10) | Journal of Clinical Mi | 2010 | Broad Detection of Diverse H5 and H7 Hemagglutinin Genes of Avian Infl |
| P1 | Ophidiomyces ophidiicola | ITS | [10.1177/1040638715573983](https://doi.org/10.1177/1040638715573983) | Journal of Veterinary  | 2015 | Development and use of a real-time polymerase chain reaction assay for |
| P1 | Ophidiomyces ophidiicola | genotyping | [10.1371/journal.pone.0289159](https://doi.org/10.1371/journal.pone.0289159) | PLOS ONE | 2023 | Development and application of a qPCR-based genotyping assay for Ophid |
| P1 | Orthobornavirus (avian) | M/N | [10.3390/v13071358](https://doi.org/10.3390/v13071358) | Viruses | 2021 | A New Multiplex Real-Time RT-PCR for Simultaneous Detection and Differ |
| P1 | Pseudogymnoascus destructa | IGS | [10.3852/12-242](https://doi.org/10.3852/12-242) | Mycologia | 2013 | Bat white-nose syndrome: a real-time TaqMan polymerase chain reaction  |
| P1 | Pseudogymnoascus destructa | ITS/IGS | [10.1128/AEM.02897-13](https://doi.org/10.1128/AEM.02897-13) | Applied and Environmen | 2014 | Highly Sensitive Quantitative PCR for the Detection and Differentiatio |
| P1 | West Nile virus | lineage 1/2 | [10.1016/j.jviromet.2007.05.021](https://doi.org/10.1016/j.jviromet.2007.05.021) | Journal of Virological | 2007 | Detection of West Nile virus lineages 1 and 2 by real-time PCR |
| P1 | West Nile virus | all lineages | [10.1016/j.jviromet.2016.07.026](https://doi.org/10.1016/j.jviromet.2016.07.026) | Journal of Virological | 2016 | Real time PCR assay for detection of all known lineages of West Nile v |
| P2 | Amphibian Perkinsea | SSU rDNA | [10.3354/dao03239](https://doi.org/10.3354/dao03239) | Diseases of Aquatic Or | 2018 | Novel quantitative PCR assay specific for the emerging Perkinsea amphi |
| P2 | Amphibian Perkinsea | SSU rDNA | [10.1098/rsos.202150](https://doi.org/10.1098/rsos.202150) | Royal Society Open Sci | 2021 | A novel duplex qPCR assay for stepwise detection of multiple Perkinsea |
| P2 | Aphanomyces astaci | ITS | [10.3354/dao072053](https://doi.org/10.3354/dao072053) | Diseases of Aquatic Or | 2006 | Detection of Aphanomyces astaci in North American crayfish by polymera |
| P2 | Aphanomyces astaci | mtDNA | [10.1017/S0031182018000227](https://doi.org/10.1017/S0031182018000227) | Parasitology | 2018 | MtDNA allows the sensitive detection and haplotyping of the crayfish p |
| P2 | Avian orthoavulavirus 1 (p | F | [10.1016/s0166-0934(02)00148-9](https://doi.org/10.1016/s0166-0934(02)00148-9) | Journal of Virological | 2002 | Development of a RT-nested PCR test detecting pigeon Paramyxovirus-1 d |
| P2 | Avipoxvirus | 4b core | [10.1371/journal.pone.0230701](https://doi.org/10.1371/journal.pone.0230701) | PLOS ONE | 2020 | TaqMan quantitative real-time PCR for detecting Avipoxvirus DNA in var |
| P2 | Avipoxvirus | 4b core | [10.1371/journal.pone.0010745](https://doi.org/10.1371/journal.pone.0010745) | PLoS ONE | 2010 | Taqman Real-Time PCR Detects Avipoxvirus DNA in Blood of Hawaìi `Amaki |
| P2 | Avipoxvirus | 4b core | [10.1099/vir.0.81738-0](https://doi.org/10.1099/vir.0.81738-0) | Journal of General Vir | 2006 | Avipoxvirus phylogenetics: identification of a PCR length polymorphism |
| P2 | Batrachovirus (amphibian h | pol/terminase | [10.1177/1040638720951134](https://doi.org/10.1177/1040638720951134) | Journal of Veterinary  | 2020 | Consensus PCR protocols for the detection of amphibian herpesviruses ( |
| P2 | Baylisascaris procyonis | ITS | [10.1645/GE-1905.1](https://doi.org/10.1645/GE-1905.1) | Journal of Parasitolog | 2009 | Pcr Assays for Detection of Baylisascaris procyonis Eggs and Larvae |
| P2 | Bd / Bsal / ranavirus | ITS/MCP | [10.3354/dao03230](https://doi.org/10.3354/dao03230) | Diseases of Aquatic Or | 2018 | Optimizing, validating, and field testing a multiplex qPCR for the det |
| P2 | Beak and feather disease v | Rep | [10.1016/j.jviromet.2017.02.017](https://doi.org/10.1016/j.jviromet.2017.02.017) | Journal of Virological | 2017 | Development and evaluation of TaqMan real-time PCR assay for detection |
| P2 | Brucella canis | IS711 | [10.1111/zph.12041](https://doi.org/10.1111/zph.12041) | Zoonoses and Public He | 2013 | Early Detection ofBrucella Canisvia Quantitative Polymerase Chain Reac |
| P2 | Brucella ceti | IS711 | [10.3354/dao03034](https://doi.org/10.3354/dao03034) | Diseases of Aquatic Or | 2016 | Detection of Brucella spp. in bottlenose dolphins Tursiops truncatus b |
| P2 | Canine morbillivirus | N/H | [10.1371/journal.pone.0232044](https://doi.org/10.1371/journal.pone.0232044) | PLOS ONE | 2020 | Development and validation of a portable, point-of-care canine distemp |
| P2 | Cetacean morbillivirus | N | [10.1016/j.jviromet.2008.11.008](https://doi.org/10.1016/j.jviromet.2008.11.008) | Journal of Virological | 2009 | Real-time RT-PCR assays for the rapid and differential detection of do |
| P2 | Chelonid alphaherpesvirus  | pol | [10.1006/viro.1998.9207](https://doi.org/10.1006/viro.1998.9207) | Virology | 1998 | Three Closely Related Herpesviruses Are Associated with Fibropapilloma |
| P2 | Chlamydia (avian) | 23S/ompA | [10.1080/03079457.2022.2031882](https://doi.org/10.1080/03079457.2022.2031882) | Avian Pathology | 2022 | A multiplex real-time PCR assay for differential identification of avi |
| P2 | Chlamydia psittaci | ompA | [10.1128/jcm.35.8.2043-2046.1997](https://doi.org/10.1128/jcm.35.8.2043-2046.1997) | Journal of Clinical Mi | 1997 | Application of a nested, multiplex PCR to psittacosis outbreaks |
| P2 | Chlamydia psittaci | incA | [10.1099/jmm.0.46335-0](https://doi.org/10.1099/jmm.0.46335-0) | Journal of Medical Mic | 2006 | Development of a real-time PCR for the detection of Chlamydia psittaci |
| P2 | Chordopoxvirinae | pan-pox | [10.1128/JCM.01697-09](https://doi.org/10.1128/JCM.01697-09) | Journal of Clinical Mi | 2010 | GC Content-Based Pan-Pox Universal PCR Assays for Poxvirus Detection |
| P2 | Deformed wing virus | RdRp | [10.3390/microorganisms12061105](https://doi.org/10.3390/microorganisms12061105) | Microorganisms | 2024 | Selection and Multiplexing of Reverse Transcription–Quantitative PCR T |
| P2 | Elephant endotheliotropic  | pol | [10.1016/j.vetmic.2010.05.042](https://doi.org/10.1016/j.vetmic.2010.05.042) | Veterinary Microbiolog | 2011 | Detection and evaluation of novel herpesviruses in routine and patholo |
| P2 | Francisella tularensis | tul4 | [10.1128/jcm.31.1.152-154.1993](https://doi.org/10.1128/jcm.31.1.152-154.1993) | Journal of Clinical Mi | 1993 | Detection of Francisella tularensis in blood by polymerase chain react |
| P2 | Hendra virus | N/M | [10.1016/j.jviromet.2012.01.020](https://doi.org/10.1016/j.jviromet.2012.01.020) | Journal of Virological | 2012 | Hendra virus detection using Loop-Mediated Isothermal Amplification |
| P2 | Influenza A virus (H5/H7/H | HA | [10.1016/j.jviromet.2024.114942](https://doi.org/10.1016/j.jviromet.2024.114942) | Journal of Virological | 2024 | Development and evaluation of a multiplex real-time RT-PCR assay for s |
| P2 | Lagovirus (RHDV2/RHDVb) | VP60 | [10.1111/tbed.12607](https://doi.org/10.1111/tbed.12607) | Transboundary and Emer | 2017 | Fast specific field detection of RHDVb |
| P2 | Leptospira | lipL32 | [10.1371/journal.pone.0241584](https://doi.org/10.1371/journal.pone.0241584) | PLOS ONE | 2020 | Development of lipL32 real-time PCR combined with an internal and extr |
| P2 | Leptospira | 16S rrs | [10.1099/jmm.0.45860-0](https://doi.org/10.1099/jmm.0.45860-0) | Journal of Medical Mic | 2005 | Detection of pathogenic leptospires by real-time quantitative PCR |
| P2 | Lyssavirus | N | [10.1016/j.jviromet.2011.07.002](https://doi.org/10.1016/j.jviromet.2011.07.002) | Journal of Virological | 2011 | A universal real-time assay for the detection of Lyssaviruses |
| P2 | Monkeypox virus | B6R/MGB | [10.1038/labinvest.3700143](https://doi.org/10.1038/labinvest.3700143) | Laboratory Investigati | 2004 | Monkeypox virus detection in rodents using real-time 3′-minor groove b |
| P2 | Mycobacterium bovis | IS6110/RD | [10.1371/journal.pone.0207365](https://doi.org/10.1371/journal.pone.0207365) | PLOS ONE | 2018 | Differential detection of tuberculous and non-tuberculous mycobacteria |
| P2 | Mycobacterium microti | RD/spoligo | [10.1128/JCM.00440-14](https://doi.org/10.1128/JCM.00440-14) | Journal of Clinical Mi | 2014 | Detection and Molecular Characterization of Mycobacterium microti Isol |
| P2 | Mycoplasma gallisepticum | mgc2 | [10.1080/03079450802216629](https://doi.org/10.1080/03079450802216629) | Avian Pathology | 2008 | Detection and quantification of Mycoplasma gallisepticum genome load i |
| P2 | Myxoma virus | M000.5/M071 | [10.1016/j.jviromet.2019.113709](https://doi.org/10.1016/j.jviromet.2019.113709) | Journal of Virological | 2019 | Detection of viral DNA of myxoma virus using a validated PCR method wi |
| P2 | Neospora caninum | Nc5 | [10.1016/j.vetpar.2012.10.001](https://doi.org/10.1016/j.vetpar.2012.10.001) | Veterinary Parasitolog | 2013 | Detection of Neospora caninum in wild carnivorans in Great Britain |
| P2 | Nipah henipavirus | N | [10.1016/j.jviromet.2004.05.018](https://doi.org/10.1016/j.jviromet.2004.05.018) | Journal of Virological | 2004 | Specific detection of Nipah virus using real-time RT-PCR (TaqMan) |
| P2 | Nosema ceranae | SSU | [10.1016/j.jip.2007.06.002](https://doi.org/10.1016/j.jip.2007.06.002) | Journal of Invertebrat | 2008 | Detection of infective Nosema ceranae (Microsporidia) spores in corbic |
| P2 | Orbivirus (Toggenburg) | segment 2 | [10.1016/j.jviromet.2010.02.027](https://doi.org/10.1016/j.jviromet.2010.02.027) | Journal of Virological | 2010 | Detection of Toggenburg Orbivirus by a segment 2-specific quantitative |
| P2 | Orthobornavirus (avian) | N | [10.1177/1040638711403406](https://doi.org/10.1177/1040638711403406) | Journal of Veterinary  | 2011 | Diagnosis of Avian bornavirus infection in psittaciformes by serum ant |
| P2 | Orthopoxvirus | ATI | [10.1016/s0166-0934(96)02155-6](https://doi.org/10.1016/s0166-0934(96)02155-6) | Journal of Virological | 1997 | Gene for A-type inclusion body protein is useful for a polymerase chai |
| P2 | Ostreid herpesvirus 1 | ORF100/C9 | [10.1016/j.jviromet.2008.01.022](https://doi.org/10.1016/j.jviromet.2008.01.022) | Journal of Virological | 2008 | Rapid and sensitive detection of ostreid herpesvirus 1 in oyster sampl |
| P2 | Paranannizziopsis spp. | ITS | [10.3389/fmicb.2023.1302586](https://doi.org/10.3389/fmicb.2023.1302586) | Frontiers in Microbiol | 2023 | Paranannizziopsis spp. infections in wild snakes and a qPCR assay for  |
| P2 | Phocine distemper virus | N/P | [10.1099/vir.0.80962-0](https://doi.org/10.1099/vir.0.80962-0) | Journal of General Vir | 2005 | Identification and real-time PCR quantification of Phocine distemper v |
| P2 | Phocine distemper virus | N | [10.7589/2014-05-142](https://doi.org/10.7589/2014-05-142) | Journal of Wildlife Di | 2015 | DEVELOPMENT OF A ONE-STEP DUPLEX RT-qPCR FOR THE QUANTIFICATION OF PHO |
| P2 | Pseudogymnoascus destructa | ITS | [10.1007/s11046-011-9435-5](https://doi.org/10.1007/s11046-011-9435-5) | Mycopathologia | 2011 | Rapid Real-Time PCR Assay for Culture and Tissue Identification of Geo |
| P2 | Psittacine DNA viruses | Rep/VP1 | [10.1016/j.jviromet.2008.08.015](https://doi.org/10.1016/j.jviromet.2008.08.015) | Journal of Virological | 2008 | Development of novel real-time PCR assays for detecting DNA virus infe |
| P2 | Reptarenavirus | L/NP | [10.3390/v15122313](https://doi.org/10.3390/v15122313) | Viruses | 2023 | A Multiplex RT-PCR Method for the Detection of Reptarenavirus Infectio |
| P2 | Testadenovirus/Atadenoviru | pol | [10.1638/2020-0078](https://doi.org/10.1638/2020-0078) | Journal of Zoo and Wil | 2021 | DETECTION OF TESTADENOVIRUSES AND ATADENOVIRUSES IN TORTOISES AND TURT |
| P2 | Testudinid herpesvirus | pol | [10.1177/104063870101300610](https://doi.org/10.1177/104063870101300610) | Journal of Veterinary  | 2001 | Development of Species-Specific PCR Techniques for the Detection of To |
| P2 | Testudinid herpesvirus 2 / | pol | [10.7589/2013-09-231](https://doi.org/10.7589/2013-09-231) | Journal of Wildlife Di | 2014 | MOLECULAR METHODS TO DETECT MYCOPLASMA SPP. AND TESTUDINID HERPESVIRUS |
| P2 | Tilapia tilapinevirus | segment 3 | [10.1128/JCM.01808-16](https://doi.org/10.1128/JCM.01808-16) | Journal of Clinical Mi | 2017 | Detection of Tilapia Lake Virus in Clinical Samples by Culturing and N |
| P2 | Tilapia tilapinevirus | segment 1 | [10.1016/j.jviromet.2022.114567](https://doi.org/10.1016/j.jviromet.2022.114567) | Journal of Virological | 2022 | Efficiency, sensitivity and specificity of a quantitative real-time PC |
| P2 | Trichomonas gallinae | ITS/SSU | [10.1007/s00436-020-06887-x](https://doi.org/10.1007/s00436-020-06887-x) | Parasitology Research | 2020 | A SYBR green I real-time polymerase chain reaction (PCR) assay for det |
| P2 | Usutu virus | NS5 | [10.2807/1560-7917.ES.2020.25.41.2001732](https://doi.org/10.2807/1560-7917.ES.2020.25.41.2001732) | Eurosurveillance | 2020 | Detection of Usutu virus infection in wild birds in the United Kingdom |
| P2 | Vairimorpha/Nosema bombi | SSU | [10.1038/s41598-020-57909-8](https://doi.org/10.1038/s41598-020-57909-8) | Scientific Reports | 2020 | Direct and sensitive detection of a microsporidian parasite of bumbleb |
| P2 | Vibrio coralliilyticus | dnaJ | [10.1128/AEM.00330-10](https://doi.org/10.1128/AEM.00330-10) | Applied and Environmen | 2010 | Detection and Quantification of the Coral Pathogen Vibrio coralliilyti |
| P3 | Aphanomyces astaci + aquat | ITS | [10.1016/j.mimet.2022.106594](https://doi.org/10.1016/j.mimet.2022.106594) | Journal of Microbiolog | 2022 | Detecting aquatic pathogens with field-compatible dried qPCR assays |
| P3 | Avian orthoavulavirus 1 | F | [10.1002/vetr.2057](https://doi.org/10.1002/vetr.2057) | Veterinary Record | 2022 | Molecular detection of pigeon paramyxovirus type 1 |
| P3 | Batrachochytrium spp. | ITS | [10.3390/jof7040258](https://doi.org/10.3390/jof7040258) | Journal of Fungi | 2021 | Dual Detection of the Chytrid Fungi Batrachochytrium spp. with an Enha |
| P3 | Baylisascaris schroederi | ITS | [10.7589/2012-07-175](https://doi.org/10.7589/2012-07-175) | Journal of Wildlife Di | 2013 | Molecular Diagnosis ofBaylisascaris schroederiInfections in Giant Pand |
| P3 | Baylisascaris transfuga | ITS | [10.1016/j.vetpar.2011.02.025](https://doi.org/10.1016/j.vetpar.2011.02.025) | Veterinary Parasitolog | 2011 | Occurrence of Baylisascaris transfuga in wild populations of European  |
| P3 | Besnoitia besnoiti | ITS-1 | [10.1016/j.vetpar.2011.01.038](https://doi.org/10.1016/j.vetpar.2011.01.038) | Veterinary Parasitolog | 2011 | Quantitative real time polymerase chain reaction assays for the sensit |
| P3 | Brucella | multiplex typi | [10.1016/j.ijmm.2009.05.002](https://doi.org/10.1016/j.ijmm.2009.05.002) | International Journal  | 2009 | Development of a PCR assay for typing and subtyping of Brucella specie |
| P3 | Canine morbillivirus | N/H | [10.3390/v13081632](https://doi.org/10.3390/v13081632) | Viruses | 2021 | A New Molecular Detection System for Canine Distemper Virus Based on a |
| P3 | Cetacean morbillivirus | N | [10.1016/j.jviromet.2016.05.005](https://doi.org/10.1016/j.jviromet.2016.05.005) | Journal of Virological | 2016 | Molecular analysis of dolphin morbillivirus: A new sensitive detection |
| P3 | Cetacean morbillivirus | N | [10.1016/j.vetmic.2012.12.031](https://doi.org/10.1016/j.vetmic.2012.12.031) | Veterinary Microbiolog | 2013 | Simultaneous diagnosis of Cetacean morbillivirus infection in dolphins |
| P3 | Crithidia/Lotmaria (bumble | SSU | [10.1016/j.jip.2018.03.009](https://doi.org/10.1016/j.jip.2018.03.009) | Journal of Invertebrat | 2018 | Novel multiplex PCR reveals multiple trypanosomatid species infecting  |
| P3 | Flavobacterium psychrophil | 16S | [10.1111/j.1365-2761.2009.01066.x](https://doi.org/10.1111/j.1365-2761.2009.01066.x) | Journal of Fish Diseas | 2009 | Development and evaluation of a loop‐mediated isothermal amplification |
| P3 | Francisella tularensis | HRM targets | [10.1016/j.meegid.2021.104741](https://doi.org/10.1016/j.meegid.2021.104741) | Infection, Genetics an | 2021 | High-resolution melting PCR assay as a powerful tool for the epidemiol |
| P3 | Haliotid herpesvirus 1 | DNA pol | [10.1016/j.jviromet.2012.03.024](https://doi.org/10.1016/j.jviromet.2012.03.024) | Journal of Virological | 2012 | Development of a polymerase chain reaction for the detection of abalon |
| P3 | Helicobacter (gopher torto | 16S | [10.1016/j.vetmic.2021.109136](https://doi.org/10.1016/j.vetmic.2021.109136) | Veterinary Microbiolog | 2021 | Identification of a novel mortality-associated Helicobacter species in |
| P3 | Leporid gammaherpesvirus 5 | pol | [10.3390/v13040715](https://doi.org/10.3390/v13040715) | Viruses | 2021 | A Versatile qPCR for Diagnosis of Leporid Gammaherpesvirus 5 Using Eva |
| P3 | Mycoplasma agassizii | 16S | [10.1016/j.mimet.2011.04.017](https://doi.org/10.1016/j.mimet.2011.04.017) | Journal of Microbiolog | 2011 | Quantitative PCR method for detection of mycoplasma spp. DNA in nasal  |
| P3 | Mycoplasma gallisepticum | strain markers | [10.3390/pathogens12010111](https://doi.org/10.3390/pathogens12010111) | Pathogens | 2023 | A Multiplex PCR Assay for Differential Identification of Wild-type and |
| P3 | Myxoma virus | M-genes | [10.1016/j.jviromet.2009.06.026](https://doi.org/10.1016/j.jviromet.2009.06.026) | Journal of Virological | 2009 | Rapid identification of myxoma virus variants by long-range PCR and re |
| P3 | Orthobornavirus (PaBV-4) | M | [10.1016/j.jviromet.2019.113749](https://doi.org/10.1016/j.jviromet.2019.113749) | Journal of Virological | 2020 | Development of a reverse transcription-loop-mediated isothermal amplif |
| P3 | Ostreid herpesvirus 1 | C9/B | [10.3354/dao03445](https://doi.org/10.3354/dao03445) | Diseases of Aquatic Or | 2020 | Detection of ostreid herpesvirus-1 in plankton and seawater samples at |
| P3 | Plasmodium (avian) | cytb | [10.1007/s00436-017-5452-8](https://doi.org/10.1007/s00436-017-5452-8) | Parasitology Research | 2017 | Development of a rapid HRM qPCR for the diagnosis of the four most pre |
| P3 | Pseudogymnoascus destructa | ITS | [10.3852/10-262](https://doi.org/10.3852/10-262) | Mycologia | 2011 | DNA-based detection of the fungal pathogen Geomyces destructans in soi |
| P3 | Ranavirus (LMBV) | MCP | [10.1577/H07-009.1](https://doi.org/10.1577/H07-009.1) | Journal of Aquatic Ani | 2007 | Quantitative Polymerase Chain Reaction Assay for Largemouth Bass Virus |
| P3 | Vibrio coralliilyticus | dnaJ | [10.1371/journal.pone.0081800](https://doi.org/10.1371/journal.pone.0081800) | PLoS ONE | 2013 | An Improved Detection and Quantification Method for the Coral Pathogen |

## If you can only get a handful

Take the top of List 1. Those are correctness, not coverage: each one turns
sequences the tool is currently screening on faith into sequences checked
against their source. The single highest-value row is the first, covering ten
oligos at once.

From List 2, the three worth having first are Ghosh 2021 on Bd lineage
discrimination (it speaks directly to the estimand problem in the review doc),
Pacheco 2018 on differential amplification of avian haemosporidians (it is
evidence about four assays already held here, so it is a validation case rather
than an addition), and either Ophidiomyces paper, since snake fungal disease
has one assay here and two in routine use.
