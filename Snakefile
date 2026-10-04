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

import json
from datetime import date
from pathlib import Path

from assaywatch.retrieve import targets_from_registry

configfile: "config.yaml"

EMAIL = config.get("email")
RETRIEVED = Path(config.get("retrieved_dir", "data/retrieved"))
RESULTS = Path(config.get("results_dir", "results"))
SCREENED = RESULTS / "screened"
REGISTRY = config.get("registry_dir", "registry")
TODAY = date.today().isoformat()
RUN_DATE = config.get("run_date") or TODAY  # names the report folder only

# {(taxid, group): {"name", "query", "assays"}} from the registry as it stands.
GROUPS = targets_from_registry([Path(REGISTRY)])

wildcard_constraints:
    taxid=r"\d+",
    group=r"all|q[0-9a-f]{10}",
    stem=r"\d{4}-\d{2}-\d{2}(_\d+)?",


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
        email=EMAIL,
    shell:
        "python -m assaywatch.retrieve {REGISTRY} --email {params.email} --run-record {output.run}"


def archives(wildcards):
    """Every archive on disk for a group the registry still asks for, oldest first."""
    checkpoints.retrieve.get()
    out = []
    for (taxid, group) in sorted(GROUPS):
        for fasta in sorted((RETRIEVED / str(taxid) / group).glob("*.fasta.gz")):
            stem = fasta.name[: -len(".fasta.gz")]
            out.append(SCREENED / str(taxid) / group / f"{stem}.tsv")
    return out


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
    threads: 1
    resources:
        mem_mb=2000,
        runtime=240,
    shell:
        "python -m assaywatch.screen {REGISTRY} {input.fasta} --only {params.only} -o {output.calls}"


rule collect_calls:
    """Concatenate every cached screen, oldest archive first so the newest version wins."""
    input:
        archives,
    output:
        RESULTS / RUN_DATE / "calls.tsv.gz",
    run:
        import gzip

        with gzip.open(output[0], "wt") as out:
            header_written = False
            for path in input:
                with open(path) as fh:
                    header = next(fh, None)
                    if header is None:
                        continue
                    if not header_written:
                        out.write(header)
                        header_written = True
                    out.writelines(fh)


rule degeneracy_table:
    """The caveat that has to travel with the coverage numbers."""
    input:
        RESULTS / RUN_DATE / ".registry-valid",
    output:
        RESULTS / RUN_DATE / "degeneracy.tsv",
    shell:
        "python -m assaywatch.degeneracy {REGISTRY} > {output}"


rule report:
    """Per-assay drift status, coverage gaps, and the degeneracy caveat beside both."""
    input:
        calls=RESULTS / RUN_DATE / "calls.tsv.gz",
    output:
        md=RESULTS / RUN_DATE / "report.md",
        html=RESULTS / RUN_DATE / "report.html",
    shell:
        "python -m assaywatch.report {input.calls} --registry {REGISTRY} "
        "--retrieved {RETRIEVED} --out {RESULTS}/{RUN_DATE} --run-date {RUN_DATE}"
