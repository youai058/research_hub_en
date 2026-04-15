---
title: "Contour Refinement using Discrete Diffusion in Low Data Regime"
authors: ["Fei Yu Guan", "Ian Keefe", "Sophie Wilkinson", "Daniel D. B. Perrakis", "Steven Waslander"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.05880"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.05880v2"
published: "2026-02-05"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:32+09:00"
---

# Contour Refinement using Discrete Diffusion in Low Data Regime

## Abstract
Boundary detection of irregular and translucent objects is an important problem with applications in medical imaging, environmental monitoring and manufacturing, where many of these applications are plagued with scarce labeled data and low in situ computational resources. While recent image segmentation studies focus on segmentation mask alignment with ground-truth, the task of boundary detection remains understudied, especially in the low data regime. In this work, we present a lightweight discrete diffusion contour refinement pipeline for robust boundary detection in the low data regime. We use a Convolutional Neural Network(CNN) architecture with self-attention layers as the core of our pipeline, and condition on a segmentation mask, iteratively denoising a sparse contour representation. We introduce multiple novel adaptations for improved low-data efficacy and inference efficiency, including using a simplified diffusion process, a customized model architecture, and minimal post processing to produce a dense, isolated contour given a dataset of size <500 training images. Our method outperforms several SOTA baselines on the medical imaging dataset KVASIR, is competitive on HAM10K and our custom wildfire dataset, Smoke, while improving inference framerate by 3.5X.

## Metadata
- venue: arXiv
- year: 2026
- authors: Fei Yu Guan, Ian Keefe, Sophie Wilkinson, Daniel D. B. Perrakis, Steven Waslander
- arxiv_id: 2602.05880
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.05880v2
- published: 2026-02-05
