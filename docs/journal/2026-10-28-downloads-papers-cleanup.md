# ~/Downloads/papers folded into papers/ (2026-10-28)

Housekeeping, not a measurement. Everything in `~/Downloads` and `~/Downloads/papers` was
compared against `papers/` and either filed under its `doi_stem` name or deleted as a
duplicate. Nothing here changes a registry entry.

## Added to `papers/`

| file | what it is |
|---|---|
| `10.1128_jcm.00693-06.pdf` | Fux et al. 2006, Nipah N-protein serodiagnosis (serology; likely no primers) |
| `10.1016_s0166-0934_02_00148-9.pdf` | Barbezange & Jestin 2002, pigeon paramyxovirus-1 RT-nested PCR, J Virol Methods 106. DOI derived from the PII printed in the file |
| `10.1016_j.jcv.2026.105989.pdf` | J Clin Virol 186 (2026) 105989 |
| `10.1128_mbio.00598-13.supp.pdf` | Anthony 2013 mBio supplement, **three one-page files merged in order** (`mbo004131613sf01` figure, `sf02` figure, `st1` table) with `pdfunite`, because the `.supp` convention allows one file per extension. The paper's existing supplement is `10.1128_mbio.00598-13.supp.docx` (the Supplemental Discussion); this PDF holds the figures and table, which the docx does not |

The 16 PDFs from the Desktop fetch list and the Besnoitia paper (`10.1016_j.vetpar.2009.06.020.pdf`,
no primers) were added earlier the same day.

## Deleted as duplicates of files already held

About 35 files, each checked against its `papers/` match before deletion: byte-identical,
or the same paper by DOI / printed citation with a page-1 text comparison. Four were
different copies of a held paper (two accepted manuscripts, two original journal PDFs
where `papers/` holds browser print-to-PDFs of `landolfi2010` and `meyer1997`); `papers/`
was kept in all four.

Supplements deleted after content checks: `pone.0207365.s001.docx` x2 (alphanumeric text
identical to `10.1371_journal.pone.0207365.supp.txt`), `viruses-13-01358-s001.zip` (its one
PDF is byte-identical to `10.3390_v13071358.supp.pdf`), and the S0014489485711071 scan
(Li et al. 1995, Exp Parasitol 81:182, which is `10.1006_expr.1995.1107.pdf`).

## Still outside `papers/`

Nothing: `~/Downloads/papers` is empty. `uwp5101320.png` (not a paper) was there when the
cleanup finished and was gone minutes later; it was not deleted by the cleanup. The
Li 1995 scan (`10.1006_expr.1995.1107.pdf`) has no text layer, so tools that read text get
nothing from it; OCR reads the title page.

## Index

`docs/papers-index.md` was not regenerated in the session that did this: Crossref is
unreachable from the sandbox and the script caches a failed lookup as a permanent null.
Run `python scripts/papers_index.py --out docs/papers-index.md` locally; the merged
mBio supplement will then show as `pdf suppl` beside the `docx suppl` already there.
