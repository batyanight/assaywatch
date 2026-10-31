# SARCOCYSTIS_18S_5_8s_rDNA_short_Kutkiene_2010

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**SARCOCYSTIS — 18S-5.8s rDNA(short)**

| | |
|---|---|
| Target | Sarcocystis ([taxid 5812](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=5812)) |
| Gene | 18S-5.8s rDNA(short) |
| Chemistry | conventional |
| Amplicon | — |
| Designed | 2010 |
| Paper | [10.1007/s00436-010-1945-4](https://doi.org/10.1007/s00436-010-1945-4) |
| Registry status | active |

!!! quote "The paper"
    Kutkienė L et al. 2010. Parasitol Res 107:879-888

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ATTGAGTGTTCCGGTGAATTA` | 21 nt |
| reverse | `GGGATTCARTKGYYGAAA` | 18 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (48 months, from Oct 2022) | 11 | 18 | 61.1% | 38.6% – 79.7% |
| baseline (everything earlier) | 84 | 172 | 48.8% | 41.5% – 56.3% |

Change from baseline, Newcombe interval: **-11.4% to 32.3%**. Threshold: **90.0%**.

*detected share 61.1% (39%-80%) since Oct 2022, upper bound below the 90% threshold; change from baseline -11% to +32% (no measurable fall from a baseline of 49%) (window widened to 48 months to reach 15 evaluable records)*

Trend across deposit years: by record rising (p=0.0171, 16 years); by footprint rising (p=0.0233). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="bb279470-3270-4025-ab1c-111da6568733" data-root-id="p31732" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"70dab3f8-67fd-4904-a463-b99213430942":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p31787","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p31788"}}},"roots":[{"type":"object","name":"Figure","id":"p31732","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p31734"},"y_range":{"type":"object","name":"Range1d","id":"p31741","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p31742"},"y_scale":{"type":"object","name":"LinearScale","id":"p31743"},"title":{"type":"object","name":"Title","id":"p31739","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p31777","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p31729","attributes":{"selected":{"type":"object","name":"Selection","id":"p31730","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p31731"},"data":{"type":"map","entries":[["year",[2000,2001,2002,2004,2005,2014,2015,2016,2017,2018,2019,2020,2021,2023,2024,2025]],["share",[0.0,0.0,16.666666666666664,0.0,16.666666666666664,97.14285714285714,8.571428571428571,60.0,42.857142857142854,70.96774193548387,0.0,100.0,100.0,100.0,87.5,0.0]],["detected",[0,0,1,0,1,34,3,9,3,22,0,5,6,4,7,0]],["evaluable",[1,1,6,3,6,35,35,15,7,31,21,5,6,4,8,6]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.791719296345839,9.328625426046248,9.791719296345839,10.994220569835573,10.994220569835573,10.423139468338052,9.897626379762722,10.913832791890265,10.652487636092928,9.667366891029102,9.791719296345839,9.517227179437622,9.989711205477885,9.791719296345839]]]}}},"view":{"type":"object","name":"CDSView","id":"p31778","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31779"}}},"glyph":{"type":"object","name":"Line","id":"p31774","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p31775","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p31776","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p31783","attributes":{"data_source":{"id":"p31729"},"view":{"type":"object","name":"CDSView","id":"p31784","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31785"}}},"glyph":{"type":"object","name":"Scatter","id":"p31780","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p31781","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p31782","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p31740","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p31754"},{"type":"object","name":"BoxZoomTool","id":"p31755","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p31756","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p31762","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31761","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p31763","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p31764"},{"type":"object","name":"SaveTool","id":"p31765"},{"type":"object","name":"HoverTool","id":"p31786","attributes":{"renderers":[{"id":"p31783"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p31749","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31750","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31751"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31752"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p31744","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31745","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31746"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31747"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p31748","attributes":{"axis":{"id":"p31744"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p31753","attributes":{"dimension":1,"axis":{"id":"p31749"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p31766","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2022.5,"right":{"type":"object","name":"Node","id":"p31768","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p31769","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p31770","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p31772","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31771","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p31773","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"70dab3f8-67fd-4904-a463-b99213430942","roots":{"p31732":"bb279470-3270-4025-ab1c-111da6568733"},"root_ids":["p31732"]}];
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

<div id="b10c5070-bda6-4e93-8ad0-4ba5e752c01d" data-root-id="p31792" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"20e5e241-4628-4a3f-b598-5961ff86850a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p31832","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p31833"}}},"roots":[{"type":"object","name":"Figure","id":"p31792","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p31793"},"y_range":{"type":"object","name":"DataRange1d","id":"p31794","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p31801"},"y_scale":{"type":"object","name":"LinearScale","id":"p31802"},"title":{"type":"object","name":"Title","id":"p31799","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p31828","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p31789","attributes":{"selected":{"type":"object","name":"Selection","id":"p31790","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p31791"},"data":{"type":"map","entries":[["year",[2000,2001,2002,2004,2005,2014,2015,2016,2017,2018,2019,2020,2021,2023,2024,2025]],["evaluable",[1,1,6,3,6,35,35,15,7,31,21,5,6,4,8,6]],["detected",[0,0,1,0,1,34,3,9,3,22,0,5,6,4,7,0]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p31829","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31830"}}},"glyph":{"type":"object","name":"VBar","id":"p31825","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p31826","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p31827","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p31800","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p31813"},{"type":"object","name":"BoxZoomTool","id":"p31814","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p31815","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p31821","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31820","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p31822","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p31823"},{"type":"object","name":"SaveTool","id":"p31824"},{"type":"object","name":"HoverTool","id":"p31831","attributes":{"renderers":[{"id":"p31828"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p31808","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31809","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31810"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31811"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p31803","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31804","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31805"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31806"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p31807","attributes":{"axis":{"id":"p31803"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p31812","attributes":{"dimension":1,"axis":{"id":"p31808"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"20e5e241-4628-4a3f-b598-5961ff86850a","roots":{"p31792":"b10c5070-bda6-4e93-8ad0-4ba5e752c01d"},"root_ids":["p31792"]}];
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

<div id="aee9a617-43fe-45f3-a655-168311ad9a1e" data-root-id="p31837" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"ce805348-579f-4856-b973-cd34a7edf704":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p31879","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p31880"}}},"roots":[{"type":"object","name":"Figure","id":"p31837","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p31839"},"y_range":{"type":"object","name":"FactorRange","id":"p31846","attributes":{"factors":["reverse"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p31847"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p31848"},"title":{"type":"object","name":"Title","id":"p31844","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p31874","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p31834","attributes":{"selected":{"type":"object","name":"Selection","id":"p31835","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p31836"},"data":{"type":"map","entries":[["x",[-8,-16,-15,-14,-18,-11]],["y",["reverse","reverse","reverse","reverse","reverse","reverse"]],["alpha",[1.0,1.0,1.0,1.0,1.0,1.0]],["pos",[8,16,15,14,18,11]],["base",["K","G","A","T","G","A"]],["n",[79,91,95,89,88,86]],["det_with",["4% of 79","11% of 91","13% of 95","13% of 89","14% of 88","15% of 86"]],["det_without",["83% of 111","86% of 99","87% of 95","82% of 101","81% of 102","79% of 104"]],["subs",["K&gt;C 76, K&gt;A 3","G&gt;A 84, G&gt;C 6, G&gt;T 1","A&gt;C 87, A&gt;T 5, A&gt;G 3","T&gt;A 85, T&gt;C 2, T&gt;G 2","G&gt;A 86, G&gt;C 2","A&gt;C 85, A&gt;G 1"]],["zone",["no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p31875","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31876"}}},"glyph":{"type":"object","name":"Rect","id":"p31871","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p31872","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p31873","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p31845","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p31859"},{"type":"object","name":"BoxZoomTool","id":"p31860","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p31861","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p31867","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31866","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p31868","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p31869"},{"type":"object","name":"SaveTool","id":"p31870"},{"type":"object","name":"HoverTool","id":"p31877","attributes":{"renderers":[{"id":"p31874"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p31854","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p31855"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p31856"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31857"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p31849","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p31878","attributes":{"ticks":[-18,-16,-15,-14,-11,-8],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31851"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-8,"8"],[-16,"16"],[-15,"15"],[-14,"14"],[-18,"18"],[-11,"11"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p31852"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p31853","attributes":{"axis":{"id":"p31849"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p31858","attributes":{"dimension":1,"axis":{"id":"p31854"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"ce805348-579f-4856-b973-cd34a7edf704","roots":{"p31837":"aee9a617-43fe-45f3-a655-168311ad9a1e"},"root_ids":["p31837"]}];
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

Disclosures on this entry: `amplicon_multimodal`.


## What reached the statistics

30,875 records were screened for this assay and **190 (1%)** were evaluable, meaning both primers landed in the right orientation and size range. 30,685 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 28,571 |
| `truncated` | 1,739 |
| `chance_anchor` | 287 |
| `chance_only` | 88 |

