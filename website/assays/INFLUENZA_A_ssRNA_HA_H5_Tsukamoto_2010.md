# INFLUENZA_A_ssRNA_HA_H5_Tsukamoto_2010

<span class="aw-chip aw-chip-stable">stable</span>

**Influenza A virus H5 subtype — hemagglutinin gene rRT-PCR (Tsukamoto 2010)**

| | |
|---|---|
| Target | Influenza A virus ([taxid 11320](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11320)) |
| Gene | HA (hemagglutinin), H5 |
| Chemistry | hydrolysis_probe |
| Amplicon | 261 bp |
| Designed | 2010 |
| Paper | [10.1128/JCM.01264-10](https://doi.org/10.1128/JCM.01264-10) |
| Registry status | active |

!!! quote "The paper"
    Tsukamoto K, Noguchi D, Suzuki K, Shishido M, Ashizawa T, Kim MC, Lee YJ, Tada T. Broad detection of diverse H5 and H7 hemagglutinin genes of avian influenza viruses by real-time reverse transcription-PCR using primer and probe sets containing mixed bases. J Clin Microbiol 48(11):4275-4278 (2010).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CCARTRGGKGCKATAAAYTC` | 20 nt |
| reverse | `GTCTGCAGCRTAYCCACTYC` | 20 nt |
| probe | `ACCATKCCYTGCCAYCCYCCYTCT` | 24 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 20,125 | 20,923 | 96.2% | 95.9% – 96.4% |
| baseline (everything earlier) | 13,075 | 14,917 | 87.7% | 87.1% – 88.2% |

Change from baseline, Newcombe interval: **8.0% to 9.1%**. Threshold: **90.0%**.

*detected share 96.2% (96%-96%) since Oct 2024*

Trend across deposit years: by record rising (p=1.65e-83, 35 years); by footprint falling (p=6.06e-07); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="d40ccabd-d2ea-40a0-9968-84c1cbafaa82" data-root-id="p14827" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b75681f6-fed2-4fb3-adaa-d7b85f3cf181":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14882","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14883"}}},"roots":[{"type":"object","name":"Figure","id":"p14827","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p14829"},"y_range":{"type":"object","name":"Range1d","id":"p14836","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p14837"},"y_scale":{"type":"object","name":"LinearScale","id":"p14838"},"title":{"type":"object","name":"Title","id":"p14834","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14872","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14824","attributes":{"selected":{"type":"object","name":"Selection","id":"p14825","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14826"},"data":{"type":"map","entries":[["year",[1988,1989,1992,1994,1995,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[66.66666666666666,100.0,100.0,100.0,0.0,71.42857142857143,90.0,87.09677419354838,100.0,57.14285714285714,100.0,98.07692307692307,95.03105590062113,98.51485148514851,95.68567026194145,95.9731543624161,98.50746268656717,90.89481946624804,93.14685314685315,80.65476190476191,87.468671679198,67.32673267326733,67.24137931034483,87.95518207282913,72.51655629139073,77.5,86.96808510638297,85.33007334963325,87.29096989966555,86.49517684887459,67.43772241992883,94.73684210526315,95.15092502434274,95.62318528874071,96.30316375014486]],["detected",[2,3,1,1,0,5,9,27,10,4,32,51,153,199,621,572,594,579,666,542,349,204,390,628,438,341,654,349,522,807,379,1980,4886,8892,8310]],["evaluable",[3,3,1,1,1,7,10,31,10,7,32,52,161,202,649,596,603,637,715,672,399,303,580,714,604,440,752,409,598,933,562,2090,5135,9299,8629]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.328625426046248,9.328625426046248,8.703135093227193,8.703135093227193,8.703135093227193,9.897626379762722,10.143865699252444,10.913832791890265,10.143865699252444,9.897626379762722,10.934913263353746,11.252690272875853,11.957559676807392,12.093261293278134,12.763341329487123,12.715933217053019,12.722444315372975,12.752974775320043,12.816966209460864,12.782656929771147,12.489546869224002,12.33122926469063,12.700742410236355,12.81619330723611,12.723367953868234,12.5452063747567,12.844789200638962,12.503662263464195,12.717801734946685,12.962864643552694,12.683114678205751,13.392730671986154,13.851987162567045,14.145047048525566,14.108567409566376]]]}}},"view":{"type":"object","name":"CDSView","id":"p14873","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14874"}}},"glyph":{"type":"object","name":"Line","id":"p14869","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p14870","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p14871","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p14878","attributes":{"data_source":{"id":"p14824"},"view":{"type":"object","name":"CDSView","id":"p14879","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14880"}}},"glyph":{"type":"object","name":"Scatter","id":"p14875","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p14876","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p14877","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14835","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14849"},{"type":"object","name":"BoxZoomTool","id":"p14850","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14851","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14857","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14856","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14858","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14859"},{"type":"object","name":"SaveTool","id":"p14860"},{"type":"object","name":"HoverTool","id":"p14881","attributes":{"renderers":[{"id":"p14878"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p14844","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14845","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14846"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14847"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14839","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14840","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14841"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14842"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14843","attributes":{"axis":{"id":"p14839"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14848","attributes":{"dimension":1,"axis":{"id":"p14844"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p14861","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p14863","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p14864","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p14865","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p14867","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14866","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p14868","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b75681f6-fed2-4fb3-adaa-d7b85f3cf181","roots":{"p14827":"d40ccabd-d2ea-40a0-9968-84c1cbafaa82"},"root_ids":["p14827"]}];
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

<div id="e26b7a20-7a90-449b-a071-35ea64d987b2" data-root-id="p14887" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"5d2f6165-0251-41e0-94b5-5f3fab273eeb":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14927","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14928"}}},"roots":[{"type":"object","name":"Figure","id":"p14887","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p14888"},"y_range":{"type":"object","name":"DataRange1d","id":"p14889","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p14896"},"y_scale":{"type":"object","name":"LinearScale","id":"p14897"},"title":{"type":"object","name":"Title","id":"p14894","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14923","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14884","attributes":{"selected":{"type":"object","name":"Selection","id":"p14885","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14886"},"data":{"type":"map","entries":[["year",[1988,1989,1992,1994,1995,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[3,3,1,1,1,7,10,31,10,7,32,52,161,202,649,596,603,637,715,672,399,303,580,714,604,440,752,409,598,933,562,2090,5135,9299,8629]],["detected",[2,3,1,1,0,5,9,27,10,4,32,51,153,199,621,572,594,579,666,542,349,204,390,628,438,341,654,349,522,807,379,1980,4886,8892,8310]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p14924","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14925"}}},"glyph":{"type":"object","name":"VBar","id":"p14920","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p14921","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p14922","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14895","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14908"},{"type":"object","name":"BoxZoomTool","id":"p14909","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14910","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14916","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14915","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14917","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14918"},{"type":"object","name":"SaveTool","id":"p14919"},{"type":"object","name":"HoverTool","id":"p14926","attributes":{"renderers":[{"id":"p14923"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p14903","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14904","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14905"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14906"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14898","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14899","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14900"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14901"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14902","attributes":{"axis":{"id":"p14898"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14907","attributes":{"dimension":1,"axis":{"id":"p14903"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"5d2f6165-0251-41e0-94b5-5f3fab273eeb","roots":{"p14887":"e26b7a20-7a90-449b-a071-35ea64d987b2"},"root_ids":["p14887"]}];
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

<div id="f3e3d4e6-c043-4a94-bd62-ab555075375e" data-root-id="p14932" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"20f43bb0-9a81-4f29-b091-ae31a00c7686":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14974","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14975"}}},"roots":[{"type":"object","name":"Figure","id":"p14932","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p14934"},"y_range":{"type":"object","name":"FactorRange","id":"p14941","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p14942"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p14943"},"title":{"type":"object","name":"Title","id":"p14939","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14969","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14929","attributes":{"selected":{"type":"object","name":"Selection","id":"p14930","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14931"},"data":{"type":"map","entries":[["x",[-2,-5,-10,-4,-2,-19,-6,-1,-23,-8,-9,-17,-18,-20,-8,-14,-12,-15,-7,-12,-17]],["y",["reverse","reverse","probe","reverse","forward","probe","forward","probe","probe","forward","forward","forward","forward","reverse","reverse","reverse","reverse","forward","probe","forward","reverse"]],["alpha",[0.1980970982142857,0.1785546875,0.16764508928571428,0.153984375,0.1533203125,0.25112723214285715,0.16138392857142855,0.16584263392857143,0.1719140625,0.15796875,0.22276227678571428,0.2156473214285714,0.29874999999999996,0.1831082589285714,0.235,0.1865234375,0.15237165178571427,0.16043526785714285,0.1629966517857143,1.0,1.0]],["pos",[2,5,10,4,2,19,6,1,23,8,9,17,18,20,8,14,12,15,7,12,17]],["base",["Y","A","Y","C","T","K","A","T","C","A","K","R","A","G","Y","A","C","R","Y","K","T"]],["n",[507,301,186,42,35,1066,120,167,231,84,767,692,1568,349,896,385,25,110,137,12684,14377]],["det_with",["0% of 507","0% of 301","0% of 186","0% of 42","3% of 35","10% of 1066","9% of 120","13% of 167","16% of 231","30% of 84","43% of 767","46% of 692","57% of 1568","58% of 349","65% of 896","69% of 385","72% of 25","78% of 110","85% of 137","94% of 12684","98% of 14377"]],["det_without",["94% of 35321","93% of 35527","93% of 35642","93% of 35786","93% of 35793","95% of 34762","93% of 35708","93% of 35661","93% of 35597","93% of 35744","94% of 35061","94% of 35136","94% of 34260","93% of 35479","93% of 34932","93% of 35443","93% of 35803","93% of 35718","93% of 35691","92% of 23144","89% of 21451"]],["subs",["Y&gt;A 361, Y&gt;G 146","A&gt;G 291, A&gt;T 8, A&gt;C 2","Y&gt;A 129, Y&gt;G 57","C&gt;T 27, C&gt;G 12, C&gt;A 3","T&gt;A 34, T&gt;C 1","K&gt;C 1007, K&gt;A 59","A&gt;G 51, A&gt;C 47, A&gt;T 22","T&gt;G 99, T&gt;A 68","C&gt;T 230, C&gt;G 1","A&gt;G 51, A&gt;T 32, A&gt;C 1","K&gt;A 699, K&gt;C 68","R&gt;T 663, R&gt;C 29","A&gt;T 759, A&gt;G 667, A&gt;C 142","G&gt;A 348, G&gt;T 1","Y&gt;A 867, Y&gt;G 29","A&gt;G 241, A&gt;T 94, A&gt;C 50","C&gt;A 20, C&gt;G 4, C&gt;T 1","R&gt;T 62, R&gt;C 48","Y&gt;G 95, Y&gt;A 42","K&gt;A 12539, K&gt;C 145","T&gt;C 14184, T&gt;A 159, T&gt;G 34"]],["zone",["yes","yes","no","yes","yes","no","no","yes","no","no","no","no","no","no","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p14970","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14971"}}},"glyph":{"type":"object","name":"Rect","id":"p14966","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p14967","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p14968","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14940","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14954"},{"type":"object","name":"BoxZoomTool","id":"p14955","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14956","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14962","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14961","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14963","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14964"},{"type":"object","name":"SaveTool","id":"p14965"},{"type":"object","name":"HoverTool","id":"p14972","attributes":{"renderers":[{"id":"p14969"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p14949","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p14950"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p14951"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14952"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14944","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p14973","attributes":{"ticks":[-23,-20,-19,-18,-17,-15,-14,-12,-10,-9,-8,-7,-6,-5,-4,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14946"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-2,"2"],[-5,"5"],[-10,"10"],[-4,"4"],[-19,"19"],[-6,"6"],[-1,"1"],[-23,"23"],[-8,"8"],[-9,"9"],[-17,"17"],[-18,"18"],[-20,"20"],[-14,"14"],[-12,"12"],[-15,"15"],[-7,"7"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p14947"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14948","attributes":{"axis":{"id":"p14944"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14953","attributes":{"dimension":1,"axis":{"id":"p14949"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"20f43bb0-9a81-4f29-b091-ae31a00c7686","roots":{"p14932":"f3e3d4e6-c043-4a94-bd62-ab555075375e"},"root_ids":["p14932"]}];
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

<div id="b900b5a8-c9db-4745-b6f5-db9f956e6b03" data-root-id="p14979" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"a2f395ca-51ea-4e69-8663-e46df790576e":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p15028","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p15029"}}},"roots":[{"type":"object","name":"Figure","id":"p14979","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p14988","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p14989","attributes":{"factors":["Alphainfluenzavirus influenzae (2955291)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p14990"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p14991"},"title":{"type":"object","name":"Title","id":"p14986","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p15023","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14976","attributes":{"selected":{"type":"object","name":"Selection","id":"p14977","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14978"},"data":{"type":"map","entries":[["y",["Alphainfluenzavirus influenzae (2955291)"]],["share",[96.2320087983551]],["lo",[95.96532199540502]],["hi",[96.48171422690919]],["n",[20913]],["det",[20125]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p15024","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15025"}}},"glyph":{"type":"object","name":"Scatter","id":"p15020","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p15021","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p15022","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14987","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p15002"},{"type":"object","name":"BoxZoomTool","id":"p15003","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p15004","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p15010","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15009","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p15011","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p15012"},{"type":"object","name":"SaveTool","id":"p15013"},{"type":"object","name":"HoverTool","id":"p15027","attributes":{"renderers":[{"id":"p15023"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p14997","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p14998"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p14999"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15000"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14992","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14993","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14994"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14995"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14996","attributes":{"axis":{"id":"p14992"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p15001","attributes":{"dimension":1,"axis":{"id":"p14997"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p15014","attributes":{"source":{"id":"p14976"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p15026","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"a2f395ca-51ea-4e69-8663-e46df790576e","roots":{"p14979":"b900b5a8-c9db-4745-b6f5-db9f956e6b03"},"root_ids":["p14979"]}];
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

Records are further restricted to those whose description names `H5`, because the subtype is in the record title and Entrez will not query it.

Disclosures on this entry: `amplicon_multimodal`, `retrieval_scope_incomplete`.


## What reached the statistics

37,112 records were screened for this assay and **35,840 (97%)** were evaluable, meaning both primers landed in the right orientation and size range. 1,272 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `truncated` | 869 |
| `no_site` | 373 |
| `chance_anchor` | 21 |
| `no_pair` | 7 |

