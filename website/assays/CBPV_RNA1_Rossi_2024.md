# CBPV_RNA1_Rossi_2024

<span class="aw-chip aw-chip-stable">stable</span>

**CHRONIC BEE PARALYSIS VIRUS — RNA1 RT-qPCR, MGB probe (Rossi 2024)**

| | |
|---|---|
| Target | Chronic bee paralysis virus ([taxid 180822](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=180822)) |
| Gene | RNA1 |
| Chemistry | mgb |
| Amplicon | 112 bp |
| Designed | 2024 |
| Paper | [10.3390/microorganisms12061105](https://doi.org/10.3390/microorganisms12061105) |
| Registry status | active |

!!! quote "The paper"
    Rossi, F.; Del Matto, I.; Ricchiuti, L.; Marino, L. Selection and Multiplexing of Reverse Transcription–Quantitative PCR Tests Targeting Relevant Honeybee Viral Pathogens. Microorganisms 2024, 12, 1105.

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GAAGTCATCCGTAGATCTGG` | 20 nt |
| reverse | `CRAGAGGGGTATGTTGTACT` | 20 nt |
| probe | `AGACKAGRGAGGAYGGGA` | 18 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 26 | 27 | 96.3% | 81.7% – 99.3% |
| baseline (everything earlier) | 112 | 124 | 90.3% | 83.8% – 94.4% |

Change from baseline, Newcombe interval: **-9.2% to 13.1%**. Threshold: **90.0%**.

*detected share 96.3% (82%-99%) since Oct 2024*

Trend across deposit years: by record falling (p=0.0965, 15 years); by footprint falling (p=0.0818). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="ac05a5ab-7b73-4b30-a75e-92b2124355f5" data-root-id="p6226" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"1da72c29-f02a-40fd-8ea3-0835d89f4d85":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p6281","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p6282"}}},"roots":[{"type":"object","name":"Figure","id":"p6226","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p6228"},"y_range":{"type":"object","name":"Range1d","id":"p6235","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p6236"},"y_scale":{"type":"object","name":"LinearScale","id":"p6237"},"title":{"type":"object","name":"Title","id":"p6233","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p6271","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p6223","attributes":{"selected":{"type":"object","name":"Selection","id":"p6224","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p6225"},"data":{"type":"map","entries":[["year",[2007,2008,2009,2011,2014,2016,2017,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,40.0,75.0,94.44444444444444,100.0,96.0]],["detected",[2,1,22,5,2,2,4,2,5,24,6,3,34,2,24]],["evaluable",[2,1,22,5,2,2,4,2,5,24,15,4,36,2,25]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,8.703135093227193,10.683957047019447,9.667366891029102,9.07684386569143,9.07684386569143,9.517227179437622,9.07684386569143,9.667366891029102,10.74264168206181,10.423139468338052,9.517227179437622,11.012804945939648,9.07684386569143,10.770092258092593]]]}}},"view":{"type":"object","name":"CDSView","id":"p6272","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p6273"}}},"glyph":{"type":"object","name":"Line","id":"p6268","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p6269","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p6270","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p6277","attributes":{"data_source":{"id":"p6223"},"view":{"type":"object","name":"CDSView","id":"p6278","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p6279"}}},"glyph":{"type":"object","name":"Scatter","id":"p6274","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p6275","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p6276","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p6234","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p6248"},{"type":"object","name":"BoxZoomTool","id":"p6249","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p6250","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p6256","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p6255","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p6257","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p6258"},{"type":"object","name":"SaveTool","id":"p6259"},{"type":"object","name":"HoverTool","id":"p6280","attributes":{"renderers":[{"id":"p6277"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p6243","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p6244","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p6245"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p6246"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p6238","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p6239","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p6240"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p6241"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p6242","attributes":{"axis":{"id":"p6238"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p6247","attributes":{"dimension":1,"axis":{"id":"p6243"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p6260","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p6262","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p6263","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p6264","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p6266","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p6265","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p6267","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"1da72c29-f02a-40fd-8ea3-0835d89f4d85","roots":{"p6226":"ac05a5ab-7b73-4b30-a75e-92b2124355f5"},"root_ids":["p6226"]}];
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

<div id="ad892096-045e-44c4-bbe0-b993b1969cac" data-root-id="p6286" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b9948391-2fa3-4251-b1b3-7ad27fa60111":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p6326","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p6327"}}},"roots":[{"type":"object","name":"Figure","id":"p6286","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p6287"},"y_range":{"type":"object","name":"DataRange1d","id":"p6288","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p6295"},"y_scale":{"type":"object","name":"LinearScale","id":"p6296"},"title":{"type":"object","name":"Title","id":"p6293","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p6322","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p6283","attributes":{"selected":{"type":"object","name":"Selection","id":"p6284","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p6285"},"data":{"type":"map","entries":[["year",[2007,2008,2009,2011,2014,2016,2017,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[2,1,22,5,2,2,4,2,5,24,15,4,36,2,25]],["detected",[2,1,22,5,2,2,4,2,5,24,6,3,34,2,24]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p6323","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p6324"}}},"glyph":{"type":"object","name":"VBar","id":"p6319","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p6320","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p6321","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p6294","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p6307"},{"type":"object","name":"BoxZoomTool","id":"p6308","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p6309","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p6315","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p6314","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p6316","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p6317"},{"type":"object","name":"SaveTool","id":"p6318"},{"type":"object","name":"HoverTool","id":"p6325","attributes":{"renderers":[{"id":"p6322"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p6302","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p6303","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p6304"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p6305"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p6297","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p6298","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p6299"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p6300"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p6301","attributes":{"axis":{"id":"p6297"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p6306","attributes":{"dimension":1,"axis":{"id":"p6302"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b9948391-2fa3-4251-b1b3-7ad27fa60111","roots":{"p6286":"ad892096-045e-44c4-bbe0-b993b1969cac"},"root_ids":["p6286"]}];
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

573 records were screened for this assay and **151 (26%)** were evaluable, meaning both primers landed in the right orientation and size range. 422 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 392 |
| `truncated` | 30 |

