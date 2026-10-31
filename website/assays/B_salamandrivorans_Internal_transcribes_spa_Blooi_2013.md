# B_salamandrivorans_Internal_transcribes_spa_Blooi_2013

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**Batrachochytrium salamandrivorans — ITS real-time PCR STerF/STerR (Blooi 2013)**

| | |
|---|---|
| Target | Batrachochytrium salamandrivorans ([taxid 1357716](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1357716)) |
| Gene | ITS1-5.8S rDNA |
| Chemistry | mgb |
| Amplicon | — |
| Designed | 2013 |
| Paper | [10.1128/JCM.02313-13](https://doi.org/10.1128/JCM.02313-13) |
| Registry status | active |

!!! quote "The paper"
    Blooi M et al. 2013. J Clin Microbiol 51:4173-4177

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `TGCTCCATCTCCCCCTCTTCA` | 21 nt |
| reverse | `TGAACGCACATTGCACTCTAC` | 21 nt |
| probe | `ACAAGAAAATACTATTGATTCTCAAACAGGCA` | 32 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 0 | 5 | 0.0% | 0.0% – 43.4% |
| baseline (everything earlier) | 1 | 1 | 100.0% | 20.7% – 100.0% |

Change from baseline, Newcombe interval: **-100.0% to -9.5%**. Threshold: **90.0%**.

*5 evaluable records since Oct 2024, below the minimum of 15; the detected share is 0% (0%-43%), too wide to act on*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="af2e8d01-418d-49e9-8f51-fcce41597ca9" data-root-id="p5780" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"0bed4e69-ceaa-4e06-9a5a-5106ec7f5feb":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p5835","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p5836"}}},"roots":[{"type":"object","name":"Figure","id":"p5780","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p5782"},"y_range":{"type":"object","name":"Range1d","id":"p5789","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p5790"},"y_scale":{"type":"object","name":"LinearScale","id":"p5791"},"title":{"type":"object","name":"Title","id":"p5787","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p5825","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p5777","attributes":{"selected":{"type":"object","name":"Selection","id":"p5778","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p5779"},"data":{"type":"map","entries":[["year",[2013,2024]],["share",[100.0,0.0]],["detected",[1,0]],["evaluable",[1,5]],["window",["baseline","recent"]],["size",[8.703135093227193,9.667366891029102]]]}}},"view":{"type":"object","name":"CDSView","id":"p5826","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p5827"}}},"glyph":{"type":"object","name":"Line","id":"p5822","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p5823","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p5824","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p5831","attributes":{"data_source":{"id":"p5777"},"view":{"type":"object","name":"CDSView","id":"p5832","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p5833"}}},"glyph":{"type":"object","name":"Scatter","id":"p5828","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p5829","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p5830","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p5788","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p5802"},{"type":"object","name":"BoxZoomTool","id":"p5803","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p5804","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p5810","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p5809","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p5811","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p5812"},{"type":"object","name":"SaveTool","id":"p5813"},{"type":"object","name":"HoverTool","id":"p5834","attributes":{"renderers":[{"id":"p5831"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p5797","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p5798","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5799"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5800"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p5792","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p5793","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5794"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5795"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p5796","attributes":{"axis":{"id":"p5792"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p5801","attributes":{"dimension":1,"axis":{"id":"p5797"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p5814","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p5816","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p5817","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p5818","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p5820","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p5819","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p5821","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"0bed4e69-ceaa-4e06-9a5a-5106ec7f5feb","roots":{"p5780":"af2e8d01-418d-49e9-8f51-fcce41597ca9"},"root_ids":["p5780"]}];
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

<div id="ca84db84-c38d-4fff-ae3f-5d9c44861648" data-root-id="p5840" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"dd645f68-de87-4f6d-8460-515660c89335":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p5880","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p5881"}}},"roots":[{"type":"object","name":"Figure","id":"p5840","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p5841"},"y_range":{"type":"object","name":"DataRange1d","id":"p5842","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p5849"},"y_scale":{"type":"object","name":"LinearScale","id":"p5850"},"title":{"type":"object","name":"Title","id":"p5847","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p5876","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p5837","attributes":{"selected":{"type":"object","name":"Selection","id":"p5838","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p5839"},"data":{"type":"map","entries":[["year",[2013,2024]],["evaluable",[1,5]],["detected",[1,0]],["colour",["#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p5877","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p5878"}}},"glyph":{"type":"object","name":"VBar","id":"p5873","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p5874","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p5875","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p5848","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p5861"},{"type":"object","name":"BoxZoomTool","id":"p5862","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p5863","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p5869","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p5868","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p5870","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p5871"},{"type":"object","name":"SaveTool","id":"p5872"},{"type":"object","name":"HoverTool","id":"p5879","attributes":{"renderers":[{"id":"p5876"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p5856","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p5857","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5858"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5859"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p5851","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p5852","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p5853"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p5854"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p5855","attributes":{"axis":{"id":"p5851"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p5860","attributes":{"dimension":1,"axis":{"id":"p5856"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"dd645f68-de87-4f6d-8460-515660c89335","roots":{"p5840":"ca84db84-c38d-4fff-ae3f-5d9c44861648"},"root_ids":["p5840"]}];
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
ITS[Title] OR ITS1[Title] OR ITS2[Title] OR "internal transcribed spacer"[Title] OR "5.8S"[Title] OR "ribosomal RNA"[Title] OR rRNA[Title] OR "ribosomal DNA"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `oligos_from_secondary_source`.


## What reached the statistics

12 records were screened for this assay and **6 (50%)** were evaluable, meaning both primers landed in the right orientation and size range. 6 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 5 |
| `truncated` | 1 |

