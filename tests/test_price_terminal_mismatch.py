"""`scripts/price_terminal_mismatch.py`: the overlay must not leak between arms.

The script scores the same bench rows under several `by_chemistry.conventional`
blocks in one process. `score.config_for` caches the merged scoring block on the
config dict it is handed, so a shallow copy would let the first arm's thresholds
answer for the second and the two arms would silently agree. That is exactly the
failure mode that makes a comparison look clean while measuring one rule twice, so
the isolation is pinned here rather than trusted.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

from assaywatch.score import config_for, load_config

ROOT = Path(__file__).resolve().parents[1]


def _module():
    spec = importlib.util.spec_from_file_location(
        "price_terminal_mismatch", ROOT / "scripts" / "price_terminal_mismatch.py"
    )
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_each_arm_sees_its_own_thresholds_and_the_base_config_is_untouched():
    mod = _module()
    base = load_config()
    shipped_penalty = base["scoring"]["primer_3prime_penalty"]

    loose = mod.with_override(base, {"primer_3prime_penalty": 2.0})
    tight = mod.with_override(base, {"primer_3prime_penalty": 3.0})

    # Resolving one arm must not answer for the other, nor write back onto `base`.
    assert config_for("conventional", loose)["scoring"]["primer_3prime_penalty"] == 2.0
    assert config_for("conventional", tight)["scoring"]["primer_3prime_penalty"] == 3.0
    assert base["scoring"]["primer_3prime_penalty"] == shipped_penalty
    assert not base["scoring"]["by_chemistry"], "the shipped config must stay empty"

    # And an override for one chemistry leaves every other chemistry alone.
    assert config_for("hydrolysis_probe", loose)["scoring"]["primer_3prime_penalty"] == shipped_penalty


def test_mcnemar_is_two_sided_and_ignores_the_concordant_pairs():
    mod = _module()
    assert mod.mcnemar_exact(0, 0) == 1.0
    assert mod.mcnemar_exact(5, 5) == 1.0
    # 6-0 is the bench result for the penalty drop: 2 * (1/2)**6.
    assert mod.mcnemar_exact(0, 6) == 0.03125
    assert mod.mcnemar_exact(6, 0) == mod.mcnemar_exact(0, 6), "direction must not matter"


def test_a_band_is_detect_or_reduced():
    """The shipped reading, held fixed here: `reduced` still puts product on a gel.

    The probe switch changes what counts as DETECTED for drift, per chemistry. It
    does not change what counts as a predicted band on a bench panel, where the
    arbiter is whether the paper saw one.
    """
    mod = _module()
    assert mod.BAND_CALLS == ("detect", "reduced")
