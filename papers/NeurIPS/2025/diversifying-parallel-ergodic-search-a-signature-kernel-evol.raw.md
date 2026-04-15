---
title: "Diversifying Parallel Ergodic Search: A Signature Kernel Evolution Strategy"
authors: ["Sreevardhan Sirigiri", "Christian Hughes", "Ian Abraham", "Fabio Ramos"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "3XuUnUEI7e"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/688b6f9425ccfb2dfe04789b9220f88eed09c698.pdf"
published: "2025"
categories: []
keywords: ["robotics exploration", "trajectory optimization", "ergodic search", "signature transform"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:50+09:00"
---

# Diversifying Parallel Ergodic Search: A Signature Kernel Evolution Strategy

## Abstract
Effective robotic exploration in continuous domains requires planning trajectories that maximize coverage over a predefined region. A recent development, Stein Variational Ergodic Search (SVES), proposed parallel ergodic exploration (a key approach within the field of robotic exploration), via Stein variational inference that computes a set of candidate trajectories approximating the posterior distribution over the solution space trajectories. While this approach leverages GPU parallelism well, the trajectories in the set might not be distinct enough, leading to a suboptimal set. In this paper, we propose two key methods to diversify the solution set of this approach.
First, we leverage the signature kernel within the SVES framework, introducing a pathwise, sequence-sensitive interaction that preserves the Markovian structure of the trajectories and naturally spreads paths across distinct regions of the search space. Second, we propose a derivative-free evolution-strategy interpretation of SVES that exploits batched, GPU-friendly fitness evaluations and can be paired with approximate gradients whenever analytic gradients of the kernel are unavailable or computationally intractable. The resulting method both retains SVES’s advantages while diversifying the solution set and extending its reach to black-box objectives. Across planar forest search, 3D quadrotor coverage, and model-predictive control benchmarks, our approach consistently reduces ergodic cost and produces markedly richer trajectory sets than SVES without significant extra tuning effort.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Sreevardhan Sirigiri, Christian Hughes, Ian Abraham, Fabio Ramos
- arxiv_id: 
- openreview_id: 3XuUnUEI7e
- anthology_id: 
- pdf_url: https://openreview.net/pdf/688b6f9425ccfb2dfe04789b9220f88eed09c698.pdf
- published: 2025
- keywords: robotics exploration, trajectory optimization, ergodic search, signature transform
