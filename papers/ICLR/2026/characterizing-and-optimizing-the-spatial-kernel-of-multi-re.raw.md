---
title: "Characterizing and Optimizing the Spatial Kernel of Multi Resolution Hash Encodings"
authors: ["Tianxiang Dai", "Jonathan Fan"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "q05hC1Pzkr"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f62817e0e74a1bccd35eee9b9d5c5fc720fef354.pdf"
published: "2026"
categories: []
keywords: ["multi-resolution hash encoding", "implicit neural representations", "neural fields", "point spread function", "spatial kernel analysis", "anisotropy", "resolution limit", "FWHM", "hash collisions", "signal-to-noise ratio", "NeRF"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:14+09:00"
---

# Characterizing and Optimizing the Spatial Kernel of Multi Resolution Hash Encodings

## Abstract
Multi-Resolution Hash Encoding (MHE), the foundational technique behind Instant Neural Graphics Primitives, provides a powerful parameterization for neural fields. However, its spatial behavior lacks rigorous understanding from a physical systems perspective, leading to reliance on heuristics for hyperparameter selection. This work introduces a novel analytical approach that characterizes MHE by examining its Point Spread Function (PSF), which is analogous to the Green's function of the system. This methodology enables a quantification of the encoding's spatial resolution and fidelity. We derive a closed-form approximation for the collision-free PSF, uncovering inherent grid-induced anisotropy and a logarithmic spatial profile. We establish that the idealized spatial bandwidth, specifically the Full Width at Half Maximum (FWHM), is determined by the average resolution, $N_{\text{avg}}$. This leads to a counterintuitive finding: the effective resolution of the model is governed by the broadened empirical FWHM (and therefore $N_{\text{avg}}$), rather than the finest resolution $N_{\max}$, a broadening effect we demonstrate arises from optimization dynamics. Furthermore, we analyze the impact of finite hash capacity, demonstrating how collisions introduce speckle noise and degrade the Signal-to-Noise Ratio (SNR). Leveraging these theoretical insights, we propose Rotated MHE (R-MHE), an architecture that applies distinct rotations to the input coordinates at each resolution level. R-MHE mitigates anisotropy while maintaining the efficiency and parameter count of the original MHE. This study establishes a methodology based on physical principles that moves beyond heuristics to characterize and optimize MHE.

## Metadata
- venue: ICLR
- year: 2026
- authors: Tianxiang Dai, Jonathan Fan
- arxiv_id: 
- openreview_id: q05hC1Pzkr
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f62817e0e74a1bccd35eee9b9d5c5fc720fef354.pdf
- published: 2026
- keywords: multi-resolution hash encoding, implicit neural representations, neural fields, point spread function, spatial kernel analysis, anisotropy, resolution limit, FWHM, hash collisions, signal-to-noise ratio, NeRF
