# POXVIRUSES_dsDNA_Polymerase

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**POXVIRUSES (dsDNA) — Polymerase**

| | |
|---|---|
| Target | Chordopoxvirinae ([taxid 10241](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10241)) |
| Gene | Polymerase |
| Chemistry | conventional |
| Amplicon | 543 bp |
| Designed | 2006 |
| Paper | [10.1007/s00705-005-0679-6](https://doi.org/10.1007/s00705-005-0679-6) |
| Registry status | active |

!!! quote "The paper"
    Bracht, A. J. et al. Genetic identification of novel poxviruses of cetaceans and pinnipeds. Archives of virology 151, 423-438, doi:Doi 10.1007/s00705-005-0679-6 (2006).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ATACAGAGCTAGTACNTTAATAAAAG` | 26 nt |
| reverse | `CTATTTTTAAATCCCATTAAACC` | 23 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 209 | 5,667 | 3.7% | 3.2% – 4.2% |
| baseline (everything earlier) | 240 | 9,314 | 2.6% | 2.3% – 2.9% |

Change from baseline, Newcombe interval: **0.5% to 1.7%**. Threshold: **90.0%**.

*detected share 3.7% (3%-4%) since Oct 2024, upper bound below the 90% threshold; change from baseline +0.5% to +2% (rose from a baseline of 3%); separately, lineage Orthopoxvirus monkeypox (3431483) (5394 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift*

Trend across deposit years: by record falling (p=2.76e-31, 33 years); by footprint rising (p=0.492); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="a6ea0734-75ea-4f15-a07c-18cd5efb1f97" data-root-id="p24326" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"c5bcd64d-c6f9-4f67-a431-4ffa3abc5085":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p24381","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p24382"}}},"roots":[{"type":"object","name":"Figure","id":"p24326","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p24328"},"y_range":{"type":"object","name":"Range1d","id":"p24335","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p24336"},"y_scale":{"type":"object","name":"LinearScale","id":"p24337"},"title":{"type":"object","name":"Title","id":"p24333","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p24371","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p24323","attributes":{"selected":{"type":"object","name":"Selection","id":"p24324","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p24325"},"data":{"type":"map","entries":[["year",[1990,1991,1993,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[0.0,0.0,0.0,0.0,0.0,0.0,0.0,33.33333333333333,68.75,50.0,37.5,30.434782608695656,0.0,0.0,0.0,100.0,0.0,6.666666666666667,0.0,19.718309859154928,1.3888888888888888,0.0,28.57142857142857,6.493506493506493,12.121212121212121,15.384615384615385,21.73913043478261,40.0,0.8879977083930106,2.009419152276295,2.0910780669144984,4.367201426024955,3.0995616781465247]],["detected",[0,0,0,0,0,0,0,2,11,4,3,7,0,0,0,1,0,1,0,14,1,0,6,5,8,16,15,18,31,64,45,98,99]],["evaluable",[1,1,2,1,2,6,3,6,16,8,8,23,19,6,1,1,8,15,37,71,72,26,21,77,66,104,69,45,3491,3185,2152,2244,3194]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.07684386569143,8.703135093227193,9.07684386569143,9.791719296345839,9.328625426046248,9.791719296345839,10.467343773689333,9.989711205477885,9.989711205477885,10.713966621835368,10.584573151575475,9.791719296345839,8.703135093227193,8.703135093227193,9.989711205477885,10.423139468338052,11.030852377887435,11.451823022921252,11.460677957646856,10.796415465069488,10.652487636092928,11.503079740144862,11.405466677556973,11.690784341861697,11.433709207718536,11.15897945775324,13.657244290896138,13.610426206643531,13.407982549254546,13.4297846877816,13.611869371715827]]]}}},"view":{"type":"object","name":"CDSView","id":"p24372","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p24373"}}},"glyph":{"type":"object","name":"Line","id":"p24368","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p24369","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p24370","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p24377","attributes":{"data_source":{"id":"p24323"},"view":{"type":"object","name":"CDSView","id":"p24378","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p24379"}}},"glyph":{"type":"object","name":"Scatter","id":"p24374","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p24375","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p24376","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p24334","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p24348"},{"type":"object","name":"BoxZoomTool","id":"p24349","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p24350","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p24356","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p24355","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p24357","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p24358"},{"type":"object","name":"SaveTool","id":"p24359"},{"type":"object","name":"HoverTool","id":"p24380","attributes":{"renderers":[{"id":"p24377"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p24343","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p24344","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p24345"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p24346"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p24338","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p24339","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p24340"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p24341"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p24342","attributes":{"axis":{"id":"p24338"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p24347","attributes":{"dimension":1,"axis":{"id":"p24343"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p24360","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p24362","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p24363","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p24364","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p24366","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p24365","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p24367","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"c5bcd64d-c6f9-4f67-a431-4ffa3abc5085","roots":{"p24326":"a6ea0734-75ea-4f15-a07c-18cd5efb1f97"},"root_ids":["p24326"]}];
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

<div id="ac55281c-dd20-4f07-92dd-50a847ffb443" data-root-id="p24386" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"f2da2c7e-e056-4bf4-97c9-374565d026e3":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p24426","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p24427"}}},"roots":[{"type":"object","name":"Figure","id":"p24386","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p24387"},"y_range":{"type":"object","name":"DataRange1d","id":"p24388","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p24395"},"y_scale":{"type":"object","name":"LinearScale","id":"p24396"},"title":{"type":"object","name":"Title","id":"p24393","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p24422","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p24383","attributes":{"selected":{"type":"object","name":"Selection","id":"p24384","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p24385"},"data":{"type":"map","entries":[["year",[1990,1991,1993,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,2,1,2,6,3,6,16,8,8,23,19,6,1,1,8,15,37,71,72,26,21,77,66,104,69,45,3491,3185,2152,2244,3194]],["detected",[0,0,0,0,0,0,0,2,11,4,3,7,0,0,0,1,0,1,0,14,1,0,6,5,8,16,15,18,31,64,45,98,99]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p24423","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p24424"}}},"glyph":{"type":"object","name":"VBar","id":"p24419","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p24420","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p24421","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p24394","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p24407"},{"type":"object","name":"BoxZoomTool","id":"p24408","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p24409","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p24415","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p24414","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p24416","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p24417"},{"type":"object","name":"SaveTool","id":"p24418"},{"type":"object","name":"HoverTool","id":"p24425","attributes":{"renderers":[{"id":"p24422"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p24402","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p24403","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p24404"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p24405"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p24397","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p24398","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p24399"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p24400"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p24401","attributes":{"axis":{"id":"p24397"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p24406","attributes":{"dimension":1,"axis":{"id":"p24402"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"f2da2c7e-e056-4bf4-97c9-374565d026e3","roots":{"p24386":"ac55281c-dd20-4f07-92dd-50a847ffb443"},"root_ids":["p24386"]}];
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

<div id="abf4e801-f2a3-4fe7-b23e-52abed53f467" data-root-id="p24431" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"6a44287d-c99d-45e4-abfb-ba6627235236":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p24473","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p24474"}}},"roots":[{"type":"object","name":"Figure","id":"p24431","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p24433"},"y_range":{"type":"object","name":"FactorRange","id":"p24440","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p24441"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p24442"},"title":{"type":"object","name":"Title","id":"p24438","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p24468","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p24428","attributes":{"selected":{"type":"object","name":"Selection","id":"p24429","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p24430"},"data":{"type":"map","entries":[["x",[-5,-8,-17,-10,-17,-23,-4,-2,-6,-20,-18,-21,-22,-12,-15,-3]],["y",["forward","forward","forward","forward","reverse","forward","reverse","forward","reverse","forward","reverse","reverse","forward","reverse","reverse","reverse"]],["alpha",[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.2128662973099259,0.21218543488418662,0.20787330618783792,0.18517789199652893,0.1545390828382618,0.16634069821774247,0.213093251451839]],["pos",[5,8,17,10,17,23,4,2,6,20,18,21,22,12,15,3]],["base",["A","A","T","T","T","C","A","A","T","A","T","A","A","T","A","A"]],["n",[14648,14641,14625,14491,14494,14549,14373,14366,14366,277,274,255,155,20,72,278]],["det_with",["0% of 14648","0% of 14641","0% of 14625","0% of 14491","0% of 14494","0% of 14549","0% of 14373","0% of 14366","0% of 14366","0% of 277","0% of 274","0% of 255","0% of 155","0% of 20","1% of 72","2% of 278"]],["det_without",["98% of 460","96% of 467","93% of 483","72% of 617","72% of 614","71% of 559","61% of 735","61% of 742","61% of 742","3% of 14831","3% of 14834","3% of 14853","3% of 14953","3% of 15088","3% of 15036","3% of 14830"]],["subs",["A&gt;C 14528, A&gt;T 120","A&gt;C 14361, A&gt;G 155, A&gt;T 125","T&gt;G 14350, T&gt;C 262, T&gt;A 13","T&gt;A 10519, T&gt;G 3849, T&gt;C 123","T&gt;C 14494","C&gt;T 14549","A&gt;G 14373","A&gt;G 14366","T&gt;C 14356, T&gt;A 8, T&gt;G 2","A&gt;G 271, A&gt;T 6","T&gt;C 153, T&gt;A 119, T&gt;G 2","A&gt;G 255","A&gt;C 155","T&gt;A 12, T&gt;C 8","A&gt;G 71, A&gt;T 1","A&gt;C 160, A&gt;T 116, A&gt;G 2"]],["zone",["yes","no","no","no","no","no","yes","yes","no","no","no","no","no","no","no","yes"]]]}}},"view":{"type":"object","name":"CDSView","id":"p24469","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p24470"}}},"glyph":{"type":"object","name":"Rect","id":"p24465","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p24466","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p24467","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p24439","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p24453"},{"type":"object","name":"BoxZoomTool","id":"p24454","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p24455","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p24461","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p24460","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p24462","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p24463"},{"type":"object","name":"SaveTool","id":"p24464"},{"type":"object","name":"HoverTool","id":"p24471","attributes":{"renderers":[{"id":"p24468"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p24448","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p24449"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p24450"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p24451"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p24443","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p24472","attributes":{"ticks":[-23,-22,-21,-20,-18,-17,-15,-12,-10,-8,-6,-5,-4,-3,-2],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p24445"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-5,"5"],[-8,"8"],[-17,"17"],[-10,"10"],[-23,"23"],[-4,"4"],[-2,"2"],[-6,"6"],[-20,"20"],[-18,"18"],[-21,"21"],[-22,"22"],[-12,"12"],[-15,"15"],[-3,"3"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p24446"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p24447","attributes":{"axis":{"id":"p24443"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p24452","attributes":{"dimension":1,"axis":{"id":"p24448"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"6a44287d-c99d-45e4-abfb-ba6627235236","roots":{"p24431":"abf4e801-f2a3-4fe7-b23e-52abed53f467"},"root_ids":["p24431"]}];
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

<div id="c8716ded-2168-4fc3-8c5f-9bc5f36c0c15" data-root-id="p24478" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"af1629cf-56d0-45c5-801a-d5b7f5d40192":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p24527","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p24528"}}},"roots":[{"type":"object","name":"Figure","id":"p24478","attributes":{"height":132,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p24487","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p24488","attributes":{"factors":["Orthopoxvirus monkeypox (3431483)","Capripoxvirus lumpyskinpox (3427718)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p24489"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p24490"},"title":{"type":"object","name":"Title","id":"p24485","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p24522","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p24475","attributes":{"selected":{"type":"object","name":"Selection","id":"p24476","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p24477"},"data":{"type":"map","entries":[["y",["Orthopoxvirus monkeypox (3431483)","Capripoxvirus lumpyskinpox (3427718)"]],["share",[0.0,99.47643979057592]],["lo",[0.0,97.09442367306261]],["hi",[0.0711665737128448,99.90751890319896]],["n",[5394,191]],["det",[0,190]],["colour",["#b3261e","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p24523","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p24524"}}},"glyph":{"type":"object","name":"Scatter","id":"p24519","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p24520","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p24521","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p24486","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p24501"},{"type":"object","name":"BoxZoomTool","id":"p24502","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p24503","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p24509","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p24508","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p24510","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p24511"},{"type":"object","name":"SaveTool","id":"p24512"},{"type":"object","name":"HoverTool","id":"p24526","attributes":{"renderers":[{"id":"p24522"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p24496","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p24497"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p24498"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p24499"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p24491","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p24492","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p24493"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p24494"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p24495","attributes":{"axis":{"id":"p24491"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p24500","attributes":{"dimension":1,"axis":{"id":"p24496"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p24513","attributes":{"source":{"id":"p24475"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p24525","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"af1629cf-56d0-45c5-801a-d5b7f5d40192","roots":{"p24478":"c8716ded-2168-4fc3-8c5f-9bc5f36c0c15"},"root_ids":["p24478"]}];
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

28,428 records were screened for this assay and **14,981 (53%)** were evaluable, meaning both primers landed in the right orientation and size range. 13,447 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 13,104 |
| `chance_anchor` | 242 |
| `truncated` | 97 |
| `no_pair` | 3 |

