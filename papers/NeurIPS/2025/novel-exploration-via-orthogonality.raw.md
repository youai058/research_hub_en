---
title: "Novel Exploration via Orthogonality"
authors: ["Andreas Theophilou", "Özgür Şimşek"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "yJS1eZSNUv"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/abec5fe5deeb22188d5d3dbfeca748fdeaa6404b.pdf"
published: "2025"
categories: []
keywords: ["Laplacian", "Novelty", "Reinforcement Learning", "Exploration", "Eigenvectors", "Spectral Methods"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:22+09:00"
---

# Novel Exploration via Orthogonality

## Abstract
Efficient exploration remains one of the most important open problems in reinforcement learning. Discovering novel states or transitions requires policies that efficiently direct the agent away from the regions of the state space that are already well explored. We introduce Novel Exploration via Orthogonality (NEO), an approach that automatically uncovers not only which regions of the environment are novel but also how to reach them by leveraging Laplacian representations. NEO uses the eigenvectors of a modified graph Laplacian to induce gradient flows from states that are frequently visited (less novel) to states that are seldom visited (more novel). We show that NEO's modified  Laplacian yields eigenvectors whose extreme values align with the most novel regions of the state space. We provide bounds for the eigenvalues of the modified Laplacian; and we show that the smoothest eigenvectors with real eigenvalues below certain thresholds provide guaranteed gradients to novel states for both undirected and directed graphs. In an empirical evaluation in online, incremental settings, NEO outperformed related state-of-the-art approaches, including eigen-options and cover options, in a large collection of undirected and directed environments with varying connectivity structures.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Andreas Theophilou, Özgür Şimşek
- arxiv_id: 
- openreview_id: yJS1eZSNUv
- anthology_id: 
- pdf_url: https://openreview.net/pdf/abec5fe5deeb22188d5d3dbfeca748fdeaa6404b.pdf
- published: 2025
- keywords: Laplacian, Novelty, Reinforcement Learning, Exploration, Eigenvectors, Spectral Methods
