"""Every key in config.yaml is read by something.

`lineage.taxid_backfill` was declared and read nowhere for three days, while the
path it names was hardcoded in `report.py` and `lineage_report.py` - so the
setting looked configurable, was not, and the audit had to find it by hand. It
was the only dead key of 73. This is the cheap check that keeps it that way:
config.yaml is where this project puts decisions, and a key nothing reads is
either a decision with no effect or a consumer with a hardcoded answer.

The match is deliberately crude - the key's name as a quoted literal anywhere in
the package, the scripts or the Snakefile. That cannot tell `cfg["lineage"]` from
the word "lineage" in a dict unrelated to config, so it under-reports. It is a
floor, not a proof, and it is enough to catch a key that nothing mentions at all.
"""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def key_paths(node: dict, path: tuple[str, ...] = ()) -> Iterator[tuple[str, ...]]:
    """Every key in the tree, as a dotted path."""
    for k, v in node.items():
        yield (*path, k)
        if isinstance(v, dict):
            yield from key_paths(v, (*path, k))


def sources() -> str:
    files = [*sorted((ROOT / "assaywatch").glob("*.py")), *sorted((ROOT / "scripts").glob("*.py"))]
    return "\n".join(p.read_text() for p in [*files, ROOT / "Snakefile"])


def mentioned(key: str, src: str) -> bool:
    return f'"{key}"' in src or f"'{key}'" in src


def test_no_config_key_is_read_by_nothing():
    cfg = yaml.safe_load((ROOT / "config.yaml").read_text())
    src = sources()
    dead = [".".join(p) for p in key_paths(cfg) if not mentioned(p[-1], src)]
    assert not dead, "declared in config.yaml and read nowhere:\n  " + "\n  ".join(dead)


def test_the_check_can_see_a_key_nothing_reads():
    """Without this, a bug in `mentioned` would make the test above vacuous."""
    assert not mentioned("taxid_backfill", 'sidecar = retrieved / ".meta.taxid.backfill.tsv.gz"')
    assert mentioned("taxid_backfill", 'lineage_cfg.get("taxid_backfill")')


def test_the_config_has_the_keys_this_check_is_worth_running_on():
    cfg = yaml.safe_load((ROOT / "config.yaml").read_text())
    assert len(list(key_paths(cfg))) > 50  # 73 on 2026-10-21; a near-empty config would pass vacuously
