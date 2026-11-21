"""Deduplication for Literature Watch.

Decides whether two records are the same paper, so nothing is shown twice
(PRD goal G3). This file starts with the smallest rule: two DOIs that differ
only in letter case are the same paper.

Standard library only, per the PRD: nothing to install.
"""


def normalize_doi(doi: str | None) -> str:
    """Return a DOI in one comparable form, or "" if there isn't one.

    DOIs are case-insensitive by definition (10.1128/JCM.1 and 10.1128/jcm.1
    resolve to the same paper), but databases store them in whatever case the
    publisher sent. Lower-casing both sides before comparing removes that
    difference. `strip()` drops stray spaces or newlines from the ends.
    """
    if not doi:  # catches None and the empty string
        return ""
    return doi.strip().lower()


def same_doi(a: str | None, b: str | None) -> bool:
    """True when a and b are the same DOI, ignoring letter case.

    A missing DOI never matches anything, including another missing DOI:
    two records without a DOI are not known to be the same paper.
    """
    a_norm = normalize_doi(a)
    b_norm = normalize_doi(b)
    if not a_norm or not b_norm:
        return False
    return a_norm == b_norm
