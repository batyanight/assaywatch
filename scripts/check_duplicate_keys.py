#!/usr/bin/env python3
"""Refuse a registry file that gives the same key twice. Report only; never edits.

    python scripts/check_duplicate_keys.py --registry registry

WHY THIS IS NOT THE VALIDATOR'S JOB. `yaml.safe_load` keeps the LAST of two
identical keys and says nothing, so by the time pydantic sees the mapping the other
value is gone -- the entry validates, screens and reports perfectly while carrying
only half of what the file says. `LEPTOSPIROSIS_Flagillar_filiment_Prote.yaml` held
two `notes_curator` keys for three days and the whole 2026-10-24 spelling note was
in the file and in no loaded entry.

pre-commit's `check-yaml` catches this, and only on files a commit touches, which is
why it surfaced on an unrelated commit three days later. This asks the question of
every file, every run, so a duplicate that lands outside a commit's diff -- in a bulk
edit, or by a script -- is found when it happens.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from assaywatch.registry import duplicate_keys  # noqa: E402
from assaywatch.registry import files as entry_files  # noqa: E402

# The finder lives in assaywatch.registry (curate asks it too); the name stays for the test.
duplicates_in = duplicate_keys


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, nargs="+", default=[REPO / "registry"])
    args = ap.parse_args(argv)

    bad = 0
    files = 0
    for root in args.registry:
        for path in entry_files(root):
            files += 1
            for key, line in duplicates_in(path.read_text()):
                print(f"DUPLICATE\t{path.name}:{line}\t{key}")
                bad += 1
    print(f"{files} files checked, {bad} duplicate keys", file=sys.stderr)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
