# Nested protocols: scoring the thing a lab actually runs

**Status: design decided 2026-11-01 by grilling; STEPS 1, 2 and 3 ARE IMPLEMENTED**
(schema and declarations; `NestPath`/`paths`/`nest_scope`/`nest_calls`/`nest_assays`;
report and website), each step test-first. On the 2026-11-01 calls the registry declares
**34 protocols, of which 31 publish a verdict** -- 8 declining, 5 low coverage, 5
insufficient data, 2 no recent data, 11 stable -- and 3 are withheld because a round of
theirs is. The assay counts are untouched. What remains is listed under "Open" at the
end.

## The problem, in one paragraph

A nested protocol is several registry entries, one per round, each screened as an
independent assay. For round 2 that answers "would these primers bind this record",
which is the right question for round 2 run DIRECTLY on a sample and the wrong one for
round 2 run as published, where its template is round 1's product and not the deposit.
`nested.py` already computes the protocol's own coverage and writes a prose warning in
one report section; it carries no status, no trend, and nothing on the website.

## What that hides, measured 2026-11-01 on `results/2026-11-01/calls.tsv.gz`

27 candidate paths, **22 with at least 15 evaluable records**, so this is not a thin
feature. Both-rounds-evaluable denominators and nested shares:

| path (terminal round) | evaluable | nested share |
|---|---|---|
| `Orthoflavivirus_NS5_Scaramozzino_2001_round2` | 34,014 | 30.4% |
| `Paramyxoviridae_L_Tong_2008_round2` | 9,229 | 31.9% |
| `Enterovirus_5UTR_VP4_VP2_Wray_2016_round2` | 8,656 | 79.0% |
| `Alphavirus_nsP4_Sanchez-Seco_2001_round2` | 8,368 | 94.2% |
| `Adenoviridae_POL_Wellehan_2004_round2` | 4,978 | 98.5% |
| **`Polyomaviridae_VP1_Johne_2005_round2`** | **3,260** | **0.2%** |
| **`Chlamydia_trachomatis_16S_Messmer_1997_round2`** | **363** | **0.0%** |
| `Chlamydia_psittaci_16S_Messmer_1997_round2` | 112 | 100.0% |

The last three are the argument for the whole feature: two protocols that essentially
never complete, and a sibling on the same round 1 that always does. No row anywhere in
the project says so today.

## The seven decisions

1. **The nest is scored, and the rounds keep their own statuses.** A round can be run
   alone -- either product reads on a gel -- so its standalone score is a true claim,
   while the nest answers the different question of what the published protocol does.
2. **The nest gets its own row and its own page, counted apart from assays.** The report
   headline names both populations ("202 assays screened: ... ; 22 nested protocols:
   ...") rather than merging them. A reader scanning for failures must be able to see a
   failing protocol whose rounds both read stable.
3. **A nest is a PATH, not a family.** `CHLAMYDIA_16S_Messmer_1997` is one genus-level
   round 1 feeding three species-specific inners, which is three protocols with three
   targets. `PROBOSCIVIRUS_..._EEHV5` has `round2` and `round2B` as alternatives.
   `..._EEHV34` is a genuine three-step chain.
4. **Scope is the intersection of every round on the path.** In all 32 families the
   inner is the narrower one, so this reduces to the terminal round's scope and gives
   the Chlamydia answer -- a *C. psittaci* record is out of scope for the pneumoniae
   protocol, not a failure of it -- while still surviving the inverted case.
5. **A nest is keyed on its terminal round, and only full paths are scored.** Every
   terminal round has exactly one chain of parents behind it, so no new id vocabulary is
   needed. `r1 -> r2` inside the EEHV3/4 chain is not a protocol anyone published.
6. **The nest inherits the weakest round's gate.** Withheld whenever any round on the
   path is withheld, naming the round responsible; `active` only when every round is.
   The live case is Borna, whose round 2 carries `oligo_sequence_uncertain`.
7. **Same threshold and same status vocabulary as an assay**, and semi-nested paths are
   **scored identically but flagged**, naming the shared oligo. 13 of 32 families share
   a primer between rounds, including the two largest nests, and there the "unreachable
   coverage" framing would otherwise imply an independence that does not hold.

## Interfaces proposed, for approval

### Schema (`source`)

```yaml
source:
  nested_round:  round1 | round2 | round2B | round3 | ...   # unchanged
  nested_family: <family id>        # becomes REQUIRED when nested_round is set
  nested_parent: <assay id>         # NEW; required unless this round is the root
```

Validator rules, each its own test. **Done 2026-11-01**: the field, the four per-entry
rules and the backfill all landed, so every path is now declared rather than inferred --
**67 rounds, 32 families, 34 nests, nothing ambiguous**. One addition the work forced:
`nested_parent_not_held`, a disclosure flag letting a round leave `nested_parent` unset
when its parent is genuinely not in the registry, without that reading as "this is the
root". The generic `nested_protocol` flag could not serve, because 12 entries carry it
simply for being in a nest.

Validator rules:

- `nested_round` set implies `nested_family` set. **The id-suffix fallback is removed**;
  it has already mis-paired two families (2026-10-14).
- a non-root round declares a `nested_parent` that resolves, sits in the same family,
  and does not cycle; exactly one root per family.
- an entry named as a parent must itself declare `nested_round`. This is what fixes the
  **39 entries with no family declared** and the **2 orphaned rounds** the report
  currently cannot assemble.

### `assaywatch/nested.py`

```python
@dataclass(frozen=True)
class NestPath:
    nest_id: str  # the terminal round's assay id
    family: str
    rounds: tuple[str, ...]  # root -> terminal, in order
    shared_oligos: tuple[str, ...]  # sequences used by more than one round on the path


def paths(assays: Iterable[Assay]) -> list[NestPath]:
    """Every full path. A terminal round is one no other round names as parent."""


def nest_scope(path: NestPath, assays: Mapping[str, Assay]) -> frozenset[int] | None:
    """Intersection of the rounds' scope_taxids; None when no round restricts."""


def nest_calls(path: NestPath, calls: Mapping[str, Mapping[str, Call]]) -> Iterator[Call]:
    """One synthetic call per record every round can be judged on: detected when
    every round detects, failed otherwise. Records unjudgeable by any round are
    not emitted, which is the existing rule about GenBank's faults versus the
    assay's."""
```

`nest_calls` returns the SAME `Call` shape the screen emits, so the existing drift
assessment scores a nest with no new statistics: thresholds, Wilson and Newcombe
intervals, the recent window, the widening, the undecided statuses and
`min_records_for_drift` all apply unchanged. That is the whole design -- one new way to
produce calls, not a second scoring engine.

### Report and site

- `report.py` gains a `Nested protocols` status table beside the assay tables, and the
  headline sentence names both populations.
- the website list gains nest rows, marked as protocols, sortable with the rest.
- **nest pages cannot live at `assays/<terminal_id>`, which the round already occupies.**
  They go under `website/nests/<terminal_id>.md`, titled `<terminal round name>
  (nested protocol)`, linking to each round and linked from each.
- a nest page states: the path, the nested share with its interval, each round's
  standalone share, the unreachable gap, the shared oligo where semi-nested, and the
  withholding reason where inherited.

## Test plan

Fixtures covering each shape, since the shapes are what the current code gets wrong: a
two-round chain, the three-step EEHV3/4 chain, the Chlamydia branch of three inners,
the EEHV5 alternatives, a semi-nested pair, and a path with a withheld round. Each
decision above gets a test that fails if it is reversed, including the two that are
easy to regress: a partial path is not scored, and a *C. psittaci* record is out of
scope for the pneumoniae nest rather than a failure of it.

## Open, deliberately

- **Whether a nest can carry its own `needs_review` flags**, or only inherit them.
- **How `report_diff` should treat nests** appearing and disappearing as parents are
  declared, since the first run after this lands will show ~22 new rows.
- **Nothing about retrieval changes**: a nest adds no query and fetches nothing.
- Citation is settled by inheritance, not by a rule: **0 of 32 families have rounds
  citing different papers** (checked 2026-11-01), so a nest cites what its rounds cite.
  If that ever stops being true the nest needs its own answer.
