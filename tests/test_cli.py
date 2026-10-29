"""`assaywatch <stage>`: one command, one subcommand per stage, parsing per stage."""

import subprocess
import sys
from pathlib import Path

import pytest

from assaywatch import cli

PENDING = Path(__file__).resolve().parents[1] / "pending"


def test_every_stage_names_a_module_with_a_main():
    import importlib

    for name, (module, _help) in cli.STAGES.items():
        assert callable(importlib.import_module(module).main), name


def test_every_module_with_a_main_is_a_stage():
    """A new `python -m assaywatch.x` must be reachable as `assaywatch x` too."""
    package = Path(cli.__file__).parent
    with_main = {p.stem for p in package.glob("*.py") if 'if __name__ == "__main__"' in p.read_text()}
    assert with_main - {"cli"} == {m.rsplit(".", 1)[1] for m, _ in cli.STAGES.values()}


def test_help_lists_every_stage(capsys):
    assert cli.main(["--help"]) == 0
    out = capsys.readouterr().out
    for name in cli.STAGES:
        assert name in out


def test_no_arguments_is_help_with_a_nonzero_exit(capsys):
    assert cli.main([]) == 2
    assert "usage" in capsys.readouterr().err.lower()


def test_an_unknown_stage_fails_and_names_the_choices(capsys):
    assert cli.main(["frobnicate"]) == 2
    assert "validate" in capsys.readouterr().err


def test_a_stage_gets_the_rest_of_the_arguments(capsys):
    assert cli.main(["validate", str(PENDING), "--pending", "--quiet"]) == 0


def test_underscore_and_hyphen_both_name_the_lineage_report():
    assert cli.resolve("lineage-report") == cli.resolve("lineage_report")


@pytest.mark.parametrize("how", [["assaywatch"], [sys.executable, "-m", "assaywatch"]])
def test_the_command_is_installed_both_ways(how):
    r = subprocess.run(
        [*how, "validate", str(PENDING), "--pending", "--quiet"], capture_output=True, text=True
    )
    assert r.returncode == 0, r.stderr
