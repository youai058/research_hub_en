---
title: "Lingshu-Cell: A generative cellular world model for transcriptome modeling toward virtual cells"
authors: ["Han Zhang", "Guo-Hua Yuan", "Chaohao Yuan", "Tingyang Xu", "Tian Bian", "Hong Cheng", "Wenbing Huang", "Deli Zhao", "Yu Rong"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.25240"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.25240v1"
published: "2026-03-26"
categories: ["q-bio.QM", "cs.AI", "q-bio.GN"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:24+09:00"
---

# Lingshu-Cell: A generative cellular world model for transcriptome modeling toward virtual cells

## Abstract
Modeling cellular states and predicting their responses to perturbations are central challenges in computational biology and the development of virtual cells. Existing foundation models for single-cell transcriptomics provide powerful static representations, but they do not explicitly model the distribution of cellular states for generative simulation. Here, we introduce Lingshu-Cell, a masked discrete diffusion model that learns transcriptomic state distributions and supports conditional simulation under perturbation. By operating directly in a discrete token space that is compatible with the sparse, non-sequential nature of single-cell transcriptomic data, Lingshu-Cell captures complex transcriptome-wide expression dependencies across approximately 18,000 genes without relying on prior gene selection, such as filtering by high variability or ranking by expression level. Across diverse tissues and species, Lingshu-Cell accurately reproduces transcriptomic distributions, marker-gene expression patterns and cell-subtype proportions, demonstrating its ability to capture complex cellular heterogeneity. Moreover, by jointly embedding cell type or donor identity with perturbation, Lingshu-Cell can predict whole-transcriptome expression changes for novel combinations of identity and perturbation. It achieves leading performance on the Virtual Cell Challenge H1 genetic perturbation benchmark and in predicting cytokine-induced responses in human PBMCs. Together, these results establish Lingshu-Cell as a flexible cellular world model for in silico simulation of cell states and perturbation responses, laying the foundation for a new paradigm in biological discovery and perturbation screening.

## Metadata
- venue: arXiv
- year: 2026
- authors: Han Zhang, Guo-Hua Yuan, Chaohao Yuan, Tingyang Xu, Tian Bian, Hong Cheng, Wenbing Huang, Deli Zhao, Yu Rong
- arxiv_id: 2603.25240
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.25240v1
- published: 2026-03-26
