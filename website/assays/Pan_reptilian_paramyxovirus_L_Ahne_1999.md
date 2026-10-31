# Pan_reptilian_paramyxovirus_L_Ahne_1999

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**Pan-reptilian paramyxovirus — RdRp (L gene)**

| | |
|---|---|
| Target | Ferlavirus ([taxid 1283308](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1283308)) |
| Gene | RdRp (L gene) |
| Chemistry | conventional |
| Amplicon | 627 bp |
| Designed | 1999 |
| Paper | [10.1016/S0168-1702(99)00059-3](https://doi.org/10.1016/S0168-1702(99)00059-3) |
| Registry status | active |

!!! quote "The paper"
    Ahne W et al. 1999. Virus Res 63:65-74

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GCAGAGATTTTCTCTTTCTT` | 20 nt |
| reverse | `AGCTCTCATTTTGTATGTCAT` | 21 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 3 | 6 | 50.0% | 18.8% – 81.2% |
| baseline (everything earlier) | 7 | 14 | 50.0% | 26.8% – 73.2% |

Change from baseline, Newcombe interval: **-38.9% to 38.9%**. Threshold: **90.0%**.

*6 evaluable records since Oct 2021, below the minimum of 15; the detected share is 50% (19%-81%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record rising (p=0.974, 7 years); by footprint falling (p=0.974); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="a9a0c822-aa9b-43e3-9b87-cfe9d606ebea" data-root-id="p28442" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b8b31ed1-fe6b-4130-b032-a718493b1aa6":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p28497","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p28498"}}},"roots":[{"type":"object","name":"Figure","id":"p28442","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p28444"},"y_range":{"type":"object","name":"Range1d","id":"p28451","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p28452"},"y_scale":{"type":"object","name":"LinearScale","id":"p28453"},"title":{"type":"object","name":"Title","id":"p28449","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p28487","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p28439","attributes":{"selected":{"type":"object","name":"Selection","id":"p28440","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p28441"},"data":{"type":"map","entries":[["year",[2003,2014,2017,2018,2021,2025,2026]],["share",[100.0,0.0,0.0,50.0,100.0,100.0,25.0]],["detected",[2,0,0,1,4,2,1]],["evaluable",[2,5,1,2,4,2,4]],["window",["baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,9.667366891029102,8.703135093227193,9.07684386569143,9.517227179437622,9.07684386569143,9.517227179437622]]]}}},"view":{"type":"object","name":"CDSView","id":"p28488","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p28489"}}},"glyph":{"type":"object","name":"Line","id":"p28484","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p28485","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p28486","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p28493","attributes":{"data_source":{"id":"p28439"},"view":{"type":"object","name":"CDSView","id":"p28494","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p28495"}}},"glyph":{"type":"object","name":"Scatter","id":"p28490","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p28491","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p28492","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p28450","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p28464"},{"type":"object","name":"BoxZoomTool","id":"p28465","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p28466","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p28472","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p28471","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p28473","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p28474"},{"type":"object","name":"SaveTool","id":"p28475"},{"type":"object","name":"HoverTool","id":"p28496","attributes":{"renderers":[{"id":"p28493"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p28459","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p28460","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28461"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28462"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p28454","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p28455","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28456"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28457"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p28458","attributes":{"axis":{"id":"p28454"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p28463","attributes":{"dimension":1,"axis":{"id":"p28459"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p28476","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2020.5,"right":{"type":"object","name":"Node","id":"p28478","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p28479","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p28480","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p28482","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p28481","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p28483","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b8b31ed1-fe6b-4130-b032-a718493b1aa6","roots":{"p28442":"a9a0c822-aa9b-43e3-9b87-cfe9d606ebea"},"root_ids":["p28442"]}];
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

<div id="e93d95e9-6660-4e66-9b8f-0edd9aa1e564" data-root-id="p28502" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"0ad712c9-0aeb-4b19-a81c-dd14b813f17b":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p28542","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p28543"}}},"roots":[{"type":"object","name":"Figure","id":"p28502","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p28503"},"y_range":{"type":"object","name":"DataRange1d","id":"p28504","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p28511"},"y_scale":{"type":"object","name":"LinearScale","id":"p28512"},"title":{"type":"object","name":"Title","id":"p28509","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p28538","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p28499","attributes":{"selected":{"type":"object","name":"Selection","id":"p28500","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p28501"},"data":{"type":"map","entries":[["year",[2003,2014,2017,2018,2021,2025,2026]],["evaluable",[2,5,1,2,4,2,4]],["detected",[2,0,0,1,4,2,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p28539","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p28540"}}},"glyph":{"type":"object","name":"VBar","id":"p28535","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p28536","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p28537","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p28510","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p28523"},{"type":"object","name":"BoxZoomTool","id":"p28524","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p28525","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p28531","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p28530","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p28532","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p28533"},{"type":"object","name":"SaveTool","id":"p28534"},{"type":"object","name":"HoverTool","id":"p28541","attributes":{"renderers":[{"id":"p28538"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p28518","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p28519","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28520"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28521"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p28513","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p28514","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28515"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28516"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p28517","attributes":{"axis":{"id":"p28513"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p28522","attributes":{"dimension":1,"axis":{"id":"p28518"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"0ad712c9-0aeb-4b19-a81c-dd14b813f17b","roots":{"p28502":"e93d95e9-6660-4e66-9b8f-0edd9aa1e564"},"root_ids":["p28502"]}];
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

<div id="caef127c-b6c7-45ce-9418-d0b08994d7bf" data-root-id="p28547" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"2b3a2a2b-319a-4bb7-9557-e9ec127dcbde":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p28589","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p28590"}}},"roots":[{"type":"object","name":"Figure","id":"p28547","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p28549"},"y_range":{"type":"object","name":"FactorRange","id":"p28556","attributes":{"factors":["forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p28557"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p28558"},"title":{"type":"object","name":"Title","id":"p28554","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p28584","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p28544","attributes":{"selected":{"type":"object","name":"Selection","id":"p28545","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p28546"},"data":{"type":"map","entries":[["x",[-20]],["y",["forward"]],["alpha",[1.0]],["pos",[20]],["base",["G"]],["n",[20]],["det_with",["50% of 20"]],["det_without",["0% of 0"]],["subs",["G&gt;T 20"]],["zone",["no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p28585","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p28586"}}},"glyph":{"type":"object","name":"Rect","id":"p28581","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p28582","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p28583","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p28555","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p28569"},{"type":"object","name":"BoxZoomTool","id":"p28570","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p28571","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p28577","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p28576","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p28578","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p28579"},{"type":"object","name":"SaveTool","id":"p28580"},{"type":"object","name":"HoverTool","id":"p28587","attributes":{"renderers":[{"id":"p28584"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p28564","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p28565"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p28566"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28567"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p28559","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p28588","attributes":{"ticks":[-20],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28561"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-20,"20"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p28562"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p28563","attributes":{"axis":{"id":"p28559"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p28568","attributes":{"dimension":1,"axis":{"id":"p28564"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"2b3a2a2b-319a-4bb7-9557-e9ec127dcbde","roots":{"p28547":"caef127c-b6c7-45ce-9418-d0b08994d7bf"},"root_ids":["p28547"]}];
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

Disclosures on this entry: `orientation_inferred`.


## What reached the statistics

61 records were screened for this assay and **20 (33%)** were evaluable, meaning both primers landed in the right orientation and size range. 41 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 32 |
| `truncated` | 8 |
| `chance_anchor` | 1 |

