# validate

Runs before any other stage and stops the pipeline if the registry does not
parse, has a duplicate key, or holds an entry without a confirmed citation.

It also runs on every commit, so a malformed entry never reaches a run. The
schema is strict: an unrecognised field is an error and is not ignored, so a
mistyped field name cannot silently disable a setting.

**Input:** `registry/*.yaml` · **Output:** clearance to proceed, or every
invalid file reported at once, not just the first.
