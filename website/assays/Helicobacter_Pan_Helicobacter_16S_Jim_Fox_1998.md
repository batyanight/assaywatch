# Helicobacter_Pan_Helicobacter_16S_Jim_Fox_1998

<span class="aw-chip aw-chip-stable">stable</span>

**Helicobacter — Pan Helicobacter 16S (Jim Fox)**

| | |
|---|---|
| Target | Helicobacter ([taxid 209](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=209)) |
| Gene | Pan Helicobacter 16S (Jim Fox) |
| Chemistry | conventional |
| Amplicon | 1196 bp |
| Designed | 1998 |
| Paper | [10.1016/S0016-5085(98)70589-X](https://doi.org/10.1016/S0016-5085(98)70589-X) |
| Registry status | active |

!!! quote "The paper"
    Fox JG et al. 1998. Gastroenterology 114:755-763

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GCTATGACGGGTATCC` | 16 nt |
| reverse | `ACTTCACCCCAGTCGCTG` | 18 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 48 | 51 | 94.1% | 84.1% – 98.0% |
| baseline (everything earlier) | 431 | 484 | 89.0% | 86.0% – 91.5% |

Change from baseline, Newcombe interval: **-5.3% to 10.0%**. Threshold: **90.0%**.

*detected share 94.1% (84%-98%) since Oct 2024*

Trend across deposit years: by record falling (p=0.0126, 32 years); by footprint falling (p=0.274). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="b8096125-d2fd-4951-9bcc-462293a7ccc7" data-root-id="p13591" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b43bf293-7528-4b17-83d0-0ce905283c53":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p13646","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p13647"}}},"roots":[{"type":"object","name":"Figure","id":"p13591","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p13593"},"y_range":{"type":"object","name":"Range1d","id":"p13600","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p13601"},"y_scale":{"type":"object","name":"LinearScale","id":"p13602"},"title":{"type":"object","name":"Title","id":"p13598","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p13636","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p13588","attributes":{"selected":{"type":"object","name":"Selection","id":"p13589","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p13590"},"data":{"type":"map","entries":[["year",[1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2013,2014,2015,2016,2017,2018,2019,2020,2022,2023,2024,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,94.73684210526315,100.0,100.0,85.71428571428571,96.0,96.7741935483871,100.0,92.85714285714286,100.0,100.0,100.0,100.0,100.0,33.33333333333333,100.0,100.0,100.0,100.0,88.88888888888889,100.0,100.0,100.0,100.0,93.75]],["detected",[1,20,4,2,1,2,8,6,18,29,29,12,24,30,16,13,11,24,13,16,14,23,17,7,13,7,8,10,13,33,10,45]],["evaluable",[1,20,4,2,1,2,8,6,19,29,29,14,25,31,16,14,11,24,13,16,14,69,17,7,13,7,9,10,13,33,10,48]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent"]],["size",[8.703135093227193,10.619414831097462,9.517227179437622,9.07684386569143,8.703135093227193,9.07684386569143,9.989711205477885,9.791719296345839,10.584573151575475,10.869436534339137,10.869436534339137,10.37579022724969,10.770092258092593,10.913832791890265,10.467343773689333,10.37579022724969,10.209683151927734,10.74264168206181,10.324834530005162,10.467343773689333,10.37579022724969,11.433709207718536,10.508782366508077,9.897626379762722,10.324834530005162,9.897626379762722,10.071067811865476,10.143865699252444,10.324834530005162,10.955310988645032,10.143865699252444,11.200908608240482]]]}}},"view":{"type":"object","name":"CDSView","id":"p13637","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13638"}}},"glyph":{"type":"object","name":"Line","id":"p13633","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p13634","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p13635","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p13642","attributes":{"data_source":{"id":"p13588"},"view":{"type":"object","name":"CDSView","id":"p13643","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13644"}}},"glyph":{"type":"object","name":"Scatter","id":"p13639","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p13640","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p13641","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p13599","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p13613"},{"type":"object","name":"BoxZoomTool","id":"p13614","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p13615","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p13621","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13620","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p13622","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p13623"},{"type":"object","name":"SaveTool","id":"p13624"},{"type":"object","name":"HoverTool","id":"p13645","attributes":{"renderers":[{"id":"p13642"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p13608","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13609","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13610"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13611"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p13603","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13604","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13605"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13606"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p13607","attributes":{"axis":{"id":"p13603"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p13612","attributes":{"dimension":1,"axis":{"id":"p13608"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p13625","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p13627","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p13628","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p13629","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p13631","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13630","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p13632","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b43bf293-7528-4b17-83d0-0ce905283c53","roots":{"p13591":"b8096125-d2fd-4951-9bcc-462293a7ccc7"},"root_ids":["p13591"]}];
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

<div id="cbcaff1a-e32f-42fb-842e-dc351477827d" data-root-id="p13651" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9dcf24b0-8e22-4eec-a923-e3506e55331a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p13691","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p13692"}}},"roots":[{"type":"object","name":"Figure","id":"p13651","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p13652"},"y_range":{"type":"object","name":"DataRange1d","id":"p13653","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p13660"},"y_scale":{"type":"object","name":"LinearScale","id":"p13661"},"title":{"type":"object","name":"Title","id":"p13658","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p13687","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p13648","attributes":{"selected":{"type":"object","name":"Selection","id":"p13649","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p13650"},"data":{"type":"map","entries":[["year",[1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2013,2014,2015,2016,2017,2018,2019,2020,2022,2023,2024,2026]],["evaluable",[1,20,4,2,1,2,8,6,19,29,29,14,25,31,16,14,11,24,13,16,14,69,17,7,13,7,9,10,13,33,10,48]],["detected",[1,20,4,2,1,2,8,6,18,29,29,12,24,30,16,13,11,24,13,16,14,23,17,7,13,7,8,10,13,33,10,45]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p13688","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13689"}}},"glyph":{"type":"object","name":"VBar","id":"p13684","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p13685","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p13686","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p13659","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p13672"},{"type":"object","name":"BoxZoomTool","id":"p13673","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p13674","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p13680","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13679","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p13681","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p13682"},{"type":"object","name":"SaveTool","id":"p13683"},{"type":"object","name":"HoverTool","id":"p13690","attributes":{"renderers":[{"id":"p13687"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p13667","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13668","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13669"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13670"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p13662","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13663","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13664"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13665"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p13666","attributes":{"axis":{"id":"p13662"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p13671","attributes":{"dimension":1,"axis":{"id":"p13667"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9dcf24b0-8e22-4eec-a923-e3506e55331a","roots":{"p13651":"cbcaff1a-e32f-42fb-842e-dc351477827d"},"root_ids":["p13651"]}];
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

<div id="fa50e783-c29d-4e6b-b5a3-0730aa9621f3" data-root-id="p13696" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"90d81ce5-5f71-41e6-9ada-220eac09c7ba":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p13738","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p13739"}}},"roots":[{"type":"object","name":"Figure","id":"p13696","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p13698"},"y_range":{"type":"object","name":"FactorRange","id":"p13705","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p13706"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p13707"},"title":{"type":"object","name":"Title","id":"p13703","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p13733","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p13693","attributes":{"selected":{"type":"object","name":"Selection","id":"p13694","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p13695"},"data":{"type":"map","entries":[["x",[-1,-5,-3,-4,-12,-14,-14]],["y",["forward","reverse","reverse","reverse","reverse","reverse","forward"]],["alpha",[0.4741121495327103,0.4423364485981308,0.46775700934579434,0.46775700934579434,0.48046728971962616,0.5376635514018692,0.32794392523364485]],["pos",[1,5,3,4,12,14,14]],["base",["C","C","C","G","C","C","T"]],["n",[51,46,50,50,52,61,28]],["det_with",["0% of 51","0% of 46","2% of 50","2% of 50","12% of 52","25% of 61","82% of 28"]],["det_without",["99% of 482","98% of 487","99% of 483","99% of 483","98% of 481","98% of 472","90% of 505"]],["subs",["C&gt;T 49, C&gt;G 2","C&gt;T 46","C&gt;T 49, C&gt;G 1","G&gt;A 49, G&gt;T 1","C&gt;G 45, C&gt;T 6, C&gt;A 1","C&gt;A 58, C&gt;T 2, C&gt;G 1","T&gt;A 22, T&gt;G 3, T&gt;C 2, T&gt;R 1"]],["zone",["yes","yes","yes","yes","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p13734","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13735"}}},"glyph":{"type":"object","name":"Rect","id":"p13730","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p13731","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p13732","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p13704","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p13718"},{"type":"object","name":"BoxZoomTool","id":"p13719","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p13720","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p13726","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13725","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p13727","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p13728"},{"type":"object","name":"SaveTool","id":"p13729"},{"type":"object","name":"HoverTool","id":"p13736","attributes":{"renderers":[{"id":"p13733"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p13713","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p13714"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p13715"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13716"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p13708","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p13737","attributes":{"ticks":[-14,-12,-5,-4,-3,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13710"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-1,"1"],[-5,"5"],[-3,"3"],[-4,"4"],[-12,"12"],[-14,"14"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p13711"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p13712","attributes":{"axis":{"id":"p13708"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p13717","attributes":{"dimension":1,"axis":{"id":"p13713"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"90d81ce5-5f71-41e6-9ada-220eac09c7ba","roots":{"p13696":"fa50e783-c29d-4e6b-b5a3-0730aa9621f3"},"root_ids":["p13696"]}];
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


## By lineage

A single pooled percentage hides the clade you may actually care about:
published misses are nearly always specific to one lineage, and a clade that is
5% of deposits can be 100% of the cases in one region. Lineages with too few
records to say anything are left out.

<div id="d9ca3863-d127-42e4-988c-3a36fa4a2ff5" data-root-id="p13743" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"f18cd671-2c3a-4e08-899d-add40164e8a2":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p13792","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p13793"}}},"roots":[{"type":"object","name":"Figure","id":"p13743","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p13752","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p13753","attributes":{"factors":["Helicobacter pylori (210)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p13754"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p13755"},"title":{"type":"object","name":"Title","id":"p13750","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p13787","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p13740","attributes":{"selected":{"type":"object","name":"Selection","id":"p13741","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p13742"},"data":{"type":"map","entries":[["y",["Helicobacter pylori (210)"]],["share",[93.47826086956522]],["lo",[82.49725891809578]],["hi",[97.75721385707115]],["n",[46]],["det",[43]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p13788","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13789"}}},"glyph":{"type":"object","name":"Scatter","id":"p13784","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p13785","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p13786","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p13751","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p13766"},{"type":"object","name":"BoxZoomTool","id":"p13767","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p13768","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p13774","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13773","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p13775","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p13776"},{"type":"object","name":"SaveTool","id":"p13777"},{"type":"object","name":"HoverTool","id":"p13791","attributes":{"renderers":[{"id":"p13787"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p13761","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p13762"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p13763"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13764"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p13756","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13757","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13758"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13759"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p13760","attributes":{"axis":{"id":"p13756"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p13765","attributes":{"dimension":1,"axis":{"id":"p13761"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p13778","attributes":{"source":{"id":"p13740"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p13790","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"f18cd671-2c3a-4e08-899d-add40164e8a2","roots":{"p13743":"d9ca3863-d127-42e4-988c-3a36fa4a2ff5"},"root_ids":["p13743"]}];
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
("16S ribosomal RNA"[Title] OR "16S rRNA"[Title] OR 16S[Title]) AND 1:30000[SLEN] NOT "whole genome shotgun"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `amplicon_measured_not_published`, `orientation_inferred`.


## What reached the statistics

3,025 records were screened for this assay and **535 (18%)** were evaluable, meaning both primers landed in the right orientation and size range. 2,490 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 1,419 |
| `truncated` | 1,057 |
| `chance_anchor` | 13 |

