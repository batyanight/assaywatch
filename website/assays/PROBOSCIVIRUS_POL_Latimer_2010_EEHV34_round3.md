# PROBOSCIVIRUS_POL_Latimer_2010_EEHV34_round3

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**EEHV3/EEHV4 — DNA polymerase, EEHV3/4-specific nested PCR round 3 (Latimer 2010)**

| | |
|---|---|
| Target | Elephant endotheliotropic herpesvirus 3 and 4 ([taxid 548689](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=548689)) |
| Gene | DNA polymerase (U38/POL) |
| Chemistry | conventional |
| Amplicon | 139 bp |
| Designed | 2010 |
| Paper | [10.1016/j.vetmic.2010.05.042](https://doi.org/10.1016/j.vetmic.2010.05.042) |
| Registry status | active |

!!! quote "The paper"
    Latimer E, Zong JC, Heaggans SY, Richman LK, Hayward GS. Detection and Evaluation of Novel Herpesviruses in Routine and Pathological Samples from Asian and African Elephants: Identification of Two New Probosciviruses (EEHV5 and EEHV6) and Two New Gammaherpesviruses (EGHV3B and EGHV5). Vet Microbiol (author manuscript, PMC 2012 January 10).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CTCACCTGCAACGCCGTCTA` | 20 nt |
| reverse | `CGTTGAAGGTGTCGCAGAT` | 19 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 4 | 4 | 100.0% | 51.0% – 100.0% |
| baseline (everything earlier) | 10 | 11 | 90.9% | 62.3% – 98.4% |

Change from baseline, Newcombe interval: **-40.5% to 37.7%**. Threshold: **90.0%**.

*4 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (51%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=0.99, 8 years); by footprint rising (p=0.824); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="a0149533-aa81-4a71-9599-a8edd3f31384" data-root-id="p25154" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"66a8f23f-d7d9-4c6e-a095-2cdb6ff8f4d3":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p25209","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p25210"}}},"roots":[{"type":"object","name":"Figure","id":"p25154","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p25156"},"y_range":{"type":"object","name":"Range1d","id":"p25163","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p25164"},"y_scale":{"type":"object","name":"LinearScale","id":"p25165"},"title":{"type":"object","name":"Title","id":"p25161","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p25199","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p25151","attributes":{"selected":{"type":"object","name":"Selection","id":"p25152","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p25153"},"data":{"type":"map","entries":[["year",[2008,2014,2015,2017,2020,2022,2023,2026]],["share",[100.0,100.0,100.0,0.0,100.0,100.0,100.0,100.0]],["detected",[2,1,6,0,1,1,1,2]],["evaluable",[2,1,6,1,1,1,1,2]],["window",["baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,8.703135093227193,9.791719296345839,8.703135093227193,8.703135093227193,8.703135093227193,8.703135093227193,9.07684386569143]]]}}},"view":{"type":"object","name":"CDSView","id":"p25200","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p25201"}}},"glyph":{"type":"object","name":"Line","id":"p25196","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p25197","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p25198","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p25205","attributes":{"data_source":{"id":"p25151"},"view":{"type":"object","name":"CDSView","id":"p25206","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p25207"}}},"glyph":{"type":"object","name":"Scatter","id":"p25202","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p25203","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p25204","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p25162","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p25176"},{"type":"object","name":"BoxZoomTool","id":"p25177","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p25178","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p25184","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p25183","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p25185","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p25186"},{"type":"object","name":"SaveTool","id":"p25187"},{"type":"object","name":"HoverTool","id":"p25208","attributes":{"renderers":[{"id":"p25205"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p25171","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p25172","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p25173"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p25174"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p25166","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p25167","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p25168"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p25169"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p25170","attributes":{"axis":{"id":"p25166"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p25175","attributes":{"dimension":1,"axis":{"id":"p25171"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p25188","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2021.5,"right":{"type":"object","name":"Node","id":"p25190","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p25191","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p25192","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p25194","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p25193","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p25195","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"66a8f23f-d7d9-4c6e-a095-2cdb6ff8f4d3","roots":{"p25154":"a0149533-aa81-4a71-9599-a8edd3f31384"},"root_ids":["p25154"]}];
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

<div id="ed691e1f-92ba-4e9f-a661-b4c66914ddbd" data-root-id="p25214" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"60e1ce88-a3df-4e9b-9627-0585610266a4":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p25254","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p25255"}}},"roots":[{"type":"object","name":"Figure","id":"p25214","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p25215"},"y_range":{"type":"object","name":"DataRange1d","id":"p25216","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p25223"},"y_scale":{"type":"object","name":"LinearScale","id":"p25224"},"title":{"type":"object","name":"Title","id":"p25221","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p25250","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p25211","attributes":{"selected":{"type":"object","name":"Selection","id":"p25212","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p25213"},"data":{"type":"map","entries":[["year",[2008,2014,2015,2017,2020,2022,2023,2026]],["evaluable",[2,1,6,1,1,1,1,2]],["detected",[2,1,6,0,1,1,1,2]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p25251","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p25252"}}},"glyph":{"type":"object","name":"VBar","id":"p25247","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p25248","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p25249","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p25222","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p25235"},{"type":"object","name":"BoxZoomTool","id":"p25236","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p25237","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p25243","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p25242","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p25244","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p25245"},{"type":"object","name":"SaveTool","id":"p25246"},{"type":"object","name":"HoverTool","id":"p25253","attributes":{"renderers":[{"id":"p25250"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p25230","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p25231","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p25232"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p25233"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p25225","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p25226","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p25227"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p25228"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p25229","attributes":{"axis":{"id":"p25225"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p25234","attributes":{"dimension":1,"axis":{"id":"p25230"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"60e1ce88-a3df-4e9b-9627-0585610266a4","roots":{"p25214":"ed691e1f-92ba-4e9f-a661-b4c66914ddbd"},"root_ids":["p25214"]}];
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

26 records were screened for this assay and **15 (58%)** were evaluable, meaning both primers landed in the right orientation and size range. 11 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_pair` | 10 |
| `no_site` | 1 |

