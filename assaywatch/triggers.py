"""Which source files a Snakefile rule actually runs, worked out from the imports.

Snakemake reruns a rule when an input or a param changes. A rule that calls
`python -m assaywatch.report` has no Snakemake-visible code, so editing report.py,
or anything report.py imports, reruns nothing unless the rule carries a hash of
those files as a param. Which files to hash was a hand-kept list, and the hand-kept
list was wrong twice: schema.py and validate.py were both missing from the
screening list, so editing either rescreened nothing and the pipeline went on
reporting the old answers.

So the list is derived. `source_names("report")` is report.py plus every
assaywatch module it imports, directly or through another, including imports made
inside a function (`from assaywatch.score import load_config` inside `main`).
Over-inclusion is harmless, since an extra file only means one more edit reruns the
rule, so the walk follows every import it can see rather than guess which are live.

It reads source text and never imports the modules, so the Snakefile can call it at
parse time without running anything.
"""

from __future__ import annotations

import re
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent

# `from assaywatch.x import ...`, `import assaywatch.x`, and the names in
# `from assaywatch import x, y`. Anchored to the start of a line (after
# indentation) so a mention inside a docstring sentence is not an import.
_FROM_MODULE = re.compile(r"^[ \t]*from[ \t]+assaywatch\.(\w+)[ \t]+import\b", re.M)
_IMPORT_MODULE = re.compile(r"^[ \t]*import[ \t]+assaywatch\.(\w+)", re.M)
_FROM_PACKAGE = re.compile(r"^[ \t]*from[ \t]+assaywatch[ \t]+import[ \t]+([\w, \t]+)", re.M)


def direct_imports(module: str, package: Path = PACKAGE) -> set[str]:
    """assaywatch modules that `package/<module>.py` imports, by name."""
    source = (package / f"{module}.py").read_text()
    found = set(_FROM_MODULE.findall(source)) | set(_IMPORT_MODULE.findall(source))
    for names in _FROM_PACKAGE.findall(source):
        found |= {n.strip() for n in names.split(",") if n.strip()}
    return {m for m in found if (package / f"{m}.py").exists()}


def import_closure(module: str, package: Path = PACKAGE) -> set[str]:
    """`module` and every assaywatch module reachable from it by imports."""
    seen = {module}
    todo = [module]
    while todo:
        for dep in direct_imports(todo.pop(), package):
            if dep not in seen:
                seen.add(dep)
                todo.append(dep)
    return seen


def source_names(module: str, package: Path = PACKAGE) -> list[str]:
    """File names (`report.py`, ...) a rule running `module` depends on, sorted."""
    return sorted(f"{m}.py" for m in import_closure(module, package))
