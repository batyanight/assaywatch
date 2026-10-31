# CHLAMYDIA_pneumoniae_16S_Messmer_1997_round2

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**CHLAMYDIA PNEUMONIAE — 16S rRNA nested multiplex PCR, second step (Messmer 1997)**

| | |
|---|---|
| Target | Chlamydia pneumoniae ([taxid 83558](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=83558)) |
| Gene | 16S rRNA |
| Chemistry | conventional |
| Amplicon | 222 bp |
| Designed | 1997 |
| Paper | [10.1128/jcm.35.8.2043-2046.1997](https://doi.org/10.1128/jcm.35.8.2043-2046.1997) |
| Registry status | active |

!!! quote "The paper"
    Messmer, T. O., Skelton, S. K., Moroney, J. F., Daugharty, H. & Fields, B. S. Application of a nested, multiplex PCR to psittacosis outbreaks. Journal of Clinical Microbiology 35, 2043-2046 (1997).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ATAATGACTTCGGTTGTTATT` | 21 nt |
| reverse | `CGTCATCGCCTTGGTGGGCTT` | 21 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 5 | 5 | 100.0% | 56.6% – 100.0% |
| baseline (everything earlier) | 11 | 11 | 100.0% | 74.1% – 100.0% |

Change from baseline, Newcombe interval: **-43.4% to 25.9%**. Threshold: **90.0%**.

*5 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (57%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="ebce31d0-1730-400f-8117-99673baf9935" data-root-id="p7979" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"7d2bfeed-6af5-43f8-aaaf-b0a6234dd4e3":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p8034","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p8035"}}},"roots":[{"type":"object","name":"Figure","id":"p7979","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p7981"},"y_range":{"type":"object","name":"Range1d","id":"p7988","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p7989"},"y_scale":{"type":"object","name":"LinearScale","id":"p7990"},"title":{"type":"object","name":"Title","id":"p7986","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p8024","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p7976","attributes":{"selected":{"type":"object","name":"Selection","id":"p7977","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p7978"},"data":{"type":"map","entries":[["year",[1993,1995,1997,1999,2000,2003,2004,2006,2008,2009,2024]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[1,2,1,1,1,1,1,1,1,1,5]],["evaluable",[1,2,1,1,1,1,1,1,1,1,5]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent"]],["size",[8.703135093227193,9.07684386569143,8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193,9.667366891029102]]]}}},"view":{"type":"object","name":"CDSView","id":"p8025","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8026"}}},"glyph":{"type":"object","name":"Line","id":"p8021","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p8022","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p8023","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p8030","attributes":{"data_source":{"id":"p7976"},"view":{"type":"object","name":"CDSView","id":"p8031","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8032"}}},"glyph":{"type":"object","name":"Scatter","id":"p8027","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p8028","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p8029","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p7987","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p8001"},{"type":"object","name":"BoxZoomTool","id":"p8002","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p8003","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p8009","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8008","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p8010","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p8011"},{"type":"object","name":"SaveTool","id":"p8012"},{"type":"object","name":"HoverTool","id":"p8033","attributes":{"renderers":[{"id":"p8030"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p7996","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7997","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7998"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7999"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p7991","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p7992","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p7993"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p7994"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p7995","attributes":{"axis":{"id":"p7991"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p8000","attributes":{"dimension":1,"axis":{"id":"p7996"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p8013","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p8015","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p8016","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p8017","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p8019","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8018","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p8020","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"7d2bfeed-6af5-43f8-aaaf-b0a6234dd4e3","roots":{"p7979":"ebce31d0-1730-400f-8117-99673baf9935"},"root_ids":["p7979"]}];
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

<div id="df480eba-4ecb-4814-b2e5-50c0bbc7e183" data-root-id="p8039" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"ea346e71-46cf-4860-85b9-24cff773c268":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p8079","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p8080"}}},"roots":[{"type":"object","name":"Figure","id":"p8039","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p8040"},"y_range":{"type":"object","name":"DataRange1d","id":"p8041","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p8048"},"y_scale":{"type":"object","name":"LinearScale","id":"p8049"},"title":{"type":"object","name":"Title","id":"p8046","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p8075","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p8036","attributes":{"selected":{"type":"object","name":"Selection","id":"p8037","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p8038"},"data":{"type":"map","entries":[["year",[1993,1995,1997,1999,2000,2003,2004,2006,2008,2009,2024]],["evaluable",[1,2,1,1,1,1,1,1,1,1,5]],["detected",[1,2,1,1,1,1,1,1,1,1,5]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p8076","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8077"}}},"glyph":{"type":"object","name":"VBar","id":"p8072","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p8073","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p8074","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p8047","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p8060"},{"type":"object","name":"BoxZoomTool","id":"p8061","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p8062","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p8068","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8067","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p8069","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p8070"},{"type":"object","name":"SaveTool","id":"p8071"},{"type":"object","name":"HoverTool","id":"p8078","attributes":{"renderers":[{"id":"p8075"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p8055","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8056","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8057"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8058"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p8050","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8051","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8052"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8053"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p8054","attributes":{"axis":{"id":"p8050"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p8059","attributes":{"dimension":1,"axis":{"id":"p8055"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"ea346e71-46cf-4860-85b9-24cff773c268","roots":{"p8039":"df480eba-4ecb-4814-b2e5-50c0bbc7e183"},"root_ids":["p8039"]}];
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
16S[Title] OR "16S ribosomal RNA"[Title] OR "small subunit ribosomal"[Title] OR "complete genome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).


## What reached the statistics

48 records were screened for this assay and **16 (33%)** were evaluable, meaning both primers landed in the right orientation and size range. 32 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `truncated` | 18 |
| `no_site` | 14 |

