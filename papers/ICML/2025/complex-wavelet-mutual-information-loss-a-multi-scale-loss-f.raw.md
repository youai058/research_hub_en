---
title: "Complex Wavelet Mutual Information Loss: A Multi-Scale Loss Function for Semantic Segmentation"
authors: ["Renhao Lu"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "iwkCnlOa2A"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5e5c50aee4afd4e89e58a2cbd503b69637a30c05.pdf"
published: "2025"
categories: []
keywords: ["Semantic segmentation", "wavelet transform", "steerable pyramid", "mutual information"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:16+09:00"
---

# Complex Wavelet Mutual Information Loss: A Multi-Scale Loss Function for Semantic Segmentation

## Abstract
Recent advancements in deep neural networks have significantly enhanced the performance of semantic segmentation. However, class imbalance and instance imbalance remain persistent challenges, where smaller instances and thin boundaries are often overshadowed by larger structures. To address the multiscale nature of segmented objects, various models have incorporated mechanisms such as spatial attention and feature pyramid networks. Despite these advancements, most loss functions are still primarily pixel-wise, while regional and boundary-focused loss functions often incur high computational costs or are restricted to small-scale regions. To address this limitation, we propose the complex wavelet mutual information (CWMI) loss, a novel loss function that leverages mutual information from subband images decomposed by a complex steerable pyramid. The complex steerable pyramid captures features across multiple orientations and preserves structural similarity across scales. Meanwhile, mutual information is well-suited to capturing high-dimensional directional features and offers greater noise robustness. Extensive experiments on diverse segmentation datasets demonstrate that CWMI loss achieves significant improvements in both pixel-wise accuracy and topological metrics compared to state-of-the-art methods, while introducing minimal computational overhead. Our code is available at https://github.com/lurenhaothu/CWMI

## Metadata
- venue: ICML
- year: 2025
- authors: Renhao Lu
- arxiv_id: 
- openreview_id: iwkCnlOa2A
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5e5c50aee4afd4e89e58a2cbd503b69637a30c05.pdf
- published: 2025
- keywords: Semantic segmentation, wavelet transform, steerable pyramid, mutual information
