# RANAVIRUS_dsDNA_Major_capsid_protein_MCP_Pallister_2007

<span class="aw-chip aw-chip-watch">watch</span>

**Ranavirus — MCP real-time PCR RanaConF/R + probe (Pallister 2007)**

| | |
|---|---|
| Target | Ranavirus ([taxid 10492](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10492)) |
| Gene | MCP |
| Chemistry | mgb |
| Amplicon | 57 bp |
| Designed | 2007 |
| Paper | [10.1111/j.1365-2761.2007.00828.x](https://doi.org/10.1111/j.1365-2761.2007.00828.x) |
| Registry status | active |

!!! quote "The paper"
    Pallister J et al. 2007. J Fish Dis 30:427-438

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CTCATCGTTCTGGCCATCAA` | 20 nt |
| reverse | `TCCCATCGAGCCGTTCA` | 17 nt |
| probe | `CACAACATTATCCGCATC` | 18 nt |

## The verdict, and the numbers behind it

**watch** — below the threshold with an interval that still covers it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 71 | 79 | 89.9% | 81.3% – 94.8% |
| baseline (everything earlier) | 241 | 273 | 88.3% | 83.9% – 91.6% |

Change from baseline, Newcombe interval: **-7.6% to 8.2%**. Threshold: **90.0%**.

*detected share 89.9% is below the 90% threshold, but its interval (81%-95%) still reaches it*

Trend across deposit years: by record falling (p=0.00345, 28 years); by footprint falling (p=0.0243). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="e9b0fab9-c9f1-4289-90f7-d51345b77945" data-root-id="p29317" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"14bb84b4-edc2-4ecd-aaf5-f4a9ef0069ff":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p29372","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p29373"}}},"roots":[{"type":"object","name":"Figure","id":"p29317","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p29319"},"y_range":{"type":"object","name":"Range1d","id":"p29326","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p29327"},"y_scale":{"type":"object","name":"LinearScale","id":"p29328"},"title":{"type":"object","name":"Title","id":"p29324","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p29362","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p29314","attributes":{"selected":{"type":"object","name":"Selection","id":"p29315","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p29316"},"data":{"type":"map","entries":[["year",[1989,1995,2000,2001,2002,2003,2004,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,94.73684210526315,100.0,50.0,100.0,100.0,100.0,100.0,75.0,100.0,80.0,84.375,92.85714285714286,100.0,37.5,37.5,81.81818181818183,92.06349206349206,81.25]],["detected",[1,1,17,2,1,3,4,6,1,1,18,4,3,5,18,12,21,9,19,24,27,26,3,3,3,9,58,13]],["evaluable",[1,1,17,2,1,3,4,6,1,1,19,4,6,5,18,12,21,12,19,30,32,28,3,8,8,11,63,16]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,10.508782366508077,9.07684386569143,8.703135093227193,9.328625426046248,9.517227179437622,9.791719296345839,8.703135093227193,8.703135093227193,10.584573151575475,9.517227179437622,9.791719296345839,9.667366891029102,10.547770533331066,10.269703144398052,10.652487636092928,10.269703144398052,10.584573151575475,10.892023970177537,10.934913263353746,10.846014908695619,9.328625426046248,9.989711205477885,9.989711205477885,10.209683151927734,11.375828278421016,10.467343773689333]]]}}},"view":{"type":"object","name":"CDSView","id":"p29363","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p29364"}}},"glyph":{"type":"object","name":"Line","id":"p29359","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b26a00","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p29360","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b26a00","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p29361","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b26a00","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p29368","attributes":{"data_source":{"id":"p29314"},"view":{"type":"object","name":"CDSView","id":"p29369","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p29370"}}},"glyph":{"type":"object","name":"Scatter","id":"p29365","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b26a00"},"hatch_color":{"type":"value","value":"#b26a00"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p29366","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b26a00"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b26a00"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p29367","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b26a00"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b26a00"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p29325","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p29339"},{"type":"object","name":"BoxZoomTool","id":"p29340","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p29341","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p29347","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p29346","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p29348","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p29349"},{"type":"object","name":"SaveTool","id":"p29350"},{"type":"object","name":"HoverTool","id":"p29371","attributes":{"renderers":[{"id":"p29368"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p29334","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p29335","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p29336"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p29337"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p29329","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p29330","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p29331"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p29332"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p29333","attributes":{"axis":{"id":"p29329"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p29338","attributes":{"dimension":1,"axis":{"id":"p29334"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p29351","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p29353","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p29354","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p29355","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p29357","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p29356","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p29358","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"14bb84b4-edc2-4ecd-aaf5-f4a9ef0069ff","roots":{"p29317":"e9b0fab9-c9f1-4289-90f7-d51345b77945"},"root_ids":["p29317"]}];
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

<div id="a11b4382-6bea-4898-aa25-860ac31e3059" data-root-id="p29377" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"22397bbf-4ba8-43b3-a5e4-fbb4ed9b9a40":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p29417","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p29418"}}},"roots":[{"type":"object","name":"Figure","id":"p29377","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p29378"},"y_range":{"type":"object","name":"DataRange1d","id":"p29379","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p29386"},"y_scale":{"type":"object","name":"LinearScale","id":"p29387"},"title":{"type":"object","name":"Title","id":"p29384","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p29413","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p29374","attributes":{"selected":{"type":"object","name":"Selection","id":"p29375","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p29376"},"data":{"type":"map","entries":[["year",[1989,1995,2000,2001,2002,2003,2004,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,17,2,1,3,4,6,1,1,19,4,6,5,18,12,21,12,19,30,32,28,3,8,8,11,63,16]],["detected",[1,1,17,2,1,3,4,6,1,1,18,4,3,5,18,12,21,9,19,24,27,26,3,3,3,9,58,13]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b26a00","#b26a00","#b26a00"]]]}}},"view":{"type":"object","name":"CDSView","id":"p29414","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p29415"}}},"glyph":{"type":"object","name":"VBar","id":"p29410","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p29411","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p29412","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p29385","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p29398"},{"type":"object","name":"BoxZoomTool","id":"p29399","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p29400","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p29406","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p29405","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p29407","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p29408"},{"type":"object","name":"SaveTool","id":"p29409"},{"type":"object","name":"HoverTool","id":"p29416","attributes":{"renderers":[{"id":"p29413"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p29393","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p29394","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p29395"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p29396"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p29388","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p29389","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p29390"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p29391"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p29392","attributes":{"axis":{"id":"p29388"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p29397","attributes":{"dimension":1,"axis":{"id":"p29393"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"22397bbf-4ba8-43b3-a5e4-fbb4ed9b9a40","roots":{"p29377":"a11b4382-6bea-4898-aa25-860ac31e3059"},"root_ids":["p29377"]}];
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

<div id="a00fa114-49ea-4d60-91d0-870da3bb6f2b" data-root-id="p29422" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"1bf754c6-f6e6-4287-805e-9467042e1a04":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p29464","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p29465"}}},"roots":[{"type":"object","name":"Figure","id":"p29422","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p29424"},"y_range":{"type":"object","name":"FactorRange","id":"p29431","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p29432"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p29433"},"title":{"type":"object","name":"Title","id":"p29429","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p29459","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p29419","attributes":{"selected":{"type":"object","name":"Selection","id":"p29420","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p29421"},"data":{"type":"map","entries":[["x",[-11,-18,-17,-15,-11,-12,-8,-17]],["y",["forward","forward","reverse","forward","reverse","forward","reverse","forward"]],["alpha",[0.5073863636363636,0.5073863636363636,0.5170454545454546,0.5267045454545455,0.5267045454545455,0.5363636363636364,0.7295454545454545,0.7971590909090909]],["pos",[11,18,17,15,11,12,8,17]],["base",["C","C","T","C","C","T","G","A"]],["n",[37,37,38,39,39,40,60,67]],["det_with",["0% of 37","0% of 37","3% of 38","5% of 39","5% of 39","8% of 40","38% of 60","45% of 67"]],["det_without",["99% of 314","99% of 314","99% of 313","99% of 312","99% of 312","99% of 311","99% of 291","99% of 284"]],["subs",["C&gt;A 37","C&gt;G 37","T&gt;A 37, T&gt;G 1","C&gt;G 37, C&gt;T 2","C&gt;G 37, C&gt;T 2","T&gt;C 40","G&gt;A 60","A&gt;G 67"]],["zone",["no","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p29460","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p29461"}}},"glyph":{"type":"object","name":"Rect","id":"p29456","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p29457","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p29458","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p29430","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p29444"},{"type":"object","name":"BoxZoomTool","id":"p29445","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p29446","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p29452","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p29451","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p29453","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p29454"},{"type":"object","name":"SaveTool","id":"p29455"},{"type":"object","name":"HoverTool","id":"p29462","attributes":{"renderers":[{"id":"p29459"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p29439","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p29440"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p29441"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p29442"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p29434","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p29463","attributes":{"ticks":[-18,-17,-15,-12,-11,-8],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p29436"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-11,"11"],[-18,"18"],[-17,"17"],[-15,"15"],[-12,"12"],[-8,"8"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p29437"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p29438","attributes":{"axis":{"id":"p29434"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p29443","attributes":{"dimension":1,"axis":{"id":"p29439"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"1bf754c6-f6e6-4287-805e-9467042e1a04","roots":{"p29422":"a00fa114-49ea-4d60-91d0-870da3bb6f2b"},"root_ids":["p29422"]}];
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

<div id="d44566c4-de4c-452f-aac4-e27d854d1696" data-root-id="p29469" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"31137830-5c83-4507-b373-5a29e1ead7e3":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p29518","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p29519"}}},"roots":[{"type":"object","name":"Figure","id":"p29469","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p29478","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p29479","attributes":{"factors":["Ranavirus micropterus1 (3432136)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p29480"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p29481"},"title":{"type":"object","name":"Title","id":"p29476","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p29513","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p29466","attributes":{"selected":{"type":"object","name":"Selection","id":"p29467","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p29468"},"data":{"type":"map","entries":[["y",["Ranavirus micropterus1 (3432136)"]],["share",[93.22033898305084]],["lo",[83.8244756312555]],["hi",[97.33213810286956]],["n",[59]],["det",[55]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p29514","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p29515"}}},"glyph":{"type":"object","name":"Scatter","id":"p29510","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p29511","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p29512","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p29477","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p29492"},{"type":"object","name":"BoxZoomTool","id":"p29493","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p29494","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p29500","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p29499","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p29501","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p29502"},{"type":"object","name":"SaveTool","id":"p29503"},{"type":"object","name":"HoverTool","id":"p29517","attributes":{"renderers":[{"id":"p29513"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p29487","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p29488"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p29489"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p29490"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p29482","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p29483","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p29484"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p29485"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p29486","attributes":{"axis":{"id":"p29482"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p29491","attributes":{"dimension":1,"axis":{"id":"p29487"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p29504","attributes":{"source":{"id":"p29466"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p29516","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"31137830-5c83-4507-b373-5a29e1ead7e3","roots":{"p29469":"d44566c4-de4c-452f-aac4-e27d854d1696"},"root_ids":["p29469"]}];
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

Disclosures on this entry: `oligos_read_from_figure`, `amplicon_measured_not_published`.


## What reached the statistics

1,467 records were screened for this assay and **352 (24%)** were evaluable, meaning both primers landed in the right orientation and size range. 1,115 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 1,076 |
| `truncated` | 28 |
| `chance_anchor` | 9 |
| `chance_only` | 2 |

