# BPSV_dsDNA_RPO147_J6R_TaqMan_Zhao_2013

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**BOVINE PAPULAR STOMATITIS VIRUS (dsDNA) — RPO147 J6R TaqMan (Zhao 2013)**

| | |
|---|---|
| Target | Bovine papular stomatitis virus ([taxid 129727](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=129727)) |
| Gene | RNA polymerase subunit RPO147 (ORF56 in ORFV IA82; vaccinia J6R homolog) |
| Chemistry | hydrolysis_probe |
| Amplicon | 91 bp |
| Designed | 2013 |
| Paper | [10.1016/j.jviromet.2013.08.027](https://doi.org/10.1016/j.jviromet.2013.08.027) |
| Registry status | draft |

!!! quote "The paper"
    Zhao H, Wilkins K, Damon IK, Li Y. 2013. Specific qPCR assays for the detection of orf virus, pseudocowpox virus and bovine papular stomatitis virus. J Virol Methods 194:229-234

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GAGATGATCTTGATGTTGTCGTACT` | 25 nt |
| reverse | `TGGGCATGATCGTGAAGTAC` | 20 nt |
| probe | `ATCATCGCGCGCTGGATCAC` | 20 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 10 | 10 | 100.0% | 72.2% – 100.0% |
| baseline (everything earlier) | 10 | 10 | 100.0% | 72.2% – 100.0% |

Change from baseline, Newcombe interval: **-27.8% to 27.8%**. Threshold: **90.0%**.

*10 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (72%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="d116bc16-65e5-448d-95a7-c38429750604" data-root-id="p5422" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"c72ef599-edd7-42bb-88de-5f284574a62c":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p5477","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p5478"}}},"roots":[{"type":"object","name":"Figure","id":"p5422","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p5424"},"y_range":{"type":"object","name":"Range1d","id":"p5431","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p5432"},"y_scale":{"type":"object","name":"LinearScale","id":"p5433"},"title":{"type":"object","name":"Title","id":"p5429","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p5467","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p5419","attributes":{"selected":{"type":"object","name":"Selection","id":"p5420","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p5421"},"data":{"type":"map","entries":[["year",[2003,2004,2009,2014,2015,2018,2023,2024,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[1,1,2,2,3,1,1,7,2]],["evaluable",[1,1,2,2,3,1,1,7,2]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.07684386569143,9.07684386569143,9.328625426046248,8.703135093227193,8.703135093227193,9.897626379762722,9.07684386569143]]]}}},"view":{"type":"object","name":"CDSView","id":"p5468","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p5469"}}},"glyph":{"type":"object","name":"Line","id":"p5464","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p5465","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p5466","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p5473","attributes":{"data_source":{"id":"p5419"},"view":{"type":"object","name":"CDSView","id":"p5474","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p5475"}}},"glyph":{"type":"object","name":"Scatter","id":"p5470","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p5471","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p5472","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p5430","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p5444"},{"type":"object","name":"BoxZoomTool","id":"p5445","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p5446","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p5452","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p5451","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p5453","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p5454"},{"type":"object","name":"SaveTool","id":"p5455"},{"type":"object","name":"HoverTool","id":"p5476","attributes":{"renderers":[{"id":"p5473"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p5439","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p5440","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5441"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5442"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p5434","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p5435","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5436"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5437"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p5438","attributes":{"axis":{"id":"p5434"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p5443","attributes":{"dimension":1,"axis":{"id":"p5439"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p5456","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2022.5,"right":{"type":"object","name":"Node","id":"p5458","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p5459","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p5460","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p5462","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p5461","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p5463","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"c72ef599-edd7-42bb-88de-5f284574a62c","roots":{"p5422":"d116bc16-65e5-448d-95a7-c38429750604"},"root_ids":["p5422"]}];
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

<div id="f764a05a-f6ec-4b35-bad7-8c59179281b9" data-root-id="p5482" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"e9746c8e-f859-4bc8-a2e8-a3735f790c91":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p5522","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p5523"}}},"roots":[{"type":"object","name":"Figure","id":"p5482","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p5483"},"y_range":{"type":"object","name":"DataRange1d","id":"p5484","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p5491"},"y_scale":{"type":"object","name":"LinearScale","id":"p5492"},"title":{"type":"object","name":"Title","id":"p5489","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p5518","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p5479","attributes":{"selected":{"type":"object","name":"Selection","id":"p5480","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p5481"},"data":{"type":"map","entries":[["year",[2003,2004,2009,2014,2015,2018,2023,2024,2026]],["evaluable",[1,1,2,2,3,1,1,7,2]],["detected",[1,1,2,2,3,1,1,7,2]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p5519","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p5520"}}},"glyph":{"type":"object","name":"VBar","id":"p5515","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p5516","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p5517","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p5490","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p5503"},{"type":"object","name":"BoxZoomTool","id":"p5504","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p5505","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p5511","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p5510","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p5512","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p5513"},{"type":"object","name":"SaveTool","id":"p5514"},{"type":"object","name":"HoverTool","id":"p5521","attributes":{"renderers":[{"id":"p5518"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p5498","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p5499","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5500"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5501"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p5493","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p5494","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5495"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5496"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p5497","attributes":{"axis":{"id":"p5493"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p5502","attributes":{"dimension":1,"axis":{"id":"p5498"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"e9746c8e-f859-4bc8-a2e8-a3735f790c91","roots":{"p5482":"f764a05a-f6ec-4b35-bad7-8c59179281b9"},"root_ids":["p5482"]}];
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

<div id="b8d1eb0f-b372-4d35-a7bf-db0c8f85ff71" data-root-id="p5527" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"d303cc38-b7e8-4ad9-87cd-39f992f99452":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p5569","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p5570"}}},"roots":[{"type":"object","name":"Figure","id":"p5527","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p5529"},"y_range":{"type":"object","name":"FactorRange","id":"p5536","attributes":{"factors":["probe"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p5537"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p5538"},"title":{"type":"object","name":"Title","id":"p5534","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p5564","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p5524","attributes":{"selected":{"type":"object","name":"Selection","id":"p5525","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p5526"},"data":{"type":"map","entries":[["x",[-3,-16,-15]],["y",["probe","probe","probe"]],["alpha",[1.0,1.0,1.0]],["pos",[3,16,15]],["base",["C","T","C"]],["n",[101,101,86]],["det_with",["0% of 101","0% of 101","0% of 86"]],["det_without",["100% of 21","100% of 21","58% of 36"]],["subs",["C&gt;G 101","T&gt;C 101","C&gt;G 86"]],["zone",["yes","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p5565","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p5566"}}},"glyph":{"type":"object","name":"Rect","id":"p5561","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p5562","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p5563","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p5535","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p5549"},{"type":"object","name":"BoxZoomTool","id":"p5550","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p5551","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p5557","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p5556","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p5558","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p5559"},{"type":"object","name":"SaveTool","id":"p5560"},{"type":"object","name":"HoverTool","id":"p5567","attributes":{"renderers":[{"id":"p5564"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p5544","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p5545"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p5546"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5547"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p5539","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p5568","attributes":{"ticks":[-16,-15,-3],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5541"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-3,"3"],[-16,"16"],[-15,"15"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p5542"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p5543","attributes":{"axis":{"id":"p5539"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p5548","attributes":{"dimension":1,"axis":{"id":"p5544"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"d303cc38-b7e8-4ad9-87cd-39f992f99452","roots":{"p5527":"b8d1eb0f-b372-4d35-a7bf-db0c8f85ff71"},"root_ids":["p5527"]}];
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

2,692 screened records fell outside the declared scope.

The paper claims this assay does **not** amplify 2 other taxa. Those are retrieved on purpose and reported as predicted cross-reactivity; they are never scored.

Disclosures on this entry: `amplicon_measured_not_published`, `thin_evidence`, `cross_reactive`, `chemistry_detail_missing`.


## What reached the statistics

127 records were screened for this assay and **20 (16%)** were evaluable, meaning both primers landed in the right orientation and size range. 107 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 88 |
| `chance_anchor` | 18 |
| `truncated` | 1 |

