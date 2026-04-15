---
title: "Deciphering the Extremes: A Novel Approach for Pathological Long-tailed Recognition in Scientific Discovery"
authors: ["Zhe Zhao", "HaiBin Wen", "Xianfu Liu", "Rui Mao", "Pengkun Wang", "Liheng Yu", "Linjiang Chen", "Bo An", "Qingfu Zhang", "Yang Wang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "E16vULI6AF"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/30f7d83b3452994b583222d8187fc0b243850349.pdf"
published: "2025"
categories: []
keywords: ["Long-tailed learning", "Imbalanced datasets"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:32+09:00"
---

# Deciphering the Extremes: A Novel Approach for Pathological Long-tailed Recognition in Scientific Discovery

## Abstract
Scientific discovery across diverse fields increasingly grapples with datasets exhibiting pathological long-tailed distributions: a few common phenomena overshadow a multitude of rare yet scientifically critical instances. Unlike standard benchmarks, these scientific datasets often feature extreme imbalance coupled with a modest number of classes and limited overall sample volume, rendering existing long-tailed recognition (LTR) techniques ineffective. Such methods, biased by majority classes or prone to overfitting on scarce tail data, frequently fail to identify the very instances—novel materials, rare disease biomarkers, faint astronomical signals—that drive scientific breakthroughs. This paper introduces a novel, end-to-end framework explicitly designed to address pathological long-tailed recognition in scientific contexts. Our approach synergizes a Balanced Supervised Contrastive Learning (B-SCL) mechanism, which enhances the representation of tail classes by dynamically re-weighting their contributions, with a Smooth Objective Regularization (SOR) strategy that manages the inherent tension between tail-class focus and overall classification performance. We introduce and analyze the real-world ZincFluor chemical dataset ($\mathcal{T}=137.54$) and synthetic benchmarks with controllable extreme imbalances (CIFAR-LT variants). Extensive evaluations demonstrate our method's superior ability to decipher these extremes. Notably, on ZincFluor, our approach achieves a Tail Top-2 accuracy of $66.84\%$, significantly outperforming existing techniques. On CIFAR-10-LT with an imbalance ratio of $1000$ ($\mathcal{T}=100$), our method achieves a tail-class accuracy of $38.99\%$, substantially leading the next best. These results underscore our framework's potential to unlock novel insights from complex, imbalanced scientific datasets, thereby accelerating discovery.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Zhe Zhao, HaiBin Wen, Xianfu Liu, Rui Mao, Pengkun Wang, Liheng Yu, Linjiang Chen, Bo An, Qingfu Zhang, Yang Wang
- arxiv_id: 
- openreview_id: E16vULI6AF
- anthology_id: 
- pdf_url: https://openreview.net/pdf/30f7d83b3452994b583222d8187fc0b243850349.pdf
- published: 2025
- keywords: Long-tailed learning, Imbalanced datasets
