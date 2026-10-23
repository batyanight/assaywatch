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


SCHEMA_PATH = Path("registry/schema.json")


def emit_schema(path: Path | None) -> None:
    """Write `Assay`'s JSON Schema to `path`; with `None`, compare against the committed copy."""
    import json

    schema = Assay.model_json_schema()
    schema["$schema"] = "https://json-schema.org/draft/2020-12/schema"
    schema["title"] = "AssayWatch registry entry"
    schema["$comment"] = (
        "Generated from assaywatch.schema by `python -m assaywatch.validate "
        "--emit-schema registry/schema.json`. Do not edit by hand. The models are "
        "the contract; this file is their published form, for reading registry/*.yaml "
        "outside Python. Licence: see LICENSE-registry."
    )
    text = json.dumps(schema, indent=2, sort_keys=True) + "\n"
    if path is None:
        current = SCHEMA_PATH
        if not current.exists() or current.read_text() != text:
            raise SystemExit(
                "registry/schema.json is stale or missing; regenerate with "
                "`python -m assaywatch.validate --emit-schema registry/schema.json`"
            )
        print("registry/schema.json matches assaywatch.schema")
        return
    path.write_text(text)
    print(f"wrote {path} ({len(text):,} bytes)")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    # `nargs="*"`, not `"+"`, so `--emit-schema` needs no paths; a bare call with
    # neither still errors below, which is what a user who forgot the registry wants.
    ap.add_argument("paths", nargs="*", type=Path)
    ap.add_argument("--active-only", action="store_true", help="only report failures for status=active files")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument(
        "--emit-schema",
        type=Path,
        metavar="PATH",
        help="write the registry's JSON Schema here and exit (no paths are read)",
    )
    ap.add_argument(
        "--check-schema",
        action="store_true",
        help="fail if registry/schema.json differs from the models; for CI",
    )
    args = ap.parse_args(argv)

    if not args.paths and not (args.emit_schema or args.check_schema):
        ap.error("give at least one path, or --emit-schema / --check-schema")
    if args.emit_schema or args.check_schema:
        # The schema has been generatable since schema.py was written -- its
        # docstring says so -- and nothing emitted it, so the registry's only
        # machine-readable contract lived in Python. A reuser of registry/*.yaml
        # outside Python had to read pydantic source or 208 files. `--check`
        # compares instead of writing, so CI can fail when the committed copy
        # drifts from the models.
        emit_schema(args.emit_schema)
        return 0

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
