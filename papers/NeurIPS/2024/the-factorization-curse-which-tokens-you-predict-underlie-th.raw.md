---
title: "The Factorization Curse: Which Tokens You Predict Underlie the Reversal Curse and More"
authors: ["Ouail Kitouni", "Niklas Nolte", "Adina Williams", "Michael Rabbat", "Diane Bouchacourt", "Mark Ibrahim"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "f70e6YYFHF"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d50242bcc72e31e97306e252e69ab08393ff2370.pdf"
published: "2024"
categories: []
keywords: ["Reversal curse", "reliability", "safety", "language models", "interpretability", "learning objectives"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:50+09:00"
---

# The Factorization Curse: Which Tokens You Predict Underlie the Reversal Curse and More

## Abstract
Today's best language models still struggle with "hallucinations", factually incorrect generations, which impede their ability to reliably retrieve information seen during training. The *reversal curse*, where models cannot recall information when probed in a different order than was encountered during training, exemplifies limitations in information retrieval. 
To better understand these limitations, we reframe the reversal curse as a *factorization curse* --- a failure of models to learn the same joint distribution under different factorizations.
We more closely simulate finetuning workflows which train pretrained models on specialized knowledge by introducing
*WikiReversal*, a realistic testbed based on Wikipedia knowledge graphs. Through a series of controlled experiments with increasing levels of realism, including non-reciprocal relations, we find that reliable information retrieval is an inherent failure of the next-token prediction objective used in popular large language models. Moreover, we demonstrate reliable information retrieval cannot be solved with scale, reversed tokens, or even naive bidirectional-attention training. Consequently, various approaches to finetuning on specialized data would necessarily provide mixed results on downstream tasks, unless the model has already seen the right sequence of tokens. 
Across five tasks of varying levels of complexity, our results uncover a promising path forward: factorization-agnostic objectives can significantly mitigate the reversal curse and hint at improved knowledge storage and planning capabilities.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Ouail Kitouni, Niklas Nolte, Adina Williams, Michael Rabbat, Diane Bouchacourt, Mark Ibrahim
- arxiv_id: 
- openreview_id: f70e6YYFHF
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d50242bcc72e31e97306e252e69ab08393ff2370.pdf
- published: 2024
- keywords: Reversal curse, reliability, safety, language models, interpretability, learning objectives
