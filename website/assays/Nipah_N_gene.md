# Nipah_N_gene

<span class="aw-chip aw-chip-stable">stable</span>

**Nipah — N gene**

| | |
|---|---|
| Target | Henipavirus nipahense (formerly Nipah henipavirus) ([taxid 3052225](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3052225)) |
| Gene | N gene |
| Chemistry | conventional |
| Amplicon | 398 bp |
| Designed | 2007 |
| Paper | [10.1016/j.jviromet.2006.11.023](https://doi.org/10.1016/j.jviromet.2006.11.023) |
| Registry status | active |

!!! quote "The paper"
    Wacharapluesadee S, Hemachudha T. 2007. Duplex nested RT-PCR for detection of Nipah virus RNA from urine specimens of bats. J Virol Methods 141:97-101

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CTTGAGCCTATGTATTTCAGAC` | 22 nt |
| reverse | `GCTTTTGCAGCCAGTCTTG` | 19 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 21 | 21 | 100.0% | 84.5% – 100.0% |
| baseline (everything earlier) | 180 | 186 | 96.8% | 93.1% – 98.5% |

Change from baseline, Newcombe interval: **-12.3% to 6.9%**. Threshold: **90.0%**.

*detected share 100.0% (85%-100%) since Oct 2024*

Trend across deposit years: by record rising (p=0.00958, 22 years); by footprint rising (p=0.611). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="ebe7195d-1b60-439d-bf37-e803a24e01c2" data-root-id="p19614" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"f7c12a43-9337-473c-a0bf-9f9d0a2b4164":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p19669","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p19670"}}},"roots":[{"type":"object","name":"Figure","id":"p19614","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p19616"},"y_range":{"type":"object","name":"Range1d","id":"p19623","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p19624"},"y_scale":{"type":"object","name":"LinearScale","id":"p19625"},"title":{"type":"object","name":"Title","id":"p19621","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p19659","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p19611","attributes":{"selected":{"type":"object","name":"Selection","id":"p19612","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p19613"},"data":{"type":"map","entries":[["year",[2000,2001,2002,2004,2005,2007,2008,2009,2010,2012,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,33.33333333333333,100.0,100.0,100.0,100.0,100.0,100.0,94.5945945945946,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[2,2,1,3,5,2,1,1,2,8,1,10,2,2,18,35,35,3,1,52,9,6]],["evaluable",[2,2,1,3,5,2,1,1,6,8,1,10,2,2,18,37,35,3,1,52,9,6]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,9.07684386569143,8.703135093227193,9.328625426046248,9.667366891029102,9.07684386569143,8.703135093227193,8.703135093227193,9.791719296345839,9.989711205477885,8.703135093227193,10.143865699252444,9.07684386569143,9.07684386569143,10.547770533331066,11.030852377887435,10.994220569835573,9.328625426046248,8.703135093227193,11.252690272875853,10.071067811865476,9.791719296345839]]]}}},"view":{"type":"object","name":"CDSView","id":"p19660","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p19661"}}},"glyph":{"type":"object","name":"Line","id":"p19656","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p19657","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p19658","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p19665","attributes":{"data_source":{"id":"p19611"},"view":{"type":"object","name":"CDSView","id":"p19666","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p19667"}}},"glyph":{"type":"object","name":"Scatter","id":"p19662","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p19663","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p19664","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p19622","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p19636"},{"type":"object","name":"BoxZoomTool","id":"p19637","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p19638","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p19644","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p19643","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p19645","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p19646"},{"type":"object","name":"SaveTool","id":"p19647"},{"type":"object","name":"HoverTool","id":"p19668","attributes":{"renderers":[{"id":"p19665"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p19631","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19632","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19633"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19634"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p19626","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19627","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19628"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19629"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p19630","attributes":{"axis":{"id":"p19626"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p19635","attributes":{"dimension":1,"axis":{"id":"p19631"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p19648","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p19650","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p19651","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p19652","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p19654","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p19653","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p19655","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"f7c12a43-9337-473c-a0bf-9f9d0a2b4164","roots":{"p19614":"ebe7195d-1b60-439d-bf37-e803a24e01c2"},"root_ids":["p19614"]}];
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

<div id="a0412a84-9948-43d9-9299-98752b75c2d3" data-root-id="p19674" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"e6a48d2a-5e5f-464d-a815-fb0239fbdd0c":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p19714","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p19715"}}},"roots":[{"type":"object","name":"Figure","id":"p19674","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p19675"},"y_range":{"type":"object","name":"DataRange1d","id":"p19676","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p19683"},"y_scale":{"type":"object","name":"LinearScale","id":"p19684"},"title":{"type":"object","name":"Title","id":"p19681","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p19710","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p19671","attributes":{"selected":{"type":"object","name":"Selection","id":"p19672","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p19673"},"data":{"type":"map","entries":[["year",[2000,2001,2002,2004,2005,2007,2008,2009,2010,2012,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[2,2,1,3,5,2,1,1,6,8,1,10,2,2,18,37,35,3,1,52,9,6]],["detected",[2,2,1,3,5,2,1,1,2,8,1,10,2,2,18,35,35,3,1,52,9,6]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p19711","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p19712"}}},"glyph":{"type":"object","name":"VBar","id":"p19707","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p19708","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p19709","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p19682","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p19695"},{"type":"object","name":"BoxZoomTool","id":"p19696","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p19697","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p19703","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p19702","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p19704","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p19705"},{"type":"object","name":"SaveTool","id":"p19706"},{"type":"object","name":"HoverTool","id":"p19713","attributes":{"renderers":[{"id":"p19710"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p19690","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19691","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19692"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19693"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p19685","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19686","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19687"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19688"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p19689","attributes":{"axis":{"id":"p19685"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p19694","attributes":{"dimension":1,"axis":{"id":"p19690"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"e6a48d2a-5e5f-464d-a815-fb0239fbdd0c","roots":{"p19674":"a0412a84-9948-43d9-9299-98752b75c2d3"},"root_ids":["p19674"]}];
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

<div id="aee911d4-38b6-444c-9c31-1e6e29ed2b5c" data-root-id="p19719" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"3d1becde-6a59-460a-8334-62550ba4cd27":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p19761","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p19762"}}},"roots":[{"type":"object","name":"Figure","id":"p19719","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p19721"},"y_range":{"type":"object","name":"FactorRange","id":"p19728","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p19729"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p19730"},"title":{"type":"object","name":"Title","id":"p19726","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p19756","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p19716","attributes":{"selected":{"type":"object","name":"Selection","id":"p19717","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p19718"},"data":{"type":"map","entries":[["x",[-17,-5,-14]],["y",["forward","reverse","reverse"]],["alpha",[1.0,1.0,1.0]],["pos",[17,5,14]],["base",["G","T","T"]],["n",[163,158,160]],["det_with",["99% of 163","100% of 158","100% of 160"]],["det_without",["95% of 42","91% of 47","91% of 45"]],["subs",["G&gt;A 163","T&gt;C 158","T&gt;A 160"]],["zone",["no","yes","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p19757","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p19758"}}},"glyph":{"type":"object","name":"Rect","id":"p19753","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p19754","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p19755","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p19727","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p19741"},{"type":"object","name":"BoxZoomTool","id":"p19742","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p19743","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p19749","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p19748","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p19750","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p19751"},{"type":"object","name":"SaveTool","id":"p19752"},{"type":"object","name":"HoverTool","id":"p19759","attributes":{"renderers":[{"id":"p19756"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p19736","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p19737"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p19738"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19739"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p19731","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p19760","attributes":{"ticks":[-17,-14,-5],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19733"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-17,"17"],[-5,"5"],[-14,"14"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p19734"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p19735","attributes":{"axis":{"id":"p19731"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p19740","attributes":{"dimension":1,"axis":{"id":"p19736"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"3d1becde-6a59-460a-8334-62550ba4cd27","roots":{"p19719":"aee911d4-38b6-444c-9c31-1e6e29ed2b5c"},"root_ids":["p19719"]}];
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

413 records were screened for this assay and **207 (50%)** were evaluable, meaning both primers landed in the right orientation and size range. 206 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 188 |
| `truncated` | 15 |
| `chance_anchor` | 3 |

