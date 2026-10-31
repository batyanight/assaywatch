# PROBOSCIVIRUS_POL_Latimer_2010_EEHV34_round1

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**EEHV3/EEHV4 — DNA polymerase, EEHV3/4-specific nested PCR round 1 (Latimer 2010)**

| | |
|---|---|
| Target | Elephant endotheliotropic herpesvirus 3 and 4 ([taxid 548689](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=548689)) |
| Gene | DNA polymerase (U38/POL) |
| Chemistry | conventional |
| Amplicon | 407 bp |
| Designed | 2010 |
| Paper | [10.1016/j.vetmic.2010.05.042](https://doi.org/10.1016/j.vetmic.2010.05.042) |
| Registry status | active |

!!! quote "The paper"
    Latimer E, Zong JC, Heaggans SY, Richman LK, Hayward GS. Detection and Evaluation of Novel Herpesviruses in Routine and Pathological Samples from Asian and African Elephants: Identification of Two New Probosciviruses (EEHV5 and EEHV6) and Two New Gammaherpesviruses (EGHV3B and EGHV5). Vet Microbiol (author manuscript, PMC 2012 January 10).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CAGCATCATCCAGGCCTACAAC` | 22 nt |
| reverse | `CGTTGAAGGTGTCGCAGAT` | 19 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 2 | 2 | 100.0% | 34.2% – 100.0% |
| baseline (everything earlier) | 7 | 9 | 77.8% | 45.3% – 93.7% |

Change from baseline, Newcombe interval: **-45.4% to 54.7%**. Threshold: **90.0%**.

*2 evaluable records since Oct 2024, below the minimum of 15; the detected share is 100% (34%-100%), too wide to act on*

Trend across deposit years: by record rising (p=0.374, 7 years); by footprint rising (p=0.577). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="c537279a-89c8-44d9-8fb1-f7e732800f09" data-root-id="p24944" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"50caf673-2092-4f45-b042-f265d134ad08":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p24999","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p25000"}}},"roots":[{"type":"object","name":"Figure","id":"p24944","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p24946"},"y_range":{"type":"object","name":"Range1d","id":"p24953","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p24954"},"y_scale":{"type":"object","name":"LinearScale","id":"p24955"},"title":{"type":"object","name":"Title","id":"p24951","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p24989","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p24941","attributes":{"selected":{"type":"object","name":"Selection","id":"p24942","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p24943"},"data":{"type":"map","entries":[["year",[2008,2014,2015,2020,2022,2023,2026]],["share",[100.0,100.0,50.0,100.0,100.0,100.0,100.0]],["detected",[1,1,2,1,1,1,2]],["evaluable",[1,1,4,1,1,1,2]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","recent"]],["size",[8.703135093227193,8.703135093227193,9.517227179437622,8.703135093227193,8.703135093227193,8.703135093227193,9.07684386569143]]]}}},"view":{"type":"object","name":"CDSView","id":"p24990","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p24991"}}},"glyph":{"type":"object","name":"Line","id":"p24986","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p24987","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p24988","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p24995","attributes":{"data_source":{"id":"p24941"},"view":{"type":"object","name":"CDSView","id":"p24996","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p24997"}}},"glyph":{"type":"object","name":"Scatter","id":"p24992","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p24993","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p24994","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p24952","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p24966"},{"type":"object","name":"BoxZoomTool","id":"p24967","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p24968","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p24974","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p24973","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p24975","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p24976"},{"type":"object","name":"SaveTool","id":"p24977"},{"type":"object","name":"HoverTool","id":"p24998","attributes":{"renderers":[{"id":"p24995"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p24961","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p24962","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p24963"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p24964"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p24956","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p24957","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p24958"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p24959"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p24960","attributes":{"axis":{"id":"p24956"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p24965","attributes":{"dimension":1,"axis":{"id":"p24961"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p24978","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2025.5,"right":{"type":"object","name":"Node","id":"p24980","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p24981","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p24982","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p24984","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p24983","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p24985","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"50caf673-2092-4f45-b042-f265d134ad08","roots":{"p24944":"c537279a-89c8-44d9-8fb1-f7e732800f09"},"root_ids":["p24944"]}];
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

<div id="e896a595-98b5-4851-aa35-88972d30c2cf" data-root-id="p25004" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"125dd08e-c6d6-4ce8-9298-6861389a25fa":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p25044","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p25045"}}},"roots":[{"type":"object","name":"Figure","id":"p25004","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p25005"},"y_range":{"type":"object","name":"DataRange1d","id":"p25006","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p25013"},"y_scale":{"type":"object","name":"LinearScale","id":"p25014"},"title":{"type":"object","name":"Title","id":"p25011","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p25040","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p25001","attributes":{"selected":{"type":"object","name":"Selection","id":"p25002","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p25003"},"data":{"type":"map","entries":[["year",[2008,2014,2015,2020,2022,2023,2026]],["evaluable",[1,1,4,1,1,1,2]],["detected",[1,1,2,1,1,1,2]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p25041","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p25042"}}},"glyph":{"type":"object","name":"VBar","id":"p25037","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p25038","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p25039","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p25012","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p25025"},{"type":"object","name":"BoxZoomTool","id":"p25026","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p25027","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p25033","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p25032","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p25034","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p25035"},{"type":"object","name":"SaveTool","id":"p25036"},{"type":"object","name":"HoverTool","id":"p25043","attributes":{"renderers":[{"id":"p25040"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p25020","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p25021","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p25022"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p25023"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p25015","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p25016","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p25017"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p25018"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p25019","attributes":{"axis":{"id":"p25015"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p25024","attributes":{"dimension":1,"axis":{"id":"p25020"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"125dd08e-c6d6-4ce8-9298-6861389a25fa","roots":{"p25004":"e896a595-98b5-4851-aa35-88972d30c2cf"},"root_ids":["p25004"]}];
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
(txid548913[Organism:exp] OR txid548914[Organism:exp] OR txid3060652[Organism:exp] OR txid3050274[Organism:exp]) AND ("DNA polymerase"[Title] OR U38[Gene] OR POL[Gene] OR "complete genome"[Title] OR "partial genome"[Title])
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).


## What reached the statistics

26 records were screened for this assay and **11 (42%)** were evaluable, meaning both primers landed in the right orientation and size range. 15 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `chance_anchor` | 8 |
| `truncated` | 5 |
| `no_site` | 2 |

