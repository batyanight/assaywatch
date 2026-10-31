# CDV_P_gene_Scagliarini_2007

<span class="aw-chip aw-chip-declining">declining</span>

**Canine distemper virus — P gene real-time RT-PCR CDVF4/CDVR3 (Scagliarini 2007)**

| | |
|---|---|
| Target | Morbillivirus canis (formerly Canine morbillivirus) ([taxid 3052342](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3052342)) |
| Gene | P |
| Chemistry | mgb |
| Amplicon | 114 bp |
| Designed | 2007 |
| Paper | [10.1007/s11259-007-0020-9](https://doi.org/10.1007/s11259-007-0020-9) |
| Registry status | active |

!!! quote "The paper"
    Scagliarini A et al. 2007. Vet Res Commun 31(Suppl 1):261-263

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GTCGGTAATCGAGGATTCGAGAG` | 23 nt |
| reverse | `GCCGAAAGAATATCCCCAGTTAG` | 23 nt |
| probe | `ATCTTCGCCAGAATCCTCAGTGCT` | 24 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 75 | 93 | 80.6% | 71.5% – 87.4% |
| baseline (everything earlier) | 378 | 509 | 74.3% | 70.3% – 77.9% |

Change from baseline, Newcombe interval: **-3.5% to 14.2%**. Threshold: **90.0%**.

*pooled share 80.6% has low coverage, but lineage Morbillivirus canis (3052342) (93 records) detects 80.6% (71.5%-87.4%); lineage verdict overrides to declining*

Trend across deposit years: by record rising (p=0.796, 33 years); by footprint falling (p=0.022); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="d0f0dc0c-9c55-4988-8e03-e99f3f1b53ba" data-root-id="p7567" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"35b06bae-4969-4063-9895-864c55036b7e":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7622","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7623"}}},"roots":[{"type":"object","name":"Figure","id":"p7567","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p7569"},"y_range":{"type":"object","name":"Range1d","id":"p7576","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p7577"},"y_scale":{"type":"object","name":"LinearScale","id":"p7578"},"title":{"type":"object","name":"Title","id":"p7574","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7612","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7564","attributes":{"selected":{"type":"object","name":"Selection","id":"p7565","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7566"},"data":{"type":"map","entries":[["year",[1990,1993,1995,1996,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,50.0,100.0,71.42857142857143,85.71428571428571,100.0,100.0,86.20689655172413,100.0,85.71428571428571,62.5,50.0,93.75,86.20689655172413,50.0,80.0,65.71428571428571,68.18181818181817,25.0,61.904761904761905,92.5925925925926,90.9090909090909,58.333333333333336,96.66666666666667,68.0,44.44444444444444,93.02325581395348,50.0,82.35294117647058,80.0,80.26315789473685]],["detected",[1,1,1,1,2,5,6,2,3,25,2,24,5,11,15,25,11,8,23,15,4,13,25,10,14,29,34,4,40,7,14,12,61]],["evaluable",[1,1,1,2,2,7,7,2,3,29,2,28,8,22,16,29,22,10,35,22,16,21,27,11,24,30,50,9,43,14,17,15,76]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,8.703135093227193,9.07684386569143,9.07684386569143,9.897626379762722,9.897626379762722,9.07684386569143,9.328625426046248,10.869436534339137,9.07684386569143,10.846014908695619,9.989711205477885,10.683957047019447,10.467343773689333,10.869436534339137,10.683957047019447,10.143865699252444,10.994220569835573,10.683957047019447,10.467343773689333,10.652487636092928,10.821697436206254,10.209683151927734,10.74264168206181,10.892023970177537,11.22734795681138,10.071067811865476,11.129349107533436,10.37579022724969,10.508782366508077,10.423139468338052,11.49483773413666]]]}}},"view":{"type":"object","name":"CDSView","id":"p7613","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7614"}}},"glyph":{"type":"object","name":"Line","id":"p7609","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p7610","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p7611","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p7618","attributes":{"data_source":{"id":"p7564"},"view":{"type":"object","name":"CDSView","id":"p7619","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7620"}}},"glyph":{"type":"object","name":"Scatter","id":"p7615","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p7616","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p7617","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7575","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7589"},{"type":"object","name":"BoxZoomTool","id":"p7590","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7591","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7597","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7596","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7598","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7599"},{"type":"object","name":"SaveTool","id":"p7600"},{"type":"object","name":"HoverTool","id":"p7621","attributes":{"renderers":[{"id":"p7618"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p7584","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7585","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7586"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7587"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7579","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7580","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7581"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7582"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7583","attributes":{"axis":{"id":"p7579"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7588","attributes":{"dimension":1,"axis":{"id":"p7584"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p7601","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p7603","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p7604","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p7605","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p7607","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7606","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p7608","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"35b06bae-4969-4063-9895-864c55036b7e","roots":{"p7567":"d0f0dc0c-9c55-4988-8e03-e99f3f1b53ba"},"root_ids":["p7567"]}];
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

<div id="c6c7da27-866a-4901-9d1f-15a3fa3fef14" data-root-id="p7627" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"1268fc39-957f-40e8-8732-087d008e552a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7667","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7668"}}},"roots":[{"type":"object","name":"Figure","id":"p7627","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p7628"},"y_range":{"type":"object","name":"DataRange1d","id":"p7629","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p7636"},"y_scale":{"type":"object","name":"LinearScale","id":"p7637"},"title":{"type":"object","name":"Title","id":"p7634","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7663","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7624","attributes":{"selected":{"type":"object","name":"Selection","id":"p7625","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7626"},"data":{"type":"map","entries":[["year",[1990,1993,1995,1996,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,1,2,2,7,7,2,3,29,2,28,8,22,16,29,22,10,35,22,16,21,27,11,24,30,50,9,43,14,17,15,76]],["detected",[1,1,1,1,2,5,6,2,3,25,2,24,5,11,15,25,11,8,23,15,4,13,25,10,14,29,34,4,40,7,14,12,61]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p7664","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7665"}}},"glyph":{"type":"object","name":"VBar","id":"p7660","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p7661","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p7662","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7635","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7648"},{"type":"object","name":"BoxZoomTool","id":"p7649","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7650","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7656","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7655","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7657","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7658"},{"type":"object","name":"SaveTool","id":"p7659"},{"type":"object","name":"HoverTool","id":"p7666","attributes":{"renderers":[{"id":"p7663"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p7643","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7644","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7645"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7646"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7638","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7639","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7640"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7641"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7642","attributes":{"axis":{"id":"p7638"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7647","attributes":{"dimension":1,"axis":{"id":"p7643"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"1268fc39-957f-40e8-8732-087d008e552a","roots":{"p7627":"c6c7da27-866a-4901-9d1f-15a3fa3fef14"},"root_ids":["p7627"]}];
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

<div id="cac1f6d0-aabb-491e-ab0f-750cb8458f57" data-root-id="p7672" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"77a3636f-f99d-45a6-8120-ebbb510e695e":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7714","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7715"}}},"roots":[{"type":"object","name":"Figure","id":"p7672","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p7674"},"y_range":{"type":"object","name":"FactorRange","id":"p7681","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p7682"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p7683"},"title":{"type":"object","name":"Title","id":"p7679","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7709","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7669","attributes":{"selected":{"type":"object","name":"Selection","id":"p7670","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7671"},"data":{"type":"map","entries":[["x",[-2,-9,-16,-1,-16,-23,-8,-19,-20,-20,-17,-23]],["y",["forward","probe","forward","forward","probe","forward","forward","forward","forward","reverse","forward","reverse"]],["alpha",[0.5735880398671096,0.3533222591362126,0.3194352159468439,0.3137873754152824,0.2629568106312292,0.3646179401993355,0.3985049833887043,0.3759136212624585,1.0,0.3985049833887043,0.3137873754152824,0.517109634551495]],["pos",[2,9,16,1,16,23,8,19,20,20,17,23]],["base",["A","C","A","G","C","G","T","G","G","G","A","G"]],["n",[75,36,30,29,20,38,44,40,499,44,29,65]],["det_with",["0% of 75","0% of 36","0% of 30","0% of 29","0% of 20","11% of 38","20% of 44","32% of 40","72% of 499","66% of 44","90% of 29","94% of 65"]],["det_without",["86% of 529","80% of 568","80% of 574","79% of 575","78% of 584","80% of 566","80% of 560","79% of 564","92% of 105","76% of 560","75% of 575","73% of 539"]],["subs",["A&gt;G 75","C&gt;T 36","A&gt;G 30","G&gt;A 27, G&gt;C 2","C&gt;T 20","G&gt;A 38","T&gt;C 43, T&gt;G 1","G&gt;A 40","G&gt;A 499","G&gt;A 43, G&gt;T 1","A&gt;G 29","G&gt;A 65"]],["zone",["yes","no","no","yes","no","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p7710","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7711"}}},"glyph":{"type":"object","name":"Rect","id":"p7706","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p7707","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p7708","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7680","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7694"},{"type":"object","name":"BoxZoomTool","id":"p7695","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7696","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7702","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7701","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7703","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7704"},{"type":"object","name":"SaveTool","id":"p7705"},{"type":"object","name":"HoverTool","id":"p7712","attributes":{"renderers":[{"id":"p7709"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p7689","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p7690"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p7691"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7692"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7684","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p7713","attributes":{"ticks":[-23,-20,-19,-17,-16,-9,-8,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7686"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-2,"2"],[-9,"9"],[-16,"16"],[-1,"1"],[-23,"23"],[-8,"8"],[-19,"19"],[-20,"20"],[-17,"17"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p7687"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7688","attributes":{"axis":{"id":"p7684"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7693","attributes":{"dimension":1,"axis":{"id":"p7689"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"77a3636f-f99d-45a6-8120-ebbb510e695e","roots":{"p7672":"cac1f6d0-aabb-491e-ab0f-750cb8458f57"},"root_ids":["p7672"]}];
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

<div id="dae69df9-50a6-4961-8538-9e8c1aa162e4" data-root-id="p7719" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"8e741ee2-1ec1-4e85-8775-9368139f254d":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7768","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7769"}}},"roots":[{"type":"object","name":"Figure","id":"p7719","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p7728","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p7729","attributes":{"factors":["Morbillivirus canis (3052342)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p7730"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p7731"},"title":{"type":"object","name":"Title","id":"p7726","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7763","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7716","attributes":{"selected":{"type":"object","name":"Selection","id":"p7717","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7718"},"data":{"type":"map","entries":[["y",["Morbillivirus canis (3052342)"]],["share",[80.64516129032258]],["lo",[71.46752808856701]],["hi",[87.39156046103633]],["n",[93]],["det",[75]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p7764","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7765"}}},"glyph":{"type":"object","name":"Scatter","id":"p7760","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p7761","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p7762","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7727","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7742"},{"type":"object","name":"BoxZoomTool","id":"p7743","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7744","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7750","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7749","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7751","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7752"},{"type":"object","name":"SaveTool","id":"p7753"},{"type":"object","name":"HoverTool","id":"p7767","attributes":{"renderers":[{"id":"p7763"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p7737","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p7738"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p7739"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7740"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7732","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7733","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7734"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7735"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7736","attributes":{"axis":{"id":"p7732"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7741","attributes":{"dimension":1,"axis":{"id":"p7737"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p7754","attributes":{"source":{"id":"p7716"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p7766","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"8e741ee2-1ec1-4e85-8775-9368139f254d","roots":{"p7719":"dae69df9-50a6-4961-8538-9e8c1aa162e4"},"root_ids":["p7719"]}];
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

This entry declares **`scope_taxids`**: [3052342](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3052342). A record counts toward the denominator when its taxid, or any ancestor, is in that set. Records outside it are screened and reported but kept out of the statistics.


## What reached the statistics

3,952 records were screened for this assay and **602 (15%)** were evaluable, meaning both primers landed in the right orientation and size range. 3,350 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 3,343 |
| `truncated` | 7 |

