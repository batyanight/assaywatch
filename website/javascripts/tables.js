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
  // `main`, not `.md-content`: that class belonged to the Material theme and
  // does not exist in this one, so the selector matched nothing and every
  // off-site link -- the DOIs included -- opened in the same tab.
  document.querySelectorAll('main a[href]').forEach(a => {
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

/* Light / dark toggle.

   The stylesheet already defines both themes: light on `:root`, dark under a
   `prefers-color-scheme` media query guarded by `:root:not([data-theme=light])`
   and again under `[data-theme=dark]`. So setting `data-theme` on the root
   element overrides the system setting in either direction, and removing it
   returns to following the system.

   Three states, cycled in that order: follow the system, force light, force
   dark. Without JavaScript the button is not rendered and the system setting
   applies, which is the correct fallback. */
function awTheme() {
  const btn = document.querySelector('.theme-toggle');
  if (!btn || btn.dataset.awBound) return;
  btn.dataset.awBound = '1';
  const root = document.documentElement;
  const systemDark = () => window.matchMedia('(prefers-color-scheme: dark)').matches;

  const paint = () => {
    const forced = root.dataset.theme;           // "light", "dark", or absent
    const dark = forced ? forced === 'dark' : systemDark();
    btn.querySelector('.tt-label').textContent = dark ? 'Light' : 'Dark';
    btn.setAttribute('aria-pressed', String(Boolean(forced)));
    btn.title = forced
      ? `Showing ${forced} — click for ${dark ? 'light' : 'dark'}, or again to follow your system`
      : `Following your system (${dark ? 'dark' : 'light'}) — click to switch`;
  };

  btn.addEventListener('click', () => {
    const forced = root.dataset.theme;
    let next;
    if (!forced) next = systemDark() ? 'light' : 'dark';   // first click: the other one
    else if (forced === (systemDark() ? 'light' : 'dark')) next = systemDark() ? 'dark' : 'light';
    else next = null;                                       // third click: back to the system
    if (next) { root.dataset.theme = next; try { localStorage.setItem('aw-theme', next); } catch (e) {} }
    else { delete root.dataset.theme; try { localStorage.removeItem('aw-theme'); } catch (e) {} }
    paint();
  });

  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', paint);
  paint();
}
document.addEventListener('DOMContentLoaded', awTheme);
if (window.document$ && window.document$.subscribe) window.document$.subscribe(awTheme);
