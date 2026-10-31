# CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme

<span class="aw-chip aw-chip-declining">declining</span>

**CORONAVIRUS (ssRNA) — RNA-dependent RNA polymerase**

| | |
|---|---|
| Target | Coronaviridae ([taxid 11118](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11118)) |
| Gene | RNA-dependent RNA polymerase |
| Chemistry | conventional |
| Amplicon | 440 bp |
| Designed | — |
| Paper | [10.3201/eid1608.100208](https://doi.org/10.3201/eid1608.100208) |
| Registry status | draft |

!!! quote "The paper"
    Watanabe S et al. 2010. Emerg Infect Dis 16:1217-1223 (pan-CoV RdRp consensus pair, made degenerate by the PREDICT panel)

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GGTTGGGAYTAYCCHAARTGTGA` | 23 nt |
| reverse | `CCATCATCASWYRGAATCATCATA` | 24 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 725 | 1,749 | 41.5% | 39.2% – 43.8% |
| baseline (everything earlier) | 2,992 | 6,250 | 47.9% | 46.6% – 49.1% |

Change from baseline, Newcombe interval: **-9.0% to -3.8%**. Threshold: **90.0%**.

*pooled share 41.5% has low coverage, but lineage Bat coronavirus (1508220) (172 records) detects only 25.6% (19.6%-32.6%), down from 75.6% on 176 earlier records; lineage verdict overrides to declining*

Trend across deposit years: by record rising (p=0.1, 30 years); by footprint falling (p=0.796); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="cfa37613-cbf4-4916-9ab2-fe57809f454e" data-root-id="p10044" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"3a9c6d8f-e410-487b-95c2-4487c89fc796":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p10099","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p10100"}}},"roots":[{"type":"object","name":"Figure","id":"p10044","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p10046"},"y_range":{"type":"object","name":"Range1d","id":"p10053","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p10054"},"y_scale":{"type":"object","name":"LinearScale","id":"p10055"},"title":{"type":"object","name":"Title","id":"p10051","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p10089","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p10041","attributes":{"selected":{"type":"object","name":"Selection","id":"p10042","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p10043"},"data":{"type":"map","entries":[["year",[1993,1997,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[50.0,100.0,100.0,100.0,71.42857142857143,100.0,1.639344262295082,6.578947368421052,15.625,73.97260273972603,65.78947368421053,50.0,45.94594594594595,43.75,16.27906976744186,38.0,46.411483253588514,36.93693693693694,63.731656184486376,34.146341463414636,55.03048780487805,47.09976798143852,42.17252396166134,60.56644880174292,41.57549234135667,45.69138276553106,48.99034240561896,57.692307692307686,32.88659793814433,49.682539682539684]],["detected",[1,2,1,5,5,1,1,5,5,54,25,14,51,21,14,38,97,123,304,98,361,203,132,278,190,228,558,270,319,313]],["evaluable",[2,2,1,5,7,1,61,76,32,73,38,28,111,48,86,100,209,333,477,287,656,431,313,459,457,499,1139,468,970,630]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,9.07684386569143,8.703135093227193,9.667366891029102,9.897626379762722,8.703135093227193,11.355225445040746,11.49483773413666,10.934913263353746,11.469403343404682,11.048392086352559,10.846014908695619,11.731005129236527,11.200908608240482,11.57251312716787,11.666489159086629,12.113478061001079,12.385822375811781,12.590917443879025,12.299721081515337,12.76929548324722,12.533472277736628,12.350039636377504,12.56916641051034,12.566694149501004,12.61635326453851,13.070879866397565,12.580152455356703,12.984011255387292,12.746831997172382]]]}}},"view":{"type":"object","name":"CDSView","id":"p10090","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p10091"}}},"glyph":{"type":"object","name":"Line","id":"p10086","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p10087","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p10088","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p10095","attributes":{"data_source":{"id":"p10041"},"view":{"type":"object","name":"CDSView","id":"p10096","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p10097"}}},"glyph":{"type":"object","name":"Scatter","id":"p10092","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p10093","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p10094","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p10052","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p10066"},{"type":"object","name":"BoxZoomTool","id":"p10067","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p10068","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p10074","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p10073","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p10075","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p10076"},{"type":"object","name":"SaveTool","id":"p10077"},{"type":"object","name":"HoverTool","id":"p10098","attributes":{"renderers":[{"id":"p10095"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p10061","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p10062","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p10063"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p10064"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p10056","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p10057","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p10058"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p10059"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p10060","attributes":{"axis":{"id":"p10056"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p10065","attributes":{"dimension":1,"axis":{"id":"p10061"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p10078","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p10080","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p10081","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p10082","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p10084","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p10083","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p10085","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"3a9c6d8f-e410-487b-95c2-4487c89fc796","roots":{"p10044":"cfa37613-cbf4-4916-9ab2-fe57809f454e"},"root_ids":["p10044"]}];
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

<div id="ae85e811-ae6c-4cf6-852b-272858bc7ccd" data-root-id="p10104" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"8814a0c3-82fa-49d5-8364-1c7d49722b64":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p10144","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p10145"}}},"roots":[{"type":"object","name":"Figure","id":"p10104","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p10105"},"y_range":{"type":"object","name":"DataRange1d","id":"p10106","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p10113"},"y_scale":{"type":"object","name":"LinearScale","id":"p10114"},"title":{"type":"object","name":"Title","id":"p10111","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p10140","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p10101","attributes":{"selected":{"type":"object","name":"Selection","id":"p10102","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p10103"},"data":{"type":"map","entries":[["year",[1993,1997,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[2,2,1,5,7,1,61,76,32,73,38,28,111,48,86,100,209,333,477,287,656,431,313,459,457,499,1139,468,970,630]],["detected",[1,2,1,5,5,1,1,5,5,54,25,14,51,21,14,38,97,123,304,98,361,203,132,278,190,228,558,270,319,313]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p10141","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p10142"}}},"glyph":{"type":"object","name":"VBar","id":"p10137","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p10138","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p10139","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p10112","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p10125"},{"type":"object","name":"BoxZoomTool","id":"p10126","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p10127","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p10133","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p10132","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p10134","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p10135"},{"type":"object","name":"SaveTool","id":"p10136"},{"type":"object","name":"HoverTool","id":"p10143","attributes":{"renderers":[{"id":"p10140"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p10120","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p10121","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p10122"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p10123"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p10115","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p10116","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p10117"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p10118"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p10119","attributes":{"axis":{"id":"p10115"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p10124","attributes":{"dimension":1,"axis":{"id":"p10120"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"8814a0c3-82fa-49d5-8364-1c7d49722b64","roots":{"p10104":"ae85e811-ae6c-4cf6-852b-272858bc7ccd"},"root_ids":["p10104"]}];
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

<div id="db1c926d-530e-418b-a633-b4e75c156fac" data-root-id="p10149" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"0322eed4-9db6-43e8-9d3b-8c4c03362f43":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p10191","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p10192"}}},"roots":[{"type":"object","name":"Figure","id":"p10149","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p10151"},"y_range":{"type":"object","name":"FactorRange","id":"p10158","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p10159"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p10160"},"title":{"type":"object","name":"Title","id":"p10156","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p10186","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p10146","attributes":{"selected":{"type":"object","name":"Selection","id":"p10147","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p10148"},"data":{"type":"map","entries":[["x",[-1,-2,-4,-24,-13,-19,-3,-10,-9,-16,-8,-22,-11,-21]],["y",["reverse","reverse","reverse","reverse","reverse","reverse","forward","reverse","forward","reverse","reverse","reverse","reverse","forward"]],["alpha",[1.0,0.832635329416177,0.596305788223528,0.4602887860982623,1.0,0.41608326040755095,0.8470871358919865,1.0,0.18485435679459933,0.4466870858857357,0.15892611576447055,0.8135079384923115,1.0,0.6855669458682335]],["pos",[1,2,4,24,13,19,3,10,9,16,8,22,11,21]],["base",["A","T","C","C","Y","A","T","A","H","A","T","A","G","T"]],["n",[3917,1606,1050,730,2884,626,1640,2939,82,698,21,1561,3697,1260]],["det_with",["0% of 3917","4% of 1606","1% of 1050","5% of 730","20% of 2884","20% of 626","29% of 1640","38% of 2939","40% of 82","46% of 698","62% of 21","59% of 1561","57% of 3697","69% of 1260"]],["det_without",["93% of 4013","58% of 6324","54% of 6880","51% of 7200","62% of 5046","49% of 7304","51% of 6290","52% of 4991","47% of 7848","47% of 7232","47% of 7909","44% of 6369","38% of 4233","43% of 6670"]],["subs",["A&gt;T 2914, A&gt;G 943, A&gt;C 60","T&gt;A 1037, T&gt;G 569","C&gt;T 520, C&gt;A 378, C&gt;G 152","C&gt;G 728, C&gt;T 2","Y&gt;A 2435, Y&gt;G 449","A&gt;G 623, A&gt;C 2, A&gt;T 1","T&gt;C 1640","A&gt;T 1668, A&gt;G 1271","H&gt;G 82","A&gt;T 389, A&gt;G 218, A&gt;C 89, A&gt;Y 1","T&gt;C 20, T&gt;A 1","A&gt;G 1559, A&gt;T 2","G&gt;A 3696, G&gt;C 1","T&gt;A 850, T&gt;C 337, T&gt;G 73"]],["zone",["yes","yes","yes","no","no","no","yes","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p10187","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p10188"}}},"glyph":{"type":"object","name":"Rect","id":"p10183","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p10184","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p10185","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p10157","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p10171"},{"type":"object","name":"BoxZoomTool","id":"p10172","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p10173","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p10179","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p10178","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p10180","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p10181"},{"type":"object","name":"SaveTool","id":"p10182"},{"type":"object","name":"HoverTool","id":"p10189","attributes":{"renderers":[{"id":"p10186"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p10166","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p10167"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p10168"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p10169"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p10161","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p10190","attributes":{"ticks":[-24,-22,-21,-19,-16,-13,-11,-10,-9,-8,-4,-3,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p10163"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-1,"1"],[-2,"2"],[-4,"4"],[-24,"24"],[-13,"13"],[-19,"19"],[-3,"3"],[-10,"10"],[-9,"9"],[-16,"16"],[-8,"8"],[-22,"22"],[-11,"11"],[-21,"21"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p10164"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p10165","attributes":{"axis":{"id":"p10161"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p10170","attributes":{"dimension":1,"axis":{"id":"p10166"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"0322eed4-9db6-43e8-9d3b-8c4c03362f43","roots":{"p10149":"db1c926d-530e-418b-a633-b4e75c156fac"},"root_ids":["p10149"]}];
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

<div id="c3874755-8665-469f-96dd-edeb04cb0d93" data-root-id="p10196" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"6f402382-5331-482c-a408-6c6df9740b18":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p10245","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p10246"}}},"roots":[{"type":"object","name":"Figure","id":"p10196","attributes":{"height":392,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p10205","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p10206","attributes":{"factors":["Alphacoronavirus amsterdamense (3433809)","Alphacoronavirus porci (3433789)","Deltacoronavirus suis (3433742)","Gammacoronavirus galli (3433766)","Bat coronavirus (1508220)","Betacoronavirus sp. (1928434)","Alphacoronavirus sp. (1906673)","Alphacoronavirus suis (3433814)","Alphacoronavirus chicagoense (3433756)","Betacoronavirus cameli (3433633)","Betacoronavirus gravedinis (3433757)","Betacoronavirus hongkongense (3433758)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p10207"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p10208"},"title":{"type":"object","name":"Title","id":"p10203","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p10240","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p10193","attributes":{"selected":{"type":"object","name":"Selection","id":"p10194","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p10195"},"data":{"type":"map","entries":[["y",["Alphacoronavirus amsterdamense (3433809)","Alphacoronavirus porci (3433789)","Deltacoronavirus suis (3433742)","Gammacoronavirus galli (3433766)","Bat coronavirus (1508220)","Betacoronavirus sp. (1928434)","Alphacoronavirus sp. (1906673)","Alphacoronavirus suis (3433814)","Alphacoronavirus chicagoense (3433756)","Betacoronavirus cameli (3433633)","Betacoronavirus gravedinis (3433757)","Betacoronavirus hongkongense (3433758)"]],["share",[0.0,0.0,0.0,0.0,25.581395348837212,27.77777777777778,75.0,96.82539682539682,100.0,100.0,100.0,100.0]],["lo",[0.0,0.0,0.0,0.0,19.64385254082827,17.61682765302237,60.55943364104085,89.14352295339258,97.56625486776706,93.78821442127972,97.86397483323124,95.90643744356734]],["hi",[3.562135437245191,1.2398143345036292,5.580153132285688,1.5014997328429098,32.5858431388152,40.89044292879526,85.42578617103513,99.12504724384196,100.0,100.0,100.0,100.0]],["n",[104,306,65,252,172,54,44,63,154,58,176,90]],["det",[0,0,0,0,44,15,33,61,154,58,176,90]],["colour",["#b3261e","#b3261e","#b3261e","#b3261e","#b3261e","#b3261e","#b3261e","#007d5c","#007d5c","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p10241","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p10242"}}},"glyph":{"type":"object","name":"Scatter","id":"p10237","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p10238","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p10239","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p10204","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p10219"},{"type":"object","name":"BoxZoomTool","id":"p10220","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p10221","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p10227","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p10226","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p10228","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p10229"},{"type":"object","name":"SaveTool","id":"p10230"},{"type":"object","name":"HoverTool","id":"p10244","attributes":{"renderers":[{"id":"p10240"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p10214","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p10215"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p10216"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p10217"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p10209","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p10210","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p10211"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p10212"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p10213","attributes":{"axis":{"id":"p10209"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p10218","attributes":{"dimension":1,"axis":{"id":"p10214"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p10231","attributes":{"source":{"id":"p10193"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p10243","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"6f402382-5331-482c-a408-6c6df9740b18","roots":{"p10196":"c3874755-8665-469f-96dd-edeb04cb0d93"},"root_ids":["p10196"]}];
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

Retrieval query:

```
(RdRp[Gene] OR orf1ab[Gene] OR ORF1ab[Title] OR "RNA-dependent RNA polymerase"[Title] OR "complete genome"[Title]) NOT txid2697049[Organism:exp]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `oligos_modified`.


## What reached the statistics

25,565 records were screened for this assay and **7,999 (31%)** were evaluable, meaning both primers landed in the right orientation and size range. 17,566 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 14,531 |
| `truncated` | 2,750 |
| `chance_anchor` | 283 |

