"""Every file in registry/ must validate. This is what CI runs on each pull request."""

from pathlib import Path

import pytest
import yaml

from assaywatch.validate import load_assay

REGISTRY = Path(__file__).resolve().parents[1] / "registry"
FILES = sorted(REGISTRY.glob("*.yaml"))


@pytest.mark.parametrize("path", FILES, ids=[p.stem for p in FILES])
def test_registry_file_validates(path):
    load_assay(path)


def test_gene_names_follow_the_rule_in_the_glossary():
    """`target.gene` is a name shown in a table column, so it holds `symbol (product)` or a
    bare name. Coordinates, accessions and ortholog lists belong in `notes_curator`; the one
    exception is a locus whose position is its only identity."""
    import re

    root = Path(__file__).resolve().parents[1]
    bad = []
    for path in sorted([*(root / "registry").glob("*.yaml"), *(root / "pending").glob("*.yaml")]):
        gene = (yaml.safe_load(path.read_text())["target"] or {}).get("gene") or ""
        if (
            re.search(r"positions?\b|;|ortholog|homolog|[A-Z]{1,2}\d{5,}", gene)
            or re.match(r"[a-z].*\(\w{2,4}\)$", gene)  # product (symbol): the wrong way round
            or len(gene) > 65
        ):
            bad.append((path.stem, gene))
    assert not bad, bad
