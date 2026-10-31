# NOSEMA_bombi_SSU_Kato_2020

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**VAIRIMORPHA (NOSEMA) BOMBI — SSU rRNA conventional PCR, Klee 2006 primers as used in Kato 2020**

| | |
|---|---|
| Target | Vairimorpha bombi ([taxid 40135](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=40135)) |
| Gene | SSU rRNA |
| Chemistry | conventional |
| Amplicon | 323 bp |
| Designed | 2006 |
| Paper | [10.1016/j.jip.2005.10.012](https://doi.org/10.1016/j.jip.2005.10.012) |
| Registry status | active |

!!! quote "The paper"
    Klee, J.; Tek Tay, W.; Paxton, R. J. Specific and sensitive detection of Nosema bombi (Microsporidia: Nosematidae) in bumble bees (Bombus spp.; Hymenoptera: Apidae) by PCR of partial rRNA gene sequences. Journal of Invertebrate Pathology 2006, 91, 98-104.

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CCATGCATGTTTTTGAAGATTATTAT` | 26 nt |
| reverse | `CATATATTTTTAAAATATGAAACAATAA` | 28 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 9 | 9 | 100.0% | 70.1% – 100.0% |
| baseline (everything earlier) | 53 | 72 | 73.6% | 62.4% – 82.4% |

Change from baseline, Newcombe interval: **-4.8% to 37.6%**. Threshold: **90.0%**.

*9 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (70%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record rising (p=0.677, 9 years); by footprint rising (p=0.801). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="a31ac744-9f8a-46ae-baf9-6a84de9ff257" data-root-id="p19310" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"556ee6a9-896e-45df-88c3-2e735efdc512":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p19365","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p19366"}}},"roots":[{"type":"object","name":"Figure","id":"p19310","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p19312"},"y_range":{"type":"object","name":"Range1d","id":"p19319","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p19320"},"y_scale":{"type":"object","name":"LinearScale","id":"p19321"},"title":{"type":"object","name":"Title","id":"p19317","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p19355","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p19307","attributes":{"selected":{"type":"object","name":"Selection","id":"p19308","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p19309"},"data":{"type":"map","entries":[["year",[2001,2005,2009,2010,2011,2013,2014,2019,2022]],["share",[100.0,100.0,100.0,50.0,100.0,60.60606060606061,100.0,100.0,100.0]],["detected",[1,11,1,6,8,20,1,5,9]],["evaluable",[1,11,1,12,8,33,1,5,9]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent"]],["size",[8.703135093227193,10.209683151927734,8.703135093227193,10.269703144398052,9.989711205477885,10.955310988645032,8.703135093227193,9.667366891029102,10.071067811865476]]]}}},"view":{"type":"object","name":"CDSView","id":"p19356","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p19357"}}},"glyph":{"type":"object","name":"Line","id":"p19352","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p19353","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p19354","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p19361","attributes":{"data_source":{"id":"p19307"},"view":{"type":"object","name":"CDSView","id":"p19362","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p19363"}}},"glyph":{"type":"object","name":"Scatter","id":"p19358","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p19359","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p19360","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p19318","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p19332"},{"type":"object","name":"BoxZoomTool","id":"p19333","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p19334","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p19340","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p19339","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p19341","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p19342"},{"type":"object","name":"SaveTool","id":"p19343"},{"type":"object","name":"HoverTool","id":"p19364","attributes":{"renderers":[{"id":"p19361"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p19327","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19328","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19329"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19330"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p19322","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19323","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19324"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19325"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p19326","attributes":{"axis":{"id":"p19322"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p19331","attributes":{"dimension":1,"axis":{"id":"p19327"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p19344","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2021.5,"right":{"type":"object","name":"Node","id":"p19346","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p19347","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p19348","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p19350","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p19349","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p19351","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"556ee6a9-896e-45df-88c3-2e735efdc512","roots":{"p19310":"a31ac744-9f8a-46ae-baf9-6a84de9ff257"},"root_ids":["p19310"]}];
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

<div id="f77feffd-2d01-433a-9b2a-79bbfc045d75" data-root-id="p19370" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"19983d87-b53c-4b43-9aed-424c0e74334b":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p19410","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p19411"}}},"roots":[{"type":"object","name":"Figure","id":"p19370","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p19371"},"y_range":{"type":"object","name":"DataRange1d","id":"p19372","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p19379"},"y_scale":{"type":"object","name":"LinearScale","id":"p19380"},"title":{"type":"object","name":"Title","id":"p19377","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p19406","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p19367","attributes":{"selected":{"type":"object","name":"Selection","id":"p19368","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p19369"},"data":{"type":"map","entries":[["year",[2001,2005,2009,2010,2011,2013,2014,2019,2022]],["evaluable",[1,11,1,12,8,33,1,5,9]],["detected",[1,11,1,6,8,20,1,5,9]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p19407","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p19408"}}},"glyph":{"type":"object","name":"VBar","id":"p19403","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p19404","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p19405","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p19378","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p19391"},{"type":"object","name":"BoxZoomTool","id":"p19392","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p19393","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p19399","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p19398","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p19400","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p19401"},{"type":"object","name":"SaveTool","id":"p19402"},{"type":"object","name":"HoverTool","id":"p19409","attributes":{"renderers":[{"id":"p19406"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p19386","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19387","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19388"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19389"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p19381","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19382","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19383"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19384"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p19385","attributes":{"axis":{"id":"p19381"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p19390","attributes":{"dimension":1,"axis":{"id":"p19386"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"19983d87-b53c-4b43-9aed-424c0e74334b","roots":{"p19370":"f77feffd-2d01-433a-9b2a-79bbfc045d75"},"root_ids":["p19370"]}];
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

<div id="fab4d6b8-d056-4dab-99cb-7cb3ab3284df" data-root-id="p19415" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"a9fed7ef-641a-40c0-afce-abb139083921":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p19457","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p19458"}}},"roots":[{"type":"object","name":"Figure","id":"p19415","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p19417"},"y_range":{"type":"object","name":"FactorRange","id":"p19424","attributes":{"factors":["reverse"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p19425"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p19426"},"title":{"type":"object","name":"Title","id":"p19422","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p19452","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p19412","attributes":{"selected":{"type":"object","name":"Selection","id":"p19413","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p19414"},"data":{"type":"map","entries":[["x",[-16]],["y",["reverse"]],["alpha",[1.0]],["pos",[16]],["base",["A"]],["n",[22]],["det_with",["14% of 22"]],["det_without",["100% of 59"]],["subs",["A&gt;G 22"]],["zone",["no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p19453","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p19454"}}},"glyph":{"type":"object","name":"Rect","id":"p19449","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p19450","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p19451","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p19423","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p19437"},{"type":"object","name":"BoxZoomTool","id":"p19438","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p19439","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p19445","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p19444","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p19446","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p19447"},{"type":"object","name":"SaveTool","id":"p19448"},{"type":"object","name":"HoverTool","id":"p19455","attributes":{"renderers":[{"id":"p19452"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p19432","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p19433"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p19434"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19435"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p19427","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p19456","attributes":{"ticks":[-16],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19429"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-16,"16"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p19430"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p19431","attributes":{"axis":{"id":"p19427"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p19436","attributes":{"dimension":1,"axis":{"id":"p19432"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"a9fed7ef-641a-40c0-afce-abb139083921","roots":{"p19415":"fab4d6b8-d056-4dab-99cb-7cb3ab3284df"},"root_ids":["p19415"]}];
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

Retrieval query:

```
16S[Title] OR 18S[Title] OR "small subunit"[Title] OR SSU[Title] OR rRNA[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `oligos_from_secondary_source`.


## What reached the statistics

259 records were screened for this assay and **81 (31%)** were evaluable, meaning both primers landed in the right orientation and size range. 178 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 90 |
| `truncated` | 88 |

