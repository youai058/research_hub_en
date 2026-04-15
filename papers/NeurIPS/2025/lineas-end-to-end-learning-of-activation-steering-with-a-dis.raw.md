---
title: "LinEAS: End-to-end Learning of Activation Steering with a Distributional Loss"
authors: ["Pau Rodriguez", "Michal Klein", "Eleonora Gualdoni", "Valentino Maiorca", "Arno Blaas", "Luca Zappella", "marco cuturi", "Xavier Suau"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "EBONa3tT3K"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6bd79496ce93954c9b101c724edeeb4fafdf93e7.pdf"
published: "2025"
categories: []
keywords: ["controllability", "generative models", "toxicity", "images"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:39+09:00"
---

# LinEAS: End-to-end Learning of Activation Steering with a Distributional Loss

## Abstract
The growing use of generative models in daily life calls for efficient mechanisms to control their generation, to e.g. produce safe content or provide users with tools to explore style changes. Ideally, such mechanisms should require low volume of unpaired data (\ie without explicit preference), and should be cheap, both at train and inference time, while preserving output quality. Recent research has shown that such mechanisms can be obtained by intervening exclusively on model activations, with the goal of correcting distributional differences between activations seen when using prompts from a source vs. a target set (e.g. toxic and non-toxic sentences). While cheap, these fast methods are inherently crude: their maps are tuned locally, not accounting for their impact on downstream layers, resulting in interventions that cause unintended shifts when used out-of-sample. We propose in this work linear end-to-end activation steering (LinEAS), an approach trained with a global loss that accounts simultaneously for all layer-wise distributional shifts. In addition to being more robust, the loss used to train LinEAS can be regularized with sparsifying norms, which can automatically carry out neuron selection. LinEAS only requires a handful of unpaired samples to be effective, and beats similar baselines on toxicity mitigation in language models, becoming competitive with oracle-dependent methods that have access to strong supervision. LinEAS is modality-agnostic and we empirically find that it outperforms existing activation steering methods at mitigating and including new concepts at the output of single-step text-to-image generation models.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Pau Rodriguez, Michal Klein, Eleonora Gualdoni, Valentino Maiorca, Arno Blaas, Luca Zappella, marco cuturi, Xavier Suau
- arxiv_id: 
- openreview_id: EBONa3tT3K
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6bd79496ce93954c9b101c724edeeb4fafdf93e7.pdf
- published: 2025
- keywords: controllability, generative models, toxicity, images
