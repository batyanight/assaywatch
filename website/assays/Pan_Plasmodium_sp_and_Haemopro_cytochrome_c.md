# Pan_Plasmodium_sp_and_Haemopro_cytochrome_c

<span class="aw-chip aw-chip-declining">declining</span>

**Pan-Plasmodium sp. and Haemoproteus sp. — cytochrome c**

| | |
|---|---|
| Target | Haemosporida ([taxid 5819](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=5819)) |
| Gene | cytochrome c |
| Chemistry | conventional |
| Amplicon | 480 bp |
| Designed | 2004 |
| Paper | [10.1645/GE-184R1](https://doi.org/10.1645/GE-184R1) |
| Registry status | active |

!!! quote "The paper"
    Hellgren O et al. 2004. J Parasitol 90:797-802 (HaemF/HaemR2 nested round)

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ATGGTGCTTTCGATATATGCATG` | 23 nt |
| reverse | `GCATTATCTGGATGTGATAATGGT` | 24 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 16 | 155 | 10.3% | 6.5% – 16.1% |
| baseline (everything earlier) | 320 | 1,626 | 19.7% | 17.8% – 21.7% |

Change from baseline, Newcombe interval: **-13.7% to -3.3%**. Threshold: **90.0%**.

*detected share 10.3% (6%-16%) since Oct 2024, upper bound below the 90% threshold; change from baseline -14% to -3%; separately, lineage Haemoproteus sp. (191679) (65 records) detects only 7.7% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift*

Trend across deposit years: by record rising (p=0.000393, 25 years); by footprint rising (p=5.08e-06). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="f04fab32-2c90-44b1-bac7-97ef4d669f06" data-root-id="p26858" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"5a85d2cc-c5b3-43c0-bd32-db04a93a0bee":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p26913","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p26914"}}},"roots":[{"type":"object","name":"Figure","id":"p26858","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p26860"},"y_range":{"type":"object","name":"Range1d","id":"p26867","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p26868"},"y_scale":{"type":"object","name":"LinearScale","id":"p26869"},"title":{"type":"object","name":"Title","id":"p26865","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p26903","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p26855","attributes":{"selected":{"type":"object","name":"Selection","id":"p26856","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p26857"},"data":{"type":"map","entries":[["year",[1998,2002,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,25.0,60.0,1.5873015873015872,19.230769230769234,0.0,0.0,21.052631578947366,37.64705882352941,10.843373493975903,3.4482758620689653,52.94117647058824,0.9174311926605505,14.035087719298245,23.076923076923077,29.807692307692307,39.0625,10.81081081081081,1.9083969465648856,57.14285714285714,90.12345679012346,17.475728155339805,33.33333333333333,10.526315789473683,10.38961038961039]],["detected",[3,9,3,1,5,0,0,8,32,9,1,9,2,8,9,62,25,4,5,8,73,18,26,8,8]],["evaluable",[3,36,5,63,26,22,60,38,85,83,29,17,218,57,39,208,64,37,262,14,81,103,78,76,77]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.328625426046248,11.012804945939648,9.667366891029102,11.375828278421016,10.796415465069488,10.683957047019447,11.34465373009984,11.048392086352559,11.56518892267352,11.550262110107914,10.869436534339137,10.508782366508077,12.138440943126074,11.311780786273989,11.06545099688784,12.11063428926748,11.385871088686695,11.030852377887435,12.2465611830693,10.37579022724969,11.53494852413258,11.684804746364165,11.511208920139431,11.49483773413666,11.503079740144862]]]}}},"view":{"type":"object","name":"CDSView","id":"p26904","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p26905"}}},"glyph":{"type":"object","name":"Line","id":"p26900","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p26901","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p26902","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p26909","attributes":{"data_source":{"id":"p26855"},"view":{"type":"object","name":"CDSView","id":"p26910","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p26911"}}},"glyph":{"type":"object","name":"Scatter","id":"p26906","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p26907","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p26908","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p26866","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p26880"},{"type":"object","name":"BoxZoomTool","id":"p26881","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p26882","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p26888","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p26887","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p26889","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p26890"},{"type":"object","name":"SaveTool","id":"p26891"},{"type":"object","name":"HoverTool","id":"p26912","attributes":{"renderers":[{"id":"p26909"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p26875","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p26876","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p26877"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p26878"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p26870","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p26871","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p26872"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p26873"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p26874","attributes":{"axis":{"id":"p26870"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p26879","attributes":{"dimension":1,"axis":{"id":"p26875"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p26892","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p26894","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p26895","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p26896","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p26898","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p26897","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p26899","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"5a85d2cc-c5b3-43c0-bd32-db04a93a0bee","roots":{"p26858":"f04fab32-2c90-44b1-bac7-97ef4d669f06"},"root_ids":["p26858"]}];
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

<div id="ef7b6b7a-b8d4-459d-8743-f9b4d1c8b9dd" data-root-id="p26918" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"fcad6929-e8f2-4f16-9e82-70244166250b":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p26958","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p26959"}}},"roots":[{"type":"object","name":"Figure","id":"p26918","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p26919"},"y_range":{"type":"object","name":"DataRange1d","id":"p26920","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p26927"},"y_scale":{"type":"object","name":"LinearScale","id":"p26928"},"title":{"type":"object","name":"Title","id":"p26925","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p26954","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p26915","attributes":{"selected":{"type":"object","name":"Selection","id":"p26916","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p26917"},"data":{"type":"map","entries":[["year",[1998,2002,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[3,36,5,63,26,22,60,38,85,83,29,17,218,57,39,208,64,37,262,14,81,103,78,76,77]],["detected",[3,9,3,1,5,0,0,8,32,9,1,9,2,8,9,62,25,4,5,8,73,18,26,8,8]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p26955","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p26956"}}},"glyph":{"type":"object","name":"VBar","id":"p26951","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p26952","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p26953","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p26926","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p26939"},{"type":"object","name":"BoxZoomTool","id":"p26940","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p26941","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p26947","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p26946","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p26948","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p26949"},{"type":"object","name":"SaveTool","id":"p26950"},{"type":"object","name":"HoverTool","id":"p26957","attributes":{"renderers":[{"id":"p26954"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p26934","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p26935","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p26936"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p26937"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p26929","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p26930","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p26931"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p26932"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p26933","attributes":{"axis":{"id":"p26929"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p26938","attributes":{"dimension":1,"axis":{"id":"p26934"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"fcad6929-e8f2-4f16-9e82-70244166250b","roots":{"p26918":"ef7b6b7a-b8d4-459d-8743-f9b4d1c8b9dd"},"root_ids":["p26918"]}];
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

<div id="b6a70b82-59fb-420b-8bec-0c0c72c01f18" data-root-id="p26963" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b58f269c-9e9f-45db-b0f2-6e14df8adc09":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p27005","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p27006"}}},"roots":[{"type":"object","name":"Figure","id":"p26963","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p26965"},"y_range":{"type":"object","name":"FactorRange","id":"p26972","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p26973"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p26974"},"title":{"type":"object","name":"Title","id":"p26970","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p27000","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p26960","attributes":{"selected":{"type":"object","name":"Selection","id":"p26961","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p26962"},"data":{"type":"map","entries":[["x",[-13,-17,-1,-4,-1,-5,-7,-18,-19,-16,-2,-14,-9,-16,-8,-2,-24,-8,-23,-10,-5,-13,-22,-14,-19,-23]],["y",["forward","forward","reverse","reverse","forward","forward","forward","forward","forward","forward","reverse","reverse","reverse","reverse","forward","forward","reverse","reverse","reverse","reverse","reverse","reverse","reverse","forward","reverse","forward"]],["alpha",[1.0,1.0,1.0,1.0,0.7131667602470523,0.594806288601909,0.4993542953396968,1.0,1.0,0.2492700729927007,0.235906793935991,0.3599943851768669,0.2855418304323414,1.0,1.0,1.0,0.2187254351487928,1.0,0.4669006176305447,1.0,0.2912689500280741,0.2492700729927007,0.4649915777653004,1.0,0.19008983717012912,0.29699606962380687]],["pos",[13,17,1,4,1,5,7,18,19,16,2,14,9,16,8,2,24,8,23,10,5,13,22,14,19,23]],["base",["C","C","T","T","G","G","A","G","T","T","G","G","G","T","T","T","G","A","C","T","A","A","A","T","A","A"]],["n",[6547,6141,1923,2406,295,233,183,496,494,52,45,110,71,2534,1741,1649,36,497,166,3716,74,52,165,669,21,77]],["det_with",["27% of 6547","22% of 6141","0% of 1923","6% of 2406","0% of 295","0% of 233","0% of 183","2% of 496","2% of 494","0% of 52","0% of 45","1% of 110","1% of 71","12% of 2534","10% of 1741","9% of 1649","8% of 36","11% of 497","17% of 166","24% of 3716","23% of 74","33% of 52","50% of 165","61% of 669","76% of 21","81% of 77"]],["det_without",["99% of 83","90% of 489","39% of 4707","40% of 4224","29% of 6335","28% of 6397","28% of 6447","30% of 6134","30% of 6136","28% of 6578","28% of 6585","28% of 6520","28% of 6559","37% of 4096","34% of 4889","33% of 4981","28% of 6594","29% of 6133","28% of 6464","32% of 2914","27% of 6556","27% of 6578","27% of 6465","24% of 5961","27% of 6609","27% of 6553"]],["subs",["C&gt;A 6545, C&gt;G 2","C&gt;T 6137, C&gt;A 4","T&gt;A 1907, T&gt;C 12, T&gt;G 4","T&gt;A 2394, T&gt;C 11, T&gt;G 1","G&gt;T 292, G&gt;A 2, G&gt;C 1","G&gt;A 229, G&gt;T 4","A&gt;T 137, A&gt;C 46","G&gt;C 495, G&gt;T 1","T&gt;G 492, T&gt;A 1, T&gt;C 1","T&gt;A 49, T&gt;C 2, T&gt;G 1","G&gt;A 35, G&gt;T 6, G&gt;C 4","G&gt;A 100, G&gt;T 10","G&gt;C 49, G&gt;A 22","T&gt;A 2526, T&gt;G 6, T&gt;C 2","T&gt;C 1741","T&gt;C 1648, T&gt;A 1","G&gt;A 30, G&gt;T 4, G&gt;C 2","A&gt;C 497","C&gt;A 157, C&gt;G 7, C&gt;T 2","T&gt;A 3362, T&gt;G 354","A&gt;G 73, A&gt;T 1","A&gt;G 51, A&gt;T 1","A&gt;G 163, A&gt;C 2","T&gt;C 668, T&gt;A 1","A&gt;G 18, A&gt;C 3","A&gt;T 44, A&gt;G 23, A&gt;C 10"]],["zone",["no","no","yes","yes","yes","yes","no","no","no","no","yes","no","no","no","no","yes","no","no","no","no","yes","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p27001","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p27002"}}},"glyph":{"type":"object","name":"Rect","id":"p26997","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p26998","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p26999","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p26971","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p26985"},{"type":"object","name":"BoxZoomTool","id":"p26986","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p26987","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p26993","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p26992","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p26994","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p26995"},{"type":"object","name":"SaveTool","id":"p26996"},{"type":"object","name":"HoverTool","id":"p27003","attributes":{"renderers":[{"id":"p27000"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p26980","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p26981"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p26982"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p26983"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p26975","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p27004","attributes":{"ticks":[-24,-23,-22,-19,-18,-17,-16,-14,-13,-10,-9,-8,-7,-5,-4,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p26977"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-13,"13"],[-17,"17"],[-1,"1"],[-4,"4"],[-5,"5"],[-7,"7"],[-18,"18"],[-19,"19"],[-16,"16"],[-2,"2"],[-14,"14"],[-9,"9"],[-8,"8"],[-24,"24"],[-23,"23"],[-10,"10"],[-22,"22"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p26978"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p26979","attributes":{"axis":{"id":"p26975"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p26984","attributes":{"dimension":1,"axis":{"id":"p26980"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b58f269c-9e9f-45db-b0f2-6e14df8adc09","roots":{"p26963":"b6a70b82-59fb-420b-8bec-0c0c72c01f18"},"root_ids":["p26963"]}];
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

<div id="ae4c57c1-6b5c-47fe-abf5-306c86d6d6a4" data-root-id="p27010" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"a689803e-2065-49c3-9c93-18d003e7c441":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p27059","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p27060"}}},"roots":[{"type":"object","name":"Figure","id":"p27010","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p27019","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p27020","attributes":{"factors":["Haemoproteus sp. (191679)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p27021"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p27022"},"title":{"type":"object","name":"Title","id":"p27017","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p27054","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p27007","attributes":{"selected":{"type":"object","name":"Selection","id":"p27008","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p27009"},"data":{"type":"map","entries":[["y",["Haemoproteus sp. (191679)"]],["share",[7.6923076923076925]],["lo",[3.330350149516352]],["hi",[16.77593327011]],["n",[65]],["det",[5]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p27055","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p27056"}}},"glyph":{"type":"object","name":"Scatter","id":"p27051","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p27052","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p27053","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p27018","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p27033"},{"type":"object","name":"BoxZoomTool","id":"p27034","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p27035","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p27041","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p27040","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p27042","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p27043"},{"type":"object","name":"SaveTool","id":"p27044"},{"type":"object","name":"HoverTool","id":"p27058","attributes":{"renderers":[{"id":"p27054"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p27028","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p27029"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p27030"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p27031"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p27023","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p27024","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p27025"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p27026"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p27027","attributes":{"axis":{"id":"p27023"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p27032","attributes":{"dimension":1,"axis":{"id":"p27028"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p27045","attributes":{"source":{"id":"p27007"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p27057","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"a689803e-2065-49c3-9c93-18d003e7c441","roots":{"p27010":"ae4c57c1-6b5c-47fe-abf5-306c86d6d6a4"},"root_ids":["p27010"]}];
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

This entry declares **`scope_taxids`**: [418104](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=418104), [418105](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=418105), [418110](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=418110), [418112](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=418112), [419353](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=419353), [77521](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=77521), [587283](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=587283). A record counts toward the denominator when its taxid, or any ancestor, is in that set. Records outside it are screened and reported but kept out of the statistics.

20,255 screened records fell outside the declared scope.

Retrieval query:

```
cytb[Gene] OR cob[Gene] OR "cytochrome b"[Title] OR cytb[Title] OR "complete genome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `oligos_read_from_figure`, `oligos_from_secondary_source`.


## What reached the statistics

11,796 records were screened for this assay and **1,781 (15%)** were evaluable, meaning both primers landed in the right orientation and size range. 10,015 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 8,993 |
| `truncated` | 1,002 |
| `chance_anchor` | 20 |

