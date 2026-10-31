# ASTROVIRUS_RdRp_Chu_2008_round1

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**Astrovirus pan-family RdRp heminested PCR (Chu 2008), round 1**

| | |
|---|---|
| Target | Astroviridae ([taxid 39733](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=39733)) |
| Gene | RNA-dependent RNA polymerase (RdRp) |
| Chemistry | conventional |
| Amplicon | — |
| Designed | 2008 |
| Paper | [10.1128/jvi.00857-08](https://doi.org/10.1128/jvi.00857-08) |
| Registry status | active |

!!! quote "The paper"
    Chu DK, Poon LL, Guan Y, Peiris JS. 2008. Novel astroviruses in insectivorous bats. J Virol 82:9107-9114

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GARTTYGATTGGRCKCGKTAYGA` | 23 nt |
| reverse | `GGYTTKACCCACATNCCRAA` | 20 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 243 | 691 | 35.2% | 31.7% – 38.8% |
| baseline (everything earlier) | 1,139 | 2,234 | 51.0% | 48.9% – 53.1% |

Change from baseline, Newcombe interval: **-19.9% to -11.6%**. Threshold: **90.0%**.

*detected share 35.2% (32%-39%) since Oct 2024, upper bound below the 90% threshold; change from baseline -20% to -12% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 51%); lineage Mamastrovirus suisencephalomyelitidis (3703181) (35 records) detects only 8.6%, but neither it nor the pooled share ever cleared the threshold, so there is no fall to call a decline*

Trend across deposit years: by record falling (p=4.94e-08, 29 years); by footprint falling (p=0.0155). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="d13c57d9-c750-4f17-975e-dbda7e1055b3" data-root-id="p3169" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"295b15b5-71b4-4b21-98ac-a5922a5aca20":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p3224","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p3225"}}},"roots":[{"type":"object","name":"Figure","id":"p3169","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p3171"},"y_range":{"type":"object","name":"Range1d","id":"p3178","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p3179"},"y_scale":{"type":"object","name":"LinearScale","id":"p3180"},"title":{"type":"object","name":"Title","id":"p3176","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p3214","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p3166","attributes":{"selected":{"type":"object","name":"Selection","id":"p3167","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p3168"},"data":{"type":"map","entries":[["year",[1993,1994,1997,1999,2000,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,50.0,33.33333333333333,100.0,50.0,100.0,66.66666666666666,70.1492537313433,69.56521739130434,25.471698113207548,47.05882352941176,60.86956521739131,45.28301886792453,62.16216216216216,52.63157894736842,50.0,73.33333333333333,24.390243902439025,59.0,61.31386861313869,36.054421768707485,47.73869346733669,47.8125,54.14847161572053,54.29864253393665,26.180257510729614,46.8421052631579]],["detected",[3,4,4,1,1,2,1,4,18,47,16,27,8,28,24,23,20,31,77,20,59,84,53,95,153,248,120,122,89]],["evaluable",[3,4,4,2,3,2,2,4,27,67,23,106,17,46,53,37,38,62,105,82,100,137,147,199,320,458,221,466,190]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.328625426046248,9.517227179437622,9.517227179437622,9.07684386569143,9.328625426046248,9.07684386569143,9.07684386569143,9.517227179437622,10.821697436206254,11.415029579131373,10.713966621835368,11.702562521586975,10.508782366508077,11.173276359477448,11.264976950698303,11.030852377887435,11.048392086352559,11.365614964623912,11.696703204756345,11.542654874768257,11.666489159086629,11.859851982963988,11.902614384823927,12.084368436583773,12.362832146851815,12.567931706405075,12.146519795051338,12.577730525242021,12.056811479830703]]]}}},"view":{"type":"object","name":"CDSView","id":"p3215","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3216"}}},"glyph":{"type":"object","name":"Line","id":"p3211","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p3212","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p3213","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p3220","attributes":{"data_source":{"id":"p3166"},"view":{"type":"object","name":"CDSView","id":"p3221","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3222"}}},"glyph":{"type":"object","name":"Scatter","id":"p3217","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p3218","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p3219","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p3177","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p3191"},{"type":"object","name":"BoxZoomTool","id":"p3192","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p3193","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p3199","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3198","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p3200","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p3201"},{"type":"object","name":"SaveTool","id":"p3202"},{"type":"object","name":"HoverTool","id":"p3223","attributes":{"renderers":[{"id":"p3220"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p3186","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3187","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3188"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3189"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p3181","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3182","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3183"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3184"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p3185","attributes":{"axis":{"id":"p3181"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p3190","attributes":{"dimension":1,"axis":{"id":"p3186"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p3203","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p3205","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p3206","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p3207","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p3209","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3208","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p3210","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"295b15b5-71b4-4b21-98ac-a5922a5aca20","roots":{"p3169":"d13c57d9-c750-4f17-975e-dbda7e1055b3"},"root_ids":["p3169"]}];
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

<div id="f966b543-0658-45c8-b791-bd959d6ae8ad" data-root-id="p3229" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"ba0a9be3-a4b4-44cf-901c-ab3c1ac217b6":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p3269","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p3270"}}},"roots":[{"type":"object","name":"Figure","id":"p3229","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p3230"},"y_range":{"type":"object","name":"DataRange1d","id":"p3231","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p3238"},"y_scale":{"type":"object","name":"LinearScale","id":"p3239"},"title":{"type":"object","name":"Title","id":"p3236","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p3265","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p3226","attributes":{"selected":{"type":"object","name":"Selection","id":"p3227","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p3228"},"data":{"type":"map","entries":[["year",[1993,1994,1997,1999,2000,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[3,4,4,2,3,2,2,4,27,67,23,106,17,46,53,37,38,62,105,82,100,137,147,199,320,458,221,466,190]],["detected",[3,4,4,1,1,2,1,4,18,47,16,27,8,28,24,23,20,31,77,20,59,84,53,95,153,248,120,122,89]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p3266","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3267"}}},"glyph":{"type":"object","name":"VBar","id":"p3262","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p3263","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p3264","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p3237","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p3250"},{"type":"object","name":"BoxZoomTool","id":"p3251","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p3252","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p3258","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3257","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p3259","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p3260"},{"type":"object","name":"SaveTool","id":"p3261"},{"type":"object","name":"HoverTool","id":"p3268","attributes":{"renderers":[{"id":"p3265"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p3245","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3246","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3247"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3248"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p3240","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3241","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3242"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3243"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p3244","attributes":{"axis":{"id":"p3240"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p3249","attributes":{"dimension":1,"axis":{"id":"p3245"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"ba0a9be3-a4b4-44cf-901c-ab3c1ac217b6","roots":{"p3229":"f966b543-0658-45c8-b791-bd959d6ae8ad"},"root_ids":["p3229"]}];
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

<div id="c7483d81-094d-4635-9802-937929a04472" data-root-id="p3274" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"cece54c0-15cd-4350-8d0a-6e0b718f340a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p3316","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p3317"}}},"roots":[{"type":"object","name":"Figure","id":"p3274","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p3276"},"y_range":{"type":"object","name":"FactorRange","id":"p3283","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p3284"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p3285"},"title":{"type":"object","name":"Title","id":"p3281","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p3311","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p3271","attributes":{"selected":{"type":"object","name":"Selection","id":"p3272","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p3273"},"data":{"type":"map","entries":[["x",[-4,-13,-14,-2,-16,-5,-1,-10,-9,-12,-11,-11,-6,-20,-19,-20,-18,-15,-15,-19]],["y",["forward","reverse","reverse","reverse","reverse","reverse","reverse","forward","forward","reverse","reverse","forward","forward","forward","reverse","reverse","forward","reverse","forward","forward"]],["alpha",[1.0,0.4603589743589743,0.1837094017094017,0.17905982905982906,0.1778974358974359,0.17673504273504273,0.1744102564102564,0.17324786324786323,1.0,0.18138461538461537,0.1744102564102564,0.2325299145299145,1.0,1.0,0.6312307692307692,0.6091452991452991,1.0,1.0,1.0,0.4522222222222222]],["pos",[4,13,14,2,16,5,1,10,9,12,11,11,6,20,19,20,18,15,15,19]],["base",["A","C","A","A","T","C","A","C","K","C","C","R","K","T","G","G","Y","K","T","T"]],["n",[1653,267,29,25,24,23,21,20,1693,27,21,71,1350,1518,414,395,1033,1540,1670,260]],["det_with",["23% of 1653","1% of 267","0% of 29","0% of 25","0% of 24","0% of 23","0% of 21","0% of 20","29% of 1693","4% of 27","5% of 21","28% of 71","38% of 1350","44% of 1518","42% of 414","44% of 395","50% of 1033","50% of 1540","51% of 1670","94% of 260"]],["det_without",["80% of 1264","52% of 2650","48% of 2888","48% of 2892","48% of 2893","48% of 2894","48% of 2896","48% of 2897","74% of 1224","48% of 2890","48% of 2896","48% of 2846","56% of 1567","51% of 1399","49% of 2503","48% of 2522","47% of 1884","46% of 1377","44% of 1247","43% of 2657"]],["subs",["A&gt;T 1652, A&gt;C 1","C&gt;T 254, C&gt;A 7, C&gt;G 6","A&gt;C 18, A&gt;T 10, A&gt;G 1","A&gt;C 18, A&gt;T 5, A&gt;G 2","T&gt;A 18, T&gt;G 6","C&gt;G 20, C&gt;A 3","A&gt;G 10, A&gt;T 7, A&gt;C 4","C&gt;A 10, C&gt;G 7, C&gt;T 3","K&gt;C 1003, K&gt;A 690","C&gt;A 19, C&gt;T 7, C&gt;G 1","C&gt;A 10, C&gt;G 7, C&gt;T 4","R&gt;T 69, R&gt;C 2","K&gt;C 897, G&gt;A 248, K&gt;A 204, G&gt;C 1","T&gt;A 937, T&gt;C 532, T&gt;G 49","G&gt;T 336, G&gt;C 54, G&gt;A 24","G&gt;C 229, G&gt;T 156, G&gt;A 10","Y&gt;G 992, Y&gt;A 41","K&gt;A 1232, K&gt;C 308","T&gt;C 1668, T&gt;G 1, T&gt;S 1","T&gt;C 245, T&gt;A 10, T&gt;G 5"]],["zone",["yes","no","no","yes","no","yes","yes","no","no","no","no","no","no","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p3312","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3313"}}},"glyph":{"type":"object","name":"Rect","id":"p3308","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p3309","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p3310","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p3282","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p3296"},{"type":"object","name":"BoxZoomTool","id":"p3297","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p3298","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p3304","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3303","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p3305","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p3306"},{"type":"object","name":"SaveTool","id":"p3307"},{"type":"object","name":"HoverTool","id":"p3314","attributes":{"renderers":[{"id":"p3311"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p3291","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p3292"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p3293"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3294"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p3286","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p3315","attributes":{"ticks":[-20,-19,-18,-16,-15,-14,-13,-12,-11,-10,-9,-6,-5,-4,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3288"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-4,"4"],[-13,"13"],[-14,"14"],[-2,"2"],[-16,"16"],[-5,"5"],[-1,"1"],[-10,"10"],[-9,"9"],[-12,"12"],[-11,"11"],[-6,"6"],[-20,"20"],[-19,"19"],[-18,"18"],[-15,"15"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p3289"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p3290","attributes":{"axis":{"id":"p3286"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p3295","attributes":{"dimension":1,"axis":{"id":"p3291"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"cece54c0-15cd-4350-8d0a-6e0b718f340a","roots":{"p3274":"c7483d81-094d-4635-9802-937929a04472"},"root_ids":["p3274"]}];
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

<div id="d0ab8fd5-aa43-4b0e-9b6f-b3b7b56aed2b" data-root-id="p3321" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9f8ccfff-38b5-4f21-854d-bfa58455ebc9":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p3370","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p3371"}}},"roots":[{"type":"object","name":"Figure","id":"p3321","attributes":{"height":262,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p3330","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p3331","attributes":{"factors":["Mamastrovirus suisvulgaris (3703182)","Mamastrovirus suisencephalomyelitidis (3703181)","Mamastrovirus sp. (1912147)","Porcine astrovirus 2 (1105378)","Bovine astrovirus (1435485)","Goose astrovirus (1349999)","Mamastrovirus hominis (3430629)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p3332"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p3333"},"title":{"type":"object","name":"Title","id":"p3328","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p3365","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p3318","attributes":{"selected":{"type":"object","name":"Selection","id":"p3319","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p3320"},"data":{"type":"map","entries":[["y",["Mamastrovirus suisvulgaris (3703182)","Mamastrovirus suisencephalomyelitidis (3703181)","Mamastrovirus sp. (1912147)","Porcine astrovirus 2 (1105378)","Bovine astrovirus (1435485)","Goose astrovirus (1349999)","Mamastrovirus hominis (3430629)"]],["share",[2.2988505747126435,8.571428571428571,14.285714285714285,18.75,40.54054054054054,93.33333333333333,100.0]],["lo",[0.6327085105926014,2.958236826696982,9.231379654107666,10.191390954847646,26.34651819201429,82.14339803640812,88.97446045395641]],["hi",[7.999318013961408,22.379273965896495,21.453317808906505,31.939867149284694,56.51403526977064,97.70679674007489,100.0]],["n",[87,35,126,48,37,45,31]],["det",[2,3,18,9,15,42,31]],["colour",["#b3261e","#b3261e","#b3261e","#b3261e","#b3261e","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p3366","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3367"}}},"glyph":{"type":"object","name":"Scatter","id":"p3362","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p3363","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p3364","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p3329","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p3344"},{"type":"object","name":"BoxZoomTool","id":"p3345","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p3346","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p3352","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3351","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p3353","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p3354"},{"type":"object","name":"SaveTool","id":"p3355"},{"type":"object","name":"HoverTool","id":"p3369","attributes":{"renderers":[{"id":"p3365"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p3339","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p3340"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p3341"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3342"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p3334","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3335","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3336"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3337"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p3338","attributes":{"axis":{"id":"p3334"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p3343","attributes":{"dimension":1,"axis":{"id":"p3339"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p3356","attributes":{"source":{"id":"p3318"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p3368","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9f8ccfff-38b5-4f21-854d-bfa58455ebc9","roots":{"p3321":"d0ab8fd5-aa43-4b0e-9b6f-b3b7b56aed2b"},"root_ids":["p3321"]}];
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

Disclosures on this entry: `nested_protocol`, `amplicon_measured_not_published`.


## What reached the statistics

16,713 records were screened for this assay and **2,925 (18%)** were evaluable, meaning both primers landed in the right orientation and size range. 13,788 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 11,956 |
| `truncated` | 1,326 |
| `chance_anchor` | 488 |
| `chance_only` | 17 |
| `no_pair` | 1 |

