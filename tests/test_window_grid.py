"""`scripts/window_grid.py`: the overlay must change exactly the two keys it names.

The grid prices `recent_window_months` and `min_records_for_drift` together by writing
one config per cell and handing it to `scripts/retrospective.py`. A regex overlay that
silently matched nothing would price the shipped config twelve times and print a flat
table that looks like "the pair does not matter". So the overlay refuses when either key
is not found exactly once, and widens `max_window_months` only when the window would
otherwise exceed it -- the validator rejects a file where it does.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest
import yaml

from assaywatch.settings import validated

ROOT = Path(__file__).resolve().parents[1]


def _module():
    spec = importlib.util.spec_from_file_location("window_grid", ROOT / "scripts" / "window_grid.py")
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_overlay_changes_the_two_keys_and_the_result_still_validates():
    mod = _module()
    base = (ROOT / "config.yaml").read_text()
    out = validated(yaml.safe_load(mod.overlay(base, 36, 30)))
    assert out["drift"]["recent_window_months"] == 36
    assert out["drift"]["min_records_for_drift"] == 30
    assert out["drift"]["max_window_months"] >= 36
    # Everything else is the shipped config, byte for byte in meaning.
    shipped = validated(yaml.safe_load(base))
    for key, value in shipped["drift"].items():
        if key not in {"recent_window_months", "min_records_for_drift", "max_window_months"}:
            assert out["drift"][key] == value, key


def test_overlay_widens_max_window_only_when_it_must():
    mod = _module()
    base = (ROOT / "config.yaml").read_text()
    shipped_max = validated(yaml.safe_load(base))["drift"]["max_window_months"]
    small = validated(yaml.safe_load(mod.overlay(base, 12, 10)))
    assert small["drift"]["max_window_months"] == shipped_max
    huge = validated(yaml.safe_load(mod.overlay(base, shipped_max + 24, 10)))
    assert huge["drift"]["max_window_months"] == shipped_max + 24


def test_overlay_refuses_a_config_without_the_keys():
    mod = _module()
    with pytest.raises(SystemExit):
        mod.overlay("drift:\n  detect_fraction_threshold: 0.9\n", 24, 15)
