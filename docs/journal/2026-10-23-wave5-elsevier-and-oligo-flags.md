# Elsevier full text, and what the oligo flags actually mean

Session of 2026-10-23, continuing the plan of attack. Three things settled: the
Elsevier full-text block is open, the largest cluster in the oligo verification
report is a matcher artifact rather than a data error, and the literature sweep
gained one verified candidate while a second lead collapsed.

Nothing in `registry/` was changed. `scripts/verify_oligos_against_paper.py` was
not changed either, though it should be; see "The `alternates` false-positive
class" below.

## The Elsevier institutional token

The 403 recorded in the fetch script's docstring was an entitlement problem and
not an IP problem, exactly as the docstring predicted. The institutional token
is now at `.secrets/elsevier.insttoken` (32 bytes, `chmod 600`). `.gitignore:25`
covers `.secrets/`, confirmed with `git check-ignore`.

Entitlement test on a single DOI, `10.1016/j.vetmic.2012.07.030`, returned a
227 KB body rather than the metadata-only envelope the script warns about, so
the entitlement is real full text.

The batch run then fetched 10 of 10 outstanding Elsevier DOIs:

    10.1016/s0166-0934(01)00306-8    126 KB
    10.1016/s0168-1702(97)01458-5     93 KB
    10.1016/0166-0934(94)90098-1      92 KB
    10.1016/s0166-0934(99)00088-9    164 KB
    10.1016/0168-1605(91)90148-i     122 KB
    10.1016/s0016-5085(98)70589-x    267 KB
    10.1016/s0166-0934(96)02155-6     64 KB
    10.1016/s0168-1702(00)00252-5    118 KB
    10.1016/s0168-1702(99)00059-3    124 KB
    10.1016/0890-8508(92)90002-f     165 KB

Effect on verification coverage: oligos that cannot be checked against a source
fell from 106 to 38 (13 `no-oligos`, 25 `no-doi`). 466 of 504 oligos are now
checkable and 393 agree with their paper, 84%. That is more than the 42 oligos
the Elsevier block was documented to carry.

### Both steps must run on the host

Neither step works from a cloud container:

- `api.elsevier.com` is not on the container proxy's allowlist. The batch run
  returned `URLError` for all 10 DOIs without reaching the API. No quota was
  consumed.
- `verify_oligos_against_paper.py` imports `StrEnum` via `assaywatch/schema.py`,
  which needs Python 3.11+. A container on 3.10 fails at import.

`api.crossref.org` is also blocked from the container (403 at the proxy tunnel).
The PubMed MCP route works and is what every identifier in this document was
verified against.

## The `alternates` false-positive class

The verification report flagged 21 probable transcription errors. Four of them
are the matcher comparing an oligo to another oligo in the same registry entry.

Every flagged `arctic` oligo in the `CDV_H_gene_Mueller_2011_*` entries is being
matched against that entry's own primary primer:

| flagged oligo | stored sequence | reported as "the paper's" | which is actually |
|---|---|---|---|
| `2Farctic` | GTGAGACAATTGGGATCAGA | GCGATACAATTGGGATCAGA | `Mueller-2F` |
| `2Rarctic` | TGGGTGAGCGACAGGTGTCA | TGGGTGAGCAACAGGTATCA | `Mueller-2R` |
| `3Farctic` | TGGGAATCTTTGGGGCAACA | TAGGGATATTTGGGGCAACA | `Mueller-3F` |
| `4Farctic` | ATCCCTCATGTGTTATCATT | ATCCCCCATGTGTTGACATT | `Mueller-4F` |

The reported edit distances (2, 2, 3, 3) are the designed divergence between
each arctic-lineage variant and its canonical counterpart. The registry is
correct here, and `CDV_H_gene_Mueller_2011_2.yaml` already records as much:
"all four Mueller_2011 entries' primer pairs verify exact against that PDF",
resolved 2026-10-22 against `10.7589/0090-3558-47.3.725`.

The cause is that `check()` searches for the nearest printed run to a given
sequence and has no notion that an `alternates` member is a deliberate variant.
The nearest printed run to any lineage variant is, predictably, the primer it
was derived from.

**The fix belongs in the script, not the registry.** When an oligo's nearest
match in the paper is another oligo within the same entry, that is a sibling
relationship and should be reported as such, or suppressed, rather than printed
as "paper prints X". Until then, every lineage variant added to an `alternates`
block will generate a spurious `near:` flag, and the 84% agreement figure is
understated by however many such variants the registry holds.

## `Mod` oligos are a different category

`GPO-1FMod` (`Pan_mycoplasma_16S_All_Van_1992.yaml:11`) and `ARS7C-MOD`
(`ARENAVIRUS_ssRNA_S_gene_2.yaml:15`) sit in primary oligo slots, not in
`alternates`. They are deliberate modifications of a published sequence, which
the verification script's own closing note anticipates.

These want a provenance field recording the modification. Applying "the paper
wins" to them would overwrite the record of an intentional change with the
unmodified published sequence, which is the opposite of what the entry means.

## 15 candidate genuine errors remain

Removing the 4 `arctic` and 2 `Mod` flags leaves 15. Ranked by how much the
evidence supports a real error:

**Internal evidence, by the script's own rule.** `CoV-RVS1`
(`CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme_L`) is 3 edits away with 3 bases
*inside* the run that the stored sequence lacks. End-position differences can be
extraction glue; interior differences cannot.

**Coronaviridae RdRp cluster.** `CoV-FWD3` and `CoV-RVS3` are 4 edits each with
no length discrepancy, the highest distances in the report, and together with
`CoV-RVS1` they make three flagged oligos from one assay family.

**Most consequential by reuse.** `AIMatrixF`
(`INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2`) is 2 edits with only 1 extra
base at the 3' end, so at least one edit is interior. Matrix-gene assays are
among the most reused in the registry.

**Both primers of one pair.** `Entamoeba_18S_small_subunit_SSU_2014` has
`GEI18SF` at 3 edits and `GEI18SR` at 2.

**Pure interior mismatches, no length discrepancy.** `AstrRVS1` (2),
`Borna-NF` (2), `Flavi-FWD` (2), `Xiao18SR1` (3).

**Probably extraction artifacts.** `4125-as` (`CMV_UL55_gB_Deckers_2009_round2`)
reports a printed run ending `...AGCMVGB` — the assay name glued on by the
extractor — with 2 extra bases at the 5' end and 5 at the 3'. `BornaPCA6`
appears in three `ORTHOBORNAVIRUS_XP_*` entries at `near:1` with 3 extra bases
at the 5' end only. `HaemR2` is 3 edits with 2 extra bases at the 3' end.

## Unexamined: the 32 `absent` oligos

The report counts 32 `absent` but does not enumerate them. `absent` means the
sequence is not in the attached paper at all, which is a worse class of problem
than a near-miss: either the wrong paper is attached to the entry, or the
sequence has no published source. Worth enumerating before acting on any of the
15 near-misses above.

## Literature sweep

Aimed at the two gaps: held-out validation cases, and within-family negatives
for the C2 bench corpus. Every identifier below was verified against PubMed.

### Verified addition: Slomka et al. 2012

*Avian Pathology* 41(2):177-193, `10.1080/03079457.2012.656578`, PMID 22515536.
Found as reference 23 of `10.1371/journal.pone.0244669`, then verified directly
rather than trusted from the citing paper's reference list.

Measured: five Eurasian RRT-PCR methods on 282 clinical specimens from 46
chickens and 48 ducks across four Vietnamese premises, **sampled 2009**, carrying
H5N1 HPAI clades 2.3.2 and 2.3.4. The H5 cleavage-site RRT-PCR was "effective
for clade 2.3.4 detection, but severely compromised for clade 2.3.2". The H5 HA2
RRT-PCR detected both clades sensitively. A new lyophilised M-gene method and the
validated H5 HA2 showed similar high sensitivity by Bayesian modelling, both
above the validated "wet" M-gene method.

Stated carefully: reduced sensitivity of the H5 CS and "wet" M-gene assays
**correlated with** target/primer/probe mismatches. The authors associated the
two; they did not demonstrate causation by substituting homologous oligos, which
is what Klungthong et al. did. Label it as correlation or the case overstates
itself.

Value: plausibly a `fails`, a `partial`, and two or three `works` rows off a
single 2009 `as_of`, plus a 5-assay by 2-clade per-clade table for the C2 corpus.

### Collapsed lead: Sreedharan et al. 2023

*Transboundary and Emerging Diseases* 2023:9980566, `10.1155/2023/9980566`.

Its abstract's claim that existing assays miss Korean, Chinese, Indian, Japanese
and Brazilian Bd haplotypes is a **citation to other work**, confirmed from the
full text, not this paper's measurement. The sentence attributing insertion-
deletion and substitution in the probe-binding and reverse-primer-binding sites
likewise cites another paper. PMC's full text strips reference numbers and omits
the reference list entirely, so **that reference is unidentified**; it needs the
publisher's bibliography. Do not cite Sreedharan for the Boyle mismatch finding.

What the paper does measure, against Boyle's TaqMan on Australian and Panamanian
GPL material: sensitivity 0.89 (95% CI 0.73-0.96), specificity 0.92 (0.74-0.99),
accuracy 0.90, and ΔCq 5.71 ± 3.00 in favour of the new primers. On the Panama
samples both assays "resulted in the same identities of samples as positives",
so this is a **`works`** case for Boyle's assay on GPL, not a failure.

Their in-silico screen of 40 isolates across four lineages checked **their own**
primers for mismatches, not Boyle's. The per-lineage Boyle mismatch table this
paper appeared to offer does not exist in it.

The dramatic figure belongs to a different assay: on the same 137 Indian
samples, nested PCR gave 1.4% prevalence (95% CI 0.1-5.4) against 70.9%
(64.5-76.7) for the new assay. That indicts nested PCR, not Boyle's.

Mechanism is `coverage` regardless — the paper states the Asian lineages are
enzootic and geographically restricted, so they are long-present rather than
newly emerged. It therefore adds to the ten coverage cases already held and does
nothing for the drift gap.

`as_of` material: Indian anuran swabs 2014-2016 (n=137) and 2018-2021 (n=90),
caecilians 2021-03-05, salamanders 2020-12. Australia n=60 and Panama n=43 are
undated in the text.

### Candidates with verified identifiers, not yet assessed

| reference | DOI | what it measures |
|---|---|---|
| Yang et al. 2013, J Clin Microbiol 52(1):76-82 | `10.1128/JCM.02467-13` | Some H1N1pdm09/H3N2 variants **not detected** by a common M-gene RT-PCR; newly emerging G225A, T228C, G238A and C163T in primer/probe regions atop C154T, C153T, G189T. Taiwan, 2012-2013 |
| Stellrecht et al. 2017, J Clin Virol 93:25-29 | `10.1016/j.jcv.2017.05.016` | Per-strain LOD elevation on A/Texas/50/2012-like and A/Switzerland/9715293/2013-like; assay sensitivities 100 / 96.7 / 91.8 / 85.2 / 75.6%. Commercial, proprietary targets — may not map to published registry entries |
| Klungthong et al. 2010, J Clin Virol 48(2):91-95 | `10.1016/j.jcv.2010.03.012` | WHO swH1 set: single mismatch at the 3rd base of the probe reduced sensitivity in 23/37 viruses; homologous oligos recovered ΔCq 4.66, P<0.0001 |
| Geiselhardt et al. 2022, J Clin Microbiol 60(5):e0250521 | `10.1128/jcm.02505-21` | Two previously published CDV RT-qPCRs less sensitive on genotype Asia-4, which varies in primer and probe binding sites |
| Becker et al. 2023, J Virol Methods 323:114853 | `10.1016/j.jviromet.2023.114853` | PP-I forward fully matched 29/194 genomes (15%), reverse 18/194 (9%); failed 9/28 clinical positives (32%). LOD equivalent to the new set, so the failure is sequence-driven and not sensitivity-driven |
| Stilwell et al. 2018, Dis Aquat Organ 128(2):105-116 | `10.3354/dao03214` | 33 ranavirus isolates amplified across fish, amphibian and reptile hosts; **did not amplify highly divergent ranaviruses**. Excluded as a case row (new assay on its own panel) but prime per-type table data |

Klungthong's ΔCq 4.66 and Sreedharan's ΔCq 5.71 ± 3.00 are arguably worth more
to the amplification model's priors than to the case set.

### A definitional seam to settle first

The tool replays history by **deposition** date. A lineage that existed but was
unsequenced is invisible at design time, so a case can read as `drift` under the
operational definition and `coverage` under the biological one. Geiselhardt's
Asia-4 is the clean instance: the lineage may well predate the assays it breaks,
but its sequences do not. This needs deciding before such cases enter the
held-out set, because whichever definition is chosen is the one the drift flag
inherits.

### Taxonomic concentration risk

SARS-CoV-2 could supply all five required drift cases by itself — S-gene target
failure from the Alpha deletion is the best-dated diagnostic drift event there
is. A held-out set whose drift cases are mostly one taxon would validate the
drift flag only on coronaviruses. Worth capping how many come from one taxon.

### Unsearched, highest expected yield

All in the registry's taxa scope, none verified:

- **Orthopoxvirus / MPXV.** The 2022 clade IIb outbreak strain is reported to
  carry a deletion affecting the target of a widely used generic assay.
  Emergence is dated to within days, which makes the cleanest possible `as_of`.
- **Coronaviridae / SARS-CoV-2.** Large literature of primer-region mutation
  surveys with precise dates. Subject to the concentration cap above.
- **Filoviridae / Ebola.** Published filovirus assays reported to underperform
  on the 2014 Makona variant, with well-documented sampling windows.

## Method notes

- Every `as_of` in the candidate table is provisional. Sampling-end dates live
  in methods sections, not abstracts. Substituting a publication date leaks the
  future into the replay and silently makes the case easier than reality.
- A literal `grep` for a sequence the report quotes as "paper prints" finds
  nothing. The script normalises before matching, because XML table cells split
  runs. Do not use grep to audit these flags.
- PMC blocked direct web fetch with a CAPTCHA. The PubMed full-text route works
  but strips reference numbers and the reference list, so it cannot resolve a
  numbered citation.
