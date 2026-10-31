# CHLAMYDIA_genus_16S_Messmer_1997_round1

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**CHLAMYDIA (genus) — 16S rRNA nested multiplex PCR, first step (Messmer 1997)**

| | |
|---|---|
| Target | Chlamydia ([taxid 810](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=810)) |
| Gene | 16S rRNA |
| Chemistry | conventional |
| Amplicon | 437 bp |
| Designed | 1997 |
| Paper | [10.1128/jcm.35.8.2043-2046.1997](https://doi.org/10.1128/jcm.35.8.2043-2046.1997) |
| Registry status | active |

!!! quote "The paper"
    Messmer, T. O., Skelton, S. K., Moroney, J. F., Daugharty, H. & Fields, B. S. Application of a nested, multiplex PCR to psittacosis outbreaks. Journal of Clinical Microbiology 35, 2043-2046 (1997).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ACGGAATAATGACTTCGG` | 18 nt |
| reverse | `TACCTGGTACGCTCAATT` | 18 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 36 | 86 | 41.9% | 32.0% – 52.4% |
| baseline (everything earlier) | 292 | 728 | 40.1% | 36.6% – 43.7% |

Change from baseline, Newcombe interval: **-8.7% to 12.9%**. Threshold: **90.0%**.

*detected share 41.9% (32%-52%) since Oct 2024, upper bound below the 90% threshold; change from baseline -9% to +13% (no measurable fall from a baseline of 40%); separately, lineage Chlamydia trachomatis (813) (39 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift*

Trend across deposit years: by record falling (p=2.62e-10, 32 years); by footprint falling (p=0.036). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="bf2d5315-347c-41ac-947c-fc03ab96398e" data-root-id="p7773" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"7d7817b9-064e-45ef-8722-228f69ee3eef":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7828","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7829"}}},"roots":[{"type":"object","name":"Figure","id":"p7773","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p7775"},"y_range":{"type":"object","name":"Range1d","id":"p7782","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p7783"},"y_scale":{"type":"object","name":"LinearScale","id":"p7784"},"title":{"type":"object","name":"Title","id":"p7780","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7818","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7770","attributes":{"selected":{"type":"object","name":"Selection","id":"p7771","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7772"},"data":{"type":"map","entries":[["year",[1993,1995,1996,1997,1998,1999,2000,2001,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,0.0,85.71428571428571,0.0,100.0,50.0,0.0,100.0,100.0,4.545454545454546,66.66666666666666,50.0,33.33333333333333,16.666666666666664,25.0,76.19047619047619,25.64102564102564,21.052631578947366,0.0,47.16981132075472,0.0,35.08771929824561,18.75,73.07692307692307,93.33333333333333,18.095238095238095,92.5925925925926,100.0,55.00000000000001,40.98360655737705,31.57894736842105]],["detected",[1,2,0,66,0,2,1,0,9,1,1,2,1,1,2,4,16,10,8,0,25,0,20,6,19,14,38,25,1,22,25,6]],["evaluable",[1,2,1,77,1,2,2,1,9,1,22,3,2,3,12,16,21,39,38,8,53,12,57,32,26,15,210,27,1,40,61,19]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,9.07684386569143,8.703135093227193,11.503079740144862,8.703135093227193,9.07684386569143,9.07684386569143,8.703135093227193,10.071067811865476,8.703135093227193,10.683957047019447,9.328625426046248,9.07684386569143,9.328625426046248,10.269703144398052,10.467343773689333,10.652487636092928,11.06545099688784,11.048392086352559,9.989711205477885,11.264976950698303,10.269703144398052,11.311780786273989,10.934913263353746,10.796415465069488,10.423139468338052,12.11630744229495,10.821697436206254,8.703135093227193,11.082053972722118,11.355225445040746,10.584573151575475]]]}}},"view":{"type":"object","name":"CDSView","id":"p7819","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7820"}}},"glyph":{"type":"object","name":"Line","id":"p7815","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p7816","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p7817","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p7824","attributes":{"data_source":{"id":"p7770"},"view":{"type":"object","name":"CDSView","id":"p7825","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7826"}}},"glyph":{"type":"object","name":"Scatter","id":"p7821","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p7822","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p7823","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7781","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7795"},{"type":"object","name":"BoxZoomTool","id":"p7796","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7797","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7803","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7802","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7804","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7805"},{"type":"object","name":"SaveTool","id":"p7806"},{"type":"object","name":"HoverTool","id":"p7827","attributes":{"renderers":[{"id":"p7824"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p7790","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7791","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7792"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7793"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7785","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7786","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7787"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7788"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7789","attributes":{"axis":{"id":"p7785"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7794","attributes":{"dimension":1,"axis":{"id":"p7790"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p7807","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p7809","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p7810","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p7811","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p7813","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7812","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p7814","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"7d7817b9-064e-45ef-8722-228f69ee3eef","roots":{"p7773":"bf2d5315-347c-41ac-947c-fc03ab96398e"},"root_ids":["p7773"]}];
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

<div id="d8cb2924-017d-4803-86f6-b112a823beb5" data-root-id="p7833" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"f5e47fc1-8ded-4e9f-bd56-1d61fdde6c86":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7873","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7874"}}},"roots":[{"type":"object","name":"Figure","id":"p7833","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p7834"},"y_range":{"type":"object","name":"DataRange1d","id":"p7835","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p7842"},"y_scale":{"type":"object","name":"LinearScale","id":"p7843"},"title":{"type":"object","name":"Title","id":"p7840","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7869","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7830","attributes":{"selected":{"type":"object","name":"Selection","id":"p7831","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7832"},"data":{"type":"map","entries":[["year",[1993,1995,1996,1997,1998,1999,2000,2001,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,2,1,77,1,2,2,1,9,1,22,3,2,3,12,16,21,39,38,8,53,12,57,32,26,15,210,27,1,40,61,19]],["detected",[1,2,0,66,0,2,1,0,9,1,1,2,1,1,2,4,16,10,8,0,25,0,20,6,19,14,38,25,1,22,25,6]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p7870","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7871"}}},"glyph":{"type":"object","name":"VBar","id":"p7866","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p7867","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p7868","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7841","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7854"},{"type":"object","name":"BoxZoomTool","id":"p7855","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7856","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7862","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7861","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7863","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7864"},{"type":"object","name":"SaveTool","id":"p7865"},{"type":"object","name":"HoverTool","id":"p7872","attributes":{"renderers":[{"id":"p7869"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p7849","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7850","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7851"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7852"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7844","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7845","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7846"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7847"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7848","attributes":{"axis":{"id":"p7844"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7853","attributes":{"dimension":1,"axis":{"id":"p7849"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"f5e47fc1-8ded-4e9f-bd56-1d61fdde6c86","roots":{"p7833":"d8cb2924-017d-4803-86f6-b112a823beb5"},"root_ids":["p7833"]}];
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

<div id="bcde10f3-4d7d-4d74-b456-7148525d2826" data-root-id="p7878" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"464c7e3e-d4ca-4682-8eec-7eeb7058a7ff":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7920","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7921"}}},"roots":[{"type":"object","name":"Figure","id":"p7878","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p7880"},"y_range":{"type":"object","name":"FactorRange","id":"p7887","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p7888"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p7889"},"title":{"type":"object","name":"Title","id":"p7885","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7915","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7875","attributes":{"selected":{"type":"object","name":"Selection","id":"p7876","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7877"},"data":{"type":"map","entries":[["x",[-8,-12,-7,-6,-13,-1,-9,-11,-17,-2]],["y",["forward","forward","forward","forward","forward","forward","forward","forward","forward","reverse"]],["alpha",[1.0,1.0,1.0,1.0,1.0,0.6637592137592138,0.2585995085995086,0.2418918918918919,0.23353808353808353,1.0]],["pos",[8,12,7,6,13,1,9,11,17,2]],["base",["G","T","A","C","A","G","T","A","C","T"]],["n",[465,468,481,380,367,123,26,22,20,794]],["det_with",["1% of 465","4% of 468","8% of 481","0% of 380","0% of 367","0% of 123","0% of 26","0% of 22","5% of 20","41% of 794"]],["det_without",["98% of 329","94% of 326","93% of 313","79% of 414","77% of 427","49% of 671","43% of 768","42% of 772","42% of 774","0% of 0"]],["subs",["G&gt;T 420, G&gt;A 26, G&gt;C 19","T&gt;C 449, T&gt;A 19","A&gt;G 469, A&gt;C 12","C&gt;T 379, C&gt;A 1","A&gt;G 367","G&gt;A 110, G&gt;T 11, G&gt;C 2","T&gt;A 19, T&gt;C 7","A&gt;T 19, A&gt;G 3","C&gt;A 19, C&gt;T 1","T&gt;A 793, T&gt;G 1"]],["zone",["no","no","no","no","no","yes","no","no","no","yes"]]]}}},"view":{"type":"object","name":"CDSView","id":"p7916","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7917"}}},"glyph":{"type":"object","name":"Rect","id":"p7912","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p7913","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p7914","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7886","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7900"},{"type":"object","name":"BoxZoomTool","id":"p7901","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7902","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7908","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7907","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7909","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7910"},{"type":"object","name":"SaveTool","id":"p7911"},{"type":"object","name":"HoverTool","id":"p7918","attributes":{"renderers":[{"id":"p7915"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p7895","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p7896"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p7897"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7898"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7890","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p7919","attributes":{"ticks":[-17,-13,-12,-11,-9,-8,-7,-6,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7892"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-8,"8"],[-12,"12"],[-7,"7"],[-6,"6"],[-13,"13"],[-1,"1"],[-9,"9"],[-11,"11"],[-17,"17"],[-2,"2"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p7893"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7894","attributes":{"axis":{"id":"p7890"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7899","attributes":{"dimension":1,"axis":{"id":"p7895"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"464c7e3e-d4ca-4682-8eec-7eeb7058a7ff","roots":{"p7878":"bcde10f3-4d7d-4d74-b456-7148525d2826"},"root_ids":["p7878"]}];
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

<div id="d27824a2-b2ea-43c1-afac-3dae9b9256df" data-root-id="p7925" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"566073e1-070f-4543-b71a-f005fac4dc42":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7974","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7975"}}},"roots":[{"type":"object","name":"Figure","id":"p7925","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p7934","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p7935","attributes":{"factors":["Chlamydia trachomatis (813)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p7936"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p7937"},"title":{"type":"object","name":"Title","id":"p7932","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7969","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7922","attributes":{"selected":{"type":"object","name":"Selection","id":"p7923","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7924"},"data":{"type":"map","entries":[["y",["Chlamydia trachomatis (813)"]],["share",[0.0]],["lo",[0.0]],["hi",[8.966685370757142]],["n",[39]],["det",[0]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p7970","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7971"}}},"glyph":{"type":"object","name":"Scatter","id":"p7966","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p7967","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p7968","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7933","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7948"},{"type":"object","name":"BoxZoomTool","id":"p7949","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7950","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7956","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7955","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7957","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7958"},{"type":"object","name":"SaveTool","id":"p7959"},{"type":"object","name":"HoverTool","id":"p7973","attributes":{"renderers":[{"id":"p7969"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p7943","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p7944"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p7945"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7946"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7938","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7939","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7940"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7941"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7942","attributes":{"axis":{"id":"p7938"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7947","attributes":{"dimension":1,"axis":{"id":"p7943"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p7960","attributes":{"source":{"id":"p7922"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p7972","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"566073e1-070f-4543-b71a-f005fac4dc42","roots":{"p7925":"d27824a2-b2ea-43c1-afac-3dae9b9256df"},"root_ids":["p7925"]}];
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

Disclosures on this entry: `primer_site_polymorphic`, `scope_narrower_than_taxid`.


## What reached the statistics

1,667 records were screened for this assay and **814 (49%)** were evaluable, meaning both primers landed in the right orientation and size range. 853 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `truncated` | 432 |
| `no_site` | 402 |
| `chance_anchor` | 13 |
| `chance_only` | 6 |

