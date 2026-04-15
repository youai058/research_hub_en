---
title: "Stopping Computation for Converged Tokens in Masked Diffusion-LM Decoding"
authors: ["Daisuke Oba", "Danushka Bollegala", "Masahiro Kaneko", "Naoaki Okazaki"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: "2602.06412"
openreview_id: "PzhNnMepgl"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7a62ee0acb5491a26d9640ce498d7ee7927c7e45.pdf"
published: "2026"
categories: []
keywords: ["diffusion language models", "compute efficient sampling", "skipping compute", "adaptive attention"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:18+09:00"
---

# Stopping Computation for Converged Tokens in Masked Diffusion-LM Decoding

## Abstract
Masked Diffusion Language Models generate sequences via iterative sampling that progressively unmasks tokens. However, they still recompute the attention and feed-forward blocks for every token position at every step---even when many unmasked tokens are essentially fixed, resulting in substantial waste in compute.
We propose **SureLock**: when the posterior at an unmasked position has stabilized across steps (our *sure* condition), we *lock* that position---thereafter skipping its query projection and feed-forward sublayers---while caching its attention keys and values so other positions can continue to attend to it.
This reduces the dominant per-iteration computational cost from $O(N^2d)$ to $O(MNd)$ where $N$ is the sequence length, $M$ is the number of unlocked token positions, and $d$ is the model dimension.
In practice, $M$ decreases as the iteration progresses, yielding substantial savings.
On LLaDA-8B, SureLock reduces algorithmic FLOPs by 30--50\% relative to the same sampler without locking, 
while maintaining comparable generation quality.
We also provide a theoretical analysis to justify the design rationale of SureLock:  monitoring only the local KL at the lock step suffices to bound the deviation in final token probabilities. Our project page is available at https://daioba.github.io/surelock.

## Metadata
- venue: ICLR
- year: 2026
- authors: Daisuke Oba, Danushka Bollegala, Masahiro Kaneko, Naoaki Okazaki
- arxiv_id: 
- openreview_id: PzhNnMepgl
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7a62ee0acb5491a26d9640ce498d7ee7927c7e45.pdf
- published: 2026
- keywords: diffusion language models, compute efficient sampling, skipping compute, adaptive attention
