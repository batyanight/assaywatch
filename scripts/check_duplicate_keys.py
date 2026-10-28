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

import yaml

REPO = Path(__file__).resolve().parents[1]


class _DupeFinder(yaml.SafeLoader):
    """A loader that collects repeated keys instead of quietly keeping the last."""

    def __init__(self, stream):
        super().__init__(stream)
        self.duplicates: list[tuple[str, int]] = []

    def construct_mapping(self, node, deep=False):
        seen: set[object] = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in seen:
                self.duplicates.append((str(key), key_node.start_mark.line + 1))
            seen.add(key)
        return super().construct_mapping(node, deep=deep)


_DupeFinder.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _DupeFinder.construct_mapping)


def duplicates_in(text: str) -> list[tuple[str, int]]:
    loader = _DupeFinder(text)
    try:
        loader.get_single_data()
        return loader.duplicates
    finally:
        loader.dispose()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, nargs="+", default=[REPO / "registry"])
    args = ap.parse_args(argv)

    bad = 0
    files = 0
    for root in args.registry:
        paths = sorted(root.glob("*.yaml")) if root.is_dir() else [root]
        for path in paths:
            files += 1
            for key, line in duplicates_in(path.read_text()):
                print(f"DUPLICATE\t{path.name}:{line}\t{key}")
                bad += 1
    print(f"{files} files checked, {bad} duplicate keys", file=sys.stderr)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
