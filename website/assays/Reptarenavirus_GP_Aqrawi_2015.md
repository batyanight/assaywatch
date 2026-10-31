# Reptarenavirus_GP_Aqrawi_2015

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**Snake arenavirus  — Glycoprotein**

| | |
|---|---|
| Target | Reptarenavirus ([taxid 1653395](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1653395)) |
| Gene | Glycoprotein |
| Chemistry | conventional |
| Amplicon | 287 bp |
| Designed | 2015 |
| Paper | [10.15654/TPK-140743](https://doi.org/10.15654/TPK-140743) |
| Registry status | active |

!!! quote "The paper"
    Aqrawi, T., Stöhr, A. C., Knauf-Witzens, T., Krengel, A., Heckers, K. O. & Marschang, R. E. Nachweis und Charakterisierung von Schlangenarenaviren bei lebenden Boas und Pythons in einem deutschen Zoo. Tierärztliche Praxis Ausgabe K: Kleintiere / Heimtiere 43, 239-247 (2015).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GGSATAACAAAYTCACTTCAAATATC` | 26 nt |
| reverse | `TTCATTTCTTCATGRACTTTRTCAATC` | 27 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 2 | 9 | 22.2% | 6.3% – 54.7% |
| baseline (everything earlier) | 73 | 105 | 69.5% | 60.2% – 77.5% |

Change from baseline, Newcombe interval: **-65.1% to -13.5%**. Threshold: **90.0%**.

*9 evaluable records since Oct 2021, below the minimum of 15; the detected share is 22% (6%-55%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=2.38e-05, 9 years); by footprint rising (p=0.86); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="cc5c4b94-1569-4dd1-ad2c-5d686b2c9bd0" data-root-id="p31475" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9b703460-deb9-4e78-9d18-f7e736e0046d":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p31530","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p31531"}}},"roots":[{"type":"object","name":"Figure","id":"p31475","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p31477"},"y_range":{"type":"object","name":"Range1d","id":"p31484","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p31485"},"y_scale":{"type":"object","name":"LinearScale","id":"p31486"},"title":{"type":"object","name":"Title","id":"p31482","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p31520","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p31472","attributes":{"selected":{"type":"object","name":"Selection","id":"p31473","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p31474"},"data":{"type":"map","entries":[["year",[2012,2013,2014,2015,2017,2018,2020,2022,2023]],["share",[100.0,50.0,50.0,78.87323943661971,42.857142857142854,46.666666666666664,25.0,12.5,100.0]],["detected",[4,1,1,56,3,7,1,1,1]],["evaluable",[4,2,2,71,7,15,4,8,1]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent"]],["size",[9.517227179437622,9.07684386569143,9.07684386569143,11.451823022921252,9.897626379762722,10.423139468338052,9.517227179437622,9.989711205477885,8.703135093227193]]]}}},"view":{"type":"object","name":"CDSView","id":"p31521","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31522"}}},"glyph":{"type":"object","name":"Line","id":"p31517","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p31518","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p31519","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p31526","attributes":{"data_source":{"id":"p31472"},"view":{"type":"object","name":"CDSView","id":"p31527","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31528"}}},"glyph":{"type":"object","name":"Scatter","id":"p31523","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p31524","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p31525","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p31483","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p31497"},{"type":"object","name":"BoxZoomTool","id":"p31498","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p31499","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p31505","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31504","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p31506","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p31507"},{"type":"object","name":"SaveTool","id":"p31508"},{"type":"object","name":"HoverTool","id":"p31529","attributes":{"renderers":[{"id":"p31526"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p31492","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31493","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31494"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31495"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p31487","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31488","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31489"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31490"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p31491","attributes":{"axis":{"id":"p31487"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p31496","attributes":{"dimension":1,"axis":{"id":"p31492"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p31509","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2021.5,"right":{"type":"object","name":"Node","id":"p31511","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p31512","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p31513","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p31515","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31514","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p31516","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9b703460-deb9-4e78-9d18-f7e736e0046d","roots":{"p31475":"cc5c4b94-1569-4dd1-ad2c-5d686b2c9bd0"},"root_ids":["p31475"]}];
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

<div id="e1c81288-6e72-4fe6-bf73-03a69295f6e6" data-root-id="p31535" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"f493283c-e8b2-44fd-8119-8f8ee2212d0a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p31575","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p31576"}}},"roots":[{"type":"object","name":"Figure","id":"p31535","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p31536"},"y_range":{"type":"object","name":"DataRange1d","id":"p31537","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p31544"},"y_scale":{"type":"object","name":"LinearScale","id":"p31545"},"title":{"type":"object","name":"Title","id":"p31542","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p31571","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p31532","attributes":{"selected":{"type":"object","name":"Selection","id":"p31533","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p31534"},"data":{"type":"map","entries":[["year",[2012,2013,2014,2015,2017,2018,2020,2022,2023]],["evaluable",[4,2,2,71,7,15,4,8,1]],["detected",[4,1,1,56,3,7,1,1,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p31572","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31573"}}},"glyph":{"type":"object","name":"VBar","id":"p31568","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p31569","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p31570","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p31543","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p31556"},{"type":"object","name":"BoxZoomTool","id":"p31557","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p31558","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p31564","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31563","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p31565","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p31566"},{"type":"object","name":"SaveTool","id":"p31567"},{"type":"object","name":"HoverTool","id":"p31574","attributes":{"renderers":[{"id":"p31571"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p31551","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31552","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31553"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31554"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p31546","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31547","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31548"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31549"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p31550","attributes":{"axis":{"id":"p31546"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p31555","attributes":{"dimension":1,"axis":{"id":"p31551"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"f493283c-e8b2-44fd-8119-8f8ee2212d0a","roots":{"p31535":"e1c81288-6e72-4fe6-bf73-03a69295f6e6"},"root_ids":["p31535"]}];
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

<div id="da3152e4-e044-4896-8917-e681d72b0ca7" data-root-id="p31580" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"844ed49f-880a-41ec-af1a-c512207e407b":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p31622","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p31623"}}},"roots":[{"type":"object","name":"Figure","id":"p31580","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p31582"},"y_range":{"type":"object","name":"FactorRange","id":"p31589","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p31590"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p31591"},"title":{"type":"object","name":"Title","id":"p31587","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p31617","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p31577","attributes":{"selected":{"type":"object","name":"Selection","id":"p31578","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p31579"},"data":{"type":"map","entries":[["x",[-3,-21,-9,-4,-19,-18]],["y",["forward","forward","forward","reverse","reverse","forward"]],["alpha",[0.9850877192982456,0.7464912280701754,0.9850877192982456,1.0,1.0,1.0]],["pos",[3,21,9,4,19,18]],["base",["A","A","T","A","T","A"]],["n",[28,20,28,89,77,88]],["det_with",["0% of 28","5% of 20","36% of 28","63% of 89","66% of 77","69% of 88"]],["det_without",["87% of 86","79% of 94","76% of 86","76% of 25","65% of 37","54% of 26"]],["subs",["A&gt;T 16, A&gt;C 12","A&gt;C 13, A&gt;T 7","T&gt;G 13, T&gt;C 12, T&gt;A 3","A&gt;T 87, A&gt;G 2","T&gt;C 77","A&gt;C 80, A&gt;T 8"]],["zone",["yes","no","no","yes","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p31618","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31619"}}},"glyph":{"type":"object","name":"Rect","id":"p31614","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p31615","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p31616","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p31588","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p31602"},{"type":"object","name":"BoxZoomTool","id":"p31603","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p31604","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p31610","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31609","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p31611","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p31612"},{"type":"object","name":"SaveTool","id":"p31613"},{"type":"object","name":"HoverTool","id":"p31620","attributes":{"renderers":[{"id":"p31617"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p31597","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p31598"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p31599"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31600"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p31592","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p31621","attributes":{"ticks":[-21,-19,-18,-9,-4,-3],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31594"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-3,"3"],[-21,"21"],[-9,"9"],[-4,"4"],[-19,"19"],[-18,"18"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p31595"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p31596","attributes":{"axis":{"id":"p31592"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p31601","attributes":{"dimension":1,"axis":{"id":"p31597"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"844ed49f-880a-41ec-af1a-c512207e407b","roots":{"p31580":"da3152e4-e044-4896-8917-e681d72b0ca7"},"root_ids":["p31580"]}];
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

Disclosures on this entry: `orientation_inferred`.


## What reached the statistics

387 records were screened for this assay and **114 (29%)** were evaluable, meaning both primers landed in the right orientation and size range. 273 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 273 |

