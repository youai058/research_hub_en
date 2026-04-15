---
title: "Neutral residues: revisiting adapters for model extension"
authors: ["Franck SIGNE TALLA", "Edouard Grave", "Herve Jegou"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "gmdElnwBxt"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/464fe19b19f50de395b04c6fda623bcaea5c8eee.pdf"
published: "2025"
categories: []
keywords: ["LLM", "Adapters", "Domain Adaptation", "Catastrophic Forgetting"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:09+09:00"
---

# Neutral residues: revisiting adapters for model extension

## Abstract
We address the problem of extending a pre-trained large language model to a new domain that was not seen during training. Standard techniques, such as fine-tuning or low-rank adaptation (LoRA) are successful at domain adaptation, but do not formally add capacity to the model. This often leads to a trade-off, between performing well on the new domain vs. degrading performance on the original domain.
Here, we propose to revisit and improve adapters to extend LLMs. Our paper analyzes this extension problem from three angles: data, architecture and training procedure, which are advantageously considered jointly. The resulting method, called neutral residues, modifies adapters in a way that leads to each new residual block to output near-zeros on the original domain. This solution leads to strong results when adapting a state-of-the-art model originally trained on English to a new language. Neutral residues significantly outperforms competing approaches such as fine-tuning, LoRA or vanilla adapters in terms of the trade-off between learning the new language and not forgetting English.

## Metadata
- venue: ICML
- year: 2025
- authors: Franck SIGNE TALLA, Edouard Grave, Herve Jegou
- arxiv_id: 
- openreview_id: gmdElnwBxt
- anthology_id: 
- pdf_url: https://openreview.net/pdf/464fe19b19f50de395b04c6fda623bcaea5c8eee.pdf
- published: 2025
- keywords: LLM, Adapters, Domain Adaptation, Catastrophic Forgetting
