# E_coli_ETEC_LT_Victor_1991

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**E. coli-ETEC-enterotoxin (LT)gene**

| | |
|---|---|
| Target | Escherichia coli ([taxid 562](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=562)) |
| Gene | — |
| Chemistry | conventional |
| Amplicon | 117 bp |
| Designed | 1991 |
| Paper | [10.1128/jcm.29.1.158-161.1991](https://doi.org/10.1128/jcm.29.1.158-161.1991) |
| Registry status | active |

!!! quote "The paper"
    Victor T, du Toit R, van Zyl J, Bester AJ, van Helden PD. 1991. Improved method for the routine identification of toxigenic Escherichia coli by DNA amplification of a conserved region of the heat-labile toxin A subunit. J Clin Microbiol 29:158-161

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GAGACCGGTATTACAGAAATC` | 21 nt |
| reverse | `GAGGTGCATGATGAATCCAG` | 20 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 1 | 1 | 100.0% | 20.7% – 100.0% |
| baseline (everything earlier) | 26 | 27 | 96.3% | 81.7% – 99.3% |

Change from baseline, Newcombe interval: **-75.7% to 18.3%**. Threshold: **90.0%**.

*1 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (21%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record rising (p=0.312, 11 years); by footprint rising (p=0.0817). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="af268be5-c565-4721-b40d-02d443a91508" data-root-id="p11696" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"f02f1fc4-7756-4144-afc4-dbf23207bace":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p11751","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p11752"}}},"roots":[{"type":"object","name":"Figure","id":"p11696","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p11698"},"y_range":{"type":"object","name":"Range1d","id":"p11705","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p11706"},"y_scale":{"type":"object","name":"LinearScale","id":"p11707"},"title":{"type":"object","name":"Title","id":"p11703","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p11741","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p11693","attributes":{"selected":{"type":"object","name":"Selection","id":"p11694","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p11695"},"data":{"type":"map","entries":[["year",[2006,2007,2010,2011,2012,2014,2015,2016,2017,2018,2021]],["share",[0.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[0,15,1,1,1,4,1,1,1,1,1]],["evaluable",[1,15,1,1,1,4,1,1,1,1,1]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent"]],["size",[8.703135093227193,10.423139468338052,8.703135093227193,8.703135093227193,8.703135093227193,9.517227179437622,8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193]]]}}},"view":{"type":"object","name":"CDSView","id":"p11742","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p11743"}}},"glyph":{"type":"object","name":"Line","id":"p11738","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p11739","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p11740","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p11747","attributes":{"data_source":{"id":"p11693"},"view":{"type":"object","name":"CDSView","id":"p11748","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p11749"}}},"glyph":{"type":"object","name":"Scatter","id":"p11744","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p11745","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p11746","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p11704","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p11718"},{"type":"object","name":"BoxZoomTool","id":"p11719","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p11720","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p11726","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p11725","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p11727","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p11728"},{"type":"object","name":"SaveTool","id":"p11729"},{"type":"object","name":"HoverTool","id":"p11750","attributes":{"renderers":[{"id":"p11747"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p11713","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p11714","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p11715"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11716"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p11708","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p11709","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p11710"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11711"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p11712","attributes":{"axis":{"id":"p11708"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p11717","attributes":{"dimension":1,"axis":{"id":"p11713"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p11730","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2020.5,"right":{"type":"object","name":"Node","id":"p11732","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p11733","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p11734","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p11736","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p11735","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p11737","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"f02f1fc4-7756-4144-afc4-dbf23207bace","roots":{"p11696":"af268be5-c565-4721-b40d-02d443a91508"},"root_ids":["p11696"]}];
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

<div id="b0772ffb-2766-4898-9502-0271867757f6" data-root-id="p11756" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"941418b3-e2f3-4405-82a0-250ab89d92be":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p11796","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p11797"}}},"roots":[{"type":"object","name":"Figure","id":"p11756","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p11757"},"y_range":{"type":"object","name":"DataRange1d","id":"p11758","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p11765"},"y_scale":{"type":"object","name":"LinearScale","id":"p11766"},"title":{"type":"object","name":"Title","id":"p11763","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p11792","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p11753","attributes":{"selected":{"type":"object","name":"Selection","id":"p11754","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p11755"},"data":{"type":"map","entries":[["year",[2006,2007,2010,2011,2012,2014,2015,2016,2017,2018,2021]],["evaluable",[1,15,1,1,1,4,1,1,1,1,1]],["detected",[0,15,1,1,1,4,1,1,1,1,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p11793","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p11794"}}},"glyph":{"type":"object","name":"VBar","id":"p11789","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p11790","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p11791","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p11764","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p11777"},{"type":"object","name":"BoxZoomTool","id":"p11778","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p11779","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p11785","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p11784","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p11786","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p11787"},{"type":"object","name":"SaveTool","id":"p11788"},{"type":"object","name":"HoverTool","id":"p11795","attributes":{"renderers":[{"id":"p11792"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p11772","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p11773","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p11774"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11775"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p11767","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p11768","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p11769"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11770"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p11771","attributes":{"axis":{"id":"p11767"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p11776","attributes":{"dimension":1,"axis":{"id":"p11772"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"941418b3-e2f3-4405-82a0-250ab89d92be","roots":{"p11756":"b0772ffb-2766-4898-9502-0271867757f6"},"root_ids":["p11756"]}];
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

<div id="b4bc0458-e90f-486e-a1cf-0eaec8c8776f" data-root-id="p11801" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"e9880a6f-7d1a-4e8d-8623-ef7242570612":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p11843","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p11844"}}},"roots":[{"type":"object","name":"Figure","id":"p11801","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p11803"},"y_range":{"type":"object","name":"FactorRange","id":"p11810","attributes":{"factors":["reverse"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p11811"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p11812"},"title":{"type":"object","name":"Title","id":"p11808","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p11838","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p11798","attributes":{"selected":{"type":"object","name":"Selection","id":"p11799","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p11800"},"data":{"type":"map","entries":[["x",[-19]],["y",["reverse"]],["alpha",[1.0]],["pos",[19]],["base",["A"]],["n",[28]],["det_with",["96% of 28"]],["det_without",["0% of 0"]],["subs",["A&gt;T 28"]],["zone",["no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p11839","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p11840"}}},"glyph":{"type":"object","name":"Rect","id":"p11835","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p11836","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p11837","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p11809","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p11823"},{"type":"object","name":"BoxZoomTool","id":"p11824","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p11825","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p11831","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p11830","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p11832","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p11833"},{"type":"object","name":"SaveTool","id":"p11834"},{"type":"object","name":"HoverTool","id":"p11841","attributes":{"renderers":[{"id":"p11838"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p11818","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p11819"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p11820"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p11821"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p11813","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p11842","attributes":{"ticks":[-19],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p11815"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-19,"19"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p11816"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p11817","attributes":{"axis":{"id":"p11813"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p11822","attributes":{"dimension":1,"axis":{"id":"p11818"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"e9880a6f-7d1a-4e8d-8623-ef7242570612","roots":{"p11801":"b4bc0458-e90f-486e-a1cf-0eaec8c8776f"},"root_ids":["p11801"]}];
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
(eltA[Gene] OR eltB[Gene] OR elt[Gene] OR "heat-labile enterotoxin"[Title] OR "LT toxin"[Title]) AND 1:30000[SLEN] NOT "whole genome shotgun"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `oligos_from_secondary_source`, `citation_is_indirect`, `orientation_inferred`.


## What reached the statistics

386 records were screened for this assay and **28 (7%)** were evaluable, meaning both primers landed in the right orientation and size range. 358 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 353 |
| `chance_anchor` | 3 |
| `truncated` | 2 |

