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


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", type=Path)
    ap.add_argument("--active-only", action="store_true", help="only report failures for status=active files")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    n_ok, failures, by_status = 0, [], Counter()
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
            n_ok += 1

    if not args.quiet:
        for line in failures:
            print("FAIL", line)
        print(f"{n_ok} valid ({dict(by_status)}), {len(failures)} problems")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
