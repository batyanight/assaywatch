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
import json
import os
import subprocess
from datetime import date
from pathlib import Path

from assaywatch.collect import concatenate_screens, stem_order
from assaywatch.assemblies import cut_parameters
from assaywatch.retrieve import targets_from_registry
from assaywatch.timing import (
    RunManifest,
    clear_run_marker,
    heartbeat,
    resolve_run_date,
    screening_progress,
    write_run_marker,
)
from assaywatch.triggers import source_names
from assaywatch.validate import iter_files

configfile: "config.yaml"

EMAIL = config.get("email")
RETRIEVED = Path(config.get("retrieved_dir", "data/retrieved"))
RESULTS = Path(config.get("results_dir", "results"))
SCREENED = RESULTS / "screened"
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
SCREEN_MB_PER_THREAD = config.get("screen_mb_per_thread", 25)  # gzipped MB per screening worker
THERMO = str(config.get("thermo", False)).lower() in ("1", "true", "yes")

# {(taxid, group): {"name", "query", "assays"}} from the registry as it stands.
GROUPS = targets_from_registry([Path(REGISTRY)], config)
# Every assay id this run screens; collect_calls refuses any other.
CURRENT_ASSAYS = frozenset(a for g in GROUPS.values() for a in g["assays"])

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
    """
    h = hashlib.sha1(_code_hash.encode())
    for aid in sorted(GROUPS[(taxid, group)]["assays"]):
        h.update((Path(REGISTRY) / f"{aid}.yaml").read_bytes())
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


rule validate:
    """Fail early: a malformed registry entry should stop the run, not the report."""
    input:
        registry=REGISTRY,
    output:
        touch(RESULTS / RUN_DATE / ".registry-valid"),
    shell:
        "python -m assaywatch.validate {input.registry}"


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
    shell:
        "python -m assaywatch.retrieve {REGISTRY} --email {EMAIL} --run-record {output.run}"


def archives(wildcards):
    """Every archive on disk for a group the registry still asks for, oldest first."""
    checkpoints.retrieve.get()
    out = []
    for (taxid, group) in sorted(GROUPS):
        for fasta in sorted((RETRIEVED / str(taxid) / group).glob("*.fasta.gz"), key=stem_order):
            stem = fasta.name[: -len(".fasta.gz")]
            out.append(SCREENED / str(taxid) / group / f"{stem}.tsv")
    return out


def archive_mb(input):
    """Gzipped size of the archive. input.size_mb is async in Snakemake 9 and
    cannot be used for threads or priority, so read the size directly."""
    return os.path.getsize(input.fasta) / 1e6


rule screen_archive:
    """Score one archive against the assays that requested its group. Cached across runs."""
    input:
        fasta=RETRIEVED / "{taxid}" / "{group}" / "{stem}.fasta.gz",
    output:
        calls=SCREENED / "{taxid}" / "{group}" / "{stem}.tsv",
    params:
        # A params change re-triggers the job, so adding an assay to a group
        # rescreens that group's archives on the next run.
        only=lambda wc: ",".join(sorted(GROUPS[(int(wc.taxid), wc.group)]["assays"])),
        # Turning thermo on or off changes the params, so cached screens are redone.
        thermo="--thermo" if THERMO else "",
        signature=lambda wc: screen_signature(int(wc.taxid), wc.group),
    # Screening time grows with archive size, and one 775 MB poxvirus archive
    # used to run alone on one core long after everything else had finished.
    # Big archives get more workers (Snakemake caps this at --cores), and
    # start first, so the long pole is not left until last.
    threads: lambda wc, input: max(1, min(16, int(archive_mb(input) // SCREEN_MB_PER_THREAD)))
    priority: lambda wc, input: int(archive_mb(input))
    resources:
        mem_mb=lambda wc, input, threads: 2000 + 500 * threads,
        runtime=240,
    shell:
        "python -m assaywatch.screen {REGISTRY} {input.fasta} --only {params.only} "
        "--workers {threads} {params.thermo} -o {output.calls}"


rule collect_calls:
    """Concatenate every cached screen, oldest archive first so the newest version wins."""
    input:
        archives,
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
            list(input),
            output[0],
            known_ids=CURRENT_ASSAYS,
            provenance={
                "run_date": RUN_DATE,
                "expected_signatures": {f"{t}/{g}": screen_signature(t, g) for t, g in GROUPS},
                "extra": {
                    "screen_code_and_config_sha1": _code_hash,
                    "collect_code_sha1": _COLLECT_CODE,
                    "thermo": THERMO,
                    "assays_screened": len(CURRENT_ASSAYS),
                    "git_commit": _git_commit(),
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
    shell:
        "python -m assaywatch.sitedrift {input.calls} --registry {REGISTRY} "
        "--retrieved {RETRIEVED} --out {RESULTS}/{RUN_DATE} --run-date {RUN_DATE}"


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
    shell:
        "python -m assaywatch.lineage_report {input.calls} "
        "--retrieved {RETRIEVED} --config config.yaml --registry {REGISTRY} --out {RESULTS}/{RUN_DATE}"


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
        "python -m assaywatch.degeneracy {REGISTRY} --tsv > {output}"


rule report:
    """Per-assay drift status, coverage gaps, and the degeneracy caveat beside both."""
    input:
        calls=RESULTS / RUN_DATE / "calls.tsv.gz",
        # scope_taxids ancestry: a rebuilt tree changes which records count
        taxonomy=config["drift"]["scope_taxonomy"],
    output:
        md=RESULTS / RUN_DATE / "report.md",
        html=RESULTS / RUN_DATE / "report.html",
    params:
        code=_REPORT_PARAMS["code"],
        inputs=_REPORT_PARAMS["inputs"],
    shell:
        "python -m assaywatch.report {input.calls} --registry {REGISTRY} "
        "--retrieved {RETRIEVED} --out {RESULTS}/{RUN_DATE} --run-date {RUN_DATE}"
