---
title: "Manipulating dropout reveals an optimal balance of efficiency and robustness in biological and machine visual systems"
authors: ["Jacob S. Prince", "Gabriel Fajardo", "George A. Alvarez", "Talia Konkle"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ADDCErFzev"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7f10cc682acaa93ecdd9fa4c23e343be124115dd.pdf"
published: "2024"
categories: []
keywords: ["Efficient coding", "object representation", "dropout", "robustness", "human fMRI", "occipitotemporal cortex", "cognitive neuroscience", "distributed coding"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:56+09:00"
---

# Manipulating dropout reveals an optimal balance of efficiency and robustness in biological and machine visual systems

## Abstract
According to the efficient coding hypothesis, neural populations encode information optimally when representations are high-dimensional and uncorrelated. However, such codes may carry a cost in terms of generalization and robustness. Past empirical studies of early visual cortex (V1) in rodents have suggested that this tradeoff indeed constrains sensory representations. However, it remains unclear whether these insights generalize across the hierarchy of the human visual system, and particularly to object representations in high-level occipitotemporal cortex (OTC). To gain new empirical clarity, here we develop a family of object recognition models with parametrically varying dropout proportion $p$, which induces systematically varying dimensionality of internal responses (while controlling all other inductive biases). We find that increasing dropout produces an increasingly smooth, low-dimensional representational space. Optimal robustness to lesioning is observed at around 70% dropout, after which both accuracy and robustness decline. Representational comparison to large-scale 7T fMRI data from occipitotemporal cortex in the Natural Scenes Dataset reveals that this optimal degree of dropout is also associated with maximal emergent neural predictivity. Finally, using new techniques for achieving denoised estimates of the eigenspectrum of human fMRI responses, we compare the rate of eigenspectrum decay between model and brain feature spaces. We observe that the match between model and brain representations is associated with a common balance between efficiency and robustness in the representational space. These results suggest that varying dropout may reveal an optimal point of balance between the efficiency of high-dimensional codes and the robustness of low dimensional codes in hierarchical vision systems.

## Metadata
- venue: ICLR
- year: 2024
- authors: Jacob S. Prince, Gabriel Fajardo, George A. Alvarez, Talia Konkle
- arxiv_id: 
- openreview_id: ADDCErFzev
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7f10cc682acaa93ecdd9fa4c23e343be124115dd.pdf
- published: 2024
- keywords: Efficient coding, object representation, dropout, robustness, human fMRI, occipitotemporal cortex, cognitive neuroscience, distributed coding
