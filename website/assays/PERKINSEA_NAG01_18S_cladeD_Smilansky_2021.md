# PERKINSEA_NAG01_18S_cladeD_Smilansky_2021

<span class="aw-chip aw-chip-no-recent-data">no recent data</span>

**PERKINSEA NAG01 Clade D (pathogenic) — 18S duplex qPCR, PPC probe (Smilansky 2021)**

| | |
|---|---|
| Target | Perkinsea (NAG01) ([taxid 27997](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=27997)) |
| Gene | 18S rRNA |
| Chemistry | hydrolysis_probe |
| Amplicon | 287 bp |
| Designed | 2021 |
| Paper | [10.1098/rsos.202150](https://doi.org/10.1098/rsos.202150) |
| Registry status | active |

!!! quote "The paper"
    Smilansky, V., Chambouvet, A., Reeves, M., Richards, T. A. & Milner, D. S. A novel duplex qPCR assay for stepwise detection of multiple Perkinsea protistan infections of amphibian tissues. Royal Society Open Science 8, 202150 (2021).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GGGCTTCAYAGTCTTGCAAT` | 20 nt |
| reverse | `GCCTGCTTGAAACRCTCTAA` | 20 nt |
| probe | `TGCCAAGAACGACCGTCCTAC` | 21 nt |

## The verdict, and the numbers behind it

**no recent data** — nothing was deposited in the window

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 0 | 0 | — | 0.0% – 100.0% |
| baseline (everything earlier) | 166 | 391 | 42.5% | 37.7% – 47.4% |

Change from baseline, Newcombe interval: **-100.0% to 100.0%**. Threshold: **90.0%**.

*no evaluable records deposited since Oct 2021 (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record rising (p=2.11e-53, 5 years); by footprint rising (p=0.00337). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="a849ec33-053b-471d-918e-a1c20036d572" data-root-id="p23245" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"0486e82b-a48a-487c-97e5-77c41dfe1342":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p23300","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p23301"}}},"roots":[{"type":"object","name":"Figure","id":"p23245","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p23247"},"y_range":{"type":"object","name":"Range1d","id":"p23254","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p23255"},"y_scale":{"type":"object","name":"LinearScale","id":"p23256"},"title":{"type":"object","name":"Title","id":"p23252","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p23290","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p23242","attributes":{"selected":{"type":"object","name":"Selection","id":"p23243","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p23244"},"data":{"type":"map","entries":[["year",[2010,2015,2017,2019,2021]],["share",[0.0,1.7777777777777777,100.0,0.0,97.22222222222221]],["detected",[0,4,92,0,70]],["evaluable",[1,225,92,1,72]],["window",["baseline","baseline","baseline","baseline","recent"]],["size",[8.703135093227193,12.157112589604052,11.614642982378804,8.703135093227193,11.460677957646856]]]}}},"view":{"type":"object","name":"CDSView","id":"p23291","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p23292"}}},"glyph":{"type":"object","name":"Line","id":"p23287","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p23288","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p23289","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p23296","attributes":{"data_source":{"id":"p23242"},"view":{"type":"object","name":"CDSView","id":"p23297","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p23298"}}},"glyph":{"type":"object","name":"Scatter","id":"p23293","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p23294","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p23295","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p23253","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p23267"},{"type":"object","name":"BoxZoomTool","id":"p23268","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p23269","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p23275","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p23274","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p23276","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p23277"},{"type":"object","name":"SaveTool","id":"p23278"},{"type":"object","name":"HoverTool","id":"p23299","attributes":{"renderers":[{"id":"p23296"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p23262","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23263","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23264"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23265"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p23257","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23258","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23259"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23260"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p23261","attributes":{"axis":{"id":"p23257"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p23266","attributes":{"dimension":1,"axis":{"id":"p23262"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p23279","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2020.5,"right":{"type":"object","name":"Node","id":"p23281","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p23282","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p23283","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p23285","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p23284","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p23286","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"0486e82b-a48a-487c-97e5-77c41dfe1342","roots":{"p23245":"a849ec33-053b-471d-918e-a1c20036d572"},"root_ids":["p23245"]}];
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

<div id="d9cbcb62-965c-4743-91b9-90625ed5e0a9" data-root-id="p23305" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"6e270e18-dc39-44ec-b967-dfefccd92b2d":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p23345","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p23346"}}},"roots":[{"type":"object","name":"Figure","id":"p23305","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p23306"},"y_range":{"type":"object","name":"DataRange1d","id":"p23307","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p23314"},"y_scale":{"type":"object","name":"LinearScale","id":"p23315"},"title":{"type":"object","name":"Title","id":"p23312","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p23341","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p23302","attributes":{"selected":{"type":"object","name":"Selection","id":"p23303","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p23304"},"data":{"type":"map","entries":[["year",[2010,2015,2017,2019,2021]],["evaluable",[1,225,92,1,72]],["detected",[0,4,92,0,70]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p23342","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p23343"}}},"glyph":{"type":"object","name":"VBar","id":"p23338","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p23339","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p23340","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p23313","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p23326"},{"type":"object","name":"BoxZoomTool","id":"p23327","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p23328","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p23334","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p23333","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p23335","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p23336"},{"type":"object","name":"SaveTool","id":"p23337"},{"type":"object","name":"HoverTool","id":"p23344","attributes":{"renderers":[{"id":"p23341"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p23321","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23322","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23323"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23324"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p23316","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23317","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23318"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23319"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p23320","attributes":{"axis":{"id":"p23316"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p23325","attributes":{"dimension":1,"axis":{"id":"p23321"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"6e270e18-dc39-44ec-b967-dfefccd92b2d","roots":{"p23305":"d9cbcb62-965c-4743-91b9-90625ed5e0a9"},"root_ids":["p23305"]}];
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

<div id="b959adb8-cc89-4c69-9cb1-1ff069ad3921" data-root-id="p23350" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"13be2295-64c1-4cb7-bc0d-a331ce2465a9":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p23392","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p23393"}}},"roots":[{"type":"object","name":"Figure","id":"p23350","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p23352"},"y_range":{"type":"object","name":"FactorRange","id":"p23359","attributes":{"factors":["probe","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p23360"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p23361"},"title":{"type":"object","name":"Title","id":"p23357","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p23387","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p23347","attributes":{"selected":{"type":"object","name":"Selection","id":"p23348","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p23349"},"data":{"type":"map","entries":[["x",[-3,-14,-6,-7,-14,-11,-16,-4,-13,-15]],["y",["probe","probe","probe","probe","forward","forward","forward","forward","forward","forward"]],["alpha",[1.0,1.0,1.0,1.0,0.8630434782608696,0.8195652173913044,0.8195652173913044,0.7847826086956522,0.7847826086956522,0.7847826086956522]],["pos",[3,14,6,7,14,11,16,4,13,15]],["base",["T","A","T","G","C","A","T","C","A","T"]],["n",[215,215,216,212,82,77,77,73,73,73]],["det_with",["0% of 215","0% of 215","0% of 216","0% of 212","0% of 82","0% of 77","0% of 77","0% of 73","0% of 73","0% of 73"]],["det_without",["67% of 249","67% of 249","67% of 248","66% of 252","43% of 382","43% of 387","43% of 387","42% of 391","42% of 391","42% of 391"]],["subs",["T&gt;C 214, T&gt;A 1","A&gt;G 215","T&gt;A 213, T&gt;G 2, T&gt;C 1","G&gt;T 211, G&gt;A 1","C&gt;T 81, C&gt;A 1","A&gt;T 77","T&gt;A 76, T&gt;C 1","C&gt;T 73","A&gt;T 69, A&gt;C 4","T&gt;A 72, T&gt;C 1"]],["zone",["yes","no","no","no","no","no","no","yes","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p23388","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p23389"}}},"glyph":{"type":"object","name":"Rect","id":"p23384","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p23385","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p23386","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p23358","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p23372"},{"type":"object","name":"BoxZoomTool","id":"p23373","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p23374","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p23380","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p23379","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p23381","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p23382"},{"type":"object","name":"SaveTool","id":"p23383"},{"type":"object","name":"HoverTool","id":"p23390","attributes":{"renderers":[{"id":"p23387"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p23367","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p23368"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p23369"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23370"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p23362","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p23391","attributes":{"ticks":[-16,-15,-14,-13,-11,-7,-6,-4,-3],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23364"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-3,"3"],[-14,"14"],[-6,"6"],[-7,"7"],[-11,"11"],[-16,"16"],[-4,"4"],[-13,"13"],[-15,"15"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p23365"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p23366","attributes":{"axis":{"id":"p23362"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p23371","attributes":{"dimension":1,"axis":{"id":"p23367"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"13be2295-64c1-4cb7-bc0d-a331ce2465a9","roots":{"p23350":"b959adb8-cc89-4c69-9cb1-1ff069ad3921"},"root_ids":["p23350"]}];
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

This entry declares **`scope_taxids`**: [373149](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=373149). A record counts toward the denominator when its taxid, or any ancestor, is in that set. Records outside it are screened and reported but kept out of the statistics.

1,389 screened records fell outside the declared scope.

Retrieval query:

```
18S[Title] OR "small subunit"[Title] OR "ribosomal RNA"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `retrieval_scope_incomplete`, `oligos_from_secondary_source`.


## What reached the statistics

537 records were screened for this assay and **391 (73%)** were evaluable, meaning both primers landed in the right orientation and size range. 146 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `truncated` | 145 |
| `no_site` | 1 |

