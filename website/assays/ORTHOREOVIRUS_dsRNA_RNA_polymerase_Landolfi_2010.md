# ORTHOREOVIRUS_dsRNA_RNA_polymerase_Landolfi_2010

<span class="aw-chip aw-chip-declining">declining</span>

**ORTHOREOVIRUS (dsRNA) — RNA polymerase**

| | |
|---|---|
| Target | Orthoreovirus ([taxid 10882](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10882)) |
| Gene | RNA polymerase |
| Chemistry | conventional |
| Amplicon | 163 bp |
| Designed | 2010 |
| Paper | [10.1177/104063871002200106](https://doi.org/10.1177/104063871002200106) |
| Registry status | active |

!!! quote "The paper"
    Landolfi JA et al. 2010. J Vet Diagn Invest 22:37-43

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GGBTCMACNGCYACYTCBACYGAGCA` | 26 nt |
| reverse | `CCRTCRTCWCCYTGRCAKACRTARTT` | 26 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 252 | 361 | 69.8% | 64.9% – 74.3% |
| baseline (everything earlier) | 591 | 671 | 88.1% | 85.4% – 90.3% |

Change from baseline, Newcombe interval: **-23.7% to -13.0%**. Threshold: **90.0%**.

*detected share 69.8% (65%-74%) since Oct 2024, upper bound below the 90% threshold; change from baseline -24% to -13%*

Trend across deposit years: by record falling (p=5.19e-07, 24 years); by footprint falling (p=0.0356). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="c7fb13d6-5309-4075-840c-ffb7d195e737" data-root-id="p21806" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9f75d36c-ebfc-416c-b1f8-f51afa5f5336":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p21861","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p21862"}}},"roots":[{"type":"object","name":"Figure","id":"p21806","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p21808"},"y_range":{"type":"object","name":"Range1d","id":"p21815","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p21816"},"y_scale":{"type":"object","name":"LinearScale","id":"p21817"},"title":{"type":"object","name":"Title","id":"p21813","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p21851","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p21803","attributes":{"selected":{"type":"object","name":"Selection","id":"p21804","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p21805"},"data":{"type":"map","entries":[["year",[1993,1994,2001,2005,2006,2007,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,71.42857142857143,80.0,100.0,100.0,63.63636363636363,90.625,79.16666666666666,94.44444444444444,93.93939393939394,84.375,94.07894736842105,96.66666666666667,84.78260869565217,76.38888888888889,85.85858585858585,68.01242236024845,85.29411764705883]],["detected",[1,2,1,1,2,1,6,5,8,29,15,21,29,19,17,31,27,143,58,39,55,85,219,29]],["evaluable",[1,2,1,1,2,1,6,7,10,29,15,33,32,24,18,33,32,152,60,46,72,99,322,34]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,9.07684386569143,8.703135093227193,8.703135093227193,9.07684386569143,8.703135093227193,9.791719296345839,9.897626379762722,10.143865699252444,10.869436534339137,10.423139468338052,10.955310988645032,10.934913263353746,10.74264168206181,10.547770533331066,10.955310988645032,10.934913263353746,11.922851885492664,11.34465373009984,11.173276359477448,11.460677957646856,11.660254037844386,12.366432781922773,10.975067467348278]]]}}},"view":{"type":"object","name":"CDSView","id":"p21852","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p21853"}}},"glyph":{"type":"object","name":"Line","id":"p21848","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p21849","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p21850","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p21857","attributes":{"data_source":{"id":"p21803"},"view":{"type":"object","name":"CDSView","id":"p21858","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p21859"}}},"glyph":{"type":"object","name":"Scatter","id":"p21854","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p21855","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p21856","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p21814","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p21828"},{"type":"object","name":"BoxZoomTool","id":"p21829","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p21830","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p21836","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p21835","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p21837","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p21838"},{"type":"object","name":"SaveTool","id":"p21839"},{"type":"object","name":"HoverTool","id":"p21860","attributes":{"renderers":[{"id":"p21857"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p21823","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p21824","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21825"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21826"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p21818","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p21819","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21820"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21821"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p21822","attributes":{"axis":{"id":"p21818"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p21827","attributes":{"dimension":1,"axis":{"id":"p21823"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p21840","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p21842","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p21843","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p21844","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p21846","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p21845","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p21847","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9f75d36c-ebfc-416c-b1f8-f51afa5f5336","roots":{"p21806":"c7fb13d6-5309-4075-840c-ffb7d195e737"},"root_ids":["p21806"]}];
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

<div id="b7bf3a83-9a03-4fe8-b826-b654589ad0b0" data-root-id="p21866" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"8608e646-7f89-4e0c-bb13-d9bf9885089b":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p21906","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p21907"}}},"roots":[{"type":"object","name":"Figure","id":"p21866","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p21867"},"y_range":{"type":"object","name":"DataRange1d","id":"p21868","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p21875"},"y_scale":{"type":"object","name":"LinearScale","id":"p21876"},"title":{"type":"object","name":"Title","id":"p21873","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p21902","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p21863","attributes":{"selected":{"type":"object","name":"Selection","id":"p21864","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p21865"},"data":{"type":"map","entries":[["year",[1993,1994,2001,2005,2006,2007,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,2,1,1,2,1,6,7,10,29,15,33,32,24,18,33,32,152,60,46,72,99,322,34]],["detected",[1,2,1,1,2,1,6,5,8,29,15,21,29,19,17,31,27,143,58,39,55,85,219,29]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p21903","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p21904"}}},"glyph":{"type":"object","name":"VBar","id":"p21899","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p21900","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p21901","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p21874","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p21887"},{"type":"object","name":"BoxZoomTool","id":"p21888","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p21889","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p21895","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p21894","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p21896","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p21897"},{"type":"object","name":"SaveTool","id":"p21898"},{"type":"object","name":"HoverTool","id":"p21905","attributes":{"renderers":[{"id":"p21902"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p21882","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p21883","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21884"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21885"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p21877","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p21878","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21879"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21880"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p21881","attributes":{"axis":{"id":"p21877"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p21886","attributes":{"dimension":1,"axis":{"id":"p21882"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"8608e646-7f89-4e0c-bb13-d9bf9885089b","roots":{"p21866":"b7bf3a83-9a03-4fe8-b826-b654589ad0b0"},"root_ids":["p21866"]}];
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

<div id="f4cd3d31-49aa-4e93-a4f3-86b8dfbe8a33" data-root-id="p21911" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"282542d5-645a-45e4-9699-5bfa5332ae29":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p21953","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p21954"}}},"roots":[{"type":"object","name":"Figure","id":"p21911","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p21913"},"y_range":{"type":"object","name":"FactorRange","id":"p21920","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p21921"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p21922"},"title":{"type":"object","name":"Title","id":"p21918","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p21948","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p21908","attributes":{"selected":{"type":"object","name":"Selection","id":"p21909","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p21910"},"data":{"type":"map","entries":[["x",[-15,-12,-6,-21,-9,-9,-18,-3,-24]],["y",["forward","forward","forward","forward","reverse","forward","reverse","forward","forward"]],["alpha",[1.0,1.0,1.0,1.0,1.0,0.23895348837209301,0.3377906976744186,1.0,0.5091085271317829]],["pos",[15,12,6,21,9,9,18,3,24]],["base",["Y","Y","Y","M","K","B","W","G","B"]],["n",[283,340,616,633,838,27,57,610,109]],["det_with",["37% of 283","47% of 340","70% of 616","72% of 633","79% of 838","67% of 27","81% of 57","83% of 610","93% of 109"]],["det_without",["99% of 750","99% of 693","99% of 417","98% of 400","96% of 195","82% of 1006","82% of 976","81% of 423","81% of 924"]],["subs",["Y&gt;G 267, Y&gt;A 16","Y&gt;A 173, Y&gt;G 167","Y&gt;G 489, Y&gt;A 127","M&gt;T 417, M&gt;G 216","K&gt;A 489, K&gt;C 349","B&gt;A 27","W&gt;G 35, W&gt;C 22","G&gt;A 610","B&gt;A 109"]],["zone",["no","no","no","no","no","no","no","yes","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p21949","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p21950"}}},"glyph":{"type":"object","name":"Rect","id":"p21945","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p21946","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p21947","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p21919","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p21933"},{"type":"object","name":"BoxZoomTool","id":"p21934","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p21935","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p21941","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p21940","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p21942","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p21943"},{"type":"object","name":"SaveTool","id":"p21944"},{"type":"object","name":"HoverTool","id":"p21951","attributes":{"renderers":[{"id":"p21948"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p21928","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p21929"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p21930"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21931"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p21923","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p21952","attributes":{"ticks":[-24,-21,-18,-15,-12,-9,-6,-3],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21925"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-15,"15"],[-12,"12"],[-6,"6"],[-21,"21"],[-9,"9"],[-18,"18"],[-3,"3"],[-24,"24"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p21926"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p21927","attributes":{"axis":{"id":"p21923"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p21932","attributes":{"dimension":1,"axis":{"id":"p21928"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"282542d5-645a-45e4-9699-5bfa5332ae29","roots":{"p21911":"f4cd3d31-49aa-4e93-a4f3-86b8dfbe8a33"},"root_ids":["p21911"]}];
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

<div id="c35249e3-eede-4a11-807d-cdd28f61dd6e" data-root-id="p21958" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"dbbd7298-ae63-4470-99e0-ad66901ed1d5":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p22007","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p22008"}}},"roots":[{"type":"object","name":"Figure","id":"p21958","attributes":{"height":132,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p21967","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p21968","attributes":{"factors":["Orthoreovirus avis (3431493)","Orthoreovirus piscis (3431498)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p21969"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p21970"},"title":{"type":"object","name":"Title","id":"p21965","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p22002","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p21955","attributes":{"selected":{"type":"object","name":"Selection","id":"p21956","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p21957"},"data":{"type":"map","entries":[["y",["Orthoreovirus avis (3431493)","Orthoreovirus piscis (3431498)"]],["share",[25.694444444444443,100.0]],["lo",[19.254368321773864,97.9329376528407]],["hi",[33.39761403934598,100.0]],["n",[144,182]],["det",[37,182]],["colour",["#b3261e","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p22003","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p22004"}}},"glyph":{"type":"object","name":"Scatter","id":"p21999","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p22000","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p22001","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p21966","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p21981"},{"type":"object","name":"BoxZoomTool","id":"p21982","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p21983","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p21989","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p21988","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p21990","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p21991"},{"type":"object","name":"SaveTool","id":"p21992"},{"type":"object","name":"HoverTool","id":"p22006","attributes":{"renderers":[{"id":"p22002"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p21976","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p21977"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p21978"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21979"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p21971","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p21972","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21973"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21974"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p21975","attributes":{"axis":{"id":"p21971"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p21980","attributes":{"dimension":1,"axis":{"id":"p21976"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p21993","attributes":{"source":{"id":"p21955"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p22005","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"dbbd7298-ae63-4470-99e0-ad66901ed1d5","roots":{"p21958":"c35249e3-eede-4a11-807d-cdd28f61dd6e"},"root_ids":["p21958"]}];
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

Disclosures on this entry: `conditions_not_printed`.


## What reached the statistics

14,479 records were screened for this assay and **1,032 (7%)** were evaluable, meaning both primers landed in the right orientation and size range. 13,447 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 13,154 |
| `chance_anchor` | 219 |
| `truncated` | 74 |

