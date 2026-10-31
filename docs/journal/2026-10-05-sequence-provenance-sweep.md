# Finding a primer's real paper by searching its sequence

2026-10-05. Europe PMC indexes full text, so a primer sequence in quotes is a
search for every open-access paper that prints it. That one move settled six
entries whose provenance had been open for two days, and it should be the first
thing tried on any `DOI_MISSING` or "not in the cited paper" entry.

    https://www.ebi.ac.uk/europepmc/webservices/rest/search?query="<SEQUENCE>"&format=json

Run over every oligo not yet confirmed against its own paper - 275 queries
across 137 oligos, each sequence and its reverse complement, degenerate ones
reduced to their longest unambiguous run - it returned hits for 77.

## What it settled

| entry | was | now |
|---|---|---|
| `CMV_..._gB`, `..._round2_2` | cited Prepens 2007, primers absent from it | Deckers 2009 Virol J 6:210, set CMV-gBp1 |
| `ADENOVIRUS_..._Primate_speci` + `..._Casas_2005` | cited Casas 2005, primers absent from it | Roy 2009 PLoS Pathog 5:e1000503, nested pol PCR |
| `POXVIRUSES_..._Polymerase_short_2` | "unpublished" | McAloose 2016 Dis Aquat Organ 119:17, via Vila 2019 |
| `Helicobacter_XREACTS_with_general_bac_2` | no citation at all | Conley 2021 PLoS One 16:e0247010 |
| `PARVOVIRUS_..._dependovirus` | no citation; sibling cited Gao 2002 | Gao 2002 PNAS 99:11854 |
| `E_coli_O157_H7_hlyA_..._Wang_1997` | "Wang et al 1997 — not resolved" | Wang 1997 J Appl Microbiol 83:727 |

Five amplicons were measured against real records in the course of it and four
were wrong: adenovirus inner 281 -> 258, outer 1560 -> 1512, AAV null -> 255 and
316 -> 255, CMV 4125 550 -> 599.

## How to read a hit

A hit is a lead, not an answer. Three kinds come back, and only the first is a
citation:

1. **The paper that designed it.** Says so, usually in the Methods, and prints
   no citation of its own for that primer. Conley 2021: "we developed a Taqman
   qPCR assay specific for *Helicobacter* sp. Grand Cayman Blue Iguana 1".
2. **A paper that reuses it and cites the source.** The useful ones: Vila 2019's
   Table 1 prints all six TSPoxPol oligos and credits McAloose 2016, which is
   how an entry marked unpublished turned out to be published. Shija 2026 did
   the same for Wang 1997.
3. **A paper that reuses it and cites nothing**, or cites something that does
   not print it. Worth nothing on its own.

So: take the earliest hit, read the sentence or table row the sequence sits in,
follow the reference attached to that row, and stop when a paper either claims
the design or cites one that does. The query is at the top of this file;
the reader used here was a throwaway.

## What it did not settle

- **Müller 2011 CDV**, the four H-gene walking-primer entries. None of 1F, 1R,
  2F, 2R, 3F, 4F or their complements is in any open full text. The one hit, on
  `3R`, is Riley 2015's F8/R8 pair sharing a single primer, which is not the
  walking set. Still needs the paper or the original records.
- **Entries whose hits are all downstream.** `Pan_hemoparasite ... Hellgren_2004`
  returns 43 papers using HaemNR3 and none that designed it; that entry's
  composite-scope question is unchanged.
- **Cross-reaction claims.** Conley 2021 designs its probe on a 14 bp insertion
  unique to one provisional *Helicobacter* species, while the entry targets the
  whole genus. The sheet's "XREACTS with general bac" is lab experience the
  paper does not report, and the entry now says so.

## A thing worth knowing about reverse primers

`PARVOVIRUS_..._dependovirus` stores its reverse primer as the reverse
complement of what Gao 2002 prints, and the verifier's `revcomp` verdict calls
that normal. It is - but which of the two strings is the oligo still matters.
Measured, 19s pairs with the stored form in 1,345 records and with Gao's printed
form in none, because the printed one is the sense strand of the same site. The
oligo name already said "(corrected)". Measure, do not assume the paper's string
is the one to order.
