---
title: "Closed-Loop Transformers: Autoregressive Modeling as Iterative Latent Equilibrium"
authors: ["Akbar Anbar Jafari", "Gholamreza Anbarjafari"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.21882"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.21882v1"
published: "2025-11-26"
categories: ["cs.LG", "cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:03+09:00"
---

# Closed-Loop Transformers: Autoregressive Modeling as Iterative Latent Equilibrium

## Abstract
Contemporary autoregressive transformers operate in open loop: each hidden state is computed in a single forward pass and never revised, causing errors to propagate uncorrected through the sequence. We identify this open-loop bottleneck as a fundamental architectural limitation underlying well-documented failures in long-range reasoning, factual consistency, and multi-step planning. To address this limitation, we introduce the closed-loop prediction principle, which requires that models iteratively refine latent representations until reaching a self-consistent equilibrium before committing to each token. We instantiate this principle as Equilibrium Transformers (EqT), which augment standard transformer layers with an Equilibrium Refinement Module that minimizes a learned energy function via gradient descent in latent space. The energy function enforces bidirectional prediction consistency, episodic memory coherence, and output confidence, all computed without external supervision. Theoretically, we prove that EqT performs approximate MAP inference in a latent energy-based model, establish linear convergence guarantees, and show that refinement improves predictions precisely on hard instances where one-shot inference is suboptimal. The framework unifies deep equilibrium models, diffusion language models, and test-time training as special cases. Preliminary experiments on the binary parity task demonstrate +3.28% average improvement on challenging sequences, with gains reaching +8.07% where standard transformers approach random performance, validating that the benefit of deliberation scales with task difficulty. Just as attention mechanisms resolved the sequential bottleneck of recurrent networks, we propose that closed-loop equilibrium may resolve the commitment bottleneck of open-loop autoregression, representing a foundational step toward language models.

## Metadata
- venue: arXiv
- year: 2025
- authors: Akbar Anbar Jafari, Gholamreza Anbarjafari
- arxiv_id: 2511.21882
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.21882v1
- published: 2025-11-26
