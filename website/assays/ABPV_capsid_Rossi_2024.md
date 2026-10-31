# ABPV_capsid_Rossi_2024

<span class="aw-chip aw-chip-declining">declining</span>

**ACUTE BEE PARALYSIS VIRUS — capsid gene RT-qPCR, MGB probe (Rossi 2024)**

| | |
|---|---|
| Target | Aparavirus apisacutum (acute bee paralysis virus; the paper's name, renamed by ICTV) ([taxid 3047346](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3047346)) |
| Gene | capsid protein gene |
| Chemistry | mgb |
| Amplicon | 143 bp |
| Designed | 2024 |
| Paper | [10.3390/microorganisms12061105](https://doi.org/10.3390/microorganisms12061105) |
| Registry status | active |

!!! quote "The paper"
    Rossi, F.; Del Matto, I.; Ricchiuti, L.; Marino, L. Selection and Multiplexing of Reverse Transcription–Quantitative PCR Tests Targeting Relevant Honeybee Viral Pathogens. Microorganisms 2024, 12, 1105.

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `TTTGTTTCAAAYAARATGTTYATGAAAYC` | 29 nt |
| reverse | `BTWGAHACAGTCTCTGGACACAT` | 23 nt |
| probe | `TATGGTGGAAAYKCTGARAAYAAT` | 24 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 1 | 18 | 5.6% | 1.0% – 25.8% |
| baseline (everything earlier) | 88 | 106 | 83.0% | 74.7% – 89.0% |

Change from baseline, Newcombe interval: **-85.0% to -55.6%**. Threshold: **90.0%**.

*detected share 5.6% (1.0%-26%) since Oct 2024, upper bound below the 90% threshold; change from baseline -85% to -56%*

Trend across deposit years: by record falling (p=1.46e-08, 20 years); by footprint falling (p=0.0135). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="fa42209a-25de-4a1f-9eb7-15e63bff82b2" data-root-id="p1009" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"24c1c8f0-7128-4890-9675-e11d32384dd8":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p1064","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p1065"}}},"roots":[{"type":"object","name":"Figure","id":"p1009","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p1011"},"y_range":{"type":"object","name":"Range1d","id":"p1018","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p1019"},"y_scale":{"type":"object","name":"LinearScale","id":"p1020"},"title":{"type":"object","name":"Title","id":"p1016","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p1054","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p1006","attributes":{"selected":{"type":"object","name":"Selection","id":"p1007","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p1008"},"data":{"type":"map","entries":[["year",[1999,2000,2001,2002,2003,2008,2009,2010,2011,2014,2015,2017,2018,2019,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,80.0,95.23809523809523,100.0,100.0,100.0,100.0,100.0,100.0,0.0,100.0,100.0,50.0,88.88888888888889,45.45454545454545,83.33333333333334,0.0,9.090909090909092,0.0]],["detected",[1,2,8,20,3,3,2,2,17,1,0,1,1,1,16,5,5,0,1,0]],["evaluable",[1,2,10,21,3,3,2,2,17,1,3,1,1,2,18,11,6,2,11,7]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,9.07684386569143,10.143865699252444,10.652487636092928,9.328625426046248,9.328625426046248,9.07684386569143,9.07684386569143,10.508782366508077,8.703135093227193,9.328625426046248,8.703135093227193,8.703135093227193,9.07684386569143,10.547770533331066,10.209683151927734,9.791719296345839,9.07684386569143,10.209683151927734,9.897626379762722]]]}}},"view":{"type":"object","name":"CDSView","id":"p1055","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p1056"}}},"glyph":{"type":"object","name":"Line","id":"p1051","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p1052","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p1053","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p1060","attributes":{"data_source":{"id":"p1006"},"view":{"type":"object","name":"CDSView","id":"p1061","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p1062"}}},"glyph":{"type":"object","name":"Scatter","id":"p1057","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p1058","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p1059","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p1017","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p1031"},{"type":"object","name":"BoxZoomTool","id":"p1032","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p1033","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p1039","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p1038","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p1040","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p1041"},{"type":"object","name":"SaveTool","id":"p1042"},{"type":"object","name":"HoverTool","id":"p1063","attributes":{"renderers":[{"id":"p1060"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p1026","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p1027","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p1028"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p1029"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p1021","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p1022","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p1023"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p1024"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p1025","attributes":{"axis":{"id":"p1021"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p1030","attributes":{"dimension":1,"axis":{"id":"p1026"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p1043","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p1045","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p1046","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p1047","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p1049","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p1048","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p1050","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"24c1c8f0-7128-4890-9675-e11d32384dd8","roots":{"p1009":"fa42209a-25de-4a1f-9eb7-15e63bff82b2"},"root_ids":["p1009"]}];
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

<div id="d65c5e32-858b-431f-8276-a2c84db7d5f4" data-root-id="p1071" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"609eddbf-b421-4122-b1ad-c07bbfe95675":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p1111","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p1112"}}},"roots":[{"type":"object","name":"Figure","id":"p1071","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p1072"},"y_range":{"type":"object","name":"DataRange1d","id":"p1073","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p1080"},"y_scale":{"type":"object","name":"LinearScale","id":"p1081"},"title":{"type":"object","name":"Title","id":"p1078","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p1107","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p1068","attributes":{"selected":{"type":"object","name":"Selection","id":"p1069","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p1070"},"data":{"type":"map","entries":[["year",[1999,2000,2001,2002,2003,2008,2009,2010,2011,2014,2015,2017,2018,2019,2021,2022,2023,2024,2025,2026]],["evaluable",[1,2,10,21,3,3,2,2,17,1,3,1,1,2,18,11,6,2,11,7]],["detected",[1,2,8,20,3,3,2,2,17,1,0,1,1,1,16,5,5,0,1,0]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p1108","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p1109"}}},"glyph":{"type":"object","name":"VBar","id":"p1104","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p1105","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p1106","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p1079","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p1092"},{"type":"object","name":"BoxZoomTool","id":"p1093","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p1094","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p1100","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p1099","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p1101","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p1102"},{"type":"object","name":"SaveTool","id":"p1103"},{"type":"object","name":"HoverTool","id":"p1110","attributes":{"renderers":[{"id":"p1107"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p1087","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p1088","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p1089"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p1090"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p1082","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p1083","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p1084"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p1085"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p1086","attributes":{"axis":{"id":"p1082"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p1091","attributes":{"dimension":1,"axis":{"id":"p1087"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"609eddbf-b421-4122-b1ad-c07bbfe95675","roots":{"p1071":"d65c5e32-858b-431f-8276-a2c84db7d5f4"},"root_ids":["p1071"]}];
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

<div id="ab02461f-4f6f-4b59-a682-f9233381f6cc" data-root-id="p1116" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"0e5ed723-b5db-4045-b54e-f1efc9e52fc0":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p1158","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p1159"}}},"roots":[{"type":"object","name":"Figure","id":"p1116","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p1118"},"y_range":{"type":"object","name":"FactorRange","id":"p1125","attributes":{"factors":["probe"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p1126"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p1127"},"title":{"type":"object","name":"Title","id":"p1123","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p1153","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p1113","attributes":{"selected":{"type":"object","name":"Selection","id":"p1114","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p1115"},"data":{"type":"map","entries":[["x",[-10]],["y",["probe"]],["alpha",[0.8903225806451613]],["pos",[10]],["base",["T"]],["n",[27]],["det_with",["0% of 27"]],["det_without",["94% of 95"]],["subs",["T&gt;C 16, T&gt;A 11"]],["zone",["no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p1154","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p1155"}}},"glyph":{"type":"object","name":"Rect","id":"p1150","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p1151","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p1152","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p1124","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p1138"},{"type":"object","name":"BoxZoomTool","id":"p1139","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p1140","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p1146","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p1145","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p1147","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p1148"},{"type":"object","name":"SaveTool","id":"p1149"},{"type":"object","name":"HoverTool","id":"p1156","attributes":{"renderers":[{"id":"p1153"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p1133","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p1134"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p1135"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p1136"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p1128","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p1157","attributes":{"ticks":[-10],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p1130"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-10,"10"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p1131"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p1132","attributes":{"axis":{"id":"p1128"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p1137","attributes":{"dimension":1,"axis":{"id":"p1133"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"0e5ed723-b5db-4045-b54e-f1efc9e52fc0","roots":{"p1116":"ab02461f-4f6f-4b59-a682-f9233381f6cc"},"root_ids":["p1116"]}];
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

983 records were screened for this assay and **124 (13%)** were evaluable, meaning both primers landed in the right orientation and size range. 859 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 851 |
| `truncated` | 8 |

