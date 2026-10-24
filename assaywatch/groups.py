"""Where a retrieval group lives on disk: `data/retrieved/<taxid>/<slug>/`.

One function, in its own module on purpose. `retrieve.py` owns the NCBI transport and
imports credentials and timing with it; `clustermaps.py` runs at report time and only
needs to know which directory holds an assay's archives. Importing `retrieve` there
would put the whole retrieval stack into the report rule's trigger closure
(`assaywatch/triggers.py`), so that editing `credentials.py` re-rendered every report.
"""

from __future__ import annotations

import hashlib


def group_slug(assay_query: str | None) -> str:
    """Directory name for a retrieval group under its taxid: `all`, or a query hash."""
    if not assay_query:
        return "all"
    return "q" + hashlib.sha1(assay_query.strip().encode()).hexdigest()[:10]
