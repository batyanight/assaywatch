# USUTU_ssRNA_NS1_realtime_Jost_2011

<span class="aw-chip aw-chip-stable">stable</span>

**USUTU VIRUS (ssRNA+) — NS1 real-time RT-PCR (Jöst 2011)**

| | |
|---|---|
| Target | Usutu virus ([taxid 64286](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=64286)) |
| Gene | NS1 |
| Chemistry | hydrolysis_probe |
| Amplicon | 91 bp |
| Designed | 2011 |
| Paper | [10.4269/ajtmh.2011.11-0248](https://doi.org/10.4269/ajtmh.2011.11-0248) |
| Registry status | active |

!!! quote "The paper"
    Jöst H, Bialonski A, Maus D, Sambri V, Eiden M, Groschup MH, Günther S, Becker N, Schmidt-Chanasit J. 2011. Isolation of Usutu virus in Germany. Am J Trop Med Hyg 85:551-553

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `CGTTCTCGACTTTGACTA` | 18 nt |
| reverse | `GCTAGTAGTAGTTCTTATGGA` | 21 nt |
| probe | `ACCGTCACAATCACTGAAGCAT` | 22 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 353 | 392 | 90.1% | 86.7% – 92.6% |
| baseline (everything earlier) | 659 | 684 | 96.3% | 94.7% – 97.5% |

Change from baseline, Newcombe interval: **-9.9% to -3.2%**. Threshold: **90.0%**.

*detected share 90.1% (87%-93%) since Oct 2024*

Trend across deposit years: by record falling (p=9.87e-05, 18 years); by footprint falling (p=5.65e-05). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="fe529061-4902-4d40-aede-5546c63130fa" data-root-id="p33817" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"0d0968b8-bf12-4a10-961f-94d66141370a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p33872","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p33873"}}},"roots":[{"type":"object","name":"Figure","id":"p33817","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p33819"},"y_range":{"type":"object","name":"Range1d","id":"p33826","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p33827"},"y_scale":{"type":"object","name":"LinearScale","id":"p33828"},"title":{"type":"object","name":"Title","id":"p33824","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p33862","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p33814","attributes":{"selected":{"type":"object","name":"Selection","id":"p33815","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p33816"},"data":{"type":"map","entries":[["year",[2004,2007,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,83.33333333333334,100.0,98.71794871794873,100.0,94.44444444444444,100.0,100.0,95.0413223140496,98.67549668874173,88.23529411764706,95.09803921568627,85.71428571428571,93.0635838150289,87.90697674418605]],["detected",[3,1,2,1,5,4,77,10,34,27,13,115,149,15,194,12,161,189]],["evaluable",[3,1,2,1,6,4,78,10,36,27,13,121,151,17,204,14,173,215]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.328625426046248,8.703135093227193,9.07684386569143,8.703135093227193,9.791719296345839,9.517227179437622,11.511208920139431,10.143865699252444,11.012804945939648,10.821697436206254,10.324834530005162,11.784019340078249,11.918861457530289,10.508782366508077,12.099112403217902,10.37579022724969,12.000762812510114,12.130243358135273]]]}}},"view":{"type":"object","name":"CDSView","id":"p33863","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33864"}}},"glyph":{"type":"object","name":"Line","id":"p33859","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p33860","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p33861","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p33868","attributes":{"data_source":{"id":"p33814"},"view":{"type":"object","name":"CDSView","id":"p33869","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33870"}}},"glyph":{"type":"object","name":"Scatter","id":"p33865","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p33866","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p33867","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p33825","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p33839"},{"type":"object","name":"BoxZoomTool","id":"p33840","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p33841","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p33847","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33846","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p33848","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p33849"},{"type":"object","name":"SaveTool","id":"p33850"},{"type":"object","name":"HoverTool","id":"p33871","attributes":{"renderers":[{"id":"p33868"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p33834","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33835","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33836"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33837"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p33829","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33830","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33831"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33832"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p33833","attributes":{"axis":{"id":"p33829"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p33838","attributes":{"dimension":1,"axis":{"id":"p33834"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p33851","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p33853","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p33854","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p33855","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p33857","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33856","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p33858","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"0d0968b8-bf12-4a10-961f-94d66141370a","roots":{"p33817":"fe529061-4902-4d40-aede-5546c63130fa"},"root_ids":["p33817"]}];
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

<div id="e6cc5e4e-a5d5-4a78-8828-264c91c75765" data-root-id="p33877" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"d58819f7-643e-47b0-99f3-c9be856ef3e7":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p33917","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p33918"}}},"roots":[{"type":"object","name":"Figure","id":"p33877","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p33878"},"y_range":{"type":"object","name":"DataRange1d","id":"p33879","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p33886"},"y_scale":{"type":"object","name":"LinearScale","id":"p33887"},"title":{"type":"object","name":"Title","id":"p33884","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p33913","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p33874","attributes":{"selected":{"type":"object","name":"Selection","id":"p33875","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p33876"},"data":{"type":"map","entries":[["year",[2004,2007,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[3,1,2,1,6,4,78,10,36,27,13,121,151,17,204,14,173,215]],["detected",[3,1,2,1,5,4,77,10,34,27,13,115,149,15,194,12,161,189]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p33914","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33915"}}},"glyph":{"type":"object","name":"VBar","id":"p33910","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p33911","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p33912","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p33885","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p33898"},{"type":"object","name":"BoxZoomTool","id":"p33899","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p33900","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p33906","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33905","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p33907","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p33908"},{"type":"object","name":"SaveTool","id":"p33909"},{"type":"object","name":"HoverTool","id":"p33916","attributes":{"renderers":[{"id":"p33913"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p33893","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33894","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33895"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33896"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p33888","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33889","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33890"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33891"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p33892","attributes":{"axis":{"id":"p33888"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p33897","attributes":{"dimension":1,"axis":{"id":"p33893"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"d58819f7-643e-47b0-99f3-c9be856ef3e7","roots":{"p33877":"e6cc5e4e-a5d5-4a78-8828-264c91c75765"},"root_ids":["p33877"]}];
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

<div id="c7083b9f-564a-4d41-971a-98f3f208a0bd" data-root-id="p33922" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"478bad57-8a76-4794-92c6-079c63cc0939":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p33964","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p33965"}}},"roots":[{"type":"object","name":"Figure","id":"p33922","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p33924"},"y_range":{"type":"object","name":"FactorRange","id":"p33931","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p33932"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p33933"},"title":{"type":"object","name":"Title","id":"p33929","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p33959","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p33919","attributes":{"selected":{"type":"object","name":"Selection","id":"p33920","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p33921"},"data":{"type":"map","entries":[["x",[-12,-15,-12,-18]],["y",["reverse","reverse","forward","forward"]],["alpha",[1.0,0.4628252788104089,0.7882899628252787,0.9715613382899628]],["pos",[12,15,12,18]],["base",["A","A","C","C"]],["n",[528,99,202,260]],["det_with",["92% of 528","91% of 99","92% of 202","93% of 260"]],["det_without",["97% of 544","95% of 973","95% of 870","95% of 812"]],["subs",["A&gt;G 527, A&gt;C 1","A&gt;G 98, A&gt;C 1","C&gt;T 202","C&gt;T 260"]],["zone",["no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p33960","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p33961"}}},"glyph":{"type":"object","name":"Rect","id":"p33956","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p33957","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p33958","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p33930","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p33944"},{"type":"object","name":"BoxZoomTool","id":"p33945","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p33946","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p33952","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33951","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p33953","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p33954"},{"type":"object","name":"SaveTool","id":"p33955"},{"type":"object","name":"HoverTool","id":"p33962","attributes":{"renderers":[{"id":"p33959"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p33939","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p33940"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p33941"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33942"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p33934","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p33963","attributes":{"ticks":[-18,-15,-12],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33936"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-12,"12"],[-15,"15"],[-18,"18"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p33937"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p33938","attributes":{"axis":{"id":"p33934"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p33943","attributes":{"dimension":1,"axis":{"id":"p33939"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"478bad57-8a76-4794-92c6-079c63cc0939","roots":{"p33922":"c7083b9f-564a-4d41-971a-98f3f208a0bd"},"root_ids":["p33922"]}];
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

<div id="e3da6bc5-0871-44b1-9441-c346414a77a4" data-root-id="p33969" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"93fbd8a5-9e73-4996-97aa-539a7eb3269d":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p34018","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p34019"}}},"roots":[{"type":"object","name":"Figure","id":"p33969","attributes":{"height":106,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p33978","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p33979","attributes":{"factors":["Orthoflavivirus usutuense (3048443)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p33980"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p33981"},"title":{"type":"object","name":"Title","id":"p33976","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p34013","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p33966","attributes":{"selected":{"type":"object","name":"Selection","id":"p33967","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p33968"},"data":{"type":"map","entries":[["y",["Orthoflavivirus usutuense (3048443)"]],["share",[90.97938144329896]],["lo",[87.71282811976803]],["hi",[93.44244344263093]],["n",[388]],["det",[353]],["colour",["#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p34014","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p34015"}}},"glyph":{"type":"object","name":"Scatter","id":"p34010","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p34011","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p34012","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p33977","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p33992"},{"type":"object","name":"BoxZoomTool","id":"p33993","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p33994","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p34000","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p33999","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p34001","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p34002"},{"type":"object","name":"SaveTool","id":"p34003"},{"type":"object","name":"HoverTool","id":"p34017","attributes":{"renderers":[{"id":"p34013"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p33987","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p33988"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p33989"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33990"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p33982","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p33983","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p33984"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p33985"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p33986","attributes":{"axis":{"id":"p33982"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p33991","attributes":{"dimension":1,"axis":{"id":"p33987"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p34004","attributes":{"source":{"id":"p33966"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p34016","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"93fbd8a5-9e73-4996-97aa-539a7eb3269d","roots":{"p33969":"e3da6bc5-0871-44b1-9441-c346414a77a4"},"root_ids":["p33969"]}];
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

Disclosures on this entry: `primer_site_polymorphic`.


## What reached the statistics

1,932 records were screened for this assay and **1,076 (56%)** were evaluable, meaning both primers landed in the right orientation and size range. 856 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 811 |
| `truncated` | 45 |

