# FILOVIRUS_ssRNA_L_gene

<span class="aw-chip aw-chip-stable">stable</span>

**FILOVIRUS (ssRNA) — L gene**

| | |
|---|---|
| Target | Filoviridae ([taxid 11266](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11266)) |
| Gene | L gene |
| Chemistry | conventional |
| Amplicon | 634 bp |
| Designed | 2007 |
| Paper | [10.1128/Jcm.01893-06](https://doi.org/10.1128/Jcm.01893-06) |
| Registry status | active |

!!! quote "The paper"
    Zhai, J. H. et al. Rapid molecular strategy for filovirus detection and characterization. Journal of clinical microbiology 45, 224-226, doi:Doi 10.1128/Jcm.01893-06 (2007).

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `TATTCTCYCTACAAAAGCATTGGG` | 24 nt |
| reverse | `GCTTCTGCGAGTGTTTGGACATT` | 23 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 109 | 110 | 99.1% | 95.0% – 99.8% |
| baseline (everything earlier) | 3,785 | 3,817 | 99.2% | 98.8% – 99.4% |

Change from baseline, Newcombe interval: **-4.1% to 0.8%**. Threshold: **90.0%**.

*detected share 99.1% (95%-100%) since Oct 2024*

Trend across deposit years: by record rising (p=0.00191, 33 years); by footprint falling (p=0.373); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the 90% threshold. Larger markers mean more records, and the chart below gives the
counts exactly — 100% of three records and 100% of three thousand are not the same
claim.

<div id="ecc67c95-7ffb-4706-9dc7-2d4c7593f824" data-root-id="p12669" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"d63f62d1-cf09-45e7-b4ad-8f9459e9ed06":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12724","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12725"}}},"roots":[{"type":"object","name":"Figure","id":"p12669","attributes":{"height":300,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p12671"},"y_range":{"type":"object","name":"Range1d","id":"p12678","attributes":{"start":-3,"end":103}},"x_scale":{"type":"object","name":"LinearScale","id":"p12679"},"y_scale":{"type":"object","name":"LinearScale","id":"p12680"},"title":{"type":"object","name":"Title","id":"p12676","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12714","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12666","attributes":{"selected":{"type":"object","name":"Selection","id":"p12667","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12668"},"data":{"type":"map","entries":[["year",[1992,1993,1994,1995,1997,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["share",[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,66.66666666666666,100.0,59.375,62.5,100.0,100.0,100.0,99.89495798319328,100.0,99.33774834437085,99.11894273127754,100.0,100.0,99.85590778097982,88.23529411764706,96.85534591194968,97.91666666666666,100.0,100.0]],["detected",[2,1,2,1,1,2,1,1,4,2,5,1,13,3,2,29,19,5,36,33,119,951,921,150,225,276,27,693,30,154,94,9,82]],["evaluable",[2,1,2,1,1,2,1,1,4,2,5,1,13,3,3,29,32,8,36,33,119,952,921,151,227,276,27,694,34,159,96,9,82]],["window",["baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","baseline","recent","recent","recent"]],["size",[9.07684386569143,8.703135093227193,9.07684386569143,8.703135093227193,8.703135093227193,9.07684386569143,8.703135093227193,8.703135093227193,9.517227179437622,9.07684386569143,9.667366891029102,8.703135093227193,10.324834530005162,9.328625426046248,9.328625426046248,10.869436534339137,10.934913263353746,9.989711205477885,11.012804945939648,10.955310988645032,11.773797988966388,12.973831887291771,12.955816040201865,11.918861457530289,12.162334373674176,12.276960398029692,10.821697436206254,12.80049080989074,10.975067467348278,11.95002790869381,11.641139586689716,10.071067811865476,11.542654874768257]]]}}},"view":{"type":"object","name":"CDSView","id":"p12715","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12716"}}},"glyph":{"type":"object","name":"Line","id":"p12711","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p12712","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p12713","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"line_color":"#007d5c","line_alpha":0.2,"line_width":2}}}},{"type":"object","name":"GlyphRenderer","id":"p12720","attributes":{"data_source":{"id":"p12666"},"view":{"type":"object","name":"CDSView","id":"p12721","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12722"}}},"glyph":{"type":"object","name":"Scatter","id":"p12717","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"hatch_color":{"type":"value","value":"#007d5c"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p12718","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p12719","attributes":{"x":{"type":"field","field":"year"},"y":{"type":"field","field":"share"},"size":{"type":"field","field":"size"},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":2},"fill_color":{"type":"value","value":"#007d5c"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#007d5c"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12677","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12691"},{"type":"object","name":"BoxZoomTool","id":"p12692","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12693","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12699","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12698","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12700","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12701"},{"type":"object","name":"SaveTool","id":"p12702"},{"type":"object","name":"HoverTool","id":"p12723","attributes":{"renderers":[{"id":"p12720"}],"tooltips":[["year","@year"],["detected","@detected of @evaluable"],["share","@share{0.0}%"],["window","@window"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p12686","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12687","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12688"},"axis_label":"predicted detection (%)","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12689"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12681","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12682","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12683"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12684"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12685","attributes":{"axis":{"id":"p12681"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12690","attributes":{"dimension":1,"axis":{"id":"p12686"},"grid_line_color":"#e5e7e9"}},{"type":"object","name":"BoxAnnotation","id":"p12703","attributes":{"line_color":null,"fill_color":"#5f6368","fill_alpha":0.07,"left":2023.5,"right":{"type":"object","name":"Node","id":"p12705","attributes":{"target":"frame","symbol":"right"}},"top":{"type":"object","name":"Node","id":"p12706","attributes":{"target":"frame","symbol":"top"}},"bottom":{"type":"object","name":"Node","id":"p12707","attributes":{"target":"frame","symbol":"bottom"}},"handles":{"type":"object","name":"BoxInteractionHandles","id":"p12709","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12708","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}},{"type":"object","name":"Span","id":"p12710","attributes":{"location":90.0,"line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"d63f62d1-cf09-45e7-b4ad-8f9459e9ed06","roots":{"p12669":"ecc67c95-7ffb-4706-9dc7-2d4c7593f824"},"root_ids":["p12669"]}];
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

<div id="cc8c3974-ef78-483b-83f9-999e91fb436b" data-root-id="p12729" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"b9346d0a-53c5-4a31-8f9b-e81eae117b46":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12769","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12770"}}},"roots":[{"type":"object","name":"Figure","id":"p12729","attributes":{"height":130,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p12730"},"y_range":{"type":"object","name":"DataRange1d","id":"p12731","attributes":{"start":0}},"x_scale":{"type":"object","name":"LinearScale","id":"p12738"},"y_scale":{"type":"object","name":"LinearScale","id":"p12739"},"title":{"type":"object","name":"Title","id":"p12736","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12765","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12726","attributes":{"selected":{"type":"object","name":"Selection","id":"p12727","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12728"},"data":{"type":"map","entries":[["year",[1992,1993,1994,1995,1997,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]],["evaluable",[2,1,2,1,1,2,1,1,4,2,5,1,13,3,3,29,32,8,36,33,119,952,921,151,227,276,27,694,34,159,96,9,82]],["detected",[2,1,2,1,1,2,1,1,4,2,5,1,13,3,2,29,19,5,36,33,119,951,921,150,225,276,27,693,30,154,94,9,82]],["colour",["#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#5f6368","#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p12766","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12767"}}},"glyph":{"type":"object","name":"VBar","id":"p12762","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"VBar","id":"p12763","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"VBar","id":"p12764","attributes":{"x":{"type":"field","field":"year"},"width":{"type":"value","value":0.72},"top":{"type":"field","field":"evaluable"},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12737","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12750"},{"type":"object","name":"BoxZoomTool","id":"p12751","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12752","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12758","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12757","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12759","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12760"},{"type":"object","name":"SaveTool","id":"p12761"},{"type":"object","name":"HoverTool","id":"p12768","attributes":{"renderers":[{"id":"p12765"}],"tooltips":[["year","@year"],["evaluable","@evaluable"],["detected","@detected"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"LinearAxis","id":"p12745","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12746","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12747"},"axis_label":"evaluable records","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12748"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12740","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12741","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12742"},"axis_label":"deposit year","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12743"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12744","attributes":{"axis":{"id":"p12740"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12749","attributes":{"dimension":1,"axis":{"id":"p12745"},"grid_line_color":"#e5e7e9"}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"b9346d0a-53c5-4a31-8f9b-e81eae117b46","roots":{"p12729":"cc8c3974-ef78-483b-83f9-999e91fb436b"},"root_ids":["p12729"]}];
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

<div id="c717ff7b-7bc1-4d51-8835-a765e9cfadb4" data-root-id="p12774" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"36ea061d-fd78-42da-90c8-f0d0ebf180a1":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12816","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12817"}}},"roots":[{"type":"object","name":"Figure","id":"p12774","attributes":{"height":154,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p12776"},"y_range":{"type":"object","name":"FactorRange","id":"p12783","attributes":{"factors":["reverse","forward"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p12784"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p12785"},"title":{"type":"object","name":"Title","id":"p12781","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12811","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12771","attributes":{"selected":{"type":"object","name":"Selection","id":"p12772","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12773"},"data":{"type":"map","entries":[["x",[-12,-15,-6,-11,-17,-20,-16,-21,-23,-8,-14]],["y",["reverse","reverse","reverse","forward","forward","forward","forward","reverse","forward","forward","forward"]],["alpha",[0.1673160173160173,0.1906926406926407,0.22792207792207791,0.1777056277056277,0.23225108225108224,0.23484848484848486,0.2564935064935065,0.21666666666666667,0.24783549783549783,0.36298701298701297,1.0]],["pos",[12,15,6,11,17,20,16,21,23,8,14]],["base",["T","G","G","A","Y","C","C","T","A","G","A"]],["n",[20,47,90,32,95,98,123,77,113,246,2346]],["det_with",["0% of 20","70% of 47","78% of 90","78% of 32","80% of 95","82% of 98","84% of 123","88% of 77","89% of 113","96% of 246","99% of 2346"]],["det_without",["100% of 3926","100% of 3899","100% of 3856","99% of 3914","100% of 3851","100% of 3848","100% of 3823","99% of 3869","99% of 3833","99% of 3700","99% of 1600"]],["subs",["T&gt;A 11, G&gt;A 7, T&gt;C 2","G&gt;A 23, G&gt;T 12, G&gt;C 7, A&gt;C 4","G&gt;A 79, A&gt;T 9, A&gt;C 2","A&gt;G 32","Y&gt;A 78, T&gt;A 10, A&gt;T 7","C&gt;T 97, T&gt;C 1","C&gt;G 77, C&gt;T 26, G&gt;A 14, C&gt;A 6","C&gt;T 70, T&gt;C 7","A&gt;G 99, A&gt;C 11, A&gt;T 3","G&gt;A 246","T&gt;A 2238, A&gt;G 75, T&gt;C 26, A&gt;T 7"]],["zone",["no","no","no","no","no","no","no","no","no","no","no"]]]}}},"view":{"type":"object","name":"CDSView","id":"p12812","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12813"}}},"glyph":{"type":"object","name":"Rect","id":"p12808","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"field","field":"alpha"},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"field","field":"alpha"},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"field","field":"alpha"}}},"nonselection_glyph":{"type":"object","name":"Rect","id":"p12809","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.1},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Rect","id":"p12810","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"width":{"type":"value","value":0.9},"height":{"type":"value","value":0.62},"line_color":{"type":"value","value":null},"line_alpha":{"type":"value","value":0.2},"fill_color":{"type":"value","value":"#b3261e"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"value","value":"#b3261e"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12782","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12796"},{"type":"object","name":"BoxZoomTool","id":"p12797","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12798","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12804","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12803","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12805","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12806"},{"type":"object","name":"SaveTool","id":"p12807"},{"type":"object","name":"HoverTool","id":"p12814","attributes":{"renderers":[{"id":"p12811"}],"tooltips":[["oligo","@y, position @pos from 3&#x27;"],["oligo base","@base"],["records mismatching","@n"],["detected when mismatched","@det_with"],["detected when not","@det_without"],["substitutions","@subs"],["inside the 3&#x27; window","@zone"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p12791","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p12792"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p12793"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12794"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12786","attributes":{"ticker":{"type":"object","name":"FixedTicker","id":"p12815","attributes":{"ticks":[-23,-21,-20,-17,-16,-15,-14,-12,-11,-8,-6],"minor_ticks":[]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12788"},"axis_label":"position from the 3&#x27; end (1 = the terminal base)","axis_label_text_font_style":"normal","major_label_overrides":{"type":"map","entries":[[-12,"12"],[-15,"15"],[-6,"6"],[-11,"11"],[-17,"17"],[-20,"20"],[-16,"16"],[-21,"21"],[-23,"23"],[-8,"8"],[-14,"14"]]},"major_label_policy":{"type":"object","name":"AllLabels","id":"p12789"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12790","attributes":{"axis":{"id":"p12786"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12795","attributes":{"dimension":1,"axis":{"id":"p12791"},"grid_line_color":null}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"36ea061d-fd78-42da-90c8-f0d0ebf180a1","roots":{"p12774":"c717ff7b-7bc1-4d51-8835-a765e9cfadb4"},"root_ids":["p12774"]}];
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

<div id="cc48ce60-c586-475b-a9c8-d262dcdd89d3" data-root-id="p12821" style="display: contents;"></div>
<script>
(function() {
  const fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
        const docs_json = '{"c2d428b3-4f47-444f-b603-608e2cd5f9b3":{"version":"3.10.1","title":"Bokeh Application","config":{"type":"object","name":"DocumentConfig","id":"p12870","attributes":{"notifications":{"type":"object","name":"Notifications","id":"p12871"}}},"roots":[{"type":"object","name":"Figure","id":"p12821","attributes":{"height":158,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"Range1d","id":"p12830","attributes":{"end":103}},"y_range":{"type":"object","name":"FactorRange","id":"p12831","attributes":{"factors":["Orthoebolavirus bundibugyoense (3052458)","Orthoebolavirus zairense (3052462)","Orthomarburgvirus marburgense (3052505)"]}},"x_scale":{"type":"object","name":"LinearScale","id":"p12832"},"y_scale":{"type":"object","name":"CategoricalScale","id":"p12833"},"title":{"type":"object","name":"Title","id":"p12828","attributes":{"text_font_style":"normal"}},"outline_line_color":null,"renderers":[{"type":"object","name":"GlyphRenderer","id":"p12865","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p12818","attributes":{"selected":{"type":"object","name":"Selection","id":"p12819","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p12820"},"data":{"type":"map","entries":[["y",["Orthoebolavirus bundibugyoense (3052458)","Orthoebolavirus zairense (3052462)","Orthomarburgvirus marburgense (3052505)"]],["share",[100.0,100.0,100.0]],["lo",[90.1099007675596,91.03331462924287,89.84854458466761]],["hi",[100.0,100.0,100.0]],["n",[35,39,34]],["det",[35,39,34]],["colour",["#007d5c","#007d5c","#007d5c"]]]}}},"view":{"type":"object","name":"CDSView","id":"p12866","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p12867"}}},"glyph":{"type":"object","name":"Scatter","id":"p12862","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"hatch_color":{"type":"field","field":"colour"}}},"nonselection_glyph":{"type":"object","name":"Scatter","id":"p12863","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.1},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.1},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.1}}},"muted_glyph":{"type":"object","name":"Scatter","id":"p12864","attributes":{"x":{"type":"field","field":"share"},"y":{"type":"field","field":"y"},"size":{"type":"value","value":9},"line_color":{"type":"value","value":"#fcfcfb"},"line_alpha":{"type":"value","value":0.2},"line_width":{"type":"value","value":1.5},"fill_color":{"type":"field","field":"colour"},"fill_alpha":{"type":"value","value":0.2},"hatch_color":{"type":"field","field":"colour"},"hatch_alpha":{"type":"value","value":0.2}}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p12829","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p12844"},{"type":"object","name":"BoxZoomTool","id":"p12845","attributes":{"dimensions":"both","overlay":{"type":"object","name":"BoxAnnotation","id":"p12846","attributes":{"syncable":false,"line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","handles":{"type":"object","name":"BoxInteractionHandles","id":"p12852","attributes":{"all":{"type":"object","name":"AreaVisuals","id":"p12851","attributes":{"fill_color":"white","hover_fill_color":"lightgray"}}}}}}}},{"type":"object","name":"WheelZoomTool","id":"p12853","attributes":{"renderers":"auto"}},{"type":"object","name":"ResetTool","id":"p12854"},{"type":"object","name":"SaveTool","id":"p12855"},{"type":"object","name":"HoverTool","id":"p12869","attributes":{"renderers":[{"id":"p12865"}],"tooltips":[["lineage","@y"],["detected","@det of @n"],["share","@share{0.0}%"],["95% interval","@lo{0.0}-@hi{0.0}%"]],"sort_by":null}}],"logo":null}},"toolbar_location":"above","left":[{"type":"object","name":"CategoricalAxis","id":"p12839","attributes":{"ticker":{"type":"object","name":"CategoricalTicker","id":"p12840"},"formatter":{"type":"object","name":"CategoricalTickFormatter","id":"p12841"},"axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12842"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"below":[{"type":"object","name":"LinearAxis","id":"p12834","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p12835","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p12836"},"axis_label":"predicted detection (%), bar = 95% interval","axis_label_text_font_style":"normal","major_label_policy":{"type":"object","name":"AllLabels","id":"p12837"},"axis_line_color":"#e5e7e9","major_tick_line_color":"#e5e7e9","minor_tick_line_color":null}}],"center":[{"type":"object","name":"Grid","id":"p12838","attributes":{"axis":{"id":"p12834"},"grid_line_color":null}},{"type":"object","name":"Grid","id":"p12843","attributes":{"dimension":1,"axis":{"id":"p12839"},"grid_line_color":null}},{"type":"object","name":"Whisker","id":"p12856","attributes":{"source":{"id":"p12818"},"lower":{"type":"field","field":"lo"},"lower_head":null,"upper":{"type":"field","field":"hi"},"upper_head":null,"base":{"type":"field","field":"y"},"dimension":"width","line_color":{"type":"value","value":"#5f6368"}}},{"type":"object","name":"Span","id":"p12868","attributes":{"location":90.0,"dimension":"height","line_color":"#5f6368","line_dash":[6]}}],"background_fill_color":null,"border_fill_color":null}}]}}';
        const render_items = [{"docid":"c2d428b3-4f47-444f-b603-608e2cd5f9b3","roots":{"p12821":"cc48ce60-c586-475b-a9c8-d262dcdd89d3"},"root_ids":["p12821"]}];
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

4,647 records were screened for this assay and **3,927 (85%)** were evaluable, meaning both primers landed in the right orientation and size range. 720 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 525 |
| `chance_anchor` | 146 |
| `truncated` | 43 |

