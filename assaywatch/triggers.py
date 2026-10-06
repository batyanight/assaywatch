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

It reads source and never imports the modules, so the Snakefile can call it at parse
time without running anything.
"""

from __future__ import annotations

import ast
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent


def direct_imports(module: str, package: Path = PACKAGE) -> set[str]:
    """assaywatch modules that `package/<module>.py` imports, by name.

    Read from the syntax tree, not by pattern: the project's own formatter turns a long
    `from assaywatch import a, b, c` into a parenthesised multi-line form, and an
    earlier version matched on text and silently missed that, along with `import x as y`,
    relative imports and the second name in `import assaywatch.a, assaywatch.b`. A missed
    dependency means an edit reruns nothing, which is the failure this module exists to
    prevent. Imports inside functions are followed (report.py imports `score` inside
    `main`), imports inside comments and strings are not imports, and `importlib` calls
    are NOT followed, since a name built at runtime is invisible to a source reader.

    A file that does not parse raises SyntaxError: a broken module should stop the
    Snakefile loudly, not quietly drop its dependencies.
    """
    path = package / f"{module}.py"
    tree = ast.parse(path.read_text(), filename=str(path))
    found: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                parts = alias.name.split(".")
                if parts[0] == "assaywatch" and len(parts) > 1:
                    found.add(parts[1])
        elif isinstance(node, ast.ImportFrom):
            if node.level == 0 and node.module and node.module.split(".")[0] == "assaywatch":
                parts = node.module.split(".")
                if len(parts) > 1:
                    found.add(parts[1])  # from assaywatch.x import y
                else:
                    found.update(a.name for a in node.names)  # from assaywatch import x, y
            elif node.level == 1:
                if node.module:
                    found.add(node.module.split(".")[0])  # from .x import y
                else:
                    found.update(a.name for a in node.names)  # from . import x
    return {m for m in found if m != "*" and (package / f"{m}.py").exists()}


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
