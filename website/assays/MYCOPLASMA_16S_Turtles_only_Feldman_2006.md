# MYCOPLASMA_16S_Turtles_only_Feldman_2006

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**MYCOPLASMA — 16S (Turtles only)**

| | |
|---|---|
| Target | Mycoplasmatota (scoped by query to the three chelonian mycoplasmas) ([taxid 544448](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=544448)) |
| Gene | 16S (Turtles only) |
| Chemistry | conventional |
| Amplicon | 994 bp |
| Designed | 2006 |
| Paper | [10.7589/0090-3558-42.2.279](https://doi.org/10.7589/0090-3558-42.2.279) |
| Registry status | active |

!!! quote "The paper"
    Feldman SH et al. 2006. J Wildl Dis 42:279-288

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CTGCTGTTATACAGAAAGAAAAG` | 23 nt |
| reverse | `GACTTTGGGCATTACCGGC` | 19 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 2 | 2 | 100.0% | 34.2% – 100.0% |
| baseline (everything earlier) | 27 | 27 | 100.0% | 87.5% – 100.0% |

Change from baseline, Newcombe interval: **-65.8% to 12.5%**. Threshold: **90.0%**.

*2 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (34%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="c350e8a1-7734-4f98-81bc-9b4d5b418700" data-root-id="p18438" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"270789bc-a39c-4fb5-8a9d-8ce91720aaa0":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p18493","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p18494"}}},"roots":[{"type":"object","name":"Figure","id":"p18438","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p18440"},"y_range":{"type":"object","name":"Range1d","id":"p18447","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p18448"},"y_scale":{"type":"object","name":"LinearScale","id":"p18449"},"title":{"type":"object","name":"Title","id":"p18445","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p18483","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p18435","attributes":{"selected":{"type":"object","name":"Selection","id":"p18436","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p18437"},"data":{"type":"map","entries":[["year",[1994,1995,1998,2003,2009,2011,2014,2016,2017,2019,2020,2024]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[1,1,1,1,2,1,1,8,8,2,1,2]],["evaluable",[1,1,1,1,2,1,1,8,8,2,1,2]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent"]],["size",[8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193,9.07684386569143,8.703135093227193,8.703135093227193,9.989711205477885,9.989711205477885,9.07684386569143,8.703135093227193,9.07684386569143]]]}}},"view":{"type":"object","name":"CDSView","id":"p18484","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p18485"}}},"glyph":{"type":"object","name":"Line","id":"p18480","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p18481","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p18482","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p18489","attributes":{"data_source":{"id":"p18435"},"view":{"type":"object","name":"CDSView","id":"p18490","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p18491"}}},"glyph":{"type":"object","name":"Scatter","id":"p18486","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p18487","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p18488","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p18446","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p18460"},{"type":"object","name":"BoxZoomTool","id":"p18461","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p18462","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p18468","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p18467","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p18469","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p18470"},{"type":"object","name":"SaveTool","id":"p18471"},{"type":"object","name":"HoverTool","id":"p18492","attributes":{"renderers":[{"id":"p18489"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p18455","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18456","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18457"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18458"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p18450","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18451","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18452"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18453"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p18454","attributes":{"axis":{"id":"p18450"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p18459","attributes":{"dimension":1,"axis":{"id":"p18455"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p18472","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p18474","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p18475","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p18476","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p18478","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p18477","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p18479","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"270789bc-a39c-4fb5-8a9d-8ce91720aaa0","roots":{"p18438":"c350e8a1-7734-4f98-81bc-9b4d5b418700"},"root_ids":["p18438"]}];
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

<div id="d15e490f-87fa-40b9-9355-529eae0db94b" data-root-id="p18498" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"06c70e56-e147-47c5-ac9a-60a2f5f22f37":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p18538","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p18539"}}},"roots":[{"type":"object","name":"Figure","id":"p18498","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p18499"},"y_range":{"type":"object","name":"DataRange1d","id":"p18500","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p18507"},"y_scale":{"type":"object","name":"LinearScale","id":"p18508"},"title":{"type":"object","name":"Title","id":"p18505","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p18534","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p18495","attributes":{"selected":{"type":"object","name":"Selection","id":"p18496","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p18497"},"data":{"type":"map","entries":[["year",[1994,1995,1998,2003,2009,2011,2014,2016,2017,2019,2020,2024]],["evaluable",[1,1,1,1,2,1,1,8,8,2,1,2]],["detected",[1,1,1,1,2,1,1,8,8,2,1,2]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p18535","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p18536"}}},"glyph":{"type":"object","name":"VBar","id":"p18531","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p18532","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p18533","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p18506","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p18519"},{"type":"object","name":"BoxZoomTool","id":"p18520","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p18521","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p18527","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p18526","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p18528","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p18529"},{"type":"object","name":"SaveTool","id":"p18530"},{"type":"object","name":"HoverTool","id":"p18537","attributes":{"renderers":[{"id":"p18534"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p18514","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18515","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18516"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18517"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p18509","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18510","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18511"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18512"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p18513","attributes":{"axis":{"id":"p18509"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p18518","attributes":{"dimension":1,"axis":{"id":"p18514"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"06c70e56-e147-47c5-ac9a-60a2f5f22f37","roots":{"p18498":"d15e490f-87fa-40b9-9355-529eae0db94b"},"root_ids":["p18498"]}];
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
(txid33922[Organism:exp] OR txid244584[Organism:exp] OR txid33924[Organism:exp])
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).


## What reached the statistics

528 records were screened for this assay and **29 (5%)** were evaluable, meaning both primers landed in the right orientation and size range. 499 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 487 |
| `truncated` | 8 |
| `chance_anchor` | 4 |

