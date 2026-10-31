# LMBV_dsDNA_MCP_Grizzle_2003

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**LARGEMOUTH BASS VIRUS (dsDNA) — MCP, LMBV288F/535R (Grizzle 2003)**

| | |
|---|---|
| Target | Largemouth bass virus (sensu stricto) ([taxid 10492](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10492)) |
| Gene | MCP |
| Chemistry | conventional |
| Amplicon | 248 bp |
| Designed | 2003 |
| Paper | [10.3354/dao054029](https://doi.org/10.3354/dao054029) |
| Registry status | active |

!!! quote "The paper"
    Grizzle, J. M., Altinok, I. & Noyes, A. D. PCR method for detection of largemouth bass virus. Diseases of Aquatic Organisms 54, 29-33 (2003).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GCGGCCAACCAGTTTAACGCAA` | 22 nt |
| reverse | `AGGACCCTAGCTCCTGCTTGAT` | 22 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 2 | 12 | 16.7% | 4.7% – 44.8% |
| baseline (everything earlier) | 10 | 22 | 45.5% | 26.9% – 65.3% |

Change from baseline, Newcombe interval: **-52.0% to 4.9%**. Threshold: **90.0%**.

*12 evaluable records since Oct 2021, below the minimum of 15; the detected share is 17% (5%-45%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=0.0638, 12 years); by footprint falling (p=0.196). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="f62cb949-d207-4ec8-adfe-1cb93fdaf757" data-root-id="p15955" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"df409a1b-fcde-425e-9da1-d5dda638fd69":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p16010","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p16011"}}},"roots":[{"type":"object","name":"Figure","id":"p15955","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p15957"},"y_range":{"type":"object","name":"Range1d","id":"p15964","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p15965"},"y_scale":{"type":"object","name":"LinearScale","id":"p15966"},"title":{"type":"object","name":"Title","id":"p15962","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p16000","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p15952","attributes":{"selected":{"type":"object","name":"Selection","id":"p15953","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p15954"},"data":{"type":"map","entries":[["year",[1998,2011,2012,2016,2018,2019,2020,2022,2023,2024,2025,2026]],["share",[100.0,33.33333333333333,100.0,0.0,80.0,0.0,66.66666666666666,0.0,0.0,100.0,33.33333333333333,0.0]],["detected",[1,1,2,0,4,0,2,0,0,1,1,0]],["evaluable",[1,3,2,3,5,5,3,4,3,1,3,1]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent","recent"]],["size",[8.703135093227193,9.328625426046248,9.07684386569143,9.328625426046248,9.667366891029102,9.667366891029102,9.328625426046248,9.517227179437622,9.328625426046248,8.703135093227193,9.328625426046248,8.703135093227193]]]}}},"view":{"type":"object","name":"CDSView","id":"p16001","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16002"}}},"glyph":{"type":"object","name":"Line","id":"p15997","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p15998","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p15999","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p16006","attributes":{"data_source":{"id":"p15952"},"view":{"type":"object","name":"CDSView","id":"p16007","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16008"}}},"glyph":{"type":"object","name":"Scatter","id":"p16003","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p16004","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p16005","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p15963","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p15977"},{"type":"object","name":"BoxZoomTool","id":"p15978","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p15979","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p15985","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15984","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p15986","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p15987"},{"type":"object","name":"SaveTool","id":"p15988"},{"type":"object","name":"HoverTool","id":"p16009","attributes":{"renderers":[{"id":"p16006"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p15972","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15973","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15974"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15975"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p15967","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15968","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15969"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15970"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p15971","attributes":{"axis":{"id":"p15967"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p15976","attributes":{"dimension":1,"axis":{"id":"p15972"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p15989","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2021.5,"right":{"type":"object","name":"Node","id":"p15991","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p15992","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p15993","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p15995","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15994","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p15996","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"df409a1b-fcde-425e-9da1-d5dda638fd69","roots":{"p15955":"f62cb949-d207-4ec8-adfe-1cb93fdaf757"},"root_ids":["p15955"]}];
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

<div id="d3fdbb86-ddbb-435f-80c2-cf575456d52b" data-root-id="p16015" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"f1471cf2-b6bc-432b-93d5-fc9840e8f905":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p16055","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p16056"}}},"roots":[{"type":"object","name":"Figure","id":"p16015","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p16016"},"y_range":{"type":"object","name":"DataRange1d","id":"p16017","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p16024"},"y_scale":{"type":"object","name":"LinearScale","id":"p16025"},"title":{"type":"object","name":"Title","id":"p16022","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p16051","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p16012","attributes":{"selected":{"type":"object","name":"Selection","id":"p16013","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p16014"},"data":{"type":"map","entries":[["year",[1998,2011,2012,2016,2018,2019,2020,2022,2023,2024,2025,2026]],["evaluable",[1,3,2,3,5,5,3,4,3,1,3,1]],["detected",[1,1,2,0,4,0,2,0,0,1,1,0]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p16052","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16053"}}},"glyph":{"type":"object","name":"VBar","id":"p16048","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p16049","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p16050","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p16023","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p16036"},{"type":"object","name":"BoxZoomTool","id":"p16037","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p16038","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p16044","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16043","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p16045","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p16046"},{"type":"object","name":"SaveTool","id":"p16047"},{"type":"object","name":"HoverTool","id":"p16054","attributes":{"renderers":[{"id":"p16051"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p16031","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16032","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16033"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16034"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p16026","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16027","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16028"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16029"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p16030","attributes":{"axis":{"id":"p16026"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p16035","attributes":{"dimension":1,"axis":{"id":"p16031"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"f1471cf2-b6bc-432b-93d5-fc9840e8f905","roots":{"p16015":"d3fdbb86-ddbb-435f-80c2-cf575456d52b"},"root_ids":["p16015"]}];
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

<div id="d6f1a313-0de3-4d0b-9c0d-05671e8bd161" data-root-id="p16060" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"7bccca34-afb3-40a0-8fc1-bac3a9bd0c4f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p16102","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p16103"}}},"roots":[{"type":"object","name":"Figure","id":"p16060","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p16062"},"y_range":{"type":"object","name":"FactorRange","id":"p16069","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p16070"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p16071"},"title":{"type":"object","name":"Title","id":"p16067","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p16097","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p16057","attributes":{"selected":{"type":"object","name":"Selection","id":"p16058","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p16059"},"data":{"type":"map","entries":[["x",[-1,-2,-3,-4,-1]],["y",["forward","forward","forward","forward","reverse"]],["alpha",[1.0,1.0,1.0,1.0,1.0]],["pos",[1,2,3,4,1]],["base",["A","A","C","G","T"]],["n",[22,22,22,22,22]],["det_with",["0% of 22","0% of 22","0% of 22","0% of 22","0% of 22"]],["det_without",["100% of 12","100% of 12","100% of 12","100% of 12","100% of 12"]],["subs",["A&gt;G 22","A&gt;T 22","C&gt;A 22","G&gt;A 22","T&gt;C 22"]],["zone",["yes","yes","yes","yes","yes"]]]}}},"view":{"type":"object","name":"CDSView","id":"p16098","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16099"}}},"glyph":{"type":"object","name":"Rect","id":"p16094","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p16095","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p16096","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p16068","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p16082"},{"type":"object","name":"BoxZoomTool","id":"p16083","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p16084","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p16090","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16089","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p16091","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p16092"},{"type":"object","name":"SaveTool","id":"p16093"},{"type":"object","name":"HoverTool","id":"p16100","attributes":{"renderers":[{"id":"p16097"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p16077","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p16078"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p16079"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16080"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p16072","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p16101","attributes":{"ticks":[-4,-3,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16074"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-1,"1"],[-2,"2"],[-3,"3"],[-4,"4"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p16075"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p16076","attributes":{"axis":{"id":"p16072"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p16081","attributes":{"dimension":1,"axis":{"id":"p16077"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"7bccca34-afb3-40a0-8fc1-bac3a9bd0c4f","roots":{"p16060":"d6f1a313-0de3-4d0b-9c0d-05671e8bd161"},"root_ids":["p16060"]}];
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


## Scope — what this assay is judged against

This entry declares no `scope_taxids`, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower set than its taxid covers, that reads as low coverage rather than as drift — see [scoping](../scoping.md).

Retrieval query:

```
txid176656[Organism:exp] OR txid198068[Organism:exp] OR txid2107207[Organism:exp] OR txid3045951[Organism:exp] OR txid1162553[Organism:exp]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).


## What reached the statistics

114 records were screened for this assay and **34 (30%)** were evaluable, meaning both primers landed in the right orientation and size range. 80 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 79 |
| `chance_anchor` | 1 |

