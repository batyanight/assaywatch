# MYCOPLASMA_gallisepticum_parE_Kang_2023

<span class="aw-chip aw-chip-stable">stable</span>

**MYCOPLASMA GALLISEPTICUM — parE species-level multiplex-PCR member (Kang 2023)**

| | |
|---|---|
| Target | Mycoplasmoides gallisepticum ([taxid 2096](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=2096)) |
| Gene | parE |
| Chemistry | conventional |
| Amplicon | 245 bp |
| Designed | 2023 |
| Paper | [10.3390/pathogens12010111](https://doi.org/10.3390/pathogens12010111) |
| Registry status | active |

!!! quote "The paper"
    Kang, S.-I., Lee, O.-M., Lee, H.-J., Kwon, Y.-K., Chae, M.J., Jeong, J.-Y. & Kang, M.-S. A Multiplex PCR Assay for Differential Identification of Wild-type and Vaccine Strains of Mycoplasma gallisepticum. Pathogens 12, 111 (2023).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `AGAACTAATCGAACAAGGTAAG` | 22 nt |
| reverse | `CAGCGTTTTGAATTGAGACT` | 20 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (36 months, from Oct 2023) | 27 | 27 | 100.0% | 87.5% – 100.0% |
| baseline (everything earlier) | 68 | 68 | 100.0% | 94.7% – 100.0% |

Change from baseline, Newcombe interval: **-12.5% to 5.3%**. Threshold: **90.0%**.

*detected share 100.0% (88%-100%) since Oct 2023 (window widened to 36 months to reach 15 evaluable records)*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="a8d445f5-8cb1-49c5-863c-a3aa6fd6e626" data-root-id="p18543" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"266522bd-2499-4fa5-88ee-3db3125805aa":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p18598","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p18599"}}},"roots":[{"type":"object","name":"Figure","id":"p18543","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p18545"},"y_range":{"type":"object","name":"Range1d","id":"p18552","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p18553"},"y_scale":{"type":"object","name":"LinearScale","id":"p18554"},"title":{"type":"object","name":"Title","id":"p18550","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p18588","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p18540","attributes":{"selected":{"type":"object","name":"Selection","id":"p18541","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p18542"},"data":{"type":"map","entries":[["year",[2003,2010,2012,2013,2014,2016,2017,2018,2019,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0]],["detected",[2,2,18,2,1,7,1,10,10,2,7,7,16,8,2]],["evaluable",[2,2,18,2,1,7,1,10,10,2,7,7,16,8,2]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent","recent"]],["size",[9.07684386569143,9.07684386569143,10.547770533331066,9.07684386569143,8.703135093227193,9.897626379762722,8.703135093227193,10.143865699252444,10.143865699252444,9.07684386569143,9.897626379762722,9.897626379762722,10.467343773689333,9.989711205477885,9.07684386569143]]]}}},"view":{"type":"object","name":"CDSView","id":"p18589","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p18590"}}},"glyph":{"type":"object","name":"Line","id":"p18585","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p18586","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p18587","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p18594","attributes":{"data_source":{"id":"p18540"},"view":{"type":"object","name":"CDSView","id":"p18595","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p18596"}}},"glyph":{"type":"object","name":"Scatter","id":"p18591","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p18592","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p18593","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p18551","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p18565"},{"type":"object","name":"BoxZoomTool","id":"p18566","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p18567","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p18573","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p18572","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p18574","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p18575"},{"type":"object","name":"SaveTool","id":"p18576"},{"type":"object","name":"HoverTool","id":"p18597","attributes":{"renderers":[{"id":"p18594"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p18560","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18561","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18562"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18563"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p18555","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18556","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18557"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18558"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p18559","attributes":{"axis":{"id":"p18555"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p18564","attributes":{"dimension":1,"axis":{"id":"p18560"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p18577","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2022.5,"right":{"type":"object","name":"Node","id":"p18579","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p18580","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p18581","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p18583","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p18582","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p18584","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"266522bd-2499-4fa5-88ee-3db3125805aa","roots":{"p18543":"a8d445f5-8cb1-49c5-863c-a3aa6fd6e626"},"root_ids":["p18543"]}];
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

<div id="ee8d36b9-cf22-4855-b7b0-bef1a1bf1d65" data-root-id="p18603" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"004c6935-0bdb-4a16-958e-377642e2904f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p18643","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p18644"}}},"roots":[{"type":"object","name":"Figure","id":"p18603","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p18604"},"y_range":{"type":"object","name":"DataRange1d","id":"p18605","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p18612"},"y_scale":{"type":"object","name":"LinearScale","id":"p18613"},"title":{"type":"object","name":"Title","id":"p18610","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p18639","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p18600","attributes":{"selected":{"type":"object","name":"Selection","id":"p18601","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p18602"},"data":{"type":"map","entries":[["year",[2003,2010,2012,2013,2014,2016,2017,2018,2019,2021,2022,2023,2024,2025,2026]],["evaluable",[2,2,18,2,1,7,1,10,10,2,7,7,16,8,2]],["detected",[2,2,18,2,1,7,1,10,10,2,7,7,16,8,2]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p18640","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p18641"}}},"glyph":{"type":"object","name":"VBar","id":"p18636","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p18637","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p18638","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p18611","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p18624"},{"type":"object","name":"BoxZoomTool","id":"p18625","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p18626","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p18632","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p18631","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p18633","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p18634"},{"type":"object","name":"SaveTool","id":"p18635"},{"type":"object","name":"HoverTool","id":"p18642","attributes":{"renderers":[{"id":"p18639"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p18619","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18620","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18621"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18622"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p18614","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18615","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18616"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18617"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p18618","attributes":{"axis":{"id":"p18614"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p18623","attributes":{"dimension":1,"axis":{"id":"p18619"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"004c6935-0bdb-4a16-958e-377642e2904f","roots":{"p18603":"ee8d36b9-cf22-4855-b7b0-bef1a1bf1d65"},"root_ids":["p18603"]}];
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
parE[Gene] OR parE[Title] OR "DNA topoisomerase IV subunit B"[Title] OR "complete genome"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).


## What reached the statistics

126 records were screened for this assay and **95 (75%)** were evaluable, meaning both primers landed in the right orientation and size range. 31 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 31 |

