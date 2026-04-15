---
title: "Born a Transformer -- Always a Transformer? On the Effect of Pretraining on Architectural Abilities"
authors: ["Mayank Jobanputra", "Yana Veitsman", "Yash Sarrof", "Aleksandra Bakalova", "Vera Demberg", "Ellie Pavlick", "Michael Hahn"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Huw15LqglI"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6ad44fb7f8e30a59cb5eed857f25dbc79c22d66f.pdf"
published: "2025"
categories: []
keywords: ["transformers", "length generalization", "empirical analysis", "explainability"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:57+09:00"
---

# Born a Transformer -- Always a Transformer? On the Effect of Pretraining on Architectural Abilities

## Abstract
Transformers have theoretical limitations in modeling certain sequence-to-sequence tasks, yet it remains largely unclear if these limitations play a role in large-scale pretrained LLMs, or whether LLMs might effectively overcome these constraints in practice due to the scale of both the models themselves and their pretraining data. We explore how these architectural constraints manifest after pretraining by studying a family of *retrieval* and *copying* tasks inspired by Liu et al. [2024a]. We use a recently proposed framework for studying length generalization [Huang et al., 2025] to provide guarantees for each of our settings. Empirically, we observe an *induction-versus-anti-induction asymmetry*, where pretrained models are better at retrieving tokens to the right (induction) rather than the left (anti-induction) of a query token. This asymmetry disappears upon targeted fine-tuning if length-generalization is guaranteed by theory. Mechanistic analysis reveals that this asymmetry is connected to the differences in the strength of induction versus anti-induction circuits within pretrained transformers. We validate our findings through practical experiments on real-world tasks demonstrating reliability risks. Our results highlight that pretraining selectively enhances certain transformer capabilities, but does not overcome fundamental length-generalization limits.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Mayank Jobanputra, Yana Veitsman, Yash Sarrof, Aleksandra Bakalova, Vera Demberg, Ellie Pavlick, Michael Hahn
- arxiv_id: 
- openreview_id: Huw15LqglI
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6ad44fb7f8e30a59cb5eed857f25dbc79c22d66f.pdf
- published: 2025
- keywords: transformers, length generalization, empirical analysis, explainability
