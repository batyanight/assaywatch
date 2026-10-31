# Leucocytozoon_cyt_c_Hellgren_2004

<span class="aw-chip aw-chip-declining">declining</span>

**For Leucocytozoon spp. (X-reacts weakly with haemoproteus) — cytochrome c**

| | |
|---|---|
| Target | Leucocytozoon ([taxid 195944](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=195944)) |
| Gene | cytochrome c |
| Chemistry | conventional |
| Amplicon | 478 bp |
| Designed | 2004 |
| Paper | [10.1645/GE-184R1](https://doi.org/10.1645/GE-184R1) |
| Registry status | active |

!!! quote "The paper"
    Hellgren O et al. 2004. J Parasitol 90:797-802 (HaemFL/HaemR2L)

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ATGGTGTTTTAGATACTTACATT` | 23 nt |
| reverse | `CATTATCTGGATGAGATAATGGNGC` | 25 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 30 | 114 | 26.3% | 19.1% – 35.1% |
| baseline (everything earlier) | 207 | 1,309 | 15.8% | 13.9% – 17.9% |

Change from baseline, Newcombe interval: **3.0% to 19.5%**. Threshold: **90.0%**.

*pooled share 26.3% has low coverage, but lineage Leucocytozoon sp. (1504291) (88 records) detects 34.1% (25.0%-44.5%), down from 92.6% on 122 earlier records; lineage verdict overrides to declining*

Trend across deposit years: by record rising (p=0.00222, 22 years); by footprint rising (p=0.463). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="a9b6f5b1-adda-405a-8d05-f140855449c6" data-root-id="p16313" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"7facee50-06c0-4902-a52f-7a8f2166db71":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p16368","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p16369"}}},"roots":[{"type":"object","name":"Figure","id":"p16313","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p16315"},"y_range":{"type":"object","name":"Range1d","id":"p16322","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p16323"},"y_scale":{"type":"object","name":"LinearScale","id":"p16324"},"title":{"type":"object","name":"Title","id":"p16320","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p16358","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p16310","attributes":{"selected":{"type":"object","name":"Selection","id":"p16311","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p16312"},"data":{"type":"map","entries":[["year",[2002,2005,2006,2007,2008,2009,2010,2011,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,0.0,100.0,0.0,82.85714285714286,100.0,0.0,0.0,9.375,1.3157894736842104,17.647058823529413,100.0,42.42424242424242,75.0,0.0,94.02985074626866,0.0,8.823529411764707,54.83870967741935,81.81818181818183,26.31578947368421,24.324324324324326]],["detected",[2,0,1,0,29,4,0,0,3,2,3,4,14,18,0,63,0,3,17,45,20,9]],["evaluable",[2,39,1,3,35,4,9,1,32,152,17,4,33,24,698,67,69,34,31,55,76,37]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,11.06545099688784,8.703135093227193,9.328625426046248,10.994220569835573,9.517227179437622,10.071067811865476,8.703135093227193,10.934913263353746,11.922851885492664,10.508782366508077,9.517227179437622,10.955310988645032,10.74264168206181,12.803669180140771,11.415029579131373,11.433709207718536,10.975067467348278,10.913832791890265,11.288829873700811,11.49483773413666,11.030852377887435]]]}}},"view":{"type":"object","name":"CDSView","id":"p16359","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16360"}}},"glyph":{"type":"object","name":"Line","id":"p16355","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p16356","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p16357","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p16364","attributes":{"data_source":{"id":"p16310"},"view":{"type":"object","name":"CDSView","id":"p16365","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16366"}}},"glyph":{"type":"object","name":"Scatter","id":"p16361","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p16362","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p16363","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p16321","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p16335"},{"type":"object","name":"BoxZoomTool","id":"p16336","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p16337","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p16343","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16342","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p16344","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p16345"},{"type":"object","name":"SaveTool","id":"p16346"},{"type":"object","name":"HoverTool","id":"p16367","attributes":{"renderers":[{"id":"p16364"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p16330","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16331","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16332"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16333"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p16325","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16326","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16327"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16328"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p16329","attributes":{"axis":{"id":"p16325"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p16334","attributes":{"dimension":1,"axis":{"id":"p16330"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p16347","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p16349","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p16350","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p16351","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p16353","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16352","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p16354","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"7facee50-06c0-4902-a52f-7a8f2166db71","roots":{"p16313":"a9b6f5b1-adda-405a-8d05-f140855449c6"},"root_ids":["p16313"]}];
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

<div id="bcf8e8e3-167f-46e3-a2a0-d3a5989ef47a" data-root-id="p16373" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"52b27366-9077-48fd-970f-e75b664a76d7":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p16413","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p16414"}}},"roots":[{"type":"object","name":"Figure","id":"p16373","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p16374"},"y_range":{"type":"object","name":"DataRange1d","id":"p16375","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p16382"},"y_scale":{"type":"object","name":"LinearScale","id":"p16383"},"title":{"type":"object","name":"Title","id":"p16380","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p16409","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p16370","attributes":{"selected":{"type":"object","name":"Selection","id":"p16371","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p16372"},"data":{"type":"map","entries":[["year",[2002,2005,2006,2007,2008,2009,2010,2011,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[2,39,1,3,35,4,9,1,32,152,17,4,33,24,698,67,69,34,31,55,76,37]],["detected",[2,0,1,0,29,4,0,0,3,2,3,4,14,18,0,63,0,3,17,45,20,9]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p16410","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16411"}}},"glyph":{"type":"object","name":"VBar","id":"p16406","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p16407","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p16408","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p16381","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p16394"},{"type":"object","name":"BoxZoomTool","id":"p16395","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p16396","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p16402","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16401","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p16403","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p16404"},{"type":"object","name":"SaveTool","id":"p16405"},{"type":"object","name":"HoverTool","id":"p16412","attributes":{"renderers":[{"id":"p16409"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p16389","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16390","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16391"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16392"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p16384","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16385","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16386"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16387"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p16388","attributes":{"axis":{"id":"p16384"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p16393","attributes":{"dimension":1,"axis":{"id":"p16389"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"52b27366-9077-48fd-970f-e75b664a76d7","roots":{"p16373":"bcf8e8e3-167f-46e3-a2a0-d3a5989ef47a"},"root_ids":["p16373"]}];
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

<div id="cefadc53-7474-4daa-b0e1-09f851f6ec23" data-root-id="p16418" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"52ee33f9-5312-4317-a3d1-ab70aa4efa44":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p16460","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p16461"}}},"roots":[{"type":"object","name":"Figure","id":"p16418","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p16420"},"y_range":{"type":"object","name":"FactorRange","id":"p16427","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p16428"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p16429"},"title":{"type":"object","name":"Title","id":"p16425","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p16455","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p16415","attributes":{"selected":{"type":"object","name":"Selection","id":"p16416","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p16417"},"data":{"type":"map","entries":[["x",[-1,-2,-16,-25,-16,-5,-24,-14,-7,-11,-18,-17,-8,-2,-12]],["y",["reverse","reverse","reverse","reverse","forward","forward","reverse","forward","forward","reverse","reverse","forward","forward","forward","reverse"]],["alpha",[0.39371047083626143,0.4056570625439213,0.3507027406886859,0.36503865073787767,0.2981377371749824,0.23601546029515108,0.20017568517217146,0.2527406886858749,0.4821152494729445,0.3554813773717498,0.37937456078706955,0.21929023190442726,0.5848559381588193,0.2240688685874912,0.4152143359100492]],["pos",[1,2,16,25,16,5,24,14,7,11,18,17,8,2,12]],["base",["C","G","G","C","T","A","A","T","T","G","T","T","C","T","A"]],["n",[102,107,84,90,62,36,21,43,139,86,96,29,182,31,111]],["det_with",["0% of 102","5% of 107","0% of 84","2% of 90","0% of 62","0% of 36","5% of 21","9% of 43","29% of 139","28% of 86","36% of 96","31% of 29","53% of 182","48% of 31","94% of 111"]],["det_without",["100% of 238","100% of 233","93% of 256","94% of 250","85% of 278","78% of 304","74% of 319","78% of 297","98% of 201","84% of 254","83% of 244","73% of 311","89% of 158","72% of 309","58% of 229"]],["subs",["C&gt;A 88, C&gt;T 12, C&gt;G 2","G&gt;A 107","G&gt;A 78, G&gt;T 6","C&gt;A 84, C&gt;G 6","T&gt;A 62","A&gt;G 32, A&gt;T 4","A&gt;G 21","T&gt;C 28, T&gt;A 15","T&gt;A 94, T&gt;C 45","G&gt;C 62, G&gt;A 24","T&gt;A 95, T&gt;C 1","T&gt;C 25, T&gt;A 4","C&gt;T 182","T&gt;C 31","A&gt;T 79, A&gt;G 32"]],["zone",["yes","yes","no","no","no","yes","no","no","no","no","no","no","no","yes","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p16456","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16457"}}},"glyph":{"type":"object","name":"Rect","id":"p16452","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p16453","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p16454","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p16426","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p16440"},{"type":"object","name":"BoxZoomTool","id":"p16441","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p16442","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p16448","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16447","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p16449","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p16450"},{"type":"object","name":"SaveTool","id":"p16451"},{"type":"object","name":"HoverTool","id":"p16458","attributes":{"renderers":[{"id":"p16455"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p16435","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p16436"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p16437"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16438"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p16430","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p16459","attributes":{"ticks":[-25,-24,-18,-17,-16,-14,-12,-11,-8,-7,-5,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16432"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-1,"1"],[-2,"2"],[-16,"16"],[-25,"25"],[-5,"5"],[-24,"24"],[-14,"14"],[-7,"7"],[-11,"11"],[-18,"18"],[-17,"17"],[-8,"8"],[-12,"12"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p16433"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p16434","attributes":{"axis":{"id":"p16430"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p16439","attributes":{"dimension":1,"axis":{"id":"p16435"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"52ee33f9-5312-4317-a3d1-ab70aa4efa44","roots":{"p16418":"cefadc53-7474-4daa-b0e1-09f851f6ec23"},"root_ids":["p16418"]}];
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

<div id="c7156f78-92c0-44ef-9da7-26c3827b98d8" data-root-id="p16465" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"225daa06-2938-4ccf-b8c7-59117eceac3a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p16514","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p16515"}}},"roots":[{"type":"object","name":"Figure","id":"p16465","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p16474","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p16475","attributes":{"factors":["Leucocytozoon sp. (1504291)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p16476"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p16477"},"title":{"type":"object","name":"Title","id":"p16472","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p16509","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p16462","attributes":{"selected":{"type":"object","name":"Selection","id":"p16463","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p16464"},"data":{"type":"map","entries":[["y",["Leucocytozoon sp. (1504291)"]],["share",[34.090909090909086]],["lo",[25.03913492660681]],["hi",[44.47354446727611]],["n",[88]],["det",[30]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p16510","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p16511"}}},"glyph":{"type":"object","name":"Scatter","id":"p16506","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p16507","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p16508","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p16473","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p16488"},{"type":"object","name":"BoxZoomTool","id":"p16489","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p16490","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p16496","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p16495","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p16497","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p16498"},{"type":"object","name":"SaveTool","id":"p16499"},{"type":"object","name":"HoverTool","id":"p16513","attributes":{"renderers":[{"id":"p16509"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p16483","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p16484"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p16485"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16486"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p16478","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p16479","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p16480"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p16481"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p16482","attributes":{"axis":{"id":"p16478"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p16487","attributes":{"dimension":1,"axis":{"id":"p16483"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p16500","attributes":{"source":{"id":"p16462"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p16512","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"225daa06-2938-4ccf-b8c7-59117eceac3a","roots":{"p16465":"c7156f78-92c0-44ef-9da7-26c3827b98d8"},"root_ids":["p16465"]}];
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

Disclosures on this entry: `cross_reactive`, `orientation_inferred`.


## What reached the statistics

7,910 records were screened for this assay and **1,423 (18%)** were evaluable, meaning both primers landed in the right orientation and size range. 6,487 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 6,297 |
| `truncated` | 177 |
| `chance_anchor` | 13 |

