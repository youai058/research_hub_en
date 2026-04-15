---
title: "ResKoopNet: Learning Koopman Representations for Complex Dynamics with Spectral Residuals"
authors: ["Yuanchao Xu", "Kaidi Shao", "Nikos K. Logothetis", "Zhongwei Shen"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Svk7jjhlSu"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/eb1b1fba5921ea6ed395fd165f62e7d37bca659c.pdf"
published: "2025"
categories: []
keywords: ["Koopman operator", "data driven dynamical system", "dictionary learning", "spectral analysis"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:41+09:00"
---

# ResKoopNet: Learning Koopman Representations for Complex Dynamics with Spectral Residuals

## Abstract
Analyzing the long-term behavior of high-dimensional nonlinear dynamical systems remains a significant challenge. While the Koopman operator framework provides a powerful global linearization tool, current methods for approximating its spectral components often face theoretical limitations and depend on predefined dictionaries. Residual Dynamic Mode Decomposition (ResDMD) advanced the field by introducing the \emph{spectral residual} to assess Koopman operator approximation accuracy; however, its approach of only filtering precomputed spectra prevents the discovery of the operator's complete spectral information, a limitation known as the `spectral inclusion' problem. We introduce ResKoopNet (Residual-based Koopman-learning Network), a novel method that directly addresses this by explicitly minimizing the \emph{spectral residual} to compute Koopman eigenpairs. This enables the identification of a more precise and complete Koopman operator spectrum. Using neural networks, our approach provides theoretical guarantees while maintaining computational adaptability. Experiments on a variety of physical and biological systems show that ResKoopNet achieves more accurate spectral approximations than existing methods, particularly for high-dimensional systems and those with continuous spectra, which demonstrates its effectiveness as a tool for analyzing complex dynamical systems.

## Metadata
- venue: ICML
- year: 2025
- authors: Yuanchao Xu, Kaidi Shao, Nikos K. Logothetis, Zhongwei Shen
- arxiv_id: 
- openreview_id: Svk7jjhlSu
- anthology_id: 
- pdf_url: https://openreview.net/pdf/eb1b1fba5921ea6ed395fd165f62e7d37bca659c.pdf
- published: 2025
- keywords: Koopman operator, data driven dynamical system, dictionary learning, spectral analysis
