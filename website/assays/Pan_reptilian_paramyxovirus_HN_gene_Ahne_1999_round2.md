# Pan_reptilian_paramyxovirus_HN_gene_Ahne_1999_round2

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**Pan-reptilian paramyxovirus — HN gene (nested)**

| | |
|---|---|
| Target | Ferlavirus ([taxid 1283308](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1283308)) |
| Gene | HN gene |
| Chemistry | conventional |
| Amplicon | 399 bp |
| Designed | 1999 |
| Paper | [10.1016/S0168-1702(99)00059-3](https://doi.org/10.1016/S0168-1702(99)00059-3) |
| Registry status | active |

!!! quote "The paper"
    Ahne W et al. 1999. Virus Res 63:65-74

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GCACTCTACCCCAGTGTTGG` | 20 nt |
| reverse | `TTCTATCCAGCTTATTCTTAT` | 21 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 6 | 6 | 100.0% | 61.0% – 100.0% |
| baseline (everything earlier) | 23 | 24 | 95.8% | 79.8% – 99.3% |

Change from baseline, Newcombe interval: **-35.0% to 20.2%**. Threshold: **90.0%**.

*6 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (61%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=0.814, 9 years); by footprint falling (p=0.738). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="a063e47d-da60-4e2d-8971-1cc258871d7a" data-root-id="p28290" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"a0177521-056d-4cdc-b2e2-563f9123528e":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p28345","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p28346"}}},"roots":[{"type":"object","name":"Figure","id":"p28290","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p28292"},"y_range":{"type":"object","name":"Range1d","id":"p28299","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p28300"},"y_scale":{"type":"object","name":"LinearScale","id":"p28301"},"title":{"type":"object","name":"Title","id":"p28297","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p28335","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p28287","attributes":{"selected":{"type":"object","name":"Selection","id":"p28288","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p28289"},"data":{"type":"map","entries":[["year",[2001,2003,2014,2017,2018,2019,2021,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,87.5,100.0,100.0,100.0]],["detected",[2,2,5,1,2,7,4,2,4]],["evaluable",[2,2,5,1,2,8,4,2,4]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,9.07684386569143,9.667366891029102,8.703135093227193,9.07684386569143,9.989711205477885,9.517227179437622,9.07684386569143,9.517227179437622]]]}}},"view":{"type":"object","name":"CDSView","id":"p28336","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p28337"}}},"glyph":{"type":"object","name":"Line","id":"p28332","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p28333","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p28334","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p28341","attributes":{"data_source":{"id":"p28287"},"view":{"type":"object","name":"CDSView","id":"p28342","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p28343"}}},"glyph":{"type":"object","name":"Scatter","id":"p28338","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p28339","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p28340","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p28298","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p28312"},{"type":"object","name":"BoxZoomTool","id":"p28313","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p28314","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p28320","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p28319","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p28321","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p28322"},{"type":"object","name":"SaveTool","id":"p28323"},{"type":"object","name":"HoverTool","id":"p28344","attributes":{"renderers":[{"id":"p28341"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p28307","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p28308","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28309"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28310"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p28302","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p28303","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28304"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28305"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p28306","attributes":{"axis":{"id":"p28302"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p28311","attributes":{"dimension":1,"axis":{"id":"p28307"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p28324","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2020.5,"right":{"type":"object","name":"Node","id":"p28326","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p28327","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p28328","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p28330","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p28329","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p28331","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"a0177521-056d-4cdc-b2e2-563f9123528e","roots":{"p28290":"a063e47d-da60-4e2d-8971-1cc258871d7a"},"root_ids":["p28290"]}];
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

<div id="d2c5987c-fab6-48e9-a80e-6d7fa60cefaf" data-root-id="p28350" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"1e5a779d-03a2-4ec8-9f2b-ede756bc4e74":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p28390","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p28391"}}},"roots":[{"type":"object","name":"Figure","id":"p28350","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p28351"},"y_range":{"type":"object","name":"DataRange1d","id":"p28352","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p28359"},"y_scale":{"type":"object","name":"LinearScale","id":"p28360"},"title":{"type":"object","name":"Title","id":"p28357","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p28386","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p28347","attributes":{"selected":{"type":"object","name":"Selection","id":"p28348","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p28349"},"data":{"type":"map","entries":[["year",[2001,2003,2014,2017,2018,2019,2021,2025,2026]],["evaluable",[2,2,5,1,2,8,4,2,4]],["detected",[2,2,5,1,2,7,4,2,4]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p28387","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p28388"}}},"glyph":{"type":"object","name":"VBar","id":"p28383","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p28384","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p28385","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p28358","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p28371"},{"type":"object","name":"BoxZoomTool","id":"p28372","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p28373","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p28379","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p28378","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p28380","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p28381"},{"type":"object","name":"SaveTool","id":"p28382"},{"type":"object","name":"HoverTool","id":"p28389","attributes":{"renderers":[{"id":"p28386"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p28366","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p28367","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28368"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28369"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p28361","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p28362","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28363"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28364"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p28365","attributes":{"axis":{"id":"p28361"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p28370","attributes":{"dimension":1,"axis":{"id":"p28366"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"1e5a779d-03a2-4ec8-9f2b-ede756bc4e74","roots":{"p28350":"d2c5987c-fab6-48e9-a80e-6d7fa60cefaf"},"root_ids":["p28350"]}];
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

<div id="bb8a90e7-1a04-4098-9fc4-43e36d7f2ed6" data-root-id="p28395" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"863e074e-3a08-4012-a439-be031aae7e6c":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p28437","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p28438"}}},"roots":[{"type":"object","name":"Figure","id":"p28395","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p28397"},"y_range":{"type":"object","name":"FactorRange","id":"p28404","attributes":{"factors":["forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p28405"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p28406"},"title":{"type":"object","name":"Title","id":"p28402","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p28432","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p28392","attributes":{"selected":{"type":"object","name":"Selection","id":"p28393","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p28394"},"data":{"type":"map","entries":[["x",[-9]],["y",["forward"]],["alpha",[1.0]],["pos",[9]],["base",["C"]],["n",[28]],["det_with",["96% of 28"]],["det_without",["100% of 2"]],["subs",["C&gt;T 16, C&gt;A 11, C&gt;G 1"]],["zone",["no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p28433","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p28434"}}},"glyph":{"type":"object","name":"Rect","id":"p28429","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p28430","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p28431","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p28403","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p28417"},{"type":"object","name":"BoxZoomTool","id":"p28418","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p28419","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p28425","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p28424","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p28426","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p28427"},{"type":"object","name":"SaveTool","id":"p28428"},{"type":"object","name":"HoverTool","id":"p28435","attributes":{"renderers":[{"id":"p28432"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p28412","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p28413"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p28414"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28415"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p28407","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p28436","attributes":{"ticks":[-9],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28409"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-9,"9"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p28410"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p28411","attributes":{"axis":{"id":"p28407"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p28416","attributes":{"dimension":1,"axis":{"id":"p28412"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"863e074e-3a08-4012-a439-be031aae7e6c","roots":{"p28395":"bb8a90e7-1a04-4098-9fc4-43e36d7f2ed6"},"root_ids":["p28395"]}];
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

61 records were screened for this assay and **30 (49%)** were evaluable, meaning both primers landed in the right orientation and size range. 31 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 31 |

