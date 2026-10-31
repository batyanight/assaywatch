# MONKEYPOX_dsDNA_F3L_region_cladeIIab_TaqMan_Huo_2022

<span class="aw-chip aw-chip-declining">declining</span>

**MONKEYPOX virus (dsDNA) — Panel 1 clade IIa/IIb probe (Huo 2022)**

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
| probe | `TCGTTGGAGCTGTAAACCATAGCAC` | 25 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 2,136 | 4,936 | 43.3% | 41.9% – 44.7% |
| baseline (everything earlier) | 7,934 | 8,566 | 92.6% | 92.0% – 93.2% |

Change from baseline, Newcombe interval: **-50.8% to -47.8%**. Threshold: **90.0%**.

*detected share 43.3% (42%-45%) since Oct 2024, upper bound below the 90% threshold; change from baseline -51% to -48%*

Trend across deposit years: by record falling (p=0, 16 years); by footprint rising (p=0.924); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="ce1061ea-2864-4a18-99cc-d1042c627dfd" data-root-id="p17296" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"8c4671f0-ca3c-49d9-9b7b-ad36116aac38":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17351","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17352"}}},"roots":[{"type":"object","name":"Figure","id":"p17296","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p17298"},"y_range":{"type":"object","name":"Range1d","id":"p17305","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p17306"},"y_scale":{"type":"object","name":"LinearScale","id":"p17307"},"title":{"type":"object","name":"Title","id":"p17303","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17341","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17293","attributes":{"selected":{"type":"object","name":"Selection","id":"p17294","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17295"},"data":{"type":"map","entries":[["year",[2001,2004,2005,2010,2011,2013,2014,2015,2018,2019,2020,2022,2023,2024,2025,2026]],["share",[0.0,100.0,71.42857142857143,0.0,0.0,0.0,4.166666666666666,45.45454545454545,100.0,100.0,72.97297297297297,99.82588508415554,99.68071519795659,72.84421152929966,60.20137784843668,27.942212825933755]],["detected",[0,1,5,0,0,0,1,5,3,8,27,3440,3122,1529,1136,793]],["evaluable",[2,1,7,3,2,2,24,11,3,8,37,3446,3132,2099,1887,2838]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,8.703135093227193,9.897626379762722,9.328625426046248,9.07684386569143,9.07684386569143,10.74264168206181,10.209683151927734,9.328625426046248,9.989711205477885,11.030852377887435,13.650635290216197,13.601839928618176,13.394973899358671,13.339248026285627,13.551262237910041]]]}}},"view":{"type":"object","name":"CDSView","id":"p17342","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17343"}}},"glyph":{"type":"object","name":"Line","id":"p17338","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p17339","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p17340","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p17347","attributes":{"data_source":{"id":"p17293"},"view":{"type":"object","name":"CDSView","id":"p17348","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17349"}}},"glyph":{"type":"object","name":"Scatter","id":"p17344","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p17345","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p17346","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17304","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17318"},{"type":"object","name":"BoxZoomTool","id":"p17319","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17320","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17326","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17325","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17327","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17328"},{"type":"object","name":"SaveTool","id":"p17329"},{"type":"object","name":"HoverTool","id":"p17350","attributes":{"renderers":[{"id":"p17347"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p17313","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17314","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17315"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17316"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17308","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17309","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17310"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17311"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17312","attributes":{"axis":{"id":"p17308"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17317","attributes":{"dimension":1,"axis":{"id":"p17313"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p17330","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p17332","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p17333","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p17334","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p17336","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17335","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p17337","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"8c4671f0-ca3c-49d9-9b7b-ad36116aac38","roots":{"p17296":"ce1061ea-2864-4a18-99cc-d1042c627dfd"},"root_ids":["p17296"]}];
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

<div id="a1fde9f6-aad3-45a1-94f6-758bb1c1995a" data-root-id="p17356" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"d1caa2eb-e2b9-4641-be8f-c283ad118e37":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17396","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17397"}}},"roots":[{"type":"object","name":"Figure","id":"p17356","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p17357"},"y_range":{"type":"object","name":"DataRange1d","id":"p17358","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p17365"},"y_scale":{"type":"object","name":"LinearScale","id":"p17366"},"title":{"type":"object","name":"Title","id":"p17363","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17392","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17353","attributes":{"selected":{"type":"object","name":"Selection","id":"p17354","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17355"},"data":{"type":"map","entries":[["year",[2001,2004,2005,2010,2011,2013,2014,2015,2018,2019,2020,2022,2023,2024,2025,2026]],["evaluable",[2,1,7,3,2,2,24,11,3,8,37,3446,3132,2099,1887,2838]],["detected",[0,1,5,0,0,0,1,5,3,8,27,3440,3122,1529,1136,793]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p17393","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17394"}}},"glyph":{"type":"object","name":"VBar","id":"p17389","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p17390","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p17391","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17364","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17377"},{"type":"object","name":"BoxZoomTool","id":"p17378","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17379","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17385","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17384","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17386","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17387"},{"type":"object","name":"SaveTool","id":"p17388"},{"type":"object","name":"HoverTool","id":"p17395","attributes":{"renderers":[{"id":"p17392"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p17372","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17373","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17374"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17375"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17367","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17368","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17369"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17370"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17371","attributes":{"axis":{"id":"p17367"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17376","attributes":{"dimension":1,"axis":{"id":"p17372"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"d1caa2eb-e2b9-4641-be8f-c283ad118e37","roots":{"p17356":"a1fde9f6-aad3-45a1-94f6-758bb1c1995a"},"root_ids":["p17356"]}];
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

<div id="e3120139-2e0c-4293-bdab-8c8225f45d9e" data-root-id="p17401" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"00f2a8e4-26ec-42e8-bdaf-c81a957f856c":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17443","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17444"}}},"roots":[{"type":"object","name":"Figure","id":"p17401","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p17403"},"y_range":{"type":"object","name":"FactorRange","id":"p17410","attributes":{"factors":["probe","reverse"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p17411"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p17412"},"title":{"type":"object","name":"Title","id":"p17408","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17438","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17398","attributes":{"selected":{"type":"object","name":"Selection","id":"p17399","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17400"},"data":{"type":"map","entries":[["x",[-11,-21,-17,-3,-14]],["y",["probe","probe","probe","probe","reverse"]],["alpha",[1.0,1.0,0.9067027107095246,0.9029254925196267,0.15629536364982966]],["pos",[11,21,17,3,14]],["base",["A","T","G","C","G"]],["n",[3563,3563,3005,2990,25]],["det_with",["0% of 3563","0% of 3563","0% of 3005","0% of 2990","0% of 25"]],["det_without",["100% of 10085","100% of 10085","95% of 10643","94% of 10658","74% of 13623"]],["subs",["A&gt;C 3562, A&gt;T 1","T&gt;C 3563","G&gt;A 2990, G&gt;T 15","C&gt;T 2990","G&gt;A 25"]],["zone",["no","no","no","yes","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p17439","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17440"}}},"glyph":{"type":"object","name":"Rect","id":"p17435","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p17436","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p17437","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17409","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17423"},{"type":"object","name":"BoxZoomTool","id":"p17424","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17425","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17431","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17430","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17432","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17433"},{"type":"object","name":"SaveTool","id":"p17434"},{"type":"object","name":"HoverTool","id":"p17441","attributes":{"renderers":[{"id":"p17438"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p17418","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p17419"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p17420"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17421"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17413","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p17442","attributes":{"ticks":[-21,-17,-14,-11,-3],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17415"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-11,"11"],[-21,"21"],[-17,"17"],[-3,"3"],[-14,"14"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p17416"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17417","attributes":{"axis":{"id":"p17413"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17422","attributes":{"dimension":1,"axis":{"id":"p17418"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"00f2a8e4-26ec-42e8-bdaf-c81a957f856c","roots":{"p17401":"e3120139-2e0c-4293-bdab-8c8225f45d9e"},"root_ids":["p17401"]}];
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

<div id="e8c0992c-d0a8-4260-8ecb-ee013834aa33" data-root-id="p17448" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"c2275cb8-1df5-4694-8391-aa02867c75e4":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17497","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17498"}}},"roots":[{"type":"object","name":"Figure","id":"p17448","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p17457","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p17458","attributes":{"factors":["Orthopoxvirus monkeypox (3431483)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p17459"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p17460"},"title":{"type":"object","name":"Title","id":"p17455","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17492","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17445","attributes":{"selected":{"type":"object","name":"Selection","id":"p17446","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17447"},"data":{"type":"map","entries":[["y",["Orthopoxvirus monkeypox (3431483)"]],["share",[46.74983585029547]],["lo",[45.30643958553569]],["hi",[48.19869277747007]],["n",[4569]],["det",[2136]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p17493","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17494"}}},"glyph":{"type":"object","name":"Scatter","id":"p17489","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p17490","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p17491","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17456","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17471"},{"type":"object","name":"BoxZoomTool","id":"p17472","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17473","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17479","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17478","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17480","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17481"},{"type":"object","name":"SaveTool","id":"p17482"},{"type":"object","name":"HoverTool","id":"p17496","attributes":{"renderers":[{"id":"p17492"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p17466","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p17467"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p17468"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17469"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17461","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17462","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17463"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17464"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17465","attributes":{"axis":{"id":"p17461"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17470","attributes":{"dimension":1,"axis":{"id":"p17466"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p17483","attributes":{"source":{"id":"p17445"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p17495","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"c2275cb8-1df5-4694-8391-aa02867c75e4","roots":{"p17448":"e8c0992c-d0a8-4260-8ecb-ee013834aa33"},"root_ids":["p17448"]}];
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

14,204 records were screened for this assay and **13,502 (95%)** were evaluable, meaning both primers landed in the right orientation and size range. 702 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 693 |

