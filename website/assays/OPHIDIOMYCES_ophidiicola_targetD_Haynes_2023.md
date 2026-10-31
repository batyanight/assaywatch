# OPHIDIOMYCES_ophidiicola_targetD_Haynes_2023

<span class="aw-chip aw-chip-stable">stable</span>

**OPHIDIOMYCES OPHIDIICOLA — genotyping-panel target D, lineage-conserved qPCR locus (Haynes 2023)**

| | |
|---|---|
| Target | Ophidiomyces ophidiicola ([taxid 1387563](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1387563)) |
| Gene | target D, unannotated genomic segment shared by all six clades/lineages (position in paper's S1 Table, not in PDF) |
| Chemistry | hydrolysis_probe |
| Amplicon | 57 bp |
| Designed | 2023 |
| Paper | [10.1371/journal.pone.0289159](https://doi.org/10.1371/journal.pone.0289159) |
| Registry status | active |

!!! quote "The paper"
    Haynes E, Lorch J, Allender MC. Development and application of a qPCR-based genotyping assay for Ophidiomyces ophidiicola to investigate the epidemiology of ophidiomycosis. PLoS ONE e0289159 (published 3 August 2023).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `AGCGTTTTGCCCCAGCTA` | 18 nt |
| reverse | `GCAATGTTGCTCCGCAGTACT` | 21 nt |
| probe | `CTCGACTACGAAATCG` | 16 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 81 | 81 | 100.0% | 95.5% – 100.0% |
| baseline (everything earlier) | 0 | 0 | — | 0.0% – 100.0% |

Change from baseline, Newcombe interval: **-100.0% to 100.0%**. Threshold: **90.0%**.

*detected share 100.0% (95%-100%) since Oct 2021 (window widened to 60 months to reach 15 evaluable records)*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="b46967d0-98ed-4728-89a8-16cbbdc280b3" data-root-id="p19918" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"6ad02a2e-db52-4fd0-92b5-e2e623632703":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p19973","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p19974"}}},"roots":[{"type":"object","name":"Figure","id":"p19918","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p19920"},"y_range":{"type":"object","name":"Range1d","id":"p19927","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p19928"},"y_scale":{"type":"object","name":"LinearScale","id":"p19929"},"title":{"type":"object","name":"Title","id":"p19925","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p19963","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p19915","attributes":{"selected":{"type":"object","name":"Selection","id":"p19916","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p19917"},"data":{"type":"map","entries":[["year",[2022]],["share",[100.0]],["detected",[81]],["evaluable",[81]],["window",["recent"]],["size",[11.53494852413258]]]}}},"view":{"type":"object","name":"CDSView","id":"p19964","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p19965"}}},"glyph":{"type":"object","name":"Line","id":"p19960","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p19961","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p19962","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p19969","attributes":{"data_source":{"id":"p19915"},"view":{"type":"object","name":"CDSView","id":"p19970","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p19971"}}},"glyph":{"type":"object","name":"Scatter","id":"p19966","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p19967","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p19968","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p19926","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p19940"},{"type":"object","name":"BoxZoomTool","id":"p19941","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p19942","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p19948","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p19947","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p19949","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p19950"},{"type":"object","name":"SaveTool","id":"p19951"},{"type":"object","name":"HoverTool","id":"p19972","attributes":{"renderers":[{"id":"p19969"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p19935","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19936","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19937"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19938"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p19930","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19931","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19932"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19933"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p19934","attributes":{"axis":{"id":"p19930"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p19939","attributes":{"dimension":1,"axis":{"id":"p19935"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p19952","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2021.5,"right":{"type":"object","name":"Node","id":"p19954","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p19955","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p19956","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p19958","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p19957","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p19959","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"6ad02a2e-db52-4fd0-92b5-e2e623632703","roots":{"p19918":"b46967d0-98ed-4728-89a8-16cbbdc280b3"},"root_ids":["p19918"]}];
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

<div id="b06ca5c1-cb4e-479e-90f8-b3e55ab61b23" data-root-id="p19978" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"3bbbe6fc-0121-4299-a0f4-da012d152ddf":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20018","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20019"}}},"roots":[{"type":"object","name":"Figure","id":"p19978","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p19979"},"y_range":{"type":"object","name":"DataRange1d","id":"p19980","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p19987"},"y_scale":{"type":"object","name":"LinearScale","id":"p19988"},"title":{"type":"object","name":"Title","id":"p19985","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20014","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p19975","attributes":{"selected":{"type":"object","name":"Selection","id":"p19976","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p19977"},"data":{"type":"map","entries":[["year",[2022]],["evaluable",[81]],["detected",[81]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p20015","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20016"}}},"glyph":{"type":"object","name":"VBar","id":"p20011","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p20012","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p20013","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p19986","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p19999"},{"type":"object","name":"BoxZoomTool","id":"p20000","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20001","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20007","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20006","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20008","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20009"},{"type":"object","name":"SaveTool","id":"p20010"},{"type":"object","name":"HoverTool","id":"p20017","attributes":{"renderers":[{"id":"p20014"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p19994","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19995","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19996"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19997"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p19989","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19990","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19991"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19992"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p19993","attributes":{"axis":{"id":"p19989"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p19998","attributes":{"dimension":1,"axis":{"id":"p19994"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"3bbbe6fc-0121-4299-a0f4-da012d152ddf","roots":{"p19978":"b06ca5c1-cb4e-479e-90f8-b3e55ab61b23"},"root_ids":["p19978"]}];
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

<div id="c4949e05-37f6-4027-a252-4037b7fc35d1" data-root-id="p20023" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"3d077a8f-1e9a-4e9d-b9ca-9ea72fd80d58":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20065","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20066"}}},"roots":[{"type":"object","name":"Figure","id":"p20023","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p20025"},"y_range":{"type":"object","name":"FactorRange","id":"p20032","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p20033"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p20034"},"title":{"type":"object","name":"Title","id":"p20030","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20060","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20020","attributes":{"selected":{"type":"object","name":"Selection","id":"p20021","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20022"},"data":{"type":"map","entries":[["x",[-10,-4,-5,-7,-5,-6,-15,-1,-7,-8,-13,-17,-10,-13,-15,-9,-8,-11,-18,-12,-14,-18,-1,-2,-9,-14,-17,-19]],["y",["forward","reverse","reverse","reverse","forward","forward","forward","forward","forward","forward","forward","forward","reverse","reverse","reverse","forward","reverse","reverse","reverse","forward","forward","forward","reverse","reverse","reverse","reverse","reverse","reverse"]],["alpha",[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]],["pos",[10,4,5,7,5,6,15,1,7,8,13,17,10,13,15,9,8,11,18,12,14,18,1,2,9,14,17,19]],["base",["G","T","G","C","A","C","G","A","C","C","T","G","C","G","T","C","G","T","A","T","T","A","T","C","C","T","T","A"]],["n",[87,87,87,87,65,65,65,46,46,46,46,46,46,46,46,41,41,41,41,24,24,24,24,24,24,24,24,24]],["det_with",["0% of 87","0% of 87","0% of 87","0% of 87","0% of 65","0% of 65","0% of 65","0% of 46","0% of 46","0% of 46","0% of 46","0% of 46","0% of 46","0% of 46","0% of 46","0% of 41","0% of 41","0% of 41","0% of 41","0% of 24","0% of 24","0% of 24","0% of 24","0% of 24","0% of 24","0% of 24","0% of 24","0% of 24"]],["det_without",["77% of 105","77% of 105","77% of 105","77% of 105","64% of 127","64% of 127","64% of 127","55% of 146","55% of 146","55% of 146","55% of 146","55% of 146","55% of 146","55% of 146","55% of 146","54% of 151","54% of 151","54% of 151","54% of 151","48% of 168","48% of 168","48% of 168","48% of 168","48% of 168","48% of 168","48% of 168","48% of 168","48% of 168"]],["subs",["G&gt;T 46, G&gt;C 41","T&gt;G 46, T&gt;A 41","G&gt;C 87","C&gt;G 46, C&gt;A 41","A&gt;T 41, A&gt;C 24","C&gt;A 41, C&gt;T 24","G&gt;T 41, G&gt;A 24","A&gt;C 46","C&gt;T 46","C&gt;G 46","T&gt;G 46","G&gt;C 46","C&gt;A 46","G&gt;A 46","T&gt;A 46","C&gt;G 41","G&gt;A 41","T&gt;C 41","A&gt;G 41","T&gt;A 24","T&gt;G 24","A&gt;C 24","T&gt;C 24","C&gt;A 24","C&gt;T 24","T&gt;G 24","T&gt;A 24","A&gt;T 24"]],["zone",["no","yes","yes","no","yes","no","no","yes","no","no","no","no","no","no","no","no","no","no","no","no","no","no","yes","yes","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p20061","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20062"}}},"glyph":{"type":"object","name":"Rect","id":"p20057","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p20058","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p20059","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20031","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20045"},{"type":"object","name":"BoxZoomTool","id":"p20046","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20047","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20053","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20052","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20054","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20055"},{"type":"object","name":"SaveTool","id":"p20056"},{"type":"object","name":"HoverTool","id":"p20063","attributes":{"renderers":[{"id":"p20060"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p20040","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p20041"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p20042"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20043"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20035","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p20064","attributes":{"ticks":[-19,-18,-17,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20037"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-10,"10"],[-4,"4"],[-5,"5"],[-7,"7"],[-6,"6"],[-15,"15"],[-1,"1"],[-8,"8"],[-13,"13"],[-17,"17"],[-9,"9"],[-11,"11"],[-18,"18"],[-12,"12"],[-14,"14"],[-2,"2"],[-19,"19"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p20038"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20039","attributes":{"axis":{"id":"p20035"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20044","attributes":{"dimension":1,"axis":{"id":"p20040"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"3d077a8f-1e9a-4e9d-b9ca-9ea72fd80d58","roots":{"p20023":"c4949e05-37f6-4027-a252-4037b7fc35d1"},"root_ids":["p20023"]}];
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

<div id="a7800984-99d7-4cdb-bb97-0a0f3ca63744" data-root-id="p20070" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"6546a1a7-718e-443c-90f3-6fbc699612b9":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20119","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20120"}}},"roots":[{"type":"object","name":"Figure","id":"p20070","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p20079","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p20080","attributes":{"factors":["Ophidiomyces ophidiicola (1387563)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p20081"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p20082"},"title":{"type":"object","name":"Title","id":"p20077","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20114","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20067","attributes":{"selected":{"type":"object","name":"Selection","id":"p20068","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20069"},"data":{"type":"map","entries":[["y",["Ophidiomyces ophidiicola (1387563)"]],["share",[100.0]],["lo",[95.47219145675847]],["hi",[100.0]],["n",[81]],["det",[81]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p20115","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20116"}}},"glyph":{"type":"object","name":"Scatter","id":"p20111","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p20112","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p20113","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20078","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20093"},{"type":"object","name":"BoxZoomTool","id":"p20094","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20095","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20101","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20100","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20102","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20103"},{"type":"object","name":"SaveTool","id":"p20104"},{"type":"object","name":"HoverTool","id":"p20118","attributes":{"renderers":[{"id":"p20114"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p20088","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p20089"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p20090"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20091"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20083","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20084","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20085"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20086"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20087","attributes":{"axis":{"id":"p20083"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20092","attributes":{"dimension":1,"axis":{"id":"p20088"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p20105","attributes":{"source":{"id":"p20067"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p20117","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"6546a1a7-718e-443c-90f3-6fbc699612b9","roots":{"p20070":"a7800984-99d7-4cdb-bb97-0a0f3ca63744"},"root_ids":["p20070"]}];
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
"whole genome shotgun"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `retrieval_scope_incomplete`, `pairing_is_curator_reading`, `chemistry_detail_missing`, `thin_evidence`.


## What reached the statistics

25,593 records were screened for this assay and **81 (0%)** were evaluable, meaning both primers landed in the right orientation and size range. 25,512 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 25,185 |
| `chance_anchor` | 118 |
| `chance_pair` | 111 |
| `chance_only` | 98 |

