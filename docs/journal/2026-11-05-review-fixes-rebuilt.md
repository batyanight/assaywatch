# 2026-11-05 — the review fixes rebuilt, and a label fault the rebuild exposed

**Finding: fixing how assembly records reach the graphs exposed a naming fault, and a pure group read
as mixed.** With assembly records in the groups, `organism()` kept strain words from their titles, so
*Y. enterocolitica* was split across names and a group that is all one species read "Y. enterocolitica
30%". Names now end at the Latin binomial. No status moved against `main`, and yearly cells equal the
graph's evaluable and detected counts with 0 mismatches over 215 assays.

## The builds

This replaces the merged build of 2026-11-04 with one command over one registry. It took two builds.
The first (2 h 20 min CPU, 10.4 GB resident) showed the fault. The second, after the fix, took
2 h 23 min and 10.8 GB, and supplies the published file, `website/data/composition.json`, 549,548
bytes against the 1.5 MB cap. `rule composition` keeps `mem_mb=13000`.

## The naming rule

Dry-run over every name in the first build before rebuilding. The first form of the rule folded 629
names into 54, and the list showed false merges: "Mute swan feces associated avastrovirus 1" became
"Mute swan", and virome names were cut to their host. So a binomial now ends a name only when the next
word opens in a capital or digit, holds a digit, or is an infraspecific marker (subsp., serovar, str.,
complex and the like), and any head naming a virus, viroid, phage or `-viridae` is left out.

| assay | before | after |
|---|---|---|
| *Y. enterocolitica* yst | Y. enterocolitica 30% | Y. enterocolitica, 37 records |
| *Y. pseudotuberculosis* inv | Y. pseudotuberculosis 75% | Y. pseudotuberculosis, 65 records |
| *E. coli* malB | E. coli 41% | E. coli, 326 records |
| *E. coli* hlyA | E. coli 74% | E. coli, 98 records |
| *Salmonella* invA | S. enterica 37% | S. enterica, 451 records |
| MTB helicase | M. tuberculosis 64% | M. tuberculosis, with *M. canetti* still listed |

Records with a taxid were never affected; they roll up through the taxonomy cache.

## The "mixes species" sentence was too strong

42 of the 201 assays with named groups have a largest group whose name carries a percent. That is
not comparable with the 17 of 199 on 2026-11-04, which also required 3 or more named species. Reading
the 42, the page's "mixes species" was false for some. *Human bocavirus* and *Bocaparvovirus primate1*
are the same virus under old and new names, as are *Adeno-associated virus* and *Dependoparvovirus
primate1*, and the EEHV names and their *Proboscivirus* forms. Title names and taxonomy names don't
reconcile, because many records have no taxid. Others are real, such as *Ranavirus* and *Helicobacter*.
The page now says the group holds several species names, which may be different species or one under
more than one name. Reconciling the names is on the roadmap, and these 42 were read, not classified.

## Checks on the published data

- Assembly records now have windows: Yersinia and MTB pages show groups, not all `unplaced`. Seven
  assays remain all `unplaced`, the ones with too few windows to cluster.
- Numbering no longer counts strata: Annis reads "B. dendrobatidis", where `main` said "B. dendrobatidis
  4", and Boyle's five groups run 1 to 5.
- Page order by eye and in the HTML: primer graph, line graph, bar graph, by-lineage table, oligos,
  verdict.

## Review findings

Security review: no finding at confidence 8 or above; the one candidate, unescaped text in generated
Markdown, was confidence 3 and was fixed anyway. Code review: 14 findings, all fixed in `26a93f5`,
among them assembly records dropped from windows, strata in the lineage numbering, one assay's
coverage series overwriting another's, and a non-atomic cache write. Details are in that commit.

## Not done

Everything on the roadmap for the next run stays there: Zimmermann's corrected primer, the
*Francisella* probe, Leporipoxvirus in the Li query, *Chlamydia* assemblies.
