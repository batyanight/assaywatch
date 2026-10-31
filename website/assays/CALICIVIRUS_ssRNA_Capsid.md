# CALICIVIRUS_ssRNA_Capsid

<span class="aw-chip aw-chip-no-recent-data">no recent data</span>

**CALICIVIRUS (ssRNA) — capsid-coding region (PREDICT P-024)**

| | |
|---|---|
| Target | Caliciviridae ([taxid 11974](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11974)) |
| Gene | Capsid-coding region |
| Chemistry | conventional |
| Amplicon | 768 bp |
| Designed | 1999 |
| Paper | [10.1016/S0166-0934(99)00088-9](https://doi.org/10.1016/S0166-0934(99)00088-9) |
| Registry status | active |

!!! quote "The paper"
    Reid, S. M. et al. Development of a reverse transcription polymerase chain reaction procedure for the detection of marine caliciviruses with potential application for nucleotide sequencing. Journal of Virological Methods 82, 99-107 (1999).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GTGAGGTGTTTGAGAATTAG` | 20 nt |
| reverse | `ACATCAATTCCGCCAGACCA` | 20 nt |

## The verdict, and the numbers behind it

**no recent data** — nothing was deposited in the window

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 0 | 0 | — | 0.0% – 100.0% |
| baseline (everything earlier) | 11 | 11 | 100.0% | 74.1% – 100.0% |

Change from baseline, Newcombe interval: **-100.0% to 100.0%**. Threshold: **90.0%**.

*no evaluable records deposited since Oct 2024*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="e2cb5ecc-d1ea-4146-aaaf-3ec299f2077c" data-root-id="p5885" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"336edde0-06d1-4bd3-a030-daab72dc2003":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p5933","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p5934"}}},"roots":[{"type":"object","name":"Figure","id":"p5885","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p5887"},"y_range":{"type":"object","name":"Range1d","id":"p5894","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p5895"},"y_scale":{"type":"object","name":"LinearScale","id":"p5896"},"title":{"type":"object","name":"Title","id":"p5892","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p5923","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p5882","attributes":{"selected":{"type":"object","name":"Selection","id":"p5883","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p5884"},"data":{"type":"map","entries":[["year",[1993,1994,1997,1998,2000,2003,2012,2014]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[2,1,3,1,1,1,1,1]],["evaluable",[2,1,3,1,1,1,1,1]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline"]],["size",[9.07684386569143,8.703135093227193,9.328625426046248,8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193]]]}}},"view":{"type":"object","name":"CDSView","id":"p5924","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p5925"}}},"glyph":{"type":"object","name":"Line","id":"p5920","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p5921","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p5922","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p5929","attributes":{"data_source":{"id":"p5882"},"view":{"type":"object","name":"CDSView","id":"p5930","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p5931"}}},"glyph":{"type":"object","name":"Scatter","id":"p5926","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p5927","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p5928","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p5893","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p5907"},{"type":"object","name":"BoxZoomTool","id":"p5908","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p5909","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p5915","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p5914","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p5916","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p5917"},{"type":"object","name":"SaveTool","id":"p5918"},{"type":"object","name":"HoverTool","id":"p5932","attributes":{"renderers":[{"id":"p5929"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p5902","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p5903","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5904"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5905"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p5897","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p5898","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5899"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5900"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p5901","attributes":{"axis":{"id":"p5897"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p5906","attributes":{"dimension":1,"axis":{"id":"p5902"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"Span","id":"p5919","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"336edde0-06d1-4bd3-a030-daab72dc2003","roots":{"p5885":"e2cb5ecc-d1ea-4146-aaaf-3ec299f2077c"},"root_ids":["p5885"]}];
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

<div id="bcd84778-3ccb-4fa2-8d6b-5580f587ca51" data-root-id="p5938" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"6baa7942-d2c1-4d5e-bc49-982735d83bfb":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p5978","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p5979"}}},"roots":[{"type":"object","name":"Figure","id":"p5938","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p5939"},"y_range":{"type":"object","name":"DataRange1d","id":"p5940","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p5947"},"y_scale":{"type":"object","name":"LinearScale","id":"p5948"},"title":{"type":"object","name":"Title","id":"p5945","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p5974","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p5935","attributes":{"selected":{"type":"object","name":"Selection","id":"p5936","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p5937"},"data":{"type":"map","entries":[["year",[1993,1994,1997,1998,2000,2003,2012,2014]],["evaluable",[2,1,3,1,1,1,1,1]],["detected",[2,1,3,1,1,1,1,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p5975","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p5976"}}},"glyph":{"type":"object","name":"VBar","id":"p5971","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p5972","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p5973","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p5946","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p5959"},{"type":"object","name":"BoxZoomTool","id":"p5960","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p5961","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p5967","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p5966","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p5968","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p5969"},{"type":"object","name":"SaveTool","id":"p5970"},{"type":"object","name":"HoverTool","id":"p5977","attributes":{"renderers":[{"id":"p5974"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p5954","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p5955","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5956"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5957"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p5949","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p5950","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5951"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5952"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p5953","attributes":{"axis":{"id":"p5949"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p5958","attributes":{"dimension":1,"axis":{"id":"p5954"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"6baa7942-d2c1-4d5e-bc49-982735d83bfb","roots":{"p5938":"bcd84778-3ccb-4fa2-8d6b-5580f587ca51"},"root_ids":["p5938"]}];
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

<div id="bfd58359-b9eb-4c1b-8b66-9507ecd34bb0" data-root-id="p5983" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"1e67e149-ba2f-482d-973c-c85ccec456d8":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p6025","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p6026"}}},"roots":[{"type":"object","name":"Figure","id":"p5983","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p5985"},"y_range":{"type":"object","name":"FactorRange","id":"p5992","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p5993"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p5994"},"title":{"type":"object","name":"Title","id":"p5990","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p6020","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p5980","attributes":{"selected":{"type":"object","name":"Selection","id":"p5981","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p5982"},"data":{"type":"map","entries":[["x",[-10,-17,-20,-16,-3,-11,-4,-5,-9,-18,-12,-15]],["y",["reverse","forward","forward","forward","forward","reverse","forward","reverse","reverse","forward","reverse","reverse"]],["alpha",[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]],["pos",[10,17,20,16,3,11,4,5,9,18,12,15]],["base",["C","A","G","G","T","C","T","G","G","G","T","A"]],["n",[30,28,26,23,22,22,21,21,27,24,50,33]],["det_with",["0% of 30","0% of 28","0% of 26","0% of 23","0% of 22","0% of 22","0% of 21","0% of 21","4% of 27","4% of 24","22% of 50","36% of 33"]],["det_without",["46% of 37","44% of 39","41% of 41","39% of 44","38% of 45","38% of 45","37% of 46","37% of 46","40% of 40","37% of 43","35% of 17","15% of 34"]],["subs",["C&gt;A 19, C&gt;T 10, C&gt;G 1","A&gt;C 17, A&gt;T 10, A&gt;G 1","G&gt;A 19, G&gt;C 5, G&gt;T 2","G&gt;A 12, G&gt;T 9, G&gt;C 2","T&gt;G 13, T&gt;A 8, T&gt;C 1","C&gt;G 21, C&gt;A 1","T&gt;C 17, T&gt;G 4","G&gt;T 14, G&gt;C 6, G&gt;A 1","G&gt;C 18, G&gt;A 5, G&gt;T 4","G&gt;A 13, G&gt;T 9, G&gt;C 2","T&gt;G 19, T&gt;C 19, T&gt;A 12","A&gt;G 19, A&gt;C 7, A&gt;T 7"]],["zone",["no","no","no","no","yes","no","yes","yes","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p6021","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p6022"}}},"glyph":{"type":"object","name":"Rect","id":"p6017","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p6018","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p6019","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p5991","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p6005"},{"type":"object","name":"BoxZoomTool","id":"p6006","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p6007","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p6013","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p6012","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p6014","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p6015"},{"type":"object","name":"SaveTool","id":"p6016"},{"type":"object","name":"HoverTool","id":"p6023","attributes":{"renderers":[{"id":"p6020"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p6000","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p6001"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p6002"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p6003"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p5995","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p6024","attributes":{"ticks":[-20,-18,-17,-16,-15,-12,-11,-10,-9,-5,-4,-3],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5997"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-10,"10"],[-17,"17"],[-20,"20"],[-16,"16"],[-3,"3"],[-11,"11"],[-4,"4"],[-5,"5"],[-9,"9"],[-18,"18"],[-12,"12"],[-15,"15"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p5998"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p5999","attributes":{"axis":{"id":"p5995"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p6004","attributes":{"dimension":1,"axis":{"id":"p6000"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"1e67e149-ba2f-482d-973c-c85ccec456d8","roots":{"p5983":"bfd58359-b9eb-4c1b-8b66-9507ecd34bb0"},"root_ids":["p5983"]}];
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

This entry declares **`scope_taxids`**: [3433198](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3433198). A record counts toward the denominator when its taxid, or any ancestor, is in that set. Records outside it are screened and reported but kept out of the statistics.

67,577 screened records fell outside the declared scope.

Retrieval query:

```
capsid[Title] OR VP1[Gene] OR VP1[Title] OR "complete genome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).


## What reached the statistics

49 records were screened for this assay and **11 (22%)** were evaluable, meaning both primers landed in the right orientation and size range. 38 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 24 |
| `truncated` | 11 |
| `chance_anchor` | 3 |

