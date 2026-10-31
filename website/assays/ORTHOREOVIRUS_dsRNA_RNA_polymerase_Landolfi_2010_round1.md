# ORTHOREOVIRUS_dsRNA_RNA_polymerase_Landolfi_2010_round1

<span class="aw-chip aw-chip-declining">declining</span>

**ORTHOREOVIRUS (dsRNA) — RNA polymerase**

| | |
|---|---|
| Target | Orthoreovirus ([taxid 10882](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10882)) |
| Gene | RNA polymerase |
| Chemistry | conventional |
| Amplicon | 274 bp |
| Designed | 2010 |
| Paper | [10.1177/104063871002200106](https://doi.org/10.1177/104063871002200106) |
| Registry status | active |

!!! quote "The paper"
    Landolfi JA et al. 2010. J Vet Diagn Invest 22:37-43

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GGBTCMACNGCYACYTCBACYGAGCA` | 26 nt |
| reverse | `CDATGTCRTAHWYCCANCCRAA` | 22 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 172 | 358 | 48.0% | 42.9% – 53.2% |
| baseline (everything earlier) | 447 | 627 | 71.3% | 67.6% – 74.7% |

Change from baseline, Newcombe interval: **-29.4% to -16.9%**. Threshold: **90.0%**.

*detected share 48.0% (43%-53%) since Oct 2024, upper bound below the 90% threshold; change from baseline -29% to -17%; separately, lineage Orthoreovirus piscis (3431498) (182 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift*

Trend across deposit years: by record falling (p=8.66e-06, 23 years); by footprint rising (p=0.73); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="eb0f5fa4-8a90-4730-b4f6-ad72bdd2278e" data-root-id="p22012" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"96c540fa-bbd4-40d3-898a-47ca95e5fd9a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p22067","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p22068"}}},"roots":[{"type":"object","name":"Figure","id":"p22012","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p22014"},"y_range":{"type":"object","name":"Range1d","id":"p22021","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p22022"},"y_scale":{"type":"object","name":"LinearScale","id":"p22023"},"title":{"type":"object","name":"Title","id":"p22019","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p22057","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p22009","attributes":{"selected":{"type":"object","name":"Selection","id":"p22010","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p22011"},"data":{"type":"map","entries":[["year",[1993,1994,2001,2006,2007,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,66.66666666666666,87.87878787878788,84.375,83.33333333333334,88.88888888888889,48.484848484848484,64.51612903225806,26.31578947368421,62.857142857142854,95.65217391304348,94.5945945945946,98.98989898989899,42.00626959247649,97.05882352941177]],["detected",[1,2,1,2,1,6,7,8,12,10,29,27,20,16,16,20,40,22,44,70,98,134,33]],["evaluable",[1,2,1,2,1,6,7,8,12,15,33,32,24,18,33,31,152,35,46,74,99,319,34]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,9.07684386569143,8.703135093227193,9.07684386569143,8.703135093227193,9.791719296345839,9.897626379762722,9.989711205477885,10.269703144398052,10.423139468338052,10.955310988645032,10.934913263353746,10.74264168206181,10.547770533331066,10.955310988645032,10.913832791890265,11.922851885492664,10.994220569835573,11.173276359477448,11.47800280636852,11.660254037844386,12.361022885240567,10.975067467348278]]]}}},"view":{"type":"object","name":"CDSView","id":"p22058","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p22059"}}},"glyph":{"type":"object","name":"Line","id":"p22054","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p22055","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p22056","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p22063","attributes":{"data_source":{"id":"p22009"},"view":{"type":"object","name":"CDSView","id":"p22064","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p22065"}}},"glyph":{"type":"object","name":"Scatter","id":"p22060","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p22061","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p22062","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p22020","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p22034"},{"type":"object","name":"BoxZoomTool","id":"p22035","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p22036","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p22042","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p22041","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p22043","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p22044"},{"type":"object","name":"SaveTool","id":"p22045"},{"type":"object","name":"HoverTool","id":"p22066","attributes":{"renderers":[{"id":"p22063"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p22029","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p22030","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p22031"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22032"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p22024","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p22025","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p22026"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22027"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p22028","attributes":{"axis":{"id":"p22024"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p22033","attributes":{"dimension":1,"axis":{"id":"p22029"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p22046","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p22048","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p22049","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p22050","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p22052","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p22051","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p22053","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"96c540fa-bbd4-40d3-898a-47ca95e5fd9a","roots":{"p22012":"eb0f5fa4-8a90-4730-b4f6-ad72bdd2278e"},"root_ids":["p22012"]}];
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

<div id="ff946fa3-854a-4fa9-abc5-028c5682bc16" data-root-id="p22072" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b785647a-36c2-4645-94fc-492cc329f433":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p22112","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p22113"}}},"roots":[{"type":"object","name":"Figure","id":"p22072","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p22073"},"y_range":{"type":"object","name":"DataRange1d","id":"p22074","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p22081"},"y_scale":{"type":"object","name":"LinearScale","id":"p22082"},"title":{"type":"object","name":"Title","id":"p22079","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p22108","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p22069","attributes":{"selected":{"type":"object","name":"Selection","id":"p22070","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p22071"},"data":{"type":"map","entries":[["year",[1993,1994,2001,2006,2007,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,2,1,2,1,6,7,8,12,15,33,32,24,18,33,31,152,35,46,74,99,319,34]],["detected",[1,2,1,2,1,6,7,8,12,10,29,27,20,16,16,20,40,22,44,70,98,134,33]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p22109","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p22110"}}},"glyph":{"type":"object","name":"VBar","id":"p22105","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p22106","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p22107","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p22080","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p22093"},{"type":"object","name":"BoxZoomTool","id":"p22094","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p22095","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p22101","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p22100","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p22102","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p22103"},{"type":"object","name":"SaveTool","id":"p22104"},{"type":"object","name":"HoverTool","id":"p22111","attributes":{"renderers":[{"id":"p22108"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p22088","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p22089","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p22090"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22091"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p22083","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p22084","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p22085"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22086"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p22087","attributes":{"axis":{"id":"p22083"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p22092","attributes":{"dimension":1,"axis":{"id":"p22088"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b785647a-36c2-4645-94fc-492cc329f433","roots":{"p22072":"ff946fa3-854a-4fa9-abc5-028c5682bc16"},"root_ids":["p22072"]}];
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

<div id="c9d18e79-f46c-4363-b0bd-b21cd90acee0" data-root-id="p22117" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"78214fb4-283c-494e-9fba-6bb8ac346fb2":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p22159","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p22160"}}},"roots":[{"type":"object","name":"Figure","id":"p22117","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p22119"},"y_range":{"type":"object","name":"FactorRange","id":"p22126","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p22127"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p22128"},"title":{"type":"object","name":"Title","id":"p22124","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p22154","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p22114","attributes":{"selected":{"type":"object","name":"Selection","id":"p22115","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p22116"},"data":{"type":"map","entries":[["x",[-14,-2,-1,-3,-21,-6,-9,-24,-18,-19,-15,-12,-12]],["y",["reverse","reverse","reverse","forward","forward","forward","forward","forward","reverse","reverse","forward","forward","reverse"]],["alpha",[1.0,1.0,1.0,1.0,1.0,1.0,0.239746192893401,0.526243654822335,0.667766497461929,0.2949746192893401,1.0,1.0,1.0]],["pos",[14,2,1,3,21,6,9,24,18,19,15,12,12]],["base",["T","A","A","G","M","Y","B","B","G","T","Y","Y","H"]],["n",[351,350,349,609,630,616,26,109,150,42,284,339,360]],["det_with",["0% of 351","0% of 350","0% of 349","42% of 609","43% of 630","43% of 616","81% of 26","92% of 109","91% of 150","98% of 42","95% of 284","96% of 339","96% of 360"]],["det_without",["97% of 638","97% of 639","97% of 640","97% of 380","97% of 359","97% of 373","62% of 963","59% of 880","58% of 839","61% of 947","50% of 705","45% of 650","44% of 629"]],["subs",["T&gt;A 351","A&gt;C 350","A&gt;T 349","G&gt;A 609","M&gt;T 416, M&gt;G 214","Y&gt;G 489, Y&gt;A 127","B&gt;A 26","B&gt;A 109","G&gt;A 148, G&gt;C 2","T&gt;C 41, T&gt;G 1","Y&gt;G 267, Y&gt;A 17","Y&gt;A 172, Y&gt;G 167","H&gt;G 360"]],["zone",["no","yes","yes","yes","no","no","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p22155","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p22156"}}},"glyph":{"type":"object","name":"Rect","id":"p22151","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p22152","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p22153","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p22125","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p22139"},{"type":"object","name":"BoxZoomTool","id":"p22140","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p22141","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p22147","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p22146","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p22148","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p22149"},{"type":"object","name":"SaveTool","id":"p22150"},{"type":"object","name":"HoverTool","id":"p22157","attributes":{"renderers":[{"id":"p22154"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p22134","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p22135"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p22136"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22137"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p22129","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p22158","attributes":{"ticks":[-24,-21,-19,-18,-15,-14,-12,-9,-6,-3,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p22131"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-14,"14"],[-2,"2"],[-1,"1"],[-3,"3"],[-21,"21"],[-6,"6"],[-9,"9"],[-24,"24"],[-18,"18"],[-19,"19"],[-15,"15"],[-12,"12"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p22132"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p22133","attributes":{"axis":{"id":"p22129"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p22138","attributes":{"dimension":1,"axis":{"id":"p22134"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"78214fb4-283c-494e-9fba-6bb8ac346fb2","roots":{"p22117":"c9d18e79-f46c-4363-b0bd-b21cd90acee0"},"root_ids":["p22117"]}];
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

<div id="e3d0191e-cb38-4643-ad15-647819e1b559" data-root-id="p22164" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"971d0039-e59f-4b36-a85c-5239cf8e3562":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p22213","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p22214"}}},"roots":[{"type":"object","name":"Figure","id":"p22164","attributes":{"height":132,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p22173","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p22174","attributes":{"factors":["Orthoreovirus piscis (3431498)","Orthoreovirus avis (3431493)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p22175"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p22176"},"title":{"type":"object","name":"Title","id":"p22171","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p22208","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p22161","attributes":{"selected":{"type":"object","name":"Selection","id":"p22162","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p22163"},"data":{"type":"map","entries":[["y",["Orthoreovirus piscis (3431498)","Orthoreovirus avis (3431493)"]],["share",[0.0,97.91666666666666]],["lo",[0.0,94.0542467130496]],["hi",[2.067062347159301,99.2889880607427]],["n",[182,144]],["det",[0,141]],["colour",["#b3261e","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p22209","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p22210"}}},"glyph":{"type":"object","name":"Scatter","id":"p22205","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p22206","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p22207","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p22172","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p22187"},{"type":"object","name":"BoxZoomTool","id":"p22188","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p22189","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p22195","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p22194","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p22196","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p22197"},{"type":"object","name":"SaveTool","id":"p22198"},{"type":"object","name":"HoverTool","id":"p22212","attributes":{"renderers":[{"id":"p22208"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p22182","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p22183"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p22184"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22185"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p22177","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p22178","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p22179"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22180"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p22181","attributes":{"axis":{"id":"p22177"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p22186","attributes":{"dimension":1,"axis":{"id":"p22182"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p22199","attributes":{"source":{"id":"p22161"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p22211","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"971d0039-e59f-4b36-a85c-5239cf8e3562","roots":{"p22164":"e3d0191e-cb38-4643-ad15-647819e1b559"},"root_ids":["p22164"]}];
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

Disclosures on this entry: `conditions_not_printed`, `pairing_is_curator_reading`.


## What reached the statistics

14,479 records were screened for this assay and **985 (7%)** were evaluable, meaning both primers landed in the right orientation and size range. 13,494 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 13,170 |
| `chance_anchor` | 265 |
| `truncated` | 59 |

