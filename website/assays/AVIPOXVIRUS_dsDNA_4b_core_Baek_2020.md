# AVIPOXVIRUS_dsDNA_4b_core_Baek_2020

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**AVIPOXVIRUS (dsDNA) — hummingbird 4b core protein TaqMan MGB (Baek 2020)**

| | |
|---|---|
| Target | Avipoxvirus ([taxid 10260](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10260)) |
| Gene | 4b core protein |
| Chemistry | mgb |
| Amplicon | 123 bp |
| Designed | 2020 |
| Paper | [10.1371/journal.pone.0230701](https://doi.org/10.1371/journal.pone.0230701) |
| Registry status | active |

!!! quote "The paper"
    Baek HE, Bandivadekar RR, Pandit P, Mah M, Sehgal RNM, Tell LA. TaqMan quantitative real-time PCR for detecting Avipoxvirus DNA in various sample types from hummingbirds. PLoS ONE 15(6):e0230701 (2020).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ACGTCAACTCATGACTGGCAAT` | 22 nt |
| reverse | `TCTCATAACTCGAATAAGATCTTGTATCG` | 29 nt |
| probe | `AGACGCAGACGCTATA` | 16 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 0 | 78 | 0.0% | 0.0% – 4.7% |
| baseline (everything earlier) | 3 | 1,005 | 0.3% | 0.1% – 0.9% |

Change from baseline, Newcombe interval: **-0.9% to 4.4%**. Threshold: **90.0%**.

*detected share 0.0% (0%-5%) since Oct 2024, upper bound below the 90% threshold; change from baseline -0.9% to +4% (no measurable fall from a baseline of 0.3%)*

Trend across deposit years: by record rising (p=0.567, 26 years); by footprint rising (p=0.15). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="e15662ce-e8ea-458c-bfde-2d7a6dd5b7ed" data-root-id="p3993" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"41e48c47-5d23-473a-9c07-7d88f1967a77":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p4048","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p4049"}}},"roots":[{"type":"object","name":"Figure","id":"p3993","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p3995"},"y_range":{"type":"object","name":"Range1d","id":"p4002","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p4003"},"y_scale":{"type":"object","name":"LinearScale","id":"p4004"},"title":{"type":"object","name":"Title","id":"p4000","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p4038","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p3990","attributes":{"selected":{"type":"object","name":"Selection","id":"p3991","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p3992"},"data":{"type":"map","entries":[["year",[1993,1998,2000,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.631578947368421,0.0,0.0,0.0,0.0,0.0,4.166666666666666,0.0,0.0,0.8695652173913043,0.0,0.0,0.0]],["detected",[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0]],["evaluable",[1,1,2,18,13,23,2,33,30,4,57,15,145,38,12,28,38,187,58,24,22,82,115,66,37,32]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.07684386569143,10.547770533331066,10.324834530005162,10.713966621835368,9.07684386569143,10.955310988645032,10.892023970177537,9.517227179437622,11.311780786273989,10.423139468338052,11.894313992355507,11.048392086352559,10.269703144398052,10.846014908695619,11.048392086352559,12.047317073673941,11.322938200602813,10.74264168206181,10.683957047019447,11.542654874768257,11.752796680528627,11.405466677556973,11.030852377887435,10.934913263353746]]]}}},"view":{"type":"object","name":"CDSView","id":"p4039","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4040"}}},"glyph":{"type":"object","name":"Line","id":"p4035","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p4036","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p4037","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p4044","attributes":{"data_source":{"id":"p3990"},"view":{"type":"object","name":"CDSView","id":"p4045","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4046"}}},"glyph":{"type":"object","name":"Scatter","id":"p4041","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p4042","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p4043","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p4001","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p4015"},{"type":"object","name":"BoxZoomTool","id":"p4016","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p4017","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p4023","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4022","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p4024","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p4025"},{"type":"object","name":"SaveTool","id":"p4026"},{"type":"object","name":"HoverTool","id":"p4047","attributes":{"renderers":[{"id":"p4044"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p4010","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4011","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4012"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4013"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p4005","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4006","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4007"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4008"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p4009","attributes":{"axis":{"id":"p4005"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p4014","attributes":{"dimension":1,"axis":{"id":"p4010"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p4027","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p4029","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p4030","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p4031","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p4033","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4032","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p4034","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"41e48c47-5d23-473a-9c07-7d88f1967a77","roots":{"p3993":"e15662ce-e8ea-458c-bfde-2d7a6dd5b7ed"},"root_ids":["p3993"]}];
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

<div id="cd92ea3c-ca8c-4602-ba9d-851379d152e8" data-root-id="p4053" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"06e18db3-b879-4125-84f1-2501222fe389":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p4093","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p4094"}}},"roots":[{"type":"object","name":"Figure","id":"p4053","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p4054"},"y_range":{"type":"object","name":"DataRange1d","id":"p4055","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p4062"},"y_scale":{"type":"object","name":"LinearScale","id":"p4063"},"title":{"type":"object","name":"Title","id":"p4060","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p4089","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p4050","attributes":{"selected":{"type":"object","name":"Selection","id":"p4051","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p4052"},"data":{"type":"map","entries":[["year",[1993,1998,2000,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,2,18,13,23,2,33,30,4,57,15,145,38,12,28,38,187,58,24,22,82,115,66,37,32]],["detected",[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p4090","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4091"}}},"glyph":{"type":"object","name":"VBar","id":"p4086","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p4087","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p4088","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p4061","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p4074"},{"type":"object","name":"BoxZoomTool","id":"p4075","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p4076","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p4082","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4081","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p4083","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p4084"},{"type":"object","name":"SaveTool","id":"p4085"},{"type":"object","name":"HoverTool","id":"p4092","attributes":{"renderers":[{"id":"p4089"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p4069","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4070","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4071"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4072"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p4064","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4065","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4066"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4067"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p4068","attributes":{"axis":{"id":"p4064"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p4073","attributes":{"dimension":1,"axis":{"id":"p4069"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"06e18db3-b879-4125-84f1-2501222fe389","roots":{"p4053":"cd92ea3c-ca8c-4602-ba9d-851379d152e8"},"root_ids":["p4053"]}];
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

<div id="ce8c925d-50e8-4b99-9763-63f0795dbdeb" data-root-id="p4098" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"81342642-fc27-437d-8386-eb758d1ef26d":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p4140","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p4141"}}},"roots":[{"type":"object","name":"Figure","id":"p4098","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p4100"},"y_range":{"type":"object","name":"FactorRange","id":"p4107","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p4108"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p4109"},"title":{"type":"object","name":"Title","id":"p4105","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p4135","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p4095","attributes":{"selected":{"type":"object","name":"Selection","id":"p4096","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p4097"},"data":{"type":"map","entries":[["x",[-20,-7,-17,-20,-29,-11,-8,-13,-18,-2,-17,-14,-8,-10,-2,-4]],["y",["forward","probe","forward","reverse","reverse","reverse","reverse","probe","reverse","reverse","reverse","forward","forward","probe","forward","probe"]],["alpha",[1.0,1.0,1.0,1.0,1.0,1.0,0.9317174515235457,0.8846260387811634,0.7307940904893814,0.30697137580794087,0.2567405355493998,0.23790397045244688,0.23476454293628807,0.219067405355494,0.21592797783933515,0.21592797783933515]],["pos",[20,7,17,20,29,11,8,13,18,2,17,14,8,10,2,4]],["base",["G","C","A","T","T","A","T","C","G","C","A","T","C","A","A","T"]],["n",[754,730,488,483,483,479,249,234,185,50,34,28,27,22,21,21]],["det_with",["0% of 754","0% of 730","0% of 488","0% of 483","0% of 483","0% of 479","0% of 249","0% of 234","0% of 185","0% of 50","0% of 34","0% of 28","0% of 27","0% of 22","0% of 21","0% of 21"]],["det_without",["100% of 3","11% of 27","1% of 269","1% of 274","1% of 274","1% of 278","1% of 508","1% of 523","1% of 572","0% of 707","0% of 723","0% of 729","0% of 730","0% of 735","0% of 736","0% of 736"]],["subs",["G&gt;A 751, G&gt;T 3","C&gt;T 730","A&gt;T 488","T&gt;G 481, T&gt;A 2","T&gt;C 483","A&gt;G 479","T&gt;C 249","C&gt;T 234","G&gt;T 185","C&gt;A 48, C&gt;G 2","A&gt;T 24, A&gt;G 10","T&gt;G 25, T&gt;A 2, T&gt;C 1","C&gt;T 27","A&gt;G 20, A&gt;T 2","A&gt;G 20, A&gt;T 1","T&gt;C 16, T&gt;A 5"]],["zone",["no","no","no","no","no","no","no","no","no","yes","no","no","no","no","yes","yes"]]]}}},"view":{"type":"object","name":"CDSView","id":"p4136","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4137"}}},"glyph":{"type":"object","name":"Rect","id":"p4132","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p4133","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p4134","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p4106","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p4120"},{"type":"object","name":"BoxZoomTool","id":"p4121","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p4122","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p4128","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4127","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p4129","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p4130"},{"type":"object","name":"SaveTool","id":"p4131"},{"type":"object","name":"HoverTool","id":"p4138","attributes":{"renderers":[{"id":"p4135"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p4115","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p4116"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p4117"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4118"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p4110","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p4139","attributes":{"ticks":[-29,-20,-18,-17,-14,-13,-11,-10,-8,-7,-4,-2],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4112"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-20,"20"],[-7,"7"],[-17,"17"],[-29,"29"],[-11,"11"],[-8,"8"],[-13,"13"],[-18,"18"],[-2,"2"],[-14,"14"],[-10,"10"],[-4,"4"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p4113"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p4114","attributes":{"axis":{"id":"p4110"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p4119","attributes":{"dimension":1,"axis":{"id":"p4115"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"81342642-fc27-437d-8386-eb758d1ef26d","roots":{"p4098":"ce8c925d-50e8-4b99-9763-63f0795dbdeb"},"root_ids":["p4098"]}];
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

Disclosures on this entry: `scope_narrower_than_taxid`.


## What reached the statistics

1,727 records were screened for this assay and **1,083 (63%)** were evaluable, meaning both primers landed in the right orientation and size range. 644 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 616 |
| `truncated` | 18 |
| `chance_anchor` | 10 |

