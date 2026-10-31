# TILV_ssRNA_segment3_ME1_ME2_Kembou_2017

<span class="aw-chip aw-chip-stable">stable</span>

**TILAPIA LAKE VIRUS (ssRNA-) — segment 3 nested RT-PCR, ME1/ME2 (via Kembou Tsofack 2017)**

| | |
|---|---|
| Target | Tilapinevirus tilapiae (formerly Tilapia tilapinevirus; Tilapia lake virus, TiLV) ([taxid 2034996](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=2034996)) |
| Gene | segment 3 |
| Chemistry | conventional |
| Amplicon | 250 bp |
| Designed | 2017 |
| Paper | [10.1128/jcm.01808-16](https://doi.org/10.1128/jcm.01808-16) |
| Registry status | active |

!!! quote "The paper"
    Kembou Tsofack, J. E., Zamostiano, R., Watted, S., Berkowitz, A., Rosenbluth, E. et al. Detection of Tilapia Lake Virus in Clinical Samples by Culturing and Nested Reverse Transcription-PCR. Journal of Clinical Microbiology 55, 759-767 (2017).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GTTGGGCACAAGGCATCCTA` | 20 nt |
| reverse | `TATCACGTGCGTACTCGTTCAGT` | 23 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (48 months, from Oct 2022) | 23 | 25 | 92.0% | 75.0% – 97.8% |
| baseline (everything earlier) | 76 | 77 | 98.7% | 93.0% – 99.8% |

Change from baseline, Newcombe interval: **-23.7% to 1.4%**. Threshold: **90.0%**.

*detected share 92.0% (75%-98%) since Oct 2022 (window widened to 48 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=0.251, 10 years); by footprint falling (p=0.632). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="df787d44-25aa-40a9-b9cf-1b16569e6d44" data-root-id="p33462" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"df134481-3d9d-47c0-877b-440f5763cec6":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p33517","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p33518"}}},"roots":[{"type":"object","name":"Figure","id":"p33462","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p33464"},"y_range":{"type":"object","name":"Range1d","id":"p33471","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p33472"},"y_scale":{"type":"object","name":"LinearScale","id":"p33473"},"title":{"type":"object","name":"Title","id":"p33469","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p33507","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p33459","attributes":{"selected":{"type":"object","name":"Selection","id":"p33460","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p33461"},"data":{"type":"map","entries":[["year",[2014,2016,2017,2018,2019,2020,2022,2023,2024,2025]],["share",[100.0,100.0,100.0,100.0,100.0,93.33333333333333,100.0,83.33333333333334,100.0,100.0]],["detected",[1,2,4,14,25,14,16,10,9,4]],["evaluable",[1,2,4,14,25,15,16,12,9,4]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent"]],["size",[8.703135093227193,9.07684386569143,9.517227179437622,10.37579022724969,10.770092258092593,10.423139468338052,10.467343773689333,10.269703144398052,10.071067811865476,9.517227179437622]]]}}},"view":{"type":"object","name":"CDSView","id":"p33508","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33509"}}},"glyph":{"type":"object","name":"Line","id":"p33504","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p33505","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p33506","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p33513","attributes":{"data_source":{"id":"p33459"},"view":{"type":"object","name":"CDSView","id":"p33514","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33515"}}},"glyph":{"type":"object","name":"Scatter","id":"p33510","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p33511","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p33512","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p33470","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p33484"},{"type":"object","name":"BoxZoomTool","id":"p33485","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p33486","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p33492","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33491","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p33493","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p33494"},{"type":"object","name":"SaveTool","id":"p33495"},{"type":"object","name":"HoverTool","id":"p33516","attributes":{"renderers":[{"id":"p33513"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p33479","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33480","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33481"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33482"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p33474","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33475","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33476"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33477"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p33478","attributes":{"axis":{"id":"p33474"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p33483","attributes":{"dimension":1,"axis":{"id":"p33479"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p33496","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2021.5,"right":{"type":"object","name":"Node","id":"p33498","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p33499","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p33500","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p33502","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33501","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p33503","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"df134481-3d9d-47c0-877b-440f5763cec6","roots":{"p33462":"df787d44-25aa-40a9-b9cf-1b16569e6d44"},"root_ids":["p33462"]}];
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

<div id="e076b1ac-3fbe-46a9-bbb4-0aec9ca2af7f" data-root-id="p33522" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"d04070b2-840f-4739-a09b-3935511f3fab":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p33562","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p33563"}}},"roots":[{"type":"object","name":"Figure","id":"p33522","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p33523"},"y_range":{"type":"object","name":"DataRange1d","id":"p33524","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p33531"},"y_scale":{"type":"object","name":"LinearScale","id":"p33532"},"title":{"type":"object","name":"Title","id":"p33529","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p33558","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p33519","attributes":{"selected":{"type":"object","name":"Selection","id":"p33520","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p33521"},"data":{"type":"map","entries":[["year",[2014,2016,2017,2018,2019,2020,2022,2023,2024,2025]],["evaluable",[1,2,4,14,25,15,16,12,9,4]],["detected",[1,2,4,14,25,14,16,10,9,4]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p33559","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33560"}}},"glyph":{"type":"object","name":"VBar","id":"p33555","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p33556","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p33557","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p33530","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p33543"},{"type":"object","name":"BoxZoomTool","id":"p33544","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p33545","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p33551","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33550","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p33552","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p33553"},{"type":"object","name":"SaveTool","id":"p33554"},{"type":"object","name":"HoverTool","id":"p33561","attributes":{"renderers":[{"id":"p33558"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p33538","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33539","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33540"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33541"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p33533","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33534","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33535"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33536"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p33537","attributes":{"axis":{"id":"p33533"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p33542","attributes":{"dimension":1,"axis":{"id":"p33538"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"d04070b2-840f-4739-a09b-3935511f3fab","roots":{"p33522":"e076b1ac-3fbe-46a9-bbb4-0aec9ca2af7f"},"root_ids":["p33522"]}];
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

<div id="afe4dabf-b826-479c-9ce6-49ba5bdc821a" data-root-id="p33567" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"d307de2c-406d-4258-848b-7b775f7c950f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p33609","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p33610"}}},"roots":[{"type":"object","name":"Figure","id":"p33567","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p33569"},"y_range":{"type":"object","name":"FactorRange","id":"p33576","attributes":{"factors":["reverse"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p33577"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p33578"},"title":{"type":"object","name":"Title","id":"p33574","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p33604","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p33564","attributes":{"selected":{"type":"object","name":"Selection","id":"p33565","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p33566"},"data":{"type":"map","entries":[["x",[-22]],["y",["reverse"]],["alpha",[1.0]],["pos",[22]],["base",["A"]],["n",[33]],["det_with",["94% of 33"]],["det_without",["99% of 69"]],["subs",["A&gt;G 32, A&gt;C 1"]],["zone",["no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p33605","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33606"}}},"glyph":{"type":"object","name":"Rect","id":"p33601","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p33602","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p33603","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p33575","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p33589"},{"type":"object","name":"BoxZoomTool","id":"p33590","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p33591","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p33597","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33596","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p33598","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p33599"},{"type":"object","name":"SaveTool","id":"p33600"},{"type":"object","name":"HoverTool","id":"p33607","attributes":{"renderers":[{"id":"p33604"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p33584","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p33585"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p33586"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33587"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p33579","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p33608","attributes":{"ticks":[-22],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33581"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-22,"22"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p33582"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p33583","attributes":{"axis":{"id":"p33579"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p33588","attributes":{"dimension":1,"axis":{"id":"p33584"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"d307de2c-406d-4258-848b-7b775f7c950f","roots":{"p33567":"afe4dabf-b826-479c-9ce6-49ba5bdc821a"},"root_ids":["p33567"]}];
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

Disclosures on this entry: `thin_evidence`, `citation_is_indirect`.


## What reached the statistics

612 records were screened for this assay and **102 (17%)** were evaluable, meaning both primers landed in the right orientation and size range. 510 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 426 |
| `truncated` | 56 |
| `chance_anchor` | 28 |

