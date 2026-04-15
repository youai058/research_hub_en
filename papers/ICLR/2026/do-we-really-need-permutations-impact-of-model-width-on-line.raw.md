---
title: "Do We Really Need Permutations? Impact of Model Width on Linear Mode Connectivity"
authors: ["Akira Ito", "Masanori Yamada", "Daiki Chijiwa", "Atsutoshi Kumagai"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ll8GLAic7q"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/57b521ef9055db739fd53c9e113a0b4ea739413d.pdf"
published: "2026"
categories: []
keywords: ["deep learning", "linear mode connectivity", "permutation symmetries"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:29+09:00"
---

# Do We Really Need Permutations? Impact of Model Width on Linear Mode Connectivity

## Abstract
Recently, Ainsworth et al. empirically demonstrated that, given two independently trained models, applying a parameter permutation that preserves the input–output behavior allows the two models to be connected by a low-loss linear path. When such a path exists, the models are said to achieve linear mode connectivity (LMC). Prior studies, including Ainsworth et al. (2023), have reported that achieving LMC requires not only an appropriate permutation search but also sufficiently wide models (e.g., a 32 $\times$ width multiplier for ResNet-20). This is broadly believed to be because increasing the model width ensures a large enough space of candidate permutations, increasing the chance of finding one that yields LMC. In this work, we empirically demonstrate that, __even without any permutations__, simply widening the models is sufficient for achieving LMC when using a suitable softmax temperature calibration. We further explain why this phenomenon arises by analyzing intermediate layer outputs. Specifically, we introduce layerwise exponentially weighted connectivity (LEWC), which states that the output of each layer of the merged model can be represented as an exponentially weighted sum of the outputs of the corresponding layers of the original models. Consequently the merged model's output matches that of an ensemble of the original models, facilitating LMC. To the best of our knowledge, this work is the first to show that widening the model not only facilitates __nonlinear__ mode connectivity, as suggested in prior research, but also significantly increases the possibility of achieving __linear__ mode connectivity.

## Metadata
- venue: ICLR
- year: 2026
- authors: Akira Ito, Masanori Yamada, Daiki Chijiwa, Atsutoshi Kumagai
- arxiv_id: 
- openreview_id: ll8GLAic7q
- anthology_id: 
- pdf_url: https://openreview.net/pdf/57b521ef9055db739fd53c9e113a0b4ea739413d.pdf
- published: 2026
- keywords: deep learning, linear mode connectivity, permutation symmetries
