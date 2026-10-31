# MONKEYPOX_dsDNA_N3R_MGB_Kulesh_2004

<span class="aw-chip aw-chip-declining">declining</span>

**MONKEYPOX virus (dsDNA) — N3R MGB TaqMan (Kulesh 2004)**

| | |
|---|---|
| Target | Monkeypox virus ([taxid 10244](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10244)) |
| Gene | N3R |
| Chemistry | mgb |
| Amplicon | 139 bp |
| Designed | 2004 |
| Paper | [10.1038/labinvest.3700143](https://doi.org/10.1038/labinvest.3700143) |
| Registry status | active |

!!! quote "The paper"
    Kulesh DA, Loveless BM, Norwood D, Garrison J, Whitehouse CA, Hartmann C, Mucker E, Miller D, Wasieloski LP Jr, Huggins J, Huhn G, Miser LL, Imig C, Martinez M, Larsen T, Rossi CA, Ludwig GV. 2004. Monkeypox virus detection in rodents using real-time 3'-minor groove binder TaqMan assays on the Roche LightCycler. Lab Invest 84:1200-1208

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `AACAACCGTCCTACAATTAAACAACA` | 26 nt |
| reverse | `CGCTATCGAACCATTTTTGTAGTCT` | 25 nt |
| probe | `TATAACGGCGAAGAATATACT` | 21 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 637 | 4,550 | 14.0% | 13.0% – 15.0% |
| baseline (everything earlier) | 558 | 8,255 | 6.8% | 6.2% – 7.3% |

Change from baseline, Newcombe interval: **6.1% to 8.4%**. Threshold: **90.0%**.

*pooled share 14.0% has low coverage, but lineage Orthopoxvirus monkeypox (3431483) (2430 records) detects 26.2% (24.5%-28.0%); lineage verdict overrides to declining*

Trend across deposit years: by record rising (p=9.64e-29, 16 years); by footprint falling (p=0.0576); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="b0069b19-ffcb-4969-8873-e8d71c4a99af" data-root-id="p18073" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"db735635-a82a-4144-aa4d-c4d95ad1f2c2":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p18128","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p18129"}}},"roots":[{"type":"object","name":"Figure","id":"p18073","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p18075"},"y_range":{"type":"object","name":"Range1d","id":"p18082","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p18083"},"y_scale":{"type":"object","name":"LinearScale","id":"p18084"},"title":{"type":"object","name":"Title","id":"p18080","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p18118","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p18070","attributes":{"selected":{"type":"object","name":"Selection","id":"p18071","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p18072"},"data":{"type":"map","entries":[["year",[2001,2004,2005,2010,2011,2013,2014,2015,2018,2019,2020,2022,2023,2024,2025,2026]],["share",[100.0,66.66666666666666,100.0,20.0,100.0,50.0,100.0,90.9090909090909,0.0,0.0,68.57142857142857,0.05943536404160475,0.06770480704129993,23.618581907090462,15.843857634902411,13.813005001923816]],["detected",[2,2,7,1,2,1,24,10,0,0,24,2,2,483,276,359]],["evaluable",[2,3,7,5,2,2,24,11,1,8,35,3365,2954,2045,1742,2599]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,9.328625426046248,9.897626379762722,9.667366891029102,9.07684386569143,9.07684386569143,10.74264168206181,10.209683151927734,8.703135093227193,9.989711205477885,10.994220569835573,13.638508015271462,13.571846439030026,13.381360254533291,13.29720518770748,13.50591898404278]]]}}},"view":{"type":"object","name":"CDSView","id":"p18119","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p18120"}}},"glyph":{"type":"object","name":"Line","id":"p18115","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p18116","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p18117","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p18124","attributes":{"data_source":{"id":"p18070"},"view":{"type":"object","name":"CDSView","id":"p18125","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p18126"}}},"glyph":{"type":"object","name":"Scatter","id":"p18121","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p18122","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p18123","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p18081","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p18095"},{"type":"object","name":"BoxZoomTool","id":"p18096","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p18097","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p18103","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p18102","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p18104","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p18105"},{"type":"object","name":"SaveTool","id":"p18106"},{"type":"object","name":"HoverTool","id":"p18127","attributes":{"renderers":[{"id":"p18124"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p18090","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18091","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18092"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18093"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p18085","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18086","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18087"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18088"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p18089","attributes":{"axis":{"id":"p18085"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p18094","attributes":{"dimension":1,"axis":{"id":"p18090"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p18107","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p18109","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p18110","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p18111","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p18113","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p18112","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p18114","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"db735635-a82a-4144-aa4d-c4d95ad1f2c2","roots":{"p18073":"b0069b19-ffcb-4969-8873-e8d71c4a99af"},"root_ids":["p18073"]}];
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

<div id="fac32c5e-b2f5-463b-879f-fbfad9349386" data-root-id="p18133" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"89f71c12-cce8-45cc-bbdb-06dc38358ba9":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p18173","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p18174"}}},"roots":[{"type":"object","name":"Figure","id":"p18133","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p18134"},"y_range":{"type":"object","name":"DataRange1d","id":"p18135","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p18142"},"y_scale":{"type":"object","name":"LinearScale","id":"p18143"},"title":{"type":"object","name":"Title","id":"p18140","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p18169","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p18130","attributes":{"selected":{"type":"object","name":"Selection","id":"p18131","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p18132"},"data":{"type":"map","entries":[["year",[2001,2004,2005,2010,2011,2013,2014,2015,2018,2019,2020,2022,2023,2024,2025,2026]],["evaluable",[2,3,7,5,2,2,24,11,1,8,35,3365,2954,2045,1742,2599]],["detected",[2,2,7,1,2,1,24,10,0,0,24,2,2,483,276,359]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p18170","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p18171"}}},"glyph":{"type":"object","name":"VBar","id":"p18166","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p18167","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p18168","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p18141","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p18154"},{"type":"object","name":"BoxZoomTool","id":"p18155","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p18156","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p18162","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p18161","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p18163","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p18164"},{"type":"object","name":"SaveTool","id":"p18165"},{"type":"object","name":"HoverTool","id":"p18172","attributes":{"renderers":[{"id":"p18169"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p18149","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18150","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18151"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18152"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p18144","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18145","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18146"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18147"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p18148","attributes":{"axis":{"id":"p18144"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p18153","attributes":{"dimension":1,"axis":{"id":"p18149"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"89f71c12-cce8-45cc-bbdb-06dc38358ba9","roots":{"p18133":"fac32c5e-b2f5-463b-879f-fbfad9349386"},"root_ids":["p18133"]}];
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

<div id="b040e487-a7c8-4468-9233-a85ad41c4001" data-root-id="p18178" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"82d2a955-8bea-4d2f-88e8-a7fc261edc4f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p18220","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p18221"}}},"roots":[{"type":"object","name":"Figure","id":"p18178","attributes":{"height":112,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p18180"},"y_range":{"type":"object","name":"FactorRange","id":"p18187","attributes":{"factors":["probe"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p18188"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p18189"},"title":{"type":"object","name":"Title","id":"p18185","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p18215","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p18175","attributes":{"selected":{"type":"object","name":"Selection","id":"p18176","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p18177"},"data":{"type":"map","entries":[["x",[-10]],["y",["probe"]],["alpha",[1.0]],["pos",[10]],["base",["A"]],["n",[8810]],["det_with",["0% of 8810"]],["det_without",["99% of 1202"]],["subs",["A&gt;C 8810"]],["zone",["no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p18216","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p18217"}}},"glyph":{"type":"object","name":"Rect","id":"p18212","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p18213","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p18214","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p18186","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p18200"},{"type":"object","name":"BoxZoomTool","id":"p18201","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p18202","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p18208","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p18207","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p18209","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p18210"},{"type":"object","name":"SaveTool","id":"p18211"},{"type":"object","name":"HoverTool","id":"p18218","attributes":{"renderers":[{"id":"p18215"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p18195","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p18196"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p18197"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18198"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p18190","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p18219","attributes":{"ticks":[-10],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18192"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-10,"10"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p18193"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p18194","attributes":{"axis":{"id":"p18190"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p18199","attributes":{"dimension":1,"axis":{"id":"p18195"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"82d2a955-8bea-4d2f-88e8-a7fc261edc4f","roots":{"p18178":"b040e487-a7c8-4468-9233-a85ad41c4001"},"root_ids":["p18178"]}];
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

<div id="ca0b03fe-0a96-49f0-a1ac-513ccf1c998e" data-root-id="p18225" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"119d5550-8fd3-4424-8132-c2b06412290a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p18274","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p18275"}}},"roots":[{"type":"object","name":"Figure","id":"p18225","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p18234","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p18235","attributes":{"factors":["Orthopoxvirus monkeypox (3431483)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p18236"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p18237"},"title":{"type":"object","name":"Title","id":"p18232","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p18269","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p18222","attributes":{"selected":{"type":"object","name":"Selection","id":"p18223","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p18224"},"data":{"type":"map","entries":[["y",["Orthopoxvirus monkeypox (3431483)"]],["share",[26.213991769547324]],["lo",[24.50387921932059]],["hi",[27.999189712698758]],["n",[2430]],["det",[637]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p18270","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p18271"}}},"glyph":{"type":"object","name":"Scatter","id":"p18266","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p18267","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p18268","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p18233","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p18248"},{"type":"object","name":"BoxZoomTool","id":"p18249","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p18250","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p18256","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p18255","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p18257","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p18258"},{"type":"object","name":"SaveTool","id":"p18259"},{"type":"object","name":"HoverTool","id":"p18273","attributes":{"renderers":[{"id":"p18269"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p18243","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p18244"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p18245"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18246"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p18238","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p18239","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p18240"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p18241"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p18242","attributes":{"axis":{"id":"p18238"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p18247","attributes":{"dimension":1,"axis":{"id":"p18243"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p18260","attributes":{"source":{"id":"p18222"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p18272","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"119d5550-8fd3-4424-8132-c2b06412290a","roots":{"p18225":"ca0b03fe-0a96-49f0-a1ac-513ccf1c998e"},"root_ids":["p18225"]}];
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

Disclosures on this entry: `primer_site_polymorphic`.


## What reached the statistics

14,204 records were screened for this assay and **12,805 (90%)** were evaluable, meaning both primers landed in the right orientation and size range. 1,399 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 747 |
| `no_pair` | 618 |
| `truncated` | 21 |

