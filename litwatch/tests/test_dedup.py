"""Tests for dedup.py.

Run from the repo root with:

    python3 -m unittest discover -s tests -v

`unittest` ships with Python, so there is nothing to install.
Each method whose name starts with `test_` is one test. A test passes
when every `assert...` line in it holds, and fails otherwise.
"""

import sys
import unittest
from pathlib import Path

# Let the tests import dedup.py from the repo root, wherever the repo is
# cloned. Path(__file__) is this file; .parents[1] is the folder above tests/.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from dedup import same_doi  # must come after the path line above


class SameDoiTest(unittest.TestCase):
    """PRD, Quality > Tests: deduplication treats DOIs case-insensitively."""

    def test_same_doi_in_different_case_is_one_paper(self) -> None:
        self.assertTrue(same_doi("10.1128/JCM.01234-20", "10.1128/jcm.01234-20"))

    def test_different_dois_are_different_papers(self) -> None:
        self.assertFalse(same_doi("10.1128/JCM.01234-20", "10.1128/JCM.09999-20"))

    def test_a_missing_doi_never_matches(self) -> None:
        # Preprints and old papers can lack a DOI. Two records that both lack
        # one must not be treated as the same paper.
        self.assertFalse(same_doi("", ""))
        self.assertFalse(same_doi(None, None))


if __name__ == "__main__":
    unittest.main()
