# Apicoplast_23S_LSU_Large_subunit_Molecular_2005

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**Apicoplast — 23S LSU (Large subunit)**

| | |
|---|---|
| Target | Apicomplexa ([taxid 5794](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=5794)) |
| Gene | 23S LSU (Large subunit) |
| Chemistry | conventional |
| Amplicon | 720 bp |
| Designed | 2000 |
| Paper | [10.1099/00221287-146-2-315](https://doi.org/10.1099/00221287-146-2-315) |
| Registry status | active |

!!! quote "The paper"
    Zhu G, Marchewka MJ, Keithly JS. 2000. Microbiology 146:315-321

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GCGAAATTCCTGTCGGGTAAGTCC` | 24 nt |
| reverse | `TTTYYGRTCCTCTCGTACT` | 19 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 0 | 29 | 0.0% | 0.0% – 11.7% |
| baseline (everything earlier) | 0 | 85 | 0.0% | 0.0% – 4.3% |

Change from baseline, Newcombe interval: **-4.3% to 11.7%**. Threshold: **90.0%**.

*detected share 0.0% (0%-12%) since Oct 2024, upper bound below the 90% threshold; change from baseline -4% to +12% (no measurable fall from a baseline of 0%)*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="c1584794-854d-41e3-95d3-d21938c46c16" data-root-id="p4297" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"f111d6e8-5c5c-423a-a6ee-1dca33ee51b6":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p4352","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p4353"}}},"roots":[{"type":"object","name":"Figure","id":"p4297","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p4299"},"y_range":{"type":"object","name":"Range1d","id":"p4306","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p4307"},"y_scale":{"type":"object","name":"LinearScale","id":"p4308"},"title":{"type":"object","name":"Title","id":"p4304","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p4342","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p4294","attributes":{"selected":{"type":"object","name":"Selection","id":"p4295","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p4296"},"data":{"type":"map","entries":[["year",[1997,1998,2001,2003,2006,2009,2010,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]],["detected",[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],["evaluable",[1,1,3,2,1,12,1,1,2,2,2,13,1,2,24,3,1,1,4,8,23,6]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.328625426046248,9.07684386569143,8.703135093227193,10.269703144398052,8.703135093227193,8.703135093227193,9.07684386569143,9.07684386569143,9.07684386569143,10.324834530005162,8.703135093227193,9.07684386569143,10.74264168206181,9.328625426046248,8.703135093227193,8.703135093227193,9.517227179437622,9.989711205477885,10.713966621835368,9.791719296345839]]]}}},"view":{"type":"object","name":"CDSView","id":"p4343","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4344"}}},"glyph":{"type":"object","name":"Line","id":"p4339","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p4340","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p4341","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p4348","attributes":{"data_source":{"id":"p4294"},"view":{"type":"object","name":"CDSView","id":"p4349","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4350"}}},"glyph":{"type":"object","name":"Scatter","id":"p4345","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p4346","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p4347","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p4305","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p4319"},{"type":"object","name":"BoxZoomTool","id":"p4320","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p4321","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p4327","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4326","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p4328","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p4329"},{"type":"object","name":"SaveTool","id":"p4330"},{"type":"object","name":"HoverTool","id":"p4351","attributes":{"renderers":[{"id":"p4348"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p4314","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4315","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4316"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4317"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p4309","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4310","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4311"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4312"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p4313","attributes":{"axis":{"id":"p4309"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p4318","attributes":{"dimension":1,"axis":{"id":"p4314"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p4331","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p4333","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p4334","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p4335","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p4337","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4336","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p4338","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"f111d6e8-5c5c-423a-a6ee-1dca33ee51b6","roots":{"p4297":"c1584794-854d-41e3-95d3-d21938c46c16"},"root_ids":["p4297"]}];
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

<div id="f92449d7-becc-4277-a751-7e9be2f24f28" data-root-id="p4357" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"0301d84d-90ca-409c-b3f5-958dd30a06ce":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p4397","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p4398"}}},"roots":[{"type":"object","name":"Figure","id":"p4357","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p4358"},"y_range":{"type":"object","name":"DataRange1d","id":"p4359","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p4366"},"y_scale":{"type":"object","name":"LinearScale","id":"p4367"},"title":{"type":"object","name":"Title","id":"p4364","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p4393","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p4354","attributes":{"selected":{"type":"object","name":"Selection","id":"p4355","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p4356"},"data":{"type":"map","entries":[["year",[1997,1998,2001,2003,2006,2009,2010,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,3,2,1,12,1,1,2,2,2,13,1,2,24,3,1,1,4,8,23,6]],["detected",[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p4394","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4395"}}},"glyph":{"type":"object","name":"VBar","id":"p4390","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p4391","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p4392","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p4365","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p4378"},{"type":"object","name":"BoxZoomTool","id":"p4379","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p4380","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p4386","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4385","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p4387","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p4388"},{"type":"object","name":"SaveTool","id":"p4389"},{"type":"object","name":"HoverTool","id":"p4396","attributes":{"renderers":[{"id":"p4393"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p4373","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4374","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4375"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4376"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p4368","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4369","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4370"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4371"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p4372","attributes":{"axis":{"id":"p4368"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p4377","attributes":{"dimension":1,"axis":{"id":"p4373"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"0301d84d-90ca-409c-b3f5-958dd30a06ce","roots":{"p4357":"f92449d7-becc-4277-a751-7e9be2f24f28"},"root_ids":["p4357"]}];
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
(apicoplast[Title] OR plastid[Title]) AND (23S[Title] OR "large subunit"[Title] OR LSU[Title] OR "ribosomal RNA"[Title] OR "complete genome"[Title] OR "complete sequence"[Title])
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `cross_reactive`.


## What reached the statistics

332 records were screened for this assay and **114 (34%)** were evaluable, meaning both primers landed in the right orientation and size range. 218 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 200 |
| `chance_anchor` | 15 |
| `truncated` | 3 |

