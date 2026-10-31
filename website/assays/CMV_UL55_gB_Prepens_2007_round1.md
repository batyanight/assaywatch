# CMV_UL55_gB_Prepens_2007_round1

<span class="aw-chip aw-chip-stable">stable</span>

**CMV-specific HERPES — UL55 /Glycoprotein B (gB)**

| | |
|---|---|
| Target | Cytomegalovirus ([taxid 10358](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10358)) |
| Gene | UL55 /Glycoprotein B (gB) |
| Chemistry | conventional |
| Amplicon | 319 bp |
| Designed | 2007 |
| Paper | [10.1186/1743-422X-4-84](https://doi.org/10.1186/1743-422X-4-84) |
| Registry status | active |

!!! quote "The paper"
    Prepens S et al. 2007. Virol J 4:84

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CGCAAATCGCAGANKCNTGGTG` | 22 nt |
| reverse | `TGGTTGCCCAACAGNATYTCRTT` | 23 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 31 | 32 | 96.9% | 84.3% – 99.4% |
| baseline (everything earlier) | 588 | 643 | 91.4% | 89.0% – 93.4% |

Change from baseline, Newcombe interval: **-7.3% to 9.0%**. Threshold: **90.0%**.

*detected share 96.9% (84%-99%) since Oct 2024*

Trend across deposit years: by record rising (p=0.115, 32 years); by footprint rising (p=0.777). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="eda04066-c7f6-49dd-9e4f-b7aa8cc38315" data-root-id="p9632" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"209456e5-25ea-40e8-af4d-54119ccd97e4":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p9687","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p9688"}}},"roots":[{"type":"object","name":"Figure","id":"p9632","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p9634"},"y_range":{"type":"object","name":"Range1d","id":"p9641","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p9642"},"y_scale":{"type":"object","name":"LinearScale","id":"p9643"},"title":{"type":"object","name":"Title","id":"p9639","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p9677","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p9629","attributes":{"selected":{"type":"object","name":"Selection","id":"p9630","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p9631"},"data":{"type":"map","entries":[["year",[1987,1989,1990,1992,1993,1994,1996,2001,2002,2003,2004,2005,2006,2007,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,33.33333333333333,0.0,100.0,78.57142857142857,50.0,100.0,50.0,66.66666666666666,86.36363636363636,57.14285714285714,57.14285714285714,0.0,100.0,100.0,98.59154929577466,100.0,91.66666666666666,85.0,87.5,95.83333333333334,66.66666666666666,85.0,96.0,71.42857142857143,95.65217391304348,100.0]],["detected",[1,2,1,14,1,1,1,0,2,11,1,1,1,2,19,4,4,0,22,26,210,84,33,51,7,23,20,17,24,5,22,9]],["evaluable",[1,2,1,14,1,1,3,4,2,14,2,1,2,3,22,7,7,1,22,26,213,84,36,60,8,24,30,20,25,7,23,9]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,9.07684386569143,8.703135093227193,10.37579022724969,8.703135093227193,8.703135093227193,9.328625426046248,9.517227179437622,9.07684386569143,10.37579022724969,9.07684386569143,8.703135093227193,9.07684386569143,9.328625426046248,10.683957047019447,9.897626379762722,9.897626379762722,8.703135093227193,10.683957047019447,10.796415465069488,12.124710643835769,11.557772674175059,11.012804945939648,11.34465373009984,9.989711205477885,10.74264168206181,10.892023970177537,10.619414831097462,10.770092258092593,9.897626379762722,10.713966621835368,10.071067811865476]]]}}},"view":{"type":"object","name":"CDSView","id":"p9678","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p9679"}}},"glyph":{"type":"object","name":"Line","id":"p9674","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p9675","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p9676","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p9683","attributes":{"data_source":{"id":"p9629"},"view":{"type":"object","name":"CDSView","id":"p9684","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p9685"}}},"glyph":{"type":"object","name":"Scatter","id":"p9680","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p9681","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p9682","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p9640","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p9654"},{"type":"object","name":"BoxZoomTool","id":"p9655","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p9656","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p9662","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p9661","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p9663","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p9664"},{"type":"object","name":"SaveTool","id":"p9665"},{"type":"object","name":"HoverTool","id":"p9686","attributes":{"renderers":[{"id":"p9683"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p9649","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p9650","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p9651"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p9652"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p9644","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p9645","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p9646"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p9647"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p9648","attributes":{"axis":{"id":"p9644"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p9653","attributes":{"dimension":1,"axis":{"id":"p9649"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p9666","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p9668","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p9669","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p9670","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p9672","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p9671","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p9673","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"209456e5-25ea-40e8-af4d-54119ccd97e4","roots":{"p9632":"eda04066-c7f6-49dd-9e4f-b7aa8cc38315"},"root_ids":["p9632"]}];
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

<div id="d9459779-e49a-44d9-8352-56d692f85e33" data-root-id="p9692" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"8e77b87d-b7e0-4a97-9746-daab0cb18a84":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p9732","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p9733"}}},"roots":[{"type":"object","name":"Figure","id":"p9692","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p9693"},"y_range":{"type":"object","name":"DataRange1d","id":"p9694","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p9701"},"y_scale":{"type":"object","name":"LinearScale","id":"p9702"},"title":{"type":"object","name":"Title","id":"p9699","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p9728","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p9689","attributes":{"selected":{"type":"object","name":"Selection","id":"p9690","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p9691"},"data":{"type":"map","entries":[["year",[1987,1989,1990,1992,1993,1994,1996,2001,2002,2003,2004,2005,2006,2007,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,2,1,14,1,1,3,4,2,14,2,1,2,3,22,7,7,1,22,26,213,84,36,60,8,24,30,20,25,7,23,9]],["detected",[1,2,1,14,1,1,1,0,2,11,1,1,1,2,19,4,4,0,22,26,210,84,33,51,7,23,20,17,24,5,22,9]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p9729","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p9730"}}},"glyph":{"type":"object","name":"VBar","id":"p9725","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p9726","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p9727","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p9700","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p9713"},{"type":"object","name":"BoxZoomTool","id":"p9714","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p9715","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p9721","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p9720","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p9722","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p9723"},{"type":"object","name":"SaveTool","id":"p9724"},{"type":"object","name":"HoverTool","id":"p9731","attributes":{"renderers":[{"id":"p9728"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p9708","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p9709","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p9710"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p9711"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p9703","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p9704","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p9705"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p9706"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p9707","attributes":{"axis":{"id":"p9703"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p9712","attributes":{"dimension":1,"axis":{"id":"p9708"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"8e77b87d-b7e0-4a97-9746-daab0cb18a84","roots":{"p9692":"d9459779-e49a-44d9-8352-56d692f85e33"},"root_ids":["p9692"]}];
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

<div id="db88b263-5819-4e1c-ae6f-0fdbe98052d4" data-root-id="p9737" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"719e4037-6822-4c1a-babd-a2e563a142c0":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p9779","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p9780"}}},"roots":[{"type":"object","name":"Figure","id":"p9737","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p9739"},"y_range":{"type":"object","name":"FactorRange","id":"p9746","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p9747"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p9748"},"title":{"type":"object","name":"Title","id":"p9744","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p9774","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p9734","attributes":{"selected":{"type":"object","name":"Selection","id":"p9735","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p9736"},"data":{"type":"map","entries":[["x",[-19,-20,-15,-22,-15,-21,-18,-10,-13,-12,-21,-18]],["y",["reverse","reverse","reverse","forward","forward","reverse","reverse","reverse","reverse","forward","forward","forward"]],["alpha",[0.40688888888888886,0.40688888888888886,0.3162222222222222,0.43207407407407405,0.26585185185185184,0.3262962962962963,0.6184444444444445,0.5882222222222222,0.5328148148148147,1.0,0.7494074074074074,1.0]],["pos",[19,20,15,22,15,21,18,10,13,12,21,18]],["base",["T","T","C","C","C","G","G","G","A","A","G","A"]],["n",[51,51,33,56,23,35,93,87,76,212,119,175]],["det_with",["0% of 51","0% of 51","0% of 33","4% of 56","17% of 23","29% of 35","42% of 93","46% of 87","53% of 76","75% of 212","84% of 119","93% of 175"]],["det_without",["100% of 679","100% of 679","97% of 697","100% of 674","95% of 707","96% of 695","100% of 637","99% of 643","97% of 654","100% of 518","94% of 611","93% of 555"]],["subs",["T&gt;G 51","T&gt;C 51","C&gt;A 30, C&gt;T 3","C&gt;G 54, C&gt;T 2","C&gt;T 23","G&gt;A 28, G&gt;T 4, G&gt;C 3","G&gt;C 45, G&gt;T 39, G&gt;A 9","G&gt;A 87","A&gt;G 76","A&gt;C 157, A&gt;T 53, A&gt;G 2","G&gt;A 80, G&gt;C 37, G&gt;T 2","A&gt;G 175"]],["zone",["no","no","no","no","no","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p9775","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p9776"}}},"glyph":{"type":"object","name":"Rect","id":"p9771","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p9772","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p9773","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p9745","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p9759"},{"type":"object","name":"BoxZoomTool","id":"p9760","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p9761","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p9767","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p9766","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p9768","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p9769"},{"type":"object","name":"SaveTool","id":"p9770"},{"type":"object","name":"HoverTool","id":"p9777","attributes":{"renderers":[{"id":"p9774"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p9754","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p9755"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p9756"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p9757"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p9749","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p9778","attributes":{"ticks":[-22,-21,-20,-19,-18,-15,-13,-12,-10],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p9751"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-19,"19"],[-20,"20"],[-15,"15"],[-22,"22"],[-21,"21"],[-18,"18"],[-10,"10"],[-13,"13"],[-12,"12"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p9752"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p9753","attributes":{"axis":{"id":"p9749"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p9758","attributes":{"dimension":1,"axis":{"id":"p9754"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"719e4037-6822-4c1a-babd-a2e563a142c0","roots":{"p9737":"db88b263-5819-4e1c-ae6f-0fdbe98052d4"},"root_ids":["p9737"]}];
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

<div id="f5cacf84-b951-48a4-a5a2-921646ffbd99" data-root-id="p9784" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"360cc13a-7757-45d9-89dd-68250a149be0":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p9833","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p9834"}}},"roots":[{"type":"object","name":"Figure","id":"p9784","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p9793","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p9794","attributes":{"factors":["Cytomegalovirus humanbeta5 (3050295)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p9795"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p9796"},"title":{"type":"object","name":"Title","id":"p9791","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p9828","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p9781","attributes":{"selected":{"type":"object","name":"Selection","id":"p9782","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p9783"},"data":{"type":"map","entries":[["y",["Cytomegalovirus humanbeta5 (3050295)"]],["share",[100.0]],["lo",[88.97446045395641]],["hi",[100.0]],["n",[31]],["det",[31]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p9829","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p9830"}}},"glyph":{"type":"object","name":"Scatter","id":"p9825","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p9826","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p9827","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p9792","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p9807"},{"type":"object","name":"BoxZoomTool","id":"p9808","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p9809","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p9815","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p9814","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p9816","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p9817"},{"type":"object","name":"SaveTool","id":"p9818"},{"type":"object","name":"HoverTool","id":"p9832","attributes":{"renderers":[{"id":"p9828"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p9802","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p9803"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p9804"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p9805"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p9797","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p9798","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p9799"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p9800"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p9801","attributes":{"axis":{"id":"p9797"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p9806","attributes":{"dimension":1,"axis":{"id":"p9802"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p9819","attributes":{"source":{"id":"p9781"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p9831","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"360cc13a-7757-45d9-89dd-68250a149be0","roots":{"p9784":"f5cacf84-b951-48a4-a5a2-921646ffbd99"},"root_ids":["p9784"]}];
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

12,051 records were screened for this assay and **675 (6%)** were evaluable, meaning both primers landed in the right orientation and size range. 11,376 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 10,230 |
| `truncated` | 870 |
| `chance_anchor` | 275 |
| `no_pair` | 1 |

