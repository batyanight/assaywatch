"""The shape of config.yaml, and the one place its defaults live.

WHY THIS EXISTS. Registry entries get 537 lines of pydantic (`schema.py`), and
the file that sets every threshold got `yaml.safe_load` and one hand-written
check over one sub-block. `score.check_chemistry_overrides` explained the stakes
exactly right and then covered 2 keys of 73:

    Both checks exist because the failure they catch is silent. A misspelled
    chemistry, or a misspelled key inside one, would simply never be applied:
    the run would succeed, the numbers would be the old ones, and the report
    would be indistinguishable from a recalibrated run.

That is true of every key. `extra="forbid"` makes a typo anywhere a startup
error instead of a silently-ignored line.

AND IT CLOSES A DRIFT. Every consumer read config as `cfg.get(key, literal)`,
so each default had two homes and six had come apart -- `drift.min_decline`
0.0 in code against 0.05 in the file, `min_records_for_drift` 20 against 15,
`lineage.min_records_per_lineage` 20 against the calibrated 30 in two places,
`lineage.require_working_baseline` False against true, and
`amplicon.record_min_overhang_bp` 0 against 100. Each would have taken effect
only if its key went missing, which is exactly what a typo does, and each
differed in the unsafe direction: `min_decline: 0.0` flags any statistically
real fall as drift. `CLAUDE.md` says no scoring number lives in code; those
were six, hidden in `.get` calls.

Validating here means every key is always present downstream with the value
from this model, so the in-code literals can never be reached. They are being
removed as their modules are touched rather than in one sweeping diff; until
then they are inert.

WHAT THIS DELIBERATELY DOES NOT DO. It does not change what `load_config`
returns. Every consumer indexes a plain dict (`cfg["scoring"]["detect_max"]`,
`cfg.get("drift", {}).get(...)`) and the Snakefile passes it through
`json.dumps`, so `load_config` validates and then returns `model_dump()`. The
models are the contract; the dict is what travels.

Nothing here carries a justification for a VALUE. Those live beside the key in
config.yaml, with its citation or its admission of having none, and that is
still the file a reader should open to find out what a number is worth.
"""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from assaywatch.schema import Chemistry


class Block(BaseModel):
    """Every block forbids unknown keys. That is the whole point."""

    model_config = ConfigDict(extra="forbid")


def check_chemistry_overrides(cfg: dict[str, Any]) -> list[str]:
    """Problems with `scoring.by_chemistry`, as messages.

    Both checks exist because the failure they catch is silent. A misspelled
    chemistry, or a misspelled key inside one, would simply never be applied:
    the run would succeed, the numbers would be the old ones, and the report
    would be indistinguishable from a recalibrated run. A config that cannot be
    read as intended has to fail loudly.

    Kept as a COLLECTOR -- it returns every problem rather than raising on the
    first -- because a config with three mistakes should report three. The
    `Scoring` model calls it, so this is the single implementation of the rule
    and the model is what enforces it at load time. `score` re-exports the name,
    which is where callers and tests have always found it.
    """
    base = cfg.get("scoring") or {}
    by = base.get("by_chemistry")
    if not by:
        return []
    if not isinstance(by, dict):
        return [f"scoring.by_chemistry must map chemistry to overrides, got {type(by).__name__}"]
    problems = []
    known_chem = {str(c) for c in Chemistry}
    # The base block defines what a scoring key is, so this needs no upkeep.
    known_keys = {k for k in base if k != "by_chemistry"}
    for chem, override in sorted(by.items()):
        if chem not in known_chem:
            problems.append(
                f"scoring.by_chemistry.{chem}: not a chemistry in the schema; "
                f"expected one of {sorted(known_chem)}"
            )
        if override is None:
            continue
        if not isinstance(override, dict):
            problems.append(f"scoring.by_chemistry.{chem} must be a mapping, got {type(override).__name__}")
            continue
        for key in sorted(set(override) - known_keys):
            problems.append(
                f"scoring.by_chemistry.{chem}.{key}: not a key in `scoring`, so it would be ignored"
            )
    return problems


class Scoring(Block):
    primer_3prime_window: int = Field(default=5, ge=0)
    primer_3prime_penalty: float = Field(default=3.0, ge=0)
    primer_mid_window: int = Field(default=5, ge=0)
    primer_mid_penalty: float = Field(default=1.0, ge=0)
    primer_5prime_penalty: float = Field(default=0.5, ge=0)
    #: primer:template mispair -> multiplier on the position penalty. Keys are
    #: free-form ("G:T"), so this stays a dict; `mispair_multiplier` validates
    #: membership at use. Empty scores byte-identically to no table at all.
    mispair_penalty: dict[str, float] = Field(default_factory=dict)
    probe_center_penalty: float = Field(default=2.0, ge=0)
    probe_outer_penalty: float = Field(default=1.0, ge=0)
    max_ambiguous_per_oligo: int = Field(default=2, ge=0)
    max_mismatches_searched: int = Field(default=6, ge=0)
    max_site_evalue: float = Field(default=0.01, gt=0)
    max_pairs_per_record: int = Field(default=5000, gt=0)
    #: null means "report the E-value, act on nothing".
    max_pair_evalue: float | None = 0.01
    detect_max: float = Field(default=1.0, ge=0)
    reduced_max: float = Field(default=3.0, ge=0)
    terminal_mismatch_fails: bool = True
    engine: Literal["budget", "serial"] = "budget"
    oligo_ok_max: float = Field(default=1.0, ge=0)
    oligo_weak_max: float = Field(default=3.0, ge=0)
    #: Per-chemistry partial overrides of the keys above. Chemistry names are
    #: checked against the registry's own enum, and each override is validated
    #: as a Scoring block, so a misspelled key inside one is an error too --
    #: which is what `score.check_chemistry_overrides` was written to catch.
    by_chemistry: dict[str, dict[str, Any]] = Field(default_factory=dict)

    @model_validator(mode="after")
    def thresholds_are_ordered(self) -> Scoring:
        if self.reduced_max < self.detect_max:
            raise ValueError(f"reduced_max ({self.reduced_max}) is below detect_max ({self.detect_max})")
        if self.oligo_weak_max < self.oligo_ok_max:
            raise ValueError(
                f"oligo_weak_max ({self.oligo_weak_max}) is below oligo_ok_max ({self.oligo_ok_max})"
            )
        return self

    @model_validator(mode="after")
    def chemistry_overrides_are_scoring_keys(self) -> Scoring:
        """Delegates to `check_chemistry_overrides`, which collects every problem.

        The base block passed in is this model's own dump, so "is this a scoring
        key?" is answered by the model's fields rather than by whichever keys the
        file happened to write -- an override naming a key config.yaml omits is
        legitimate and used to be rejected.
        """
        problems = check_chemistry_overrides({"scoring": self.model_dump()})
        if problems:
            raise ValueError("; ".join(problems))
        for override in self.by_chemistry.values():
            if isinstance(override, dict) and override:
                # A bad VALUE in an override is caught here; the keys are checked above.
                Scoring(**{**self.model_dump(exclude={"by_chemistry"}), **override})
        return self


class Amplicon(Block):
    min_bp: int = Field(default=50, gt=0)
    max_bp: int = Field(default=3000, gt=0)
    declared_tolerance: float | None = Field(default=0.25, ge=0)
    record_min_overhang_bp: int = Field(default=100, ge=0)

    @model_validator(mode="after")
    def window_is_ordered(self) -> Amplicon:
        if self.max_bp <= self.min_bp:
            raise ValueError(f"amplicon.max_bp ({self.max_bp}) must exceed min_bp ({self.min_bp})")
        return self


class Retrieve(Block):
    page_size: int = Field(default=500, gt=0)
    page_target_bytes: int = Field(default=20_000_000, gt=0)
    min_length: int = Field(default=100, ge=0)
    max_length: int | None = None
    query_suffix: str | None = None
    max_records_per_taxon: int = Field(default=100_000, gt=0)
    incremental_overlap_days: int = Field(default=3, ge=0)
    #: Taxa opted past `max_records_per_taxon`, by taxid, one at a time.
    large_taxa_allowed: list[int] = Field(default_factory=list)


class Assemblies(Block):
    taxa: list[int] = Field(default_factory=list)
    levels: list[str] = Field(default_factory=lambda: ["complete_genome", "chromosome"])
    per_year: int = Field(default=20, gt=0)
    batch: int = Field(default=10, gt=0)
    max_pair_evalue: float = Field(default=0.01, gt=0)


class Windows(Block):
    buffer_bp: int = Field(default=300, ge=0)


class ThermoConditions(Block):
    mv_conc: float = Field(default=50, ge=0)
    dv_conc: float = Field(default=3.0, ge=0)
    dntp_conc: float = Field(default=0.8, ge=0)
    dna_conc: float = Field(default=250, ge=0)


class Degeneracy(Block):
    #: [[fold, label], ...] ascending. Anything above the last fold is the tier
    #: beyond it, which `tier()` names.
    tiers: list[tuple[int, str]] = Field(
        default_factory=lambda: [(8, "negligible"), (128, "moderate"), (4096, "high")]
    )

    @model_validator(mode="after")
    def tiers_ascend(self) -> Degeneracy:
        folds = [f for f, _ in self.tiers]
        if folds != sorted(folds):
            raise ValueError(f"degeneracy.tiers folds must ascend, got {folds}")
        return self


class Drift(Block):
    detect_fraction_threshold: float = Field(default=0.9, ge=0, le=1)
    recent_window_months: int = Field(default=24, gt=0)
    max_window_months: int = Field(default=60, gt=0)
    min_records_for_drift: int = Field(default=15, ge=0)
    min_records_for_coverage: int = Field(default=10, ge=0)
    scope_taxonomy: str | None = None
    min_decline: float = Field(default=0.05, ge=0, le=1)
    require_working_baseline: bool = True
    count_diverged_as_fail: bool = False
    exclude_patent_records: bool = False

    @model_validator(mode="after")
    def windows_are_ordered(self) -> Drift:
        if self.max_window_months < self.recent_window_months:
            raise ValueError(
                f"drift.max_window_months ({self.max_window_months}) is below "
                f"recent_window_months ({self.recent_window_months}); widening could only shrink"
            )
        return self


class SiteDrift(Block):
    min_records_for_position: int = Field(default=20, ge=0)
    top_footprints: int = Field(default=8, gt=0)


class Figures(Block):
    max_forest_rows: int = Field(default=40, gt=0)
    max_site_assays: int = Field(default=6, gt=0)


class Report(Block):
    #: How many assays the triage list at the top of the report may name. The
    #: point of the list is that a reader can act on all of it in one sitting;
    #: past a dozen it is another table. Not a scoring number -- it changes what
    #: leads the page, never a status.
    max_triage_rows: int = Field(default=10, gt=0)


class Lineage(Block):
    #: FWER, not FDR: the rule is "any lineage below threshold fails the assay",
    #: so what needs controlling is the chance of at least one false rejection.
    multiple_testing: Literal["holm", "bonferroni", "fdr_bh", "fdr_by"] = "holm"
    alpha: float = Field(default=0.05, gt=0, lt=1)
    min_records_per_lineage: int = Field(default=30, ge=0)
    taxa_cache: str | None = None
    taxid_backfill: str | None = None
    require_working_baseline: bool = True
    group_at_rank: Literal["species"] | None = "species"
    unclassified_is_bucket: bool = False
    #: Per-assay resolver chains; shape validated by `lineage.build_resolvers`.
    sublineage: dict[str, Any] = Field(default_factory=dict)


class Settings(Block):
    """config.yaml, whole."""

    registry_dir: str = "registry"
    retrieved_dir: str = "data/retrieved"
    results_dir: str = "results"
    scoring: Scoring = Field(default_factory=Scoring)
    amplicon: Amplicon = Field(default_factory=Amplicon)
    retrieve: Retrieve = Field(default_factory=Retrieve)
    assemblies: Assemblies = Field(default_factory=Assemblies)
    windows: Windows = Field(default_factory=Windows)
    thermo: bool = False
    thermo_conditions: ThermoConditions = Field(default_factory=ThermoConditions)
    degeneracy: Degeneracy = Field(default_factory=Degeneracy)
    drift: Drift = Field(default_factory=Drift)
    sitedrift: SiteDrift = Field(default_factory=SiteDrift)
    figures: Figures = Field(default_factory=Figures)
    report: Report = Field(default_factory=Report)
    lineage: Lineage = Field(default_factory=Lineage)


def validated(raw: dict[str, Any]) -> dict[str, Any]:
    """`raw` from YAML -> the same shape, defaults filled, unknown keys refused.

    Returns a plain dict because that is what every consumer and the Snakefile
    expect; the model is the contract, not the currency.

    Raises `ValueError`, not `SystemExit`. An invalid VALUE is something a
    caller can reasonably catch and report its own way, and this module is
    library code -- `drift.py` raising `SystemExit` for a bad setting is a
    defect recorded in the 2026-10-23 audit, not a pattern to copy. A MISSING
    config file is different and stays `SystemExit` in `load_config`: that is
    about the environment, not a value, and its message is instructions.
    """
    from pydantic import ValidationError

    try:
        settings = Settings(**raw)
    except ValidationError as e:
        lines = []
        for err in e.errors():
            where = ".".join(str(p) for p in err["loc"]) or "(root)"
            msg = err["msg"]
            # A nested block's own validator arrives wrapped as "Value error, ...";
            # the inner message is the useful part.
            lines.append(f"  {where}: {msg.removeprefix('Value error, ')}")
        raise ValueError("config.yaml is not valid:\n" + "\n".join(lines)) from None
    # `degeneracy.tiers` round-trips as tuples; the consumers unpack pairs, and
    # the Snakefile hashes the structure, so lists keep that hash stable.
    out = settings.model_dump()
    out["degeneracy"]["tiers"] = [list(t) for t in out["degeneracy"]["tiers"]]
    return out
