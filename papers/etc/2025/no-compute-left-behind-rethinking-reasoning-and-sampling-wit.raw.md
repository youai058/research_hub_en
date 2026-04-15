---
title: "No Compute Left Behind: Rethinking Reasoning and Sampling with Masked Diffusion Models"
authors: ["Zachary Horvitz", "Raghav Singhal", "Hao Zou", "Carles Domingo-Enrich", "Zhou Yu", "Rajesh Ranganath", "Kathleen McKeown"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.19990"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.19990v1"
published: "2025-10-22"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:06+09:00"
---

# No Compute Left Behind: Rethinking Reasoning and Sampling with Masked Diffusion Models

## Abstract
Masked diffusion language models (MDLMs) are trained to in-fill positions in randomly masked sequences, in contrast to next-token prediction models. Discussions around MDLMs focus on two benefits: (1) any-order decoding and 2) multi-token decoding. However, we observe that for math and coding tasks, any-order algorithms often underperform or behave similarly to left-to-right sampling, and standard multi-token decoding significantly degrades performance. At inference time, MDLMs compute the conditional distribution of all masked positions. A natural question is: How can we justify this additional compute when left-to-right one-token-at-a-time decoding is on par with any-order decoding algorithms? First, we propose reasoning-as-infilling. By using MDLMs to infill a reasoning template, we can structure outputs and distinguish between reasoning and answer tokens. In turn, this enables measuring answer uncertainty during reasoning, and early exits when the model converges on an answer. Next, given an answer, reasoning-as-infilling enables sampling from the MDLM posterior over reasoning traces conditioned on the answer, providing a new source of high-quality data for post-training. On GSM8k, we observe that fine-tuning LLaDA-8B Base on its posterior reasoning traces provides a performance boost on par with fine-tuning on human-written reasoning traces. Additionally, given an answer, reasoning-as-infilling provides a method for scoring the correctness of the reasoning process at intermediate steps. Second, we propose multi-token entropy decoding (MED), a simple adaptive sampler that minimizes the error incurred by decoding positions in parallel based on the conditional entropies of those positions. MED preserves performance across benchmarks and leads to 2.7x fewer steps. Our work demonstrates that the training and compute used by MDLMs unlock many new inference and post-training methods.

## Metadata
- venue: arXiv
- year: 2025
- authors: Zachary Horvitz, Raghav Singhal, Hao Zou, Carles Domingo-Enrich, Zhou Yu, Rajesh Ranganath, Kathleen McKeown
- arxiv_id: 2510.19990
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.19990v1
- published: 2025-10-22
