# TRICHOMONAS_gallinae_18S_Renteria_Solis_2020

<span class="aw-chip aw-chip-stable">stable</span>

**TRICHOMONAS GALLINAE — 18S rRNA SYBR Green qPCR (Rentería-Solís 2020)**

| | |
|---|---|
| Target | Trichomonas gallinae ([taxid 56777](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=56777)) |
| Gene | 18S rRNA |
| Chemistry | sybr |
| Amplicon | 113 bp |
| Designed | 2020 |
| Paper | [10.1007/s00436-020-06887-x](https://doi.org/10.1007/s00436-020-06887-x) |
| Registry status | active |

!!! quote "The paper"
    Rentería-Solís Z, Nguyen-Ho-Bao T, Taha S, Daugschies A. A SYBR green I real-time polymerase chain reaction (PCR) assay for detection and quantification of Trichomonas gallinae.

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GGTGGAGCCTGTGGCTTAAT` | 20 nt |
| reverse | `CCATGCACCACCAAAAGCAA` | 20 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (48 months, from Oct 2022) | 21 | 21 | 100.0% | 84.5% – 100.0% |
| baseline (everything earlier) | 46 | 46 | 100.0% | 92.3% – 100.0% |

Change from baseline, Newcombe interval: **-15.5% to 7.7%**. Threshold: **90.0%**.

*detected share 100.0% (85%-100%) since Oct 2022 (window widened to 48 months to reach 15 evaluable records)*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="dd10c5d8-019e-4195-a1b3-4bc191be2a18" data-root-id="p33614" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"e4a5216e-8fa6-4108-ad64-5da0c74e9941":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p33669","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p33670"}}},"roots":[{"type":"object","name":"Figure","id":"p33614","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p33616"},"y_range":{"type":"object","name":"Range1d","id":"p33623","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p33624"},"y_scale":{"type":"object","name":"LinearScale","id":"p33625"},"title":{"type":"object","name":"Title","id":"p33621","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p33659","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p33611","attributes":{"selected":{"type":"object","name":"Selection","id":"p33612","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p33613"},"data":{"type":"map","entries":[["year",[2008,2010,2013,2014,2015,2016,2017,2019,2022,2023,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[4,5,1,7,1,15,2,9,2,12,7,2]],["evaluable",[4,5,1,7,1,15,2,9,2,12,7,2]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent"]],["size",[9.517227179437622,9.667366891029102,8.703135093227193,9.897626379762722,8.703135093227193,10.423139468338052,9.07684386569143,10.071067811865476,9.07684386569143,10.269703144398052,9.897626379762722,9.07684386569143]]]}}},"view":{"type":"object","name":"CDSView","id":"p33660","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33661"}}},"glyph":{"type":"object","name":"Line","id":"p33656","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p33657","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p33658","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p33665","attributes":{"data_source":{"id":"p33611"},"view":{"type":"object","name":"CDSView","id":"p33666","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33667"}}},"glyph":{"type":"object","name":"Scatter","id":"p33662","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p33663","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p33664","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p33622","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p33636"},{"type":"object","name":"BoxZoomTool","id":"p33637","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p33638","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p33644","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33643","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p33645","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p33646"},{"type":"object","name":"SaveTool","id":"p33647"},{"type":"object","name":"HoverTool","id":"p33668","attributes":{"renderers":[{"id":"p33665"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p33631","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33632","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33633"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33634"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p33626","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33627","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33628"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33629"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p33630","attributes":{"axis":{"id":"p33626"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p33635","attributes":{"dimension":1,"axis":{"id":"p33631"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p33648","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2021.5,"right":{"type":"object","name":"Node","id":"p33650","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p33651","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p33652","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p33654","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33653","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p33655","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"e4a5216e-8fa6-4108-ad64-5da0c74e9941","roots":{"p33614":"dd10c5d8-019e-4195-a1b3-4bc191be2a18"},"root_ids":["p33614"]}];
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

<div id="b765c917-a3ed-455e-bb63-1cdc4785f9dd" data-root-id="p33674" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"776ff751-ceb2-4f32-a0bb-63d1977e0a74":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p33714","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p33715"}}},"roots":[{"type":"object","name":"Figure","id":"p33674","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p33675"},"y_range":{"type":"object","name":"DataRange1d","id":"p33676","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p33683"},"y_scale":{"type":"object","name":"LinearScale","id":"p33684"},"title":{"type":"object","name":"Title","id":"p33681","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p33710","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p33671","attributes":{"selected":{"type":"object","name":"Selection","id":"p33672","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p33673"},"data":{"type":"map","entries":[["year",[2008,2010,2013,2014,2015,2016,2017,2019,2022,2023,2025,2026]],["evaluable",[4,5,1,7,1,15,2,9,2,12,7,2]],["detected",[4,5,1,7,1,15,2,9,2,12,7,2]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p33711","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33712"}}},"glyph":{"type":"object","name":"VBar","id":"p33707","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p33708","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p33709","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p33682","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p33695"},{"type":"object","name":"BoxZoomTool","id":"p33696","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p33697","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p33703","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33702","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p33704","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p33705"},{"type":"object","name":"SaveTool","id":"p33706"},{"type":"object","name":"HoverTool","id":"p33713","attributes":{"renderers":[{"id":"p33710"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p33690","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33691","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33692"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33693"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p33685","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33686","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33687"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33688"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p33689","attributes":{"axis":{"id":"p33685"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p33694","attributes":{"dimension":1,"axis":{"id":"p33690"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"776ff751-ceb2-4f32-a0bb-63d1977e0a74","roots":{"p33674":"b765c917-a3ed-455e-bb63-1cdc4785f9dd"},"root_ids":["p33674"]}];
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


## Scope — what this assay is judged against

This entry declares no `scope_taxids`, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower set than its taxid covers, that reads as low coverage rather than as drift — see [scoping](../scoping.md).

Retrieval query:

```
18S[Title] OR "small subunit ribosomal"[Title] OR SSU[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).


## What reached the statistics

345 records were screened for this assay and **67 (19%)** were evaluable, meaning both primers landed in the right orientation and size range. 278 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `chance_anchor` | 241 |
| `no_site` | 37 |

