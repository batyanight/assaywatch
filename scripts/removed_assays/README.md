# Removed assays

Entries taken out of `registry/`, kept so the removal is a record rather than a
deletion. They are not validated and are not screened; `../removed_assays.txt`
lists the out-of-scope files that were dropped without being kept.

**Their `needs_review` is the old free-text form, on purpose.** The registry's
field became a controlled vocabulary on 2026-10-21 (`assaywatch/review.py`);
these files were written before that and are left as they were, because what
they say is *why each one was removed*, in the words used at the time. Three of
the strings here have no home in the vocabulary and should not get one:
`NEED_TO_ORDER` recorded the lab's 2018 stock and was deliberately retired,
`REMOVED_2026_10_21_LAB_MADE_FFPE_PRIMER_UNPUBLISHED` is a removal reason rather
than a property of an assay, and `DOI_MISSING` / `NO_YEAR` restate fields on the
same document.

Restoring one of these to `registry/` therefore means rewriting its
`needs_review` into the current form first, or the validator will refuse it —
which is the intended outcome, not an obstacle: an entry coming back deserves a
fresh read of what is still open about it.
