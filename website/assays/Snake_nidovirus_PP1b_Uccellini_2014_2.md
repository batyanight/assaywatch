# Snake_nidovirus_PP1b_Uccellini_2014_2

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**NIDOVIRUS (ssRNA)-SNAKE — PP1b**

| | |
|---|---|
| Target | Serpentovirinae (snake nidoviruses, Tobaniviridae) ([taxid 2508240](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=2508240)) |
| Gene | PP1b |
| Chemistry | conventional |
| Amplicon | 1694 bp |
| Designed | 2014 |
| Paper | [10.1186/1743-422X-11-144](https://doi.org/10.1186/1743-422X-11-144) |
| Registry status | active |

!!! quote "The paper"
    Uccellini L et al. 2014. Virol J 11:144

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GTGACTACACGAAATGCGACC` | 21 nt |
| reverse | `ACGTAGTCTTGCCAGTTCCC` | 20 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (36 months, from Oct 2023) | 1 | 23 | 4.3% | 0.8% – 21.0% |
| baseline (everything earlier) | 5 | 37 | 13.5% | 5.9% – 28.0% |

Change from baseline, Newcombe interval: **-24.1% to 9.1%**. Threshold: **90.0%**.

*detected share 4.3% (0.8%-21%) since Oct 2023, upper bound below the 90% threshold; change from baseline -24% to +9% (no measurable fall from a baseline of 14%) (window widened to 36 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=0.00913, 10 years); by footprint falling (p=0.315). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="f2b4f6dc-525c-468a-86de-e095c9ebaba3" data-root-id="p32962" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"a5376399-f786-4bf1-9b6e-c9b8361e7cb3":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p33017","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p33018"}}},"roots":[{"type":"object","name":"Figure","id":"p32962","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p32964"},"y_range":{"type":"object","name":"Range1d","id":"p32971","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p32972"},"y_scale":{"type":"object","name":"LinearScale","id":"p32973"},"title":{"type":"object","name":"Title","id":"p32969","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p33007","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p32959","attributes":{"selected":{"type":"object","name":"Selection","id":"p32960","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p32961"},"data":{"type":"map","entries":[["year",[2014,2016,2017,2018,2019,2020,2023,2024,2025,2026]],["share",[100.0,0.0,0.0,33.33333333333333,5.88235294117647,0.0,0.0,0.0,0.0,33.33333333333333]],["detected",[3,0,0,1,1,0,0,0,0,1]],["evaluable",[3,3,3,3,17,4,4,16,4,3]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent"]],["size",[9.328625426046248,9.328625426046248,9.328625426046248,9.328625426046248,10.508782366508077,9.517227179437622,9.517227179437622,10.467343773689333,9.517227179437622,9.328625426046248]]]}}},"view":{"type":"object","name":"CDSView","id":"p33008","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33009"}}},"glyph":{"type":"object","name":"Line","id":"p33004","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p33005","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p33006","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p33013","attributes":{"data_source":{"id":"p32959"},"view":{"type":"object","name":"CDSView","id":"p33014","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33015"}}},"glyph":{"type":"object","name":"Scatter","id":"p33010","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p33011","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p33012","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p32970","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p32984"},{"type":"object","name":"BoxZoomTool","id":"p32985","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p32986","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p32992","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p32991","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p32993","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p32994"},{"type":"object","name":"SaveTool","id":"p32995"},{"type":"object","name":"HoverTool","id":"p33016","attributes":{"renderers":[{"id":"p33013"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p32979","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p32980","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p32981"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p32982"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p32974","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p32975","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p32976"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p32977"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p32978","attributes":{"axis":{"id":"p32974"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p32983","attributes":{"dimension":1,"axis":{"id":"p32979"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p32996","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2022.5,"right":{"type":"object","name":"Node","id":"p32998","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p32999","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p33000","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p33002","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33001","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p33003","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"a5376399-f786-4bf1-9b6e-c9b8361e7cb3","roots":{"p32962":"f2b4f6dc-525c-468a-86de-e095c9ebaba3"},"root_ids":["p32962"]}];
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

<div id="fb25cdf7-2de0-40ee-aa30-4a0b76ca3aba" data-root-id="p33022" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"450e06ed-0217-4471-bc93-77aba899f615":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p33062","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p33063"}}},"roots":[{"type":"object","name":"Figure","id":"p33022","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p33023"},"y_range":{"type":"object","name":"DataRange1d","id":"p33024","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p33031"},"y_scale":{"type":"object","name":"LinearScale","id":"p33032"},"title":{"type":"object","name":"Title","id":"p33029","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p33058","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p33019","attributes":{"selected":{"type":"object","name":"Selection","id":"p33020","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p33021"},"data":{"type":"map","entries":[["year",[2014,2016,2017,2018,2019,2020,2023,2024,2025,2026]],["evaluable",[3,3,3,3,17,4,4,16,4,3]],["detected",[3,0,0,1,1,0,0,0,0,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p33059","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33060"}}},"glyph":{"type":"object","name":"VBar","id":"p33055","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p33056","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p33057","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p33030","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p33043"},{"type":"object","name":"BoxZoomTool","id":"p33044","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p33045","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p33051","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33050","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p33052","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p33053"},{"type":"object","name":"SaveTool","id":"p33054"},{"type":"object","name":"HoverTool","id":"p33061","attributes":{"renderers":[{"id":"p33058"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p33038","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33039","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33040"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33041"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p33033","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33034","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33035"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33036"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p33037","attributes":{"axis":{"id":"p33033"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p33042","attributes":{"dimension":1,"axis":{"id":"p33038"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"450e06ed-0217-4471-bc93-77aba899f615","roots":{"p33022":"fb25cdf7-2de0-40ee-aa30-4a0b76ca3aba"},"root_ids":["p33022"]}];
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

<div id="fcdb610d-72c7-4434-b513-1bc225f5c084" data-root-id="p33067" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"c2bc284a-5436-43df-ae44-de21026eac75":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p33109","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p33110"}}},"roots":[{"type":"object","name":"Figure","id":"p33067","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p33069"},"y_range":{"type":"object","name":"FactorRange","id":"p33076","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p33077"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p33078"},"title":{"type":"object","name":"Title","id":"p33074","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p33104","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p33064","attributes":{"selected":{"type":"object","name":"Selection","id":"p33065","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p33066"},"data":{"type":"map","entries":[["x",[-11,-1,-16,-19,-7,-14,-20,-4,-5,-8]],["y",["forward","reverse","reverse","reverse","reverse","forward","forward","reverse","forward","forward"]],["alpha",[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]],["pos",[11,1,16,19,7,14,20,4,5,8]],["base",["G","C","A","C","A","C","T","T","C","A"]],["n",[49,49,39,38,36,37,23,21,28,22]],["det_with",["0% of 49","0% of 49","0% of 39","0% of 38","0% of 36","3% of 37","0% of 23","0% of 21","4% of 28","5% of 22"]],["det_without",["86% of 7","86% of 7","35% of 17","33% of 18","30% of 20","26% of 19","18% of 33","17% of 35","18% of 28","15% of 34"]],["subs",["G&gt;C 28, G&gt;A 12, G&gt;T 9","C&gt;T 41, C&gt;A 8","A&gt;T 22, A&gt;G 14, A&gt;C 3","C&gt;T 26, C&gt;G 7, C&gt;A 5","A&gt;G 32, A&gt;T 4","C&gt;T 37","T&gt;C 21, T&gt;A 2","T&gt;A 13, T&gt;G 8","C&gt;T 28","A&gt;G 22"]],["zone",["no","yes","no","no","no","no","no","yes","yes","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p33105","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33106"}}},"glyph":{"type":"object","name":"Rect","id":"p33101","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p33102","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p33103","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p33075","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p33089"},{"type":"object","name":"BoxZoomTool","id":"p33090","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p33091","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p33097","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33096","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p33098","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p33099"},{"type":"object","name":"SaveTool","id":"p33100"},{"type":"object","name":"HoverTool","id":"p33107","attributes":{"renderers":[{"id":"p33104"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p33084","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p33085"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p33086"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33087"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p33079","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p33108","attributes":{"ticks":[-20,-19,-16,-14,-11,-8,-7,-5,-4,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33081"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-11,"11"],[-1,"1"],[-16,"16"],[-19,"19"],[-7,"7"],[-14,"14"],[-20,"20"],[-4,"4"],[-5,"5"],[-8,"8"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p33082"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p33083","attributes":{"axis":{"id":"p33079"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p33088","attributes":{"dimension":1,"axis":{"id":"p33084"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"c2bc284a-5436-43df-ae44-de21026eac75","roots":{"p33067":"fcdb610d-72c7-4434-b513-1bc225f5c084"},"root_ids":["p33067"]}];
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

Disclosures on this entry: `pairing_is_curator_reading`.


## What reached the statistics

279 records were screened for this assay and **60 (22%)** were evaluable, meaning both primers landed in the right orientation and size range. 219 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 151 |
| `truncated` | 56 |
| `chance_anchor` | 12 |

