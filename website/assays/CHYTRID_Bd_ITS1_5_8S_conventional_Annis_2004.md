# CHYTRID_Bd_ITS1_5_8S_conventional_Annis_2004

<span class="aw-chip aw-chip-stable">stable</span>

**Batrachochytrium dendrobatidis — ITS1/5.8S conventional PCR Bd1a/Bd2a (Annis 2004)**

| | |
|---|---|
| Target | Batrachochytrium dendrobatidis ([taxid 109871](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=109871)) |
| Gene | ITS1-5.8S rDNA |
| Chemistry | conventional |
| Amplicon | 300 bp |
| Designed | 2004 |
| Paper | [10.7589/0090-3558-40.3.420](https://doi.org/10.7589/0090-3558-40.3.420) |
| Registry status | active |

!!! quote "The paper"
    Annis SL et al. 2004. J Wildl Dis 40:420-428

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CAGTGTGCCATATGTCACG` | 19 nt |
| reverse | `CATGGTTCATATCTGTCCAG` | 20 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 17 | 17 | 100.0% | 81.6% – 100.0% |
| baseline (everything earlier) | 143 | 163 | 87.7% | 81.8% – 91.9% |

Change from baseline, Newcombe interval: **-6.6% to 18.2%**. Threshold: **90.0%**.

*detected share 100.0% (82%-100%) since Oct 2024*

Trend across deposit years: by record rising (p=0.77, 11 years); by footprint falling (p=0.678); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="bfc0063a-0b70-4efc-bb2a-13ea677fcc6a" data-root-id="p8442" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"77a5cdff-bf35-4cbd-aa1b-da26d46cca7f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p8497","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p8498"}}},"roots":[{"type":"object","name":"Figure","id":"p8442","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p8444"},"y_range":{"type":"object","name":"Range1d","id":"p8451","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p8452"},"y_scale":{"type":"object","name":"LinearScale","id":"p8453"},"title":{"type":"object","name":"Title","id":"p8449","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p8487","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p8439","attributes":{"selected":{"type":"object","name":"Selection","id":"p8440","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p8441"},"data":{"type":"map","entries":[["year",[2005,2006,2011,2012,2014,2016,2018,2020,2023,2024,2025]],["share",[100.0,62.5,100.0,100.0,55.55555555555556,100.0,90.9090909090909,100.0,76.92307692307693,88.63636363636364,100.0]],["detected",[1,5,10,56,10,1,10,1,10,39,17]],["evaluable",[1,8,10,56,18,1,11,1,13,44,17]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent"]],["size",[8.703135093227193,9.989711205477885,10.143865699252444,11.300413928944284,10.547770533331066,8.703135093227193,10.209683151927734,8.703135093227193,10.324834530005162,11.144342382561259,10.508782366508077]]]}}},"view":{"type":"object","name":"CDSView","id":"p8488","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8489"}}},"glyph":{"type":"object","name":"Line","id":"p8484","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p8485","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p8486","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p8493","attributes":{"data_source":{"id":"p8439"},"view":{"type":"object","name":"CDSView","id":"p8494","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8495"}}},"glyph":{"type":"object","name":"Scatter","id":"p8490","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p8491","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p8492","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p8450","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p8464"},{"type":"object","name":"BoxZoomTool","id":"p8465","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p8466","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p8472","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8471","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p8473","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p8474"},{"type":"object","name":"SaveTool","id":"p8475"},{"type":"object","name":"HoverTool","id":"p8496","attributes":{"renderers":[{"id":"p8493"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p8459","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8460","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8461"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8462"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p8454","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8455","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8456"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8457"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p8458","attributes":{"axis":{"id":"p8454"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p8463","attributes":{"dimension":1,"axis":{"id":"p8459"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p8476","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p8478","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p8479","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p8480","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p8482","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8481","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p8483","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"77a5cdff-bf35-4cbd-aa1b-da26d46cca7f","roots":{"p8442":"bfc0063a-0b70-4efc-bb2a-13ea677fcc6a"},"root_ids":["p8442"]}];
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

<div id="cb38ee6b-e22c-46be-a553-f352201a9908" data-root-id="p8502" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"0c892e21-f0b1-440c-886b-80f7bdc90300":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p8542","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p8543"}}},"roots":[{"type":"object","name":"Figure","id":"p8502","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p8503"},"y_range":{"type":"object","name":"DataRange1d","id":"p8504","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p8511"},"y_scale":{"type":"object","name":"LinearScale","id":"p8512"},"title":{"type":"object","name":"Title","id":"p8509","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p8538","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p8499","attributes":{"selected":{"type":"object","name":"Selection","id":"p8500","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p8501"},"data":{"type":"map","entries":[["year",[2005,2006,2011,2012,2014,2016,2018,2020,2023,2024,2025]],["evaluable",[1,8,10,56,18,1,11,1,13,44,17]],["detected",[1,5,10,56,10,1,10,1,10,39,17]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p8539","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8540"}}},"glyph":{"type":"object","name":"VBar","id":"p8535","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p8536","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p8537","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p8510","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p8523"},{"type":"object","name":"BoxZoomTool","id":"p8524","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p8525","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p8531","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8530","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p8532","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p8533"},{"type":"object","name":"SaveTool","id":"p8534"},{"type":"object","name":"HoverTool","id":"p8541","attributes":{"renderers":[{"id":"p8538"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p8518","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8519","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8520"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8521"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p8513","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8514","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8515"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8516"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p8517","attributes":{"axis":{"id":"p8513"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p8522","attributes":{"dimension":1,"axis":{"id":"p8518"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"0c892e21-f0b1-440c-886b-80f7bdc90300","roots":{"p8502":"cb38ee6b-e22c-46be-a553-f352201a9908"},"root_ids":["p8502"]}];
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

Disclosures on this entry: `orientation_inferred`.


## What reached the statistics

9,491 records were screened for this assay and **180 (2%)** were evaluable, meaning both primers landed in the right orientation and size range. 9,311 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 9,105 |
| `chance_anchor` | 96 |
| `chance_only` | 63 |
| `truncated` | 47 |

