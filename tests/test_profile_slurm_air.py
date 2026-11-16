"""The Air's Slurm profile must ask only for what the Air's one node has.

On SLURM a rule's `resources:` become the `sbatch` request. A job asking for more
memory than any node offers is never started: it sits pending, and Snakemake waits
on it. The Air is one node with `RealMemory=5800` (MB) in its `slurm.conf`, read
with `scontrol show node` on 2026-11-15, and one partition, `debug`. Every rule the
Air half of a run sends to Slurm must fit under that, so every memory value this
profile sets is checked against it here (issue #21, spec #19).
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "profiles" / "slurm-air" / "config.yaml"

AIR_REAL_MEMORY_MB = 5800  # `scontrol show node` on the Air, 2026-11-15
AIR_CPUS = 4  # `CPUTot` in the same output
AIR_PARTITION = "debug"  # the Air's only partition, `sinfo`


def _default_resources(entries: list[str]) -> dict[str, str]:
    """`default-resources` is a list of `key=value` strings; return it as a dict.

    `["mem_mb=4000", 'slurm_partition="debug"']` -> {"mem_mb": "4000", ...}."""
    out = {}
    for entry in entries:
        key, _, value = entry.partition("=")
        out[key.strip()] = value.strip().strip('"')
    return out


@pytest.fixture(scope="module")
def profile() -> dict:
    return yaml.safe_load(PROFILE.read_text())


def test_runs_on_slurm_in_the_airs_partition(profile):
    assert profile["executor"] == "slurm"
    assert _default_resources(profile["default-resources"])["slurm_partition"] == AIR_PARTITION
    for rule, resources in profile["set-resources"].items():
        assert resources.get("slurm_partition", AIR_PARTITION) == AIR_PARTITION, rule


def test_no_rule_asks_for_more_cpus_than_the_air_has(profile):
    """`refseq_twins` declares 6 threads and `screen_archive` scales to
    `screen.max_workers` (16). On SLURM threads become `--cpus-per-task`, and a
    request larger than the node is never started, so the profile caps them."""
    assert profile["max-threads"] <= AIR_CPUS


def test_set_resources_is_the_two_level_mapping_snakemake_accepts(profile):
    """Snakemake 9.27 refuses a list per rule here ("Invalid set-resources format in
    profile. Expected two-level mapping"), found by the first dry run on the Air.
    The generic and Greene profiles were written in the list form and never run."""
    for rule, resources in profile["set-resources"].items():
        assert isinstance(resources, dict), f"{rule}: a list, not a mapping"


def test_no_memory_request_exceeds_the_airs_node(profile):
    mem_mb = {"default": int(_default_resources(profile["default-resources"])["mem_mb"])}
    for rule, resources in profile["set-resources"].items():
        if "mem_mb" in resources:
            mem_mb[rule] = int(resources["mem_mb"])
    too_big = {rule: mb for rule, mb in mem_mb.items() if mb > AIR_REAL_MEMORY_MB}
    assert not too_big, f"unschedulable on the Air: {too_big}"


def test_rules_that_ask_for_more_than_the_air_has_are_capped(profile):
    """`screen_archive` scales past 5800 MB on a retry, and `site_drift` and
    `figures` declare 6000, so each needs its own override or the Snakefile's value
    reaches `sbatch`. `collect_calls` declares nothing and was never measured; it
    carries a deliberate 5500 MB rather than the 4000 default."""
    capped = profile["set-resources"]
    for rule in ("screen_archive", "site_drift", "figures", "collect_calls"):
        assert "mem_mb" in capped.get(rule, {}), f"{rule} has no mem_mb cap"


def test_retries_are_not_wasted_on_requests_that_cannot_grow(profile):
    """The generic profile retries 3 times with a larger request each attempt.

    Here the caps are flat and already near the node's limit, so a retry asks for
    the same memory and fails the same way. One retry covers a transient failure.
    """
    assert profile["restart-times"] <= 1
