---
title: "From Broad Exploration to Stable Synthesis: Entropy-Guided Optimization for Autoregressive Image Generation"
authors: ["Han Song", "Yucheng Zhou", "Jianbing Shen", "Yu Cheng"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "NCLjpR2MDq"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9dafdde03fc617fb6691c8bd666b3ffed66b77a5.pdf"
published: "2026"
categories: []
keywords: ["Language Models", "Autoregressive Image Generation", "Chain-of-Thought"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:17+09:00"
---

# From Broad Exploration to Stable Synthesis: Entropy-Guided Optimization for Autoregressive Image Generation

## Abstract
Combining Chain-of-Thought (CoT) with Reinforcement Learning (RL) improves text-to-image (T2I) generation, yet the underlying interaction between CoT's exploration and RL's optimization remains unclear. We present a systematic entropy-based analysis that yields three key insights: (1) CoT expands the generative exploration space, while RL contracts it toward high-reward regions; (2) final reward is strongly negatively correlated with both the mean and variance of image-token entropy, highlighting the need to reduce uncertainty and instability; and (3) the entropy of the textual CoT directly governs downstream image quality, with lower-entropy CoTs leading to better generations. Motivated by these findings, we propose Entropy-Guided Group Relative Policy Optimization (EG-GRPO), a fine-tuning strategy that reallocates optimization budget by uncertainty: low-entropy tokens are excluded from reward-driven updates to preserve stability, while high-entropy tokens receive an entropy bonus that encourages structured exploration without collapse. Experiments on standard T2I benchmarks demonstrate that EG-GRPO achieves state-of-the-art performance.

## Metadata
- venue: ICLR
- year: 2026
- authors: Han Song, Yucheng Zhou, Jianbing Shen, Yu Cheng
- arxiv_id: 
- openreview_id: NCLjpR2MDq
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9dafdde03fc617fb6691c8bd666b3ffed66b77a5.pdf
- published: 2026
- keywords: Language Models, Autoregressive Image Generation, Chain-of-Thought
