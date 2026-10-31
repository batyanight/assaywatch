# Nipah_N_gene_2

<span class="aw-chip aw-chip-stable">stable</span>

**Nipah — N gene**

| | |
|---|---|
| Target | Henipavirus nipahense (formerly Nipah henipavirus) ([taxid 3052225](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3052225)) |
| Gene | N gene |
| Chemistry | conventional |
| Amplicon | 227 bp |
| Designed | 2000 |
| Paper | [10.1126/science.288.5470.1432](https://doi.org/10.1126/science.288.5470.1432) |
| Registry status | active |

!!! quote "The paper"
    Chua KB, Bellini WJ, Rota PA, Harcourt BH, Tamin A, Lam SK, Ksiazek TG, Rollin PE, Zaki SR, Shieh WJ, Goldsmith CS, Gubler DJ, Roehrig JT, Eaton B, Gould AR, Olson J, Field H, Daniels P, Ling AE, Peters CJ, Anderson LJ, Mahy BWJ. 2000. Nipah virus - a recently emergent deadly paramyxovirus. Science 288:1432-1435

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CTGCTGCAGTTCAGGAAACATCAG` | 24 nt |
| reverse | `ACCGGATGTGCTCACAGAACTG` | 22 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 23 | 23 | 100.0% | 85.7% – 100.0% |
| baseline (everything earlier) | 269 | 275 | 97.8% | 95.3% – 99.0% |

Change from baseline, Newcombe interval: **-12.2% to 4.7%**. Threshold: **90.0%**.

*detected share 100.0% (86%-100%) since Oct 2024*

Trend across deposit years: by record rising (p=0.125, 23 years); by footprint rising (p=0.755). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="ac106c96-6dee-456c-a40a-40b28c8c338e" data-root-id="p19766" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"3c0af1a5-0680-4688-beb6-97dce18bb92e":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p19821","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p19822"}}},"roots":[{"type":"object","name":"Figure","id":"p19766","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p19768"},"y_range":{"type":"object","name":"Range1d","id":"p19775","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p19776"},"y_scale":{"type":"object","name":"LinearScale","id":"p19777"},"title":{"type":"object","name":"Title","id":"p19773","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p19811","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p19763","attributes":{"selected":{"type":"object","name":"Selection","id":"p19764","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p19765"},"data":{"type":"map","entries":[["year",[2000,2001,2002,2004,2005,2007,2008,2009,2010,2012,2013,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,33.33333333333333,100.0,100.0,100.0,100.0,100.0,100.0,100.0,94.5945945945946,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[2,2,1,3,5,19,1,37,2,8,8,3,11,2,2,18,35,56,3,1,58,9,6]],["evaluable",[2,2,1,3,5,19,1,37,6,8,8,3,11,2,2,18,37,56,3,1,58,9,6]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,9.07684386569143,8.703135093227193,9.328625426046248,9.667366891029102,10.584573151575475,8.703135093227193,11.030852377887435,9.791719296345839,9.989711205477885,9.989711205477885,9.328625426046248,10.209683151927734,9.07684386569143,9.07684386569143,10.547770533331066,11.030852377887435,11.300413928944284,9.328625426046248,8.703135093227193,11.322938200602813,10.071067811865476,9.791719296345839]]]}}},"view":{"type":"object","name":"CDSView","id":"p19812","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p19813"}}},"glyph":{"type":"object","name":"Line","id":"p19808","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p19809","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p19810","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p19817","attributes":{"data_source":{"id":"p19763"},"view":{"type":"object","name":"CDSView","id":"p19818","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p19819"}}},"glyph":{"type":"object","name":"Scatter","id":"p19814","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p19815","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p19816","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p19774","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p19788"},{"type":"object","name":"BoxZoomTool","id":"p19789","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p19790","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p19796","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p19795","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p19797","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p19798"},{"type":"object","name":"SaveTool","id":"p19799"},{"type":"object","name":"HoverTool","id":"p19820","attributes":{"renderers":[{"id":"p19817"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p19783","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19784","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19785"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19786"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p19778","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19779","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19780"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19781"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p19782","attributes":{"axis":{"id":"p19778"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p19787","attributes":{"dimension":1,"axis":{"id":"p19783"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p19800","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p19802","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p19803","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p19804","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p19806","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p19805","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p19807","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"3c0af1a5-0680-4688-beb6-97dce18bb92e","roots":{"p19766":"ac106c96-6dee-456c-a40a-40b28c8c338e"},"root_ids":["p19766"]}];
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

<div id="e5ae1d80-6b26-4589-bdd2-86601322e12d" data-root-id="p19826" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"db47e9c1-7aa5-4a8f-ba13-a30505b54068":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p19866","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p19867"}}},"roots":[{"type":"object","name":"Figure","id":"p19826","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p19827"},"y_range":{"type":"object","name":"DataRange1d","id":"p19828","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p19835"},"y_scale":{"type":"object","name":"LinearScale","id":"p19836"},"title":{"type":"object","name":"Title","id":"p19833","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p19862","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p19823","attributes":{"selected":{"type":"object","name":"Selection","id":"p19824","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p19825"},"data":{"type":"map","entries":[["year",[2000,2001,2002,2004,2005,2007,2008,2009,2010,2012,2013,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[2,2,1,3,5,19,1,37,6,8,8,3,11,2,2,18,37,56,3,1,58,9,6]],["detected",[2,2,1,3,5,19,1,37,2,8,8,3,11,2,2,18,35,56,3,1,58,9,6]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p19863","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p19864"}}},"glyph":{"type":"object","name":"VBar","id":"p19859","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p19860","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p19861","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p19834","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p19847"},{"type":"object","name":"BoxZoomTool","id":"p19848","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p19849","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p19855","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p19854","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p19856","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p19857"},{"type":"object","name":"SaveTool","id":"p19858"},{"type":"object","name":"HoverTool","id":"p19865","attributes":{"renderers":[{"id":"p19862"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p19842","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19843","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19844"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19845"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p19837","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19838","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19839"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19840"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p19841","attributes":{"axis":{"id":"p19837"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p19846","attributes":{"dimension":1,"axis":{"id":"p19842"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"db47e9c1-7aa5-4a8f-ba13-a30505b54068","roots":{"p19826":"e5ae1d80-6b26-4589-bdd2-86601322e12d"},"root_ids":["p19826"]}];
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

<div id="b7bf0892-e771-4685-b782-f10c03a7dde5" data-root-id="p19871" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"18829348-5db7-4fe5-bab4-4a378c965e62":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p19913","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p19914"}}},"roots":[{"type":"object","name":"Figure","id":"p19871","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p19873"},"y_range":{"type":"object","name":"FactorRange","id":"p19880","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p19881"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p19882"},"title":{"type":"object","name":"Title","id":"p19878","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p19908","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p19868","attributes":{"selected":{"type":"object","name":"Selection","id":"p19869","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p19870"},"data":{"type":"map","entries":[["x",[-7,-11,-19,-20,-16]],["y",["reverse","forward","reverse","forward","reverse"]],["alpha",[0.49228187919463084,1.0,1.0,1.0,1.0]],["pos",[7,11,19,20,16]],["base",["A","G","G","T","T"]],["n",[30,238,238,236,236]],["det_with",["97% of 30","99% of 238","99% of 238","100% of 236","100% of 236"]],["det_without",["99% of 267","97% of 59","97% of 59","93% of 61","93% of 61"]],["subs",["A&gt;G 30","G&gt;A 238","G&gt;T 236, G&gt;A 2","T&gt;C 236","T&gt;G 235, T&gt;A 1"]],["zone",["no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p19909","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p19910"}}},"glyph":{"type":"object","name":"Rect","id":"p19905","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p19906","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p19907","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p19879","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p19893"},{"type":"object","name":"BoxZoomTool","id":"p19894","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p19895","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p19901","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p19900","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p19902","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p19903"},{"type":"object","name":"SaveTool","id":"p19904"},{"type":"object","name":"HoverTool","id":"p19911","attributes":{"renderers":[{"id":"p19908"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p19888","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p19889"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p19890"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19891"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p19883","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p19912","attributes":{"ticks":[-20,-19,-16,-11,-7],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19885"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-7,"7"],[-11,"11"],[-19,"19"],[-20,"20"],[-16,"16"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p19886"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p19887","attributes":{"axis":{"id":"p19883"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p19892","attributes":{"dimension":1,"axis":{"id":"p19888"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"18829348-5db7-4fe5-bab4-4a378c965e62","roots":{"p19871":"b7bf0892-e771-4685-b782-f10c03a7dde5"},"root_ids":["p19871"]}];
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

Disclosures on this entry: `primer_site_polymorphic`, `oligos_from_secondary_source`.


## What reached the statistics

413 records were screened for this assay and **298 (72%)** were evaluable, meaning both primers landed in the right orientation and size range. 115 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 82 |
| `truncated` | 33 |

