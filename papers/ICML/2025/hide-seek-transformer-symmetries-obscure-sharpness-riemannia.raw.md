---
title: "Hide & Seek: Transformer Symmetries Obscure Sharpness & Riemannian Geometry Finds It"
authors: ["Marvin F. da Silva", "Felix Dangel", "Sageev Oore"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5QAKPBVdFH"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c37e40aed10aa72aed4e76053cecd9e389eeb710.pdf"
published: "2025"
categories: []
keywords: ["generalization", "symmetry", "sharpness", "flatness", "riemannian geometry", "loss landscape"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:13+09:00"
---

# Hide & Seek: Transformer Symmetries Obscure Sharpness & Riemannian Geometry Finds It

## Abstract
The concept of sharpness has been successfully applied to traditional architectures like MLPs and CNNs to predict their generalization. For transformers, however, recent work reported weak correlation between flatness and generalization. We argue that existing sharpness measures fail for transformers, because they have much richer symmetries in their attention mechanism that induce directions in parameter space along which the network or its loss remain identical. We posit that sharpness must account fully for these symmetries, and thus we redefine it on a quotient manifold that results from quotienting out the transformer symmetries, thereby removing their ambiguities. Leveraging tools from Riemannian geometry, we propose a fully general notion of sharpness, in terms of a geodesic ball on the symmetry-corrected quotient manifold. In practice, we need to resort to approximating the geodesics. Doing so up to first order yields existing adaptive sharpness measures, and we demonstrate that including higher-order terms is crucial to recover correlation with generalization. We present results on diagonal networks with synthetic data, and show that our geodesic sharpness reveals strong correlation for real-world transformers on both text and image classification tasks.

## Metadata
- venue: ICML
- year: 2025
- authors: Marvin F. da Silva, Felix Dangel, Sageev Oore
- arxiv_id: 
- openreview_id: 5QAKPBVdFH
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c37e40aed10aa72aed4e76053cecd9e389eeb710.pdf
- published: 2025
- keywords: generalization, symmetry, sharpness, flatness, riemannian geometry, loss landscape
