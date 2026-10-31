# Encephalitozoon_Polar_tube_protein_E_cun_Xiao_2001

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**Encephalitozoon — Polar tube protein (E. cuniculi only)**

| | |
|---|---|
| Target | Encephalitozoon cuniculi ([taxid 6035](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=6035)) |
| Gene | Polar tube protein (E. cuniculi only) |
| Chemistry | conventional |
| Amplicon | — |
| Designed | 2001 |
| Paper | [10.1128/JCM.39.6.2248-2253.2001](https://doi.org/10.1128/JCM.39.6.2248-2253.2001) |
| Registry status | active |

!!! quote "The paper"
    Xiao L, Li L, Visvesvara GS, Moura H, Didier ES, Lal AA. 2001. Genotyping Encephalitozoon cuniculi by multilocus analyses of genes with repetitive sequences. J Clin Microbiol 39:2248-2253

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GCAGTTCCAGGCTACTAC` | 18 nt |
| reverse | `AGGAACTCCGGATGTTCC` | 18 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 7 | 12 | 58.3% | 32.0% – 80.7% |
| baseline (everything earlier) | 10 | 23 | 43.5% | 25.6% – 63.2% |

Change from baseline, Newcombe interval: **-18.1% to 43.4%**. Threshold: **90.0%**.

*12 evaluable records since Oct 2021, below the minimum of 15; the detected share is 58% (32%-81%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record rising (p=0.632, 11 years); by footprint falling (p=0.788); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="cfe42a22-9120-4ae6-b473-89934fd33cf0" data-root-id="p12358" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"74e4063f-e6d2-405a-955b-86f22e071a27":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12413","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12414"}}},"roots":[{"type":"object","name":"Figure","id":"p12358","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p12360"},"y_range":{"type":"object","name":"Range1d","id":"p12367","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p12368"},"y_scale":{"type":"object","name":"LinearScale","id":"p12369"},"title":{"type":"object","name":"Title","id":"p12365","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12403","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12355","attributes":{"selected":{"type":"object","name":"Selection","id":"p12356","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12357"},"data":{"type":"map","entries":[["year",[1998,2000,2001,2006,2008,2010,2013,2015,2022,2023,2026]],["share",[100.0,100.0,100.0,9.090909090909092,0.0,0.0,50.0,100.0,0.0,100.0,100.0]],["detected",[1,1,5,1,0,0,1,1,0,1,6]],["evaluable",[1,1,5,11,1,1,2,1,5,1,6]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.667366891029102,10.209683151927734,8.703135093227193,8.703135093227193,9.07684386569143,8.703135093227193,9.667366891029102,8.703135093227193,9.791719296345839]]]}}},"view":{"type":"object","name":"CDSView","id":"p12404","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12405"}}},"glyph":{"type":"object","name":"Line","id":"p12400","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p12401","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p12402","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p12409","attributes":{"data_source":{"id":"p12355"},"view":{"type":"object","name":"CDSView","id":"p12410","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12411"}}},"glyph":{"type":"object","name":"Scatter","id":"p12406","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p12407","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p12408","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12366","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12380"},{"type":"object","name":"BoxZoomTool","id":"p12381","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12382","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12388","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12387","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12389","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12390"},{"type":"object","name":"SaveTool","id":"p12391"},{"type":"object","name":"HoverTool","id":"p12412","attributes":{"renderers":[{"id":"p12409"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p12375","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12376","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12377"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12378"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12370","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12371","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12372"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12373"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12374","attributes":{"axis":{"id":"p12370"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12379","attributes":{"dimension":1,"axis":{"id":"p12375"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p12392","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2021.5,"right":{"type":"object","name":"Node","id":"p12394","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p12395","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p12396","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p12398","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12397","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p12399","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"74e4063f-e6d2-405a-955b-86f22e071a27","roots":{"p12358":"cfe42a22-9120-4ae6-b473-89934fd33cf0"},"root_ids":["p12358"]}];
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

<div id="fc00fd18-95a1-4d24-9bcf-9311a906c598" data-root-id="p12418" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9c881b6b-7d27-4499-9d77-5c37fdbeecbf":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12458","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12459"}}},"roots":[{"type":"object","name":"Figure","id":"p12418","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p12419"},"y_range":{"type":"object","name":"DataRange1d","id":"p12420","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p12427"},"y_scale":{"type":"object","name":"LinearScale","id":"p12428"},"title":{"type":"object","name":"Title","id":"p12425","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12454","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12415","attributes":{"selected":{"type":"object","name":"Selection","id":"p12416","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12417"},"data":{"type":"map","entries":[["year",[1998,2000,2001,2006,2008,2010,2013,2015,2022,2023,2026]],["evaluable",[1,1,5,11,1,1,2,1,5,1,6]],["detected",[1,1,5,1,0,0,1,1,0,1,6]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p12455","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12456"}}},"glyph":{"type":"object","name":"VBar","id":"p12451","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p12452","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p12453","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12426","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12439"},{"type":"object","name":"BoxZoomTool","id":"p12440","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12441","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12447","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12446","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12448","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12449"},{"type":"object","name":"SaveTool","id":"p12450"},{"type":"object","name":"HoverTool","id":"p12457","attributes":{"renderers":[{"id":"p12454"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p12434","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12435","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12436"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12437"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12429","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12430","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12431"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12432"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12433","attributes":{"axis":{"id":"p12429"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12438","attributes":{"dimension":1,"axis":{"id":"p12434"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9c881b6b-7d27-4499-9d77-5c37fdbeecbf","roots":{"p12418":"fc00fd18-95a1-4d24-9bcf-9311a906c598"},"root_ids":["p12418"]}];
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

Disclosures on this entry: `amplicon_multimodal`, `thin_evidence`.


## What reached the statistics

2,730 records were screened for this assay and **35 (1%)** were evaluable, meaning both primers landed in the right orientation and size range. 2,695 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 2,534 |
| `chance_only` | 99 |
| `chance_anchor` | 46 |
| `truncated` | 14 |
| `no_pair` | 2 |

