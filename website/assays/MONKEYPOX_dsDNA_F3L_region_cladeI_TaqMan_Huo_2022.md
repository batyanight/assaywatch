# MONKEYPOX_dsDNA_F3L_region_cladeI_TaqMan_Huo_2022

<span class="aw-chip aw-chip-declining">declining</span>

**MONKEYPOX virus (dsDNA) — Panel 1 clade I probe (Huo 2022)**

| | |
|---|---|
| Target | Monkeypox virus ([taxid 10244](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10244)) |
| Gene | F3L region (positions 46313-46491 of ON563414.2) |
| Chemistry | hydrolysis_probe |
| Amplicon | 179 bp |
| Designed | 2022 |
| Paper | [10.1016/j.bsheal.2022.10.005](https://doi.org/10.1016/j.bsheal.2022.10.005) |
| Registry status | draft |

!!! quote "The paper"
    Huo S, Chen Y, Lu R, Zhang Z, Zhang G, Zhao L, Deng Y, Wu C, Tan W. 2022. Development of two multiplex real-time PCR assays for simultaneous detection and differentiation of monkeypox virus IIa, IIb, and I clades and the B.1 lineage. Biosaf Health 4:392-398

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ATCCTCTCTCATTGATTTTTCGCGGGA` | 27 nt |
| reverse | `TGGAGAAGCGAGAAGTTAATAAAGC` | 25 nt |
| probe | `TCGTCGGAACTGTACACCATAGTAC` | 25 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 2,429 | 4,935 | 49.2% | 47.8% – 50.6% |
| baseline (everything earlier) | 549 | 8,566 | 6.4% | 5.9% – 6.9% |

Change from baseline, Newcombe interval: **41.3% to 44.3%**. Threshold: **90.0%**.

*pooled share 49.2% has low coverage, but lineage Orthopoxvirus monkeypox (3431483) (4568 records) detects 53.2% (51.7%-54.6%); lineage verdict overrides to declining*

Trend across deposit years: by record rising (p=0, 16 years); by footprint falling (p=0.261); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="af4579a7-3af0-4e96-8b99-704ae3b50d21" data-root-id="p17502" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"444abe12-fb8d-44cc-899f-cd5a7d70d2e8":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17557","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17558"}}},"roots":[{"type":"object","name":"Figure","id":"p17502","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p17504"},"y_range":{"type":"object","name":"Range1d","id":"p17511","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p17512"},"y_scale":{"type":"object","name":"LinearScale","id":"p17513"},"title":{"type":"object","name":"Title","id":"p17509","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17547","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17499","attributes":{"selected":{"type":"object","name":"Selection","id":"p17500","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17501"},"data":{"type":"map","entries":[["year",[2001,2004,2005,2010,2011,2013,2014,2015,2018,2019,2020,2022,2023,2024,2025,2026]],["share",[100.0,0.0,28.57142857142857,33.33333333333333,100.0,100.0,95.83333333333334,54.54545454545454,0.0,0.0,27.027027027027028,0.02901915264074289,0.09578544061302681,23.820867079561697,36.16118769883351,61.45172656800564]],["detected",[2,0,2,1,2,2,23,6,0,0,10,1,3,500,682,1744]],["evaluable",[2,1,7,3,2,2,24,11,3,8,37,3446,3132,2099,1886,2838]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,8.703135093227193,9.897626379762722,9.328625426046248,9.07684386569143,9.07684386569143,10.74264168206181,10.209683151927734,9.328625426046248,9.989711205477885,11.030852377887435,13.650635290216197,13.601839928618176,13.394973899358671,13.338969847336015,13.551262237910041]]]}}},"view":{"type":"object","name":"CDSView","id":"p17548","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17549"}}},"glyph":{"type":"object","name":"Line","id":"p17544","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p17545","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p17546","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p17553","attributes":{"data_source":{"id":"p17499"},"view":{"type":"object","name":"CDSView","id":"p17554","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17555"}}},"glyph":{"type":"object","name":"Scatter","id":"p17550","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p17551","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p17552","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17510","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17524"},{"type":"object","name":"BoxZoomTool","id":"p17525","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17526","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17532","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17531","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17533","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17534"},{"type":"object","name":"SaveTool","id":"p17535"},{"type":"object","name":"HoverTool","id":"p17556","attributes":{"renderers":[{"id":"p17553"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p17519","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17520","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17521"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17522"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17514","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17515","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17516"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17517"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17518","attributes":{"axis":{"id":"p17514"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17523","attributes":{"dimension":1,"axis":{"id":"p17519"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p17536","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p17538","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p17539","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p17540","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p17542","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17541","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p17543","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"444abe12-fb8d-44cc-899f-cd5a7d70d2e8","roots":{"p17502":"af4579a7-3af0-4e96-8b99-704ae3b50d21"},"root_ids":["p17502"]}];
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

<div id="bb79e64d-eca0-444a-97e1-7a713b76ccb1" data-root-id="p17562" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9c7375db-4a0d-4b4c-8952-1c822f11d0f5":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17602","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17603"}}},"roots":[{"type":"object","name":"Figure","id":"p17562","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p17563"},"y_range":{"type":"object","name":"DataRange1d","id":"p17564","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p17571"},"y_scale":{"type":"object","name":"LinearScale","id":"p17572"},"title":{"type":"object","name":"Title","id":"p17569","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17598","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17559","attributes":{"selected":{"type":"object","name":"Selection","id":"p17560","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17561"},"data":{"type":"map","entries":[["year",[2001,2004,2005,2010,2011,2013,2014,2015,2018,2019,2020,2022,2023,2024,2025,2026]],["evaluable",[2,1,7,3,2,2,24,11,3,8,37,3446,3132,2099,1886,2838]],["detected",[2,0,2,1,2,2,23,6,0,0,10,1,3,500,682,1744]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p17599","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17600"}}},"glyph":{"type":"object","name":"VBar","id":"p17595","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p17596","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p17597","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17570","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17583"},{"type":"object","name":"BoxZoomTool","id":"p17584","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17585","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17591","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17590","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17592","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17593"},{"type":"object","name":"SaveTool","id":"p17594"},{"type":"object","name":"HoverTool","id":"p17601","attributes":{"renderers":[{"id":"p17598"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p17578","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17579","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17580"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17581"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17573","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17574","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17575"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17576"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17577","attributes":{"axis":{"id":"p17573"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17582","attributes":{"dimension":1,"axis":{"id":"p17578"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9c7375db-4a0d-4b4c-8952-1c822f11d0f5","roots":{"p17562":"bb79e64d-eca0-444a-97e1-7a713b76ccb1"},"root_ids":["p17562"]}];
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

<div id="ac2f7af1-5452-4678-8fb0-75fcbf6ecfbc" data-root-id="p17607" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"ca422f8f-76e9-4940-9df1-d00f1221af69":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17649","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17650"}}},"roots":[{"type":"object","name":"Figure","id":"p17607","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p17609"},"y_range":{"type":"object","name":"FactorRange","id":"p17616","attributes":{"factors":["probe","reverse"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p17617"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p17618"},"title":{"type":"object","name":"Title","id":"p17614","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17644","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17604","attributes":{"selected":{"type":"object","name":"Selection","id":"p17605","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17606"},"data":{"type":"map","entries":[["x",[-3,-17,-11,-21,-14]],["y",["probe","probe","probe","probe","reverse"]],["alpha",[1.0,1.0,1.0,1.0,0.15629582993852306]],["pos",[3,17,11,21,14]],["base",["T","A","C","C","G"]],["n",[10647,10643,10071,10070,25]],["det_with",["0% of 10647","0% of 10643","0% of 10071","0% of 10070","0% of 25"]],["det_without",["99% of 3000","99% of 3004","83% of 3576","83% of 3577","22% of 13622"]],["subs",["T&gt;C 10647","A&gt;G 10628, A&gt;T 15","C&gt;A 10070, C&gt;T 1","C&gt;T 10070","G&gt;A 25"]],["zone",["yes","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p17645","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17646"}}},"glyph":{"type":"object","name":"Rect","id":"p17641","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p17642","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p17643","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17615","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17629"},{"type":"object","name":"BoxZoomTool","id":"p17630","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17631","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17637","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17636","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17638","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17639"},{"type":"object","name":"SaveTool","id":"p17640"},{"type":"object","name":"HoverTool","id":"p17647","attributes":{"renderers":[{"id":"p17644"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p17624","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p17625"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p17626"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17627"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17619","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p17648","attributes":{"ticks":[-21,-17,-14,-11,-3],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17621"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-3,"3"],[-17,"17"],[-11,"11"],[-21,"21"],[-14,"14"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p17622"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17623","attributes":{"axis":{"id":"p17619"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17628","attributes":{"dimension":1,"axis":{"id":"p17624"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"ca422f8f-76e9-4940-9df1-d00f1221af69","roots":{"p17607":"ac2f7af1-5452-4678-8fb0-75fcbf6ecfbc"},"root_ids":["p17607"]}];
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

<div id="faed981f-31ec-498a-80df-28c1b4bac787" data-root-id="p17654" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"08f45e84-4b33-4d57-bf1b-8ae59b9d5717":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17703","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17704"}}},"roots":[{"type":"object","name":"Figure","id":"p17654","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p17663","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p17664","attributes":{"factors":["Orthopoxvirus monkeypox (3431483)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p17665"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p17666"},"title":{"type":"object","name":"Title","id":"p17661","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17698","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17651","attributes":{"selected":{"type":"object","name":"Selection","id":"p17652","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17653"},"data":{"type":"map","entries":[["y",["Orthopoxvirus monkeypox (3431483)"]],["share",[53.17425569176882]],["lo",[51.72516226781192]],["hi",[54.61801482203417]],["n",[4568]],["det",[2429]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p17699","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17700"}}},"glyph":{"type":"object","name":"Scatter","id":"p17695","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p17696","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p17697","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17662","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17677"},{"type":"object","name":"BoxZoomTool","id":"p17678","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17679","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17685","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17684","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17686","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17687"},{"type":"object","name":"SaveTool","id":"p17688"},{"type":"object","name":"HoverTool","id":"p17702","attributes":{"renderers":[{"id":"p17698"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p17672","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p17673"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p17674"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17675"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17667","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17668","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17669"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17670"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17671","attributes":{"axis":{"id":"p17667"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17676","attributes":{"dimension":1,"axis":{"id":"p17672"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p17689","attributes":{"source":{"id":"p17651"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p17701","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"08f45e84-4b33-4d57-bf1b-8ae59b9d5717","roots":{"p17654":"faed981f-31ec-498a-80df-28c1b4bac787"},"root_ids":["p17654"]}];
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

3,772 screened records fell outside the declared scope.

The paper claims this assay does **not** amplify 7 other taxa. Those are retrieved on purpose and reported as predicted cross-reactivity; they are never scored.

Disclosures on this entry: `amplicon_measured_not_published`, `scope_narrower_than_taxid`.


## What reached the statistics

14,204 records were screened for this assay and **13,501 (95%)** were evaluable, meaning both primers landed in the right orientation and size range. 703 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 693 |

