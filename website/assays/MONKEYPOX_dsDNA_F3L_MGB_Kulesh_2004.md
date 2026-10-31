# MONKEYPOX_dsDNA_F3L_MGB_Kulesh_2004

<span class="aw-chip aw-chip-stable">stable</span>

**MONKEYPOX virus (dsDNA) — F3L MGB TaqMan (Kulesh 2004)**

| | |
|---|---|
| Target | Monkeypox virus ([taxid 10244](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10244)) |
| Gene | F3L |
| Chemistry | mgb |
| Amplicon | 107 bp |
| Designed | 2004 |
| Paper | [10.1038/labinvest.3700143](https://doi.org/10.1038/labinvest.3700143) |
| Registry status | active |

!!! quote "The paper"
    Kulesh DA, Loveless BM, Norwood D, Garrison J, Whitehouse CA, Hartmann C, Mucker E, Miller D, Wasieloski LP Jr, Huggins J, Huhn G, Miser LL, Imig C, Martinez M, Larsen T, Rossi CA, Ludwig GV. 2004. Monkeypox virus detection in rodents using real-time 3'-minor groove binder TaqMan assays on the Roche LightCycler. Lab Invest 84:1200-1208

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CTCATTGATTTTTCGCGGGATA` | 22 nt |
| reverse | `GACGATACTCCTCCTCGTTGGT` | 22 nt |
| probe | `CATCAGAATCTGTAGGCCGT` | 20 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 4,455 | 4,920 | 90.5% | 89.7% – 91.3% |
| baseline (everything earlier) | 8,497 | 8,564 | 99.2% | 99.0% – 99.4% |

Change from baseline, Newcombe interval: **-9.5% to -7.9%**. Threshold: **90.0%**.

*detected share 90.5% (90%-91%) since Oct 2024*

Trend across deposit years: by record falling (p=2.26e-121, 16 years); by footprint falling (p=0.0376). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="bec2954f-262d-4196-82a2-6a9b0435c8f9" data-root-id="p17090" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"c38719ce-ef30-4336-9e07-4eeaa2102e9f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17145","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17146"}}},"roots":[{"type":"object","name":"Figure","id":"p17090","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p17092"},"y_range":{"type":"object","name":"Range1d","id":"p17099","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p17100"},"y_scale":{"type":"object","name":"LinearScale","id":"p17101"},"title":{"type":"object","name":"Title","id":"p17097","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17135","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17087","attributes":{"selected":{"type":"object","name":"Selection","id":"p17088","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17089"},"data":{"type":"map","entries":[["year",[2001,2004,2005,2010,2011,2013,2014,2015,2018,2019,2020,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,33.33333333333333,100.0,100.0,100.0,100.0,100.0,100.0,100.0,99.88388969521044,99.77642925582882,97.09385421629348,94.27662957074722,87.59744861800142]],["detected",[2,1,7,1,2,2,24,11,3,8,37,3441,3124,2038,1779,2472]],["evaluable",[2,1,7,3,2,2,24,11,3,8,37,3445,3131,2099,1887,2822]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,8.703135093227193,9.897626379762722,9.328625426046248,9.07684386569143,9.07684386569143,10.74264168206181,10.209683151927734,9.328625426046248,9.989711205477885,11.030852377887435,13.65048739860295,13.601676463401796,13.394973899358671,13.339248026285627,13.548353992622403]]]}}},"view":{"type":"object","name":"CDSView","id":"p17136","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17137"}}},"glyph":{"type":"object","name":"Line","id":"p17132","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p17133","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p17134","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p17141","attributes":{"data_source":{"id":"p17087"},"view":{"type":"object","name":"CDSView","id":"p17142","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17143"}}},"glyph":{"type":"object","name":"Scatter","id":"p17138","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p17139","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p17140","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17098","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17112"},{"type":"object","name":"BoxZoomTool","id":"p17113","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17114","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17120","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17119","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17121","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17122"},{"type":"object","name":"SaveTool","id":"p17123"},{"type":"object","name":"HoverTool","id":"p17144","attributes":{"renderers":[{"id":"p17141"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p17107","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17108","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17109"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17110"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17102","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17103","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17104"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17105"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17106","attributes":{"axis":{"id":"p17102"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17111","attributes":{"dimension":1,"axis":{"id":"p17107"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p17124","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p17126","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p17127","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p17128","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p17130","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17129","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p17131","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"c38719ce-ef30-4336-9e07-4eeaa2102e9f","roots":{"p17090":"bec2954f-262d-4196-82a2-6a9b0435c8f9"},"root_ids":["p17090"]}];
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

<div id="eeaf4106-8ed7-4215-8592-4ca5320c20e8" data-root-id="p17150" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"049fdd78-ffff-4b43-981b-cb0825c11c7e":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17190","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17191"}}},"roots":[{"type":"object","name":"Figure","id":"p17150","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p17151"},"y_range":{"type":"object","name":"DataRange1d","id":"p17152","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p17159"},"y_scale":{"type":"object","name":"LinearScale","id":"p17160"},"title":{"type":"object","name":"Title","id":"p17157","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17186","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17147","attributes":{"selected":{"type":"object","name":"Selection","id":"p17148","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17149"},"data":{"type":"map","entries":[["year",[2001,2004,2005,2010,2011,2013,2014,2015,2018,2019,2020,2022,2023,2024,2025,2026]],["evaluable",[2,1,7,3,2,2,24,11,3,8,37,3445,3131,2099,1887,2822]],["detected",[2,1,7,1,2,2,24,11,3,8,37,3441,3124,2038,1779,2472]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p17187","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17188"}}},"glyph":{"type":"object","name":"VBar","id":"p17183","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p17184","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p17185","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17158","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17171"},{"type":"object","name":"BoxZoomTool","id":"p17172","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17173","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17179","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17178","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17180","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17181"},{"type":"object","name":"SaveTool","id":"p17182"},{"type":"object","name":"HoverTool","id":"p17189","attributes":{"renderers":[{"id":"p17186"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p17166","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17167","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17168"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17169"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17161","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17162","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17163"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17164"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17165","attributes":{"axis":{"id":"p17161"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17170","attributes":{"dimension":1,"axis":{"id":"p17166"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"049fdd78-ffff-4b43-981b-cb0825c11c7e","roots":{"p17150":"eeaf4106-8ed7-4215-8592-4ca5320c20e8"},"root_ids":["p17150"]}];
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

<div id="addb793f-a400-40a1-b6a6-e7c9ad00cc7c" data-root-id="p17195" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"c766ccbc-febb-4a01-baf1-eacc642a89f5":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17237","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17238"}}},"roots":[{"type":"object","name":"Figure","id":"p17195","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p17197"},"y_range":{"type":"object","name":"FactorRange","id":"p17204","attributes":{"factors":["reverse"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p17205"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p17206"},"title":{"type":"object","name":"Title","id":"p17202","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17232","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17192","attributes":{"selected":{"type":"object","name":"Selection","id":"p17193","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17194"},"data":{"type":"map","entries":[["x",[-7,-22]],["y",["reverse","reverse"]],["alpha",[0.18353604271729457,1.0]],["pos",[7,22]],["base",["C","G"]],["n",[133,10074]],["det_with",["1% of 133","99% of 10074"]],["det_without",["100% of 12971","100% of 3030"]],["subs",["C&gt;T 132, C&gt;A 1","G&gt;A 10074"]],["zone",["no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p17233","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17234"}}},"glyph":{"type":"object","name":"Rect","id":"p17229","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p17230","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p17231","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17203","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17217"},{"type":"object","name":"BoxZoomTool","id":"p17218","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17219","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17225","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17224","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17226","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17227"},{"type":"object","name":"SaveTool","id":"p17228"},{"type":"object","name":"HoverTool","id":"p17235","attributes":{"renderers":[{"id":"p17232"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p17212","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p17213"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p17214"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17215"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17207","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p17236","attributes":{"ticks":[-22,-7],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17209"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-7,"7"],[-22,"22"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p17210"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17211","attributes":{"axis":{"id":"p17207"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17216","attributes":{"dimension":1,"axis":{"id":"p17212"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"c766ccbc-febb-4a01-baf1-eacc642a89f5","roots":{"p17195":"addb793f-a400-40a1-b6a6-e7c9ad00cc7c"},"root_ids":["p17195"]}];
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

<div id="db97d98c-0f58-4d40-bfa3-afc794a4b5a6" data-root-id="p17242" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"1059afa8-62e6-4e93-beda-4c21247e2c58":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17291","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17292"}}},"roots":[{"type":"object","name":"Figure","id":"p17242","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p17251","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p17252","attributes":{"factors":["Orthopoxvirus monkeypox (3431483)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p17253"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p17254"},"title":{"type":"object","name":"Title","id":"p17249","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17286","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17239","attributes":{"selected":{"type":"object","name":"Selection","id":"p17240","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17241"},"data":{"type":"map","entries":[["y",["Orthopoxvirus monkeypox (3431483)"]],["share",[97.18586387434554]],["lo",[96.66618660224803]],["hi",[97.6265224817315]],["n",[4584]],["det",[4455]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p17287","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17288"}}},"glyph":{"type":"object","name":"Scatter","id":"p17283","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p17284","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p17285","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17250","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17265"},{"type":"object","name":"BoxZoomTool","id":"p17266","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17267","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17273","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17272","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17274","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17275"},{"type":"object","name":"SaveTool","id":"p17276"},{"type":"object","name":"HoverTool","id":"p17290","attributes":{"renderers":[{"id":"p17286"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p17260","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p17261"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p17262"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17263"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17255","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17256","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17257"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17258"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17259","attributes":{"axis":{"id":"p17255"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17264","attributes":{"dimension":1,"axis":{"id":"p17260"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p17277","attributes":{"source":{"id":"p17239"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p17289","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"1059afa8-62e6-4e93-beda-4c21247e2c58","roots":{"p17242":"db97d98c-0f58-4d40-bfa3-afc794a4b5a6"},"root_ids":["p17242"]}];
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

14,204 records were screened for this assay and **13,484 (95%)** were evaluable, meaning both primers landed in the right orientation and size range. 720 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 706 |
| `chance_anchor` | 5 |

