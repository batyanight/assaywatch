# ORTHOBUNYAVIRUS_ssRNA_M_segment

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**ORTHOBUNYAVIRUS (ssRNA) — M segment (PREDICT P-023)**

| | |
|---|---|
| Target | Orthobunyavirus ([taxid 11572](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11572)) |
| Gene | M segment |
| Chemistry | conventional |
| Amplicon | — |
| Designed | 2007 |
| Paper | [10.1007/s00705-007-1069-z](https://doi.org/10.1007/s00705-007-1069-z) |
| Registry status | active |

!!! quote "The paper"
    Briese, T., Kapoor, V. & Lipkin, W. I. Natural M-segment reassortment in Potosi and Main Drain viruses: implications for the evolution of orthobunyaviruses. Archives of Virology 152, 2237-2247 (2007).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `TCNAARGGHTGYGGNAATGT` | 20 nt |
| reverse | `CGCGCCAGTAGTGTGCTACC` | 20 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (48 months, from Oct 2022) | 12 | 20 | 60.0% | 38.7% – 78.1% |
| baseline (everything earlier) | 87 | 207 | 42.0% | 35.5% – 48.8% |

Change from baseline, Newcombe interval: **-4.4% to 37.2%**. Threshold: **90.0%**.

*detected share 60.0% (39%-78%) since Oct 2022, upper bound below the 90% threshold; change from baseline -4% to +37% (no measurable fall from a baseline of 42%) (window widened to 48 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=0.104, 29 years); by footprint rising (p=0.529); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="f52e6608-f1ed-4af0-b29a-2f019677ae68" data-root-id="p20938" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"31400a10-51a8-42a5-a476-3f4b63f84251":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20993","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20994"}}},"roots":[{"type":"object","name":"Figure","id":"p20938","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p20940"},"y_range":{"type":"object","name":"Range1d","id":"p20947","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p20948"},"y_scale":{"type":"object","name":"LinearScale","id":"p20949"},"title":{"type":"object","name":"Title","id":"p20945","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20983","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20935","attributes":{"selected":{"type":"object","name":"Selection","id":"p20936","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20937"},"data":{"type":"map","entries":[["year",[1989,1993,1995,1996,1998,1999,2000,2001,2002,2003,2004,2007,2009,2010,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,50.0,100.0,0.0,100.0,100.0,100.0,80.0,66.66666666666666,66.66666666666666,20.0,0.0,33.33333333333333,75.0,50.0,80.0,31.03448275862069,15.0,33.33333333333333,55.172413793103445,23.076923076923077,50.0,14.285714285714285,54.54545454545454,50.0,50.0,55.55555555555556,50.0,100.0]],["detected",[1,1,2,0,4,1,7,4,2,4,1,0,2,3,1,4,9,3,7,16,3,5,1,6,2,3,5,1,1]],["evaluable",[1,2,2,7,4,1,7,5,3,6,5,5,6,4,2,5,29,20,21,29,13,10,7,11,4,6,9,2,1]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent","recent"]],["size",[8.703135093227193,9.07684386569143,9.07684386569143,9.897626379762722,9.517227179437622,8.703135093227193,9.897626379762722,9.667366891029102,9.328625426046248,9.791719296345839,9.667366891029102,9.667366891029102,9.791719296345839,9.517227179437622,9.07684386569143,9.667366891029102,10.869436534339137,10.619414831097462,10.652487636092928,10.869436534339137,10.324834530005162,10.143865699252444,9.897626379762722,10.209683151927734,9.517227179437622,9.791719296345839,10.071067811865476,9.07684386569143,8.703135093227193]]]}}},"view":{"type":"object","name":"CDSView","id":"p20984","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20985"}}},"glyph":{"type":"object","name":"Line","id":"p20980","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p20981","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p20982","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p20989","attributes":{"data_source":{"id":"p20935"},"view":{"type":"object","name":"CDSView","id":"p20990","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20991"}}},"glyph":{"type":"object","name":"Scatter","id":"p20986","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p20987","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p20988","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20946","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20960"},{"type":"object","name":"BoxZoomTool","id":"p20961","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20962","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20968","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20967","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20969","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20970"},{"type":"object","name":"SaveTool","id":"p20971"},{"type":"object","name":"HoverTool","id":"p20992","attributes":{"renderers":[{"id":"p20989"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p20955","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20956","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20957"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20958"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20950","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20951","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20952"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20953"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20954","attributes":{"axis":{"id":"p20950"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20959","attributes":{"dimension":1,"axis":{"id":"p20955"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p20972","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2021.5,"right":{"type":"object","name":"Node","id":"p20974","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p20975","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p20976","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p20978","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20977","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p20979","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"31400a10-51a8-42a5-a476-3f4b63f84251","roots":{"p20938":"f52e6608-f1ed-4af0-b29a-2f019677ae68"},"root_ids":["p20938"]}];
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

<div id="d49bc064-724b-439a-a3db-b4428b662d53" data-root-id="p20998" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"80783532-e2d4-4c8a-9f2f-3c49b99b8bef":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p21038","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p21039"}}},"roots":[{"type":"object","name":"Figure","id":"p20998","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p20999"},"y_range":{"type":"object","name":"DataRange1d","id":"p21000","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p21007"},"y_scale":{"type":"object","name":"LinearScale","id":"p21008"},"title":{"type":"object","name":"Title","id":"p21005","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p21034","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20995","attributes":{"selected":{"type":"object","name":"Selection","id":"p20996","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20997"},"data":{"type":"map","entries":[["year",[1989,1993,1995,1996,1998,1999,2000,2001,2002,2003,2004,2007,2009,2010,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,2,2,7,4,1,7,5,3,6,5,5,6,4,2,5,29,20,21,29,13,10,7,11,4,6,9,2,1]],["detected",[1,1,2,0,4,1,7,4,2,4,1,0,2,3,1,4,9,3,7,16,3,5,1,6,2,3,5,1,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p21035","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p21036"}}},"glyph":{"type":"object","name":"VBar","id":"p21031","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p21032","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p21033","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p21006","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p21019"},{"type":"object","name":"BoxZoomTool","id":"p21020","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p21021","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p21027","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p21026","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p21028","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p21029"},{"type":"object","name":"SaveTool","id":"p21030"},{"type":"object","name":"HoverTool","id":"p21037","attributes":{"renderers":[{"id":"p21034"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p21014","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p21015","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21016"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21017"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p21009","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p21010","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21011"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21012"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p21013","attributes":{"axis":{"id":"p21009"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p21018","attributes":{"dimension":1,"axis":{"id":"p21014"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"80783532-e2d4-4c8a-9f2f-3c49b99b8bef","roots":{"p20998":"d49bc064-724b-439a-a3db-b4428b662d53"},"root_ids":["p20998"]}];
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

<div id="ee663441-0036-4953-b8f0-3934f0289b27" data-root-id="p21043" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9570b9ac-9d0a-430a-b222-0659ed901511":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p21085","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p21086"}}},"roots":[{"type":"object","name":"Figure","id":"p21043","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p21045"},"y_range":{"type":"object","name":"FactorRange","id":"p21052","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p21053"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p21054"},"title":{"type":"object","name":"Title","id":"p21050","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p21080","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p21040","attributes":{"selected":{"type":"object","name":"Selection","id":"p21041","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p21042"},"data":{"type":"map","entries":[["x",[-3,-1,-2,-5,-8,-11,-7,-14,-2,-16,-4,-19,-10,-8,-13,-6,-3,-1,-11,-13,-14,-17,-20]],["y",["reverse","reverse","reverse","forward","reverse","forward","forward","forward","forward","forward","forward","forward","forward","forward","forward","reverse","forward","forward","reverse","reverse","reverse","forward","forward"]],["alpha",[1.0,0.9288546255506608,0.4495594713656388,0.6742290748898678,0.6143171806167401,0.4645374449339207,0.7790748898678413,1.0,1.0,0.5693832599118943,0.6742290748898678,1.0,1.0,1.0,1.0,0.9887665198237886,0.7790748898678413,0.7341409691629956,0.4645374449339207,0.629295154185022,0.6592511013215859,1.0,1.0]],["pos",[3,1,2,5,8,11,7,14,2,16,4,19,10,8,13,6,3,1,11,13,14,17,20]],["base",["A","C","C","A","G","T","G","G","G","A","A","C","G","G","G","G","T","T","A","G","A","A","T"]],["n",[59,52,20,35,31,21,42,57,84,28,35,87,63,70,84,56,42,39,21,32,34,76,58]],["det_with",["2% of 59","0% of 52","0% of 20","6% of 35","6% of 31","14% of 21","19% of 42","23% of 57","29% of 84","25% of 28","29% of 35","33% of 87","32% of 63","34% of 70","38% of 84","38% of 56","43% of 42","44% of 39","48% of 21","50% of 32","50% of 34","49% of 76","52% of 58"]],["det_without",["58% of 168","57% of 175","48% of 207","51% of 192","49% of 196","47% of 206","49% of 185","51% of 170","52% of 143","46% of 199","46% of 192","50% of 140","48% of 164","48% of 157","47% of 143","46% of 171","44% of 185","44% of 188","43% of 206","43% of 195","42% of 193","41% of 151","41% of 169"]],["subs",["A&gt;C 52, A&gt;G 5, A&gt;T 2","C&gt;A 33, C&gt;T 12, C&gt;G 7","C&gt;T 12, C&gt;A 8","A&gt;T 15, A&gt;G 11, A&gt;C 9","G&gt;A 20, G&gt;C 8, G&gt;T 3","T&gt;A 12, T&gt;G 5, T&gt;C 4","G&gt;C 16, G&gt;T 14, G&gt;A 12","G&gt;T 39, G&gt;A 16, G&gt;C 2","G&gt;A 60, G&gt;T 17, G&gt;C 7","A&gt;C 12, A&gt;T 11, A&gt;G 5","A&gt;G 20, A&gt;T 9, A&gt;C 6","C&gt;A 31, C&gt;T 29, C&gt;G 27","G&gt;A 48, G&gt;T 10, G&gt;C 5","G&gt;T 33, G&gt;A 32, G&gt;C 5","G&gt;T 50, G&gt;A 24, G&gt;C 10","G&gt;A 30, G&gt;T 20, G&gt;C 6","T&gt;C 21, T&gt;A 12, T&gt;G 9","T&gt;C 24, T&gt;A 8, T&gt;G 7","A&gt;T 20, A&gt;G 1","G&gt;T 29, G&gt;C 2, G&gt;A 1","A&gt;T 19, A&gt;G 15","A&gt;C 75, A&gt;T 1","T&gt;G 27, T&gt;A 19, T&gt;C 12"]],["zone",["yes","yes","yes","yes","no","no","no","no","yes","no","yes","no","no","no","no","no","yes","yes","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p21081","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p21082"}}},"glyph":{"type":"object","name":"Rect","id":"p21077","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p21078","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p21079","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p21051","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p21065"},{"type":"object","name":"BoxZoomTool","id":"p21066","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p21067","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p21073","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p21072","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p21074","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p21075"},{"type":"object","name":"SaveTool","id":"p21076"},{"type":"object","name":"HoverTool","id":"p21083","attributes":{"renderers":[{"id":"p21080"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p21060","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p21061"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p21062"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p21063"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p21055","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p21084","attributes":{"ticks":[-20,-19,-17,-16,-14,-13,-11,-10,-8,-7,-6,-5,-4,-3,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p21057"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-3,"3"],[-1,"1"],[-2,"2"],[-5,"5"],[-8,"8"],[-11,"11"],[-7,"7"],[-14,"14"],[-16,"16"],[-4,"4"],[-19,"19"],[-10,"10"],[-13,"13"],[-6,"6"],[-17,"17"],[-20,"20"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p21058"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p21059","attributes":{"axis":{"id":"p21055"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p21064","attributes":{"dimension":1,"axis":{"id":"p21060"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9570b9ac-9d0a-430a-b222-0659ed901511","roots":{"p21043":"ee663441-0036-4953-b8f0-3934f0289b27"},"root_ids":["p21043"]}];
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
S[Gene] OR M[Gene] OR "S segment"[Title] OR "M segment"[Title] OR nucleocapsid[Title] OR glycoprotein[Title] OR "complete genome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `amplicon_multimodal`.


## What reached the statistics

2,083 records were screened for this assay and **227 (11%)** were evaluable, meaning both primers landed in the right orientation and size range. 1,856 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `chance_only` | 1,428 |
| `no_site` | 408 |
| `chance_anchor` | 20 |

