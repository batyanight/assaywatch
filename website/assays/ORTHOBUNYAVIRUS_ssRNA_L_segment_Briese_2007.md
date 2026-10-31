# ORTHOBUNYAVIRUS_ssRNA_L_segment_Briese_2007

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**ORTHOBUNYAVIRUS (ssRNA) — L segment, BUNL-5n/BUNL650R (Briese 2007)**

| | |
|---|---|
| Target | Orthobunyavirus ([taxid 11572](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11572)) |
| Gene | L segment |
| Chemistry | conventional |
| Amplicon | 630 bp |
| Designed | 2007 |
| Paper | [10.1007/s00705-007-1069-z](https://doi.org/10.1007/s00705-007-1069-z) |
| Registry status | active |

!!! quote "The paper"
    Briese, T., Kapoor, V. & Lipkin, W. I. Natural M-segment reassortment in Potosi and Main Drain viruses: implications for the evolution of orthobunyaviruses. Archives of Virology 152, 2237-2247 (2007).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CGCCGCAGTAGTGTACTYCTA` | 21 nt |
| reverse | `ACCAKGGTGCTGTMARAGTGAARTCWCCAT` | 30 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (48 months, from Oct 2022) | 3 | 23 | 13.0% | 4.5% – 32.1% |
| baseline (everything earlier) | 50 | 169 | 29.6% | 23.2% – 36.9% |

Change from baseline, Newcombe interval: **-27.7% to 3.6%**. Threshold: **90.0%**.

*detected share 13.0% (5%-32%) since Oct 2022, upper bound below the 90% threshold; change from baseline -28% to +4% (no measurable fall from a baseline of 30%) (window widened to 48 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=2.63e-05, 23 years); by footprint falling (p=0.00662). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="a72238ca-b829-48a6-b73e-bbbbf794f38c" data-root-id="p20786" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"f8ac806d-50d8-47fa-b8f3-254dadcacaf1":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20841","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20842"}}},"roots":[{"type":"object","name":"Figure","id":"p20786","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p20788"},"y_range":{"type":"object","name":"Range1d","id":"p20795","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p20796"},"y_scale":{"type":"object","name":"LinearScale","id":"p20797"},"title":{"type":"object","name":"Title","id":"p20793","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20831","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20783","attributes":{"selected":{"type":"object","name":"Selection","id":"p20784","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20785"},"data":{"type":"map","entries":[["year",[1991,1994,2002,2006,2007,2008,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,0.0,0.0,0.0,50.0,87.5,0.0,25.0,52.63157894736842,6.25,3.3333333333333335,86.66666666666667,16.666666666666664,0.0,0.0,10.0,42.857142857142854,16.666666666666664,0.0,0.0,0.0]],["detected",[1,1,1,0,0,0,3,14,0,1,10,1,1,13,2,0,0,1,3,1,0,0,0]],["evaluable",[1,1,1,1,1,6,6,16,7,4,19,16,30,15,12,7,15,10,7,6,6,4,1]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193,9.791719296345839,9.791719296345839,10.467343773689333,9.897626379762722,9.517227179437622,10.584573151575475,10.467343773689333,10.892023970177537,10.423139468338052,10.269703144398052,9.897626379762722,10.423139468338052,10.143865699252444,9.897626379762722,9.791719296345839,9.791719296345839,9.517227179437622,8.703135093227193]]]}}},"view":{"type":"object","name":"CDSView","id":"p20832","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20833"}}},"glyph":{"type":"object","name":"Line","id":"p20828","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p20829","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p20830","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p20837","attributes":{"data_source":{"id":"p20783"},"view":{"type":"object","name":"CDSView","id":"p20838","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20839"}}},"glyph":{"type":"object","name":"Scatter","id":"p20834","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p20835","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p20836","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20794","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20808"},{"type":"object","name":"BoxZoomTool","id":"p20809","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20810","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20816","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20815","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20817","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20818"},{"type":"object","name":"SaveTool","id":"p20819"},{"type":"object","name":"HoverTool","id":"p20840","attributes":{"renderers":[{"id":"p20837"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p20803","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20804","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20805"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20806"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20798","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20799","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20800"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20801"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20802","attributes":{"axis":{"id":"p20798"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20807","attributes":{"dimension":1,"axis":{"id":"p20803"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p20820","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2021.5,"right":{"type":"object","name":"Node","id":"p20822","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p20823","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p20824","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p20826","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20825","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p20827","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"f8ac806d-50d8-47fa-b8f3-254dadcacaf1","roots":{"p20786":"a72238ca-b829-48a6-b73e-bbbbf794f38c"},"root_ids":["p20786"]}];
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

<div id="bda75802-89ef-4986-91f8-58e0c77e3b00" data-root-id="p20846" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"e8ec45bd-8bd4-4614-bf01-7ec6b8a89918":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20886","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20887"}}},"roots":[{"type":"object","name":"Figure","id":"p20846","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p20847"},"y_range":{"type":"object","name":"DataRange1d","id":"p20848","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p20855"},"y_scale":{"type":"object","name":"LinearScale","id":"p20856"},"title":{"type":"object","name":"Title","id":"p20853","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20882","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20843","attributes":{"selected":{"type":"object","name":"Selection","id":"p20844","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20845"},"data":{"type":"map","entries":[["year",[1991,1994,2002,2006,2007,2008,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,1,1,1,6,6,16,7,4,19,16,30,15,12,7,15,10,7,6,6,4,1]],["detected",[1,1,1,0,0,0,3,14,0,1,10,1,1,13,2,0,0,1,3,1,0,0,0]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p20883","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20884"}}},"glyph":{"type":"object","name":"VBar","id":"p20879","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p20880","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p20881","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20854","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20867"},{"type":"object","name":"BoxZoomTool","id":"p20868","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20869","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20875","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20874","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20876","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20877"},{"type":"object","name":"SaveTool","id":"p20878"},{"type":"object","name":"HoverTool","id":"p20885","attributes":{"renderers":[{"id":"p20882"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p20862","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20863","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20864"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20865"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20857","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20858","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20859"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20860"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20861","attributes":{"axis":{"id":"p20857"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20866","attributes":{"dimension":1,"axis":{"id":"p20862"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"e8ec45bd-8bd4-4614-bf01-7ec6b8a89918","roots":{"p20846":"bda75802-89ef-4986-91f8-58e0c77e3b00"},"root_ids":["p20846"]}];
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

<div id="cbf3e612-1378-4980-99ee-bfd7088bb9c9" data-root-id="p20891" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"332aa975-cae3-411d-8b75-f23582ee2447":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20933","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20934"}}},"roots":[{"type":"object","name":"Figure","id":"p20891","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p20893"},"y_range":{"type":"object","name":"FactorRange","id":"p20900","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p20901"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p20902"},"title":{"type":"object","name":"Title","id":"p20898","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20928","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20888","attributes":{"selected":{"type":"object","name":"Selection","id":"p20889","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20890"},"data":{"type":"map","entries":[["x",[-11,-8,-6,-7,-13,-1,-12,-2,-3,-5,-4,-5,-26,-17,-11,-14,-20,-23]],["y",["forward","forward","forward","forward","forward","forward","forward","forward","forward","forward","forward","reverse","reverse","reverse","reverse","reverse","reverse","reverse"]],["alpha",[1.0,1.0,1.0,0.9822916666666667,0.8229166666666666,0.7875,0.7520833333333333,0.6635416666666667,0.6635416666666667,0.7697916666666667,0.521875,0.7166666666666667,0.8052083333333334,1.0,1.0,1.0,1.0,0.7697916666666667]],["pos",[11,8,6,7,13,1,12,2,3,5,4,5,26,17,11,14,20,23]],["base",["G","T","C","A","T","A","A","T","C","T","Y","W","K","M","G","A","T","T"]],["n",[71,68,57,47,38,36,34,29,29,35,21,32,37,54,60,88,53,35]],["det_with",["0% of 71","0% of 68","0% of 57","0% of 47","0% of 38","0% of 36","0% of 34","0% of 29","0% of 29","3% of 35","0% of 21","19% of 32","24% of 37","28% of 54","28% of 60","36% of 88","40% of 53","43% of 35"]],["det_without",["61% of 87","59% of 90","52% of 101","48% of 111","44% of 120","43% of 122","43% of 124","41% of 129","41% of 129","42% of 123","39% of 137","37% of 126","36% of 121","37% of 104","37% of 98","30% of 70","30% of 105","31% of 123"]],["subs",["G&gt;C 40, G&gt;A 30, G&gt;T 1","T&gt;A 42, T&gt;G 23, T&gt;C 3","C&gt;A 41, C&gt;G 13, C&gt;T 3","A&gt;T 23, A&gt;C 23, A&gt;G 1","T&gt;C 27, T&gt;A 10, T&gt;G 1","A&gt;T 21, A&gt;C 8, A&gt;G 7","A&gt;G 26, A&gt;T 6, A&gt;C 2","T&gt;C 20, T&gt;A 8, T&gt;G 1","C&gt;T 24, C&gt;G 3, C&gt;A 2","T&gt;C 20, T&gt;A 15","Y&gt;A 18, Y&gt;G 3","W&gt;G 22, W&gt;C 10","K&gt;A 34, K&gt;C 3","M&gt;T 51, M&gt;G 3","G&gt;A 53, G&gt;C 7","A&gt;T 51, A&gt;G 32, A&gt;C 5","T&gt;A 37, T&gt;C 16","T&gt;A 15, T&gt;C 11, T&gt;G 9"]],["zone",["no","no","no","no","no","yes","no","yes","yes","yes","yes","yes","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p20929","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20930"}}},"glyph":{"type":"object","name":"Rect","id":"p20925","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p20926","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p20927","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20899","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20913"},{"type":"object","name":"BoxZoomTool","id":"p20914","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20915","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20921","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20920","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20922","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20923"},{"type":"object","name":"SaveTool","id":"p20924"},{"type":"object","name":"HoverTool","id":"p20931","attributes":{"renderers":[{"id":"p20928"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p20908","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p20909"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p20910"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20911"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20903","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p20932","attributes":{"ticks":[-26,-23,-20,-17,-14,-13,-12,-11,-8,-7,-6,-5,-4,-3,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20905"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-11,"11"],[-8,"8"],[-6,"6"],[-7,"7"],[-13,"13"],[-1,"1"],[-12,"12"],[-2,"2"],[-3,"3"],[-5,"5"],[-4,"4"],[-26,"26"],[-17,"17"],[-14,"14"],[-20,"20"],[-23,"23"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p20906"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20907","attributes":{"axis":{"id":"p20903"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20912","attributes":{"dimension":1,"axis":{"id":"p20908"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"332aa975-cae3-411d-8b75-f23582ee2447","roots":{"p20891":"cbf3e612-1378-4980-99ee-bfd7088bb9c9"},"root_ids":["p20891"]}];
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
L[Gene] OR "L segment"[Title] OR polymerase[Title] OR "RNA-dependent RNA polymerase"[Title] OR "complete genome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).


## What reached the statistics

2,143 records were screened for this assay and **192 (9%)** were evaluable, meaning both primers landed in the right orientation and size range. 1,951 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 1,756 |
| `truncated` | 112 |
| `chance_anchor` | 75 |
| `no_pair` | 8 |

