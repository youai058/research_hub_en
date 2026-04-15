---
title: "CarbonNovo: Joint Design of Protein Structure and Sequence Using a Unified Energy-based Model"
authors: ["Milong Ren", "Tian Zhu", "Haicang Zhang"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "FSxTEvuFa7"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/effb2ec20822a0131bcb7ca6422394a6d59ce67b.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:40+09:00"
---

# CarbonNovo: Joint Design of Protein Structure and Sequence Using a Unified Energy-based Model

## Abstract
De novo protein design aims to create novel protein structures and sequences unseen in nature. Recent structure-oriented design methods typically employ a two-stage strategy, where structure design and sequence design modules are trained separately, and the backbone structures and sequences are generated sequentially in inference. While diffusion-based generative models like RFdiffusion show great promise in structure design, they face inherent limitations within the two-stage framework. First, the sequence design module risks overfitting, as the accuracy of the generated structures may not align with that of the crystal structures used for training. Second, the sequence design module lacks interaction with the structure design module to further optimize the generated structures. To address these challenges, we propose CarbonNovo, a unified energy-based model for jointly generating protein structure and sequence. Specifically, we leverage a score-based generative model and Markov Random Fields for describing the energy landscape of protein structure and sequence. In CarbonNovo, the structure and sequence design module communicates at each diffusion step, encouraging the generation of more coherent structure-sequence pairs. Moreover, the unified framework allows for incorporating the protein language models as evolutionary constraints for generated proteins. The rigorous evaluation demonstrates that CarbonNovo outperforms two-stage methods across various metrics, including designability, novelty, sequence plausibility, and Rosetta Energy.

## Metadata
- venue: ICML
- year: 2024
- authors: Milong Ren, Tian Zhu, Haicang Zhang
- arxiv_id: 
- openreview_id: FSxTEvuFa7
- anthology_id: 
- pdf_url: https://openreview.net/pdf/effb2ec20822a0131bcb7ca6422394a6d59ce67b.pdf
- published: 2024
