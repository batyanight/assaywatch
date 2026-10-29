# The to-do list was three days behind the repo: six items closed by reading the files, none by doing work

2026-10-30. `ROADMAP.md` is the one to-do list, and the rule is that finishing an item
means ticking it there. On the architecture day eleven PRs landed in one session and the
ticks did not all follow, so the first job of the next session was to compare every open
line against what the repository actually holds. No code, no registry field and no
number changed; this entry records what was already true.

## What was open on paper and closed in fact

| Roadmap line | What the repo showed | Closed how |
|---|---|---|
| Architecture step 1, Glossary: "left to do: commit on branch `glossary`" | Branch merged into `main` at 3928be8; `CLAUDE.md` already points at `GLOSSARY.md` | ticked |
| Architecture step 5 parent, unticked | 5a to 5g each ticked (5g by deciding not to) | ticked |
| "18 entries carry a taxid NCBI has merged away ... do it as its own live run" | `rg -l 'TAXID RETIRED' registry/` finds 18; `data/retrieved/` moved under the canonical ids and the manifest rebuilt in the same commit (2026-10-27); `check_taxids.py` reports 0 merged roots since 2026-10-28 | moved to `## Done` |
| "Three entries carry a value that is now disbelieved ... a hand edit each" | `CMV_UL55_gB_Deckers_2009`, the three Sigrist `ORTHOBORNAVIRUS_XP_*` and `LEPTOSPIROSIS_Flagillar_filiment_Prote` each carry a `CONDITIONS CORRECTED 2026-10-28 ... REMOVED, not replaced` note and the value is gone | struck in place |
| `orientation_inferred`: "what is owed is a `note` on each of the 26 carrying its number" | All 28 flagged entries carry "the archive yields N products and M none under this orientation (2026-10-27 run)" | struck in place |
| S3b: "the next full pipeline run has not happened yet" | `results/2026-10-27/` exists and is `docs/example-run-2026-10-27/`; the Operations item three screens down already said so | struck in place; heading renamed from "Shipped today" to "S3b, shipped 2026-10-27" |

The check for each was one `rg` over `registry/` or one `git merge-base`. The lesson is
not new: a dated phrase ("today", "after the live run", "left to do") in the roadmap
reads as current on every later day, so an item should carry the date it was written and
be re-read against the files before it is acted on.

## What is genuinely open, sorted by who can move it

**Needs the maintainer, and nothing else blocks on Claude:**
S7b (`scoring.mispair_window: 10`, priced and passing, `docs/journal/2026-10-29-s7b-priced.md`);
the works/fails sign-off on the eleven proposed rows in `docs/validation-cases-heldout-2.tsv`,
Hellgren `fails` first; the Quackenbush 1998 row; whether `CALICIVIRUS_ssRNA_Helicase_Reid_1999`
becomes `active`; whether the repo goes public.

**Build work, in the order `RESUME-HERE.md` already set:**
`drift.window_on` step 1 (collection date for `asm` records, interface first); the 93
`use` rows that did not reach CONFIRMED (`docs/2026-10-29-use-identity.tsv`); the trend
over distinct footprints; and the design conversation for a drift-mechanism case hunt,
since zero held-out rows carry `mechanism: drift`.

Nothing under `assaywatch/`, `config.yaml`, `registry/` or `Snakefile` is touched while
the Sunday 09:00 run is in progress.
