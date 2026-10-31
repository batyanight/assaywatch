# The public repository was recreated from a clean tree (2026-10-31)

**Finding.** The working tree had been clean of an institutional name since
2026-10-23 (`journal/2026-10-23-verified-doi-gate.md`), but the git history had not:
grepping every blob of every commit found the name in **345 of 649 commits** across
249 paths, and in 6 commit messages. `CLAUDE.md` once named it as the source registry,
`LICENSE-registry` said 138 entries derived from it, the README documented the import
script by its real filename. The repository had been public since 2026-10-03, so that
history was fetchable for four weeks. GitHub-side text (PR bodies, issues, comments)
was clean. Traffic showed 556 clones from 36 unique cloners and 0 views over 14 days,
which is the signature of this repository's own CI checking itself out rather than of
readers; no forks exist.

**Why replace rather than rewrite.** `git filter-repo` and a force push leave the old
objects on GitHub, fetchable by anyone holding a commit SHA, until GitHub Support
garbage-collects on request. A fresh repository has no residue. The cost was measured
before deciding: 2 short SHAs cited anywhere in the docs, 0 PR numbers, and one claim
(`README.md`, the co-authorship trailer count) that describes the history. The
reasoning trail is `docs/journal/`, 136 files in the tree, so it survives.

**What was done.** A bare mirror of the full history was taken first. The existing
GitHub repository was renamed and set private, keeping its history, branches and the
one open PR (#33, the collection-year lens, out of scope for v0.1). A new public
repository under the original name received the clean tree as one commit. The
trailer figures were read from the full history before it left the public record:
581 of 640 commits on `main` carried a `Co-Authored-By: Claude` trailer and 64 had
Claude as the git author. `docs/ai-involvement.md` now says the history is not
reconstructible here and why.

**Kept deliberately.** 27 registry entries and 13 journals say "the seed list",
unnamed, almost always as the thing that was wrong ("the seed list had a transcription
error", "the 121 came from the seed list"). That is the correction record and it is
what makes those amplicon and citation fixes auditable. Every entry cites its own paper
as its source; the phrase names no institution and no file. Decision taken by the
maintainer on 2026-10-31, after seeing the list.

**Checked and found to be noise.** A `git grep` hit in `docs/taxonomy-cache.json.gz`
matched the *compressed* bytes; the decompressed JSON contains 0 matches. `Zoo` (93
files) is *Leucocytozoon* and *Encephalitozoon*.
