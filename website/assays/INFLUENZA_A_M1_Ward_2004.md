# INFLUENZA_A_M1_Ward_2004

<span class="aw-chip aw-chip-declining">declining</span>

**Influenza A virus — M1 gene real-time RT-PCR (Ward 2004)**

| | |
|---|---|
| Target | Influenza A virus ([taxid 11320](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11320)) |
| Gene | M1 (matrix) |
| Chemistry | hydrolysis_probe |
| Amplicon | 95 bp |
| Designed | 2004 |
| Paper | [10.1016/S1386-6532(03)00122-7](https://doi.org/10.1016/S1386-6532(03)00122-7) |
| Registry status | draft |

!!! quote "The paper"
    Ward CL et al. 2004. J Clin Virol 29:179-188

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `AAGACCAATCCTGTCACCTCTGA` | 23 nt |
| reverse | `CAAAGCGTCTACGCTGCAGTCC` | 22 nt |
| probe | `TTTGTGTTCACGCTCACCGT` | 20 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 41,798 | 70,578 | 59.2% | 58.9% – 59.6% |
| baseline (everything earlier) | 66,714 | 113,283 | 58.9% | 58.6% – 59.2% |

Change from baseline, Newcombe interval: **-0.1% to 0.8%**. Threshold: **90.0%**.

*pooled share 59.2% has low coverage, but lineage Alphainfluenzavirus influenzae (2955291) (70566 records) detects 59.2% (58.9%-59.6%); lineage verdict overrides to declining*

Trend across deposit years: by record falling (p=0, 37 years); by footprint falling (p=3.26e-23). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="e4e25dd5-870d-4278-a0e4-611b07095b0a" data-root-id="p14415" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"7b7e79e5-55a2-4032-948b-f302ddca6372":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14470","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14471"}}},"roots":[{"type":"object","name":"Figure","id":"p14415","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p14417"},"y_range":{"type":"object","name":"Range1d","id":"p14424","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p14425"},"y_scale":{"type":"object","name":"LinearScale","id":"p14426"},"title":{"type":"object","name":"Title","id":"p14422","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14460","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14412","attributes":{"selected":{"type":"object","name":"Selection","id":"p14413","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14414"},"data":{"type":"map","entries":[["year",[1982,1987,1988,1990,1992,1993,1994,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,50.0,100.0,100.0,91.66666666666666,100.0,100.0,100.0,92.5,91.66666666666666,94.64285714285714,93.75,94.68085106382979,88.37209302325581,92.63657957244655,89.30778739184177,91.4609739826551,87.38812042310822,93.02838247451089,91.28736081265872,88.27433628318585,86.72364672364672,81.69596690796277,78.11194653299917,68.299366329851,57.95936931473621,66.69435215946844,53.01223010720217,39.38156359393232,64.46833617411826,61.085043988269796,20.54150816737525,46.050732109713344,61.47627268516569,60.51943764272154,53.32983193277311]],["detected",[1,1,1,1,1,11,2,5,5,37,22,53,30,178,152,780,1445,1371,1074,3376,4673,1197,1522,3950,2805,3988,3823,2409,3511,4725,4917,2083,1836,6699,14600,21997,15231]],["evaluable",[1,1,2,1,1,12,2,5,5,40,24,56,32,188,172,842,1618,1499,1229,3629,5119,1356,1755,4835,3591,5839,6596,3612,6623,11998,7627,3410,8938,14547,23749,36347,28560]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.07684386569143,8.703135093227193,8.703135093227193,10.269703144398052,9.07684386569143,9.667366891029102,9.667366891029102,11.082053972722118,10.74264168206181,11.300413928944284,10.934913263353746,12.050499715724602,11.997285845087944,12.906850628005783,13.258224564652226,13.21774346303488,13.111756908964187,13.676968934388766,13.850426213951035,13.164373871099656,13.301121918958735,13.821837057760497,13.671616944019387,13.916057950460413,13.976505003962387,13.674581914023637,13.978524859671293,14.268479326569256,14.048088844200574,13.64528266347047,14.125745971931131,14.360901474335865,14.592738690621045,14.790335575568323,14.678798535409525]]]}}},"view":{"type":"object","name":"CDSView","id":"p14461","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14462"}}},"glyph":{"type":"object","name":"Line","id":"p14457","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p14458","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p14459","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p14466","attributes":{"data_source":{"id":"p14412"},"view":{"type":"object","name":"CDSView","id":"p14467","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14468"}}},"glyph":{"type":"object","name":"Scatter","id":"p14463","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p14464","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p14465","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14423","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14437"},{"type":"object","name":"BoxZoomTool","id":"p14438","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14439","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14445","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14444","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14446","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14447"},{"type":"object","name":"SaveTool","id":"p14448"},{"type":"object","name":"HoverTool","id":"p14469","attributes":{"renderers":[{"id":"p14466"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p14432","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14433","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14434"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14435"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14427","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14428","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14429"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14430"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14431","attributes":{"axis":{"id":"p14427"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14436","attributes":{"dimension":1,"axis":{"id":"p14432"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p14449","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p14451","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p14452","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p14453","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p14455","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14454","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p14456","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"7b7e79e5-55a2-4032-948b-f302ddca6372","roots":{"p14415":"e4e25dd5-870d-4278-a0e4-611b07095b0a"},"root_ids":["p14415"]}];
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

<div id="a46ba23a-9e8b-4754-8a10-6ab2a4446943" data-root-id="p14475" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"2650e852-a854-4e4b-a09b-bcaa87968221":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14515","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14516"}}},"roots":[{"type":"object","name":"Figure","id":"p14475","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p14476"},"y_range":{"type":"object","name":"DataRange1d","id":"p14477","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p14484"},"y_scale":{"type":"object","name":"LinearScale","id":"p14485"},"title":{"type":"object","name":"Title","id":"p14482","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14511","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14472","attributes":{"selected":{"type":"object","name":"Selection","id":"p14473","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14474"},"data":{"type":"map","entries":[["year",[1982,1987,1988,1990,1992,1993,1994,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,2,1,1,12,2,5,5,40,24,56,32,188,172,842,1618,1499,1229,3629,5119,1356,1755,4835,3591,5839,6596,3612,6623,11998,7627,3410,8938,14547,23749,36347,28560]],["detected",[1,1,1,1,1,11,2,5,5,37,22,53,30,178,152,780,1445,1371,1074,3376,4673,1197,1522,3950,2805,3988,3823,2409,3511,4725,4917,2083,1836,6699,14600,21997,15231]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p14512","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14513"}}},"glyph":{"type":"object","name":"VBar","id":"p14508","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p14509","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p14510","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14483","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14496"},{"type":"object","name":"BoxZoomTool","id":"p14497","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14498","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14504","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14503","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14505","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14506"},{"type":"object","name":"SaveTool","id":"p14507"},{"type":"object","name":"HoverTool","id":"p14514","attributes":{"renderers":[{"id":"p14511"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p14491","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14492","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14493"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14494"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14486","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14487","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14488"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14489"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14490","attributes":{"axis":{"id":"p14486"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14495","attributes":{"dimension":1,"axis":{"id":"p14491"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"2650e852-a854-4e4b-a09b-bcaa87968221","roots":{"p14475":"a46ba23a-9e8b-4754-8a10-6ab2a4446943"},"root_ids":["p14475"]}];
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

<div id="c430bab2-b33a-4aa4-b0b9-a4ff87af776a" data-root-id="p14520" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"8bbfc4f7-87fe-40c2-9e3e-ea4b7224ac7e":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14562","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14563"}}},"roots":[{"type":"object","name":"Figure","id":"p14520","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p14522"},"y_range":{"type":"object","name":"FactorRange","id":"p14529","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p14530"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p14531"},"title":{"type":"object","name":"Title","id":"p14527","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14557","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14517","attributes":{"selected":{"type":"object","name":"Selection","id":"p14518","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14519"},"data":{"type":"map","entries":[["x",[-4,-15,-14,-12,-7,-9,-1,-5,-13,-11,-17,-16,-15,-8,-22,-3,-9,-6,-12,-23,-11,-17,-18,-20,-5,-20,-21,-2,-17,-14,-18,-3,-13,-11,-8,-13,-22]],["y",["forward","probe","forward","probe","forward","probe","forward","reverse","probe","probe","probe","reverse","reverse","forward","forward","probe","reverse","reverse","reverse","forward","forward","reverse","probe","forward","forward","probe","reverse","forward","forward","reverse","reverse","reverse","reverse","reverse","reverse","forward","reverse"]],["alpha",[1.0,1.0,1.0,0.22868444096355398,0.17738699343525816,0.15743387667857783,0.15075818145229275,0.15053627468576805,0.15053627468576805,0.15036984461087452,0.15952349873001886,0.15181223859328513,0.15613942054051702,0.15305121803971478,0.1523485132790532,0.15443813533049422,0.1803457503222543,0.15846944158902648,0.1520526375903536,0.15046230576359315,0.1510170726799049,0.15048079799413688,0.18966583451629218,0.16399861852160055,0.15858039497228885,0.1516458085183916,0.1801978124779045,0.1877426425397447,0.1822134656071706,0.15073968922174905,0.4276608416140454,0.1519231919765475,0.1504253213025057,0.15044381353304942,0.15059175137739922,1.0,0.850726091993408]],["pos",[4,15,14,12,7,9,1,5,13,11,17,16,15,8,22,3,9,6,12,23,11,17,18,20,5,20,21,2,17,14,18,3,13,11,8,13,22]],["base",["C","G","C","C","C","G","A","A","T","A","G","G","T","A","A","C","C","C","A","A","G","C","T","A","T","T","A","G","A","C","G","T","T","C","T","C","C"]],["n",[58685,65336,62744,4255,1481,402,41,29,29,20,515,98,332,165,127,240,1641,458,111,25,55,26,2145,757,464,89,1633,2041,1742,40,15015,104,23,24,32,60700,37893]],["det_with",["0% of 58685","5% of 65336","6% of 62744","0% of 4255","0% of 1481","0% of 402","0% of 41","0% of 29","0% of 29","0% of 20","1% of 515","7% of 98","9% of 332","9% of 165","10% of 127","11% of 240","12% of 1641","17% of 458","27% of 111","28% of 25","31% of 55","35% of 26","38% of 2145","39% of 757","53% of 464","55% of 89","56% of 1633","56% of 2041","57% of 1742","60% of 40","62% of 15015","64% of 104","74% of 23","88% of 24","88% of 32","84% of 60700","96% of 37893"]],["det_without",["87% of 125151","89% of 118500","86% of 121092","60% of 179581","60% of 182355","59% of 183434","59% of 183795","59% of 183807","59% of 183807","59% of 183816","59% of 183321","59% of 183738","59% of 183504","59% of 183671","59% of 183709","59% of 183596","59% of 182195","59% of 183378","59% of 183725","59% of 183811","59% of 183781","59% of 183810","59% of 181691","59% of 183079","59% of 183372","59% of 183747","59% of 182203","59% of 181795","59% of 182094","59% of 183796","59% of 168821","59% of 183732","59% of 183813","59% of 183812","59% of 183804","47% of 123136","49% of 145943"]],["subs",["C&gt;T 58247, C&gt;A 437, C&gt;G 1","G&gt;T 58925, G&gt;A 6355, G&gt;C 56","C&gt;T 62594, C&gt;A 149, C&gt;G 1","C&gt;T 4254, C&gt;A 1","C&gt;T 1478, C&gt;A 2, C&gt;G 1","G&gt;A 399, G&gt;T 3","A&gt;G 28, A&gt;T 12, A&gt;C 1","A&gt;T 16, A&gt;G 10, A&gt;C 3","T&gt;A 24, T&gt;C 4, T&gt;G 1","A&gt;C 9, A&gt;G 6, A&gt;T 5","G&gt;A 509, G&gt;T 6","G&gt;T 96, G&gt;C 2","T&gt;C 332","A&gt;G 152, A&gt;C 7, A&gt;T 6","A&gt;C 122, A&gt;G 5","C&gt;T 201, C&gt;A 37, C&gt;G 2","C&gt;T 1633, C&gt;A 8","C&gt;A 356, C&gt;T 99, C&gt;G 3","A&gt;G 108, A&gt;C 2, A&gt;T 1","A&gt;G 16, A&gt;C 7, A&gt;T 2","G&gt;A 50, G&gt;T 5","C&gt;T 17, C&gt;A 6, C&gt;G 3","T&gt;C 2049, T&gt;A 85, T&gt;G 11","A&gt;G 754, A&gt;C 2, A&gt;T 1","T&gt;C 360, T&gt;A 95, T&gt;G 9","T&gt;G 47, T&gt;C 42","A&gt;G 1628, A&gt;T 4, A&gt;C 1","G&gt;A 1984, G&gt;T 52, G&gt;C 5","A&gt;G 1533, A&gt;T 196, A&gt;C 13","C&gt;T 22, C&gt;A 13, C&gt;G 5","G&gt;A 6947, G&gt;C 5391, G&gt;T 2510, G&gt;M 165","T&gt;C 90, T&gt;G 13, T&gt;A 1","T&gt;G 23","C&gt;A 21, C&gt;T 3","T&gt;A 28, T&gt;G 2, T&gt;C 2","C&gt;T 60695, C&gt;A 3, C&gt;G 2","C&gt;T 37890, C&gt;A 3"]],["zone",["yes","no","no","no","no","no","yes","yes","no","no","no","no","no","no","no","yes","no","no","no","no","no","no","no","no","yes","no","no","yes","no","no","no","yes","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p14558","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14559"}}},"glyph":{"type":"object","name":"Rect","id":"p14554","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p14555","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p14556","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14528","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14542"},{"type":"object","name":"BoxZoomTool","id":"p14543","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14544","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14550","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14549","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14551","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14552"},{"type":"object","name":"SaveTool","id":"p14553"},{"type":"object","name":"HoverTool","id":"p14560","attributes":{"renderers":[{"id":"p14557"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p14537","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p14538"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p14539"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14540"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14532","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p14561","attributes":{"ticks":[-23,-22,-21,-20,-18,-17,-16,-15,-14,-13,-12,-11,-9,-8,-7,-6,-5,-4,-3,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14534"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-4,"4"],[-15,"15"],[-14,"14"],[-12,"12"],[-7,"7"],[-9,"9"],[-1,"1"],[-5,"5"],[-13,"13"],[-11,"11"],[-17,"17"],[-16,"16"],[-8,"8"],[-22,"22"],[-3,"3"],[-6,"6"],[-23,"23"],[-18,"18"],[-20,"20"],[-21,"21"],[-2,"2"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p14535"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14536","attributes":{"axis":{"id":"p14532"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14541","attributes":{"dimension":1,"axis":{"id":"p14537"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"8bbfc4f7-87fe-40c2-9e3e-ea4b7224ac7e","roots":{"p14520":"c430bab2-b33a-4aa4-b0b9-a4ff87af776a"},"root_ids":["p14520"]}];
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

<div id="f1a4acb3-ee0a-468d-9d1d-67f92f872b48" data-root-id="p14567" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"076a2b2b-a918-489d-b79a-ea1c73fbf9d6":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14616","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14617"}}},"roots":[{"type":"object","name":"Figure","id":"p14567","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p14576","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p14577","attributes":{"factors":["Alphainfluenzavirus influenzae (2955291)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p14578"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p14579"},"title":{"type":"object","name":"Title","id":"p14574","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14611","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14564","attributes":{"selected":{"type":"object","name":"Selection","id":"p14565","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14566"},"data":{"type":"map","entries":[["y",["Alphainfluenzavirus influenzae (2955291)"]],["share",[59.232491568177316]],["lo",[58.86943222571126]],["hi",[59.59454577203349]],["n",[70566]],["det",[41798]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p14612","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14613"}}},"glyph":{"type":"object","name":"Scatter","id":"p14608","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p14609","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p14610","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14575","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14590"},{"type":"object","name":"BoxZoomTool","id":"p14591","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14592","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14598","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14597","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14599","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14600"},{"type":"object","name":"SaveTool","id":"p14601"},{"type":"object","name":"HoverTool","id":"p14615","attributes":{"renderers":[{"id":"p14611"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p14585","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p14586"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p14587"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14588"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14580","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14581","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14582"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14583"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14584","attributes":{"axis":{"id":"p14580"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14589","attributes":{"dimension":1,"axis":{"id":"p14585"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p14602","attributes":{"source":{"id":"p14564"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p14614","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"076a2b2b-a918-489d-b79a-ea1c73fbf9d6","roots":{"p14567":"f1a4acb3-ee0a-468d-9d1d-67f92f872b48"},"root_ids":["p14567"]}];
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
"segment 7"[Title] OR ("matrix protein"[Title] AND M[Gene])
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `amplicon_disagrees_with_paper`.


## What reached the statistics

184,853 records were screened for this assay and **183,861 (99%)** were evaluable, meaning both primers landed in the right orientation and size range. 992 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 763 |
| `truncated` | 203 |
| `chance_anchor` | 2 |

