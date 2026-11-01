# Development of a rapid on-site detection method for largemouth bass virus based on RPA-CRISPR/Cas12a system

<p class="aw-byline">Li · Frontiers in Microbiology · 2025</p>

<p class="aw-doi"><a href="https://doi.org/10.3389/fmicb.2025.1599006">doi:10.3389/fmicb.2025.1599006</a></p>

??? quote "Full citation"
    Li, N. et al. Development of a rapid on-site detection method for largemouth bass virus based on RPA-CRISPR/Cas12a system. Frontiers in Microbiology 16, 1599006 (2025).

<p class="aw-assay-line"><span class="aw-chip aw-chip-none">status withheld</span> <span class="aw-id">LMBV_dsDNA_MCP_RPA_Li_2025</span></p>

**LARGEMOUTH BASS VIRUS / Santee-Cooper ranavirus (dsDNA) — MCP, RPA F1/R1 (Li 2025)**

| | |
|---|---|
| Target | Ranavirus micropterus1 (Santee-Cooper ranavirus) (<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10492">taxid 10492</a>) |
| Gene | MCP |
| Chemistry | rpa |
| Amplicon | 127 bp |
| Registry status | active |

## Oligos

| role | name | sequence (5'→3') | length |
|---|---|---|---|
| forward | MCP-F1 | `GTTCATTGATCTCGCCACTTATGACAGCCT` | 30 nt |
| reverse | MCP-R1 | `TGTGGCAGCCGTAGGCAGTTTGGTAAACCA` | 30 nt |

!!! warning "No status is reported for this assay"

    A property of this entry would render a predicted-detection figure
    misleading: a chemistry this scoring does not model, or a readout other
    than amplification. The sequences were screened and still appear in the
    tables below that do not depend on a verdict. The verdict is withheld
    deliberately, rather than presented with a caveat attached.

    - **`not_screenable`** — the chemistry is RPA; the penalties are calibrated on PCR


## Scope

This entry declares no scope restriction, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower range than its taxid covers, that presents as low coverage rather than drift; see [scope and retrieval](../scoping.md).

Retrieval query:

```
txid3432136[Organism:exp] OR txid2487147[Organism:exp] OR txid3045952[Organism:exp] OR txid3691958[Organism:exp] OR txid3042780[Organism:exp] OR txid3045951[Organism:exp] OR txid2951525[Organism:exp]
```

A retrieval query is a claim about the population against which the assay is evaluated, and it can cease to be accurate without producing an error; see [scope and retrieval](../scoping.md).

Disclosures on this entry: `not_screenable`.


## Curation record

Added 2026-10-04 to cover the Santee-Cooper group, which no other assay in this registry reaches and which is what both MCP assays here trip over (RANAVIRUS_dsDNA_Major_capsid_protein_MCP_Johnson_2008 and RANAVIRUS_dsDNA_Major_capsid_protein_MCP_Pallister_2007). 

<details class="aw-curation"><summary>The full note, as the curator wrote it · in the order the curator wrote it, oldest first</summary><p><b>2026-10-04</b> Added 2026-10-04 to cover the Santee-Cooper group, which no other assay in this registry reaches and which is what both MCP assays here trip over (RANAVIRUS_dsDNA_Major_capsid_protein_MCP_Johnson_2008 and RANAVIRUS_dsDNA_Major_capsid_protein_MCP_Pallister_2007). CHEMISTRY. This is RPA, not PCR: the primers are the RPA pair F1/R1 of Li et al. 2025, chosen in that paper over two other candidate pairs by amplification efficiency, and used ahead of a CRISPR/Cas12a readout. They are recorded here because the question this tool asks - do these primer sequences still match what is being deposited - is worth asking of any published oligo. But the penalty weights in config.yaml are calibrated on PCR, so a `reduced` or `fail` call here should be read as `these sequences have diverged`, not as a prediction about an RPA reaction at 39 C. SEQUENCES were read from the open-access full text (Front Microbiol, CC-BY), Table 2, rows F1 and R1, not from a secondary list. VERIFIED against real records before the entry was trusted: both primers match with zero mismatches in 4 of 4 LMBV complete genomes tested (PX879566.1, PV833272.1, PX463212.1, PV459226.1), on the plus strand in three and the minus strand in one, giving a 127 bp product every time. amplicon_bp is therefore measured on real sequence rather than quoted or computed; the paper gives no product size. Those four accessions are themselves among the records the two MCP assays fail, so this entry covers exactly the observed gap.</p><p><b>2026-10-04</b> RETRIEVAL SCOPE is deliberately not a bare taxid. The formal ICTV species is Ranavirus micropterus1 (txid3432136, the old name Santee-Cooper ranavirus survives as a no-rank node inside it, alongside Largemouth bass virus, Smallmouth bass virus, Doctor fish virus, Guppy virus 6 and Guppyfish iridovirus). But Mandarin fish ranavirus (txid2487147) and Siniperca chuatsi ranavirus (txid3045952) are phylogenetically allied and sit in NCBI's `unclassified Ranavirus`, so a scope of txid3432136 alone would silently miss them: 113 records, against 131 for the union used here. The query is a positive union rather than an exclusion, which also sidesteps the leading-NOT trap documented in docs/journal/2026-10-04-assay-investigations.md.</p><p>THE SCOPE WAS SET EMPIRICALLY, AND THAT IS THE PROCEDURE TO REPEAT. The first draft of this query listed only micropterus1 plus the Mandarin fish and Siniperca chuatsi taxids. Screening the assay against the whole genus archive then showed it also detects four records the query would have excluded, all of them sitting in `unclassified Ranavirus`: Macropharyngodon choati ranavirus (txid3691958, PX883867), Halichoeres melanurus ranavirus (txid2951525, ON595973, a MAG), Hybrid snakehead ranavirus (txid3042780, OP628213) and Micropterus salmoides ranavirus (txid3045951, OQ267587). Those are now included. The lesson generalises: for a lineage whose members keep arriving unclassified, the defensible way to set a scope is to screen the parent taxon and look at what is actually detected outside the proposed boundary, not to trust the taxonomy to be current. Re-run that check when NCBI reclassifies, and recount.</p><p>HOST RANGE is worth knowing when reading a result, because it is not what the name suggests. Besides largemouth and smallmouth bass, this group includes isolates from doctor fish (Garra rufa, the pedicure fish), guppy, and - from the empirical check above - two traded marine wrasses, Macropharyngodon choati and Halichoeres melanurus.</p><p>A North American freshwater bass virus and an Indo-Pacific reef wrasse virus are not plausibly linked by geography or host phylogeny, so the ornamental fish trade is the obvious connection. Deposits here are therefore a sample of trade and of sequencing effort, not of any one watershed, which is worth remembering before reading a detected share as epidemiology.</p><p><b>2026-10-05</b> VERIFIED AGAINST THE PAPER, 2026-10-05, by the new scripts/fetch_europepmc_fulltext.py: all four oligos read exact against the paper's own open-access full text, which was recovered from Europe PMC and saved as papers/10.3389_fmicb.2025.1599006.txt.</p></details>

## Corrections

If this entry misrepresents the assay, that is a defect and a report is
welcome — particularly from the group that designed it. The sequences,
the product size and the scope are all curated from the paper and can be
wrong.

<div class="aw-contribute" markdown="0">
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/issues/new?title=LMBV_dsDNA_MCP_RPA_Li_2025%3A%20&body=Entry%3A%20LMBV_dsDNA_MCP_RPA_Li_2025%0APage%3A%20https%3A//batyanight.github.io/assaywatch/assays/LMBV_dsDNA_MCP_RPA_Li_2025/%0ARun%3A%202026-10-31%0A%0AWhat%20is%20wrong%2C%20and%20what%20it%20should%20be%3A%0A%0A"><b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry and run. A sentence is enough.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/edit/main/registry/LMBV_dsDNA_MCP_RPA_Li_2025.yaml"><b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving offers to open a pull request for you.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/blob/main/registry/LMBV_dsDNA_MCP_RPA_Li_2025.yaml"><b>Read the entry</b><span>The file behind this page, with every field and the curator's note.</span></a>
</div>

Contributing an assay is documented in [CONTRIBUTING.md](https://github.com/batyanight/assaywatch/blob/main/CONTRIBUTING.md).

