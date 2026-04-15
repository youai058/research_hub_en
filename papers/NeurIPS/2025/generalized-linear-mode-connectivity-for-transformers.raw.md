---
title: "Generalized Linear Mode Connectivity for Transformers"
authors: ["Alexander Theus", "Alessandro Cabodi", "Sotiris Anagnostidis", "Antonio Orvieto", "Sidak Pal Singh", "Valentina Boeva"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "KurYdcCbjv"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/74f91986c42f68d256ffcef1d4a4ee46f7530d3d.pdf"
published: "2025"
categories: []
keywords: ["Neural Network Merging", "Linear Mode Connectivity", "Model Re-basin", "Parameter Space Geometry", "Transformer", "Permutation Invariance", "Model Fusion"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:25+09:00"
---

# Generalized Linear Mode Connectivity for Transformers

## Abstract
Understanding the geometry of neural network loss landscapes is a central question in deep learning, with implications for generalization and optimization. A striking phenomenon is $\textit{linear mode connectivity}$ (LMC), where independently trained models can be connected by low- or zero-barrier paths, despite appearing to lie in separate loss basins. However, this is often obscured by symmetries in parameter space—such as neuron permutations—which make functionally equivalent models appear dissimilar. Prior work has predominantly focused on neuron reordering through permutations, but such approaches are limited in scope and fail to capture the richer symmetries exhibited by modern architectures such as Transformers. In this work, we introduce a unified framework that captures four symmetry classes—permutations, semi-permutations, orthogonal transformations, and general invertible maps—broadening the set of valid reparameterizations and subsuming many previous approaches as special cases. Crucially, this generalization enables, for the first time, the discovery of low- and zero-barrier linear interpolation paths between independently trained Vision Transformers and GPT-2 models. Furthermore, our framework extends beyond pairwise alignment, to multi-model and width-heterogeneous settings, enabling alignment across architectures of different sizes. These results reveal deeper structure in the loss landscape and underscore the importance of symmetry-aware analysis for understanding model space geometry.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Alexander Theus, Alessandro Cabodi, Sotiris Anagnostidis, Antonio Orvieto, Sidak Pal Singh, Valentina Boeva
- arxiv_id: 
- openreview_id: KurYdcCbjv
- anthology_id: 
- pdf_url: https://openreview.net/pdf/74f91986c42f68d256ffcef1d4a4ee46f7530d3d.pdf
- published: 2025
- keywords: Neural Network Merging, Linear Mode Connectivity, Model Re-basin, Parameter Space Geometry, Transformer, Permutation Invariance, Model Fusion
