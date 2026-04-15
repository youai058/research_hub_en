---
title: "Efficient Prediction of Large Protein Complexes via Subunit-Guided Hierarchical Refinement"
authors: ["Chixiang Lu", "Yunhua Zhong", "Shikang Liang", "Xiaojuan Qi", "Haibo Jiang"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "0G8Cq9z2Hp"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1c7bd6e4ca49ab3ad24be6b9acb834dc21a034b4.pdf"
published: "2026"
categories: []
keywords: ["Protein complex structure prediction", "AlphaFold3", "complex modularity"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:31+09:00"
---

# Efficient Prediction of Large Protein Complexes via Subunit-Guided Hierarchical Refinement

## Abstract
State-of-the-art protein structure predictors have revolutionized structural biology, yet quadratic memory growth with token length makes end-to-end inference impractical for large complexes beyond a few thousand tokens. We introduce HierAFold, a hierarchical pipeline that exploits the modularity of large complexes via PAE-guided (Predicted Aligned Error) subunit decomposition, targeted interface-aware refinement, and confidence-weighted assembly. PAE maps localize rigid intra-chain segments and sparse inter-chain interfaces, enabling joint refinement of likely interacting subunits to capture multi-body cooperativity without increasing memory. HierAFold matches AlphaFold3 accuracy, raises success rates from 49.9\% (CombFold) to 73.1\% on recent PDB set. While for large complexes, it cuts peak memory by $\sim$25\,GB on a 4,000-token target ($\sim$40\%), successfully models complexes with over $5{,}000$ tokens that are out-of-memory for AlphaFold3, and raises success rates by two-fold compared with CombFold.

## Metadata
- venue: ICLR
- year: 2026
- authors: Chixiang Lu, Yunhua Zhong, Shikang Liang, Xiaojuan Qi, Haibo Jiang
- arxiv_id: 
- openreview_id: 0G8Cq9z2Hp
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1c7bd6e4ca49ab3ad24be6b9acb834dc21a034b4.pdf
- published: 2026
- keywords: Protein complex structure prediction, AlphaFold3, complex modularity
