# PERKINSEA_NAG01_18S_cladeAC_Smilansky_2021

<span class="aw-chip aw-chip-no-recent-data">no recent data</span>

**PERKINSEA NAG01 Clades A-C — 18S duplex qPCR, NAG01a-c probe (Smilansky 2021)**

| | |
|---|---|
| Target | Perkinsea (NAG01) ([taxid 27997](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=27997)) |
| Gene | 18S rRNA |
| Chemistry | hydrolysis_probe |
| Amplicon | 287 bp |
| Designed | 2021 |
| Paper | [10.1098/rsos.202150](https://doi.org/10.1098/rsos.202150) |
| Registry status | active |

!!! quote "The paper"
    Smilansky, V., Chambouvet, A., Reeves, M., Richards, T. A. & Milner, D. S. A novel duplex qPCR assay for stepwise detection of multiple Perkinsea protistan infections of amphibian tissues. Royal Society Open Science 8, 202150 (2021).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GGGCTTCAYAGTCTTGCAAT` | 20 nt |
| reverse | `GCCTGCTTGAAACRCTCTAA` | 20 nt |
| probe | `CAAGGACGACCTACCCACCTTAG` | 23 nt |

## The verdict, and the numbers behind it

**no recent data** — nothing was deposited in the window

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 0 | 0 | — | 0.0% – 100.0% |
| baseline (everything earlier) | 196 | 391 | 50.1% | 45.2% – 55.1% |

Change from baseline, Newcombe interval: **-100.0% to 100.0%**. Threshold: **90.0%**.

*no evaluable records deposited since Oct 2021 (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=1.48e-42, 5 years); by footprint falling (p=0.181). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="b988b828-2719-405b-8e53-8211f2ead8fe" data-root-id="p23093" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"ee24c09a-c19b-43b2-9c76-27bbce704d81":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p23148","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p23149"}}},"roots":[{"type":"object","name":"Figure","id":"p23093","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p23095"},"y_range":{"type":"object","name":"Range1d","id":"p23102","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p23103"},"y_scale":{"type":"object","name":"LinearScale","id":"p23104"},"title":{"type":"object","name":"Title","id":"p23100","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p23138","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p23090","attributes":{"selected":{"type":"object","name":"Selection","id":"p23091","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p23092"},"data":{"type":"map","entries":[["year",[2010,2015,2017,2019,2021]],["share",[0.0,87.1111111111111,0.0,0.0,0.0]],["detected",[0,196,0,0,0]],["evaluable",[1,225,92,1,72]],["window",["baseline","baseline","baseline","baseline","recent"]],["size",[8.703135093227193,12.157112589604052,11.614642982378804,8.703135093227193,11.460677957646856]]]}}},"view":{"type":"object","name":"CDSView","id":"p23139","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p23140"}}},"glyph":{"type":"object","name":"Line","id":"p23135","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p23136","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p23137","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p23144","attributes":{"data_source":{"id":"p23090"},"view":{"type":"object","name":"CDSView","id":"p23145","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p23146"}}},"glyph":{"type":"object","name":"Scatter","id":"p23141","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p23142","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p23143","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p23101","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p23115"},{"type":"object","name":"BoxZoomTool","id":"p23116","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p23117","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p23123","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p23122","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p23124","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p23125"},{"type":"object","name":"SaveTool","id":"p23126"},{"type":"object","name":"HoverTool","id":"p23147","attributes":{"renderers":[{"id":"p23144"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p23110","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23111","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23112"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23113"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p23105","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23106","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23107"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23108"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p23109","attributes":{"axis":{"id":"p23105"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p23114","attributes":{"dimension":1,"axis":{"id":"p23110"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p23127","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2020.5,"right":{"type":"object","name":"Node","id":"p23129","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p23130","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p23131","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p23133","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p23132","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p23134","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"ee24c09a-c19b-43b2-9c76-27bbce704d81","roots":{"p23093":"b988b828-2719-405b-8e53-8211f2ead8fe"},"root_ids":["p23093"]}];
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

<div id="a54888c8-b5bb-4ceb-a893-3b25432662d2" data-root-id="p23153" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"072bbc4c-a75e-4663-a293-9cf7fbca11b6":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p23193","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p23194"}}},"roots":[{"type":"object","name":"Figure","id":"p23153","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p23154"},"y_range":{"type":"object","name":"DataRange1d","id":"p23155","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p23162"},"y_scale":{"type":"object","name":"LinearScale","id":"p23163"},"title":{"type":"object","name":"Title","id":"p23160","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p23189","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p23150","attributes":{"selected":{"type":"object","name":"Selection","id":"p23151","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p23152"},"data":{"type":"map","entries":[["year",[2010,2015,2017,2019,2021]],["evaluable",[1,225,92,1,72]],["detected",[0,196,0,0,0]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p23190","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p23191"}}},"glyph":{"type":"object","name":"VBar","id":"p23186","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p23187","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p23188","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p23161","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p23174"},{"type":"object","name":"BoxZoomTool","id":"p23175","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p23176","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p23182","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p23181","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p23183","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p23184"},{"type":"object","name":"SaveTool","id":"p23185"},{"type":"object","name":"HoverTool","id":"p23192","attributes":{"renderers":[{"id":"p23189"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p23169","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23170","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23171"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23172"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p23164","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23165","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23166"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23167"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p23168","attributes":{"axis":{"id":"p23164"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p23173","attributes":{"dimension":1,"axis":{"id":"p23169"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"072bbc4c-a75e-4663-a293-9cf7fbca11b6","roots":{"p23153":"a54888c8-b5bb-4ceb-a893-3b25432662d2"},"root_ids":["p23153"]}];
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

<div id="d8a5e310-a1e5-4537-b3d7-0ca8d897a131" data-root-id="p23198" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"5e5a22c9-f0d2-41b8-bf8a-6f5aa272c32b":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p23240","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p23241"}}},"roots":[{"type":"object","name":"Figure","id":"p23198","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p23200"},"y_range":{"type":"object","name":"FactorRange","id":"p23207","attributes":{"factors":["probe","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p23208"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p23209"},"title":{"type":"object","name":"Title","id":"p23205","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p23235","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p23195","attributes":{"selected":{"type":"object","name":"Selection","id":"p23196","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p23197"},"data":{"type":"map","entries":[["x",[-11,-12,-8,-19,-2,-14,-11,-16,-4,-13,-15]],["y",["probe","probe","probe","probe","probe","forward","forward","forward","forward","forward","forward"]],["alpha",[1.0,1.0,1.0,1.0,1.0,0.8630434782608696,0.8195652173913044,0.8195652173913044,0.7847826086956522,0.7847826086956522,0.7847826086956522]],["pos",[11,12,8,19,2,14,11,16,4,13,15]],["base",["A","T","C","G","A","C","A","T","C","A","T"]],["n",[169,169,167,166,184,82,77,77,73,73,73]],["det_with",["0% of 169","0% of 169","0% of 167","0% of 166","3% of 184","0% of 82","0% of 77","0% of 77","0% of 73","0% of 73","0% of 73"]],["det_without",["66% of 295","66% of 295","66% of 297","66% of 298","68% of 280","51% of 382","51% of 387","51% of 387","50% of 391","50% of 391","50% of 391"]],["subs",["A&gt;T 165, A&gt;G 3, A&gt;C 1","T&gt;G 168, T&gt;A 1","C&gt;T 166, C&gt;A 1","G&gt;A 166","A&gt;C 183, A&gt;G 1","C&gt;T 81, C&gt;A 1","A&gt;T 77","T&gt;A 76, T&gt;C 1","C&gt;T 73","A&gt;T 69, A&gt;C 4","T&gt;A 72, T&gt;C 1"]],["zone",["no","no","no","no","yes","no","no","no","yes","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p23236","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p23237"}}},"glyph":{"type":"object","name":"Rect","id":"p23232","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p23233","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p23234","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p23206","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p23220"},{"type":"object","name":"BoxZoomTool","id":"p23221","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p23222","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p23228","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p23227","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p23229","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p23230"},{"type":"object","name":"SaveTool","id":"p23231"},{"type":"object","name":"HoverTool","id":"p23238","attributes":{"renderers":[{"id":"p23235"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p23215","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p23216"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p23217"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23218"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p23210","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p23239","attributes":{"ticks":[-19,-16,-15,-14,-13,-12,-11,-8,-4,-2],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23212"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-11,"11"],[-12,"12"],[-8,"8"],[-19,"19"],[-2,"2"],[-14,"14"],[-16,"16"],[-4,"4"],[-13,"13"],[-15,"15"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p23213"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p23214","attributes":{"axis":{"id":"p23210"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p23219","attributes":{"dimension":1,"axis":{"id":"p23215"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"5e5a22c9-f0d2-41b8-bf8a-6f5aa272c32b","roots":{"p23198":"d8a5e310-a1e5-4537-b3d7-0ca8d897a131"},"root_ids":["p23198"]}];
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

This entry declares **`scope_taxids`**: [373149](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=373149). A record counts toward the denominator when its taxid, or any ancestor, is in that set. Records outside it are screened and reported but kept out of the statistics.

1,389 screened records fell outside the declared scope.

Retrieval query:

```
18S[Title] OR "small subunit"[Title] OR "ribosomal RNA"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `oligos_from_secondary_source`.


## What reached the statistics

537 records were screened for this assay and **391 (73%)** were evaluable, meaning both primers landed in the right orientation and size range. 146 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `truncated` | 145 |
| `no_site` | 1 |

