# BOCAVIRUS_ssDNA_NS1_gene_round2

<span class="aw-chip aw-chip-stable">stable</span>

**BOCAVIRUS (ssDNA) — NS1 gene**

| | |
|---|---|
| Target | Bocaparvovirus ([taxid 1507401](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1507401)) |
| Gene | NS1 gene |
| Chemistry | conventional |
| Amplicon | 290 bp |
| Designed | 2010 |
| Paper | [10.1371/journal.pone.0011948](https://doi.org/10.1371/journal.pone.0011948) |
| Registry status | active |

!!! quote "The paper"
    Kapoor A et al. 2010. PLoS ONE 5:e11948 (PANBOV primers)

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GCAYCARGAYTGGGTNGANCCWGC` | 24 nt |
| reverse | `GTACAGTCRTAYTCRTTRAARCACCA` | 26 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 395 | 415 | 95.2% | 92.7% – 96.9% |
| baseline (everything earlier) | 1,033 | 1,526 | 67.7% | 65.3% – 70.0% |

Change from baseline, Newcombe interval: **24.1% to 30.4%**. Threshold: **90.0%**.

*detected share 95.2% (93%-97%) since Oct 2024*

Trend across deposit years: by record falling (p=0.0533, 22 years); by footprint falling (p=6.69e-07). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="c3118bda-3932-406b-814c-b52886e538be" data-root-id="p4804" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"52e5aa58-f081-4a1b-93e7-043812f013ba":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p4859","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p4860"}}},"roots":[{"type":"object","name":"Figure","id":"p4804","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p4806"},"y_range":{"type":"object","name":"Range1d","id":"p4813","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p4814"},"y_scale":{"type":"object","name":"LinearScale","id":"p4815"},"title":{"type":"object","name":"Title","id":"p4811","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p4849","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p4801","attributes":{"selected":{"type":"object","name":"Selection","id":"p4802","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p4803"},"data":{"type":"map","entries":[["year",[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,98.80952380952381,82.0,83.07692307692308,88.88888888888889,74.50980392156863,96.15384615384616,55.223880597014926,43.58974358974359,11.016949152542372,6.666666666666667,84.84848484848484,60.71428571428571,56.666666666666664,11.904761904761903,75.25987525987526,81.48148148148148,97.5]],["detected",[3,4,33,16,127,83,41,54,48,38,50,37,17,13,6,28,17,51,5,362,44,351]],["evaluable",[3,4,33,16,127,84,50,65,54,51,52,67,39,118,90,33,28,90,42,481,54,360]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.328625426046248,9.517227179437622,10.955310988645032,10.467343773689333,11.813639954139079,11.557772674175059,11.22734795681138,11.395748828338466,11.27702043233893,11.24015070195139,11.252690272875853,11.415029579131373,11.06545099688784,11.768618707345716,11.600932205756964,10.955310988645032,10.846014908695619,11.600932205756964,11.113982461744026,12.595633171186321,11.27702043233893,12.430677602783453]]]}}},"view":{"type":"object","name":"CDSView","id":"p4850","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4851"}}},"glyph":{"type":"object","name":"Line","id":"p4846","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p4847","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p4848","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p4855","attributes":{"data_source":{"id":"p4801"},"view":{"type":"object","name":"CDSView","id":"p4856","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4857"}}},"glyph":{"type":"object","name":"Scatter","id":"p4852","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p4853","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p4854","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p4812","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p4826"},{"type":"object","name":"BoxZoomTool","id":"p4827","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p4828","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p4834","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4833","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p4835","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p4836"},{"type":"object","name":"SaveTool","id":"p4837"},{"type":"object","name":"HoverTool","id":"p4858","attributes":{"renderers":[{"id":"p4855"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p4821","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4822","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4823"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4824"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p4816","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4817","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4818"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4819"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p4820","attributes":{"axis":{"id":"p4816"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p4825","attributes":{"dimension":1,"axis":{"id":"p4821"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p4838","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p4840","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p4841","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p4842","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p4844","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4843","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p4845","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"52e5aa58-f081-4a1b-93e7-043812f013ba","roots":{"p4804":"c3118bda-3932-406b-814c-b52886e538be"},"root_ids":["p4804"]}];
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

<div id="e795f7c1-8c2f-4a6f-b3f6-3ce56f81ee15" data-root-id="p4864" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"29498999-c546-4625-942b-09f72ff2ff12":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p4904","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p4905"}}},"roots":[{"type":"object","name":"Figure","id":"p4864","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p4865"},"y_range":{"type":"object","name":"DataRange1d","id":"p4866","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p4873"},"y_scale":{"type":"object","name":"LinearScale","id":"p4874"},"title":{"type":"object","name":"Title","id":"p4871","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p4900","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p4861","attributes":{"selected":{"type":"object","name":"Selection","id":"p4862","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p4863"},"data":{"type":"map","entries":[["year",[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[3,4,33,16,127,84,50,65,54,51,52,67,39,118,90,33,28,90,42,481,54,360]],["detected",[3,4,33,16,127,83,41,54,48,38,50,37,17,13,6,28,17,51,5,362,44,351]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p4901","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4902"}}},"glyph":{"type":"object","name":"VBar","id":"p4897","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p4898","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p4899","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p4872","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p4885"},{"type":"object","name":"BoxZoomTool","id":"p4886","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p4887","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p4893","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4892","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p4894","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p4895"},{"type":"object","name":"SaveTool","id":"p4896"},{"type":"object","name":"HoverTool","id":"p4903","attributes":{"renderers":[{"id":"p4900"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p4880","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4881","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4882"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4883"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p4875","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4876","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4877"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4878"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p4879","attributes":{"axis":{"id":"p4875"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p4884","attributes":{"dimension":1,"axis":{"id":"p4880"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"29498999-c546-4625-942b-09f72ff2ff12","roots":{"p4864":"e795f7c1-8c2f-4a6f-b3f6-3ce56f81ee15"},"root_ids":["p4864"]}];
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

<div id="aa7d482f-49fd-40d3-a1a4-4185e0b201a0" data-root-id="p4909" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"602c656b-2fb2-46d6-b9e0-b75cf781d161":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p4951","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p4952"}}},"roots":[{"type":"object","name":"Figure","id":"p4909","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p4911"},"y_range":{"type":"object","name":"FactorRange","id":"p4918","attributes":{"factors":["reverse"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p4919"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p4920"},"title":{"type":"object","name":"Title","id":"p4916","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p4946","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p4906","attributes":{"selected":{"type":"object","name":"Selection","id":"p4907","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p4908"},"data":{"type":"map","entries":[["x",[-21]],["y",["reverse"]],["alpha",[0.37071097372488404]],["pos",[21]],["base",["G"]],["n",[126]],["det_with",["96% of 126"]],["det_without",["100% of 1312"]],["subs",["G&gt;T 117, G&gt;C 5, G&gt;A 4"]],["zone",["no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p4947","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4948"}}},"glyph":{"type":"object","name":"Rect","id":"p4943","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p4944","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p4945","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p4917","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p4931"},{"type":"object","name":"BoxZoomTool","id":"p4932","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p4933","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p4939","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4938","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p4940","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p4941"},{"type":"object","name":"SaveTool","id":"p4942"},{"type":"object","name":"HoverTool","id":"p4949","attributes":{"renderers":[{"id":"p4946"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p4926","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p4927"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p4928"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4929"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p4921","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p4950","attributes":{"ticks":[-21],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4923"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-21,"21"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p4924"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p4925","attributes":{"axis":{"id":"p4921"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p4930","attributes":{"dimension":1,"axis":{"id":"p4926"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"602c656b-2fb2-46d6-b9e0-b75cf781d161","roots":{"p4909":"aa7d482f-49fd-40d3-a1a4-4185e0b201a0"},"root_ids":["p4909"]}];
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

<div id="d8eb9267-3017-491e-a057-23307a8d87bb" data-root-id="p4956" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"7cd7596e-1c13-479a-9952-34e2d630249c":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p5005","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p5006"}}},"roots":[{"type":"object","name":"Figure","id":"p4956","attributes":{"height":132,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p4965","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p4966","attributes":{"factors":["Bocaparvovirus primate1 (3052040)","Human bocavirus (329641)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p4967"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p4968"},"title":{"type":"object","name":"Title","id":"p4963","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p5000","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p4953","attributes":{"selected":{"type":"object","name":"Selection","id":"p4954","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p4955"},"data":{"type":"map","entries":[["y",["Bocaparvovirus primate1 (3052040)","Human bocavirus (329641)"]],["share",[100.0,100.0]],["lo",[95.67605161859485,98.70588871380849]],["hi",[100.0,100.0]],["n",[85,293]],["det",[85,293]],["colour",["#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p5001","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p5002"}}},"glyph":{"type":"object","name":"Scatter","id":"p4997","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p4998","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p4999","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p4964","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p4979"},{"type":"object","name":"BoxZoomTool","id":"p4980","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p4981","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p4987","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4986","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p4988","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p4989"},{"type":"object","name":"SaveTool","id":"p4990"},{"type":"object","name":"HoverTool","id":"p5004","attributes":{"renderers":[{"id":"p5000"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p4974","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p4975"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p4976"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4977"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p4969","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4970","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4971"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4972"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p4973","attributes":{"axis":{"id":"p4969"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p4978","attributes":{"dimension":1,"axis":{"id":"p4974"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p4991","attributes":{"source":{"id":"p4953"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p5003","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"7cd7596e-1c13-479a-9952-34e2d630249c","roots":{"p4956":"d8eb9267-3017-491e-a057-23307a8d87bb"},"root_ids":["p4956"]}];
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


## What reached the statistics

7,497 records were screened for this assay and **1,941 (26%)** were evaluable, meaning both primers landed in the right orientation and size range. 5,556 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 5,020 |
| `truncated` | 349 |
| `chance_anchor` | 187 |

