# INFLUENZA_A_M1_Yang_2014

<span class="aw-chip aw-chip-stable">stable</span>

**Influenza A virus — M1 gene real-time RT-PCR, degenerate (Yang 2014, "At" assay)**

| | |
|---|---|
| Target | Influenza A virus ([taxid 11320](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11320)) |
| Gene | M1 (matrix) |
| Chemistry | hydrolysis_probe |
| Amplicon | 95 bp |
| Designed | 2014 |
| Paper | [10.1128/JCM.02467-13](https://doi.org/10.1128/JCM.02467-13) |
| Registry status | draft |

!!! quote "The paper"
    Yang J-R et al. 2014. J Clin Microbiol 52:76-82

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `AAGACCAATYYTGTCACCTYTGA` | 23 nt |
| reverse | `TAAAGCGTCTRCGYTGCAGTCC` | 22 nt |
| probe | `TTTGTNTTCACGCTCACCGT` | 20 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 68,395 | 70,582 | 96.9% | 96.8% – 97.0% |
| baseline (everything earlier) | 105,605 | 113,286 | 93.2% | 93.1% – 93.4% |

Change from baseline, Newcombe interval: **3.5% to 3.9%**. Threshold: **90.0%**.

*detected share 96.9% (97%-97%) since Oct 2024*

Trend across deposit years: by record rising (p=3.6e-258, 37 years); by footprint falling (p=0.56); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="abcf044e-b980-4754-84a5-5ad04b149800" data-root-id="p14621" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"fe1d0ea7-ddb4-47e2-9401-bb9e6f2bbbd3":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14676","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14677"}}},"roots":[{"type":"object","name":"Figure","id":"p14621","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p14623"},"y_range":{"type":"object","name":"Range1d","id":"p14630","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p14631"},"y_scale":{"type":"object","name":"LinearScale","id":"p14632"},"title":{"type":"object","name":"Title","id":"p14628","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14666","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14618","attributes":{"selected":{"type":"object","name":"Selection","id":"p14619","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14620"},"data":{"type":"map","entries":[["year",[1982,1987,1988,1990,1992,1993,1994,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,0.0,100.0,100.0,100.0,100.0,100.0,100.0,90.0,91.66666666666666,91.07142857142857,93.75,97.3404255319149,83.13953488372093,91.80522565320665,87.82447466007417,92.99533022014677,89.25956061838893,93.16616147699091,93.04143862392495,91.07669616519173,92.02279202279202,92.16132368148914,92.98245614035088,95.59856139749957,95.0879320800485,85.68660022148394,90.78967235391816,94.96582763793965,88.44741673223184,78.38709677419354,93.08570149921682,97.36842105263158,96.2103667522843,96.83089873731122,97.06932773109244]],["detected",[1,1,0,1,1,12,2,5,5,36,22,51,30,183,143,773,1421,1394,1097,3381,4760,1235,1615,4456,3339,5582,6272,3095,6013,11394,6745,2673,8320,14171,22849,35199,27723]],["evaluable",[1,1,2,1,1,12,2,5,5,40,24,56,32,188,172,842,1618,1499,1229,3629,5116,1356,1755,4835,3591,5839,6596,3612,6623,11998,7626,3410,8938,14554,23749,36351,28560]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.07684386569143,8.703135093227193,8.703135093227193,10.269703144398052,9.07684386569143,9.667366891029102,9.667366891029102,11.082053972722118,10.74264168206181,11.300413928944284,10.934913263353746,12.050499715724602,11.997285845087944,12.906850628005783,13.258224564652226,13.21774346303488,13.111756908964187,13.676968934388766,13.850132968047117,13.164373871099656,13.301121918958735,13.821837057760497,13.671616944019387,13.916057950460413,13.976505003962387,13.674581914023637,13.978524859671293,14.268479326569256,14.04802442338529,13.64528266347047,14.125745971931131,14.361131336463403,14.592738690621045,14.790386242289632,14.678798535409525]]]}}},"view":{"type":"object","name":"CDSView","id":"p14667","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14668"}}},"glyph":{"type":"object","name":"Line","id":"p14663","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p14664","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p14665","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p14672","attributes":{"data_source":{"id":"p14618"},"view":{"type":"object","name":"CDSView","id":"p14673","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14674"}}},"glyph":{"type":"object","name":"Scatter","id":"p14669","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p14670","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p14671","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14629","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14643"},{"type":"object","name":"BoxZoomTool","id":"p14644","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14645","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14651","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14650","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14652","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14653"},{"type":"object","name":"SaveTool","id":"p14654"},{"type":"object","name":"HoverTool","id":"p14675","attributes":{"renderers":[{"id":"p14672"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p14638","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14639","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14640"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14641"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14633","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14634","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14635"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14636"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14637","attributes":{"axis":{"id":"p14633"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14642","attributes":{"dimension":1,"axis":{"id":"p14638"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p14655","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p14657","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p14658","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p14659","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p14661","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14660","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p14662","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"fe1d0ea7-ddb4-47e2-9401-bb9e6f2bbbd3","roots":{"p14621":"abcf044e-b980-4754-84a5-5ad04b149800"},"root_ids":["p14621"]}];
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

<div id="d684704a-b46f-4728-a963-69e97072f7e4" data-root-id="p14681" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9994a4da-f70e-41b3-baad-77e1b9e3f369":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14721","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14722"}}},"roots":[{"type":"object","name":"Figure","id":"p14681","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p14682"},"y_range":{"type":"object","name":"DataRange1d","id":"p14683","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p14690"},"y_scale":{"type":"object","name":"LinearScale","id":"p14691"},"title":{"type":"object","name":"Title","id":"p14688","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14717","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14678","attributes":{"selected":{"type":"object","name":"Selection","id":"p14679","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14680"},"data":{"type":"map","entries":[["year",[1982,1987,1988,1990,1992,1993,1994,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,2,1,1,12,2,5,5,40,24,56,32,188,172,842,1618,1499,1229,3629,5116,1356,1755,4835,3591,5839,6596,3612,6623,11998,7626,3410,8938,14554,23749,36351,28560]],["detected",[1,1,0,1,1,12,2,5,5,36,22,51,30,183,143,773,1421,1394,1097,3381,4760,1235,1615,4456,3339,5582,6272,3095,6013,11394,6745,2673,8320,14171,22849,35199,27723]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p14718","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14719"}}},"glyph":{"type":"object","name":"VBar","id":"p14714","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p14715","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p14716","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14689","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14702"},{"type":"object","name":"BoxZoomTool","id":"p14703","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14704","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14710","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14709","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14711","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14712"},{"type":"object","name":"SaveTool","id":"p14713"},{"type":"object","name":"HoverTool","id":"p14720","attributes":{"renderers":[{"id":"p14717"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p14697","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14698","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14699"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14700"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14692","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14693","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14694"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14695"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14696","attributes":{"axis":{"id":"p14692"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14701","attributes":{"dimension":1,"axis":{"id":"p14697"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9994a4da-f70e-41b3-baad-77e1b9e3f369","roots":{"p14681":"d684704a-b46f-4728-a963-69e97072f7e4"},"root_ids":["p14681"]}];
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

<div id="fd917abf-2fb4-410e-9e64-2e42319b6c65" data-root-id="p14726" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"66a719ce-7d03-4bf4-9b33-a40fbb92223c":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14768","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14769"}}},"roots":[{"type":"object","name":"Figure","id":"p14726","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p14728"},"y_range":{"type":"object","name":"FactorRange","id":"p14735","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p14736"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p14737"},"title":{"type":"object","name":"Title","id":"p14733","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14763","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14723","attributes":{"selected":{"type":"object","name":"Selection","id":"p14724","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14725"},"data":{"type":"map","entries":[["x",[-12,-7,-4,-9,-18,-1,-13,-5,-11,-16,-17,-6,-20,-8,-8,-17,-14,-20,-15,-21,-17,-14,-13,-3,-5,-11,-18,-3,-22,-22,-11,-23,-2]],["y",["probe","forward","forward","probe","probe","forward","probe","reverse","probe","reverse","probe","reverse","probe","reverse","forward","reverse","reverse","forward","reverse","reverse","forward","forward","reverse","reverse","forward","forward","reverse","probe","forward","reverse","reverse","forward","forward"]],["alpha",[0.2286814453847325,0.17738595079078467,0.15809928862009703,0.15745208519155046,0.18966432440663955,0.15075815258772599,0.15055474579589706,0.15053625426936715,0.15036983053059802,0.15181216959993038,0.15954162768942937,0.15846911915069506,0.15164574586116125,0.15059172884895686,0.15305110187743382,0.15048077968977744,0.15073966106119607,0.16399808558313572,0.15613918680792743,0.18019666282332977,0.18221223921508908,0.15277372897948527,0.15042530511018773,0.1519231187591098,0.15858006830987448,0.1510170339591446,0.4276502708464768,0.15443796636717644,0.15234842386929753,1.0,0.15044379663671764,0.15046228816324755,0.18774120564752975]],["pos",[12,7,4,9,18,1,13,5,11,16,17,6,20,8,8,17,14,20,15,21,17,14,13,3,5,11,18,3,22,22,11,23,2]],["base",["C","C","Y","G","T","A","T","A","A","G","G","C","T","T","A","C","C","A","T","A","A","Y","T","T","T","G","G","C","A","T","C","A","G"]],["n",[4255,1481,438,403,2145,41,30,29,20,98,516,458,89,32,165,26,40,757,332,1633,1742,150,23,104,464,55,15015,240,127,145944,24,25,2041]],["det_with",["0% of 4255","0% of 1481","0% of 438","0% of 403","1% of 2145","0% of 41","0% of 30","0% of 29","0% of 20","1% of 98","2% of 516","3% of 458","3% of 89","9% of 32","18% of 165","19% of 26","45% of 40","61% of 757","62% of 332","64% of 1633","65% of 1742","66% of 150","70% of 23","71% of 104","73% of 464","75% of 55","77% of 15015","78% of 240","88% of 127","94% of 145944","92% of 24","92% of 25","94% of 2041"]],["det_without",["97% of 179591","95% of 182365","95% of 183408","95% of 183443","96% of 181701","95% of 183805","95% of 183816","95% of 183817","95% of 183826","95% of 183748","95% of 183330","95% of 183388","95% of 183757","95% of 183814","95% of 183681","95% of 183820","95% of 183806","95% of 183089","95% of 183514","95% of 182213","95% of 182104","95% of 183696","95% of 183823","95% of 183742","95% of 183382","95% of 183791","96% of 168831","95% of 183606","95% of 183719","99% of 37902","95% of 183822","95% of 183821","95% of 181805"]],["subs",["C&gt;T 4254, C&gt;A 1","C&gt;T 1478, C&gt;A 2, C&gt;G 1","Y&gt;A 437, Y&gt;G 1","G&gt;A 400, G&gt;T 3","T&gt;C 2049, T&gt;A 85, T&gt;G 11","A&gt;G 28, A&gt;T 12, A&gt;C 1","T&gt;A 24, T&gt;C 5, T&gt;G 1","A&gt;T 16, A&gt;G 10, A&gt;C 3","A&gt;C 9, A&gt;G 6, A&gt;T 5","G&gt;T 96, G&gt;C 2","G&gt;A 509, G&gt;T 6, G&gt;C 1","C&gt;A 356, C&gt;T 99, C&gt;G 3","T&gt;G 47, T&gt;C 42","T&gt;A 28, T&gt;G 2, T&gt;C 2","A&gt;G 152, A&gt;C 7, A&gt;T 6","C&gt;T 17, C&gt;A 6, C&gt;G 3","C&gt;T 22, C&gt;A 13, C&gt;G 5","A&gt;G 754, A&gt;C 2, A&gt;T 1","T&gt;C 332","A&gt;G 1628, A&gt;T 4, A&gt;C 1","A&gt;G 1533, A&gt;T 196, A&gt;C 13","Y&gt;A 149, Y&gt;G 1","T&gt;G 23","T&gt;C 90, T&gt;G 13, T&gt;A 1","T&gt;C 360, T&gt;A 95, T&gt;G 9","G&gt;A 50, G&gt;T 5","G&gt;A 6947, G&gt;C 5391, G&gt;T 2510, G&gt;M 165","C&gt;T 201, C&gt;A 37, C&gt;G 2","A&gt;C 122, A&gt;G 5","T&gt;C 145941, T&gt;A 3","C&gt;A 21, C&gt;T 3","A&gt;G 16, A&gt;C 7, A&gt;T 2","G&gt;A 1984, G&gt;T 52, G&gt;C 5"]],["zone",["no","no","yes","no","no","yes","no","yes","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","yes","yes","no","no","yes","no","no","no","no","yes"]]]}}},"view":{"type":"object","name":"CDSView","id":"p14764","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14765"}}},"glyph":{"type":"object","name":"Rect","id":"p14760","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p14761","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p14762","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14734","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14748"},{"type":"object","name":"BoxZoomTool","id":"p14749","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14750","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14756","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14755","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14757","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14758"},{"type":"object","name":"SaveTool","id":"p14759"},{"type":"object","name":"HoverTool","id":"p14766","attributes":{"renderers":[{"id":"p14763"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p14743","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p14744"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p14745"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14746"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14738","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p14767","attributes":{"ticks":[-23,-22,-21,-20,-18,-17,-16,-15,-14,-13,-12,-11,-9,-8,-7,-6,-5,-4,-3,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14740"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-12,"12"],[-7,"7"],[-4,"4"],[-9,"9"],[-18,"18"],[-1,"1"],[-13,"13"],[-5,"5"],[-11,"11"],[-16,"16"],[-17,"17"],[-6,"6"],[-20,"20"],[-8,"8"],[-14,"14"],[-15,"15"],[-21,"21"],[-3,"3"],[-22,"22"],[-23,"23"],[-2,"2"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p14741"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14742","attributes":{"axis":{"id":"p14738"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14747","attributes":{"dimension":1,"axis":{"id":"p14743"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"66a719ce-7d03-4bf4-9b33-a40fbb92223c","roots":{"p14726":"fd917abf-2fb4-410e-9e64-2e42319b6c65"},"root_ids":["p14726"]}];
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

<div id="fa92fcf4-ca39-4751-ba57-b240abad0aac" data-root-id="p14773" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"f01bb47e-0f69-4dc4-9fa9-eecd5efaa0c4":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14822","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14823"}}},"roots":[{"type":"object","name":"Figure","id":"p14773","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p14782","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p14783","attributes":{"factors":["Alphainfluenzavirus influenzae (2955291)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p14784"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p14785"},"title":{"type":"object","name":"Title","id":"p14780","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14817","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14770","attributes":{"selected":{"type":"object","name":"Selection","id":"p14771","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14772"},"data":{"type":"map","entries":[["y",["Alphainfluenzavirus influenzae (2955291)"]],["share",[96.91932718332413]],["lo",[96.78926319888687]],["hi",[97.0442832917132]],["n",[70569]],["det",[68395]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p14818","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14819"}}},"glyph":{"type":"object","name":"Scatter","id":"p14814","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p14815","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p14816","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14781","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14796"},{"type":"object","name":"BoxZoomTool","id":"p14797","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14798","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14804","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14803","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14805","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14806"},{"type":"object","name":"SaveTool","id":"p14807"},{"type":"object","name":"HoverTool","id":"p14821","attributes":{"renderers":[{"id":"p14817"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p14791","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p14792"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p14793"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14794"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14786","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14787","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14788"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14789"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14790","attributes":{"axis":{"id":"p14786"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14795","attributes":{"dimension":1,"axis":{"id":"p14791"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p14808","attributes":{"source":{"id":"p14770"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p14820","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"f01bb47e-0f69-4dc4-9fa9-eecd5efaa0c4","roots":{"p14773":"fa92fcf4-ca39-4751-ba57-b240abad0aac"},"root_ids":["p14773"]}];
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

Disclosures on this entry: `oligos_modified`, `orientation_inferred`, `amplicon_disagrees_with_paper`.


## What reached the statistics

184,853 records were screened for this assay and **183,868 (99%)** were evaluable, meaning both primers landed in the right orientation and size range. 985 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 762 |
| `truncated` | 203 |
| `chance_anchor` | 7 |

