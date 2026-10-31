# ORTHOBORNAVIRUS_XP_passerine_Sigrist_2021

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**AVIAN ORTHOBORNAVIRUS — X/P triplex qPCR, passerine probe (Sigrist 2021)**

| | |
|---|---|
| Target | Orthobornavirus ([taxid 186458](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=186458)) |
| Gene | X/P |
| Chemistry | hydrolysis_probe |
| Amplicon | 123 bp |
| Designed | 2021 |
| Paper | [10.3390/v13071358](https://doi.org/10.3390/v13071358) |
| Registry status | active |

!!! quote "The paper"
    Sigrist, B., Geers, J., Albini, S., Rubbenstroth, D. & Wolfrum, N. A New Multiplex Real-Time RT-PCR for Simultaneous Detection and Differentiation of Avian Bornaviruses. Viruses 13, 1358 (2021).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CCCGCAGACAGYACGT` | 16 nt |
| reverse | `GAGATCATGGANGGRTTCTT` | 20 nt |
| probe | `AGATGCATTGACCCARCCRGT` | 21 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 2 | 4 | 50.0% | 15.0% – 85.0% |
| baseline (everything earlier) | 18 | 23 | 78.3% | 58.1% – 90.3% |

Change from baseline, Newcombe interval: **-65.3% to 12.1%**. Threshold: **90.0%**.

*4 evaluable records since Oct 2021, below the minimum of 15; the detected share is 50% (15%-85%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=0.221, 8 years); by footprint rising (p=0.98); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="efbff0bc-0224-4c78-b4d9-2bf3ab781578" data-root-id="p20428" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"65a88a59-5996-4719-8f8b-e2604fc4ee3d":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20483","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20484"}}},"roots":[{"type":"object","name":"Figure","id":"p20428","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p20430"},"y_range":{"type":"object","name":"Range1d","id":"p20437","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p20438"},"y_scale":{"type":"object","name":"LinearScale","id":"p20439"},"title":{"type":"object","name":"Title","id":"p20435","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20473","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20425","attributes":{"selected":{"type":"object","name":"Selection","id":"p20426","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20427"},"data":{"type":"map","entries":[["year",[2012,2013,2014,2016,2018,2023,2024,2026]],["share",[100.0,75.0,100.0,87.5,0.0,0.0,100.0,50.0]],["detected",[1,9,1,7,0,0,1,1]],["evaluable",[1,12,1,8,1,1,1,2]],["window",["baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,10.269703144398052,8.703135093227193,9.989711205477885,8.703135093227193,8.703135093227193,8.703135093227193,9.07684386569143]]]}}},"view":{"type":"object","name":"CDSView","id":"p20474","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20475"}}},"glyph":{"type":"object","name":"Line","id":"p20470","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p20471","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p20472","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p20479","attributes":{"data_source":{"id":"p20425"},"view":{"type":"object","name":"CDSView","id":"p20480","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20481"}}},"glyph":{"type":"object","name":"Scatter","id":"p20476","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p20477","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p20478","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20436","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20450"},{"type":"object","name":"BoxZoomTool","id":"p20451","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20452","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20458","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20457","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20459","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20460"},{"type":"object","name":"SaveTool","id":"p20461"},{"type":"object","name":"HoverTool","id":"p20482","attributes":{"renderers":[{"id":"p20479"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p20445","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20446","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20447"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20448"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20440","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20441","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20442"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20443"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20444","attributes":{"axis":{"id":"p20440"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20449","attributes":{"dimension":1,"axis":{"id":"p20445"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p20462","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2022.5,"right":{"type":"object","name":"Node","id":"p20464","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p20465","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p20466","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p20468","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20467","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p20469","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"65a88a59-5996-4719-8f8b-e2604fc4ee3d","roots":{"p20428":"efbff0bc-0224-4c78-b4d9-2bf3ab781578"},"root_ids":["p20428"]}];
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

<div id="b61b22b9-419b-4c89-a6ff-50cb14ca5880" data-root-id="p20488" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"d82eeeba-5822-4e45-840c-94743f0e3b26":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20528","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20529"}}},"roots":[{"type":"object","name":"Figure","id":"p20488","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p20489"},"y_range":{"type":"object","name":"DataRange1d","id":"p20490","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p20497"},"y_scale":{"type":"object","name":"LinearScale","id":"p20498"},"title":{"type":"object","name":"Title","id":"p20495","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20524","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20485","attributes":{"selected":{"type":"object","name":"Selection","id":"p20486","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20487"},"data":{"type":"map","entries":[["year",[2012,2013,2014,2016,2018,2023,2024,2026]],["evaluable",[1,12,1,8,1,1,1,2]],["detected",[1,9,1,7,0,0,1,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p20525","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20526"}}},"glyph":{"type":"object","name":"VBar","id":"p20521","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p20522","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p20523","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20496","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20509"},{"type":"object","name":"BoxZoomTool","id":"p20510","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20511","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20517","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20516","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20518","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20519"},{"type":"object","name":"SaveTool","id":"p20520"},{"type":"object","name":"HoverTool","id":"p20527","attributes":{"renderers":[{"id":"p20524"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p20504","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20505","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20506"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20507"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20499","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20500","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20501"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20502"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20503","attributes":{"axis":{"id":"p20499"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20508","attributes":{"dimension":1,"axis":{"id":"p20504"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"d82eeeba-5822-4e45-840c-94743f0e3b26","roots":{"p20488":"b61b22b9-419b-4c89-a6ff-50cb14ca5880"},"root_ids":["p20488"]}];
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

<div id="ce3a798c-dff2-4c31-b5bd-02026472de2b" data-root-id="p20533" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"99a92f43-2fac-46c3-a81c-904b36934bab":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20575","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20576"}}},"roots":[{"type":"object","name":"Figure","id":"p20533","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p20535"},"y_range":{"type":"object","name":"FactorRange","id":"p20542","attributes":{"factors":["probe","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p20543"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p20544"},"title":{"type":"object","name":"Title","id":"p20540","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20570","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20530","attributes":{"selected":{"type":"object","name":"Selection","id":"p20531","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20532"},"data":{"type":"map","entries":[["x",[-6,-1,-13,-21,-20,-14,-9,-15,-14,-3,-12,-16]],["y",["forward","forward","forward","probe","probe","probe","probe","probe","forward","probe","probe","forward"]],["alpha",[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]],["pos",[6,1,13,21,20,14,9,15,14,3,12,16]],["base",["G","T","G","A","G","T","C","A","C","R","G","C"]],["n",[361,354,350,337,322,241,87,44,40,40,35,27]],["det_with",["0% of 361","0% of 354","0% of 350","0% of 337","0% of 322","0% of 241","0% of 87","0% of 44","0% of 40","0% of 40","0% of 35","0% of 27"]],["det_without",["11% of 175","11% of 182","11% of 186","10% of 199","9% of 214","7% of 295","4% of 449","4% of 492","4% of 496","4% of 496","4% of 501","4% of 509"]],["subs",["G&gt;C 348, G&gt;T 13","T&gt;A 349, T&gt;C 5","G&gt;C 349, G&gt;A 1","A&gt;G 337","G&gt;A 321, G&gt;C 1","T&gt;C 241","C&gt;A 66, C&gt;T 21","A&gt;T 39, A&gt;G 3, A&gt;C 2","C&gt;T 40","R&gt;T 40","G&gt;A 35","C&gt;T 27"]],["zone",["no","yes","no","no","no","no","no","no","no","yes","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p20571","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20572"}}},"glyph":{"type":"object","name":"Rect","id":"p20567","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p20568","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p20569","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20541","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20555"},{"type":"object","name":"BoxZoomTool","id":"p20556","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20557","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20563","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20562","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20564","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20565"},{"type":"object","name":"SaveTool","id":"p20566"},{"type":"object","name":"HoverTool","id":"p20573","attributes":{"renderers":[{"id":"p20570"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p20550","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p20551"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p20552"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20553"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20545","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p20574","attributes":{"ticks":[-21,-20,-16,-15,-14,-13,-12,-9,-6,-3,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20547"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-6,"6"],[-1,"1"],[-13,"13"],[-21,"21"],[-20,"20"],[-14,"14"],[-9,"9"],[-15,"15"],[-3,"3"],[-12,"12"],[-16,"16"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p20548"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20549","attributes":{"axis":{"id":"p20545"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20554","attributes":{"dimension":1,"axis":{"id":"p20550"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"99a92f43-2fac-46c3-a81c-904b36934bab","roots":{"p20533":"ce3a798c-dff2-4c31-b5bd-02026472de2b"},"root_ids":["p20533"]}];
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

This entry declares **`scope_taxids`**: [1548720](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1548720), [1548721](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1548721). A record counts toward the denominator when its taxid, or any ancestor, is in that set. Records outside it are screened and reported but kept out of the statistics.

1,275 screened records fell outside the declared scope.

Disclosures on this entry: `cross_reactive`, `oligos_read_from_figure`.


## What reached the statistics

85 records were screened for this assay and **27 (32%)** were evaluable, meaning both primers landed in the right orientation and size range. 58 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 58 |

