# ASTROVIRUS_ssRNA_RNA_dependent_RNA_polyme_round2

<span class="aw-chip aw-chip-stable">stable</span>

**ASTROVIRUS (ssRNA) — RNA-dependent RNA polymerase (RdRp)**

| | |
|---|---|
| Target | Astroviridae ([taxid 39733](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=39733)) |
| Gene | RNA-dependent RNA polymerase (RdRp) |
| Chemistry | conventional |
| Amplicon | 342 bp |
| Designed | 2009 |
| Paper | [10.1016/j.vetmic.2008.10.035](https://doi.org/10.1016/j.vetmic.2008.10.035) |
| Registry status | active |

!!! quote "The paper"
    Atkins, A. et al. Characterization of an outbreak of astroviral diarrhea in a group of cheetahs (Acinonyx jubatus). Veterinary microbiology 136, 160-165, doi:10.1016/j.vetmic.2008.10.035 (2009).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GAYTGGRCNCGNTWYGATGGNACNAT` | 26 nt |
| reverse | `ARNCKRTCATCNCCATA` | 17 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 683 | 711 | 96.1% | 94.4% – 97.3% |
| baseline (everything earlier) | 2,358 | 2,598 | 90.8% | 89.6% – 91.8% |

Change from baseline, Newcombe interval: **3.3% to 7.0%**. Threshold: **90.0%**.

*detected share 96.1% (94%-97%) since Oct 2024*

Trend across deposit years: by record rising (p=4.77e-38, 29 years); by footprint rising (p=0.0171). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="cf153049-74fd-4372-91c0-5e0378c0c75e" data-root-id="p3787" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9a146f64-cb9e-4450-afc9-850881776758":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p3842","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p3843"}}},"roots":[{"type":"object","name":"Figure","id":"p3787","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p3789"},"y_range":{"type":"object","name":"Range1d","id":"p3796","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p3797"},"y_scale":{"type":"object","name":"LinearScale","id":"p3798"},"title":{"type":"object","name":"Title","id":"p3794","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p3832","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p3784","attributes":{"selected":{"type":"object","name":"Selection","id":"p3785","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p3786"},"data":{"type":"map","entries":[["year",[1993,1994,1997,1999,2000,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,32.432432432432435,90.78947368421053,100.0,100.0,90.0,64.0,96.875,47.05882352941176,62.71186440677966,99.07407407407408,99.04761904761905,96.3855421686747,83.33333333333334,97.2027972027972,91.35135135135135,99.54337899543378,98.23008849557522,95.35864978902954,90.0398406374502,97.26890756302521,96.35416666666666]],["detected",[3,4,4,2,3,2,2,4,24,69,23,113,18,48,62,32,37,107,104,80,115,139,169,218,333,452,226,463,185]],["evaluable",[3,4,4,2,3,2,2,4,74,76,23,113,20,75,64,68,59,108,105,83,138,143,185,219,339,474,251,476,192]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.328625426046248,9.517227179437622,9.517227179437622,9.07684386569143,9.328625426046248,9.07684386569143,9.07684386569143,9.517227179437622,11.47800280636852,11.49483773413666,10.713966621835368,11.74200327633271,10.619414831097462,11.486479824227462,11.385871088686695,11.42444225266168,11.333893523413357,11.71410709416149,11.696703204756345,11.550262110107914,11.864274928405164,11.88589119348089,12.040897278779795,12.141146920411856,12.396114778250443,12.58735314049825,12.22144313649109,12.589731981447805,12.063053167955838]]]}}},"view":{"type":"object","name":"CDSView","id":"p3833","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3834"}}},"glyph":{"type":"object","name":"Line","id":"p3829","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p3830","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p3831","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p3838","attributes":{"data_source":{"id":"p3784"},"view":{"type":"object","name":"CDSView","id":"p3839","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3840"}}},"glyph":{"type":"object","name":"Scatter","id":"p3835","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p3836","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p3837","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p3795","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p3809"},{"type":"object","name":"BoxZoomTool","id":"p3810","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p3811","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p3817","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3816","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p3818","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p3819"},{"type":"object","name":"SaveTool","id":"p3820"},{"type":"object","name":"HoverTool","id":"p3841","attributes":{"renderers":[{"id":"p3838"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p3804","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3805","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3806"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3807"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p3799","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3800","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3801"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3802"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p3803","attributes":{"axis":{"id":"p3799"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p3808","attributes":{"dimension":1,"axis":{"id":"p3804"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p3821","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p3823","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p3824","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p3825","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p3827","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3826","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p3828","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9a146f64-cb9e-4450-afc9-850881776758","roots":{"p3787":"cf153049-74fd-4372-91c0-5e0378c0c75e"},"root_ids":["p3787"]}];
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

<div id="c321376e-296f-44d9-a9a2-756498c60824" data-root-id="p3847" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"0956111c-49fe-41f1-8f5a-254d15170361":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p3887","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p3888"}}},"roots":[{"type":"object","name":"Figure","id":"p3847","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p3848"},"y_range":{"type":"object","name":"DataRange1d","id":"p3849","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p3856"},"y_scale":{"type":"object","name":"LinearScale","id":"p3857"},"title":{"type":"object","name":"Title","id":"p3854","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p3883","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p3844","attributes":{"selected":{"type":"object","name":"Selection","id":"p3845","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p3846"},"data":{"type":"map","entries":[["year",[1993,1994,1997,1999,2000,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[3,4,4,2,3,2,2,4,74,76,23,113,20,75,64,68,59,108,105,83,138,143,185,219,339,474,251,476,192]],["detected",[3,4,4,2,3,2,2,4,24,69,23,113,18,48,62,32,37,107,104,80,115,139,169,218,333,452,226,463,185]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p3884","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3885"}}},"glyph":{"type":"object","name":"VBar","id":"p3880","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p3881","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p3882","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p3855","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p3868"},{"type":"object","name":"BoxZoomTool","id":"p3869","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p3870","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p3876","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3875","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p3877","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p3878"},{"type":"object","name":"SaveTool","id":"p3879"},{"type":"object","name":"HoverTool","id":"p3886","attributes":{"renderers":[{"id":"p3883"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p3863","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3864","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3865"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3866"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p3858","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3859","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3860"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3861"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p3862","attributes":{"axis":{"id":"p3858"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p3867","attributes":{"dimension":1,"axis":{"id":"p3863"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"0956111c-49fe-41f1-8f5a-254d15170361","roots":{"p3847":"c321376e-296f-44d9-a9a2-756498c60824"},"root_ids":["p3847"]}];
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

<div id="ed992644-c112-40a8-a10b-2f3b5a48094f" data-root-id="p3892" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b900f21d-a61a-446e-a988-a0f12c43ef93":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p3934","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p3935"}}},"roots":[{"type":"object","name":"Figure","id":"p3892","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p3894"},"y_range":{"type":"object","name":"FactorRange","id":"p3901","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p3902"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p3903"},"title":{"type":"object","name":"Title","id":"p3899","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p3929","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p3889","attributes":{"selected":{"type":"object","name":"Selection","id":"p3890","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p3891"},"data":{"type":"map","entries":[["x",[-10,-1,-2,-7,-11,-12,-5,-8,-4,-14,-13,-21,-22,-19,-3,-9,-16,-9,-17,-20,-2]],["y",["reverse","reverse","reverse","reverse","reverse","reverse","reverse","reverse","reverse","reverse","reverse","forward","forward","forward","reverse","reverse","reverse","forward","forward","forward","forward"]],["alpha",[0.22809005741915986,0.216787549108492,0.216787549108492,0.2506950740404956,0.20445754004230884,0.19726503475370202,0.2373375642187972,0.19418253248715622,0.18082502266545783,0.27330009066183136,0.19829253550921727,0.21473254759746147,0.2116500453309157,0.2188425506195225,0.7212904200664854,0.8209579933514657,0.4099576911453612,0.5836053188274403,0.9380930794802055,0.2270625566636446,0.4253702024780901]],["pos",[10,1,2,7,11,12,5,8,4,14,13,21,22,19,3,9,16,9,17,20,2]],["base",["C","A","T","C","T","R","C","T","C","C","K","G","G","C","A","A","R","T","C","R","A"]],["n",[76,65,65,98,53,46,85,43,30,120,47,63,60,67,556,653,253,422,767,75,268]],["det_with",["0% of 76","0% of 65","0% of 65","1% of 98","0% of 53","0% of 46","1% of 85","0% of 43","0% of 30","43% of 120","49% of 47","59% of 63","63% of 60","75% of 67","79% of 556","87% of 653","87% of 253","88% of 422","91% of 767","92% of 75","94% of 268"]],["det_without",["96% of 3170","96% of 3181","96% of 3181","97% of 3148","96% of 3193","95% of 3200","97% of 3161","95% of 3203","95% of 3216","96% of 3126","95% of 3199","95% of 3183","95% of 3186","94% of 3179","97% of 2690","96% of 2593","95% of 2993","95% of 2824","95% of 2479","94% of 3171","94% of 2978"]],["subs",["C&gt;G 35, C&gt;T 27, C&gt;A 14","A&gt;T 58, A&gt;G 6, A&gt;C 1","T&gt;A 52, T&gt;C 11, T&gt;G 2","C&gt;G 47, C&gt;A 40, C&gt;T 11","T&gt;C 31, T&gt;G 15, T&gt;A 7","R&gt;T 40, R&gt;C 6","C&gt;T 65, C&gt;A 15, C&gt;G 5","T&gt;A 38, T&gt;C 5","C&gt;G 26, C&gt;A 3, C&gt;T 1","C&gt;A 49, C&gt;T 46, C&gt;G 25","K&gt;C 26, K&gt;A 21","G&gt;C 32, G&gt;T 30, G&gt;A 1","G&gt;A 31, G&gt;T 29","C&gt;A 53, C&gt;G 8, C&gt;T 6","A&gt;G 492, A&gt;C 43, A&gt;T 21","A&gt;G 640, A&gt;C 7, A&gt;T 6","R&gt;T 201, R&gt;C 52","T&gt;C 418, T&gt;G 3, T&gt;A 1","C&gt;A 759, C&gt;G 4, C&gt;T 4","R&gt;T 74, R&gt;C 1","A&gt;T 250, A&gt;C 11, A&gt;G 7"]],["zone",["no","yes","yes","no","no","no","yes","no","yes","no","no","no","no","no","yes","no","no","no","no","no","yes"]]]}}},"view":{"type":"object","name":"CDSView","id":"p3930","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3931"}}},"glyph":{"type":"object","name":"Rect","id":"p3926","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p3927","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p3928","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p3900","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p3914"},{"type":"object","name":"BoxZoomTool","id":"p3915","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p3916","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p3922","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3921","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p3923","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p3924"},{"type":"object","name":"SaveTool","id":"p3925"},{"type":"object","name":"HoverTool","id":"p3932","attributes":{"renderers":[{"id":"p3929"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p3909","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p3910"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p3911"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3912"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p3904","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p3933","attributes":{"ticks":[-22,-21,-20,-19,-17,-16,-14,-13,-12,-11,-10,-9,-8,-7,-5,-4,-3,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3906"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-10,"10"],[-1,"1"],[-2,"2"],[-7,"7"],[-11,"11"],[-12,"12"],[-5,"5"],[-8,"8"],[-4,"4"],[-14,"14"],[-13,"13"],[-21,"21"],[-22,"22"],[-19,"19"],[-3,"3"],[-9,"9"],[-16,"16"],[-17,"17"],[-20,"20"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p3907"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p3908","attributes":{"axis":{"id":"p3904"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p3913","attributes":{"dimension":1,"axis":{"id":"p3909"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b900f21d-a61a-446e-a988-a0f12c43ef93","roots":{"p3892":"ed992644-c112-40a8-a10b-2f3b5a48094f"},"root_ids":["p3892"]}];
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

<div id="a8d78afe-e6dc-4051-8a93-fb8859ea7a0d" data-root-id="p3939" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"922fb1f3-9589-48bd-a135-15ff88e4f81f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p3988","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p3989"}}},"roots":[{"type":"object","name":"Figure","id":"p3939","attributes":{"height":262,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p3948","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p3949","attributes":{"factors":["Mamastrovirus suisvulgaris (3703182)","Goose astrovirus (1349999)","Mamastrovirus sp. (1912147)","Bovine astrovirus (1435485)","Mamastrovirus hominis (3430629)","Mamastrovirus suisencephalomyelitidis (3703181)","Porcine astrovirus 2 (1105378)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p3950"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p3951"},"title":{"type":"object","name":"Title","id":"p3946","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p3983","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p3936","attributes":{"selected":{"type":"object","name":"Selection","id":"p3937","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p3938"},"data":{"type":"map","entries":[["y",["Mamastrovirus suisvulgaris (3703182)","Goose astrovirus (1349999)","Mamastrovirus sp. (1912147)","Bovine astrovirus (1435485)","Mamastrovirus hominis (3430629)","Mamastrovirus suisencephalomyelitidis (3703181)","Porcine astrovirus 2 (1105378)"]],["share",[94.25287356321839,95.65217391304348,96.09375,97.2972972972973,100.0,100.0,100.0]],["lo",[87.24262350954837,85.46774097378093,91.18129792331631,86.1759301362695,88.97446045395641,90.1099007675596,92.58998703338824]],["hi",[97.52043622068464,98.79945544014434,98.32013892021962,99.52130255480596,100.0,100.0,100.0]],["n",[87,46,128,37,31,35,48]],["det",[82,44,123,36,31,35,48]],["colour",["#007d5c","#007d5c","#007d5c","#007d5c","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p3984","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3985"}}},"glyph":{"type":"object","name":"Scatter","id":"p3980","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p3981","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p3982","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p3947","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p3962"},{"type":"object","name":"BoxZoomTool","id":"p3963","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p3964","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p3970","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3969","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p3971","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p3972"},{"type":"object","name":"SaveTool","id":"p3973"},{"type":"object","name":"HoverTool","id":"p3987","attributes":{"renderers":[{"id":"p3983"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p3957","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p3958"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p3959"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3960"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p3952","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3953","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3954"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3955"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p3956","attributes":{"axis":{"id":"p3952"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p3961","attributes":{"dimension":1,"axis":{"id":"p3957"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p3974","attributes":{"source":{"id":"p3936"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p3986","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"922fb1f3-9589-48bd-a135-15ff88e4f81f","roots":{"p3939":"a8d78afe-e6dc-4051-8a93-fb8859ea7a0d"},"root_ids":["p3939"]}];
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

Disclosures on this entry: `nested_protocol`.


## What reached the statistics

16,713 records were screened for this assay and **3,309 (20%)** were evaluable, meaning both primers landed in the right orientation and size range. 13,404 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 8,291 |
| `truncated` | 4,387 |
| `chance_anchor` | 596 |
| `chance_only` | 124 |
| `no_pair` | 6 |

