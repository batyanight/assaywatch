# SBV_polyprotein_Rossi_2024

<span class="aw-chip aw-chip-declining">declining</span>

**SACBROOD VIRUS — polyprotein gene RT-qPCR, hydrolysis probe (Rossi 2024)**

| | |
|---|---|
| Target | Iflavirus sacbroodi (sacbrood virus; the paper's name, renamed by ICTV) ([taxid 3048309](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3048309)) |
| Gene | polyprotein gene |
| Chemistry | hydrolysis_probe |
| Amplicon | 122 bp |
| Designed | 2024 |
| Paper | [10.3390/microorganisms12061105](https://doi.org/10.3390/microorganisms12061105) |
| Registry status | active |

!!! quote "The paper"
    Rossi, F.; Del Matto, I.; Ricchiuti, L.; Marino, L. Selection and Multiplexing of Reverse Transcription–Quantitative PCR Tests Targeting Relevant Honeybee Viral Pathogens. Microorganisms 2024, 12, 1105.

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `AAYGTCCACTACACCGAAATGT` | 22 nt |
| reverse | `TAHGAGGTAATAACTTTTCGCCA` | 23 nt |
| probe | `TGATGAGAGTGGACGAAGAATCTGGAATG` | 29 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 32 | 54 | 59.3% | 46.0% – 71.3% |
| baseline (everything earlier) | 282 | 323 | 87.3% | 83.2% – 90.5% |

Change from baseline, Newcombe interval: **-41.7% to -15.3%**. Threshold: **90.0%**.

*detected share 59.3% (46%-71%) since Oct 2024, upper bound below the 90% threshold; change from baseline -42% to -15%*

Trend across deposit years: by record falling (p=0.015, 24 years); by footprint falling (p=0.112). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="b376b345-96b0-4b2c-8299-4c5738437436" data-root-id="p31884" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"a6911329-0c62-4c62-a32b-486c25106a40":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p31939","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p31940"}}},"roots":[{"type":"object","name":"Figure","id":"p31884","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p31886"},"y_range":{"type":"object","name":"Range1d","id":"p31893","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p31894"},"y_scale":{"type":"object","name":"LinearScale","id":"p31895"},"title":{"type":"object","name":"Title","id":"p31891","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p31929","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p31881","attributes":{"selected":{"type":"object","name":"Selection","id":"p31882","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p31883"},"data":{"type":"map","entries":[["year",[1999,2001,2002,2003,2004,2007,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,85.71428571428571,100.0,100.0,100.0,100.0,100.0,0.0,100.0,86.66666666666667,72.72727272727273,84.84848484848484,100.0,100.0,78.57142857142857,60.0,100.0,75.0,95.83333333333334,100.0,76.47058823529412,73.68421052631578,53.125,71.42857142857143]],["detected",[2,12,1,3,1,1,1,0,12,13,8,28,6,4,11,9,17,6,92,14,13,28,17,15]],["evaluable",[2,14,1,3,1,1,1,1,12,15,11,33,6,4,14,15,17,8,96,14,17,38,32,21]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,10.37579022724969,8.703135093227193,9.328625426046248,8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193,10.269703144398052,10.423139468338052,10.209683151927734,10.955310988645032,9.791719296345839,9.517227179437622,10.37579022724969,10.423139468338052,10.508782366508077,9.989711205477885,11.641139586689716,10.37579022724969,10.508782366508077,11.048392086352559,10.934913263353746,10.652487636092928]]]}}},"view":{"type":"object","name":"CDSView","id":"p31930","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31931"}}},"glyph":{"type":"object","name":"Line","id":"p31926","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p31927","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p31928","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p31935","attributes":{"data_source":{"id":"p31881"},"view":{"type":"object","name":"CDSView","id":"p31936","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31937"}}},"glyph":{"type":"object","name":"Scatter","id":"p31932","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p31933","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p31934","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p31892","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p31906"},{"type":"object","name":"BoxZoomTool","id":"p31907","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p31908","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p31914","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31913","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p31915","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p31916"},{"type":"object","name":"SaveTool","id":"p31917"},{"type":"object","name":"HoverTool","id":"p31938","attributes":{"renderers":[{"id":"p31935"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p31901","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31902","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31903"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31904"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p31896","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31897","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31898"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31899"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p31900","attributes":{"axis":{"id":"p31896"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p31905","attributes":{"dimension":1,"axis":{"id":"p31901"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p31918","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p31920","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p31921","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p31922","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p31924","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31923","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p31925","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"a6911329-0c62-4c62-a32b-486c25106a40","roots":{"p31884":"b376b345-96b0-4b2c-8299-4c5738437436"},"root_ids":["p31884"]}];
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

<div id="c11bd626-2aa0-4717-b17c-877a895c961c" data-root-id="p31944" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b591a34c-ebf7-4a00-a350-fd9caa91ac5b":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p31984","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p31985"}}},"roots":[{"type":"object","name":"Figure","id":"p31944","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p31945"},"y_range":{"type":"object","name":"DataRange1d","id":"p31946","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p31953"},"y_scale":{"type":"object","name":"LinearScale","id":"p31954"},"title":{"type":"object","name":"Title","id":"p31951","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p31980","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p31941","attributes":{"selected":{"type":"object","name":"Selection","id":"p31942","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p31943"},"data":{"type":"map","entries":[["year",[1999,2001,2002,2003,2004,2007,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[2,14,1,3,1,1,1,1,12,15,11,33,6,4,14,15,17,8,96,14,17,38,32,21]],["detected",[2,12,1,3,1,1,1,0,12,13,8,28,6,4,11,9,17,6,92,14,13,28,17,15]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p31981","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31982"}}},"glyph":{"type":"object","name":"VBar","id":"p31977","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p31978","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p31979","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p31952","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p31965"},{"type":"object","name":"BoxZoomTool","id":"p31966","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p31967","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p31973","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31972","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p31974","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p31975"},{"type":"object","name":"SaveTool","id":"p31976"},{"type":"object","name":"HoverTool","id":"p31983","attributes":{"renderers":[{"id":"p31980"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p31960","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31961","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31962"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31963"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p31955","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31956","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31957"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31958"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p31959","attributes":{"axis":{"id":"p31955"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p31964","attributes":{"dimension":1,"axis":{"id":"p31960"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b591a34c-ebf7-4a00-a350-fd9caa91ac5b","roots":{"p31944":"c11bd626-2aa0-4717-b17c-877a895c961c"},"root_ids":["p31944"]}];
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

<div id="ed34ae7d-bf76-4949-8150-3b5d2d20e5e1" data-root-id="p31989" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"5653cc7c-84fd-45b7-bd96-1a20ea2eb0ce":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p32031","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p32032"}}},"roots":[{"type":"object","name":"Figure","id":"p31989","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p31991"},"y_range":{"type":"object","name":"FactorRange","id":"p31998","attributes":{"factors":["probe","reverse"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p31999"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p32000"},"title":{"type":"object","name":"Title","id":"p31996","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p32026","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p31986","attributes":{"selected":{"type":"object","name":"Selection","id":"p31987","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p31988"},"data":{"type":"map","entries":[["x",[-15,-16,-12,-23]],["y",["reverse","reverse","reverse","probe"]],["alpha",[0.46564986737400527,0.42055702917771876,0.45663129973474803,0.6550397877984084]],["pos",[15,16,12,23]],["base",["A","T","A","G"]],["n",[35,30,34,56]],["det_with",["0% of 35","0% of 30","6% of 34","29% of 56"]],["det_without",["92% of 342","91% of 347","91% of 343","93% of 321"]],["subs",["A&gt;T 32, A&gt;C 2, A&gt;G 1","T&gt;A 30","A&gt;T 31, A&gt;C 2, A&gt;G 1","G&gt;A 40, G&gt;T 16"]],["zone",["no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p32027","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p32028"}}},"glyph":{"type":"object","name":"Rect","id":"p32023","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p32024","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p32025","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p31997","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p32011"},{"type":"object","name":"BoxZoomTool","id":"p32012","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p32013","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p32019","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p32018","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p32020","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p32021"},{"type":"object","name":"SaveTool","id":"p32022"},{"type":"object","name":"HoverTool","id":"p32029","attributes":{"renderers":[{"id":"p32026"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p32006","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p32007"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p32008"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p32009"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p32001","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p32030","attributes":{"ticks":[-23,-16,-15,-12],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p32003"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-15,"15"],[-16,"16"],[-12,"12"],[-23,"23"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p32004"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p32005","attributes":{"axis":{"id":"p32001"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p32010","attributes":{"dimension":1,"axis":{"id":"p32006"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"5653cc7c-84fd-45b7-bd96-1a20ea2eb0ce","roots":{"p31989":"ed34ae7d-bf76-4949-8150-3b5d2d20e5e1"},"root_ids":["p31989"]}];
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

<div id="eee9f1ca-4068-4ce5-bb75-c28219a71a4a" data-root-id="p32036" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9e0c180f-e256-4809-8c98-2ffc41804556":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p32085","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p32086"}}},"roots":[{"type":"object","name":"Figure","id":"p32036","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p32045","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p32046","attributes":{"factors":["Iflavirus sacbroodi (3048309)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p32047"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p32048"},"title":{"type":"object","name":"Title","id":"p32043","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p32080","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p32033","attributes":{"selected":{"type":"object","name":"Selection","id":"p32034","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p32035"},"data":{"type":"map","entries":[["y",["Iflavirus sacbroodi (3048309)"]],["share",[59.25925925925925]],["lo",[45.966849343490566]],["hi",[71.32178791408542]],["n",[54]],["det",[32]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p32081","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p32082"}}},"glyph":{"type":"object","name":"Scatter","id":"p32077","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p32078","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p32079","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p32044","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p32059"},{"type":"object","name":"BoxZoomTool","id":"p32060","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p32061","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p32067","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p32066","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p32068","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p32069"},{"type":"object","name":"SaveTool","id":"p32070"},{"type":"object","name":"HoverTool","id":"p32084","attributes":{"renderers":[{"id":"p32080"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p32054","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p32055"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p32056"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p32057"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p32049","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p32050","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p32051"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p32052"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p32053","attributes":{"axis":{"id":"p32049"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p32058","attributes":{"dimension":1,"axis":{"id":"p32054"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p32071","attributes":{"source":{"id":"p32033"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p32083","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9e0c180f-e256-4809-8c98-2ffc41804556","roots":{"p32036":"eee9f1ca-4068-4ce5-bb75-c28219a71a4a"},"root_ids":["p32036"]}];
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

Disclosures on this entry: `oligos_from_secondary_source`.


## What reached the statistics

918 records were screened for this assay and **377 (41%)** were evaluable, meaning both primers landed in the right orientation and size range. 541 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 531 |
| `truncated` | 10 |

