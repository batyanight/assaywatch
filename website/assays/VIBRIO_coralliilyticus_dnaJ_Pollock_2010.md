# VIBRIO_coralliilyticus_dnaJ_Pollock_2010

<span class="aw-chip aw-chip-watch">watch</span>

**VIBRIO CORALLIILYTICUS — dnaJ TaqMan MGB qPCR (Pollock 2010)**

| | |
|---|---|
| Target | Vibrio coralliilyticus ([taxid 190893](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=190893)) |
| Gene | dnaJ |
| Chemistry | mgb |
| Amplicon | 128 bp |
| Designed | 2010 |
| Paper | [10.1128/aem.00330-10](https://doi.org/10.1128/aem.00330-10) |
| Registry status | active |

!!! quote "The paper"
    Pollock, F. J., Morris, P. J., Willis, B. L. & Bourne, D. G. Detection and Quantification of the Coral Pathogen Vibrio coralliilyticus by Real-Time PCR with TaqMan Fluorescent Probes. Applied and Environmental Microbiology 76, 5282-5286 (2010).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CGGTTCGYGGTGTTTCAAAA` | 20 nt |
| reverse | `AACCTGACCATGACCGTGACA` | 21 nt |
| probe | `CAGTGGCGCGAAG` | 13 nt |

## The verdict, and the numbers behind it

**watch** — below the threshold with an interval that still covers it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 12 | 15 | 80.0% | 54.8% – 93.0% |
| baseline (everything earlier) | 34 | 56 | 60.7% | 47.6% – 72.4% |

Change from baseline, Newcombe interval: **-8.5% to 37.7%**. Threshold: **90.0%**.

*detected share 80.0% is below the 90% threshold, but its interval (55%-93%) still reaches it*

Trend across deposit years: by record rising (p=0.93, 16 years); by footprint falling (p=0.308); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="c4dc1052-dd26-4130-8e5b-3344650e70e1" data-root-id="p34023" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"0ae59d96-92cc-430b-9432-c9c8bda796cd":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p34078","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p34079"}}},"roots":[{"type":"object","name":"Figure","id":"p34023","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p34025"},"y_range":{"type":"object","name":"Range1d","id":"p34032","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p34033"},"y_scale":{"type":"object","name":"LinearScale","id":"p34034"},"title":{"type":"object","name":"Title","id":"p34030","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p34068","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p34020","attributes":{"selected":{"type":"object","name":"Selection","id":"p34021","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p34022"},"data":{"type":"map","entries":[["year",[2007,2009,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,40.0,0.0,75.0,0.0,0.0,70.0,0.0,0.0,0.0,85.71428571428571,100.0,75.0]],["detected",[1,2,2,2,2,0,6,0,0,14,0,0,0,6,2,9]],["evaluable",[1,2,2,2,5,3,8,1,1,20,1,2,2,7,2,12]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,9.07684386569143,9.07684386569143,9.07684386569143,9.667366891029102,9.328625426046248,9.989711205477885,8.703135093227193,8.703135093227193,10.619414831097462,8.703135093227193,9.07684386569143,9.07684386569143,9.897626379762722,9.07684386569143,10.269703144398052]]]}}},"view":{"type":"object","name":"CDSView","id":"p34069","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p34070"}}},"glyph":{"type":"object","name":"Line","id":"p34065","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b26a00","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p34066","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b26a00","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p34067","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b26a00","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p34074","attributes":{"data_source":{"id":"p34020"},"view":{"type":"object","name":"CDSView","id":"p34075","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p34076"}}},"glyph":{"type":"object","name":"Scatter","id":"p34071","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b26a00"},"hatch_color":{"type":"value","value":"#b26a00"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p34072","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b26a00"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b26a00"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p34073","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b26a00"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b26a00"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p34031","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p34045"},{"type":"object","name":"BoxZoomTool","id":"p34046","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p34047","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p34053","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p34052","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p34054","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p34055"},{"type":"object","name":"SaveTool","id":"p34056"},{"type":"object","name":"HoverTool","id":"p34077","attributes":{"renderers":[{"id":"p34074"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p34040","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34041","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34042"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34043"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p34035","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34036","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34037"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34038"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p34039","attributes":{"axis":{"id":"p34035"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p34044","attributes":{"dimension":1,"axis":{"id":"p34040"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p34057","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p34059","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p34060","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p34061","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p34063","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p34062","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p34064","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"0ae59d96-92cc-430b-9432-c9c8bda796cd","roots":{"p34023":"c4dc1052-dd26-4130-8e5b-3344650e70e1"},"root_ids":["p34023"]}];
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

<div id="b0a83854-6a9d-480f-85da-8c87a9a7f9e9" data-root-id="p34083" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"be54445f-6c45-4e5c-9d8f-741ea956c4a6":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p34123","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p34124"}}},"roots":[{"type":"object","name":"Figure","id":"p34083","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p34084"},"y_range":{"type":"object","name":"DataRange1d","id":"p34085","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p34092"},"y_scale":{"type":"object","name":"LinearScale","id":"p34093"},"title":{"type":"object","name":"Title","id":"p34090","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p34119","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p34080","attributes":{"selected":{"type":"object","name":"Selection","id":"p34081","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p34082"},"data":{"type":"map","entries":[["year",[2007,2009,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,2,2,2,5,3,8,1,1,20,1,2,2,7,2,12]],["detected",[1,2,2,2,2,0,6,0,0,14,0,0,0,6,2,9]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b26a00","#b26a00","#b26a00"]]]}}},"view":{"type":"object","name":"CDSView","id":"p34120","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p34121"}}},"glyph":{"type":"object","name":"VBar","id":"p34116","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p34117","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p34118","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p34091","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p34104"},{"type":"object","name":"BoxZoomTool","id":"p34105","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p34106","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p34112","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p34111","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p34113","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p34114"},{"type":"object","name":"SaveTool","id":"p34115"},{"type":"object","name":"HoverTool","id":"p34122","attributes":{"renderers":[{"id":"p34119"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p34099","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34100","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34101"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34102"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p34094","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34095","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34096"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34097"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p34098","attributes":{"axis":{"id":"p34094"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p34103","attributes":{"dimension":1,"axis":{"id":"p34099"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"be54445f-6c45-4e5c-9d8f-741ea956c4a6","roots":{"p34083":"b0a83854-6a9d-480f-85da-8c87a9a7f9e9"},"root_ids":["p34083"]}];
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

<div id="e5ab34dd-82c6-433a-8c62-95b757978e5d" data-root-id="p34128" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"38beb2ce-c206-4ba1-988b-77b75cefbe46":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p34170","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p34171"}}},"roots":[{"type":"object","name":"Figure","id":"p34128","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p34130"},"y_range":{"type":"object","name":"FactorRange","id":"p34137","attributes":{"factors":["probe"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p34138"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p34139"},"title":{"type":"object","name":"Title","id":"p34135","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p34165","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p34125","attributes":{"selected":{"type":"object","name":"Selection","id":"p34126","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p34127"},"data":{"type":"map","entries":[["x",[-10,-7]],["y",["probe","probe"]],["alpha",[1.0,1.0]],["pos",[10,7]],["base",["T","C"]],["n",[23,21]],["det_with",["0% of 23","0% of 21"]],["det_without",["96% of 48","92% of 50"]],["subs",["T&gt;C 23","C&gt;T 21"]],["zone",["no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p34166","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p34167"}}},"glyph":{"type":"object","name":"Rect","id":"p34162","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p34163","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p34164","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p34136","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p34150"},{"type":"object","name":"BoxZoomTool","id":"p34151","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p34152","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p34158","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p34157","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p34159","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p34160"},{"type":"object","name":"SaveTool","id":"p34161"},{"type":"object","name":"HoverTool","id":"p34168","attributes":{"renderers":[{"id":"p34165"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p34145","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p34146"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p34147"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34148"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p34140","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p34169","attributes":{"ticks":[-10,-7],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34142"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-10,"10"],[-7,"7"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p34143"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p34144","attributes":{"axis":{"id":"p34140"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p34149","attributes":{"dimension":1,"axis":{"id":"p34145"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"38beb2ce-c206-4ba1-988b-77b75cefbe46","roots":{"p34128":"e5ab34dd-82c6-433a-8c62-95b757978e5d"},"root_ids":["p34128"]}];
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
dnaJ[All Fields] OR "complete genome"[Title] OR "chromosome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `primer_site_polymorphic`.


## What reached the statistics

139 records were screened for this assay and **71 (51%)** were evaluable, meaning both primers landed in the right orientation and size range. 68 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 53 |
| `truncated` | 13 |
| `chance_only` | 2 |

