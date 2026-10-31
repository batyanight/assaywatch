# BQCV_capsid_Rossi_2024

<span class="aw-chip aw-chip-declining">declining</span>

**BLACK QUEEN CELL VIRUS — capsid gene RT-qPCR, MGB probe (Rossi 2024)**

| | |
|---|---|
| Target | Triatovirus nigereginacellulae (black queen cell virus; the paper's name, renamed by ICTV) ([taxid 3047684](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3047684)) |
| Gene | capsid protein gene |
| Chemistry | mgb |
| Amplicon | 69 bp |
| Designed | 2024 |
| Paper | [10.3390/microorganisms12061105](https://doi.org/10.3390/microorganisms12061105) |
| Registry status | active |

!!! quote "The paper"
    Rossi, F.; Del Matto, I.; Ricchiuti, L.; Marino, L. Selection and Multiplexing of Reverse Transcription–Quantitative PCR Tests Targeting Relevant Honeybee Viral Pathogens. Microorganisms 2024, 12, 1105.

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GTGCGGGAGATGATATGGA` | 19 nt |
| reverse | `CCGTCTGAGATGCATGAATAC` | 21 nt |
| probe | `TTTCCATCTTTATCGGTACGC` | 21 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 119 | 172 | 69.2% | 61.9% – 75.6% |
| baseline (everything earlier) | 882 | 1,057 | 83.4% | 81.1% – 85.6% |

Change from baseline, Newcombe interval: **-21.8% to -7.4%**. Threshold: **90.0%**.

*detected share 69.2% (62%-76%) since Oct 2024, upper bound below the 90% threshold; change from baseline -22% to -7%*

Trend across deposit years: by record falling (p=0.0412, 25 years); by footprint falling (p=0.000201). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="b85f4ecd-4cfd-4ee5-afff-7d51b45b4a58" data-root-id="p5574" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"fa49f70c-6f5e-442e-acef-86d86d9d3545":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p5629","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p5630"}}},"roots":[{"type":"object","name":"Figure","id":"p5574","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p5576"},"y_range":{"type":"object","name":"Range1d","id":"p5583","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p5584"},"y_scale":{"type":"object","name":"LinearScale","id":"p5585"},"title":{"type":"object","name":"Title","id":"p5581","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p5619","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p5571","attributes":{"selected":{"type":"object","name":"Selection","id":"p5572","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p5573"},"data":{"type":"map","entries":[["year",[2000,2002,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,83.33333333333334,100.0,87.5,59.74025974025974,98.0392156862745,100.0,100.0,81.63265306122449,97.36842105263158,63.888888888888886,85.55555555555556,95.1048951048951,70.88607594936708,92.36641221374046,55.81395348837209,88.46153846153845,78.46153846153847,57.49999999999999,64.81481481481481]],["detected",[2,1,1,1,1,1,5,4,7,46,50,6,19,80,37,23,77,136,56,121,24,92,153,23,35]],["evaluable",[2,1,1,1,1,1,6,4,8,77,51,6,19,98,38,36,90,143,79,131,43,104,195,40,54]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193,9.791719296345839,9.517227179437622,9.989711205477885,11.503079740144862,11.24015070195139,9.791719296345839,10.584573151575475,11.653951690698229,11.048392086352559,11.012804945939648,11.600932205756964,11.88589119348089,11.51922823234585,11.832573140379097,11.129349107533436,11.690784341861697,12.072287571715961,11.082053972722118,11.27702043233893]]]}}},"view":{"type":"object","name":"CDSView","id":"p5620","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p5621"}}},"glyph":{"type":"object","name":"Line","id":"p5616","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p5617","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p5618","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p5625","attributes":{"data_source":{"id":"p5571"},"view":{"type":"object","name":"CDSView","id":"p5626","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p5627"}}},"glyph":{"type":"object","name":"Scatter","id":"p5622","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p5623","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p5624","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p5582","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p5596"},{"type":"object","name":"BoxZoomTool","id":"p5597","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p5598","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p5604","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p5603","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p5605","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p5606"},{"type":"object","name":"SaveTool","id":"p5607"},{"type":"object","name":"HoverTool","id":"p5628","attributes":{"renderers":[{"id":"p5625"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p5591","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p5592","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5593"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5594"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p5586","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p5587","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5588"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5589"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p5590","attributes":{"axis":{"id":"p5586"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p5595","attributes":{"dimension":1,"axis":{"id":"p5591"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p5608","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p5610","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p5611","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p5612","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p5614","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p5613","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p5615","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"fa49f70c-6f5e-442e-acef-86d86d9d3545","roots":{"p5574":"b85f4ecd-4cfd-4ee5-afff-7d51b45b4a58"},"root_ids":["p5574"]}];
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

<div id="a6622160-4a2a-4653-8b91-48a87d3361e4" data-root-id="p5634" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"014a49e3-ffdc-49a0-9d5c-e1a5830a4da7":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p5674","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p5675"}}},"roots":[{"type":"object","name":"Figure","id":"p5634","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p5635"},"y_range":{"type":"object","name":"DataRange1d","id":"p5636","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p5643"},"y_scale":{"type":"object","name":"LinearScale","id":"p5644"},"title":{"type":"object","name":"Title","id":"p5641","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p5670","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p5631","attributes":{"selected":{"type":"object","name":"Selection","id":"p5632","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p5633"},"data":{"type":"map","entries":[["year",[2000,2002,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[2,1,1,1,1,1,6,4,8,77,51,6,19,98,38,36,90,143,79,131,43,104,195,40,54]],["detected",[2,1,1,1,1,1,5,4,7,46,50,6,19,80,37,23,77,136,56,121,24,92,153,23,35]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p5671","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p5672"}}},"glyph":{"type":"object","name":"VBar","id":"p5667","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p5668","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p5669","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p5642","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p5655"},{"type":"object","name":"BoxZoomTool","id":"p5656","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p5657","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p5663","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p5662","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p5664","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p5665"},{"type":"object","name":"SaveTool","id":"p5666"},{"type":"object","name":"HoverTool","id":"p5673","attributes":{"renderers":[{"id":"p5670"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p5650","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p5651","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5652"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5653"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p5645","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p5646","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5647"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5648"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p5649","attributes":{"axis":{"id":"p5645"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p5654","attributes":{"dimension":1,"axis":{"id":"p5650"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"014a49e3-ffdc-49a0-9d5c-e1a5830a4da7","roots":{"p5634":"a6622160-4a2a-4653-8b91-48a87d3361e4"},"root_ids":["p5634"]}];
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

<div id="f8969fdc-9235-4655-9507-86908f271338" data-root-id="p5679" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"27312509-d01e-43c4-a9a7-f59853544323":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p5721","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p5722"}}},"roots":[{"type":"object","name":"Figure","id":"p5679","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p5681"},"y_range":{"type":"object","name":"FactorRange","id":"p5688","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p5689"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p5690"},"title":{"type":"object","name":"Title","id":"p5686","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p5716","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p5676","attributes":{"selected":{"type":"object","name":"Selection","id":"p5677","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p5678"},"data":{"type":"map","entries":[["x",[-2,-8,-5,-2,-3,-14,-12,-13,-8,-17,-20,-6,-11,-18,-15]],["y",["reverse","probe","reverse","probe","reverse","reverse","forward","reverse","reverse","reverse","reverse","forward","reverse","forward","forward"]],["alpha",[0.4460130187144019,0.2855573637103336,0.26065907241659886,0.2578925956061839,0.2274613506916192,0.26065907241659886,0.2661920260374288,0.2827908868999186,0.2966232709519935,0.6811635475996746,0.33812042310821805,0.23852725793327906,0.38515052888527257,0.5234743694060211,0.23852725793327906]],["pos",[2,8,5,2,3,14,12,13,8,17,20,6,11,18,15]],["base",["A","C","A","G","T","A","A","G","A","C","C","T","T","T","G"]],["n",[107,49,40,39,28,40,42,48,53,192,68,32,85,135,32]],["det_with",["0% of 107","0% of 49","0% of 40","0% of 39","0% of 28","2% of 40","5% of 42","8% of 48","26% of 53","35% of 192","29% of 68","31% of 32","34% of 85","41% of 135","62% of 32"]],["det_without",["89% of 1121","85% of 1179","84% of 1188","84% of 1189","84% of 1200","84% of 1188","84% of 1186","85% of 1180","84% of 1175","90% of 1036","85% of 1160","83% of 1196","85% of 1143","87% of 1093","82% of 1196"]],["subs",["A&gt;G 107","C&gt;T 47, C&gt;G 2","A&gt;G 40","G&gt;A 31, G&gt;C 8","T&gt;C 28","A&gt;G 31, A&gt;T 9","A&gt;T 28, A&gt;C 11, A&gt;G 3","G&gt;A 46, G&gt;T 2","A&gt;G 53","C&gt;T 181, C&gt;G 11","C&gt;T 31, C&gt;A 31, C&gt;G 6","T&gt;C 32","T&gt;C 79, T&gt;A 6","T&gt;C 87, T&gt;A 47, T&gt;G 1","G&gt;A 30, G&gt;C 1, G&gt;T 1"]],["zone",["yes","no","yes","yes","yes","no","no","no","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p5717","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p5718"}}},"glyph":{"type":"object","name":"Rect","id":"p5713","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p5714","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p5715","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p5687","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p5701"},{"type":"object","name":"BoxZoomTool","id":"p5702","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p5703","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p5709","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p5708","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p5710","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p5711"},{"type":"object","name":"SaveTool","id":"p5712"},{"type":"object","name":"HoverTool","id":"p5719","attributes":{"renderers":[{"id":"p5716"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p5696","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p5697"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p5698"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5699"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p5691","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p5720","attributes":{"ticks":[-20,-18,-17,-15,-14,-13,-12,-11,-8,-6,-5,-3,-2],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5693"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-2,"2"],[-8,"8"],[-5,"5"],[-3,"3"],[-14,"14"],[-12,"12"],[-13,"13"],[-17,"17"],[-20,"20"],[-6,"6"],[-11,"11"],[-18,"18"],[-15,"15"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p5694"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p5695","attributes":{"axis":{"id":"p5691"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p5700","attributes":{"dimension":1,"axis":{"id":"p5696"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"27312509-d01e-43c4-a9a7-f59853544323","roots":{"p5679":"f8969fdc-9235-4655-9507-86908f271338"},"root_ids":["p5679"]}];
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

<div id="de165b8f-c048-426b-a4fc-4a766cc1e27a" data-root-id="p5726" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"2399a617-1a78-4f3d-981a-675cd24d074f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p5775","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p5776"}}},"roots":[{"type":"object","name":"Figure","id":"p5726","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p5735","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p5736","attributes":{"factors":["Triatovirus nigereginacellulae (3047684)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p5737"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p5738"},"title":{"type":"object","name":"Title","id":"p5733","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p5770","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p5723","attributes":{"selected":{"type":"object","name":"Selection","id":"p5724","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p5725"},"data":{"type":"map","entries":[["y",["Triatovirus nigereginacellulae (3047684)"]],["share",[69.18604651162791]],["lo",[61.92955270525795]],["hi",[75.60425783216505]],["n",[172]],["det",[119]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p5771","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p5772"}}},"glyph":{"type":"object","name":"Scatter","id":"p5767","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p5768","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p5769","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p5734","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p5749"},{"type":"object","name":"BoxZoomTool","id":"p5750","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p5751","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p5757","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p5756","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p5758","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p5759"},{"type":"object","name":"SaveTool","id":"p5760"},{"type":"object","name":"HoverTool","id":"p5774","attributes":{"renderers":[{"id":"p5770"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p5744","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p5745"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p5746"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5747"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p5739","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p5740","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5741"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5742"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p5743","attributes":{"axis":{"id":"p5739"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p5748","attributes":{"dimension":1,"axis":{"id":"p5744"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p5761","attributes":{"source":{"id":"p5723"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p5773","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"2399a617-1a78-4f3d-981a-675cd24d074f","roots":{"p5726":"de165b8f-c048-426b-a4fc-4a766cc1e27a"},"root_ids":["p5726"]}];
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

1,615 records were screened for this assay and **1,229 (76%)** were evaluable, meaning both primers landed in the right orientation and size range. 386 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 344 |
| `chance_anchor` | 29 |
| `truncated` | 10 |

