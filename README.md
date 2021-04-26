# lca-methods-timeline
A timeline of methods for life cycle assessment (LCA)

## TL;DR
Data collection is ongoing. Please open an [issue](https://github.com/BenPortner/lca-methods-timeline/issues) to report errors or to make suggestions.
The interactive timeline with tooltips is available on [githack](https://rawcdn.githack.com/BenPortner/lca-methods-timeline/434efa66b580472bf3349b071abf3095dc18e228/visualization/timeline.html). You can also [download](https://github.com/BenPortner/lca-methods-timeline/archive/refs/heads/main.zip) the repo and view the file locally on your computer. View in 1920 x 1080 resolution for best results. Alternatively, see the [static version](https://github.com/BenPortner/lca-methods-timeline/tree/main/visualization/timeline.png).

## Introduction

This repo is an attempt to create a timeline of impact assessment methods for Life Cycle Assessment (LCA). The data was collected from four sources:
- Figure 2.1 from Rosenbaum, R. K. (2017). Selection of Impact Categories, Category Indicators and Characterization Models in Goal and Scope Definition. In Goal and Scope Definition in Life Cycle Assessment (p. 65). Springer, Dordrecht.
- Figure 1 from Pizzol, M., Christensen, P., Schmidt, J., & Thomsen, M. (2011). Impacts of “metals” on human health: a comparison between nine different methodologies for Life Cycle Impact Assessment (LCIA). Journal of Cleaner Production, 19(6-7), 646-656.
- Figure 1.1 from Frischknecht, R. Jolliet, O., Milà i Canals, L., Pfister, S., Sahnoune, A., Ugaya, C. & Vigon, B. (2016). Motivation, Context and Overview. In Global Guidance for Life Cycle Impact Assessment Indicators Vol. 1 (p. 31). UNEP/SETAC Life Cycle Initiative.
- Lecture slides provided by Bo P. Weidema.

Additional data (current website, publications, ...) were obtained via a google search.

## Contents

In the main folder:

`methods.json` contains the collected data: 
- name
- alternative names (synonyms)
- year of release
- origin (region/country of development), 
- relevant publications
- website 
- previous methods borrowed from (parents).

In the `visualization` folder:
- `timeline_interactive.py`: a python script, which reads the data, creates a timeline using plotly and exports it as a .html file `timeline.html` 
- `timeline.html` an interactive html document, showing the timelien of lca methods. When hovering over individual methods, additional data is shown in tooltips. The Graph can be panned, zoomed or exported as an image file
- `timeline.png` exported image file

## License

The data, code and visualizations are provided under a GPL 3.0 license. This means you are free to use, modify and distribute them privately or commercially, as long as you a) link to this repo as the source b) state any changes made and c) provide derivatives freely under the exact same license. No warranty is given for data, code or visualizations. No lability is taken for any damages that may result from their use. For more information, please read the [license](https://github.com/BenPortner/lca-methods-timeline/blob/main/LICENSE) contained in the repo.