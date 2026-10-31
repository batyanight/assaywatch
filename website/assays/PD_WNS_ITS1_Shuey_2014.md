# PD_WNS_ITS1_Shuey_2014

<span class="aw-chip aw-chip-declining">declining</span>

**PSEUDOGYMNOASCUS DESTRUCTANS (white-nose syndrome) — ITS1 qPCR (Shuey 2014)**

| | |
|---|---|
| Target | Pseudogymnoascus destructans ([taxid 655981](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=655981)) |
| Gene | ITS1 |
| Chemistry | mgb |
| Amplicon | 140 bp |
| Designed | 2014 |
| Paper | [10.1128/aem.02897-13](https://doi.org/10.1128/aem.02897-13) |
| Registry status | active |

!!! quote "The paper"
    Shuey, M. M., Drees, K. P., Lindner, D. L., Keim, P. & Foster, J. T. Highly Sensitive Quantitative PCR for the Detection and Differentiation of Pseudogymnoascus destructans and Other Pseudogymnoascus Species. Applied and Environmental Microbiology 80, 1726-1731 (2014).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CTTTGTTTATTACACTTTGTTGCTTT` | 26 nt |
| reverse | `CCGTTGTTGAAAGTTTTAACTATTATAT` | 28 nt |
| probe | `CTTGCCAGAGGACTAA` | 16 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (36 months, from Oct 2023) | 8 | 16 | 50.0% | 28.0% – 72.0% |
| baseline (everything earlier) | 379 | 441 | 85.9% | 82.4% – 88.9% |

Change from baseline, Newcombe interval: **-58.1% to -13.7%**. Threshold: **90.0%**.

*detected share 50.0% (28%-72%) since Oct 2023, upper bound below the 90% threshold; change from baseline -58% to -14% (window widened to 36 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=4.58e-17, 18 years); by footprint falling (p=0.01). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="f224febb-1594-435a-abb4-d65e55602cfe" data-root-id="p22941" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"61359d01-8b88-4847-9612-1300720a3de6":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p22996","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p22997"}}},"roots":[{"type":"object","name":"Figure","id":"p22941","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p22943"},"y_range":{"type":"object","name":"Range1d","id":"p22950","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p22951"},"y_scale":{"type":"object","name":"LinearScale","id":"p22952"},"title":{"type":"object","name":"Title","id":"p22948","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p22986","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p22938","attributes":{"selected":{"type":"object","name":"Selection","id":"p22939","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p22940"},"data":{"type":"map","entries":[["year",[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,92.85714285714286,100.0,20.0,45.45454545454545,37.5,90.27777777777779,0.0,76.0,66.66666666666666,0.0,25.0,58.333333333333336]],["detected",[10,16,60,17,14,18,13,63,1,5,3,130,0,19,10,0,1,7]],["evaluable",[10,16,60,17,14,18,14,63,5,11,8,144,11,25,15,10,4,12]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[10.143865699252444,10.467343773689333,11.34465373009984,10.508782366508077,10.37579022724969,10.547770533331066,10.37579022724969,11.375828278421016,9.667366891029102,10.209683151927734,9.989711205477885,11.890118112594138,10.209683151927734,10.770092258092593,10.423139468338052,10.143865699252444,9.517227179437622,10.269703144398052]]]}}},"view":{"type":"object","name":"CDSView","id":"p22987","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p22988"}}},"glyph":{"type":"object","name":"Line","id":"p22983","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p22984","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p22985","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p22992","attributes":{"data_source":{"id":"p22938"},"view":{"type":"object","name":"CDSView","id":"p22993","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p22994"}}},"glyph":{"type":"object","name":"Scatter","id":"p22989","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p22990","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p22991","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p22949","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p22963"},{"type":"object","name":"BoxZoomTool","id":"p22964","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p22965","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p22971","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p22970","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p22972","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p22973"},{"type":"object","name":"SaveTool","id":"p22974"},{"type":"object","name":"HoverTool","id":"p22995","attributes":{"renderers":[{"id":"p22992"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p22958","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p22959","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p22960"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22961"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p22953","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p22954","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p22955"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22956"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p22957","attributes":{"axis":{"id":"p22953"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p22962","attributes":{"dimension":1,"axis":{"id":"p22958"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p22975","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2022.5,"right":{"type":"object","name":"Node","id":"p22977","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p22978","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p22979","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p22981","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p22980","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p22982","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"61359d01-8b88-4847-9612-1300720a3de6","roots":{"p22941":"f224febb-1594-435a-abb4-d65e55602cfe"},"root_ids":["p22941"]}];
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

<div id="a67dcf18-d8c6-47e8-aa3c-3866e1741304" data-root-id="p23001" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"3b6e0eed-3a3d-44d3-ae11-13276f5130ba":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p23041","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p23042"}}},"roots":[{"type":"object","name":"Figure","id":"p23001","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p23002"},"y_range":{"type":"object","name":"DataRange1d","id":"p23003","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p23010"},"y_scale":{"type":"object","name":"LinearScale","id":"p23011"},"title":{"type":"object","name":"Title","id":"p23008","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p23037","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p22998","attributes":{"selected":{"type":"object","name":"Selection","id":"p22999","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p23000"},"data":{"type":"map","entries":[["year",[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]],["evaluable",[10,16,60,17,14,18,14,63,5,11,8,144,11,25,15,10,4,12]],["detected",[10,16,60,17,14,18,13,63,1,5,3,130,0,19,10,0,1,7]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p23038","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p23039"}}},"glyph":{"type":"object","name":"VBar","id":"p23034","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p23035","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p23036","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p23009","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p23022"},{"type":"object","name":"BoxZoomTool","id":"p23023","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p23024","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p23030","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p23029","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p23031","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p23032"},{"type":"object","name":"SaveTool","id":"p23033"},{"type":"object","name":"HoverTool","id":"p23040","attributes":{"renderers":[{"id":"p23037"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p23017","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23018","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23019"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23020"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p23012","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23013","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23014"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23015"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p23016","attributes":{"axis":{"id":"p23012"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p23021","attributes":{"dimension":1,"axis":{"id":"p23017"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"3b6e0eed-3a3d-44d3-ae11-13276f5130ba","roots":{"p23001":"a67dcf18-d8c6-47e8-aa3c-3866e1741304"},"root_ids":["p23001"]}];
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

<div id="cc0718d3-9a3a-46a4-89c3-5cfea15d35d3" data-root-id="p23046" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"ebccce6d-1ea0-4d21-ad18-979d5b579485":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p23088","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p23089"}}},"roots":[{"type":"object","name":"Figure","id":"p23046","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p23048"},"y_range":{"type":"object","name":"FactorRange","id":"p23055","attributes":{"factors":["probe"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p23056"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p23057"},"title":{"type":"object","name":"Title","id":"p23053","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p23083","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p23043","attributes":{"selected":{"type":"object","name":"Selection","id":"p23044","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p23045"},"data":{"type":"map","entries":[["x",[-2,-3]],["y",["probe","probe"]],["alpha",[0.6410284463894967,0.6410284463894967]],["pos",[2,3]],["base",["A","T"]],["n",[66,66]],["det_with",["0% of 66","0% of 66"]],["det_without",["100% of 388","100% of 388"]],["subs",["A&gt;T 66","T&gt;C 66"]],["zone",["yes","yes"]]]}}},"view":{"type":"object","name":"CDSView","id":"p23084","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p23085"}}},"glyph":{"type":"object","name":"Rect","id":"p23080","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p23081","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p23082","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p23054","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p23068"},{"type":"object","name":"BoxZoomTool","id":"p23069","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p23070","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p23076","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p23075","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p23077","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p23078"},{"type":"object","name":"SaveTool","id":"p23079"},{"type":"object","name":"HoverTool","id":"p23086","attributes":{"renderers":[{"id":"p23083"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p23063","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p23064"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p23065"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23066"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p23058","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p23087","attributes":{"ticks":[-3,-2],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23060"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-2,"2"],[-3,"3"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p23061"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p23062","attributes":{"axis":{"id":"p23058"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p23067","attributes":{"dimension":1,"axis":{"id":"p23063"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"ebccce6d-1ea0-4d21-ad18-979d5b579485","roots":{"p23046":"cc0718d3-9a3a-46a4-89c3-5cfea15d35d3"},"root_ids":["p23046"]}];
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


## What reached the statistics

12,691 records were screened for this assay and **457 (4%)** were evaluable, meaning both primers landed in the right orientation and size range. 12,234 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 12,226 |
| `chance_anchor` | 5 |
| `truncated` | 3 |

