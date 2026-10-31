# MONKEYPOX_dsDNA_B1_SNP_nonB1_MGB_Huo_2022

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**MONKEYPOX virus (dsDNA) — Panel 2 non-B.1 clades MGB probe (Huo 2022)**

| | |
|---|---|
| Target | Monkeypox virus ([taxid 10244](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10244)) |
| Gene | SNP-typing locus at 183524-183539 of ON563414.2 |
| Chemistry | mgb |
| Amplicon | 81 bp |
| Designed | 2022 |
| Paper | [10.1016/j.bsheal.2022.10.005](https://doi.org/10.1016/j.bsheal.2022.10.005) |
| Registry status | draft |

!!! quote "The paper"
    Huo S, Chen Y, Lu R, Zhang Z, Zhang G, Zhao L, Deng Y, Wu C, Tan W. 2022. Development of two multiplex real-time PCR assays for simultaneous detection and differentiation of monkeypox virus IIa, IIb, and I clades and the B.1 lineage. Biosaf Health 4:392-398

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `AGTACACAGACCTCCACCAC` | 20 nt |
| reverse | `AGTAATTGACCTACTGGTCTAGGG` | 24 nt |
| probe | `AGTCCAAAATCCGCCA` | 16 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 437 | 4,838 | 9.0% | 8.3% – 9.9% |
| baseline (everything earlier) | 253 | 8,368 | 3.0% | 2.7% – 3.4% |

Change from baseline, Newcombe interval: **5.1% to 6.9%**. Threshold: **90.0%**.

*detected share 9.0% (8%-10%) since Oct 2024, upper bound below the 90% threshold; change from baseline +5% to +7% (rose from a baseline of 3%); separately, lineage Orthopoxvirus monkeypox (3431483) (4793 records) detects only 9.1% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift*

Trend across deposit years: by record rising (p=0.000112, 16 years); by footprint falling (p=0.292); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="efb67135-2522-465f-9a0e-a5705772580d" data-root-id="p16725" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"d4fac347-d880-4890-9ebc-6d137ed2c84a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p16780","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p16781"}}},"roots":[{"type":"object","name":"Figure","id":"p16725","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p16727"},"y_range":{"type":"object","name":"Range1d","id":"p16734","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p16735"},"y_scale":{"type":"object","name":"LinearScale","id":"p16736"},"title":{"type":"object","name":"Title","id":"p16732","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p16770","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p16722","attributes":{"selected":{"type":"object","name":"Selection","id":"p16723","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p16724"},"data":{"type":"map","entries":[["year",[2001,2004,2005,2010,2011,2013,2014,2015,2018,2019,2020,2022,2023,2024,2025,2026]],["share",[0.0,50.0,71.42857142857143,0.0,0.0,0.0,4.166666666666666,45.45454545454545,100.0,100.0,72.97297297297297,2.0708283313325326,0.2579812963560142,6.256109481915933,21.458773784355177,1.13345521023766]],["detected",[0,1,5,0,0,0,1,5,1,8,27,69,8,128,406,31]],["evaluable",[2,2,7,5,2,1,24,11,1,8,37,3332,3101,2046,1892,2735]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,9.07684386569143,9.897626379762722,9.667366891029102,9.07684386569143,8.703135093227193,10.74264168206181,10.209683151927734,8.703135093227193,9.989711205477885,11.030852377887435,13.633479338462706,13.596746898786423,13.381615773402649,13.340636602699803,13.53223159288676]]]}}},"view":{"type":"object","name":"CDSView","id":"p16771","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16772"}}},"glyph":{"type":"object","name":"Line","id":"p16767","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p16768","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p16769","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p16776","attributes":{"data_source":{"id":"p16722"},"view":{"type":"object","name":"CDSView","id":"p16777","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16778"}}},"glyph":{"type":"object","name":"Scatter","id":"p16773","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p16774","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p16775","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p16733","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p16747"},{"type":"object","name":"BoxZoomTool","id":"p16748","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p16749","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p16755","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16754","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p16756","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p16757"},{"type":"object","name":"SaveTool","id":"p16758"},{"type":"object","name":"HoverTool","id":"p16779","attributes":{"renderers":[{"id":"p16776"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p16742","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16743","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16744"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16745"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p16737","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16738","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16739"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16740"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p16741","attributes":{"axis":{"id":"p16737"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p16746","attributes":{"dimension":1,"axis":{"id":"p16742"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p16759","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p16761","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p16762","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p16763","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p16765","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16764","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p16766","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"d4fac347-d880-4890-9ebc-6d137ed2c84a","roots":{"p16725":"efb67135-2522-465f-9a0e-a5705772580d"},"root_ids":["p16725"]}];
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

<div id="b605c9ef-065a-43dd-a9cb-3efd63a017a3" data-root-id="p16785" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"946a7c92-fe6c-4f77-b167-de71a1c798c8":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p16825","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p16826"}}},"roots":[{"type":"object","name":"Figure","id":"p16785","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p16786"},"y_range":{"type":"object","name":"DataRange1d","id":"p16787","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p16794"},"y_scale":{"type":"object","name":"LinearScale","id":"p16795"},"title":{"type":"object","name":"Title","id":"p16792","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p16821","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p16782","attributes":{"selected":{"type":"object","name":"Selection","id":"p16783","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p16784"},"data":{"type":"map","entries":[["year",[2001,2004,2005,2010,2011,2013,2014,2015,2018,2019,2020,2022,2023,2024,2025,2026]],["evaluable",[2,2,7,5,2,1,24,11,1,8,37,3332,3101,2046,1892,2735]],["detected",[0,1,5,0,0,0,1,5,1,8,27,69,8,128,406,31]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p16822","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16823"}}},"glyph":{"type":"object","name":"VBar","id":"p16818","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p16819","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p16820","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p16793","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p16806"},{"type":"object","name":"BoxZoomTool","id":"p16807","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p16808","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p16814","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16813","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p16815","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p16816"},{"type":"object","name":"SaveTool","id":"p16817"},{"type":"object","name":"HoverTool","id":"p16824","attributes":{"renderers":[{"id":"p16821"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p16801","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16802","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16803"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16804"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p16796","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16797","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16798"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16799"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p16800","attributes":{"axis":{"id":"p16796"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p16805","attributes":{"dimension":1,"axis":{"id":"p16801"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"946a7c92-fe6c-4f77-b167-de71a1c798c8","roots":{"p16785":"b605c9ef-065a-43dd-a9cb-3efd63a017a3"},"root_ids":["p16785"]}];
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

<div id="f1c46131-e84a-4bd5-abdd-88511aba88e6" data-root-id="p16830" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"faa2e254-fff8-439f-818d-9555671fc43f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p16872","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p16873"}}},"roots":[{"type":"object","name":"Figure","id":"p16830","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p16832"},"y_range":{"type":"object","name":"FactorRange","id":"p16839","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p16840"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p16841"},"title":{"type":"object","name":"Title","id":"p16837","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p16867","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p16827","attributes":{"selected":{"type":"object","name":"Selection","id":"p16828","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p16829"},"data":{"type":"map","entries":[["x",[-6,-5,-24]],["y",["probe","forward","reverse"]],["alpha",[1.0,0.9846812055126457,0.9846812055126457]],["pos",[6,5,24]],["base",["C","A","A"]],["n",[9197,3242,3242]],["det_with",["0% of 9197","0% of 3242","0% of 3242"]],["det_without",["18% of 3934","7% of 9889","7% of 9889"]],["subs",["C&gt;T 9197","A&gt;G 3242","A&gt;G 3241, A&gt;T 1"]],["zone",["no","yes","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p16868","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16869"}}},"glyph":{"type":"object","name":"Rect","id":"p16864","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p16865","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p16866","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p16838","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p16852"},{"type":"object","name":"BoxZoomTool","id":"p16853","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p16854","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p16860","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16859","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p16861","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p16862"},{"type":"object","name":"SaveTool","id":"p16863"},{"type":"object","name":"HoverTool","id":"p16870","attributes":{"renderers":[{"id":"p16867"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p16847","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p16848"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p16849"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16850"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p16842","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p16871","attributes":{"ticks":[-24,-6,-5],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16844"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-6,"6"],[-5,"5"],[-24,"24"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p16845"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p16846","attributes":{"axis":{"id":"p16842"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p16851","attributes":{"dimension":1,"axis":{"id":"p16847"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"faa2e254-fff8-439f-818d-9555671fc43f","roots":{"p16830":"f1c46131-e84a-4bd5-abdd-88511aba88e6"},"root_ids":["p16830"]}];
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

<div id="f60d42ed-fbc5-4ea5-9f14-cdd5b5310691" data-root-id="p16877" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9299fdd9-fdb2-4ce6-8bae-1fd04a8131c5":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p16926","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p16927"}}},"roots":[{"type":"object","name":"Figure","id":"p16877","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p16886","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p16887","attributes":{"factors":["Orthopoxvirus monkeypox (3431483)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p16888"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p16889"},"title":{"type":"object","name":"Title","id":"p16884","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p16921","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p16874","attributes":{"selected":{"type":"object","name":"Selection","id":"p16875","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p16876"},"data":{"type":"map","entries":[["y",["Orthopoxvirus monkeypox (3431483)"]],["share",[9.117462966826622]],["lo",[8.334939246295061]],["hi",[9.96546668449657]],["n",[4793]],["det",[437]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p16922","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16923"}}},"glyph":{"type":"object","name":"Scatter","id":"p16918","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p16919","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p16920","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p16885","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p16900"},{"type":"object","name":"BoxZoomTool","id":"p16901","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p16902","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p16908","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16907","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p16909","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p16910"},{"type":"object","name":"SaveTool","id":"p16911"},{"type":"object","name":"HoverTool","id":"p16925","attributes":{"renderers":[{"id":"p16921"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p16895","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p16896"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p16897"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16898"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p16890","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16891","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16892"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16893"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p16894","attributes":{"axis":{"id":"p16890"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p16899","attributes":{"dimension":1,"axis":{"id":"p16895"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p16912","attributes":{"source":{"id":"p16874"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p16924","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9299fdd9-fdb2-4ce6-8bae-1fd04a8131c5","roots":{"p16877":"f60d42ed-fbc5-4ea5-9f14-cdd5b5310691"},"root_ids":["p16877"]}];
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

Disclosures on this entry: `amplicon_measured_not_published`, `scope_narrower_than_taxid`.


## What reached the statistics

14,204 records were screened for this assay and **13,206 (93%)** were evaluable, meaning both primers landed in the right orientation and size range. 998 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 976 |
| `chance_anchor` | 5 |
| `no_pair` | 1 |

