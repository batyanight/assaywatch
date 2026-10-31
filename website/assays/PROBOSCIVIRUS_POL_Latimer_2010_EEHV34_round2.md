# PROBOSCIVIRUS_POL_Latimer_2010_EEHV34_round2

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**EEHV3/EEHV4 — DNA polymerase, EEHV3/4-specific nested PCR round 2 (Latimer 2010)**

| | |
|---|---|
| Target | Elephant endotheliotropic herpesvirus 3 and 4 ([taxid 548689](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=548689)) |
| Gene | DNA polymerase (U38/POL) |
| Chemistry | conventional |
| Amplicon | 259 bp |
| Designed | 2010 |
| Paper | [10.1016/j.vetmic.2010.05.042](https://doi.org/10.1016/j.vetmic.2010.05.042) |
| Registry status | active |

!!! quote "The paper"
    Latimer E, Zong JC, Heaggans SY, Richman LK, Hayward GS. Detection and Evaluation of Novel Herpesviruses in Routine and Pathological Samples from Asian and African Elephants: Identification of Two New Probosciviruses (EEHV5 and EEHV6) and Two New Gammaherpesviruses (EGHV3B and EGHV5). Vet Microbiol (author manuscript, PMC 2012 January 10).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ATCCTGGCGCAGCTGCTGAC` | 20 nt |
| reverse | `CGTTGAAGGTGTCGCAGAT` | 19 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 2 | 2 | 100.0% | 34.2% – 100.0% |
| baseline (everything earlier) | 10 | 10 | 100.0% | 72.2% – 100.0% |

Change from baseline, Newcombe interval: **-65.8% to 27.8%**. Threshold: **90.0%**.

*2 evaluable records since Oct 2024, below the minimum of 15; the detected share is 100% (34%-100%), too wide to act on*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="ace0133b-3215-4199-91e0-94de5bae935d" data-root-id="p25049" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"c0e5d42c-4fa1-47c3-9b97-e811fc4f7a2c":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p25104","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p25105"}}},"roots":[{"type":"object","name":"Figure","id":"p25049","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p25051"},"y_range":{"type":"object","name":"Range1d","id":"p25058","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p25059"},"y_scale":{"type":"object","name":"LinearScale","id":"p25060"},"title":{"type":"object","name":"Title","id":"p25056","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p25094","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p25046","attributes":{"selected":{"type":"object","name":"Selection","id":"p25047","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p25048"},"data":{"type":"map","entries":[["year",[2008,2014,2015,2020,2022,2023,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[2,1,4,1,1,1,2]],["evaluable",[2,1,4,1,1,1,2]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","recent"]],["size",[9.07684386569143,8.703135093227193,9.517227179437622,8.703135093227193,8.703135093227193,8.703135093227193,9.07684386569143]]]}}},"view":{"type":"object","name":"CDSView","id":"p25095","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p25096"}}},"glyph":{"type":"object","name":"Line","id":"p25091","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p25092","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p25093","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p25100","attributes":{"data_source":{"id":"p25046"},"view":{"type":"object","name":"CDSView","id":"p25101","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p25102"}}},"glyph":{"type":"object","name":"Scatter","id":"p25097","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p25098","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p25099","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p25057","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p25071"},{"type":"object","name":"BoxZoomTool","id":"p25072","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p25073","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p25079","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p25078","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p25080","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p25081"},{"type":"object","name":"SaveTool","id":"p25082"},{"type":"object","name":"HoverTool","id":"p25103","attributes":{"renderers":[{"id":"p25100"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p25066","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p25067","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p25068"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p25069"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p25061","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p25062","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p25063"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p25064"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p25065","attributes":{"axis":{"id":"p25061"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p25070","attributes":{"dimension":1,"axis":{"id":"p25066"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p25083","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2025.5,"right":{"type":"object","name":"Node","id":"p25085","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p25086","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p25087","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p25089","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p25088","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p25090","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"c0e5d42c-4fa1-47c3-9b97-e811fc4f7a2c","roots":{"p25049":"ace0133b-3215-4199-91e0-94de5bae935d"},"root_ids":["p25049"]}];
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

<div id="ba04d58a-7555-48d5-96f0-5a5593cd9a71" data-root-id="p25109" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"3d90b8be-0ca4-47a5-9d44-198be3d2b723":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p25149","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p25150"}}},"roots":[{"type":"object","name":"Figure","id":"p25109","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p25110"},"y_range":{"type":"object","name":"DataRange1d","id":"p25111","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p25118"},"y_scale":{"type":"object","name":"LinearScale","id":"p25119"},"title":{"type":"object","name":"Title","id":"p25116","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p25145","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p25106","attributes":{"selected":{"type":"object","name":"Selection","id":"p25107","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p25108"},"data":{"type":"map","entries":[["year",[2008,2014,2015,2020,2022,2023,2026]],["evaluable",[2,1,4,1,1,1,2]],["detected",[2,1,4,1,1,1,2]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p25146","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p25147"}}},"glyph":{"type":"object","name":"VBar","id":"p25142","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p25143","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p25144","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p25117","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p25130"},{"type":"object","name":"BoxZoomTool","id":"p25131","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p25132","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p25138","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p25137","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p25139","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p25140"},{"type":"object","name":"SaveTool","id":"p25141"},{"type":"object","name":"HoverTool","id":"p25148","attributes":{"renderers":[{"id":"p25145"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p25125","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p25126","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p25127"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p25128"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p25120","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p25121","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p25122"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p25123"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p25124","attributes":{"axis":{"id":"p25120"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p25129","attributes":{"dimension":1,"axis":{"id":"p25125"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"3d90b8be-0ca4-47a5-9d44-198be3d2b723","roots":{"p25109":"ba04d58a-7555-48d5-96f0-5a5593cd9a71"},"root_ids":["p25109"]}];
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

26 records were screened for this assay and **12 (46%)** were evaluable, meaning both primers landed in the right orientation and size range. 14 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_pair` | 8 |
| `chance_anchor` | 2 |
| `no_site` | 2 |
| `truncated` | 2 |

