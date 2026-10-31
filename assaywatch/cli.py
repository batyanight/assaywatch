"""`assaywatch <stage> [args]`: the one command, with one subcommand per stage.

Each stage's arguments are parsed by that stage's own `main(argv)`, which is also what
`python -m assaywatch.<stage>` runs. This module only owns the table of stages and the
dispatch, so reading it tells you how the tool is driven and nothing else. Adding a
stage is one line in STAGES; `tests/test_cli.py` checks that every module with a
`__main__` block is listed here and vice versa.

    assaywatch validate registry
    assaywatch retrieve registry --email you@example.org
    assaywatch report results/2026-10-27/calls.tsv.gz --out results/2026-10-27/report
"""

from __future__ import annotations

import importlib
import sys

#: stage name -> (module, one line of help). Order is the pipeline's.
STAGES: dict[str, tuple[str, str]] = {
    "validate": ("assaywatch.validate", "check every entry against the schema and the live rule"),
    "curate": (
        "assaywatch.curate",
        "run the curation chain on an entry: verify, measure, fill in, list what is left",
    ),
    "credentials": (
        "assaywatch.credentials",
        "find the NCBI key and, with --check, ask NCBI whether it works",
    ),
    "retrieve": ("assaywatch.retrieve", "fetch and archive a target's GenBank records, incrementally"),
    "screen": ("assaywatch.screen", "screen assays against a FASTA: one call per (assay, record)"),
    "windows": ("assaywatch.windows", "cut archives down to the windows around screened sites"),
    "sitedrift": ("assaywatch.sitedrift", "which oligo positions fail, and in which accessions"),
    "lineage-report": (
        "assaywatch.lineage_report",
        "per-lineage detection and the lineage-conditional verdict",
    ),
    "degeneracy": ("assaywatch.degeneracy", "primer-pool degeneracy per assay"),
    "figures": ("assaywatch.figures", "the report's figures"),
    "report": ("assaywatch.report", "render report.md and report.html from a calls table"),
}


def resolve(name: str) -> str | None:
    """The module for a stage name; `lineage_report` and `lineage-report` are the same."""
    entry = STAGES.get(name) or STAGES.get(name.replace("_", "-"))
    return entry[0] if entry else None


def _usage() -> str:
    width = max(map(len, STAGES))
    lines = ["usage: assaywatch <stage> [args]", "", "stages, in pipeline order:"]
    lines += [f"  {name:<{width}}  {help_}" for name, (_, help_) in STAGES.items()]
    lines += ["", "`assaywatch <stage> --help` describes one stage's arguments."]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    if not argv:
        print(_usage(), file=sys.stderr)
        return 2
    if argv[0] in ("-h", "--help"):
        print(_usage())
        return 0
    module = resolve(argv[0])
    if module is None:
        print(f"assaywatch: unknown stage {argv[0]!r}\n\n{_usage()}", file=sys.stderr)
        return 2
    return int(importlib.import_module(module).main(argv[1:]) or 0)


if __name__ == "__main__":
    raise SystemExit(main())
