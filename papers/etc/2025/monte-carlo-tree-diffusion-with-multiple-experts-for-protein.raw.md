---
title: "Monte Carlo Tree Diffusion with Multiple Experts for Protein Design"
authors: ["Xuefeng Liu", "Mingxuan Cao", "Songhao Jiang", "Xiao Luo", "Xiaotian Duan", "Mengdi Wang", "Tobin R. Sosnick", "Jinbo Xu", "Rick Stevens"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.15796"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.15796v2"
published: "2025-09-19"
categories: ["cs.LG", "cs.AI", "q-bio.BM"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:26+09:00"
---

# Monte Carlo Tree Diffusion with Multiple Experts for Protein Design

## Abstract
The goal of protein design is to generate amino acid sequences that fold into functional structures with desired properties. Prior methods combining autoregressive language models with Monte Carlo Tree Search (MCTS) struggle with long-range dependencies and suffer from an impractically large search space. We propose MCTD-ME, Monte Carlo Tree Diffusion with Multiple Experts, which integrates masked diffusion models with tree search to enable multi-token planning and efficient exploration under the guidance of multiple experts. Unlike autoregressive planners, MCTD-ME uses biophysical-fidelity-enhanced diffusion denoising as the rollout engine, jointly revising multiple positions and scaling to large sequence spaces. It further leverages experts of varying capacities to enrich exploration, guided by a pLDDT-based masking schedule that targets low-confidence regions while preserving reliable residues. We propose a novel multi-expert selection rule ( PH-UCT-ME) extends Shannon-entropy-based UCT to expert ensembles with mutual information. MCTD-ME achieves superior performance on the CAMEO and PDB benchmarks, excelling in protein design tasks such as inverse folding, folding, and conditional design challenges like motif scaffolding on lead optimization tasks. Our framework is model-agnostic, plug-and-play, and extensible to denovo protein engineering and beyond.

## Metadata
- venue: arXiv
- year: 2025
- authors: Xuefeng Liu, Mingxuan Cao, Songhao Jiang, Xiao Luo, Xiaotian Duan, Mengdi Wang, Tobin R. Sosnick, Jinbo Xu, Rick Stevens
- arxiv_id: 2509.15796
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.15796v2
- published: 2025-09-19
