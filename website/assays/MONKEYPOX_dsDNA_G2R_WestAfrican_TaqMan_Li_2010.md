# MONKEYPOX_dsDNA_G2R_WestAfrican_TaqMan_Li_2010

<span class="aw-chip aw-chip-declining">declining</span>

**MONKEYPOX virus (dsDNA) — G2R_WA West African clade TaqMan (Li 2010)**

| | |
|---|---|
| Target | Monkeypox virus ([taxid 10244](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10244)) |
| Gene | TNF receptor (G2R), inverted terminal repeat |
| Chemistry | hydrolysis_probe |
| Amplicon | 85 bp |
| Designed | 2010 |
| Paper | [10.1016/j.jviromet.2010.07.012](https://doi.org/10.1016/j.jviromet.2010.07.012) |
| Registry status | draft |

!!! quote "The paper"
    Li Y, Zhao H, Wilkins K, Hughes C, Damon IK. 2010. Real-time PCR assays for the specific detection of monkeypox virus West African and Congo Basin strain DNA. J Virol Methods 169:223-227

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CACACCGTCTCTTCCACAGA` | 20 nt |
| reverse | `GATACAGGTTAATTTCCACATCG` | 23 nt |
| probe | `AACCCGTCGTAACCAGCAATACATTT` | 26 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 2,000 | 4,784 | 41.8% | 40.4% – 43.2% |
| baseline (everything earlier) | 7,710 | 8,113 | 95.0% | 94.5% – 95.5% |

Change from baseline, Newcombe interval: **-54.7% to -51.7%**. Threshold: **90.0%**.

*detected share 41.8% (40%-43%) since Oct 2024, upper bound below the 90% threshold; change from baseline -55% to -52%*

Trend across deposit years: by record falling (p=0, 16 years); by footprint rising (p=0.927); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="cbb1877e-df12-4f94-b030-325b0afdddc7" data-root-id="p17708" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"3e97a4ce-b060-4f55-8ade-578dcb2c3d44":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17763","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17764"}}},"roots":[{"type":"object","name":"Figure","id":"p17708","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p17710"},"y_range":{"type":"object","name":"Range1d","id":"p17717","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p17718"},"y_scale":{"type":"object","name":"LinearScale","id":"p17719"},"title":{"type":"object","name":"Title","id":"p17715","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17753","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17705","attributes":{"selected":{"type":"object","name":"Selection","id":"p17706","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17707"},"data":{"type":"map","entries":[["year",[1998,2001,2004,2005,2010,2011,2013,2014,2015,2019,2020,2022,2023,2024,2025,2026]],["share",[69.23076923076923,0.0,50.0,71.42857142857143,0.0,0.0,0.0,4.166666666666666,45.45454545454545,100.0,72.97297297297297,99.93966817496229,99.7346600331675,81.97767145135566,57.555178268251275,27.619387027797575]],["detected",[9,0,1,5,0,0,0,1,5,8,27,3313,3007,1542,1017,775]],["evaluable",[13,2,2,7,5,2,2,24,11,8,37,3315,3015,1881,1767,2806]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[10.324834530005162,9.07684386569143,9.07684386569143,9.897626379762722,9.667366891029102,9.07684386569143,9.07684386569143,10.74264168206181,10.209683151927734,9.989711205477885,11.030852377887435,13.63086840511893,13.582333553141453,13.337576624977489,13.304710404321238,13.545428408360705]]]}}},"view":{"type":"object","name":"CDSView","id":"p17754","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17755"}}},"glyph":{"type":"object","name":"Line","id":"p17750","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p17751","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p17752","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p17759","attributes":{"data_source":{"id":"p17705"},"view":{"type":"object","name":"CDSView","id":"p17760","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17761"}}},"glyph":{"type":"object","name":"Scatter","id":"p17756","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p17757","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p17758","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17716","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17730"},{"type":"object","name":"BoxZoomTool","id":"p17731","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17732","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17738","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17737","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17739","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17740"},{"type":"object","name":"SaveTool","id":"p17741"},{"type":"object","name":"HoverTool","id":"p17762","attributes":{"renderers":[{"id":"p17759"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p17725","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17726","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17727"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17728"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17720","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17721","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17722"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17723"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17724","attributes":{"axis":{"id":"p17720"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17729","attributes":{"dimension":1,"axis":{"id":"p17725"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p17742","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p17744","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p17745","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p17746","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p17748","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17747","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p17749","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"3e97a4ce-b060-4f55-8ade-578dcb2c3d44","roots":{"p17708":"cbb1877e-df12-4f94-b030-325b0afdddc7"},"root_ids":["p17708"]}];
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

<div id="ee3f171d-8b25-4bc2-95af-8ed53a041abf" data-root-id="p17768" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"f7c133f5-011f-45b0-b773-8d389dd51da5":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17808","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17809"}}},"roots":[{"type":"object","name":"Figure","id":"p17768","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p17769"},"y_range":{"type":"object","name":"DataRange1d","id":"p17770","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p17777"},"y_scale":{"type":"object","name":"LinearScale","id":"p17778"},"title":{"type":"object","name":"Title","id":"p17775","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17804","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17765","attributes":{"selected":{"type":"object","name":"Selection","id":"p17766","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17767"},"data":{"type":"map","entries":[["year",[1998,2001,2004,2005,2010,2011,2013,2014,2015,2019,2020,2022,2023,2024,2025,2026]],["evaluable",[13,2,2,7,5,2,2,24,11,8,37,3315,3015,1881,1767,2806]],["detected",[9,0,1,5,0,0,0,1,5,8,27,3313,3007,1542,1017,775]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p17805","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17806"}}},"glyph":{"type":"object","name":"VBar","id":"p17801","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p17802","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p17803","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17776","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17789"},{"type":"object","name":"BoxZoomTool","id":"p17790","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17791","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17797","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17796","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17798","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17799"},{"type":"object","name":"SaveTool","id":"p17800"},{"type":"object","name":"HoverTool","id":"p17807","attributes":{"renderers":[{"id":"p17804"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p17784","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17785","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17786"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17787"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17779","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17780","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17781"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17782"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17783","attributes":{"axis":{"id":"p17779"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17788","attributes":{"dimension":1,"axis":{"id":"p17784"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"f7c133f5-011f-45b0-b773-8d389dd51da5","roots":{"p17768":"ee3f171d-8b25-4bc2-95af-8ed53a041abf"},"root_ids":["p17768"]}];
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

<p class="aw-empty">No position carried a mismatch in enough records to report.</p>


## By lineage

A single pooled percentage hides the clade you may actually care about:
published misses are nearly always specific to one lineage, and a clade that is
5% of deposits can be 100% of the cases in one region. Lineages with too few
records to say anything are left out.

<div id="c6343d96-c22f-4b21-bb46-802e373da095" data-root-id="p17813" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"fb8018ff-01f3-461f-af56-9c3e6d9fbd43":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17862","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17863"}}},"roots":[{"type":"object","name":"Figure","id":"p17813","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p17822","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p17823","attributes":{"factors":["Orthopoxvirus monkeypox (3431483)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p17824"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p17825"},"title":{"type":"object","name":"Title","id":"p17820","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17857","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17810","attributes":{"selected":{"type":"object","name":"Selection","id":"p17811","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17812"},"data":{"type":"map","entries":[["y",["Orthopoxvirus monkeypox (3431483)"]],["share",[42.07868714496108]],["lo",[40.6821297172943]],["hi",[43.488038523152326]],["n",[4753]],["det",[2000]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p17858","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17859"}}},"glyph":{"type":"object","name":"Scatter","id":"p17854","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p17855","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p17856","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17821","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17836"},{"type":"object","name":"BoxZoomTool","id":"p17837","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17838","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17844","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17843","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17845","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17846"},{"type":"object","name":"SaveTool","id":"p17847"},{"type":"object","name":"HoverTool","id":"p17861","attributes":{"renderers":[{"id":"p17857"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p17831","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p17832"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p17833"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17834"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17826","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17827","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17828"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17829"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17830","attributes":{"axis":{"id":"p17826"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17835","attributes":{"dimension":1,"axis":{"id":"p17831"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p17848","attributes":{"source":{"id":"p17810"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p17860","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"fb8018ff-01f3-461f-af56-9c3e6d9fbd43","roots":{"p17813":"c6343d96-c22f-4b21-bb46-802e373da095"},"root_ids":["p17813"]}];
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

14,204 records were screened for this assay and **12,897 (91%)** were evaluable, meaning both primers landed in the right orientation and size range. 1,307 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 1,291 |
| `no_pair` | 3 |
| `chance_anchor` | 3 |

