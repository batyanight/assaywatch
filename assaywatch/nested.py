"""Nested protocols: score each round on its own, then warn round 2 about round 1.

A nested or semi-nested protocol is several entries here, one per round, and
each is screened as an independent assay. That is right, and it is also how the
report became misleading: on the 2026-10-07 records, 10 of 23 families carry
rounds with contradictory statuses, and `Lyssavirus_N_Vazquez-Moron_2006_round1`
is the extreme - round 1 `low coverage` at 32.5%, round 2 `stable` at 99.5%,
printed as two rows a screen apart.

THE BIOLOGY THE TWO ROWS LEAVE OUT. Screening asks what each pair does against
a GenBank record, which for round 2 is the question "would these primers bind
this sequence" - the right question for round 2 run DIRECTLY on a sample, and
the wrong one for round 2 run as published, where its template is not the
sequence but round 1's product. A record whose outer primers have drifted
yields no round-1 product, so the nested reaction has nothing enriched to work
on, however well the inner primers match. Round 2's 99.5% is therefore a real
number about a direct PCR and an unreachable one about the nested protocol: on
the same records, both rounds succeed on 32.4%.

WHAT THIS MODULE DOES, AND DOES NOT. It computes, per record, the share where
BOTH rounds would amplify - the nested protocol's own coverage - and compares
it with each round's standalone share. Nothing is merged and no status changes:
each round keeps the score it earned, because either product can be read on a
gel and a round whose primers still match is still a usable assay on its own.
What is added is the warning the per-round rows cannot carry.

THE DEPENDENCY IS ONE-DIRECTIONAL. Round 1 failing compromises round 2; round 2
failing does not compromise round 1, whose product is still there to read. So
the warning propagates outward-in only.

WHICH ROUND-1 FAILURES COUNT. Only the ones that are the assay's fault: a `fail`
call, or a `no_amplicon` the screener labelled `diverged` (the binding site is
present in the deposit and does not match). A `truncated` deposit, or one with
no credible site at all, says something about GenBank rather than about round 1
- the same distinction the drift denominator already makes, for the same
reason.

A SEMI-NESTED PAIR SHARING AN OLIGO is not two independent rounds: the Landolfi
orthoreovirus rounds share forward primer 2090F, so an escape there takes both
at once. The per-record arithmetic handles that correctly - a record failing
both is counted once - but the note says when a family shares an oligo, because
a reader estimating the risk of the two rounds failing together should not
assume independence.
"""

from __future__ import annotations

import re
from collections import defaultdict
from collections.abc import Iterable, Iterator, Mapping
from dataclasses import dataclass, field
from typing import Any

ROUND_SUFFIX = re.compile(r"_round\d+[A-Z]?$", re.I)

DETECTED = ("detect", "reduced")
# A round-1 outcome that is evidence about the assay rather than about the deposit.
ASSAY_FAILURE = ("fail",)
ASSAY_FAILURE_EXCLUSION = ("diverged",)


def family_id(assay_id: str) -> str:
    """The id with any `_round2` / `_round2B` suffix removed."""
    return ROUND_SUFFIX.sub("", assay_id)


def _declares_nest(assay: Any) -> bool:
    """Does this entry say it is part of a nest at all?"""
    src = getattr(assay, "source", None)
    if src is None:
        return False
    return bool(getattr(src, "nested_round", None) or getattr(src, "nested_family", None))


def family_of(assay_id: str, assay: Any = None) -> str:
    """The nest an entry belongs to: `source.nested_family` if it says, else the id base."""
    src = getattr(assay, "source", None) if assay is not None else None
    declared = getattr(src, "nested_family", None) if src is not None else None
    return declared or family_id(assay_id)


def families(assays: Mapping[str, Any]) -> dict[str, list[str]]:
    """{family: [assay ids]} for every family carrying more than one round.

    Membership is the registry's word, not the geometry. Round 2's amplicon
    lies inside round 1's, which is tempting to detect from the calls table -
    but any two assays targeting one gene nest that way without being one
    protocol, and the data says so: an unrelated adenovirus round 2 (since
    removed) sat inside the Casas hexon amplicon on 5,810 records. So the registry
    declares the family and containment checks it.

    Pass the `{id: assay}` mapping, not a list of ids. Given the mapping, an
    entry joins a family only if it SAYS it is a round, and a declared
    `source.nested_family` overrides the id base. Both matter: sharing a base
    is not the same as being a round of the same protocol, and the 440 bp
    coronavirus consensus entry proved it by displacing Lan 2010's real round 1
    and making that nest read as disjoint. A bare iterable of ids is still
    accepted, and then the id base is all there is to go on.
    """
    mapping = assays if isinstance(assays, Mapping) else None
    out: dict[str, list[str]] = defaultdict(list)
    for aid in assays:
        assay = mapping.get(aid) if mapping is not None else None
        if mapping is not None and not _declares_nest(assay):
            continue
        out[family_of(aid, assay)].append(aid)
    return {k: sorted(v) for k, v in sorted(out.items()) if len(v) > 1}


def unpaired(assays: dict[str, Any]) -> list[str]:
    """Entries declaring a round that end up in no family.

    15 on 2026-10-14, when the id base was the only key. Most were not missing a
    sibling at all - the sibling was there under an unlike name, and
    `source.nested_family` now joins them. What should remain is the genuinely
    unpartnered: `Elephant_endotheliotropic_herpesvirus_6_POL_Latimer_2012_round2`, whose round 1 is
    not in the registry, and any round-2 entry whose outer round has not been
    identified (the two `Orthohantavirus_S_Anthony_2013_round1` round 2s, which carry no
    DOI and whose outer rounds are a curator's call, not a guess).

    Listed rather than guessed: a warning that cannot be computed is better
    missing than invented.
    """
    grouped = {i for v in families(assays).values() for i in v}
    out = []
    for aid, a in assays.items():
        if aid in grouped:
            continue
        src = getattr(a, "source", None)
        if src is not None and getattr(src, "nested_round", None):
            out.append(aid)
    return sorted(out)


def _round_number(assay: Any) -> int | None:
    """The round an entry declares, as an integer. None when it declares none."""
    src = getattr(assay, "source", None)
    raw = getattr(src, "nested_round", None) if src is not None else None
    if not raw:
        return None
    m = re.search(r"\d+", str(raw))
    return int(m.group()) if m else None


def _order(rounds: list[str], assays: dict[str, Any]) -> tuple[str, str]:
    """(outer, inner) for a two-round family: which is round 1 and which round 2.

    NOT the id order. The base id usually holds round 1, with the `_round2`
    sibling beside it - but not always: the Landolfi orthoreovirus entry stored
    the paper's SECOND round all along, so its family is a base holding round 2
    and a `_round1` sibling. Taking the base as the outer round inverted that
    pair, and the containment check caught it, reporting 0 of 987 records with
    the inner amplicon inside the outer when the truth is the reverse.

    So the order is read from what the registry declares, in descending
    confidence: `source.nested_round`, then the declared product sizes (an
    outer round is the longer product, which is what nesting means), then the
    id. Each fallback is weaker than the last, and the containment check is
    what catches a family where all three are wrong.
    """
    a, b = rounds
    na, nb = _round_number(assays.get(a)), _round_number(assays.get(b))
    if na is not None and nb is not None and na != nb:
        return (a, b) if na < nb else (b, a)
    pa = getattr(assays.get(a), "amplicon_bp", None)
    pb = getattr(assays.get(b), "amplicon_bp", None)
    if pa and pb and pa != pb:
        return (a, b) if pa > pb else (b, a)
    return a, b


SITE = re.compile(r"^(\d+)-(\d+)([+-])$")


def _three_prime(site: Any) -> int | None:
    """The 3' end of a primer's binding site, as written by the screener (`2885-2912-`).

    The 3' end is the one that has to anneal: a polymerase extends from the
    3'-OH, and a primer whose 5' tail hangs off the end of the template primes
    anyway. On the plus strand that is the higher coordinate, on the minus
    strand the lower one.
    """
    if not site:
        return None
    m = SITE.match(str(site).strip())
    if not m:
        return None
    lo, hi, strand = int(m.group(1)), int(m.group(2)), m.group(3)
    return hi if strand == "+" else lo


def _usable(call: str, exclusion: str) -> bool:
    """Is this row evidence about the assay, rather than about the deposit?"""
    return call in DETECTED or call in ASSAY_FAILURE or exclusion in ASSAY_FAILURE_EXCLUSION


def nest_calls(
    path: NestPath, calls: Mapping[str, Mapping[str, Mapping[str, Any]]]
) -> Iterator[Mapping[str, Any]]:
    """The protocol's own calls, one per record every round can be judged on.

    Emitted in the shape the screen already produces, keyed to `nest_id`, so
    the existing drift assessment scores a nest with no second statistics
    engine: thresholds, intervals, the recent window and the undecided statuses
    all apply unchanged.

    The call IS the terminal round's call -- its footprint, its sites, its
    reason -- downgraded to `fail` when any round above it does not amplify.
    That is the biology: round 2's template is round 1's product, not the
    deposit, so an inner pair that matches perfectly yields nothing when the
    outer reaction has already failed.

    WHICH RECORDS COUNT. Only those every round on the path is evidence about.
    A `fail`, or a `no_amplicon` the screener labelled `diverged`, is the
    assay's fault and counts; a truncated deposit or one with no credible site
    says something about GenBank instead, and the record is not emitted at all
    -- the same distinction the drift denominator already makes.
    """
    for row, rows in _protocol_records(path, calls):
        reached = all(r.get("call") in DETECTED for r in rows)
        out = dict(row)
        out["assay_id"] = path.nest_id
        if not reached:
            out["call"] = "fail"
            out["exclusion"] = ""
        yield out


def _protocol_records(
    path: NestPath, calls: Mapping[str, Mapping[str, Mapping[str, Any]]]
) -> Iterator[tuple[Mapping[str, Any], list[Mapping[str, Any]]]]:
    """(terminal row, upstream rows) for each record every round is evidence about.

    The one definition of which records a protocol counts, shared by
    `nest_calls` and `round_calls` so the two cannot drift apart.
    """
    terminal = calls.get(path.nest_id) or {}
    upstream = [calls.get(r) or {} for r in path.rounds[:-1]]
    for rid, row in terminal.items():
        if not _usable(row.get("call", ""), row.get("exclusion", "")):
            continue
        rows = [u.get(rid) for u in upstream]
        if any(r is None or not _usable(r.get("call", ""), r.get("exclusion", "")) for r in rows):
            continue
        yield row, rows  # type: ignore[misc]  # None ruled out above


def round_alone_id(nest_id: str, round_id: str) -> str:
    """The key for one round measured alone on one protocol's records.

    Keyed by both, because a shared round is a different measurement under each
    protocol: Messmer's genus round 1 sits under three species protocols.
    """
    return f"{nest_id}@{round_id}"


def round_calls(
    path: NestPath, calls: Mapping[str, Mapping[str, Mapping[str, Any]]]
) -> Iterator[Mapping[str, Any]]:
    """Each round's OWN call, on exactly the records the protocol counts.

    A round's own assessment covers its own target. Where a genus round 1 feeds
    a species round 2 (Chlamydia, Messmer 1997) that figure describes the
    genus, and on the species protocol's page it would be read as what round 1
    costs that protocol. Measured on the protocol's records instead, the gap
    between a round's share and the protocol's is the gating and nothing else,
    and the protocol's share can never exceed its weakest round's.
    Keyed by `round_alone_id`, in the screen's call shape, so the ordinary
    assessment scores it with the protocol's scope and window.
    """
    for row, rows in _protocol_records(path, calls):
        for round_id, r in zip(path.rounds, [*rows, row], strict=True):
            out = dict(r)
            out["assay_id"] = round_alone_id(path.nest_id, round_id)
            yield out


@dataclass(frozen=True)
class NestPath:
    """One nested protocol: the route from a root round to a terminal one.

    A FAMILY is not a protocol. `Chlamydia_16S_Messmer_1997` is one genus-level
    round 1 feeding three species-specific round 2 entries, which is three
    protocols with three targets; `Elephant_endotheliotropic_herpesvirus_5_POL_Latimer_2012` has `round2` and
    `round2B` as alternatives rather than a chain. A path is what a lab runs,
    and it is identified by the round it ENDS on, since every terminal round has
    exactly one chain of parents behind it.
    """

    nest_id: str  # the terminal round's assay id
    family: str
    rounds: tuple[str, ...]  # root -> terminal, in order
    shared_oligos: tuple[str, ...]  # sequences used by more than one round


def _oligo_seqs(assay: Any) -> set[str]:
    out = set()
    for role in ("forward", "reverse", "probe"):
        o = getattr(assay.oligos, role, None)
        seq = getattr(o, "matching_seq", None) if o is not None else None
        if seq:
            out.add(seq)
    return out


def paths(assays: Mapping[str, Any]) -> list[NestPath]:
    """Every full path. A terminal round is one no other round names as parent.

    Partial routes are not protocols: where a paper prescribes three rounds,
    `r1 -> r2` is not something it published. A round whose parent is genuinely
    absent (`nested_parent_not_held`) yields no path at all, because a protocol
    that cannot be assembled must not be scored as one -- it keeps its own
    standalone verdict instead.
    """
    rounds = {i: a for i, a in assays.items() if getattr(a.source, "nested_round", None)}
    parent_of = {i: getattr(a.source, "nested_parent", None) for i, a in rounds.items()}
    has_child = {p for p in parent_of.values() if p}
    out: list[NestPath] = []
    for i, a in sorted(rounds.items()):
        if i in has_child or not parent_of.get(i):
            continue  # not terminal, or a root with nothing below it
        chain = [i]
        seen = {i}
        node = i
        while up := parent_of.get(node):
            if up in seen or up not in rounds:
                break  # a cycle, or a parent outside the registry
            chain.append(up)
            seen.add(up)
            node = up
        chain.reverse()
        counts: dict[str, int] = defaultdict(int)
        for member in chain:
            for seq in _oligo_seqs(rounds[member]):
                counts[seq] += 1
        out.append(
            NestPath(
                nest_id=i,
                family=getattr(a.source, "nested_family", None) or family_id(i),
                rounds=tuple(chain),
                shared_oligos=tuple(sorted(s for s, n in counts.items() if n > 1)),
            )
        )
    return out


def nest_scope(path: NestPath, assays: Mapping[str, Any]) -> frozenset[int] | None:
    """The intersection of the rounds' scopes, or None when none restricts.

    A record is the nest's business only if every round claims it. On the
    Chlamydia branch that makes a *C. psittaci* record out of scope for the
    pneumoniae protocol rather than a failure of it, which is the
    `scope_narrower_than_taxid` trap. An unrestricted round constrains nothing
    and is skipped, so the intersection is over the rounds that do restrict.
    """
    scopes = []
    for member in path.rounds:
        a = assays.get(member)
        taxids = getattr(getattr(a, "target", None), "scope_taxids", None)
        if taxids:
            scopes.append(frozenset(int(t) for t in taxids))
    if not scopes:
        return None
    return frozenset.intersection(*scopes)


def nest_assays(ps: Iterable[NestPath], assays: Mapping[str, Any]) -> dict[str, Any]:
    """Each nest as a synthetic assay the ordinary assessment can score.

    The alternative was a second set of rules inside the report, which is how
    two documents come to disagree. Instead the nest is the TERMINAL round with
    three things replaced:

      * `target.scope_taxids`, the intersection over the path, so a record is
        the nest's business only if every round claims it;
      * `status`, the weakest of its rounds -- `active` only when all are;
      * `needs_review`, the union, so a blocking flag anywhere on the path
        withholds the protocol. Borna is the case: round 2's printed primer may
        be a transcription error, and a protocol built on it must not publish a
        verdict just because round 1 is sound.

    Everything else -- taxid, chemistry, citation, oligos -- is the terminal
    round's, which is what the protocol yields and what its product size is.
    """
    rank = {"active": 0, "draft": 1, "deprecated": 2}
    out: dict[str, Any] = {}
    for path in ps:
        members = [assays[r] for r in path.rounds if r in assays]
        if len(members) != len(path.rounds):
            continue
        terminal = members[-1]
        scope = nest_scope(path, assays)
        weakest = max(members, key=lambda a: rank.get(str(getattr(a, "status", "draft")), 1))
        # One entry per FLAG, not per round: `nested_protocol` is on every round
        # by definition, and listing it once per round printed it twice on the
        # site (2026-11-02). The first round to carry it wins, so round 1's
        # wording leads; where a later round says something different its note
        # is pointed at rather than dropped, since a disclosure nobody can read
        # is worse than a long one.
        flags: list[Any] = []
        at: dict[str, int] = {}
        for member in members:
            for flag in getattr(member, "needs_review", None) or []:
                name = str(getattr(flag.flag, "value", flag.flag))
                if name not in at:
                    at[name] = len(flags)
                    flags.append(flag)
                    continue
                kept = flags[at[name]]
                note = kept.note or ""
                if flag.note and flag.note != note and "also on" not in note:
                    flags[at[name]] = kept.model_copy(
                        update={"note": f"{note or name}; also on {member.id}, which says more"}
                    )
        target = terminal.target.model_copy(update={"scope_taxids": sorted(scope) if scope else None})
        out[path.nest_id] = terminal.model_copy(
            update={"target": target, "status": weakest.status, "needs_review": flags}
        )
    return out


@dataclass
class NestedFamily:
    """One protocol's rounds, each round's own share, and the nest's own share."""

    family: str
    rounds: list[str]
    outer: str = ""
    inner: str = ""
    records: int = 0  # records where both rounds are evidence about the assay
    outer_detected: int = 0
    inner_detected: int = 0
    both_detected: int = 0
    # Records counted as round-1 failures only because the screener labelled them
    # `diverged`. Kept apart because that label is not reliable for every assay:
    # it needs one primer site credible by a per-record E-value, and across an
    # archive of thousands of records chance sites clear that bar. Sampled on
    # 2026-10-23, round-1 anchors ran from 96-97% near-perfect (Alphavirus NSP4,
    # Phlebovirus L) to 60% at five or six mismatches (Orthoreovirus Landolfi).
    # Counting these as failures is right where the label is right, so they stay
    # counted; this number is what lets a reader see how much of a nest's loss
    # rests on them. docs/journal/2026-10-23-wave2-diverged-and-patent.md.
    outer_diverged: int = 0
    shared_oligos: tuple[str, ...] = ()
    # {(outer, inner): (records where the inner amplicon sits inside the outer, records scored by both)}
    containment: dict[tuple[str, str], tuple[int, int]] = field(default_factory=dict)

    def _share(self, k: int) -> float | None:
        return k / self.records if self.records else None

    @property
    def outer_share(self) -> float | None:
        return self._share(self.outer_detected)

    @property
    def inner_share(self) -> float | None:
        """Round 2 run directly on the sample: what screening measures."""
        return self._share(self.inner_detected)

    @property
    def nested_share(self) -> float | None:
        """Round 2 run as published: both rounds must amplify the same record."""
        return self._share(self.both_detected)

    @property
    def gap(self) -> float | None:
        """How much of round 2's coverage is unreachable through round 1."""
        if self.inner_share is None or self.nested_share is None:
            return None
        return self.inner_share - self.nested_share

    @property
    def nests(self) -> bool | None:
        """Does the inner amplicon actually sit inside the outer one?

        None when no record was scored by both rounds. This is the check review
        3.8 asked for, and it does not pass everywhere.

        Every one of the three families reported as non-nesting on 2026-10-14
        turned out to be a fault in the measurement, not in a protocol. Two
        were mis-pairings by the id base: the coronavirus "disjoint" finding
        came from pairing Lan 2010's round 2 with the unrelated 440 bp
        consensus entry sharing its id base, and the CMV gB one from pairing
        Deckers' round 1 with Prepens' round 2. `source.nested_family` exists
        so that cannot recur.

        The third, `Enterovirus_VP3_VP1_Nix_2006_round1`, was correctly paired and failed
        on the criterion itself: the rounds share their reverse SITE and round
        2's primer is 8 nt longer at its 5' end, so its amplicon ended exactly
        8 bp past round 1's on 3,722 of 3,808 records while priming from the
        identical base. Asking where the inner primers extend FROM, rather than
        where their amplicon would end, reads it as the nest it is.

        On the 2026-10-15 calls all 26 families with per-record data now nest,
        and nothing fails. That is not the check going quiet: it still fails a
        pair whose inner primers land outside the outer product, which is what
        a reader should want it to mean.
        """
        c = self.containment.get((self.outer, self.inner))
        if not c or not c[1]:
            return None
        return c[0] / c[1] >= 0.5

    def warns(self, threshold: float, floor: float = 0.05) -> bool:
        """Does reading round 2's own share mislead about the protocol?

        Two ways it can. The one that matters most is a verdict flip: round 2
        clears the threshold on its own and the nest does not, which is the
        lyssavirus shape - 99.5% against 32.4%. The second is a fall large
        enough to matter even when both sides land on the same side of the
        threshold, which `floor` sets.
        """
        if self.gap is None or self.nested_share is None or self.inner_share is None:
            return False
        # A warning conditions round 2 on round 1, which is only meaningful if
        # round 2 really runs on round 1's product. Where the amplicons do not
        # nest, the right output is that finding, not a conditional share.
        if self.nests is not True:
            return False
        flipped = self.inner_share >= threshold > self.nested_share
        return flipped or self.gap >= floor

    def note(self, threshold: float) -> str:
        """The sentence the per-round rows cannot say on their own."""
        if not self.records:
            return ""
        if self.nests is False:
            c = self.containment.get((self.outer, self.inner), (0, 0))
            return (
                f"These entries are labelled as rounds of one protocol, but their amplicons do not nest: "
                f"on {c[1]:,} records scored by both, the inner product lies inside the outer on {c[0]:,}. "
                f"A nested reaction amplifies the outer product, so these two cannot be running that way "
                f"- either the round labels are wrong or they are separate assays that share a name. "
                f"No conditional coverage is reported for them, because conditioning round 2 on a round 1 "
                f"that does not feed it would invent a number. Curation, not a calculation."
            )
        assert self.nested_share is not None and self.inner_share is not None
        base = (
            f"Run as published, this nest detects {self.nested_share:.1%} of the {self.records:,} records "
            f"both rounds can be judged on: round 1 reaches {self.outer_share:.1%} and round 2 "
            f"{self.inner_share:.1%} on its own"
        )
        if not self.warns(threshold):
            return base + ", and round 1 is not what limits it."
        text = (
            base + f". Round 2's own figure is what it would do as a DIRECT PCR; within the nest "
            f"{self.gap:.1%} of that coverage is unreachable, because round 1 escapes on those records "
            f"and leaves the inner reaction no enriched template."
        )
        if self.inner_share >= threshold > self.nested_share:
            text += (
                f" That crosses the {threshold:.0%} threshold: round 2 alone reads as working and the "
                f"protocol does not."
            )
        if self.shared_oligos:
            text += (
                f" The rounds share {', '.join(self.shared_oligos)}, so their failures are not "
                f"independent - an escape there takes both."
            )
        return text


def assess(assays: dict[str, Any], calls: Iterable[Mapping[str, Any]]) -> dict[str, NestedFamily]:
    """Per-record nested coverage for every two-round family in the registry.

    `calls` is any iterable of screen rows (`assay_id`, `record_id`, `call`,
    optionally `exclusion`, `amplicon_start`, `amplicon_end`, `fwd_site`,
    `rev_site`). Containment uses the inner round's binding sites and falls
    back to its amplicon span only where sites were never written. Families with
    more than two rounds are grouped and counted but get no nested share: which
    round feeds which is a protocol fact the ids do not carry.
    """
    fams = {k: NestedFamily(k, v) for k, v in families(assays).items()}
    member = {i: k for k, f in fams.items() for i in f.rounds}
    for f in fams.values():
        if len(f.rounds) == 2:
            f.outer, f.inner = _order(f.rounds, assays)
            a, b = assays.get(f.outer), assays.get(f.inner)
            if a is not None and b is not None:
                seqs = {
                    n: {getattr(getattr(x.oligos, n, None), "matching_seq", None) for x in (a, b)}
                    for n in ("forward", "reverse", "probe")
                }
                f.shared_oligos = tuple(n for n, v in seqs.items() if len(v) == 1 and None not in v)

    per: dict[str, dict[str, tuple[str, str, Any, Any]]] = defaultdict(dict)
    for row in calls:
        aid = row.get("assay_id")
        if aid in member:
            per[row["record_id"]][aid] = (
                row.get("call", ""),
                row.get("exclusion") or "",
                row.get("amplicon_start"),
                row.get("amplicon_end"),
                row.get("fwd_site"),
                row.get("rev_site"),
            )
    for by_assay in per.values():
        for fam in fams.values():
            if not fam.outer or fam.outer not in by_assay or fam.inner not in by_assay:
                continue
            (oc, ox, os_, oe, _, _), (ic, ix, is_, ie, ifs, irs) = (
                by_assay[fam.outer],
                by_assay[fam.inner],
            )
            if not (_usable(oc, ox) and _usable(ic, ix)):
                continue
            fam.records += 1
            fam.outer_diverged += oc not in DETECTED and ox in ASSAY_FAILURE_EXCLUSION
            fam.outer_detected += oc in DETECTED
            fam.inner_detected += ic in DETECTED
            fam.both_detected += oc in DETECTED and ic in DETECTED
            if os_ in (None, "") or oe in (None, ""):
                continue
            os_, oe = int(os_), int(oe)
            # The inner reaction runs on the outer PRODUCT, so what has to lie
            # inside it is where the inner primers EXTEND FROM, not the span
            # they would make on an uncut template. Comparing amplicon spans
            # instead failed the enterovirus VP3/VP1 pair on 3,722 of 3,808
            # records for no biological reason: the two rounds share the
            # reverse site, and round 2's primer is 8 nt longer at its 5' end,
            # so its amplicon ends exactly 8 bp past round 1's while priming
            # from the identical base.
            f3, r3 = _three_prime(ifs), _three_prime(irs)
            if f3 is not None and r3 is not None:
                inside = os_ <= f3 <= oe and os_ <= r3 <= oe
            elif is_ not in (None, "") and ie not in (None, ""):
                # Calls written before the screener recorded binding sites.
                # The span test is stricter and is all there is to go on.
                inside = os_ <= int(is_) and int(ie) <= oe
            else:
                continue
            seen, total = fam.containment.get((fam.outer, fam.inner), (0, 0))
            fam.containment[(fam.outer, fam.inner)] = (seen + inside, total + 1)
    return fams
