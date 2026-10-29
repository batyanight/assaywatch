# Installation

## Not on PyPI

`pip install assaywatch` does not work: the package is not published. Install
from a checkout.

## The supported route: conda

`environment.yml` is the environment this project is developed and tested in.

```bash
git clone <this repository>
cd assaywatch
conda env create -f environment.yml
conda activate assaywatch
```

That gives you Python 3.12, the package installed editable (`pip: -e .`), the
test and lint tooling pinned to the versions CI uses (`ruff=0.16.10`, matching
`.pre-commit-config.yaml` and `pyproject.toml`), the Snakemake minor pinned in
`environment.yml` for the pipeline, and the NCBI command-line tools. The pin is
not repeated here: it moved once already, and `tests/test_reproducibility.py`
checks `environment.yml` against CI, not against this prose.

Verify:

```bash
pytest -q
ruff check . && ruff format --check .
assaywatch validate registry
python scripts/check_citations.py
```

All four must pass. They are the project's gates — see `CLAUDE.md`.

## Pip, if you would rather

```bash
python -m pip install -e ".[dev,pdf]"
```

Runtime dependencies are `pydantic>=2`, `pyyaml>=6`, `numpy>=1.24`, `requests>=2`
and `matplotlib>=3.8`. `matplotlib` is NOT optional: `rule all` requires
`results/<date>/figures/figures.html` unconditionally, so a pip install without it
cannot finish a run. It reached `environment.yml` and not `pyproject.toml` once and
turned both CI jobs red while the Mac stayed green.

| extra | brings | for |
|---|---|---|
| `dev` | pytest, ruff, pre-commit, build | the gates, and `python -m build` |
| `lineage` | scipy, statsmodels | the per-lineage verdict and its multiple-testing correction. **Without it anything that computes a verdict raises**, including most of `tests/test_drift.py` — and the lineage check drives 18 of the 38 `declining` calls, so this is not a side feature. CI runs one job without it on purpose, to prove the rest of the pipeline still works. |
| `pdf` | pypdf | `scripts/verify_oligos_against_paper.py --pdf-dir` |
| `thermo` | primer3-py | the duplex-Tm columns, opt-in via `thermo: true` |

Pip alone does **not** install Snakemake or the NCBI CLI tools. Without
Snakemake you can still use the library and `assaywatch screen`
directly — see `examples/README.md` — but not the `Snakefile` pipeline.

## The NCBI command-line tools

`environment.yml` installs `entrez-direct` (`esearch`, `efetch`, `xtract`) and
`ncbi-datasets-cli`. The pipeline does **not** need them: it calls the
E-utilities and Datasets REST APIs directly through `requests`. They are there
for ad-hoc GenBank and taxonomy lookups, which `CLAUDE.md` asks you to prefer
over writing one-off Python.

## An NCBI API key (optional)

A key raises the E-utilities rate limit from 3 requests/second to 10. Everything
works without one, three times slower.

Get a key from https://www.ncbi.nlm.nih.gov/account/settings/ and put it in
**one** place. Resolution order, first hit wins:

1. the `NCBI_API_KEY` environment variable
2. `.secrets/ncbi.key` — **relative to the checkout**, not your home directory

```bash
mkdir -p .secrets
printf '%s' 'YOUR-KEY' > .secrets/ncbi.key
```

`.secrets/` is gitignored in full, and `*.key` separately, so a key file there
cannot be committed by accident.

Prefer the environment variable in a cloud session: it is the only route where
the key never touches a filesystem, a chat window or a diff.

Check it was picked up, without printing it:

```bash
assaywatch credentials            # says which credentials are visible
assaywatch credentials --check    # also asks NCBI whether it accepts the key
```

A key that is unusable — more than one line, control characters, an empty or
unreadable file — is ignored with a reason given, and never sent.

## Network access

The pipeline needs `eutils.ncbi.nlm.nih.gov` and `api.ncbi.nlm.nih.gov`. The
citation and literature tooling additionally needs `api.crossref.org`,
`api.unpaywall.org`, `api.openalex.org` and `www.ebi.ac.uk`. Some sandboxed
environments block these; `CLAUDE.md` records that network steps are run
locally for that reason.

`scripts/check_citations.py` reads the committed
`docs/papers-index.cache.json` and so passes offline — but a **new** DOI cannot
be verified without Crossref, and waits rather than being entered.

## Next

- `examples/README.md` — screen one assay offline in a second
- `README.md` — what the project is and how the registry is laid out
- `CONTRIBUTING.md` — how an assay gets in
