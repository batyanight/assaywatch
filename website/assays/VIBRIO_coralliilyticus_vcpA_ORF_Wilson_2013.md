# VIBRIO_coralliilyticus_vcpA_ORF_Wilson_2013

<span class="aw-chip aw-chip-stable">stable</span>

**VIBRIO CORALLIILYTICUS — vcpA full-ORF PCR (primers from Pollock 2010, used by Wilson 2013)**

| | |
|---|---|
| Target | Vibrio coralliilyticus ([taxid 190893](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=190893)) |
| Gene | vcpA |
| Chemistry | conventional |
| Amplicon | 1854 bp |
| Designed | 2013 |
| Paper | [10.1371/journal.pone.0081800](https://doi.org/10.1371/journal.pone.0081800) |
| Registry status | active |

!!! quote "The paper"
    Wilson, B., Muirhead, A., Bazanella, M., Huete-Stauffer, C., Vezzulli, L. & Bourne, D. G. An Improved Detection and Quantification Method for the Coral Pathogen Vibrio coralliilyticus. PLoS ONE 8, e81800 (2013).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ATGAAACAACGTCAAATGCTTTG` | 23 nt |
| reverse | `CCCTTTCACTTCCGATGTTGTG` | 22 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (48 months, from Oct 2022) | 16 | 16 | 100.0% | 80.6% – 100.0% |
| baseline (everything earlier) | 19 | 19 | 100.0% | 83.2% – 100.0% |

Change from baseline, Newcombe interval: **-19.4% to 16.8%**. Threshold: **90.0%**.

*detected share 100.0% (81%-100%) since Oct 2022 (window widened to 48 months to reach 15 evaluable records)*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="af7b80a7-7d4e-407d-8e71-6e7dae209d30" data-root-id="p34175" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"d3c8afaf-e4b3-4a94-9007-145993901618":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p34230","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p34231"}}},"roots":[{"type":"object","name":"Figure","id":"p34175","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p34177"},"y_range":{"type":"object","name":"Range1d","id":"p34184","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p34185"},"y_scale":{"type":"object","name":"LinearScale","id":"p34186"},"title":{"type":"object","name":"Title","id":"p34182","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p34220","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p34172","attributes":{"selected":{"type":"object","name":"Selection","id":"p34173","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p34174"},"data":{"type":"map","entries":[["year",[2014,2015,2016,2017,2018,2019,2020,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[2,3,4,1,1,1,5,2,2,4,2,8]],["evaluable",[2,3,4,1,1,1,5,2,2,4,2,8]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent","recent"]],["size",[9.07684386569143,9.328625426046248,9.517227179437622,8.703135093227193,8.703135093227193,8.703135093227193,9.667366891029102,9.07684386569143,9.07684386569143,9.517227179437622,9.07684386569143,9.989711205477885]]]}}},"view":{"type":"object","name":"CDSView","id":"p34221","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p34222"}}},"glyph":{"type":"object","name":"Line","id":"p34217","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p34218","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p34219","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p34226","attributes":{"data_source":{"id":"p34172"},"view":{"type":"object","name":"CDSView","id":"p34227","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p34228"}}},"glyph":{"type":"object","name":"Scatter","id":"p34223","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p34224","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p34225","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p34183","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p34197"},{"type":"object","name":"BoxZoomTool","id":"p34198","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p34199","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p34205","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p34204","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p34206","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p34207"},{"type":"object","name":"SaveTool","id":"p34208"},{"type":"object","name":"HoverTool","id":"p34229","attributes":{"renderers":[{"id":"p34226"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p34192","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34193","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34194"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34195"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p34187","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34188","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34189"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34190"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p34191","attributes":{"axis":{"id":"p34187"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p34196","attributes":{"dimension":1,"axis":{"id":"p34192"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p34209","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2021.5,"right":{"type":"object","name":"Node","id":"p34211","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p34212","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p34213","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p34215","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p34214","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p34216","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"d3c8afaf-e4b3-4a94-9007-145993901618","roots":{"p34175":"af7b80a7-7d4e-407d-8e71-6e7dae209d30"},"root_ids":["p34175"]}];
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

<div id="b4161ec9-5a90-4bca-8ab7-326f865ebbb8" data-root-id="p34235" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"25fa2829-7e99-42d3-87bd-a48b2f7646e0":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p34275","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p34276"}}},"roots":[{"type":"object","name":"Figure","id":"p34235","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p34236"},"y_range":{"type":"object","name":"DataRange1d","id":"p34237","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p34244"},"y_scale":{"type":"object","name":"LinearScale","id":"p34245"},"title":{"type":"object","name":"Title","id":"p34242","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p34271","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p34232","attributes":{"selected":{"type":"object","name":"Selection","id":"p34233","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p34234"},"data":{"type":"map","entries":[["year",[2014,2015,2016,2017,2018,2019,2020,2022,2023,2024,2025,2026]],["evaluable",[2,3,4,1,1,1,5,2,2,4,2,8]],["detected",[2,3,4,1,1,1,5,2,2,4,2,8]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p34272","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p34273"}}},"glyph":{"type":"object","name":"VBar","id":"p34268","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p34269","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p34270","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p34243","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p34256"},{"type":"object","name":"BoxZoomTool","id":"p34257","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p34258","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p34264","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p34263","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p34265","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p34266"},{"type":"object","name":"SaveTool","id":"p34267"},{"type":"object","name":"HoverTool","id":"p34274","attributes":{"renderers":[{"id":"p34271"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p34251","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34252","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34253"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34254"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p34246","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34247","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34248"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34249"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p34250","attributes":{"axis":{"id":"p34246"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p34255","attributes":{"dimension":1,"axis":{"id":"p34251"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"25fa2829-7e99-42d3-87bd-a48b2f7646e0","roots":{"p34235":"b4161ec9-5a90-4bca-8ab7-326f865ebbb8"},"root_ids":["p34235"]}];
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

<div id="ba364364-b238-45af-b242-6a18b83acfb0" data-root-id="p34280" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b4f09a0c-f9fc-4340-91b6-042c21803bb6":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p34322","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p34323"}}},"roots":[{"type":"object","name":"Figure","id":"p34280","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p34282"},"y_range":{"type":"object","name":"FactorRange","id":"p34289","attributes":{"factors":["reverse"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p34290"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p34291"},"title":{"type":"object","name":"Title","id":"p34287","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p34317","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p34277","attributes":{"selected":{"type":"object","name":"Selection","id":"p34278","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p34279"},"data":{"type":"map","entries":[["x",[-11]],["y",["reverse"]],["alpha",[1.0]],["pos",[11]],["base",["C"]],["n",[35]],["det_with",["100% of 35"]],["det_without",["0% of 0"]],["subs",["C&gt;A 35"]],["zone",["no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p34318","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p34319"}}},"glyph":{"type":"object","name":"Rect","id":"p34314","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p34315","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p34316","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p34288","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p34302"},{"type":"object","name":"BoxZoomTool","id":"p34303","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p34304","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p34310","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p34309","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p34311","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p34312"},{"type":"object","name":"SaveTool","id":"p34313"},{"type":"object","name":"HoverTool","id":"p34320","attributes":{"renderers":[{"id":"p34317"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p34297","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p34298"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p34299"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34300"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p34292","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p34321","attributes":{"ticks":[-11],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34294"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-11,"11"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p34295"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p34296","attributes":{"axis":{"id":"p34292"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p34301","attributes":{"dimension":1,"axis":{"id":"p34297"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b4f09a0c-f9fc-4340-91b6-042c21803bb6","roots":{"p34280":"ba364364-b238-45af-b242-6a18b83acfb0"},"root_ids":["p34280"]}];
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
vcpA[All Fields] OR vtpA[All Fields] OR "complete genome"[Title] OR "chromosome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `amplicon_disagrees_with_paper`, `oligos_from_secondary_source`.


## What reached the statistics

97 records were screened for this assay and **35 (36%)** were evaluable, meaning both primers landed in the right orientation and size range. 62 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 46 |
| `truncated` | 16 |

