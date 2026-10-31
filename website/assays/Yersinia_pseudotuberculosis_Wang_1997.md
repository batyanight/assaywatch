# Yersinia_pseudotuberculosis_Wang_1997

<span class="aw-chip aw-chip-stable">stable</span>

**Yersinia pseudotuberculosis, inv gene**

| | |
|---|---|
| Target | Yersinia pseudotuberculosis ([taxid 633](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=633)) |
| Gene | — |
| Chemistry | conventional |
| Amplicon | 440 bp |
| Designed | 1997 |
| Paper | [10.1046/j.1365-2672.1997.00300.x](https://doi.org/10.1046/j.1365-2672.1997.00300.x) |
| Registry status | active |

!!! quote "The paper"
    Wang RF, Cao WW, Cerniglia CE. 1997. A universal protocol for PCR detection of 13 species of foodborne pathogens in foods. J Appl Microbiol 83:727-736

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CTTGGCTGATGGCACGAT` | 18 nt |
| reverse | `TCGTCACCTGACCCTGAT` | 18 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (48 months, from Oct 2022) | 16 | 16 | 100.0% | 80.6% – 100.0% |
| baseline (everything earlier) | 49 | 49 | 100.0% | 92.7% – 100.0% |

Change from baseline, Newcombe interval: **-19.4% to 7.3%**. Threshold: **90.0%**.

*detected share 100.0% (81%-100%) since Oct 2022 (window widened to 48 months to reach 15 evaluable records)*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="bed714f9-03dc-45a0-8b10-a1f33fbd73a5" data-root-id="p34743" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b5d25d5a-9180-4fb5-b839-785111bb6727":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p34798","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p34799"}}},"roots":[{"type":"object","name":"Figure","id":"p34743","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p34745"},"y_range":{"type":"object","name":"Range1d","id":"p34752","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p34753"},"y_scale":{"type":"object","name":"LinearScale","id":"p34754"},"title":{"type":"object","name":"Title","id":"p34750","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p34788","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p34740","attributes":{"selected":{"type":"object","name":"Selection","id":"p34741","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p34742"},"data":{"type":"map","entries":[["year",[1989,2006,2007,2012,2013,2014,2015,2017,2018,2019,2021,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[1,1,1,18,1,1,9,1,12,1,3,3,7,5,1]],["evaluable",[1,1,1,18,1,1,9,1,12,1,3,3,7,5,1]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,8.703135093227193,10.547770533331066,8.703135093227193,8.703135093227193,10.071067811865476,8.703135093227193,10.269703144398052,8.703135093227193,9.328625426046248,9.328625426046248,9.897626379762722,9.667366891029102,8.703135093227193]]]}}},"view":{"type":"object","name":"CDSView","id":"p34789","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p34790"}}},"glyph":{"type":"object","name":"Line","id":"p34785","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p34786","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p34787","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p34794","attributes":{"data_source":{"id":"p34740"},"view":{"type":"object","name":"CDSView","id":"p34795","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p34796"}}},"glyph":{"type":"object","name":"Scatter","id":"p34791","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p34792","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p34793","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p34751","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p34765"},{"type":"object","name":"BoxZoomTool","id":"p34766","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p34767","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p34773","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p34772","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p34774","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p34775"},{"type":"object","name":"SaveTool","id":"p34776"},{"type":"object","name":"HoverTool","id":"p34797","attributes":{"renderers":[{"id":"p34794"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p34760","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34761","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34762"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34763"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p34755","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34756","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34757"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34758"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p34759","attributes":{"axis":{"id":"p34755"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p34764","attributes":{"dimension":1,"axis":{"id":"p34760"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p34777","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2022.5,"right":{"type":"object","name":"Node","id":"p34779","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p34780","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p34781","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p34783","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p34782","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p34784","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b5d25d5a-9180-4fb5-b839-785111bb6727","roots":{"p34743":"bed714f9-03dc-45a0-8b10-a1f33fbd73a5"},"root_ids":["p34743"]}];
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

<div id="c5e8ecba-49a9-46c5-8bd7-85d0e16f9d7b" data-root-id="p34803" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"a6ae6dd1-cca5-4052-bcfe-1092b6f212dc":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p34843","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p34844"}}},"roots":[{"type":"object","name":"Figure","id":"p34803","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p34804"},"y_range":{"type":"object","name":"DataRange1d","id":"p34805","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p34812"},"y_scale":{"type":"object","name":"LinearScale","id":"p34813"},"title":{"type":"object","name":"Title","id":"p34810","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p34839","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p34800","attributes":{"selected":{"type":"object","name":"Selection","id":"p34801","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p34802"},"data":{"type":"map","entries":[["year",[1989,2006,2007,2012,2013,2014,2015,2017,2018,2019,2021,2023,2024,2025,2026]],["evaluable",[1,1,1,18,1,1,9,1,12,1,3,3,7,5,1]],["detected",[1,1,1,18,1,1,9,1,12,1,3,3,7,5,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p34840","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p34841"}}},"glyph":{"type":"object","name":"VBar","id":"p34836","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p34837","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p34838","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p34811","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p34824"},{"type":"object","name":"BoxZoomTool","id":"p34825","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p34826","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p34832","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p34831","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p34833","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p34834"},{"type":"object","name":"SaveTool","id":"p34835"},{"type":"object","name":"HoverTool","id":"p34842","attributes":{"renderers":[{"id":"p34839"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p34819","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34820","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34821"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34822"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p34814","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34815","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34816"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34817"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p34818","attributes":{"axis":{"id":"p34814"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p34823","attributes":{"dimension":1,"axis":{"id":"p34819"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"a6ae6dd1-cca5-4052-bcfe-1092b6f212dc","roots":{"p34803":"c5e8ecba-49a9-46c5-8bd7-85d0e16f9d7b"},"root_ids":["p34803"]}];
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
(inv[Gene] OR invasin[Title]) AND 1:30000[SLEN] NOT "whole genome shotgun"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `orientation_inferred`.


## What reached the statistics

66 records were screened for this assay and **65 (98%)** were evaluable, meaning both primers landed in the right orientation and size range. 1 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 1 |

