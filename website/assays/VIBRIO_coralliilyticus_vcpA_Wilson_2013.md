# VIBRIO_coralliilyticus_vcpA_Wilson_2013

<span class="aw-chip aw-chip-stable">stable</span>

**VIBRIO CORALLIILYTICUS — vcpA SYBR Green qPCR (Wilson 2013)**

| | |
|---|---|
| Target | Vibrio coralliilyticus ([taxid 190893](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=190893)) |
| Gene | vcpA |
| Chemistry | sybr |
| Amplicon | 166 bp |
| Designed | 2013 |
| Paper | [10.1371/journal.pone.0081800](https://doi.org/10.1371/journal.pone.0081800) |
| Registry status | active |

!!! quote "The paper"
    Wilson, B., Muirhead, A., Bazanella, M., Huete-Stauffer, C., Vezzulli, L. & Bourne, D. G. An Improved Detection and Quantification Method for the Coral Pathogen Vibrio coralliilyticus. PLoS ONE 8, e81800 (2013).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `AGCTACGACTGCCGCCCTTAC` | 21 nt |
| reverse | `GGAGCCCTTTCACTTACGATGTTG` | 24 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (48 months, from Oct 2022) | 16 | 16 | 100.0% | 80.6% – 100.0% |
| baseline (everything earlier) | 17 | 19 | 89.5% | 68.6% – 97.1% |

Change from baseline, Newcombe interval: **-10.3% to 31.4%**. Threshold: **90.0%**.

*detected share 100.0% (81%-100%) since Oct 2022 (window widened to 48 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=0.729, 12 years); by footprint falling (p=0.522). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="c7429c88-b56b-4063-81ba-4ca840785596" data-root-id="p34327" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9a5ef066-f60e-44a9-a021-9afd76d1a7ff":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p34382","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p34383"}}},"roots":[{"type":"object","name":"Figure","id":"p34327","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p34329"},"y_range":{"type":"object","name":"Range1d","id":"p34336","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p34337"},"y_scale":{"type":"object","name":"LinearScale","id":"p34338"},"title":{"type":"object","name":"Title","id":"p34334","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p34372","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p34324","attributes":{"selected":{"type":"object","name":"Selection","id":"p34325","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p34326"},"data":{"type":"map","entries":[["year",[2014,2015,2016,2017,2018,2019,2020,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,0.0,100.0,100.0,100.0,100.0]],["detected",[2,3,4,1,1,1,5,0,2,4,2,8]],["evaluable",[2,3,4,1,1,1,5,2,2,4,2,8]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent","recent"]],["size",[9.07684386569143,9.328625426046248,9.517227179437622,8.703135093227193,8.703135093227193,8.703135093227193,9.667366891029102,9.07684386569143,9.07684386569143,9.517227179437622,9.07684386569143,9.989711205477885]]]}}},"view":{"type":"object","name":"CDSView","id":"p34373","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p34374"}}},"glyph":{"type":"object","name":"Line","id":"p34369","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p34370","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p34371","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p34378","attributes":{"data_source":{"id":"p34324"},"view":{"type":"object","name":"CDSView","id":"p34379","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p34380"}}},"glyph":{"type":"object","name":"Scatter","id":"p34375","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p34376","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p34377","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p34335","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p34349"},{"type":"object","name":"BoxZoomTool","id":"p34350","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p34351","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p34357","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p34356","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p34358","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p34359"},{"type":"object","name":"SaveTool","id":"p34360"},{"type":"object","name":"HoverTool","id":"p34381","attributes":{"renderers":[{"id":"p34378"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p34344","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34345","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34346"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34347"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p34339","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34340","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34341"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34342"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p34343","attributes":{"axis":{"id":"p34339"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p34348","attributes":{"dimension":1,"axis":{"id":"p34344"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p34361","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2021.5,"right":{"type":"object","name":"Node","id":"p34363","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p34364","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p34365","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p34367","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p34366","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p34368","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9a5ef066-f60e-44a9-a021-9afd76d1a7ff","roots":{"p34327":"c7429c88-b56b-4063-81ba-4ca840785596"},"root_ids":["p34327"]}];
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

<div id="d9db1e75-c350-43da-b1b7-a297b9efcc7d" data-root-id="p34387" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"3362219d-4136-4b84-8e5b-fb36e44f6dda":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p34427","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p34428"}}},"roots":[{"type":"object","name":"Figure","id":"p34387","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p34388"},"y_range":{"type":"object","name":"DataRange1d","id":"p34389","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p34396"},"y_scale":{"type":"object","name":"LinearScale","id":"p34397"},"title":{"type":"object","name":"Title","id":"p34394","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p34423","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p34384","attributes":{"selected":{"type":"object","name":"Selection","id":"p34385","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p34386"},"data":{"type":"map","entries":[["year",[2014,2015,2016,2017,2018,2019,2020,2022,2023,2024,2025,2026]],["evaluable",[2,3,4,1,1,1,5,2,2,4,2,8]],["detected",[2,3,4,1,1,1,5,0,2,4,2,8]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p34424","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p34425"}}},"glyph":{"type":"object","name":"VBar","id":"p34420","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p34421","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p34422","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p34395","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p34408"},{"type":"object","name":"BoxZoomTool","id":"p34409","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p34410","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p34416","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p34415","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p34417","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p34418"},{"type":"object","name":"SaveTool","id":"p34419"},{"type":"object","name":"HoverTool","id":"p34426","attributes":{"renderers":[{"id":"p34423"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p34403","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34404","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34405"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34406"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p34398","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34399","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34400"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34401"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p34402","attributes":{"axis":{"id":"p34398"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p34407","attributes":{"dimension":1,"axis":{"id":"p34403"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"3362219d-4136-4b84-8e5b-fb36e44f6dda","roots":{"p34387":"d9db1e75-c350-43da-b1b7-a297b9efcc7d"},"root_ids":["p34387"]}];
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

Retrieval query:

```
vcpA[All Fields] OR vtpA[All Fields] OR "complete genome"[Title] OR "chromosome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).


## What reached the statistics

97 records were screened for this assay and **35 (36%)** were evaluable, meaning both primers landed in the right orientation and size range. 62 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 46 |
| `truncated` | 16 |

