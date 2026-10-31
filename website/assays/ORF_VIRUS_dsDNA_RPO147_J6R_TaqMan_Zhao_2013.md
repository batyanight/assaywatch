# ORF_VIRUS_dsDNA_RPO147_J6R_TaqMan_Zhao_2013

<span class="aw-chip aw-chip-stable">stable</span>

**ORF VIRUS (dsDNA) — RPO147 J6R TaqMan, ORFV-specific (Zhao 2013)**

| | |
|---|---|
| Target | Orf virus ([taxid 10258](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10258)) |
| Gene | RNA polymerase subunit RPO147 (ORF56 in ORFV IA82; vaccinia J6R homolog) |
| Chemistry | hydrolysis_probe |
| Amplicon | 68 bp |
| Designed | 2013 |
| Paper | [10.1016/j.jviromet.2013.08.027](https://doi.org/10.1016/j.jviromet.2013.08.027) |
| Registry status | draft |

!!! quote "The paper"
    Zhao H, Wilkins K, Damon IK, Li Y. 2013. Specific qPCR assays for the detection of orf virus, pseudocowpox virus and bovine papular stomatitis virus. J Virol Methods 194:229-234

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GAGTTCGAGGAGATGATCTTGA` | 22 nt |
| reverse | `GCCGAGGAGCAGGTCA` | 16 nt |
| probe | `CTCGATCACGGCGCGCT` | 17 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 27 | 27 | 100.0% | 87.5% – 100.0% |
| baseline (everything earlier) | 56 | 56 | 100.0% | 93.6% – 100.0% |

Change from baseline, Newcombe interval: **-12.5% to 6.4%**. Threshold: **90.0%**.

*detected share 100.0% (88%-100%) since Oct 2024*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="bb99fdfb-f042-4de9-9322-a4ff234b5f6f" data-root-id="p20124" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9b5c0ad7-b103-45e6-990f-3455489d7398":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20179","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20180"}}},"roots":[{"type":"object","name":"Figure","id":"p20124","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p20126"},"y_range":{"type":"object","name":"Range1d","id":"p20133","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p20134"},"y_scale":{"type":"object","name":"LinearScale","id":"p20135"},"title":{"type":"object","name":"Title","id":"p20131","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20169","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20121","attributes":{"selected":{"type":"object","name":"Selection","id":"p20122","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20123"},"data":{"type":"map","entries":[["year",[2003,2004,2006,2009,2011,2012,2014,2015,2018,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[2,1,1,2,1,1,2,5,3,5,1,8,13,11,16,11]],["evaluable",[2,1,1,2,1,1,2,5,3,5,1,8,13,11,16,11]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,8.703135093227193,8.703135093227193,9.07684386569143,8.703135093227193,8.703135093227193,9.07684386569143,9.667366891029102,9.328625426046248,9.667366891029102,8.703135093227193,9.989711205477885,10.324834530005162,10.209683151927734,10.467343773689333,10.209683151927734]]]}}},"view":{"type":"object","name":"CDSView","id":"p20170","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20171"}}},"glyph":{"type":"object","name":"Line","id":"p20166","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p20167","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p20168","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p20175","attributes":{"data_source":{"id":"p20121"},"view":{"type":"object","name":"CDSView","id":"p20176","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20177"}}},"glyph":{"type":"object","name":"Scatter","id":"p20172","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p20173","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p20174","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20132","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20146"},{"type":"object","name":"BoxZoomTool","id":"p20147","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20148","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20154","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20153","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20155","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20156"},{"type":"object","name":"SaveTool","id":"p20157"},{"type":"object","name":"HoverTool","id":"p20178","attributes":{"renderers":[{"id":"p20175"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p20141","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20142","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20143"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20144"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20136","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20137","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20138"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20139"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20140","attributes":{"axis":{"id":"p20136"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20145","attributes":{"dimension":1,"axis":{"id":"p20141"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p20158","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p20160","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p20161","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p20162","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p20164","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20163","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p20165","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9b5c0ad7-b103-45e6-990f-3455489d7398","roots":{"p20124":"bb99fdfb-f042-4de9-9322-a4ff234b5f6f"},"root_ids":["p20124"]}];
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

<div id="d211805f-9595-447f-b758-fde9c0f4c9e5" data-root-id="p20184" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9e48d2c9-f33a-4f96-a8aa-be5a5993b014":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20224","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20225"}}},"roots":[{"type":"object","name":"Figure","id":"p20184","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p20185"},"y_range":{"type":"object","name":"DataRange1d","id":"p20186","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p20193"},"y_scale":{"type":"object","name":"LinearScale","id":"p20194"},"title":{"type":"object","name":"Title","id":"p20191","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20220","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20181","attributes":{"selected":{"type":"object","name":"Selection","id":"p20182","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20183"},"data":{"type":"map","entries":[["year",[2003,2004,2006,2009,2011,2012,2014,2015,2018,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[2,1,1,2,1,1,2,5,3,5,1,8,13,11,16,11]],["detected",[2,1,1,2,1,1,2,5,3,5,1,8,13,11,16,11]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p20221","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20222"}}},"glyph":{"type":"object","name":"VBar","id":"p20217","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p20218","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p20219","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20192","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20205"},{"type":"object","name":"BoxZoomTool","id":"p20206","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20207","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20213","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20212","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20214","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20215"},{"type":"object","name":"SaveTool","id":"p20216"},{"type":"object","name":"HoverTool","id":"p20223","attributes":{"renderers":[{"id":"p20220"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p20200","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20201","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20202"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20203"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20195","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20196","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20197"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20198"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20199","attributes":{"axis":{"id":"p20195"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20204","attributes":{"dimension":1,"axis":{"id":"p20200"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9e48d2c9-f33a-4f96-a8aa-be5a5993b014","roots":{"p20184":"d211805f-9595-447f-b758-fde9c0f4c9e5"},"root_ids":["p20184"]}];
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

<div id="ece1a08e-83eb-4fc6-925f-c27409f09ffe" data-root-id="p20229" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"233e68a3-c3bf-4fcd-a103-c17f4996cc88":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20271","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20272"}}},"roots":[{"type":"object","name":"Figure","id":"p20229","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p20231"},"y_range":{"type":"object","name":"FactorRange","id":"p20238","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p20239"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p20240"},"title":{"type":"object","name":"Title","id":"p20236","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20266","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20226","attributes":{"selected":{"type":"object","name":"Selection","id":"p20227","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20228"},"data":{"type":"map","entries":[["x",[-9,-18,-4,-9,-12,-1,-7,-13,-15,-7,-13,-16,-8,-2,-9,-14]],["y",["forward","forward","reverse","reverse","reverse","forward","forward","forward","forward","reverse","reverse","reverse","probe","reverse","probe","forward"]],["alpha",[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]],["pos",[9,18,4,9,12,1,7,13,15,7,13,16,8,2,9,14]],["base",["T","T","G","A","A","A","A","G","A","C","G","G","G","C","C","G"]],["n",[78,78,78,78,78,77,77,77,77,77,77,77,37,22,22,28]],["det_with",["0% of 78","0% of 78","0% of 78","0% of 78","0% of 78","0% of 77","0% of 77","0% of 77","0% of 77","0% of 77","0% of 77","0% of 77","0% of 37","0% of 22","0% of 22","14% of 28"]],["det_without",["70% of 125","70% of 125","70% of 125","70% of 125","70% of 125","70% of 126","70% of 126","70% of 126","70% of 126","70% of 126","70% of 126","70% of 126","53% of 166","49% of 181","49% of 181","48% of 175"]],["subs",["T&gt;A 77, T&gt;C 1","T&gt;C 78","G&gt;C 77, G&gt;A 1","A&gt;T 77, A&gt;G 1","A&gt;T 77, A&gt;C 1","A&gt;T 77","A&gt;T 76, A&gt;C 1","G&gt;A 77","A&gt;C 77","C&gt;G 77","G&gt;T 77","G&gt;T 77","G&gt;C 37","C&gt;G 22","C&gt;T 22","G&gt;C 24, G&gt;A 4"]],["zone",["no","no","yes","no","no","yes","no","no","no","no","no","no","no","yes","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p20267","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20268"}}},"glyph":{"type":"object","name":"Rect","id":"p20263","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p20264","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p20265","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20237","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20251"},{"type":"object","name":"BoxZoomTool","id":"p20252","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20253","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20259","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20258","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20260","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20261"},{"type":"object","name":"SaveTool","id":"p20262"},{"type":"object","name":"HoverTool","id":"p20269","attributes":{"renderers":[{"id":"p20266"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p20246","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p20247"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p20248"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20249"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20241","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p20270","attributes":{"ticks":[-18,-16,-15,-14,-13,-12,-9,-8,-7,-4,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20243"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-9,"9"],[-18,"18"],[-4,"4"],[-12,"12"],[-1,"1"],[-7,"7"],[-13,"13"],[-15,"15"],[-16,"16"],[-8,"8"],[-2,"2"],[-14,"14"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p20244"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20245","attributes":{"axis":{"id":"p20241"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20250","attributes":{"dimension":1,"axis":{"id":"p20246"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"233e68a3-c3bf-4fcd-a103-c17f4996cc88","roots":{"p20229":"ece1a08e-83eb-4fc6-925f-c27409f09ffe"},"root_ids":["p20229"]}];
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

307 screened records fell outside the declared scope.

The paper claims this assay does **not** amplify 2 other taxa. Those are retrieved on purpose and reported as predicted cross-reactivity; they are never scored.

Disclosures on this entry: `amplicon_measured_not_published`, `chemistry_detail_missing`.


## What reached the statistics

2,463 records were screened for this assay and **83 (3%)** were evaluable, meaning both primers landed in the right orientation and size range. 2,380 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 2,172 |
| `chance_anchor` | 132 |
| `chance_pair` | 76 |

