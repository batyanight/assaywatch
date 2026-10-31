"""`scripts/check_taxids.py`: a deliberate genus-level root reads as SCOPED, not MISMATCH.

Eight registry entries name a species but root retrieval at its genus, narrowed by
`txid<N>[Organism:exp]` terms in the query, because the species has no usable
retrieval root of its own. The name check could only see that the genus is not called
"Elephant endotheliotropic herpesvirus 5", so for three weeks a deliberate design and
a wrong taxid printed the same line.

What is pinned here is the part that keeps SCOPED from excusing a real error: the
narrowing counts only when EVERY organism taxid in the query descends from the entry's
own taxid. A query that reaches outside the root is the Mycoplasma failure in a second
disguise and must still report MISMATCH.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# {taxid: (scientific name, lineage, other names, ancestor taxids, canonical id)},
# the shape fetch_taxa returns. 548689 is genus Proboscivirus; 768738 is EEHV5
# inside it; 10492 is genus Ranavirus, outside it.
TAXA = {
    548689: ("Proboscivirus", "Viruses; ...; Orthoherpesviridae", set(), {548689}, 548689),
    768738: (
        "Elephant endotheliotropic herpesvirus 5",
        "Viruses; ...; Proboscivirus",
        set(),
        {548689, 768738},
        768738,
    ),
    548913: (
        "Elephant endotheliotropic herpesvirus 3",
        "Viruses; ...; Proboscivirus",
        set(),
        {548689, 548913},
        548913,
    ),
    10492: ("Ranavirus", "Viruses; ...; Iridoviridae", set(), {10492}, 10492),
}


def _module():
    spec = importlib.util.spec_from_file_location("check_taxids", ROOT / "scripts" / "check_taxids.py")
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_name_of_a_pinned_descendant_is_scoped():
    narrowed_to = _module().narrowed_to
    got = narrowed_to("elephant endotheliotropic herpesvirus 5", 548689, [768738], TAXA)
    assert got == "Elephant endotheliotropic herpesvirus 5 (768738)"


def test_a_name_covering_two_pinned_species_still_matches():
    # The registry entry is one primer pair over EEHV3 and EEHV4; NCBI has no name
    # for the pair, so the stored name CONTAINS the pinned taxon's name.
    narrowed_to = _module().narrowed_to
    got = narrowed_to("elephant endotheliotropic herpesvirus 3 and 4", 548689, [548913], TAXA)
    assert got.endswith("(548913)")


def test_a_query_reaching_outside_the_root_is_not_scoped():
    narrowed_to = _module().narrowed_to
    assert narrowed_to("ranavirus", 548689, [10492], TAXA) == ""


def test_an_unpinned_query_is_not_scoped():
    narrowed_to = _module().narrowed_to
    assert narrowed_to("elephant endotheliotropic herpesvirus 5", 548689, [], TAXA) == ""
