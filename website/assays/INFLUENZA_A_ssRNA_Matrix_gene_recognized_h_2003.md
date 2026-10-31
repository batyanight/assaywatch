# INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003

<span class="aw-chip aw-chip-declining">declining</span>

**Influenza A virus — matrix gene real-time RT-PCR (Spackman, modified)**

| | |
|---|---|
| Target | Influenza A virus ([taxid 11320](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11320)) |
| Gene | M (matrix) |
| Chemistry | mgb |
| Amplicon | 100 bp |
| Designed | 2002 |
| Paper | [10.1128/JCM.40.9.3256-3260.2002](https://doi.org/10.1128/JCM.40.9.3256-3260.2002) |
| Registry status | active |

!!! quote "The paper"
    Spackman E et al. 2002. J Clin Microbiol 40:3256-3260 (matrix primers/probe); 2003 Avian Dis 47:1079 is the field validation, doi 10.1637/0005-2086-47.S3.1079

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ARATGAGTCTTCTRACCGAGGTCG` | 24 nt |
| reverse | `TGAAAAGACATCYTCAAGYYTCTG` | 24 nt |
| probe | `TCAGGCCCCCTCAAAGCCGA` | 20 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 1,970 | 30,392 | 6.5% | 6.2% – 6.8% |
| baseline (everything earlier) | 12,594 | 59,909 | 21.0% | 20.7% – 21.4% |

Change from baseline, Newcombe interval: **-15.0% to -14.1%**. Threshold: **90.0%**.

*detected share 6.5% (6%-7%) since Oct 2024, upper bound below the 90% threshold; change from baseline -15% to -14%*

Trend across deposit years: by record falling (p=0, 37 years); by footprint falling (p=0.608). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="e4654741-41a0-4f1b-b8ae-2129c38f1522" data-root-id="p15239" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"d91a09c5-6c96-428b-89e9-088518dbc2c2":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p15294","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p15295"}}},"roots":[{"type":"object","name":"Figure","id":"p15239","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p15241"},"y_range":{"type":"object","name":"Range1d","id":"p15248","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p15249"},"y_scale":{"type":"object","name":"LinearScale","id":"p15250"},"title":{"type":"object","name":"Title","id":"p15246","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p15284","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p15236","attributes":{"selected":{"type":"object","name":"Selection","id":"p15237","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p15238"},"data":{"type":"map","entries":[["year",[1982,1987,1988,1990,1992,1993,1994,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,50.0,50.0,0.0,0.0,100.0,0.0,100.0,100.0,40.0,71.42857142857143,19.047619047619047,92.85714285714286,93.33333333333333,96.36363636363636,12.808641975308642,45.61532792925571,40.66924066924067,63.73801916932907,41.760722347629795,30.52007299270073,51.9607843137255,23.649906890130353,30.859835100117785,28.947368421052634,51.03211009174312,18.25247291568535,58.73479318734793,30.25096525096525,12.356979405034325,30.070867649875506,44.926829268292686,8.261269549218031,3.919136797717971,7.623938376456646,7.616648674583184,3.972131016256907]],["detected",[1,1,1,0,0,1,0,4,1,2,5,8,13,42,53,83,619,316,399,740,669,159,127,262,352,445,775,1207,1567,918,1570,921,449,316,772,1270,496]],["evaluable",[1,2,2,1,1,1,2,4,1,5,7,42,14,45,55,648,1357,777,626,1772,2192,306,537,849,1216,872,4246,2055,5180,7429,5221,2050,5435,8063,10126,16674,12487]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,9.07684386569143,9.07684386569143,8.703135093227193,8.703135093227193,8.703135093227193,9.07684386569143,9.517227179437622,8.703135093227193,9.667366891029102,9.897626379762722,11.113982461744026,10.37579022724969,11.15897945775324,11.288829873700811,12.762485207159559,13.164767299284922,12.862783071970215,12.743289409679255,13.306198056995747,13.417579651336393,12.336940579597242,12.657616522292637,12.911380990702423,13.106050883295197,12.925993959933647,13.75648904265546,13.383909560376619,13.856350206546306,14.035158374215314,13.86029104983716,13.382636539396398,13.880348624998714,14.075367396955112,14.186465941014841,14.425919922033179,14.287706686982926]]]}}},"view":{"type":"object","name":"CDSView","id":"p15285","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15286"}}},"glyph":{"type":"object","name":"Line","id":"p15281","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p15282","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p15283","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p15290","attributes":{"data_source":{"id":"p15236"},"view":{"type":"object","name":"CDSView","id":"p15291","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15292"}}},"glyph":{"type":"object","name":"Scatter","id":"p15287","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p15288","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p15289","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p15247","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p15261"},{"type":"object","name":"BoxZoomTool","id":"p15262","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p15263","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p15269","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15268","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p15270","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p15271"},{"type":"object","name":"SaveTool","id":"p15272"},{"type":"object","name":"HoverTool","id":"p15293","attributes":{"renderers":[{"id":"p15290"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p15256","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15257","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15258"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15259"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p15251","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15252","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15253"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15254"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p15255","attributes":{"axis":{"id":"p15251"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p15260","attributes":{"dimension":1,"axis":{"id":"p15256"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p15273","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p15275","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p15276","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p15277","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p15279","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15278","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p15280","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"d91a09c5-6c96-428b-89e9-088518dbc2c2","roots":{"p15239":"e4654741-41a0-4f1b-b8ae-2129c38f1522"},"root_ids":["p15239"]}];
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

<div id="a56931b8-c3e1-4f8e-98a6-726ff8c2f0d3" data-root-id="p15299" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"c5ee2a9b-a542-4a73-b729-5a9799ef12ea":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p15339","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p15340"}}},"roots":[{"type":"object","name":"Figure","id":"p15299","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p15300"},"y_range":{"type":"object","name":"DataRange1d","id":"p15301","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p15308"},"y_scale":{"type":"object","name":"LinearScale","id":"p15309"},"title":{"type":"object","name":"Title","id":"p15306","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p15335","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p15296","attributes":{"selected":{"type":"object","name":"Selection","id":"p15297","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p15298"},"data":{"type":"map","entries":[["year",[1982,1987,1988,1990,1992,1993,1994,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,2,2,1,1,1,2,4,1,5,7,42,14,45,55,648,1357,777,626,1772,2192,306,537,849,1216,872,4246,2055,5180,7429,5221,2050,5435,8063,10126,16674,12487]],["detected",[1,1,1,0,0,1,0,4,1,2,5,8,13,42,53,83,619,316,399,740,669,159,127,262,352,445,775,1207,1567,918,1570,921,449,316,772,1270,496]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p15336","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15337"}}},"glyph":{"type":"object","name":"VBar","id":"p15332","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p15333","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p15334","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p15307","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p15320"},{"type":"object","name":"BoxZoomTool","id":"p15321","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p15322","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p15328","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15327","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p15329","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p15330"},{"type":"object","name":"SaveTool","id":"p15331"},{"type":"object","name":"HoverTool","id":"p15338","attributes":{"renderers":[{"id":"p15335"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p15315","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15316","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15317"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15318"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p15310","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15311","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15312"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15313"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p15314","attributes":{"axis":{"id":"p15310"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p15319","attributes":{"dimension":1,"axis":{"id":"p15315"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"c5ee2a9b-a542-4a73-b729-5a9799ef12ea","roots":{"p15299":"a56931b8-c3e1-4f8e-98a6-726ff8c2f0d3"},"root_ids":["p15299"]}];
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

<div id="e6ad17ca-3af8-44ea-909a-5a841ccdbbb1" data-root-id="p15344" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"312cd1cf-9a34-472b-91cf-5d87bdaf176f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p15386","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p15387"}}},"roots":[{"type":"object","name":"Figure","id":"p15344","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p15346"},"y_range":{"type":"object","name":"FactorRange","id":"p15353","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p15354"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p15355"},"title":{"type":"object","name":"Title","id":"p15351","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p15381","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p15341","attributes":{"selected":{"type":"object","name":"Selection","id":"p15342","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p15343"},"data":{"type":"map","entries":[["x",[-17,-24,-9,-14,-13,-11,-18,-8,-2,-3,-14,-6,-9,-7,-15,-21,-13,-16,-22,-24,-16,-14,-2,-23,-5,-18]],["y",["forward","reverse","reverse","reverse","reverse","forward","probe","forward","forward","reverse","probe","probe","forward","reverse","reverse","reverse","forward","reverse","reverse","forward","forward","forward","reverse","reverse","forward","reverse"]],["alpha",[1.0,1.0,1.0,1.0,1.0,1.0,0.2603575818650956,0.19367614976578332,0.19164294969047962,0.15753037064927297,0.15240971860776736,0.15229676304802825,0.15124251115713003,0.16939070442187792,0.16234980786480768,0.16310284492973498,0.1525603260207528,0.15154372598310095,1.0,0.15210850378179644,0.15112955559739094,0.15425465941683925,0.15180728895582551,0.15598664466617201,0.15222145934153553,0.6505813889104218]],["pos",[17,24,9,14,13,11,18,8,2,3,14,6,9,7,15,21,13,16,22,24,16,14,2,23,5,18]],["base",["T","T","A","T","C","R","A","C","C","C","C","A","C","G","A","A","C","C","A","A","C","T","T","G","G","G"]],["n",[40756,40430,31181,30240,29291,28866,2931,1160,1106,200,64,61,33,515,328,348,68,41,89494,56,30,113,48,159,59,13295]],["det_with",["0% of 40756","1% of 40430","0% of 31181","0% of 30240","0% of 29291","0% of 28866","0% of 2931","0% of 1160","0% of 1106","0% of 200","0% of 64","0% of 61","0% of 33","0% of 515","2% of 328","3% of 348","4% of 68","5% of 41","16% of 89494","25% of 56","30% of 30","32% of 113","44% of 48","55% of 159","66% of 59","62% of 13295"]],["det_without",["29% of 48872","29% of 49198","25% of 58447","24% of 59388","24% of 60337","24% of 60762","17% of 86697","16% of 88468","16% of 88522","16% of 89428","16% of 89564","16% of 89567","16% of 89595","16% of 89113","16% of 89300","16% of 89280","16% of 89560","16% of 89587","8% of 134","16% of 89572","16% of 89598","16% of 89515","16% of 89580","16% of 89469","16% of 89569","8% of 76333"]],["subs",["T&gt;C 40755, T&gt;A 1","T&gt;A 40179, T&gt;C 213, T&gt;G 37, T&gt;M 1","A&gt;C 30857, A&gt;T 175, A&gt;G 149","T&gt;C 30232, T&gt;G 7, T&gt;A 1","C&gt;T 29291","R&gt;T 28840, R&gt;C 26","A&gt;G 2482, A&gt;C 396, A&gt;T 53","C&gt;T 696, C&gt;A 450, C&gt;G 14","C&gt;T 981, C&gt;A 121, C&gt;G 4","C&gt;T 198, C&gt;A 2","C&gt;T 63, C&gt;A 1","A&gt;G 61","C&gt;A 32, C&gt;G 1","G&gt;A 317, G&gt;T 198","A&gt;G 197, A&gt;T 112, A&gt;C 19","A&gt;G 347, A&gt;C 1","C&gt;T 64, C&gt;G 4","C&gt;T 39, C&gt;G 1, C&gt;A 1","A&gt;C 89479, A&gt;T 15","A&gt;G 26, A&gt;T 26, A&gt;C 4","C&gt;T 27, C&gt;A 2, C&gt;G 1","T&gt;C 106, T&gt;A 6, T&gt;G 1","T&gt;C 26, T&gt;A 21, T&gt;G 1","G&gt;A 159","G&gt;A 58, G&gt;C 1","G&gt;A 5941, G&gt;C 4893, G&gt;T 2396, G&gt;M 55"]],["zone",["no","no","no","no","no","no","no","no","yes","yes","no","no","no","no","no","no","no","no","no","no","no","no","yes","no","yes","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p15382","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15383"}}},"glyph":{"type":"object","name":"Rect","id":"p15378","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p15379","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p15380","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p15352","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p15366"},{"type":"object","name":"BoxZoomTool","id":"p15367","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p15368","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p15374","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15373","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p15375","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p15376"},{"type":"object","name":"SaveTool","id":"p15377"},{"type":"object","name":"HoverTool","id":"p15384","attributes":{"renderers":[{"id":"p15381"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p15361","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p15362"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p15363"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15364"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p15356","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p15385","attributes":{"ticks":[-24,-23,-22,-21,-18,-17,-16,-15,-14,-13,-11,-9,-8,-7,-6,-5,-3,-2],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15358"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-17,"17"],[-24,"24"],[-9,"9"],[-14,"14"],[-13,"13"],[-11,"11"],[-18,"18"],[-8,"8"],[-2,"2"],[-3,"3"],[-6,"6"],[-7,"7"],[-15,"15"],[-21,"21"],[-16,"16"],[-22,"22"],[-23,"23"],[-5,"5"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p15359"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p15360","attributes":{"axis":{"id":"p15356"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p15365","attributes":{"dimension":1,"axis":{"id":"p15361"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"312cd1cf-9a34-472b-91cf-5d87bdaf176f","roots":{"p15344":"e6ad17ca-3af8-44ea-909a-5a841ccdbbb1"},"root_ids":["p15344"]}];
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

<div id="d55f6248-ab51-4308-82a3-68754ca762a8" data-root-id="p15391" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"0a82d678-5610-4f9a-8143-3295357100ba":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p15440","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p15441"}}},"roots":[{"type":"object","name":"Figure","id":"p15391","attributes":{"height":522,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p15400","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p15401","attributes":{"factors":["H1","H1pdm09","H3","H3N2","H1N1","Alphainfluenzavirus influenzae (2955291)","H1N2","HxN2","H5N1","H6N2","H9N2","H10N7","H5N2","H5N8","H13N6","H3N8","H4N6"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p15402"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p15403"},"title":{"type":"object","name":"Title","id":"p15398","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p15435","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p15388","attributes":{"selected":{"type":"object","name":"Selection","id":"p15389","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p15390"},"data":{"type":"map","entries":[["y",["H1","H1pdm09","H3","H3N2","H1N1","Alphainfluenzavirus influenzae (2955291)","H1N2","HxN2","H5N1","H6N2","H9N2","H10N7","H5N2","H5N8","H13N6","H3N8","H4N6"]],["share",[0.0,0.0,0.0,0.30028069717344474,0.4580652197622424,0.4784688995215311,6.369426751592357,6.666666666666667,10.590440487347703,28.57142857142857,69.49891067538127,86.74698795180723,87.5,89.47368421052632,93.02325581395348,95.88744588744589,98.82352941176471]],["lo",[0.0,0.0,0.0,0.22521493819803595,0.3390782228358179,0.18621981871041185,4.160715032770676,1.8477023791270377,8.883362305941509,21.02483979908171,66.4444230286671,77.80725361545822,80.39705979199262,78.87718941661296,81.39101309875801,93.66648068402064,93.6328291175061]],["hi",[10.151455415332377,0.8577720407596655,0.4217483496708449,0.40026604115075415,0.618547167453959,1.2237437757663252,9.632784085740065,21.323458362616922,12.580268647777446,37.53921793235873,72.3908882468734,92.43569350724009,92.27650272660462,95.08553414762552,97.59884104227855,97.35160969234511,99.79202128653361]],["n",[34,444,907,15319,9169,836,314,30,1067,112,918,83,120,57,43,462,85]],["det",[0,0,0,46,42,4,20,2,113,32,638,72,105,51,40,443,84]],["colour",["#b3261e","#b3261e","#b3261e","#b3261e","#b3261e","#b3261e","#b3261e","#b3261e","#b3261e","#b3261e","#b3261e","#007d5c","#007d5c","#007d5c","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p15436","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15437"}}},"glyph":{"type":"object","name":"Scatter","id":"p15432","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p15433","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p15434","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p15399","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p15414"},{"type":"object","name":"BoxZoomTool","id":"p15415","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p15416","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p15422","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15421","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p15423","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p15424"},{"type":"object","name":"SaveTool","id":"p15425"},{"type":"object","name":"HoverTool","id":"p15439","attributes":{"renderers":[{"id":"p15435"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p15409","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p15410"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p15411"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15412"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p15404","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15405","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15406"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15407"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p15408","attributes":{"axis":{"id":"p15404"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p15413","attributes":{"dimension":1,"axis":{"id":"p15409"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p15426","attributes":{"source":{"id":"p15388"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p15438","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"0a82d678-5610-4f9a-8143-3295357100ba","roots":{"p15391":"d55f6248-ab51-4308-82a3-68754ca762a8"},"root_ids":["p15391"]}];
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
"segment 7"[Title] OR ("matrix protein"[Title] AND M[Gene])
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `oligos_modified`.


## What reached the statistics

184,853 records were screened for this assay and **90,301 (49%)** were evaluable, meaning both primers landed in the right orientation and size range. 94,552 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `truncated` | 93,269 |
| `no_site` | 1,171 |
| `chance_anchor` | 102 |
| `no_pair` | 3 |

