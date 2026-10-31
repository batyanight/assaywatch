# INFLUENZA_A_HA_H3_CDC_Shu_2026

<span class="aw-chip aw-chip-low-coverage">low coverage</span>

**Influenza A virus H3 subtype — hemagglutinin rRT-PCR (CDC H3, as printed by Shu 2026)**

| | |
|---|---|
| Target | Influenza A virus ([taxid 11320](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11320)) |
| Gene | HA (hemagglutinin), H3 |
| Chemistry | hydrolysis_probe |
| Amplicon | 147 bp |
| Designed | 2008 |
| Paper | [10.1128/jcm.00727-26](https://doi.org/10.1128/jcm.00727-26) |
| Registry status | draft |

!!! quote "The paper"
    Shu B et al. 2026. J Clin Microbiol (prints the oligos); assay source FDA 510(k) K080570 (2008)

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `AAGCATTCCCAATGACAAACC` | 21 nt |
| reverse | `ATTGCRCCRAATATGCCTCTAGT` | 23 nt |
| probe | `CAGGATCACATATGGGSCCTGTCCCAG` | 27 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 59 | 26,817 | 0.2% | 0.2% – 0.3% |
| baseline (everything earlier) | 4,993 | 64,849 | 7.7% | 7.5% – 7.9% |

Change from baseline, Newcombe interval: **-7.7% to -7.3%**. Threshold: **90.0%**.

*detected share 0.2% (0.2%-0.3%) since Oct 2024, upper bound below the 90% threshold; change from baseline -8% to -7% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 8%); separately, lineage Alphainfluenzavirus influenzae (2955291) (26780 records) detects only 0.2% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift*

Trend across deposit years: by record falling (p=0, 41 years); by footprint falling (p=2.27e-38). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="f6294759-c02c-404a-9e17-909298eb8195" data-root-id="p14003" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"2db1b08a-43f2-47eb-8b7d-c7ab081d5dec":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14058","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14059"}}},"roots":[{"type":"object","name":"Figure","id":"p14003","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p14005"},"y_range":{"type":"object","name":"Range1d","id":"p14012","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p14013"},"y_scale":{"type":"object","name":"LinearScale","id":"p14014"},"title":{"type":"object","name":"Title","id":"p14010","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14048","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14000","attributes":{"selected":{"type":"object","name":"Selection","id":"p14001","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14002"},"data":{"type":"map","entries":[["year",[1982,1983,1987,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,22.22222222222222,18.181818181818183,0.0,33.33333333333333,0.0,69.23076923076923,53.84615384615385,73.21428571428571,0.0,30.0,45.13618677042802,88.10888252148997,88.20809248554913,69.02912621359224,31.26642143983184,13.984461709211987,2.8301886792452833,21.179302045728036,23.940886699507388,7.441067878443625,6.927374301675977,7.112476370510397,5.622042861118842,1.0903426791277258,1.545916012921089,0.4032258064516129,2.2492970946579196,1.2376237623762376,0.7141876115918143,0.4198966408268734,0.9170105456212746,0.17894422904861318,0.22502611910311018]],["detected",[0,0,0,0,0,0,0,0,4,2,0,2,0,9,7,41,0,3,116,615,763,711,595,126,18,176,486,262,186,301,202,63,67,29,48,10,52,26,80,24,28]],["evaluable",[1,1,3,21,2,1,6,7,18,11,1,6,5,13,13,56,11,10,257,698,865,1030,1903,901,636,831,2030,3521,2685,4232,3593,5778,4334,7192,2134,808,7281,6192,8724,13412,12443]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[8.703135093227193,8.703135093227193,9.328625426046248,10.652487636092928,9.07684386569143,8.703135093227193,9.791719296345839,9.897626379762722,10.547770533331066,10.209683151927734,8.703135093227193,9.791719296345839,9.667366891029102,10.324834530005162,10.324834530005162,11.300413928944284,10.209683151927734,10.143865699252444,12.235285195871363,12.803669180140771,12.921589958289633,13.016559620552755,13.343677953281967,12.943850533799699,12.752101609826662,12.899650658344875,13.377511651890359,13.661600901871232,13.52272066569846,13.754822486301217,13.67190010351127,13.910834860892159,13.76683461121725,14.019199222607767,13.403602596409865,12.88426593330566,14.025255863922077,13.945205662765742,14.113916316527689,14.322020496125784,14.28600904044103]]]}}},"view":{"type":"object","name":"CDSView","id":"p14049","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14050"}}},"glyph":{"type":"object","name":"Line","id":"p14045","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p14046","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p14047","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#8a4b9c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p14054","attributes":{"data_source":{"id":"p14000"},"view":{"type":"object","name":"CDSView","id":"p14055","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14056"}}},"glyph":{"type":"object","name":"Scatter","id":"p14051","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"hatch_color":{"type":"value","value":"#8a4b9c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p14052","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p14053","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#8a4b9c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#8a4b9c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14011","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14025"},{"type":"object","name":"BoxZoomTool","id":"p14026","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14027","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14033","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14032","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14034","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14035"},{"type":"object","name":"SaveTool","id":"p14036"},{"type":"object","name":"HoverTool","id":"p14057","attributes":{"renderers":[{"id":"p14054"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p14020","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14021","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14022"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14023"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14015","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14016","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14017"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14018"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14019","attributes":{"axis":{"id":"p14015"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14024","attributes":{"dimension":1,"axis":{"id":"p14020"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p14037","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p14039","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p14040","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p14041","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p14043","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14042","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p14044","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"2db1b08a-43f2-47eb-8b7d-c7ab081d5dec","roots":{"p14003":"f6294759-c02c-404a-9e17-909298eb8195"},"root_ids":["p14003"]}];
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

<div id="b3bcad04-88a8-423d-a0e9-3a0df55d77c8" data-root-id="p14063" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"fd2741d1-c6b9-44c3-abab-517e23ef0e71":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14103","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14104"}}},"roots":[{"type":"object","name":"Figure","id":"p14063","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p14064"},"y_range":{"type":"object","name":"DataRange1d","id":"p14065","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p14072"},"y_scale":{"type":"object","name":"LinearScale","id":"p14073"},"title":{"type":"object","name":"Title","id":"p14070","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14099","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14060","attributes":{"selected":{"type":"object","name":"Selection","id":"p14061","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14062"},"data":{"type":"map","entries":[["year",[1982,1983,1987,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[1,1,3,21,2,1,6,7,18,11,1,6,5,13,13,56,11,10,257,698,865,1030,1903,901,636,831,2030,3521,2685,4232,3593,5778,4334,7192,2134,808,7281,6192,8724,13412,12443]],["detected",[0,0,0,0,0,0,0,0,4,2,0,2,0,9,7,41,0,3,116,615,763,711,595,126,18,176,486,262,186,301,202,63,67,29,48,10,52,26,80,24,28]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#8a4b9c","#8a4b9c","#8a4b9c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p14100","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14101"}}},"glyph":{"type":"object","name":"VBar","id":"p14096","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p14097","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p14098","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14071","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14084"},{"type":"object","name":"BoxZoomTool","id":"p14085","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14086","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14092","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14091","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14093","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14094"},{"type":"object","name":"SaveTool","id":"p14095"},{"type":"object","name":"HoverTool","id":"p14102","attributes":{"renderers":[{"id":"p14099"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p14079","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14080","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14081"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14082"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14074","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14075","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14076"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14077"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14078","attributes":{"axis":{"id":"p14074"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14083","attributes":{"dimension":1,"axis":{"id":"p14079"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"fd2741d1-c6b9-44c3-abab-517e23ef0e71","roots":{"p14063":"b3bcad04-88a8-423d-a0e9-3a0df55d77c8"},"root_ids":["p14063"]}];
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

<div id="ce7edbd3-988c-4d5e-b2a5-f323b455bd93" data-root-id="p14108" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"c0c9f72b-e30f-4b01-95cb-f6e353992a0a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14150","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14151"}}},"roots":[{"type":"object","name":"Figure","id":"p14108","attributes":{"height":196,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p14110"},"y_range":{"type":"object","name":"FactorRange","id":"p14117","attributes":{"factors":["probe","reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p14118"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p14119"},"title":{"type":"object","name":"Title","id":"p14115","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14145","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14105","attributes":{"selected":{"type":"object","name":"Selection","id":"p14106","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14107"},"data":{"type":"map","entries":[["x",[-15,-3,-1,-3,-25,-12,-10,-18,-12,-4,-11,-10,-20,-5,-4,-15,-13,-9,-1,-6,-2,-12,-9,-2,-15,-9,-21,-6,-14,-3,-21,-18,-23,-10,-20,-27,-21,-24,-18,-17,-7,-16,-23,-26,-13,-8,-6,-19]],["y",["probe","reverse","reverse","forward","probe","probe","reverse","probe","reverse","forward","probe","probe","forward","reverse","reverse","reverse","reverse","probe","probe","forward","reverse","forward","reverse","probe","forward","forward","forward","reverse","forward","probe","probe","reverse","reverse","forward","probe","probe","reverse","probe","forward","forward","forward","reverse","probe","probe","forward","forward","probe","forward"]],["alpha",[1.0,1.0,0.45462985185346805,0.37295507603691663,0.4303351297100343,0.33653153841118844,0.3339351558920428,0.21379682761329172,0.2991807213143368,0.17095651604738943,0.17065978661662995,0.16164663015731023,0.15663932101324374,0.15534112975367093,0.15229965308838608,0.1514094647961076,0.15092727947112342,0.5014760107346234,0.3244769052865839,0.1923581262409181,0.19180175855824405,0.3728808936792267,0.3237721728885301,0.16179499487268997,0.3759223703445116,0.20682368599044357,0.29721488883555514,0.386307900421094,0.26665175746732706,0.16969541596666157,0.20304038574825997,0.20571095062509545,0.15886479174393994,0.15415421203063295,0.15274474723452533,0.18141622848166167,0.16824885999170902,0.24402613837191545,0.15990334475159818,0.15211419719416142,0.1616095389784653,0.15074182357689875,0.15812296816704122,0.15155782951148736,0.15333820609604432,0.16772958348787992,0.20808478607117142,0.15155782951148736]],["pos",[15,3,1,3,25,12,10,18,12,4,11,10,20,5,4,15,13,9,1,6,2,12,9,2,15,9,21,6,14,3,21,18,23,10,20,27,21,24,18,17,7,16,23,26,13,8,6,19]],["base",["T","A","T","A","G","G","T","A","T","A","S","C","A","C","T","R","A","C","G","C","G","C","G","A","T","T","A","T","C","C","C","R","A","A","A","C","T","G","C","A","A","C","A","A","C","G","T","G"]],["n",[79486,45436,8213,6011,7558,5029,4959,1720,4022,565,557,314,179,144,62,38,25,9476,4704,1142,1127,6009,4685,318,6091,1532,3969,6371,3145,531,1430,1502,239,112,74,847,492,2535,267,57,313,20,219,42,90,478,1566,42]],["det_with",["0% of 79486","0% of 45436","0% of 8213","0% of 6011","0% of 7558","0% of 5029","0% of 4959","0% of 1720","0% of 4022","0% of 565","0% of 557","0% of 314","0% of 179","0% of 144","0% of 62","0% of 38","0% of 25","1% of 9476","0% of 4704","0% of 1142","0% of 1127","1% of 6009","1% of 4685","1% of 318","1% of 6091","1% of 1532","1% of 3969","1% of 6371","1% of 3145","2% of 531","2% of 1430","3% of 1502","3% of 239","3% of 112","3% of 74","3% of 847","3% of 492","4% of 2535","5% of 267","7% of 57","8% of 313","10% of 20","11% of 219","12% of 42","16% of 90","17% of 478","18% of 1566","40% of 42"]],["det_without",["36% of 13866","11% of 47916","6% of 85139","6% of 87341","6% of 85794","6% of 88323","6% of 88393","6% of 91632","6% of 89330","5% of 92787","5% of 92795","5% of 93038","5% of 93173","5% of 93208","5% of 93290","5% of 93314","5% of 93327","6% of 83876","6% of 88648","5% of 92210","5% of 92225","6% of 87343","6% of 88667","5% of 93034","6% of 87261","5% of 91820","6% of 89383","6% of 86981","6% of 90207","5% of 92821","5% of 91922","5% of 91850","5% of 93113","5% of 93240","5% of 93278","5% of 92505","5% of 92860","5% of 90817","5% of 93085","5% of 93295","5% of 93039","5% of 93332","5% of 93133","5% of 93310","5% of 93262","5% of 92874","5% of 91786","5% of 93310"]],["subs",["T&gt;C 79485, T&gt;G 1","A&gt;G 45178, A&gt;T 242, A&gt;C 13, A&gt;K 2","T&gt;C 7958, T&gt;A 200, T&gt;G 54, T&gt;M 1","A&gt;G 6006, A&gt;C 4, A&gt;T 1","G&gt;A 7549, G&gt;T 5, G&gt;M 3, G&gt;C 1","G&gt;A 4959, G&gt;T 69, G&gt;C 1","T&gt;G 4764, T&gt;A 169, T&gt;C 26","A&gt;C 1343, A&gt;G 276, A&gt;T 101","T&gt;C 2911, T&gt;G 1045, T&gt;A 65, T&gt;M 1","A&gt;G 558, A&gt;T 6, A&gt;C 1","S&gt;A 467, S&gt;T 90","C&gt;A 189, C&gt;T 121, C&gt;G 4","A&gt;G 179","C&gt;T 137, C&gt;A 7","T&gt;G 62","R&gt;C 25, R&gt;T 13","A&gt;G 24, A&gt;C 1","C&gt;A 9175, C&gt;T 187, C&gt;G 114","G&gt;A 4686, G&gt;T 15, G&gt;C 3","C&gt;A 662, C&gt;T 451, C&gt;G 29","G&gt;A 981, G&gt;T 134, G&gt;C 12","C&gt;A 5581, C&gt;T 419, C&gt;G 9","G&gt;A 3339, G&gt;T 1322, G&gt;C 24","A&gt;C 312, A&gt;G 4, A&gt;T 2","T&gt;C 5569, T&gt;A 517, T&gt;G 5","T&gt;C 1529, T&gt;A 2, T&gt;G 1","A&gt;G 1789, A&gt;T 1098, A&gt;C 1082","T&gt;C 6371","C&gt;T 3121, C&gt;A 24","C&gt;T 426, C&gt;A 104, C&gt;G 1","C&gt;T 958, C&gt;A 470, C&gt;G 2","R&gt;T 788, R&gt;C 714","A&gt;T 232, A&gt;G 6, A&gt;C 1","A&gt;G 90, A&gt;C 17, A&gt;T 5","A&gt;G 67, A&gt;T 5, A&gt;C 2","C&gt;T 845, C&gt;A 2","T&gt;C 256, T&gt;A 130, T&gt;G 106","G&gt;A 2534, G&gt;T 1","C&gt;T 266, C&gt;A 1","A&gt;G 46, A&gt;C 8, A&gt;T 3","A&gt;G 305, A&gt;T 6, A&gt;C 2","C&gt;T 15, C&gt;G 5","A&gt;G 219","A&gt;C 34, A&gt;G 5, A&gt;T 3","C&gt;T 71, C&gt;A 18, C&gt;G 1","G&gt;A 464, G&gt;T 12, G&gt;C 2","T&gt;C 1565, T&gt;G 1","G&gt;A 41, G&gt;C 1"]],["zone",["no","yes","yes","yes","no","no","no","no","no","yes","no","no","no","yes","yes","no","no","no","yes","no","yes","no","no","yes","no","no","no","no","no","yes","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p14146","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14147"}}},"glyph":{"type":"object","name":"Rect","id":"p14142","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p14143","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p14144","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14116","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14130"},{"type":"object","name":"BoxZoomTool","id":"p14131","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14132","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14138","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14137","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14139","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14140"},{"type":"object","name":"SaveTool","id":"p14141"},{"type":"object","name":"HoverTool","id":"p14148","attributes":{"renderers":[{"id":"p14145"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p14125","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p14126"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p14127"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14128"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14120","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p14149","attributes":{"ticks":[-27,-26,-25,-24,-23,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14122"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-15,"15"],[-3,"3"],[-1,"1"],[-25,"25"],[-12,"12"],[-10,"10"],[-18,"18"],[-4,"4"],[-11,"11"],[-20,"20"],[-5,"5"],[-13,"13"],[-9,"9"],[-6,"6"],[-2,"2"],[-21,"21"],[-14,"14"],[-23,"23"],[-27,"27"],[-24,"24"],[-17,"17"],[-7,"7"],[-16,"16"],[-26,"26"],[-8,"8"],[-19,"19"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p14123"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14124","attributes":{"axis":{"id":"p14120"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14129","attributes":{"dimension":1,"axis":{"id":"p14125"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"c0c9f72b-e30f-4b01-95cb-f6e353992a0a","roots":{"p14108":"ce7edbd3-988c-4d5e-b2a5-f323b455bd93"},"root_ids":["p14108"]}];
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

<div id="d3f7ec63-29de-4b2a-9692-e18b0784264a" data-root-id="p14155" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"498b7a14-494a-4e87-93f9-b35eb8056f2c":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p14204","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p14205"}}},"roots":[{"type":"object","name":"Figure","id":"p14155","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p14164","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p14165","attributes":{"factors":["Alphainfluenzavirus influenzae (2955291)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p14166"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p14167"},"title":{"type":"object","name":"Title","id":"p14162","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p14199","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p14152","attributes":{"selected":{"type":"object","name":"Selection","id":"p14153","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p14154"},"data":{"type":"map","entries":[["y",["Alphainfluenzavirus influenzae (2955291)"]],["share",[0.22031366691560866]],["lo",[0.17085072904140666]],["hi",[0.28405585711062636]],["n",[26780]],["det",[59]],["colour",["#b3261e"]]]}}},"view":{"type":"object","name":"CDSView","id":"p14200","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p14201"}}},"glyph":{"type":"object","name":"Scatter","id":"p14196","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p14197","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p14198","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p14163","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p14178"},{"type":"object","name":"BoxZoomTool","id":"p14179","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p14180","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p14186","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p14185","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p14187","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p14188"},{"type":"object","name":"SaveTool","id":"p14189"},{"type":"object","name":"HoverTool","id":"p14203","attributes":{"renderers":[{"id":"p14199"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p14173","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p14174"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p14175"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14176"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p14168","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p14169","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p14170"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p14171"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p14172","attributes":{"axis":{"id":"p14168"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p14177","attributes":{"dimension":1,"axis":{"id":"p14173"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p14190","attributes":{"source":{"id":"p14152"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p14202","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"498b7a14-494a-4e87-93f9-b35eb8056f2c","roots":{"p14155":"d3f7ec63-29de-4b2a-9692-e18b0784264a"},"root_ids":["p14155"]}];
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

Disclosures on this entry: `citation_is_indirect`, `oligos_from_secondary_source`, `retrieval_scope_incomplete`, `conditions_not_printed`.


## What reached the statistics

108,814 records were screened for this assay and **91,666 (84%)** were evaluable, meaning both primers landed in the right orientation and size range. 17,148 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `truncated` | 8,343 |
| `no_site` | 6,984 |
| `chance_pair` | 1,773 |
| `chance_anchor` | 38 |

