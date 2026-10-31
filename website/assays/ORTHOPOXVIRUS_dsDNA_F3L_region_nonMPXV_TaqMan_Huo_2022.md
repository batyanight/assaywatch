# ORTHOPOXVIRUS_dsDNA_F3L_region_nonMPXV_TaqMan_Huo_2022

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**ORTHOPOXVIRUS (dsDNA) — Panel 1 other-orthopoxvirus probe (Huo 2022)**

| | |
|---|---|
| Target | Orthopoxvirus ([taxid 10242](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10242)) |
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
| probe | `TCGTCGGAGCTGTACACCATAGCAC` | 25 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 29 | 5,703 | 0.5% | 0.4% – 0.7% |
| baseline (everything earlier) | 392 | 8,967 | 4.4% | 4.0% – 4.8% |

Change from baseline, Newcombe interval: **-4.3% to -3.4%**. Threshold: **90.0%**.

*detected share 0.5% (0.4%-0.7%) since Oct 2024, upper bound below the 90% threshold; change from baseline -4% to -3% (fell less than the 5% that counts as declining, from a baseline of 4%); separately, lineage Orthopoxvirus monkeypox (3431483) (5175 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift*

Trend across deposit years: by record falling (p=0, 32 years); by footprint falling (p=3.05e-08). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="f9b8cece-0e8f-4b22-b7ad-17c2f387fd06" data-root-id="p21600" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"dc8fcb72-9000-48dc-ada2-f9ae2a4e8d32":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p21655","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p21656"}}},"roots":[{"type":"object","name":"Figure","id":"p21600","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p21602"},"y_range":{"type":"object","name":"Range1d","id":"p21609","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p21610"},"y_scale":{"type":"object","name":"LinearScale","id":"p21611"},"title":{"type":"object","name":"Title","id":"p21607","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p21645","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p21597","attributes":{"selected":{"type":"object","name":"Selection","id":"p21598","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p21599"},"data":{"type":"map","entries":[["year",[1991,1993,1994,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,50.0,100.0,100.0,75.0,41.66666666666667,100.0,100.0,100.0,0.0,84.61538461538461,93.75,93.93939393939394,63.63636363636363,35.294117647058826,50.0,95.0,76.19047619047619,72.72727272727273,29.629629629629626,100.0,0.43340075122796884,0.47664442326024786,1.6861826697892273,0.27088036117381487,0.7018614586512053]],["detected",[2,4,1,1,1,3,1,2,5,2,3,5,66,4,1,0,11,15,31,42,6,2,38,16,24,16,24,15,15,36,6,23]],["evaluable",[2,4,1,1,1,3,1,4,5,2,4,12,66,4,1,3,13,16,33,66,17,4,40,21,33,54,24,3461,3147,2135,2215,3277]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,9.517227179437622,8.703135093227193,8.703135093227193,8.703135093227193,9.328625426046248,8.703135093227193,9.517227179437622,9.667366891029102,9.07684386569143,9.517227179437622,10.269703144398052,11.405466677556973,9.517227179437622,8.703135093227193,9.328625426046248,10.324834530005162,10.467343773689333,10.955310988645032,11.405466677556973,10.508782366508077,9.517227179437622,11.082053972722118,10.652487636092928,10.955310988645032,11.27702043233893,10.74264168206181,13.652848285246739,13.604285364520123,13.403846942785776,13.423015106072224,13.624981116729666]]]}}},"view":{"type":"object","name":"CDSView","id":"p21646","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p21647"}}},"glyph":{"type":"object","name":"Line","id":"p21642","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p21643","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p21644","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p21651","attributes":{"data_source":{"id":"p21597"},"view":{"type":"object","name":"CDSView","id":"p21652","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p21653"}}},"glyph":{"type":"object","name":"Scatter","id":"p21648","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p21649","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p21650","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p21608","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p21622"},{"type":"object","name":"BoxZoomTool","id":"p21623","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p21624","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p21630","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p21629","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p21631","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p21632"},{"type":"object","name":"SaveTool","id":"p21633"},{"type":"object","name":"HoverTool","id":"p21654","attributes":{"renderers":[{"id":"p21651"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p21617","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p21618","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21619"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21620"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p21612","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p21613","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21614"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21615"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p21616","attributes":{"axis":{"id":"p21612"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p21621","attributes":{"dimension":1,"axis":{"id":"p21617"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p21634","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p21636","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p21637","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p21638","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p21640","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p21639","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p21641","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"dc8fcb72-9000-48dc-ada2-f9ae2a4e8d32","roots":{"p21600":"f9b8cece-0e8f-4b22-b7ad-17c2f387fd06"},"root_ids":["p21600"]}];
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

<div id="b0bd6724-df82-4a06-b65e-4d89641dde7b" data-root-id="p21660" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b969c25f-5d9a-4d87-8ff0-5b88649c4e3d":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p21700","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p21701"}}},"roots":[{"type":"object","name":"Figure","id":"p21660","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p21661"},"y_range":{"type":"object","name":"DataRange1d","id":"p21662","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p21669"},"y_scale":{"type":"object","name":"LinearScale","id":"p21670"},"title":{"type":"object","name":"Title","id":"p21667","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p21696","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p21657","attributes":{"selected":{"type":"object","name":"Selection","id":"p21658","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p21659"},"data":{"type":"map","entries":[["year",[1991,1993,1994,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[2,4,1,1,1,3,1,4,5,2,4,12,66,4,1,3,13,16,33,66,17,4,40,21,33,54,24,3461,3147,2135,2215,3277]],["detected",[2,4,1,1,1,3,1,2,5,2,3,5,66,4,1,0,11,15,31,42,6,2,38,16,24,16,24,15,15,36,6,23]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p21697","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p21698"}}},"glyph":{"type":"object","name":"VBar","id":"p21693","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p21694","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p21695","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p21668","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p21681"},{"type":"object","name":"BoxZoomTool","id":"p21682","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p21683","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p21689","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p21688","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p21690","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p21691"},{"type":"object","name":"SaveTool","id":"p21692"},{"type":"object","name":"HoverTool","id":"p21699","attributes":{"renderers":[{"id":"p21696"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p21676","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p21677","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21678"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21679"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p21671","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p21672","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21673"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21674"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p21675","attributes":{"axis":{"id":"p21671"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p21680","attributes":{"dimension":1,"axis":{"id":"p21676"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b969c25f-5d9a-4d87-8ff0-5b88649c4e3d","roots":{"p21660":"b0bd6724-df82-4a06-b65e-4d89641dde7b"},"root_ids":["p21660"]}];
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

<div id="cd664123-950c-49c3-bf5a-506f2c8cd854" data-root-id="p21705" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"874dc5bc-6d57-4dcb-80cd-ec7af7db829d":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p21747","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p21748"}}},"roots":[{"type":"object","name":"Figure","id":"p21705","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p21707"},"y_range":{"type":"object","name":"FactorRange","id":"p21714","attributes":{"factors":["probe","reverse"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p21715"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p21716"},"title":{"type":"object","name":"Title","id":"p21712","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p21742","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p21702","attributes":{"selected":{"type":"object","name":"Selection","id":"p21703","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p21704"},"data":{"type":"map","entries":[["x",[-11,-21,-3,-17,-14]],["y",["probe","probe","probe","probe","reverse"]],["alpha",[1.0,1.0,0.8571165644171779,0.8617518745739605,0.1557941376959782]],["pos",[11,21,3,17,14]],["base",["C","C","C","G","G"]],["n",[10616,10615,3051,3071,25]],["det_with",["0% of 10616","0% of 10615","0% of 3051","1% of 3071","96% of 25"]],["det_without",["16% of 3649","16% of 3650","5% of 11214","5% of 11194","4% of 14240"]],["subs",["C&gt;A 10615, C&gt;T 1","C&gt;T 10615","C&gt;T 3051","G&gt;A 3056, G&gt;T 15","G&gt;A 25"]],["zone",["no","no","yes","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p21743","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p21744"}}},"glyph":{"type":"object","name":"Rect","id":"p21739","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p21740","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p21741","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p21713","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p21727"},{"type":"object","name":"BoxZoomTool","id":"p21728","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p21729","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p21735","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p21734","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p21736","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p21737"},{"type":"object","name":"SaveTool","id":"p21738"},{"type":"object","name":"HoverTool","id":"p21745","attributes":{"renderers":[{"id":"p21742"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p21722","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p21723"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p21724"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21725"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p21717","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p21746","attributes":{"ticks":[-21,-17,-14,-11,-3],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21719"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-11,"11"],[-21,"21"],[-3,"3"],[-17,"17"],[-14,"14"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p21720"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p21721","attributes":{"axis":{"id":"p21717"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p21726","attributes":{"dimension":1,"axis":{"id":"p21722"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"874dc5bc-6d57-4dcb-80cd-ec7af7db829d","roots":{"p21705":"cd664123-950c-49c3-bf5a-506f2c8cd854"},"root_ids":["p21705"]}];
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

<div id="edef3903-e74a-46ec-b248-0182563f7514" data-root-id="p21752" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"fb0158d6-dfca-4263-ae5d-46c2495a7d57":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p21801","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p21802"}}},"roots":[{"type":"object","name":"Figure","id":"p21752","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p21761","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p21762","attributes":{"factors":["Orthopoxvirus monkeypox (3431483)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p21763"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p21764"},"title":{"type":"object","name":"Title","id":"p21759","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p21796","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p21749","attributes":{"selected":{"type":"object","name":"Selection","id":"p21750","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p21751"},"data":{"type":"map","entries":[["y",["Orthopoxvirus monkeypox (3431483)"]],["share",[0.0]],["lo",[0.0]],["hi",[0.0741760266507345]],["n",[5175]],["det",[0]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p21797","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p21798"}}},"glyph":{"type":"object","name":"Scatter","id":"p21793","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p21794","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p21795","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p21760","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p21775"},{"type":"object","name":"BoxZoomTool","id":"p21776","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p21777","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p21783","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p21782","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p21784","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p21785"},{"type":"object","name":"SaveTool","id":"p21786"},{"type":"object","name":"HoverTool","id":"p21800","attributes":{"renderers":[{"id":"p21796"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p21770","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p21771"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p21772"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21773"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p21765","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p21766","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21767"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21768"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p21769","attributes":{"axis":{"id":"p21765"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p21774","attributes":{"dimension":1,"axis":{"id":"p21770"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p21787","attributes":{"source":{"id":"p21749"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p21799","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"fb0158d6-dfca-4263-ae5d-46c2495a7d57","roots":{"p21752":"edef3903-e74a-46ec-b248-0182563f7514"},"root_ids":["p21752"]}];
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

Disclosures on this entry: `amplicon_measured_not_published`.


## What reached the statistics

17,577 records were screened for this assay and **14,670 (83%)** were evaluable, meaning both primers landed in the right orientation and size range. 2,907 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 2,892 |
| `chance_anchor` | 3 |

