# Pipeline

Nine stages turn a directory of assay descriptions into a report. Every stage
has its own page; select one in the diagram or from the list below.

<figure class="aw-pipeline">
<svg viewBox="0 0 726 1210" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Pipeline, top to bottom: registry, validate, retrieve, screen, collect, then one calls table that four analyses each read. Degeneracy is computed from the registry alone.">
<defs><marker id="aw-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/></marker></defs>
<a class="aw-node" href="registry/" aria-label="registry"><rect x="70" y="18" width="250" height="70" rx="7"/><text x="195.0" y="48">registry</text><text x="195.0" y="70" class="sub">218 assay files</text></a>
<g class="aw-edge"><line x1="195.0" y1="88" x2="195.0" y2="118" marker-end="url(#aw-arrow)"/>
</g>
<a class="aw-node" href="validate/" aria-label="validate"><rect x="70" y="122" width="250" height="70" rx="7"/><text x="195.0" y="152">validate</text><text x="195.0" y="174" class="sub">schema and citation</text></a>
<g class="aw-edge"><line x1="195.0" y1="192" x2="195.0" y2="222" marker-end="url(#aw-arrow)"/>
<text x="207.0" y="212" text-anchor="start">targets to fetch</text>
</g>
<a class="aw-node" href="retrieve/" aria-label="retrieve"><rect x="70" y="226" width="250" height="70" rx="7"/><text x="195.0" y="256">retrieve</text><text x="195.0" y="278" class="sub">115 archives</text></a>
<g class="aw-edge"><line x1="195.0" y1="296" x2="195.0" y2="326" marker-end="url(#aw-arrow)"/>
<text x="207.0" y="316" text-anchor="start">FASTA on disk</text>
</g>
<a class="aw-node" href="screen/" aria-label="screen"><rect x="70" y="330" width="250" height="70" rx="7"/><text x="195.0" y="360">screen</text><text x="195.0" y="382" class="sub">oligos × records</text></a>
<g class="aw-edge"><line x1="195.0" y1="400" x2="195.0" y2="430" marker-end="url(#aw-arrow)"/>
<text x="207.0" y="420" text-anchor="start">one screen per archive</text>
</g>
<a class="aw-node" href="collect/" aria-label="collect"><rect x="70" y="434" width="250" height="70" rx="7"/><text x="195.0" y="464">collect</text><text x="195.0" y="486" class="sub">into one table</text></a>
<g class="aw-edge"><line x1="195.0" y1="504" x2="195.0" y2="534" marker-end="url(#aw-arrow)"/>
</g>
<a class="aw-node aw-store" href="calls/" aria-label="the calls table"><rect x="30.0" y="538" width="330" height="76" rx="7"/><text x="195.0" y="569">the calls table</text><text x="195.0" y="592" class="sub">3.0M rows</text></a>
<g class="aw-edge"><path d="M 195.0 614 L 195.0 977.0" fill="none"/></g>
<text class="aw-bus-label" x="185.0" y="640" text-anchor="end">each reads it</text>
<g class="aw-edge"><line x1="195.0" y1="689.0" x2="246" y2="689.0" marker-end="url(#aw-arrow)"/></g>
<a class="aw-node" href="report/" aria-label="drift + report"><rect x="250" y="654" width="300" height="70" rx="7"/><text x="400.0" y="684">drift + report</text><text x="400.0" y="706" class="sub">the verdicts</text></a>
<g class="aw-edge"><line x1="195.0" y1="785.0" x2="246" y2="785.0" marker-end="url(#aw-arrow)"/></g>
<a class="aw-node" href="lineage/" aria-label="lineage"><rect x="250" y="750" width="300" height="70" rx="7"/><text x="400.0" y="780">lineage</text><text x="400.0" y="802" class="sub">per clade</text></a>
<g class="aw-edge"><line x1="195.0" y1="881.0" x2="246" y2="881.0" marker-end="url(#aw-arrow)"/></g>
<a class="aw-node" href="sitedrift/" aria-label="site drift"><rect x="250" y="846" width="300" height="70" rx="7"/><text x="400.0" y="876">site drift</text><text x="400.0" y="898" class="sub">which base</text></a>
<g class="aw-edge"><line x1="195.0" y1="977.0" x2="246" y2="977.0" marker-end="url(#aw-arrow)"/></g>
<a class="aw-node" href="figures/" aria-label="figures"><rect x="250" y="942" width="300" height="70" rx="7"/><text x="400.0" y="972">figures</text><text x="400.0" y="994" class="sub">inline SVG</text></a>
<g class="aw-edge aw-dashed"><path d="M 562 785.0 L 596 785.0 L 596 689.0 L 562 689.0" fill="none" marker-end="url(#aw-arrow)"/><text x="602" y="741.0" text-anchor="start">worst clade</text><text x="602" y="757.0" text-anchor="start">can override</text></g>
<g class="aw-edge aw-dashed"><path d="M 70 53 L 14 53 L 14 1101.0 L 66 1101.0" fill="none" marker-end="url(#aw-arrow)"/></g>
<a class="aw-node" href="degeneracy/" aria-label="degeneracy"><rect x="70" y="1066" width="250" height="70" rx="7"/><text x="195.0" y="1096">degeneracy</text><text x="195.0" y="1118" class="sub">from the oligos alone</text></a>
<a class="aw-node aw-config" href="config/" aria-label="config.yaml"><rect x="420" y="330" width="180" height="62" rx="7"/><text x="510" y="357">config.yaml</text><text x="510" y="378" class="sub">19 thresholds</text></a>
<g class="aw-edge aw-dashed"><line x1="416" y1="361" x2="324" y2="361" marker-end="url(#aw-arrow)"/><path d="M 510 392 L 510 640 L 400.0 640 L 400.0 650" fill="none" marker-end="url(#aw-arrow)"/></g>
</svg>
<figcaption>
Sequence flows down the spine and is never re-fetched in order to re-score:
archives are kept whole, so changing a threshold re-reads local storage. The
four analyses each read the one calls table, which is why they cannot disagree
about the data. Dashed edges are influence rather than data — the thresholds
that decide verdicts, the single reverse path by which one failing clade
overrides an otherwise reassuring pooled figure, and the degeneracy table,
computed from the oligonucleotide sequences alone.
</figcaption>
</figure>

## The stages

**[The registry](registry/)** — One YAML file per assay; 218 in total. Each records the oligonucleotide sequences, target organism, chemistry, product size and source publication.

**[validate](validate/)** — Executes before any other stage and halts the pipeline on a registry that does not parse, contains a duplicate key, or holds an entry without a confirmed citation.

**[retrieve](retrieve/)** — Retrieves nucleotide records from GenBank for each target and archives them.

**[screen](screen/)** — The computationally dominant stage, and the only one operating on sequence at scale.

**[collect](collect/)** — Consolidates the cached per-archive results into a single table for the run.

**[The calls table](calls/)** — Every subsequent stage reads this file and nothing else. This is deliberate: the four analyzes below cannot disagree about the data, because a single copy exists.

**[drift + report](report/)** — Groups calls by deposit year, compares recent detection against all earlier records, and assigns a status.

**[lineage](lineage/)** — Divides each assay's records by organism below the target and recomputes detection per clade.

**[site drift](sitedrift/)** — For flagged assays, identifies **which base** is responsible.

**[figures](figures/)** — Draws the overview plots and embeds them in the HTML report.

**[degeneracy](degeneracy/)** — Computed from the oligonucleotide sequences alone, with no sequence database involved, which is why it derives from the registry rather than the calls table.

**[config.yaml](config/)** — Nineteen thresholds determine every verdict; all but one were set by inspection. None are embedded in code.


*A complete run takes approximately 50 minutes on eight cores, excluding retrieval.*
