# ADENOVIRUS_dsDNA_Hexon_gene_round2

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**ADENOVIRUS (dsDNA) — Hexon gene**

| | |
|---|---|
| Target | Adenoviridae ([taxid 10508](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10508)) |
| Gene | Hexon gene |
| Chemistry | conventional |
| Amplicon | 370 bp |
| Designed | 2005 |
| Paper | [10.1128/JCM.43.12.6176-6182.2005](https://doi.org/10.1128/JCM.43.12.6176-6182.2005) |
| Registry status | active |

!!! quote "The paper"
    Casas I et al. 2005. J Clin Microbiol 43:6176-6182 (ADHEX primers)

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CCCNTTYAACCACCACCG` | 18 nt |
| reverse | `KATGGGGTARAGCATGTT` | 18 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 1,257 | 1,429 | 88.0% | 86.2% – 89.5% |
| baseline (everything earlier) | 3,873 | 4,267 | 90.8% | 89.9% – 91.6% |

Change from baseline, Newcombe interval: **-4.8% to -1.0%**. Threshold: **90.0%**.

*detected share 88.0% (86%-90%) since Oct 2024, upper bound below the 90% threshold; change from baseline -5% to -1.0% (fell less than the 5% that counts as declining, from a baseline of 91%); separately, lineage Aviadenovirus hepatitidis (3426530) (49 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift*

Trend across deposit years: by record rising (p=0.482, 38 years); by footprint falling (p=7.51e-06); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="ba51a23f-30a1-4483-981e-dd11c20a54ed" data-root-id="p1369" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"c08bce9e-a270-4f35-91c9-b445b86f3c56":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p1424","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p1425"}}},"roots":[{"type":"object","name":"Figure","id":"p1369","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p1371"},"y_range":{"type":"object","name":"Range1d","id":"p1378","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p1379"},"y_scale":{"type":"object","name":"LinearScale","id":"p1380"},"title":{"type":"object","name":"Title","id":"p1376","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p1414","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p1366","attributes":{"selected":{"type":"object","name":"Selection","id":"p1367","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p1368"},"data":{"type":"map","entries":[["year",[1985,1987,1990,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[50.0,0.0,75.0,0.0,91.66666666666666,0.0,100.0,33.33333333333333,50.0,71.42857142857143,100.0,33.33333333333333,86.95652173913044,100.0,95.23809523809523,89.65517241379311,93.45794392523365,90.9090909090909,79.41176470588235,100.0,97.0873786407767,78.49462365591397,86.25,98.88888888888889,98.21428571428571,88.88888888888889,90.30303030303031,63.44086021505376,83.88888888888889,75.88652482269504,82.53968253968253,97.38675958188153,96.51162790697676,87.95180722891565,94.33656957928802,89.47368421052632,79.5031055900621,91.64733178654292]],["detected",[1,0,3,0,11,0,3,2,1,5,13,2,20,7,40,26,100,20,27,115,100,73,69,89,165,80,149,59,151,107,156,559,498,365,583,357,384,790]],["evaluable",[2,1,4,1,12,1,3,6,2,7,13,6,23,7,42,29,107,22,34,115,103,93,80,90,168,90,165,93,180,141,189,574,516,415,618,399,483,862]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,8.703135093227193,9.517227179437622,8.703135093227193,10.269703144398052,8.703135093227193,9.328625426046248,9.791719296345839,9.07684386569143,9.897626379762722,10.324834530005162,9.791719296345839,10.713966621835368,9.897626379762722,11.113982461744026,10.869436534339137,11.70836344482554,10.683957047019447,10.975067467348278,11.752796680528627,11.684804746364165,11.621380187649333,11.527140521415502,11.600932205756964,11.983160224294224,11.600932205756964,11.972329808973887,11.621380187649333,12.024520174044136,11.877342429442294,12.053664452795935,12.694931465319431,12.635209576202717,12.5119573835078,12.736131995073965,12.489546869224002,12.597975517842828,12.919691018014635]]]}}},"view":{"type":"object","name":"CDSView","id":"p1415","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p1416"}}},"glyph":{"type":"object","name":"Line","id":"p1411","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p1412","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p1413","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p1420","attributes":{"data_source":{"id":"p1366"},"view":{"type":"object","name":"CDSView","id":"p1421","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p1422"}}},"glyph":{"type":"object","name":"Scatter","id":"p1417","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p1418","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p1419","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p1377","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p1391"},{"type":"object","name":"BoxZoomTool","id":"p1392","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p1393","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p1399","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p1398","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p1400","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p1401"},{"type":"object","name":"SaveTool","id":"p1402"},{"type":"object","name":"HoverTool","id":"p1423","attributes":{"renderers":[{"id":"p1420"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p1386","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p1387","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p1388"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p1389"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p1381","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p1382","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p1383"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p1384"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p1385","attributes":{"axis":{"id":"p1381"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p1390","attributes":{"dimension":1,"axis":{"id":"p1386"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p1403","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p1405","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p1406","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p1407","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p1409","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p1408","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p1410","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"c08bce9e-a270-4f35-91c9-b445b86f3c56","roots":{"p1369":"ba51a23f-30a1-4483-981e-dd11c20a54ed"},"root_ids":["p1369"]}];
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

<div id="f8d38c17-7ec7-4def-8505-b092c29604db" data-root-id="p1429" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"6bfe5ec6-22c4-4cd9-9368-e5bd0f4d94e1":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p1469","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p1470"}}},"roots":[{"type":"object","name":"Figure","id":"p1429","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p1430"},"y_range":{"type":"object","name":"DataRange1d","id":"p1431","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p1438"},"y_scale":{"type":"object","name":"LinearScale","id":"p1439"},"title":{"type":"object","name":"Title","id":"p1436","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p1465","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p1426","attributes":{"selected":{"type":"object","name":"Selection","id":"p1427","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p1428"},"data":{"type":"map","entries":[["year",[1985,1987,1990,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[2,1,4,1,12,1,3,6,2,7,13,6,23,7,42,29,107,22,34,115,103,93,80,90,168,90,165,93,180,141,189,574,516,415,618,399,483,862]],["detected",[1,0,3,0,11,0,3,2,1,5,13,2,20,7,40,26,100,20,27,115,100,73,69,89,165,80,149,59,151,107,156,559,498,365,583,357,384,790]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p1466","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p1467"}}},"glyph":{"type":"object","name":"VBar","id":"p1462","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p1463","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p1464","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p1437","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p1450"},{"type":"object","name":"BoxZoomTool","id":"p1451","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p1452","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p1458","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p1457","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p1459","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p1460"},{"type":"object","name":"SaveTool","id":"p1461"},{"type":"object","name":"HoverTool","id":"p1468","attributes":{"renderers":[{"id":"p1465"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p1445","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p1446","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p1447"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p1448"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p1440","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p1441","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p1442"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p1443"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p1444","attributes":{"axis":{"id":"p1440"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p1449","attributes":{"dimension":1,"axis":{"id":"p1445"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"6bfe5ec6-22c4-4cd9-9368-e5bd0f4d94e1","roots":{"p1429":"f8d38c17-7ec7-4def-8505-b092c29604db"},"root_ids":["p1429"]}];
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

<div id="e494b0d8-f3be-44ef-b46f-30faf3f1af29" data-root-id="p1474" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"7cc7d5ee-634b-4012-aeb3-2420d41bd29e":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p1516","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p1517"}}},"roots":[{"type":"object","name":"Figure","id":"p1474","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p1476"},"y_range":{"type":"object","name":"FactorRange","id":"p1483","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p1484"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p1485"},"title":{"type":"object","name":"Title","id":"p1481","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p1511","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p1471","attributes":{"selected":{"type":"object","name":"Selection","id":"p1472","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p1473"},"data":{"type":"map","entries":[["x",[-14,-5,-4,-16,-11,-14,-16,-8,-10,-10,-17,-7,-5,-4,-17,-13,-1,-13,-8,-11,-6,-3,-1,-2,-3,-2,-15,-6,-9,-7,-18,-9,-12,-18]],["y",["reverse","reverse","reverse","reverse","forward","forward","forward","forward","reverse","forward","forward","forward","forward","forward","reverse","reverse","reverse","forward","reverse","reverse","reverse","forward","forward","reverse","reverse","forward","reverse","forward","forward","reverse","reverse","reverse","reverse","forward"]],["alpha",[0.32370084269662924,0.2926615168539326,0.2992275280898876,0.3231039325842696,0.21446629213483145,0.203125,0.19417134831460675,0.19297752808988763,0.18760533707865168,0.18700842696629214,0.17924859550561797,0.17686095505617977,0.17089185393258427,0.16850421348314606,0.20014044943820225,0.215063202247191,0.18521769662921347,0.18820224719101122,0.16790730337078652,0.2114817415730337,0.2138693820224719,0.227001404494382,0.1971558988764045,0.19536516853932584,0.1774578651685393,0.29027387640449437,0.6263342696629214,0.486060393258427,0.5696278089887641,0.32429775280898876,1.0,0.8871839887640449,0.9617977528089887,1.0]],["pos",[14,5,4,16,11,14,16,8,10,10,17,7,5,4,17,13,1,13,8,11,6,3,1,2,3,2,15,6,9,7,18,9,12,18]],["base",["G","A","T","T","A","T","C","C","A","A","C","A","C","A","A","G","T","T","A","T","C","C","G","T","G","C","G","C","C","G","K","R","G","C"]],["n",[291,239,250,290,108,89,74,72,63,62,49,45,35,31,84,109,59,64,30,103,107,129,79,76,46,235,798,563,703,292,2233,1235,1360,2846]],["det_with",["0% of 291","0% of 239","0% of 250","2% of 290","0% of 108","0% of 89","0% of 74","0% of 72","0% of 63","0% of 62","0% of 49","0% of 45","0% of 35","0% of 31","1% of 84","3% of 109","3% of 59","6% of 64","7% of 30","12% of 103","13% of 107","15% of 129","15% of 79","16% of 76","26% of 46","36% of 235","58% of 798","82% of 563","85% of 703","88% of 292","89% of 2233","92% of 1235","93% of 1360","93% of 2846"]],["det_without",["95% of 5721","95% of 5773","95% of 5762","95% of 5722","93% of 5904","92% of 5923","92% of 5938","92% of 5940","92% of 5949","92% of 5950","92% of 5963","92% of 5967","91% of 5977","91% of 5981","92% of 5928","92% of 5903","92% of 5953","92% of 5948","91% of 5982","92% of 5909","92% of 5905","93% of 5883","92% of 5933","92% of 5936","91% of 5966","93% of 5777","96% of 5214","92% of 5449","92% of 5309","91% of 5720","92% of 3779","91% of 4777","90% of 4652","89% of 3166"]],["subs",["G&gt;T 239, G&gt;C 32, G&gt;A 20","A&gt;G 198, A&gt;T 38, A&gt;C 3","T&gt;C 199, T&gt;G 38, T&gt;A 13","T&gt;C 258, T&gt;G 30, T&gt;A 2","A&gt;C 60, A&gt;T 36, A&gt;G 12","T&gt;C 46, T&gt;G 33, T&gt;A 10","C&gt;A 38, C&gt;T 28, C&gt;G 8","C&gt;T 33, C&gt;A 27, C&gt;G 12","A&gt;T 36, A&gt;C 23, A&gt;G 4","A&gt;G 42, A&gt;T 14, A&gt;C 6","C&gt;G 28, C&gt;A 11, C&gt;T 10","A&gt;T 23, A&gt;G 19, A&gt;C 3","C&gt;A 26, C&gt;T 8, C&gt;W 1","A&gt;T 24, A&gt;C 5, A&gt;G 2","A&gt;T 45, A&gt;C 25, A&gt;G 14","G&gt;C 55, G&gt;T 37, G&gt;A 17","T&gt;A 28, T&gt;G 24, T&gt;C 7","T&gt;G 37, T&gt;A 16, T&gt;C 11","A&gt;G 14, A&gt;T 12, A&gt;C 4","T&gt;A 69, T&gt;G 17, T&gt;C 17","C&gt;A 51, C&gt;T 35, C&gt;G 21","C&gt;T 87, C&gt;G 32, C&gt;A 10","G&gt;A 45, G&gt;T 28, G&gt;C 6","T&gt;C 29, T&gt;G 24, T&gt;A 23","G&gt;A 34, G&gt;C 11, G&gt;T 1","C&gt;A 224, C&gt;T 8, C&gt;G 3","G&gt;A 438, G&gt;C 254, G&gt;T 106","C&gt;T 532, C&gt;G 26, C&gt;A 5","C&gt;T 682, C&gt;G 13, C&gt;A 8","G&gt;A 282, G&gt;T 10","K&gt;A 2072, K&gt;C 161","R&gt;T 743, R&gt;C 492","G&gt;A 1352, G&gt;T 8","C&gt;T 2821, C&gt;A 17, C&gt;G 8"]],["zone",["no","yes","yes","no","no","no","no","no","no","no","no","no","yes","yes","no","no","yes","no","no","no","no","yes","yes","yes","yes","yes","no","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p1512","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p1513"}}},"glyph":{"type":"object","name":"Rect","id":"p1508","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p1509","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p1510","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p1482","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p1496"},{"type":"object","name":"BoxZoomTool","id":"p1497","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p1498","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p1504","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p1503","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p1505","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p1506"},{"type":"object","name":"SaveTool","id":"p1507"},{"type":"object","name":"HoverTool","id":"p1514","attributes":{"renderers":[{"id":"p1511"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p1491","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p1492"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p1493"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p1494"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p1486","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p1515","attributes":{"ticks":[-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p1488"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-14,"14"],[-5,"5"],[-4,"4"],[-16,"16"],[-11,"11"],[-8,"8"],[-10,"10"],[-17,"17"],[-7,"7"],[-13,"13"],[-1,"1"],[-6,"6"],[-3,"3"],[-2,"2"],[-15,"15"],[-9,"9"],[-18,"18"],[-12,"12"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p1489"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p1490","attributes":{"axis":{"id":"p1486"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p1495","attributes":{"dimension":1,"axis":{"id":"p1491"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"7cc7d5ee-634b-4012-aeb3-2420d41bd29e","roots":{"p1474":"e494b0d8-f3be-44ef-b46f-30faf3f1af29"},"root_ids":["p1474"]}];
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

<div id="e418d412-ad01-4c7d-9acb-4317a9115932" data-root-id="p1521" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"dd040844-e41d-4b8d-84de-0b3639cf165b":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p1570","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p1571"}}},"roots":[{"type":"object","name":"Figure","id":"p1521","attributes":{"height":210,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p1530","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p1531","attributes":{"factors":["Aviadenovirus hepatitidis (3426530)","Human adenovirus sp. (1907210)","Mastadenovirus faecale (3241426)","Mastadenovirus blackbeardi (3241406)","Mastadenovirus caesari (3241411)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p1532"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p1533"},"title":{"type":"object","name":"Title","id":"p1528","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p1565","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p1518","attributes":{"selected":{"type":"object","name":"Selection","id":"p1519","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p1520"},"data":{"type":"map","entries":[["y",["Aviadenovirus hepatitidis (3426530)","Human adenovirus sp. (1907210)","Mastadenovirus faecale (3241426)","Mastadenovirus blackbeardi (3241406)","Mastadenovirus caesari (3241411)"]],["share",[0.0,85.08771929824562,98.28326180257511,100.0,100.0]],["lo",[0.0,77.4116058983086,95.66983901628329,99.38124963046263,97.95494623774134]],["hi",[7.269781922049637,90.47621626598321,99.33042027967934,100.0,100.0]],["n",[49,114,233,617,184]],["det",[0,97,229,617,184]],["colour",["#b3261e","#007d5c","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p1566","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p1567"}}},"glyph":{"type":"object","name":"Scatter","id":"p1562","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p1563","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p1564","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p1529","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p1544"},{"type":"object","name":"BoxZoomTool","id":"p1545","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p1546","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p1552","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p1551","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p1553","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p1554"},{"type":"object","name":"SaveTool","id":"p1555"},{"type":"object","name":"HoverTool","id":"p1569","attributes":{"renderers":[{"id":"p1565"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p1539","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p1540"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p1541"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p1542"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p1534","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p1535","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p1536"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p1537"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p1538","attributes":{"axis":{"id":"p1534"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p1543","attributes":{"dimension":1,"axis":{"id":"p1539"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p1556","attributes":{"source":{"id":"p1518"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p1568","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"dd040844-e41d-4b8d-84de-0b3639cf165b","roots":{"p1521":"e418d412-ad01-4c7d-9acb-4317a9115932"},"root_ids":["p1521"]}];
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

38,024 records were screened for this assay and **5,696 (15%)** were evaluable, meaning both primers landed in the right orientation and size range. 32,328 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 21,581 |
| `chance_only` | 5,260 |
| `truncated` | 4,830 |
| `chance_anchor` | 569 |
| `no_pair` | 86 |

