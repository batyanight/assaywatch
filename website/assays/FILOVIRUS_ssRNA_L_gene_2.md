# FILOVIRUS_ssRNA_L_gene_2

<span class="aw-chip aw-chip-stable">stable</span>

**FILOVIRUS (ssRNA) — L gene**

| | |
|---|---|
| Target | Filoviridae ([taxid 11266](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11266)) |
| Gene | L gene |
| Chemistry | conventional |
| Amplicon | 634 bp |
| Designed | 2007 |
| Paper | [10.1128/Jcm.01893-06](https://doi.org/10.1128/Jcm.01893-06) |
| Registry status | active |

!!! quote "The paper"
    Zhai, J. H. et al. Rapid molecular strategy for filovirus detection and characterization. Journal of clinical microbiology 45, 224-226, doi:Doi 10.1128/Jcm.01893-06 (2007).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `TNTTYTCHVTNCAAAANCAYTGGG` | 24 nt |
| reverse | `GCYTCNSMNANNGTTTGNACATT` | 23 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 40 | 40 | 100.0% | 91.2% – 100.0% |
| baseline (everything earlier) | 3,511 | 3,537 | 99.3% | 98.9% – 99.5% |

Change from baseline, Newcombe interval: **-8.0% to 1.1%**. Threshold: **90.0%**.

*detected share 100.0% (91%-100%) since Oct 2024*

Trend across deposit years: by record falling (p=0.992, 27 years); by footprint falling (p=0.603). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="d1eb0e7b-fb0a-4c36-ad52-cb55d73f0625" data-root-id="p12875" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"f40bc92a-1932-4aa9-a95b-947432c25e5c":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12930","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12931"}}},"roots":[{"type":"object","name":"Figure","id":"p12875","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p12877"},"y_range":{"type":"object","name":"Range1d","id":"p12884","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p12885"},"y_scale":{"type":"object","name":"LinearScale","id":"p12886"},"title":{"type":"object","name":"Title","id":"p12882","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12920","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12872","attributes":{"selected":{"type":"object","name":"Selection","id":"p12873","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12874"},"data":{"type":"map","entries":[["year",[1997,1999,2000,2001,2002,2003,2004,2006,2007,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,66.66666666666666,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,81.81818181818183,100.0,100.0,100.0,100.0,99.89373007438896,99.56663055254604,100.0,99.07834101382488,100.0,71.42857142857143,98.41954022988506,100.0,100.0,98.71794871794873,100.0,100.0]],["detected",[1,2,1,1,4,1,1,2,2,22,18,5,2,21,118,940,919,142,215,268,5,685,24,36,77,1,38]],["evaluable",[1,3,1,1,4,1,1,2,2,22,22,5,2,21,118,941,923,142,217,268,7,696,24,36,78,1,38]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,9.328625426046248,8.703135093227193,8.703135093227193,9.517227179437622,8.703135093227193,8.703135093227193,9.07684386569143,9.07684386569143,10.683957047019447,10.683957047019447,9.667366891029102,9.07684386569143,10.652487636092928,11.768618707345716,12.967510851251777,12.956997503288964,11.881632785508899,12.135721774447552,12.259795192122782,9.897626379762722,12.802082403879812,10.74264168206181,11.012804945939648,11.511208920139431,8.703135093227193,11.048392086352559]]]}}},"view":{"type":"object","name":"CDSView","id":"p12921","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12922"}}},"glyph":{"type":"object","name":"Line","id":"p12917","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p12918","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p12919","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p12926","attributes":{"data_source":{"id":"p12872"},"view":{"type":"object","name":"CDSView","id":"p12927","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12928"}}},"glyph":{"type":"object","name":"Scatter","id":"p12923","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p12924","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p12925","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12883","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12897"},{"type":"object","name":"BoxZoomTool","id":"p12898","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12899","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12905","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12904","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12906","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12907"},{"type":"object","name":"SaveTool","id":"p12908"},{"type":"object","name":"HoverTool","id":"p12929","attributes":{"renderers":[{"id":"p12926"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p12892","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12893","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12894"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12895"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12887","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12888","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12889"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12890"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12891","attributes":{"axis":{"id":"p12887"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12896","attributes":{"dimension":1,"axis":{"id":"p12892"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p12909","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p12911","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p12912","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p12913","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p12915","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12914","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p12916","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"f40bc92a-1932-4aa9-a95b-947432c25e5c","roots":{"p12875":"d1eb0e7b-fb0a-4c36-ad52-cb55d73f0625"},"root_ids":["p12875"]}];
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

<div id="be32b638-3ab2-419b-b1be-e74a91f0f7d8" data-root-id="p12935" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"13638afb-4e36-44b3-bbdc-cfc9b8c2d77a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12975","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12976"}}},"roots":[{"type":"object","name":"Figure","id":"p12935","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p12936"},"y_range":{"type":"object","name":"DataRange1d","id":"p12937","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p12944"},"y_scale":{"type":"object","name":"LinearScale","id":"p12945"},"title":{"type":"object","name":"Title","id":"p12942","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12971","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12932","attributes":{"selected":{"type":"object","name":"Selection","id":"p12933","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12934"},"data":{"type":"map","entries":[["year",[1997,1999,2000,2001,2002,2003,2004,2006,2007,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,3,1,1,4,1,1,2,2,22,22,5,2,21,118,941,923,142,217,268,7,696,24,36,78,1,38]],["detected",[1,2,1,1,4,1,1,2,2,22,18,5,2,21,118,940,919,142,215,268,5,685,24,36,77,1,38]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p12972","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12973"}}},"glyph":{"type":"object","name":"VBar","id":"p12968","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p12969","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p12970","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12943","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12956"},{"type":"object","name":"BoxZoomTool","id":"p12957","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12958","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12964","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12963","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12965","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12966"},{"type":"object","name":"SaveTool","id":"p12967"},{"type":"object","name":"HoverTool","id":"p12974","attributes":{"renderers":[{"id":"p12971"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p12951","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12952","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12953"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12954"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12946","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12947","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12948"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12949"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12950","attributes":{"axis":{"id":"p12946"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12955","attributes":{"dimension":1,"axis":{"id":"p12951"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"13638afb-4e36-44b3-bbdc-cfc9b8c2d77a","roots":{"p12935":"be32b638-3ab2-419b-b1be-e74a91f0f7d8"},"root_ids":["p12935"]}];
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

<div id="ddc79553-83bf-4e1e-8c85-87bb6c4a306f" data-root-id="p12980" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"5f230c8b-ac46-494d-9234-0a2c4e2d5765":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p13022","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p13023"}}},"roots":[{"type":"object","name":"Figure","id":"p12980","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p12982"},"y_range":{"type":"object","name":"FactorRange","id":"p12989","attributes":{"factors":["forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p12990"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p12991"},"title":{"type":"object","name":"Title","id":"p12987","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p13017","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12977","attributes":{"selected":{"type":"object","name":"Selection","id":"p12978","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12979"},"data":{"type":"map","entries":[["x",[-16]],["y",["forward"]],["alpha",[0.17376292982946603]],["pos",[16]],["base",["V"]],["n",[25]],["det_with",["100% of 25"]],["det_without",["100% of 3549"]],["subs",["V&gt;T 25"]],["zone",["no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p13018","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13019"}}},"glyph":{"type":"object","name":"Rect","id":"p13014","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p13015","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p13016","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12988","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p13002"},{"type":"object","name":"BoxZoomTool","id":"p13003","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p13004","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p13010","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13009","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p13011","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p13012"},{"type":"object","name":"SaveTool","id":"p13013"},{"type":"object","name":"HoverTool","id":"p13020","attributes":{"renderers":[{"id":"p13017"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p12997","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p12998"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p12999"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13000"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12992","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p13021","attributes":{"ticks":[-16],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12994"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-16,"16"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p12995"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12996","attributes":{"axis":{"id":"p12992"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p13001","attributes":{"dimension":1,"axis":{"id":"p12997"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"5f230c8b-ac46-494d-9234-0a2c4e2d5765","roots":{"p12980":"ddc79553-83bf-4e1e-8c85-87bb6c4a306f"},"root_ids":["p12980"]}];
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

<div id="b832ebe2-8be8-4b60-858b-a318bf0bb963" data-root-id="p13027" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"1b378d0c-c597-4eaa-ab13-f2b6d8c55dc9":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p13076","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p13077"}}},"roots":[{"type":"object","name":"Figure","id":"p13027","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p13036","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p13037","attributes":{"factors":["Orthoebolavirus zairense (3052462)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p13038"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p13039"},"title":{"type":"object","name":"Title","id":"p13034","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p13071","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p13024","attributes":{"selected":{"type":"object","name":"Selection","id":"p13025","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p13026"},"data":{"type":"map","entries":[["y",["Orthoebolavirus zairense (3052462)"]],["share",[100.0]],["lo",[91.03331462924287]],["hi",[100.0]],["n",[39]],["det",[39]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p13072","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13073"}}},"glyph":{"type":"object","name":"Scatter","id":"p13068","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p13069","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p13070","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p13035","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p13050"},{"type":"object","name":"BoxZoomTool","id":"p13051","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p13052","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p13058","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13057","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p13059","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p13060"},{"type":"object","name":"SaveTool","id":"p13061"},{"type":"object","name":"HoverTool","id":"p13075","attributes":{"renderers":[{"id":"p13071"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p13045","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p13046"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p13047"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13048"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p13040","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13041","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13042"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13043"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p13044","attributes":{"axis":{"id":"p13040"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p13049","attributes":{"dimension":1,"axis":{"id":"p13045"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p13062","attributes":{"source":{"id":"p13024"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p13074","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"1b378d0c-c597-4eaa-ab13-f2b6d8c55dc9","roots":{"p13027":"b832ebe2-8be8-4b60-858b-a318bf0bb963"},"root_ids":["p13027"]}];
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

4,647 records were screened for this assay and **3,577 (77%)** were evaluable, meaning both primers landed in the right orientation and size range. 1,070 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 500 |
| `chance_only` | 148 |
| `chance_anchor` | 37 |
| `truncated` | 10 |

