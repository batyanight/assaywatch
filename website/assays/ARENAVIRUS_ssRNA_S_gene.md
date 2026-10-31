# ARENAVIRUS_ssRNA_S_gene

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**ARENAVIRUS (ssRNA) — S gene**

| | |
|---|---|
| Target | Arenaviridae ([taxid 11617](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11617)) |
| Gene | S gene |
| Chemistry | conventional |
| Amplicon | 630 bp |
| Designed | 1997 |
| Paper | [10.1016/S0168-1702(97)01458-5](https://doi.org/10.1016/S0168-1702(97)01458-5) |
| Registry status | active |

!!! quote "The paper"
    Lozano, M. E. et al. Characterization of arenaviruses using a family-specific primer set for RT-PCR amplification and RFLP analysis - Its potential use for detection of uncharacterized arenaviruses. Virus Res 49, 79-89, doi:Doi 10.1016/S0168-1702(97)01458-5 (1997).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GGCATWGANCCAAACTGATT` | 20 nt |
| reverse | `CGCACCGGGGATCCTAGGC` | 19 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 9 | 69 | 13.0% | 7.0% – 23.0% |
| baseline (everything earlier) | 388 | 989 | 39.2% | 36.2% – 42.3% |

Change from baseline, Newcombe interval: **-33.0% to -15.8%**. Threshold: **90.0%**.

*detected share 13.0% (7%-23%) since Oct 2024, upper bound below the 90% threshold; change from baseline -33% to -16% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 39%)*

Trend across deposit years: by record falling (p=4.23e-05, 39 years); by footprint falling (p=0.000437). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="e646657d-f21a-4ae8-97c5-aa7e64c500e9" data-root-id="p2811" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"8593ecd7-b19a-43ca-aec5-470b4306c5fc":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p2866","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p2867"}}},"roots":[{"type":"object","name":"Figure","id":"p2811","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p2813"},"y_range":{"type":"object","name":"Range1d","id":"p2820","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p2821"},"y_scale":{"type":"object","name":"LinearScale","id":"p2822"},"title":{"type":"object","name":"Title","id":"p2818","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p2856","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p2808","attributes":{"selected":{"type":"object","name":"Selection","id":"p2809","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p2810"},"data":{"type":"map","entries":[["year",[1985,1986,1987,1989,1990,1992,1993,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,87.5,33.33333333333333,100.0,57.14285714285714,0.0,100.0,25.0,57.14285714285714,0.0,100.0,33.33333333333333,66.66666666666666,30.0,29.545454545454547,66.66666666666666,40.909090909090914,40.909090909090914,30.23255813953488,47.61904761904761,24.0,33.33333333333333,51.5625,30.0,46.666666666666664,50.0,53.57142857142857,41.30434782608695,10.0,36.84210526315789,33.33333333333333,26.08695652173913,37.03703703703704,36.708860759493675,42.30769230769231,9.090909090909092,17.647058823529413]],["detected",[2,1,1,7,1,1,4,0,2,1,4,0,1,1,12,3,13,2,9,9,13,30,6,15,33,3,70,14,15,19,7,14,9,6,20,29,11,3,6]],["evaluable",[2,1,1,8,3,1,7,1,2,4,7,12,1,3,18,10,44,3,22,22,43,63,25,45,64,10,150,28,28,46,70,38,27,23,54,79,26,33,34]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,8.703135093227193,8.703135093227193,9.989711205477885,9.328625426046248,8.703135093227193,9.897626379762722,8.703135093227193,9.07684386569143,9.517227179437622,9.897626379762722,10.269703144398052,8.703135093227193,9.328625426046248,10.547770533331066,10.143865699252444,11.144342382561259,9.328625426046248,10.683957047019447,10.683957047019447,11.129349107533436,11.375828278421016,10.770092258092593,11.15897945775324,11.385871088686695,10.143865699252444,11.914842886014831,10.846014908695619,10.846014908695619,11.173276359477448,11.442834756050653,11.048392086352559,10.821697436206254,10.713966621835368,11.27702043233893,11.51922823234585,10.796415465069488,10.955310988645032,10.975067467348278]]]}}},"view":{"type":"object","name":"CDSView","id":"p2857","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p2858"}}},"glyph":{"type":"object","name":"Line","id":"p2853","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p2854","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p2855","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p2862","attributes":{"data_source":{"id":"p2808"},"view":{"type":"object","name":"CDSView","id":"p2863","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p2864"}}},"glyph":{"type":"object","name":"Scatter","id":"p2859","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p2860","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p2861","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p2819","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p2833"},{"type":"object","name":"BoxZoomTool","id":"p2834","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p2835","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p2841","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p2840","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p2842","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p2843"},{"type":"object","name":"SaveTool","id":"p2844"},{"type":"object","name":"HoverTool","id":"p2865","attributes":{"renderers":[{"id":"p2862"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p2828","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p2829","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p2830"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p2831"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p2823","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p2824","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p2825"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p2826"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p2827","attributes":{"axis":{"id":"p2823"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p2832","attributes":{"dimension":1,"axis":{"id":"p2828"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p2845","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p2847","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p2848","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p2849","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p2851","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p2850","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p2852","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"8593ecd7-b19a-43ca-aec5-470b4306c5fc","roots":{"p2811":"e646657d-f21a-4ae8-97c5-aa7e64c500e9"},"root_ids":["p2811"]}];
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

<div id="e3d1bc1b-c9d0-4db6-a757-408ba2b2b014" data-root-id="p2871" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"c9434711-e422-41f5-a7f9-108703d94efb":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p2911","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p2912"}}},"roots":[{"type":"object","name":"Figure","id":"p2871","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p2872"},"y_range":{"type":"object","name":"DataRange1d","id":"p2873","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p2880"},"y_scale":{"type":"object","name":"LinearScale","id":"p2881"},"title":{"type":"object","name":"Title","id":"p2878","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p2907","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p2868","attributes":{"selected":{"type":"object","name":"Selection","id":"p2869","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p2870"},"data":{"type":"map","entries":[["year",[1985,1986,1987,1989,1990,1992,1993,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[2,1,1,8,3,1,7,1,2,4,7,12,1,3,18,10,44,3,22,22,43,63,25,45,64,10,150,28,28,46,70,38,27,23,54,79,26,33,34]],["detected",[2,1,1,7,1,1,4,0,2,1,4,0,1,1,12,3,13,2,9,9,13,30,6,15,33,3,70,14,15,19,7,14,9,6,20,29,11,3,6]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p2908","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p2909"}}},"glyph":{"type":"object","name":"VBar","id":"p2904","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p2905","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p2906","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p2879","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p2892"},{"type":"object","name":"BoxZoomTool","id":"p2893","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p2894","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p2900","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p2899","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p2901","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p2902"},{"type":"object","name":"SaveTool","id":"p2903"},{"type":"object","name":"HoverTool","id":"p2910","attributes":{"renderers":[{"id":"p2907"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p2887","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p2888","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p2889"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p2890"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p2882","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p2883","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p2884"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p2885"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p2886","attributes":{"axis":{"id":"p2882"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p2891","attributes":{"dimension":1,"axis":{"id":"p2887"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"c9434711-e422-41f5-a7f9-108703d94efb","roots":{"p2871":"e3d1bc1b-c9d0-4db6-a757-408ba2b2b014"},"root_ids":["p2871"]}];
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

<div id="e3fe0ea6-7dd5-45db-bf95-77ab6f191b95" data-root-id="p2916" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"5d400d83-1427-491b-ab3f-1334b752909c":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p2958","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p2959"}}},"roots":[{"type":"object","name":"Figure","id":"p2916","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p2918"},"y_range":{"type":"object","name":"FactorRange","id":"p2925","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p2926"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p2927"},"title":{"type":"object","name":"Title","id":"p2923","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p2953","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p2913","attributes":{"selected":{"type":"object","name":"Selection","id":"p2914","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p2915"},"data":{"type":"map","entries":[["x",[-3,-1,-5,-2,-5,-1,-7,-7,-17,-18,-19,-19,-6,-18,-16,-11,-8,-20,-9,-13,-12,-15,-14]],["y",["forward","reverse","reverse","reverse","forward","forward","forward","reverse","forward","reverse","reverse","forward","forward","forward","forward","forward","forward","forward","forward","forward","reverse","forward","reverse"]],["alpha",[0.7252362948960303,0.3749527410207939,0.36852551984877124,0.2978260869565217,0.29461247637051036,0.272117202268431,0.2656899810964083,0.23034026465028357,0.3074669187145558,0.22391304347826085,0.30103969754253307,0.62882797731569,0.9887523629489603,0.6416824196597353,0.5549149338374291,0.5227788279773157,0.5002835538752363,0.4906427221172023,0.7413043478260869,1.0,1.0,0.7862948960302458,1.0]],["pos",[3,1,5,2,5,1,7,7,17,18,19,19,6,18,16,11,8,20,9,13,12,15,14]],["base",["A","C","T","G","T","T","A","C","A","G","C","G","C","C","T","C","A","G","A","A","G","W","C"]],["n",[179,70,68,46,45,38,36,25,49,23,47,149,261,153,126,116,109,106,184,489,592,198,558]],["det_with",["5% of 179","0% of 70","0% of 68","0% of 46","0% of 45","0% of 38","0% of 36","0% of 25","2% of 49","13% of 23","32% of 47","39% of 149","45% of 261","44% of 153","45% of 126","50% of 116","51% of 109","53% of 106","54% of 184","57% of 489","58% of 592","67% of 198","64% of 558"]],["det_without",["76% of 561","65% of 670","64% of 672","62% of 694","62% of 695","62% of 702","62% of 704","61% of 715","63% of 691","60% of 717","60% of 693","63% of 591","66% of 479","62% of 587","61% of 614","60% of 624","60% of 631","59% of 634","60% of 556","62% of 251","61% of 148","55% of 542","42% of 182"]],["subs",["A&gt;G 168, A&gt;T 9, A&gt;C 2","C&gt;T 45, C&gt;G 25","T&gt;G 45, T&gt;C 23","G&gt;T 46","T&gt;A 41, T&gt;G 4","T&gt;A 33, T&gt;C 4, T&gt;G 1","A&gt;T 34, A&gt;C 2","C&gt;T 22, C&gt;G 3","A&gt;G 48, A&gt;T 1","G&gt;C 13, G&gt;T 6, G&gt;A 4","C&gt;T 27, C&gt;A 10, C&gt;G 9, C&gt;R 1","G&gt;T 115, G&gt;A 22, G&gt;C 12","C&gt;T 249, C&gt;G 9, C&gt;A 3","C&gt;A 65, C&gt;T 58, C&gt;G 30","T&gt;C 73, T&gt;A 46, T&gt;G 7","C&gt;T 95, C&gt;G 16, C&gt;A 5","A&gt;T 89, A&gt;C 10, A&gt;G 10","G&gt;C 85, G&gt;A 15, G&gt;T 6","A&gt;G 168, A&gt;C 16","A&gt;T 396, A&gt;C 90, A&gt;G 3","G&gt;T 448, G&gt;A 142, G&gt;C 1, G&gt;W 1","W&gt;G 170, W&gt;C 28","C&gt;A 530, C&gt;G 21, C&gt;T 6, C&gt;R 1"]],["zone",["yes","yes","yes","yes","yes","yes","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p2954","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p2955"}}},"glyph":{"type":"object","name":"Rect","id":"p2950","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p2951","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p2952","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p2924","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p2938"},{"type":"object","name":"BoxZoomTool","id":"p2939","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p2940","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p2946","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p2945","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p2947","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p2948"},{"type":"object","name":"SaveTool","id":"p2949"},{"type":"object","name":"HoverTool","id":"p2956","attributes":{"renderers":[{"id":"p2953"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p2933","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p2934"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p2935"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p2936"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p2928","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p2957","attributes":{"ticks":[-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-9,-8,-7,-6,-5,-3,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p2930"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-3,"3"],[-1,"1"],[-5,"5"],[-2,"2"],[-7,"7"],[-17,"17"],[-18,"18"],[-19,"19"],[-6,"6"],[-16,"16"],[-11,"11"],[-8,"8"],[-20,"20"],[-9,"9"],[-13,"13"],[-12,"12"],[-15,"15"],[-14,"14"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p2931"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p2932","attributes":{"axis":{"id":"p2928"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p2937","attributes":{"dimension":1,"axis":{"id":"p2933"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"5d400d83-1427-491b-ab3f-1334b752909c","roots":{"p2916":"e3fe0ea6-7dd5-45db-bf95-77ab6f191b95"},"root_ids":["p2916"]}];
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

This entry declares **`scope_taxids`**: [208898](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=208898), [1653394](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1653394). A record counts toward the denominator when its taxid, or any ancestor, is in that set. Records outside it are screened and reported but kept out of the statistics.

473 screened records fell outside the declared scope.

Disclosures on this entry: `orientation_inferred`.


## What reached the statistics

5,755 records were screened for this assay and **1,058 (18%)** were evaluable, meaning both primers landed in the right orientation and size range. 4,697 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 3,948 |
| `chance_anchor` | 367 |
| `truncated` | 320 |
| `no_pair` | 46 |
| `chance_only` | 13 |

