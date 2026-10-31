# CHYTRID_Bd_mtDNA_lineage_BdGPL_Ghosh_2021

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**BATRACHOCHYTRIUM DENDROBATIDIS — BdGPL lineage-specific mtDNA qPCR (Ghosh 2021)**

| | |
|---|---|
| Target | Batrachochytrium dendrobatidis ([taxid 109871](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=109871)) |
| Gene | mtDNA |
| Chemistry | mgb |
| Amplicon | 98 bp |
| Designed | 2021 |
| Paper | [10.1111/1755-0998.13299](https://doi.org/10.1111/1755-0998.13299) |
| Registry status | active |

!!! quote "The paper"
    Ghosh, P. N., Verster, R., Sewell, T. R., O'Hanlon, S. J., Brookes, L. M., Rieux, A., Garner, T. W. J., Weldon, C. & Fisher, M. C. Discriminating lineages of Batrachochytrium dendrobatidis using quantitative PCR. Molecular Ecology Resources 21, 1452-1459 (2021).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GAATCACAAACCTGGCAAAACA` | 22 nt |
| reverse | `TTTAAGACCTCATCCTCATAACAGATAGG` | 29 nt |
| probe | `TATAATTGAAGTATGAGGCGC` | 21 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 2 | 2 | 100.0% | 34.2% – 100.0% |
| baseline (everything earlier) | 2 | 6 | 33.3% | 9.7% – 70.0% |

Change from baseline, Newcombe interval: **-8.6% to 90.3%**. Threshold: **90.0%**.

*2 evaluable records since Oct 2024, below the minimum of 15; the detected share is 100% (34%-100%), too wide to act on*

Trend across deposit years: by record falling (p=0.379, 4 years); by footprint falling (p=0.434). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="c189cf9b-f7cb-45e4-9468-bed490e32503" data-root-id="p8757" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"0f62bae4-3e26-4200-9f5c-ebfe2545c7b8":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p8812","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p8813"}}},"roots":[{"type":"object","name":"Figure","id":"p8757","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p8759"},"y_range":{"type":"object","name":"Range1d","id":"p8766","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p8767"},"y_scale":{"type":"object","name":"LinearScale","id":"p8768"},"title":{"type":"object","name":"Title","id":"p8764","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p8802","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p8754","attributes":{"selected":{"type":"object","name":"Selection","id":"p8755","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p8756"},"data":{"type":"map","entries":[["year",[2006,2023,2024,2025]],["share",[100.0,0.0,25.0,100.0]],["detected",[1,0,1,2]],["evaluable",[1,1,4,2]],["window",["baseline","baseline","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.517227179437622,9.07684386569143]]]}}},"view":{"type":"object","name":"CDSView","id":"p8803","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8804"}}},"glyph":{"type":"object","name":"Line","id":"p8799","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p8800","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p8801","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p8808","attributes":{"data_source":{"id":"p8754"},"view":{"type":"object","name":"CDSView","id":"p8809","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8810"}}},"glyph":{"type":"object","name":"Scatter","id":"p8805","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p8806","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p8807","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p8765","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p8779"},{"type":"object","name":"BoxZoomTool","id":"p8780","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p8781","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p8787","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8786","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p8788","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p8789"},{"type":"object","name":"SaveTool","id":"p8790"},{"type":"object","name":"HoverTool","id":"p8811","attributes":{"renderers":[{"id":"p8808"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p8774","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8775","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8776"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8777"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p8769","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8770","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8771"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8772"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p8773","attributes":{"axis":{"id":"p8769"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p8778","attributes":{"dimension":1,"axis":{"id":"p8774"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p8791","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p8793","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p8794","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p8795","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p8797","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8796","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p8798","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"0f62bae4-3e26-4200-9f5c-ebfe2545c7b8","roots":{"p8757":"c189cf9b-f7cb-45e4-9468-bed490e32503"},"root_ids":["p8757"]}];
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

<div id="f7013ef0-acd7-4cd8-8d48-c8b9efc05f6c" data-root-id="p8817" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"865640dc-b3e5-484e-bc0d-9654797397b8":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p8857","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p8858"}}},"roots":[{"type":"object","name":"Figure","id":"p8817","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p8818"},"y_range":{"type":"object","name":"DataRange1d","id":"p8819","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p8826"},"y_scale":{"type":"object","name":"LinearScale","id":"p8827"},"title":{"type":"object","name":"Title","id":"p8824","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p8853","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p8814","attributes":{"selected":{"type":"object","name":"Selection","id":"p8815","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p8816"},"data":{"type":"map","entries":[["year",[2006,2023,2024,2025]],["evaluable",[1,1,4,2]],["detected",[1,0,1,2]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p8854","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p8855"}}},"glyph":{"type":"object","name":"VBar","id":"p8850","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p8851","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p8852","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p8825","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p8838"},{"type":"object","name":"BoxZoomTool","id":"p8839","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p8840","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p8846","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p8845","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p8847","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p8848"},{"type":"object","name":"SaveTool","id":"p8849"},{"type":"object","name":"HoverTool","id":"p8856","attributes":{"renderers":[{"id":"p8853"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p8833","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8834","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8835"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8836"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p8828","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p8829","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p8830"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p8831"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p8832","attributes":{"axis":{"id":"p8828"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p8837","attributes":{"dimension":1,"axis":{"id":"p8833"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"865640dc-b3e5-484e-bc0d-9654797397b8","roots":{"p8817":"f7013ef0-acd7-4cd8-8d48-c8b9efc05f6c"},"root_ids":["p8817"]}];
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

Disclosures on this entry: `scope_narrower_than_taxid`, `oligos_read_from_figure`.


## What reached the statistics

9,491 records were screened for this assay and **8 (0%)** were evaluable, meaning both primers landed in the right orientation and size range. 9,483 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 9,400 |
| `chance_anchor` | 83 |

