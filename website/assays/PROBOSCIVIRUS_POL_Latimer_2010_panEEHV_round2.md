# PROBOSCIVIRUS_POL_Latimer_2010_panEEHV_round2

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**PROBOSCIVIRUS (elephant herpesviruses, EEHV) — pan-EEHV DNA polymerase, round 2 (Latimer 2010)**

| | |
|---|---|
| Target | Proboscivirus (elephant endotheliotropic herpesviruses) ([taxid 548689](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=548689)) |
| Gene | DNA polymerase (U38/POL) |
| Chemistry | conventional |
| Amplicon | 239 bp |
| Designed | 2010 |
| Paper | [10.1016/j.vetmic.2010.05.042](https://doi.org/10.1016/j.vetmic.2010.05.042) |
| Registry status | active |

!!! quote "The paper"
    Latimer E, Zong JC, Heaggans SY, Richman LK, Hayward GS. Detection and Evaluation of Novel Herpesviruses in Routine and Pathological Samples from Asian and African Elephants: Identification of Two New Probosciviruses (EEHV5 and EEHV6) and Two New Gammaherpesviruses (EGHV3B and EGHV5). Vet Microbiol (author manuscript, PMC 2012 January 10).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `TGYAAYGCCGTNTAYGGATTYACCGG` | 26 nt |
| reverse | `ACAAACACGCTGTCRGTRTCYCCRTA` | 26 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 13 | 14 | 92.9% | 68.5% – 98.7% |
| baseline (everything earlier) | 25 | 25 | 100.0% | 86.7% – 100.0% |

Change from baseline, Newcombe interval: **-31.5% to 7.4%**. Threshold: **90.0%**.

*14 evaluable records since Oct 2021, below the minimum of 15; the detected share is 93% (69%-99%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=0.557, 13 years); by footprint falling (p=0.662). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="a2730a39-2040-481a-940b-8d1129537b0e" data-root-id="p25777" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9aa391a6-c3ae-492b-bfb0-682ade0d29ca":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p25832","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p25833"}}},"roots":[{"type":"object","name":"Figure","id":"p25777","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p25779"},"y_range":{"type":"object","name":"Range1d","id":"p25786","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p25787"},"y_scale":{"type":"object","name":"LinearScale","id":"p25788"},"title":{"type":"object","name":"Title","id":"p25784","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p25822","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p25774","attributes":{"selected":{"type":"object","name":"Selection","id":"p25775","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p25776"},"data":{"type":"map","entries":[["year",[2000,2011,2012,2013,2014,2015,2019,2020,2021,2022,2023,2024,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,66.66666666666666,100.0,100.0,100.0,100.0]],["detected",[1,2,1,4,2,7,1,6,2,3,4,4,1]],["evaluable",[1,2,1,4,2,7,1,6,3,3,4,4,1]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent","recent"]],["size",[8.703135093227193,9.07684386569143,8.703135093227193,9.517227179437622,9.07684386569143,9.897626379762722,8.703135093227193,9.791719296345839,9.328625426046248,9.328625426046248,9.517227179437622,9.517227179437622,8.703135093227193]]]}}},"view":{"type":"object","name":"CDSView","id":"p25823","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p25824"}}},"glyph":{"type":"object","name":"Line","id":"p25819","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p25820","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p25821","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p25828","attributes":{"data_source":{"id":"p25774"},"view":{"type":"object","name":"CDSView","id":"p25829","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p25830"}}},"glyph":{"type":"object","name":"Scatter","id":"p25825","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p25826","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p25827","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p25785","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p25799"},{"type":"object","name":"BoxZoomTool","id":"p25800","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p25801","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p25807","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p25806","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p25808","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p25809"},{"type":"object","name":"SaveTool","id":"p25810"},{"type":"object","name":"HoverTool","id":"p25831","attributes":{"renderers":[{"id":"p25828"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p25794","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p25795","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p25796"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p25797"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p25789","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p25790","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p25791"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p25792"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p25793","attributes":{"axis":{"id":"p25789"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p25798","attributes":{"dimension":1,"axis":{"id":"p25794"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p25811","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2020.5,"right":{"type":"object","name":"Node","id":"p25813","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p25814","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p25815","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p25817","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p25816","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p25818","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9aa391a6-c3ae-492b-bfb0-682ade0d29ca","roots":{"p25777":"a2730a39-2040-481a-940b-8d1129537b0e"},"root_ids":["p25777"]}];
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

<div id="fc57dffb-137a-4816-9538-bc9e8a2e0ee4" data-root-id="p25837" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"cdcbfe19-7d85-45d5-bc47-ecf040476083":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p25877","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p25878"}}},"roots":[{"type":"object","name":"Figure","id":"p25837","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p25838"},"y_range":{"type":"object","name":"DataRange1d","id":"p25839","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p25846"},"y_scale":{"type":"object","name":"LinearScale","id":"p25847"},"title":{"type":"object","name":"Title","id":"p25844","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p25873","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p25834","attributes":{"selected":{"type":"object","name":"Selection","id":"p25835","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p25836"},"data":{"type":"map","entries":[["year",[2000,2011,2012,2013,2014,2015,2019,2020,2021,2022,2023,2024,2026]],["evaluable",[1,2,1,4,2,7,1,6,3,3,4,4,1]],["detected",[1,2,1,4,2,7,1,6,2,3,4,4,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p25874","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p25875"}}},"glyph":{"type":"object","name":"VBar","id":"p25870","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p25871","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p25872","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p25845","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p25858"},{"type":"object","name":"BoxZoomTool","id":"p25859","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p25860","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p25866","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p25865","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p25867","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p25868"},{"type":"object","name":"SaveTool","id":"p25869"},{"type":"object","name":"HoverTool","id":"p25876","attributes":{"renderers":[{"id":"p25873"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p25853","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p25854","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p25855"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p25856"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p25848","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p25849","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p25850"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p25851"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p25852","attributes":{"axis":{"id":"p25848"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p25857","attributes":{"dimension":1,"axis":{"id":"p25853"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"cdcbfe19-7d85-45d5-bc47-ecf040476083","roots":{"p25837":"fc57dffb-137a-4816-9538-bc9e8a2e0ee4"},"root_ids":["p25837"]}];
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

240 records were screened for this assay and **39 (16%)** were evaluable, meaning both primers landed in the right orientation and size range. 201 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `truncated` | 167 |
| `no_site` | 34 |

