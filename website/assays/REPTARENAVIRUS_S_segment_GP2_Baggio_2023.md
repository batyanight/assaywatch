# REPTARENAVIRUS_S_segment_GP2_Baggio_2023

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**REPTARENAVIRUS — S segment GP2 multiplex RT-PCR, 6 forward + 7 reverse primer mix (Baggio 2023)**

| | |
|---|---|
| Target | Reptarenavirus ([taxid 1653395](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1653395)) |
| Gene | S segment, glycoprotein precursor (GP2 region) |
| Chemistry | conventional |
| Amplicon | 145 bp |
| Designed | 2023 |
| Paper | [10.3390/v15122313](https://doi.org/10.3390/v15122313) |
| Registry status | active |

!!! quote "The paper"
    Baggio, F.; Hetzel, U.; Prähauser, B.; Dervas, E.; Michalopoulou, E.; Thiele, T.; Kipar, A.; Hepojoki, J. A Multiplex RT-PCR Method for the Detection of Reptarenavirus Infection. Viruses 2023, 15, 2313.

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GTGCAGGCATAACCAATTCAC` | 21 nt |
| reverse | `CATGATCTCTAATTTCTCCTTCTTC` | 25 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 9 | 9 | 100.0% | 70.1% – 100.0% |
| baseline (everything earlier) | 100 | 105 | 95.2% | 89.3% – 97.9% |

Change from baseline, Newcombe interval: **-25.3% to 10.7%**. Threshold: **90.0%**.

*9 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (70%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record rising (p=0.0252, 9 years); by footprint rising (p=0.155). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="ab895063-69b6-45dc-9528-3a9b2f8390f8" data-root-id="p29729" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b914b6d2-6300-4949-8edb-587e0ed999d0":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p29784","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p29785"}}},"roots":[{"type":"object","name":"Figure","id":"p29729","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p29731"},"y_range":{"type":"object","name":"Range1d","id":"p29738","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p29739"},"y_scale":{"type":"object","name":"LinearScale","id":"p29740"},"title":{"type":"object","name":"Title","id":"p29736","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p29774","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p29726","attributes":{"selected":{"type":"object","name":"Selection","id":"p29727","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p29728"},"data":{"type":"map","entries":[["year",[2012,2013,2014,2015,2017,2018,2020,2022,2023]],["share",[50.0,100.0,100.0,95.77464788732394,100.0,100.0,100.0,100.0,100.0]],["detected",[2,2,2,68,7,15,4,8,1]],["evaluable",[4,2,2,71,7,15,4,8,1]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent"]],["size",[9.517227179437622,9.07684386569143,9.07684386569143,11.451823022921252,9.897626379762722,10.423139468338052,9.517227179437622,9.989711205477885,8.703135093227193]]]}}},"view":{"type":"object","name":"CDSView","id":"p29775","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p29776"}}},"glyph":{"type":"object","name":"Line","id":"p29771","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p29772","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p29773","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p29780","attributes":{"data_source":{"id":"p29726"},"view":{"type":"object","name":"CDSView","id":"p29781","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p29782"}}},"glyph":{"type":"object","name":"Scatter","id":"p29777","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p29778","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p29779","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p29737","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p29751"},{"type":"object","name":"BoxZoomTool","id":"p29752","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p29753","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p29759","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p29758","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p29760","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p29761"},{"type":"object","name":"SaveTool","id":"p29762"},{"type":"object","name":"HoverTool","id":"p29783","attributes":{"renderers":[{"id":"p29780"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p29746","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p29747","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p29748"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p29749"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p29741","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p29742","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p29743"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p29744"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p29745","attributes":{"axis":{"id":"p29741"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p29750","attributes":{"dimension":1,"axis":{"id":"p29746"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p29763","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2021.5,"right":{"type":"object","name":"Node","id":"p29765","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p29766","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p29767","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p29769","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p29768","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p29770","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b914b6d2-6300-4949-8edb-587e0ed999d0","roots":{"p29729":"ab895063-69b6-45dc-9528-3a9b2f8390f8"},"root_ids":["p29729"]}];
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

<div id="f3300ea5-5d71-4275-9f59-4d3a2daa47c9" data-root-id="p29789" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"33f21c35-282b-4adb-9771-5c056d6e9486":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p29829","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p29830"}}},"roots":[{"type":"object","name":"Figure","id":"p29789","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p29790"},"y_range":{"type":"object","name":"DataRange1d","id":"p29791","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p29798"},"y_scale":{"type":"object","name":"LinearScale","id":"p29799"},"title":{"type":"object","name":"Title","id":"p29796","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p29825","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p29786","attributes":{"selected":{"type":"object","name":"Selection","id":"p29787","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p29788"},"data":{"type":"map","entries":[["year",[2012,2013,2014,2015,2017,2018,2020,2022,2023]],["evaluable",[4,2,2,71,7,15,4,8,1]],["detected",[2,2,2,68,7,15,4,8,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p29826","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p29827"}}},"glyph":{"type":"object","name":"VBar","id":"p29822","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p29823","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p29824","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p29797","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p29810"},{"type":"object","name":"BoxZoomTool","id":"p29811","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p29812","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p29818","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p29817","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p29819","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p29820"},{"type":"object","name":"SaveTool","id":"p29821"},{"type":"object","name":"HoverTool","id":"p29828","attributes":{"renderers":[{"id":"p29825"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p29805","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p29806","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p29807"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p29808"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p29800","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p29801","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p29802"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p29803"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p29804","attributes":{"axis":{"id":"p29800"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p29809","attributes":{"dimension":1,"axis":{"id":"p29805"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"33f21c35-282b-4adb-9771-5c056d6e9486","roots":{"p29789":"f3300ea5-5d71-4275-9f59-4d3a2daa47c9"},"root_ids":["p29789"]}];
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

<div id="dfac5336-0209-4ae8-8506-491dbe289ba3" data-root-id="p29834" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"8f2eda25-8446-414e-bfab-2847efc339e9":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p29876","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p29877"}}},"roots":[{"type":"object","name":"Figure","id":"p29834","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p29836"},"y_range":{"type":"object","name":"FactorRange","id":"p29843","attributes":{"factors":["forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p29844"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p29845"},"title":{"type":"object","name":"Title","id":"p29841","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p29871","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p29831","attributes":{"selected":{"type":"object","name":"Selection","id":"p29832","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p29833"},"data":{"type":"map","entries":[["x",[-5]],["y",["forward"]],["alpha",[0.8061403508771929]],["pos",[5]],["base",["T"]],["n",[22]],["det_with",["100% of 22"]],["det_without",["95% of 92"]],["subs",["T&gt;C 22"]],["zone",["yes"]]]}}},"view":{"type":"object","name":"CDSView","id":"p29872","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p29873"}}},"glyph":{"type":"object","name":"Rect","id":"p29868","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p29869","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p29870","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p29842","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p29856"},{"type":"object","name":"BoxZoomTool","id":"p29857","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p29858","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p29864","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p29863","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p29865","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p29866"},{"type":"object","name":"SaveTool","id":"p29867"},{"type":"object","name":"HoverTool","id":"p29874","attributes":{"renderers":[{"id":"p29871"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p29851","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p29852"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p29853"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p29854"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p29846","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p29875","attributes":{"ticks":[-5],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p29848"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-5,"5"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p29849"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p29850","attributes":{"axis":{"id":"p29846"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p29855","attributes":{"dimension":1,"axis":{"id":"p29851"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"8f2eda25-8446-414e-bfab-2847efc339e9","roots":{"p29834":"dfac5336-0209-4ae8-8506-491dbe289ba3"},"root_ids":["p29834"]}];
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
"segment S"[Title] OR "S segment"[Title] OR nucleoprotein[Title] OR glycoprotein[Title] OR GPC[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `pooled_as_one_assay`.


## What reached the statistics

124 records were screened for this assay and **114 (92%)** were evaluable, meaning both primers landed in the right orientation and size range. 10 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 6 |
| `truncated` | 4 |

