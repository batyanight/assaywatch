# NOSEMA_apis_SSU_Martin-Hernandez_2007

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**VAIRIMORPHA (NOSEMA) APIS - SSU rRNA duplex PCR, 321APIS (Martin-Hernandez 2007)**

| | |
|---|---|
| Target | Vairimorpha apis ([taxid 35231](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=35231)) |
| Gene | SSU rRNA |
| Chemistry | conventional |
| Amplicon | 312 bp |
| Designed | 2007 |
| Paper | [10.1128/AEM.00270-07](https://doi.org/10.1128/AEM.00270-07) |
| Registry status | active |

!!! quote "The paper"
    Martín-Hernández R, Meana A, Prieto L, Salvador AM, Garrido-Bailón E, Higes M. 2007. Outcome of Colonization of Apis mellifera by Nosema ceranae. Appl Environ Microbiol 73:6331-6338

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GGGGGCATGTCTTTGACGTACTATGTA` | 27 nt |
| reverse | `GGGGGGCGTTTAAAATGTGAAACAACTATG` | 30 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 4 | 4 | 100.0% | 51.0% – 100.0% |
| baseline (everything earlier) | 19 | 19 | 100.0% | 83.2% – 100.0% |

Change from baseline, Newcombe interval: **-49.0% to 16.8%**. Threshold: **90.0%**.

*4 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (51%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="d401d8a4-09de-463d-8532-880a3fc21a7c" data-root-id="p19205" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"089ba58b-1640-43b6-8642-a77c669e7a04":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p19260","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p19261"}}},"roots":[{"type":"object","name":"Figure","id":"p19205","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p19207"},"y_range":{"type":"object","name":"Range1d","id":"p19214","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p19215"},"y_scale":{"type":"object","name":"LinearScale","id":"p19216"},"title":{"type":"object","name":"Title","id":"p19212","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p19250","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p19202","attributes":{"selected":{"type":"object","name":"Selection","id":"p19203","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p19204"},"data":{"type":"map","entries":[["year",[1994,1995,1998,2005,2012,2014,2016,2019,2021,2022,2024,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[1,1,1,1,9,4,1,1,1,1,1,1]],["evaluable",[1,1,1,1,9,4,1,1,1,1,1,1]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193,10.071067811865476,9.517227179437622,8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193]]]}}},"view":{"type":"object","name":"CDSView","id":"p19251","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p19252"}}},"glyph":{"type":"object","name":"Line","id":"p19247","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p19248","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p19249","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p19256","attributes":{"data_source":{"id":"p19202"},"view":{"type":"object","name":"CDSView","id":"p19257","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p19258"}}},"glyph":{"type":"object","name":"Scatter","id":"p19253","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p19254","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p19255","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p19213","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p19227"},{"type":"object","name":"BoxZoomTool","id":"p19228","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p19229","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p19235","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p19234","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p19236","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p19237"},{"type":"object","name":"SaveTool","id":"p19238"},{"type":"object","name":"HoverTool","id":"p19259","attributes":{"renderers":[{"id":"p19256"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p19222","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19223","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19224"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19225"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p19217","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19218","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19219"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19220"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p19221","attributes":{"axis":{"id":"p19217"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p19226","attributes":{"dimension":1,"axis":{"id":"p19222"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p19239","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2020.5,"right":{"type":"object","name":"Node","id":"p19241","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p19242","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p19243","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p19245","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p19244","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p19246","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"089ba58b-1640-43b6-8642-a77c669e7a04","roots":{"p19205":"d401d8a4-09de-463d-8532-880a3fc21a7c"},"root_ids":["p19205"]}];
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

<div id="e9716d24-47f3-4d1f-9b55-1bd49a5998bc" data-root-id="p19265" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"6131e91e-bee8-42f1-bcc4-4978b8bd0645":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p19305","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p19306"}}},"roots":[{"type":"object","name":"Figure","id":"p19265","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p19266"},"y_range":{"type":"object","name":"DataRange1d","id":"p19267","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p19274"},"y_scale":{"type":"object","name":"LinearScale","id":"p19275"},"title":{"type":"object","name":"Title","id":"p19272","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p19301","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p19262","attributes":{"selected":{"type":"object","name":"Selection","id":"p19263","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p19264"},"data":{"type":"map","entries":[["year",[1994,1995,1998,2005,2012,2014,2016,2019,2021,2022,2024,2026]],["evaluable",[1,1,1,1,9,4,1,1,1,1,1,1]],["detected",[1,1,1,1,9,4,1,1,1,1,1,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p19302","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p19303"}}},"glyph":{"type":"object","name":"VBar","id":"p19298","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p19299","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p19300","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p19273","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p19286"},{"type":"object","name":"BoxZoomTool","id":"p19287","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p19288","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p19294","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p19293","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p19295","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p19296"},{"type":"object","name":"SaveTool","id":"p19297"},{"type":"object","name":"HoverTool","id":"p19304","attributes":{"renderers":[{"id":"p19301"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p19281","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19282","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19283"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19284"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p19276","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p19277","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p19278"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p19279"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p19280","attributes":{"axis":{"id":"p19276"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p19285","attributes":{"dimension":1,"axis":{"id":"p19281"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"6131e91e-bee8-42f1-bcc4-4978b8bd0645","roots":{"p19265":"e9716d24-47f3-4d1f-9b55-1bd49a5998bc"},"root_ids":["p19265"]}];
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
16S[Title] OR 18S[Title] OR "small subunit"[Title] OR SSU[Title] OR rRNA[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `oligos_read_from_figure`.


## What reached the statistics

78 records were screened for this assay and **23 (29%)** were evaluable, meaning both primers landed in the right orientation and size range. 55 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `truncated` | 31 |
| `no_site` | 24 |

