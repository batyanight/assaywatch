# 2026-11-06 — The 31 papers behind negative verdicts reread: two statuses withheld, one withheld for chemistry, and two primer pairs were cut short

**Finding: on the 2026-11-01 calls three statuses move, all to withheld, and nothing else does. Two entries
stored primers shorter than their papers print, with no disclosure.** 65 entries got a `citation.claim`, 63 of them
applied; the two Keele rows wait on a source.

Method as `docs/journal/2026-11-04-scope-reread.md`. Subagents read, every quote was checked by script against the
paper, and a separate subagent verified each reported discrepancy against the paper before anything was applied. That
step earned its cost: 2 of 20 were overstated and 1 was wrong (Bourhy round 2, whose protocol prints its rounds).

| entry | status | why |
|---|---|---|
| `West_Nile_virus_E_Lanciotti_2001` | `declining` to withheld | the pair is NASBA, isothermal at 41 C; the 45 cycles belonged to the paper's other assay |
| `Simian_immunodeficiency_virus_pol_Keele_2009_PTS_spol_F1` | `stable` to withheld, draft | the paper prints no primers, and no held paper or supplement does |
| `Simian_immunodeficiency_virus_pol_Keele_2009_PTS_spol_F2` | `declining` to withheld, draft | the same |

- **Primers cut short.** `Escherichia_coli_malB_Candrian_1991` lost 6 and 4 bases at the 5' ends, and Mueller-4R one.
  The restored bases match all 326 and 365 measured products, so no call moves on that evidence.
- **Broadened.** Kakugo virus for DWV-A, Varroa destructor virus 1 for DWV-B, *Mycoplasmopsis* for Rebelo, Ranid
  herpesvirus 5 for the Batravirus pan pair, whose genome carries both primer sites for the expected 200 bp. Each sits
  outside its entry's old retrieval taxon, so retrieval moves. They change nothing until the frozen run.
- **Sizes.** Forslund 484, Landolfi round 2 161, Mankertz 580 and 274, Keele 827 and 547, Candrian 595, each by
  measurement. The verifier's further table of stored against modal sizes isn't applied: `local/`-held, listed on the roadmap.
- **Not applied.** Narrower claims were not tested yet. The stored `MGB-NFQ` on Spackman doesn't come from Spackman; its
  primers are Lindsay 2013's modified form, already disclosed.

The taxonomy cache was rebuilt to carry the new scope taxa (159,307 parent links), and moved no status by itself.
