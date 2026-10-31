# Wave 5: config.yaml gets a schema, and six defaults lose their second home (2026-10-23)

Plan item 5.12.

## The gap

Registry entries got 537 lines of pydantic. The file that sets every threshold got
`yaml.safe_load` and one hand-written check over one sub-block.
`score.check_chemistry_overrides` stated the stakes exactly right:

> Both checks exist because the failure they catch is silent. A misspelled chemistry, or
> a misspelled key inside one, would simply never be applied: the run would succeed, the
> numbers would be the old ones, and the report would be indistinguishable from a
> recalibrated run.

That is true of all 67 keys. It checked two.

And every consumer read config as `cfg.get(key, literal)`, so each default had two homes.
Six had come apart, every one in the unsafe direction, every one reachable exactly when
its key goes missing — which is what a typo does:

| key | in code | in config.yaml |
|---|---|---|
| `drift.min_decline` | **0.0** — any statistically real fall is drift | 0.05 |
| `drift.min_records_for_drift` | 20 | 15 (calibrated 2026-10-21) |
| `lineage.min_records_per_lineage` | 20, in two modules — the value the calibration rejected | 30 |
| `lineage.require_working_baseline` | **False** | true |
| `amplicon.record_min_overhang_bp` | 0 | 100 |

## What was built

`assaywatch/settings.py`: one pydantic model per config block, every block
`extra="forbid"`, defaults in the model. `load_config` validates and then returns
`model_dump()`, because every consumer indexes a plain dict and the Snakefile puts the
config through `json.dumps` — the models are the contract, the dict is what travels.

```
>>> validated({**raw, "drift": {"min_dec1ine": 0.05}})
ValueError: config.yaml is not valid:
  drift.min_dec1ine: Extra inputs are not permitted
```

Beyond key names, it refuses incoherent **pairs** that are each individually fine:
`reduced_max` below `detect_max`, `amplicon.max_bp` below `min_bp`,
`max_window_months` below `recent_window_months`, non-ascending `degeneracy.tiers`.
`scoring.engine` and `lineage.multiple_testing` are `Literal`s, so a typo in a method
name is an error rather than a silent fallthrough.

`check_chemistry_overrides` moved to `settings.py` and the `Scoring` model calls it, so
there is one implementation of that rule and the model enforces it. It stays a
*collector* — returning every problem rather than raising on the first — because a
config with three mistakes should report three. `score` re-exports the name, where
callers and tests have always found it. Its notion of "is this a scoring key?" now comes
from the model's fields rather than from whichever keys the file happened to write, so an
override naming a key `config.yaml` omits is no longer wrongly rejected.

## Deleting the fallbacks was tried and reverted

Removing the `cfg.get(key, literal)` calls broke **115 tests**: they build partial config
dicts by hand, and the fallbacks are what makes a hand-built dict usable. So they stay,
corrected to the model's values, and
`tests/test_settings.py::test_every_in_code_fallback_matches_the_model` walks the AST of
every module in `assaywatch/` and fails on any `.get("key", literal)` whose literal
disagrees with the model. A grep, not a type system, because that is the shape of the
hazard.

It found three more the audit had missed:

- **`lineage_report.py` hardcoded `"docs/taxa-cache.json"`** while `report.py` reads the
  same key with no fallback. That is the exact shape of the `lineage.taxid_backfill` bug
  the audit found — a path with a second home, so the setting looks configurable and is
  not. Fixed to match `report.py`.
- `score.py`'s `Call.extra.get("thermo", {})` and `subcluster.py`'s
  `cfg.get("buffer_bp", 0)` are name collisions with dicts that are not config at all
  (`subcluster` reads a `cluster:` block `config.yaml` does not have — an open wave-3
  item). Both named in the test's skip list with the reason, not waived silently.

Two tests asserted the drifted values and had to be rewritten: one pinned
`min_records == 20` and one `gate is False`. A test pinning the wrong value is what made
the drift look intended.

## What it does not change

Verified before and after: **validation alters no value in the committed `config.yaml`**
— same 67 keys, same values, nothing added. That matters because the screen signature
hashes the `scoring` and `amplicon` blocks, so a silent change would have invalidated
457 MB of cached screens without saying so. `report.md` regenerates byte-identical to
the wave-2 run, and a test pins the no-change property so a future field default cannot
quietly move a shipped value.

`validated` raises `ValueError`, not `SystemExit`: an invalid value is something a
caller can catch, and this is library code — `drift.py` raising `SystemExit` for a bad
setting is a defect the audit recorded, not a pattern to copy. A *missing* config file
stays `SystemExit` in `load_config`, because that is about the environment and its
message is instructions.

Nothing in `settings.py` carries a justification for a *value*. Those stay beside the key
in `config.yaml`, with its citation or its admission of having none, which is still the
file to open to find out what a number is worth.
