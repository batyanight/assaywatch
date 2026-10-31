# RHABDOVIRUS_ssRNA_L_gene_round1

<span class="aw-chip aw-chip-declining">declining</span>

**RHABDOVIRUS (ssRNA) — L (pan-rhabdovirus, PREDICT P-016 round 1)**

| | |
|---|---|
| Target | Rhabdoviridae ([taxid 11270](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11270)) |
| Gene | L |
| Chemistry | conventional |
| Amplicon | 460 bp |
| Designed | 2005 |
| Paper | [10.1099/vir.0.81128-0](https://doi.org/10.1099/vir.0.81128-0) |
| Registry status | active |

!!! quote "The paper"
    Bourhy, H., Cowley, J. A., Larrous, F., Holmes, E. C. & Walker, P. J. Phylogenetic relationships among rhabdoviruses inferred using the L polymerase gene. J Gen Virol 86, 2849-2858 (2005).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `RAAGGYAGRTTTTTYKCDYTRATG` | 24 nt |
| reverse | `CCADMCBTTTTGYCKYARRCCTTC` | 24 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 915 | 1,302 | 70.3% | 67.7% – 72.7% |
| baseline (everything earlier) | 4,043 | 5,458 | 74.1% | 72.9% – 75.2% |

Change from baseline, Newcombe interval: **-6.6% to -1.1%**. Threshold: **90.0%**.

*pooled share 70.3% has low coverage, but lineage Lyssavirus rabies (11292) (970 records) detects 84.8% (82.5%-87.0%), down from 95.1% on 3678 earlier records; lineage verdict overrides to declining*

Trend across deposit years: by record falling (p=5.45e-12, 35 years); by footprint falling (p=2.77e-06). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="adeb9f39-499d-4ef7-bd3f-8346c68c07a1" data-root-id="p31063" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"5fa9950a-b5b4-4608-8ca0-a8f392d191bc":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p31118","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p31119"}}},"roots":[{"type":"object","name":"Figure","id":"p31063","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p31065"},"y_range":{"type":"object","name":"Range1d","id":"p31072","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p31073"},"y_scale":{"type":"object","name":"LinearScale","id":"p31074"},"title":{"type":"object","name":"Title","id":"p31070","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p31108","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p31060","attributes":{"selected":{"type":"object","name":"Selection","id":"p31061","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p31062"},"data":{"type":"map","entries":[["year",[1985,1986,1989,1990,1993,1995,1997,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,66.66666666666666,0.0,66.66666666666666,0.0,100.0,0.0,71.42857142857143,100.0,33.33333333333333,37.5,66.66666666666666,85.18518518518519,78.57142857142857,51.85185185185185,70.96774193548387,68.18181818181817,90.36697247706422,76.27118644067797,55.10204081632652,81.70347003154575,81.95876288659794,80.14059753954305,85.76271186440678,80.78034682080924,66.46464646464646,39.67611336032389,64.38053097345133,90.6347554630593,70.89627391742196,46.724890829694324,56.08974358974359]],["detected",[1,1,1,2,2,0,4,0,4,0,5,2,1,3,2,23,33,14,22,15,197,45,54,259,318,456,253,559,329,98,291,871,704,214,175]],["evaluable",[1,1,1,2,3,5,6,10,4,1,7,2,3,8,3,27,42,27,31,22,218,59,98,317,388,569,295,692,495,247,452,961,993,458,312]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,8.703135093227193,9.07684386569143,9.328625426046248,9.667366891029102,9.791719296345839,10.143865699252444,9.517227179437622,8.703135093227193,9.897626379762722,9.07684386569143,9.328625426046248,9.989711205477885,9.328625426046248,10.821697436206254,11.113982461744026,10.821697436206254,10.913832791890265,10.683957047019447,12.138440943126074,11.333893523413357,11.653951690698229,12.357386280346175,12.473581162007465,12.690039803417337,12.315701410869364,12.798894369534512,12.611817825586112,12.212018889508172,12.56046311902937,12.978946677928755,12.996732446651396,12.567931706405075,12.348187441352533]]]}}},"view":{"type":"object","name":"CDSView","id":"p31109","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31110"}}},"glyph":{"type":"object","name":"Line","id":"p31105","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p31106","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p31107","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p31114","attributes":{"data_source":{"id":"p31060"},"view":{"type":"object","name":"CDSView","id":"p31115","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31116"}}},"glyph":{"type":"object","name":"Scatter","id":"p31111","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p31112","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p31113","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p31071","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p31085"},{"type":"object","name":"BoxZoomTool","id":"p31086","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p31087","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p31093","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31092","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p31094","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p31095"},{"type":"object","name":"SaveTool","id":"p31096"},{"type":"object","name":"HoverTool","id":"p31117","attributes":{"renderers":[{"id":"p31114"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p31080","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31081","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31082"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31083"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p31075","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31076","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31077"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31078"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p31079","attributes":{"axis":{"id":"p31075"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p31084","attributes":{"dimension":1,"axis":{"id":"p31080"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p31097","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p31099","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p31100","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p31101","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p31103","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31102","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p31104","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"5fa9950a-b5b4-4608-8ca0-a8f392d191bc","roots":{"p31063":"adeb9f39-499d-4ef7-bd3f-8346c68c07a1"},"root_ids":["p31063"]}];
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

<div id="ed1d31a8-7817-422a-84d1-251ac8fe8156" data-root-id="p31123" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"2e07fa6e-dbb1-4c0e-b116-23fa749cc423":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p31163","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p31164"}}},"roots":[{"type":"object","name":"Figure","id":"p31123","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p31124"},"y_range":{"type":"object","name":"DataRange1d","id":"p31125","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p31132"},"y_scale":{"type":"object","name":"LinearScale","id":"p31133"},"title":{"type":"object","name":"Title","id":"p31130","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p31159","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p31120","attributes":{"selected":{"type":"object","name":"Selection","id":"p31121","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p31122"},"data":{"type":"map","entries":[["year",[1985,1986,1989,1990,1993,1995,1997,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,1,2,3,5,6,10,4,1,7,2,3,8,3,27,42,27,31,22,218,59,98,317,388,569,295,692,495,247,452,961,993,458,312]],["detected",[1,1,1,2,2,0,4,0,4,0,5,2,1,3,2,23,33,14,22,15,197,45,54,259,318,456,253,559,329,98,291,871,704,214,175]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p31160","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31161"}}},"glyph":{"type":"object","name":"VBar","id":"p31156","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p31157","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p31158","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p31131","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p31144"},{"type":"object","name":"BoxZoomTool","id":"p31145","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p31146","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p31152","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31151","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p31153","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p31154"},{"type":"object","name":"SaveTool","id":"p31155"},{"type":"object","name":"HoverTool","id":"p31162","attributes":{"renderers":[{"id":"p31159"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p31139","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31140","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31141"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31142"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p31134","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31135","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31136"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31137"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p31138","attributes":{"axis":{"id":"p31134"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p31143","attributes":{"dimension":1,"axis":{"id":"p31139"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"2e07fa6e-dbb1-4c0e-b116-23fa749cc423","roots":{"p31123":"ed1d31a8-7817-422a-84d1-251ac8fe8156"},"root_ids":["p31123"]}];
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

<div id="a625f5c4-09ba-4a05-8ec9-645d90672da4" data-root-id="p31168" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"3bb93ff7-040a-4c55-b276-935027694b13":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p31210","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p31211"}}},"roots":[{"type":"object","name":"Figure","id":"p31168","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p31170"},"y_range":{"type":"object","name":"FactorRange","id":"p31177","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p31178"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p31179"},"title":{"type":"object","name":"Title","id":"p31175","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p31205","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p31165","attributes":{"selected":{"type":"object","name":"Selection","id":"p31166","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p31167"},"data":{"type":"map","entries":[["x",[-8,-16,-9,-4,-10,-15,-3,-1,-17,-14,-9,-7,-21,-24,-11,-6,-20,-21,-12,-19,-19,-20,-16,-23,-13,-6,-22,-7,-15,-3,-18]],["y",["forward","reverse","reverse","forward","reverse","forward","forward","forward","reverse","forward","forward","reverse","forward","forward","forward","forward","forward","reverse","reverse","forward","reverse","reverse","forward","forward","forward","reverse","forward","forward","reverse","reverse","forward"]],["alpha",[0.2923372781065089,0.2742307692307692,0.573491124260355,0.337603550295858,0.27020710059171593,0.3627514792899408,0.1731360946745562,0.16207100591715976,0.1615680473372781,0.3119526627218935,0.17162721893491123,0.17464497041420118,0.24556213017751477,0.20985207100591716,0.1686094674556213,0.16307692307692306,0.34967455621301774,0.3954437869822485,0.4889940828402367,0.8048520710059172,0.1711242603550296,0.167603550295858,0.21991124260355027,0.5946153846153847,1.0,1.0,1.0,1.0,1.0,1.0,1.0]],["pos",[8,16,9,4,10,15,3,1,17,14,9,7,21,24,11,6,20,21,12,19,19,20,16,23,13,6,22,7,15,3,18]],["base",["C","T","Y","R","K","T","A","G","T","T","K","R","G","R","T","Y","G","D","Y","Y","C","M","R","A","T","R","A","D","T","T","A"]],["n",[283,247,842,373,239,423,46,24,23,322,43,49,190,119,37,26,397,488,674,1302,42,35,139,884,3516,3070,4005,2312,4931,4917,4835]],["det_with",["0% of 283","0% of 247","6% of 842","2% of 373","0% of 239","3% of 423","0% of 46","0% of 24","0% of 23","4% of 322","2% of 43","4% of 49","9% of 190","9% of 119","11% of 37","12% of 26","15% of 397","18% of 488","23% of 674","30% of 1302","21% of 42","26% of 35","27% of 139","38% of 884","54% of 3516","53% of 3070","68% of 4005","68% of 2312","76% of 4931","83% of 4917","85% of 4835"]],["det_without",["75% of 6670","75% of 6706","81% of 6111","76% of 6580","75% of 6714","77% of 6530","73% of 6907","72% of 6929","72% of 6930","76% of 6631","73% of 6910","73% of 6904","74% of 6763","73% of 6834","73% of 6916","72% of 6927","76% of 6556","76% of 6465","78% of 6279","82% of 5651","73% of 6911","72% of 6918","73% of 6814","77% of 6069","91% of 3437","87% of 3883","78% of 2948","74% of 4641","62% of 2022","46% of 2036","42% of 2118"]],["subs",["C&gt;G 277, C&gt;A 6","T&gt;A 233, T&gt;C 13, T&gt;G 1","Y&gt;G 473, Y&gt;A 369","R&gt;C 246, R&gt;T 126, R&gt;Y 1","K&gt;A 239","T&gt;G 234, T&gt;A 161, T&gt;C 28","A&gt;T 23, A&gt;C 23","G&gt;A 12, G&gt;C 8, G&gt;T 4","T&gt;C 21, T&gt;A 2","T&gt;G 235, T&gt;A 87","K&gt;A 43","R&gt;T 39, R&gt;C 10","G&gt;C 183, G&gt;T 6, G&gt;A 1","R&gt;T 80, R&gt;C 39","T&gt;A 33, T&gt;C 3, T&gt;G 1","Y&gt;A 20, Y&gt;G 6","G&gt;C 395, G&gt;A 2","D&gt;C 488","Y&gt;A 384, Y&gt;G 290","Y&gt;G 652, Y&gt;A 650","C&gt;A 32, C&gt;T 7, C&gt;G 3","M&gt;G 18, M&gt;T 17","R&gt;T 87, R&gt;C 52","A&gt;C 467, A&gt;T 385, A&gt;G 32","T&gt;C 3067, T&gt;A 250, T&gt;G 199","R&gt;C 1755, R&gt;T 1314, R&gt;Y 1","A&gt;G 3398, A&gt;T 396, A&gt;C 211","D&gt;C 2312","T&gt;C 4931","T&gt;C 4917","A&gt;C 4831, A&gt;G 3, A&gt;T 1"]],["zone",["no","no","no","yes","no","no","yes","yes","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","yes","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p31206","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31207"}}},"glyph":{"type":"object","name":"Rect","id":"p31202","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p31203","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p31204","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p31176","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p31190"},{"type":"object","name":"BoxZoomTool","id":"p31191","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p31192","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p31198","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31197","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p31199","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p31200"},{"type":"object","name":"SaveTool","id":"p31201"},{"type":"object","name":"HoverTool","id":"p31208","attributes":{"renderers":[{"id":"p31205"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p31185","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p31186"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p31187"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31188"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p31180","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p31209","attributes":{"ticks":[-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-4,-3,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31182"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-8,"8"],[-16,"16"],[-9,"9"],[-4,"4"],[-10,"10"],[-15,"15"],[-3,"3"],[-1,"1"],[-17,"17"],[-14,"14"],[-7,"7"],[-21,"21"],[-24,"24"],[-11,"11"],[-6,"6"],[-20,"20"],[-12,"12"],[-19,"19"],[-23,"23"],[-13,"13"],[-22,"22"],[-18,"18"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p31183"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p31184","attributes":{"axis":{"id":"p31180"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p31189","attributes":{"dimension":1,"axis":{"id":"p31185"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"3bb93ff7-040a-4c55-b276-935027694b13","roots":{"p31168":"a625f5c4-09ba-4a05-8ec9-645d90672da4"},"root_ids":["p31168"]}];
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

<div id="f2e6d85f-1875-4e8f-be61-a22ce7e3fd3f" data-root-id="p31215" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"ec8e82f7-e597-4f45-a904-cdd6988b866c":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p31264","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p31265"}}},"roots":[{"type":"object","name":"Figure","id":"p31215","attributes":{"height":132,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p31224","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p31225","attributes":{"factors":["Lyssavirus rabies (11292)","Vesiculovirus indiana (1972577)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p31226"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p31227"},"title":{"type":"object","name":"Title","id":"p31222","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p31259","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p31212","attributes":{"selected":{"type":"object","name":"Selection","id":"p31213","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p31214"},"data":{"type":"map","entries":[["y",["Lyssavirus rabies (11292)","Vesiculovirus indiana (1972577)"]],["share",[84.84536082474227,100.0]],["lo",[82.45160130991361,88.64866068260312]],["hi",[86.96421518434661,100.0]],["n",[970,30]],["det",[823,30]],["colour",["#b3261e","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p31260","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p31261"}}},"glyph":{"type":"object","name":"Scatter","id":"p31256","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p31257","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p31258","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p31223","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p31238"},{"type":"object","name":"BoxZoomTool","id":"p31239","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p31240","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p31246","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p31245","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p31247","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p31248"},{"type":"object","name":"SaveTool","id":"p31249"},{"type":"object","name":"HoverTool","id":"p31263","attributes":{"renderers":[{"id":"p31259"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p31233","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p31234"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p31235"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31236"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p31228","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p31229","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p31230"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p31231"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p31232","attributes":{"axis":{"id":"p31228"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p31237","attributes":{"dimension":1,"axis":{"id":"p31233"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p31250","attributes":{"source":{"id":"p31212"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p31262","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"ec8e82f7-e597-4f45-a904-cdd6988b866c","roots":{"p31215":"f2e6d85f-1875-4e8f-be61-a22ce7e3fd3f"},"root_ids":["p31215"]}];
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

This entry declares **`scope_taxids`**: [35303](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=35303), [2842407](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=2842407), [2842415](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=2842415), [3152207](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3152207). A record counts toward the denominator when its taxid, or any ancestor, is in that set. Records outside it are screened and reported but kept out of the statistics.

769 screened records fell outside the declared scope.

Retrieval query:

```
L[Gene] OR "L protein"[Title] OR "large polymerase"[Title] OR polymerase[Title] OR "complete genome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).


## What reached the statistics

9,129 records were screened for this assay and **6,760 (74%)** were evaluable, meaning both primers landed in the right orientation and size range. 2,369 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 2,101 |
| `truncated` | 170 |
| `chance_anchor` | 88 |
| `chance_only` | 1 |

