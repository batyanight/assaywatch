# ASTROVIRUS_RdRp_Chu_2008_round2

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**Astrovirus pan-family RdRp heminested PCR (Chu 2008), round 2**

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
| forward | `CGKTAYGATGGKACKATHCC` | 20 nt |
| reverse | `GGYTTKACCCACATNCCRAA` | 20 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 561 | 716 | 78.4% | 75.2% – 81.2% |
| baseline (everything earlier) | 2,010 | 2,591 | 77.6% | 75.9% – 79.1% |

Change from baseline, Newcombe interval: **-2.8% to 4.1%**. Threshold: **90.0%**.

*detected share 78.4% (75%-81%) since Oct 2024, upper bound below the 90% threshold; change from baseline -3% to +4% (no measurable fall from a baseline of 78%); separately, lineage Goose astrovirus (1349999) (46 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift*

Trend across deposit years: by record falling (p=2e-15, 29 years); by footprint falling (p=1.25e-05). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="ce5a6f0c-f59c-4418-8c54-36b7856ee1d4" data-root-id="p3375" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"f8f8b1fe-5043-4d26-bcaf-83ddba331b85":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p3430","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p3431"}}},"roots":[{"type":"object","name":"Figure","id":"p3375","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p3377"},"y_range":{"type":"object","name":"Range1d","id":"p3384","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p3385"},"y_scale":{"type":"object","name":"LinearScale","id":"p3386"},"title":{"type":"object","name":"Title","id":"p3382","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p3420","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p3372","attributes":{"selected":{"type":"object","name":"Selection","id":"p3373","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p3374"},"data":{"type":"map","entries":[["year",[1993,1994,1997,1999,2000,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,50.0,100.0,100.0,100.0,100.0,100.0,100.0,97.26027397260275,95.65217391304348,95.57522123893806,76.47058823529412,80.76923076923077,90.9090909090909,93.33333333333333,93.61702127659575,81.5126050420168,93.75,73.52941176470588,71.05263157894737,84.80392156862744,60.0,77.92792792792793,67.87878787878789,70.16129032258065,80.25210084033614,79.59183673469387,72.25130890052355]],["detected",[3,4,2,2,3,2,2,4,24,71,22,108,13,42,60,28,44,97,120,100,81,173,102,173,224,348,191,390,138]],["evaluable",[3,4,4,2,3,2,2,4,24,73,23,113,17,52,66,30,47,119,128,136,114,204,170,222,330,496,238,490,191]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.328625426046248,9.517227179437622,9.517227179437622,9.07684386569143,9.328625426046248,9.07684386569143,9.07684386569143,9.517227179437622,10.74264168206181,11.469403343404682,10.713966621835368,11.74200327633271,10.508782366508077,11.252690272875853,11.405466677556973,10.892023970177537,11.18724806845314,11.773797988966388,11.818431989729309,11.85539463710738,11.747425107358183,12.099112403217902,11.990267112817275,12.149186935252992,12.38060231778285,12.612955306165388,12.190209329699918,12.606093758811342,12.05994098863722]]]}}},"view":{"type":"object","name":"CDSView","id":"p3421","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3422"}}},"glyph":{"type":"object","name":"Line","id":"p3417","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p3418","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p3419","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p3426","attributes":{"data_source":{"id":"p3372"},"view":{"type":"object","name":"CDSView","id":"p3427","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3428"}}},"glyph":{"type":"object","name":"Scatter","id":"p3423","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p3424","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p3425","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p3383","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p3397"},{"type":"object","name":"BoxZoomTool","id":"p3398","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p3399","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p3405","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3404","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p3406","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p3407"},{"type":"object","name":"SaveTool","id":"p3408"},{"type":"object","name":"HoverTool","id":"p3429","attributes":{"renderers":[{"id":"p3426"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p3392","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3393","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3394"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3395"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p3387","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3388","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3389"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3390"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p3391","attributes":{"axis":{"id":"p3387"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p3396","attributes":{"dimension":1,"axis":{"id":"p3392"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p3409","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p3411","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p3412","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p3413","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p3415","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3414","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p3416","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"f8f8b1fe-5043-4d26-bcaf-83ddba331b85","roots":{"p3375":"ce5a6f0c-f59c-4418-8c54-36b7856ee1d4"},"root_ids":["p3375"]}];
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

<div id="fffdeb3c-7a94-4208-9499-3dd1ed5cfaa0" data-root-id="p3435" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"fd177dde-e8d4-46c1-a708-7aaee7da6b2e":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p3475","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p3476"}}},"roots":[{"type":"object","name":"Figure","id":"p3435","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p3436"},"y_range":{"type":"object","name":"DataRange1d","id":"p3437","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p3444"},"y_scale":{"type":"object","name":"LinearScale","id":"p3445"},"title":{"type":"object","name":"Title","id":"p3442","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p3471","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p3432","attributes":{"selected":{"type":"object","name":"Selection","id":"p3433","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p3434"},"data":{"type":"map","entries":[["year",[1993,1994,1997,1999,2000,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[3,4,4,2,3,2,2,4,24,73,23,113,17,52,66,30,47,119,128,136,114,204,170,222,330,496,238,490,191]],["detected",[3,4,2,2,3,2,2,4,24,71,22,108,13,42,60,28,44,97,120,100,81,173,102,173,224,348,191,390,138]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p3472","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3473"}}},"glyph":{"type":"object","name":"VBar","id":"p3468","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p3469","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p3470","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p3443","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p3456"},{"type":"object","name":"BoxZoomTool","id":"p3457","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p3458","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p3464","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3463","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p3465","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p3466"},{"type":"object","name":"SaveTool","id":"p3467"},{"type":"object","name":"HoverTool","id":"p3474","attributes":{"renderers":[{"id":"p3471"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p3451","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3452","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3453"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3454"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p3446","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3447","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3448"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3449"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p3450","attributes":{"axis":{"id":"p3446"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p3455","attributes":{"dimension":1,"axis":{"id":"p3451"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"fd177dde-e8d4-46c1-a708-7aaee7da6b2e","roots":{"p3435":"fffdeb3c-7a94-4208-9499-3dd1ed5cfaa0"},"root_ids":["p3435"]}];
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

<div id="c330701d-973e-4251-9204-d86b20be667d" data-root-id="p3480" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"03e88f27-f2c5-4a1c-968d-b6c2aa77b0c8":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p3522","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p3523"}}},"roots":[{"type":"object","name":"Figure","id":"p3480","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p3482"},"y_range":{"type":"object","name":"FactorRange","id":"p3489","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p3490"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p3491"},"title":{"type":"object","name":"Title","id":"p3487","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p3517","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p3477","attributes":{"selected":{"type":"object","name":"Selection","id":"p3478","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p3479"},"data":{"type":"map","entries":[["x",[-5,-11,-7,-1,-7,-17,-10,-9,-1,-8,-12,-14,-14,-11,-3,-19,-15,-12,-9,-6,-19,-20,-18,-13,-16]],["y",["forward","forward","forward","forward","reverse","forward","forward","reverse","reverse","forward","reverse","forward","reverse","reverse","forward","forward","reverse","forward","forward","forward","reverse","reverse","forward","reverse","forward"]],["alpha",[0.4872240701542183,0.2055185969156335,0.1972936195947989,0.19420925309948595,0.19420925309948595,0.1931811309343816,0.19009676443906864,0.184956153613547,0.17467493196250378,0.18598427577865134,0.20449047475052917,0.2014061082552162,0.17467493196250378,0.19009676443906864,0.445071061384941,0.1798155427880254,1.0,0.5581644995464167,1.0,1.0,0.6260205624433021,0.597233141820381,1.0,0.4471273057151497,1.0]],["pos",[5,11,7,1,7,17,10,9,1,8,12,14,14,11,3,19,15,12,9,6,19,20,18,13,16]],["base",["A","G","C","C","T","T","G","C","A","A","C","G","A","C","H","G","K","T","K","K","G","G","K","C","A"]],["n",[328,54,46,43,43,42,39,34,24,35,53,50,24,39,287,29,1688,397,1725,1535,463,435,1533,289,1835]],["det_with",["0% of 328","0% of 54","0% of 46","0% of 43","0% of 43","0% of 42","0% of 39","0% of 34","0% of 24","3% of 35","4% of 53","4% of 50","4% of 24","5% of 39","12% of 287","10% of 29","67% of 1688","71% of 397","74% of 1725","76% of 1535","75% of 463","76% of 435","79% of 1533","82% of 289","83% of 1835"]],["det_without",["86% of 2985","79% of 3259","79% of 3267","79% of 3270","79% of 3270","79% of 3271","79% of 3274","79% of 3279","79% of 3289","79% of 3278","79% of 3260","79% of 3263","79% of 3289","79% of 3274","84% of 3026","79% of 3284","90% of 1625","79% of 2916","82% of 1588","80% of 1778","78% of 2850","78% of 2878","77% of 1780","78% of 3024","72% of 1478"]],["subs",["A&gt;T 277, A&gt;G 30, A&gt;C 21","G&gt;C 28, G&gt;T 24, G&gt;A 2","C&gt;A 29, C&gt;G 10, C&gt;T 7","C&gt;A 27, C&gt;T 16","T&gt;C 31, T&gt;A 12","T&gt;A 29, T&gt;C 8, T&gt;G 5","G&gt;C 27, G&gt;A 11, G&gt;T 1","C&gt;T 32, C&gt;G 1, C&gt;A 1","A&gt;G 12, A&gt;C 7, A&gt;T 5","A&gt;T 26, A&gt;G 5, A&gt;C 4","C&gt;T 43, C&gt;A 7, C&gt;G 3","G&gt;A 31, G&gt;T 11, G&gt;C 8","A&gt;T 12, A&gt;C 10, A&gt;G 2","C&gt;T 30, C&gt;G 6, C&gt;A 3","H&gt;G 287","G&gt;T 25, G&gt;A 2, G&gt;C 2","K&gt;A 1361, K&gt;C 327","T&gt;C 367, T&gt;A 28, T&gt;G 2","K&gt;C 924, K&gt;A 801","K&gt;A 791, K&gt;C 744","G&gt;T 353, G&gt;C 73, G&gt;A 37","G&gt;C 244, G&gt;T 182, G&gt;A 9","K&gt;C 927, K&gt;A 343, G&gt;A 261, G&gt;C 2","C&gt;T 259, C&gt;G 24, C&gt;A 6","A&gt;T 1835"]],["zone",["yes","no","no","yes","no","no","no","no","yes","no","no","no","no","no","yes","no","no","no","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p3518","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3519"}}},"glyph":{"type":"object","name":"Rect","id":"p3514","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p3515","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p3516","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p3488","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p3502"},{"type":"object","name":"BoxZoomTool","id":"p3503","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p3504","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p3510","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3509","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p3511","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p3512"},{"type":"object","name":"SaveTool","id":"p3513"},{"type":"object","name":"HoverTool","id":"p3520","attributes":{"renderers":[{"id":"p3517"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p3497","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p3498"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p3499"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3500"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p3492","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p3521","attributes":{"ticks":[-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-3,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3494"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-5,"5"],[-11,"11"],[-7,"7"],[-1,"1"],[-17,"17"],[-10,"10"],[-9,"9"],[-8,"8"],[-12,"12"],[-14,"14"],[-3,"3"],[-19,"19"],[-15,"15"],[-6,"6"],[-20,"20"],[-18,"18"],[-13,"13"],[-16,"16"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p3495"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p3496","attributes":{"axis":{"id":"p3492"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p3501","attributes":{"dimension":1,"axis":{"id":"p3497"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"03e88f27-f2c5-4a1c-968d-b6c2aa77b0c8","roots":{"p3480":"c330701d-973e-4251-9204-d86b20be667d"},"root_ids":["p3480"]}];
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

<div id="a4064ce9-738c-490d-ba5f-0dd77edbb3f6" data-root-id="p3527" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"5c32d738-ee4f-409a-95b7-44b8c7616b52":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p3576","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p3577"}}},"roots":[{"type":"object","name":"Figure","id":"p3527","attributes":{"height":262,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p3536","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p3537","attributes":{"factors":["Goose astrovirus (1349999)","Mamastrovirus suisencephalomyelitidis (3703181)","Mamastrovirus sp. (1912147)","Bovine astrovirus (1435485)","Porcine astrovirus 2 (1105378)","Mamastrovirus suisvulgaris (3703182)","Mamastrovirus hominis (3430629)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p3538"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p3539"},"title":{"type":"object","name":"Title","id":"p3534","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p3571","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p3524","attributes":{"selected":{"type":"object","name":"Selection","id":"p3525","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p3526"},"data":{"type":"map","entries":[["y",["Goose astrovirus (1349999)","Mamastrovirus suisencephalomyelitidis (3703181)","Mamastrovirus sp. (1912147)","Bovine astrovirus (1435485)","Porcine astrovirus 2 (1105378)","Mamastrovirus suisvulgaris (3703182)","Mamastrovirus hominis (3430629)"]],["share",[0.0,80.0,84.375,86.48648648648648,89.58333333333334,96.55172413793103,100.0]],["lo",[0.0,64.10838693433439,77.09518905710296,72.02258821599021,77.83257830561368,90.34591761312561,88.97446045395641]],["hi",[7.7073563085580385,89.95755352620137,89.65164519909334,94.086705574268,95.46782809581869,98.82041794724941,100.0]],["n",[46,35,128,37,48,87,31]],["det",[0,28,108,32,43,84,31]],["colour",["#b3261e","#b3261e","#b3261e","#007d5c","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p3572","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p3573"}}},"glyph":{"type":"object","name":"Scatter","id":"p3568","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p3569","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p3570","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p3535","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p3550"},{"type":"object","name":"BoxZoomTool","id":"p3551","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p3552","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p3558","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p3557","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p3559","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p3560"},{"type":"object","name":"SaveTool","id":"p3561"},{"type":"object","name":"HoverTool","id":"p3575","attributes":{"renderers":[{"id":"p3571"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p3545","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p3546"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p3547"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3548"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p3540","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p3541","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p3542"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p3543"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p3544","attributes":{"axis":{"id":"p3540"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p3549","attributes":{"dimension":1,"axis":{"id":"p3545"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p3562","attributes":{"source":{"id":"p3524"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p3574","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"5c32d738-ee4f-409a-95b7-44b8c7616b52","roots":{"p3527":"a4064ce9-738c-490d-ba5f-0dd77edbb3f6"},"root_ids":["p3527"]}];
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

16,713 records were screened for this assay and **3,307 (20%)** were evaluable, meaning both primers landed in the right orientation and size range. 13,406 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 11,765 |
| `truncated` | 935 |
| `chance_anchor` | 501 |
| `chance_only` | 204 |
| `no_pair` | 1 |

