# PHLEBOVIRUS_ssRNA_L_segment_round2

<span class="aw-chip aw-chip-stable">stable</span>

**PHLEBOVIRUS (ssRNA) — L segment (PREDICT P-021 round 2)**

| | |
|---|---|
| Target | Phlebovirus ([taxid 11584](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11584)) |
| Gene | L segment |
| Chemistry | conventional |
| Amplicon | 244 bp |
| Designed | 2003 |
| Paper | [10.1002/jmv.10465](https://doi.org/10.1002/jmv.10465) |
| Registry status | active |

!!! quote "The paper"
    Sanchez-Seco, M. P. et al. Detection and identification of Toscana and other phleboviruses by RT-nested-PCR assays with degenerated primers. J Med Virol 71, 140-149 (2003).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `WTNCCNAANCCNYMSAARATG` | 21 nt |
| reverse | `TCYTCYTTRTTYTTRARRTARCC` | 23 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 138 | 142 | 97.2% | 93.0% – 98.9% |
| baseline (everything earlier) | 273 | 320 | 85.3% | 81.0% – 88.8% |

Change from baseline, Newcombe interval: **6.4% to 16.5%**. Threshold: **90.0%**.

*detected share 97.2% (93%-99%) since Oct 2024*

Trend across deposit years: by record rising (p=3.83e-09, 21 years); by footprint rising (p=0.325). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="ae511913-b417-40f0-807b-834016ce7b3a" data-root-id="p23502" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"a79e647a-3bb4-4994-9bd6-2818c67f74e6":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p23557","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p23558"}}},"roots":[{"type":"object","name":"Figure","id":"p23502","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p23504"},"y_range":{"type":"object","name":"Range1d","id":"p23511","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p23512"},"y_scale":{"type":"object","name":"LinearScale","id":"p23513"},"title":{"type":"object","name":"Title","id":"p23509","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p23547","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p23499","attributes":{"selected":{"type":"object","name":"Selection","id":"p23500","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p23501"},"data":{"type":"map","entries":[["year",[1992,2005,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,60.0,86.36363636363636,100.0,85.71428571428571,55.55555555555556,33.33333333333333,10.0,66.66666666666666,93.93939393939394,88.88888888888889,14.285714285714285,86.66666666666667,84.0,98.0,98.86363636363636,96.49122807017544,98.75]],["detected",[1,1,5,3,3,19,5,6,10,1,1,12,31,8,1,13,21,49,87,55,79]],["evaluable",[1,1,5,3,5,22,5,7,18,3,10,18,33,9,7,15,25,50,88,57,80]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.667366891029102,9.328625426046248,9.667366891029102,10.683957047019447,9.667366891029102,9.897626379762722,10.547770533331066,9.328625426046248,10.143865699252444,10.547770533331066,10.955310988645032,10.071067811865476,9.897626379762722,10.423139468338052,10.770092258092593,11.22734795681138,11.586894093100417,11.311780786273989,11.527140521415502]]]}}},"view":{"type":"object","name":"CDSView","id":"p23548","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p23549"}}},"glyph":{"type":"object","name":"Line","id":"p23544","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p23545","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p23546","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p23553","attributes":{"data_source":{"id":"p23499"},"view":{"type":"object","name":"CDSView","id":"p23554","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p23555"}}},"glyph":{"type":"object","name":"Scatter","id":"p23550","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p23551","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p23552","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p23510","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p23524"},{"type":"object","name":"BoxZoomTool","id":"p23525","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p23526","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p23532","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p23531","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p23533","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p23534"},{"type":"object","name":"SaveTool","id":"p23535"},{"type":"object","name":"HoverTool","id":"p23556","attributes":{"renderers":[{"id":"p23553"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p23519","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23520","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23521"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23522"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p23514","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23515","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23516"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23517"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p23518","attributes":{"axis":{"id":"p23514"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p23523","attributes":{"dimension":1,"axis":{"id":"p23519"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p23536","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p23538","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p23539","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p23540","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p23542","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p23541","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p23543","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"a79e647a-3bb4-4994-9bd6-2818c67f74e6","roots":{"p23502":"ae511913-b417-40f0-807b-834016ce7b3a"},"root_ids":["p23502"]}];
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

<div id="c6521cf9-8d31-403f-b415-45835b021677" data-root-id="p23562" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"580f1668-2002-40b5-9e53-d049a8934784":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p23602","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p23603"}}},"roots":[{"type":"object","name":"Figure","id":"p23562","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p23563"},"y_range":{"type":"object","name":"DataRange1d","id":"p23564","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p23571"},"y_scale":{"type":"object","name":"LinearScale","id":"p23572"},"title":{"type":"object","name":"Title","id":"p23569","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p23598","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p23559","attributes":{"selected":{"type":"object","name":"Selection","id":"p23560","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p23561"},"data":{"type":"map","entries":[["year",[1992,2005,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,5,3,5,22,5,7,18,3,10,18,33,9,7,15,25,50,88,57,80]],["detected",[1,1,5,3,3,19,5,6,10,1,1,12,31,8,1,13,21,49,87,55,79]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p23599","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p23600"}}},"glyph":{"type":"object","name":"VBar","id":"p23595","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p23596","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p23597","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p23570","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p23583"},{"type":"object","name":"BoxZoomTool","id":"p23584","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p23585","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p23591","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p23590","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p23592","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p23593"},{"type":"object","name":"SaveTool","id":"p23594"},{"type":"object","name":"HoverTool","id":"p23601","attributes":{"renderers":[{"id":"p23598"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p23578","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23579","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23580"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23581"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p23573","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23574","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23575"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23576"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p23577","attributes":{"axis":{"id":"p23573"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p23582","attributes":{"dimension":1,"axis":{"id":"p23578"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"580f1668-2002-40b5-9e53-d049a8934784","roots":{"p23562":"c6521cf9-8d31-403f-b415-45835b021677"},"root_ids":["p23562"]}];
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

<div id="c0817e5c-23b3-4d48-ad0a-31a1188bc9f8" data-root-id="p23607" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"39d8ad4a-8905-4a3a-964d-c8c7d64e93ff":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p23649","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p23650"}}},"roots":[{"type":"object","name":"Figure","id":"p23607","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p23609"},"y_range":{"type":"object","name":"FactorRange","id":"p23616","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p23617"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p23618"},"title":{"type":"object","name":"Title","id":"p23614","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p23644","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p23604","attributes":{"selected":{"type":"object","name":"Selection","id":"p23605","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p23606"},"data":{"type":"map","entries":[["x",[-18,-3,-21,-7,-14,-9]],["y",["forward","reverse","forward","forward","forward","forward"]],["alpha",[0.30454545454545456,0.5694805194805195,0.6136363636363635,1.0,0.3781385281385281,1.0]],["pos",[18,3,21,7,14,9]],["base",["C","R","W","S","A","Y"]],["n",[21,57,63,120,31,136]],["det_with",["0% of 21","65% of 57","67% of 63","81% of 120","84% of 31","93% of 136"]],["det_without",["95% of 432","94% of 396","95% of 390","94% of 333","91% of 422","90% of 317"]],["subs",["C&gt;T 17, C&gt;A 4","R&gt;T 33, R&gt;C 24","W&gt;C 48, W&gt;G 15","S&gt;T 85, S&gt;A 35","A&gt;G 30, A&gt;C 1","Y&gt;G 128, Y&gt;A 8"]],["zone",["no","yes","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p23645","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p23646"}}},"glyph":{"type":"object","name":"Rect","id":"p23641","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p23642","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p23643","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p23615","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p23629"},{"type":"object","name":"BoxZoomTool","id":"p23630","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p23631","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p23637","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p23636","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p23638","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p23639"},{"type":"object","name":"SaveTool","id":"p23640"},{"type":"object","name":"HoverTool","id":"p23647","attributes":{"renderers":[{"id":"p23644"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p23624","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p23625"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p23626"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23627"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p23619","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p23648","attributes":{"ticks":[-21,-18,-14,-9,-7,-3],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23621"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-18,"18"],[-3,"3"],[-21,"21"],[-7,"7"],[-14,"14"],[-9,"9"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p23622"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p23623","attributes":{"axis":{"id":"p23619"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p23628","attributes":{"dimension":1,"axis":{"id":"p23624"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"39d8ad4a-8905-4a3a-964d-c8c7d64e93ff","roots":{"p23607":"c0817e5c-23b3-4d48-ad0a-31a1188bc9f8"},"root_ids":["p23607"]}];
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

<div id="c7b5e3dc-8d11-44ae-b21a-d69b416105a0" data-root-id="p23654" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"d148a417-7975-4287-a7fe-27893ec35944":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p23703","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p23704"}}},"roots":[{"type":"object","name":"Figure","id":"p23654","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p23663","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p23664","attributes":{"factors":["Phlebovirus mukawaense (3052664)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p23665"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p23666"},"title":{"type":"object","name":"Title","id":"p23661","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p23698","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p23651","attributes":{"selected":{"type":"object","name":"Selection","id":"p23652","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p23653"},"data":{"type":"map","entries":[["y",["Phlebovirus mukawaense (3052664)"]],["share",[98.71794871794873]],["lo",[93.0891429982978]],["hi",[99.77332682461663]],["n",[78]],["det",[77]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p23699","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p23700"}}},"glyph":{"type":"object","name":"Scatter","id":"p23695","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p23696","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p23697","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p23662","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p23677"},{"type":"object","name":"BoxZoomTool","id":"p23678","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p23679","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p23685","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p23684","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p23686","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p23687"},{"type":"object","name":"SaveTool","id":"p23688"},{"type":"object","name":"HoverTool","id":"p23702","attributes":{"renderers":[{"id":"p23698"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p23672","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p23673"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p23674"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23675"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p23667","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23668","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23669"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23670"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p23671","attributes":{"axis":{"id":"p23667"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p23676","attributes":{"dimension":1,"axis":{"id":"p23672"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p23689","attributes":{"source":{"id":"p23651"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p23701","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"d148a417-7975-4287-a7fe-27893ec35944","roots":{"p23654":"c7b5e3dc-8d11-44ae-b21a-d69b416105a0"},"root_ids":["p23654"]}];
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
L[Gene] OR "L segment"[Title] OR polymerase[Title] OR "complete genome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).


## What reached the statistics

1,147 records were screened for this assay and **462 (40%)** were evaluable, meaning both primers landed in the right orientation and size range. 685 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 547 |
| `truncated` | 88 |
| `chance_only` | 6 |
| `chance_anchor` | 5 |

