# INFLUENZA_A_ssRNA_NP_Tsukamoto_2010

<span class="aw-chip aw-chip-declining">declining</span>

**Influenza A virus — nucleoprotein (NP) gene rRT-PCR (Tsukamoto 2010)**

| | |
|---|---|
| Target | Influenza A virus ([taxid 11320](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11320)) |
| Gene | NP (nucleoprotein) |
| Chemistry | hydrolysis_probe |
| Amplicon | 329 bp |
| Designed | 2010 |
| Paper | [10.1128/JCM.01264-10](https://doi.org/10.1128/JCM.01264-10) |
| Registry status | active |

!!! quote "The paper"
    Tsukamoto K, Noguchi D, Suzuki K, Shishido M, Ashizawa T, Kim MC, Lee YJ, Tada T. Broad detection of diverse H5 and H7 hemagglutinin genes of avian influenza viruses by real-time reverse transcription-PCR using primer and probe sets containing mixed bases. J Clin Microbiol 48(11):4275-4278 (2010).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `AGRTAYTGGGCYATAAGRAC` | 20 nt |
| reverse | `GCATTGTCTCCGAAGAAATAAG` | 22 nt |
| probe | `ATCGGGYTCGTYGCCTTTTCGTCY` | 24 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 42,373 | 69,645 | 60.8% | 60.5% – 61.2% |
| baseline (everything earlier) | 71,809 | 117,340 | 61.2% | 60.9% – 61.5% |

Change from baseline, Newcombe interval: **-0.8% to 0.1%**. Threshold: **90.0%**.

*pooled share 60.8% has low coverage, but lineage Alphainfluenzavirus influenzae (2955291) (69635 records) detects 60.9% (60.5%-61.2%), down from 61.2% on 117286 earlier records; lineage verdict overrides to declining*

Trend across deposit years: by record falling (p=1.77e-221, 41 years); by footprint falling (p=3.02e-09). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="f996391a-c48b-4522-b5b2-89f3c46bcf2f" data-root-id="p15445" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"8c62261c-ad3a-4a74-ac19-a32cfcba999c":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p15500","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p15501"}}},"roots":[{"type":"object","name":"Figure","id":"p15445","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p15447"},"y_range":{"type":"object","name":"Range1d","id":"p15454","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p15455"},"y_scale":{"type":"object","name":"LinearScale","id":"p15456"},"title":{"type":"object","name":"Title","id":"p15452","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p15490","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p15442","attributes":{"selected":{"type":"object","name":"Selection","id":"p15443","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p15444"},"data":{"type":"map","entries":[["year",[1982,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[0.0,0.0,66.66666666666666,73.33333333333333,73.33333333333333,25.0,88.88888888888889,84.26966292134831,75.0,100.0,0.0,50.0,76.47058823529412,86.66666666666667,88.63636363636364,68.75,82.0,66.97247706422019,90.0,23.178016726403825,50.847457627118644,52.97569153394803,79.84293193717278,81.86626369474878,83.36731721526361,80.32353912182238,71.5549215406562,81.50112176218641,69.5294365899979,74.81394437916177,62.5035201351732,47.344403599949295,57.56564630784854,47.11407103825137,82.85714285714286,86.14303959131546,30.57701044979555,53.713517951780254,66.95284469502819,61.60893294720427,55.53897003944983]],["detected",[0,0,2,11,22,2,8,75,6,4,0,1,13,26,39,22,41,73,117,194,990,632,915,2167,2862,2433,2508,3996,3295,3820,4439,3735,3968,5518,6235,2698,2692,7196,15675,22125,15627]],["evaluable",[1,1,3,15,30,8,9,89,8,4,3,2,17,30,44,32,50,109,130,837,1947,1193,1146,2647,3433,3029,3505,4903,4739,5106,7102,7889,6893,11712,7525,3132,8804,13397,23412,35912,28137]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.328625426046248,10.423139468338052,10.892023970177537,9.989711205477885,10.071067811865476,11.593955011284567,9.989711205477885,9.517227179437622,9.328625426046248,9.07684386569143,10.508782366508077,10.892023970177537,11.144342382561259,10.934913263353746,11.22734795681138,11.71979455772644,11.827897959955934,12.903590281597726,13.355661437762675,13.09579655945155,13.07417914509821,13.515367303104137,13.648709183305856,13.584709051861445,13.659282236339575,13.828839343981375,13.811774070052156,13.849154181151107,14.012994386941337,14.064670129752423,13.9982626799326,14.256851406239113,14.041472064430364,13.601839928618176,14.118373712354806,14.321483972358791,14.58604447722169,14.784790712526705,14.671860632843485]]]}}},"view":{"type":"object","name":"CDSView","id":"p15491","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15492"}}},"glyph":{"type":"object","name":"Line","id":"p15487","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p15488","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p15489","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p15496","attributes":{"data_source":{"id":"p15442"},"view":{"type":"object","name":"CDSView","id":"p15497","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15498"}}},"glyph":{"type":"object","name":"Scatter","id":"p15493","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p15494","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p15495","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p15453","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p15467"},{"type":"object","name":"BoxZoomTool","id":"p15468","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p15469","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p15475","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15474","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p15476","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p15477"},{"type":"object","name":"SaveTool","id":"p15478"},{"type":"object","name":"HoverTool","id":"p15499","attributes":{"renderers":[{"id":"p15496"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p15462","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15463","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15464"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15465"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p15457","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15458","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15459"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15460"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p15461","attributes":{"axis":{"id":"p15457"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p15466","attributes":{"dimension":1,"axis":{"id":"p15462"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p15479","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p15481","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p15482","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p15483","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p15485","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15484","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p15486","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"8c62261c-ad3a-4a74-ac19-a32cfcba999c","roots":{"p15445":"f996391a-c48b-4522-b5b2-89f3c46bcf2f"},"root_ids":["p15445"]}];
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

<div id="b926bb1f-0817-4a4d-827b-e7d373721b60" data-root-id="p15505" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"33ab9ff7-a741-474f-9412-32e15105ac4f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p15545","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p15546"}}},"roots":[{"type":"object","name":"Figure","id":"p15505","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p15506"},"y_range":{"type":"object","name":"DataRange1d","id":"p15507","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p15514"},"y_scale":{"type":"object","name":"LinearScale","id":"p15515"},"title":{"type":"object","name":"Title","id":"p15512","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p15541","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p15502","attributes":{"selected":{"type":"object","name":"Selection","id":"p15503","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p15504"},"data":{"type":"map","entries":[["year",[1982,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,3,15,30,8,9,89,8,4,3,2,17,30,44,32,50,109,130,837,1947,1193,1146,2647,3433,3029,3505,4903,4739,5106,7102,7889,6893,11712,7525,3132,8804,13397,23412,35912,28137]],["detected",[0,0,2,11,22,2,8,75,6,4,0,1,13,26,39,22,41,73,117,194,990,632,915,2167,2862,2433,2508,3996,3295,3820,4439,3735,3968,5518,6235,2698,2692,7196,15675,22125,15627]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p15542","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15543"}}},"glyph":{"type":"object","name":"VBar","id":"p15538","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p15539","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p15540","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p15513","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p15526"},{"type":"object","name":"BoxZoomTool","id":"p15527","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p15528","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p15534","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15533","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p15535","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p15536"},{"type":"object","name":"SaveTool","id":"p15537"},{"type":"object","name":"HoverTool","id":"p15544","attributes":{"renderers":[{"id":"p15541"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p15521","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15522","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15523"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15524"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p15516","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15517","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15518"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15519"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p15520","attributes":{"axis":{"id":"p15516"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p15525","attributes":{"dimension":1,"axis":{"id":"p15521"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"33ab9ff7-a741-474f-9412-32e15105ac4f","roots":{"p15505":"b926bb1f-0817-4a4d-827b-e7d373721b60"},"root_ids":["p15505"]}];
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

<div id="e63126e8-53be-432b-9f02-bb0d6325325a" data-root-id="p15550" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"87c237b8-070e-4aec-acba-c62ca69ba035":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p15592","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p15593"}}},"roots":[{"type":"object","name":"Figure","id":"p15550","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p15552"},"y_range":{"type":"object","name":"FactorRange","id":"p15559","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p15560"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p15561"},"title":{"type":"object","name":"Title","id":"p15557","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p15587","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p15547","attributes":{"selected":{"type":"object","name":"Selection","id":"p15548","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p15549"},"data":{"type":"map","entries":[["x",[-7,-20,-14,-1,-9,-5,-13,-2,-5,-10,-16,-15,-4,-1,-21,-14,-17,-9,-22,-7,-18,-11,-4,-22,-19,-19,-19,-20,-6,-8,-23,-17,-18,-20,-18,-4,-17]],["y",["probe","forward","probe","probe","probe","reverse","probe","reverse","forward","probe","probe","probe","reverse","reverse","reverse","reverse","forward","forward","probe","reverse","forward","reverse","probe","reverse","probe","reverse","forward","reverse","forward","reverse","probe","probe","reverse","probe","probe","forward","reverse"]],["alpha",[1.0,1.0,1.0,0.7265007888333289,0.17980239056608818,0.17698398267240686,0.16974703853250261,0.16036446773805385,0.15407305398828783,0.15245474235901274,0.15140011230847394,0.1504727651950691,0.15063641468566996,0.15165467818274192,0.1507091477926037,0.15094553039013825,0.15127282937133993,0.20711367221969676,0.15965531994545015,0.15069096451587025,0.1564732465171003,0.17103805118057597,0.1598735192662513,0.15056368157873626,0.1580551915929085,0.16109179880739097,0.2400254031072011,0.15740059363050513,0.15689146188196915,0.15205471027087733,0.1567278123913683,0.1518365109500762,0.15063641468566996,0.15087279728320452,0.15794609193250794,0.15874615610877876,0.15741877690723854]],["pos",[7,20,14,1,9,5,13,2,5,10,16,15,4,1,21,14,17,9,22,7,18,11,4,22,19,19,19,20,6,8,23,17,18,20,18,4,17]],["base",["T","A","T","Y","T","A","Y","A","A","C","C","G","T","G","C","T","T","Y","C","A","R","G","G","G","G","T","G","A","A","G","T","T","T","G","Y","G","G"]],["n",[65320,65624,55128,31705,1639,1484,1086,570,224,135,77,26,35,91,39,52,70,3141,531,38,356,1157,543,31,443,610,4951,407,379,113,370,101,35,48,437,481,408]],["det_with",["0% of 65320","1% of 65624","0% of 55128","2% of 31705","0% of 1639","0% of 1484","0% of 1086","0% of 570","0% of 224","0% of 135","0% of 77","0% of 26","3% of 35","15% of 91","28% of 39","35% of 52","36% of 70","37% of 3141","39% of 531","39% of 38","42% of 356","43% of 1157","45% of 543","45% of 31","56% of 443","56% of 610","60% of 4951","60% of 407","61% of 379","69% of 113","74% of 370","74% of 101","74% of 35","81% of 48","87% of 437","89% of 481","97% of 408"]],["det_without",["94% of 121601","94% of 121297","87% of 131793","73% of 155216","62% of 185282","62% of 185437","61% of 185835","61% of 186351","61% of 186697","61% of 186786","61% of 186844","61% of 186895","61% of 186886","61% of 186830","61% of 186882","61% of 186869","61% of 186851","62% of 183780","61% of 186390","61% of 186883","61% of 186565","61% of 185764","61% of 186378","61% of 186890","61% of 186478","61% of 186311","61% of 181970","61% of 186514","61% of 186542","61% of 186808","61% of 186551","61% of 186820","61% of 186886","61% of 186873","61% of 186484","61% of 186440","61% of 186513"]],["subs",["T&gt;C 65309, T&gt;A 6, T&gt;G 5","A&gt;G 65076, A&gt;C 548","T&gt;C 55078, T&gt;A 45, T&gt;G 3, T&gt;M 2","Y&gt;A 31678, Y&gt;G 27","T&gt;C 1637, T&gt;G 2","A&gt;G 1478, A&gt;T 5, A&gt;C 1","Y&gt;G 1039, Y&gt;A 47","A&gt;G 542, A&gt;C 23, A&gt;T 5","A&gt;C 219, A&gt;G 4, A&gt;T 1","C&gt;T 132, C&gt;A 2, C&gt;G 1","C&gt;A 38, C&gt;T 36, C&gt;G 3","G&gt;A 19, G&gt;C 6, G&gt;T 1","T&gt;A 33, T&gt;C 1, T&gt;G 1","G&gt;T 65, G&gt;A 23, G&gt;C 3","C&gt;G 18, C&gt;T 16, C&gt;A 5","T&gt;C 48, T&gt;A 4","T&gt;C 66, T&gt;A 3, T&gt;G 1","Y&gt;A 2665, Y&gt;G 476","C&gt;T 491, C&gt;A 35, C&gt;G 5","A&gt;G 34, A&gt;T 4","R&gt;T 219, R&gt;C 137","G&gt;A 1148, G&gt;C 7, G&gt;T 2","G&gt;A 541, G&gt;T 1, G&gt;C 1","G&gt;T 22, G&gt;C 6, G&gt;A 3","G&gt;C 425, G&gt;A 10, G&gt;T 8","T&gt;C 510, T&gt;G 76, T&gt;A 24","G&gt;A 4930, G&gt;T 18, G&gt;C 3","A&gt;G 358, A&gt;T 37, A&gt;C 12","A&gt;T 202, A&gt;C 176, A&gt;G 1","G&gt;A 108, G&gt;T 4, G&gt;C 1","T&gt;C 362, T&gt;G 7, T&gt;A 1","T&gt;C 57, T&gt;G 34, T&gt;A 10","T&gt;G 22, T&gt;C 10, T&gt;A 3","G&gt;A 46, G&gt;C 1, G&gt;T 1","Y&gt;G 370, Y&gt;A 67","G&gt;A 479, G&gt;T 2","G&gt;A 401, G&gt;T 7"]],["zone",["no","no","no","yes","no","yes","no","yes","yes","no","no","no","yes","yes","no","no","no","no","no","no","no","no","yes","no","no","no","no","no","no","no","no","no","no","no","no","yes","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p15588","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15589"}}},"glyph":{"type":"object","name":"Rect","id":"p15584","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p15585","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p15586","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p15558","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p15572"},{"type":"object","name":"BoxZoomTool","id":"p15573","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p15574","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p15580","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15579","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p15581","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p15582"},{"type":"object","name":"SaveTool","id":"p15583"},{"type":"object","name":"HoverTool","id":"p15590","attributes":{"renderers":[{"id":"p15587"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p15567","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p15568"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p15569"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15570"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p15562","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p15591","attributes":{"ticks":[-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-11,-10,-9,-8,-7,-6,-5,-4,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15564"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-7,"7"],[-20,"20"],[-14,"14"],[-1,"1"],[-9,"9"],[-5,"5"],[-13,"13"],[-2,"2"],[-10,"10"],[-16,"16"],[-15,"15"],[-4,"4"],[-21,"21"],[-17,"17"],[-22,"22"],[-18,"18"],[-11,"11"],[-19,"19"],[-6,"6"],[-8,"8"],[-23,"23"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p15565"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p15566","attributes":{"axis":{"id":"p15562"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p15571","attributes":{"dimension":1,"axis":{"id":"p15567"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"87c237b8-070e-4aec-acba-c62ca69ba035","roots":{"p15550":"e63126e8-53be-432b-9f02-bb0d6325325a"},"root_ids":["p15550"]}];
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

<div id="fd9d0439-0fe5-495f-abfd-ce9105280233" data-root-id="p15597" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"7c08c02b-110c-489f-b757-7c269b1a002f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p15646","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p15647"}}},"roots":[{"type":"object","name":"Figure","id":"p15597","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p15606","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p15607","attributes":{"factors":["Alphainfluenzavirus influenzae (2955291)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p15608"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p15609"},"title":{"type":"object","name":"Title","id":"p15604","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p15641","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p15594","attributes":{"selected":{"type":"object","name":"Selection","id":"p15595","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p15596"},"data":{"type":"map","entries":[["y",["Alphainfluenzavirus influenzae (2955291)"]],["share",[60.850147196093914]],["lo",[60.48703967026354]],["hi",[61.21205767749394]],["n",[69635]],["det",[42373]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p15642","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15643"}}},"glyph":{"type":"object","name":"Scatter","id":"p15638","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p15639","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p15640","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p15605","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p15620"},{"type":"object","name":"BoxZoomTool","id":"p15621","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p15622","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p15628","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15627","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p15629","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p15630"},{"type":"object","name":"SaveTool","id":"p15631"},{"type":"object","name":"HoverTool","id":"p15645","attributes":{"renderers":[{"id":"p15641"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p15615","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p15616"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p15617"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15618"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p15610","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15611","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15612"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15613"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p15614","attributes":{"axis":{"id":"p15610"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p15619","attributes":{"dimension":1,"axis":{"id":"p15615"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p15632","attributes":{"source":{"id":"p15594"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p15644","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"7c08c02b-110c-489f-b757-7c269b1a002f","roots":{"p15597":"fd9d0439-0fe5-495f-abfd-ce9105280233"},"root_ids":["p15597"]}];
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
"segment 5"[Title] OR nucleoprotein[Title] OR NP[Gene]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `retrieval_scope_incomplete`.


## What reached the statistics

191,509 records were screened for this assay and **186,985 (98%)** were evaluable, meaning both primers landed in the right orientation and size range. 4,524 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `truncated` | 3,314 |
| `no_site` | 1,196 |
| `chance_anchor` | 2 |

