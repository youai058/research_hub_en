---
title: "Decomposing and Editing Predictions by Modeling Model Computation"
authors: ["Harshay Shah", "Andrew Ilyas", "Aleksander Madry"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rTBR0eqE4G"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4219c2823786d14eea86c45e5436c6386089c7af.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:23+09:00"
---

# Decomposing and Editing Predictions by Modeling Model Computation

## Abstract
*How does the internal computation of a machine learning model transform inputs into predictions?* To tackle this question, we introduce a framework called *component modeling* for decomposing a model prediction in terms of its components---architectural "building blocks" such as convolution filters or attention heads. We focus on a special case of this framework, *component attribution*, where the goal is to estimate the counterfactual impact of individual components on a given prediction. We then present COAR, a scalable algorithm for estimating component attributions, and demonstrate its effectiveness across models, datasets and modalities. Finally, we show that COAR directly enables effective model editing. Our code is available at [github.com/MadryLab/modelcomponents]([https://github.com/MadryLab/modelcomponents]).

## Metadata
- venue: ICML
- year: 2024
- authors: Harshay Shah, Andrew Ilyas, Aleksander Madry
- arxiv_id: 
- openreview_id: rTBR0eqE4G
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4219c2823786d14eea86c45e5436c6386089c7af.pdf
- published: 2024
