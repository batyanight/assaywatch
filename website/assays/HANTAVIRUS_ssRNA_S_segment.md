# HANTAVIRUS_ssRNA_S_segment

<span class="aw-chip aw-chip-declining">declining</span>

**HANTAVIRUS (ssRNA) — S segment**

| | |
|---|---|
| Target | Orthohantavirus ([taxid 1980442](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1980442)) |
| Gene | S segment |
| Chemistry | conventional |
| Amplicon | 250 bp |
| Designed | 2013 |
| Paper | [10.1128/mbio.00598-13](https://doi.org/10.1128/mbio.00598-13) |
| Registry status | active |

!!! quote "The paper"
    Anthony SJ et al. 2013. mBio 4:e00598-13 (universal hantavirus S-segment primers UHantaF1/UHantaR1)

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GWGGVCARACWGCHGAYT` | 18 nt |
| reverse | `CCWGGTGTDADYTCHTCWGC` | 20 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 390 | 443 | 88.0% | 84.7% – 90.7% |
| baseline (everything earlier) | 3,712 | 3,849 | 96.4% | 95.8% – 97.0% |

Change from baseline, Newcombe interval: **-11.8% to -5.6%**. Threshold: **90.0%**.

*pooled share 88.0% is above the 90% threshold, but lineage Orthohantavirus tulaense (3052503) (102 records) detects only 64.7% (55.1%-73.3%), down from 93.3% on 386 earlier records; lineage verdict overrides to declining*

Trend across deposit years: by record falling (p=0.000637, 38 years); by footprint falling (p=2.32e-05). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="bc920baf-bc50-42ea-b3ac-92c4f3edb956" data-root-id="p13233" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"54e4c344-9c60-4bef-9433-8e5ce3ed1943":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p13288","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p13289"}}},"roots":[{"type":"object","name":"Figure","id":"p13233","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p13235"},"y_range":{"type":"object","name":"Range1d","id":"p13242","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p13243"},"y_scale":{"type":"object","name":"LinearScale","id":"p13244"},"title":{"type":"object","name":"Title","id":"p13240","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p13278","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p13230","attributes":{"selected":{"type":"object","name":"Selection","id":"p13231","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p13232"},"data":{"type":"map","entries":[["year",[1987,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,94.11764705882352,95.0,100.0,100.0,96.49122807017544,100.0,100.0,100.0,100.0,90.9090909090909,100.0,94.94949494949495,95.6989247311828,75.90361445783132,97.19626168224299,99.64028776978418,98.4536082474227,93.46733668341709,97.87234042553192,98.5981308411215,91.57894736842105,95.08771929824562,88.94009216589862,97.53694581280789,99.39485627836612,93.12977099236642,97.61092150170649,96.03174603174604,97.48743718592965,80.60344827586206]],["detected",[1,1,2,1,6,19,25,9,16,19,17,23,55,13,30,21,27,20,99,94,89,63,104,277,191,186,46,211,87,271,193,198,657,122,286,242,194,187]],["evaluable",[1,1,2,1,6,19,25,9,17,20,17,23,57,13,30,21,27,22,99,99,93,83,107,278,194,199,47,214,95,285,217,203,661,131,293,252,199,232]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.07684386569143,8.703135093227193,9.791719296345839,10.584573151575475,10.770092258092593,10.071067811865476,10.508782366508077,10.619414831097462,10.508782366508077,10.713966621835368,11.311780786273989,10.324834530005162,10.892023970177537,10.652487636092928,10.821697436206254,10.683957047019447,11.660254037844386,11.660254037844386,11.621380187649333,11.550262110107914,11.70836344482554,12.281169381163126,12.069226278137675,12.084368436583773,11.18724806845314,12.127483853608844,11.634626849261593,12.295652254050067,12.135721774447552,12.096194489216217,12.773507545195455,11.832573140379097,12.3117497421432,12.223774337514739,12.084368436583773,12.17517836478673]]]}}},"view":{"type":"object","name":"CDSView","id":"p13279","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13280"}}},"glyph":{"type":"object","name":"Line","id":"p13275","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p13276","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p13277","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p13284","attributes":{"data_source":{"id":"p13230"},"view":{"type":"object","name":"CDSView","id":"p13285","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13286"}}},"glyph":{"type":"object","name":"Scatter","id":"p13281","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p13282","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p13283","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p13241","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p13255"},{"type":"object","name":"BoxZoomTool","id":"p13256","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p13257","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p13263","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13262","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p13264","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p13265"},{"type":"object","name":"SaveTool","id":"p13266"},{"type":"object","name":"HoverTool","id":"p13287","attributes":{"renderers":[{"id":"p13284"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p13250","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13251","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13252"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13253"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p13245","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13246","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13247"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13248"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p13249","attributes":{"axis":{"id":"p13245"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p13254","attributes":{"dimension":1,"axis":{"id":"p13250"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p13267","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p13269","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p13270","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p13271","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p13273","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13272","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p13274","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"54e4c344-9c60-4bef-9433-8e5ce3ed1943","roots":{"p13233":"bc920baf-bc50-42ea-b3ac-92c4f3edb956"},"root_ids":["p13233"]}];
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

<div id="a601176a-7cdb-4302-9f98-319be7ed7d22" data-root-id="p13293" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"55e6dac7-594e-40bb-bdce-47c2a67cb459":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p13333","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p13334"}}},"roots":[{"type":"object","name":"Figure","id":"p13293","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p13294"},"y_range":{"type":"object","name":"DataRange1d","id":"p13295","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p13302"},"y_scale":{"type":"object","name":"LinearScale","id":"p13303"},"title":{"type":"object","name":"Title","id":"p13300","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p13329","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p13290","attributes":{"selected":{"type":"object","name":"Selection","id":"p13291","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p13292"},"data":{"type":"map","entries":[["year",[1987,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,2,1,6,19,25,9,17,20,17,23,57,13,30,21,27,22,99,99,93,83,107,278,194,199,47,214,95,285,217,203,661,131,293,252,199,232]],["detected",[1,1,2,1,6,19,25,9,16,19,17,23,55,13,30,21,27,20,99,94,89,63,104,277,191,186,46,211,87,271,193,198,657,122,286,242,194,187]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p13330","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13331"}}},"glyph":{"type":"object","name":"VBar","id":"p13326","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p13327","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p13328","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p13301","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p13314"},{"type":"object","name":"BoxZoomTool","id":"p13315","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p13316","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p13322","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13321","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p13323","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p13324"},{"type":"object","name":"SaveTool","id":"p13325"},{"type":"object","name":"HoverTool","id":"p13332","attributes":{"renderers":[{"id":"p13329"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p13309","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13310","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13311"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13312"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p13304","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13305","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13306"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13307"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p13308","attributes":{"axis":{"id":"p13304"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p13313","attributes":{"dimension":1,"axis":{"id":"p13309"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"55e6dac7-594e-40bb-bdce-47c2a67cb459","roots":{"p13293":"a601176a-7cdb-4302-9f98-319be7ed7d22"},"root_ids":["p13293"]}];
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

<div id="d4c7e01e-ec3d-4edc-a744-5c4f9eed0130" data-root-id="p13338" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"6ceb6403-8708-4411-b3ca-b3975658a94f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p13380","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p13381"}}},"roots":[{"type":"object","name":"Figure","id":"p13338","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p13340"},"y_range":{"type":"object","name":"FactorRange","id":"p13347","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p13348"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p13349"},"title":{"type":"object","name":"Title","id":"p13345","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p13375","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p13335","attributes":{"selected":{"type":"object","name":"Selection","id":"p13336","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p13337"},"data":{"type":"map","entries":[["x",[-1,-16,-2,-1,-7,-2,-8,-15,-13,-5,-9,-19,-6,-20,-11,-4,-13,-12,-4,-10,-8,-18,-17,-5,-15,-3,-12,-6,-14,-18]],["y",["reverse","forward","forward","forward","forward","reverse","reverse","forward","reverse","reverse","forward","reverse","forward","reverse","forward","reverse","forward","forward","forward","forward","forward","forward","forward","forward","reverse","reverse","reverse","reverse","forward","reverse"]],["alpha",[0.2450605778191985,0.2276328052190121,0.20149114631873252,0.18723205964585274,0.18723205964585274,0.22208760484622553,0.18168685927306616,0.2331780055917987,0.21099720410065237,0.20862068965517241,0.20624417520969243,0.19594594594594594,0.17534948741845294,0.16742777260018638,0.18089468779123952,0.17851817334575953,0.21495806150978564,0.21812674743709226,0.24902143522833178,0.18327120223671947,0.19356943150046596,1.0,0.3282385834109972,0.26169617893755825,0.9865330848089469,0.381314072693383,0.4906337371854613,0.20069897483690585,1.0,0.43676607642124887]],["pos",[1,16,2,1,7,2,8,15,13,5,9,19,6,20,11,4,13,12,4,10,8,18,17,5,15,3,12,6,14,18]],["base",["C","G","Y","T","G","G","T","G","T","T","C","C","C","C","R","C","C","A","G","A","W","G","W","H","T","W","D","H","V","W"]],["n",[120,98,65,47,47,91,40,105,77,74,71,58,32,22,39,36,82,86,125,42,55,1608,225,141,1056,292,430,64,1209,362]],["det_with",["0% of 120","0% of 98","0% of 65","0% of 47","0% of 47","1% of 91","0% of 40","2% of 105","1% of 77","1% of 74","1% of 71","3% of 58","3% of 32","5% of 22","5% of 39","6% of 36","9% of 82","9% of 86","11% of 125","17% of 42","80% of 55","93% of 1608","94% of 225","94% of 141","97% of 1056","98% of 292","98% of 430","98% of 64","99% of 1209","100% of 362"]],["det_without",["98% of 4196","98% of 4218","97% of 4251","97% of 4269","97% of 4269","98% of 4225","96% of 4276","98% of 4211","97% of 4239","97% of 4242","97% of 4245","97% of 4258","96% of 4284","96% of 4294","96% of 4277","96% of 4280","97% of 4234","97% of 4230","98% of 4191","96% of 4274","96% of 4261","97% of 2708","96% of 4091","96% of 4175","95% of 3260","95% of 4024","95% of 3886","96% of 4252","94% of 3107","95% of 3954"]],["subs",["C&gt;A 62, C&gt;T 57, C&gt;G 1","G&gt;A 55, G&gt;T 31, G&gt;C 12","Y&gt;G 38, Y&gt;A 27","T&gt;A 25, T&gt;G 19, T&gt;C 3","G&gt;A 21, G&gt;C 17, G&gt;T 9","G&gt;A 83, G&gt;T 6, G&gt;C 2","T&gt;C 39, T&gt;A 1","G&gt;T 52, G&gt;C 32, G&gt;A 21","T&gt;A 60, T&gt;C 11, T&gt;G 6","T&gt;G 62, T&gt;C 7, T&gt;A 5","C&gt;A 52, C&gt;T 14, C&gt;G 5","C&gt;A 36, C&gt;T 14, C&gt;G 8","C&gt;T 19, C&gt;G 8, C&gt;A 5","C&gt;T 20, C&gt;A 2","R&gt;T 32, R&gt;C 7","C&gt;T 33, C&gt;G 2, C&gt;A 1","C&gt;G 34, C&gt;A 32, C&gt;T 16","A&gt;C 59, A&gt;G 14, A&gt;T 13","G&gt;A 55, G&gt;C 36, G&gt;T 34","A&gt;T 23, A&gt;G 15, A&gt;C 4","W&gt;C 28, W&gt;G 27","G&gt;C 1565, G&gt;T 34, G&gt;A 9","W&gt;C 208, W&gt;G 17","H&gt;G 141","T&gt;A 616, T&gt;G 304, T&gt;C 135, T&gt;R 1","W&gt;G 248, W&gt;C 44","D&gt;C 430","H&gt;G 64","V&gt;T 1209","W&gt;G 246, W&gt;C 116"]],["zone",["yes","no","yes","yes","no","yes","no","no","no","yes","no","no","no","no","no","yes","no","no","yes","no","no","no","no","yes","no","yes","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p13376","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13377"}}},"glyph":{"type":"object","name":"Rect","id":"p13372","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p13373","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p13374","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p13346","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p13360"},{"type":"object","name":"BoxZoomTool","id":"p13361","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p13362","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p13368","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13367","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p13369","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p13370"},{"type":"object","name":"SaveTool","id":"p13371"},{"type":"object","name":"HoverTool","id":"p13378","attributes":{"renderers":[{"id":"p13375"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p13355","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p13356"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p13357"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13358"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p13350","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p13379","attributes":{"ticks":[-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13352"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-1,"1"],[-16,"16"],[-2,"2"],[-7,"7"],[-8,"8"],[-15,"15"],[-13,"13"],[-5,"5"],[-9,"9"],[-19,"19"],[-6,"6"],[-20,"20"],[-11,"11"],[-4,"4"],[-12,"12"],[-10,"10"],[-18,"18"],[-17,"17"],[-3,"3"],[-14,"14"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p13353"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p13354","attributes":{"axis":{"id":"p13350"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p13359","attributes":{"dimension":1,"axis":{"id":"p13355"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"6ceb6403-8708-4411-b3ca-b3975658a94f","roots":{"p13338":"d4c7e01e-ec3d-4edc-a744-5c4f9eed0130"},"root_ids":["p13338"]}];
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

<div id="a00a063a-d43f-47e4-aa13-9b434dd2a4ab" data-root-id="p13385" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"44c55393-36cd-4354-8a8a-75d7e7ab4fcd":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p13434","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p13435"}}},"roots":[{"type":"object","name":"Figure","id":"p13385","attributes":{"height":236,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p13394","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p13395","attributes":{"factors":["Orthohantavirus tulaense (3052503)","Orthohantavirus hantanense (3052480)","Orthohantavirus seoulense (3052498)","Juquitiba virus (430511)","Orthohantavirus andesense (1980456)","Orthohantavirus puumalaense (3052493)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p13396"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p13397"},"title":{"type":"object","name":"Title","id":"p13392","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p13429","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p13382","attributes":{"selected":{"type":"object","name":"Selection","id":"p13383","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p13384"},"data":{"type":"map","entries":[["y",["Orthohantavirus tulaense (3052503)","Orthohantavirus hantanense (3052480)","Orthohantavirus seoulense (3052498)","Juquitiba virus (430511)","Orthohantavirus andesense (1980456)","Orthohantavirus puumalaense (3052493)"]],["share",[64.70588235294117,94.64285714285714,98.38709677419355,100.0,100.0,100.0]],["lo",[55.05227800497734,85.39269093117848,91.41327973931,90.35813714055362,95.00079920442688,91.23783988027135]],["hi",[73.29200252012669,98.1614218617891,99.71471328313783,100.0,100.0,100.0]],["n",[102,56,62,36,73,40]],["det",[66,53,61,36,73,40]],["colour",["#b3261e","#007d5c","#007d5c","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p13430","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p13431"}}},"glyph":{"type":"object","name":"Scatter","id":"p13426","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p13427","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p13428","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p13393","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p13408"},{"type":"object","name":"BoxZoomTool","id":"p13409","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p13410","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p13416","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p13415","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p13417","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p13418"},{"type":"object","name":"SaveTool","id":"p13419"},{"type":"object","name":"HoverTool","id":"p13433","attributes":{"renderers":[{"id":"p13429"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p13403","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p13404"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p13405"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13406"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p13398","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p13399","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p13400"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p13401"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p13402","attributes":{"axis":{"id":"p13398"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p13407","attributes":{"dimension":1,"axis":{"id":"p13403"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p13420","attributes":{"source":{"id":"p13382"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p13432","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"44c55393-36cd-4354-8a8a-75d7e7ab4fcd","roots":{"p13385":"a00a063a-d43f-47e4-aa13-9b434dd2a4ab"},"root_ids":["p13385"]}];
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

Disclosures on this entry: `nested_protocol`.


## What reached the statistics

16,099 records were screened for this assay and **4,292 (27%)** were evaluable, meaning both primers landed in the right orientation and size range. 11,807 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `chance_only` | 5,460 |
| `no_site` | 5,131 |
| `truncated` | 1,110 |
| `chance_anchor` | 105 |

