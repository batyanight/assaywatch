"""config.yaml's shape, and the drift the model closes."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from assaywatch.score import load_config
from assaywatch.settings import Settings, validated

ROOT = Path(__file__).resolve().parents[1]


def raw() -> dict:
    return yaml.safe_load((ROOT / "config.yaml").read_text())


def test_validation_changes_no_value_in_the_committed_config():
    """The model must be a description of config.yaml, not a correction of it.

    Introducing validation that silently moved a scoring value would invalidate
    every cached screen in results/screened/ without saying so, because the
    screen signature hashes the scoring block.
    """

    def flat(d, p=""):
        out = {}
        for k, v in d.items():
            if isinstance(v, dict):
                out.update(flat(v, f"{p}{k}."))
            else:
                out[f"{p}{k}"] = v
        return out

    before, after = flat(raw()), flat(validated(raw()))
    assert set(before) == set(after), "validation added or dropped a key"
    assert before == after, "validation changed a value"


def test_a_misspelled_key_anywhere_is_refused():
    """The whole point. `score.check_chemistry_overrides` covered `by_chemistry`
    and said why -- "the run would succeed, the numbers would be the old ones,
    and the report would be indistinguishable from a recalibrated run" -- and
    that was true of all 67 keys, of which it checked two."""
    for block, key in [("drift", "min_dec1ine"), ("scoring", "detect_maxx"), ("lineage", "alfa")]:
        cfg = raw()
        cfg[block][key] = 1
        with pytest.raises(ValueError, match=f"{block}.{key}"):
            validated(cfg)
    cfg = raw()
    cfg["retreive"] = {}
    with pytest.raises(ValueError, match="retreive"):
        validated(cfg)


def test_the_defaults_live_here_and_nowhere_else():
    """Every consumer read `cfg.get(key, literal)`, so each default had two
    homes and six had come apart -- each in the unsafe direction, and each
    reachable only if its key went missing, which is what a typo does.

    The model fills every key, so the literals can no longer be reached. This
    pins the values the drifted ones disagreed with.
    """
    d = Settings().model_dump()
    assert d["drift"]["min_decline"] == 0.05  # code said 0.0: any real fall is drift
    assert d["drift"]["min_records_for_drift"] == 15  # code said 20
    assert d["drift"]["require_working_baseline"] is True
    assert d["lineage"]["min_records_per_lineage"] == 30  # code said 20, the rejected value
    assert d["lineage"]["require_working_baseline"] is True  # code said False
    assert d["amplicon"]["record_min_overhang_bp"] == 100  # code said 0
    # and a config with those blocks absent entirely still gets them
    filled = validated({})
    assert filled["drift"]["min_decline"] == 0.05
    assert filled["lineage"]["multiple_testing"] == "holm"


def test_an_incoherent_pair_is_refused_even_though_each_value_is_fine():
    """Ranges catch a bad number; these catch a bad pair."""
    for block, patch in [
        ("scoring", {"detect_max": 3.0, "reduced_max": 1.0}),
        ("amplicon", {"min_bp": 500, "max_bp": 100}),
        ("drift", {"recent_window_months": 60, "max_window_months": 24}),
    ]:
        cfg = raw()
        cfg[block].update(patch)
        with pytest.raises(ValueError):
            validated(cfg)


def test_load_config_goes_through_the_model():
    cfg = load_config()
    assert cfg["drift"]["min_decline"] == 0.05
    assert cfg["lineage"]["multiple_testing"] == "holm"
    # the degeneracy tiers stay lists, which the Snakefile hashes
    assert cfg["degeneracy"]["tiers"] == [[8, "negligible"], [128, "moderate"], [4096, "high"]]


def test_every_in_code_fallback_matches_the_model():
    """The real guarantee. Deleting the fallbacks was tried and reverted: tests
    build partial config dicts by hand, so `cfg["key"]` breaks 115 of them, and
    the fallbacks are what makes a hand-built dict usable.

    So they stay, and this makes them harmless: every `cfg.get("key", literal)`
    over a key the model knows must use the model's default. Six had drifted --
    `min_decline` 0.0 against 0.05, `min_records_for_drift` 20 against the
    calibrated 15, `min_records_per_lineage` 20 against 30 in two places,
    `lineage.require_working_baseline` False against True, and
    `record_min_overhang_bp` 0 against 100 -- every one in the unsafe direction,
    and every one reachable only when its key is absent, which is what a typo
    does. A grep, not a type system, because that is what the hazard is.
    """
    import ast

    from assaywatch.settings import Settings

    # key -> default, for every leaf the model knows, as a flat name.
    want: dict[str, object] = {}
    for block, model in Settings.model_fields.items():
        ann = model.annotation
        sub = getattr(ann, "model_fields", None)
        if sub:
            for key, f in sub.items():
                want[key] = f.get_default(call_default_factory=True)
        else:
            want[block] = model.get_default(call_default_factory=True)

    # Keys whose name is ambiguous out of context, or read from a dict that is
    # not config at all. Each is a real collision, not a waiver:
    #   thermo     -- `Call.extra["thermo"]`, the per-call thermodynamic columns
    #   buffer_bp  -- `subcluster` reads a `cluster:` block that config.yaml does
    #                 not have (an open wave-3 item); `windows.buffer_bp` is a
    #                 different setting that happens to share the name
    SKIP = {
        "taxa",
        "levels",
        "batch",
        "engine",
        "alpha",
        "tiers",
        "sublineage",
        "thermo",
        "buffer_bp",
    }

    offenders = []
    for path in sorted((ROOT / "assaywatch").glob("*.py")):
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if not (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "get"
                and len(node.args) == 2
                and isinstance(node.args[0], ast.Constant)
                and isinstance(node.args[0].value, str)
            ):
                continue
            key = node.args[0].value
            if key not in want or key in SKIP:
                continue
            try:
                fallback = ast.literal_eval(node.args[1])
            except ValueError:
                continue  # a computed fallback, e.g. another config value
            if fallback != want[key]:
                offenders.append(
                    f"{path.name}:{node.lineno} {key} falls back to {fallback!r}, model says {want[key]!r}"
                )
    assert not offenders, "in-code defaults disagree with assaywatch.settings:\n  " + "\n  ".join(offenders)
