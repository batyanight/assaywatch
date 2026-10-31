# E_coli_malB_Candrian_1991

<span class="aw-chip aw-chip-declining">declining</span>

**E. coli-malB promoter**

| | |
|---|---|
| Target | Escherichia coli ([taxid 562](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=562)) |
| Gene | — |
| Chemistry | conventional |
| Amplicon | 585 bp |
| Designed | 1991 |
| Paper | [10.1016/0168-1605(91)90148-I](https://doi.org/10.1016/0168-1605(91)90148-I) |
| Registry status | active |

!!! quote "The paper"
    Candrian U et al. 1991. Int J Food Microbiol 12:339-351 (seed list spells it Candrain)

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GACCTCGGTTTAGTTCACAGA` | 21 nt |
| reverse | `CACACGCTGACGCTGACCA` | 19 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 29 | 49 | 59.2% | 45.2% – 71.8% |
| baseline (everything earlier) | 205 | 277 | 74.0% | 68.5% – 78.8% |

Change from baseline, Newcombe interval: **-29.6% to -1.1%**. Threshold: **90.0%**.

*detected share 59.2% (45%-72%) since Oct 2024, upper bound below the 90% threshold; change from baseline -30% to -1%*

Trend across deposit years: by record falling (p=0.00206, 24 years); by footprint falling (p=0.159). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="a9fad787-98f9-427d-a7ea-504f7e3f3782" data-root-id="p12000" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"93f46176-bb0a-44c2-9c9e-1ecf62d059a2":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12055","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12056"}}},"roots":[{"type":"object","name":"Figure","id":"p12000","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p12002"},"y_range":{"type":"object","name":"Range1d","id":"p12009","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p12010"},"y_scale":{"type":"object","name":"LinearScale","id":"p12011"},"title":{"type":"object","name":"Title","id":"p12007","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12045","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p11997","attributes":{"selected":{"type":"object","name":"Selection","id":"p11998","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p11999"},"data":{"type":"map","entries":[["year",[1993,2002,2004,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,50.0,83.33333333333334,72.72727272727273,91.66666666666666,100.0,70.0,71.42857142857143,85.0,85.0,50.0,80.0,65.0,80.0,60.0,80.0,70.0,75.0,55.00000000000001,70.0,45.0]],["detected",[1,1,1,4,1,10,8,11,5,7,5,17,17,10,16,13,16,12,16,14,15,11,14,9]],["evaluable",[1,1,1,4,2,12,11,12,5,10,7,20,20,20,20,20,20,20,20,20,20,20,20,20]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,8.703135093227193,9.517227179437622,9.07684386569143,10.269703144398052,10.209683151927734,10.269703144398052,9.667366891029102,10.143865699252444,9.897626379762722,10.619414831097462,10.619414831097462,10.619414831097462,10.619414831097462,10.619414831097462,10.619414831097462,10.619414831097462,10.619414831097462,10.619414831097462,10.619414831097462,10.619414831097462,10.619414831097462,10.619414831097462]]]}}},"view":{"type":"object","name":"CDSView","id":"p12046","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12047"}}},"glyph":{"type":"object","name":"Line","id":"p12042","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p12043","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p12044","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p12051","attributes":{"data_source":{"id":"p11997"},"view":{"type":"object","name":"CDSView","id":"p12052","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12053"}}},"glyph":{"type":"object","name":"Scatter","id":"p12048","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p12049","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p12050","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12008","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12022"},{"type":"object","name":"BoxZoomTool","id":"p12023","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12024","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12030","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12029","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12031","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12032"},{"type":"object","name":"SaveTool","id":"p12033"},{"type":"object","name":"HoverTool","id":"p12054","attributes":{"renderers":[{"id":"p12051"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p12017","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12018","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12019"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12020"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12012","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12013","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12014"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12015"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12016","attributes":{"axis":{"id":"p12012"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12021","attributes":{"dimension":1,"axis":{"id":"p12017"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p12034","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p12036","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p12037","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p12038","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p12040","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12039","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p12041","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"93f46176-bb0a-44c2-9c9e-1ecf62d059a2","roots":{"p12000":"a9fad787-98f9-427d-a7ea-504f7e3f3782"},"root_ids":["p12000"]}];
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

<div id="cc0a0c60-4594-4bbb-aede-6d298473bf7c" data-root-id="p12060" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"515ccc46-b5d2-4252-a629-30d24ce89323":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12100","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12101"}}},"roots":[{"type":"object","name":"Figure","id":"p12060","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p12061"},"y_range":{"type":"object","name":"DataRange1d","id":"p12062","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p12069"},"y_scale":{"type":"object","name":"LinearScale","id":"p12070"},"title":{"type":"object","name":"Title","id":"p12067","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12096","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12057","attributes":{"selected":{"type":"object","name":"Selection","id":"p12058","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12059"},"data":{"type":"map","entries":[["year",[1993,2002,2004,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,1,4,2,12,11,12,5,10,7,20,20,20,20,20,20,20,20,20,20,20,20,20]],["detected",[1,1,1,4,1,10,8,11,5,7,5,17,17,10,16,13,16,12,16,14,15,11,14,9]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p12097","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12098"}}},"glyph":{"type":"object","name":"VBar","id":"p12093","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p12094","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p12095","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12068","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12081"},{"type":"object","name":"BoxZoomTool","id":"p12082","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12083","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12089","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12088","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12090","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12091"},{"type":"object","name":"SaveTool","id":"p12092"},{"type":"object","name":"HoverTool","id":"p12099","attributes":{"renderers":[{"id":"p12096"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p12076","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12077","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12078"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12079"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12071","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12072","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12073"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12074"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12075","attributes":{"axis":{"id":"p12071"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12080","attributes":{"dimension":1,"axis":{"id":"p12076"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"515ccc46-b5d2-4252-a629-30d24ce89323","roots":{"p12060":"cc0a0c60-4594-4bbb-aede-6d298473bf7c"},"root_ids":["p12060"]}];
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

<div id="ece29e20-e0c7-4590-b8ec-20f2a54f8908" data-root-id="p12105" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"50a5148d-e1c7-4da2-a39a-ca1241345a63":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12147","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12148"}}},"roots":[{"type":"object","name":"Figure","id":"p12105","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p12107"},"y_range":{"type":"object","name":"FactorRange","id":"p12114","attributes":{"factors":["reverse"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p12115"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p12116"},"title":{"type":"object","name":"Title","id":"p12112","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12142","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12102","attributes":{"selected":{"type":"object","name":"Selection","id":"p12103","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12104"},"data":{"type":"map","entries":[["x",[-1]],["y",["reverse"]],["alpha",[1.0]],["pos",[1]],["base",["A"]],["n",[92]],["det_with",["0% of 92"]],["det_without",["100% of 234"]],["subs",["A&gt;G 92"]],["zone",["yes"]]]}}},"view":{"type":"object","name":"CDSView","id":"p12143","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12144"}}},"glyph":{"type":"object","name":"Rect","id":"p12139","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p12140","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p12141","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12113","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12127"},{"type":"object","name":"BoxZoomTool","id":"p12128","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12129","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12135","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12134","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12136","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12137"},{"type":"object","name":"SaveTool","id":"p12138"},{"type":"object","name":"HoverTool","id":"p12145","attributes":{"renderers":[{"id":"p12142"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p12122","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p12123"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p12124"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12125"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12117","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p12146","attributes":{"ticks":[-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12119"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-1,"1"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p12120"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12121","attributes":{"axis":{"id":"p12117"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12126","attributes":{"dimension":1,"axis":{"id":"p12122"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"50a5148d-e1c7-4da2-a39a-ca1241345a63","roots":{"p12105":"ece29e20-e0c7-4590-b8ec-20f2a54f8908"},"root_ids":["p12105"]}];
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

<div id="ffa39c62-796d-4aee-906e-428d20a99439" data-root-id="p12152" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"621e3afc-2d41-4b2d-99c0-ed3215caebfd":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12201","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12202"}}},"roots":[{"type":"object","name":"Figure","id":"p12152","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p12161","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p12162","attributes":{"factors":["unresolved"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p12163"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p12164"},"title":{"type":"object","name":"Title","id":"p12159","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12196","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12149","attributes":{"selected":{"type":"object","name":"Selection","id":"p12150","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12151"},"data":{"type":"map","entries":[["y",["unresolved"]],["share",[59.183673469387756]],["lo",[45.24731939184714]],["hi",[71.78476147961312]],["n",[49]],["det",[29]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p12197","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12198"}}},"glyph":{"type":"object","name":"Scatter","id":"p12193","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p12194","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p12195","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12160","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12175"},{"type":"object","name":"BoxZoomTool","id":"p12176","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12177","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12183","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12182","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12184","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12185"},{"type":"object","name":"SaveTool","id":"p12186"},{"type":"object","name":"HoverTool","id":"p12200","attributes":{"renderers":[{"id":"p12196"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p12170","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p12171"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p12172"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12173"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12165","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12166","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12167"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12168"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12169","attributes":{"axis":{"id":"p12165"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12174","attributes":{"dimension":1,"axis":{"id":"p12170"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p12187","attributes":{"source":{"id":"p12149"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p12199","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"621e3afc-2d41-4b2d-99c0-ed3215caebfd","roots":{"p12152":"ffa39c62-796d-4aee-906e-428d20a99439"},"root_ids":["p12152"]}];
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
(malB[Gene] OR malE[Gene] OR malK[Gene] OR "malB"[Title] OR "malE-malK"[Title]) AND 1:30000[SLEN] NOT "whole genome shotgun"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `orientation_inferred`.


## What reached the statistics

401 records were screened for this assay and **326 (81%)** were evaluable, meaning both primers landed in the right orientation and size range. 75 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 73 |
| `truncated` | 2 |

