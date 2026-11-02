"""Every file in registry/ must validate. This is what CI runs on each pull request."""

from pathlib import Path

import pytest

from assaywatch.validate import load_assay

REGISTRY = Path(__file__).resolve().parents[1] / "registry"
FILES = sorted(REGISTRY.glob("*.yaml"))


@pytest.mark.parametrize("path", FILES, ids=[p.stem for p in FILES])
def test_registry_file_validates(path):
    load_assay(path)
