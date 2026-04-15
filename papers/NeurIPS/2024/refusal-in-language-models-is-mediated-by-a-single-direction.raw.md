---
title: "Refusal in Language Models Is Mediated by a Single Direction"
authors: ["Andy Arditi", "Oscar Balcells Obeso", "Aaquib Syed", "Daniel Paleka", "Nina Rimsky", "Wes Gurnee", "Neel Nanda"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "pH3XAQME6c"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/8671368b91e68640bc816aa01b23ac6335bb2bf0.pdf"
published: "2024"
categories: []
keywords: ["mechanistic interpretability", "refusal", "jailbreaks", "language models", "steering vectors", "representation engineering"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:41+09:00"
---

# Refusal in Language Models Is Mediated by a Single Direction

## Abstract
Conversational large language models are fine-tuned for both instruction-following and safety, resulting in models that obey benign requests but refuse harmful ones. While this refusal behavior is widespread across chat models, its underlying mechanisms remain poorly understood. In this work, we show that refusal is mediated by a one-dimensional subspace, across 13 popular open-source chat models up to 72B parameters in size. Specifically, for each model, we find a single direction such that erasing this direction from the model's residual stream activations prevents it from refusing harmful instructions, while adding this direction elicits refusal on even harmless instructions. Leveraging this insight, we propose a novel white-box jailbreak method that surgically disables a model's ability to refuse, with minimal effect on other capabilities. This interpretable rank-one weight edit results in an effective jailbreak technique that is simpler and more efficient than fine-tuning. Finally, we mechanistically analyze how adversarial suffixes suppress propagation of the refusal-mediating direction. Our findings underscore the brittleness of current safety fine-tuning methods. More broadly, our work showcases how an understanding of model internals can be leveraged to develop practical methods for controlling model behavior.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Andy Arditi, Oscar Balcells Obeso, Aaquib Syed, Daniel Paleka, Nina Rimsky, Wes Gurnee, Neel Nanda
- arxiv_id: 
- openreview_id: pH3XAQME6c
- anthology_id: 
- pdf_url: https://openreview.net/pdf/8671368b91e68640bc816aa01b23ac6335bb2bf0.pdf
- published: 2024
- keywords: mechanistic interpretability, refusal, jailbreaks, language models, steering vectors, representation engineering
