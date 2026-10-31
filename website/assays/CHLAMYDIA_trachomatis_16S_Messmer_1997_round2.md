# CHLAMYDIA_trachomatis_16S_Messmer_1997_round2

<span class="aw-chip aw-chip-declining">declining</span>

**CHLAMYDIA TRACHOMATIS — 16S rRNA nested multiplex PCR, second step (Messmer 1997)**

| | |
|---|---|
| Target | Chlamydia trachomatis ([taxid 813](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=813)) |
| Gene | 16S rRNA |
| Chemistry | conventional |
| Amplicon | 413 bp |
| Designed | 1997 |
| Paper | [10.1128/jcm.35.8.2043-2046.1997](https://doi.org/10.1128/jcm.35.8.2043-2046.1997) |
| Registry status | active |

!!! quote "The paper"
    Messmer, T. O., Skelton, S. K., Moroney, J. F., Daugharty, H. & Fields, B. S. Application of a nested, multiplex PCR to psittacosis outbreaks. Journal of Clinical Microbiology 35, 2043-2046 (1997).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GCAATTGTTTCGGCAATTG` | 19 nt |
| reverse | `AGCGGGTATTAACCGCCT` | 18 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 18 | 39 | 46.2% | 31.6% – 61.4% |
| baseline (everything earlier) | 239 | 323 | 74.0% | 68.9% – 78.5% |

Change from baseline, Newcombe interval: **-43.1% to -11.8%**. Threshold: **90.0%**.

*detected share 46.2% (32%-61%) since Oct 2024, upper bound below the 90% threshold; change from baseline -43% to -12%*

Trend across deposit years: by record rising (p=7.26e-08, 20 years); by footprint rising (p=0.169). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="b7756ecb-f433-4203-b926-e3c93617ce90" data-root-id="p8236" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"d907fb02-1227-41a8-8007-cb2652cb5c9a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p8291","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p8292"}}},"roots":[{"type":"object","name":"Figure","id":"p8236","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p8238"},"y_range":{"type":"object","name":"Range1d","id":"p8245","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p8246"},"y_scale":{"type":"object","name":"LinearScale","id":"p8247"},"title":{"type":"object","name":"Title","id":"p8243","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p8281","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p8233","attributes":{"selected":{"type":"object","name":"Selection","id":"p8234","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p8235"},"data":{"type":"map","entries":[["year",[1996,1997,1998,2001,2005,2008,2009,2010,2011,2012,2013,2015,2016,2017,2019,2021,2022,2024,2025,2026]],["share",[0.0,33.33333333333333,0.0,0.0,38.095238095238095,100.0,0.0,33.33333333333333,50.0,59.09090909090909,90.9090909090909,66.66666666666666,77.77777777777779,18.181818181818183,100.0,97.48427672955975,100.0,58.82352941176471,44.44444444444444,100.0]],["detected",[0,2,0,0,8,2,0,3,1,13,20,8,7,6,2,155,2,10,16,2]],["evaluable",[1,6,1,1,21,2,3,9,2,22,22,12,9,33,2,159,2,17,36,2]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,9.791719296345839,8.703135093227193,8.703135093227193,10.652487636092928,9.07684386569143,9.328625426046248,10.071067811865476,9.07684386569143,10.683957047019447,10.683957047019447,10.269703144398052,10.071067811865476,10.955310988645032,9.07684386569143,11.95002790869381,9.07684386569143,10.508782366508077,11.012804945939648,9.07684386569143]]]}}},"view":{"type":"object","name":"CDSView","id":"p8282","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8283"}}},"glyph":{"type":"object","name":"Line","id":"p8278","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p8279","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p8280","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p8287","attributes":{"data_source":{"id":"p8233"},"view":{"type":"object","name":"CDSView","id":"p8288","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8289"}}},"glyph":{"type":"object","name":"Scatter","id":"p8284","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p8285","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p8286","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p8244","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p8258"},{"type":"object","name":"BoxZoomTool","id":"p8259","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p8260","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p8266","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8265","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p8267","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p8268"},{"type":"object","name":"SaveTool","id":"p8269"},{"type":"object","name":"HoverTool","id":"p8290","attributes":{"renderers":[{"id":"p8287"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p8253","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8254","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8255"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8256"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p8248","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8249","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8250"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8251"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p8252","attributes":{"axis":{"id":"p8248"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p8257","attributes":{"dimension":1,"axis":{"id":"p8253"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p8270","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p8272","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p8273","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p8274","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p8276","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8275","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p8277","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"d907fb02-1227-41a8-8007-cb2652cb5c9a","roots":{"p8236":"b7756ecb-f433-4203-b926-e3c93617ce90"},"root_ids":["p8236"]}];
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

<div id="fd01a83d-5876-4f04-8db1-a6936c681034" data-root-id="p8296" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"643b984b-6c0f-4b4c-84cf-b33da0c4ed7a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p8336","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p8337"}}},"roots":[{"type":"object","name":"Figure","id":"p8296","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p8297"},"y_range":{"type":"object","name":"DataRange1d","id":"p8298","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p8305"},"y_scale":{"type":"object","name":"LinearScale","id":"p8306"},"title":{"type":"object","name":"Title","id":"p8303","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p8332","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p8293","attributes":{"selected":{"type":"object","name":"Selection","id":"p8294","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p8295"},"data":{"type":"map","entries":[["year",[1996,1997,1998,2001,2005,2008,2009,2010,2011,2012,2013,2015,2016,2017,2019,2021,2022,2024,2025,2026]],["evaluable",[1,6,1,1,21,2,3,9,2,22,22,12,9,33,2,159,2,17,36,2]],["detected",[0,2,0,0,8,2,0,3,1,13,20,8,7,6,2,155,2,10,16,2]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p8333","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8334"}}},"glyph":{"type":"object","name":"VBar","id":"p8329","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p8330","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p8331","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p8304","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p8317"},{"type":"object","name":"BoxZoomTool","id":"p8318","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p8319","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p8325","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8324","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p8326","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p8327"},{"type":"object","name":"SaveTool","id":"p8328"},{"type":"object","name":"HoverTool","id":"p8335","attributes":{"renderers":[{"id":"p8332"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p8312","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8313","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8314"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8315"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p8307","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8308","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8309"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8310"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p8311","attributes":{"axis":{"id":"p8307"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p8316","attributes":{"dimension":1,"axis":{"id":"p8312"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"643b984b-6c0f-4b4c-84cf-b33da0c4ed7a","roots":{"p8296":"fd01a83d-5876-4f04-8db1-a6936c681034"},"root_ids":["p8296"]}];
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

<div id="f2a88d81-08b6-439b-ba35-ef24fb1c6aba" data-root-id="p8341" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"cb9a4260-8cf2-4e76-a1b6-e3bc180cad53":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p8383","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p8384"}}},"roots":[{"type":"object","name":"Figure","id":"p8341","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p8343"},"y_range":{"type":"object","name":"FactorRange","id":"p8350","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p8351"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p8352"},"title":{"type":"object","name":"Title","id":"p8348","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p8378","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p8338","attributes":{"selected":{"type":"object","name":"Selection","id":"p8339","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p8340"},"data":{"type":"map","entries":[["x",[-5,-7,-3]],["y",["forward","forward","reverse"]],["alpha",[1.0,1.0,1.0]],["pos",[5,7,3]],["base",["A","G","C"]],["n",[110,110,156]],["det_with",["5% of 110","5% of 110","33% of 156"]],["det_without",["100% of 253","100% of 253","100% of 207"]],["subs",["A&gt;G 110","G&gt;A 110","C&gt;T 156"]],["zone",["yes","no","yes"]]]}}},"view":{"type":"object","name":"CDSView","id":"p8379","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8380"}}},"glyph":{"type":"object","name":"Rect","id":"p8375","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p8376","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p8377","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p8349","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p8363"},{"type":"object","name":"BoxZoomTool","id":"p8364","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p8365","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p8371","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8370","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p8372","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p8373"},{"type":"object","name":"SaveTool","id":"p8374"},{"type":"object","name":"HoverTool","id":"p8381","attributes":{"renderers":[{"id":"p8378"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p8358","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p8359"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p8360"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8361"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p8353","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p8382","attributes":{"ticks":[-7,-5,-3],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8355"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-5,"5"],[-7,"7"],[-3,"3"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p8356"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p8357","attributes":{"axis":{"id":"p8353"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p8362","attributes":{"dimension":1,"axis":{"id":"p8358"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"cb9a4260-8cf2-4e76-a1b6-e3bc180cad53","roots":{"p8341":"f2a88d81-08b6-439b-ba35-ef24fb1c6aba"},"root_ids":["p8341"]}];
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

<div id="c8ef3167-3296-4e20-b3cf-0c5db7c4bd98" data-root-id="p8388" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"001cdecd-86b4-4ef3-bf13-1ff547d65098":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p8437","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p8438"}}},"roots":[{"type":"object","name":"Figure","id":"p8388","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p8397","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p8398","attributes":{"factors":["Chlamydia trachomatis (813)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p8399"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p8400"},"title":{"type":"object","name":"Title","id":"p8395","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p8432","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p8385","attributes":{"selected":{"type":"object","name":"Selection","id":"p8386","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p8387"},"data":{"type":"map","entries":[["y",["Chlamydia trachomatis (813)"]],["share",[46.15384615384615]],["lo",[31.566885606727844]],["hi",[61.43055172948425]],["n",[39]],["det",[18]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p8433","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8434"}}},"glyph":{"type":"object","name":"Scatter","id":"p8429","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p8430","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p8431","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p8396","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p8411"},{"type":"object","name":"BoxZoomTool","id":"p8412","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p8413","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p8419","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8418","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p8420","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p8421"},{"type":"object","name":"SaveTool","id":"p8422"},{"type":"object","name":"HoverTool","id":"p8436","attributes":{"renderers":[{"id":"p8432"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p8406","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p8407"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p8408"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8409"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p8401","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8402","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8403"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8404"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p8405","attributes":{"axis":{"id":"p8401"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p8410","attributes":{"dimension":1,"axis":{"id":"p8406"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p8423","attributes":{"source":{"id":"p8385"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p8435","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"001cdecd-86b4-4ef3-bf13-1ff547d65098","roots":{"p8388":"c8ef3167-3296-4e20-b3cf-0c5db7c4bd98"},"root_ids":["p8388"]}];
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
16S[Title] OR "16S ribosomal RNA"[Title] OR "small subunit ribosomal"[Title] OR "complete genome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `primer_site_polymorphic`.


## What reached the statistics

378 records were screened for this assay and **362 (96%)** were evaluable, meaning both primers landed in the right orientation and size range. 16 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 16 |

