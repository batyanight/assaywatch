# PARANANNIZZIOPSIS_ITS_Lorch_2023

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**PARANANNIZZIOPSIS spp. — ITS qPCR (Lorch 2023)**

| | |
|---|---|
| Target | Paranannizziopsis ([taxid 1387564](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1387564)) |
| Gene | ITS |
| Chemistry | hydrolysis_probe |
| Amplicon | 82 bp |
| Designed | 2023 |
| Paper | [10.3389/fmicb.2023.1302586](https://doi.org/10.3389/fmicb.2023.1302586) |
| Registry status | active |

!!! quote "The paper"
    Lorch, J. M. et al. Paranannizziopsis spp. infections in wild snakes and a qPCR assay for detection of the fungus. Frontiers in Microbiology 14, 1302586 (2023).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `AGCACGGCTTGTGTGTT` | 17 nt |
| reverse | `CGCAGACACCTGGAACTC` | 18 nt |
| probe | `TGGACGGGCCTNAAATGCAGT` | 21 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 10 | 10 | 100.0% | 72.2% – 100.0% |
| baseline (everything earlier) | 20 | 20 | 100.0% | 83.9% – 100.0% |

Change from baseline, Newcombe interval: **-27.8% to 16.1%**. Threshold: **90.0%**.

*10 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (72%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="e819cf34-4e64-4d35-8e92-c8ebc6a82900" data-root-id="p22424" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b6460486-51ba-4a8f-856d-7e5bcd1069c9":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p22479","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p22480"}}},"roots":[{"type":"object","name":"Figure","id":"p22424","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p22426"},"y_range":{"type":"object","name":"Range1d","id":"p22433","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p22434"},"y_scale":{"type":"object","name":"LinearScale","id":"p22435"},"title":{"type":"object","name":"Title","id":"p22431","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p22469","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p22421","attributes":{"selected":{"type":"object","name":"Selection","id":"p22422","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p22423"},"data":{"type":"map","entries":[["year",[2013,2014,2018,2020,2022,2024,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[11,3,2,4,1,8,1]],["evaluable",[11,3,2,4,1,8,1]],["window",["baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[10.209683151927734,9.328625426046248,9.07684386569143,9.517227179437622,8.703135093227193,9.989711205477885,8.703135093227193]]]}}},"view":{"type":"object","name":"CDSView","id":"p22470","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p22471"}}},"glyph":{"type":"object","name":"Line","id":"p22466","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p22467","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p22468","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p22475","attributes":{"data_source":{"id":"p22421"},"view":{"type":"object","name":"CDSView","id":"p22476","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p22477"}}},"glyph":{"type":"object","name":"Scatter","id":"p22472","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p22473","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p22474","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p22432","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p22446"},{"type":"object","name":"BoxZoomTool","id":"p22447","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p22448","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p22454","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p22453","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p22455","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p22456"},{"type":"object","name":"SaveTool","id":"p22457"},{"type":"object","name":"HoverTool","id":"p22478","attributes":{"renderers":[{"id":"p22475"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p22441","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p22442","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p22443"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22444"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p22436","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p22437","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p22438"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22439"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p22440","attributes":{"axis":{"id":"p22436"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p22445","attributes":{"dimension":1,"axis":{"id":"p22441"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p22458","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2021.5,"right":{"type":"object","name":"Node","id":"p22460","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p22461","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p22462","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p22464","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p22463","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p22465","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b6460486-51ba-4a8f-856d-7e5bcd1069c9","roots":{"p22424":"e819cf34-4e64-4d35-8e92-c8ebc6a82900"},"root_ids":["p22424"]}];
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

<div id="d9a533cb-c455-4d51-b2ae-7ae7285d440e" data-root-id="p22484" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"9837665b-0662-4a6d-92d5-c12a7e02b683":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p22524","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p22525"}}},"roots":[{"type":"object","name":"Figure","id":"p22484","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p22485"},"y_range":{"type":"object","name":"DataRange1d","id":"p22486","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p22493"},"y_scale":{"type":"object","name":"LinearScale","id":"p22494"},"title":{"type":"object","name":"Title","id":"p22491","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p22520","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p22481","attributes":{"selected":{"type":"object","name":"Selection","id":"p22482","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p22483"},"data":{"type":"map","entries":[["year",[2013,2014,2018,2020,2022,2024,2026]],["evaluable",[11,3,2,4,1,8,1]],["detected",[11,3,2,4,1,8,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p22521","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p22522"}}},"glyph":{"type":"object","name":"VBar","id":"p22517","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p22518","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p22519","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p22492","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p22505"},{"type":"object","name":"BoxZoomTool","id":"p22506","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p22507","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p22513","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p22512","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p22514","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p22515"},{"type":"object","name":"SaveTool","id":"p22516"},{"type":"object","name":"HoverTool","id":"p22523","attributes":{"renderers":[{"id":"p22520"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p22500","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p22501","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p22502"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22503"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p22495","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p22496","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p22497"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p22498"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p22499","attributes":{"axis":{"id":"p22495"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p22504","attributes":{"dimension":1,"axis":{"id":"p22500"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"9837665b-0662-4a6d-92d5-c12a7e02b683","roots":{"p22484":"d9a533cb-c455-4d51-b2ae-7ae7285d440e"},"root_ids":["p22484"]}];
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


## What reached the statistics

131 records were screened for this assay and **30 (23%)** were evaluable, meaning both primers landed in the right orientation and size range. 101 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 101 |

