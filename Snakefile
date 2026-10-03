# AssayWatch pipeline.
#
#     snakemake --cores 4 --config email=you@example.org
#     snakemake --cores 4 --config email=... full=true      # ignore the manifest
#     snakemake --profile profiles/slurm --config email=...  # on a cluster
#
# Why a workflow manager at all, when this is four steps: Snakemake tracks
# which inputs produced which outputs, so a failed scoring run re-uses the
# sequences already fetched instead of hammering NCBI again, and editing one
# assay re-scores only what depends on it. The same Snakefile runs on a laptop
# and on SLURM with a different --profile; nothing in the rules changes.
#
# The structure is unusual in one way worth understanding. Snakemake normally
# builds its whole job graph before running anything, from filenames it can
# work out in advance. Here the set of taxa to screen is not known until
# retrieval has run and told us which taxids returned records. That is what a
# `checkpoint` is for: it is a rule that forces the graph to be re-evaluated
# after it completes, so later rules can glob the files it produced.

import json
from pathlib import Path

configfile: "config.yaml"

EMAIL = config.get("email")
RETRIEVED = Path(config.get("retrieved_dir", "data/retrieved"))
RESULTS = Path(config.get("results_dir", "results"))
REGISTRY = config.get("registry_dir", "registry")
RUN_DATE = config.get("run_date") or __import__("datetime").date.today().isoformat()


rule all:
    input:
        RESULTS / RUN_DATE / "report.html",
        RESULTS / RUN_DATE / "degeneracy.tsv",


rule validate:
    """Fail early: a malformed registry entry should stop the run, not the report."""
    input:
        registry=REGISTRY,
    output:
        touch(RESULTS / RUN_DATE / ".registry-valid")
    shell:
        "python -m assaywatch.validate {input.registry}"


checkpoint retrieve:
    """Fetch new records for every taxid in the registry. Writes the manifest.

    One job for all taxa rather than one per taxon, because the politeness
    limit is global: parallel jobs would each sleep for their own rate limit
    and together exceed NCBI's. The per-taxon parallelism worth having is in
    scoring, which is pure CPU.
    """
    input:
        RESULTS / RUN_DATE / ".registry-valid",
    output:
        manifest=RETRIEVED / "manifest.json",
    params:
        full="--full" if config.get("full") else "",
        email=EMAIL,
    shell:
        "python -m assaywatch.retrieve {REGISTRY} --email {params.email} {params.full}"


def fetched_taxa(wildcards):
    """Taxa that actually returned sequences in this run, read from the manifest."""
    manifest_file = checkpoints.retrieve.get(**wildcards).output.manifest
    runs = json.loads(Path(manifest_file).read_text())["runs"]
    return sorted({r["taxid"] for r in runs if r["run_date"] == RUN_DATE and r["n_fetched"] > 0})


rule screen_taxon:
    """Score every assay for one taxon against that taxon's new records."""
    input:
        fasta=RETRIEVED / "{taxid}" / f"{RUN_DATE}.fasta.gz",
    output:
        calls=RESULTS / RUN_DATE / "by-taxon" / "{taxid}.tsv",
    threads: 1
    resources:
        mem_mb=2000,
        runtime=120,
    shell:
        "python -m assaywatch.screen {REGISTRY} {input.fasta} -o {output.calls}"


def taxon_calls(wildcards):
    return [RESULTS / RUN_DATE / "by-taxon" / f"{t}.tsv" for t in fetched_taxa(wildcards)]


rule collect_calls:
    input:
        taxon_calls,
    output:
        RESULTS / RUN_DATE / "calls.tsv.gz",
    run:
        import gzip

        with gzip.open(output[0], "wt") as out:
            for i, path in enumerate(input):
                with open(path) as fh:
                    header = next(fh)
                    if i == 0:
                        out.write(header)
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
        manifest=RETRIEVED / "manifest.json",
    output:
        md=RESULTS / RUN_DATE / "report.md",
        html=RESULTS / RUN_DATE / "report.html",
    shell:
        "python -m assaywatch.report {input.calls} --registry {REGISTRY} "
        "--retrieved {RETRIEVED} --out {RESULTS}/{RUN_DATE} --run-date {RUN_DATE}"
