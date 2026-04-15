---
title: "Exact Conversion of In-Context Learning to Model Weights in Linearized-Attention Transformers"
authors: ["Brian K Chen", "Tianyang Hu", "Hui Jin", "Hwee Kuan Lee", "Kenji Kawaguchi"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "LVF4P1NNwO"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/25c3e1583fb72822e03302699b39755b701738a4.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:12+09:00"
---

# Exact Conversion of In-Context Learning to Model Weights in Linearized-Attention Transformers

## Abstract
In-Context Learning (ICL) has been a powerful emergent property of large language models that has attracted increasing attention in recent years. In contrast to regular gradient-based learning, ICL is highly interpretable and does not require parameter updates. In this paper, we show that, for linearized transformer networks, ICL can be made explicit and permanent through the inclusion of bias terms. We mathematically demonstrate the equivalence between a model with ICL demonstration prompts and the same model with the additional bias terms. Our algorithm (ICLCA) allows for exact conversion in an inexpensive manner. Existing methods are not exact and require expensive parameter updates. We demonstrate the efficacy of our approach through experiments that show the exact incorporation of ICL tokens into a linear transformer. We further suggest how our method can be adapted to achieve cheap approximate conversion of ICL tokens, even in regular transformer networks that are not linearized. Our experiments on GPT-2 show that, even though the conversion is only approximate, the model still gains valuable context from the included bias terms.

## Metadata
- venue: ICML
- year: 2024
- authors: Brian K Chen, Tianyang Hu, Hui Jin, Hwee Kuan Lee, Kenji Kawaguchi
- arxiv_id: 
- openreview_id: LVF4P1NNwO
- anthology_id: 
- pdf_url: https://openreview.net/pdf/25c3e1583fb72822e03302699b39755b701738a4.pdf
- published: 2024
