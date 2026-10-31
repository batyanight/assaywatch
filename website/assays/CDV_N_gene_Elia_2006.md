# CDV_N_gene_Elia_2006

<span class="aw-chip aw-chip-declining">declining</span>

**CANINE DISTEMPER VIRUS — N gene TaqMan RT-qPCR (Elia 2006)**

| | |
|---|---|
| Target | Morbillivirus canis (formerly Canine morbillivirus) ([taxid 3052342](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3052342)) |
| Gene | N |
| Chemistry | hydrolysis_probe |
| Amplicon | 83 bp |
| Designed | 2006 |
| Paper | [10.1016/j.jviromet.2006.05.004](https://doi.org/10.1016/j.jviromet.2006.05.004) |
| Registry status | active |

!!! quote "The paper"
    Elia G, Decaro N, Martella V, Cirone F, Lucente MS, Lorusso E, Di Trani L, Buonavoglia C. Detection of canine distemper virus in dogs by real-time RT-PCR. J Virol Methods 2006;136:171-176.

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `AGCTAGTTTCATCTTAACTATCAAATT` | 27 nt |
| reverse | `TTAACTCTCCAGAAAACTCATGC` | 23 nt |
| probe | `ACCCAAGAGCCGGATACATAGTTTCAATGC` | 30 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 64 | 105 | 61.0% | 51.4% – 69.7% |
| baseline (everything earlier) | 282 | 554 | 50.9% | 46.7% – 55.0% |

Change from baseline, Newcombe interval: **-0.4% to 19.8%**. Threshold: **90.0%**.

*pooled share 61.0% has low coverage, but lineage Morbillivirus canis (3052342) (105 records) detects 61.0% (51.4%-69.7%); lineage verdict overrides to declining*

Trend across deposit years: by record falling (p=0.393, 30 years); by footprint falling (p=1). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="dc8fd8bd-91ca-468b-bf29-16703027d789" data-root-id="p7155" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"d8591cef-50c8-4c46-96b9-0ebc7db06cd5":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7210","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7211"}}},"roots":[{"type":"object","name":"Figure","id":"p7155","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p7157"},"y_range":{"type":"object","name":"Range1d","id":"p7164","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p7165"},"y_scale":{"type":"object","name":"LinearScale","id":"p7166"},"title":{"type":"object","name":"Title","id":"p7162","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7200","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7152","attributes":{"selected":{"type":"object","name":"Selection","id":"p7153","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7154"},"data":{"type":"map","entries":[["year",[1985,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[0.0,0.0,77.77777777777779,0.0,0.0,0.0,100.0,66.66666666666666,75.0,66.66666666666666,60.0,35.294117647058826,21.875,53.84615384615385,61.111111111111114,78.78787878787878,82.22222222222221,40.909090909090914,50.0,70.0,21.428571428571427,36.36363636363637,37.03703703703704,38.961038961038966,100.0,28.07017543859649,19.047619047619047,85.71428571428571,42.30769230769231,66.23376623376623]],["detected",[0,0,7,0,0,0,6,4,9,4,3,6,7,7,11,26,37,9,5,35,3,12,10,30,21,16,4,12,11,51]],["evaluable",[1,2,9,1,1,3,6,6,12,6,5,17,32,13,18,33,45,22,10,50,14,33,27,77,21,57,21,14,26,77]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,9.07684386569143,10.071067811865476,8.703135093227193,8.703135093227193,9.328625426046248,9.791719296345839,9.791719296345839,10.269703144398052,9.791719296345839,9.667366891029102,10.508782366508077,10.934913263353746,10.324834530005162,10.547770533331066,10.955310988645032,11.15897945775324,10.683957047019447,10.143865699252444,11.22734795681138,10.37579022724969,10.955310988645032,10.821697436206254,11.503079740144862,10.652487636092928,11.311780786273989,10.652487636092928,10.37579022724969,10.796415465069488,11.503079740144862]]]}}},"view":{"type":"object","name":"CDSView","id":"p7201","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7202"}}},"glyph":{"type":"object","name":"Line","id":"p7197","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p7198","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p7199","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p7206","attributes":{"data_source":{"id":"p7152"},"view":{"type":"object","name":"CDSView","id":"p7207","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7208"}}},"glyph":{"type":"object","name":"Scatter","id":"p7203","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p7204","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p7205","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7163","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7177"},{"type":"object","name":"BoxZoomTool","id":"p7178","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7179","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7185","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7184","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7186","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7187"},{"type":"object","name":"SaveTool","id":"p7188"},{"type":"object","name":"HoverTool","id":"p7209","attributes":{"renderers":[{"id":"p7206"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p7172","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7173","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7174"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7175"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7167","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7168","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7169"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7170"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7171","attributes":{"axis":{"id":"p7167"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7176","attributes":{"dimension":1,"axis":{"id":"p7172"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p7189","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p7191","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p7192","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p7193","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p7195","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7194","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p7196","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"d8591cef-50c8-4c46-96b9-0ebc7db06cd5","roots":{"p7155":"dc8fd8bd-91ca-468b-bf29-16703027d789"},"root_ids":["p7155"]}];
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

<div id="cbd994d7-610c-4c6f-8ad3-c2c1b94c5c7e" data-root-id="p7215" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"0c68a485-4696-4a3d-b220-3c9ba6237027":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7255","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7256"}}},"roots":[{"type":"object","name":"Figure","id":"p7215","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p7216"},"y_range":{"type":"object","name":"DataRange1d","id":"p7217","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p7224"},"y_scale":{"type":"object","name":"LinearScale","id":"p7225"},"title":{"type":"object","name":"Title","id":"p7222","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7251","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7212","attributes":{"selected":{"type":"object","name":"Selection","id":"p7213","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7214"},"data":{"type":"map","entries":[["year",[1985,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,2,9,1,1,3,6,6,12,6,5,17,32,13,18,33,45,22,10,50,14,33,27,77,21,57,21,14,26,77]],["detected",[0,0,7,0,0,0,6,4,9,4,3,6,7,7,11,26,37,9,5,35,3,12,10,30,21,16,4,12,11,51]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p7252","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7253"}}},"glyph":{"type":"object","name":"VBar","id":"p7248","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p7249","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p7250","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7223","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7236"},{"type":"object","name":"BoxZoomTool","id":"p7237","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7238","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7244","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7243","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7245","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7246"},{"type":"object","name":"SaveTool","id":"p7247"},{"type":"object","name":"HoverTool","id":"p7254","attributes":{"renderers":[{"id":"p7251"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p7231","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7232","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7233"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7234"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7226","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7227","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7228"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7229"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7230","attributes":{"axis":{"id":"p7226"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7235","attributes":{"dimension":1,"axis":{"id":"p7231"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"0c68a485-4696-4a3d-b220-3c9ba6237027","roots":{"p7215":"cbd994d7-610c-4c6f-8ad3-c2c1b94c5c7e"},"root_ids":["p7215"]}];
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

<div id="d50a1b64-0abf-4c6b-8bab-95456dc69a68" data-root-id="p7260" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"337fda8a-73c5-4c9f-9f22-72b9c8b34c62":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7302","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7303"}}},"roots":[{"type":"object","name":"Figure","id":"p7260","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p7262"},"y_range":{"type":"object","name":"FactorRange","id":"p7269","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p7270"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p7271"},"title":{"type":"object","name":"Title","id":"p7267","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7297","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7257","attributes":{"selected":{"type":"object","name":"Selection","id":"p7258","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7259"},"data":{"type":"map","entries":[["x",[-3,-14,-23,-20,-19,-10,-26,-27,-13,-21,-12,-9,-16,-24]],["y",["forward","forward","probe","probe","reverse","reverse","probe","forward","reverse","forward","forward","forward","reverse","forward"]],["alpha",[0.6917298937784522,0.5833839150227618,0.37701062215477993,0.2789833080424886,0.6349772382397573,0.25834597875569043,0.5782245827010621,0.26350531107738995,1.0,0.33057663125948406,0.5163125948406677,0.2996206373292868,0.4595599393019727,0.3099393019726859]],["pos",[3,14,23,20,19,10,26,27,13,21,12,9,16,24]],["base",["A","T","A","C","C","A","A","A","A","T","A","T","T","T"]],["n",[105,84,44,25,94,21,83,22,451,35,71,29,60,31]],["det_with",["0% of 105","2% of 84","0% of 44","0% of 25","7% of 94","5% of 21","11% of 83","9% of 22","40% of 451","26% of 35","31% of 71","34% of 29","53% of 60","61% of 31"]],["det_without",["62% of 559","59% of 580","56% of 620","54% of 639","60% of 570","54% of 643","58% of 581","54% of 642","77% of 213","54% of 629","55% of 593","53% of 635","52% of 604","52% of 633"]],["subs",["A&gt;G 104, A&gt;C 1","T&gt;C 84","A&gt;G 28, A&gt;C 15, A&gt;T 1","C&gt;T 15, C&gt;G 6, C&gt;A 4","C&gt;T 93, C&gt;A 1","A&gt;G 21","A&gt;G 49, A&gt;T 34","A&gt;G 22","A&gt;G 447, A&gt;T 4","T&gt;C 35","A&gt;G 71","T&gt;C 14, T&gt;G 14, T&gt;A 1","T&gt;C 52, T&gt;A 8","T&gt;C 14, T&gt;G 13, T&gt;A 4"]],["zone",["yes","no","no","no","no","no","no","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p7298","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7299"}}},"glyph":{"type":"object","name":"Rect","id":"p7294","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p7295","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p7296","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7268","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7282"},{"type":"object","name":"BoxZoomTool","id":"p7283","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7284","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7290","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7289","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7291","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7292"},{"type":"object","name":"SaveTool","id":"p7293"},{"type":"object","name":"HoverTool","id":"p7300","attributes":{"renderers":[{"id":"p7297"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p7277","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p7278"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p7279"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7280"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7272","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p7301","attributes":{"ticks":[-27,-26,-24,-23,-21,-20,-19,-16,-14,-13,-12,-10,-9,-3],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7274"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-3,"3"],[-14,"14"],[-23,"23"],[-20,"20"],[-19,"19"],[-10,"10"],[-26,"26"],[-27,"27"],[-13,"13"],[-21,"21"],[-12,"12"],[-9,"9"],[-16,"16"],[-24,"24"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p7275"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7276","attributes":{"axis":{"id":"p7272"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7281","attributes":{"dimension":1,"axis":{"id":"p7277"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"337fda8a-73c5-4c9f-9f22-72b9c8b34c62","roots":{"p7260":"d50a1b64-0abf-4c6b-8bab-95456dc69a68"},"root_ids":["p7260"]}];
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

<div id="aa5fcb18-6e99-4092-8bb5-440f3ffc5775" data-root-id="p7307" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"a9f5f3b4-dca3-49d8-acc4-70a6b13f0849":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7356","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7357"}}},"roots":[{"type":"object","name":"Figure","id":"p7307","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p7316","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p7317","attributes":{"factors":["Morbillivirus canis (3052342)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p7318"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p7319"},"title":{"type":"object","name":"Title","id":"p7314","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7351","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7304","attributes":{"selected":{"type":"object","name":"Selection","id":"p7305","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7306"},"data":{"type":"map","entries":[["y",["Morbillivirus canis (3052342)"]],["share",[60.952380952380956]],["lo",[51.39244529196772]],["hi",[69.7392082610137]],["n",[105]],["det",[64]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p7352","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7353"}}},"glyph":{"type":"object","name":"Scatter","id":"p7348","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p7349","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p7350","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7315","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7330"},{"type":"object","name":"BoxZoomTool","id":"p7331","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7332","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7338","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7337","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7339","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7340"},{"type":"object","name":"SaveTool","id":"p7341"},{"type":"object","name":"HoverTool","id":"p7355","attributes":{"renderers":[{"id":"p7351"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p7325","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p7326"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p7327"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7328"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7320","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7321","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7322"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7323"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7324","attributes":{"axis":{"id":"p7320"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7329","attributes":{"dimension":1,"axis":{"id":"p7325"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p7342","attributes":{"source":{"id":"p7304"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p7354","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"a9f5f3b4-dca3-49d8-acc4-70a6b13f0849","roots":{"p7307":"aa5fcb18-6e99-4092-8bb5-440f3ffc5775"},"root_ids":["p7307"]}];
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

Disclosures on this entry: `citation_is_indirect`, `amplicon_disagrees_with_paper`, `oligos_from_secondary_source`.


## What reached the statistics

3,952 records were screened for this assay and **659 (17%)** were evaluable, meaning both primers landed in the right orientation and size range. 3,293 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 3,282 |
| `truncated` | 11 |

