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
import hashlib
import json
import os
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
SCREEN_MB_PER_THREAD = config.get("screen_mb_per_thread", 25)  # gzipped MB per screening worker
THERMO = str(config.get("thermo", False)).lower() in ("1", "true", "yes")

# {(taxid, group): {"name", "query", "assays"}} from the registry as it stands.
GROUPS = targets_from_registry([Path(REGISTRY)], config)

# What a cached screen depends on besides its archive: the group's assay files,
# the scoring settings and the screening code. Its hash is a param of
# screen_archive, so editing an assay, changing a threshold or upgrading the
# matcher rescreens exactly the archives affected, with no `-R` to remember.
_CODE = ("score.py", "match.py", "iupac.py", "chance.py", "screen.py", "thermo.py", "degeneracy.py", "fasta.py")
_SCREEN_CFG = {k: config.get(k) for k in ("scoring", "amplicon", "degeneracy", "thermo_conditions")}
_code_hash = hashlib.sha1(
    b"".join((Path(workflow.basedir) / "assaywatch" / f).read_bytes() for f in _CODE)
    + json.dumps(_SCREEN_CFG, sort_keys=True, default=str).encode()
).hexdigest()


def screen_signature(taxid, group):
    h = hashlib.sha1(_code_hash.encode())
    for aid in sorted(GROUPS[(taxid, group)]["assays"]):
        h.update((Path(REGISTRY) / f"{aid}.yaml").read_bytes())
    return h.hexdigest()[:16]


def stem_order(path):
    """`2026-10-04` < `2026-10-04_2` < `2026-10-04_10`: archive names in fetch order."""
    stem = path.name.split(".")[0]
    day, _, n = stem.partition("_")
    return (day, int(n or 1))

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
    run:
        import csv
        import gzip

        # Screens made at different times can differ in columns (with or without
        # --thermo, before or after a column was added). Plain concatenation would
        # shift those rows a column sideways; rows are written by column name.
        headers = []
        for path in input:
            with open(path) as fh:
                headers.append(next(fh, "").rstrip("\r\n").split("\t"))
        columns = []
        for h in headers:
            columns += [c for c in h if c and c not in columns]
        with gzip.open(output[0], "wt", newline="") as out:
            out.write("\t".join(columns) + "\n")
            for path, header in zip(input, headers):
                with open(path, newline="") as fh:
                    next(fh, None)
                    if header == columns:
                        out.writelines(fh)  # the usual case: same columns, copy as is
                    else:
                        w = csv.DictWriter(out, columns, delimiter="\t", restval="", lineterminator="\r\n")
                        w.writerows(csv.DictReader(fh, fieldnames=header, delimiter="\t"))


rule degeneracy_table:
    """The caveat that has to travel with the coverage numbers."""
    input:
        RESULTS / RUN_DATE / ".registry-valid",
    output:
        RESULTS / RUN_DATE / "degeneracy.tsv",
    shell:
        "python -m assaywatch.degeneracy {REGISTRY} --tsv > {output}"


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
