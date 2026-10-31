# CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004

<span class="aw-chip aw-chip-stable">stable</span>

**Batrachochytrium dendrobatidis — ITS1/5.8S real-time PCR (Boyle 2004)**

| | |
|---|---|
| Target | Batrachochytrium dendrobatidis ([taxid 109871](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=109871)) |
| Gene | ITS1-5.8S rDNA |
| Chemistry | mgb |
| Amplicon | 146 bp |
| Designed | 2004 |
| Paper | [10.3354/dao060141](https://doi.org/10.3354/dao060141) |
| Registry status | active |

!!! quote "The paper"
    Boyle DG et al. 2004. Dis Aquat Org 60:141-148

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CCTTGATATAATACAGTGTGCCATATGTC` | 29 nt |
| reverse | `AGCCAAGAGATCCGTTGTCAAA` | 22 nt |
| probe | `CGAGTCGAACAAAAT` | 15 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 17 | 17 | 100.0% | 81.6% – 100.0% |
| baseline (everything earlier) | 157 | 162 | 96.9% | 93.0% – 98.7% |

Change from baseline, Newcombe interval: **-15.4% to 7.0%**. Threshold: **90.0%**.

*detected share 100.0% (82%-100%) since Oct 2024*

Trend across deposit years: by record rising (p=0.253, 12 years); by footprint rising (p=0.645). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="c29d71aa-d564-4815-8abc-73e7c80d304a" data-root-id="p8547" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"a2bc8b0c-8f7f-43a5-81d7-aa8506bb9679":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p8602","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p8603"}}},"roots":[{"type":"object","name":"Figure","id":"p8547","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p8549"},"y_range":{"type":"object","name":"Range1d","id":"p8556","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p8557"},"y_scale":{"type":"object","name":"LinearScale","id":"p8558"},"title":{"type":"object","name":"Title","id":"p8554","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p8592","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p8544","attributes":{"selected":{"type":"object","name":"Selection","id":"p8545","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p8546"},"data":{"type":"map","entries":[["year",[2004,2005,2006,2011,2012,2014,2016,2018,2020,2023,2024,2025]],["share",[100.0,100.0,83.33333333333334,100.0,100.0,83.33333333333334,93.75,100.0,80.0,100.0,100.0,100.0]],["detected",[1,1,5,10,56,10,15,8,4,10,37,17]],["evaluable",[1,1,6,10,56,12,16,8,5,10,37,17]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.791719296345839,10.143865699252444,11.300413928944284,10.269703144398052,10.467343773689333,9.989711205477885,9.667366891029102,10.143865699252444,11.030852377887435,10.508782366508077]]]}}},"view":{"type":"object","name":"CDSView","id":"p8593","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8594"}}},"glyph":{"type":"object","name":"Line","id":"p8589","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p8590","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p8591","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p8598","attributes":{"data_source":{"id":"p8544"},"view":{"type":"object","name":"CDSView","id":"p8599","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8600"}}},"glyph":{"type":"object","name":"Scatter","id":"p8595","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p8596","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p8597","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p8555","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p8569"},{"type":"object","name":"BoxZoomTool","id":"p8570","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p8571","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p8577","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8576","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p8578","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p8579"},{"type":"object","name":"SaveTool","id":"p8580"},{"type":"object","name":"HoverTool","id":"p8601","attributes":{"renderers":[{"id":"p8598"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p8564","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8565","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8566"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8567"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p8559","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8560","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8561"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8562"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p8563","attributes":{"axis":{"id":"p8559"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p8568","attributes":{"dimension":1,"axis":{"id":"p8564"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p8581","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p8583","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p8584","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p8585","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p8587","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8586","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p8588","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"a2bc8b0c-8f7f-43a5-81d7-aa8506bb9679","roots":{"p8547":"c29d71aa-d564-4815-8abc-73e7c80d304a"},"root_ids":["p8547"]}];
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

<div id="af9522d5-c5d1-4a84-8075-1e23f43209ed" data-root-id="p8607" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"e5a3225a-795d-43c3-a584-dfbda1cb257c":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p8647","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p8648"}}},"roots":[{"type":"object","name":"Figure","id":"p8607","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p8608"},"y_range":{"type":"object","name":"DataRange1d","id":"p8609","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p8616"},"y_scale":{"type":"object","name":"LinearScale","id":"p8617"},"title":{"type":"object","name":"Title","id":"p8614","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p8643","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p8604","attributes":{"selected":{"type":"object","name":"Selection","id":"p8605","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p8606"},"data":{"type":"map","entries":[["year",[2004,2005,2006,2011,2012,2014,2016,2018,2020,2023,2024,2025]],["evaluable",[1,1,6,10,56,12,16,8,5,10,37,17]],["detected",[1,1,5,10,56,10,15,8,4,10,37,17]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p8644","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8645"}}},"glyph":{"type":"object","name":"VBar","id":"p8640","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p8641","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p8642","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p8615","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p8628"},{"type":"object","name":"BoxZoomTool","id":"p8629","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p8630","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p8636","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8635","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p8637","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p8638"},{"type":"object","name":"SaveTool","id":"p8639"},{"type":"object","name":"HoverTool","id":"p8646","attributes":{"renderers":[{"id":"p8643"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p8623","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8624","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8625"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8626"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p8618","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8619","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8620"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8621"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p8622","attributes":{"axis":{"id":"p8618"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p8627","attributes":{"dimension":1,"axis":{"id":"p8623"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"e5a3225a-795d-43c3-a584-dfbda1cb257c","roots":{"p8607":"af9522d5-c5d1-4a84-8075-1e23f43209ed"},"root_ids":["p8607"]}];
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

Disclosures on this entry: `amplicon_measured_not_published`.


## What reached the statistics

9,491 records were screened for this assay and **179 (2%)** were evaluable, meaning both primers landed in the right orientation and size range. 9,312 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 8,855 |
| `truncated` | 392 |
| `chance_anchor` | 65 |

