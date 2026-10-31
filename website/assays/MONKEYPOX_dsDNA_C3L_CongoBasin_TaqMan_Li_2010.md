# MONKEYPOX_dsDNA_C3L_CongoBasin_TaqMan_Li_2010

<span class="aw-chip aw-chip-stable">stable</span>

**MONKEYPOX virus (dsDNA) — C3L Congo Basin clade TaqMan (Li 2010)**

| | |
|---|---|
| Target | Monkeypox virus ([taxid 10244](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10244)) |
| Gene | complement binding protein (C3L) |
| Chemistry | hydrolysis_probe |
| Amplicon | 100 bp |
| Designed | 2010 |
| Paper | [10.1016/j.jviromet.2010.07.012](https://doi.org/10.1016/j.jviromet.2010.07.012) |
| Registry status | active |

!!! quote "The paper"
    Li Y, Zhao H, Wilkins K, Hughes C, Damon IK. 2010. Real-time PCR assays for the specific detection of monkeypox virus West African and Congo Basin strain DNA. J Virol Methods 169:223-227

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `TGTCTACCTGGATACAGAAAGCAA` | 24 nt |
| reverse | `GGCATCTCCGTTTAATACATTGAT` | 24 nt |
| probe | `CCCATATATGCTAAATGTACCGGTACCGGA` | 30 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 852 | 866 | 98.4% | 97.3% – 99.0% |
| baseline (everything earlier) | 457 | 466 | 98.1% | 96.4% – 99.0% |

Change from baseline, Newcombe interval: **-1.1% to 2.1%**. Threshold: **90.0%**.

*detected share 98.4% (97%-99%) since Oct 2024*

Trend across deposit years: by record rising (p=0.000344, 15 years); by footprint falling (p=0.13); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="cea9936d-236c-4236-99cb-d0561cc27cb2" data-root-id="p16931" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"3ff35dc3-c442-4e91-9085-a3a39e70bac1":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p16986","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p16987"}}},"roots":[{"type":"object","name":"Figure","id":"p16931","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p16933"},"y_range":{"type":"object","name":"Range1d","id":"p16940","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p16941"},"y_scale":{"type":"object","name":"LinearScale","id":"p16942"},"title":{"type":"object","name":"Title","id":"p16938","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p16976","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p16928","attributes":{"selected":{"type":"object","name":"Selection","id":"p16929","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p16930"},"data":{"type":"map","entries":[["year",[2001,2004,2005,2008,2010,2011,2013,2014,2015,2020,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,20.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,98.75930521091811,95.6989247311828,99.11764705882354]],["detected",[5,4,2,1,1,1,2,23,6,10,1,3,398,178,674]],["evaluable",[5,4,2,1,5,1,2,23,6,10,1,3,403,186,680]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.667366891029102,9.517227179437622,9.07684386569143,8.703135093227193,9.667366891029102,8.703135093227193,9.07684386569143,10.713966621835368,9.791719296345839,10.143865699252444,8.703135093227193,9.328625426046248,12.49523744451739,12.044116328498461,12.789212317537077]]]}}},"view":{"type":"object","name":"CDSView","id":"p16977","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16978"}}},"glyph":{"type":"object","name":"Line","id":"p16973","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p16974","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p16975","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p16982","attributes":{"data_source":{"id":"p16928"},"view":{"type":"object","name":"CDSView","id":"p16983","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16984"}}},"glyph":{"type":"object","name":"Scatter","id":"p16979","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p16980","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p16981","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p16939","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p16953"},{"type":"object","name":"BoxZoomTool","id":"p16954","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p16955","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p16961","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16960","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p16962","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p16963"},{"type":"object","name":"SaveTool","id":"p16964"},{"type":"object","name":"HoverTool","id":"p16985","attributes":{"renderers":[{"id":"p16982"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p16948","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16949","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16950"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16951"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p16943","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16944","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16945"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16946"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p16947","attributes":{"axis":{"id":"p16943"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p16952","attributes":{"dimension":1,"axis":{"id":"p16948"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p16965","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p16967","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p16968","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p16969","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p16971","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16970","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p16972","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"3ff35dc3-c442-4e91-9085-a3a39e70bac1","roots":{"p16931":"cea9936d-236c-4236-99cb-d0561cc27cb2"},"root_ids":["p16931"]}];
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

<div id="f0445f6e-5fbf-4893-8a3b-5731a0dea07a" data-root-id="p16991" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"438d3e25-aebc-4114-bbbd-b675ebd45d98":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17031","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17032"}}},"roots":[{"type":"object","name":"Figure","id":"p16991","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p16992"},"y_range":{"type":"object","name":"DataRange1d","id":"p16993","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p17000"},"y_scale":{"type":"object","name":"LinearScale","id":"p17001"},"title":{"type":"object","name":"Title","id":"p16998","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17027","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p16988","attributes":{"selected":{"type":"object","name":"Selection","id":"p16989","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p16990"},"data":{"type":"map","entries":[["year",[2001,2004,2005,2008,2010,2011,2013,2014,2015,2020,2022,2023,2024,2025,2026]],["evaluable",[5,4,2,1,5,1,2,23,6,10,1,3,403,186,680]],["detected",[5,4,2,1,1,1,2,23,6,10,1,3,398,178,674]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p17028","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17029"}}},"glyph":{"type":"object","name":"VBar","id":"p17024","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p17025","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p17026","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p16999","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17012"},{"type":"object","name":"BoxZoomTool","id":"p17013","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17014","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17020","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17019","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17021","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17022"},{"type":"object","name":"SaveTool","id":"p17023"},{"type":"object","name":"HoverTool","id":"p17030","attributes":{"renderers":[{"id":"p17027"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p17007","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17008","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17009"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17010"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17002","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17003","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17004"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17005"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17006","attributes":{"axis":{"id":"p17002"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17011","attributes":{"dimension":1,"axis":{"id":"p17007"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"438d3e25-aebc-4114-bbbd-b675ebd45d98","roots":{"p16991":"f0445f6e-5fbf-4893-8a3b-5731a0dea07a"},"root_ids":["p16991"]}];
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


## By lineage

A single pooled percentage hides the clade you may actually care about:
published misses are nearly always specific to one lineage, and a clade that is
5% of deposits can be 100% of the cases in one region. Lineages with too few
records to say anything are left out.

<div id="f642c496-8a44-416f-b281-b53c0ca1e810" data-root-id="p17036" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"a161cf0a-ed3b-4000-86e4-0efe331bd6fe":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p17085","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p17086"}}},"roots":[{"type":"object","name":"Figure","id":"p17036","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p17045","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p17046","attributes":{"factors":["Orthopoxvirus monkeypox (3431483)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p17047"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p17048"},"title":{"type":"object","name":"Title","id":"p17043","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p17080","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p17033","attributes":{"selected":{"type":"object","name":"Selection","id":"p17034","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p17035"},"data":{"type":"map","entries":[["y",["Orthopoxvirus monkeypox (3431483)"]],["share",[99.76580796252928]],["lo",[99.15015556940155]],["hi",[99.9357525852971]],["n",[854]],["det",[852]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p17081","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p17082"}}},"glyph":{"type":"object","name":"Scatter","id":"p17077","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p17078","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p17079","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p17044","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p17059"},{"type":"object","name":"BoxZoomTool","id":"p17060","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p17061","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p17067","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p17066","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p17068","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p17069"},{"type":"object","name":"SaveTool","id":"p17070"},{"type":"object","name":"HoverTool","id":"p17084","attributes":{"renderers":[{"id":"p17080"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p17054","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p17055"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p17056"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17057"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p17049","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p17050","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p17051"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p17052"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p17053","attributes":{"axis":{"id":"p17049"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p17058","attributes":{"dimension":1,"axis":{"id":"p17054"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p17071","attributes":{"source":{"id":"p17033"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p17083","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"a161cf0a-ed3b-4000-86e4-0efe331bd6fe","roots":{"p17036":"f642c496-8a44-416f-b281-b53c0ca1e810"},"root_ids":["p17036"]}];
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

Disclosures on this entry: `amplicon_measured_not_published`, `scope_narrower_than_taxid`.


## What reached the statistics

14,204 records were screened for this assay and **1,332 (9%)** were evaluable, meaning both primers landed in the right orientation and size range. 12,872 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 12,870 |

