# MONKEYPOX_dsDNA_G2R_generic_TaqMan_Li_2010

<span class="aw-chip aw-chip-stable">stable</span>

**MONKEYPOX virus (dsDNA) — G2R_G generic TaqMan (Li 2010)**

| | |
|---|---|
| Target | Monkeypox virus ([taxid 10244](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10244)) |
| Gene | TNF receptor (G2R), inverted terminal repeat |
| Chemistry | hydrolysis_probe |
| Amplicon | 90 bp |
| Designed | 2010 |
| Paper | [10.1016/j.jviromet.2010.07.012](https://doi.org/10.1016/j.jviromet.2010.07.012) |
| Registry status | draft |

!!! quote "The paper"
    Li Y, Zhao H, Wilkins K, Hughes C, Damon IK. 2010. Real-time PCR assays for the specific detection of monkeypox virus West African and Congo Basin strain DNA. J Virol Methods 169:223-227

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GGAAAATGTAAAGACAACGAATACAG` | 26 nt |
| reverse | `GCTATCACATAATCTGGAAGCGTA` | 24 nt |
| probe | `AAGCCGTAATCTATGTTGTCTATCGTGTCC` | 30 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 4,597 | 4,762 | 96.5% | 96.0% – 97.0% |
| baseline (everything earlier) | 7,879 | 7,987 | 98.6% | 98.4% – 98.9% |

Change from baseline, Newcombe interval: **-2.7% to -1.6%**. Threshold: **90.0%**.

*detected share 96.5% (96%-97%) since Oct 2024*

Trend across deposit years: by record falling (p=6.43e-13, 16 years); by footprint rising (p=0.965); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="c736680a-a57c-4d5a-902d-834529391e55" data-root-id="p17867" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"30c414f7-8fc9-4735-94a7-4eaaa9076dcc":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17922","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17923"}}},"roots":[{"type":"object","name":"Figure","id":"p17867","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p17869"},"y_range":{"type":"object","name":"Range1d","id":"p17876","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p17877"},"y_scale":{"type":"object","name":"LinearScale","id":"p17878"},"title":{"type":"object","name":"Title","id":"p17874","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17912","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17864","attributes":{"selected":{"type":"object","name":"Selection","id":"p17865","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17866"},"data":{"type":"map","entries":[["year",[1998,2001,2004,2005,2010,2011,2013,2014,2015,2019,2020,2022,2023,2024,2025,2026]],["share",[92.3076923076923,100.0,50.0,100.0,20.0,100.0,100.0,100.0,100.0,100.0,100.0,99.9083689676237,99.35571380128857,95.70354457572503,97.1919770773639,95.86600142551674]],["detected",[12,2,1,7,1,2,2,24,11,8,37,3271,2930,1782,1696,2690]],["evaluable",[13,2,2,7,5,2,2,24,11,8,37,3274,2949,1862,1745,2806]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[10.324834530005162,9.07684386569143,9.07684386569143,9.897626379762722,9.667366891029102,9.07684386569143,9.07684386569143,10.74264168206181,10.209683151927734,9.989711205477885,11.030852377887435,13.624513288061483,13.570976794953912,13.332246675936752,13.298111767903801,13.545428408360705]]]}}},"view":{"type":"object","name":"CDSView","id":"p17913","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17914"}}},"glyph":{"type":"object","name":"Line","id":"p17909","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p17910","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p17911","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p17918","attributes":{"data_source":{"id":"p17864"},"view":{"type":"object","name":"CDSView","id":"p17919","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17920"}}},"glyph":{"type":"object","name":"Scatter","id":"p17915","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p17916","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p17917","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17875","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17889"},{"type":"object","name":"BoxZoomTool","id":"p17890","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17891","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17897","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17896","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17898","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17899"},{"type":"object","name":"SaveTool","id":"p17900"},{"type":"object","name":"HoverTool","id":"p17921","attributes":{"renderers":[{"id":"p17918"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p17884","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17885","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17886"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17887"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17879","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17880","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17881"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17882"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17883","attributes":{"axis":{"id":"p17879"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17888","attributes":{"dimension":1,"axis":{"id":"p17884"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p17901","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p17903","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p17904","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p17905","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p17907","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17906","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p17908","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"30c414f7-8fc9-4735-94a7-4eaaa9076dcc","roots":{"p17867":"c736680a-a57c-4d5a-902d-834529391e55"},"root_ids":["p17867"]}];
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

<div id="a0ccfbac-7ca5-4eca-8600-c1da36b0d09d" data-root-id="p17927" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"c1a3da25-b87d-4f57-8b61-2d48b3b192d4":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17967","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17968"}}},"roots":[{"type":"object","name":"Figure","id":"p17927","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p17928"},"y_range":{"type":"object","name":"DataRange1d","id":"p17929","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p17936"},"y_scale":{"type":"object","name":"LinearScale","id":"p17937"},"title":{"type":"object","name":"Title","id":"p17934","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17963","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17924","attributes":{"selected":{"type":"object","name":"Selection","id":"p17925","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17926"},"data":{"type":"map","entries":[["year",[1998,2001,2004,2005,2010,2011,2013,2014,2015,2019,2020,2022,2023,2024,2025,2026]],["evaluable",[13,2,2,7,5,2,2,24,11,8,37,3274,2949,1862,1745,2806]],["detected",[12,2,1,7,1,2,2,24,11,8,37,3271,2930,1782,1696,2690]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p17964","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17965"}}},"glyph":{"type":"object","name":"VBar","id":"p17960","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p17961","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p17962","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17935","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17948"},{"type":"object","name":"BoxZoomTool","id":"p17949","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17950","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17956","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17955","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17957","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17958"},{"type":"object","name":"SaveTool","id":"p17959"},{"type":"object","name":"HoverTool","id":"p17966","attributes":{"renderers":[{"id":"p17963"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p17943","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17944","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17945"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17946"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17938","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17939","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17940"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17941"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17942","attributes":{"axis":{"id":"p17938"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17947","attributes":{"dimension":1,"axis":{"id":"p17943"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"c1a3da25-b87d-4f57-8b61-2d48b3b192d4","roots":{"p17927":"a0ccfbac-7ca5-4eca-8600-c1da36b0d09d"},"root_ids":["p17927"]}];
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

<div id="ff9fa412-93ec-42c2-a59a-11fd6227c5e9" data-root-id="p17972" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"63bfe555-43bb-491b-bb77-1b3c117075b7":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p18014","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p18015"}}},"roots":[{"type":"object","name":"Figure","id":"p17972","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p17974"},"y_range":{"type":"object","name":"FactorRange","id":"p17981","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p17982"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p17983"},"title":{"type":"object","name":"Title","id":"p17979","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p18009","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17969","attributes":{"selected":{"type":"object","name":"Selection","id":"p17970","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17971"},"data":{"type":"map","entries":[["x",[-21,-8]],["y",["forward","reverse"]],["alpha",[1.0,1.0]],["pos",[21,8]],["base",["A","G"]],["n",[9573,8958]],["det_with",["100% of 9573","100% of 8958"]],["det_without",["100% of 2913","100% of 3528"]],["subs",["A&gt;G 9573","G&gt;A 8958"]],["zone",["no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p18010","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p18011"}}},"glyph":{"type":"object","name":"Rect","id":"p18006","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p18007","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p18008","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17980","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17994"},{"type":"object","name":"BoxZoomTool","id":"p17995","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17996","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p18002","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p18001","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p18003","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p18004"},{"type":"object","name":"SaveTool","id":"p18005"},{"type":"object","name":"HoverTool","id":"p18012","attributes":{"renderers":[{"id":"p18009"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p17989","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p17990"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p17991"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17992"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17984","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p18013","attributes":{"ticks":[-21,-8],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17986"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-21,"21"],[-8,"8"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p17987"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17988","attributes":{"axis":{"id":"p17984"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17993","attributes":{"dimension":1,"axis":{"id":"p17989"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"63bfe555-43bb-491b-bb77-1b3c117075b7","roots":{"p17972":"ff9fa412-93ec-42c2-a59a-11fd6227c5e9"},"root_ids":["p17972"]}];
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

<div id="e47fa131-2d42-4ccb-b6ef-010e179362d6" data-root-id="p18019" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"df46d755-9bb9-4a6e-a2a6-7f52f74f2ec7":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p18068","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p18069"}}},"roots":[{"type":"object","name":"Figure","id":"p18019","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p18028","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p18029","attributes":{"factors":["Orthopoxvirus monkeypox (3431483)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p18030"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p18031"},"title":{"type":"object","name":"Title","id":"p18026","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p18063","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p18016","attributes":{"selected":{"type":"object","name":"Selection","id":"p18017","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p18018"},"data":{"type":"map","entries":[["y",["Orthopoxvirus monkeypox (3431483)"]],["share",[100.0]],["lo",[99.91650529897461]],["hi",[100.0]],["n",[4597]],["det",[4597]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p18064","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p18065"}}},"glyph":{"type":"object","name":"Scatter","id":"p18060","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p18061","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p18062","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p18027","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p18042"},{"type":"object","name":"BoxZoomTool","id":"p18043","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p18044","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p18050","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p18049","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p18051","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p18052"},{"type":"object","name":"SaveTool","id":"p18053"},{"type":"object","name":"HoverTool","id":"p18067","attributes":{"renderers":[{"id":"p18063"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p18037","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p18038"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p18039"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18040"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p18032","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18033","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18034"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18035"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p18036","attributes":{"axis":{"id":"p18032"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p18041","attributes":{"dimension":1,"axis":{"id":"p18037"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p18054","attributes":{"source":{"id":"p18016"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p18066","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"df46d755-9bb9-4a6e-a2a6-7f52f74f2ec7","roots":{"p18019":"e47fa131-2d42-4ccb-b6ef-010e179362d6"},"root_ids":["p18019"]}];
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

14,204 records were screened for this assay and **12,749 (90%)** were evaluable, meaning both primers landed in the right orientation and size range. 1,455 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 1,424 |
| `truncated` | 9 |
| `no_pair` | 7 |
| `chance_anchor` | 4 |

