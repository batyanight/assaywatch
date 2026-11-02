# AssayWatch pipeline.
#
#     snakemake --cores 4 --config email=you@example.org
#     snakemake --profile profiles/slurm --config email=...   # on a cluster
#
# Why a workflow manager at all: Snakemake tracks which inputs produced which
# outputs, so a failed run resumes from what finished, and a new week's run
# screens only the archives that are new. The same Snakefile runs on a laptop
# and on SLURM with a different --profile.
#
# State and outputs are kept strictly apart, and that distinction is the
# important design point here. Snakemake deletes a rule's declared outputs
# before running it. Anything that must outlive one run (the retrieval
# manifest, the sequence archives) is therefore never declared as an output:
# the retrieve step's output is a small per-day run record, and the manifest
# beside it is state the retrieve code manages itself. Declaring the manifest
# as an output is how the first two pipeline runs each erased the fetch
# history.
#
# Reports are cumulative. Every archive ever fetched is screened once, the
# result is cached under results/screened/ keyed by the archive's own name,
# and each report is built from all of them, with the newest version of each
# accession winning. A group with nothing new this week still appears in the
# report, and next week only the new archives are screened.
#
# `retrieve` is a checkpoint: which archives exist is not known until it has
# run, so the job graph is re-evaluated after it finishes.

import hashlib
import functools
import json
import os
import subprocess
import yaml
from collections import Counter
from datetime import date
from pathlib import Path

from assaywatch.collect import concatenate_screens, stem_order
from assaywatch.credentials import require_contact_email
from assaywatch.assemblies import cut_parameters
from assaywatch.retrieve import targets_from_registry
from assaywatch.timing import (
    RunManifest,
    clear_run_marker,
    heartbeat,
    resolve_run_date,
    screen_core_seconds,
    screen_workers,
    screening_progress,
    write_run_marker,
)
from assaywatch.settings import Settings
from assaywatch.signature import screen_key
from assaywatch.triggers import source_names
from assaywatch.validate import iter_files, load_assay, not_live_because

configfile: "config.yaml"

# Falling back to `contact_email()` rather than to None. `config.get("email")`
# alone interpolated the literal string "None" into the retrieve shell command
# when --config email= was omitted, and `retrieve.py`'s --email is required=True
# so argparse accepted it: NCBI was told the caller's contact address was
# "None". That is worse than failing, because the address exists so NCBI can
# warn a caller before blocking the IP, and a blocked IP affects everyone at the
# institution. `require_contact_email` raises SystemExit naming the three ways to
# set one, which is the right behaviour at parse time — a run that cannot
# identify itself should not start.
EMAIL = config.get("email") or require_contact_email("--config email=")
RETRIEVED = Path(config.get("retrieved_dir", "data/retrieved"))
RESULTS = Path(config.get("results_dir", "results"))
SCREENED = RESULTS / "screened"
# Per-job wall time and max RSS (timekeeping item 2,
# docs/journal/2026-10-18-pipeline-timekeeping-todo.md). Deliberately NOT under
# RESULTS/RUN_DATE: a screen is cached across runs, so a date-keyed benchmark
# would be absent for every cached archive on the next run, and the whole point
# of the cache is that those 330 jobs do not re-execute. Keyed by the archive
# instead, so a benchmark exists exactly where its screen does and a rescreen
# refreshes it. Snakemake's benchmark TSV carries no timestamp of its own, so
# when a measurement was taken is the file's mtime - the same evidence
# `screened_at` rests on.
#
# ON THIS LAPTOP THESE RECORD WALL TIME ONLY, and that is not a bug to chase.
# Snakemake samples with psutil's `memory_full_info()`, which macOS refuses for
# a child process (AccessDenied, verified 2026-10-22), and its sampling loop
# skips a process it cannot read without ever setting `data_collected` - so
# max_rss/vms/uss/pss, the io counters and cpu_time all read NA however long the
# job runs. psutil's plain `memory_info()` does work here, so this is
# Snakemake's choice of the uss/pss-capable call, not macOS being unable to
# report RSS. On Linux - CI, and Greene - the memory columns do fill in, which
# is where the `mem_mb` guesses below are worth checking against.
BENCH = RESULTS / "benchmarks"
REGISTRY = config.get("registry_dir", "registry")
# The run's date is pinned ONCE and reused by every later process of the same
# run, including a resume after a failure (assaywatch/timing.py explains the
# resolution order). It used to be `date.today()` evaluated here, which is a
# bug with a two-hour fuse: the 2026-10-17 run started at 22:49, crossed
# midnight, re-fired retrieval against the new date and wrote
# data/retrieved/runs/2026-10-18.json while the targets still pointed at
# results/2026-10-17/. Every screen was cached and correct; the run failed on
# a MissingOutputException anyway.
_STATE_DIR = Path(workflow.basedir) / ".snakemake"
# Read-only at parse time: this code also runs on `snakemake -n`, and a dry run
# must not pin a date. The marker is written in `onstart`, which Snakemake does
# not fire on a dry run.
RUN_DATE, RUN_DATE_REASON = resolve_run_date(config, _STATE_DIR)
# Retrieval's run record is named for the SAME pinned date, so a fetch that
# starts before midnight and finishes after it stays one run record instead of
# starting a second one halfway through.
TODAY = RUN_DATE

# The merged config, written in onstart and passed to every subprocess so that a
# --config / --configfile override actually reaches the code. See onstart.
CONFIG_EFFECTIVE = RESULTS / RUN_DATE / "config.effective.yaml"
THERMO = str(config.get("thermo", False)).lower() in ("1", "true", "yes")

# Only an assay with a verified DOI goes live. The validator enforces this in CI and
# pre-commit; checking here as well means a hand-edited registry cannot be screened.
_not_live = [
    f"{p.name}: {why}" for p in iter_files(Path(REGISTRY)) if (why := not_live_because(load_assay(p)))
]
if _not_live:
    raise SystemExit("registry entries without a verified DOI:\n  " + "\n  ".join(_not_live))

# {(taxid, group): {"name", "query", "assays"}} from the registry as it stands.
GROUPS = targets_from_registry([Path(REGISTRY)], config)
# Every assay id this run screens; collect_calls refuses any other.
CURRENT_ASSAYS = frozenset(a for g in GROUPS.values() for a in g["assays"])

# What `status` each screened assay carried AT RUN TIME, for the provenance
# sidecar. `active` is not a fixed property: 178 entries were promoted on
# 2026-10-24, so a report from before that says "180 draft, 1 active" and a
# reader cannot tell WHICH entries those were, because the registry has moved on
# since. `git_commit` does not rescue it either -- it is often `(dirty)`, and the
# 2026-10-24 promotion landed after the run it would have to explain. Recorded as
# a map rather than a count so "was this assay active for that run" is answerable
# from the run's own files.
STATUS_AT_RUN = {
    a.id: a.status.value
    for p in iter_files(Path(REGISTRY))
    if (a := load_assay(p)).id in CURRENT_ASSAYS
}

# What a cached screen depends on besides its archive: the group's assay files,
# the scoring settings and the screening code. Its hash is a param of
# screen_archive, so editing an assay, changing a threshold or upgrading the
# matcher rescreens exactly the archives affected, with no `-R` to remember.
# The code is screen.py and everything it imports (assaywatch/triggers.py works
# that out from the source). It used to be a hand-kept list, and the list missed
# schema.py, which owns Oligo.matching_seq, tail_5prime and seq_as_written, and
# validate.py, which decides what loads at all, so editing either rescreened
# nothing.
_CODE = source_names("screen")
_SCREEN_CFG = {k: config.get(k) for k in ("scoring", "amplicon", "degeneracy", "thermo_conditions")}
_code_hash = hashlib.sha1(
    b"".join((Path(workflow.basedir) / "assaywatch" / f).read_bytes() for f in _CODE)
    + json.dumps(_SCREEN_CFG, sort_keys=True, default=str).encode()
).hexdigest()


def screen_signature(taxid, group):
    """What a cached screen depends on besides its archive.

    Snakemake reruns a job when an input or a param changes, and a screen's only
    input is the FASTA — so without this, editing an assay or a scoring threshold
    left stale results in place. Anything that can change a call belongs in here:
    miss one (schema.py, which owns Oligo.matching_seq, was missed at first) and
    the pipeline silently reports yesterday's answers.

    IT HASHES EACH ENTRY'S SCREEN-RELEVANT FIELDS, NOT ITS BYTES (2026-10-28).
    Hashing the file meant a curator's note, a review flag's wording or a
    `conditions` block invalidated every group holding that entry, and the measured
    cost of that was 312 of 494 cached screens stale after two days of curation in
    which no sequence, amplicon or query changed. `signature.screen_key` keeps the
    fields a call can depend on and drops provenance prose; the projection is listed
    and justified there, and pinned against the schema by a test, because leaving a
    field out is the dangerous direction.
    """
    h = hashlib.sha1(_code_hash.encode())
    for aid in sorted(GROUPS[(taxid, group)]["assays"]):
        h.update(screen_key(yaml.safe_load((Path(REGISTRY) / f"{aid}.yaml").read_text())))
    return h.hexdigest()[:16]


# stem_order lives in assaywatch/collect.py with collect_calls' logic, so both
# can be tested: archives are concatenated oldest first, and `_10` must sort
# after `_2`, so that the newest version of an accession survives deduplication.


def _git_commit():
    """`<sha> (dirty)` for the working tree, or "" when git cannot say.

    Recorded in the calls sidecar because the code hash alone identifies the
    screening path, not the rest of the tree that produced a run. Never raises:
    provenance that fails a run is worse than provenance that is blank, and a
    release tarball with no .git is a legitimate way to run this.
    """
    try:
        out = subprocess.run(
            ["git", "-C", str(workflow.basedir), "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if out.returncode != 0:
            return ""
        sha = out.stdout.strip()
        changed = subprocess.run(
            ["git", "-C", str(workflow.basedir), "status", "--porcelain"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        return f"{sha} (dirty)" if changed.stdout.strip() else sha
    except Exception:
        return ""


def _package_hash(*names):
    """Hash of assaywatch/<name> files, for use as a param.

    Snakemake reruns a `run:` block when its own code changes, but not a `shell:`
    command's module, and not logic that has been moved out of a `run:` block
    into a module (collect_calls did exactly that, so editing the module stopped
    rerunning the rule). A rule's modules therefore travel as a param: edit the
    code and the rule is listed for rerun, with no `-R` to remember.

    Which files, is `assaywatch.triggers.source_names`: the module a rule runs
    plus everything it imports, derived from the source rather than listed by
    hand (the hand-kept screening list above missed schema.py and validate.py).
    """
    h = hashlib.sha1()
    for name in names:
        h.update(name.encode() + b"\0")
        h.update((Path(workflow.basedir) / "assaywatch" / name).read_bytes())
    return h.hexdigest()[:16]


def _registry_and_config_hash(*config_keys):
    """Every registry file plus the named config sections, for rules that read both."""
    h = hashlib.sha1()
    for path in sorted(iter_files(Path(REGISTRY))):
        h.update(path.name.encode() + b"\0")
        h.update(path.read_bytes())
    h.update(json.dumps({k: config.get(k) for k in config_keys}, sort_keys=True, default=str).encode())
    return h.hexdigest()[:16]


# report.py reads the drift and degeneracy settings and every assay's metadata (names,
# citations, status); degeneracy.py reads the registry and its tier settings. Neither names
# the registry as an input, so it travels as a param. `scoring` and `amplicon` are hashed
# into the report's params only because the report loads the whole config through
# score.load_config, which validates them (a malformed by_chemistry stops the report); its
# numbers do not depend on them, and a scoring edit reruns the screens and so the report
# anyway.
_COLLECT_CODE = _package_hash(*source_names("collect"))
_REPORT_PARAMS = {
    "code": _package_hash(*source_names("report")),
    # "lineage": the per-lineage check (min_records_per_lineage, sublineage chains)
    # can override a verdict, so the report depends on it too.
    "inputs": _registry_and_config_hash("drift", "degeneracy", "scoring", "amplicon", "lineage"),
}
_DEGENERACY_PARAMS = {
    "code": _package_hash(*source_names("degeneracy")),
    "inputs": _registry_and_config_hash("degeneracy"),
}
_SITEDRIFT_PARAMS = {
    "code": _package_hash(*source_names("sitedrift")),
    # The site report selects which assays to describe by drift status, so a
    # change to the drift settings changes its contents as well as the report's.
    "inputs": _registry_and_config_hash("drift", "sitedrift", "scoring", "amplicon", "lineage"),
}
_LINEAGE_PARAMS = {
    "code": _package_hash(*source_names("lineage_report")),
    "inputs": _registry_and_config_hash("lineage"),
}
# figures.py runs both assessments itself rather than parsing the rendered
# documents, so it depends on everything either of them depends on. source_names
# follows the imports and picks that up without the list being kept by hand.
_FIGURES_PARAMS = {
    "code": _package_hash(*source_names("figures")),
    "inputs": _registry_and_config_hash("drift", "sitedrift", "scoring", "amplicon", "lineage", "figures"),
}


wildcard_constraints:
    taxid=r"\d+",
    group=r"all|asm|q[0-9a-f]{10}",
    stem=r"\d{4}-\d{2}-\d{2}(_\d+)?",


# Retrieval needs the internet, which cluster compute nodes often lack.
localrules: retrieve


# --------------------------------------------------------------------------
# Wall-clock instrumentation.
#
# The 2026-10-17 run could not be monitored: Snakemake's "N of 249 steps"
# weights a one-second validate the same as a 24,000-record poxvirus screen, so
# the percentage sat near 99% through the slow part, and `pgrep`/`ps` were
# unavailable in the sandbox, so "is it alive" had no answer except watching a
# directory grow by hand.
#
# The manifest records stage wall times and survives a crash (it is rewritten
# after every change). The heartbeat answers "alive?" and "stuck?" from a file,
# and carries a size-weighted ETA rather than a step count.
#
# None of this touches the screening code or its imports, so the screen cache
# is unaffected: instrumenting `screen.py` would change `_code_hash` and
# rescreen all 246 archives to gain a log line.
# --------------------------------------------------------------------------

_MANIFEST = RunManifest(
    run_date=RUN_DATE,
    run_date_reason=RUN_DATE_REASON,
    path=RESULTS / RUN_DATE / "run-timing.json",
)
# A dict rather than a module-level name, because the onstart/onsuccess blocks
# are executed as separate code objects and rebinding a bare global from inside
# one of them is not reliable across Snakemake versions.
_HB = {}


onstart:
    # Pin the date now, not at parse time: a real run has started, so the folder
    # is decided and a later process of the same run must reuse it.
    write_run_marker(RUN_DATE, _STATE_DIR)
    (RESULTS / RUN_DATE).mkdir(parents=True, exist_ok=True)
    Path(".tmp").mkdir(exist_ok=True)
    # Dump the MERGED config -- config.yaml plus any --configfile plus any
    # --config key=value -- and hand that file to every subprocess.
    #
    # Until 2026-10-27 no rule passed a config path at all (except
    # lineage_analysis, which hardcoded `--config config.yaml`), so every module
    # called load_config(None) and read DEFAULT_CONFIG, the repo's own
    # config.yaml, whatever Snakemake had been given. An override therefore moved
    # the params hash, rescreened all ~335 archives for hours, produced
    # byte-identical results, and recorded the overridden hash as having produced
    # them -- decoupling the invalidation signal from the rules actually applied,
    # which is the failure collect.py's docstrings say burned this project twice.
    #
    # Deliberately NOT declared as an input of any rule. Its content is already
    # hashed into _code_hash via _SCREEN_CFG and into the report/sitedrift/lineage
    # params, so a real change already invalidates the right jobs; declaring a new
    # input would instead invalidate every cached screen once, for nothing.
    # Filtered to the keys `Settings` knows, NOT the raw merged dict. settings.py
    # sets extra="forbid", and Snakemake's `config` also carries workflow-only
    # keys -- `email` (always, from --config email=...), plus heartbeat_seconds
    # and stall_seconds if set -- which are consumed by this file and are fields
    # on no model. Dumping them verbatim makes score.load_config raise
    # "Extra inputs are not permitted" and would break EVERY rule on the next
    # live run; confirmed by trying it on 2026-10-27 before shipping it. The
    # split is the real distinction: these three configure the workflow, the
    # other 17 blocks configure the code.
    _effective = {k: v for k, v in config.items() if k in Settings.model_fields}
    Path(CONFIG_EFFECTIVE).write_text(yaml.safe_dump(_effective, sort_keys=True))
    _MANIFEST.start_stage("workflow")
    _HB["stop"] = heartbeat(
        Path(".tmp") / f"heartbeat-{RUN_DATE}.json",
        screening_progress(RETRIEVED, SCREENED),
        interval=float(config.get("heartbeat_seconds", 60)),
        stall_after=float(config.get("stall_seconds", 900)),
    )
    print(
        f"[assaywatch] run {RUN_DATE} ({RUN_DATE_REASON}); "
        f"heartbeat .tmp/heartbeat-{RUN_DATE}.json; "
        f"timing {RESULTS / RUN_DATE / 'run-timing.json'}"
    )


onsuccess:
    if _HB.get("stop"):
        _HB["stop"]()
    _MANIFEST.end_stage("workflow")
    _MANIFEST.finish("success")
    # Only a SUCCESSFUL run clears the pin. After a failure the marker is left
    # so the next invocation is treated as a resume and writes to the same
    # folder instead of starting a second one.
    clear_run_marker(_STATE_DIR)
    print("\n".join(_MANIFEST.summary_lines()))


onerror:
    if _HB.get("stop"):
        _HB["stop"]()
    _MANIFEST.finish("failed")
    print("\n".join(_MANIFEST.summary_lines()))
    print(
        f"[assaywatch] run date {RUN_DATE} stays pinned; rerunning resumes into "
        f"the same folder."
    )


rule all:
    input:
        RESULTS / RUN_DATE / "report.html",
        RESULTS / RUN_DATE / "degeneracy.tsv",
        RESULTS / RUN_DATE / "site-drift.md",
        RESULTS / RUN_DATE / "lineage.md",
        RESULTS / RUN_DATE / "figures" / "figures.html",


rule validate:
    """Fail early: a malformed registry entry should stop the run, not the report."""
    input:
        registry=REGISTRY,
    output:
        touch(RESULTS / RUN_DATE / ".registry-valid"),
    shell:
        "assaywatch validate {input.registry}"


checkpoint retrieve:
    """Fetch new records for every group. Output is today's run record, never the manifest.

    One job for all groups, because NCBI's rate limit is global: parallel jobs
    would each sleep for their own limit and together exceed it.
    """
    input:
        RESULTS / RUN_DATE / ".registry-valid",
    output:
        run=RETRIEVED / "runs" / f"{TODAY}.json",
    params:
        # Which groups the registry asks for. Without this, retrieval ran at most
        # once a day (its output is the day's run record), so a group added or
        # re-scoped later that day got no data until tomorrow. Existing groups
        # stay incremental; only new ones are fetched in full.
        groups=hashlib.sha1(
            repr(sorted((t, g, str(v["query"])) for (t, g), v in GROUPS.items())).encode()
        ).hexdigest()[:16],
        # The settings that decide how a genome is cut down to its candidate amplicons.
        # Changing one has to rerun retrieval, or `asm` archives stay cut at the old
        # settings until something else happens to rerun it (see cut_parameters).
        cut=hashlib.sha1(json.dumps(cut_parameters(config), sort_keys=True).encode()).hexdigest()[:16],
    # The email is read from config in the command, not passed as a param: a
    # params change reruns the rule, and a different contact address is no
    # reason to fetch again.
    # Per-day, like the rule's own output: retrieval is one job for all groups,
    # and it is the stage that has run for hours (the 2026-10-17 PANPOX stall).
    # A date-keyed path costs nothing here because the output is date-keyed too.
    benchmark:
        BENCH / "retrieve" / f"{TODAY}.tsv"
    shell:
        "assaywatch retrieve {REGISTRY} --email {EMAIL} --run-record {output.run} "
        "--config {CONFIG_EFFECTIVE}"


def archives(wildcards):
    """Every archive on disk for a group the registry still asks for, oldest first."""
    checkpoints.retrieve.get()
    out = []
    for (taxid, group) in sorted(GROUPS):
        for fasta in sorted((RETRIEVED / str(taxid) / group).glob("*.fasta.gz"), key=stem_order):
            stem = fasta.name[: -len(".fasta.gz")]
            out.append(SCREENED / str(taxid) / group / f"{stem}.tsv")
    return out


def archive_signatures(wildcards):
    """The .sig beside each screen, requested so that a missing one is REBUILT.

    Declaring the .sig as an output of screen_archive is necessary and not
    sufficient: Snakemake only rebuilds a file something asks for, and until
    2026-10-27 nothing did. So a screen whose .sig was gone -- a kill between
    screen.py's rename and its signature write, a restore, a .tsv copied from
    another checkout -- left the .tsv that collect_calls requests present and up
    to date, Snakemake said "nothing to be done", and `collect_calls` then HARD
    RAISED on the unsigned screen. No rerun could fix it, because the only file
    in the DAG was already there; the archive's .tsv had to be deleted by hand.
    Verified both ways on 2026-10-27: with the .sig missing, asking for the .tsv
    gives "Nothing to be done" while asking for the .sig schedules the rescreen.
    """
    return [f"{p}.sig" for p in archives(wildcards)]


def archive_mb(input):
    """Gzipped size of the archive. input.size_mb is async in Snakemake 9 and
    cannot be used for threads or priority, so read the size directly."""
    return os.path.getsize(input.fasta) / 1e6


@functools.lru_cache(maxsize=1)
def _archive_records():
    """{fasta path: records fetched} from the retrieval manifest, read once.

    The manifest is state the retrieve step manages (see the header), and this
    only reads it. It is the one place a record count exists without
    decompressing an archive, which a DAG build cannot afford 335 times over.
    Missing or unreadable -> empty, and `screen_cost` falls back to the size
    terms alone.
    """
    try:
        runs = json.loads((RETRIEVED / "manifest.json").read_text()).get("runs", [])
    except (OSError, ValueError):
        return {}
    return {r["fasta"]: r.get("n_fetched") for r in runs if r.get("fasta")}


def screen_threads(wc, input):
    """Workers for one screening job, from its predicted cost. A named function
    rather than a lambda because a rule body takes only a single-line one."""
    return screen_workers(
        archive_mb(input),
        _archive_records().get(str(input.fasta)),
        len(GROUPS[(int(wc.taxid), wc.group)]["assays"]),
        config,
    )


def screen_cost(wc, input):
    """Predicted core-seconds to screen this archive against its group's assays.

    Sizes both `threads` and `priority`, so the two cannot disagree about which
    job is expensive -- the fault being fixed here was partly that `priority`
    ranked a 52-second archive near the back of the queue because it was 10 MB.
    """
    records = _archive_records().get(str(input.fasta))
    assays = len(GROUPS[(int(wc.taxid), wc.group)]["assays"])
    return screen_core_seconds(archive_mb(input), records, assays, config)


rule screen_archive:
    """Score one archive against the assays that requested its group. Cached across runs."""
    input:
        fasta=RETRIEVED / "{taxid}" / "{group}" / "{stem}.fasta.gz",
    output:
        calls=SCREENED / "{taxid}" / "{group}" / "{stem}.tsv",
        # The .sig is written by the same shell command and `collect` HARD-RAISES
        # on any screen lacking one, so it has to be declared. Undeclared,
        # Snakemake could neither notice a missing .sig nor rebuild it: the .tsv
        # it tracks is present and current, so no rerun regenerated the .sig and
        # every run died in collect_calls until the .tsv was deleted by hand.
        # Reachable without a bug -- a kill between screen.py's rename and its
        # signature write, a restore, or a .tsv copied from another checkout.
        sig=SCREENED / "{taxid}" / "{group}" / "{stem}.tsv.sig",
    params:
        # A params change re-triggers the job, so adding an assay to a group
        # rescreens that group's archives on the next run.
        only=lambda wc: ",".join(sorted(GROUPS[(int(wc.taxid), wc.group)]["assays"])),
        # Turning thermo on or off changes the params, so cached screens are redone.
        thermo="--thermo" if THERMO else "",
        signature=lambda wc: screen_signature(int(wc.taxid), wc.group),
    # Both from predicted work, so the expensive jobs get the workers AND start
    # first. Sizing on gzipped bytes alone, as this did until 2026-10-23, gave one
    # worker and near-bottom priority to a 10 MB archive of 190,101 records that
    # cost 52 s, while a 760 MB archive needing one assay's work got sixteen: cost
    # scales with bytes TIMES the number of assays in the group, which is what the
    # old rule left out. Measured in docs/journal/2026-10-18-pipeline-timekeeping-todo.md;
    # the fit is assaywatch.timing.screen_core_seconds, and its constants live in
    # config.yaml under `screen:`. Snakemake caps threads at --cores.
    #
    # Neither value is in the screen signature, because neither changes a screen's
    # output. Note what that does and does not buy: resizing a job on its own
    # reruns nothing, but ADDING the settings block that holds these constants did
    # rerun all 335 screens, because settings.py is inside screen.py's import
    # closure and so is hashed into `_code_hash`. The trigger is conservative by
    # design: a module that COULD change a call must invalidate, whether or not
    # this one does. screen.py never reads the `screen:` block, so the rescreen it
    # forced is expected to reproduce every screen byte for byte.
    threads: screen_threads
    priority: lambda wc, input: int(screen_cost(wc, input))
    resources:
        # Scaled by `attempt` so a retry asks for more than the request that was
        # just killed. On SLURM resources ARE the sbatch request, and these
        # constants were fitted on a dev Mac where max_rss is never measured, so
        # an under-request is the likely failure and a flat value made every
        # retry fail identically. Locally `attempt` is 1 and this is unchanged.
        mem_mb=lambda wc, input, threads, attempt: (2000 + 500 * threads) * attempt,
        runtime=lambda wc, attempt: 240 * attempt,
    # Mirrors output.calls rather than the run date, for the reason given at
    # BENCH. This is what made `threads` and `priority` above checkable, and then
    # correctable: the 2026-10-23 benchmarks are what the cost model is fitted on.
    benchmark:
        BENCH / "screen" / "{taxid}" / "{group}" / "{stem}.tsv"
    shell:
        # --signature writes params.signature to <output>.sig. It was already a
        # param, which reruns the job when it changes — but only where Snakemake
        # holds a metadata record for the output to compare against. The
        # 2026-10-21 run found 20 screens with no such record, where the params
        # check could not fire and a changed code hash did not invalidate them.
        # On disk it is checkable by `collect` whatever Snakemake remembers.
        "assaywatch screen {REGISTRY} {input.fasta} --only {params.only} "
        "--workers {threads} {params.thermo} --signature {params.signature} -o {output.calls} "
        "--config {CONFIG_EFFECTIVE}"


rule collect_calls:
    """Concatenate every cached screen, oldest archive first so the newest version wins."""
    input:
        calls=archives,
        # Not consumed by concatenate_screens; requested so Snakemake rebuilds a
        # screen whose signature has gone missing. See archive_signatures.
        sigs=archive_signatures,
    output:
        RESULTS / RUN_DATE / "calls.tsv.gz",
    params:
        # The logic is in a module, so Snakemake's own code trigger no longer sees
        # it; see _package_hash.
        code=_COLLECT_CODE,
        # The set it checks ids against: a rename must re-run the check.
        assays=hashlib.sha1(",".join(sorted(CURRENT_ASSAYS)).encode()).hexdigest()[:16],
    run:
        # The logic is in assaywatch/collect.py, where it is tested. It reconciles
        # a cached screen made before a column was added with one made after,
        # writing rows by column name, since plain concatenation would shift the
        # older rows a column sideways. It also refuses a screen holding an assay
        # id the run no longer screens (renamed, removed, deprecated): a stale
        # cached screen that would otherwise be double-counted in every report.
        # The sidecar (calls.provenance.json) is written in the same pass: a calls
        # table could not say what produced it, which is why establishing that
        # results/2026-10-18/ ran under a since-reverted scoring override took
        # noticing a commit three minutes after the run finished.
        concatenate_screens(
            # input.calls, not list(input): `input` now also carries the .sig
            # paths, which are a rebuild dependency and not screens to read.
            list(input.calls),
            output[0],
            known_ids=CURRENT_ASSAYS,
            expected_signatures={f"{t}/{g}": screen_signature(t, g) for t, g in GROUPS},
            provenance={
                "run_date": RUN_DATE,
                "extra": {
                    "screen_code_and_config_sha1": _code_hash,
                    "collect_code_sha1": _COLLECT_CODE,
                    "thermo": THERMO,
                    "assays_screened": len(CURRENT_ASSAYS),
                    "git_commit": _git_commit(),
                    # Counts for reading, the map for answering.
                    "status_counts_at_run": dict(sorted(Counter(STATUS_AT_RUN.values()).items())),
                    "status_at_run": dict(sorted(STATUS_AT_RUN.items())),
                },
            },
        )


rule site_drift:
    """Which oligo positions are failing, and in which groups of accessions.

    Reads only the calls table the report already depends on, so it adds no
    screening work. Separate from `report` because it answers a different
    question (where on the primer, and in which records) and is the slower of
    the two: it re-reads the calls table keeping the mismatch columns that
    `report.read_calls` deliberately folds away.
    """
    input:
        calls=RESULTS / RUN_DATE / "calls.tsv.gz",
    output:
        md=RESULTS / RUN_DATE / "site-drift.md",
        tsv=RESULTS / RUN_DATE / "site-drift.tsv",
    params:
        code=_SITEDRIFT_PARAMS["code"],
        inputs=_SITEDRIFT_PARAMS["inputs"],
    # MEMORY. This rule loads the whole calls table through `calls.read_calls`:
    # 2.7M rows on 2026-10-22, about 1-1.5 GB resident after the interning that
    # docstring describes. `report` and `site_drift` can be co-scheduled under
    # --cores, so without a declaration two of these land on one node together;
    # on SLURM, where `resources:` becomes the sbatch request, the job is killed
    # rather than slowed. Sized at 3 GB: measured peak plus headroom for a
    # registry that grows, since the table is assays x records.
    resources:
        mem_mb=3000,
        runtime=60,
    shell:
        "assaywatch sitedrift {input.calls} --registry {REGISTRY} "
        "--retrieved {RETRIEVED} --out {RESULTS}/{RUN_DATE} --run-date {RUN_DATE} "
        "--config {CONFIG_EFFECTIVE}"


rule lineage_analysis:
    """Per-lineage detection statistics (phase 1 of estimand rebuild).

    Groups records by NCBI taxid and computes detection share per lineage.
    Reads the calls table only, adding no screening work. This is reporting
    and analysis; verdict changes come in phase 2.
    """
    input:
        calls=RESULTS / RUN_DATE / "calls.tsv.gz",
    output:
        md=RESULTS / RUN_DATE / "lineage.md",
    params:
        code=_LINEAGE_PARAMS["code"],
        inputs=_LINEAGE_PARAMS["inputs"],
    # MEMORY. This rule loads the whole calls table through `calls.read_calls`:
    # 2.7M rows on 2026-10-22, about 1-1.5 GB resident after the interning that
    # docstring describes. `report` and `site_drift` can be co-scheduled under
    # --cores, so without a declaration two of these land on one node together;
    # on SLURM, where `resources:` becomes the sbatch request, the job is killed
    # rather than slowed. Sized at 3 GB: measured peak plus headroom for a
    # registry that grows, since the table is assays x records.
    resources:
        mem_mb=3000,
        runtime=60,
    shell:
        "assaywatch lineage-report {input.calls} "
        "--retrieved {RETRIEVED} --config {CONFIG_EFFECTIVE} --registry {REGISTRY} --out {RESULTS}/{RUN_DATE}"


rule degeneracy_table:
    """The caveat that has to travel with the coverage numbers."""
    input:
        RESULTS / RUN_DATE / ".registry-valid",
    output:
        RESULTS / RUN_DATE / "degeneracy.tsv",
    params:
        code=_DEGENERACY_PARAMS["code"],
        inputs=_DEGENERACY_PARAMS["inputs"],
    shell:
        # -o, not `> {output}`: a redirect truncates the declared output before
        # python loads, so the tracked file was empty for the whole job and a
        # process death left a zero-byte table with a fresh mtime that `rule all`
        # accepts. -o writes a .part and renames.
        "assaywatch degeneracy {REGISTRY} --tsv -o {output} --config {CONFIG_EFFECTIVE}"


rule figures:
    """The two plots the tables leave to the reader's arithmetic.

    Separate from `report` so that adjusting a plot re-renders the figures and
    the page, and screens nothing: the expensive work is upstream of both. It
    runs the drift and site assessments itself rather than parsing report.md,
    which would be a second implementation of the same numbers and free to
    disagree with the first.
    """
    input:
        calls=RESULTS / RUN_DATE / "calls.tsv.gz",
        taxonomy=config["drift"]["scope_taxonomy"],
    output:
        forest=RESULTS / RUN_DATE / "figures" / "forest.svg",
        sites=RESULTS / RUN_DATE / "figures" / "site-positions.svg",
        page=RESULTS / RUN_DATE / "figures" / "figures.html",
    params:
        code=_FIGURES_PARAMS["code"],
        inputs=_FIGURES_PARAMS["inputs"],
    resources:
        mem_mb=4000,
        runtime=60,
    shell:
        "MPLBACKEND=Agg assaywatch figures {input.calls} --registry {REGISTRY} "
        "--retrieved {RETRIEVED} --out {RESULTS}/{RUN_DATE} --run-date {RUN_DATE} "
        "--config {CONFIG_EFFECTIVE}"


rule report:
    """Per-assay drift status, coverage gaps, and the degeneracy caveat beside both."""
    input:
        calls=RESULTS / RUN_DATE / "calls.tsv.gz",
        # scope_taxids ancestry: a rebuilt tree changes which records count
        taxonomy=config["drift"]["scope_taxonomy"],
        # Inlined into the HTML. A hard input, so the page is never published
        # with a figure from an earlier run beside this run's tables.
        forest=RESULTS / RUN_DATE / "figures" / "forest.svg",
        sites=RESULTS / RUN_DATE / "figures" / "site-positions.svg",
    output:
        md=RESULTS / RUN_DATE / "report.md",
        html=RESULTS / RUN_DATE / "report.html",
    params:
        code=_REPORT_PARAMS["code"],
        inputs=_REPORT_PARAMS["inputs"],
    # MEMORY. This rule loads the whole calls table through `calls.read_calls`:
    # 2.7M rows on 2026-10-22, about 1-1.5 GB resident after the interning that
    # docstring describes. `report` and `site_drift` can be co-scheduled under
    # --cores, so without a declaration two of these land on one node together;
    # on SLURM, where `resources:` becomes the sbatch request, the job is killed
    # rather than slowed. Sized at 3 GB: measured peak plus headroom for a
    # registry that grows, since the table is assays x records.
    resources:
        mem_mb=3000,
        runtime=60,
    shell:
        "assaywatch report {input.calls} --registry {REGISTRY} "
        "--retrieved {RETRIEVED} --out {RESULTS}/{RUN_DATE} --run-date {RUN_DATE} "
        "--figures {RESULTS}/{RUN_DATE}/figures --config {CONFIG_EFFECTIVE}"
