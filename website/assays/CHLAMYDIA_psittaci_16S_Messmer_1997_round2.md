# CHLAMYDIA_psittaci_16S_Messmer_1997_round2

<span class="aw-chip aw-chip-stable">stable</span>

**CHLAMYDIA PSITTACI — 16S rRNA nested multiplex PCR, second step (Messmer 1997)**

| | |
|---|---|
| Target | Chlamydia psittaci ([taxid 83554](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=83554)) |
| Gene | 16S rRNA |
| Chemistry | conventional |
| Amplicon | 128 bp |
| Designed | 1997 |
| Paper | [10.1128/jcm.35.8.2043-2046.1997](https://doi.org/10.1128/jcm.35.8.2043-2046.1997) |
| Registry status | active |

!!! quote "The paper"
    Messmer, T. O., Skelton, S. K., Moroney, J. F., Daugharty, H. & Fields, B. S. Application of a nested, multiplex PCR to psittacosis outbreaks. Journal of Clinical Microbiology 35, 2043-2046 (1997).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ATAATGACTTCGGTTGTTATT` | 21 nt |
| reverse | `TGTTTTAGATGCCTAAACAT` | 20 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 16 | 16 | 100.0% | 80.6% – 100.0% |
| baseline (everything earlier) | 146 | 146 | 100.0% | 97.4% – 100.0% |

Change from baseline, Newcombe interval: **-19.4% to 2.6%**. Threshold: **90.0%**.

*detected share 100.0% (81%-100%) since Oct 2024*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="c84ea810-68dc-4f8c-bd52-a06bf34a2496" data-root-id="p8084" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"93d62c2d-58c0-4a21-b253-05aa0d0b31d5":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p8139","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p8140"}}},"roots":[{"type":"object","name":"Figure","id":"p8084","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p8086"},"y_range":{"type":"object","name":"Range1d","id":"p8093","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p8094"},"y_scale":{"type":"object","name":"LinearScale","id":"p8095"},"title":{"type":"object","name":"Title","id":"p8091","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p8129","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p8081","attributes":{"selected":{"type":"object","name":"Selection","id":"p8082","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p8083"},"data":{"type":"map","entries":[["year",[1997,2003,2007,2009,2010,2011,2012,2013,2014,2015,2017,2018,2019,2020,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[43,4,1,1,1,8,10,3,2,7,13,8,9,25,10,1,1,14,1]],["evaluable",[43,4,1,1,1,8,10,3,2,7,13,8,9,25,10,1,1,14,1]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[11.129349107533436,9.517227179437622,8.703135093227193,8.703135093227193,8.703135093227193,9.989711205477885,10.143865699252444,9.328625426046248,9.07684386569143,9.897626379762722,10.324834530005162,9.989711205477885,10.071067811865476,10.770092258092593,10.143865699252444,8.703135093227193,8.703135093227193,10.37579022724969,8.703135093227193]]]}}},"view":{"type":"object","name":"CDSView","id":"p8130","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8131"}}},"glyph":{"type":"object","name":"Line","id":"p8126","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p8127","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p8128","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p8135","attributes":{"data_source":{"id":"p8081"},"view":{"type":"object","name":"CDSView","id":"p8136","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8137"}}},"glyph":{"type":"object","name":"Scatter","id":"p8132","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p8133","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p8134","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p8092","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p8106"},{"type":"object","name":"BoxZoomTool","id":"p8107","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p8108","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p8114","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8113","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p8115","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p8116"},{"type":"object","name":"SaveTool","id":"p8117"},{"type":"object","name":"HoverTool","id":"p8138","attributes":{"renderers":[{"id":"p8135"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p8101","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8102","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8103"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8104"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p8096","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8097","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8098"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8099"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p8100","attributes":{"axis":{"id":"p8096"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p8105","attributes":{"dimension":1,"axis":{"id":"p8101"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p8118","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p8120","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p8121","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p8122","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p8124","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8123","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p8125","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"93d62c2d-58c0-4a21-b253-05aa0d0b31d5","roots":{"p8084":"c84ea810-68dc-4f8c-bd52-a06bf34a2496"},"root_ids":["p8084"]}];
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

<div id="f99e2217-8e91-4166-a6f7-d9f4adbfabb9" data-root-id="p8144" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"4a332fad-96ff-4b66-8d26-5f81b558f545":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p8184","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p8185"}}},"roots":[{"type":"object","name":"Figure","id":"p8144","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p8145"},"y_range":{"type":"object","name":"DataRange1d","id":"p8146","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p8153"},"y_scale":{"type":"object","name":"LinearScale","id":"p8154"},"title":{"type":"object","name":"Title","id":"p8151","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p8180","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p8141","attributes":{"selected":{"type":"object","name":"Selection","id":"p8142","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p8143"},"data":{"type":"map","entries":[["year",[1997,2003,2007,2009,2010,2011,2012,2013,2014,2015,2017,2018,2019,2020,2022,2023,2024,2025,2026]],["evaluable",[43,4,1,1,1,8,10,3,2,7,13,8,9,25,10,1,1,14,1]],["detected",[43,4,1,1,1,8,10,3,2,7,13,8,9,25,10,1,1,14,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p8181","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8182"}}},"glyph":{"type":"object","name":"VBar","id":"p8177","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p8178","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p8179","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p8152","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p8165"},{"type":"object","name":"BoxZoomTool","id":"p8166","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p8167","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p8173","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8172","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p8174","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p8175"},{"type":"object","name":"SaveTool","id":"p8176"},{"type":"object","name":"HoverTool","id":"p8183","attributes":{"renderers":[{"id":"p8180"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p8160","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8161","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8162"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8163"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p8155","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8156","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8157"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8158"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p8159","attributes":{"axis":{"id":"p8155"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p8164","attributes":{"dimension":1,"axis":{"id":"p8160"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"4a332fad-96ff-4b66-8d26-5f81b558f545","roots":{"p8144":"f99e2217-8e91-4166-a6f7-d9f4adbfabb9"},"root_ids":["p8144"]}];
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

<div id="b88daf71-808b-4b38-aae6-1ddbba842f30" data-root-id="p8189" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"8828df53-3c2e-43bc-a1c5-ac4f141daf5e":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p8231","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p8232"}}},"roots":[{"type":"object","name":"Figure","id":"p8189","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p8191"},"y_range":{"type":"object","name":"FactorRange","id":"p8198","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p8199"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p8200"},"title":{"type":"object","name":"Title","id":"p8196","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p8226","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p8186","attributes":{"selected":{"type":"object","name":"Selection","id":"p8187","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p8188"},"data":{"type":"map","entries":[["x",[-6,-18,-10,-11]],["y",["forward","reverse","reverse","reverse"]],["alpha",[1.0,0.9895061728395061,0.5907407407407407,0.5907407407407407]],["pos",[6,18,10,11]],["base",["G","T","G","T"]],["n",[59,40,21,21]],["det_with",["100% of 59","100% of 40","100% of 21","100% of 21"]],["det_without",["100% of 103","100% of 122","100% of 141","100% of 141"]],["subs",["G&gt;A 58, G&gt;T 1","T&gt;C 40","G&gt;T 21","T&gt;A 21"]],["zone",["no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p8227","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8228"}}},"glyph":{"type":"object","name":"Rect","id":"p8223","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p8224","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p8225","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p8197","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p8211"},{"type":"object","name":"BoxZoomTool","id":"p8212","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p8213","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p8219","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8218","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p8220","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p8221"},{"type":"object","name":"SaveTool","id":"p8222"},{"type":"object","name":"HoverTool","id":"p8229","attributes":{"renderers":[{"id":"p8226"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p8206","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p8207"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p8208"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8209"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p8201","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p8230","attributes":{"ticks":[-18,-11,-10,-6],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8203"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-6,"6"],[-18,"18"],[-10,"10"],[-11,"11"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p8204"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p8205","attributes":{"axis":{"id":"p8201"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p8210","attributes":{"dimension":1,"axis":{"id":"p8206"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"8828df53-3c2e-43bc-a1c5-ac4f141daf5e","roots":{"p8189":"b88daf71-808b-4b38-aae6-1ddbba842f30"},"root_ids":["p8189"]}];
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
16S[Title] OR "16S ribosomal RNA"[Title] OR "small subunit ribosomal"[Title] OR "complete genome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `cross_reactive`.


## What reached the statistics

270 records were screened for this assay and **162 (60%)** were evaluable, meaning both primers landed in the right orientation and size range. 108 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 94 |
| `truncated` | 14 |

