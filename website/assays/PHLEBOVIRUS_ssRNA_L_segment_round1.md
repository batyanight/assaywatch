# PHLEBOVIRUS_ssRNA_L_segment_round1

<span class="aw-chip aw-chip-stable">stable</span>

**PHLEBOVIRUS (ssRNA) — L segment (PREDICT P-021 round 1)**

| | |
|---|---|
| Target | Phlebovirus ([taxid 11584](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11584)) |
| Gene | L segment |
| Chemistry | conventional |
| Amplicon | 553 bp |
| Designed | 2003 |
| Paper | [10.1002/jmv.10465](https://doi.org/10.1002/jmv.10465) |
| Registry status | active |

!!! quote "The paper"
    Sanchez-Seco, M. P. et al. Detection and identification of Toscana and other phleboviruses by RT-nested-PCR assays with degenerated primers. J Med Virol 71, 140-149 (2003).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ATGGARGGNTTTGTNWSNCNNCC` | 23 nt |
| reverse | `AARTTRCTNGWNGCYTTNARNGTNGC` | 26 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 53 | 54 | 98.1% | 90.2% – 99.7% |
| baseline (everything earlier) | 208 | 216 | 96.3% | 92.9% – 98.1% |

Change from baseline, Newcombe interval: **-6.3% to 5.6%**. Threshold: **90.0%**.

*detected share 98.1% (90%-100%) since Oct 2024*

Trend across deposit years: by record rising (p=0.585, 17 years); by footprint falling (p=0.669); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="b327ae59-f8f0-4733-b323-f350f15f7591" data-root-id="p23397" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"70c1fe2c-18e4-49d8-aaf2-676b4b6bb03c":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p23452","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p23453"}}},"roots":[{"type":"object","name":"Figure","id":"p23397","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p23399"},"y_range":{"type":"object","name":"Range1d","id":"p23406","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p23407"},"y_scale":{"type":"object","name":"LinearScale","id":"p23408"},"title":{"type":"object","name":"Title","id":"p23404","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p23442","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p23394","attributes":{"selected":{"type":"object","name":"Selection","id":"p23395","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p23396"},"data":{"type":"map","entries":[["year",[1992,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,66.66666666666666,100.0,100.0,100.0,100.0,90.625,100.0,90.9090909090909,92.85714285714286,97.87234042553192,98.48484848484848,96.875,100.0]],["detected",[1,1,22,5,2,3,1,1,10,29,3,10,13,46,65,31,18]],["evaluable",[1,1,22,5,3,3,1,1,10,32,3,11,14,47,66,32,18]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,10.683957047019447,9.667366891029102,9.328625426046248,9.328625426046248,8.703135093227193,8.703135093227193,10.143865699252444,10.934913263353746,9.328625426046248,10.209683151927734,10.37579022724969,11.18724806845314,11.405466677556973,10.934913263353746,10.547770533331066]]]}}},"view":{"type":"object","name":"CDSView","id":"p23443","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p23444"}}},"glyph":{"type":"object","name":"Line","id":"p23439","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p23440","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p23441","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p23448","attributes":{"data_source":{"id":"p23394"},"view":{"type":"object","name":"CDSView","id":"p23449","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p23450"}}},"glyph":{"type":"object","name":"Scatter","id":"p23445","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p23446","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p23447","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p23405","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p23419"},{"type":"object","name":"BoxZoomTool","id":"p23420","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p23421","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p23427","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p23426","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p23428","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p23429"},{"type":"object","name":"SaveTool","id":"p23430"},{"type":"object","name":"HoverTool","id":"p23451","attributes":{"renderers":[{"id":"p23448"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p23414","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23415","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23416"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23417"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p23409","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23410","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23411"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23412"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p23413","attributes":{"axis":{"id":"p23409"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p23418","attributes":{"dimension":1,"axis":{"id":"p23414"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p23431","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p23433","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p23434","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p23435","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p23437","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p23436","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p23438","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"70c1fe2c-18e4-49d8-aaf2-676b4b6bb03c","roots":{"p23397":"b327ae59-f8f0-4733-b323-f350f15f7591"},"root_ids":["p23397"]}];
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

<div id="da7e8687-d0c8-4365-82d0-0220699d0b6f" data-root-id="p23457" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"90e71069-a8c2-4e61-896c-d90499a70022":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p23497","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p23498"}}},"roots":[{"type":"object","name":"Figure","id":"p23457","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p23458"},"y_range":{"type":"object","name":"DataRange1d","id":"p23459","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p23466"},"y_scale":{"type":"object","name":"LinearScale","id":"p23467"},"title":{"type":"object","name":"Title","id":"p23464","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p23493","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p23454","attributes":{"selected":{"type":"object","name":"Selection","id":"p23455","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p23456"},"data":{"type":"map","entries":[["year",[1992,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,22,5,3,3,1,1,10,32,3,11,14,47,66,32,18]],["detected",[1,1,22,5,2,3,1,1,10,29,3,10,13,46,65,31,18]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p23494","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p23495"}}},"glyph":{"type":"object","name":"VBar","id":"p23490","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p23491","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p23492","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p23465","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p23478"},{"type":"object","name":"BoxZoomTool","id":"p23479","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p23480","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p23486","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p23485","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p23487","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p23488"},{"type":"object","name":"SaveTool","id":"p23489"},{"type":"object","name":"HoverTool","id":"p23496","attributes":{"renderers":[{"id":"p23493"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p23473","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23474","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23475"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23476"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p23468","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p23469","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p23470"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p23471"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p23472","attributes":{"axis":{"id":"p23468"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p23477","attributes":{"dimension":1,"axis":{"id":"p23473"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"90e71069-a8c2-4e61-896c-d90499a70022","roots":{"p23457":"da7e8687-d0c8-4365-82d0-0220699d0b6f"},"root_ids":["p23457"]}];
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
L[Gene] OR "L segment"[Title] OR polymerase[Title] OR "complete genome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).


## What reached the statistics

1,147 records were screened for this assay and **270 (24%)** were evaluable, meaning both primers landed in the right orientation and size range. 877 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 661 |
| `chance_anchor` | 113 |
| `truncated` | 5 |

