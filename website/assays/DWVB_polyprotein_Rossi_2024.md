# DWVB_polyprotein_Rossi_2024

<span class="aw-chip aw-chip-declining">declining</span>

**DEFORMED WING VIRUS B — polyprotein gene RT-qPCR, MGB probe (Rossi 2024)**

| | |
|---|---|
| Target | Deformed wing virus B ([taxid 2498590](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=2498590)) |
| Gene | polyprotein gene |
| Chemistry | mgb |
| Amplicon | 138 bp |
| Designed | 2024 |
| Paper | [10.3390/microorganisms12061105](https://doi.org/10.3390/microorganisms12061105) |
| Registry status | active |

!!! quote "The paper"
    Rossi, F.; Del Matto, I.; Ricchiuti, L.; Marino, L. Selection and Multiplexing of Reverse Transcription–Quantitative PCR Tests Targeting Relevant Honeybee Viral Pathogens. Microorganisms 2024, 12, 1105.

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `TTTATCTTCATTAAAACCGCCA` | 22 nt |
| reverse | `CTCATTAACTGAGTTGTTGTC` | 21 nt |
| probe | `ATCTTTTGAGAGGGATGAGA` | 20 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 12 | 16 | 75.0% | 50.5% – 89.8% |
| baseline (everything earlier) | 41 | 41 | 100.0% | 91.4% – 100.0% |

Change from baseline, Newcombe interval: **-49.5% to -7.9%**. Threshold: **90.0%**.

*detected share 75.0% (51%-90%) since Oct 2024, upper bound below the 90% threshold; change from baseline -49% to -8%*

Trend across deposit years: by record falling (p=8.25e-05, 3 years); by footprint falling (p=0.0232). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="b02a4b66-9536-429b-b7b4-ec1eacbe2f60" data-root-id="p11179" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"8318378e-25d3-474a-88b2-25c0246f864b":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p11234","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p11235"}}},"roots":[{"type":"object","name":"Figure","id":"p11179","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p11181"},"y_range":{"type":"object","name":"Range1d","id":"p11188","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p11189"},"y_scale":{"type":"object","name":"LinearScale","id":"p11190"},"title":{"type":"object","name":"Title","id":"p11186","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p11224","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p11176","attributes":{"selected":{"type":"object","name":"Selection","id":"p11177","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p11178"},"data":{"type":"map","entries":[["year",[2023,2025,2026]],["share",[100.0,90.0,50.0]],["detected",[41,9,3]],["evaluable",[41,10,6]],["window",["baseline","recent","recent"]],["size",[11.098224018878925,10.143865699252444,9.791719296345839]]]}}},"view":{"type":"object","name":"CDSView","id":"p11225","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p11226"}}},"glyph":{"type":"object","name":"Line","id":"p11221","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p11222","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p11223","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p11230","attributes":{"data_source":{"id":"p11176"},"view":{"type":"object","name":"CDSView","id":"p11231","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p11232"}}},"glyph":{"type":"object","name":"Scatter","id":"p11227","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p11228","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p11229","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p11187","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p11201"},{"type":"object","name":"BoxZoomTool","id":"p11202","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p11203","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p11209","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p11208","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p11210","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p11211"},{"type":"object","name":"SaveTool","id":"p11212"},{"type":"object","name":"HoverTool","id":"p11233","attributes":{"renderers":[{"id":"p11230"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p11196","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p11197","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p11198"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11199"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p11191","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p11192","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p11193"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11194"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p11195","attributes":{"axis":{"id":"p11191"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p11200","attributes":{"dimension":1,"axis":{"id":"p11196"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p11213","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2024.5,"right":{"type":"object","name":"Node","id":"p11215","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p11216","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p11217","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p11219","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p11218","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p11220","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"8318378e-25d3-474a-88b2-25c0246f864b","roots":{"p11179":"b02a4b66-9536-429b-b7b4-ec1eacbe2f60"},"root_ids":["p11179"]}];
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

<div id="bf1e7cdd-c53b-4fdf-ab17-53e5053a63d2" data-root-id="p11239" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"61ae92f7-4375-4bf5-89cb-0bdcb9b4d8e5":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p11279","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p11280"}}},"roots":[{"type":"object","name":"Figure","id":"p11239","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p11240"},"y_range":{"type":"object","name":"DataRange1d","id":"p11241","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p11248"},"y_scale":{"type":"object","name":"LinearScale","id":"p11249"},"title":{"type":"object","name":"Title","id":"p11246","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p11275","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p11236","attributes":{"selected":{"type":"object","name":"Selection","id":"p11237","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p11238"},"data":{"type":"map","entries":[["year",[2023,2025,2026]],["evaluable",[41,10,6]],["detected",[41,9,3]],["colour",["#5f6368","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p11276","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p11277"}}},"glyph":{"type":"object","name":"VBar","id":"p11272","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p11273","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p11274","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p11247","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p11260"},{"type":"object","name":"BoxZoomTool","id":"p11261","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p11262","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p11268","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p11267","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p11269","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p11270"},{"type":"object","name":"SaveTool","id":"p11271"},{"type":"object","name":"HoverTool","id":"p11278","attributes":{"renderers":[{"id":"p11275"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p11255","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p11256","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p11257"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11258"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p11250","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p11251","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p11252"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11253"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p11254","attributes":{"axis":{"id":"p11250"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p11259","attributes":{"dimension":1,"axis":{"id":"p11255"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"61ae92f7-4375-4bf5-89cb-0bdcb9b4d8e5","roots":{"p11239":"bf1e7cdd-c53b-4fdf-ab17-53e5053a63d2"},"root_ids":["p11239"]}];
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

Disclosures on this entry: `oligos_from_secondary_source`, `scope_narrower_than_taxid`.


## What reached the statistics

737 records were screened for this assay and **57 (8%)** were evaluable, meaning both primers landed in the right orientation and size range. 680 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 670 |
| `truncated` | 9 |

