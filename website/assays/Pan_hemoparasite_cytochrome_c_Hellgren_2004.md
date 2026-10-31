# Pan_hemoparasite_cytochrome_c_Hellgren_2004

<span class="aw-chip aw-chip-declining">declining</span>

**Pan-hemoparasite — cytochrome c**

| | |
|---|---|
| Target | Haemosporida ([taxid 5819](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=5819)) |
| Gene | cytochrome c |
| Chemistry | conventional |
| Amplicon | 617 bp |
| Designed | 2004 |
| Paper | [10.1645/GE-184R1](https://doi.org/10.1645/GE-184R1) |
| Registry status | active |

!!! quote "The paper"
    Hellgren O, Waldenström J, Bensch S. 2004. J Parasitol 90:797-802

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CATATATTAAGAGAANTATGGAG` | 23 nt |
| reverse | `ATAGAAAGATAAGAAATACCATTC` | 24 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 129 | 193 | 66.8% | 59.9% – 73.1% |
| baseline (everything earlier) | 717 | 830 | 86.4% | 83.9% – 88.6% |

Change from baseline, Newcombe interval: **-26.8% to -12.8%**. Threshold: **90.0%**.

*detected share 66.8% (60%-73%) since Oct 2024, upper bound below the 90% threshold; change from baseline -27% to -13%*

Trend across deposit years: by record rising (p=0.149, 25 years); by footprint falling (p=0.101); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="c392d900-89ab-4059-9688-3c39e608ea60" data-root-id="p27780" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"616575ed-4f6e-41fe-b526-1ebe167d02d0":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p27835","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p27836"}}},"roots":[{"type":"object","name":"Figure","id":"p27780","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p27782"},"y_range":{"type":"object","name":"Range1d","id":"p27789","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p27790"},"y_scale":{"type":"object","name":"LinearScale","id":"p27791"},"title":{"type":"object","name":"Title","id":"p27787","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p27825","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p27777","attributes":{"selected":{"type":"object","name":"Selection","id":"p27778","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p27779"},"data":{"type":"map","entries":[["year",[1998,2002,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,2.4390243902439024,100.0,100.0,93.75,87.8048780487805,90.12345679012346,62.5,14.285714285714285,72.72727272727273,100.0,100.0,91.66666666666666,92.10526315789474,96.15384615384616,43.75,98.85057471264368,100.0,96.72131147540983,93.93939393939394,85.24590163934425,57.02479338842975,83.33333333333334]],["detected",[3,38,5,1,15,3,30,36,73,20,1,8,13,14,11,70,75,7,86,4,59,93,52,69,60]],["evaluable",[3,38,5,41,15,3,32,41,81,32,7,11,13,14,12,76,78,16,87,4,61,99,61,121,72]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.328625426046248,11.048392086352559,9.667366891029102,11.098224018878925,10.423139468338052,9.328625426046248,10.934913263353746,11.098224018878925,11.53494852413258,10.934913263353746,9.897626379762722,10.209683151927734,10.324834530005162,10.37579022724969,10.269703144398052,11.49483773413666,11.511208920139431,10.467343773689333,11.579747479020243,9.517227179437622,11.355225445040746,11.660254037844386,11.355225445040746,11.784019340078249,11.460677957646856]]]}}},"view":{"type":"object","name":"CDSView","id":"p27826","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p27827"}}},"glyph":{"type":"object","name":"Line","id":"p27822","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p27823","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p27824","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p27831","attributes":{"data_source":{"id":"p27777"},"view":{"type":"object","name":"CDSView","id":"p27832","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p27833"}}},"glyph":{"type":"object","name":"Scatter","id":"p27828","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p27829","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p27830","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p27788","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p27802"},{"type":"object","name":"BoxZoomTool","id":"p27803","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p27804","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p27810","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p27809","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p27811","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p27812"},{"type":"object","name":"SaveTool","id":"p27813"},{"type":"object","name":"HoverTool","id":"p27834","attributes":{"renderers":[{"id":"p27831"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p27797","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p27798","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p27799"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p27800"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p27792","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p27793","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p27794"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p27795"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p27796","attributes":{"axis":{"id":"p27792"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p27801","attributes":{"dimension":1,"axis":{"id":"p27797"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p27814","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p27816","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p27817","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p27818","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p27820","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p27819","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p27821","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"616575ed-4f6e-41fe-b526-1ebe167d02d0","roots":{"p27780":"c392d900-89ab-4059-9688-3c39e608ea60"},"root_ids":["p27780"]}];
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

<div id="c9141c06-f9db-4e87-a38c-cce4fe7027e2" data-root-id="p27840" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"142f7833-e250-4014-af7b-385404cfb764":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p27880","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p27881"}}},"roots":[{"type":"object","name":"Figure","id":"p27840","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p27841"},"y_range":{"type":"object","name":"DataRange1d","id":"p27842","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p27849"},"y_scale":{"type":"object","name":"LinearScale","id":"p27850"},"title":{"type":"object","name":"Title","id":"p27847","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p27876","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p27837","attributes":{"selected":{"type":"object","name":"Selection","id":"p27838","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p27839"},"data":{"type":"map","entries":[["year",[1998,2002,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[3,38,5,41,15,3,32,41,81,32,7,11,13,14,12,76,78,16,87,4,61,99,61,121,72]],["detected",[3,38,5,1,15,3,30,36,73,20,1,8,13,14,11,70,75,7,86,4,59,93,52,69,60]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p27877","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p27878"}}},"glyph":{"type":"object","name":"VBar","id":"p27873","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p27874","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p27875","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p27848","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p27861"},{"type":"object","name":"BoxZoomTool","id":"p27862","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p27863","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p27869","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p27868","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p27870","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p27871"},{"type":"object","name":"SaveTool","id":"p27872"},{"type":"object","name":"HoverTool","id":"p27879","attributes":{"renderers":[{"id":"p27876"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p27856","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p27857","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p27858"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p27859"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p27851","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p27852","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p27853"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p27854"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p27855","attributes":{"axis":{"id":"p27851"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p27860","attributes":{"dimension":1,"axis":{"id":"p27856"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"142f7833-e250-4014-af7b-385404cfb764","roots":{"p27840":"c9141c06-f9db-4e87-a38c-cce4fe7027e2"},"root_ids":["p27840"]}];
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

<div id="d16a440d-2263-4f62-a20c-c3ab8b7d414d" data-root-id="p27885" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"e241efc0-cd4b-4714-a138-4c6fcf4fcec0":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p27927","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p27928"}}},"roots":[{"type":"object","name":"Figure","id":"p27885","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p27887"},"y_range":{"type":"object","name":"FactorRange","id":"p27894","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p27895"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p27896"},"title":{"type":"object","name":"Title","id":"p27892","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p27922","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p27882","attributes":{"selected":{"type":"object","name":"Selection","id":"p27883","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p27884"},"data":{"type":"map","entries":[["x",[-12,-18,-18,-9,-16,-21,-13,-21,-2,-22,-4,-12,-23,-10,-5,-3,-6,-9,-15,-1,-24,-3,-17]],["y",["reverse","forward","reverse","reverse","reverse","reverse","reverse","forward","forward","forward","forward","forward","forward","forward","forward","forward","forward","forward","reverse","forward","reverse","reverse","forward"]],["alpha",[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.8280058651026393,0.5455034213098728,0.3627077223851417,0.27961876832844573,0.5587976539589443,0.3793255131964809,0.3693548387096774,0.3660312805474096,0.2929130009775171,1.0,0.3028836754643206,0.8113880742913001,0.4823558162267839,0.336119257086999,1.0]],["pos",[12,18,18,9,16,21,13,21,2,22,4,12,23,10,5,3,6,9,15,1,24,3,17]],["base",["G","A","A","A","A","G","A","T","A","A","G","A","C","A","T","G","A","A","T","G","A","T","T"]],["n",[4292,4820,4898,3852,6207,5928,1816,2494,204,119,64,39,123,69,66,65,43,615,46,199,100,56,478]],["det_with",["9% of 4292","18% of 4820","20% of 4898","11% of 3852","34% of 6207","32% of 5928","3% of 1816","9% of 2494","0% of 204","0% of 119","0% of 64","0% of 39","2% of 123","1% of 69","2% of 66","2% of 65","9% of 43","12% of 615","24% of 46","36% of 199","48% of 100","91% of 56","90% of 478"]],["det_without",["91% of 2183","92% of 1655","90% of 1577","74% of 2623","91% of 268","88% of 547","50% of 4659","54% of 3981","38% of 6271","37% of 6356","37% of 6411","37% of 6436","37% of 6352","37% of 6406","37% of 6409","37% of 6410","37% of 6432","39% of 5860","37% of 6429","37% of 6276","37% of 6375","36% of 6419","32% of 5997"]],["subs",["G&gt;A 4292","A&gt;T 4450, A&gt;C 284, A&gt;G 86","A&gt;T 4883, A&gt;G 9, A&gt;C 6","A&gt;G 3852","A&gt;G 6086, A&gt;C 121","G&gt;A 5928","A&gt;G 1816","T&gt;C 2494","A&gt;T 141, A&gt;G 63","A&gt;C 61, A&gt;T 57, A&gt;G 1","G&gt;A 64","A&gt;G 39","C&gt;T 123","A&gt;G 68, A&gt;T 1","T&gt;A 65, T&gt;C 1","G&gt;T 56, G&gt;C 8, G&gt;A 1","A&gt;G 41, A&gt;C 2","A&gt;G 613, A&gt;T 2","T&gt;C 46","G&gt;A 139, G&gt;C 59, G&gt;T 1","A&gt;G 100","T&gt;C 55, T&gt;A 1","T&gt;A 336, T&gt;C 129, T&gt;G 13"]],["zone",["no","no","no","no","no","no","no","no","yes","no","yes","no","no","no","yes","yes","no","no","no","yes","no","yes","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p27923","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p27924"}}},"glyph":{"type":"object","name":"Rect","id":"p27919","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p27920","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p27921","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p27893","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p27907"},{"type":"object","name":"BoxZoomTool","id":"p27908","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p27909","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p27915","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p27914","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p27916","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p27917"},{"type":"object","name":"SaveTool","id":"p27918"},{"type":"object","name":"HoverTool","id":"p27925","attributes":{"renderers":[{"id":"p27922"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p27902","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p27903"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p27904"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p27905"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p27897","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p27926","attributes":{"ticks":[-24,-23,-22,-21,-18,-17,-16,-15,-13,-12,-10,-9,-6,-5,-4,-3,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p27899"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-12,"12"],[-18,"18"],[-9,"9"],[-16,"16"],[-21,"21"],[-13,"13"],[-2,"2"],[-22,"22"],[-4,"4"],[-23,"23"],[-10,"10"],[-5,"5"],[-3,"3"],[-6,"6"],[-15,"15"],[-1,"1"],[-24,"24"],[-17,"17"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p27900"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p27901","attributes":{"axis":{"id":"p27897"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p27906","attributes":{"dimension":1,"axis":{"id":"p27902"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"e241efc0-cd4b-4714-a138-4c6fcf4fcec0","roots":{"p27885":"d16a440d-2263-4f62-a20c-c3ab8b7d414d"},"root_ids":["p27885"]}];
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

<div id="aeb30891-40bc-494f-b8ec-39d414bbe98a" data-root-id="p27932" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"ee8dd190-4a03-4a2b-a75d-4bb01df8eac8":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p27981","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p27982"}}},"roots":[{"type":"object","name":"Figure","id":"p27932","attributes":{"height":132,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p27941","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p27942","attributes":{"factors":["Leucocytozoon sp. (1504291)","Haemoproteus sp. (191679)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p27943"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p27944"},"title":{"type":"object","name":"Title","id":"p27939","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p27976","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p27929","attributes":{"selected":{"type":"object","name":"Selection","id":"p27930","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p27931"},"data":{"type":"map","entries":[["y",["Leucocytozoon sp. (1504291)","Haemoproteus sp. (191679)"]],["share",[27.500000000000004,100.0]],["lo",[18.9177571880842,94.07561321018872]],["hi",[38.14405864101452,100.0]],["n",[80,61]],["det",[22,61]],["colour",["#b3261e","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p27977","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p27978"}}},"glyph":{"type":"object","name":"Scatter","id":"p27973","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p27974","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p27975","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p27940","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p27955"},{"type":"object","name":"BoxZoomTool","id":"p27956","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p27957","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p27963","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p27962","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p27964","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p27965"},{"type":"object","name":"SaveTool","id":"p27966"},{"type":"object","name":"HoverTool","id":"p27980","attributes":{"renderers":[{"id":"p27976"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p27950","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p27951"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p27952"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p27953"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p27945","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p27946","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p27947"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p27948"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p27949","attributes":{"axis":{"id":"p27945"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p27954","attributes":{"dimension":1,"axis":{"id":"p27950"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p27967","attributes":{"source":{"id":"p27929"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p27979","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"ee8dd190-4a03-4a2b-a75d-4bb01df8eac8","roots":{"p27932":"aeb30891-40bc-494f-b8ec-39d414bbe98a"},"root_ids":["p27932"]}];
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

This entry declares **`scope_taxids`**: [418104](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=418104), [418105](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=418105), [418110](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=418110), [418112](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=418112), [419353](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=419353), [77521](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=77521), [587283](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=587283), [195944](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=195944). A record counts toward the denominator when its taxid, or any ancestor, is in that set. Records outside it are screened and reported but kept out of the statistics.

13,071 screened records fell outside the declared scope.

Retrieval query:

```
cytb[Gene] OR cob[Gene] OR "cytochrome b"[Title] OR cytb[Title] OR "complete genome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `oligos_not_in_cited_paper`, `orientation_inferred`.


## What reached the statistics

18,980 records were screened for this assay and **1,023 (5%)** were evaluable, meaning both primers landed in the right orientation and size range. 17,957 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 16,593 |
| `truncated` | 948 |
| `chance_anchor` | 402 |
| `no_pair` | 14 |

