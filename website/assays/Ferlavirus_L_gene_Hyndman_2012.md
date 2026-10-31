# Ferlavirus_L_gene_Hyndman_2012

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**Ferlavirus — L gene**

| | |
|---|---|
| Target | Ferlavirus ([taxid 1283308](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1283308)) |
| Gene | L gene |
| Chemistry | conventional |
| Amplicon | 149 bp |
| Designed | 2012 |
| Paper | [10.1016/j.vetmic.2012.07.030](https://doi.org/10.1016/j.vetmic.2012.07.030) |
| Registry status | active |

!!! quote "The paper"
    Hyndman TH et al. 2012. Vet Microbiol 161:77-87

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GTTATGGCAAATCATGCTGCGATACCTTA` | 29 nt |
| reverse | `CTGATGGGAGATAATGCCTTGTCCTTCAT` | 29 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 6 | 7 | 85.7% | 48.7% – 97.4% |
| baseline (everything earlier) | 21 | 46 | 45.7% | 32.2% – 59.8% |

Change from baseline, Newcombe interval: **0.4% to 57.9%**. Threshold: **90.0%**.

*7 evaluable records since Oct 2021, below the minimum of 15; the detected share is 86% (49%-97%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record rising (p=0.0134, 11 years); by footprint rising (p=0.188). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="bbb23304-26ed-4ab1-bec8-d5051ce3755d" data-root-id="p13081" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"1c667322-77dc-4d1a-8d66-d23bcb6c99c2":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p13136","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p13137"}}},"roots":[{"type":"object","name":"Figure","id":"p13081","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p13083"},"y_range":{"type":"object","name":"Range1d","id":"p13090","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p13091"},"y_scale":{"type":"object","name":"LinearScale","id":"p13092"},"title":{"type":"object","name":"Title","id":"p13088","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p13126","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p13078","attributes":{"selected":{"type":"object","name":"Selection","id":"p13079","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p13080"},"data":{"type":"map","entries":[["year",[2001,2003,2014,2017,2018,2019,2020,2021,2024,2025,2026]],["share",[50.0,0.0,0.0,0.0,50.0,53.57142857142857,100.0,75.0,100.0,100.0,75.0]],["detected",[1,0,0,0,1,15,1,3,1,2,3]],["evaluable",[2,2,5,2,2,28,1,4,1,2,4]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent"]],["size",[9.07684386569143,9.07684386569143,9.667366891029102,9.07684386569143,9.07684386569143,10.846014908695619,8.703135093227193,9.517227179437622,8.703135093227193,9.07684386569143,9.517227179437622]]]}}},"view":{"type":"object","name":"CDSView","id":"p13127","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13128"}}},"glyph":{"type":"object","name":"Line","id":"p13123","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p13124","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p13125","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p13132","attributes":{"data_source":{"id":"p13078"},"view":{"type":"object","name":"CDSView","id":"p13133","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13134"}}},"glyph":{"type":"object","name":"Scatter","id":"p13129","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p13130","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p13131","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p13089","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p13103"},{"type":"object","name":"BoxZoomTool","id":"p13104","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p13105","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p13111","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13110","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p13112","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p13113"},{"type":"object","name":"SaveTool","id":"p13114"},{"type":"object","name":"HoverTool","id":"p13135","attributes":{"renderers":[{"id":"p13132"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p13098","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13099","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13100"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13101"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p13093","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13094","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13095"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13096"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p13097","attributes":{"axis":{"id":"p13093"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p13102","attributes":{"dimension":1,"axis":{"id":"p13098"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p13115","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2020.5,"right":{"type":"object","name":"Node","id":"p13117","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p13118","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p13119","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p13121","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13120","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p13122","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"1c667322-77dc-4d1a-8d66-d23bcb6c99c2","roots":{"p13081":"bbb23304-26ed-4ab1-bec8-d5051ce3755d"},"root_ids":["p13081"]}];
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

<div id="a7530503-03d0-4e81-82b7-f80e009d5fb3" data-root-id="p13141" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"53d6b31e-8a7e-4155-bc8a-87e594c77f33":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p13181","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p13182"}}},"roots":[{"type":"object","name":"Figure","id":"p13141","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p13142"},"y_range":{"type":"object","name":"DataRange1d","id":"p13143","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p13150"},"y_scale":{"type":"object","name":"LinearScale","id":"p13151"},"title":{"type":"object","name":"Title","id":"p13148","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p13177","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p13138","attributes":{"selected":{"type":"object","name":"Selection","id":"p13139","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p13140"},"data":{"type":"map","entries":[["year",[2001,2003,2014,2017,2018,2019,2020,2021,2024,2025,2026]],["evaluable",[2,2,5,2,2,28,1,4,1,2,4]],["detected",[1,0,0,0,1,15,1,3,1,2,3]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p13178","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13179"}}},"glyph":{"type":"object","name":"VBar","id":"p13174","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p13175","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p13176","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p13149","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p13162"},{"type":"object","name":"BoxZoomTool","id":"p13163","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p13164","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p13170","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13169","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p13171","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p13172"},{"type":"object","name":"SaveTool","id":"p13173"},{"type":"object","name":"HoverTool","id":"p13180","attributes":{"renderers":[{"id":"p13177"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p13157","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13158","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13159"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13160"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p13152","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13153","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13154"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13155"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p13156","attributes":{"axis":{"id":"p13152"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p13161","attributes":{"dimension":1,"axis":{"id":"p13157"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"53d6b31e-8a7e-4155-bc8a-87e594c77f33","roots":{"p13141":"a7530503-03d0-4e81-82b7-f80e009d5fb3"},"root_ids":["p13141"]}];
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

<div id="e435a80e-749b-4c30-b286-f89c29d4c5eb" data-root-id="p13186" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"dded6e97-b4c5-4f50-bd10-0ae2c8c1c505":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p13228","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p13229"}}},"roots":[{"type":"object","name":"Figure","id":"p13186","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p13188"},"y_range":{"type":"object","name":"FactorRange","id":"p13195","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p13196"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p13197"},"title":{"type":"object","name":"Title","id":"p13193","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p13223","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p13183","attributes":{"selected":{"type":"object","name":"Selection","id":"p13184","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p13185"},"data":{"type":"map","entries":[["x",[-24,-6,-9,-6,-12]],["y",["reverse","forward","forward","reverse","reverse"]],["alpha",[1.0,1.0,1.0,1.0,1.0]],["pos",[24,6,9,6,12]],["base",["G","A","G","C","C"]],["n",[23,21,24,37,29]],["det_with",["13% of 23","10% of 21","21% of 24","68% of 37","86% of 29"]],["det_without",["100% of 24","96% of 26","96% of 23","20% of 10","11% of 18"]],["subs",["G&gt;A 23","A&gt;T 12, A&gt;C 9","G&gt;A 21, G&gt;T 3","C&gt;T 37","C&gt;T 29"]],["zone",["no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p13224","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13225"}}},"glyph":{"type":"object","name":"Rect","id":"p13220","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p13221","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p13222","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p13194","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p13208"},{"type":"object","name":"BoxZoomTool","id":"p13209","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p13210","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p13216","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13215","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p13217","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p13218"},{"type":"object","name":"SaveTool","id":"p13219"},{"type":"object","name":"HoverTool","id":"p13226","attributes":{"renderers":[{"id":"p13223"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p13203","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p13204"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p13205"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13206"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p13198","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p13227","attributes":{"ticks":[-24,-12,-9,-6],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13200"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-24,"24"],[-6,"6"],[-9,"9"],[-12,"12"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p13201"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p13202","attributes":{"axis":{"id":"p13198"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p13207","attributes":{"dimension":1,"axis":{"id":"p13203"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"dded6e97-b4c5-4f50-bd10-0ae2c8c1c505","roots":{"p13186":"e435a80e-749b-4c30-b286-f89c29d4c5eb"},"root_ids":["p13186"]}];
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

Disclosures on this entry: `orientation_inferred`.


## What reached the statistics

61 records were screened for this assay and **53 (87%)** were evaluable, meaning both primers landed in the right orientation and size range. 8 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 8 |

