---
title: "How Smooth Is Attention?"
authors: ["Valérie Castin", "Pierre Ablin", "Gabriel Peyré"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "aP0H8A1ywk"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/454a11e1967292e5586589d2bb9de114ec52ad95.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:49+09:00"
---

# How Smooth Is Attention?

## Abstract
Self-attention and masked self-attention are at the heart of Transformers' outstanding success. Still, our mathematical understanding of attention, in particular of its Lipschitz properties — which are key when it comes to analyzing robustness and expressive power — is incomplete. We provide a detailed study of the Lipschitz constant of self-attention in several practical scenarios, discussing the impact of the sequence length $n$ and layer normalization on the local Lipschitz constant of both unmasked and masked self-attention. In particular, we show that for inputs of length $n$ in any compact set, the Lipschitz constant of self-attention is bounded by $\sqrt{n}$ up to a constant factor and that this bound is tight for reasonable sequence lengths. When the sequence length $n$ is too large for the previous bound to be tight, which we refer to as the mean-field regime, we provide an upper bound and a matching lower bound which are independent of $n$. Our mean-field framework for masked self-attention is novel and of independent interest. Our experiments on pretrained and randomly initialized BERT and GPT-2 support our theoretical findings.

## Metadata
- venue: ICML
- year: 2024
- authors: Valérie Castin, Pierre Ablin, Gabriel Peyré
- arxiv_id: 
- openreview_id: aP0H8A1ywk
- anthology_id: 
- pdf_url: https://openreview.net/pdf/454a11e1967292e5586589d2bb9de114ec52ad95.pdf
- published: 2024
