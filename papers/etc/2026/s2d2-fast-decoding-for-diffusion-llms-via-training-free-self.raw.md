---
title: "S2D2: Fast Decoding for Diffusion LLMs via Training-Free Self-Speculation"
authors: ["Ligong Han", "Hao Wang", "Han Gao", "Kai Xu", "Akash Srivastava"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.25702"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.25702v1"
published: "2026-03-26"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:54+09:00"
---

# S2D2: Fast Decoding for Diffusion LLMs via Training-Free Self-Speculation

## Abstract
Block-diffusion language models offer a promising path toward faster-than-autoregressive generation by combining block-wise autoregressive decoding with within-block parallel denoising. However, in the few-step regime needed for practical acceleration, standard confidence-thresholded decoding is often brittle: aggressive thresholds hurt quality, while conservative thresholds require unnecessary denoising steps. Existing approaches that address this issue either require additional training or incur extra test-time compute. We present S2D2, a training-free self-speculative decoding framework for block-diffusion language models. Our key observation is that a block-diffusion model becomes autoregressive when the block size is reduced to one, allowing the same pretrained model to act as both drafter and verifier. S2D2 inserts a speculative verification step into standard block-diffusion decoding and uses lightweight routing policies to decide when verification is worth its cost. This yields a hybrid decoding trajectory in which diffusion proposes tokens in parallel, while the autoregressive mode acts as a local sequence-level critic. Across three mainstream block-diffusion families, S2D2 consistently improves the accuracy-speed tradeoff over strong confidence-thresholding baselines. On SDAR, we observe up to $4.7\times$ speedup over autoregressive decoding, and up to $1.57\times$ over a tuned dynamic decoding baseline while improving accuracy by up to $4.5$ points. On LLaDA2.1-Mini, S2D2 remains complementary to built-in self-correction, including a conservative setting where it is $4.4\times$ faster than the static baseline with slightly higher accuracy.

## Metadata
- venue: arXiv
- year: 2026
- authors: Ligong Han, Hao Wang, Han Gao, Kai Xu, Akash Srivastava
- arxiv_id: 2603.25702
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.25702v1
- published: 2026-03-26
