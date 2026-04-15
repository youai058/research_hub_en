---
title: "Lookahead Unmasking Elicits Accurate Decoding in Diffusion Language Models"
authors: ["Sanghyun Lee", "Seungryong Kim", "Jongho Park", "Dongmin Park"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.05563"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.05563v1"
published: "2025-11-04"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:22+09:00"
---

# Lookahead Unmasking Elicits Accurate Decoding in Diffusion Language Models

## Abstract
Masked Diffusion Models (MDMs) as language models generate by iteratively unmasking tokens, yet their performance crucially depends on the inference time order of unmasking. Prevailing heuristics, such as confidence based sampling, are myopic: they optimize locally, fail to leverage extra test-time compute, and let early decoding mistakes cascade. We propose Lookahead Unmasking (LookUM), which addresses these concerns by reformulating sampling as path selection over all possible unmasking orders without the need for an external reward model. Our framework couples (i) a path generator that proposes paths by sampling from pools of unmasking sets with (ii) a verifier that computes the uncertainty of the proposed paths and performs importance sampling to subsequently select the final paths. Empirically, erroneous unmasking measurably inflates sequence level uncertainty, and our method exploits this to avoid error-prone trajectories. We validate our framework across six benchmarks, such as mathematics, planning, and coding, and demonstrate consistent performance improvements. LookUM requires only two to three paths to achieve peak performance, demonstrating remarkably efficient path selection. The consistent improvements on both LLaDA and post-trained LLaDA 1.5 are particularly striking: base LLaDA with LookUM rivals the performance of RL-tuned LLaDA 1.5, while LookUM further enhances LLaDA 1.5 itself showing that uncertainty based verification provides orthogonal benefits to reinforcement learning and underscoring the versatility of our framework. Code will be publicly released.

## Metadata
- venue: arXiv
- year: 2025
- authors: Sanghyun Lee, Seungryong Kim, Jongho Park, Dongmin Park
- arxiv_id: 2511.05563
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.05563v1
- published: 2025-11-04
