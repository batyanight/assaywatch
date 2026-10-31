# CALICIVIRUS_ssRNA_RdRp_Neill_Seal_1995

<span class="aw-chip aw-chip-no-recent-data">no recent data</span>

**CALICIVIRUS (ssRNA) — RNA-dependent RNA polymerase (Neill & Seal 1995)**

| | |
|---|---|
| Target | Caliciviridae ([taxid 11974](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11974)) |
| Gene | RNA-dependent RNA polymerase |
| Chemistry | conventional |
| Amplicon | 520 bp |
| Designed | 1995 |
| Paper | [10.1016/S0890-8508(95)90962-1](https://doi.org/10.1016/S0890-8508(95)90962-1) |
| Registry status | draft |

!!! quote "The paper"
    Neill JD, Seal BS 1995. Development of PCR primers for specific amplification of two distinct regions of the genomes of San Miguel sea-lion and vesicular exanthema of swine viruses. Mol Cell Probes 9:33-37

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GCCTTCTGGTATGCCACTAACATCC` | 25 nt |
| reverse | `GACGAGCGGTATGATCTTGTTGGTG` | 25 nt |

## The verdict, and the numbers behind it

**no recent data** — nothing was deposited in the window

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 0 | 0 | — | 0.0% – 100.0% |
| baseline (everything earlier) | 10 | 25 | 40.0% | 23.4% – 59.3% |

Change from baseline, Newcombe interval: **-100.0% to 100.0%**. Threshold: **90.0%**.

*no evaluable records deposited since Oct 2021 (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=0.000416, 9 years); by footprint falling (p=0.0112). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="c2987ae0-0d6a-47bd-80b0-35e63ff61755" data-root-id="p6128" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"dd60e95a-78f8-42e0-8850-762ca20635fc":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p6176","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p6177"}}},"roots":[{"type":"object","name":"Figure","id":"p6128","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p6130"},"y_range":{"type":"object","name":"Range1d","id":"p6137","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p6138"},"y_scale":{"type":"object","name":"LinearScale","id":"p6139"},"title":{"type":"object","name":"Title","id":"p6135","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p6166","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p6125","attributes":{"selected":{"type":"object","name":"Selection","id":"p6126","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p6127"},"data":{"type":"map","entries":[["year",[1994,1995,1997,1998,2000,2003,2007,2012,2014]],["share",[100.0,100.0,0.0,0.0,0.0,0.0,11.11111111111111,0.0,0.0]],["detected",[2,7,0,0,0,0,1,0,0]],["evaluable",[2,7,2,1,1,1,9,1,1]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline"]],["size",[9.07684386569143,9.897626379762722,9.07684386569143,8.703135093227193,8.703135093227193,8.703135093227193,10.071067811865476,8.703135093227193,8.703135093227193]]]}}},"view":{"type":"object","name":"CDSView","id":"p6167","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p6168"}}},"glyph":{"type":"object","name":"Line","id":"p6163","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p6164","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p6165","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p6172","attributes":{"data_source":{"id":"p6125"},"view":{"type":"object","name":"CDSView","id":"p6173","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p6174"}}},"glyph":{"type":"object","name":"Scatter","id":"p6169","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p6170","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p6171","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p6136","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p6150"},{"type":"object","name":"BoxZoomTool","id":"p6151","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p6152","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p6158","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p6157","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p6159","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p6160"},{"type":"object","name":"SaveTool","id":"p6161"},{"type":"object","name":"HoverTool","id":"p6175","attributes":{"renderers":[{"id":"p6172"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p6145","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p6146","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p6147"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p6148"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p6140","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p6141","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p6142"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p6143"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p6144","attributes":{"axis":{"id":"p6140"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p6149","attributes":{"dimension":1,"axis":{"id":"p6145"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"Span","id":"p6162","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"dd60e95a-78f8-42e0-8850-762ca20635fc","roots":{"p6128":"c2987ae0-0d6a-47bd-80b0-35e63ff61755"},"root_ids":["p6128"]}];
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

<div id="e5461621-5d59-4abf-af9b-bda491e0d9e5" data-root-id="p6181" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"7e573e6b-a9b2-47cc-a045-a2c924500753":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p6221","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p6222"}}},"roots":[{"type":"object","name":"Figure","id":"p6181","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p6182"},"y_range":{"type":"object","name":"DataRange1d","id":"p6183","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p6190"},"y_scale":{"type":"object","name":"LinearScale","id":"p6191"},"title":{"type":"object","name":"Title","id":"p6188","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p6217","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p6178","attributes":{"selected":{"type":"object","name":"Selection","id":"p6179","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p6180"},"data":{"type":"map","entries":[["year",[1994,1995,1997,1998,2000,2003,2007,2012,2014]],["evaluable",[2,7,2,1,1,1,9,1,1]],["detected",[2,7,0,0,0,0,1,0,0]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p6218","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p6219"}}},"glyph":{"type":"object","name":"VBar","id":"p6214","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p6215","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p6216","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p6189","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p6202"},{"type":"object","name":"BoxZoomTool","id":"p6203","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p6204","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p6210","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p6209","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p6211","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p6212"},{"type":"object","name":"SaveTool","id":"p6213"},{"type":"object","name":"HoverTool","id":"p6220","attributes":{"renderers":[{"id":"p6217"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p6197","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p6198","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p6199"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p6200"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p6192","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p6193","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p6194"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p6195"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p6196","attributes":{"axis":{"id":"p6192"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p6201","attributes":{"dimension":1,"axis":{"id":"p6197"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"7e573e6b-a9b2-47cc-a045-a2c924500753","roots":{"p6181":"e5461621-5d59-4abf-af9b-bda491e0d9e5"},"root_ids":["p6181"]}];
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

This entry declares **`scope_taxids`**: [3433198](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3433198). A record counts toward the denominator when its taxid, or any ancestor, is in that set. Records outside it are screened and reported but kept out of the statistics.

84,751 screened records fell outside the declared scope.

Disclosures on this entry: `thin_evidence`.


## What reached the statistics

115 records were screened for this assay and **25 (22%)** were evaluable, meaning both primers landed in the right orientation and size range. 90 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 71 |
| `truncated` | 19 |

