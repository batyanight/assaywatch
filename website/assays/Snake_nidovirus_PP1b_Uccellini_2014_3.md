# Snake_nidovirus_PP1b_Uccellini_2014_3

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**NIDOVIRUS (ssRNA)-SNAKE — PP1b**

| | |
|---|---|
| Target | Serpentovirinae (snake nidoviruses, Tobaniviridae) ([taxid 2508240](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=2508240)) |
| Gene | PP1b |
| Chemistry | conventional |
| Amplicon | 1059 bp |
| Designed | 2014 |
| Paper | [10.1186/1743-422X-11-144](https://doi.org/10.1186/1743-422X-11-144) |
| Registry status | active |

!!! quote "The paper"
    Uccellini L et al. 2014. Virol J 11:144

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ACCTGCTACCGATGTCCAAG` | 20 nt |
| reverse | `GTCGTTGTTGGCTGAGTGTG` | 20 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (36 months, from Oct 2023) | 3 | 17 | 17.6% | 6.2% – 41.0% |
| baseline (everything earlier) | 9 | 27 | 33.3% | 18.6% – 52.2% |

Change from baseline, Newcombe interval: **-37.7% to 11.9%**. Threshold: **90.0%**.

*detected share 17.6% (6%-41%) since Oct 2023, upper bound below the 90% threshold; change from baseline -38% to +12% (no measurable fall from a baseline of 33%) (window widened to 36 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=0.0165, 11 years); by footprint falling (p=0.0757). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="ea7a91d5-b813-4d74-95b3-64edae7b2243" data-root-id="p33114" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"88826b64-4be5-4e21-8ee6-c3709195ce68":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p33169","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p33170"}}},"roots":[{"type":"object","name":"Figure","id":"p33114","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p33116"},"y_range":{"type":"object","name":"Range1d","id":"p33123","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p33124"},"y_scale":{"type":"object","name":"LinearScale","id":"p33125"},"title":{"type":"object","name":"Title","id":"p33121","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p33159","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p33111","attributes":{"selected":{"type":"object","name":"Selection","id":"p33112","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p33113"},"data":{"type":"map","entries":[["year",[2014,2016,2017,2018,2019,2020,2021,2023,2024,2025,2026]],["share",[100.0,0.0,100.0,50.0,30.76923076923077,0.0,0.0,0.0,16.666666666666664,0.0,50.0]],["detected",[2,0,2,1,4,0,0,0,2,0,1]],["evaluable",[2,1,2,2,13,3,1,3,12,3,2]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent"]],["size",[9.07684386569143,8.703135093227193,9.07684386569143,9.07684386569143,10.324834530005162,9.328625426046248,8.703135093227193,9.328625426046248,10.269703144398052,9.328625426046248,9.07684386569143]]]}}},"view":{"type":"object","name":"CDSView","id":"p33160","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33161"}}},"glyph":{"type":"object","name":"Line","id":"p33156","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p33157","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p33158","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p33165","attributes":{"data_source":{"id":"p33111"},"view":{"type":"object","name":"CDSView","id":"p33166","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33167"}}},"glyph":{"type":"object","name":"Scatter","id":"p33162","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p33163","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p33164","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p33122","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p33136"},{"type":"object","name":"BoxZoomTool","id":"p33137","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p33138","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p33144","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33143","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p33145","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p33146"},{"type":"object","name":"SaveTool","id":"p33147"},{"type":"object","name":"HoverTool","id":"p33168","attributes":{"renderers":[{"id":"p33165"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p33131","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33132","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33133"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33134"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p33126","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33127","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33128"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33129"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p33130","attributes":{"axis":{"id":"p33126"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p33135","attributes":{"dimension":1,"axis":{"id":"p33131"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p33148","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2022.5,"right":{"type":"object","name":"Node","id":"p33150","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p33151","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p33152","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p33154","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33153","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p33155","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"88826b64-4be5-4e21-8ee6-c3709195ce68","roots":{"p33114":"ea7a91d5-b813-4d74-95b3-64edae7b2243"},"root_ids":["p33114"]}];
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

<div id="c0bdc8f9-cf79-47da-90c8-ade1bd58217e" data-root-id="p33174" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"1f153ecb-acb5-46de-8b99-acdc643fa9b9":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p33214","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p33215"}}},"roots":[{"type":"object","name":"Figure","id":"p33174","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p33175"},"y_range":{"type":"object","name":"DataRange1d","id":"p33176","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p33183"},"y_scale":{"type":"object","name":"LinearScale","id":"p33184"},"title":{"type":"object","name":"Title","id":"p33181","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p33210","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p33171","attributes":{"selected":{"type":"object","name":"Selection","id":"p33172","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p33173"},"data":{"type":"map","entries":[["year",[2014,2016,2017,2018,2019,2020,2021,2023,2024,2025,2026]],["evaluable",[2,1,2,2,13,3,1,3,12,3,2]],["detected",[2,0,2,1,4,0,0,0,2,0,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p33211","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33212"}}},"glyph":{"type":"object","name":"VBar","id":"p33207","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p33208","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p33209","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p33182","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p33195"},{"type":"object","name":"BoxZoomTool","id":"p33196","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p33197","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p33203","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33202","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p33204","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p33205"},{"type":"object","name":"SaveTool","id":"p33206"},{"type":"object","name":"HoverTool","id":"p33213","attributes":{"renderers":[{"id":"p33210"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p33190","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33191","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33192"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33193"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p33185","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33186","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33187"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33188"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p33189","attributes":{"axis":{"id":"p33185"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p33194","attributes":{"dimension":1,"axis":{"id":"p33190"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"1f153ecb-acb5-46de-8b99-acdc643fa9b9","roots":{"p33174":"c0bdc8f9-cf79-47da-90c8-ade1bd58217e"},"root_ids":["p33174"]}];
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

<div id="a8b243f8-dc57-4391-91fa-d4f907a48926" data-root-id="p33219" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b1d52f46-a666-4be1-9100-b6864e28fd50":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p33261","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p33262"}}},"roots":[{"type":"object","name":"Figure","id":"p33219","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p33221"},"y_range":{"type":"object","name":"FactorRange","id":"p33228","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p33229"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p33230"},"title":{"type":"object","name":"Title","id":"p33226","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p33256","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p33216","attributes":{"selected":{"type":"object","name":"Selection","id":"p33217","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p33218"},"data":{"type":"map","entries":[["x",[-18,-8,-2,-6,-11]],["y",["forward","reverse","reverse","reverse","reverse"]],["alpha",[1.0,1.0,1.0,1.0,1.0]],["pos",[18,8,2,6,11]],["base",["C","T","T","A","G"]],["n",[25,25,24,22,30]],["det_with",["0% of 25","0% of 25","0% of 24","0% of 22","23% of 30"]],["det_without",["63% of 19","63% of 19","60% of 20","55% of 22","36% of 14"]],["subs",["C&gt;A 19, C&gt;G 3, C&gt;T 3","T&gt;G 19, T&gt;A 6","T&gt;G 19, T&gt;A 3, T&gt;C 2","A&gt;T 19, A&gt;C 2, A&gt;G 1","G&gt;A 18, G&gt;T 6, G&gt;C 6"]],["zone",["no","no","yes","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p33257","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33258"}}},"glyph":{"type":"object","name":"Rect","id":"p33253","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p33254","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p33255","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p33227","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p33241"},{"type":"object","name":"BoxZoomTool","id":"p33242","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p33243","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p33249","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33248","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p33250","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p33251"},{"type":"object","name":"SaveTool","id":"p33252"},{"type":"object","name":"HoverTool","id":"p33259","attributes":{"renderers":[{"id":"p33256"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p33236","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p33237"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p33238"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33239"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p33231","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p33260","attributes":{"ticks":[-18,-11,-8,-6,-2],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33233"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-18,"18"],[-8,"8"],[-2,"2"],[-6,"6"],[-11,"11"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p33234"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p33235","attributes":{"axis":{"id":"p33231"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p33240","attributes":{"dimension":1,"axis":{"id":"p33236"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b1d52f46-a666-4be1-9100-b6864e28fd50","roots":{"p33219":"a8b243f8-dc57-4391-91fa-d4f907a48926"},"root_ids":["p33219"]}];
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


## What reached the statistics

279 records were screened for this assay and **44 (16%)** were evaluable, meaning both primers landed in the right orientation and size range. 235 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 183 |
| `chance_anchor` | 50 |
| `truncated` | 2 |

