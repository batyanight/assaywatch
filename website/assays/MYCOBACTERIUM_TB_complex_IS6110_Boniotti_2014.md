# MYCOBACTERIUM_TB_complex_IS6110_Boniotti_2014

<span class="aw-chip aw-chip-stable">stable</span>

**MYCOBACTERIUM TUBERCULOSIS COMPLEX — IS6110 PCR (Boniotti 2014)**

| | |
|---|---|
| Target | Mycobacterium tuberculosis complex ([taxid 77643](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=77643)) |
| Gene | IS6110 |
| Chemistry | conventional |
| Amplicon | 209 bp |
| Designed | 2014 |
| Paper | [10.1128/jcm.00440-14](https://doi.org/10.1128/jcm.00440-14) |
| Registry status | active |

!!! quote "The paper"
    Boniotti, M. B., Gaffuri, A., Gelmetti, D., Tagliabue, S., Chiari, M., Mangeli, A., Spisani, M., Nassuato, C., Gibelli, L., Sacchi, C., Zanoni, M. & Pacciarini, M. L. Detection and Molecular Characterization of Mycobacterium microti Isolates in Wild Boar from Northern Italy. Journal of Clinical Microbiology 52, 2834-2843 (2014).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CCCGGACAGGCCGAGTTT` | 18 nt |
| reverse | `CCCCATCGACCTACTACG` | 18 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 274 | 274 | 100.0% | 98.6% – 100.0% |
| baseline (everything earlier) | 3,731 | 3,738 | 99.8% | 99.6% – 99.9% |

Change from baseline, Newcombe interval: **-1.2% to 0.4%**. Threshold: **90.0%**.

*detected share 100.0% (99%-100%) since Oct 2024*

Trend across deposit years: by record rising (p=0.00708, 29 years). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="aba9ed4d-0a80-40dc-8d12-8d90ff29bb9b" data-root-id="p18279" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"016aed03-36e3-421d-83d4-5b445afe8650":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p18334","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p18335"}}},"roots":[{"type":"object","name":"Figure","id":"p18279","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p18281"},"y_range":{"type":"object","name":"Range1d","id":"p18288","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p18289"},"y_scale":{"type":"object","name":"LinearScale","id":"p18290"},"title":{"type":"object","name":"Title","id":"p18286","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p18324","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p18276","attributes":{"selected":{"type":"object","name":"Selection","id":"p18277","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p18278"},"data":{"type":"map","entries":[["year",[1990,1992,1996,1997,1998,1999,2001,2002,2004,2005,2007,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,66.66666666666666,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,99.9057048561999,100.0,100.0,100.0,100.0,100.0,91.8918918918919,100.0,100.0,100.0,100.0,100.0]],["detected",[1,1,1,8,2,4,2,2,1,3,8,7,9,22,14,32,49,2119,561,184,68,32,216,34,84,185,91,109,156]],["evaluable",[1,1,1,8,2,6,2,2,1,3,8,7,9,22,14,32,49,2121,561,184,68,32,216,37,84,185,91,109,156]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,8.703135093227193,9.989711205477885,9.07684386569143,9.791719296345839,9.07684386569143,9.07684386569143,8.703135093227193,9.328625426046248,9.989711205477885,9.897626379762722,10.071067811865476,10.683957047019447,10.37579022724969,10.934913263353746,11.214271124597754,13.400415111385366,12.682117944397627,12.03765971975463,11.42444225266168,10.934913263353746,12.132989288629066,11.030852377887435,11.557772674175059,12.040897278779795,11.607827582127728,11.71979455772644,11.938539663179375]]]}}},"view":{"type":"object","name":"CDSView","id":"p18325","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p18326"}}},"glyph":{"type":"object","name":"Line","id":"p18321","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p18322","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p18323","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p18330","attributes":{"data_source":{"id":"p18276"},"view":{"type":"object","name":"CDSView","id":"p18331","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p18332"}}},"glyph":{"type":"object","name":"Scatter","id":"p18327","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p18328","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p18329","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p18287","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p18301"},{"type":"object","name":"BoxZoomTool","id":"p18302","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p18303","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p18309","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p18308","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p18310","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p18311"},{"type":"object","name":"SaveTool","id":"p18312"},{"type":"object","name":"HoverTool","id":"p18333","attributes":{"renderers":[{"id":"p18330"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p18296","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18297","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18298"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18299"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p18291","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18292","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18293"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18294"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p18295","attributes":{"axis":{"id":"p18291"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p18300","attributes":{"dimension":1,"axis":{"id":"p18296"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p18313","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p18315","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p18316","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p18317","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p18319","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p18318","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p18320","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"016aed03-36e3-421d-83d4-5b445afe8650","roots":{"p18279":"aba9ed4d-0a80-40dc-8d12-8d90ff29bb9b"},"root_ids":["p18279"]}];
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

<div id="f2da4c01-7614-4d7a-b0a5-5c739df7416c" data-root-id="p18339" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"2b8814f9-019c-447f-94ec-3530cd2fb37b":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p18379","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p18380"}}},"roots":[{"type":"object","name":"Figure","id":"p18339","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p18340"},"y_range":{"type":"object","name":"DataRange1d","id":"p18341","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p18348"},"y_scale":{"type":"object","name":"LinearScale","id":"p18349"},"title":{"type":"object","name":"Title","id":"p18346","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p18375","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p18336","attributes":{"selected":{"type":"object","name":"Selection","id":"p18337","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p18338"},"data":{"type":"map","entries":[["year",[1990,1992,1996,1997,1998,1999,2001,2002,2004,2005,2007,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,1,8,2,6,2,2,1,3,8,7,9,22,14,32,49,2121,561,184,68,32,216,37,84,185,91,109,156]],["detected",[1,1,1,8,2,4,2,2,1,3,8,7,9,22,14,32,49,2119,561,184,68,32,216,34,84,185,91,109,156]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p18376","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p18377"}}},"glyph":{"type":"object","name":"VBar","id":"p18372","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p18373","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p18374","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p18347","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p18360"},{"type":"object","name":"BoxZoomTool","id":"p18361","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p18362","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p18368","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p18367","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p18369","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p18370"},{"type":"object","name":"SaveTool","id":"p18371"},{"type":"object","name":"HoverTool","id":"p18378","attributes":{"renderers":[{"id":"p18375"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p18355","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18356","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18357"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18358"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p18350","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18351","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18352"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18353"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p18354","attributes":{"axis":{"id":"p18350"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p18359","attributes":{"dimension":1,"axis":{"id":"p18355"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"2b8814f9-019c-447f-94ec-3530cd2fb37b","roots":{"p18339":"f2da4c01-7614-4d7a-b0a5-5c739df7416c"},"root_ids":["p18339"]}];
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

<p class="aw-empty">No position carried a mismatch in enough records to report.</p>


## By lineage

A single pooled percentage hides the clade you may actually care about:
published misses are nearly always specific to one lineage, and a clade that is
5% of deposits can be 100% of the cases in one region. Lineages with too few
records to say anything are left out.

<div id="e5ad454c-dcac-4cb6-979f-a97505b9143d" data-root-id="p18384" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9fe893a3-ea44-49b6-962a-487d44fa89e2":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p18433","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p18434"}}},"roots":[{"type":"object","name":"Figure","id":"p18384","attributes":{"height":132,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p18393","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p18394","attributes":{"factors":["Mycobacterium tuberculosis (1773)","unresolved"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p18395"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p18396"},"title":{"type":"object","name":"Title","id":"p18391","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p18428","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p18381","attributes":{"selected":{"type":"object","name":"Selection","id":"p18382","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p18383"},"data":{"type":"map","entries":[["y",["Mycobacterium tuberculosis (1773)","unresolved"]],["share",[100.0,100.0]],["lo",[98.40498440779082,90.59421741627975]],["hi",[100.0,100.0]],["n",[237,37]],["det",[237,37]],["colour",["#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p18429","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p18430"}}},"glyph":{"type":"object","name":"Scatter","id":"p18425","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p18426","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p18427","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p18392","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p18407"},{"type":"object","name":"BoxZoomTool","id":"p18408","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p18409","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p18415","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p18414","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p18416","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p18417"},{"type":"object","name":"SaveTool","id":"p18418"},{"type":"object","name":"HoverTool","id":"p18432","attributes":{"renderers":[{"id":"p18428"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p18402","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p18403"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p18404"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18405"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p18397","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18398","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18399"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18400"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p18401","attributes":{"axis":{"id":"p18397"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p18406","attributes":{"dimension":1,"axis":{"id":"p18402"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p18419","attributes":{"source":{"id":"p18381"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p18431","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9fe893a3-ea44-49b6-962a-487d44fa89e2","roots":{"p18384":"e5ad454c-dcac-4cb6-979f-a97505b9143d"},"root_ids":["p18384"]}];
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
IS6110[All Fields] OR "complete genome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).


## What reached the statistics

4,805 records were screened for this assay and **4,012 (83%)** were evaluable, meaning both primers landed in the right orientation and size range. 793 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 524 |
| `chance_only` | 205 |
| `truncated` | 61 |
| `no_pair` | 2 |
| `chance_anchor` | 1 |

