# Helicobacter_16S_Conley_2021

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**Helicobacter — 16S rRNA qPCR (Helico New F/R + PROBE1)**

| | |
|---|---|
| Target | Helicobacter ([taxid 209](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=209)) |
| Gene | 16S rRNA |
| Chemistry | mgb |
| Amplicon | 191 bp |
| Designed | 2021 |
| Paper | [10.1371/journal.pone.0247010](https://doi.org/10.1371/journal.pone.0247010) |
| Registry status | active |

!!! quote "The paper"
    Conley KJ et al. 2021. Systemic Helicobacter infection and associated mortalities in endangered Grand Cayman blue iguanas (Cyclura lewisi) and introduced green iguanas (Iguana iguana). PLoS One 16:e0247010

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `TAGATAACATGCCCTTTAGTCTGGGATAGCCA` | 32 nt |
| reverse | `GTGTGTCCGTTCACCCTCTCAGG` | 23 nt |
| probe | `CTGGATACTCCCCAAGGGGATACC` | 24 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 0 | 75 | 0.0% | 0.0% – 4.9% |
| baseline (everything earlier) | 0 | 1,080 | 0.0% | 0.0% – 0.4% |

Change from baseline, Newcombe interval: **-0.4% to 4.9%**. Threshold: **90.0%**.

*detected share 0.0% (0%-5%) since Oct 2024, upper bound below the 90% threshold; change from baseline -0.4% to +5% (no measurable fall from a baseline of 0%)*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="b19521b4-4be9-41d3-96a3-bc011db17b32" data-root-id="p13439" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"3bd291aa-e0be-427b-b4f5-7d8570b15d6e":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p13494","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p13495"}}},"roots":[{"type":"object","name":"Figure","id":"p13439","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p13441"},"y_range":{"type":"object","name":"Range1d","id":"p13448","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p13449"},"y_scale":{"type":"object","name":"LinearScale","id":"p13450"},"title":{"type":"object","name":"Title","id":"p13446","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p13484","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p13436","attributes":{"selected":{"type":"object","name":"Selection","id":"p13437","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p13438"},"data":{"type":"map","entries":[["year",[1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]],["detected",[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],["evaluable",[11,31,5,2,8,18,10,20,26,34,46,25,59,64,21,22,48,24,202,22,14,52,36,16,19,21,12,23,16,85,44,33,14,20,52]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[10.209683151927734,10.913832791890265,9.667366891029102,9.07684386569143,9.989711205477885,10.547770533331066,10.143865699252444,10.619414831097462,10.796415465069488,10.975067467348278,11.173276359477448,10.770092258092593,11.333893523413357,11.385871088686695,10.652487636092928,10.683957047019447,11.200908608240482,10.74264168206181,12.093261293278134,10.683957047019447,10.37579022724969,11.252690272875853,11.012804945939648,10.467343773689333,10.584573151575475,10.652487636092928,10.269703144398052,10.713966621835368,10.467343773689333,11.56518892267352,11.144342382561259,10.955310988645032,10.37579022724969,10.619414831097462,11.252690272875853]]]}}},"view":{"type":"object","name":"CDSView","id":"p13485","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13486"}}},"glyph":{"type":"object","name":"Line","id":"p13481","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p13482","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p13483","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p13490","attributes":{"data_source":{"id":"p13436"},"view":{"type":"object","name":"CDSView","id":"p13491","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13492"}}},"glyph":{"type":"object","name":"Scatter","id":"p13487","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p13488","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p13489","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p13447","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p13461"},{"type":"object","name":"BoxZoomTool","id":"p13462","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p13463","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p13469","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13468","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p13470","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p13471"},{"type":"object","name":"SaveTool","id":"p13472"},{"type":"object","name":"HoverTool","id":"p13493","attributes":{"renderers":[{"id":"p13490"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p13456","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13457","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13458"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13459"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p13451","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13452","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13453"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13454"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p13455","attributes":{"axis":{"id":"p13451"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p13460","attributes":{"dimension":1,"axis":{"id":"p13456"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p13473","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p13475","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p13476","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p13477","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p13479","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13478","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p13480","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"3bd291aa-e0be-427b-b4f5-7d8570b15d6e","roots":{"p13439":"b19521b4-4be9-41d3-96a3-bc011db17b32"},"root_ids":["p13439"]}];
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

<div id="f22fee90-9502-4484-b108-33cb368aefc8" data-root-id="p13499" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"619223e8-d3e7-4dae-9883-9ea7c4666c3f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p13539","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p13540"}}},"roots":[{"type":"object","name":"Figure","id":"p13499","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p13500"},"y_range":{"type":"object","name":"DataRange1d","id":"p13501","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p13508"},"y_scale":{"type":"object","name":"LinearScale","id":"p13509"},"title":{"type":"object","name":"Title","id":"p13506","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p13535","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p13496","attributes":{"selected":{"type":"object","name":"Selection","id":"p13497","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p13498"},"data":{"type":"map","entries":[["year",[1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[11,31,5,2,8,18,10,20,26,34,46,25,59,64,21,22,48,24,202,22,14,52,36,16,19,21,12,23,16,85,44,33,14,20,52]],["detected",[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p13536","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13537"}}},"glyph":{"type":"object","name":"VBar","id":"p13532","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p13533","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p13534","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p13507","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p13520"},{"type":"object","name":"BoxZoomTool","id":"p13521","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p13522","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p13528","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13527","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p13529","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p13530"},{"type":"object","name":"SaveTool","id":"p13531"},{"type":"object","name":"HoverTool","id":"p13538","attributes":{"renderers":[{"id":"p13535"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p13515","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13516","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13517"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13518"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p13510","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13511","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13512"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13513"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p13514","attributes":{"axis":{"id":"p13510"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p13519","attributes":{"dimension":1,"axis":{"id":"p13515"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"619223e8-d3e7-4dae-9883-9ea7c4666c3f","roots":{"p13499":"f22fee90-9502-4484-b108-33cb368aefc8"},"root_ids":["p13499"]}];
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

<div id="ab8a51a2-a3e9-4efa-a9ec-4e7fa6ee8875" data-root-id="p13544" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"4b5ed0c3-0ba9-4f1e-9c07-3f4cc38b887d":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p13586","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p13587"}}},"roots":[{"type":"object","name":"Figure","id":"p13544","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p13546"},"y_range":{"type":"object","name":"FactorRange","id":"p13553","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p13554"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p13555"},"title":{"type":"object","name":"Title","id":"p13551","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p13581","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p13541","attributes":{"selected":{"type":"object","name":"Selection","id":"p13542","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p13543"},"data":{"type":"map","entries":[["x",[-29,-27,-25,-14,-24,-1,-2,-12,-4,-10,-5,-12,-18,-17,-10,-8,-22,-19]],["y",["forward","forward","forward","reverse","forward","probe","probe","probe","probe","probe","probe","forward","forward","forward","forward","forward","forward","forward"]],["alpha",[1.0,1.0,1.0,1.0,1.0,0.8388311688311689,0.8388311688311689,0.8388311688311689,0.8358874458874459,0.8358874458874459,0.8182251082251082,0.7151948051948052,0.6680952380952382,0.6268831168831168,0.48558441558441556,0.3119047619047619,0.2441991341991342,0.20887445887445888]],["pos",[29,27,25,14,24,1,2,12,4,10,5,12,18,17,10,8,22,19]],["base",["A","A","C","T","A","C","C","C","T","A","A","C","T","T","G","G","G","C"]],["n",[512,453,397,361,343,234,234,234,233,233,227,192,176,162,114,55,32,20]],["det_with",["0% of 512","0% of 453","0% of 397","0% of 361","0% of 343","0% of 234","0% of 234","0% of 234","0% of 233","0% of 233","0% of 227","0% of 192","0% of 176","0% of 162","0% of 114","0% of 55","0% of 32","0% of 20"]],["det_without",["0% of 283","0% of 342","0% of 398","0% of 434","0% of 452","0% of 561","0% of 561","0% of 561","0% of 562","0% of 562","0% of 568","0% of 603","0% of 619","0% of 633","0% of 681","0% of 740","0% of 763","0% of 775"]],["subs",["A&gt;G 512","A&gt;T 335, A&gt;G 114, A&gt;C 4","C&gt;T 397","T&gt;A 338, T&gt;C 19, T&gt;G 3, T&gt;R 1","A&gt;G 342, A&gt;C 1","C&gt;G 232, C&gt;T 2","C&gt;A 230, C&gt;G 4","C&gt;T 234","T&gt;A 233","A&gt;C 227, A&gt;T 6","A&gt;G 227","C&gt;T 190, C&gt;A 2","T&gt;C 176","T&gt;A 162","G&gt;A 114","G&gt;A 55","G&gt;A 31, G&gt;C 1","C&gt;T 20"]],["zone",["no","no","no","no","no","yes","yes","no","yes","no","yes","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p13582","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13583"}}},"glyph":{"type":"object","name":"Rect","id":"p13578","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p13579","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p13580","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p13552","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p13566"},{"type":"object","name":"BoxZoomTool","id":"p13567","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p13568","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p13574","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13573","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p13575","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p13576"},{"type":"object","name":"SaveTool","id":"p13577"},{"type":"object","name":"HoverTool","id":"p13584","attributes":{"renderers":[{"id":"p13581"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p13561","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p13562"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p13563"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13564"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p13556","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p13585","attributes":{"ticks":[-29,-27,-25,-24,-22,-19,-18,-17,-14,-12,-10,-8,-5,-4,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13558"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-29,"29"],[-27,"27"],[-25,"25"],[-14,"14"],[-24,"24"],[-1,"1"],[-2,"2"],[-12,"12"],[-4,"4"],[-10,"10"],[-5,"5"],[-18,"18"],[-17,"17"],[-8,"8"],[-22,"22"],[-19,"19"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p13559"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p13560","attributes":{"axis":{"id":"p13556"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p13565","attributes":{"dimension":1,"axis":{"id":"p13561"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"4b5ed0c3-0ba9-4f1e-9c07-3f4cc38b887d","roots":{"p13544":"ab8a51a2-a3e9-4efa-a9ec-4e7fa6ee8875"},"root_ids":["p13544"]}];
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
("16S ribosomal RNA"[Title] OR "16S rRNA"[Title] OR 16S[Title]) AND 1:30000[SLEN] NOT "whole genome shotgun"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `cross_reactive`, `thin_evidence`, `scope_narrower_than_taxid`, `retrieval_scope_incomplete`, `amplicon_disagrees_with_paper`.


## What reached the statistics

3,025 records were screened for this assay and **1,155 (38%)** were evaluable, meaning both primers landed in the right orientation and size range. 1,870 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 1,110 |
| `truncated` | 616 |
| `no_pair` | 141 |
| `chance_anchor` | 3 |

