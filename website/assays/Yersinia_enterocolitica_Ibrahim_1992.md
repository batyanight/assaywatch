# Yersinia_enterocolitica_Ibrahim_1992

<span class="aw-chip aw-chip-stable">stable</span>

**Yersinia enterocolitica, enterotoxin gene**

| | |
|---|---|
| Target | Yersinia enterocolitica ([taxid 630](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=630)) |
| Gene | — |
| Chemistry | conventional |
| Amplicon | 159 bp |
| Designed | 1992 |
| Paper | [10.1128/jcm.30.8.1942-1947.1992](https://doi.org/10.1128/jcm.30.8.1942-1947.1992) |
| Registry status | active |

!!! quote "The paper"
    Ibrahim A, Liesack W, Stackebrandt E. 1992. J Clin Microbiol 30:1942-1947

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CTGTCTTCATTTGGAGCATTC` | 21 nt |
| reverse | `GCAACATACATCACAGCAATC` | 21 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (36 months, from Oct 2023) | 15 | 15 | 100.0% | 79.6% – 100.0% |
| baseline (everything earlier) | 22 | 22 | 100.0% | 85.1% – 100.0% |

Change from baseline, Newcombe interval: **-20.4% to 14.9%**. Threshold: **90.0%**.

*detected share 100.0% (80%-100%) since Oct 2023 (window widened to 36 months to reach 15 evaluable records)*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="ad724d0c-a7f3-4f1f-9d40-8f80b47af71d" data-root-id="p34638" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"155b4338-357f-4f67-8562-11ff6c78d508":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p34693","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p34694"}}},"roots":[{"type":"object","name":"Figure","id":"p34638","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p34640"},"y_range":{"type":"object","name":"Range1d","id":"p34647","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p34648"},"y_scale":{"type":"object","name":"LinearScale","id":"p34649"},"title":{"type":"object","name":"Title","id":"p34645","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p34683","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p34635","attributes":{"selected":{"type":"object","name":"Selection","id":"p34636","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p34637"},"data":{"type":"map","entries":[["year",[1992,1994,2007,2011,2015,2016,2018,2019,2021,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[1,1,1,2,4,6,2,3,2,2,5,8]],["evaluable",[1,1,1,2,4,6,2,3,2,2,5,8]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,8.703135093227193,9.07684386569143,9.517227179437622,9.791719296345839,9.07684386569143,9.328625426046248,9.07684386569143,9.07684386569143,9.667366891029102,9.989711205477885]]]}}},"view":{"type":"object","name":"CDSView","id":"p34684","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p34685"}}},"glyph":{"type":"object","name":"Line","id":"p34680","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p34681","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p34682","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p34689","attributes":{"data_source":{"id":"p34635"},"view":{"type":"object","name":"CDSView","id":"p34690","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p34691"}}},"glyph":{"type":"object","name":"Scatter","id":"p34686","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p34687","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p34688","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p34646","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p34660"},{"type":"object","name":"BoxZoomTool","id":"p34661","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p34662","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p34668","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p34667","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p34669","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p34670"},{"type":"object","name":"SaveTool","id":"p34671"},{"type":"object","name":"HoverTool","id":"p34692","attributes":{"renderers":[{"id":"p34689"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p34655","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34656","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34657"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34658"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p34650","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34651","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34652"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34653"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p34654","attributes":{"axis":{"id":"p34650"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p34659","attributes":{"dimension":1,"axis":{"id":"p34655"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p34672","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p34674","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p34675","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p34676","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p34678","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p34677","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p34679","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"155b4338-357f-4f67-8562-11ff6c78d508","roots":{"p34638":"ad724d0c-a7f3-4f1f-9d40-8f80b47af71d"},"root_ids":["p34638"]}];
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

<div id="dd0f2ac3-9326-463c-9b41-b82a331b87c2" data-root-id="p34698" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"69156d04-ccf0-441b-892e-a9894d5be0cf":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p34738","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p34739"}}},"roots":[{"type":"object","name":"Figure","id":"p34698","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p34699"},"y_range":{"type":"object","name":"DataRange1d","id":"p34700","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p34707"},"y_scale":{"type":"object","name":"LinearScale","id":"p34708"},"title":{"type":"object","name":"Title","id":"p34705","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p34734","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p34695","attributes":{"selected":{"type":"object","name":"Selection","id":"p34696","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p34697"},"data":{"type":"map","entries":[["year",[1992,1994,2007,2011,2015,2016,2018,2019,2021,2024,2025,2026]],["evaluable",[1,1,1,2,4,6,2,3,2,2,5,8]],["detected",[1,1,1,2,4,6,2,3,2,2,5,8]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p34735","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p34736"}}},"glyph":{"type":"object","name":"VBar","id":"p34731","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p34732","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p34733","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p34706","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p34719"},{"type":"object","name":"BoxZoomTool","id":"p34720","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p34721","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p34727","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p34726","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p34728","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p34729"},{"type":"object","name":"SaveTool","id":"p34730"},{"type":"object","name":"HoverTool","id":"p34737","attributes":{"renderers":[{"id":"p34734"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p34714","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34715","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34716"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34717"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p34709","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p34710","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p34711"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p34712"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p34713","attributes":{"axis":{"id":"p34709"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p34718","attributes":{"dimension":1,"axis":{"id":"p34714"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"69156d04-ccf0-441b-892e-a9894d5be0cf","roots":{"p34698":"dd0f2ac3-9326-463c-9b41-b82a331b87c2"},"root_ids":["p34698"]}];
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
(yst[Gene] OR ystA[Gene] OR "heat-stable enterotoxin"[Title] OR yst[Title]) AND 1:30000[SLEN] NOT "whole genome shotgun"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `amplicon_disagrees_with_paper`, `oligos_not_in_cited_paper`, `orientation_inferred`.


## What reached the statistics

38 records were screened for this assay and **37 (97%)** were evaluable, meaning both primers landed in the right orientation and size range. 1 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `truncated` | 1 |

