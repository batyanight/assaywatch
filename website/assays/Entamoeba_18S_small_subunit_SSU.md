# Entamoeba_18S_small_subunit_SSU

<span class="aw-chip aw-chip-stable">stable</span>

**Entamoeba — 18S small subunit (SSU)**

| | |
|---|---|
| Target | Entamoeba ([taxid 5758](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=5758)) |
| Gene | 18S small subunit (SSU) |
| Chemistry | conventional |
| Amplicon | 572 bp |
| Designed | — |
| Paper | [10.1638/2020-0148](https://doi.org/10.1638/2020-0148) |
| Registry status | draft |

!!! quote "The paper"
    McFarland A, Conley KJ, Seimon TA, Sykes JM. 2021. A retrospective analysis of amoebiasis in reptiles in a zoological institution. J Zoo Wildl Med 52:232-240

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CGAACGAGACTKDAWCYTATTWAT` | 24 nt |
| reverse | `AATTTCACCTHTWTNTTCAATC` | 22 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (48 months, from Oct 2022) | 80 | 80 | 100.0% | 95.4% – 100.0% |
| baseline (everything earlier) | 134 | 134 | 100.0% | 97.2% – 100.0% |

Change from baseline, Newcombe interval: **-4.6% to 2.8%**. Threshold: **90.0%**.

*detected share 100.0% (95%-100%) since Oct 2022 (window widened to 48 months to reach 15 evaluable records)*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="c22740d5-5e23-4df4-91f3-2aee8974eaca" data-root-id="p12463" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"48f48e43-33a5-452e-8b78-45d6c4f60645":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12518","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12519"}}},"roots":[{"type":"object","name":"Figure","id":"p12463","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p12465"},"y_range":{"type":"object","name":"Range1d","id":"p12472","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p12473"},"y_scale":{"type":"object","name":"LinearScale","id":"p12474"},"title":{"type":"object","name":"Title","id":"p12470","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12508","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12460","attributes":{"selected":{"type":"object","name":"Selection","id":"p12461","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12462"},"data":{"type":"map","entries":[["year",[1991,1992,1995,1996,1999,2002,2004,2005,2007,2008,2009,2010,2011,2012,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[1,1,1,1,10,1,1,3,6,1,3,38,1,3,9,2,9,6,34,1,1,3,67,2,8,1]],["evaluable",[1,1,1,1,10,1,1,3,6,1,3,38,1,3,9,2,9,6,34,1,1,3,67,2,8,1]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193,10.143865699252444,8.703135093227193,8.703135093227193,9.328625426046248,9.791719296345839,8.703135093227193,9.328625426046248,11.048392086352559,8.703135093227193,9.328625426046248,10.071067811865476,9.07684386569143,10.071067811865476,9.791719296345839,10.975067467348278,8.703135093227193,8.703135093227193,9.328625426046248,11.415029579131373,9.07684386569143,9.989711205477885,8.703135093227193]]]}}},"view":{"type":"object","name":"CDSView","id":"p12509","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12510"}}},"glyph":{"type":"object","name":"Line","id":"p12505","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p12506","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p12507","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p12514","attributes":{"data_source":{"id":"p12460"},"view":{"type":"object","name":"CDSView","id":"p12515","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12516"}}},"glyph":{"type":"object","name":"Scatter","id":"p12511","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p12512","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p12513","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12471","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12485"},{"type":"object","name":"BoxZoomTool","id":"p12486","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12487","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12493","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12492","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12494","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12495"},{"type":"object","name":"SaveTool","id":"p12496"},{"type":"object","name":"HoverTool","id":"p12517","attributes":{"renderers":[{"id":"p12514"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p12480","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12481","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12482"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12483"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12475","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12476","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12477"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12478"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12479","attributes":{"axis":{"id":"p12475"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12484","attributes":{"dimension":1,"axis":{"id":"p12480"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p12497","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2021.5,"right":{"type":"object","name":"Node","id":"p12499","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p12500","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p12501","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p12503","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12502","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p12504","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"48f48e43-33a5-452e-8b78-45d6c4f60645","roots":{"p12463":"c22740d5-5e23-4df4-91f3-2aee8974eaca"},"root_ids":["p12463"]}];
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

<div id="fdc63398-4ffe-49fd-9336-9f7f84c97afb" data-root-id="p12523" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b5de8104-62d3-441d-bf73-5a6c5a0124c4":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12563","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12564"}}},"roots":[{"type":"object","name":"Figure","id":"p12523","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p12524"},"y_range":{"type":"object","name":"DataRange1d","id":"p12525","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p12532"},"y_scale":{"type":"object","name":"LinearScale","id":"p12533"},"title":{"type":"object","name":"Title","id":"p12530","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12559","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12520","attributes":{"selected":{"type":"object","name":"Selection","id":"p12521","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12522"},"data":{"type":"map","entries":[["year",[1991,1992,1995,1996,1999,2002,2004,2005,2007,2008,2009,2010,2011,2012,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,1,1,10,1,1,3,6,1,3,38,1,3,9,2,9,6,34,1,1,3,67,2,8,1]],["detected",[1,1,1,1,10,1,1,3,6,1,3,38,1,3,9,2,9,6,34,1,1,3,67,2,8,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p12560","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12561"}}},"glyph":{"type":"object","name":"VBar","id":"p12556","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p12557","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p12558","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12531","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12544"},{"type":"object","name":"BoxZoomTool","id":"p12545","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12546","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12552","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12551","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12553","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12554"},{"type":"object","name":"SaveTool","id":"p12555"},{"type":"object","name":"HoverTool","id":"p12562","attributes":{"renderers":[{"id":"p12559"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p12539","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12540","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12541"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12542"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12534","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12535","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12536"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12537"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12538","attributes":{"axis":{"id":"p12534"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12543","attributes":{"dimension":1,"axis":{"id":"p12539"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b5de8104-62d3-441d-bf73-5a6c5a0124c4","roots":{"p12523":"fdc63398-4ffe-49fd-9336-9f7f84c97afb"},"root_ids":["p12523"]}];
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

<div id="aac9d4fc-8981-456e-8372-5d73689f5b00" data-root-id="p12568" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9e5f9030-1a55-4a45-af1b-72985b675dba":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12610","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12611"}}},"roots":[{"type":"object","name":"Figure","id":"p12568","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p12570"},"y_range":{"type":"object","name":"FactorRange","id":"p12577","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p12578"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p12579"},"title":{"type":"object","name":"Title","id":"p12575","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12605","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12565","attributes":{"selected":{"type":"object","name":"Selection","id":"p12566","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12567"},"data":{"type":"map","entries":[["x",[-11,-10,-6]],["y",["reverse","forward","reverse"]],["alpha",[1.0,1.0,1.0]],["pos",[11,10,6]],["base",["T","W","T"]],["n",[73,71,71]],["det_with",["100% of 73","100% of 71","100% of 71"]],["det_without",["100% of 141","100% of 143","100% of 143"]],["subs",["T&gt;C 72, T&gt;A 1","W&gt;G 71","T&gt;C 71"]],["zone",["no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p12606","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12607"}}},"glyph":{"type":"object","name":"Rect","id":"p12602","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p12603","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p12604","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12576","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12590"},{"type":"object","name":"BoxZoomTool","id":"p12591","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12592","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12598","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12597","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12599","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12600"},{"type":"object","name":"SaveTool","id":"p12601"},{"type":"object","name":"HoverTool","id":"p12608","attributes":{"renderers":[{"id":"p12605"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p12585","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p12586"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p12587"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12588"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12580","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p12609","attributes":{"ticks":[-11,-10,-6],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12582"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-11,"11"],[-10,"10"],[-6,"6"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p12583"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12584","attributes":{"axis":{"id":"p12580"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12589","attributes":{"dimension":1,"axis":{"id":"p12585"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9e5f9030-1a55-4a45-af1b-72985b675dba","roots":{"p12568":"aac9d4fc-8981-456e-8372-5d73689f5b00"},"root_ids":["p12568"]}];
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

<div id="dd0debd1-cbe0-41bf-b52a-893b1ff49c88" data-root-id="p12615" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"cb8f34e9-3061-4010-a4e7-6773ef4a8840":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12664","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12665"}}},"roots":[{"type":"object","name":"Figure","id":"p12615","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p12624","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p12625","attributes":{"factors":["Entamoeba bovis (715123)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p12626"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p12627"},"title":{"type":"object","name":"Title","id":"p12622","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12659","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12612","attributes":{"selected":{"type":"object","name":"Selection","id":"p12613","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12614"},"data":{"type":"map","entries":[["y",["Entamoeba bovis (715123)"]],["share",[100.0]],["lo",[89.5730002457548]],["hi",[100.0]],["n",[33]],["det",[33]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p12660","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12661"}}},"glyph":{"type":"object","name":"Scatter","id":"p12656","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p12657","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p12658","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12623","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12638"},{"type":"object","name":"BoxZoomTool","id":"p12639","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12640","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12646","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12645","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12647","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12648"},{"type":"object","name":"SaveTool","id":"p12649"},{"type":"object","name":"HoverTool","id":"p12663","attributes":{"renderers":[{"id":"p12659"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p12633","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p12634"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p12635"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12636"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12628","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12629","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12630"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12631"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12632","attributes":{"axis":{"id":"p12628"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12637","attributes":{"dimension":1,"axis":{"id":"p12633"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p12650","attributes":{"source":{"id":"p12612"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p12662","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"cb8f34e9-3061-4010-a4e7-6773ef4a8840","roots":{"p12615":"dd0debd1-cbe0-41bf-b52a-893b1ff49c88"},"root_ids":["p12615"]}];
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
18S[Title] OR "small subunit ribosomal"[Title] OR SSU[Title] OR "ribosomal RNA"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `oligos_modified`.


## What reached the statistics

3,324 records were screened for this assay and **214 (6%)** were evaluable, meaning both primers landed in the right orientation and size range. 3,110 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 2,110 |
| `truncated` | 973 |
| `chance_anchor` | 27 |

