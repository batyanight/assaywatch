# PARVOVIRUS_ssDNA_VP1_gene_dependovirus_2002

<span class="aw-chip aw-chip-stable">stable</span>

**PARVOVIRUS (ssDNA) — VP1 gene (dependovirus)**

| | |
|---|---|
| Target | Dependoparvovirus ([taxid 10803](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10803)) |
| Gene | VP1 gene (dependovirus) |
| Chemistry | conventional |
| Amplicon | 255 bp |
| Designed | 2002 |
| Paper | [10.1073/pnas.182412299](https://doi.org/10.1073/pnas.182412299) |
| Registry status | active |

!!! quote "The paper"
    Gao GP et al. 2002. Proc Natl Acad Sci USA 99:11854-11859

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GGYAATKCCTCVGGWRATTGGCATT` | 25 nt |
| reverse | `GADBCCCCARTKGTTGTTGATRAGYC` | 26 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 255 | 256 | 99.6% | 97.8% – 99.9% |
| baseline (everything earlier) | 1,749 | 1,775 | 98.5% | 97.9% – 99.0% |

Change from baseline, Newcombe interval: **-0.8% to 1.8%**. Threshold: **90.0%**.

*detected share 99.6% (98%-100%) since Oct 2024*

Trend across deposit years: by record falling (p=0.00353, 33 years); by footprint falling (p=0.0115). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="dc3919a1-177e-467c-bee1-4ef0793407c2" data-root-id="p22735" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"43645b83-209c-4423-a7a8-32540651faa9":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p22790","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p22791"}}},"roots":[{"type":"object","name":"Figure","id":"p22735","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p22737"},"y_range":{"type":"object","name":"Range1d","id":"p22744","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p22745"},"y_scale":{"type":"object","name":"LinearScale","id":"p22746"},"title":{"type":"object","name":"Title","id":"p22742","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p22780","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p22732","attributes":{"selected":{"type":"object","name":"Selection","id":"p22733","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p22734"},"data":{"type":"map","entries":[["year",[1991,1993,1995,1996,1997,1998,1999,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,93.75,100.0,100.0,100.0,100.0,96.66666666666667,100.0,100.0,95.45454545454545,99.29577464788733,96.72131147540983,91.76470588235294,97.84172661870504,98.75,96.15384615384616,96.05263157894737,99.14529914529915,100.0]],["detected",[1,1,6,2,2,3,4,4,2,41,114,8,15,14,31,15,4,472,3,25,58,49,45,21,282,118,78,136,79,50,73,116,132]],["evaluable",[1,1,6,2,2,3,4,4,2,41,114,8,15,14,31,16,4,472,3,25,60,49,45,22,284,122,85,139,80,52,76,117,132]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.791719296345839,9.07684386569143,9.07684386569143,9.328625426046248,9.517227179437622,9.517227179437622,9.07684386569143,11.098224018878925,11.747425107358183,9.989711205477885,10.423139468338052,10.37579022724969,10.913832791890265,10.467343773689333,9.517227179437622,12.584963668081652,9.328625426046248,10.770092258092593,11.34465373009984,11.214271124597754,11.15897945775324,10.683957047019447,12.293606485117214,11.789062964047131,11.56518892267352,11.868663985739676,11.527140521415502,11.252690272875853,11.49483773413666,11.763392618310167,11.837210590688509]]]}}},"view":{"type":"object","name":"CDSView","id":"p22781","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p22782"}}},"glyph":{"type":"object","name":"Line","id":"p22777","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p22778","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p22779","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p22786","attributes":{"data_source":{"id":"p22732"},"view":{"type":"object","name":"CDSView","id":"p22787","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p22788"}}},"glyph":{"type":"object","name":"Scatter","id":"p22783","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p22784","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p22785","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p22743","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p22757"},{"type":"object","name":"BoxZoomTool","id":"p22758","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p22759","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p22765","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p22764","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p22766","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p22767"},{"type":"object","name":"SaveTool","id":"p22768"},{"type":"object","name":"HoverTool","id":"p22789","attributes":{"renderers":[{"id":"p22786"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p22752","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p22753","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p22754"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22755"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p22747","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p22748","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p22749"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22750"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p22751","attributes":{"axis":{"id":"p22747"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p22756","attributes":{"dimension":1,"axis":{"id":"p22752"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p22769","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p22771","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p22772","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p22773","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p22775","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p22774","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p22776","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"43645b83-209c-4423-a7a8-32540651faa9","roots":{"p22735":"dc3919a1-177e-467c-bee1-4ef0793407c2"},"root_ids":["p22735"]}];
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

<div id="f24752b4-d6c2-4f75-bd45-ea5553c88dc1" data-root-id="p22795" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"505bceab-7ed2-4ea8-9a7d-97454a4717b7":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p22835","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p22836"}}},"roots":[{"type":"object","name":"Figure","id":"p22795","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p22796"},"y_range":{"type":"object","name":"DataRange1d","id":"p22797","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p22804"},"y_scale":{"type":"object","name":"LinearScale","id":"p22805"},"title":{"type":"object","name":"Title","id":"p22802","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p22831","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p22792","attributes":{"selected":{"type":"object","name":"Selection","id":"p22793","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p22794"},"data":{"type":"map","entries":[["year",[1991,1993,1995,1996,1997,1998,1999,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,6,2,2,3,4,4,2,41,114,8,15,14,31,16,4,472,3,25,60,49,45,22,284,122,85,139,80,52,76,117,132]],["detected",[1,1,6,2,2,3,4,4,2,41,114,8,15,14,31,15,4,472,3,25,58,49,45,21,282,118,78,136,79,50,73,116,132]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p22832","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p22833"}}},"glyph":{"type":"object","name":"VBar","id":"p22828","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p22829","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p22830","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p22803","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p22816"},{"type":"object","name":"BoxZoomTool","id":"p22817","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p22818","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p22824","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p22823","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p22825","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p22826"},{"type":"object","name":"SaveTool","id":"p22827"},{"type":"object","name":"HoverTool","id":"p22834","attributes":{"renderers":[{"id":"p22831"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p22811","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p22812","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p22813"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22814"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p22806","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p22807","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p22808"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22809"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p22810","attributes":{"axis":{"id":"p22806"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p22815","attributes":{"dimension":1,"axis":{"id":"p22811"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"505bceab-7ed2-4ea8-9a7d-97454a4717b7","roots":{"p22795":"f24752b4-d6c2-4f75-bd45-ea5553c88dc1"},"root_ids":["p22795"]}];
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

<div id="dba85267-83a2-42cc-92f3-aa1dd7f98189" data-root-id="p22840" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"469d14c4-7bd1-4ece-a1f0-1976fe4cc29f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p22882","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p22883"}}},"roots":[{"type":"object","name":"Figure","id":"p22840","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p22842"},"y_range":{"type":"object","name":"FactorRange","id":"p22849","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p22850"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p22851"},"title":{"type":"object","name":"Title","id":"p22847","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p22877","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p22837","attributes":{"selected":{"type":"object","name":"Selection","id":"p22838","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p22839"},"data":{"type":"map","entries":[["x",[-22,-19,-4,-2,-2,-20,-18,-6,-17,-11,-16,-7,-13,-15,-26,-21,-4,-9,-18,-25,-14,-8]],["y",["forward","reverse","forward","reverse","forward","forward","reverse","reverse","forward","reverse","reverse","forward","reverse","reverse","reverse","forward","reverse","forward","forward","reverse","reverse","reverse"]],["alpha",[0.18515509601181684,0.18682914820285573,0.2052437223042836,0.2069177744953225,0.2018956179222058,0.25713934022648943,0.30066469719350075,0.3257754800590842,0.19519940915805023,0.21193993106843917,0.23370260955194483,0.23872476612506155,0.23872476612506155,0.3408419497784343,1.0,1.0,0.1935253569670113,0.23537666174298374,0.23705071393402266,0.23705071393402266,0.27387986213687837,0.4479812900049237]],["pos",[22,19,4,2,2,20,18,6,17,11,16,7,13,15,26,21,4,9,18,25,14,8]],["base",["A","C","C","Y","T","T","A","T","C","G","T","T","T","K","G","A","A","A","C","A","G","G"]],["n",[21,22,33,34,31,64,90,105,27,37,50,53,53,114,576,1826,26,51,52,52,74,178]],["det_with",["71% of 21","73% of 22","82% of 33","82% of 34","84% of 31","88% of 64","92% of 90","93% of 105","96% of 27","97% of 37","98% of 50","98% of 53","98% of 53","99% of 114","99% of 576","100% of 1826","100% of 26","100% of 51","100% of 52","100% of 52","100% of 74","100% of 178"]],["det_without",["100% of 6925","100% of 6924","100% of 6913","100% of 6912","100% of 6915","100% of 6882","100% of 6856","100% of 6841","100% of 6919","100% of 6909","100% of 6896","100% of 6893","100% of 6893","100% of 6832","100% of 6370","100% of 5120","100% of 6920","100% of 6895","100% of 6894","100% of 6894","100% of 6872","100% of 6768"]],["subs",["A&gt;C 11, A&gt;G 7, A&gt;T 3","C&gt;G 15, C&gt;A 6, C&gt;T 1","C&gt;T 26, C&gt;G 5, C&gt;A 2","Y&gt;G 27, Y&gt;A 7","T&gt;C 26, T&gt;G 3, T&gt;A 2","T&gt;C 44, T&gt;G 10, T&gt;A 10","A&gt;G 69, A&gt;T 16, A&gt;C 5","T&gt;C 104, T&gt;G 1","C&gt;T 25, C&gt;A 2","G&gt;A 37","T&gt;C 48, T&gt;G 2","T&gt;C 52, T&gt;A 1","T&gt;C 52, T&gt;G 1","K&gt;A 114","G&gt;C 367, G&gt;A 125, G&gt;T 84","A&gt;G 1804, A&gt;C 22","A&gt;G 26","A&gt;G 51","C&gt;T 52","A&gt;G 51, A&gt;T 1","G&gt;A 74","G&gt;A 178"]],["zone",["no","no","yes","yes","yes","no","no","no","no","no","no","no","no","no","no","no","yes","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p22878","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p22879"}}},"glyph":{"type":"object","name":"Rect","id":"p22874","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p22875","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p22876","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p22848","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p22862"},{"type":"object","name":"BoxZoomTool","id":"p22863","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p22864","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p22870","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p22869","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p22871","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p22872"},{"type":"object","name":"SaveTool","id":"p22873"},{"type":"object","name":"HoverTool","id":"p22880","attributes":{"renderers":[{"id":"p22877"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p22857","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p22858"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p22859"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22860"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p22852","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p22881","attributes":{"ticks":[-26,-25,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-11,-9,-8,-7,-6,-4,-2],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p22854"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-22,"22"],[-19,"19"],[-4,"4"],[-2,"2"],[-20,"20"],[-18,"18"],[-6,"6"],[-17,"17"],[-11,"11"],[-16,"16"],[-7,"7"],[-13,"13"],[-15,"15"],[-26,"26"],[-21,"21"],[-9,"9"],[-25,"25"],[-14,"14"],[-8,"8"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p22855"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p22856","attributes":{"axis":{"id":"p22852"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p22861","attributes":{"dimension":1,"axis":{"id":"p22857"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"469d14c4-7bd1-4ece-a1f0-1976fe4cc29f","roots":{"p22840":"dba85267-83a2-42cc-92f3-aa1dd7f98189"},"root_ids":["p22840"]}];
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

<div id="a4cb2b2c-0f1d-4ac5-92c0-e5cd3c2116e0" data-root-id="p22887" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"f84ab6cd-c337-49cc-a99e-14d1357098a2":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p22936","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p22937"}}},"roots":[{"type":"object","name":"Figure","id":"p22887","attributes":{"height":158,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p22896","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p22897","attributes":{"factors":["Adeno-associated virus (272636)","Dependoparvovirus anseriform1 (1511895)","Dependoparvovirus avian1 (1511894)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p22898"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p22899"},"title":{"type":"object","name":"Title","id":"p22894","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p22931","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p22884","attributes":{"selected":{"type":"object","name":"Selection","id":"p22885","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p22886"},"data":{"type":"map","entries":[["y",["Adeno-associated virus (272636)","Dependoparvovirus anseriform1 (1511895)","Dependoparvovirus avian1 (1511894)"]],["share",[100.0,100.0,100.0]],["lo",[91.03331462924287,97.01846062916736,89.28208017449293]],["hi",[100.0,100.0,100.0]],["n",[39,125,32]],["det",[39,125,32]],["colour",["#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p22932","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p22933"}}},"glyph":{"type":"object","name":"Scatter","id":"p22928","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p22929","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p22930","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p22895","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p22910"},{"type":"object","name":"BoxZoomTool","id":"p22911","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p22912","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p22918","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p22917","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p22919","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p22920"},{"type":"object","name":"SaveTool","id":"p22921"},{"type":"object","name":"HoverTool","id":"p22935","attributes":{"renderers":[{"id":"p22931"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p22905","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p22906"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p22907"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22908"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p22900","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p22901","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p22902"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22903"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p22904","attributes":{"axis":{"id":"p22900"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p22909","attributes":{"dimension":1,"axis":{"id":"p22905"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p22922","attributes":{"source":{"id":"p22884"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p22934","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"f84ab6cd-c337-49cc-a99e-14d1357098a2","roots":{"p22887":"a4cb2b2c-0f1d-4ac5-92c0-e5cd3c2116e0"},"root_ids":["p22887"]}];
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

Disclosures on this entry: `oligos_modified`.


## What reached the statistics

3,240 records were screened for this assay and **2,031 (63%)** were evaluable, meaning both primers landed in the right orientation and size range. 1,209 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 903 |
| `truncated` | 302 |
| `no_pair` | 3 |

