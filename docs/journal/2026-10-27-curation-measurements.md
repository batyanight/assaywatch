# Three curation items measured rather than argued, and one plan assumption refuted

2026-10-27. The roadmap's curation section is mostly reading papers. Three of its items
turned out to have a measurement in them, and one turned out to rest on a wrong premise.

## `orientation_inferred`: the archive confirms 26 of 28

The flag says which oligo is forward and which reverse was read off coordinates or
labels, not stated by the source. It is the largest `needs_review` class (28 entries).
The screen settles the question every time it finds an amplicon: `score.py` draws both
orientations on the plus strand, and a product only forms when a plus-strand site runs
rightwards to a minus-strand site. A pair stored the wrong way round faces outward and
yields nothing in any record.

    python scripts/check_orientation.py --calls results/2026-10-26/calls.tsv.gz

26 of 28 flagged entries produce ≥ 20 amplicons under the stored orientation — from 20
(`Pan_reptilian_paramyxovirus_L_Ahne_1999`) to 16,410 (`PAPILLOMAVIRUS_dsDNA_L1_gene_Forslund_1999`).
**None produces zero.** Two produce 2 each, both Sunshinevirus RdRp pairs on 8 records,
which is too few to say anything either way. So the inference stands for 26, on the
archive's evidence.

**The flag is not removed by this.** It records provenance — the source did not state
the orientation — and that stays true, the way `oligos_modified` stays true. What
changes is that each flag can now carry a `note` with the number, so a reader sees
"inferred, and the archive yields 740 products under it" rather than "inferred" alone.
That edit is to 26 registry files and waits for the live run to finish, because the
screen signature hashes the registry.

## The 20 `in-text` oligos, enumerated

`docs/2026-10-27-in-text-oligos.tsv`. The verifier reads `in-text` when the stored
sequence occurs in the paper's text but in no oligo table the extractor could parse. 505
oligos checked against the 189 papers on disk: 421 `exact`, 22 `absent`, **20
`in-text`**, 16 `modified`, 13 `no-oligos`, 6 `near`, 4 `sibling`, 3 `revcomp`. The 20
span 12 entries — the Ghosh 2021 Bd lineage pairs, the Haynes 2023 Ophidiomyces trio,
Sethabutr's Shigella pair, both adenovirus pan-polymerase outers — and in every case the
string *is* in the paper; what is missing is the extractor recognising the table it sits
in. Each needs one human read of one page. None changes a sequence.

## The Hantavirus `pending/` entries: the plan was wrong about them

The plan proposed citing Aitichou 2005 with `oligos_modified` for the four Hantavirus
S-segment entries, on the strength of their curator note finding Aitichou as the
ancestor. Reading the note to the end: Aitichou prints HANTAV1U/L, the ancestors of
**UHantaF1/R1 — and that pair is already live in `registry/`**, citing Anthony 2013,
which prints it character for character. The three *pending* entries are the other
nests — F2/R2, F3/R3 and F4/R3 — and nothing on disk prints them: not Anthony, not
Aitichou, not the PREDICT protocol document they came from. Their nesting was read off
amplicon geometry and one shared reverse primer, and their own note says to re-check
that first if a source ever appears. They stay pending, correctly, and the roadmap now
says why.

## The bee-virus names and the genus-level taxids

`check_taxids.py` has reported 11 `taxon_name` mismatches since the ICTV binomial
renames, and nobody had run it since 2026-10-04. Three are a name the paper used against
the name NCBI now uses (ABPV → *Aparavirus apisacutum*, BQCV → *Triatovirus
nigereginacellulae*, SBV → *Iflavirus sacbroodi*): a name-only edit in the house pattern
(NCBI name, paper's name in parentheses), no retrieval effect, and it too waits for the
run. Eight are a species-level name on a deliberate genus-level taxid narrowed by
query — LMBV on *Ranavirus*, seven EEHV entries on *Proboscivirus* — which is a design,
not an error, and the script needs a status that reads the `query` before it can say so.
