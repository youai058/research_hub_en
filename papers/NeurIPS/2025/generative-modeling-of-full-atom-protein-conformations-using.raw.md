---
title: "Generative Modeling of Full-Atom Protein Conformations using Latent Diffusion on Graph Embeddings"
authors: ["Aditya Sengar", "Ali Hariri", "Daniel Probst", "PATRICK BARTH", "Pierre Vandergheynst"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "JPjMXgQQxk"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a98baeaa5867971c7e7ebb650d1d64686abf8c93.pdf"
published: "2025"
categories: []
keywords: ["Latent Diffusion", "Graph Neural Networks", "Protein Structure Generation", "All-atom modeling", "Molecular Dynamics"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:33+09:00"
---

# Generative Modeling of Full-Atom Protein Conformations using Latent Diffusion on Graph Embeddings

## Abstract
Generating diverse, all‐atom conformational ensembles of dynamic proteins such as G‐protein‐coupled receptors (GPCRs) is critical for understanding their function, yet most generative models simplify atomic detail or ignore conformational diversity altogether. We present latent diffusion for full protein generation (LD-FPG), a framework that constructs complete all‐atom protein structures, including every side‐chain heavy atom, directly from molecular dynamics (MD) trajectories. LD-FPG employs a Chebyshev graph neural network (ChebNet) to obtain low‐dimensional latent embeddings of protein conformations, which are processed using three pooling strategies: blind, sequential and residue‐based. A diffusion model trained on these latent representations generates new samples that a decoder, optionally regularized by dihedral‐angle losses, maps back to Cartesian coordinates. Using D2R-MD, a $2\mu\text{s}$ MD trajectory (12 000 frames) of the human dopamine D$2$ receptor in a membrane environment, the sequential and residue-based pooling strategies reproduce the reference ensemble with high structural fidelity (all‐atom lDDT \~ $0.7$; $C\alpha$-lDDT \~ $0.8$) and recovers backbone and side‐chain dihedral‐angle distributions with a Jensen–Shannon divergence $<0.03$ compared to the MD data. LD-FPG thereby offers a practical route to system‐specific, all‐atom ensemble generation for large proteins, providing a promising tool for structure‐based therapeutic design on complex, dynamic targets. The D2R-MD dataset and our implementation are freely available to facilitate further research.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Aditya Sengar, Ali Hariri, Daniel Probst, PATRICK BARTH, Pierre Vandergheynst
- arxiv_id: 
- openreview_id: JPjMXgQQxk
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a98baeaa5867971c7e7ebb650d1d64686abf8c93.pdf
- published: 2025
- keywords: Latent Diffusion, Graph Neural Networks, Protein Structure Generation, All-atom modeling, Molecular Dynamics
