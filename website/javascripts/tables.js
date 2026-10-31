/* Filter and sort for the assay list. No dependency, no build step: the table is
   plain HTML in the generated page, so it reads and prints without JavaScript and
   this only adds the two affordances a 217-row table needs.

   Re-run on every MkDocs instant-navigation page load, not just DOMContentLoaded,
   because `navigation.instant` swaps the body without a reload. */
function awInitTables() {
  const box = document.querySelector('.aw-filter');
  const table = document.querySelector('table.aw-assays');
  if (!table) return;
  const rows = Array.from(table.tBodies[0].rows);

  if (box && !box.dataset.awBound) {
    box.dataset.awBound = '1';
    box.addEventListener('input', () => {
      const q = box.value.trim().toLowerCase();
      let shown = 0;
      for (const r of rows) {
        const hit = !q || r.textContent.toLowerCase().includes(q);
        r.hidden = !hit;
        if (hit) shown++;
      }
      box.setAttribute('aria-label', `filter assays, ${shown} of ${rows.length} shown`);
    });
  }

  table.querySelectorAll('th').forEach((th, i) => {
    if (th.dataset.awBound) return;
    th.dataset.awBound = '1';
    th.setAttribute('role', 'button');
    th.setAttribute('tabindex', '0');
    const sort = () => {
      const asc = th.dataset.dir !== 'asc';
      table.querySelectorAll('th').forEach(o => { if (o !== th) delete o.dataset.dir; });
      th.dataset.dir = asc ? 'asc' : 'desc';
      const key = (r) => {
        const c = r.cells[i];
        /* data-sort carries the numeric value where the cell shows a formatted
           one, so "59.2%" and "1,234" sort as numbers rather than as text. */
        const d = c.getAttribute('data-sort');
        return d !== null ? parseFloat(d) : c.textContent.trim().toLowerCase();
      };
      rows.sort((a, b) => {
        const x = key(a), y = key(b);
        if (x === y) return 0;
        return (x < y ? -1 : 1) * (asc ? 1 : -1);
      });
      const body = table.tBodies[0];
      rows.forEach(r => body.appendChild(r));
    };
    th.addEventListener('click', sort);
    th.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); sort(); } });
  });
}
document.addEventListener('DOMContentLoaded', awInitTables);
if (window.document$ && window.document$.subscribe) window.document$.subscribe(awInitTables);

/* The pipeline diagram: click a stage, open that stage.

   Progressive enhancement. Every stage section is in the page as ordinary
   markdown, so with JavaScript off (or if this file fails to load) the page is
   a complete written outline of the pipeline and the diagram above it is a
   static figure. Only once this runs do the sections collapse to one at a time. */
function awInitPipeline() {
  const svg = document.querySelector('.aw-pipeline svg');
  const sections = Array.from(document.querySelectorAll('.aw-stage'));
  if (!svg || !sections.length) return;

  const show = (id, focus) => {
    let found = false;
    for (const s of sections) {
      const on = s.id === 'stage-' + id;
      s.hidden = !on;
      if (on) found = true;
    }
    if (!found) return;
    svg.querySelectorAll('.aw-node').forEach(n =>
      n.classList.toggle('is-open', n.dataset.stage === id));
    if (history.replaceState) history.replaceState(null, '', '#stage-' + id);
    if (focus) {
      const el = document.getElementById('stage-' + id);
      el.setAttribute('tabindex', '-1');
      el.focus({preventScroll: true});
    }
  };

  svg.querySelectorAll('.aw-node').forEach(node => {
    if (node.dataset.awBound) return;
    node.dataset.awBound = '1';
    const open = () => show(node.dataset.stage, true);
    node.addEventListener('click', open);
    node.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); }
    });
  });

  /* Deep links work: /pipeline/#stage-screen opens that stage rather than
     scrolling to a hidden element. */
  const wanted = (location.hash || '').replace('#stage-', '');
  show(sections.some(s => s.id === 'stage-' + wanted) ? wanted : 'registry', false);
}
document.addEventListener('DOMContentLoaded', awInitPipeline);
if (window.document$ && window.document$.subscribe) window.document$.subscribe(awInitPipeline);

/* Links that leave the site open in a new tab.

   Applied to every off-site link rather than just the DOI, so the rule is one a
   reader can learn: anything that leaves assaywatch opens beside it, anything
   within it navigates in place. A page of assay dashboards is something you
   read across, and losing your position in a 217-row table to follow a citation
   is the wrong trade.

   `rel="noopener noreferrer"` goes with every one: without `noopener` the opened
   page gets a handle on this one through `window.opener`, which is a tab-jacking
   route, and it also keeps the new tab off this one's process.

   Progressive enhancement: with JavaScript off the links still work, they just
   navigate in place. */
function awExternalLinks() {
  const here = location.hostname;
  document.querySelectorAll('.md-content a[href]').forEach(a => {
    if (a.dataset.awExt) return;
    let host;
    try { host = new URL(a.href, location.href).hostname; } catch { return; }
    if (!host || host === here) return;
    a.dataset.awExt = '1';
    a.target = '_blank';
    a.rel = (a.rel ? a.rel + ' ' : '') + 'noopener noreferrer';
    if (!a.title) a.title = 'opens in a new tab';
  });
}
document.addEventListener('DOMContentLoaded', awExternalLinks);
if (window.document$ && window.document$.subscribe) window.document$.subscribe(awExternalLinks);
