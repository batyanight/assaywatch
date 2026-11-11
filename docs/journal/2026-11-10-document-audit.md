# Every tracked document, who it is for, and the six that want a decision

2026-11-10, the maintainer's request of 2026-11-06: "go through every tracked document,
decide who it's for, and list what to keep, move to `local/` or remove". **Nothing is moved
or removed here.** This is the list.

## The audiences

The repository is public (2026-10-30). Four audiences, and almost every document has a clear
one:

| audience | documents |
|---|---|
| **a reader deciding whether to trust the output** | `README.md`, `docs/state-of-the-project.md`, `docs/screening-and-the-drift-call.md`, `docs/related-work.md`, `GLOSSARY.md`, `docs/example-run-2026-11-01/`, `website/` |
| **someone installing or running it** | `docs/installation.md`, `docs/running-the-pipeline.md`, `docs/pipeline-architecture.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `examples/README.md`, `pending/README.md`, `profiles/launchd/README.md` |
| **the maintainer and the next session** | `ROADMAP.md`, `CLAUDE.md`, `docs/INDEX.md`, `docs/PRD.md`, `docs/RESUME-HERE.md`, `docs/bayesian-scoring-plan.md`, `docs/nested-protocol-plan.md`, `docs/journal/` (151 files) |
| **the record behind a number** | `docs/bench-panels/`, `docs/validation-cases*.tsv`, `docs/design-era.tsv`, `docs/assay-sheet.tsv`, the dated `docs/*.tsv`, the caches, `tests/fixtures/` |

**The 151 journals: keep all of them, unchanged.** Triaged file by file against the policy in
`docs/journal/README.md`. No named employer, no `/Users/` path, no credential (the only token
hits are the *path* `.secrets/elsevier.insttoken`), no pasted PDF text, no duplicate, and no
uncorrected false statement -- `2026-10-22-M1-tier2.md` already carries its own superseded
banner. Third-party names are paper authors in citations. The worklists in the Superseded
section all carry reasoning and `INDEX.md` justifies each.

## The six that want a decision

### 1. `docs/2026-10-06-lab-leads.tsv` names research groups as the origin of leads

188 rows with a `lab_named_by_search` column: "Canadian Wildlife Health Cooperative
(Western/Northern node, WCVM)", "Guelph Pathobiology", and so on. The scope rule in
`CLAUDE.md` is "Source: the literature. Every entry cites its own paper; never mention any lab
or list as a source." Nothing in `registry/` breaks that rule; this file sits beside it and
reads as though labs were a source, which is the appearance the rule exists to prevent. The
groups are publicly published and attached to public DOIs, so this is not a confidentiality
problem -- it is a consistency one.

**Options:** move the TSV to `local/` and leave `journal/2026-10-06-lab-leads.md` (which reads
fine without it) pointing at nothing; or drop the one column and keep the leads; or keep it and
accept the appearance. **Recommend dropping the column**: the pathogen, the DOI and the reason
are what make a lead workable, and the group name is the part that reads as a source.

### 2. `docs/RESUME-HERE.md` is 294 KB and 27 stacked resume points

`CLAUDE.md` says it "says where work stopped and keeps no list". It now carries every handoff
back to 2026-10-24, of which exactly one is live. At 294 KB it is the third largest document in
the repository and a session reading it as instructed reads 26 dead ones first.

**Recommend:** keep the newest three in place and move the rest to one
`docs/journal/2026-11-10-resume-points-archive.md`, indexed as history. No word is lost, which
is the standing condition for this kind of move.

### 3. Two superseded "papers still needed" lists

`papers/papers-fetch-list.md` opens "**Fetch list — EMPTY as of 2026-10-28.** Every paper this
list asked for is now in `papers/`." It is the one deliberate non-roadmap queue named in
`CLAUDE.md`. Beside it sit `papers/papers-still-needed.md` (118 lines, undated, "Downloaded 56
of 153") and `papers/papers-still-needed-2026-10-24.md` (127 lines), two earlier generations of
the same list, both answered.

**Recommend:** move both to `local/`. They are superseded by a file that says so in its first
line, and a contributor meeting three lists cannot tell which is live.

### 4. `docs/INDEX.md` describes one file as two different runs

Two rows both link `example-run-2026-11-01/report.md`. One calls it "**the current committed
run**, under today's scoring"; the other calls it "the last run under the scoring that shipped
before 2026-10-27, kept so the two can be diffed". Only one example-run directory has ever
existed, so the second row describes a file that is not there and a reader following it draws
the wrong conclusion from the right file.

**Recommend:** delete the second row, or restore the older run it was written for. A defect,
not a preference.

### 5. `ROADMAP.md` line 1923 prints an absolute home path

`/Users/batya/assaywatch`, inside the record of the 2026-10-29 change that *removed* hardcoded
paths from two scripts. The mention is honest history and the only one in any tracked file, but
it publishes the username.

**Recommend:** reword to `the repository root`. The sentence loses nothing.

### 6. `docs/journal/2026-10-06-lab-leads.md` prints a lab's contact address

Line 87, `cwhl@cornell.edu`, as the practical route to ask for primer details. It is a public
institutional address, not a personal one.

**Recommend:** keep. Redact only if the maintainer would rather no address appeared at all.

## What the audit did not find

No credential, key or token value in any tracked file. No copyrighted PDF text (`papers/` holds
the PDFs and is gitignored, as `CLAUDE.md` requires; only the lists are tracked). No personal
data beyond the maintainer's own name and the one institutional address above. No tracked
document that is a to-do list competing with `ROADMAP.md` -- the three `papers/` lists are the
nearest thing and finding 3 is about exactly that.

The 2.4 MB of committed output in `docs/example-run-2026-11-01/` is deliberate and has the
clearest audience of anything here: it is what the tool produces, readable without installing
it. Keep.
