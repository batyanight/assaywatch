# ASTROVIRUS_ssRNA_RNA_dependent_RNA_polyme_round1

<span class="aw-chip aw-chip-stable">stable</span>

**ASTROVIRUS (ssRNA) — RNA-dependent RNA polymerase (RdRp)**

| | |
|---|---|
| Target | Astroviridae ([taxid 39733](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=39733)) |
| Gene | RNA-dependent RNA polymerase (RdRp) |
| Chemistry | conventional |
| Amplicon | 431 bp |
| Designed | 2009 |
| Paper | [10.1016/j.vetmic.2008.10.035](https://doi.org/10.1016/j.vetmic.2008.10.035) |
| Registry status | active |

!!! quote "The paper"
    Atkins, A. et al. Characterization of an outbreak of astroviral diarrhea in a group of cheetahs (Acinonyx jubatus). Veterinary microbiology 136, 160-165, doi:10.1016/j.vetmic.2008.10.035 (2009).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GAYTGGRCNCGNTWYGATGGNACNAT` | 26 nt |
| reverse | `GGYTTNACCCACATNCCAAA` | 20 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 685 | 694 | 98.7% | 97.6% – 99.3% |
| baseline (everything earlier) | 2,276 | 2,360 | 96.4% | 95.6% – 97.1% |

Change from baseline, Newcombe interval: **0.9% to 3.3%**. Threshold: **90.0%**.

*detected share 98.7% (98%-99%) since Oct 2024*

Trend across deposit years: by record falling (p=0.534, 29 years); by footprint falling (p=0.0101). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="ae5ab1fe-01a4-4115-b163-5d974982dd65" data-root-id="p3581" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"25bbd124-dd85-43ae-a609-621502eedb8c":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p3636","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p3637"}}},"roots":[{"type":"object","name":"Figure","id":"p3581","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p3583"},"y_range":{"type":"object","name":"Range1d","id":"p3590","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p3591"},"y_scale":{"type":"object","name":"LinearScale","id":"p3592"},"title":{"type":"object","name":"Title","id":"p3588","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p3626","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p3578","attributes":{"selected":{"type":"object","name":"Selection","id":"p3579","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p3580"},"data":{"type":"map","entries":[["year",[1993,1994,1997,1999,2000,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,78.94736842105263,100.0,100.0,100.0,97.43589743589743,99.07407407407408,99.04761904761905,100.0,76.98412698412699,99.27536231884058,96.07843137254902,94.4954128440367,98.47560975609755,97.4304068522484,94.5945945945946,98.72611464968153,98.40425531914893]],["detected",[3,4,4,2,3,2,2,4,24,69,23,113,15,45,62,30,38,107,104,82,97,137,147,206,323,455,210,465,185]],["evaluable",[3,4,4,2,3,2,2,4,24,69,23,113,19,45,62,30,39,108,105,82,126,138,153,218,328,467,222,471,188]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.328625426046248,9.517227179437622,9.517227179437622,9.07684386569143,9.328625426046248,9.07684386569143,9.07684386569143,9.517227179437622,10.74264168206181,11.433709207718536,10.713966621835368,11.74200327633271,10.584573151575475,11.15897945775324,11.365614964623912,10.892023970177537,11.06545099688784,11.71410709416149,11.696703204756345,11.542654874768257,11.808807695931325,11.864274928405164,11.926814550606032,12.138440943126074,12.377094296675775,12.578942860611138,12.149186935252992,12.583764916036504,12.050499715724602]]]}}},"view":{"type":"object","name":"CDSView","id":"p3627","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3628"}}},"glyph":{"type":"object","name":"Line","id":"p3623","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p3624","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p3625","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p3632","attributes":{"data_source":{"id":"p3578"},"view":{"type":"object","name":"CDSView","id":"p3633","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3634"}}},"glyph":{"type":"object","name":"Scatter","id":"p3629","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p3630","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p3631","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p3589","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p3603"},{"type":"object","name":"BoxZoomTool","id":"p3604","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p3605","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p3611","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3610","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p3612","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p3613"},{"type":"object","name":"SaveTool","id":"p3614"},{"type":"object","name":"HoverTool","id":"p3635","attributes":{"renderers":[{"id":"p3632"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p3598","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3599","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3600"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3601"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p3593","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3594","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3595"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3596"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p3597","attributes":{"axis":{"id":"p3593"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p3602","attributes":{"dimension":1,"axis":{"id":"p3598"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p3615","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p3617","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p3618","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p3619","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p3621","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3620","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p3622","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"25bbd124-dd85-43ae-a609-621502eedb8c","roots":{"p3581":"ae5ab1fe-01a4-4115-b163-5d974982dd65"},"root_ids":["p3581"]}];
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

<div id="dc4df1f7-343b-47fa-8e8b-f24f26595485" data-root-id="p3641" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"ff71d12e-5347-4887-ba49-26e8726996df":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p3681","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p3682"}}},"roots":[{"type":"object","name":"Figure","id":"p3641","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p3642"},"y_range":{"type":"object","name":"DataRange1d","id":"p3643","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p3650"},"y_scale":{"type":"object","name":"LinearScale","id":"p3651"},"title":{"type":"object","name":"Title","id":"p3648","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p3677","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p3638","attributes":{"selected":{"type":"object","name":"Selection","id":"p3639","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p3640"},"data":{"type":"map","entries":[["year",[1993,1994,1997,1999,2000,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[3,4,4,2,3,2,2,4,24,69,23,113,19,45,62,30,39,108,105,82,126,138,153,218,328,467,222,471,188]],["detected",[3,4,4,2,3,2,2,4,24,69,23,113,15,45,62,30,38,107,104,82,97,137,147,206,323,455,210,465,185]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p3678","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3679"}}},"glyph":{"type":"object","name":"VBar","id":"p3674","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p3675","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p3676","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p3649","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p3662"},{"type":"object","name":"BoxZoomTool","id":"p3663","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p3664","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p3670","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3669","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p3671","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p3672"},{"type":"object","name":"SaveTool","id":"p3673"},{"type":"object","name":"HoverTool","id":"p3680","attributes":{"renderers":[{"id":"p3677"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p3657","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3658","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3659"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3660"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p3652","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3653","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3654"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3655"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p3656","attributes":{"axis":{"id":"p3652"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p3661","attributes":{"dimension":1,"axis":{"id":"p3657"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"ff71d12e-5347-4887-ba49-26e8726996df","roots":{"p3641":"dc4df1f7-343b-47fa-8e8b-f24f26595485"},"root_ids":["p3641"]}];
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

<div id="e5d21d9f-46d3-46cc-b1f0-f3af98f500c7" data-root-id="p3686" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"e9714bd7-9d4e-4ed9-8560-83130b8f1b8e":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p3728","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p3729"}}},"roots":[{"type":"object","name":"Figure","id":"p3686","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p3688"},"y_range":{"type":"object","name":"FactorRange","id":"p3695","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p3696"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p3697"},"title":{"type":"object","name":"Title","id":"p3693","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p3723","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p3683","attributes":{"selected":{"type":"object","name":"Selection","id":"p3684","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p3685"},"data":{"type":"map","entries":[["x",[-1,-16,-17,-19,-21,-22,-13,-20,-19,-3,-9,-17,-2,-20]],["y",["reverse","reverse","reverse","forward","forward","forward","reverse","reverse","reverse","reverse","forward","forward","forward","forward"]],["alpha",[0.17226588081204977,0.1800589390962672,0.1800589390962672,0.20677799607072692,0.20455140798952193,0.20343811394891945,0.48064833005893914,0.6342829076620825,0.6543222003929273,0.4505893909626719,0.5730517354289456,0.9460052390307793,0.4405697445972495,0.2268172888015717]],["pos",[1,16,17,19,21,22,13,20,19,3,9,17,2,20]],["base",["A","T","T","C","G","G","C","G","G","A","T","C","A","R"]],["n",[20,27,27,51,49,48,297,435,453,270,380,715,261,69]],["det_with",["0% of 20","33% of 27","33% of 27","35% of 51","41% of 49","42% of 48","87% of 297","92% of 435","93% of 453","93% of 270","94% of 380","96% of 715","95% of 261","99% of 69"]],["det_without",["98% of 3024","98% of 3017","98% of 3017","99% of 2993","99% of 2995","99% of 2996","99% of 2747","99% of 2609","99% of 2591","98% of 2774","98% of 2664","98% of 2329","98% of 2783","98% of 2975"]],["subs",["A&gt;G 12, A&gt;T 5, A&gt;C 3","T&gt;G 24, T&gt;A 3","T&gt;G 26, T&gt;C 1","C&gt;A 41, C&gt;G 7, C&gt;T 3","G&gt;C 30, G&gt;T 18, G&gt;A 1","G&gt;T 25, G&gt;A 23","C&gt;T 259, C&gt;G 31, C&gt;A 7","G&gt;C 245, G&gt;T 181, G&gt;A 9","G&gt;T 355, G&gt;C 74, G&gt;A 24","A&gt;G 265, A&gt;C 5","T&gt;C 378, T&gt;A 2","C&gt;A 712, C&gt;T 2, C&gt;G 1","A&gt;T 246, A&gt;C 9, A&gt;G 6","R&gt;T 69"]],["zone",["yes","no","no","no","no","no","no","no","no","yes","no","no","yes","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p3724","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3725"}}},"glyph":{"type":"object","name":"Rect","id":"p3720","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p3721","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p3722","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p3694","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p3708"},{"type":"object","name":"BoxZoomTool","id":"p3709","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p3710","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p3716","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3715","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p3717","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p3718"},{"type":"object","name":"SaveTool","id":"p3719"},{"type":"object","name":"HoverTool","id":"p3726","attributes":{"renderers":[{"id":"p3723"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p3703","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p3704"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p3705"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3706"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p3698","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p3727","attributes":{"ticks":[-22,-21,-20,-19,-17,-16,-13,-9,-3,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3700"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-1,"1"],[-16,"16"],[-17,"17"],[-19,"19"],[-21,"21"],[-22,"22"],[-13,"13"],[-20,"20"],[-3,"3"],[-9,"9"],[-2,"2"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p3701"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p3702","attributes":{"axis":{"id":"p3698"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p3707","attributes":{"dimension":1,"axis":{"id":"p3703"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"e9714bd7-9d4e-4ed9-8560-83130b8f1b8e","roots":{"p3686":"e5d21d9f-46d3-46cc-b1f0-f3af98f500c7"},"root_ids":["p3686"]}];
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

<div id="b5a9003e-0bd0-4323-835e-6913a01e9fad" data-root-id="p3733" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"488c8f63-eac8-4371-b7cf-7e3a332281a9":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p3782","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p3783"}}},"roots":[{"type":"object","name":"Figure","id":"p3733","attributes":{"height":262,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p3742","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p3743","attributes":{"factors":["Goose astrovirus (1349999)","Bovine astrovirus (1435485)","Mamastrovirus hominis (3430629)","Mamastrovirus sp. (1912147)","Mamastrovirus suisencephalomyelitidis (3703181)","Mamastrovirus suisvulgaris (3703182)","Porcine astrovirus 2 (1105378)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p3744"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p3745"},"title":{"type":"object","name":"Title","id":"p3740","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p3777","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p3730","attributes":{"selected":{"type":"object","name":"Selection","id":"p3731","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p3732"},"data":{"type":"map","entries":[["y",["Goose astrovirus (1349999)","Bovine astrovirus (1435485)","Mamastrovirus hominis (3430629)","Mamastrovirus sp. (1912147)","Mamastrovirus suisencephalomyelitidis (3703181)","Mamastrovirus suisvulgaris (3703182)","Porcine astrovirus 2 (1105378)"]],["share",[95.65217391304348,100.0,100.0,100.0,100.0,100.0,100.0]],["lo",[85.46774097378093,90.59421741627975,88.97446045395641,97.01846062916736,90.1099007675596,95.77124930558794,92.58998703338824]],["hi",[98.79945544014434,100.0,100.0,100.0,100.0,100.0,100.0]],["n",[46,37,31,125,35,87,48]],["det",[44,37,31,125,35,87,48]],["colour",["#007d5c","#007d5c","#007d5c","#007d5c","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p3778","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3779"}}},"glyph":{"type":"object","name":"Scatter","id":"p3774","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p3775","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p3776","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p3741","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p3756"},{"type":"object","name":"BoxZoomTool","id":"p3757","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p3758","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p3764","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3763","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p3765","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p3766"},{"type":"object","name":"SaveTool","id":"p3767"},{"type":"object","name":"HoverTool","id":"p3781","attributes":{"renderers":[{"id":"p3777"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p3751","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p3752"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p3753"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3754"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p3746","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3747","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3748"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3749"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p3750","attributes":{"axis":{"id":"p3746"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p3755","attributes":{"dimension":1,"axis":{"id":"p3751"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p3768","attributes":{"source":{"id":"p3730"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p3780","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"488c8f63-eac8-4371-b7cf-7e3a332281a9","roots":{"p3733":"b5a9003e-0bd0-4323-835e-6913a01e9fad"},"root_ids":["p3733"]}];
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


## What reached the statistics

16,713 records were screened for this assay and **3,054 (18%)** were evaluable, meaning both primers landed in the right orientation and size range. 13,659 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 11,886 |
| `truncated` | 1,638 |
| `chance_anchor` | 132 |
| `chance_only` | 2 |
| `no_pair` | 1 |

