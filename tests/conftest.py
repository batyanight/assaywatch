"""Test tiers. `pytest -m fast` is the write-test-run loop; see pyproject.toml.

The fast tier is a list of files, kept in one place so it is easy to read and to
change. A file belongs here when every test in it is a pure function over small
in-memory inputs or the tiny fixtures: no whole-registry sweep, no subprocess, no
screen over the fixture FASTA. Check the budget after adding one:

    pytest -m fast --durations=5      # whole tier under 10 s
"""

import pytest

FAST_FILES = frozenset(
    f"test_{name}.py"
    for name in (
        "accession",
        "chance",
        "chance_pair",
        "clustering",
        "degeneracy",
        "flag_rule",
        "gapped",
        "iupac",
        "lineage",
        "load_assay_cache",
        "locus_identity",
        "loci",
        "metadata",
        "nested",
        "sitedrift",
        "trend",
        "windows",
    )
)


def pytest_collection_modifyitems(items):
    for item in items:
        if item.path.name in FAST_FILES:
            item.add_marker(pytest.mark.fast)
