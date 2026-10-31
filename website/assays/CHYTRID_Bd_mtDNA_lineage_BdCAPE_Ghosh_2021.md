# CHYTRID_Bd_mtDNA_lineage_BdCAPE_Ghosh_2021

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**BATRACHOCHYTRIUM DENDROBATIDIS — BdCAPE lineage-specific mtDNA qPCR (Ghosh 2021)**

| | |
|---|---|
| Target | Batrachochytrium dendrobatidis ([taxid 109871](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=109871)) |
| Gene | mtDNA |
| Chemistry | mgb |
| Amplicon | 64 bp |
| Designed | 2021 |
| Paper | [10.1111/1755-0998.13299](https://doi.org/10.1111/1755-0998.13299) |
| Registry status | active |

!!! quote "The paper"
    Ghosh, P. N., Verster, R., Sewell, T. R., O'Hanlon, S. J., Brookes, L. M., Rieux, A., Garner, T. W. J., Weldon, C. & Fisher, M. C. Discriminating lineages of Batrachochytrium dendrobatidis using quantitative PCR. Molecular Ecology Resources 21, 1452-1459 (2021).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CACCAACACCCCACCACTTTAG` | 22 nt |
| reverse | `AAAGTCAATCGGTGATATCGTAGCT` | 25 nt |
| probe | `CCAGGCCTTAATTCA` | 15 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 0 | 3 | 0.0% | 0.0% – 56.1% |
| baseline (everything earlier) | 0 | 6 | 0.0% | 0.0% – 39.0% |

Change from baseline, Newcombe interval: **-39.0% to 56.1%**. Threshold: **90.0%**.

*3 evaluable records since Oct 2024, below the minimum of 15; the detected share is 0% (0%-56%), too wide to act on*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="bf1e5d01-5d5a-453d-a7bb-06332d33c2b1" data-root-id="p8652" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"12003875-6a4f-4c18-a69d-2c45dc0918f8":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p8707","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p8708"}}},"roots":[{"type":"object","name":"Figure","id":"p8652","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p8654"},"y_range":{"type":"object","name":"Range1d","id":"p8661","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p8662"},"y_scale":{"type":"object","name":"LinearScale","id":"p8663"},"title":{"type":"object","name":"Title","id":"p8659","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p8697","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p8649","attributes":{"selected":{"type":"object","name":"Selection","id":"p8650","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p8651"},"data":{"type":"map","entries":[["year",[2006,2023,2024,2025]],["share",[0.0,0.0,0.0,0.0]],["detected",[0,0,0,0]],["evaluable",[1,1,4,3]],["window",["baseline","baseline","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.517227179437622,9.328625426046248]]]}}},"view":{"type":"object","name":"CDSView","id":"p8698","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8699"}}},"glyph":{"type":"object","name":"Line","id":"p8694","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p8695","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p8696","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p8703","attributes":{"data_source":{"id":"p8649"},"view":{"type":"object","name":"CDSView","id":"p8704","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8705"}}},"glyph":{"type":"object","name":"Scatter","id":"p8700","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p8701","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p8702","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p8660","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p8674"},{"type":"object","name":"BoxZoomTool","id":"p8675","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p8676","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p8682","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8681","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p8683","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p8684"},{"type":"object","name":"SaveTool","id":"p8685"},{"type":"object","name":"HoverTool","id":"p8706","attributes":{"renderers":[{"id":"p8703"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p8669","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8670","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8671"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8672"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p8664","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8665","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8666"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8667"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p8668","attributes":{"axis":{"id":"p8664"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p8673","attributes":{"dimension":1,"axis":{"id":"p8669"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p8686","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p8688","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p8689","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p8690","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p8692","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8691","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p8693","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"12003875-6a4f-4c18-a69d-2c45dc0918f8","roots":{"p8652":"bf1e5d01-5d5a-453d-a7bb-06332d33c2b1"},"root_ids":["p8652"]}];
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

<div id="bddfd757-a948-4c31-b4d3-4197885f3fdf" data-root-id="p8712" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9ee1489d-9891-4a2e-8ead-df1e995fccee":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p8752","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p8753"}}},"roots":[{"type":"object","name":"Figure","id":"p8712","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p8713"},"y_range":{"type":"object","name":"DataRange1d","id":"p8714","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p8721"},"y_scale":{"type":"object","name":"LinearScale","id":"p8722"},"title":{"type":"object","name":"Title","id":"p8719","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p8748","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p8709","attributes":{"selected":{"type":"object","name":"Selection","id":"p8710","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p8711"},"data":{"type":"map","entries":[["year",[2006,2023,2024,2025]],["evaluable",[1,1,4,3]],["detected",[0,0,0,0]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p8749","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8750"}}},"glyph":{"type":"object","name":"VBar","id":"p8745","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p8746","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p8747","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p8720","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p8733"},{"type":"object","name":"BoxZoomTool","id":"p8734","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p8735","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p8741","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8740","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p8742","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p8743"},{"type":"object","name":"SaveTool","id":"p8744"},{"type":"object","name":"HoverTool","id":"p8751","attributes":{"renderers":[{"id":"p8748"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p8728","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8729","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8730"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8731"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p8723","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8724","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8725"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8726"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p8727","attributes":{"axis":{"id":"p8723"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p8732","attributes":{"dimension":1,"axis":{"id":"p8728"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9ee1489d-9891-4a2e-8ead-df1e995fccee","roots":{"p8712":"bddfd757-a948-4c31-b4d3-4197885f3fdf"},"root_ids":["p8712"]}];
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

Disclosures on this entry: `scope_narrower_than_taxid`, `oligos_read_from_figure`.


## What reached the statistics

9,491 records were screened for this assay and **9 (0%)** were evaluable, meaning both primers landed in the right orientation and size range. 9,482 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 9,428 |
| `chance_anchor` | 54 |

