---
title: "Test-Time Scaling with Diffusion Language Models via Reward-Guided Stitching"
authors: ["Roy Miles", "Aysim Toker", "Andreea-Maria Oncescu", "Songcen Xu", "Jiankang Deng", "Ismail Elezi"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.22871"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.22871v1"
published: "2026-02-26"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:02+09:00"
---

# Test-Time Scaling with Diffusion Language Models via Reward-Guided Stitching

## Abstract
Reasoning with large language models often benefits from generating multiple chains-of-thought, but existing aggregation strategies are typically trajectory-level (e.g., selecting the best trace or voting on the final answer), discarding useful intermediate work from partial or "nearly correct" attempts. We propose Stitching Noisy Diffusion Thoughts, a self-consistency framework that turns cheap diffusion-sampled reasoning into a reusable pool of step-level candidates. Given a problem, we (i) sample many diverse, low-cost reasoning trajectories using a masked diffusion language model, (ii) score every intermediate step with an off-the-shelf process reward model (PRM), and (iii) stitch these highest-quality steps across trajectories into a composite rationale. This rationale then conditions an autoregressive (AR) model (solver) to recompute only the final answer. This modular pipeline separates exploration (diffusion) from evaluation and solution synthesis, avoiding monolithic unified hybrids while preserving broad search. Across math reasoning benchmarks, we find that step-level recombination is most beneficial on harder problems, and ablations highlight the importance of the final AR solver in converting stitched but imperfect rationales into accurate answers. Using low-confidence diffusion sampling with parallel, independent rollouts, our training-free framework improves average accuracy by up to 23.8% across six math and coding tasks. At the same time, it achieves up to a 1.8x latency reduction relative to both traditional diffusion models (e.g., Dream, LLaDA) and unified architectures (e.g., TiDAR). Code is available at https://github.com/roymiles/diffusion-stitching.

## Metadata
- venue: arXiv
- year: 2026
- authors: Roy Miles, Aysim Toker, Andreea-Maria Oncescu, Songcen Xu, Jiankang Deng, Ismail Elezi
- arxiv_id: 2602.22871
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.22871v1
- published: 2026-02-26
