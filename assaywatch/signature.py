"""Where a cached screen records what it was produced under.

A convention, not logic, and it lives alone because of who has to share it.
`screen.py` writes the file and `collect.py` reads it, and neither may import
the other:

* `collect` inside `screen`'s import closure would mean every edit to
  collect.py rescreens all 316 archives, because the Snakefile hashes that
  closure into `screen_archive`'s params (see `assaywatch/triggers.py` and
  `_code_hash` in the Snakefile).
* `screen` inside `collect`'s closure would mean every edit to score.py or
  schema.py re-triggers `collect_calls`. Harmless — collecting is cheap — but
  it is noise in the one mechanism the pipeline uses to decide what is stale,
  and that mechanism has already been wrong twice.

So the convention sits here, where both can reach it and neither drags the
other along. Editing this file does rescreen everything, which is correct: it
changes where a screen's signature is kept.

WHY A FILE ON DISK AT ALL. `screen_signature` was already a `screen_archive`
param, and Snakemake reruns a job when a param changes — but only where it
holds a metadata record for that output to compare against. The 2026-10-21 run
found 20 screens of 316 with no such record, written by a different Snakemake
install: the params check had nothing to compare, the changed code hash did not
invalidate them, and they were reused in silence. A file beside the screen is
checkable by `collect` whatever Snakemake remembers.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

#: Appended to a screen's own name, so the result cannot be mistaken for a
#: screen by anything globbing `*.tsv` — `assaywatch/windows.py` does.
SIGNATURE_SUFFIX = ".sig"

#: The fields of an assay entry a screen's result can depend on. Everything else in
#: a registry YAML is provenance, citation or curation prose, and hashing it made
#: every note edit rescreen the groups that hold that entry.
#:
#: MEASURED, 2026-10-28: 192 entries were edited in two days -- the conditions
#: curation, five deletions, a reflagging, three provenance notes -- and 312 of 494
#: cached screens went stale. Not one of those edits could change a call: not a
#: sequence, not an amplicon, not a query. The signature hashed the whole file.
#:
#: Each name here is justified by a reader of it:
#:   oligos      `score.screen_one` reads matching_seq for every oligo, which is
#:               built from seq, seq_as_written and tail_5prime (schema.Oligo), and
#:               the alternates list is searched too
#:   chemistry   `score.config_for` resolves `scoring.by_chemistry` on it, so the
#:               same mismatch costs different penalties per chemistry
#:   amplicon_bp, amplicon_bp_range, species_sizes
#:               `score` gates a product against the declared size and
#:               `config.amplicon.declared_tolerance`
#:   target      taxid, query, scope_taxids and exclusivity_taxids decide which
#:               archives a group holds and which records are screened at all
#:   status      a `deprecated` entry is not screened (retrieve.targets_from_registry)
#:   needs_review flags, WITHOUT their notes: an OPEN flag on an `active` entry makes
#:               the file fail validation (`Assay.active_requires_resolved_review`), and
#:               an entry that will not load is an entry that is not screened -- so a
#:               flag CAN change what a run sees, in combination with `status`. The
#:               note cannot. Measured cost of keeping them: adding
#:               `conditions_not_printed` to two orthoreovirus entries rescreens 3
#:               archives, which is the price of not reasoning about which flags are
#:               load-bearing in which status
#:
#: Adding a field is cheap and safe. Leaving one out is the dangerous direction --
#: it means an edit that changes a call reuses a stale screen -- so
#: `tests/test_signature_projection.py` pins this list against the schema and fails
#: when a new field appears that nobody has classified.
SCREEN_FIELDS = (
    "oligos",
    "chemistry",
    "amplicon_bp",
    "amplicon_bp_range",
    "species_sizes",
    "target",
    "status",
)


def signature_path(calls: Path) -> Path:
    """Where `calls`'s signature lives: `2026-10-03.tsv` -> `2026-10-03.tsv.sig`."""
    return calls.with_name(calls.name + SIGNATURE_SUFFIX)


def stored_signature(calls: Path) -> str | None:
    """What `calls` says it was produced under, or None if it does not say.

    None is the honest answer for every screen written before 2026-10-21, and
    callers must keep it distinct from disagreement: "does not say" and "says
    something else" are different facts and only the second is a defect.
    """
    sig = signature_path(calls)
    if not sig.exists():
        return None
    return sig.read_text().strip() or None


def screen_key(doc: dict[str, Any]) -> bytes:
    """The part of one registry entry a screen's result can depend on, canonically.

    Takes the loaded YAML rather than the pydantic model, because the Snakefile hashes
    this for every assay of every group before anything is screened and loading 214
    models to hash them is work for nothing. The cost of that choice is that this reads
    raw field names, which is why the field list is pinned against the schema by a test.

    A missing field and a null field hash the same, so adding `conditions: null` to an
    entry does not rescreen it.
    """
    projection = {k: doc.get(k) for k in SCREEN_FIELDS if doc.get(k) is not None}
    # Flag names only. `needs_review` notes are prose, and the 2026-10-28 reflagging of
    # one calicivirus entry showed why that matters: changing a flag's NAME can change
    # what the pipeline does with the entry, while rewriting its note cannot.
    flags = sorted(i.get("flag") for i in (doc.get("needs_review") or []) if i.get("flag"))
    if flags:
        projection["needs_review_flags"] = flags
    return json.dumps(projection, sort_keys=True, default=str, separators=(",", ":")).encode()
