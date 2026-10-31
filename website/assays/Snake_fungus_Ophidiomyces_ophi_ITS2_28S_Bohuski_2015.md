# Snake_fungus_Ophidiomyces_ophi_ITS2_28S_Bohuski_2015

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**Ophidiomyces ophidiicola — ITS2 real-time PCR (Bohuski 2015)**

| | |
|---|---|
| Target | Ophidiomyces ophidiicola ([taxid 1387563](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1387563)) |
| Gene | ITS2 |
| Chemistry | mgb |
| Amplicon | 82 bp |
| Designed | 2015 |
| Paper | [10.1186/s12917-015-0407-8](https://doi.org/10.1186/s12917-015-0407-8) |
| Registry status | active |

!!! quote "The paper"
    Bohuski E et al. 2015. BMC Vet Res 11:95

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GAGTGTATGGGAATCTGTTTC` | 21 nt |
| reverse | `GGTCAAACCGGAAAGAATG` | 19 nt |
| probe | `TCTCGCTCGAAGACCCGATCG` | 21 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 5 | 8 | 62.5% | 30.6% – 86.3% |
| baseline (everything earlier) | 17 | 17 | 100.0% | 81.6% – 100.0% |

Change from baseline, Newcombe interval: **-69.4% to -7.4%**. Threshold: **90.0%**.

*8 evaluable records since Oct 2021, below the minimum of 15; the detected share is 62% (31%-86%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=0.00964, 8 years); by footprint falling (p=0.105). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="c95e5224-f234-47b2-bb29-42158669fd0e" data-root-id="p32705" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"5a3cbc8c-cacd-4479-8e6d-c41f2a7a7c5a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p32760","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p32761"}}},"roots":[{"type":"object","name":"Figure","id":"p32705","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p32707"},"y_range":{"type":"object","name":"Range1d","id":"p32714","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p32715"},"y_scale":{"type":"object","name":"LinearScale","id":"p32716"},"title":{"type":"object","name":"Title","id":"p32712","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p32750","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p32702","attributes":{"selected":{"type":"object","name":"Selection","id":"p32703","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p32704"},"data":{"type":"map","entries":[["year",[2008,2012,2013,2014,2021,2022,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,40.0]],["detected",[1,1,10,1,4,2,1,2]],["evaluable",[1,1,10,1,4,2,1,5]],["window",["baseline","baseline","baseline","baseline","recent","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,10.143865699252444,8.703135093227193,9.517227179437622,9.07684386569143,8.703135093227193,9.667366891029102]]]}}},"view":{"type":"object","name":"CDSView","id":"p32751","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p32752"}}},"glyph":{"type":"object","name":"Line","id":"p32747","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p32748","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p32749","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p32756","attributes":{"data_source":{"id":"p32702"},"view":{"type":"object","name":"CDSView","id":"p32757","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p32758"}}},"glyph":{"type":"object","name":"Scatter","id":"p32753","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p32754","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p32755","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p32713","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p32727"},{"type":"object","name":"BoxZoomTool","id":"p32728","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p32729","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p32735","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p32734","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p32736","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p32737"},{"type":"object","name":"SaveTool","id":"p32738"},{"type":"object","name":"HoverTool","id":"p32759","attributes":{"renderers":[{"id":"p32756"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p32722","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p32723","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p32724"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p32725"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p32717","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p32718","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p32719"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p32720"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p32721","attributes":{"axis":{"id":"p32717"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p32726","attributes":{"dimension":1,"axis":{"id":"p32722"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p32739","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2020.5,"right":{"type":"object","name":"Node","id":"p32741","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p32742","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p32743","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p32745","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p32744","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p32746","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"5a3cbc8c-cacd-4479-8e6d-c41f2a7a7c5a","roots":{"p32705":"c95e5224-f234-47b2-bb29-42158669fd0e"},"root_ids":["p32705"]}];
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

<div id="de201b2c-ab6f-4d80-bcd6-e7a57716278f" data-root-id="p32765" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b6e43dd7-fda4-4cb4-be0e-f08ddd0023d0":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p32805","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p32806"}}},"roots":[{"type":"object","name":"Figure","id":"p32765","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p32766"},"y_range":{"type":"object","name":"DataRange1d","id":"p32767","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p32774"},"y_scale":{"type":"object","name":"LinearScale","id":"p32775"},"title":{"type":"object","name":"Title","id":"p32772","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p32801","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p32762","attributes":{"selected":{"type":"object","name":"Selection","id":"p32763","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p32764"},"data":{"type":"map","entries":[["year",[2008,2012,2013,2014,2021,2022,2025,2026]],["evaluable",[1,1,10,1,4,2,1,5]],["detected",[1,1,10,1,4,2,1,2]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p32802","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p32803"}}},"glyph":{"type":"object","name":"VBar","id":"p32798","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p32799","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p32800","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p32773","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p32786"},{"type":"object","name":"BoxZoomTool","id":"p32787","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p32788","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p32794","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p32793","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p32795","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p32796"},{"type":"object","name":"SaveTool","id":"p32797"},{"type":"object","name":"HoverTool","id":"p32804","attributes":{"renderers":[{"id":"p32801"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p32781","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p32782","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p32783"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p32784"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p32776","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p32777","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p32778"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p32779"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p32780","attributes":{"axis":{"id":"p32776"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p32785","attributes":{"dimension":1,"axis":{"id":"p32781"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b6e43dd7-fda4-4cb4-be0e-f08ddd0023d0","roots":{"p32765":"de201b2c-ab6f-4d80-bcd6-e7a57716278f"},"root_ids":["p32765"]}];
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
ITS[Title] OR ITS2[Title] OR "internal transcribed spacer"[Title] OR IGS[Title] OR "intergenic spacer"[Title] OR 28S[Title] OR "large subunit"[Title] OR "ribosomal RNA"[Title] OR rRNA[Title] OR "ribosomal DNA"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).


## What reached the statistics

196 records were screened for this assay and **25 (13%)** were evaluable, meaning both primers landed in the right orientation and size range. 171 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `truncated` | 88 |
| `no_site` | 83 |

