"""How each assay's record mix changes over time, and what that does to its graph.

ROADMAP "Lineage composition over time" (designed and grilled 2026-11-02). An assay's
per-year detection share can move because detection WITHIN lineages changed (drift)
or because the MIX of lineages being sequenced changed. This stage separates the two,
using sequence clusters as lineages: composition windows (`subcluster.flanked_region`)
are sampled across deposit years, clustered at a per-assay cut, and every record is
assigned to its nearest sampled member.

REPORT-ONLY. Nothing here moves a status; like the trend, collection-year and
hierarchical lenses, it is printed beside the verdict.

Built in steps; the entry point `build` arrives at step 12. Until then this module
holds the stage's internals, each tested at its own boundary.
"""

from __future__ import annotations

import hashlib
import re
from collections import Counter, defaultdict
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any

from assaywatch.accession import strip_version
from assaywatch.subcluster import Region


def _order_key(record_id: str) -> tuple[bytes, str]:
    """Deterministic, input-order-free rank of a record: a hash of its accession
    WITHOUT version, so `.1` and `.2` of one record rank the same; the accession
    breaks the (vanishingly rare) hash tie."""
    acc = strip_version(record_id)
    return hashlib.blake2b(acc.encode(), digest_size=8).digest(), acc


def sample_windows(regions: Sequence[Region], years: Sequence[int], cap: int) -> list[int]:
    """Indices of the windows to cluster: at most `cap`, spread across deposit years.

    Rules, each pinned by a test in tests/test_composition.py:

    - Only full-flank windows are sampled (finding 2); short ones are assigned later.
    - Identical windows count once, keeping the lowest-ranked record: a clone deposited
      twenty times is one member of its lineage, not twenty.
    - ROUND-ROBIN across years, one window per year per pass, years in chronological
      order within a pass. A busy year therefore cannot crowd out a quiet one, which is
      the point: a lineage seen only in a quiet year must still be clustered.
    - Within a year, records are taken in `_order_key` order, so the same archive read
      in any order samples the same records.

    Returned in (year, rank) order.
    """
    if len(regions) != len(years):
        raise ValueError(f"{len(regions)} regions but {len(years)} years")
    best: dict[str, int] = {}
    for i, r in enumerate(regions):
        if not r.full_flank:
            continue
        j = best.get(r.seq)
        if j is None or _order_key(r.record_id) < _order_key(regions[j].record_id):
            best[r.seq] = i
    per_year: dict[int, list[int]] = defaultdict(list)
    for i in best.values():
        per_year[years[i]].append(i)
    queues = {y: sorted(ix, key=lambda i: _order_key(regions[i].record_id)) for y, ix in per_year.items()}
    chosen: list[int] = []
    depth = 0
    while len(chosen) < cap:
        took = False
        for y in sorted(queues):
            if depth < len(queues[y]) and len(chosen) < cap:
                chosen.append(queues[y][depth])
                took = True
        if not took:
            break
        depth += 1
    rank = {i: (years[i], _order_key(regions[i].record_id)) for i in chosen}
    return sorted(chosen, key=rank.__getitem__)


# ---- What a cluster is called, and what else it holds (ROADMAP composition step 6) ----

# A nuccore title is "<organism> <qualifier> <everything else>", so the name ends at the
# first qualifier. Measured against the influenza, Chlamydia, coronavirus and
# haemosporidian archives on 2026-11-03. "sp." is NOT a qualifier: "Plasmodium sp." is
# the name GenBank gives a record it cannot place further, and a cluster of them must say
# so rather than read as its genus.
_QUALIFIER = re.compile(
    r"^(strain|isolate|clone|voucher|genotype|serotype|subtype|variant|segment|gene|genes|mRNA|"
    r"cds|DNA|RNA|genome|genomic|chromosome|plasmid|contig|scaffold|partial|complete|cytochrome|"
    r"polyprotein|protein|ribosomal|16S|18S|23S|28S|ITS|from|and|sequence|region|locus|"
    r"polymerase|nonstructural|hypothetical|putative|haplotype|lineage|ORF\w*|UNVERIFIED|TPA|MAG)$",
    re.IGNORECASE,
)
#: Dropped from the head of a title: a flag about the record, not part of the organism.
_TITLE_PREFIX = re.compile(
    r"^(UNVERIFIED:?|UNVERIFIED_ORG:?|TPA:?|TPA_asm:?|MAG:?|Uncultured)\s+", re.IGNORECASE
)
#: A name's longest sensible run. "Porcine epidemic diarrhea virus" is 4 words.
_NAME_MAX_WORDS = 5
#: A strain or sample identifier, which follows the organism with no qualifier between:
#: `HCoVOC43_Fukushima_OR427_2021`, `A/canine/Madison/5/2015`, `PHEV/TN25-P046-NNFL/P`.
#: Any token holding "_" or "/", or 8 characters or more with a digit in it. Keeps the
#: short alphanumerics that ARE part of a name -- 229E, OC43, NL63, HKU1.
_IDENTIFIER = re.compile(r"[_/]|(?=.{8})\w*\d")
#: GenBank's "we cannot place this further". Whatever follows is an isolate code
#: ("Plasmodium sp. AP30"), so the name ends here: 3,186 of the haemosporidian
#: archive's 3,873 names were singletons until it did.
_UNPLACED = {"sp.", "spp.", "cf.", "aff."}
#: A name whose last word leaves the name open: a virus name may carry one more token.
_OPEN_ENDED = re.compile(r"virus(es)?$", re.IGNORECASE)
#: What may complete such a name: a serial, or a short letter-and-digit code.
_NAME_CODE = re.compile(r"^(?:\d{1,4}|(?=[A-Za-z0-9]{2,6}$)(?=[^\d]*\d)[A-Za-z0-9]+)$")
_TOKEN = re.compile(r"[A-Za-z0-9][A-Za-z0-9.-]*[A-Za-z0-9]")


def organism(title: str) -> str:
    """The organism name at the head of a nuccore title, or "" if it has none.

    The FALLBACK for a record whose archive metadata carries no taxid (most of them
    predate the column). Where a taxid is present the species comes from the taxonomy
    cache instead, which is authoritative; this only reads what the depositor wrote.

    The name ends at the first qualifier word, strain identifier, bracket, comma or
    semicolon, whichever comes first, and never runs past `_NAME_MAX_WORDS`. Keeping the words
    BEFORE the qualifier is what distinguishes "Human coronavirus 229E" from "Human
    coronavirus OC43" -- two viruses about 30% apart whose records both begin "Human
    coronavirus", which is why a two-word rule held the pan-coronavirus purity at 68%
    at every cut (step 4b, `docs/journal/2026-11-03-composition-cut-measured.md`).
    """
    head = _TITLE_PREFIX.sub("", title.strip())
    head = re.split(r"[(,;:\[]", head, maxsplit=1)[0]
    words: list[str] = []
    for w in head.split():
        open_ended = bool(words) and _OPEN_ENDED.search(words[-1])
        if w.lower() in _UNPLACED:
            words.append(w)
            break
        if _QUALIFIER.match(w.rstrip(".")):
            break
        if _IDENTIFIER.search(w):
            break
        if open_ended:
            # After "... virus" or "... herpesvirus" the next token either completes the
            # name (229E, OC43, NL63, HKU1, or the serial of "Bufonid herpesvirus 1") or
            # is the depositor's isolate code (SHG-5, Mebus, BJ04). Only a short
            # alphanumeric completes a name, and nothing follows it.
            if _NAME_CODE.match(w):
                words.append(w)
            break
        words.append(w)
        if len(words) == _NAME_MAX_WORDS:
            break
    return " ".join(words)


def species_mix(species: Sequence[str]) -> list[tuple[str, int]]:
    """``(species, count)`` commonest first, ties by name, unnamed records dropped.

    Names that differ only in case are ONE species, shown in the commonest spelling:
    the influenza archive writes "Influenza A Virus" on 94 of its 187,658 records, and
    counting that as a second organism would make a pure cluster read as mixed."""
    counts: Counter[str] = Counter()
    spellings: dict[str, Counter] = defaultdict(Counter)
    for s in species:
        if s:
            counts[s.casefold()] += 1
            spellings[s.casefold()][s] += 1
    out = [(spellings[k].most_common(1)[0][0], n) for k, n in counts.items()]
    return sorted(out, key=lambda kv: (-kv[1], kv[0]))


def _abbreviate(name: str) -> str:
    """``Chlamydia trachomatis`` -> ``C. trachomatis``, for a legend of eight entries.
    Only a two-word binomial abbreviates; ``Plasmodium sp.`` and
    ``Porcine epidemic diarrhea virus`` are left as they are."""
    parts = name.split()
    if len(parts) == 2 and parts[1].isalpha() and parts[1].islower() and parts[0][:1].isupper():
        return f"{parts[0][0]}. {parts[1]}"
    return name


def cluster_names(
    mixes: Sequence[Sequence[tuple[str, int]]], representatives: Sequence[str], *, pure_share: float
) -> list[str]:
    """One name per cluster, in cluster order (largest first), numbered where two
    clusters share a modal species.

    A cluster whose modal species covers at least ``pure_share`` of it is named for that
    species. Below that the name CARRIES THE SHARE -- "P. falciparum 38%" -- because a
    legend entry reading "P. falciparum" would be a false statement about the other 62%,
    and the pan-coronavirus measurement of step 4b produced exactly such a cluster. A
    cluster whose records name no species at all is "unnamed (<representative>)"; nothing
    is invented for it.
    """
    if len(mixes) != len(representatives):
        raise ValueError(f"{len(mixes)} mixes but {len(representatives)} representatives")
    base: list[str] = []
    for mix, rep in zip(mixes, representatives, strict=True):
        if not mix:
            base.append(f"unnamed ({rep})")
            continue
        species, n = mix[0]
        total = sum(c for _, c in mix)
        name = _abbreviate(species)
        base.append(name if n / total >= pure_share else f"{name} {n / total:.0%}")
    repeated = {name for name, c in Counter(base).items() if c > 1}
    seen: Counter[str] = Counter()
    out: list[str] = []
    for name in base:
        if name in repeated:
            seen[name] += 1
            out.append(f"{name} {seen[name]}")
        else:
            out.append(name)
    return out


def title_tokens(
    titles: Sequence[str],
    background: Sequence[str],
    *,
    name: str,
    min_share: float,
    min_lift: float,
    top: int,
) -> list[str]:
    """Up to ``top`` words that this cluster's titles carry and the OTHER clusters' do not:
    what the name leaves out, for the panel's tooltip.

    A token must appear in at least ``min_share`` of this cluster's titles (so one odd
    deposit cannot name a lineage) and at least ``min_lift`` times as often here as in
    ``background``. Words of the cluster's own name are skipped, and so are the record
    qualifiers of ``_QUALIFIER`` -- a cluster whose depositors wrote "clone" where another's
    wrote "isolate" is not a lineage finding, and that token outranked the real one when
    this was first written. Every token is skipped
    when there is no background: "distinguishing" needs something to be distinguished
    from. Ranked by the difference in share, ties alphabetically, displayed in the
    commonest spelling the titles use.
    """
    if not titles or not background:
        return []
    own = {w.lower() for w in _TOKEN.findall(name)}

    def shares(rows: Sequence[str]) -> tuple[dict[str, float], dict[str, Counter]]:
        docs: Counter[str] = Counter()
        spellings: dict[str, Counter] = defaultdict(Counter)
        for row in rows:
            found = set()
            for tok in _TOKEN.findall(row):
                key = tok.lower()
                found.add(key)
                spellings[key][tok] += 1
            docs.update(found)
        return {k: v / len(rows) for k, v in docs.items()}, spellings

    mine, spellings = shares(titles)
    theirs, _ = shares(background)
    scored = [
        (mine[k] - theirs.get(k, 0.0), k)
        for k in mine
        if k not in own
        and not _QUALIFIER.match(k)
        and mine[k] >= min_share
        and mine[k] >= min_lift * theirs.get(k, 0.0)
    ]
    scored.sort(key=lambda s: (-s[0], s[1]))
    return [spellings[k].most_common(1)[0][0] for _, k in scored[:top]]


# ---- The same-mix line (ROADMAP composition step 7) ----


@dataclass(frozen=True)
class Cell:
    """One assay's records of one deposit year in one lineage: the panel's unit.

    ``cluster`` is a label from ``subcluster.components_at`` -- ``0, 1, ...``, or
    ``OTHER`` / ``UNPLACED`` / the diverged stratum, each of which is a lineage here like
    any other, because the graph counted those records too. ``detected`` counts the
    records the screen detected, under the same rule the graph applies.
    """

    year: int
    cluster: int
    records: int
    detected: int


def observed_series(cells: Sequence[Cell]) -> dict[int, float]:
    """Each year's detected share, as the graph draws it: the year's own arithmetic."""
    totals: dict[int, list[int]] = defaultdict(lambda: [0, 0])
    for c in cells:
        totals[c.year][0] += c.records
        totals[c.year][1] += c.detected
    return {y: d / n for y, (n, d) in sorted(totals.items()) if n}


def same_mix_series(cells: Sequence[Cell], *, min_covered: float) -> dict[int, float]:
    """Each year's detection recomputed on the WHOLE PERIOD's lineage mix: the line that
    answers "what would this year have read if the same lineages had been sequenced?"

    Direct standardisation. Each lineage's weight is its share of all the assay's records;
    a year's own within-lineage detection rates are then combined on those weights
    instead of the year's. A fall that was only the mix changing therefore flattens, and
    a fall inside the lineages survives.

    A year is drawn only where the lineages PRESENT in it carry at least ``min_covered``
    of the weight, and the weights are renormalised over those present. A year holding
    one lineage of two says nothing about the other, and standardising over it would
    invent the missing half rather than measure it.
    """
    weight_of: dict[int, int] = defaultdict(int)
    for c in cells:
        weight_of[c.cluster] += c.records
    overall = sum(weight_of.values())
    if not overall:
        return {}
    per_year: dict[int, list[Cell]] = defaultdict(list)
    for c in cells:
        if c.records:
            per_year[c.year].append(c)
    out: dict[int, float] = {}
    for year, rows in sorted(per_year.items()):
        covered = sum(weight_of[c.cluster] for c in rows) / overall
        if covered < min_covered:
            continue
        total = sum(weight_of[c.cluster] * (c.detected / c.records) for c in rows)
        out[year] = total / (covered * overall)
    return out


# ---- The mix / within split (ROADMAP composition step 8) ----


@dataclass(frozen=True)
class Split:
    """Why an assay's detected share differs between two periods, in two numbers that add
    to the difference: how much the LINEAGE MIX moved, and how much detection moved
    WITHIN the lineages."""

    baseline_share: float
    recent_share: float
    change: float
    mix: float
    within: float
    mix_ci: tuple[float, float] | None
    within_ci: tuple[float, float] | None
    n_boot: int
    #: Lineages present in one period only: their whole effect sits in `mix`.
    one_period_clusters: tuple[int, ...]


def _totals(cells: Sequence[Cell]) -> tuple[dict[int, int], dict[int, int], int]:
    records: dict[int, int] = defaultdict(int)
    detected: dict[int, int] = defaultdict(int)
    for c in cells:
        records[c.cluster] += c.records
        detected[c.cluster] += c.detected
    return records, detected, sum(records.values())


def _kitagawa(
    base_n: dict[int, int], base_d: dict[int, int], rec_n: dict[int, int], rec_d: dict[int, int]
) -> tuple[float, float, float, float]:
    """(baseline share, recent share, mix part, within part) by Kitagawa's decomposition.

        mix    = sum (w_r - w_b)(p_r + p_b) / 2
        within = sum (p_r - p_b)(w_r + w_b) / 2

    and the two add to the change exactly, which is the property the report prints.

    A lineage present in ONE period only has no detection rate in the other, so its
    missing rate is taken to be the rate it has: its within term is then zero and its
    whole effect lands in the mix part. That is both the arithmetic that keeps the
    identity exact and the honest reading -- a lineage that appeared, or stopped being
    deposited, is a change in what was sequenced, not in how the assay performs.
    """
    nb, nr = sum(base_n.values()), sum(rec_n.values())
    mix = within = 0.0
    for k in set(base_n) | set(rec_n):
        wb, wr = base_n.get(k, 0) / nb, rec_n.get(k, 0) / nr
        pb = base_d[k] / base_n[k] if base_n.get(k) else None
        pr = rec_d[k] / rec_n[k] if rec_n.get(k) else None
        if pb is None:
            pb = pr
        if pr is None:
            pr = pb
        assert pb is not None and pr is not None
        mix += (wr - wb) * (pr + pb) / 2
        within += (pr - pb) * (wr + wb) / 2
    share_b = sum(base_d.values()) / nb
    share_r = sum(rec_d.values()) / nr
    return share_b, share_r, mix, within


def _resample(
    rng: Any, records: dict[int, int], detected: dict[int, int]
) -> tuple[dict[int, int], dict[int, int]]:
    """One multinomial resample of a period's records over (lineage, detected or not).

    Resampling RECORDS, not lineages: the uncertainty being priced is which records were
    deposited and which the screen detected. It does NOT include uncertainty in the
    clustering itself -- the cut, the sample and the labels are taken as given -- and the
    report says so beside the interval.
    """
    keys = sorted(records)
    cats = [(k, hit) for k in keys for hit in (True, False)]
    weights = [detected[k] if hit else records[k] - detected[k] for k, hit in cats]
    n = sum(records.values())
    draw = rng.multinomial(n, [w / n for w in weights])
    out_n: dict[int, int] = defaultdict(int)
    out_d: dict[int, int] = defaultdict(int)
    for (k, hit), count in zip(cats, draw.tolist(), strict=True):
        out_n[k] += count
        if hit:
            out_d[k] += count
    return {k: v for k, v in out_n.items() if v}, out_d


def split_change(baseline: Sequence[Cell], recent: Sequence[Cell], *, n_boot: int, seed: int) -> Split | None:
    """Split the change in detected share between two periods into a mix part and a within
    part, with percentile bootstrap intervals. ``None`` if either period holds no records.
    """
    base_n, base_d, nb = _totals(baseline)
    rec_n, rec_d, nr = _totals(recent)
    if not nb or not nr:
        return None
    base_n = {k: v for k, v in base_n.items() if v}
    rec_n = {k: v for k, v in rec_n.items() if v}
    share_b, share_r, mix, within = _kitagawa(base_n, base_d, rec_n, rec_d)
    one_period = tuple(sorted(set(base_n) ^ set(rec_n)))
    mix_ci = within_ci = None
    if n_boot:
        import numpy as np

        rng = np.random.default_rng(seed)
        mixes, withins = [], []
        for _ in range(n_boot):
            bn, bd = _resample(rng, base_n, base_d)
            rn, rd = _resample(rng, rec_n, rec_d)
            _, _, m, w = _kitagawa(bn, bd, rn, rd)
            mixes.append(m)
            withins.append(w)
        mix_ci = (float(np.percentile(mixes, 2.5)), float(np.percentile(mixes, 97.5)))
        within_ci = (float(np.percentile(withins, 2.5)), float(np.percentile(withins, 97.5)))
    return Split(share_b, share_r, share_r - share_b, mix, within, mix_ci, within_ci, n_boot, one_period)
