---
title: "S-Crescendo: A Nested Transformer Weaving Framework for Scalable Nonlinear System in S-Domain Representation"
authors: ["Junlang Huang", "Chen Hao", "Li Luo", "Yong Cai", "Lexin Zhang", "Tianhao Ma", "Yitian Zhang", "Zhong Guan"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Y6tRVadmgo"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c9d27a819f08f4d17e75c5fde70607f0bd8116dd.pdf"
published: "2025"
categories: []
keywords: ["nonlinear systems", "VLSI backend design", "transformer", "transfer function"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:51+09:00"
---

# S-Crescendo: A Nested Transformer Weaving Framework for Scalable Nonlinear System in S-Domain Representation

## Abstract
Simulation of high-order nonlinear system requires extensive computational resources, especially in modern VLSI backend design where bifurcation-induced instability and chaos-like transient behaviors pose challenges. We present S-Crescendo - a nested transformer weaving framework that synergizes S-domain with neural operators for scalable time-domain prediction in high-order nonlinear networks, alleviating the computational bottlenecks of conventional solvers via Newton-Raphson method. By leveraging the partial-fraction decomposition of an n-th order transfer function into first-order modal terms with repeated poles and residues, our method bypasses the conventional Jacobian matrix-based iterations and efficiently reduces computational complexity from cubic $O(n^3)$ to linear $O(n)$.The proposed architecture seamlessly integrates an S-domain encoder with an attention-based correction operator to simultaneously isolate dominant response and adaptively capture higher-order non-linearities. Validated on order-1 to order-10 networks, our method achieves up to 0.99 test-set \(R^2\) accuracy against HSPICE golden waveforms and accelerates simulation by up to 18\(\times\), providing a scalable, physics-aware framework for high-dimensional nonlinear modeling.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Junlang Huang, Chen Hao, Li Luo, Yong Cai, Lexin Zhang, Tianhao Ma, Yitian Zhang, Zhong Guan
- arxiv_id: 
- openreview_id: Y6tRVadmgo
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c9d27a819f08f4d17e75c5fde70607f0bd8116dd.pdf
- published: 2025
- keywords: nonlinear systems, VLSI backend design, transformer, transfer function
