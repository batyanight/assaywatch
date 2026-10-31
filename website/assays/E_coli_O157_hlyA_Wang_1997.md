# E_coli_O157_hlyA_Wang_1997

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**E.coli-O157:H7 -hlyA gene**

| | |
|---|---|
| Target | Escherichia coli ([taxid 562](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=562)) |
| Gene | — |
| Chemistry | conventional |
| Amplicon | 361 bp |
| Designed | 1997 |
| Paper | [10.1046/j.1365-2672.1997.00300.x](https://doi.org/10.1046/j.1365-2672.1997.00300.x) |
| Registry status | active |

!!! quote "The paper"
    Wang RF, Cao WW, Cerniglia CE. 1997. A universal protocol for PCR detection of 13 species of foodborne pathogens in foods. J Appl Microbiol 83:727-736

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GTAGGGAAGCGAACAGAG` | 18 nt |
| reverse | `AAGCTCCGTGTGCCTGAA` | 18 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 2 | 2 | 100.0% | 34.2% – 100.0% |
| baseline (everything earlier) | 96 | 96 | 100.0% | 96.2% – 100.0% |

Change from baseline, Newcombe interval: **-65.8% to 3.8%**. Threshold: **90.0%**.

*2 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (34%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="b51fde10-fc55-4794-9427-614741c5b0fb" data-root-id="p11848" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"636f6071-b9a7-41bd-9de8-abe2ecca3e19":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p11903","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p11904"}}},"roots":[{"type":"object","name":"Figure","id":"p11848","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p11850"},"y_range":{"type":"object","name":"Range1d","id":"p11857","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p11858"},"y_scale":{"type":"object","name":"LinearScale","id":"p11859"},"title":{"type":"object","name":"Title","id":"p11855","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p11893","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p11845","attributes":{"selected":{"type":"object","name":"Selection","id":"p11846","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p11847"},"data":{"type":"map","entries":[["year",[1994,1995,1998,2004,2006,2007,2008,2009,2012,2014,2015,2016,2017,2018,2019,2020,2021,2025]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[2,1,1,2,2,11,1,6,1,13,3,2,1,39,6,2,3,2]],["evaluable",[2,1,1,2,2,11,1,6,1,13,3,2,1,39,6,2,3,2]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent"]],["size",[9.07684386569143,8.703135093227193,8.703135093227193,9.07684386569143,9.07684386569143,10.209683151927734,8.703135093227193,9.791719296345839,8.703135093227193,10.324834530005162,9.328625426046248,9.07684386569143,8.703135093227193,11.06545099688784,9.791719296345839,9.07684386569143,9.328625426046248,9.07684386569143]]]}}},"view":{"type":"object","name":"CDSView","id":"p11894","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p11895"}}},"glyph":{"type":"object","name":"Line","id":"p11890","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p11891","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p11892","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p11899","attributes":{"data_source":{"id":"p11845"},"view":{"type":"object","name":"CDSView","id":"p11900","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p11901"}}},"glyph":{"type":"object","name":"Scatter","id":"p11896","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p11897","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p11898","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p11856","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p11870"},{"type":"object","name":"BoxZoomTool","id":"p11871","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p11872","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p11878","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p11877","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p11879","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p11880"},{"type":"object","name":"SaveTool","id":"p11881"},{"type":"object","name":"HoverTool","id":"p11902","attributes":{"renderers":[{"id":"p11899"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p11865","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p11866","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p11867"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11868"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p11860","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p11861","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p11862"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11863"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p11864","attributes":{"axis":{"id":"p11860"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p11869","attributes":{"dimension":1,"axis":{"id":"p11865"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p11882","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2020.5,"right":{"type":"object","name":"Node","id":"p11884","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p11885","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p11886","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p11888","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p11887","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p11889","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"636f6071-b9a7-41bd-9de8-abe2ecca3e19","roots":{"p11848":"b51fde10-fc55-4794-9427-614741c5b0fb"},"root_ids":["p11848"]}];
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

<div id="ed07fb60-cf9d-481b-874e-4614e315090e" data-root-id="p11908" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"151990b9-683c-42d9-9518-2c2322cf5d8b":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p11948","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p11949"}}},"roots":[{"type":"object","name":"Figure","id":"p11908","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p11909"},"y_range":{"type":"object","name":"DataRange1d","id":"p11910","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p11917"},"y_scale":{"type":"object","name":"LinearScale","id":"p11918"},"title":{"type":"object","name":"Title","id":"p11915","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p11944","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p11905","attributes":{"selected":{"type":"object","name":"Selection","id":"p11906","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p11907"},"data":{"type":"map","entries":[["year",[1994,1995,1998,2004,2006,2007,2008,2009,2012,2014,2015,2016,2017,2018,2019,2020,2021,2025]],["evaluable",[2,1,1,2,2,11,1,6,1,13,3,2,1,39,6,2,3,2]],["detected",[2,1,1,2,2,11,1,6,1,13,3,2,1,39,6,2,3,2]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p11945","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p11946"}}},"glyph":{"type":"object","name":"VBar","id":"p11941","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p11942","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p11943","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p11916","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p11929"},{"type":"object","name":"BoxZoomTool","id":"p11930","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p11931","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p11937","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p11936","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p11938","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p11939"},{"type":"object","name":"SaveTool","id":"p11940"},{"type":"object","name":"HoverTool","id":"p11947","attributes":{"renderers":[{"id":"p11944"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p11924","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p11925","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p11926"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11927"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p11919","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p11920","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p11921"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11922"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p11923","attributes":{"axis":{"id":"p11919"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p11928","attributes":{"dimension":1,"axis":{"id":"p11924"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"151990b9-683c-42d9-9518-2c2322cf5d8b","roots":{"p11908":"ed07fb60-cf9d-481b-874e-4614e315090e"},"root_ids":["p11908"]}];
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

<div id="d19d8d39-10df-4840-93cc-b1a020787e62" data-root-id="p11953" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"1d796cb6-a8ee-4086-a7b6-c5b0ff328e06":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p11995","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p11996"}}},"roots":[{"type":"object","name":"Figure","id":"p11953","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p11955"},"y_range":{"type":"object","name":"FactorRange","id":"p11962","attributes":{"factors":["forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p11963"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p11964"},"title":{"type":"object","name":"Title","id":"p11960","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p11990","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p11950","attributes":{"selected":{"type":"object","name":"Selection","id":"p11951","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p11952"},"data":{"type":"map","entries":[["x",[-9]],["y",["forward"]],["alpha",[0.9132653061224489]],["pos",[9]],["base",["C"]],["n",[22]],["det_with",["100% of 22"]],["det_without",["100% of 76"]],["subs",["C&gt;A 22"]],["zone",["no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p11991","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p11992"}}},"glyph":{"type":"object","name":"Rect","id":"p11987","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p11988","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p11989","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p11961","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p11975"},{"type":"object","name":"BoxZoomTool","id":"p11976","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p11977","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p11983","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p11982","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p11984","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p11985"},{"type":"object","name":"SaveTool","id":"p11986"},{"type":"object","name":"HoverTool","id":"p11993","attributes":{"renderers":[{"id":"p11990"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p11970","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p11971"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p11972"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11973"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p11965","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p11994","attributes":{"ticks":[-9],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p11967"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-9,"9"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p11968"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p11969","attributes":{"axis":{"id":"p11965"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p11974","attributes":{"dimension":1,"axis":{"id":"p11970"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"1d796cb6-a8ee-4086-a7b6-c5b0ff328e06","roots":{"p11953":"d19d8d39-10df-4840-93cc-b1a020787e62"},"root_ids":["p11953"]}];
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
(hlyA[Gene] OR ehxA[Gene] OR "EHEC hemolysin"[Title] OR "enterohemolysin"[Title] OR "hlyA"[Title]) AND 1:30000[SLEN] NOT "whole genome shotgun"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `orientation_inferred`.


## What reached the statistics

486 records were screened for this assay and **98 (20%)** were evaluable, meaning both primers landed in the right orientation and size range. 388 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 377 |
| `chance_only` | 11 |

