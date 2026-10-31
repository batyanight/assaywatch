# LEPTOSPIRA_lipL32_Ahmed_2020

<span class="aw-chip aw-chip-stable">stable</span>

**LEPTOSPIRA (pathogenic) — lipL32 real-time PCR (Ahmed 2020)**

| | |
|---|---|
| Target | Leptospira ([taxid 171](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=171)) |
| Gene | lipL32 |
| Chemistry | hydrolysis_probe |
| Amplicon | 114 bp |
| Designed | 2020 |
| Paper | [10.1371/journal.pone.0241584](https://doi.org/10.1371/journal.pone.0241584) |
| Registry status | active |

!!! quote "The paper"
    Ahmed, A., Goris, M. G. A. & Meijer, M. C. Development of lipL32 real-time PCR combined with an internal and extraction control for pathogenic Leptospira detection. PLOS ONE 15, e0241584 (2020).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CGCTGAAATGGGAGTTCGTATGATTTCC` | 28 nt |
| reverse | `GGCATTGATTTTTCTTCYGGGGTWGCC` | 27 nt |
| probe | `AGGCGAAATCGGKGARCCAGGCGAYGG` | 27 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 433 | 441 | 98.2% | 96.5% – 99.1% |
| baseline (everything earlier) | 1,303 | 1,496 | 87.1% | 85.3% – 88.7% |

Change from baseline, Newcombe interval: **8.7% to 13.1%**. Threshold: **90.0%**.

*detected share 98.2% (96%-99%) since Oct 2024*

Trend across deposit years: by record falling (p=0.284, 26 years); by footprint falling (p=0.0055). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="dc894ab1-4e94-4bcf-acc3-6533b1465978" data-root-id="p15749" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"7dcd28eb-9c45-4da1-ab7a-dc87c3a9054a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p15804","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p15805"}}},"roots":[{"type":"object","name":"Figure","id":"p15749","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p15751"},"y_range":{"type":"object","name":"Range1d","id":"p15758","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p15759"},"y_scale":{"type":"object","name":"LinearScale","id":"p15760"},"title":{"type":"object","name":"Title","id":"p15756","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p15794","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p15746","attributes":{"selected":{"type":"object","name":"Selection","id":"p15747","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p15748"},"data":{"type":"map","entries":[["year",[2000,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,98.27586206896551,100.0,90.0,100.0,100.0,100.0,100.0,100.0,93.44262295081968,97.27626459143968,90.32258064516128,100.0,90.3448275862069,64.19753086419753,71.42857142857143,50.0,100.0,96.47058823529412,84.95575221238938,81.68316831683168,93.42105263157895,98.0544747081712,98.07692307692307]],["detected",[6,8,4,57,3,9,2,13,10,2,35,57,250,28,19,131,52,45,54,132,82,96,165,71,252,153]],["evaluable",[6,8,4,58,3,10,2,13,10,2,35,61,257,31,19,145,81,63,108,132,85,113,202,76,257,156]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.791719296345839,9.989711205477885,9.517227179437622,11.322938200602813,9.328625426046248,10.143865699252444,9.07684386569143,10.324834530005162,10.143865699252444,9.07684386569143,10.994220569835573,11.355225445040746,12.235285195871363,10.913832791890265,10.584573151575475,11.894313992355507,11.53494852413258,11.375828278421016,11.71410709416149,11.837210590688509,11.56518892267352,11.74200327633271,12.093261293278134,11.49483773413666,12.235285195871363,11.938539663179375]]]}}},"view":{"type":"object","name":"CDSView","id":"p15795","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15796"}}},"glyph":{"type":"object","name":"Line","id":"p15791","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p15792","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p15793","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p15800","attributes":{"data_source":{"id":"p15746"},"view":{"type":"object","name":"CDSView","id":"p15801","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15802"}}},"glyph":{"type":"object","name":"Scatter","id":"p15797","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p15798","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p15799","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p15757","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p15771"},{"type":"object","name":"BoxZoomTool","id":"p15772","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p15773","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p15779","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15778","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p15780","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p15781"},{"type":"object","name":"SaveTool","id":"p15782"},{"type":"object","name":"HoverTool","id":"p15803","attributes":{"renderers":[{"id":"p15800"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p15766","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15767","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15768"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15769"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p15761","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15762","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15763"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15764"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p15765","attributes":{"axis":{"id":"p15761"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p15770","attributes":{"dimension":1,"axis":{"id":"p15766"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p15783","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p15785","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p15786","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p15787","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p15789","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15788","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p15790","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"7dcd28eb-9c45-4da1-ab7a-dc87c3a9054a","roots":{"p15749":"dc894ab1-4e94-4bcf-acc3-6533b1465978"},"root_ids":["p15749"]}];
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

<div id="c94d9759-22a7-4a23-8839-d5f466105380" data-root-id="p15809" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"f53675ca-74fa-481b-aa06-903f5298d01a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p15849","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p15850"}}},"roots":[{"type":"object","name":"Figure","id":"p15809","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p15810"},"y_range":{"type":"object","name":"DataRange1d","id":"p15811","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p15818"},"y_scale":{"type":"object","name":"LinearScale","id":"p15819"},"title":{"type":"object","name":"Title","id":"p15816","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p15845","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p15806","attributes":{"selected":{"type":"object","name":"Selection","id":"p15807","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p15808"},"data":{"type":"map","entries":[["year",[2000,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[6,8,4,58,3,10,2,13,10,2,35,61,257,31,19,145,81,63,108,132,85,113,202,76,257,156]],["detected",[6,8,4,57,3,9,2,13,10,2,35,57,250,28,19,131,52,45,54,132,82,96,165,71,252,153]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p15846","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15847"}}},"glyph":{"type":"object","name":"VBar","id":"p15842","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p15843","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p15844","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p15817","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p15830"},{"type":"object","name":"BoxZoomTool","id":"p15831","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p15832","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p15838","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15837","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p15839","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p15840"},{"type":"object","name":"SaveTool","id":"p15841"},{"type":"object","name":"HoverTool","id":"p15848","attributes":{"renderers":[{"id":"p15845"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p15825","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15826","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15827"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15828"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p15820","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15821","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15822"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15823"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p15824","attributes":{"axis":{"id":"p15820"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p15829","attributes":{"dimension":1,"axis":{"id":"p15825"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"f53675ca-74fa-481b-aa06-903f5298d01a","roots":{"p15809":"c94d9759-22a7-4a23-8839-d5f466105380"},"root_ids":["p15809"]}];
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

<div id="d2e75073-b03b-4c05-80bf-e0d7a67c530c" data-root-id="p15854" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b99ce3b5-2ae8-42e9-b150-abc3444bacf3":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p15896","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p15897"}}},"roots":[{"type":"object","name":"Figure","id":"p15854","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p15856"},"y_range":{"type":"object","name":"FactorRange","id":"p15863","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p15864"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p15865"},"title":{"type":"object","name":"Title","id":"p15861","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p15891","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p15851","attributes":{"selected":{"type":"object","name":"Selection","id":"p15852","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p15853"},"data":{"type":"map","entries":[["x",[-1,-7,-7,-22,-15,-9,-13,-20,-21,-6,-22,-19,-26,-16,-13,-21,-27,-9,-9]],["y",["reverse","reverse","forward","reverse","probe","forward","reverse","reverse","reverse","probe","forward","forward","forward","forward","forward","forward","probe","probe","reverse"]],["alpha",[0.37994321115126484,0.37116675271037686,0.23951987609705727,0.2324987093443469,0.23074341765616932,0.21845637583892616,0.2079246257098606,0.20616933402168303,0.20616933402168303,0.18686112545172948,0.18510583376355189,0.26233866804336603,0.19739287558079505,0.2693598347960764,0.21494579246257098,0.2324987093443469,0.18686112545172948,0.28340216830149717,0.29042333505420753]],["pos",[1,7,7,22,15,9,13,20,21,6,22,19,26,16,13,21,27,9,9]],["base",["C","G","G","T","K","A","T","A","G","C","A","G","C","A","T","A","A","A","G"]],["n",[131,126,51,47,46,39,33,32,32,21,20,64,27,68,37,47,21,76,80]],["det_with",["0% of 131","1% of 126","0% of 51","0% of 47","0% of 46","0% of 39","0% of 33","0% of 32","0% of 32","0% of 21","0% of 20","5% of 64","4% of 27","9% of 68","8% of 37","15% of 47","14% of 21","37% of 76","70% of 80"]],["det_without",["95% of 1824","95% of 1829","91% of 1904","91% of 1908","91% of 1909","91% of 1916","90% of 1922","90% of 1923","90% of 1923","90% of 1934","90% of 1935","92% of 1891","90% of 1928","92% of 1887","90% of 1918","91% of 1908","90% of 1934","91% of 1879","90% of 1875"]],["subs",["C&gt;A 97, C&gt;T 31, C&gt;G 3","G&gt;A 126","G&gt;A 35, G&gt;C 16","T&gt;G 41, T&gt;A 6","K&gt;C 42, K&gt;A 4","A&gt;C 38, A&gt;T 1","T&gt;C 33","A&gt;T 32","G&gt;C 28, G&gt;T 4","C&gt;T 18, C&gt;A 3","A&gt;G 19, A&gt;C 1","G&gt;A 35, G&gt;C 26, G&gt;T 3","C&gt;T 27","A&gt;T 26, A&gt;C 23, A&gt;G 19","T&gt;C 32, T&gt;G 4, T&gt;A 1","A&gt;C 27, A&gt;T 20","A&gt;T 16, A&gt;C 5","A&gt;C 42, A&gt;G 33, A&gt;T 1","G&gt;C 42, G&gt;A 35, G&gt;T 3"]],["zone",["yes","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p15892","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15893"}}},"glyph":{"type":"object","name":"Rect","id":"p15888","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p15889","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p15890","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p15862","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p15876"},{"type":"object","name":"BoxZoomTool","id":"p15877","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p15878","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p15884","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15883","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p15885","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p15886"},{"type":"object","name":"SaveTool","id":"p15887"},{"type":"object","name":"HoverTool","id":"p15894","attributes":{"renderers":[{"id":"p15891"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p15871","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p15872"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p15873"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15874"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p15866","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p15895","attributes":{"ticks":[-27,-26,-22,-21,-20,-19,-16,-15,-13,-9,-7,-6,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15868"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-1,"1"],[-7,"7"],[-22,"22"],[-15,"15"],[-9,"9"],[-13,"13"],[-20,"20"],[-21,"21"],[-6,"6"],[-19,"19"],[-26,"26"],[-16,"16"],[-27,"27"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p15869"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p15870","attributes":{"axis":{"id":"p15866"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p15875","attributes":{"dimension":1,"axis":{"id":"p15871"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b99ce3b5-2ae8-42e9-b150-abc3444bacf3","roots":{"p15854":"d2e75073-b03b-4c05-80bf-e0d7a67c530c"},"root_ids":["p15854"]}];
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

<div id="a91a7ac0-a4ee-43f5-b1d4-90589bfb57b5" data-root-id="p15901" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"dd2793db-1588-43a4-b454-adc058535a40":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p15950","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p15951"}}},"roots":[{"type":"object","name":"Figure","id":"p15901","attributes":{"height":132,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p15910","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p15911","attributes":{"factors":["Leptospira borgpetersenii (174)","Leptospira interrogans (173)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p15912"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p15913"},"title":{"type":"object","name":"Title","id":"p15908","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p15945","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p15898","attributes":{"selected":{"type":"object","name":"Selection","id":"p15899","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p15900"},"data":{"type":"map","entries":[["y",["Leptospira borgpetersenii (174)","Leptospira interrogans (173)"]],["share",[100.0,100.0]],["lo",[92.29264369144198,98.88924282421392]],["hi",[100.0,100.0]],["n",[46,342]],["det",[46,342]],["colour",["#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p15946","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15947"}}},"glyph":{"type":"object","name":"Scatter","id":"p15942","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p15943","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p15944","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p15909","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p15924"},{"type":"object","name":"BoxZoomTool","id":"p15925","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p15926","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p15932","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15931","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p15933","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p15934"},{"type":"object","name":"SaveTool","id":"p15935"},{"type":"object","name":"HoverTool","id":"p15949","attributes":{"renderers":[{"id":"p15945"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p15919","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p15920"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p15921"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15922"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p15914","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15915","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15916"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15917"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p15918","attributes":{"axis":{"id":"p15914"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p15923","attributes":{"dimension":1,"axis":{"id":"p15919"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p15936","attributes":{"source":{"id":"p15898"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p15948","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"dd2793db-1588-43a4-b454-adc058535a40","roots":{"p15901":"a91a7ac0-a4ee-43f5-b1d4-90589bfb57b5"},"root_ids":["p15901"]}];
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
lipL32[Gene] OR lipL32[All Fields] OR "complete genome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `primer_site_polymorphic`, `scope_narrower_than_taxid`.


## What reached the statistics

2,822 records were screened for this assay and **1,937 (69%)** were evaluable, meaning both primers landed in the right orientation and size range. 885 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 719 |
| `truncated` | 129 |
| `chance_pair` | 19 |
| `chance_anchor` | 18 |

