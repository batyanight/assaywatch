# validate

Executes before any other stage and halts the pipeline on a registry that does
not parse, contains a duplicate key, or holds an entry without a confirmed
citation.

It also runs on every commit, so a malformed entry does not reach a run. The
schema is strict: an unrecognised field is an error rather than being ignored,
which prevents a mistyped field name from silently disabling a setting.

**Input:** `registry/*.yaml` · **Output:** clearance to proceed, or every
invalid file reported at once rather than only the first.
