---
title: "DGPO: RL-Steered Graph Diffusion for Neural Architecture Generation"
authors: ["Aleksei Liuliakov", "Luca Hermes", "Barbara Hammer"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.19261"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.19261v2"
published: "2026-02-22"
categories: ["cs.LG", "cs.AI", "cs.NE"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:32+09:00"
---

# DGPO: RL-Steered Graph Diffusion for Neural Architecture Generation

## Abstract
Reinforcement learning fine-tuning has proven effective for steering generative diffusion models toward desired properties in image and molecular domains. Graph diffusion models have similarly been applied to combinatorial structure generation, including neural architecture search (NAS). However, neural architectures are directed acyclic graphs (DAGs) where edge direction encodes functional semantics such as data flow-information that existing graph diffusion methods, designed for undirected structures, discard. We propose Directed Graph Policy Optimization (DGPO), which extends reinforcement learning fine-tuning of discrete graph diffusion models to DAGs via topological node ordering and positional encoding. Validated on NAS-Bench-101 and NAS-Bench-201, DGPO matches the benchmark optimum on all three NAS-Bench-201 tasks (91.61%, 73.49%, 46.77%). The central finding is that the model learns transferable structural priors: pretrained on only 7% of the search space, it generates near-oracle architectures after fine-tuning, within 0.32 percentage points of the full-data model and extrapolating 7.3 percentage points beyond its training ceiling. Bidirectional control experiments confirm genuine reward-driven steering, with inverse optimization reaching near random-chance accuracy (9.5%). These results demonstrate that reinforcement learning-steered discrete diffusion, once extended to handle directionality, provides a controllable generative framework for directed combinatorial structures.

## Metadata
- venue: arXiv
- year: 2026
- authors: Aleksei Liuliakov, Luca Hermes, Barbara Hammer
- arxiv_id: 2602.19261
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.19261v2
- published: 2026-02-22
