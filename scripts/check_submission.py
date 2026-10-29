#!/usr/bin/env python3
"""Check a submitted or existing assay entry before it is trusted.

    python scripts/check_submission.py registry/NEW_ASSAY.yaml --email you@example.org
    python scripts/check_submission.py registry/ --offline      # schema and oligo checks only

Everything that went wrong in this registry's first months was a transcription
or provenance error, not a modelling error: a Sarcocystis primer carried one
extra C and failed on 98% of records; two orthobunyavirus primers carried
non-templated cloning tails and matched nothing at all; three taxids pointed at
the wrong organism, one of them to a genus of moths; five DOIs resolved to
other papers. Each was caught eventually by a different ad-hoc script. This
collects those checks in one place and runs them against a candidate entry, so
a submission is checked before it reaches a report rather than after.

The checks, in increasing cost:

  schema      the entry parses, the oligos are IUPAC and the right length
  tails       no restriction site sitting at an oligo's 5' end (a cloning tail
              does not bind the target, so it must be declared in tail_5prime)
  degeneracy  the primer pool size, and a warning when it is so large that an
              in-silico `detect` means little
  citation    the DOI resolves, and its first author and year match the entry
  taxon       the taxid exists and still means what the entry says it does
  amplify     the decisive one: fetch a sample of real records for this target
              and check the oligos actually find their amplicon in them

The `amplify` check is what catches a mistyped oligo. An assay whose primers
match nothing in their own target taxon is far more likely to be wrong than to
be a real discovery, and that is exactly the signature of both bugs above.

Exit status is 0 when nothing failed, 1 when any check failed. Warnings do not
fail the run: a brand-new pathogen with three deposited sequences will warn on
`amplify` and still be a perfectly good submission.
"""

# Since 2026-10-29 every check here is a step of `assaywatch curate`, which also
# writes what it can resolve (doi_verified, a missing taxid, an unset amplicon_bp)
# and fetches the paper. This script is the old spelling of that command and takes
# the same arguments; `assaywatch curate --dry-run` is this script's behaviour.

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch.curate import main as curate_main  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    if "--dry-run" not in argv:
        argv.append("--dry-run")
    return curate_main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
