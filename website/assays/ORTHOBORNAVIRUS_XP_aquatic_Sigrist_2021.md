# ORTHOBORNAVIRUS_XP_aquatic_Sigrist_2021

<span class="aw-chip aw-chip-stable">stable</span>

**AVIAN ORTHOBORNAVIRUS — X/P triplex qPCR, aquatic bird probe (Sigrist 2021)**

| | |
|---|---|
| Target | Orthobornavirus ([taxid 186458](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=186458)) |
| Gene | X/P |
| Chemistry | hydrolysis_probe |
| Amplicon | 123 bp |
| Designed | 2021 |
| Paper | [10.3390/v13071358](https://doi.org/10.3390/v13071358) |
| Registry status | active |

!!! quote "The paper"
    Sigrist, B., Geers, J., Albini, S., Rubbenstroth, D. & Wolfrum, N. A New Multiplex Real-Time RT-PCR for Simultaneous Detection and Differentiation of Avian Bornaviruses. Viruses 13, 1358 (2021).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CCCGCAGACAGYACGT` | 16 nt |
| reverse | `GAGATCATGGANGGRTTCTT` | 20 nt |
| probe | `CTGACACAACCAGTCGAACA` | 20 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 18 | 18 | 100.0% | 82.4% – 100.0% |
| baseline (everything earlier) | 21 | 21 | 100.0% | 84.5% – 100.0% |

Change from baseline, Newcombe interval: **-17.6% to 15.5%**. Threshold: **90.0%**.

*detected share 100.0% (82%-100%) since Oct 2021 (window widened to 60 months to reach 15 evaluable records)*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="b9402ba4-6eaf-4367-8466-4f9491485145" data-root-id="p20276" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"3a085dbd-aaab-4750-802b-80b1712fe5fd":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20331","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20332"}}},"roots":[{"type":"object","name":"Figure","id":"p20276","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p20278"},"y_range":{"type":"object","name":"Range1d","id":"p20285","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p20286"},"y_scale":{"type":"object","name":"LinearScale","id":"p20287"},"title":{"type":"object","name":"Title","id":"p20283","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20321","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20273","attributes":{"selected":{"type":"object","name":"Selection","id":"p20274","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20275"},"data":{"type":"map","entries":[["year",[2011,2012,2013,2014,2015,2016,2019,2021]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[2,3,1,1,8,4,1,19]],["evaluable",[2,3,1,1,8,4,1,19]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent"]],["size",[9.07684386569143,9.328625426046248,8.703135093227193,8.703135093227193,9.989711205477885,9.517227179437622,8.703135093227193,10.584573151575475]]]}}},"view":{"type":"object","name":"CDSView","id":"p20322","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20323"}}},"glyph":{"type":"object","name":"Line","id":"p20318","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p20319","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p20320","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p20327","attributes":{"data_source":{"id":"p20273"},"view":{"type":"object","name":"CDSView","id":"p20328","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20329"}}},"glyph":{"type":"object","name":"Scatter","id":"p20324","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p20325","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p20326","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20284","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20298"},{"type":"object","name":"BoxZoomTool","id":"p20299","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20300","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20306","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20305","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20307","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20308"},{"type":"object","name":"SaveTool","id":"p20309"},{"type":"object","name":"HoverTool","id":"p20330","attributes":{"renderers":[{"id":"p20327"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p20293","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20294","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20295"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20296"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20288","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20289","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20290"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20291"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20292","attributes":{"axis":{"id":"p20288"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20297","attributes":{"dimension":1,"axis":{"id":"p20293"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p20310","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2020.5,"right":{"type":"object","name":"Node","id":"p20312","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p20313","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p20314","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p20316","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20315","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p20317","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"3a085dbd-aaab-4750-802b-80b1712fe5fd","roots":{"p20276":"b9402ba4-6eaf-4367-8466-4f9491485145"},"root_ids":["p20276"]}];
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

<div id="d18b872d-2959-4479-8b2a-c81c3c16ec86" data-root-id="p20336" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b0e3c5c3-8318-4cc1-ac62-d7bab07196e0":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20376","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20377"}}},"roots":[{"type":"object","name":"Figure","id":"p20336","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p20337"},"y_range":{"type":"object","name":"DataRange1d","id":"p20338","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p20345"},"y_scale":{"type":"object","name":"LinearScale","id":"p20346"},"title":{"type":"object","name":"Title","id":"p20343","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20372","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20333","attributes":{"selected":{"type":"object","name":"Selection","id":"p20334","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20335"},"data":{"type":"map","entries":[["year",[2011,2012,2013,2014,2015,2016,2019,2021]],["evaluable",[2,3,1,1,8,4,1,19]],["detected",[2,3,1,1,8,4,1,19]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p20373","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20374"}}},"glyph":{"type":"object","name":"VBar","id":"p20369","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p20370","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p20371","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20344","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20357"},{"type":"object","name":"BoxZoomTool","id":"p20358","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20359","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20365","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20364","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20366","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20367"},{"type":"object","name":"SaveTool","id":"p20368"},{"type":"object","name":"HoverTool","id":"p20375","attributes":{"renderers":[{"id":"p20372"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p20352","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20353","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20354"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20355"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20347","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20348","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20349"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20350"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20351","attributes":{"axis":{"id":"p20347"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20356","attributes":{"dimension":1,"axis":{"id":"p20352"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b0e3c5c3-8318-4cc1-ac62-d7bab07196e0","roots":{"p20336":"d18b872d-2959-4479-8b2a-c81c3c16ec86"},"root_ids":["p20336"]}];
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

<div id="d44f8164-7e9e-43a5-b12a-7441fe117aef" data-root-id="p20381" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"22ceb82d-f8ad-45bf-a2e3-ba142715d2cb":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20423","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20424"}}},"roots":[{"type":"object","name":"Figure","id":"p20381","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p20383"},"y_range":{"type":"object","name":"FactorRange","id":"p20390","attributes":{"factors":["probe","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p20391"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p20392"},"title":{"type":"object","name":"Title","id":"p20388","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20418","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20378","attributes":{"selected":{"type":"object","name":"Selection","id":"p20379","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20380"},"data":{"type":"map","entries":[["x",[-3,-15,-6,-1,-13,-6,-20,-9,-14,-1,-16,-18]],["y",["probe","probe","forward","forward","forward","probe","probe","probe","forward","probe","forward","probe"]],["alpha",[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]],["pos",[3,15,6,1,13,6,20,9,14,1,16,18]],["base",["A","A","G","T","G","C","C","A","C","A","C","G"]],["n",[369,362,361,354,350,342,187,69,40,28,27,35]],["det_with",["0% of 369","0% of 362","0% of 361","0% of 354","0% of 350","0% of 342","0% of 187","0% of 69","0% of 40","0% of 28","0% of 27","3% of 35"]],["det_without",["23% of 167","22% of 174","22% of 175","21% of 182","21% of 186","20% of 194","11% of 349","8% of 467","8% of 496","8% of 508","8% of 509","8% of 501"]],["subs",["A&gt;C 346, A&gt;G 21, A&gt;T 2","A&gt;C 341, A&gt;T 21","G&gt;C 348, G&gt;T 13","T&gt;A 349, T&gt;C 5","G&gt;C 349, G&gt;A 1","C&gt;A 280, C&gt;G 62","C&gt;T 187","A&gt;T 40, A&gt;G 29","C&gt;T 40","A&gt;G 27, A&gt;T 1","C&gt;T 27","G&gt;A 35"]],["zone",["yes","no","no","yes","no","no","no","no","no","yes","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p20419","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20420"}}},"glyph":{"type":"object","name":"Rect","id":"p20415","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p20416","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p20417","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20389","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20403"},{"type":"object","name":"BoxZoomTool","id":"p20404","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20405","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20411","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20410","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20412","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20413"},{"type":"object","name":"SaveTool","id":"p20414"},{"type":"object","name":"HoverTool","id":"p20421","attributes":{"renderers":[{"id":"p20418"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p20398","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p20399"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p20400"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20401"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20393","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p20422","attributes":{"ticks":[-20,-18,-16,-15,-14,-13,-9,-6,-3,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20395"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-3,"3"],[-15,"15"],[-6,"6"],[-1,"1"],[-13,"13"],[-20,"20"],[-9,"9"],[-14,"14"],[-16,"16"],[-18,"18"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p20396"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20397","attributes":{"axis":{"id":"p20393"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20402","attributes":{"dimension":1,"axis":{"id":"p20398"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"22ceb82d-f8ad-45bf-a2e3-ba142715d2cb","roots":{"p20381":"d44f8164-7e9e-43a5-b12a-7441fe117aef"},"root_ids":["p20381"]}];
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

This entry declares **`scope_taxids`**: [1548722](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1548722). A record counts toward the denominator when its taxid, or any ancestor, is in that set. Records outside it are screened and reported but kept out of the statistics.

1,278 screened records fell outside the declared scope.

Disclosures on this entry: `chemistry_detail_missing`, `oligos_read_from_figure`.


## What reached the statistics

82 records were screened for this assay and **39 (48%)** were evaluable, meaning both primers landed in the right orientation and size range. 43 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 43 |

