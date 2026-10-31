# BOCAVIRUS_ssDNA_NS1_gene_round1

<span class="aw-chip aw-chip-stable">stable</span>

**BOCAVIRUS (ssDNA) — NS1 gene**

| | |
|---|---|
| Target | Bocaparvovirus ([taxid 1507401](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1507401)) |
| Gene | NS1 gene |
| Chemistry | conventional |
| Amplicon | 293 bp |
| Designed | 2010 |
| Paper | [10.1371/journal.pone.0011948](https://doi.org/10.1371/journal.pone.0011948) |
| Registry status | active |

!!! quote "The paper"
    Kapoor A et al. 2010. PLoS ONE 5:e11948 (PANBOV primers)

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `TAATGCAYCARGAYTGGGTNGANCC` | 25 nt |
| reverse | `GTACAGTCRTAYTCRTTRAARCACCA` | 26 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 395 | 425 | 92.9% | 90.1% – 95.0% |
| baseline (everything earlier) | 1,032 | 1,625 | 63.5% | 61.1% – 65.8% |

Change from baseline, Newcombe interval: **25.8% to 32.6%**. Threshold: **90.0%**.

*detected share 92.9% (90%-95%) since Oct 2024*

Trend across deposit years: by record falling (p=0.278, 22 years); by footprint falling (p=2.26e-07). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="eb5e07e2-6f5c-4f0f-807e-4bcef83e4a46" data-root-id="p4598" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"e0a838e3-12aa-44ba-9a5a-1aa62749bcd9":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p4653","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p4654"}}},"roots":[{"type":"object","name":"Figure","id":"p4598","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p4600"},"y_range":{"type":"object","name":"Range1d","id":"p4607","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p4608"},"y_scale":{"type":"object","name":"LinearScale","id":"p4609"},"title":{"type":"object","name":"Title","id":"p4605","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p4643","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p4595","attributes":{"selected":{"type":"object","name":"Selection","id":"p4596","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p4597"},"data":{"type":"map","entries":[["year",[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,98.80952380952381,80.3921568627451,75.0,77.41935483870968,64.40677966101694,87.71929824561403,46.25,34.69387755102041,10.483870967741936,5.660377358490567,81.81818181818183,51.515151515151516,51.0,11.11111111111111,74.18032786885246,78.57142857142857,95.38043478260869]],["detected",[3,4,33,16,127,83,41,54,48,38,50,37,17,13,6,27,17,51,5,362,44,351]],["evaluable",[3,4,33,16,127,84,51,72,62,59,57,80,49,124,106,33,33,100,45,488,56,368]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.328625426046248,9.517227179437622,10.955310988645032,10.467343773689333,11.813639954139079,11.557772674175059,11.24015070195139,11.460677957646856,11.365614964623912,11.333893523413357,11.311780786273989,11.527140521415502,11.214271124597754,11.79901985025613,11.702562521586975,10.955310988645032,10.955310988645032,11.666489159086629,11.15897945775324,12.603786830104596,11.300413928944284,12.44328645938354]]]}}},"view":{"type":"object","name":"CDSView","id":"p4644","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4645"}}},"glyph":{"type":"object","name":"Line","id":"p4640","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p4641","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p4642","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p4649","attributes":{"data_source":{"id":"p4595"},"view":{"type":"object","name":"CDSView","id":"p4650","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4651"}}},"glyph":{"type":"object","name":"Scatter","id":"p4646","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p4647","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p4648","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p4606","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p4620"},{"type":"object","name":"BoxZoomTool","id":"p4621","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p4622","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p4628","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4627","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p4629","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p4630"},{"type":"object","name":"SaveTool","id":"p4631"},{"type":"object","name":"HoverTool","id":"p4652","attributes":{"renderers":[{"id":"p4649"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p4615","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4616","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4617"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4618"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p4610","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4611","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4612"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4613"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p4614","attributes":{"axis":{"id":"p4610"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p4619","attributes":{"dimension":1,"axis":{"id":"p4615"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p4632","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p4634","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p4635","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p4636","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p4638","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4637","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p4639","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"e0a838e3-12aa-44ba-9a5a-1aa62749bcd9","roots":{"p4598":"eb5e07e2-6f5c-4f0f-807e-4bcef83e4a46"},"root_ids":["p4598"]}];
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

<div id="ec643f58-f741-419b-a34b-5d15a29814e6" data-root-id="p4658" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"0138d4f0-c7ce-4bfd-b45b-0eb29f21aaa5":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p4698","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p4699"}}},"roots":[{"type":"object","name":"Figure","id":"p4658","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p4659"},"y_range":{"type":"object","name":"DataRange1d","id":"p4660","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p4667"},"y_scale":{"type":"object","name":"LinearScale","id":"p4668"},"title":{"type":"object","name":"Title","id":"p4665","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p4694","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p4655","attributes":{"selected":{"type":"object","name":"Selection","id":"p4656","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p4657"},"data":{"type":"map","entries":[["year",[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[3,4,33,16,127,84,51,72,62,59,57,80,49,124,106,33,33,100,45,488,56,368]],["detected",[3,4,33,16,127,83,41,54,48,38,50,37,17,13,6,27,17,51,5,362,44,351]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p4695","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4696"}}},"glyph":{"type":"object","name":"VBar","id":"p4691","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p4692","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p4693","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p4666","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p4679"},{"type":"object","name":"BoxZoomTool","id":"p4680","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p4681","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p4687","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4686","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p4688","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p4689"},{"type":"object","name":"SaveTool","id":"p4690"},{"type":"object","name":"HoverTool","id":"p4697","attributes":{"renderers":[{"id":"p4694"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p4674","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4675","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4676"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4677"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p4669","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4670","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4671"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4672"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p4673","attributes":{"axis":{"id":"p4669"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p4678","attributes":{"dimension":1,"axis":{"id":"p4674"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"0138d4f0-c7ce-4bfd-b45b-0eb29f21aaa5","roots":{"p4658":"ec643f58-f741-419b-a34b-5d15a29814e6"},"root_ids":["p4658"]}];
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

<div id="cd8d1677-8dcc-4d73-b02d-5c6d7f568178" data-root-id="p4703" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"aab30e16-12fd-47b1-bbe2-6decb5f8eb1f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p4745","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p4746"}}},"roots":[{"type":"object","name":"Figure","id":"p4703","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p4705"},"y_range":{"type":"object","name":"FactorRange","id":"p4712","attributes":{"factors":["reverse"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p4713"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p4714"},"title":{"type":"object","name":"Title","id":"p4710","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p4740","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p4700","attributes":{"selected":{"type":"object","name":"Selection","id":"p4701","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p4702"},"data":{"type":"map","entries":[["x",[-21]],["y",["reverse"]],["alpha",[0.35897560975609755]],["pos",[21]],["base",["G"]],["n",[126]],["det_with",["96% of 126"]],["det_without",["100% of 1311"]],["subs",["G&gt;T 117, G&gt;C 5, G&gt;A 4"]],["zone",["no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p4741","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4742"}}},"glyph":{"type":"object","name":"Rect","id":"p4737","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p4738","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p4739","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p4711","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p4725"},{"type":"object","name":"BoxZoomTool","id":"p4726","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p4727","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p4733","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4732","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p4734","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p4735"},{"type":"object","name":"SaveTool","id":"p4736"},{"type":"object","name":"HoverTool","id":"p4743","attributes":{"renderers":[{"id":"p4740"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p4720","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p4721"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p4722"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4723"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p4715","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p4744","attributes":{"ticks":[-21],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4717"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-21,"21"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p4718"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p4719","attributes":{"axis":{"id":"p4715"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p4724","attributes":{"dimension":1,"axis":{"id":"p4720"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"aab30e16-12fd-47b1-bbe2-6decb5f8eb1f","roots":{"p4703":"cd8d1677-8dcc-4d73-b02d-5c6d7f568178"},"root_ids":["p4703"]}];
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


## By lineage

A single pooled percentage hides the clade you may actually care about:
published misses are nearly always specific to one lineage, and a clade that is
5% of deposits can be 100% of the cases in one region. Lineages with too few
records to say anything are left out.

<div id="eacb4816-fe94-44df-aa15-e1aea0cf3525" data-root-id="p4750" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"01d3e6bc-8d17-47d1-8c2e-f201b3f583ae":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p4799","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p4800"}}},"roots":[{"type":"object","name":"Figure","id":"p4750","attributes":{"height":132,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p4759","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p4760","attributes":{"factors":["Bocaparvovirus primate1 (3052040)","Human bocavirus (329641)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p4761"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p4762"},"title":{"type":"object","name":"Title","id":"p4757","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p4794","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p4747","attributes":{"selected":{"type":"object","name":"Selection","id":"p4748","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p4749"},"data":{"type":"map","entries":[["y",["Bocaparvovirus primate1 (3052040)","Human bocavirus (329641)"]],["share",[100.0,100.0]],["lo",[95.67605161859485,98.70588871380849]],["hi",[100.0,100.0]],["n",[85,293]],["det",[85,293]],["colour",["#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p4795","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p4796"}}},"glyph":{"type":"object","name":"Scatter","id":"p4791","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p4792","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p4793","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p4758","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p4773"},{"type":"object","name":"BoxZoomTool","id":"p4774","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p4775","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p4781","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p4780","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p4782","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p4783"},{"type":"object","name":"SaveTool","id":"p4784"},{"type":"object","name":"HoverTool","id":"p4798","attributes":{"renderers":[{"id":"p4794"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p4768","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p4769"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p4770"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4771"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p4763","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p4764","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p4765"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p4766"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p4767","attributes":{"axis":{"id":"p4763"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p4772","attributes":{"dimension":1,"axis":{"id":"p4768"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p4785","attributes":{"source":{"id":"p4747"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p4797","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"01d3e6bc-8d17-47d1-8c2e-f201b3f583ae","roots":{"p4750":"eacb4816-fe94-44df-aa15-e1aea0cf3525"},"root_ids":["p4750"]}];
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


## Scope — what this assay is judged against

This entry declares no `scope_taxids`, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower set than its taxid covers, that reads as low coverage rather than as drift — see [scoping](../scoping.md).


## What reached the statistics

7,497 records were screened for this assay and **2,050 (27%)** were evaluable, meaning both primers landed in the right orientation and size range. 5,447 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 4,948 |
| `truncated` | 370 |
| `chance_anchor` | 129 |

