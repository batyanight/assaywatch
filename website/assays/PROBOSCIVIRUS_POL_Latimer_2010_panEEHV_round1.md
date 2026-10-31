# PROBOSCIVIRUS_POL_Latimer_2010_panEEHV_round1

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**PROBOSCIVIRUS (elephant herpesviruses, EEHV) — pan-EEHV DNA polymerase, round 1 (Latimer 2010)**

| | |
|---|---|
| Target | Proboscivirus (elephant endotheliotropic herpesviruses) ([taxid 548689](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=548689)) |
| Gene | DNA polymerase (U38/POL) |
| Chemistry | conventional |
| Amplicon | 536 bp |
| Designed | 2010 |
| Paper | [10.1016/j.vetmic.2010.05.042](https://doi.org/10.1016/j.vetmic.2010.05.042) |
| Registry status | active |

!!! quote "The paper"
    Latimer E, Zong JC, Heaggans SY, Richman LK, Hayward GS. Detection and Evaluation of Novel Herpesviruses in Routine and Pathological Samples from Asian and African Elephants: Identification of Two New Probosciviruses (EEHV5 and EEHV6) and Two New Gammaherpesviruses (EGHV3B and EGHV5). Vet Microbiol (author manuscript, PMC 2012 January 10).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GTATTTGATTTYGCNAGYYTGTAYCC` | 26 nt |
| reverse | `ACAAACACGCTGTCRGTRTCYCCRTA` | 26 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 7 | 12 | 58.3% | 32.0% – 80.7% |
| baseline (everything earlier) | 13 | 20 | 65.0% | 43.3% – 81.9% |

Change from baseline, Newcombe interval: **-38.0% to 24.5%**. Threshold: **90.0%**.

*12 evaluable records since Oct 2021, below the minimum of 15; the detected share is 58% (32%-81%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record rising (p=0.807, 12 years); by footprint falling (p=0.88); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="f0ed6b77-bbcb-4296-bf1d-90780b008404" data-root-id="p25672" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"31741407-a7ee-49e5-942c-4620058f1ffd":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p25727","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p25728"}}},"roots":[{"type":"object","name":"Figure","id":"p25672","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p25674"},"y_range":{"type":"object","name":"Range1d","id":"p25681","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p25682"},"y_scale":{"type":"object","name":"LinearScale","id":"p25683"},"title":{"type":"object","name":"Title","id":"p25679","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p25717","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p25669","attributes":{"selected":{"type":"object","name":"Selection","id":"p25670","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p25671"},"data":{"type":"map","entries":[["year",[2000,2011,2013,2014,2015,2019,2020,2021,2022,2023,2024,2026]],["share",[100.0,0.0,100.0,0.0,33.33333333333333,100.0,83.33333333333334,100.0,0.0,75.0,33.33333333333333,100.0]],["detected",[1,0,4,0,1,1,5,3,0,3,1,1]],["evaluable",[1,2,4,2,3,1,6,3,2,4,3,1]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent","recent"]],["size",[8.703135093227193,9.07684386569143,9.517227179437622,9.07684386569143,9.328625426046248,8.703135093227193,9.791719296345839,9.328625426046248,9.07684386569143,9.517227179437622,9.328625426046248,8.703135093227193]]]}}},"view":{"type":"object","name":"CDSView","id":"p25718","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p25719"}}},"glyph":{"type":"object","name":"Line","id":"p25714","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p25715","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p25716","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p25723","attributes":{"data_source":{"id":"p25669"},"view":{"type":"object","name":"CDSView","id":"p25724","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p25725"}}},"glyph":{"type":"object","name":"Scatter","id":"p25720","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p25721","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p25722","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p25680","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p25694"},{"type":"object","name":"BoxZoomTool","id":"p25695","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p25696","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p25702","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p25701","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p25703","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p25704"},{"type":"object","name":"SaveTool","id":"p25705"},{"type":"object","name":"HoverTool","id":"p25726","attributes":{"renderers":[{"id":"p25723"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p25689","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p25690","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p25691"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p25692"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p25684","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p25685","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p25686"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p25687"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p25688","attributes":{"axis":{"id":"p25684"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p25693","attributes":{"dimension":1,"axis":{"id":"p25689"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p25706","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2020.5,"right":{"type":"object","name":"Node","id":"p25708","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p25709","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p25710","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p25712","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p25711","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p25713","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"31741407-a7ee-49e5-942c-4620058f1ffd","roots":{"p25672":"f0ed6b77-bbcb-4296-bf1d-90780b008404"},"root_ids":["p25672"]}];
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

<div id="d842744c-c950-46b0-8575-26a54b92cfba" data-root-id="p25732" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"f36060ad-b290-4b47-965c-fe2c00c1ed05":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p25772","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p25773"}}},"roots":[{"type":"object","name":"Figure","id":"p25732","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p25733"},"y_range":{"type":"object","name":"DataRange1d","id":"p25734","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p25741"},"y_scale":{"type":"object","name":"LinearScale","id":"p25742"},"title":{"type":"object","name":"Title","id":"p25739","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p25768","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p25729","attributes":{"selected":{"type":"object","name":"Selection","id":"p25730","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p25731"},"data":{"type":"map","entries":[["year",[2000,2011,2013,2014,2015,2019,2020,2021,2022,2023,2024,2026]],["evaluable",[1,2,4,2,3,1,6,3,2,4,3,1]],["detected",[1,0,4,0,1,1,5,3,0,3,1,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p25769","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p25770"}}},"glyph":{"type":"object","name":"VBar","id":"p25765","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p25766","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p25767","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p25740","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p25753"},{"type":"object","name":"BoxZoomTool","id":"p25754","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p25755","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p25761","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p25760","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p25762","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p25763"},{"type":"object","name":"SaveTool","id":"p25764"},{"type":"object","name":"HoverTool","id":"p25771","attributes":{"renderers":[{"id":"p25768"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p25748","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p25749","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p25750"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p25751"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p25743","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p25744","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p25745"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p25746"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p25747","attributes":{"axis":{"id":"p25743"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p25752","attributes":{"dimension":1,"axis":{"id":"p25748"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"f36060ad-b290-4b47-965c-fe2c00c1ed05","roots":{"p25732":"d842744c-c950-46b0-8575-26a54b92cfba"},"root_ids":["p25732"]}];
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
"DNA polymerase"[Title] OR U38[Gene] OR POL[Gene] OR "complete genome"[Title] OR "partial genome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).


## What reached the statistics

240 records were screened for this assay and **32 (13%)** were evaluable, meaning both primers landed in the right orientation and size range. 208 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 188 |
| `truncated` | 20 |

