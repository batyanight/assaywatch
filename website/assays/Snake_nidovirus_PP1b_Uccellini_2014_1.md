# Snake_nidovirus_PP1b_Uccellini_2014_1

<span class="aw-chip aw-chip-insufficient-data">insufficient data</span>

**NIDOVIRUS (ssRNA)-SNAKE — PP1b**

| | |
|---|---|
| Target | Serpentovirinae (snake nidoviruses, Tobaniviridae) ([taxid 2508240](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=2508240)) |
| Gene | PP1b |
| Chemistry | conventional |
| Amplicon | 420 bp |
| Designed | 2014 |
| Paper | [10.1186/1743-422X-11-144](https://doi.org/10.1186/1743-422X-11-144) |
| Registry status | active |

!!! quote "The paper"
    Uccellini L et al. 2014. Virol J 11:144

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GTCGTCAACTTGTCCCACCA` | 20 nt |
| reverse | `GTCAAACATGAAAGCGTGCG` | 20 nt |

## The verdict, and the numbers behind it

**insufficient data** — too few evaluable records to say anything; reported, never flagged

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 4 | 10 | 40.0% | 16.8% – 68.7% |
| baseline (everything earlier) | 10 | 18 | 55.6% | 33.7% – 75.4% |

Change from baseline, Newcombe interval: **-46.1% to 20.5%**. Threshold: **90.0%**.

*10 evaluable records since Oct 2021, below the minimum of 15; the detected share is 40% (17%-69%), too wide to act on (window widened to 60 months to reach 15 evaluable records)*

Trend across deposit years: by record falling (p=0.101, 8 years); by footprint falling (p=0.155). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="fe00d685-6798-4096-8dc4-2ff47adee704" data-root-id="p32810" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"ac681088-de79-4fe2-9b12-0ff9a67cab0a":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p32865","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p32866"}}},"roots":[{"type":"object","name":"Figure","id":"p32810","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p32812"},"y_range":{"type":"object","name":"Range1d","id":"p32819","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p32820"},"y_scale":{"type":"object","name":"LinearScale","id":"p32821"},"title":{"type":"object","name":"Title","id":"p32817","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p32855","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p32807","attributes":{"selected":{"type":"object","name":"Selection","id":"p32808","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p32809"},"data":{"type":"map","entries":[["year",[2014,2017,2018,2019,2020,2023,2024,2026]],["share",[100.0,100.0,100.0,40.0,0.0,0.0,37.5,100.0]],["detected",[3,2,1,4,0,0,3,1]],["evaluable",[3,2,1,10,2,1,8,1]],["window",["baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.328625426046248,9.07684386569143,8.703135093227193,10.143865699252444,9.07684386569143,8.703135093227193,9.989711205477885,8.703135093227193]]]}}},"view":{"type":"object","name":"CDSView","id":"p32856","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p32857"}}},"glyph":{"type":"object","name":"Line","id":"p32852","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p32853","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p32854","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#5f6368","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p32861","attributes":{"data_source":{"id":"p32807"},"view":{"type":"object","name":"CDSView","id":"p32862","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p32863"}}},"glyph":{"type":"object","name":"Scatter","id":"p32858","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"hatch_color":{"type":"value","value":"#5f6368"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p32859","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p32860","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#5f6368"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#5f6368"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p32818","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p32832"},{"type":"object","name":"BoxZoomTool","id":"p32833","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p32834","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p32840","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p32839","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p32841","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p32842"},{"type":"object","name":"SaveTool","id":"p32843"},{"type":"object","name":"HoverTool","id":"p32864","attributes":{"renderers":[{"id":"p32861"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p32827","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p32828","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p32829"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p32830"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p32822","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p32823","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p32824"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p32825"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p32826","attributes":{"axis":{"id":"p32822"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p32831","attributes":{"dimension":1,"axis":{"id":"p32827"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p32844","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2022.5,"right":{"type":"object","name":"Node","id":"p32846","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p32847","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p32848","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p32850","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p32849","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p32851","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"ac681088-de79-4fe2-9b12-0ff9a67cab0a","roots":{"p32810":"fe00d685-6798-4096-8dc4-2ff47adee704"},"root_ids":["p32810"]}];
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

<div id="e4750831-3cc8-433f-9ebc-dc2ff3230856" data-root-id="p32870" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"303c0653-0dbb-4f95-ace6-13e44cb058b3":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p32910","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p32911"}}},"roots":[{"type":"object","name":"Figure","id":"p32870","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p32871"},"y_range":{"type":"object","name":"DataRange1d","id":"p32872","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p32879"},"y_scale":{"type":"object","name":"LinearScale","id":"p32880"},"title":{"type":"object","name":"Title","id":"p32877","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p32906","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p32867","attributes":{"selected":{"type":"object","name":"Selection","id":"p32868","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p32869"},"data":{"type":"map","entries":[["year",[2014,2017,2018,2019,2020,2023,2024,2026]],["evaluable",[3,2,1,10,2,1,8,1]],["detected",[3,2,1,4,0,0,3,1]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368"]]]}}},"view":{"type":"object","name":"CDSView","id":"p32907","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p32908"}}},"glyph":{"type":"object","name":"VBar","id":"p32903","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p32904","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p32905","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p32878","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p32891"},{"type":"object","name":"BoxZoomTool","id":"p32892","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p32893","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p32899","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p32898","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p32900","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p32901"},{"type":"object","name":"SaveTool","id":"p32902"},{"type":"object","name":"HoverTool","id":"p32909","attributes":{"renderers":[{"id":"p32906"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p32886","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p32887","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p32888"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p32889"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p32881","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p32882","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p32883"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p32884"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p32885","attributes":{"axis":{"id":"p32881"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p32890","attributes":{"dimension":1,"axis":{"id":"p32886"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"303c0653-0dbb-4f95-ace6-13e44cb058b3","roots":{"p32870":"e4750831-3cc8-433f-9ebc-dc2ff3230856"},"root_ids":["p32870"]}];
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

<div id="e230a473-7546-4493-b8c0-579fcc496e37" data-root-id="p32915" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"651c2877-a22c-43f2-ac0b-80acf99158dd":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p32957","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p32958"}}},"roots":[{"type":"object","name":"Figure","id":"p32915","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p32917"},"y_range":{"type":"object","name":"FactorRange","id":"p32924","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p32925"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p32926"},"title":{"type":"object","name":"Title","id":"p32922","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p32952","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p32912","attributes":{"selected":{"type":"object","name":"Selection","id":"p32913","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p32914"},"data":{"type":"map","entries":[["x",[-1,-20]],["y",["reverse","forward"]],["alpha",[1.0,1.0]],["pos",[1,20]],["base",["G","G"]],["n",[20,27]],["det_with",["30% of 20","48% of 27"]],["det_without",["100% of 8","100% of 1"]],["subs",["G&gt;A 20","G&gt;C 27"]],["zone",["yes","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p32953","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p32954"}}},"glyph":{"type":"object","name":"Rect","id":"p32949","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p32950","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p32951","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p32923","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p32937"},{"type":"object","name":"BoxZoomTool","id":"p32938","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p32939","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p32945","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p32944","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p32946","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p32947"},{"type":"object","name":"SaveTool","id":"p32948"},{"type":"object","name":"HoverTool","id":"p32955","attributes":{"renderers":[{"id":"p32952"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p32932","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p32933"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p32934"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p32935"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p32927","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p32956","attributes":{"ticks":[-20,-1],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p32929"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-1,"1"],[-20,"20"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p32930"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p32931","attributes":{"axis":{"id":"p32927"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p32936","attributes":{"dimension":1,"axis":{"id":"p32932"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"651c2877-a22c-43f2-ac0b-80acf99158dd","roots":{"p32915":"e230a473-7546-4493-b8c0-579fcc496e37"},"root_ids":["p32915"]}];
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

Disclosures on this entry: `pairing_is_curator_reading`.


## What reached the statistics

279 records were screened for this assay and **28 (10%)** were evaluable, meaning both primers landed in the right orientation and size range. 251 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 187 |
| `truncated` | 56 |
| `chance_anchor` | 7 |
| `chance_only` | 1 |

