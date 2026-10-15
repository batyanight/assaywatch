"""Validate every YAML file in a registry directory against the schema.

    python -m assaywatch.validate registry/            # all files
    python -m assaywatch.validate registry/foo.yaml    # one file
    python -m assaywatch.validate registry/ --active-only

Exit code 1 if any file fails, so this doubles as the pre-commit hook and the
CI check. Prints one line per failure with the field path and the reason.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

import yaml
from pydantic import ValidationError

from assaywatch.schema import Assay


def load_assay(path: Path) -> Assay:
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, dict):
        raise ValueError("top level is not a mapping")
    assay = Assay.model_validate(data)
    if assay.id != path.stem:
        raise ValueError(f"id '{assay.id}' does not match file name '{path.stem}'")
    return assay


def iter_files(target: Path):
    if target.is_dir():
        yield from sorted(p for p in target.glob("*.yaml") if p.name != "README.md")
    else:
        yield target


def _tally(counts: Counter) -> str:
    """`a 3, b 1`, commonest first then alphabetical, so the line is stable."""
    return ", ".join(f"{name} {n}" for name, n in sorted(counts.items(), key=lambda x: (-x[1], x[0])))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", type=Path)
    ap.add_argument("--active-only", action="store_true", help="only report failures for status=active files")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    n_ok, failures, by_status, by_chemistry = 0, [], Counter(), Counter()
    n_probe = 0
    seen_ids: dict[str, Path] = {}
    for target in args.paths:
        for path in iter_files(target):
            try:
                assay = load_assay(path)
            except ValidationError as e:
                if args.active_only and yaml.safe_load(path.read_text()).get("status") != "active":
                    continue
                for err in e.errors():
                    loc = ".".join(str(x) for x in err["loc"]) or "<root>"
                    failures.append(f"{path.name}: {loc}: {err['msg']}")
                continue
            except (ValueError, yaml.YAMLError) as e:
                failures.append(f"{path.name}: {e}")
                continue
            if assay.id in seen_ids:
                failures.append(f"{path.name}: duplicate id also in {seen_ids[assay.id].name}")
            seen_ids[assay.id] = path
            by_status[assay.status.value] += 1
            by_chemistry[str(assay.chemistry)] += 1
            n_probe += assay.oligos.probe is not None
            n_ok += 1

    if not args.quiet:
        for line in failures:
            print("FAIL", line)
        # Printed rather than written into prose: the counts in README.md and
        # config.yaml drifted from the registry as it grew (they said 164 assays
        # and 21 probe-based when there were 214 and 44), and the argument for
        # how harsh `terminal_mismatch_fails` is rests on exactly these numbers.
        print(f"{n_ok} valid, {len(failures)} problems")
        print("  status:    " + _tally(by_status))
        print("  chemistry: " + _tally(by_chemistry))
        print(f"  oligos:    {n_probe} with a probe, {n_ok - n_probe} primers only")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
