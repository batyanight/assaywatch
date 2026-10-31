# ORTHOBUNYAVIRUS_ssRNA_S_segment

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**ORTHOBUNYAVIRUS (ssRNA) — S segment (PREDICT P-022)**

| | |
|---|---|
| Target | Orthobunyavirus ([taxid 11572](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11572)) |
| Gene | S segment |
| Chemistry | conventional |
| Amplicon | — |
| Designed | 2007 |
| Paper | [10.1007/s00705-007-1069-z](https://doi.org/10.1007/s00705-007-1069-z) |
| Registry status | active |

!!! quote "The paper"
    Briese, T., Kapoor, V. & Lipkin, W. I. Natural M-segment reassortment in Potosi and Main Drain viruses: implications for the evolution of orthobunyaviruses. Archives of Virology 152, 2237-2247 (2007).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CGGCGCCAGTAGTGTACTCCAC` | 22 nt |
| reverse | `GCGGCCAGTAGTGTGCTCCAC` | 21 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (48 months, from Oct 2022) | 4 | 15 | 26.7% | 10.9% – 52.0% |
| baseline (everything earlier) | 60 | 166 | 36.1% | 29.2% – 43.7% |

Change from baseline, Newcombe interval: **-27.0% to 16.7%**. Threshold: **90.0%**.

*detected share 26.7% (11%-52%) since Oct 2022, upper bound below the 90% threshold; change from baseline -27% to +17% (no measurable fall from a baseline of 36%) (window widened to 48 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=0.0074, 26 years); by footprint falling (p=0.228). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="fb060abf-915d-4391-a85b-a2fdfae3390b" data-root-id="p21448" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b24a7321-6495-4531-8e34-eb08783a765f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p21503","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p21504"}}},"roots":[{"type":"object","name":"Figure","id":"p21448","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p21450"},"y_range":{"type":"object","name":"Range1d","id":"p21457","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p21458"},"y_scale":{"type":"object","name":"LinearScale","id":"p21459"},"title":{"type":"object","name":"Title","id":"p21455","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p21493","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p21445","attributes":{"selected":{"type":"object","name":"Selection","id":"p21446","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p21447"},"data":{"type":"map","entries":[["year",[1989,1993,1995,1996,1998,2002,2003,2004,2007,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]],["share",[0.0,66.66666666666666,0.0,100.0,0.0,33.33333333333333,0.0,66.66666666666666,16.666666666666664,70.0,50.0,100.0,40.0,50.0,42.857142857142854,10.0,50.0,0.0,23.52941176470588,15.384615384615385,42.857142857142854,0.0,0.0,50.0,0.0,0.0]],["detected",[0,2,0,7,0,3,0,2,2,7,1,4,2,4,6,1,10,0,4,2,3,0,0,4,0,0]],["evaluable",[1,3,2,7,3,9,1,3,12,10,2,4,5,8,14,10,20,7,17,13,7,6,4,8,1,4]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent"]],["size",[8.703135093227193,9.328625426046248,9.07684386569143,9.897626379762722,9.328625426046248,10.071067811865476,8.703135093227193,9.328625426046248,10.269703144398052,10.143865699252444,9.07684386569143,9.517227179437622,9.667366891029102,9.989711205477885,10.37579022724969,10.143865699252444,10.619414831097462,9.897626379762722,10.508782366508077,10.324834530005162,9.897626379762722,9.791719296345839,9.517227179437622,9.989711205477885,8.703135093227193,9.517227179437622]]]}}},"view":{"type":"object","name":"CDSView","id":"p21494","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p21495"}}},"glyph":{"type":"object","name":"Line","id":"p21490","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p21491","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p21492","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p21499","attributes":{"data_source":{"id":"p21445"},"view":{"type":"object","name":"CDSView","id":"p21500","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p21501"}}},"glyph":{"type":"object","name":"Scatter","id":"p21496","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p21497","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p21498","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p21456","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p21470"},{"type":"object","name":"BoxZoomTool","id":"p21471","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p21472","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p21478","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p21477","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p21479","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p21480"},{"type":"object","name":"SaveTool","id":"p21481"},{"type":"object","name":"HoverTool","id":"p21502","attributes":{"renderers":[{"id":"p21499"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p21465","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p21466","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21467"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21468"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p21460","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p21461","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21462"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21463"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p21464","attributes":{"axis":{"id":"p21460"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p21469","attributes":{"dimension":1,"axis":{"id":"p21465"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p21482","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2021.5,"right":{"type":"object","name":"Node","id":"p21484","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p21485","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p21486","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p21488","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p21487","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p21489","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b24a7321-6495-4531-8e34-eb08783a765f","roots":{"p21448":"fb060abf-915d-4391-a85b-a2fdfae3390b"},"root_ids":["p21448"]}];
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

<div id="d0039513-f593-4886-a2c0-16657cc38240" data-root-id="p21508" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"3021374d-ef86-4e1e-ad31-9f527405fec4":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p21548","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p21549"}}},"roots":[{"type":"object","name":"Figure","id":"p21508","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p21509"},"y_range":{"type":"object","name":"DataRange1d","id":"p21510","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p21517"},"y_scale":{"type":"object","name":"LinearScale","id":"p21518"},"title":{"type":"object","name":"Title","id":"p21515","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p21544","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p21505","attributes":{"selected":{"type":"object","name":"Selection","id":"p21506","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p21507"},"data":{"type":"map","entries":[["year",[1989,1993,1995,1996,1998,2002,2003,2004,2007,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]],["evaluable",[1,3,2,7,3,9,1,3,12,10,2,4,5,8,14,10,20,7,17,13,7,6,4,8,1,4]],["detected",[0,2,0,7,0,3,0,2,2,7,1,4,2,4,6,1,10,0,4,2,3,0,0,4,0,0]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p21545","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p21546"}}},"glyph":{"type":"object","name":"VBar","id":"p21541","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p21542","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p21543","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p21516","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p21529"},{"type":"object","name":"BoxZoomTool","id":"p21530","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p21531","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p21537","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p21536","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p21538","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p21539"},{"type":"object","name":"SaveTool","id":"p21540"},{"type":"object","name":"HoverTool","id":"p21547","attributes":{"renderers":[{"id":"p21544"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p21524","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p21525","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21526"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21527"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p21519","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p21520","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21521"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21522"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p21523","attributes":{"axis":{"id":"p21519"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p21528","attributes":{"dimension":1,"axis":{"id":"p21524"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"3021374d-ef86-4e1e-ad31-9f527405fec4","roots":{"p21508":"d0039513-f593-4886-a2c0-16657cc38240"},"root_ids":["p21508"]}];
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

<div id="c69d32d7-48bd-4a13-a0f0-f31133de56a2" data-root-id="p21553" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9ea3a165-1c70-4e71-8134-5de7850f14d8":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p21595","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p21596"}}},"roots":[{"type":"object","name":"Figure","id":"p21553","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p21555"},"y_range":{"type":"object","name":"FactorRange","id":"p21562","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p21563"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p21564"},"title":{"type":"object","name":"Title","id":"p21560","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p21590","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p21550","attributes":{"selected":{"type":"object","name":"Selection","id":"p21551","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p21552"},"data":{"type":"map","entries":[["x",[-2,-4,-1,-1,-2,-9,-3,-6,-5,-13,-12,-11,-11,-15,-7,-14,-15,-7]],["y",["forward","reverse","reverse","forward","reverse","reverse","reverse","reverse","reverse","reverse","reverse","forward","reverse","forward","forward","reverse","reverse","reverse"]],["alpha",[1.0,1.0,0.9953038674033149,0.9201657458563536,1.0,0.5820441988950277,0.5632596685082872,0.5632596685082872,0.6008287292817679,0.6196132596685083,0.8262430939226519,0.7323204419889503,1.0,0.769889502762431,0.657182320441989,1.0,0.9013812154696133,1.0]],["pos",[2,4,1,1,2,9,3,6,5,13,12,11,11,15,7,14,15,7]],["base",["A","C","C","C","A","G","C","C","T","T","A","G","G","A","A","G","A","G"]],["n",[50,48,45,41,47,23,22,22,24,25,36,31,60,33,27,48,40,54]],["det_with",["0% of 50","0% of 48","0% of 45","0% of 41","2% of 47","0% of 23","0% of 22","0% of 22","4% of 24","8% of 25","14% of 36","16% of 31","23% of 60","21% of 33","22% of 27","29% of 48","35% of 40","37% of 54"]],["det_without",["49% of 131","48% of 133","47% of 136","46% of 140","47% of 134","41% of 158","40% of 159","40% of 159","40% of 157","40% of 156","41% of 145","39% of 150","41% of 121","39% of 148","38% of 154","38% of 133","35% of 141","35% of 127"]],["subs",["A&gt;T 20, A&gt;C 18, A&gt;G 12","C&gt;A 22, C&gt;T 17, C&gt;G 9","C&gt;A 31, C&gt;G 8, C&gt;T 6","C&gt;T 20, C&gt;A 16, C&gt;G 5","A&gt;C 28, A&gt;T 13, A&gt;G 6","G&gt;A 9, G&gt;T 8, G&gt;C 6","C&gt;A 13, C&gt;G 9","C&gt;T 17, C&gt;G 4, C&gt;A 1","T&gt;C 20, T&gt;A 4","T&gt;C 11, T&gt;A 9, T&gt;G 5","A&gt;C 13, A&gt;G 12, A&gt;T 11","G&gt;T 20, G&gt;A 6, G&gt;C 5","G&gt;C 29, G&gt;T 18, G&gt;A 13","A&gt;G 16, A&gt;T 12, A&gt;C 5","A&gt;T 15, A&gt;G 11, A&gt;C 1","G&gt;A 24, G&gt;T 19, G&gt;C 5","A&gt;T 16, A&gt;C 15, A&gt;G 9","G&gt;A 25, G&gt;T 22, G&gt;C 7"]],["zone",["yes","yes","yes","yes","yes","no","yes","no","yes","no","no","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p21591","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p21592"}}},"glyph":{"type":"object","name":"Rect","id":"p21587","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p21588","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p21589","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p21561","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p21575"},{"type":"object","name":"BoxZoomTool","id":"p21576","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p21577","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p21583","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p21582","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p21584","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p21585"},{"type":"object","name":"SaveTool","id":"p21586"},{"type":"object","name":"HoverTool","id":"p21593","attributes":{"renderers":[{"id":"p21590"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p21570","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p21571"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p21572"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21573"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p21565","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p21594","attributes":{"ticks":[-15,-14,-13,-12,-11,-9,-7,-6,-5,-4,-3,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21567"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-2,"2"],[-4,"4"],[-1,"1"],[-9,"9"],[-3,"3"],[-6,"6"],[-5,"5"],[-13,"13"],[-12,"12"],[-11,"11"],[-15,"15"],[-7,"7"],[-14,"14"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p21568"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p21569","attributes":{"axis":{"id":"p21565"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p21574","attributes":{"dimension":1,"axis":{"id":"p21570"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9ea3a165-1c70-4e71-8134-5de7850f14d8","roots":{"p21553":"c69d32d7-48bd-4a13-a0f0-f31133de56a2"},"root_ids":["p21553"]}];
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
S[Gene] OR M[Gene] OR "S segment"[Title] OR "M segment"[Title] OR nucleocapsid[Title] OR glycoprotein[Title] OR "complete genome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `amplicon_multimodal`.


## What reached the statistics

2,083 records were screened for this assay and **181 (9%)** were evaluable, meaning both primers landed in the right orientation and size range. 1,902 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `chance_only` | 1,209 |
| `no_site` | 685 |
| `no_pair` | 5 |
| `chance_anchor` | 3 |

