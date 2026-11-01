# drift + report

Groups calls by deposit year, compares recent detection against all earlier
records, and assigns a status.

An assay is flagged only where the **upper** bound of its recent confidence
interval falls below the threshold: the data must be inconsistent with
continued function, not merely compatible with failure. Where records are
scarce the window extends to a maximum of five years, and each assay reports
the window applied.

**Output:** `report.md` for reading on GitHub, and a self-contained
`report.html` with no external dependencies, which opens from a local file path
without specialist software.
