# DWVA_polyprotein_Rossi_2024

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**DEFORMED WING VIRUS A — polyprotein gene RT-qPCR, MGB probe (Rossi 2024)**

| | |
|---|---|
| Target | Deformed wing virus A ([taxid 2951794](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=2951794)) |
| Gene | polyprotein gene |
| Chemistry | mgb |
| Amplicon | 139 bp |
| Designed | 2024 |
| Paper | [10.3390/microorganisms12061105](https://doi.org/10.3390/microorganisms12061105) |
| Registry status | active |

!!! quote "The paper"
    Rossi, F.; Del Matto, I.; Ricchiuti, L.; Marino, L. Selection and Multiplexing of Reverse Transcription–Quantitative PCR Tests Targeting Relevant Honeybee Viral Pathogens. Microorganisms 2024, 12, 1105.

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CTTTGTCTTCATTAAAGCCAC` | 21 nt |
| reverse | `CTCATTAACTGTGTCGTTGAT` | 21 nt |
| probe | `TGCGTGGAATGCGTCC` | 16 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 23 | 47 | 48.9% | 35.3% – 62.8% |
| baseline (everything earlier) | 35 | 40 | 87.5% | 73.9% – 94.5% |

Change from baseline, Newcombe interval: **-53.9% to -19.2%**. Threshold: **90.0%**.

*detected share 48.9% (35%-63%) since Oct 2024, upper bound below the 90% threshold; change from baseline -54% to -19% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 88%)*

Trend across deposit years: by record falling (p=0.00812, 5 years); by footprint falling (p=0.0323). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="d544ef2d-7ef3-4453-8194-192a035efec2" data-root-id="p10973" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"4cd3b216-5e5b-409a-85fe-821f0863da8f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p11028","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p11029"}}},"roots":[{"type":"object","name":"Figure","id":"p10973","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p10975"},"y_range":{"type":"object","name":"Range1d","id":"p10982","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p10983"},"y_scale":{"type":"object","name":"LinearScale","id":"p10984"},"title":{"type":"object","name":"Title","id":"p10980","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p11018","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p10970","attributes":{"selected":{"type":"object","name":"Selection","id":"p10971","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p10972"},"data":{"type":"map","entries":[["year",[2022,2023,2024,2025,2026]],["share",[83.33333333333334,87.5,100.0,23.809523809523807,69.23076923076923]],["detected",[5,28,2,5,18]],["evaluable",[6,32,2,21,26]],["window",["baseline","baseline","recent","recent","recent"]],["size",[9.791719296345839,10.934913263353746,9.07684386569143,10.652487636092928,10.796415465069488]]]}}},"view":{"type":"object","name":"CDSView","id":"p11019","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p11020"}}},"glyph":{"type":"object","name":"Line","id":"p11015","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p11016","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p11017","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p11024","attributes":{"data_source":{"id":"p10970"},"view":{"type":"object","name":"CDSView","id":"p11025","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p11026"}}},"glyph":{"type":"object","name":"Scatter","id":"p11021","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p11022","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p11023","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p10981","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p10995"},{"type":"object","name":"BoxZoomTool","id":"p10996","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p10997","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p11003","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p11002","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p11004","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p11005"},{"type":"object","name":"SaveTool","id":"p11006"},{"type":"object","name":"HoverTool","id":"p11027","attributes":{"renderers":[{"id":"p11024"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p10990","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p10991","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p10992"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p10993"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p10985","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p10986","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p10987"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p10988"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p10989","attributes":{"axis":{"id":"p10985"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p10994","attributes":{"dimension":1,"axis":{"id":"p10990"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p11007","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p11009","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p11010","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p11011","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p11013","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p11012","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p11014","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"4cd3b216-5e5b-409a-85fe-821f0863da8f","roots":{"p10973":"d544ef2d-7ef3-4453-8194-192a035efec2"},"root_ids":["p10973"]}];
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

<div id="f7119aeb-57d5-49dd-86e0-bd1e9f3c9a81" data-root-id="p11033" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"3a5ad9bd-c543-4898-8125-4424e3d53bd7":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p11073","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p11074"}}},"roots":[{"type":"object","name":"Figure","id":"p11033","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p11034"},"y_range":{"type":"object","name":"DataRange1d","id":"p11035","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p11042"},"y_scale":{"type":"object","name":"LinearScale","id":"p11043"},"title":{"type":"object","name":"Title","id":"p11040","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p11069","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p11030","attributes":{"selected":{"type":"object","name":"Selection","id":"p11031","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p11032"},"data":{"type":"map","entries":[["year",[2022,2023,2024,2025,2026]],["evaluable",[6,32,2,21,26]],["detected",[5,28,2,5,18]],["colour",["#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p11070","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p11071"}}},"glyph":{"type":"object","name":"VBar","id":"p11066","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p11067","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p11068","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p11041","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p11054"},{"type":"object","name":"BoxZoomTool","id":"p11055","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p11056","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p11062","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p11061","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p11063","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p11064"},{"type":"object","name":"SaveTool","id":"p11065"},{"type":"object","name":"HoverTool","id":"p11072","attributes":{"renderers":[{"id":"p11069"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p11049","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p11050","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p11051"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11052"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p11044","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p11045","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p11046"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11047"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p11048","attributes":{"axis":{"id":"p11044"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p11053","attributes":{"dimension":1,"axis":{"id":"p11049"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"3a5ad9bd-c543-4898-8125-4424e3d53bd7","roots":{"p11033":"f7119aeb-57d5-49dd-86e0-bd1e9f3c9a81"},"root_ids":["p11033"]}];
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

<div id="d096ded5-983a-4830-b4aa-a35f2a670cf5" data-root-id="p11078" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9d941f70-1af5-47c4-9dee-341d9587e6ca":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p11120","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p11121"}}},"roots":[{"type":"object","name":"Figure","id":"p11078","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p11080"},"y_range":{"type":"object","name":"FactorRange","id":"p11087","attributes":{"factors":["reverse"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p11088"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p11089"},"title":{"type":"object","name":"Title","id":"p11085","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p11115","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p11075","attributes":{"selected":{"type":"object","name":"Selection","id":"p11076","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p11077"},"data":{"type":"map","entries":[["x",[-4,-7]],["y",["reverse","reverse"]],["alpha",[1.0,1.0]],["pos",[4,7]],["base",["T","C"]],["n",[25,29]],["det_with",["16% of 25","21% of 29"]],["det_without",["87% of 62","90% of 58"]],["subs",["T&gt;C 25","C&gt;T 29"]],["zone",["yes","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p11116","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p11117"}}},"glyph":{"type":"object","name":"Rect","id":"p11112","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p11113","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p11114","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p11086","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p11100"},{"type":"object","name":"BoxZoomTool","id":"p11101","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p11102","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p11108","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p11107","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p11109","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p11110"},{"type":"object","name":"SaveTool","id":"p11111"},{"type":"object","name":"HoverTool","id":"p11118","attributes":{"renderers":[{"id":"p11115"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p11095","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p11096"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p11097"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11098"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p11090","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p11119","attributes":{"ticks":[-7,-4],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p11092"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-4,"4"],[-7,"7"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p11093"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p11094","attributes":{"axis":{"id":"p11090"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p11099","attributes":{"dimension":1,"axis":{"id":"p11095"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9d941f70-1af5-47c4-9dee-341d9587e6ca","roots":{"p11078":"d096ded5-983a-4830-b4aa-a35f2a670cf5"},"root_ids":["p11078"]}];
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

<div id="cd31406f-4c70-4624-8ece-763f8d828b75" data-root-id="p11125" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"deff70b7-c526-472f-af2e-898865d704ae":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p11174","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p11175"}}},"roots":[{"type":"object","name":"Figure","id":"p11125","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p11134","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p11135","attributes":{"factors":["Iflavirus aladeformis (3047792)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p11136"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p11137"},"title":{"type":"object","name":"Title","id":"p11132","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p11169","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p11122","attributes":{"selected":{"type":"object","name":"Selection","id":"p11123","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p11124"},"data":{"type":"map","entries":[["y",["Iflavirus aladeformis (3047792)"]],["share",[48.93617021276596]],["lo",[35.275555033682146]],["hi",[62.75754625177314]],["n",[47]],["det",[23]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p11170","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p11171"}}},"glyph":{"type":"object","name":"Scatter","id":"p11166","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p11167","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p11168","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p11133","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p11148"},{"type":"object","name":"BoxZoomTool","id":"p11149","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p11150","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p11156","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p11155","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p11157","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p11158"},{"type":"object","name":"SaveTool","id":"p11159"},{"type":"object","name":"HoverTool","id":"p11173","attributes":{"renderers":[{"id":"p11169"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p11143","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p11144"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p11145"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11146"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p11138","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p11139","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p11140"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11141"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p11142","attributes":{"axis":{"id":"p11138"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p11147","attributes":{"dimension":1,"axis":{"id":"p11143"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p11160","attributes":{"source":{"id":"p11122"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p11172","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"deff70b7-c526-472f-af2e-898865d704ae","roots":{"p11125":"cd31406f-4c70-4624-8ece-763f8d828b75"},"root_ids":["p11125"]}];
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

Disclosures on this entry: `oligos_from_secondary_source`, `scope_narrower_than_taxid`.


## What reached the statistics

245 records were screened for this assay and **87 (36%)** were evaluable, meaning both primers landed in the right orientation and size range. 158 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 142 |
| `truncated` | 16 |

