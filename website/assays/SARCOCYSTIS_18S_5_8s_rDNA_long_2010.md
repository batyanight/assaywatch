# SARCOCYSTIS_18S_5_8s_rDNA_long_2010

<span class="aw-chip aw-chip-watch">watch</span>

**SARCOCYSTIS — 18S-5.8s rDNA (long)**

| | |
|---|---|
| Target | Sarcocystis ([taxid 5812](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=5812)) |
| Gene | 18S-5.8s rDNA (long) |
| Chemistry | conventional |
| Amplicon | — |
| Designed | 2010 |
| Paper | [10.1007/s00436-010-1945-4](https://doi.org/10.1007/s00436-010-1945-4) |
| Registry status | active |

!!! quote "The paper"
    Kutkienė L et al. 2010. Parasitol Res 107:879-888

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ATTGAGTGTTCCGGTGAATTA` | 21 nt |
| reverse | `GCCATTTGCGTTCAGAAATC` | 20 nt |

## The verdict, and the numbers behind it

**watch** — below the threshold with an interval that still covers it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (48 months, from Oct 2022) | 12 | 15 | 80.0% | 54.8% – 93.0% |
| baseline (everything earlier) | 152 | 154 | 98.7% | 95.4% – 99.6% |

Change from baseline, Newcombe interval: **-43.9% to -5.3%**. Threshold: **90.0%**.

*detected share 80.0% is below the 90% threshold, but its interval (55%-93%) still reaches it (window widened to 48 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=0.00152, 11 years); by footprint falling (p=0.0598). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="ec8c3277-029f-4937-8dbd-5f7f62b1e7d9" data-root-id="p31627" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"61887319-7f50-4a4b-9b31-5a0ec78e7098":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p31682","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p31683"}}},"roots":[{"type":"object","name":"Figure","id":"p31627","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p31629"},"y_range":{"type":"object","name":"Range1d","id":"p31636","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p31637"},"y_scale":{"type":"object","name":"LinearScale","id":"p31638"},"title":{"type":"object","name":"Title","id":"p31634","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p31672","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p31624","attributes":{"selected":{"type":"object","name":"Selection","id":"p31625","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p31626"},"data":{"type":"map","entries":[["year",[2014,2015,2016,2017,2018,2019,2020,2021,2023,2024,2025]],["share",[100.0,100.0,100.0,85.71428571428571,100.0,95.23809523809523,100.0,100.0,0.0,75.0,100.0]],["detected",[34,35,15,6,31,20,5,6,0,6,6]],["evaluable",[34,35,15,7,31,21,5,6,1,8,6]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[10.975067467348278,10.994220569835573,10.423139468338052,9.897626379762722,10.913832791890265,10.652487636092928,9.667366891029102,9.791719296345839,8.703135093227193,9.989711205477885,9.791719296345839]]]}}},"view":{"type":"object","name":"CDSView","id":"p31673","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31674"}}},"glyph":{"type":"object","name":"Line","id":"p31669","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b26a00","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p31670","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b26a00","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p31671","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b26a00","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p31678","attributes":{"data_source":{"id":"p31624"},"view":{"type":"object","name":"CDSView","id":"p31679","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31680"}}},"glyph":{"type":"object","name":"Scatter","id":"p31675","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b26a00"},"hatch_color":{"type":"value","value":"#b26a00"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p31676","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b26a00"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b26a00"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p31677","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b26a00"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b26a00"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p31635","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p31649"},{"type":"object","name":"BoxZoomTool","id":"p31650","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p31651","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p31657","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31656","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p31658","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p31659"},{"type":"object","name":"SaveTool","id":"p31660"},{"type":"object","name":"HoverTool","id":"p31681","attributes":{"renderers":[{"id":"p31678"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p31644","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31645","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31646"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31647"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p31639","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31640","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31641"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31642"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p31643","attributes":{"axis":{"id":"p31639"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p31648","attributes":{"dimension":1,"axis":{"id":"p31644"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p31661","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2022.5,"right":{"type":"object","name":"Node","id":"p31663","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p31664","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p31665","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p31667","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31666","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p31668","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"61887319-7f50-4a4b-9b31-5a0ec78e7098","roots":{"p31627":"ec8c3277-029f-4937-8dbd-5f7f62b1e7d9"},"root_ids":["p31627"]}];
        root.Bokeh.embed.embed_items(docs_json, render_items);
        }
        if (root.Bokeh !== undefined) {
          embed_document(root);
        } else {
          let attempts = 0;
          const timer = setInterval(function(root) {
            if (root.Bokeh !== undefined) {
              clearInterval(timer);
              embed_document(root);
            } else {
              attempts++;
              if (attempts > 100) {
                clearInterval(timer);
                console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
              }
            }
          }, 10, root)
        }
      })(window);
    });
  };
  if (document.readyState != "loading") fn();
  else document.addEventListener("DOMContentLoaded", fn);
})();
</script>

<div id="da05ef52-ae6e-45d9-8f3d-545c72c12d6f" data-root-id="p31687" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"21ab1c49-bf8e-454f-8d49-6e8aec35a47a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p31727","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p31728"}}},"roots":[{"type":"object","name":"Figure","id":"p31687","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p31688"},"y_range":{"type":"object","name":"DataRange1d","id":"p31689","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p31696"},"y_scale":{"type":"object","name":"LinearScale","id":"p31697"},"title":{"type":"object","name":"Title","id":"p31694","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p31723","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p31684","attributes":{"selected":{"type":"object","name":"Selection","id":"p31685","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p31686"},"data":{"type":"map","entries":[["year",[2014,2015,2016,2017,2018,2019,2020,2021,2023,2024,2025]],["evaluable",[34,35,15,7,31,21,5,6,1,8,6]],["detected",[34,35,15,6,31,20,5,6,0,6,6]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b26a00","#b26a00","#b26a00"]]]}}},"view":{"type":"object","name":"CDSView","id":"p31724","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31725"}}},"glyph":{"type":"object","name":"VBar","id":"p31720","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p31721","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p31722","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p31695","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p31708"},{"type":"object","name":"BoxZoomTool","id":"p31709","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p31710","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p31716","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31715","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p31717","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p31718"},{"type":"object","name":"SaveTool","id":"p31719"},{"type":"object","name":"HoverTool","id":"p31726","attributes":{"renderers":[{"id":"p31723"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p31703","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31704","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31705"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31706"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p31698","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31699","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31700"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31701"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p31702","attributes":{"axis":{"id":"p31698"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p31707","attributes":{"dimension":1,"axis":{"id":"p31703"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"21ab1c49-bf8e-454f-8d49-6e8aec35a47a","roots":{"p31687":"da05ef52-ae6e-45d9-8f3d-545c72c12d6f"},"root_ids":["p31687"]}];
        root.Bokeh.embed.embed_items(docs_json, render_items);
        }
        if (root.Bokeh !== undefined) {
          embed_document(root);
        } else {
          let attempts = 0;
          const timer = setInterval(function(root) {
            if (root.Bokeh !== undefined) {
              clearInterval(timer);
              embed_document(root);
            } else {
              attempts++;
              if (attempts > 100) {
                clearInterval(timer);
                console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
              }
            }
          }, 10, root)
        }
      })(window);
    });
  };
  if (document.readyState != "loading") fn();
  else document.addEventListener("DOMContentLoaded", fn);
})();
</script>


## Where the mismatches sit

One cell per position along each oligo, 3' end on the right. Darker means more
records mismatch there. Hover any cell for the comparison that matters: detection
among records that mismatch at that position against records that do not. A
position where those two differ sharply is one worth redesigning around.

<p class="aw-empty">No position carried a mismatch in enough records to report.</p>


## Scope — what this assay is judged against

This entry declares no `scope_taxids`, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower set than its taxid covers, that reads as low coverage rather than as drift — see [scoping](../scoping.md).


## What reached the statistics

30,875 records were screened for this assay and **169 (1%)** were evaluable, meaning both primers landed in the right orientation and size range. 30,706 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 29,169 |
| `truncated` | 1,365 |
| `chance_anchor` | 137 |
| `chance_only` | 35 |

