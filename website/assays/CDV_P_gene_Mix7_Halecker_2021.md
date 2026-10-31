# CDV_P_gene_Mix7_Halecker_2021

<span class="aw-chip aw-chip-stable">stable</span>

**CANINE DISTEMPER VIRUS — P gene TaqMan RT-qPCR CDV-Mix 7 (Halecker 2021)**

| | |
|---|---|
| Target | Morbillivirus canis (formerly Canine morbillivirus) ([taxid 3052342](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3052342)) |
| Gene | P |
| Chemistry | hydrolysis_probe |
| Amplicon | 96 bp |
| Designed | 2021 |
| Paper | [10.3390/v13081632](https://doi.org/10.3390/v13081632) |
| Registry status | active |

!!! quote "The paper"
    Halecker S, Bock S, Beer M, Hoffmann B. A New Molecular Detection System for Canine Distemper Virus Based on a Double-Check Strategy. Viruses 2021;13:1632.

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `AGGARCAGGCCTAYCATGTCA` | 21 nt |
| reverse | `TRCTGCTGACCTCTTGAATCTC` | 22 nt |
| probe | `ATGCCTCAAARCCCTCAGAGAGAATCC` | 27 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 85 | 86 | 98.8% | 93.7% – 99.8% |
| baseline (everything earlier) | 264 | 287 | 92.0% | 88.3% – 94.6% |

Change from baseline, Newcombe interval: **1.1% to 10.7%**. Threshold: **90.0%**.

*detected share 98.8% (94%-100%) since Oct 2024*

Trend across deposit years: by record falling (p=0.277, 29 years); by footprint falling (p=0.0845). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="ea49c98a-047e-4c22-bf55-7d12db15b550" data-root-id="p7361" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"20516c93-7a21-45dc-89be-e32f60f240df":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7416","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7417"}}},"roots":[{"type":"object","name":"Figure","id":"p7361","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p7363"},"y_range":{"type":"object","name":"Range1d","id":"p7370","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p7371"},"y_scale":{"type":"object","name":"LinearScale","id":"p7372"},"title":{"type":"object","name":"Title","id":"p7368","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7406","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7358","attributes":{"selected":{"type":"object","name":"Selection","id":"p7359","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7360"},"data":{"type":"map","entries":[["year",[1990,1993,1998,1999,2000,2001,2002,2003,2004,2005,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,85.71428571428571,100.0,93.33333333333333,100.0,100.0,75.0,86.95652173913044,96.0,77.77777777777779,97.5609756097561,41.66666666666667,91.66666666666666,100.0,100.0]],["detected",[1,1,2,2,7,1,3,5,2,3,9,2,4,4,11,6,16,14,13,10,18,20,48,7,40,5,11,12,72]],["evaluable",[1,1,2,2,7,1,3,5,2,3,9,2,4,4,11,7,16,15,13,10,24,23,50,9,41,12,12,12,72]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.07684386569143,9.07684386569143,9.897626379762722,8.703135093227193,9.328625426046248,9.667366891029102,9.07684386569143,9.328625426046248,10.071067811865476,9.07684386569143,9.517227179437622,9.517227179437622,10.209683151927734,9.897626379762722,10.467343773689333,10.423139468338052,10.324834530005162,10.143865699252444,10.74264168206181,10.713966621835368,11.22734795681138,10.071067811865476,11.098224018878925,10.269703144398052,10.269703144398052,10.269703144398052,11.460677957646856]]]}}},"view":{"type":"object","name":"CDSView","id":"p7407","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7408"}}},"glyph":{"type":"object","name":"Line","id":"p7403","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p7404","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p7405","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p7412","attributes":{"data_source":{"id":"p7358"},"view":{"type":"object","name":"CDSView","id":"p7413","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7414"}}},"glyph":{"type":"object","name":"Scatter","id":"p7409","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p7410","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p7411","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7369","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7383"},{"type":"object","name":"BoxZoomTool","id":"p7384","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7385","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7391","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7390","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7392","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7393"},{"type":"object","name":"SaveTool","id":"p7394"},{"type":"object","name":"HoverTool","id":"p7415","attributes":{"renderers":[{"id":"p7412"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p7378","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7379","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7380"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7381"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7373","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7374","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7375"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7376"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7377","attributes":{"axis":{"id":"p7373"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7382","attributes":{"dimension":1,"axis":{"id":"p7378"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p7395","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p7397","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p7398","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p7399","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p7401","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7400","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p7402","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"20516c93-7a21-45dc-89be-e32f60f240df","roots":{"p7361":"ea49c98a-047e-4c22-bf55-7d12db15b550"},"root_ids":["p7361"]}];
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

<div id="aa326f91-554d-4441-9e44-f3b0fa0ae3f7" data-root-id="p7421" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"849f9c7b-a1e6-4b7a-8eb2-049c9cb83fe7":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7461","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7462"}}},"roots":[{"type":"object","name":"Figure","id":"p7421","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p7422"},"y_range":{"type":"object","name":"DataRange1d","id":"p7423","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p7430"},"y_scale":{"type":"object","name":"LinearScale","id":"p7431"},"title":{"type":"object","name":"Title","id":"p7428","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7457","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7418","attributes":{"selected":{"type":"object","name":"Selection","id":"p7419","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7420"},"data":{"type":"map","entries":[["year",[1990,1993,1998,1999,2000,2001,2002,2003,2004,2005,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,2,2,7,1,3,5,2,3,9,2,4,4,11,7,16,15,13,10,24,23,50,9,41,12,12,12,72]],["detected",[1,1,2,2,7,1,3,5,2,3,9,2,4,4,11,6,16,14,13,10,18,20,48,7,40,5,11,12,72]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p7458","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7459"}}},"glyph":{"type":"object","name":"VBar","id":"p7454","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p7455","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p7456","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7429","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7442"},{"type":"object","name":"BoxZoomTool","id":"p7443","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7444","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7450","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7449","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7451","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7452"},{"type":"object","name":"SaveTool","id":"p7453"},{"type":"object","name":"HoverTool","id":"p7460","attributes":{"renderers":[{"id":"p7457"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p7437","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7438","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7439"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7440"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7432","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7433","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7434"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7435"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7436","attributes":{"axis":{"id":"p7432"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7441","attributes":{"dimension":1,"axis":{"id":"p7437"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"849f9c7b-a1e6-4b7a-8eb2-049c9cb83fe7","roots":{"p7421":"aa326f91-554d-4441-9e44-f3b0fa0ae3f7"},"root_ids":["p7421"]}];
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

<div id="d9bfccea-06d6-430e-a09d-7396dfb16265" data-root-id="p7466" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"4d6d99f9-e386-41f8-9b47-07e95cdc8aee":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7508","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7509"}}},"roots":[{"type":"object","name":"Figure","id":"p7466","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p7468"},"y_range":{"type":"object","name":"FactorRange","id":"p7475","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p7476"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p7477"},"title":{"type":"object","name":"Title","id":"p7473","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7503","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7463","attributes":{"selected":{"type":"object","name":"Selection","id":"p7464","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7465"},"data":{"type":"map","entries":[["x",[-20,-22]],["y",["forward","reverse"]],["alpha",[0.8336461126005362,0.44168900804289546]],["pos",[20,22]],["base",["G","T"]],["n",[75,32]],["det_with",["96% of 75","100% of 32"]],["det_without",["93% of 302","93% of 345"]],["subs",["G&gt;A 75","T&gt;G 32"]],["zone",["no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p7504","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7505"}}},"glyph":{"type":"object","name":"Rect","id":"p7500","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p7501","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p7502","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7474","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7488"},{"type":"object","name":"BoxZoomTool","id":"p7489","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7490","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7496","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7495","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7497","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7498"},{"type":"object","name":"SaveTool","id":"p7499"},{"type":"object","name":"HoverTool","id":"p7506","attributes":{"renderers":[{"id":"p7503"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p7483","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p7484"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p7485"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7486"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7478","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p7507","attributes":{"ticks":[-22,-20],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7480"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-20,"20"],[-22,"22"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p7481"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7482","attributes":{"axis":{"id":"p7478"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7487","attributes":{"dimension":1,"axis":{"id":"p7483"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"4d6d99f9-e386-41f8-9b47-07e95cdc8aee","roots":{"p7466":"d9bfccea-06d6-430e-a09d-7396dfb16265"},"root_ids":["p7466"]}];
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

<div id="fde8b1e4-77ac-4867-a92d-4b1307e9a106" data-root-id="p7513" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"fd2669ee-e2cb-4c3a-97aa-ec33527143d7":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7562","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7563"}}},"roots":[{"type":"object","name":"Figure","id":"p7513","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p7522","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p7523","attributes":{"factors":["Morbillivirus canis (3052342)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p7524"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p7525"},"title":{"type":"object","name":"Title","id":"p7520","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7557","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7510","attributes":{"selected":{"type":"object","name":"Selection","id":"p7511","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7512"},"data":{"type":"map","entries":[["y",["Morbillivirus canis (3052342)"]],["share",[98.83720930232558]],["lo",[93.70359341070827]],["hi",[99.79444313347503]],["n",[86]],["det",[85]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p7558","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7559"}}},"glyph":{"type":"object","name":"Scatter","id":"p7554","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p7555","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p7556","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7521","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7536"},{"type":"object","name":"BoxZoomTool","id":"p7537","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7538","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7544","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7543","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7545","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7546"},{"type":"object","name":"SaveTool","id":"p7547"},{"type":"object","name":"HoverTool","id":"p7561","attributes":{"renderers":[{"id":"p7557"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p7531","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p7532"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p7533"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7534"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7526","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7527","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7528"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7529"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7530","attributes":{"axis":{"id":"p7526"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7535","attributes":{"dimension":1,"axis":{"id":"p7531"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p7548","attributes":{"source":{"id":"p7510"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p7560","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"fd2669ee-e2cb-4c3a-97aa-ec33527143d7","roots":{"p7513":"fde8b1e4-77ac-4867-a92d-4b1307e9a106"},"root_ids":["p7513"]}];
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

3,952 records were screened for this assay and **373 (9%)** were evaluable, meaning both primers landed in the right orientation and size range. 3,579 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 3,554 |
| `chance_anchor` | 21 |
| `truncated` | 4 |

