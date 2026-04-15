---
title: "The Diffusion Duality, Chapter II: $Ψ$-Samplers and Efficient Curriculum"
authors: ["Justin Deschenaux", "Caglar Gulcehre", "Subham Sekhar Sahoo"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.21185"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.21185v1"
published: "2026-02-24"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:13+09:00"
---

# The Diffusion Duality, Chapter II: $Ψ$-Samplers and Efficient Curriculum

## Abstract
Uniform-state discrete diffusion models excel at few-step generation and guidance due to their ability to self-correct, making them preferred over autoregressive or Masked diffusion models in these settings. However, their sampling quality plateaus with ancestral samplers as the number of steps increases. We introduce a family of Predictor-Corrector (PC) samplers for discrete diffusion that generalize prior methods and apply to arbitrary noise processes. When paired with uniform-state diffusion, our samplers outperform ancestral sampling on both language and image modeling, achieving lower generative perplexity at matched unigram entropy on OpenWebText and better FID/IS scores on CIFAR10. Crucially, unlike conventional samplers, our PC methods continue to improve with more sampling steps. Taken together, these findings call into question the assumption that Masked diffusion is the inevitable future of diffusion-based language modeling. Beyond sampling, we develop a memory-efficient curriculum for the Gaussian relaxation training phase, reducing training time by 25% and memory by 33% compared to Duo while maintaining comparable perplexity on OpenWebText and LM1B and strong downstream performance. We release code, checkpoints, and a video-tutorial on: https://s-sahoo.com/duo-ch2

## Metadata
- venue: arXiv
- year: 2026
- authors: Justin Deschenaux, Caglar Gulcehre, Subham Sekhar Sahoo
- arxiv_id: 2602.21185
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.21185v1
- published: 2026-02-24
