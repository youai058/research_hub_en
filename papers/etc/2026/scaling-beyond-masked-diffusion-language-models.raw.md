---
title: "Scaling Beyond Masked Diffusion Language Models"
authors: ["Subham Sekhar Sahoo", "Jean-Marie Lemercier", "Zhihan Yang", "Justin Deschenaux", "Jingyu Liu", "John Thickstun", "Ante Jukic"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.15014"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.15014v1"
published: "2026-02-16"
categories: ["cs.LG", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:02+09:00"
---

# Scaling Beyond Masked Diffusion Language Models

## Abstract
Diffusion language models are a promising alternative to autoregressive models due to their potential for faster generation. Among discrete diffusion approaches, Masked diffusion currently dominates, largely driven by strong perplexity on language modeling benchmarks. In this work, we present the first scaling law study of uniform-state and interpolating discrete diffusion methods. We also show that Masked diffusion models can be made approximately 12% more FLOPs-efficient when trained with a simple cross-entropy objective. We find that perplexity is informative within a diffusion family but can be misleading across families, where models with worse likelihood scaling may be preferable due to faster and more practical sampling, as reflected by the speed-quality Pareto frontier. These results challenge the view that Masked diffusion is categorically the future of diffusion language modeling and that perplexity alone suffices for cross-algorithm comparison. Scaling all methods to 1.7B parameters, we show that uniform-state diffusion remains competitive on likelihood-based benchmarks and outperforms autoregressive and Masked diffusion models on GSM8K, despite worse validation perplexity. We provide the code, model checkpoints, and video tutorials on the project page: http://s-sahoo.github.io/scaling-dllms

## Metadata
- venue: arXiv
- year: 2026
- authors: Subham Sekhar Sahoo, Jean-Marie Lemercier, Zhihan Yang, Justin Deschenaux, Jingyu Liu, John Thickstun, Ante Jukic
- arxiv_id: 2602.15014
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.15014v1
- published: 2026-02-16
