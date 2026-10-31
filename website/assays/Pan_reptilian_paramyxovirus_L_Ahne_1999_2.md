# Pan_reptilian_paramyxovirus_L_Ahne_1999_2

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**Pan-reptilian paramyxovirus — RdRp (L gene)**

| | |
|---|---|
| Target | Ferlavirus ([taxid 1283308](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1283308)) |
| Gene | RdRp (L gene) |
| Chemistry | conventional |
| Amplicon | 566 bp |
| Designed | 1999 |
| Paper | [10.1016/S0168-1702(99)00059-3](https://doi.org/10.1016/S0168-1702(99)00059-3) |
| Registry status | active |

!!! quote "The paper"
    Ahne W et al. 1999. Virus Res 63:65-74

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `TAGAGGCTGTTACTGCTGC` | 19 nt |
| reverse | `CATCTTGGCAAATAATCTGCC` | 21 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 3 | 6 | 50.0% | 18.8% – 81.2% |
| baseline (everything earlier) | 11 | 16 | 68.8% | 44.4% – 85.8% |

Change from baseline, Newcombe interval: **-54.4% to 20.9%**. Threshold: **90.0%**.

*6 evaluable records since Oct 2021, below the minimum of 15; the detected share is 50% (19%-81%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=0.161, 8 years); by footprint falling (p=0.873). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="dbcea227-ef16-45ae-83f1-d6f51f98c3a2" data-root-id="p28594" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"a06c69d0-5864-41d2-a241-f0dfe955b071":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p28649","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p28650"}}},"roots":[{"type":"object","name":"Figure","id":"p28594","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p28596"},"y_range":{"type":"object","name":"Range1d","id":"p28603","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p28604"},"y_scale":{"type":"object","name":"LinearScale","id":"p28605"},"title":{"type":"object","name":"Title","id":"p28601","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p28639","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p28591","attributes":{"selected":{"type":"object","name":"Selection","id":"p28592","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p28593"},"data":{"type":"map","entries":[["year",[2001,2003,2014,2017,2018,2021,2025,2026]],["share",[50.0,100.0,100.0,100.0,50.0,25.0,100.0,25.0]],["detected",[1,2,5,1,1,1,2,1]],["evaluable",[2,2,5,1,2,4,2,4]],["window",["baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,9.07684386569143,9.667366891029102,8.703135093227193,9.07684386569143,9.517227179437622,9.07684386569143,9.517227179437622]]]}}},"view":{"type":"object","name":"CDSView","id":"p28640","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p28641"}}},"glyph":{"type":"object","name":"Line","id":"p28636","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p28637","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p28638","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p28645","attributes":{"data_source":{"id":"p28591"},"view":{"type":"object","name":"CDSView","id":"p28646","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p28647"}}},"glyph":{"type":"object","name":"Scatter","id":"p28642","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p28643","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p28644","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p28602","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p28616"},{"type":"object","name":"BoxZoomTool","id":"p28617","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p28618","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p28624","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p28623","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p28625","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p28626"},{"type":"object","name":"SaveTool","id":"p28627"},{"type":"object","name":"HoverTool","id":"p28648","attributes":{"renderers":[{"id":"p28645"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p28611","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p28612","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28613"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28614"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p28606","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p28607","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28608"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28609"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p28610","attributes":{"axis":{"id":"p28606"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p28615","attributes":{"dimension":1,"axis":{"id":"p28611"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p28628","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2020.5,"right":{"type":"object","name":"Node","id":"p28630","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p28631","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p28632","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p28634","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p28633","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p28635","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"a06c69d0-5864-41d2-a241-f0dfe955b071","roots":{"p28594":"dbcea227-ef16-45ae-83f1-d6f51f98c3a2"},"root_ids":["p28594"]}];
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

<div id="a2ea44d0-c184-4190-8aec-8ab99db987b9" data-root-id="p28654" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"8254a99e-aa30-4e53-96d4-3ea841cf3c86":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p28694","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p28695"}}},"roots":[{"type":"object","name":"Figure","id":"p28654","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p28655"},"y_range":{"type":"object","name":"DataRange1d","id":"p28656","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p28663"},"y_scale":{"type":"object","name":"LinearScale","id":"p28664"},"title":{"type":"object","name":"Title","id":"p28661","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p28690","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p28651","attributes":{"selected":{"type":"object","name":"Selection","id":"p28652","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p28653"},"data":{"type":"map","entries":[["year",[2001,2003,2014,2017,2018,2021,2025,2026]],["evaluable",[2,2,5,1,2,4,2,4]],["detected",[1,2,5,1,1,1,2,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p28691","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p28692"}}},"glyph":{"type":"object","name":"VBar","id":"p28687","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p28688","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p28689","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p28662","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p28675"},{"type":"object","name":"BoxZoomTool","id":"p28676","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p28677","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p28683","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p28682","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p28684","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p28685"},{"type":"object","name":"SaveTool","id":"p28686"},{"type":"object","name":"HoverTool","id":"p28693","attributes":{"renderers":[{"id":"p28690"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p28670","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p28671","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28672"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28673"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p28665","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p28666","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p28667"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p28668"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p28669","attributes":{"axis":{"id":"p28665"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p28674","attributes":{"dimension":1,"axis":{"id":"p28670"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"8254a99e-aa30-4e53-96d4-3ea841cf3c86","roots":{"p28654":"a2ea44d0-c184-4190-8aec-8ab99db987b9"},"root_ids":["p28654"]}];
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

Disclosures on this entry: `orientation_inferred`.


## What reached the statistics

61 records were screened for this assay and **22 (36%)** were evaluable, meaning both primers landed in the right orientation and size range. 39 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 28 |
| `chance_anchor` | 8 |
| `truncated` | 3 |

