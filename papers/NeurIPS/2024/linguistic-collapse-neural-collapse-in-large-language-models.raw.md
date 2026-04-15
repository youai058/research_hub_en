---
title: "Linguistic Collapse: Neural Collapse in (Large) Language Models"
authors: ["Robert Wu", "Vardan Papyan"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "G0LfcMiRkc"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/90683e10fe052468efca9262de53b88c6f422097.pdf"
published: "2024"
categories: []
keywords: ["neural collapse", "uniformity", "large language models", "LLM", "GPT", "language modeling", "geometry", "unconstrained features", "generative model", "transformer", "attention", "causal", "autoregressive"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:55+09:00"
---

# Linguistic Collapse: Neural Collapse in (Large) Language Models

## Abstract
Neural collapse ($\mathcal{NC}$) is a phenomenon observed in classification tasks where top-layer representations collapse into their class means, which become equinorm, equiangular and aligned with the classifiers.
These behaviors -- associated with generalization and robustness -- would manifest under specific conditions: models are trained towards zero loss, with noise-free labels belonging to balanced classes, which do not outnumber the model's hidden dimension.
Recent studies have explored $\mathcal{NC}$ in the absence of one or more of these conditions to extend and capitalize on the associated benefits of ideal geometries.
Language modeling presents a curious frontier, as \textit{training by token prediction} constitutes a classification task where none of the conditions exist: the vocabulary is imbalanced and exceeds the embedding dimension; different tokens might correspond to similar contextual embeddings; and large language models (LLMs) in particular are typically only trained for a few epochs.
This paper empirically investigates the impact of scaling the architectures and training of causal language models (CLMs) on their progression towards $\mathcal{NC}$.
We find that $\mathcal{NC}$ properties that develop with scale (and regularization) are linked to generalization.
Moreover, there is evidence of some relationship between $\mathcal{NC}$ and generalization independent of scale.
Our work thereby underscores the generality of $\mathcal{NC}$ as it extends to the novel and more challenging setting of language modeling.
Downstream, we seek to inspire further research on the phenomenon to deepen our understanding of LLMs -- and neural networks at large -- and improve existing architectures based on $\mathcal{NC}$-related properties.
Our code is hosted on GitHub: [`https://github.com/rhubarbwu/linguistic-collapse`](https://github.com/rhubarbwu/linguistic-collapse).

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Robert Wu, Vardan Papyan
- arxiv_id: 
- openreview_id: G0LfcMiRkc
- anthology_id: 
- pdf_url: https://openreview.net/pdf/90683e10fe052468efca9262de53b88c6f422097.pdf
- published: 2024
- keywords: neural collapse, uniformity, large language models, LLM, GPT, language modeling, geometry, unconstrained features, generative model, transformer, attention, causal, autoregressive
