# AVIPOXVIRUS_dsDNA_4b_core_Farias_2010

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**AVIPOXVIRUS (dsDNA) — 4b core protein TaqMan (Farias 2010)**

| | |
|---|---|
| Target | Avipoxvirus ([taxid 10260](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10260)) |
| Gene | 4b core protein |
| Chemistry | hydrolysis_probe |
| Amplicon | 250 bp |
| Designed | 2010 |
| Paper | [10.1371/journal.pone.0010745](https://doi.org/10.1371/journal.pone.0010745) |
| Registry status | active |

!!! quote "The paper"
    Farias, M. E. M., LaPointe, D. A., Atkinson, C. T., Czerwonka, C., Shrestha, R. & Jarvi, S. I. Taqman real-time PCR detects Avipoxvirus DNA in blood of Hawai'i 'Amakihi (Hemignathus virens). PLoS ONE 5, e10745 (2010).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `TCCTTGTAAAAGCGATACAGGAA` | 23 nt |
| reverse | `CCCCTTAACATGTGCTAACAA` | 21 nt |
| probe | `CAGCGTGATGAAGACGCTAA` | 20 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 15 | 24 | 62.5% | 42.7% – 78.8% |
| baseline (everything earlier) | 175 | 229 | 76.4% | 70.5% – 81.5% |

Change from baseline, Newcombe interval: **-34.3% to 3.5%**. Threshold: **90.0%**.

*detected share 62.5% (43%-79%) since Oct 2024, upper bound below the 90% threshold; change from baseline -34% to +3% (no measurable fall from a baseline of 76%)*

Trend across deposit years: by record falling (p=0.322, 21 years); by footprint falling (p=0.241). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="a5402f4d-b276-4ec2-9d8c-29a781e9cabc" data-root-id="p4145" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"e912e58f-4fba-42bd-b6cd-9ef94a3f65b6":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p4200","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p4201"}}},"roots":[{"type":"object","name":"Figure","id":"p4145","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p4147"},"y_range":{"type":"object","name":"Range1d","id":"p4154","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p4155"},"y_scale":{"type":"object","name":"LinearScale","id":"p4156"},"title":{"type":"object","name":"Title","id":"p4152","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p4190","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p4142","attributes":{"selected":{"type":"object","name":"Selection","id":"p4143","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p4144"},"data":{"type":"map","entries":[["year",[2003,2004,2006,2008,2009,2010,2011,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,40.0,100.0,80.0,100.0,82.14285714285714,71.875,100.0,100.0,0.0,60.0,50.0,25.0,66.66666666666666,0.0,82.35294117647058,96.55172413793103,87.5,93.33333333333333,12.5]],["detected",[1,4,2,22,8,2,23,46,1,2,0,6,6,1,2,0,14,28,7,14,1]],["evaluable",[1,4,5,22,10,2,28,64,1,2,6,10,12,4,3,2,17,29,8,15,8]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,9.517227179437622,9.667366891029102,10.683957047019447,10.143865699252444,9.07684386569143,10.846014908695619,11.385871088686695,8.703135093227193,9.07684386569143,9.791719296345839,10.143865699252444,10.269703144398052,9.517227179437622,9.328625426046248,9.07684386569143,10.508782366508077,10.869436534339137,9.989711205477885,10.423139468338052,9.989711205477885]]]}}},"view":{"type":"object","name":"CDSView","id":"p4191","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4192"}}},"glyph":{"type":"object","name":"Line","id":"p4187","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p4188","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p4189","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p4196","attributes":{"data_source":{"id":"p4142"},"view":{"type":"object","name":"CDSView","id":"p4197","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4198"}}},"glyph":{"type":"object","name":"Scatter","id":"p4193","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p4194","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p4195","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p4153","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p4167"},{"type":"object","name":"BoxZoomTool","id":"p4168","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p4169","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p4175","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4174","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p4176","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p4177"},{"type":"object","name":"SaveTool","id":"p4178"},{"type":"object","name":"HoverTool","id":"p4199","attributes":{"renderers":[{"id":"p4196"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p4162","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4163","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4164"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4165"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p4157","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4158","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4159"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4160"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p4161","attributes":{"axis":{"id":"p4157"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p4166","attributes":{"dimension":1,"axis":{"id":"p4162"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p4179","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p4181","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p4182","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p4183","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p4185","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4184","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p4186","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"e912e58f-4fba-42bd-b6cd-9ef94a3f65b6","roots":{"p4145":"a5402f4d-b276-4ec2-9d8c-29a781e9cabc"},"root_ids":["p4145"]}];
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

<div id="c44c8931-f327-4afc-9704-bec25e15bcdc" data-root-id="p4205" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"f6161fcc-0a8a-481d-9220-0b04003ac793":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p4245","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p4246"}}},"roots":[{"type":"object","name":"Figure","id":"p4205","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p4206"},"y_range":{"type":"object","name":"DataRange1d","id":"p4207","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p4214"},"y_scale":{"type":"object","name":"LinearScale","id":"p4215"},"title":{"type":"object","name":"Title","id":"p4212","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p4241","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p4202","attributes":{"selected":{"type":"object","name":"Selection","id":"p4203","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p4204"},"data":{"type":"map","entries":[["year",[2003,2004,2006,2008,2009,2010,2011,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,4,5,22,10,2,28,64,1,2,6,10,12,4,3,2,17,29,8,15,8]],["detected",[1,4,2,22,8,2,23,46,1,2,0,6,6,1,2,0,14,28,7,14,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p4242","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4243"}}},"glyph":{"type":"object","name":"VBar","id":"p4238","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p4239","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p4240","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p4213","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p4226"},{"type":"object","name":"BoxZoomTool","id":"p4227","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p4228","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p4234","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4233","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p4235","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p4236"},{"type":"object","name":"SaveTool","id":"p4237"},{"type":"object","name":"HoverTool","id":"p4244","attributes":{"renderers":[{"id":"p4241"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p4221","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4222","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4223"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4224"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p4216","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4217","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4218"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4219"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p4220","attributes":{"axis":{"id":"p4216"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p4225","attributes":{"dimension":1,"axis":{"id":"p4221"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"f6161fcc-0a8a-481d-9220-0b04003ac793","roots":{"p4205":"c44c8931-f327-4afc-9704-bec25e15bcdc"},"root_ids":["p4205"]}];
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

<div id="b73c24a8-4e48-432b-9af5-82c4f5889ed5" data-root-id="p4250" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"4934a65e-e530-476a-99a6-b5fa573bfe81":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p4292","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p4293"}}},"roots":[{"type":"object","name":"Figure","id":"p4250","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p4252"},"y_range":{"type":"object","name":"FactorRange","id":"p4259","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p4260"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p4261"},"title":{"type":"object","name":"Title","id":"p4257","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p4287","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p4247","attributes":{"selected":{"type":"object","name":"Selection","id":"p4248","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p4249"},"data":{"type":"map","entries":[["x",[-18,-21,-17,-20,-5,-11,-9,-14,-3,-3,-10,-18,-2,-13,-4,-2]],["y",["reverse","reverse","probe","probe","probe","forward","reverse","probe","forward","reverse","forward","probe","forward","forward","reverse","probe"]],["alpha",[0.8219367588932807,0.7278656126482214,0.7278656126482214,0.6741106719367589,0.5800395256916996,0.5666007905138339,0.5666007905138339,0.5531620553359683,0.5397233201581028,0.5397233201581028,0.5262845849802371,0.5262845849802371,0.5128458498023715,0.5128458498023715,0.5128458498023715,0.5128458498023715]],["pos",[18,21,17,20,5,11,9,14,3,3,10,18,2,13,4,2]],["base",["C","C","C","C","G","C","T","G","G","C","G","G","A","A","A","A"]],["n",[50,43,43,39,32,31,31,30,29,29,28,28,27,27,27,27]],["det_with",["0% of 50","0% of 43","0% of 43","0% of 39","0% of 32","0% of 31","0% of 31","0% of 30","0% of 29","0% of 29","0% of 28","0% of 28","0% of 27","0% of 27","0% of 27","0% of 27"]],["det_without",["95% of 201","91% of 208","91% of 208","90% of 212","87% of 219","86% of 220","86% of 220","86% of 221","86% of 222","86% of 222","85% of 223","85% of 223","85% of 224","85% of 224","85% of 224","85% of 224"]],["subs",["C&gt;T 50","C&gt;T 43","C&gt;T 43","C&gt;T 39","G&gt;A 21, G&gt;T 10, G&gt;C 1","C&gt;A 28, C&gt;T 2, C&gt;G 1","T&gt;A 27, T&gt;C 4","G&gt;A 30","G&gt;A 29","C&gt;T 29","G&gt;A 28","G&gt;A 27, G&gt;C 1","A&gt;T 27","A&gt;G 27","A&gt;G 27","A&gt;G 27"]],["zone",["no","no","no","no","yes","no","no","no","yes","yes","no","no","yes","no","yes","yes"]]]}}},"view":{"type":"object","name":"CDSView","id":"p4288","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4289"}}},"glyph":{"type":"object","name":"Rect","id":"p4284","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p4285","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p4286","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p4258","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p4272"},{"type":"object","name":"BoxZoomTool","id":"p4273","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p4274","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p4280","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4279","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p4281","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p4282"},{"type":"object","name":"SaveTool","id":"p4283"},{"type":"object","name":"HoverTool","id":"p4290","attributes":{"renderers":[{"id":"p4287"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p4267","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p4268"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p4269"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4270"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p4262","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p4291","attributes":{"ticks":[-21,-20,-18,-17,-14,-13,-11,-10,-9,-5,-4,-3,-2],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4264"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-18,"18"],[-21,"21"],[-17,"17"],[-20,"20"],[-5,"5"],[-11,"11"],[-9,"9"],[-14,"14"],[-3,"3"],[-10,"10"],[-2,"2"],[-13,"13"],[-4,"4"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p4265"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p4266","attributes":{"axis":{"id":"p4262"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p4271","attributes":{"dimension":1,"axis":{"id":"p4267"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"4934a65e-e530-476a-99a6-b5fa573bfe81","roots":{"p4250":"b73c24a8-4e48-432b-9af5-82c4f5889ed5"},"root_ids":["p4250"]}];
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

Disclosures on this entry: `amplicon_disagrees_with_paper`.


## What reached the statistics

1,727 records were screened for this assay and **253 (15%)** were evaluable, meaning both primers landed in the right orientation and size range. 1,474 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 1,389 |
| `truncated` | 55 |
| `chance_anchor` | 30 |

