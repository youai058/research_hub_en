---
title: "EntRGi: Entropy Aware Reward Guidance for Diffusion Language Models"
authors: ["Atula Tejaswi", "Litu Rout", "Constantine Caramanis", "Sanjay Shakkottai", "Sujay Sanghavi"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.05000"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.05000v1"
published: "2026-02-04"
categories: ["cs.LG", "cs.AI", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:05+09:00"
---

# EntRGi: Entropy Aware Reward Guidance for Diffusion Language Models

## Abstract
Reward guidance has been applied to great success in the test-time adaptation of continuous diffusion models; it updates each denoising step using the gradients from a downstream reward model. We study reward guidance for discrete diffusion language models, where one cannot differentiate through the natural outputs of the model because they are discrete tokens. Existing approaches either replace these discrete tokens with continuous relaxations, or employ techniques like the straight-through estimator. In this work, we show the downsides of both these methods. The former degrades gradient feedback because the reward model has never been trained with continuous inputs. The latter involves incorrect optimization because the gradient evaluated at discrete tokens is used to update continuous logits. Our key innovation is to go beyond this tradeoff by introducing a novel mechanism called EntRGi: Entropy aware Reward Guidance that dynamically regulates the gradients from the reward model. By modulating the continuous relaxation using the model's confidence, our approach substantially improves reward guidance while providing reliable inputs to the reward model. We empirically validate our approach on a 7B-parameter diffusion language model across 3 diverse reward models and 3 multi-skill benchmarks, showing consistent improvements over state-of-the-art methods.

## Metadata
- venue: arXiv
- year: 2026
- authors: Atula Tejaswi, Litu Rout, Constantine Caramanis, Sanjay Shakkottai, Sujay Sanghavi
- arxiv_id: 2602.05000
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.05000v1
- published: 2026-02-04
