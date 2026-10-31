# CMV_UL55_gB_Prepens_2007_round2

<span class="aw-chip aw-chip-stable">stable</span>

**CMV-specific HERPES — UL55 /Glycoprotein B (gB)**

| | |
|---|---|
| Target | Cytomegalovirus ([taxid 10358](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10358)) |
| Gene | UL55 /Glycoprotein B (gB) |
| Chemistry | conventional |
| Amplicon | 250 bp |
| Designed | 2007 |
| Paper | [10.1186/1743-422X-4-84](https://doi.org/10.1186/1743-422X-4-84) |
| Registry status | active |

!!! quote "The paper"
    Prepens S et al. 2007. Virol J 4:84

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `TTCAAGGAACTCAGYAARATNAAYCC` | 26 nt |
| reverse | `CGTTGTCCTCNCCNARYTGNCC` | 22 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 31 | 32 | 96.9% | 84.3% – 99.4% |
| baseline (everything earlier) | 646 | 664 | 97.3% | 95.8% – 98.3% |

Change from baseline, Newcombe interval: **-13.1% to 2.6%**. Threshold: **90.0%**.

*detected share 96.9% (84%-99%) since Oct 2024*

Trend across deposit years: by record rising (p=0.00099, 35 years); by footprint rising (p=0.336). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="e4d95f63-cd58-4da5-aa4d-f6ac230c68d0" data-root-id="p9838" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"7aff510a-f664-4be7-8719-06f61338ddfe":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p9893","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p9894"}}},"roots":[{"type":"object","name":"Figure","id":"p9838","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p9840"},"y_range":{"type":"object","name":"Range1d","id":"p9847","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p9848"},"y_scale":{"type":"object","name":"LinearScale","id":"p9849"},"title":{"type":"object","name":"Title","id":"p9845","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p9883","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p9835","attributes":{"selected":{"type":"object","name":"Selection","id":"p9836","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p9837"},"data":{"type":"map","entries":[["year",[1987,1989,1990,1992,1993,1994,1996,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,0.0,0.0,0.0,100.0,100.0,100.0,100.0,50.0,100.0,100.0,83.33333333333334,62.5,50.0,100.0,100.0,100.0,100.0,100.0,97.5609756097561,100.0,100.0,100.0,100.0,100.0,100.0,71.42857142857143,95.65217391304348,100.0]],["detected",[1,2,1,14,1,1,3,0,0,0,4,2,14,2,1,2,5,20,5,4,1,22,26,214,84,40,62,8,24,32,21,25,5,22,9]],["evaluable",[1,2,1,14,1,1,3,1,1,1,4,2,14,2,2,2,5,24,8,8,1,22,26,214,84,41,62,8,24,32,21,25,7,23,9]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,9.07684386569143,8.703135093227193,10.37579022724969,8.703135093227193,8.703135093227193,9.328625426046248,8.703135093227193,8.703135093227193,8.703135093227193,9.517227179437622,9.07684386569143,10.37579022724969,9.07684386569143,9.07684386569143,9.07684386569143,9.667366891029102,10.74264168206181,9.989711205477885,9.989711205477885,8.703135093227193,10.683957047019447,10.796415465069488,12.127483853608844,11.557772674175059,11.098224018878925,11.365614964623912,9.989711205477885,10.74264168206181,10.934913263353746,10.652487636092928,10.770092258092593,9.897626379762722,10.713966621835368,10.071067811865476]]]}}},"view":{"type":"object","name":"CDSView","id":"p9884","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p9885"}}},"glyph":{"type":"object","name":"Line","id":"p9880","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p9881","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p9882","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p9889","attributes":{"data_source":{"id":"p9835"},"view":{"type":"object","name":"CDSView","id":"p9890","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p9891"}}},"glyph":{"type":"object","name":"Scatter","id":"p9886","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p9887","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p9888","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p9846","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p9860"},{"type":"object","name":"BoxZoomTool","id":"p9861","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p9862","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p9868","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p9867","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p9869","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p9870"},{"type":"object","name":"SaveTool","id":"p9871"},{"type":"object","name":"HoverTool","id":"p9892","attributes":{"renderers":[{"id":"p9889"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p9855","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p9856","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p9857"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p9858"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p9850","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p9851","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p9852"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p9853"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p9854","attributes":{"axis":{"id":"p9850"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p9859","attributes":{"dimension":1,"axis":{"id":"p9855"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p9872","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p9874","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p9875","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p9876","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p9878","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p9877","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p9879","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"7aff510a-f664-4be7-8719-06f61338ddfe","roots":{"p9838":"e4d95f63-cd58-4da5-aa4d-f6ac230c68d0"},"root_ids":["p9838"]}];
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

<div id="f89fcbd3-a806-4bd5-b6a0-ab4c62ca77d0" data-root-id="p9898" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"46f161cd-c3fa-441a-b2e8-a331ea2142ba":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p9938","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p9939"}}},"roots":[{"type":"object","name":"Figure","id":"p9898","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p9899"},"y_range":{"type":"object","name":"DataRange1d","id":"p9900","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p9907"},"y_scale":{"type":"object","name":"LinearScale","id":"p9908"},"title":{"type":"object","name":"Title","id":"p9905","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p9934","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p9895","attributes":{"selected":{"type":"object","name":"Selection","id":"p9896","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p9897"},"data":{"type":"map","entries":[["year",[1987,1989,1990,1992,1993,1994,1996,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,2,1,14,1,1,3,1,1,1,4,2,14,2,2,2,5,24,8,8,1,22,26,214,84,41,62,8,24,32,21,25,7,23,9]],["detected",[1,2,1,14,1,1,3,0,0,0,4,2,14,2,1,2,5,20,5,4,1,22,26,214,84,40,62,8,24,32,21,25,5,22,9]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p9935","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p9936"}}},"glyph":{"type":"object","name":"VBar","id":"p9931","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p9932","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p9933","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p9906","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p9919"},{"type":"object","name":"BoxZoomTool","id":"p9920","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p9921","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p9927","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p9926","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p9928","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p9929"},{"type":"object","name":"SaveTool","id":"p9930"},{"type":"object","name":"HoverTool","id":"p9937","attributes":{"renderers":[{"id":"p9934"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p9914","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p9915","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p9916"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p9917"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p9909","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p9910","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p9911"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p9912"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p9913","attributes":{"axis":{"id":"p9909"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p9918","attributes":{"dimension":1,"axis":{"id":"p9914"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"46f161cd-c3fa-441a-b2e8-a331ea2142ba","roots":{"p9898":"f89fcbd3-a806-4bd5-b6a0-ab4c62ca77d0"},"root_ids":["p9898"]}];
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

<div id="bc9e5203-5cfe-4e70-9565-39273f60ff4a" data-root-id="p9943" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"efb889b1-e61b-4f05-88e2-ffcdf3034f76":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p9985","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p9986"}}},"roots":[{"type":"object","name":"Figure","id":"p9943","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p9945"},"y_range":{"type":"object","name":"FactorRange","id":"p9952","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p9953"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p9954"},"title":{"type":"object","name":"Title","id":"p9950","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p9980","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p9940","attributes":{"selected":{"type":"object","name":"Selection","id":"p9941","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p9942"},"data":{"type":"map","entries":[["x",[-24,-26,-21,-15,-16,-18,-15,-22,-21,-13,-14,-18]],["y",["forward","forward","reverse","reverse","reverse","reverse","forward","forward","forward","forward","forward","forward"]],["alpha",[0.3600574712643678,0.2672413793103448,0.43333333333333335,0.4528735632183908,0.41867816091954024,0.7752873563218391,0.8632183908045977,0.2574712643678161,0.6433908045977011,0.3112068965517241,0.3112068965517241,0.3112068965517241]],["pos",[24,26,21,15,16,18,15,22,21,13,14,18]],["base",["C","T","G","C","C","G","C","A","G","G","A","A"]],["n",[43,24,58,62,55,128,146,22,101,33,33,33]],["det_with",["67% of 43","67% of 24","79% of 58","81% of 62","82% of 55","89% of 128","92% of 146","91% of 22","96% of 101","100% of 33","100% of 33","100% of 33"]],["det_without",["100% of 705","99% of 724","100% of 690","100% of 686","99% of 693","100% of 620","100% of 602","98% of 726","98% of 647","98% of 715","98% of 715","98% of 715"]],["subs",["C&gt;G 19, C&gt;T 16, C&gt;A 8","T&gt;C 24","G&gt;A 58","C&gt;T 62","C&gt;A 30, C&gt;T 14, C&gt;G 11","G&gt;A 128","C&gt;T 92, C&gt;G 44, C&gt;A 10","A&gt;G 20, A&gt;C 2","G&gt;A 98, G&gt;T 3","G&gt;C 33","A&gt;T 33","A&gt;G 33"]],["zone",["no","no","no","no","no","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p9981","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p9982"}}},"glyph":{"type":"object","name":"Rect","id":"p9977","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p9978","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p9979","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p9951","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p9965"},{"type":"object","name":"BoxZoomTool","id":"p9966","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p9967","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p9973","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p9972","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p9974","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p9975"},{"type":"object","name":"SaveTool","id":"p9976"},{"type":"object","name":"HoverTool","id":"p9983","attributes":{"renderers":[{"id":"p9980"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p9960","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p9961"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p9962"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p9963"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p9955","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p9984","attributes":{"ticks":[-26,-24,-22,-21,-18,-16,-15,-14,-13],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p9957"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-24,"24"],[-26,"26"],[-21,"21"],[-15,"15"],[-16,"16"],[-18,"18"],[-22,"22"],[-13,"13"],[-14,"14"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p9958"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p9959","attributes":{"axis":{"id":"p9955"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p9964","attributes":{"dimension":1,"axis":{"id":"p9960"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"efb889b1-e61b-4f05-88e2-ffcdf3034f76","roots":{"p9943":"bc9e5203-5cfe-4e70-9565-39273f60ff4a"},"root_ids":["p9943"]}];
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

<div id="afd9f453-a0a2-47eb-bcc7-0a970416164f" data-root-id="p9990" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"5e3f95ee-a58a-4ca2-830e-07aa5a69bbe6":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p10039","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p10040"}}},"roots":[{"type":"object","name":"Figure","id":"p9990","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p9999","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p10000","attributes":{"factors":["Cytomegalovirus humanbeta5 (3050295)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p10001"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p10002"},"title":{"type":"object","name":"Title","id":"p9997","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p10034","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p9987","attributes":{"selected":{"type":"object","name":"Selection","id":"p9988","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p9989"},"data":{"type":"map","entries":[["y",["Cytomegalovirus humanbeta5 (3050295)"]],["share",[100.0]],["lo",[88.97446045395641]],["hi",[100.0]],["n",[31]],["det",[31]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p10035","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p10036"}}},"glyph":{"type":"object","name":"Scatter","id":"p10031","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p10032","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p10033","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p9998","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p10013"},{"type":"object","name":"BoxZoomTool","id":"p10014","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p10015","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p10021","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p10020","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p10022","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p10023"},{"type":"object","name":"SaveTool","id":"p10024"},{"type":"object","name":"HoverTool","id":"p10038","attributes":{"renderers":[{"id":"p10034"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p10008","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p10009"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p10010"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p10011"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p10003","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p10004","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p10005"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p10006"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p10007","attributes":{"axis":{"id":"p10003"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p10012","attributes":{"dimension":1,"axis":{"id":"p10008"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p10025","attributes":{"source":{"id":"p9987"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p10037","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"5e3f95ee-a58a-4ca2-830e-07aa5a69bbe6","roots":{"p9990":"afd9f453-a0a2-47eb-bcc7-0a970416164f"},"root_ids":["p9990"]}];
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

12,051 records were screened for this assay and **696 (6%)** were evaluable, meaning both primers landed in the right orientation and size range. 11,355 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 10,518 |
| `truncated` | 788 |
| `chance_anchor` | 47 |
| `no_pair` | 2 |

