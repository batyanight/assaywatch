# ORTHOBORNAVIRUS_XP_psittacine_Sigrist_2021

<span class="aw-chip aw-chip-stable">stable</span>

**AVIAN ORTHOBORNAVIRUS — X/P triplex qPCR, psittacine probe (Sigrist 2021)**

| | |
|---|---|
| Target | Orthobornavirus ([taxid 186458](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=186458)) |
| Gene | X/P |
| Chemistry | hydrolysis_probe |
| Amplicon | 123 bp |
| Designed | 2021 |
| Paper | [10.3390/v13071358](https://doi.org/10.3390/v13071358) |
| Registry status | active |

!!! quote "The paper"
    Sigrist, B., Geers, J., Albini, S., Rubbenstroth, D. & Wolfrum, N. A New Multiplex Real-Time RT-PCR for Simultaneous Detection and Differentiation of Avian Bornaviruses. Viruses 13, 1358 (2021).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CCCGCAGACAGYACGT` | 16 nt |
| reverse | `GAGATCATGGANGGRTTCTT` | 20 nt |
| probe | `CGAATWCCCAGGGAGGCYCT` | 20 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 35 | 35 | 100.0% | 90.1% – 100.0% |
| baseline (everything earlier) | 58 | 59 | 98.3% | 91.0% – 99.7% |

Change from baseline, Newcombe interval: **-8.3% to 9.0%**. Threshold: **90.0%**.

*detected share 100.0% (90%-100%) since Oct 2021 (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record rising (p=0.0521, 15 years); by footprint rising (p=0.107). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="d8b44f2c-da02-491d-91c1-def5da316043" data-root-id="p20580" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"185a8674-08d0-4d2b-89a4-b5b7a16e7a45":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20635","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20636"}}},"roots":[{"type":"object","name":"Figure","id":"p20580","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p20582"},"y_range":{"type":"object","name":"Range1d","id":"p20589","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p20590"},"y_scale":{"type":"object","name":"LinearScale","id":"p20591"},"title":{"type":"object","name":"Title","id":"p20587","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20625","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20577","attributes":{"selected":{"type":"object","name":"Selection","id":"p20578","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20579"},"data":{"type":"map","entries":[["year",[2008,2009,2010,2011,2012,2016,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[66.66666666666666,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[2,2,3,9,11,11,1,12,6,24,2,1,3,4,2]],["evaluable",[3,2,3,9,11,11,1,12,6,24,2,1,3,4,2]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent","recent","recent"]],["size",[9.328625426046248,9.07684386569143,9.328625426046248,10.071067811865476,10.209683151927734,10.209683151927734,8.703135093227193,10.269703144398052,9.791719296345839,10.74264168206181,9.07684386569143,8.703135093227193,9.328625426046248,9.517227179437622,9.07684386569143]]]}}},"view":{"type":"object","name":"CDSView","id":"p20626","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20627"}}},"glyph":{"type":"object","name":"Line","id":"p20622","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p20623","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p20624","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p20631","attributes":{"data_source":{"id":"p20577"},"view":{"type":"object","name":"CDSView","id":"p20632","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20633"}}},"glyph":{"type":"object","name":"Scatter","id":"p20628","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p20629","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p20630","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20588","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20602"},{"type":"object","name":"BoxZoomTool","id":"p20603","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20604","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20610","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20609","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20611","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20612"},{"type":"object","name":"SaveTool","id":"p20613"},{"type":"object","name":"HoverTool","id":"p20634","attributes":{"renderers":[{"id":"p20631"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p20597","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20598","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20599"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20600"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20592","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20593","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20594"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20595"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20596","attributes":{"axis":{"id":"p20592"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20601","attributes":{"dimension":1,"axis":{"id":"p20597"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p20614","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2020.5,"right":{"type":"object","name":"Node","id":"p20616","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p20617","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p20618","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p20620","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20619","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p20621","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"185a8674-08d0-4d2b-89a4-b5b7a16e7a45","roots":{"p20580":"d8b44f2c-da02-491d-91c1-def5da316043"},"root_ids":["p20580"]}];
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

<div id="b3c521cc-a5d9-4c22-a847-b4f41544af93" data-root-id="p20640" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"0fae1331-0f17-47a3-acec-77785406de76":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20680","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20681"}}},"roots":[{"type":"object","name":"Figure","id":"p20640","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p20641"},"y_range":{"type":"object","name":"DataRange1d","id":"p20642","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p20649"},"y_scale":{"type":"object","name":"LinearScale","id":"p20650"},"title":{"type":"object","name":"Title","id":"p20647","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20676","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20637","attributes":{"selected":{"type":"object","name":"Selection","id":"p20638","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20639"},"data":{"type":"map","entries":[["year",[2008,2009,2010,2011,2012,2016,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[3,2,3,9,11,11,1,12,6,24,2,1,3,4,2]],["detected",[2,2,3,9,11,11,1,12,6,24,2,1,3,4,2]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p20677","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20678"}}},"glyph":{"type":"object","name":"VBar","id":"p20673","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p20674","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p20675","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20648","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20661"},{"type":"object","name":"BoxZoomTool","id":"p20662","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20663","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20669","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20668","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20670","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20671"},{"type":"object","name":"SaveTool","id":"p20672"},{"type":"object","name":"HoverTool","id":"p20679","attributes":{"renderers":[{"id":"p20676"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p20656","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20657","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20658"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20659"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20651","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20652","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20653"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20654"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20655","attributes":{"axis":{"id":"p20651"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20660","attributes":{"dimension":1,"axis":{"id":"p20656"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"0fae1331-0f17-47a3-acec-77785406de76","roots":{"p20640":"b3c521cc-a5d9-4c22-a847-b4f41544af93"},"root_ids":["p20640"]}];
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

<div id="c8a0298f-8609-4dc6-a3e9-aad20ed9522f" data-root-id="p20685" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"599f04ca-d9ac-497e-a143-7f8fa25febcf":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20727","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20728"}}},"roots":[{"type":"object","name":"Figure","id":"p20685","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p20687"},"y_range":{"type":"object","name":"FactorRange","id":"p20694","attributes":{"factors":["probe","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p20695"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p20696"},"title":{"type":"object","name":"Title","id":"p20692","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20722","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20682","attributes":{"selected":{"type":"object","name":"Selection","id":"p20683","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20684"},"data":{"type":"map","entries":[["x",[-6,-1,-13,-14,-16,-18]],["y",["forward","forward","forward","forward","forward","probe"]],["alpha",[1.0,1.0,1.0,1.0,1.0,0.9457446808510639]],["pos",[6,1,13,14,16,18]],["base",["G","T","G","C","C","A"]],["n",[361,354,350,40,27,22]],["det_with",["0% of 361","0% of 354","0% of 350","0% of 40","0% of 27","36% of 22"]],["det_without",["53% of 175","51% of 182","50% of 186","19% of 496","18% of 509","17% of 514"]],["subs",["G&gt;C 348, G&gt;T 13","T&gt;A 349, T&gt;C 5","G&gt;C 349, G&gt;A 1","C&gt;T 40","C&gt;T 27","A&gt;G 19, A&gt;C 3"]],["zone",["no","yes","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p20723","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20724"}}},"glyph":{"type":"object","name":"Rect","id":"p20719","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p20720","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p20721","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20693","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20707"},{"type":"object","name":"BoxZoomTool","id":"p20708","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20709","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20715","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20714","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20716","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20717"},{"type":"object","name":"SaveTool","id":"p20718"},{"type":"object","name":"HoverTool","id":"p20725","attributes":{"renderers":[{"id":"p20722"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p20702","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p20703"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p20704"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20705"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20697","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p20726","attributes":{"ticks":[-18,-16,-14,-13,-6,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20699"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-6,"6"],[-1,"1"],[-13,"13"],[-14,"14"],[-16,"16"],[-18,"18"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p20700"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20701","attributes":{"axis":{"id":"p20697"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20706","attributes":{"dimension":1,"axis":{"id":"p20702"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"599f04ca-d9ac-497e-a143-7f8fa25febcf","roots":{"p20685":"c8a0298f-8609-4dc6-a3e9-aad20ed9522f"},"root_ids":["p20685"]}];
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

<div id="b1a059ec-e56e-45aa-a54d-aabe67ea8075" data-root-id="p20732" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"bd7e0eaa-78e9-49da-a78c-dfd7d9fa27c0":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p20781","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p20782"}}},"roots":[{"type":"object","name":"Figure","id":"p20732","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p20741","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p20742","attributes":{"factors":["Orthobornavirus alphapsittaciforme (1548713)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p20743"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p20744"},"title":{"type":"object","name":"Title","id":"p20739","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p20776","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p20729","attributes":{"selected":{"type":"object","name":"Selection","id":"p20730","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p20731"},"data":{"type":"map","entries":[["y",["Orthobornavirus alphapsittaciforme (1548713)"]],["share",[100.0]],["lo",[90.1099007675596]],["hi",[100.0]],["n",[35]],["det",[35]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p20777","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p20778"}}},"glyph":{"type":"object","name":"Scatter","id":"p20773","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p20774","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p20775","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p20740","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p20755"},{"type":"object","name":"BoxZoomTool","id":"p20756","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p20757","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p20763","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p20762","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p20764","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p20765"},{"type":"object","name":"SaveTool","id":"p20766"},{"type":"object","name":"HoverTool","id":"p20780","attributes":{"renderers":[{"id":"p20776"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p20750","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p20751"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p20752"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20753"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p20745","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p20746","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p20747"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p20748"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p20749","attributes":{"axis":{"id":"p20745"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p20754","attributes":{"dimension":1,"axis":{"id":"p20750"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p20767","attributes":{"source":{"id":"p20729"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p20779","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"bd7e0eaa-78e9-49da-a78c-dfd7d9fa27c0","roots":{"p20732":"b1a059ec-e56e-45aa-a54d-aabe67ea8075"},"root_ids":["p20732"]}];
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

This entry declares **`scope_taxids`**: [1548713](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1548713). A record counts toward the denominator when its taxid, or any ancestor, is in that set. Records outside it are screened and reported but kept out of the statistics.

721 screened records fell outside the declared scope.

Disclosures on this entry: `oligos_read_from_figure`.


## What reached the statistics

639 records were screened for this assay and **94 (15%)** were evaluable, meaning both primers landed in the right orientation and size range. 545 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 545 |

