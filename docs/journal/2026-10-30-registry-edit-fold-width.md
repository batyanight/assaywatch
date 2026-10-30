# `registry.edit()` folds at the width entries are written at

2026-10-30. Closes the Hygiene item opened earlier the same day, when a prose edit to
`CALICIVIRUS_ssRNA_Helicase_Reid_1999` came back as one line and had to be reverted.

## The bug

`registry.write()` (new entries, PyYAML) folds long scalars at `_WIDTH = 120`. Every
entry in `registry/` is written that way, which is why a curator note sits as a quoted
scalar wrapped at roughly 120 characters with a four-space continuation indent.

`registry.edit()` (changes to existing entries, ruamel round-trip) set

    rt.width = 1_000_000

deliberately, on the reasoning that re-folding would turn a one-line note into eight
lines of diff. The reasoning was backwards: nothing in `registry/` holds a one-line long
note, because `write()` folded them all. What an effectively infinite width does is
*unfold* — the Reid note came back as a single 2,893-character line, so a two-word
change to a note produced a diff of the whole note and lost the house format for good.

## The fix

`rt.width = _WIDTH`. One line, plus a comment that now records why rather than the
opposite. The regression test is a round trip of the plain fixture, which already
carries a folded note: an edit may not widen the file, the note must read back character
for character, and a second edit must leave the file byte-identical apart from the key
it changed.

## Measured on the real registry

A no-op `edit(path, {})` over a scratch copy of all 214 entries:

| | |
|---|---|
| Entries whose formatting changes on their first edit | **192 of 214** (5,005 lines) |
| Entries whose *content* changes | **0** |
| Entries that change again on a second edit | **0** |
| Entries where the widest line grows | 8 |

So the reformat is semantically empty and is paid once per entry. ruamel chooses slightly
different break points from PyYAML, and in eight entries declines a break PyYAML took,
leaving a few lines between 127 and 169 characters — the worst is a note containing the
56-character entry id `ORTHOREOVIRUS_dsRNA_RNA_polymerase_Landolfi_2010_round1`. That is
cosmetic and stable, and it replaces a failure mode that unfolded notes to thousands of
characters.

No rescreen: `signature.screen_key` hashes the screen-relevant projection, and formatting
is not in it (`docs/journal/2026-10-28-screen-signature-projection.md`).

## What this unblocks

Prose edits on entries with wrapped notes can go through `registry.edit()` again instead
of being hand-applied as text edits, which is what the curation chain and every script
that records a finding into `source.notes_curator` use.
