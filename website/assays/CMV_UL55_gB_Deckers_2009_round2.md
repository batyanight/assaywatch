# CMV_UL55_gB_Deckers_2009_round2

<span class="aw-chip aw-chip-stable">stable</span>

**CMV-specific HERPES — UL55 /Glycoprotein B (gB)**

| | |
|---|---|
| Target | Cytomegalovirus ([taxid 10358](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10358)) |
| Gene | UL55 /Glycoprotein B (gB) |
| Chemistry | conventional |
| Amplicon | 550 bp |
| Designed | 2009 |
| Paper | [10.1186/1743-422X-6-210](https://doi.org/10.1186/1743-422X-6-210) |
| Registry status | active |

!!! quote "The paper"
    Deckers, M.; Hofmann, J.; Kreuzer, K. A.; Reinhard, H.; Edubio, A.; Hengel, H. High genotypic diversity and a novel variant of human cytomegalovirus revealed by combined UL33/UL55 genotyping with broad-range PCR. Virology Journal 2009, 6, 210.

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GCGGACTCGGTGATNTCNTGGGA` | 23 nt |
| reverse | `GCTGACGGGTTGATCTTGCTRAG` | 23 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 29 | 32 | 90.6% | 75.8% – 96.8% |
| baseline (everything earlier) | 511 | 542 | 94.3% | 92.0% – 95.9% |

Change from baseline, Newcombe interval: **-18.6% to 2.9%**. Threshold: **90.0%**.

*detected share 90.6% (76%-97%) since Oct 2024*

Trend across deposit years: by record rising (p=0.183, 30 years); by footprint falling (p=0.633); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="b981b4d3-cfce-425c-baac-b150c406911a" data-root-id="p9480" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"38959b33-8e90-421b-827f-e3c114615cb0":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p9535","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p9536"}}},"roots":[{"type":"object","name":"Figure","id":"p9480","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p9482"},"y_range":{"type":"object","name":"Range1d","id":"p9489","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p9490"},"y_scale":{"type":"object","name":"LinearScale","id":"p9491"},"title":{"type":"object","name":"Title","id":"p9487","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p9525","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p9477","attributes":{"selected":{"type":"object","name":"Selection","id":"p9478","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p9479"},"data":{"type":"map","entries":[["year",[1987,1989,1990,1992,1993,1994,1996,2002,2003,2004,2005,2006,2007,2009,2010,2011,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,83.33333333333334,100.0,100.0,100.0,66.66666666666666,69.56521739130434,80.0,100.0,84.21052631578947,100.0,93.7062937062937,100.0,100.0,92.06349206349206,100.0,100.0,90.47619047619048,100.0,100.0,91.66666666666666,86.95652173913044,100.0]],["detected",[1,2,1,11,1,1,1,2,10,1,1,1,2,16,4,4,16,26,134,84,33,58,7,23,19,17,24,11,20,9]],["evaluable",[1,2,1,11,1,1,1,2,12,1,1,1,3,23,5,4,19,26,143,84,33,63,7,23,21,17,24,12,23,9]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,9.07684386569143,8.703135093227193,10.209683151927734,8.703135093227193,8.703135093227193,8.703135093227193,9.07684386569143,10.269703144398052,8.703135093227193,8.703135093227193,8.703135093227193,9.328625426046248,10.713966621835368,9.667366891029102,9.517227179437622,10.584573151575475,10.796415465069488,11.88589119348089,11.557772674175059,10.955310988645032,11.375828278421016,9.897626379762722,10.713966621835368,10.652487636092928,10.508782366508077,10.74264168206181,10.269703144398052,10.713966621835368,10.071067811865476]]]}}},"view":{"type":"object","name":"CDSView","id":"p9526","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p9527"}}},"glyph":{"type":"object","name":"Line","id":"p9522","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p9523","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p9524","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p9531","attributes":{"data_source":{"id":"p9477"},"view":{"type":"object","name":"CDSView","id":"p9532","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p9533"}}},"glyph":{"type":"object","name":"Scatter","id":"p9528","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p9529","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p9530","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p9488","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p9502"},{"type":"object","name":"BoxZoomTool","id":"p9503","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p9504","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p9510","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p9509","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p9511","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p9512"},{"type":"object","name":"SaveTool","id":"p9513"},{"type":"object","name":"HoverTool","id":"p9534","attributes":{"renderers":[{"id":"p9531"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p9497","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p9498","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p9499"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p9500"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p9492","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p9493","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p9494"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p9495"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p9496","attributes":{"axis":{"id":"p9492"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p9501","attributes":{"dimension":1,"axis":{"id":"p9497"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p9514","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p9516","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p9517","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p9518","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p9520","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p9519","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p9521","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"38959b33-8e90-421b-827f-e3c114615cb0","roots":{"p9480":"b981b4d3-cfce-425c-baac-b150c406911a"},"root_ids":["p9480"]}];
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

<div id="c57a259d-b8ea-4435-b040-41f7abb2c9f9" data-root-id="p9540" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"1fbf4163-fd0c-4692-8a7c-8e6bf5387e5a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p9580","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p9581"}}},"roots":[{"type":"object","name":"Figure","id":"p9540","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p9541"},"y_range":{"type":"object","name":"DataRange1d","id":"p9542","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p9549"},"y_scale":{"type":"object","name":"LinearScale","id":"p9550"},"title":{"type":"object","name":"Title","id":"p9547","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p9576","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p9537","attributes":{"selected":{"type":"object","name":"Selection","id":"p9538","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p9539"},"data":{"type":"map","entries":[["year",[1987,1989,1990,1992,1993,1994,1996,2002,2003,2004,2005,2006,2007,2009,2010,2011,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,2,1,11,1,1,1,2,12,1,1,1,3,23,5,4,19,26,143,84,33,63,7,23,21,17,24,12,23,9]],["detected",[1,2,1,11,1,1,1,2,10,1,1,1,2,16,4,4,16,26,134,84,33,58,7,23,19,17,24,11,20,9]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p9577","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p9578"}}},"glyph":{"type":"object","name":"VBar","id":"p9573","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p9574","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p9575","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p9548","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p9561"},{"type":"object","name":"BoxZoomTool","id":"p9562","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p9563","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p9569","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p9568","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p9570","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p9571"},{"type":"object","name":"SaveTool","id":"p9572"},{"type":"object","name":"HoverTool","id":"p9579","attributes":{"renderers":[{"id":"p9576"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p9556","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p9557","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p9558"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p9559"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p9551","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p9552","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p9553"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p9554"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p9555","attributes":{"axis":{"id":"p9551"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p9560","attributes":{"dimension":1,"axis":{"id":"p9556"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"1fbf4163-fd0c-4692-8a7c-8e6bf5387e5a","roots":{"p9540":"c57a259d-b8ea-4435-b040-41f7abb2c9f9"},"root_ids":["p9540"]}];
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

<div id="bf5d48c4-e26a-4bab-b284-c9a680cd6565" data-root-id="p9585" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"65b61d12-bc2f-437d-b975-d3a7ee7a77a2":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p9627","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p9628"}}},"roots":[{"type":"object","name":"Figure","id":"p9585","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p9587"},"y_range":{"type":"object","name":"FactorRange","id":"p9594","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p9595"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p9596"},"title":{"type":"object","name":"Title","id":"p9592","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p9622","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p9582","attributes":{"selected":{"type":"object","name":"Selection","id":"p9583","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p9584"},"data":{"type":"map","entries":[["x",[-21,-18,-12,-15,-18,-21,-15]],["y",["reverse","forward","reverse","forward","reverse","forward","reverse"]],["alpha",[0.30993031358885015,0.36324041811846686,0.2980836236933798,0.7127177700348433,0.9259581881533101,1.0,0.7719512195121951]],["pos",[21,18,12,15,18,21,15]],["base",["T","C","G","G","C","G","G"]],["n",[27,36,25,95,131,163,105]],["det_with",["33% of 27","69% of 36","76% of 25","80% of 95","82% of 131","88% of 163","92% of 105"]],["det_without",["99% of 566","98% of 557","97% of 568","99% of 498","100% of 462","99% of 430","97% of 488"]],["subs",["T&gt;C 16, T&gt;A 11","C&gt;T 35, C&gt;G 1","G&gt;A 23, G&gt;T 2","G&gt;A 68, G&gt;C 19, G&gt;T 8","C&gt;T 100, C&gt;A 22, C&gt;G 9","G&gt;C 153, G&gt;A 7, G&gt;T 3","G&gt;A 105"]],["zone",["no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p9623","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p9624"}}},"glyph":{"type":"object","name":"Rect","id":"p9619","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p9620","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p9621","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p9593","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p9607"},{"type":"object","name":"BoxZoomTool","id":"p9608","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p9609","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p9615","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p9614","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p9616","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p9617"},{"type":"object","name":"SaveTool","id":"p9618"},{"type":"object","name":"HoverTool","id":"p9625","attributes":{"renderers":[{"id":"p9622"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p9602","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p9603"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p9604"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p9605"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p9597","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p9626","attributes":{"ticks":[-21,-18,-15,-12],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p9599"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-21,"21"],[-18,"18"],[-12,"12"],[-15,"15"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p9600"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p9601","attributes":{"axis":{"id":"p9597"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p9606","attributes":{"dimension":1,"axis":{"id":"p9602"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"65b61d12-bc2f-437d-b975-d3a7ee7a77a2","roots":{"p9585":"bf5d48c4-e26a-4bab-b284-c9a680cd6565"},"root_ids":["p9585"]}];
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

Disclosures on this entry: `citation_is_indirect`.


## What reached the statistics

12,051 records were screened for this assay and **574 (5%)** were evaluable, meaning both primers landed in the right orientation and size range. 11,477 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 10,478 |
| `truncated` | 971 |
| `chance_anchor` | 28 |

