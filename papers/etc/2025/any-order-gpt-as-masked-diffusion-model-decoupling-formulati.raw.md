---
title: "Any-Order GPT as Masked Diffusion Model: Decoupling Formulation and Architecture"
authors: ["Shuchen Xue", "Tianyu Xie", "Tianyang Hu", "Zijin Feng", "Jiacheng Sun", "Kenji Kawaguchi", "Zhenguo Li", "Zhi-Ming Ma"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2506.19935"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2506.19935v1"
published: "2025-06-24"
categories: ["cs.LG", "cs.CV", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:29+09:00"
---

# Any-Order GPT as Masked Diffusion Model: Decoupling Formulation and Architecture

## Abstract
Large language models (LLMs) predominantly use autoregressive (AR) approaches, but masked diffusion models (MDMs) are emerging as viable alternatives. A key challenge in comparing AR and MDM paradigms is their typical architectural difference: AR models are often decoder-only, while MDMs have largely been encoder-only. This practice of changing both the modeling paradigm and architecture simultaneously makes direct comparisons unfair, as it's hard to distinguish whether observed differences stem from the paradigm itself or the architectural shift. This research evaluates MDMs within a decoder-only framework to: (1) equitably compare MDM (as Any-Order AR, or AO-AR) and standard AR paradigms. Our investigation suggests that the standard AO-AR objective, which averages over all token permutations, may benefit from refinement, as many permutations appear less informative compared to the language's inherent left-to-right structure. (2) Investigate architectural influences (decoder-only vs. encoder-only) within MDMs. We demonstrate that while encoder-only MDMs model a simpler conditional probability space, decoder-only MDMs can achieve dramatic generation speedups ($\sim25\times$) and comparable perplexity with temperature annealing despite modeling a vastly larger space, highlighting key trade-offs. This work thus decouples core paradigm differences from architectural influences, offering insights for future model design. Code is available at https://github.com/scxue/AO-GPT-MDM.

## Metadata
- venue: arXiv
- year: 2025
- authors: Shuchen Xue, Tianyu Xie, Tianyang Hu, Zijin Feng, Jiacheng Sun, Kenji Kawaguchi, Zhenguo Li, Zhi-Ming Ma
- arxiv_id: 2506.19935
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2506.19935v1
- published: 2025-06-24
