"""The environment is declared in several files; these assert they agree.

R1 (2026-10-21). `environment.yml` is the single source of truth for a local
install, but CI installs with pip and the ruff pin is repeated in three files.
A fresh `conda env create -f environment.yml` was found unable to run four
documented commands because the deps behind them lived only in pyproject extras,
and the Snakemake pin in the env (`>=8`) disagreed with CI's (`>=9.27,<9.28`),
so laptop and CI could resolve different majors. Nothing caught either, because
nothing checked. These do.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENV = (ROOT / "environment.yml").read_text()
CI = (ROOT / ".github" / "workflows" / "validate.yml").read_text()
PYPROJECT = (ROOT / "pyproject.toml").read_text()
PRECOMMIT = (ROOT / ".pre-commit-config.yaml").read_text()


def _env_dep(name: str) -> str | None:
    """The version constraint on a conda dep in environment.yml, '' if unpinned."""
    m = re.search(rf"^\s*-\s*{re.escape(name)}([<>=!].*?)?\s*(?:#.*)?$", ENV, re.M)
    if m is None:
        return None
    return (m.group(1) or "").strip()


def test_the_documented_commands_have_their_dependencies_in_the_env():
    """A fresh env must be able to run every command the docs tell a user to run.

    Each of these backed a documented command that a core-only install left out
    (parse_wcs_primers, verify_oligos_against_paper --pdf-dir,
    verify_predict_supplement, the SLURM profile). If one is dropped from
    environment.yml, the command silently breaks only on a clean machine.
    """
    for dep in ("openpyxl", "pypdf", "poppler", "snakemake-executor-plugin-slurm"):
        assert _env_dep(dep) is not None, f"{dep} missing from environment.yml"


def test_snakemake_pin_agrees_between_env_and_ci():
    """Laptop and CI must not resolve different Snakemake majors."""
    env = _env_dep("snakemake-minimal")
    assert env, "environment.yml does not pin snakemake-minimal"
    ci = re.search(r'"snakemake(>=[\d.]+,<[\d.]+)"', CI)
    assert ci, "could not find CI's snakemake pin"
    # The env pins snakemake-minimal, CI pins snakemake; compare the constraints.
    assert env == ci.group(1), f"env {env!r} vs CI {ci.group(1)!r}"


def test_ruff_pin_agrees_across_every_file_that_states_it():
    """A hook on a different ruff reformats what the local ruff just formatted."""
    env = _env_dep("ruff")  # e.g. '=0.16.10'
    assert env, "environment.yml does not pin ruff"
    env_ver = env.lstrip("=")
    pyproject = re.search(r"ruff==([\d.]+)", PYPROJECT)
    precommit = re.search(r"ruff-pre-commit\s*\n(?:.*\n)*?\s*rev:\s*v([\d.]+)", PRECOMMIT)
    assert pyproject and pyproject.group(1) == env_ver, f"pyproject ruff != {env_ver}"
    assert precommit and precommit.group(1) == env_ver, f"pre-commit ruff != {env_ver}"


def test_env_installs_the_package_itself():
    """The whole point of the env is that `import assaywatch` works; -e . must stay."""
    assert re.search(r"pip:\s*\n\s*-\s*-e\s*\.", ENV), "environment.yml must `pip: -e .`"
