# drift + report

Groups calls by deposit year, compares recent detection with all earlier
records, and assigns a status.

An assay is flagged only when the **upper** bound of its recent confidence
interval falls below the threshold. The data must be inconsistent with the assay
still working, not just compatible with failure. Where records are scarce the
window widens to a maximum of five years, and each assay reports the window it
used.

**Output:** `report.md` for reading on GitHub, and a self-contained
`report.html` with no external dependencies, which opens from a local file path
without any special software.
