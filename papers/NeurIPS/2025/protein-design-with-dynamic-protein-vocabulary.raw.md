---
title: "Protein Design with Dynamic Protein Vocabulary"
authors: ["Nuowei Liu", "Jiahao Kuang", "Yanting Liu", "Tao Ji", "Changzhi Sun", "Man Lan", "Yuanbin Wu"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "MpJkAzwUtl"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/80c2b5c41eda8d76419bc7f20cc82d3a85ec7a92.pdf"
published: "2025"
categories: []
keywords: ["function-based protein design"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:00+09:00"
---

# Protein Design with Dynamic Protein Vocabulary

## Abstract
Protein design is a fundamental challenge in biotechnology, aiming to design novel sequences with specific functions within the vast space of possible proteins. Recent advances in deep generative models have enabled function-based protein design from textual descriptions, yet struggle with structural plausibility. Inspired by classical protein design methods that leverage natural protein structures, we explore whether incorporating fragments from natural proteins can enhance foldability in generative models. Our empirical results show that even random incorporation of fragments improves foldability. Building on this insight, we introduce ProDVa, a novel protein design approach that integrates a text encoder for functional descriptions, a protein language model for designing proteins, and a fragment encoder to dynamically retrieve protein fragments based on textual functional descriptions. Experimental results demonstrate that our approach effectively designs protein sequences that are both functionally aligned and structurally plausible. Compared to state-of-the-art models, ProDVa achieves comparable function alignment using less than 0.04% of the training data, while designing significantly more well-folded proteins, with the proportion of proteins having pLDDT above 70 increasing by 7.38% and those with PAE below 10 increasing by 9.62%.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Nuowei Liu, Jiahao Kuang, Yanting Liu, Tao Ji, Changzhi Sun, Man Lan, Yuanbin Wu
- arxiv_id: 
- openreview_id: MpJkAzwUtl
- anthology_id: 
- pdf_url: https://openreview.net/pdf/80c2b5c41eda8d76419bc7f20cc82d3a85ec7a92.pdf
- published: 2025
- keywords: function-based protein design
