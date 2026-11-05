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

import dataclasses
import hashlib
import json
import re
from collections import Counter, defaultdict
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from assaywatch.accession import strip_version
from assaywatch.drift import GraphRecord
from assaywatch.subcluster import (
    OTHER,
    UNPLACED,
    Region,
    assign_nearest,
    components_at,
    jaccard_matrix,
    kmer_matrix,
    mash_distances,
)
from assaywatch.taxonomy import Taxonomy


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


# ---- The `composition:` block, read once (ROADMAP composition step 12) ----


@dataclass(frozen=True)
class Options:
    """The `composition:` settings, read once rather than per assay.

    Mirrors `settings.Composition`, which is the contract and holds the ranges; every
    value and its justification (or the admission of having none) is beside the key in
    config.yaml. The pattern is `drift.DriftSettings.from_config`.
    """

    flank_bp: int
    shape_quantile: float
    mask_buffer_bp: int
    stop_n_run: int
    kmer_len: int
    sample_cap: int
    cut: float
    min_cluster_size: int
    name_pure_share: float
    token_min_share: float
    token_min_lift: float
    title_tokens_shown: int
    show_clusters: int
    n_boot: int
    boot_seed: int
    same_mix_min_covered: float

    @classmethod
    def from_config(cls, cfg: Mapping[str, Any]) -> Options:
        c = cfg.get("composition") or {}
        return cls(
            flank_bp=int(c.get("flank_bp", 500)),
            shape_quantile=float(c.get("shape_quantile", 0.1)),
            mask_buffer_bp=int(c.get("mask_buffer_bp", 5)),
            stop_n_run=int(c.get("stop_n_run", 10)),
            kmer_len=int(c.get("kmer_len", 15)),
            sample_cap=int(c.get("sample_cap", 2000)),
            cut=float(c.get("cut", 0.05)),
            min_cluster_size=int(c.get("min_cluster_size", 3)),
            name_pure_share=float(c.get("name_pure_share", 0.9)),
            token_min_share=float(c.get("token_min_share", 0.2)),
            token_min_lift=float(c.get("token_min_lift", 2.0)),
            title_tokens_shown=int(c.get("title_tokens_shown", 5)),
            show_clusters=int(c.get("show_clusters", 8)),
            n_boot=int(c.get("n_boot", 2000)),
            boot_seed=int(c.get("boot_seed", 0)),
            same_mix_min_covered=float(c.get("same_mix_min_covered", 0.8)),
        )


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
#: The colon may come with no space after it ("TPA_asm:Bat coronavirus ..." occurs),
#: "TPA_asm" must be tried before "TPA", and flags STACK: "MAG TPA_asm: Pigeon
#: coronavirus rin35 RNA, nearly complete genome".
_TITLE_PREFIX = re.compile(
    r"^(?:(?:UNVERIFIED_ORG|UNVERIFIED|TPA_asm|TPA|MAG|Mutant|Recombinant|Synthetic|Uncultured)"
    r"(?:\s*:\s*|\s+))+",
    re.IGNORECASE,
)
#: A name's longest sensible run. "Severe acute respiratory syndrome coronavirus 2" is 6.
_NAME_MAX_WORDS = 6
#: A strain or sample identifier, which follows the organism with no qualifier between:
#: `HCoVOC43_Fukushima_OR427_2021`, `A/canine/Madison/5/2015`, `PHEV/TN25-P046-NNFL/P`.
#: Any token holding "_" or "/", both a "-" and a digit, or 8 characters or more with a
#: digit in it. Keeps the short alphanumerics that ARE part of a name -- 229E, OC43,
#: NL63, HKU1 -- and never applies to a title's FIRST token, which may be the name
#: itself: "SARS-CoV-2 isolate Wuhan-Hu-1" is a record of SARS-CoV-2.
_IDENTIFIER = re.compile(r"[_/]|(?=.{8})\w*\d|(?=.*-)(?=.*\d)")
#: GenBank's "we cannot place this further". Whatever follows is an isolate code
#: ("Plasmodium sp. AP30"), so the name ends here: 3,186 of the haemosporidian
#: archive's 3,873 names were singletons until it did.
_UNPLACED = {"sp.", "spp.", "cf.", "aff."}
#: A name whose last word leaves the name open: a virus name may carry one more token.
_OPEN_ENDED = re.compile(r"virus(es)?$", re.IGNORECASE)
#: What may complete such a name: a serial ("Bufonid herpesvirus 1"), or a short
#: UPPERCASE letter-and-digit code (229E, OC43, NL63, HKU1). Lower case marks a
#: depositor's isolate code instead -- "Pigeon coronavirus rin35" is one record of
#: Pigeon coronavirus.
_NAME_CODE = re.compile(r"^(?:\d{1,4}|(?=[A-Z0-9]{2,6}$)(?=[^\d]*\d)[A-Z0-9]+)$")
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
        if words and _IDENTIFIER.search(w):
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
    #: How many of them are inside the assay's own recent window, which may have widened.
    #: Defaulted, so a hand-built Cell in a test need not state it.
    recent: int = 0


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


# ---- Species, when each first arrived, and what is new (ROADMAP composition step 9) ----


@dataclass(frozen=True)
class SpeciesYear:
    """One species under an assay's target taxon, and when our archive first saw it."""

    taxid: int | None
    name: str
    #: The earliest deposit year IN OUR ARCHIVE. Not the species' first deposit in
    #: GenBank, and not when it was described: the archive holds what this assay's
    #: retrieval query returned, so a species may be older than the year printed here.
    first_year: int
    records: int
    #: First seen after the assay's `citation.design_year`, so the designers could not
    #: have had it in front of them. False whenever the design year is unknown.
    new_since_design: bool


def species_years(
    rows: Sequence[tuple[int | None, int, str]], taxonomy: Taxonomy, *, design_year: int | None
) -> list[SpeciesYear]:
    """``(taxid or None, deposit year, title)`` per record -> one row per species, oldest
    first, ties by name.

    A taxid is canonicalised and rolled up to its species, so a merged-away id and its
    current one are one species (11232 -> 3052342), and a no-rank child is its species
    rather than a species of its own (3139435 "canine distemper virus" under
    *Morbillivirus canis*) -- the shape that made a species copy look new to the archive
    before `taxonomy.species_of` existed.

    A record whose metadata carries no taxid, which is most of the archives, is named from
    its title by `organism` and cannot be rolled up; a taxid the cache does not hold is
    kept as itself and named from its title. A record with no deposit year cannot date
    anything and is dropped, which is why the counts here can be below the archive's.
    """
    first: dict[tuple[int | None, str], int] = {}
    counts: Counter[tuple[int | None, str]] = Counter()
    for taxid, year, title in rows:
        if year <= 0:
            continue
        key_id, name = resolve_species(taxid, title, taxonomy)
        key = (key_id, name or "unnamed")
        counts[key] += 1
        first[key] = min(first.get(key, year), year)
    out = [
        SpeciesYear(
            taxid=key[0],
            name=key[1],
            first_year=first[key],
            records=n,
            new_since_design=design_year is not None and first[key] > design_year,
        )
        for key, n in counts.items()
    ]
    return sorted(out, key=lambda s: (s.first_year, s.name))


# ---- The panel's cells (ROADMAP composition step 11) ----

#: A record whose primers both landed past the mismatch budget, so it has no amplicon and
#: no window: its own stratum, drawn and counted (decision 2026-11-02, finding 1). The
#: label space is shared with `subcluster.OTHER` (-1) and `UNPLACED` (-2), and a test
#: pins that the three cannot collide.
DIVERGED = -3

#: Strata that say what the clustering could NOT do. They are never pooled into "other":
#: the panel's sentence states their share, and pooling would hide exactly that.
_NEVER_POOLED = (DIVERGED, UNPLACED)


def cells_from(records: Sequence[GraphRecord], labels: Mapping[str, int]) -> list[Cell]:
    """The panel's cells for one assay: year x lineage x records x detections.

    ``labels`` maps record id to the cluster `assign_nearest` placed it in. A record that
    is not in it is `UNPLACED`, and a DIVERGED record takes that stratum whatever label it
    might have been given, since no window exists to have clustered.

    Only records in the graph's denominator are counted, because the panel sits under the
    graph and shares it: a record with no amplicon is not in the graph's evaluable count
    and must not appear in the bar below it. `detected` is the graph's own detection rule,
    already resolved per assay on `GraphRecord`.
    """
    totals: dict[tuple[int, int], list[int]] = defaultdict(lambda: [0, 0, 0])
    for r in records:
        if not r.evaluable:
            continue
        label = DIVERGED if r.diverged else labels.get(r.record_id, UNPLACED)
        cell = totals[(r.year, label)]
        cell[0] += 1
        cell[1] += int(r.detected)
        cell[2] += int(r.recent)
    return [Cell(year, cluster, n, d, rec) for (year, cluster), (n, d, rec) in sorted(totals.items())]


def pool_small_clusters(cells: Sequence[Cell], *, show: int) -> list[Cell]:
    """Keep the ``show`` biggest clusters of an assay and pool the rest into `OTHER`.

    Ranked by each cluster's records over ALL years, so a cluster keeps its identity
    across the panel rather than appearing and vanishing year by year. Ties go to the
    lower label, which `components_at` already ordered by size. `DIVERGED` and `UNPLACED`
    are kept whatever their size. Every record and every year survives.
    """
    size: dict[int, int] = defaultdict(int)
    for c in cells:
        if c.cluster not in _NEVER_POOLED:
            size[c.cluster] += c.records
    keep = {k for k, _ in sorted(size.items(), key=lambda kv: (-kv[1], kv[0]))[:show]}
    totals: dict[tuple[int, int], list[int]] = defaultdict(lambda: [0, 0, 0])
    for c in cells:
        label = c.cluster if (c.cluster in keep or c.cluster in _NEVER_POOLED) else OTHER
        cell = totals[(c.year, label)]
        cell[0] += c.records
        cell[1] += c.detected
        cell[2] += c.recent
    return [Cell(year, cluster, n, d, rec) for (year, cluster), (n, d, rec) in sorted(totals.items())]


# ---- The stage: one assay at a time, then the run (ROADMAP composition step 12) ----

#: `composition.tsv`'s columns, in order. The panel is drawn from these and from
#: `composition.json`; the TSV is the readable half, one row per (assay, year, cluster).
TSV_COLUMNS = (
    "assay_id",
    "year",
    "cluster_id",
    "cluster_name",
    "cluster_rank",
    "records",
    "detected",
    "recent_records",
    "top_species",
    "top_species_taxid",
    "species_mix",
    "cluster_first_year",
    "new_since_design",
    "representative",
    "cut",
    "left_bp",
    "right_bp",
)


@dataclass(frozen=True)
class Cluster:
    """One lineage of one assay, as the panel labels it."""

    id: int
    name: str
    n_records: int
    #: The lowest-ranked accession in the cluster: its stable identity across runs.
    representative: str
    species_mix: tuple[tuple[str, int], ...]
    top_species_taxid: int | None
    title_tokens: tuple[str, ...]
    first_year: int | None
    new_since_design: bool


@dataclass(frozen=True)
class AssayComposition:
    """One assay's lineage composition over time."""

    assay_id: str
    cut: float
    left_bp: int
    right_bp: int
    clusters: tuple[Cluster, ...]
    cells: tuple[Cell, ...]
    #: Deposit year -> detected share, as the graph draws it and on a fixed mix.
    observed: dict[int, float]
    same_mix: dict[int, float]
    split: Split | None
    species: tuple[SpeciesYear, ...]
    #: What this assay's reader has to be told: how much is unplaced or diverged, and
    #: whether the clustering could run at all.
    note: str
    #: `{"query": {year: n}, "taxon": {year: n}}` from `retrieve --year-counts`: how many
    #: records this assay's retrieval query returned per deposit year against how many its
    #: target taxon holds. Where the first falls away from the second, the query stopped
    #: seeing what was deposited, which is a fact about the QUERY and not the taxon -- the
    #: influenza case of 2026-10-30. DEFAULTED, because a run without a coverage file is a
    #: complete run: the series is a lens on the stage, not an input to it.
    coverage: dict[str, dict[int, int]] = dataclasses.field(default_factory=dict)


@dataclass(frozen=True)
class CompositionRun:
    run_date: str
    assays: dict[str, AssayComposition]


def resolve_species(taxid: int | None, title: str, taxonomy: Taxonomy | None) -> tuple[int | None, str]:
    """One record's species: its taxid rolled up to species rank where the cache knows it,
    else the name in its title. The one place either is decided, so the cluster mixes and
    `species_years` cannot disagree about what a record is."""
    key: int | None = None
    name = ""
    if taxid and taxonomy is not None:
        canon = taxonomy.canonical(taxid)
        key = taxonomy.species_of(canon) or canon
        name = taxonomy.name.get(key, "")
    elif taxid:
        key = taxid
    if not name:
        name = organism(title) or (f"taxid {key}" if key else "")
    return key, name


def label_records(regions: list[Region], years: list[int], opts: Options) -> tuple[dict[str, int], float]:
    """Cluster an assay's windows and label every record. Returns (record id -> label,
    the cut used). Sampled windows set the clusters; everything else, short flanks
    included, is assigned to its nearest sampled member (`assign_nearest`)."""
    picked = sample_windows(regions, years, opts.sample_cap)
    if len(picked) < opts.min_cluster_size:
        return {}, opts.cut
    ref = [regions[i].seq for i in picked]
    dist = mash_distances(jaccard_matrix(kmer_matrix(ref, opts.kmer_len)), opts.kmer_len)
    ref_labels = components_at(dist, opts.cut, opts.min_cluster_size)
    chosen = set(picked)
    rest = [i for i in range(len(regions)) if i not in chosen]
    labels = {regions[i].record_id: lab for i, lab in zip(picked, ref_labels, strict=True)}
    if rest:
        short = {n for n, i in enumerate(rest) if not regions[i].full_flank}
        assigned = assign_nearest(
            [regions[i].seq for i in rest],
            ref,
            ref_labels,
            opts.kmer_len,
            opts.cut,
            containment_for=short,
        )
        labels.update({regions[i].record_id: lab for i, lab in zip(rest, assigned, strict=True)})
    return labels, opts.cut


def name_drawn(
    drawn: Sequence[int],
    mixes: Sequence[Sequence[tuple[str, int]]],
    representatives: Sequence[str],
    *,
    pure_share: float,
) -> list[str]:
    """The name of each drawn column. Only real clusters enter `cluster_names`: counting
    diverged, unplaced and other toward its numbering made Annis's one group
    "B. dendrobatidis 4", implying three lineages that do not exist."""
    real = [i for i, lab in enumerate(drawn) if lab >= 0]
    named = cluster_names([mixes[i] for i in real], [representatives[i] for i in real], pure_share=pure_share)
    by_position = dict(zip(real, named, strict=True))
    return [by_position.get(i) or _special_name(lab) or "" for i, lab in enumerate(drawn)]


def describe_clusters(
    cells: Sequence[Cell],
    labels: Mapping[str, int],
    species: Mapping[str, tuple[int | None, str]],
    titles: Mapping[str, str],
    years: Mapping[str, int],
    design_year: int | None,
    opts: Options,
) -> tuple[Cluster, ...]:
    """Name every drawn cluster and say what else it holds."""
    drawn = sorted({c.cluster for c in cells})
    members: dict[int, list[str]] = defaultdict(list)
    for rid, lab in labels.items():
        members[lab].append(rid)
    for lab in drawn:
        members.setdefault(lab, [])
    mixes = [species_mix([species.get(r, (None, ""))[1] for r in members[lab]]) for lab in drawn]
    reps = [min(members[lab], key=_order_key) if members[lab] else "" for lab in drawn]
    names = name_drawn(drawn, mixes, reps, pure_share=opts.name_pure_share)
    by_cluster = {lab: [titles.get(r, "") for r in members[lab]] for lab in drawn}
    out = []
    for lab, mix, rep, name in zip(drawn, mixes, reps, names, strict=True):
        background = [t for other, rows in by_cluster.items() if other != lab for t in rows]
        first = min((years[r] for r in members[lab] if r in years), default=None)
        top_taxid = next(
            (
                species[r][0]
                for r in members[lab]
                if r in species and species[r][1] == (mix[0][0] if mix else None)
            ),
            None,
        )
        out.append(
            Cluster(
                id=lab,
                name=name,
                n_records=sum(c.records for c in cells if c.cluster == lab),
                representative=rep,
                species_mix=tuple(mix),
                top_species_taxid=top_taxid,
                title_tokens=tuple(
                    title_tokens(
                        by_cluster[lab],
                        background,
                        # A stratum's name is not in its titles, its modal species may be.
                        name=cluster_names([mix], [rep], pure_share=opts.name_pure_share)[0],
                        min_share=opts.token_min_share,
                        min_lift=opts.token_min_lift,
                        top=opts.title_tokens_shown,
                    )
                ),
                first_year=first,
                # Only a real cluster can be new: "diverged", "unplaced" and "other" are
                # statements about the clustering, and a badge on one would read as a
                # finding about the taxon.
                new_since_design=(
                    lab >= 0 and design_year is not None and first is not None and first > design_year
                ),
            )
        )
    return tuple(out)


def _special_name(label: int) -> str:
    """The three labels that are not clusters say what they are, not a species."""
    return {DIVERGED: "diverged (no site)", UNPLACED: "unplaced", OTHER: "other"}.get(label, "")


def write(run: CompositionRun, out_dir: Path) -> tuple[Path, Path]:
    """Write `composition.tsv` (one row per assay, year and cluster) and
    `composition.json` (everything, for the site and the report). Returns both paths."""
    out_dir.mkdir(parents=True, exist_ok=True)
    tsv, js = out_dir / "composition.tsv", out_dir / "composition.json"
    with tsv.open("w") as fh:
        fh.write("\t".join(TSV_COLUMNS) + "\n")
        for assay_id, a in sorted(run.assays.items()):
            by_id = {c.id: (rank, c) for rank, c in enumerate(a.clusters)}
            for cell in a.cells:
                rank, cluster = by_id.get(cell.cluster, (-1, None))
                mix = cluster.species_mix if cluster else ()
                fh.write(
                    "\t".join(
                        str(v)
                        for v in (
                            assay_id,
                            cell.year,
                            cell.cluster,
                            cluster.name if cluster else "",
                            rank,
                            cell.records,
                            cell.detected,
                            cell.recent,
                            mix[0][0] if mix else "",
                            (cluster.top_species_taxid if cluster else None) or "",
                            "; ".join(f"{name} {n}" for name, n in mix[:4]),
                            (cluster.first_year if cluster else None) or "",
                            int(cluster.new_since_design) if cluster else 0,
                            cluster.representative if cluster else "",
                            f"{a.cut:g}",
                            a.left_bp,
                            a.right_bp,
                        )
                    )
                    + "\n"
                )
    js.write_text(json.dumps(_as_json(run), indent=1, sort_keys=True) + "\n")
    return tsv, js


def _as_json(run: CompositionRun) -> dict[str, Any]:
    return {
        "run_date": run.run_date,
        "assays": {
            aid: {
                "cut": a.cut,
                "left_bp": a.left_bp,
                "right_bp": a.right_bp,
                "note": a.note,
                "clusters": [dataclasses.asdict(c) for c in a.clusters],
                "cells": [dataclasses.asdict(c) for c in a.cells],
                "coverage": {k: {str(y): n for y, n in v.items()} for k, v in a.coverage.items()},
                "observed": {str(y): v for y, v in a.observed.items()},
                "same_mix": {str(y): v for y, v in a.same_mix.items()},
                "split": dataclasses.asdict(a.split) if a.split else None,
                "species": [dataclasses.asdict(s) for s in a.species],
            }
            for aid, a in sorted(run.assays.items())
        },
    }


def read_summary(path: Path) -> CompositionRun:
    """Read back what `write` wrote, as the same objects. The site and the report read a
    run through this, so the JSON is a format and not a dump: a round-trip test holds it
    to that."""
    data = json.loads(Path(path).read_text())
    assays = {}
    for aid, a in data["assays"].items():
        split = a.get("split")
        assays[aid] = AssayComposition(
            assay_id=aid,
            cut=a["cut"],
            left_bp=a["left_bp"],
            right_bp=a["right_bp"],
            clusters=tuple(
                Cluster(
                    **{
                        **c,
                        "species_mix": tuple((n, k) for n, k in c["species_mix"]),
                        "title_tokens": tuple(c["title_tokens"]),
                    }
                )
                for c in a["clusters"]
            ),
            cells=tuple(Cell(**c) for c in a["cells"]),
            coverage={
                k: {int(y): int(n) for y, n in v.items()} for k, v in (a.get("coverage") or {}).items()
            },
            observed={int(y): v for y, v in a["observed"].items()},
            same_mix={int(y): v for y, v in a["same_mix"].items()},
            split=(
                Split(
                    **{
                        **split,
                        "mix_ci": tuple(split["mix_ci"]) if split["mix_ci"] else None,
                        "within_ci": tuple(split["within_ci"]) if split["within_ci"] else None,
                        "one_period_clusters": tuple(split["one_period_clusters"]),
                    }
                )
                if split
                else None
            ),
            species=tuple(SpeciesYear(**s) for s in a["species"]),
            note=a["note"],
        )
    return CompositionRun(run_date=data["run_date"], assays=assays)


# ---- The compact file the website reads (ROADMAP composition step 15) ----

#: `website/data/composition.json`'s schema version. The site refuses a file it does not
#: know, as it already does for `run.json`.
SITE_SCHEMA = 2


def site_data(run: CompositionRun) -> dict[str, Any]:
    """`website/data/composition.json`: the panel's data, COLUMNAR.

    A separate file from `run.json` (decided 2026-11-02), which is 2.5 MB and committed
    every week: this would more than double it, and every weekly commit would carry the
    growth in the repository's history for good.

    Columnar because the shape is a dense grid. One `names` list per assay holds each
    drawn cluster's label once; `years` holds the years that have records; `records` and
    `detected` are one row per year, one column per cluster, aligned by index to both. The
    object-per-cell form of the same grid was about four times the size on the measured
    runs, and a reader of the file cannot tell which cells are missing from it, where an
    aligned grid says so by construction.
    """
    out: dict[str, Any] = {"schema": SITE_SCHEMA, "run_date": run.run_date, "assays": {}}
    for assay_id, a in sorted(run.assays.items()):
        ids = [c.id for c in a.clusters]
        slot = {cid: i for i, cid in enumerate(ids)}
        years = sorted({c.year for c in a.cells})
        records = [[0] * len(ids) for _ in years]
        detected = [[0] * len(ids) for _ in years]
        for cell in a.cells:
            if cell.cluster not in slot:
                continue
            row, col = years.index(cell.year), slot[cell.cluster]
            records[row][col] += cell.records
            detected[row][col] += cell.detected
        s = a.split
        coverage_years = sorted({y for series in a.coverage.values() for y in series})
        out["assays"][assay_id] = {
            "cut": a.cut,
            "left_bp": a.left_bp,
            "right_bp": a.right_bp,
            "note": a.note,
            "ids": ids,
            "names": [c.name for c in a.clusters],
            "mix": [[list(m) for m in c.species_mix[:3]] for c in a.clusters],
            "tokens": [list(c.title_tokens) for c in a.clusters],
            "new_since_design": [bool(c.new_since_design) for c in a.clusters],
            "years": years,
            # Aligned to `coverage_years`, NOT `years`: the series exists for the years an
            # archive stopped while the taxon went on, which have no cells. What the query
            # returned and what the taxon holds, or null where the count is not known (NCBI
            # unreachable and nothing cached -- which is not the same as zero).
            "coverage_years": coverage_years,
            "coverage_query": [a.coverage.get("query", {}).get(y) for y in coverage_years],
            "coverage_taxon": [a.coverage.get("taxon", {}).get(y) for y in coverage_years],
            "records": records,
            "detected": detected,
            # Aligned to `years`; null for a year whose clusters cover too little of the
            # period's weight to standardise (`same_mix_min_covered`). Rounded, because
            # this file is committed every run and 17 digits of a float that moved in the
            # 12th are a diff nobody can read.
            "same_mix": [None if (v := a.same_mix.get(y)) is None else round(v, 4) for y in years],
            "split": (
                None
                if s is None
                else {
                    "change": round(s.change, 4),
                    "mix": round(s.mix, 4),
                    "within": round(s.within, 4),
                    "mix_ci": [round(v, 4) for v in s.mix_ci] if s.mix_ci else None,
                    "within_ci": [round(v, 4) for v in s.within_ci] if s.within_ci else None,
                    "baseline_share": round(s.baseline_share, 4),
                    "recent_share": round(s.recent_share, 4),
                }
            ),
        }
    return out


def _site_json(data: dict[str, Any]) -> str:
    """ONE LINE PER ASSAY, compact within it.

    The file is committed every run, so its diff has to be readable: a line per assay
    means a changed assay is a changed line, and `git log -p` says which assays moved.
    `json.dumps(indent=1)`, which `run.json` uses, spends a newline and a space on every
    number of a dense numeric grid -- 2.6x the bytes here, measured -- and a fully compact
    file would be one line whose diff says only that something changed.
    """
    assays = ",\n".join(
        f"  {json.dumps(aid)}: {json.dumps(body, separators=(',', ':'))}"
        for aid, body in data["assays"].items()
    )
    return (
        "{\n"
        f' "schema": {json.dumps(data["schema"])},\n'
        f' "run_date": {json.dumps(data["run_date"])},\n'
        ' "assays": {\n' + assays + "\n }\n}\n"
    )


def write_site_data(run: CompositionRun, out_dir: Path, *, max_bytes: int) -> Path:
    """Write `composition.json` for the website, refusing to exceed `max_bytes`.

    The cap is a real gate and not a warning: this file is committed on every run, and a
    file that grew without anyone noticing would be noticed only in the repository's size.
    It nearly fired on the first real measurement: at `json.dumps(indent=1)`, two assays
    of the 2026-11-01 run came to 13.8 KB, which is about 1,491 KB over 216 assays against
    a 1,465 KB cap. `_site_json` writes the same data at 5.2 KB for those two, about
    567 KB over the registry.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "composition.json"
    text = _site_json(site_data(run))
    if len(text.encode()) > max_bytes:
        raise ValueError(
            f"composition.json would be {len(text.encode()):,} bytes, over the "
            f"composition.site_max_bytes cap of {max_bytes:,}: draw fewer clusters "
            f"(composition.show_clusters) or raise the cap deliberately"
        )
    path.write_text(text)
    return path
