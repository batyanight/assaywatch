# CDV_H_gene_Mueller_2011_4

<span class="aw-chip aw-chip-stable">stable</span>

**Canine distemper virus specific — H gene**

| | |
|---|---|
| Target | Morbillivirus canis (formerly Canine morbillivirus) ([taxid 3052342](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3052342)) |
| Gene | H gene |
| Chemistry | conventional |
| Amplicon | 572 bp |
| Designed | 2011 |
| Paper | [10.7589/0090-3558-47.3.725](https://doi.org/10.7589/0090-3558-47.3.725) |
| Registry status | active |

!!! quote "The paper"
    Müller A, Silva E, Santos N, Thompson G. 2011. Domestic dog origin of canine distemper virus in free-ranging wolves in Portugal as revealed by hemagglutinin gene characterization. J Wildl Dis 47:725-729

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ATCCCCCATGTGTTGACATT` | 20 nt |
| reverse | `GACCTCAGGGTATAGAATCTGG` | 22 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 87 | 87 | 100.0% | 95.8% – 100.0% |
| baseline (everything earlier) | 274 | 276 | 99.3% | 97.4% – 99.8% |

Change from baseline, Newcombe interval: **-3.5% to 2.6%**. Threshold: **90.0%**.

*detected share 100.0% (96%-100%) since Oct 2024*

Trend across deposit years: by record falling (p=0.837, 29 years); by footprint falling (p=0.655). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="b04758ec-0cde-44f0-a868-87f57c093b60" data-root-id="p6949" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"4219f6ea-d3f3-4400-b8ec-2167f3e5150e":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7004","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7005"}}},"roots":[{"type":"object","name":"Figure","id":"p6949","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p6951"},"y_range":{"type":"object","name":"Range1d","id":"p6958","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p6959"},"y_scale":{"type":"object","name":"LinearScale","id":"p6960"},"title":{"type":"object","name":"Title","id":"p6956","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p6994","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p6946","attributes":{"selected":{"type":"object","name":"Selection","id":"p6947","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p6948"},"data":{"type":"map","entries":[["year",[1993,1998,1999,2000,2001,2002,2003,2004,2005,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,96.07843137254902,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[1,2,1,1,1,3,5,2,3,4,5,4,3,3,7,9,15,8,21,10,24,23,49,9,41,12,10,12,73]],["evaluable",[1,2,1,1,1,3,5,2,3,4,5,4,3,3,7,9,15,8,21,10,24,23,51,9,41,12,10,12,73]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,9.07684386569143,8.703135093227193,8.703135093227193,8.703135093227193,9.328625426046248,9.667366891029102,9.07684386569143,9.328625426046248,9.517227179437622,9.667366891029102,9.517227179437622,9.328625426046248,9.328625426046248,9.897626379762722,10.071067811865476,10.423139468338052,9.989711205477885,10.652487636092928,10.143865699252444,10.74264168206181,10.713966621835368,11.24015070195139,10.071067811865476,11.098224018878925,10.269703144398052,10.143865699252444,10.269703144398052,11.469403343404682]]]}}},"view":{"type":"object","name":"CDSView","id":"p6995","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p6996"}}},"glyph":{"type":"object","name":"Line","id":"p6991","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p6992","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p6993","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p7000","attributes":{"data_source":{"id":"p6946"},"view":{"type":"object","name":"CDSView","id":"p7001","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7002"}}},"glyph":{"type":"object","name":"Scatter","id":"p6997","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p6998","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p6999","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p6957","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p6971"},{"type":"object","name":"BoxZoomTool","id":"p6972","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p6973","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p6979","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p6978","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p6980","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p6981"},{"type":"object","name":"SaveTool","id":"p6982"},{"type":"object","name":"HoverTool","id":"p7003","attributes":{"renderers":[{"id":"p7000"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p6966","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p6967","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p6968"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p6969"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p6961","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p6962","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p6963"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p6964"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p6965","attributes":{"axis":{"id":"p6961"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p6970","attributes":{"dimension":1,"axis":{"id":"p6966"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p6983","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p6985","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p6986","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p6987","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p6989","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p6988","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p6990","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"4219f6ea-d3f3-4400-b8ec-2167f3e5150e","roots":{"p6949":"b04758ec-0cde-44f0-a868-87f57c093b60"},"root_ids":["p6949"]}];
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

<div id="ebc69554-ce41-416b-acd1-07761ad4d8e4" data-root-id="p7009" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"99499f84-30bc-4422-a6de-2727220ee5f3":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7049","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7050"}}},"roots":[{"type":"object","name":"Figure","id":"p7009","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p7010"},"y_range":{"type":"object","name":"DataRange1d","id":"p7011","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p7018"},"y_scale":{"type":"object","name":"LinearScale","id":"p7019"},"title":{"type":"object","name":"Title","id":"p7016","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7045","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7006","attributes":{"selected":{"type":"object","name":"Selection","id":"p7007","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7008"},"data":{"type":"map","entries":[["year",[1993,1998,1999,2000,2001,2002,2003,2004,2005,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,2,1,1,1,3,5,2,3,4,5,4,3,3,7,9,15,8,21,10,24,23,51,9,41,12,10,12,73]],["detected",[1,2,1,1,1,3,5,2,3,4,5,4,3,3,7,9,15,8,21,10,24,23,49,9,41,12,10,12,73]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p7046","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7047"}}},"glyph":{"type":"object","name":"VBar","id":"p7042","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p7043","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p7044","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7017","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7030"},{"type":"object","name":"BoxZoomTool","id":"p7031","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7032","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7038","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7037","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7039","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7040"},{"type":"object","name":"SaveTool","id":"p7041"},{"type":"object","name":"HoverTool","id":"p7048","attributes":{"renderers":[{"id":"p7045"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p7025","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7026","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7027"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7028"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7020","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7021","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7022"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7023"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7024","attributes":{"axis":{"id":"p7020"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7029","attributes":{"dimension":1,"axis":{"id":"p7025"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"99499f84-30bc-4422-a6de-2727220ee5f3","roots":{"p7009":"ebc69554-ce41-416b-acd1-07761ad4d8e4"},"root_ids":["p7009"]}];
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

<div id="fbe40f08-8f10-400b-9466-c61513c942d0" data-root-id="p7054" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9c7a41cc-77e8-4227-81bf-e0acea95a853":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7096","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7097"}}},"roots":[{"type":"object","name":"Figure","id":"p7054","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p7056"},"y_range":{"type":"object","name":"FactorRange","id":"p7063","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p7064"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p7065"},"title":{"type":"object","name":"Title","id":"p7061","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7091","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7051","attributes":{"selected":{"type":"object","name":"Selection","id":"p7052","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7053"},"data":{"type":"map","entries":[["x",[-6,-1,-19,-18,-20,-9,-13,-8,-15]],["y",["forward","reverse","forward","forward","forward","forward","reverse","reverse","forward"]],["alpha",[1.0,1.0,0.9274104683195592,0.6276859504132232,0.5433884297520661,0.5059228650137741,0.4965564738292011,0.48719008264462804,0.38415977961432507]],["pos",[6,1,19,18,20,9,13,8,15]],["base",["G","G","T","C","A","G","G","G","C"]],["n",[134,129,83,51,42,38,37,36,25]],["det_with",["100% of 134","100% of 129","100% of 83","100% of 51","100% of 42","100% of 38","100% of 37","100% of 36","100% of 25"]],["det_without",["100% of 231","100% of 236","100% of 282","100% of 314","100% of 323","100% of 327","100% of 328","100% of 329","100% of 340"]],["subs",["G&gt;A 106, A&gt;G 28","G&gt;A 129","T&gt;C 82, T&gt;G 1","C&gt;T 35, C&gt;A 16","A&gt;C 32, A&gt;G 10","G&gt;A 37, G&gt;C 1","G&gt;A 37","G&gt;A 36","C&gt;T 23, T&gt;C 2"]],["zone",["no","yes","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p7092","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7093"}}},"glyph":{"type":"object","name":"Rect","id":"p7088","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p7089","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p7090","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7062","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7076"},{"type":"object","name":"BoxZoomTool","id":"p7077","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7078","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7084","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7083","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7085","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7086"},{"type":"object","name":"SaveTool","id":"p7087"},{"type":"object","name":"HoverTool","id":"p7094","attributes":{"renderers":[{"id":"p7091"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p7071","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p7072"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p7073"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7074"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7066","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p7095","attributes":{"ticks":[-20,-19,-18,-15,-13,-9,-8,-6,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7068"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-6,"6"],[-1,"1"],[-19,"19"],[-18,"18"],[-20,"20"],[-9,"9"],[-13,"13"],[-8,"8"],[-15,"15"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p7069"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7070","attributes":{"axis":{"id":"p7066"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7075","attributes":{"dimension":1,"axis":{"id":"p7071"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9c7a41cc-77e8-4227-81bf-e0acea95a853","roots":{"p7054":"fbe40f08-8f10-400b-9466-c61513c942d0"},"root_ids":["p7054"]}];
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

<div id="dfde68ed-75f6-449f-ad60-650fa3ae5ab6" data-root-id="p7101" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"3ab3959e-5fae-4fb2-9dbd-c4446eb90416":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p7150","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p7151"}}},"roots":[{"type":"object","name":"Figure","id":"p7101","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p7110","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p7111","attributes":{"factors":["Morbillivirus canis (3052342)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p7112"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p7113"},"title":{"type":"object","name":"Title","id":"p7108","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p7145","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7098","attributes":{"selected":{"type":"object","name":"Selection","id":"p7099","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7100"},"data":{"type":"map","entries":[["y",["Morbillivirus canis (3052342)"]],["share",[100.0]],["lo",[95.77124930558794]],["hi",[100.0]],["n",[87]],["det",[87]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p7146","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p7147"}}},"glyph":{"type":"object","name":"Scatter","id":"p7142","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p7143","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p7144","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7109","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p7124"},{"type":"object","name":"BoxZoomTool","id":"p7125","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p7126","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p7132","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p7131","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p7133","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p7134"},{"type":"object","name":"SaveTool","id":"p7135"},{"type":"object","name":"HoverTool","id":"p7149","attributes":{"renderers":[{"id":"p7145"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p7119","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p7120"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p7121"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7122"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7114","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7115","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7116"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7117"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7118","attributes":{"axis":{"id":"p7114"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p7123","attributes":{"dimension":1,"axis":{"id":"p7119"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p7136","attributes":{"source":{"id":"p7098"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p7148","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"3ab3959e-5fae-4fb2-9dbd-c4446eb90416","roots":{"p7101":"dfde68ed-75f6-449f-ad60-650fa3ae5ab6"},"root_ids":["p7101"]}];
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

Disclosures on this entry: `pairing_is_curator_reading`.


## What reached the statistics

3,952 records were screened for this assay and **363 (9%)** were evaluable, meaning both primers landed in the right orientation and size range. 3,589 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `truncated` | 1,797 |
| `no_site` | 1,554 |
| `chance_anchor` | 238 |

