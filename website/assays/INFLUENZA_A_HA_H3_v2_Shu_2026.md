# INFLUENZA_A_HA_H3_v2_Shu_2026

<span class="aw-chip aw-chip-stable">stable</span>

**Influenza A virus H3 subtype — hemagglutinin rRT-PCR, redesigned (CDC H3_v2, Shu 2026)**

| | |
|---|---|
| Target | Influenza A virus ([taxid 11320](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11320)) |
| Gene | HA (hemagglutinin), H3 |
| Chemistry | hydrolysis_probe |
| Amplicon | 103 bp |
| Designed | 2026 |
| Paper | [10.1128/jcm.00727-26](https://doi.org/10.1128/jcm.00727-26) |
| Registry status | draft |

!!! quote "The paper"
    Shu B et al. 2026. J Clin Microbiol

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `AAGCATTCCYAATGACAAACC` | 21 nt |
| reverse | `CATYCCTGTTGCCAATTTCAG` | 21 nt |
| probe | `CAGGATCACATAYGGGGCMTGTCCCAG` | 27 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 25,204 | 26,920 | 93.6% | 93.3% – 93.9% |
| baseline (everything earlier) | 60,487 | 72,235 | 83.7% | 83.5% – 84.0% |

Change from baseline, Newcombe interval: **9.5% to 10.3%**. Threshold: **90.0%**.

*detected share 93.6% (93%-94%) since Oct 2024*

Trend across deposit years: by record rising (p=6.98e-274, 41 years); by footprint falling (p=0.0431); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="b70e7ef5-3ea6-4294-88bd-d47fc0aca90b" data-root-id="p14209" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"85d4c257-d90f-4f03-9fb3-45902df7824b":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14264","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14265"}}},"roots":[{"type":"object","name":"Figure","id":"p14209","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p14211"},"y_range":{"type":"object","name":"Range1d","id":"p14218","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p14219"},"y_scale":{"type":"object","name":"LinearScale","id":"p14220"},"title":{"type":"object","name":"Title","id":"p14216","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14254","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14206","attributes":{"selected":{"type":"object","name":"Selection","id":"p14207","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14208"},"data":{"type":"map","entries":[["year",[1982,1983,1987,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[0.0,0.0,0.0,4.761904761904762,0.0,20.0,0.0,41.17647058823529,63.888888888888886,47.368421052631575,0.0,88.88888888888889,77.77777777777779,88.7218045112782,48.38709677419355,83.7037037037037,70.70707070707071,77.58620689655173,77.7439024390244,85.95213319458897,86.4039408866995,88.6021505376344,88.3433900164564,76.46520146520146,70.16806722689076,64.04391582799634,82.12824010914052,77.36292428198433,69.59719789842381,86.29673826571201,81.71926006528835,88.52014900101591,88.7622521085024,90.30916400942742,65.16598453842656,57.79702970297029,86.16904500548847,83.3038158106585,88.36093660765277,94.95716945996276,92.7226300670284]],["detected",[0,0,0,1,0,1,0,14,23,9,0,232,35,118,15,113,70,45,255,826,877,1236,3221,835,668,700,3010,2963,1987,4339,3004,5228,3894,6514,1433,467,6280,5174,7736,12748,11620]],["evaluable",[1,1,5,21,2,5,7,34,36,19,2,261,45,133,31,135,99,58,328,961,1015,1395,3646,1092,952,1093,3665,3830,2855,5028,3676,5906,4387,7213,2199,808,7288,6211,8755,13425,12532]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.667366891029102,10.652487636092928,9.07684386569143,9.667366891029102,9.897626379762722,10.975067467348278,11.012804945939648,10.584573151575475,9.07684386569143,12.244324328094164,11.15897945775324,11.841810898176924,10.913832791890265,11.85090236694855,11.660254037844386,11.322938200602813,12.377094296675775,12.978946677928755,13.008613425380037,13.179495835117699,13.679344272137898,13.048159236832515,12.973831887291771,13.048653295339395,13.681985373312163,13.70433574770415,13.554333473867663,13.841450128581656,13.683507885836075,13.92172945423226,13.77295992160775,14.020635346909842,13.419240232404432,12.88426593330566,14.025728944415182,13.946724906400682,14.115648601066756,14.322484977743292,14.289436478041369]]]}}},"view":{"type":"object","name":"CDSView","id":"p14255","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14256"}}},"glyph":{"type":"object","name":"Line","id":"p14251","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p14252","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p14253","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p14260","attributes":{"data_source":{"id":"p14206"},"view":{"type":"object","name":"CDSView","id":"p14261","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14262"}}},"glyph":{"type":"object","name":"Scatter","id":"p14257","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p14258","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p14259","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14217","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14231"},{"type":"object","name":"BoxZoomTool","id":"p14232","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14233","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14239","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14238","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14240","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14241"},{"type":"object","name":"SaveTool","id":"p14242"},{"type":"object","name":"HoverTool","id":"p14263","attributes":{"renderers":[{"id":"p14260"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p14226","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14227","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14228"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14229"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14221","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14222","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14223"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14224"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14225","attributes":{"axis":{"id":"p14221"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14230","attributes":{"dimension":1,"axis":{"id":"p14226"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p14243","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p14245","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p14246","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p14247","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p14249","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14248","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p14250","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"85d4c257-d90f-4f03-9fb3-45902df7824b","roots":{"p14209":"b70e7ef5-3ea6-4294-88bd-d47fc0aca90b"},"root_ids":["p14209"]}];
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

<div id="aec6ece0-23e8-4b13-ad3a-da36152ec6ea" data-root-id="p14269" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"1981b886-e669-4124-8d93-da984aa64a4a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14309","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14310"}}},"roots":[{"type":"object","name":"Figure","id":"p14269","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p14270"},"y_range":{"type":"object","name":"DataRange1d","id":"p14271","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p14278"},"y_scale":{"type":"object","name":"LinearScale","id":"p14279"},"title":{"type":"object","name":"Title","id":"p14276","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14305","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14266","attributes":{"selected":{"type":"object","name":"Selection","id":"p14267","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14268"},"data":{"type":"map","entries":[["year",[1982,1983,1987,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,5,21,2,5,7,34,36,19,2,261,45,133,31,135,99,58,328,961,1015,1395,3646,1092,952,1093,3665,3830,2855,5028,3676,5906,4387,7213,2199,808,7288,6211,8755,13425,12532]],["detected",[0,0,0,1,0,1,0,14,23,9,0,232,35,118,15,113,70,45,255,826,877,1236,3221,835,668,700,3010,2963,1987,4339,3004,5228,3894,6514,1433,467,6280,5174,7736,12748,11620]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p14306","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14307"}}},"glyph":{"type":"object","name":"VBar","id":"p14302","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p14303","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p14304","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14277","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14290"},{"type":"object","name":"BoxZoomTool","id":"p14291","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14292","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14298","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14297","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14299","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14300"},{"type":"object","name":"SaveTool","id":"p14301"},{"type":"object","name":"HoverTool","id":"p14308","attributes":{"renderers":[{"id":"p14305"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p14285","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14286","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14287"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14288"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14280","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14281","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14282"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14283"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14284","attributes":{"axis":{"id":"p14280"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14289","attributes":{"dimension":1,"axis":{"id":"p14285"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"1981b886-e669-4124-8d93-da984aa64a4a","roots":{"p14269":"aec6ece0-23e8-4b13-ad3a-da36152ec6ea"},"root_ids":["p14269"]}];
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

<div id="ca1fd89b-f309-48a9-af5f-cf4061614f3b" data-root-id="p14314" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b86131a1-ebf3-4223-88d0-c00ad0389419":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14356","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14357"}}},"roots":[{"type":"object","name":"Figure","id":"p14314","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p14316"},"y_range":{"type":"object","name":"FactorRange","id":"p14323","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p14324"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p14325"},"title":{"type":"object","name":"Title","id":"p14321","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14351","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14311","attributes":{"selected":{"type":"object","name":"Selection","id":"p14312","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14313"},"data":{"type":"map","entries":[["x",[-3,-12,-1,-3,-18,-11,-4,-10,-25,-7,-14,-15,-6,-27,-15,-1,-21,-9,-2,-24,-3,-19,-6,-9,-13,-12,-9,-18,-20,-6,-14,-17,-21,-10,-18,-11,-7,-26,-5,-23,-5,-8,-12,-13,-20]],["y",["forward","probe","probe","reverse","probe","probe","forward","probe","probe","reverse","forward","reverse","reverse","probe","forward","reverse","probe","forward","probe","probe","probe","forward","forward","reverse","reverse","reverse","probe","reverse","probe","probe","reverse","forward","forward","forward","forward","forward","forward","probe","probe","probe","reverse","forward","forward","forward","forward"]],["alpha",[0.3696258383339216,0.35508698502344815,0.3522409359084262,0.27882658464020976,0.24374817205385507,0.1832610559225455,0.16968231556653723,0.1621728606726842,0.4547672835459634,0.29058796833240885,0.2672023599415057,0.2532807221017599,0.3151737179163935,0.18535273057334475,0.37593515203469313,0.2601386717765115,0.2131617165044627,0.21377893197519035,0.16128132721496646,0.2571897534163683,0.18850738742373052,0.15154303867681912,0.19018758509404468,0.19855428369724168,0.15150874892844535,0.2567439866875095,0.16152135545358276,0.1510629821995865,0.15257173112803185,0.2191624224698704,0.15120014119308153,0.152125964399173,0.28846200393323584,0.1539433210629822,0.15990973728001612,0.15078866421259643,0.1633730018657657,0.1514744591800716,0.1507200847158489,0.1582981191064495,0.15161161817356664,0.16731632292874793,0.3428112551056427,0.15332610559225454,0.15620644445565024]],["pos",[3,12,1,3,18,11,4,10,25,7,14,15,6,27,15,1,21,9,2,24,3,19,6,9,13,12,9,18,20,6,14,17,21,10,18,11,7,26,5,23,5,8,12,13,20]],["base",["A","G","G","C","A","G","A","C","G","A","C","T","T","C","T","G","C","T","A","G","C","G","C","C","T","T","M","Y","A","T","G","A","A","A","C","A","A","A","C","A","T","G","Y","C","A"]],["n",[6405,5981,5898,3757,2734,970,574,355,8888,4100,3418,3012,4817,1031,6589,3212,1842,1860,329,3126,1123,45,1172,1416,44,3113,336,31,75,2017,35,62,4038,115,289,23,390,43,21,242,47,505,5623,97,181]],["det_with",["0% of 6405","0% of 5981","1% of 5898","0% of 3757","0% of 2734","0% of 970","0% of 574","0% of 355","9% of 8888","5% of 4100","5% of 3418","5% of 3012","9% of 4817","6% of 1031","11% of 6589","9% of 3212","9% of 1842","10% of 1860","12% of 329","15% of 3126","15% of 1123","16% of 45","18% of 1172","19% of 1416","20% of 44","30% of 3113","34% of 336","35% of 31","36% of 75","37% of 2017","37% of 35","42% of 62","46% of 4038","47% of 115","47% of 289","52% of 23","55% of 390","56% of 43","57% of 21","58% of 242","64% of 47","67% of 505","80% of 5623","82% of 97","97% of 181"]],["det_without",["91% of 93782","91% of 94206","91% of 94289","89% of 96430","88% of 97453","86% of 99217","86% of 99613","86% of 99832","93% of 91299","89% of 96087","88% of 96769","88% of 97175","89% of 95370","86% of 99156","91% of 93598","88% of 96975","87% of 98345","87% of 98327","86% of 99858","88% of 97061","86% of 99064","86% of 100142","86% of 99015","86% of 98771","86% of 100143","87% of 97074","86% of 99851","86% of 100156","86% of 100112","87% of 98170","86% of 100152","86% of 100125","87% of 96149","86% of 100072","86% of 99898","86% of 100164","86% of 99797","86% of 100144","86% of 100166","86% of 99945","86% of 100140","86% of 99682","86% of 94564","86% of 100090","86% of 100006"]],["subs",["A&gt;G 6398, A&gt;C 6, A&gt;T 1","G&gt;A 5904, G&gt;T 75, G&gt;C 2","G&gt;A 5878, G&gt;T 15, G&gt;C 5","C&gt;T 3675, C&gt;A 78, C&gt;G 3, C&gt;W 1","A&gt;C 1822, A&gt;T 617, A&gt;G 295","G&gt;A 499, G&gt;C 371, G&gt;T 100","A&gt;G 567, A&gt;T 6, A&gt;C 1","C&gt;A 207, C&gt;T 142, C&gt;G 6","G&gt;A 8879, G&gt;T 5, G&gt;M 3, G&gt;C 1","A&gt;G 4081, A&gt;T 16, A&gt;C 3","C&gt;T 3385, C&gt;A 32, C&gt;G 1","T&gt;A 2370, T&gt;G 452, T&gt;C 190","T&gt;C 4814, T&gt;A 3","C&gt;T 1029, C&gt;A 2","T&gt;C 6047, T&gt;A 537, T&gt;G 5","G&gt;A 3202, G&gt;T 8, G&gt;C 2","C&gt;T 1353, C&gt;A 487, C&gt;G 2","T&gt;C 1852, T&gt;A 7, T&gt;G 1","A&gt;C 323, A&gt;G 4, A&gt;T 2","G&gt;A 3125, G&gt;T 1","C&gt;T 1010, C&gt;A 112, C&gt;G 1","G&gt;A 44, G&gt;C 1","C&gt;A 680, C&gt;T 462, C&gt;G 30","C&gt;T 1406, C&gt;A 10","T&gt;A 32, T&gt;G 8, T&gt;C 4","T&gt;A 1560, T&gt;G 1348, T&gt;C 204, T&gt;R 1","M&gt;T 202, M&gt;G 134","Y&gt;A 21, Y&gt;G 10","A&gt;G 67, A&gt;T 5, A&gt;C 3","T&gt;C 2016, T&gt;G 1","G&gt;A 35","A&gt;G 46, A&gt;T 8, A&gt;C 8","A&gt;G 1839, A&gt;T 1117, A&gt;C 1082","A&gt;G 90, A&gt;C 20, A&gt;T 5","C&gt;T 288, C&gt;A 1","A&gt;G 11, A&gt;C 7, A&gt;T 5","A&gt;G 382, A&gt;T 6, A&gt;C 2","A&gt;C 34, A&gt;G 6, A&gt;T 3","C&gt;T 18, C&gt;G 3","A&gt;G 242","T&gt;C 43, T&gt;A 3, T&gt;G 1","G&gt;A 490, G&gt;T 13, G&gt;C 2","Y&gt;A 5613, Y&gt;G 10","C&gt;T 78, C&gt;A 18, C&gt;G 1","A&gt;G 179, A&gt;T 2"]],["zone",["yes","no","yes","yes","no","no","yes","no","no","no","no","no","no","no","no","yes","no","no","yes","no","yes","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","yes","no","yes","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p14352","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14353"}}},"glyph":{"type":"object","name":"Rect","id":"p14348","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p14349","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p14350","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14322","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14336"},{"type":"object","name":"BoxZoomTool","id":"p14337","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14338","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14344","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14343","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14345","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14346"},{"type":"object","name":"SaveTool","id":"p14347"},{"type":"object","name":"HoverTool","id":"p14354","attributes":{"renderers":[{"id":"p14351"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p14331","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p14332"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p14333"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14334"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14326","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p14355","attributes":{"ticks":[-27,-26,-25,-24,-23,-21,-20,-19,-18,-17,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14328"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-3,"3"],[-12,"12"],[-1,"1"],[-18,"18"],[-11,"11"],[-4,"4"],[-10,"10"],[-25,"25"],[-7,"7"],[-14,"14"],[-15,"15"],[-6,"6"],[-27,"27"],[-21,"21"],[-9,"9"],[-2,"2"],[-24,"24"],[-19,"19"],[-13,"13"],[-20,"20"],[-17,"17"],[-26,"26"],[-5,"5"],[-23,"23"],[-8,"8"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p14329"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14330","attributes":{"axis":{"id":"p14326"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14335","attributes":{"dimension":1,"axis":{"id":"p14331"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b86131a1-ebf3-4223-88d0-c00ad0389419","roots":{"p14314":"ca1fd89b-f309-48a9-af5f-cf4061614f3b"},"root_ids":["p14314"]}];
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

<div id="ef5bc537-940f-4c02-9141-765fdc515ed8" data-root-id="p14361" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"bed1022f-cc0f-4e5a-947a-b9c24dadb510":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14410","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14411"}}},"roots":[{"type":"object","name":"Figure","id":"p14361","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p14370","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p14371","attributes":{"factors":["Alphainfluenzavirus influenzae (2955291)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p14372"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p14373"},"title":{"type":"object","name":"Title","id":"p14368","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14405","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14358","attributes":{"selected":{"type":"object","name":"Selection","id":"p14359","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14360"},"data":{"type":"map","entries":[["y",["Alphainfluenzavirus influenzae (2955291)"]],["share",[93.6986505074538]],["lo",[93.40198662493516]],["hi",[93.98283492257484]],["n",[26899]],["det",[25204]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p14406","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14407"}}},"glyph":{"type":"object","name":"Scatter","id":"p14402","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p14403","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p14404","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14369","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14384"},{"type":"object","name":"BoxZoomTool","id":"p14385","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14386","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14392","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14391","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14393","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14394"},{"type":"object","name":"SaveTool","id":"p14395"},{"type":"object","name":"HoverTool","id":"p14409","attributes":{"renderers":[{"id":"p14405"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p14379","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p14380"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p14381"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14382"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14374","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14375","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14376"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14377"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14378","attributes":{"axis":{"id":"p14374"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14383","attributes":{"dimension":1,"axis":{"id":"p14379"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p14396","attributes":{"source":{"id":"p14358"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p14408","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"bed1022f-cc0f-4e5a-947a-b9c24dadb510","roots":{"p14361":"ef5bc537-940f-4c02-9141-765fdc515ed8"},"root_ids":["p14361"]}];
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
txid11320[Organism:exp] AND (hemagglutinin[Title] OR "segment 4"[Title] OR HA[Gene])
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Records are further restricted to those whose description names `H3`, because the subtype is in the record title and Entrez will not query it.

Disclosures on this entry: `oligos_modified`, `retrieval_scope_incomplete`, `thin_evidence`.


## What reached the statistics

108,814 records were screened for this assay and **99,155 (91%)** were evaluable, meaning both primers landed in the right orientation and size range. 9,659 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 7,013 |
| `truncated` | 1,376 |
| `chance_pair` | 1,058 |
| `chance_anchor` | 204 |
| `no_pair` | 1 |

