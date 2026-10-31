# A note edit cost 444 archive rescreens; now it costs none. And the diagnosis I wrote first was wrong

2026-10-28. Yesterday's conditions curation touched 192 registry entries, and today a
report re-render turned into a screening run. I wrote down the cause — "the screen
signature hashes the whole of `registry/`" — in the roadmap, a journal and the resume
point, and committed all three. **It was wrong**, and the correction matters more than the
original claim, because the fix it implied would have been building something that already
existed.

## What was actually true

`screen_signature(taxid, group)` in the Snakefile has always hashed **only that group's
own assay files**, plus the screening code and the scoring config. Per-group invalidation
was already the design.

The "357 screen jobs" came from reading a stopped run's progress counter. After the
`retrieve` checkpoint, Snakemake re-evaluates the DAG and its `N of M steps` denominator
counts every screen job in it. Four jobs had started and each printed a changed
per-group parameter; the other 348 were indistinguishable from up to date, in a log I
killed before it could say. **That is a bad way to find out what a run will do**, so the
first thing built today was a way to ask directly: `scripts/stale_screens.py` computes
every group's signature and compares it with the `.sig` beside each cached screen.

Its answer, before any change: **182 fresh, 312 stale**, in the groups holding the 192
entries curated yesterday. So the staleness was real and the mechanism was not what I
said.

## The real defect, and its size

The signature hashed **each entry's whole YAML**. A `notes_curator` sentence, a review
flag's wording, a `conditions.annealing_c` value — none of which any screening code reads
— invalidated every group holding that entry.

`signature.screen_key` now hashes a projection: the fields a call can depend on, which are
`oligos`, `chemistry`, `amplicon_bp`, `amplicon_bp_range`, `species_sizes`, `target` and
`status`, plus review flag NAMES without their notes. Each is justified in the module by
naming its reader, because the dangerous direction here is omission: a field left out
means an edit that *does* change a call silently reuses a stale screen, which is the
failure the whole mechanism exists to prevent.

Replaying the two days of curation (`fe983b9` → HEAD) over all 125 groups:

| scheme | groups rescreened | archives |
|---|---|---|
| whole-file bytes | **108 of 125** | **444** |
| screen-relevant projection | **10** | **47** |

And the ten are the ten that should be: the four retired-taxid roots, where
`target.taxid` moved; BPSV and its two neighbour groups, which gained
`exclusivity_taxids`; the Caliciviridae group, where Hel1's flag changed from
`oligo_sequence_uncertain` to `oligos_modified`; and the orthoreovirus pair, which gained
a `conditions_not_printed` flag.

## Why flags stay in, at a cost of three archives

A flag's name is projected and its note is not, which looks inconsistent until you follow
what a flag does: `Assay.active_requires_resolved_review` refuses an `active` entry with
an OPEN flag, and an entry that fails validation is an entry that never reaches a screen.
So a flag plus a status can change what a run sees. Deciding which flags are load-bearing
in which status is exactly the reasoning that gets a cache wrong, so all flag names are
in. The measured price is the three orthoreovirus archives above.

## What it costs once

Changing `signature.py` changes the screening code hash, so **every cached screen is stale
one more time**, which is correct: the definition of the signature moved. Sunday's
scheduled run absorbs it. From then on, the curation this project has most of ahead of it
— conditions for the entries that still lack them, exclusivity claims read one paper at a
time, provenance notes — is free.

## The retraction, plainly

Three committed documents said the signature hashed the whole registry directory. They now
say what the measurement says. The mistake was reading a progress counter as a work queue
and writing the inference down as a finding in the same hour; `scripts/stale_screens.py`
exists so the question has an answer that does not require starting a run and guessing.
