# INFLUENZA_A_ssRNA_HA_H7_Tsukamoto_2010

<span class="aw-chip aw-chip-declining">declining</span>

**Influenza A virus H7 subtype — hemagglutinin gene rRT-PCR (Tsukamoto 2010)**

| | |
|---|---|
| Target | Influenza A virus ([taxid 11320](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11320)) |
| Gene | HA (hemagglutinin), H7 |
| Chemistry | hydrolysis_probe |
| Amplicon | 241 bp |
| Designed | 2010 |
| Paper | [10.1128/JCM.01264-10](https://doi.org/10.1128/JCM.01264-10) |
| Registry status | active |

!!! quote "The paper"
    Tsukamoto K, Noguchi D, Suzuki K, Shishido M, Ashizawa T, Kim MC, Lee YJ, Tada T. Broad detection of diverse H5 and H7 hemagglutinin genes of avian influenza viruses by real-time reverse transcription-PCR using primer and probe sets containing mixed bases. J Clin Microbiol 48(11):4275-4278 (2010).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ATMAATAGCAGRGCARTRGG` | 20 nt |
| reverse | `GATCWATTGCHGAYTGRGTG` | 20 nt |
| probe | `CCYTCYCCYTGTGCRTTYTG` | 20 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 126 | 157 | 80.3% | 73.3% – 85.7% |
| baseline (everything earlier) | 2,320 | 4,298 | 54.0% | 52.5% – 55.5% |

Change from baseline, Newcombe interval: **19.2% to 31.9%**. Threshold: **90.0%**.

*pooled share 80.3% has low coverage, but lineage Alphainfluenzavirus influenzae (2955291) (157 records) detects 80.3% (73.3%-85.7%); lineage verdict overrides to declining*

Trend across deposit years: by record falling (p=4.46e-61, 36 years); by footprint falling (p=0.135). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="a41eb020-41df-4272-b337-947132959953" data-root-id="p15033" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"4484eab2-e56b-44a1-86b2-7263ffb48b9b":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p15088","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p15089"}}},"roots":[{"type":"object","name":"Figure","id":"p15033","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p15035"},"y_range":{"type":"object","name":"Range1d","id":"p15042","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p15043"},"y_scale":{"type":"object","name":"LinearScale","id":"p15044"},"title":{"type":"object","name":"Title","id":"p15040","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p15078","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p15030","attributes":{"selected":{"type":"object","name":"Selection","id":"p15031","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p15032"},"data":{"type":"map","entries":[["year",[1982,1987,1988,1989,1990,1991,1994,1995,1996,1998,1999,2000,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[0.0,0.0,100.0,0.0,100.0,0.0,0.0,83.33333333333334,100.0,100.0,100.0,85.18518518518519,92.42424242424242,79.3103448275862,94.44444444444444,82.97872340425532,87.2,91.23376623376623,93.52941176470588,87.77777777777777,85.18518518518519,94.11764705882352,39.166666666666664,74.13793103448276,24.563445867287545,39.130434782608695,60.63829787234043,27.559055118110237,78.0701754385965,37.22627737226277,14.723926380368098,39.42307692307692,60.86956521739131,83.33333333333334,66.66666666666666,92.7536231884058]],["detected",[0,0,2,0,1,0,0,5,3,2,13,23,61,23,17,39,109,281,159,79,69,96,141,258,211,99,228,70,89,102,24,41,14,75,48,64]],["evaluable",[1,1,2,2,1,1,1,6,3,2,13,27,66,29,18,47,125,308,170,90,81,102,360,348,859,253,376,254,114,274,163,104,23,90,72,69]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.07684386569143,9.07684386569143,8.703135093227193,8.703135093227193,8.703135093227193,9.791719296345839,9.328625426046248,9.07684386569143,10.324834530005162,10.821697436206254,11.405466677556973,10.869436534339137,10.547770533331066,11.18724806845314,11.80393455381962,12.34071528233362,11.990267112817275,11.600932205756964,11.53494852413258,11.67876319631025,12.430677602783453,12.41119735602115,12.917785099561756,12.226095756900556,12.455608587243066,12.228407474253013,11.747425107358183,12.272718983435041,11.964992816572273,11.690784341861697,10.713966621835368,11.600932205756964,11.460677957646856,11.433709207718536]]]}}},"view":{"type":"object","name":"CDSView","id":"p15079","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15080"}}},"glyph":{"type":"object","name":"Line","id":"p15075","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p15076","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p15077","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#b3261e","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p15084","attributes":{"data_source":{"id":"p15030"},"view":{"type":"object","name":"CDSView","id":"p15085","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15086"}}},"glyph":{"type":"object","name":"Scatter","id":"p15081","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"hatch_color":{"type":"value","value":"#b3261e"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p15082","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p15083","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p15041","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p15055"},{"type":"object","name":"BoxZoomTool","id":"p15056","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p15057","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p15063","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15062","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p15064","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p15065"},{"type":"object","name":"SaveTool","id":"p15066"},{"type":"object","name":"HoverTool","id":"p15087","attributes":{"renderers":[{"id":"p15084"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p15050","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15051","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15052"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15053"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p15045","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15046","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15047"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15048"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p15049","attributes":{"axis":{"id":"p15045"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p15054","attributes":{"dimension":1,"axis":{"id":"p15050"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p15067","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p15069","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p15070","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p15071","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p15073","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15072","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p15074","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"4484eab2-e56b-44a1-86b2-7263ffb48b9b","roots":{"p15033":"a41eb020-41df-4272-b337-947132959953"},"root_ids":["p15033"]}];
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

<div id="e9f97ba6-0276-4c8d-85dd-094ad11128ba" data-root-id="p15093" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"f45e8312-5518-4169-8c82-e66eeadebd95":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p15133","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p15134"}}},"roots":[{"type":"object","name":"Figure","id":"p15093","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p15094"},"y_range":{"type":"object","name":"DataRange1d","id":"p15095","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p15102"},"y_scale":{"type":"object","name":"LinearScale","id":"p15103"},"title":{"type":"object","name":"Title","id":"p15100","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p15129","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p15090","attributes":{"selected":{"type":"object","name":"Selection","id":"p15091","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p15092"},"data":{"type":"map","entries":[["year",[1982,1987,1988,1989,1990,1991,1994,1995,1996,1998,1999,2000,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,2,2,1,1,1,6,3,2,13,27,66,29,18,47,125,308,170,90,81,102,360,348,859,253,376,254,114,274,163,104,23,90,72,69]],["detected",[0,0,2,0,1,0,0,5,3,2,13,23,61,23,17,39,109,281,159,79,69,96,141,258,211,99,228,70,89,102,24,41,14,75,48,64]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#b3261e","#b3261e","#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p15130","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15131"}}},"glyph":{"type":"object","name":"VBar","id":"p15126","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p15127","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p15128","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p15101","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p15114"},{"type":"object","name":"BoxZoomTool","id":"p15115","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p15116","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p15122","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15121","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p15123","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p15124"},{"type":"object","name":"SaveTool","id":"p15125"},{"type":"object","name":"HoverTool","id":"p15132","attributes":{"renderers":[{"id":"p15129"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p15109","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15110","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15111"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15112"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p15104","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15105","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15106"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15107"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p15108","attributes":{"axis":{"id":"p15104"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p15113","attributes":{"dimension":1,"axis":{"id":"p15109"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"f45e8312-5518-4169-8c82-e66eeadebd95","roots":{"p15093":"e9f97ba6-0276-4c8d-85dd-094ad11128ba"},"root_ids":["p15093"]}];
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

<div id="f1ba2005-eae5-45a4-a3c0-c6bf3acdbbd4" data-root-id="p15138" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"afab2769-fe6e-4b38-a300-d178565a57b2":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p15180","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p15181"}}},"roots":[{"type":"object","name":"Figure","id":"p15138","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p15140"},"y_range":{"type":"object","name":"FactorRange","id":"p15147","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p15148"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p15149"},"title":{"type":"object","name":"Title","id":"p15145","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p15175","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p15135","attributes":{"selected":{"type":"object","name":"Selection","id":"p15136","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p15137"},"data":{"type":"map","entries":[["x",[-3,-17,-9,-7,-14,-9,-13,-10,-7,-12,-20,-13,-6,-14,-18,-8,-17,-15,-19,-16,-1]],["y",["forward","forward","probe","probe","forward","reverse","forward","reverse","forward","forward","forward","reverse","forward","reverse","forward","forward","reverse","forward","reverse","reverse","reverse"]],["alpha",[1.0,1.0,0.2896632996632997,0.20418630751964084,0.24310886644219976,0.1675533108866442,0.24921436588103252,0.21792368125701458,0.1950280583613917,0.22402918069584735,0.2362401795735129,0.2904264870931538,0.1965544332210999,0.1683164983164983,0.3026374859708193,0.24005611672278337,0.27668911335578006,0.4239842873176206,0.2858473625140292,0.2537934904601571,0.1927384960718294]],["pos",[3,17,9,7,14,9,13,10,7,12,20,13,6,14,18,8,17,15,19,16,1]],["base",["R","A","T","C","A","G","G","H","C","C","A","T","A","T","M","G","C","T","A","W","G"]],["n",[1452,1584,183,71,122,23,130,89,59,97,113,184,61,24,200,118,166,359,178,136,56]],["det_with",["0% of 1452","4% of 1584","0% of 183","0% of 71","2% of 122","4% of 23","7% of 130","8% of 89","10% of 59","11% of 97","15% of 113","17% of 184","21% of 61","25% of 24","27% of 200","36% of 118","43% of 166","50% of 359","65% of 178","65% of 136","70% of 56"]],["det_without",["82% of 3000","83% of 2868","57% of 4269","56% of 4381","56% of 4330","55% of 4429","56% of 4322","56% of 4363","56% of 4393","56% of 4355","56% of 4339","57% of 4268","55% of 4391","55% of 4428","56% of 4252","55% of 4334","55% of 4286","55% of 4093","55% of 4274","55% of 4316","55% of 4396"]],["subs",["R&gt;T 1413, K&gt;C 35, R&gt;C 4","A&gt;G 1584","T&gt;C 143, T&gt;G 39, T&gt;A 1","C&gt;A 67, C&gt;T 4","Y&gt;A 97, A&gt;C 21, A&gt;G 4","G&gt;T 23","C&gt;G 93, G&gt;C 21, G&gt;A 12, C&gt;A 3","H&gt;G 89","C&gt;T 59","C&gt;T 94, Y&gt;G 2, C&gt;A 1","A&gt;G 112, A&gt;C 1","T&gt;A 100, T&gt;C 79, T&gt;G 5","A&gt;T 23, A&gt;G 17, W&gt;G 15, A&gt;C 5","T&gt;C 24","C&gt;T 75, C&gt;A 70, M&gt;T 55","G&gt;A 61, A&gt;G 56, A&gt;C 1","C&gt;T 166","C&gt;T 242, T&gt;C 117","A&gt;G 176, A&gt;C 2","W&gt;G 135, W&gt;C 1","G&gt;A 56"]],["zone",["yes","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","yes"]]]}}},"view":{"type":"object","name":"CDSView","id":"p15176","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15177"}}},"glyph":{"type":"object","name":"Rect","id":"p15172","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p15173","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p15174","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p15146","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p15160"},{"type":"object","name":"BoxZoomTool","id":"p15161","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p15162","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p15168","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15167","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p15169","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p15170"},{"type":"object","name":"SaveTool","id":"p15171"},{"type":"object","name":"HoverTool","id":"p15178","attributes":{"renderers":[{"id":"p15175"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p15155","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p15156"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p15157"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15158"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p15150","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p15179","attributes":{"ticks":[-20,-19,-18,-17,-16,-15,-14,-13,-12,-10,-9,-8,-7,-6,-3,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15152"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-3,"3"],[-17,"17"],[-9,"9"],[-7,"7"],[-14,"14"],[-13,"13"],[-10,"10"],[-12,"12"],[-20,"20"],[-6,"6"],[-18,"18"],[-8,"8"],[-15,"15"],[-19,"19"],[-16,"16"],[-1,"1"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p15153"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p15154","attributes":{"axis":{"id":"p15150"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p15159","attributes":{"dimension":1,"axis":{"id":"p15155"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"afab2769-fe6e-4b38-a300-d178565a57b2","roots":{"p15138":"f1ba2005-eae5-45a4-a3c0-c6bf3acdbbd4"},"root_ids":["p15138"]}];
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

<div id="d9f8b7cd-7c49-4ffa-b31b-c6cba5901451" data-root-id="p15185" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"cc79b3da-0f30-47c5-a1b0-776ae274e06f":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p15234","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p15235"}}},"roots":[{"type":"object","name":"Figure","id":"p15185","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p15194","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p15195","attributes":{"factors":["Alphainfluenzavirus influenzae (2955291)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p15196"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p15197"},"title":{"type":"object","name":"Title","id":"p15192","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p15229","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p15182","attributes":{"selected":{"type":"object","name":"Selection","id":"p15183","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p15184"},"data":{"type":"map","entries":[["y",["Alphainfluenzavirus influenzae (2955291)"]],["share",[80.2547770700637]],["lo",[73.33790661378463]],["hi",[85.72646689821262]],["n",[157]],["det",[126]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p15230","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p15231"}}},"glyph":{"type":"object","name":"Scatter","id":"p15226","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p15227","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p15228","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p15193","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p15208"},{"type":"object","name":"BoxZoomTool","id":"p15209","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p15210","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p15216","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p15215","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p15217","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p15218"},{"type":"object","name":"SaveTool","id":"p15219"},{"type":"object","name":"HoverTool","id":"p15233","attributes":{"renderers":[{"id":"p15229"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p15203","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p15204"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p15205"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15206"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p15198","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p15199","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p15200"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p15201"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p15202","attributes":{"axis":{"id":"p15198"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p15207","attributes":{"dimension":1,"axis":{"id":"p15203"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p15220","attributes":{"source":{"id":"p15182"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p15232","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"cc79b3da-0f30-47c5-a1b0-776ae274e06f","roots":{"p15185":"d9f8b7cd-7c49-4ffa-b31b-c6cba5901451"},"root_ids":["p15185"]}];
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

Records are further restricted to those whose description names `H7`, because the subtype is in the record title and Entrez will not query it.

Disclosures on this entry: `primer_site_polymorphic`, `retrieval_scope_incomplete`.


## What reached the statistics

4,652 records were screened for this assay and **4,455 (96%)** were evaluable, meaning both primers landed in the right orientation and size range. 197 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `truncated` | 116 |
| `no_site` | 74 |
| `chance_anchor` | 5 |

