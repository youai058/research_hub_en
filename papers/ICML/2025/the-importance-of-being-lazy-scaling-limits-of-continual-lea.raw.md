---
title: "The Importance of Being Lazy: Scaling Limits of Continual Learning"
authors: ["Jacopo Graldi", "Alessandro Breccia", "Giulia Lanzillotta", "Thomas Hofmann", "Lorenzo Noci"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "edhBkkYS8R"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/791c0ae7246e770543382d739786f83d3080a09d.pdf"
published: "2025"
categories: []
keywords: ["feature learning", "continual learning", "deep learning", "forgetting", "ntk", "muP", "lazy", "dmft"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:07+09:00"
---

# The Importance of Being Lazy: Scaling Limits of Continual Learning

## Abstract
Despite recent efforts, neural networks still struggle to learn in non-stationary environments, and our understanding of catastrophic forgetting (CF) is far from complete.
In this work, we perform a systematic study on the impact of model scale and the degree of feature learning in continual learning. We reconcile existing contradictory observations on scale in the literature, by differentiating between *lazy* and *rich* training regimes through a variable parameterization of the architecture. We show that increasing model width is only beneficial when it reduces the amount of *feature learning*, yielding more laziness. Using the framework of dynamical mean field theory, we then study the infinite width dynamics of the model in the feature learning regime and characterize CF, extending prior theoretical results limited to the lazy regime. We study the intricate relationship between feature learning, task non-stationarity, and forgetting, finding that high feature learning is only beneficial with highly similar tasks. We identify a transition modulated by task similarity where the model exits an effectively lazy regime with low forgetting to enter a rich regime with significant forgetting. Finally, our findings reveal that neural networks achieve optimal performance at a critical level of feature learning, which depends on task non-stationarity and *transfers across model scales*. This work provides a unified perspective on the role of scale and feature learning in continual learning.

## Metadata
- venue: ICML
- year: 2025
- authors: Jacopo Graldi, Alessandro Breccia, Giulia Lanzillotta, Thomas Hofmann, Lorenzo Noci
- arxiv_id: 
- openreview_id: edhBkkYS8R
- anthology_id: 
- pdf_url: https://openreview.net/pdf/791c0ae7246e770543382d739786f83d3080a09d.pdf
- published: 2025
- keywords: feature learning, continual learning, deep learning, forgetting, ntk, muP, lazy, dmft
