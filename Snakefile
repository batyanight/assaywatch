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
from datetime import date
from pathlib import Path

from assaywatch.collect import concatenate_screens, stem_order
from assaywatch.assemblies import cut_parameters
from assaywatch.retrieve import targets_from_registry
from assaywatch.triggers import source_names
from assaywatch.validate import iter_files

configfile: "config.yaml"

EMAIL = config.get("email")
RETRIEVED = Path(config.get("retrieved_dir", "data/retrieved"))
RESULTS = Path(config.get("results_dir", "results"))
SCREENED = RESULTS / "screened"
REGISTRY = config.get("registry_dir", "registry")
TODAY = date.today().isoformat()
RUN_DATE = config.get("run_date") or TODAY  # names the report folder only
SCREEN_MB_PER_THREAD = config.get("screen_mb_per_thread", 25)  # gzipped MB per screening worker
THERMO = str(config.get("thermo", False)).lower() in ("1", "true", "yes")

# {(taxid, group): {"name", "query", "assays"}} from the registry as it stands.
GROUPS = targets_from_registry([Path(REGISTRY)], config)

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
    "inputs": _registry_and_config_hash("drift", "degeneracy", "scoring", "amplicon"),
}
_DEGENERACY_PARAMS = {
    "code": _package_hash(*source_names("degeneracy")),
    "inputs": _registry_and_config_hash("degeneracy"),
}


wildcard_constraints:
    taxid=r"\d+",
    group=r"all|asm|q[0-9a-f]{10}",
    stem=r"\d{4}-\d{2}-\d{2}(_\d+)?",


# Retrieval needs the internet, which cluster compute nodes often lack.
localrules: retrieve


rule all:
    input:
        RESULTS / RUN_DATE / "report.html",
        RESULTS / RUN_DATE / "degeneracy.tsv",


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
    run:
        # The logic is in assaywatch/collect.py, where it is tested. It reconciles
        # a cached screen made before a column was added with one made after,
        # writing rows by column name, since plain concatenation would shift the
        # older rows a column sideways.
        concatenate_screens(list(input), output[0])


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
    output:
        md=RESULTS / RUN_DATE / "report.md",
        html=RESULTS / RUN_DATE / "report.html",
    params:
        code=_REPORT_PARAMS["code"],
        inputs=_REPORT_PARAMS["inputs"],
    shell:
        "python -m assaywatch.report {input.calls} --registry {REGISTRY} "
        "--retrieved {RETRIEVED} --out {RESULTS}/{RUN_DATE} --run-date {RUN_DATE}"
