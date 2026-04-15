---
title: "LS-Merge: Merging Language Models in Latent Space"
authors: ["Bedionita Soro", "Aoxuan Silvia Zhang", "Bruno Andreis", "Jaehyeong Jo", "Song Chong", "Sung Ju Hwang"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "VSDV0SWwOC"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b60bfa1260889795bc72736799c10ba011815c07.pdf"
published: "2026"
categories: []
keywords: ["LS-Merge", "LLM merging", "latent space", "weight space learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:27+09:00"
---

# LS-Merge: Merging Language Models in Latent Space

## Abstract
Model merging in weight space is an efficient way to reuse pretrained models, but existing methods typically assume matching architectures or sizes, making heterogeneous merges brittle or infeasible. We address this limitation by encoding model weights into a smooth latent space, enabling cross-architecture operations, and performing the merge in the latent space before decoding back to weights. This approach faces two major challenges. First, LLMs contain billions of parameters, which makes latent encoding computationally demanding. Second, using high compression ratios often hinders the encoder’s ability to generalize to unseen weights. We tackle these issues with a transformer-based variational autoencoder (VAE) trained in a two-stage compression curriculum with structured layer-aware chunking: the model first learns a high-capacity latent representation and then distills to a compact code, improving both stability and out-of-distribution generalization. To align heterogeneous models, we introduce a dimensionality-matching projection that allows interpolation between models of different sizes. Empirically, latent-space interpolation is consistently more robust than direct weight-space averaging and yields stronger downstream performance when merging models of different sizes. Together, these components provide a scalable, architecture-agnostic recipe for model merging.

## Metadata
- venue: ICLR
- year: 2026
- authors: Bedionita Soro, Aoxuan Silvia Zhang, Bruno Andreis, Jaehyeong Jo, Song Chong, Sung Ju Hwang
- arxiv_id: 
- openreview_id: VSDV0SWwOC
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b60bfa1260889795bc72736799c10ba011815c07.pdf
- published: 2026
- keywords: LS-Merge, LLM merging, latent space, weight space learning
