---
title: "Exploring Diverse Generation Paths via Inference-time Stiefel Activation Steering"
authors: ["Dongxuan Zhu", "Ly Tran Ho Khanh", "Andy Yat-Ming Cheung", "Man-Chung Yue", "Viet Anh Nguyen"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "v0QOVSVPtq"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9ce441ef7acf7686fd62a348c4506a8d92cd9d9d.pdf"
published: "2026"
categories: []
keywords: ["activation steering", "generation diversity", "manifold opimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:22+09:00"
---

# Exploring Diverse Generation Paths via Inference-time Stiefel Activation Steering

## Abstract
Language models often default to a narrow set of high-probability outputs, leaving their generation paths homogeneous and prone to mode collapse. Sampling-based strategies inject randomness but still struggle to guarantee diversity across multiple concurrent generation runs. We address this limitation by introducing STARS (**ST**iefel-based **A**ctivation Steering for Diverse **R**ea**S**oning), a training-free, inference-time intervention method that transforms activation steering into an exploration engine. At each token, STARS collects the hidden activations of concurrent generation runs and optimizes multiple additive steering directions jointly on the Stiefel manifold. STARS maximizes the geometric volume of the steered activations, while the Stiefel manifold induces orthogonality of the steering interventions. This formulation explicitly promotes divergent activation vectors of concurrent generation runs, and implicitly promotes divergent generation trajectories. This manifold optimization formulation can be solved using a Riemannian gradient descent algorithm with convergence guarantees, but this algorithm is too time-consuming for real-time inference. To guarantee low latency, we further design a lightweight one-step update with an aggressive, closed-form stepsize. For test case generation and scientific discovery benchmarks, STARS consistently outperforms standard sampling methods, achieving greater diversity without sacrificing qualitative performance.

## Metadata
- venue: ICLR
- year: 2026
- authors: Dongxuan Zhu, Ly Tran Ho Khanh, Andy Yat-Ming Cheung, Man-Chung Yue, Viet Anh Nguyen
- arxiv_id: 
- openreview_id: v0QOVSVPtq
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9ce441ef7acf7686fd62a348c4506a8d92cd9d9d.pdf
- published: 2026
- keywords: activation steering, generation diversity, manifold opimization
