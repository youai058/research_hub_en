---
title: "Autoregressive vs. Masked Diffusion Language Models: A Controlled Comparison"
authors: ["Caio Vicentino"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.22075"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.22075v1"
published: "2026-03-23"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:09+09:00"
---

# Autoregressive vs. Masked Diffusion Language Models: A Controlled Comparison

## Abstract
We present a controlled empirical comparison between autoregressive (AR) and masked diffusion (MDLM) language models. Both models are trained on identical data (50M tokens from TinyStories), identical compute budget (20,000 steps, batch size 32, sequence length 512), and identical hardware (NVIDIA H100 80GB), isolating the generation paradigm as the sole variable. We report three findings. First, both paradigms achieve comparable training throughput (~50K tokens/second), with MDLM requiring only 4.7% more wall-clock time. Second, AR converges faster and begins overfitting by step 14,000, while MDLM converges more slowly and is still improving at step 20,000, suggesting different compute-optimal training regimes. Third, quantitative diversity analysis over 1,000 generated samples reveals a structural diversity-fluency trade-off: AR produces fluent but repetitive outputs (99.8% begin with the same word), while MDLM generates more diverse narratives (93.4% unique 5-word openings, higher Distinct-n, lower Self-BLEU), at the cost of occasional grammatical inconsistencies. All code, trained checkpoints, and data pipelines are released for reproducibility.

## Metadata
- venue: arXiv
- year: 2026
- authors: Caio Vicentino
- arxiv_id: 2603.22075
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.22075v1
- published: 2026-03-23
