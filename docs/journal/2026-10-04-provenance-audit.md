# Provenance audit: does each citation design its oligos?

2026-10-04. Prompted by the ranavirus scoping error earlier the same day.

## The failure being audited for

`RANAVIRUS_dsDNA_Major_capsid_protein_MCP_Johnson_2008` was scoped away from the
fish ranaviruses because Johnson et al. 2008 is a box-turtle and tortoise study.
Its oligos turn out to be byte-identical to FV3-54F / FV3-584R of Mao et al.
1997, which Grizzle et al. 2003 reports amplifying every ranavirus tested, fish
included. The `citation` field recorded where the sequences were **read from**;
an assay's scope follows from where they were **designed**.

This is a population-level risk, not one bad row: **138 of 151 entries** were
transcribed from a single lab spreadsheet, and a lab spreadsheet lists a primer
beside whoever the lab got it from.

## The structural fix

`citation.oligos_designed_here: bool | None`, defaulting to **None**. An
unexamined entry must read as unknown rather than as vouched for, which is why
it is nullable rather than defaulting to True.

- `True` — the cited paper designed them; its claims bound the scope.
- `False` — the paper used someone else's; find the design paper before scoping.
- `None` — not established. 93 entries are here, honestly.

## The repeatable check

`scripts/audit_provenance.py`, because a one-off audit decays. It exploits the
fact that **oligo names usually carry the design lab's convention**: `RanaFWD`
sat under Johnson 2008 while the same sequences are Mao's `FV3-54F`; `HahnF2`
sits under Takehisa 2009.

    151 entries audited

        4  name-vs-author     a surname-shaped token that is not the cited author
       10  modified           name says mod/new/corrected: sequence may not be the published one
       33  no-citation        no reference and no DOI; cannot be scope-checked at all
        6  id-mismatch        the id's Author_Year disagrees with the citation
       14  lab-designed       TS prefix, the spreadsheet's in-house convention
       93  unestablished      oligos_designed_here still null

      129 of 151 entries carry at least one flag

It proposes and never edits. The first run returned 10 `name-vs-author` rows, of
which **6 were false positives** — `Fouter` is "F-outer", `Pythin` a typo for
Python, `Matrix` the influenza gene. Those are suppressed as data rather than by
tightening the regex, because a pattern loose enough to catch `Hahn` and
`Rebelo` is worth a short exclusion list.

## Resolved

**The two flavivirus NS5 entries are composites.** The lab encoded the
provenance in the names and deserves credit for it: `-Zino-` is Scaramozzino,
`-GORO-` is **Goro Kuno**. cFD2 is conventionally Kuno et al. 1998, *J Virol*
72:73-83 (DOI verified: "Phylogeny of the Genus *Flavivirus*", Kuno, Chang,
Tsuchiya, Karabatsos, Cropp). Scaramozzino et al. 2001 contributed MAMD and
FS778 — and its own title, "**Comparison** of Flavivirus Universal Primer Pairs
and Development of a Rapid, Highly Sensitive Heminested RT-PCR Assay", is
evidence it evaluated pre-existing pairs rather than designing them all. Set
`False`, flagged `OLIGOS_FROM_TWO_PAPERS`. Not yet confirmed from Kuno 1998's
own methods; that is what would close it.

**Two mycoplasma entries had no citation but are half Rebelo 2011** — resolved
from sequence evidence alone, no paper required. `16-23 F1 (Rebelo F)` is
byte-identical to `RebeloF` in the sibling entry that does carry
doi:10.1177/1040638711416846 (verified: Rebelo, Parker & Cai, *J Vet Diagn
Invest* 23:932-936), and `16-23 R3 (Rebelo R)` likewise matches `RebeloR`. So
three entries share Rebelo oligos and only one named the paper. Both now cite
it, set `False`, flagged `PARTNER_PRIMER_UNATTRIBUTED`, since each pairs one
Rebelo primer with a partner the spreadsheet does not attribute.

**`Lancotti` → `Lanciotti`.** A real person's name misspelled in a user-facing
id. Renamed, with `docs/validation-cases.tsv` and `scripts/curation.yaml`
updated.

**Eight entries set `True`** — the six Briese, Grizzle and Li entries whose
papers were read directly this session. **Johnson 2008 set `False`**, the case
that started this.

## Open, and what each needs

| entry | problem | what would close it |
|---|---|---|
| `RETROVIRUS_RNA_polymerase_SIV_Takehisa_2009` | oligos named `HahnF2`/`HahnR2`; Takehisa 2009 may be a user | Takehisa 2009 methods. PMC2643789 holds abstract only — **PDF needed** |
| `RETROVIRUS_RNA_polymerase_SIV_3` | `HahnF1`/`HahnR1`, no citation at all | same paper |
| `Morbillivirus_including_CDV_P_gene` | oligos named `Grosh F`/`Grosh R` under a Barrett citation; "Grosh" is nobody in that author list | identify Grosh; possibly a lab member rather than a publication |
| `Morbillivirus_including_CDV_P_gene_Barrett_2003` | id says 2003, `design_year` 1993 | decide which is the real paper |
| 4 `modified` entries with a DOI attached | `ARS7C-MOD`, `Ziao18SR1 corrected`, `GEI18SF Mod`, `MOD-FWD`/`MOD-RVS` — the DOI asserts a sequence the paper never printed | each paper's primer table, to recover the unmodified sequence and record the modification as a modification |
| `Snake_arenavirus_..._Nachweis_2015` | reference is a German title, so no author is readable | the paper |
| 33 `no-citation` entries | mostly honest "unpublished" | nothing — but they can never be scope-checked, which is worth stating in the paper |

The four `modified`-plus-DOI entries are **worse than the Johnson case**: there
the citation pointed at the wrong paper, but the sequence was at least somebody's
published oligo. Here the stored sequence may be one no paper ever printed, while
a DOI implies otherwise.

## What generalises

Three scoping bugs were found today and all three were silent: untagged Entrez
fields searching every column, a leading `NOT` that Entrez evaporates, and a
taxonomy that lags the data. This is a fourth of the same character — a field
that looked populated and correct and was answering a different question than
the one the code asked of it. The common defence is cheap and boring: **count
or compare before and after, and make the tool say which question it answered.**
