# MONKEYPOX_dsDNA_B1_SNP_lineageB1_TaqMan_Huo_2022

<span class="aw-chip aw-chip-declining">declining</span>

**MONKEYPOX virus (dsDNA) — Panel 2 B.1 lineage SNP probe (Huo 2022)**

| | |
|---|---|
| Target | Monkeypox virus ([taxid 10244](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10244)) |
| Gene | SNP-typing locus at 183519-183542 of ON563414.2 |
| Chemistry | hydrolysis_probe |
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
| probe | `AAACCAGTCCAAAATTCGCCACAA` | 24 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 1,676 | 4,839 | 34.6% | 33.3% – 36.0% |
| baseline (everything earlier) | 7,517 | 8,369 | 89.8% | 89.2% – 90.4% |

Change from baseline, Newcombe interval: **-56.7% to -53.7%**. Threshold: **90.0%**.

*detected share 34.6% (33%-36%) since Oct 2024, upper bound below the 90% threshold; change from baseline -57% to -54%*

Trend across deposit years: by record falling (p=0, 16 years); by footprint rising (p=0.0621); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="d986f55a-ed3b-4023-8366-9a621f84f6d6" data-root-id="p16519" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"cff9ba5b-9fd4-40a3-9123-7c03bb2aa104":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p16574","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p16575"}}},"roots":[{"type":"object","name":"Figure","id":"p16519","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p16521"},"y_range":{"type":"object","name":"Range1d","id":"p16528","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p16529"},"y_scale":{"type":"object","name":"LinearScale","id":"p16530"},"title":{"type":"object","name":"Title","id":"p16526","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p16564","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p16516","attributes":{"selected":{"type":"object","name":"Selection","id":"p16517","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p16518"},"data":{"type":"map","entries":[["year",[2001,2004,2005,2010,2011,2013,2014,2015,2018,2019,2020,2022,2023,2024,2025,2026]],["share",[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,97.80912364945978,99.54853273137697,67.36687835857353,37.77073428420496,27.531992687385742]],["detected",[0,0,0,0,0,0,0,0,0,0,0,3259,3087,1379,715,753]],["evaluable",[2,2,7,5,2,1,24,11,1,8,37,3332,3101,2047,1893,2735]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,9.07684386569143,9.897626379762722,9.667366891029102,9.07684386569143,8.703135093227193,10.74264168206181,10.209683151927734,8.703135093227193,9.989711205477885,11.030852377887435,13.633479338462706,13.596746898786423,13.381871161192226,13.34091385549079,13.53223159288676]]]}}},"view":{"type":"object","name":"CDSView","id":"p16565","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16566"}}},"glyph":{"type":"object","name":"Line","id":"p16561","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p16562","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p16563","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p16570","attributes":{"data_source":{"id":"p16516"},"view":{"type":"object","name":"CDSView","id":"p16571","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16572"}}},"glyph":{"type":"object","name":"Scatter","id":"p16567","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p16568","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p16569","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p16527","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p16541"},{"type":"object","name":"BoxZoomTool","id":"p16542","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p16543","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p16549","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16548","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p16550","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p16551"},{"type":"object","name":"SaveTool","id":"p16552"},{"type":"object","name":"HoverTool","id":"p16573","attributes":{"renderers":[{"id":"p16570"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p16536","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16537","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16538"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16539"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p16531","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16532","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16533"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16534"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p16535","attributes":{"axis":{"id":"p16531"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p16540","attributes":{"dimension":1,"axis":{"id":"p16536"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p16553","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p16555","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p16556","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p16557","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p16559","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16558","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p16560","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"cff9ba5b-9fd4-40a3-9123-7c03bb2aa104","roots":{"p16519":"d986f55a-ed3b-4023-8366-9a621f84f6d6"},"root_ids":["p16519"]}];
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

<div id="d97ca8ce-9986-48b5-b6d9-75dae5e2f899" data-root-id="p16579" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"370db5ed-3b19-414e-9724-9761cf14c44a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p16619","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p16620"}}},"roots":[{"type":"object","name":"Figure","id":"p16579","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p16580"},"y_range":{"type":"object","name":"DataRange1d","id":"p16581","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p16588"},"y_scale":{"type":"object","name":"LinearScale","id":"p16589"},"title":{"type":"object","name":"Title","id":"p16586","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p16615","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p16576","attributes":{"selected":{"type":"object","name":"Selection","id":"p16577","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p16578"},"data":{"type":"map","entries":[["year",[2001,2004,2005,2010,2011,2013,2014,2015,2018,2019,2020,2022,2023,2024,2025,2026]],["evaluable",[2,2,7,5,2,1,24,11,1,8,37,3332,3101,2047,1893,2735]],["detected",[0,0,0,0,0,0,0,0,0,0,0,3259,3087,1379,715,753]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p16616","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16617"}}},"glyph":{"type":"object","name":"VBar","id":"p16612","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p16613","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p16614","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p16587","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p16600"},{"type":"object","name":"BoxZoomTool","id":"p16601","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p16602","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p16608","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16607","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p16609","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p16610"},{"type":"object","name":"SaveTool","id":"p16611"},{"type":"object","name":"HoverTool","id":"p16618","attributes":{"renderers":[{"id":"p16615"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p16595","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16596","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16597"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16598"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p16590","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16591","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16592"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16593"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p16594","attributes":{"axis":{"id":"p16590"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p16599","attributes":{"dimension":1,"axis":{"id":"p16595"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"370db5ed-3b19-414e-9724-9761cf14c44a","roots":{"p16579":"d97ca8ce-9986-48b5-b6d9-75dae5e2f899"},"root_ids":["p16579"]}];
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

<div id="d9ed0085-49a4-4ecc-ae73-6e9de09f7c17" data-root-id="p16624" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"108cf80f-1f8c-44de-9e84-a5a2367432ab":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p16666","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p16667"}}},"roots":[{"type":"object","name":"Figure","id":"p16624","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p16626"},"y_range":{"type":"object","name":"FactorRange","id":"p16633","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p16634"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p16635"},"title":{"type":"object","name":"Title","id":"p16631","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p16661","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p16621","attributes":{"selected":{"type":"object","name":"Selection","id":"p16622","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p16623"},"data":{"type":"map","entries":[["x",[-9,-5,-24]],["y",["probe","forward","reverse"]],["alpha",[1.0,0.9848122350090853,0.9848122350090853]],["pos",[9,5,24]],["base",["T","A","A"]],["n",[3932,3243,3243]],["det_with",["0% of 3932","0% of 3243","0% of 3243"]],["det_without",["100% of 9201","93% of 9890","93% of 9890"]],["subs",["T&gt;C 3932","A&gt;G 3243","A&gt;G 3242, A&gt;T 1"]],["zone",["no","yes","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p16662","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16663"}}},"glyph":{"type":"object","name":"Rect","id":"p16658","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p16659","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p16660","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p16632","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p16646"},{"type":"object","name":"BoxZoomTool","id":"p16647","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p16648","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p16654","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16653","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p16655","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p16656"},{"type":"object","name":"SaveTool","id":"p16657"},{"type":"object","name":"HoverTool","id":"p16664","attributes":{"renderers":[{"id":"p16661"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p16641","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p16642"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p16643"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16644"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p16636","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p16665","attributes":{"ticks":[-24,-9,-5],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16638"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-9,"9"],[-5,"5"],[-24,"24"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p16639"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p16640","attributes":{"axis":{"id":"p16636"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p16645","attributes":{"dimension":1,"axis":{"id":"p16641"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"108cf80f-1f8c-44de-9e84-a5a2367432ab","roots":{"p16624":"d9ed0085-49a4-4ecc-ae73-6e9de09f7c17"},"root_ids":["p16624"]}];
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

<div id="f2a23798-7f3b-4209-b647-fedc8dc59971" data-root-id="p16671" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"395748dd-08ec-43bd-8ca6-9e2a2b2600fe":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p16720","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p16721"}}},"roots":[{"type":"object","name":"Figure","id":"p16671","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p16680","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p16681","attributes":{"factors":["Orthopoxvirus monkeypox (3431483)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p16682"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p16683"},"title":{"type":"object","name":"Title","id":"p16678","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p16715","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p16668","attributes":{"selected":{"type":"object","name":"Selection","id":"p16669","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p16670"},"data":{"type":"map","entries":[["y",["Orthopoxvirus monkeypox (3431483)"]],["share",[34.96036712557363]],["lo",[33.623074792240004]],["hi",[36.3217428434298]],["n",[4794]],["det",[1676]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p16716","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16717"}}},"glyph":{"type":"object","name":"Scatter","id":"p16712","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p16713","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p16714","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p16679","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p16694"},{"type":"object","name":"BoxZoomTool","id":"p16695","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p16696","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p16702","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16701","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p16703","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p16704"},{"type":"object","name":"SaveTool","id":"p16705"},{"type":"object","name":"HoverTool","id":"p16719","attributes":{"renderers":[{"id":"p16715"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p16689","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p16690"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p16691"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16692"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p16684","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16685","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16686"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16687"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p16688","attributes":{"axis":{"id":"p16684"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p16693","attributes":{"dimension":1,"axis":{"id":"p16689"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p16706","attributes":{"source":{"id":"p16668"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p16718","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"395748dd-08ec-43bd-8ca6-9e2a2b2600fe","roots":{"p16671":"f2a23798-7f3b-4209-b647-fedc8dc59971"},"root_ids":["p16671"]}];
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

14,204 records were screened for this assay and **13,208 (93%)** were evaluable, meaning both primers landed in the right orientation and size range. 996 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 976 |
| `chance_anchor` | 5 |
| `no_pair` | 1 |

