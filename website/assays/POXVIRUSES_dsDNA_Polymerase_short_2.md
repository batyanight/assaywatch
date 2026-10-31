# POXVIRUSES_dsDNA_Polymerase_short_2

<span class="aw-chip aw-chip-stable">stable</span>

**POXVIRUSES (dsDNA) — Polymerase short**

| | |
|---|---|
| Target | Chordopoxvirinae ([taxid 10241](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10241)) |
| Gene | Polymerase short |
| Chemistry | conventional |
| Amplicon | 192 bp |
| Designed | 2016 |
| Paper | [10.3354/dao02986](https://doi.org/10.3354/dao02986) |
| Registry status | active |

!!! quote "The paper"
    McAloose D, ..., Seimon T, ..., Uhart M. 2016. Post-mortem findings in southern right whales Eubalaena australis at Peninsula Valdes, Argentina, 2003-2012. Dis Aquat Organ 119:17-36 (pan-poxvirus DNA polymerase PCR)

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `TATAGAGCGAGTACAGTCATCAAG` | 24 nt |
| reverse | `CANACATTNGGATAYARACTATTATAATC` | 29 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 5,803 | 5,879 | 98.7% | 98.4% – 99.0% |
| baseline (everything earlier) | 9,425 | 9,676 | 97.4% | 97.1% – 97.7% |

Change from baseline, Newcombe interval: **0.9% to 1.7%**. Threshold: **90.0%**.

*detected share 98.7% (98%-99%) since Oct 2024*

Trend across deposit years: by record rising (p=1.22e-119, 35 years); by footprint falling (p=0.28); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="e8c1c904-e8f5-4170-9d95-a5c233dcec62" data-root-id="p24532" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"42c6e4ce-5f4f-47a0-a648-7e57729d83e8":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p24587","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p24588"}}},"roots":[{"type":"object","name":"Figure","id":"p24532","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p24534"},"y_range":{"type":"object","name":"Range1d","id":"p24541","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p24542"},"y_scale":{"type":"object","name":"LinearScale","id":"p24543"},"title":{"type":"object","name":"Title","id":"p24539","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p24577","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p24529","attributes":{"selected":{"type":"object","name":"Selection","id":"p24530","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p24531"},"data":{"type":"map","entries":[["year",[1990,1991,1993,1994,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,33.33333333333333,100.0,100.0,42.857142857142854,100.0,57.14285714285714,100.0,100.0,100.0,96.7741935483871,96.82539682539682,66.66666666666666,0.0,100.0,50.0,93.75,34.21052631578947,87.67123287671232,98.66666666666667,100.0,69.56521739130434,64.83516483516483,90.42553191489363,52.892561983471076,96.20253164556962,88.52459016393442,99.85851726089417,98.65278628291489,98.50948509485094,98.98605830164765,98.59884252208346]],["detected",[1,1,4,1,1,1,2,3,3,4,16,12,10,30,61,4,0,1,6,15,13,64,74,35,16,59,85,64,76,54,3529,3222,2181,2343,3237]],["evaluable",[1,1,4,1,3,1,2,7,3,7,16,12,10,31,63,6,4,1,12,16,38,73,75,35,23,91,94,121,79,61,3534,3266,2214,2367,3283]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.517227179437622,8.703135093227193,9.328625426046248,8.703135093227193,9.07684386569143,9.897626379762722,9.328625426046248,9.897626379762722,10.467343773689333,10.269703144398052,10.143865699252444,10.913832791890265,11.375828278421016,9.791719296345839,9.517227179437622,8.703135093227193,10.269703144398052,10.467343773689333,11.048392086352559,11.469403343404682,11.486479824227462,10.994220569835573,10.713966621835368,11.607827582127728,11.62804092087081,11.784019340078249,11.51922823234585,11.355225445040746,13.663476705714839,13.623263545722939,13.422780016098258,13.457511293384869,13.625915429325845]]]}}},"view":{"type":"object","name":"CDSView","id":"p24578","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p24579"}}},"glyph":{"type":"object","name":"Line","id":"p24574","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p24575","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p24576","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p24583","attributes":{"data_source":{"id":"p24529"},"view":{"type":"object","name":"CDSView","id":"p24584","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p24585"}}},"glyph":{"type":"object","name":"Scatter","id":"p24580","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p24581","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p24582","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p24540","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p24554"},{"type":"object","name":"BoxZoomTool","id":"p24555","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p24556","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p24562","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p24561","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p24563","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p24564"},{"type":"object","name":"SaveTool","id":"p24565"},{"type":"object","name":"HoverTool","id":"p24586","attributes":{"renderers":[{"id":"p24583"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p24549","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p24550","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p24551"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p24552"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p24544","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p24545","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p24546"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p24547"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p24548","attributes":{"axis":{"id":"p24544"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p24553","attributes":{"dimension":1,"axis":{"id":"p24549"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p24566","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p24568","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p24569","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p24570","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p24572","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p24571","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p24573","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"42c6e4ce-5f4f-47a0-a648-7e57729d83e8","roots":{"p24532":"e8c1c904-e8f5-4170-9d95-a5c233dcec62"},"root_ids":["p24532"]}];
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

<div id="e4671ad0-8a05-406a-aea4-b97c60a26910" data-root-id="p24592" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"531b7d99-4ab0-4b1b-be5c-031cb9d93bd7":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p24632","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p24633"}}},"roots":[{"type":"object","name":"Figure","id":"p24592","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p24593"},"y_range":{"type":"object","name":"DataRange1d","id":"p24594","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p24601"},"y_scale":{"type":"object","name":"LinearScale","id":"p24602"},"title":{"type":"object","name":"Title","id":"p24599","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p24628","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p24589","attributes":{"selected":{"type":"object","name":"Selection","id":"p24590","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p24591"},"data":{"type":"map","entries":[["year",[1990,1991,1993,1994,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,4,1,3,1,2,7,3,7,16,12,10,31,63,6,4,1,12,16,38,73,75,35,23,91,94,121,79,61,3534,3266,2214,2367,3283]],["detected",[1,1,4,1,1,1,2,3,3,4,16,12,10,30,61,4,0,1,6,15,13,64,74,35,16,59,85,64,76,54,3529,3222,2181,2343,3237]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p24629","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p24630"}}},"glyph":{"type":"object","name":"VBar","id":"p24625","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p24626","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p24627","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p24600","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p24613"},{"type":"object","name":"BoxZoomTool","id":"p24614","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p24615","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p24621","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p24620","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p24622","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p24623"},{"type":"object","name":"SaveTool","id":"p24624"},{"type":"object","name":"HoverTool","id":"p24631","attributes":{"renderers":[{"id":"p24628"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p24608","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p24609","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p24610"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p24611"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p24603","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p24604","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p24605"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p24606"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p24607","attributes":{"axis":{"id":"p24603"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p24612","attributes":{"dimension":1,"axis":{"id":"p24608"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"531b7d99-4ab0-4b1b-be5c-031cb9d93bd7","roots":{"p24592":"e4671ad0-8a05-406a-aea4-b97c60a26910"},"root_ids":["p24592"]}];
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

<div id="c1572394-3c61-4d2e-a27a-f5d8c8091d4d" data-root-id="p24637" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"e023bdf9-1cd0-440d-9c33-3a2e4a05e1b3":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p24679","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p24680"}}},"roots":[{"type":"object","name":"Figure","id":"p24637","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p24639"},"y_range":{"type":"object","name":"FactorRange","id":"p24646","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p24647"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p24648"},"title":{"type":"object","name":"Title","id":"p24644","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p24674","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p24634","attributes":{"selected":{"type":"object","name":"Selection","id":"p24635","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p24636"},"data":{"type":"map","entries":[["x",[-21,-22,-7,-4,-3,-15,-1,-8,-16,-18,-18,-12,-10,-20,-24,-9,-6,-9]],["y",["forward","forward","forward","forward","reverse","reverse","forward","forward","forward","reverse","forward","reverse","forward","forward","reverse","forward","reverse","reverse"]],["alpha",[0.18344262295081967,0.18387978142076503,0.19415300546448086,0.19327868852459015,0.19065573770491803,0.16617486338797813,0.15852459016393441,0.17491803278688522,0.18344262295081967,0.1762295081967213,0.15524590163934426,0.2831147540983606,0.2686885245901639,0.1705464480874317,0.2531693989071038,1.0,0.25491803278688524,1.0]],["pos",[21,22,7,4,3,15,1,8,16,18,18,12,10,20,24,9,6,9]],["base",["A","T","C","C","A","Y","G","T","G","A","G","A","A","G","A","G","A","A"]],["n",[153,155,202,198,186,74,39,114,153,120,24,609,543,94,472,10900,480,14655]],["det_with",["0% of 153","5% of 155","11% of 202","15% of 198","20% of 186","20% of 74","28% of 39","34% of 114","41% of 153","46% of 120","67% of 24","74% of 609","84% of 543","94% of 94","97% of 472","98% of 10900","98% of 480","100% of 14655"]],["det_without",["99% of 15481","99% of 15479","99% of 15432","99% of 15436","99% of 15448","99% of 15560","99% of 15595","99% of 15520","99% of 15481","99% of 15514","98% of 15610","99% of 15025","99% of 15091","98% of 15540","98% of 15162","99% of 4734","98% of 15154","76% of 979"]],["subs",["A&gt;C 153","T&gt;C 155","T&gt;G 153, C&gt;G 16, C&gt;A 16, C&gt;T 11","T&gt;C 169, C&gt;T 24, C&gt;A 4, A&gt;T 1","G&gt;A 186","Y&gt;G 71, Y&gt;A 3","G&gt;A 31, A&gt;G 8","G&gt;T 114","G&gt;C 106, G&gt;T 22, G&gt;A 15, T&gt;A 6","G&gt;A 115, A&gt;G 3, G&gt;C 1, A&gt;C 1","G&gt;T 18, G&gt;A 6","G&gt;A 605, A&gt;G 4","G&gt;A 417, C&gt;G 100, C&gt;A 10, G&gt;T 5","G&gt;A 94","G&gt;A 451, A&gt;G 20, G&gt;C 1","G&gt;A 10629, C&gt;T 153, T&gt;C 104, G&gt;T 6","G&gt;A 480","A&gt;G 14620, G&gt;A 35"]],["zone",["no","no","no","yes","yes","no","yes","no","no","no","no","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p24675","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p24676"}}},"glyph":{"type":"object","name":"Rect","id":"p24671","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p24672","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p24673","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p24645","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p24659"},{"type":"object","name":"BoxZoomTool","id":"p24660","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p24661","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p24667","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p24666","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p24668","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p24669"},{"type":"object","name":"SaveTool","id":"p24670"},{"type":"object","name":"HoverTool","id":"p24677","attributes":{"renderers":[{"id":"p24674"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p24654","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p24655"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p24656"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p24657"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p24649","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p24678","attributes":{"ticks":[-24,-22,-21,-20,-18,-16,-15,-12,-10,-9,-8,-7,-6,-4,-3,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p24651"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-21,"21"],[-22,"22"],[-7,"7"],[-4,"4"],[-3,"3"],[-15,"15"],[-1,"1"],[-8,"8"],[-16,"16"],[-18,"18"],[-12,"12"],[-10,"10"],[-20,"20"],[-24,"24"],[-9,"9"],[-6,"6"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p24652"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p24653","attributes":{"axis":{"id":"p24649"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p24658","attributes":{"dimension":1,"axis":{"id":"p24654"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"e023bdf9-1cd0-440d-9c33-3a2e4a05e1b3","roots":{"p24637":"c1572394-3c61-4d2e-a27a-f5d8c8091d4d"},"root_ids":["p24637"]}];
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

<div id="e5f9aa64-1043-4ca8-822f-514bc936df59" data-root-id="p24684" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"e2bfe8b1-fc7d-4348-a917-ac98ada836a8":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p24733","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p24734"}}},"roots":[{"type":"object","name":"Figure","id":"p24684","attributes":{"height":132,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p24693","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p24694","attributes":{"factors":["Orthopoxvirus monkeypox (3431483)","Capripoxvirus lumpyskinpox (3427718)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p24695"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p24696"},"title":{"type":"object","name":"Title","id":"p24691","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p24728","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p24681","attributes":{"selected":{"type":"object","name":"Selection","id":"p24682","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p24683"},"data":{"type":"map","entries":[["y",["Orthopoxvirus monkeypox (3431483)","Capripoxvirus lumpyskinpox (3427718)"]],["share",[99.94580924855492,100.0]],["lo",[99.84078267383452,98.0384853933246]],["hi",[99.9815685812718,100.0]],["n",[5536,192]],["det",[5533,192]],["colour",["#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p24729","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p24730"}}},"glyph":{"type":"object","name":"Scatter","id":"p24725","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p24726","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p24727","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p24692","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p24707"},{"type":"object","name":"BoxZoomTool","id":"p24708","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p24709","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p24715","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p24714","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p24716","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p24717"},{"type":"object","name":"SaveTool","id":"p24718"},{"type":"object","name":"HoverTool","id":"p24732","attributes":{"renderers":[{"id":"p24728"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p24702","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p24703"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p24704"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p24705"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p24697","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p24698","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p24699"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p24700"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p24701","attributes":{"axis":{"id":"p24697"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p24706","attributes":{"dimension":1,"axis":{"id":"p24702"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p24719","attributes":{"source":{"id":"p24681"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p24731","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"e2bfe8b1-fc7d-4348-a917-ac98ada836a8","roots":{"p24684":"e5f9aa64-1043-4ca8-822f-514bc936df59"},"root_ids":["p24684"]}];
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

Disclosures on this entry: `oligos_modified`, `pairing_is_curator_reading`, `oligos_from_secondary_source`.


## What reached the statistics

28,428 records were screened for this assay and **15,555 (55%)** were evaluable, meaning both primers landed in the right orientation and size range. 12,873 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 12,665 |
| `truncated` | 200 |
| `chance_anchor` | 1 |

