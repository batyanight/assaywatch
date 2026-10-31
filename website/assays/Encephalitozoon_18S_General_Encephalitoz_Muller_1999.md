# Encephalitozoon_18S_General_Encephalitoz_Muller_1999

<span class="aw-chip aw-chip-stable">stable</span>

**Encephalitozoon — 18S (General Encephalitozoon)**

| | |
|---|---|
| Target | Encephalitozoon ([taxid 6033](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=6033)) |
| Gene | 18S (General Encephalitozoon) |
| Chemistry | conventional |
| Amplicon | 279 bp |
| Designed | 1999 |
| Paper | [10.1128/CDLI.6.2.243-246.1999](https://doi.org/10.1128/CDLI.6.2.243-246.1999) |
| Registry status | active |

!!! quote "The paper"
    seed list: Müller A et al. 1999 Clin Diagn Lab Immunol; PMP1/PMP2 pan-microsporidial primers are usually credited to Fedorko DP et al. 1995 J Clin Microbiol 33:1739 — check which paper these sequences come from

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CACCAGGTTGATTCTGCCTGAC` | 22 nt |
| reverse | `CCTCTCCGGAACCAAACCCTG` | 21 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (48 months, from Oct 2022) | 33 | 33 | 100.0% | 89.6% – 100.0% |
| baseline (everything earlier) | 72 | 83 | 86.7% | 77.8% – 92.4% |

Change from baseline, Newcombe interval: **1.4% to 22.2%**. Threshold: **90.0%**.

*detected share 100.0% (90%-100%) since Oct 2022 (window widened to 48 months to reach 15 evaluable records)*

Trend across deposit years: by record rising (p=0.163, 19 years); by footprint falling (p=0.634); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="ef636a17-1d82-42ed-9f7e-13c0a4293b00" data-root-id="p12206" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"dde4becb-dd81-4450-bb47-e9eeecb56dd9":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12261","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12262"}}},"roots":[{"type":"object","name":"Figure","id":"p12206","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p12208"},"y_range":{"type":"object","name":"Range1d","id":"p12215","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p12216"},"y_scale":{"type":"object","name":"LinearScale","id":"p12217"},"title":{"type":"object","name":"Title","id":"p12213","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12251","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12203","attributes":{"selected":{"type":"object","name":"Selection","id":"p12204","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12205"},"data":{"type":"map","entries":[["year",[1993,1994,1995,1996,1998,1999,2000,2001,2006,2008,2010,2012,2013,2016,2021,2022,2023,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,0.0,100.0,100.0,66.66666666666666,100.0,100.0,100.0,96.15384615384616,100.0,100.0,100.0]],["detected",[6,1,3,3,2,5,1,4,0,2,8,8,2,1,3,25,22,3,6]],["evaluable",[6,1,3,3,2,5,1,4,6,2,8,12,2,1,3,26,22,3,6]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent"]],["size",[9.791719296345839,8.703135093227193,9.328625426046248,9.328625426046248,9.07684386569143,9.667366891029102,8.703135093227193,9.517227179437622,9.791719296345839,9.07684386569143,9.989711205477885,10.269703144398052,9.07684386569143,8.703135093227193,9.328625426046248,10.796415465069488,10.683957047019447,9.328625426046248,9.791719296345839]]]}}},"view":{"type":"object","name":"CDSView","id":"p12252","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12253"}}},"glyph":{"type":"object","name":"Line","id":"p12248","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p12249","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p12250","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p12257","attributes":{"data_source":{"id":"p12203"},"view":{"type":"object","name":"CDSView","id":"p12258","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12259"}}},"glyph":{"type":"object","name":"Scatter","id":"p12254","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p12255","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p12256","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12214","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12228"},{"type":"object","name":"BoxZoomTool","id":"p12229","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12230","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12236","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12235","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12237","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12238"},{"type":"object","name":"SaveTool","id":"p12239"},{"type":"object","name":"HoverTool","id":"p12260","attributes":{"renderers":[{"id":"p12257"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p12223","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12224","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12225"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12226"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12218","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12219","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12220"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12221"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12222","attributes":{"axis":{"id":"p12218"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12227","attributes":{"dimension":1,"axis":{"id":"p12223"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p12240","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2021.5,"right":{"type":"object","name":"Node","id":"p12242","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p12243","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p12244","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p12246","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12245","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p12247","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"dde4becb-dd81-4450-bb47-e9eeecb56dd9","roots":{"p12206":"ef636a17-1d82-42ed-9f7e-13c0a4293b00"},"root_ids":["p12206"]}];
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

<div id="c9d3123b-5601-4295-980e-1fb823d62004" data-root-id="p12266" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b16ecaca-f6fc-4237-893e-4eb4aeceab35":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12306","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12307"}}},"roots":[{"type":"object","name":"Figure","id":"p12266","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p12267"},"y_range":{"type":"object","name":"DataRange1d","id":"p12268","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p12275"},"y_scale":{"type":"object","name":"LinearScale","id":"p12276"},"title":{"type":"object","name":"Title","id":"p12273","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12302","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12263","attributes":{"selected":{"type":"object","name":"Selection","id":"p12264","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12265"},"data":{"type":"map","entries":[["year",[1993,1994,1995,1996,1998,1999,2000,2001,2006,2008,2010,2012,2013,2016,2021,2022,2023,2025,2026]],["evaluable",[6,1,3,3,2,5,1,4,6,2,8,12,2,1,3,26,22,3,6]],["detected",[6,1,3,3,2,5,1,4,0,2,8,8,2,1,3,25,22,3,6]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p12303","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12304"}}},"glyph":{"type":"object","name":"VBar","id":"p12299","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p12300","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p12301","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12274","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12287"},{"type":"object","name":"BoxZoomTool","id":"p12288","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12289","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12295","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12294","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12296","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12297"},{"type":"object","name":"SaveTool","id":"p12298"},{"type":"object","name":"HoverTool","id":"p12305","attributes":{"renderers":[{"id":"p12302"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p12282","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12283","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12284"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12285"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12277","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12278","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12279"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12280"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12281","attributes":{"axis":{"id":"p12277"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12286","attributes":{"dimension":1,"axis":{"id":"p12282"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b16ecaca-f6fc-4237-893e-4eb4aeceab35","roots":{"p12266":"c9d3123b-5601-4295-980e-1fb823d62004"},"root_ids":["p12266"]}];
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

<div id="a167d0ef-3065-470c-8253-4c049a7fcfa1" data-root-id="p12311" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"fd8c633c-e425-4d88-b89d-82e3c16a07de":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12353","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12354"}}},"roots":[{"type":"object","name":"Figure","id":"p12311","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p12313"},"y_range":{"type":"object","name":"FactorRange","id":"p12320","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p12321"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p12322"},"title":{"type":"object","name":"Title","id":"p12318","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12348","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12308","attributes":{"selected":{"type":"object","name":"Selection","id":"p12309","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12310"},"data":{"type":"map","entries":[["x",[-20,-10,-2]],["y",["forward","reverse","reverse"]],["alpha",[1.0,1.0,1.0]],["pos",[20,10,2]],["base",["C","C","T"]],["n",[72,71,32]],["det_with",["100% of 72","100% of 71","100% of 32"]],["det_without",["100% of 33","100% of 34","100% of 73"]],["subs",["C&gt;T 72","C&gt;T 70, C&gt;A 1","T&gt;C 32"]],["zone",["no","no","yes"]]]}}},"view":{"type":"object","name":"CDSView","id":"p12349","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12350"}}},"glyph":{"type":"object","name":"Rect","id":"p12345","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p12346","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p12347","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12319","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12333"},{"type":"object","name":"BoxZoomTool","id":"p12334","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12335","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12341","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12340","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12342","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12343"},{"type":"object","name":"SaveTool","id":"p12344"},{"type":"object","name":"HoverTool","id":"p12351","attributes":{"renderers":[{"id":"p12348"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p12328","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p12329"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p12330"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12331"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12323","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p12352","attributes":{"ticks":[-20,-10,-2],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12325"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-20,"20"],[-10,"10"],[-2,"2"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p12326"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12327","attributes":{"axis":{"id":"p12323"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12332","attributes":{"dimension":1,"axis":{"id":"p12328"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"fd8c633c-e425-4d88-b89d-82e3c16a07de","roots":{"p12311":"a167d0ef-3065-470c-8253-4c049a7fcfa1"},"root_ids":["p12311"]}];
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

9,091 records were screened for this assay and **116 (1%)** were evaluable, meaning both primers landed in the right orientation and size range. 8,975 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 8,688 |
| `chance_anchor` | 208 |
| `truncated` | 79 |

