---
title: "Set Block Decoding is a Language Model Inference Accelerator"
authors: ["Itai Gat", "Heli Ben-Hamu", "Marton Havasi", "Daniel Haziza", "Jeremy Reizenstein", "Gabriel Synnaeve", "David Lopez-Paz", "Brian Karrer", "Yaron Lipman"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.04185"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.04185v1"
published: "2025-09-04"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:44+09:00"
---

# Set Block Decoding is a Language Model Inference Accelerator

## Abstract
Autoregressive next token prediction language models offer powerful capabilities but face significant challenges in practical deployment due to the high computational and memory costs of inference, particularly during the decoding stage. We introduce Set Block Decoding (SBD), a simple and flexible paradigm that accelerates generation by integrating standard next token prediction (NTP) and masked token prediction (MATP) within a single architecture. SBD allows the model to sample multiple, not necessarily consecutive, future tokens in parallel, a key distinction from previous acceleration methods. This flexibility allows the use of advanced solvers from the discrete diffusion literature, offering significant speedups without sacrificing accuracy. SBD requires no architectural changes or extra training hyperparameters, maintains compatibility with exact KV-caching, and can be implemented by fine-tuning existing next token prediction models. By fine-tuning Llama-3.1 8B and Qwen-3 8B, we demonstrate that SBD enables a 3-5x reduction in the number of forward passes required for generation while achieving same performance as equivalent NTP training.

## Metadata
- venue: arXiv
- year: 2025
- authors: Itai Gat, Heli Ben-Hamu, Marton Havasi, Daniel Haziza, Jeremy Reizenstein, Gabriel Synnaeve, David Lopez-Paz, Brian Karrer, Yaron Lipman
- arxiv_id: 2509.04185
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.04185v1
- published: 2025-09-04
