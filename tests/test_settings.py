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


def test_the_composition_block_carries_the_numbers_the_plan_and_the_measurement_set():
    """ROADMAP "Lineage composition over time". Pinned so a later edit to one of these is
    a visible decision rather than a drift; `cut` and `shape_quantile` are the two that
    were measured (step 4b), the rest are judgements justified in config.yaml."""
    d = Settings().model_dump()["composition"]
    assert d["flank_bp"] == 500
    assert d["shape_quantile"] == 0.1
    assert d["kmer_len"] == 15
    assert d["sample_cap"] == 2000
    assert d["cut"] == 0.05
    assert d["min_cluster_size"] == 3
    assert d["name_pure_share"] == 0.9
    assert d["show_clusters"] == 8
    assert d["n_boot"] == 2000
    assert d["report_min_mix"] == 0.05  # matches drift.min_decline
    assert d["site_max_bytes"] == 1_500_000
    assert d["coverage_refresh_years"] == 2
    assert validated({})["composition"] == d


def test_the_composition_block_is_in_the_committed_config():
    assert "composition" in raw(), "config.yaml has no composition: block"


def test_the_model_and_the_committed_config_hold_the_same_composition_keys():
    """Every key now has a reader, so the draft file is gone: `report_min_mix` landed at
    step 14, `site_max_bytes` at 15 and `coverage_refresh_years` at 17. `extra="forbid"`
    would refuse a config key the model lacks, and a model key the config lacks fails
    `test_validation_changes_no_value_in_the_committed_config`."""
    assert set(Settings().model_dump()["composition"]) == set(raw()["composition"])


def test_every_dataclass_and_signature_default_matches_the_model():
    """The fallback test above sees `cfg.get("key", literal)`. It cannot see a dataclass
    field or a keyword default that mirrors a config key under another name, and those
    are the same hazard: `AssayDrift.min_decline` still said 0.0 and `min_records` 20 on
    2026-11-09, the two values the module docstring of settings.py calls unsafe, reachable
    by any caller that builds the object without `from_config`. The alias table is the
    contract: a default that mirrors a key reads the model, and this test is what makes
    a new mirror declare itself."""
    import inspect

    from assaywatch import drift, lineage, lineage_report, report, site, sitedrift
    from assaywatch.settings import Settings

    model = Settings()
    mirrors: list[tuple[object, str, str]] = [
        (drift.AssayDrift, "threshold", "drift.detect_fraction_threshold"),
        (drift.AssayDrift, "min_records", "drift.min_records_for_drift"),
        (drift.AssayDrift, "min_decline", "drift.min_decline"),
        (drift.AssayDrift, "require_working_baseline", "drift.require_working_baseline"),
        (drift.AssayDrift, "min_records_for_year", "drift.min_records_for_coverage"),
        (drift.AssayDrift, "trend_min_years", "drift.trend_min_years"),
        (drift.AssayDrift, "flag_rule", "drift.flag_rule"),
        (drift.AssayDrift, "flag_credibility", "drift.flag_posterior_credibility"),
        (drift.AssayDrift, "lineage_method", "lineage.multiple_testing"),
        (drift.AssayDrift, "lineage_alpha", "lineage.alpha"),
        (drift.AssayDrift, "lineage_verdict_from", "lineage.verdict_from"),
        (drift.AssayDrift, "lineage_credibility", "lineage.posterior_credibility"),
        (drift.DriftSettings, "trend_min_years", "drift.trend_min_years"),
        (drift.DriftSettings, "flag_rule", "drift.flag_rule"),
        (drift.DriftSettings, "flag_credibility", "drift.flag_posterior_credibility"),
        (drift.AssayDrift._lineage_check, "min_records_for_year", "drift.min_records_for_coverage"),
        (lineage.per_lineage_stats, "min_records", "lineage.min_records_per_lineage"),
        (lineage_report.render_lineage_report, "min_records", "lineage.min_records_per_lineage"),
        (lineage_report.render_lineage_report, "threshold", "drift.detect_fraction_threshold"),
        (lineage_report.render_lineage_report, "thin_of_best", "composition.coverage_thin_of_best"),
        (report.ReportModel, "composition_min_mix", "composition.report_min_mix"),
        (site.AssayPage, "threshold", "drift.detect_fraction_threshold"),
        (sitedrift.AssaySites, "lead_min_share", "sitedrift.lead_min_share"),
        (sitedrift.analyse_assay, "min_records", "sitedrift.min_records_for_position"),
        (sitedrift.analyse_assay, "top_footprints", "sitedrift.top_footprints"),
        (sitedrift.analyse_assay, "cover", "sitedrift.replacement_covers"),
        (sitedrift.analyse_assay, "three_prime_zone", "scoring.primer_3prime_window"),
        (sitedrift.analyse_assay, "lead_min_share", "sitedrift.lead_min_share"),
    ]

    def default_of(obj: object, name: str) -> object:
        if inspect.isclass(obj):
            return obj.__dataclass_fields__[name].default
        return inspect.signature(obj).parameters[name].default

    offenders = []
    for obj, name, key in mirrors:
        block, leaf = key.split(".")
        want = getattr(getattr(model, block), leaf)
        have = default_of(obj, name)
        if have != want:
            offenders.append(f"{getattr(obj, '__qualname__', obj)}.{name} = {have!r}, model {key} = {want!r}")
    assert not offenders, "\n".join(offenders)
