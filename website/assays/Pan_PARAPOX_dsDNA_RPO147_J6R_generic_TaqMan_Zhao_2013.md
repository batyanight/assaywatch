# Pan_PARAPOX_dsDNA_RPO147_J6R_generic_TaqMan_Zhao_2013

<span class="aw-chip aw-chip-stable">stable</span>

**PARAPOXVIRUS (dsDNA) — RPO147 J6R generic TaqMan (Zhao 2013)**

| | |
|---|---|
| Target | Parapoxvirus ([taxid 10257](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10257)) |
| Gene | RNA polymerase subunit RPO147 (ORF56 in ORFV IA82; vaccinia J6R homolog) |
| Chemistry | hydrolysis_probe |
| Amplicon | 85 bp |
| Designed | 2013 |
| Paper | [10.1016/j.jviromet.2013.08.027](https://doi.org/10.1016/j.jviromet.2013.08.027) |
| Registry status | draft |

!!! quote "The paper"
    Zhao H, Wilkins K, Damon IK, Li Y. 2013. Specific qPCR assays for the detection of orf virus, pseudocowpox virus and bovine papular stomatitis virus. J Virol Methods 194:229-234

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CGCGGTCTGGTCCTTG` | 16 nt |
| reverse | `CAGCATCAACCTCTCCTACATCA` | 23 nt |
| probe | `CCACGAAGCTGCGCAGCAT` | 19 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 32 | 33 | 97.0% | 84.7% – 99.5% |
| baseline (everything earlier) | 82 | 86 | 95.3% | 88.6% – 98.2% |

Change from baseline, Newcombe interval: **-11.0% to 8.8%**. Threshold: **90.0%**.

*detected share 97.0% (85%-99%) since Oct 2024*

Trend across deposit years: by record falling (p=0.453, 17 years); by footprint falling (p=0.171). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="f2617d45-185c-42b9-8679-4617dda9eec1" data-root-id="p26706" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"5c6c682b-7d7d-4e37-8769-39ff8a80c5a3":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p26761","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p26762"}}},"roots":[{"type":"object","name":"Figure","id":"p26706","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p26708"},"y_range":{"type":"object","name":"Range1d","id":"p26715","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p26716"},"y_scale":{"type":"object","name":"LinearScale","id":"p26717"},"title":{"type":"object","name":"Title","id":"p26713","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p26751","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p26703","attributes":{"selected":{"type":"object","name":"Selection","id":"p26704","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p26705"},"data":{"type":"map","entries":[["year",[2003,2004,2006,2009,2010,2011,2012,2014,2015,2018,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,87.5,100.0,100.0,100.0,100.0,92.85714285714286,90.47619047619048,94.73684210526315,100.0]],["detected",[3,2,1,8,3,1,1,5,7,4,6,1,8,13,19,18,14]],["evaluable",[3,2,1,8,3,1,1,5,8,4,6,1,8,14,21,19,14]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.328625426046248,9.07684386569143,8.703135093227193,9.989711205477885,9.328625426046248,8.703135093227193,8.703135093227193,9.667366891029102,9.989711205477885,9.517227179437622,9.791719296345839,8.703135093227193,9.989711205477885,10.37579022724969,10.652487636092928,10.584573151575475,10.37579022724969]]]}}},"view":{"type":"object","name":"CDSView","id":"p26752","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p26753"}}},"glyph":{"type":"object","name":"Line","id":"p26748","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p26749","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p26750","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p26757","attributes":{"data_source":{"id":"p26703"},"view":{"type":"object","name":"CDSView","id":"p26758","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p26759"}}},"glyph":{"type":"object","name":"Scatter","id":"p26754","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p26755","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p26756","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p26714","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p26728"},{"type":"object","name":"BoxZoomTool","id":"p26729","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p26730","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p26736","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p26735","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p26737","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p26738"},{"type":"object","name":"SaveTool","id":"p26739"},{"type":"object","name":"HoverTool","id":"p26760","attributes":{"renderers":[{"id":"p26757"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p26723","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p26724","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p26725"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p26726"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p26718","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p26719","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p26720"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p26721"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p26722","attributes":{"axis":{"id":"p26718"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p26727","attributes":{"dimension":1,"axis":{"id":"p26723"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p26740","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p26742","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p26743","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p26744","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p26746","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p26745","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p26747","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"5c6c682b-7d7d-4e37-8769-39ff8a80c5a3","roots":{"p26706":"f2617d45-185c-42b9-8679-4617dda9eec1"},"root_ids":["p26706"]}];
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

<div id="f671e94f-3136-4aab-aa39-247948f83075" data-root-id="p26766" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"4ece067e-d87b-4b19-9a76-53a9bd3277f6":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p26806","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p26807"}}},"roots":[{"type":"object","name":"Figure","id":"p26766","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p26767"},"y_range":{"type":"object","name":"DataRange1d","id":"p26768","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p26775"},"y_scale":{"type":"object","name":"LinearScale","id":"p26776"},"title":{"type":"object","name":"Title","id":"p26773","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p26802","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p26763","attributes":{"selected":{"type":"object","name":"Selection","id":"p26764","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p26765"},"data":{"type":"map","entries":[["year",[2003,2004,2006,2009,2010,2011,2012,2014,2015,2018,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[3,2,1,8,3,1,1,5,8,4,6,1,8,14,21,19,14]],["detected",[3,2,1,8,3,1,1,5,7,4,6,1,8,13,19,18,14]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p26803","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p26804"}}},"glyph":{"type":"object","name":"VBar","id":"p26799","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p26800","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p26801","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p26774","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p26787"},{"type":"object","name":"BoxZoomTool","id":"p26788","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p26789","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p26795","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p26794","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p26796","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p26797"},{"type":"object","name":"SaveTool","id":"p26798"},{"type":"object","name":"HoverTool","id":"p26805","attributes":{"renderers":[{"id":"p26802"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p26782","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p26783","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p26784"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p26785"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p26777","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p26778","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p26779"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p26780"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p26781","attributes":{"axis":{"id":"p26777"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p26786","attributes":{"dimension":1,"axis":{"id":"p26782"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"4ece067e-d87b-4b19-9a76-53a9bd3277f6","roots":{"p26766":"f671e94f-3136-4aab-aa39-247948f83075"},"root_ids":["p26766"]}];
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

<div id="e2c0be11-4de8-4eff-9b19-b2d22bc39ad4" data-root-id="p26811" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"e096fb3a-62eb-4cbf-a6a2-3eada29433b5":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p26853","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p26854"}}},"roots":[{"type":"object","name":"Figure","id":"p26811","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p26813"},"y_range":{"type":"object","name":"FactorRange","id":"p26820","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p26821"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p26822"},"title":{"type":"object","name":"Title","id":"p26818","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p26848","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p26808","attributes":{"selected":{"type":"object","name":"Selection","id":"p26809","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p26810"},"data":{"type":"map","entries":[["x",[-11,-4,-6,-14,-16,-13,-4,-2,-20,-12,-8]],["y",["reverse","probe","probe","probe","probe","forward","forward","reverse","reverse","probe","reverse"]],["alpha",[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]],["pos",[11,4,6,14,16,13,4,2,20,12,8]],["base",["C","G","C","A","C","G","C","C","C","G","C"]],["n",[85,72,72,72,72,86,56,52,52,52,44]],["det_with",["2% of 85","0% of 72","0% of 72","0% of 72","0% of 72","7% of 86","0% of 56","0% of 52","0% of 52","0% of 52","66% of 44"]],["det_without",["95% of 132","88% of 145","88% of 145","88% of 145","88% of 145","92% of 131","79% of 161","77% of 165","77% of 165","77% of 165","57% of 173"]],["subs",["C&gt;G 71, C&gt;A 12, C&gt;T 2","G&gt;T 72","C&gt;G 72","A&gt;T 72","C&gt;T 72","G&gt;C 72, G&gt;A 14","C&gt;T 56","C&gt;T 52","C&gt;T 52","G&gt;A 52","C&gt;G 40, C&gt;T 3, C&gt;A 1"]],["zone",["no","yes","no","no","no","no","yes","yes","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p26849","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p26850"}}},"glyph":{"type":"object","name":"Rect","id":"p26845","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p26846","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p26847","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p26819","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p26833"},{"type":"object","name":"BoxZoomTool","id":"p26834","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p26835","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p26841","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p26840","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p26842","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p26843"},{"type":"object","name":"SaveTool","id":"p26844"},{"type":"object","name":"HoverTool","id":"p26851","attributes":{"renderers":[{"id":"p26848"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p26828","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p26829"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p26830"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p26831"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p26823","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p26852","attributes":{"ticks":[-20,-16,-14,-13,-12,-11,-8,-6,-4,-2],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p26825"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-11,"11"],[-4,"4"],[-6,"6"],[-14,"14"],[-16,"16"],[-13,"13"],[-2,"2"],[-20,"20"],[-12,"12"],[-8,"8"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p26826"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p26827","attributes":{"axis":{"id":"p26823"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p26832","attributes":{"dimension":1,"axis":{"id":"p26828"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"e096fb3a-62eb-4cbf-a6a2-3eada29433b5","roots":{"p26811":"e2c0be11-4de8-4eff-9b19-b2d22bc39ad4"},"root_ids":["p26811"]}];
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

This entry declares **`scope_taxids`**: [10258](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10258), [129726](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=129726), [129727](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=129727). A record counts toward the denominator when its taxid, or any ancestor, is in that set. Records outside it are screened and reported but kept out of the statistics.

698 screened records fell outside the declared scope.

The paper claims this assay does **not** amplify 2 other taxa. Those are retrieved on purpose and reported as predicted cross-reactivity; they are never scored.

Disclosures on this entry: `amplicon_measured_not_published`, `primer_site_polymorphic`, `chemistry_detail_missing`.


## What reached the statistics

2,768 records were screened for this assay and **119 (4%)** were evaluable, meaning both primers landed in the right orientation and size range. 2,649 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 2,256 |
| `chance_anchor` | 393 |

