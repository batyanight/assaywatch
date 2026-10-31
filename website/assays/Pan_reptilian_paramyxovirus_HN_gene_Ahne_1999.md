# Pan_reptilian_paramyxovirus_HN_gene_Ahne_1999

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**Pan-reptilian paramyxovirus — HN gene**

| | |
|---|---|
| Target | Ferlavirus ([taxid 1283308](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1283308)) |
| Gene | HN gene |
| Chemistry | conventional |
| Amplicon | 679 bp |
| Designed | 1999 |
| Paper | [10.1016/S0168-1702(99)00059-3](https://doi.org/10.1016/S0168-1702(99)00059-3) |
| Registry status | active |

!!! quote "The paper"
    Ahne W et al. 1999. Virus Res 63:65-74

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `AAATCCTGCAGTACCGTGGCA` | 21 nt |
| reverse | `AGATATCTGTGTAAACTCCTG` | 21 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 4 | 6 | 66.7% | 30.0% – 90.3% |
| baseline (everything earlier) | 21 | 22 | 95.5% | 78.2% – 99.2% |

Change from baseline, Newcombe interval: **-65.6% to 0.5%**. Threshold: **90.0%**.

*6 evaluable records since Oct 2021, below the minimum of 15; the detected share is 67% (30%-90%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=0.154, 8 years); by footprint falling (p=0.385). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="a18c5ee7-11b2-4e58-bf8b-3d545e3ce9ca" data-root-id="p28138" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9dea7edf-b89e-4d27-8ba4-1cf464de3d18":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p28193","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p28194"}}},"roots":[{"type":"object","name":"Figure","id":"p28138","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p28140"},"y_range":{"type":"object","name":"Range1d","id":"p28147","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p28148"},"y_scale":{"type":"object","name":"LinearScale","id":"p28149"},"title":{"type":"object","name":"Title","id":"p28145","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p28183","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p28135","attributes":{"selected":{"type":"object","name":"Selection","id":"p28136","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p28137"},"data":{"type":"map","entries":[["year",[2003,2014,2017,2018,2019,2021,2025,2026]],["share",[100.0,100.0,100.0,100.0,87.5,100.0,0.0,100.0]],["detected",[2,5,1,2,7,4,0,4]],["evaluable",[2,5,1,2,8,4,2,4]],["window",["baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,9.667366891029102,8.703135093227193,9.07684386569143,9.989711205477885,9.517227179437622,9.07684386569143,9.517227179437622]]]}}},"view":{"type":"object","name":"CDSView","id":"p28184","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p28185"}}},"glyph":{"type":"object","name":"Line","id":"p28180","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p28181","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p28182","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p28189","attributes":{"data_source":{"id":"p28135"},"view":{"type":"object","name":"CDSView","id":"p28190","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p28191"}}},"glyph":{"type":"object","name":"Scatter","id":"p28186","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p28187","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p28188","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p28146","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p28160"},{"type":"object","name":"BoxZoomTool","id":"p28161","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p28162","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p28168","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p28167","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p28169","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p28170"},{"type":"object","name":"SaveTool","id":"p28171"},{"type":"object","name":"HoverTool","id":"p28192","attributes":{"renderers":[{"id":"p28189"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p28155","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p28156","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28157"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28158"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p28150","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p28151","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28152"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28153"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p28154","attributes":{"axis":{"id":"p28150"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p28159","attributes":{"dimension":1,"axis":{"id":"p28155"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p28172","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2020.5,"right":{"type":"object","name":"Node","id":"p28174","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p28175","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p28176","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p28178","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p28177","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p28179","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9dea7edf-b89e-4d27-8ba4-1cf464de3d18","roots":{"p28138":"a18c5ee7-11b2-4e58-bf8b-3d545e3ce9ca"},"root_ids":["p28138"]}];
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

<div id="e57b48c6-9c86-435b-8ffc-de396b14d3ae" data-root-id="p28198" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"aed74bef-d59d-4095-bb99-5d83151848ef":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p28238","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p28239"}}},"roots":[{"type":"object","name":"Figure","id":"p28198","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p28199"},"y_range":{"type":"object","name":"DataRange1d","id":"p28200","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p28207"},"y_scale":{"type":"object","name":"LinearScale","id":"p28208"},"title":{"type":"object","name":"Title","id":"p28205","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p28234","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p28195","attributes":{"selected":{"type":"object","name":"Selection","id":"p28196","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p28197"},"data":{"type":"map","entries":[["year",[2003,2014,2017,2018,2019,2021,2025,2026]],["evaluable",[2,5,1,2,8,4,2,4]],["detected",[2,5,1,2,7,4,0,4]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p28235","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p28236"}}},"glyph":{"type":"object","name":"VBar","id":"p28231","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p28232","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p28233","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p28206","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p28219"},{"type":"object","name":"BoxZoomTool","id":"p28220","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p28221","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p28227","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p28226","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p28228","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p28229"},{"type":"object","name":"SaveTool","id":"p28230"},{"type":"object","name":"HoverTool","id":"p28237","attributes":{"renderers":[{"id":"p28234"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p28214","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p28215","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28216"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28217"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p28209","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p28210","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28211"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28212"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p28213","attributes":{"axis":{"id":"p28209"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p28218","attributes":{"dimension":1,"axis":{"id":"p28214"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"aed74bef-d59d-4095-bb99-5d83151848ef","roots":{"p28198":"e57b48c6-9c86-435b-8ffc-de396b14d3ae"},"root_ids":["p28198"]}];
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

<div id="f7912dbd-f68e-4ef2-9235-7842553a940c" data-root-id="p28243" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"61860ade-4521-45c7-a667-78191d121aa1":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p28285","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p28286"}}},"roots":[{"type":"object","name":"Figure","id":"p28243","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p28245"},"y_range":{"type":"object","name":"FactorRange","id":"p28252","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p28253"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p28254"},"title":{"type":"object","name":"Title","id":"p28250","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p28280","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p28240","attributes":{"selected":{"type":"object","name":"Selection","id":"p28241","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p28242"},"data":{"type":"map","entries":[["x",[-17,-10,-13]],["y",["reverse","forward","forward"]],["alpha",[1.0,1.0,1.0]],["pos",[17,10,13]],["base",["A","T","C"]],["n",[23,24,25]],["det_with",["91% of 23","92% of 24","92% of 25"]],["det_without",["80% of 5","75% of 4","67% of 3"]],["subs",["A&gt;G 23","T&gt;C 24","C&gt;T 25"]],["zone",["no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p28281","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p28282"}}},"glyph":{"type":"object","name":"Rect","id":"p28277","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p28278","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p28279","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p28251","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p28265"},{"type":"object","name":"BoxZoomTool","id":"p28266","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p28267","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p28273","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p28272","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p28274","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p28275"},{"type":"object","name":"SaveTool","id":"p28276"},{"type":"object","name":"HoverTool","id":"p28283","attributes":{"renderers":[{"id":"p28280"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p28260","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p28261"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p28262"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28263"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p28255","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p28284","attributes":{"ticks":[-17,-13,-10],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28257"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-17,"17"],[-10,"10"],[-13,"13"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p28258"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p28259","attributes":{"axis":{"id":"p28255"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p28264","attributes":{"dimension":1,"axis":{"id":"p28260"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"61860ade-4521-45c7-a667-78191d121aa1","roots":{"p28243":"f7912dbd-f68e-4ef2-9235-7842553a940c"},"root_ids":["p28243"]}];
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

Disclosures on this entry: `amplicon_measured_not_published`.


## What reached the statistics

61 records were screened for this assay and **28 (46%)** were evaluable, meaning both primers landed in the right orientation and size range. 33 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 33 |

