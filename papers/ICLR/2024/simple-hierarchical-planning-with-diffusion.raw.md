---
title: "Simple Hierarchical Planning with Diffusion"
authors: ["Chang Chen", "Fei Deng", "Kenji Kawaguchi", "Caglar Gulcehre", "Sungjin Ahn"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "kXHEBK9uAY"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/cd376c92489e21ca9086764bc0ac0d95877b8ad5.pdf"
published: "2024"
categories: []
keywords: ["Hierarchical Offline RL", "Hierarchical planning", "Hierarchical Reinforcement Learning", "Diffusion-Based Planning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:19+09:00"
---

# Simple Hierarchical Planning with Diffusion

## Abstract
Diffusion-based generative methods have proven effective in modeling trajectories with offline datasets. However, they often face computational challenges and can falter in generalization, especially in capturing temporal abstractions for long-horizon tasks. To overcome this, we introduce the Hierarchical Diffuser, a simple, fast, yet effective planning method combining the advantages of hierarchical and diffusion-based planning. Our model adopts a “jumpy” planning strategy at the high level, which allows it to have a larger receptive field but at a lower computational cost—a crucial factor for diffusion-based planning methods, as we have empirically verified. Additionally, the jumpy sub-goals guide our low-level planner, facilitating a fine-tuning stage and further improving our approach’s effectiveness. We conducted empirical evaluations on standard offline reinforcement learning benchmarks, demonstrating our method’s superior performance and efficiency in terms of training and planning speed compared to the non-hierarchical Diffuser as well as other hierarchical planning methods. Moreover, we explore our model’s generalization capability, particularly on how our method improves generalization capabilities on compositional out-of-distribution tasks.

## Metadata
- venue: ICLR
- year: 2024
- authors: Chang Chen, Fei Deng, Kenji Kawaguchi, Caglar Gulcehre, Sungjin Ahn
- arxiv_id: 
- openreview_id: kXHEBK9uAY
- anthology_id: 
- pdf_url: https://openreview.net/pdf/cd376c92489e21ca9086764bc0ac0d95877b8ad5.pdf
- published: 2024
- keywords: Hierarchical Offline RL, Hierarchical planning, Hierarchical Reinforcement Learning, Diffusion-Based Planning
